 # -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 21:03:36 2021

@author: charlie
"""
from jumpy import codebase
import numpy as np
import os
import pathlib
from matplotlib import pyplot as plt


def calc_dis(a, b):
  return((((a[0]-b[0])**2)+((a[1]-b[1])**2))**0.5)
  
def calc_triangle_area(counter, list_n):
  y1=max(list_n)
  x1=list_n.index(y1)
  len_=len(list_n)-1
  a=calc_dis([y1, x1], [list_n[0], 0])#((y1-list_n[0])**2+(x1-0)**2)**0.5
  b=calc_dis([y1, list_n[len_]], [list_n[0], len_])#((y1-list_n[len_])**2+(x1-len_)**2)**0.5
  c=calc_dis([list_n[0], list_n[len_]], [0, len_])#((list_n[0]-list_n[len_])**2+(0-len_)**2)**0.5
  s=(a+b+c)
  area=(s*(s-a)*(s-b)*(s-c))**0.5
  return area 


# Specify your video name and target pose class to count the repetitions.
# Open the video.
import cv2

def Counting(video_path):
    list_area=[]
    input_path = './Video/'+video_path
    video_cap = cv2.VideoCapture(input_path)

    # Get some video parameters to generate output video with classificaiton.
    video_n_frames = video_cap.get(cv2.CAP_PROP_FRAME_COUNT)
    video_fps = video_cap.get(cv2.CAP_PROP_FPS)
    video_width = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Initilize tracker, classifier and counter.
    # Do that before every video as all of them have state.
    from mediapipe.python.solutions import pose as mp_pose


    # Initialize tracker.
    pose_tracker = mp_pose.Pose(upper_body_only=False)

    print("A-------------------A")
    print(pathlib.Path().absolute())
    print("A-------------------A")
    pose_samples_folder = './jumpy/Jump_csvs_out'
    pose_embedder = codebase.FullBodyPoseEmbedder()

    pose_classifier = codebase.PoseClassifier(
        pose_samples_folder=pose_samples_folder,
        pose_embedder=pose_embedder,
        top_n_by_max_distance=30,
        top_n_by_mean_distance=10)


    # Run classification on a video.
    import os
    import tqdm
    from sklearn import preprocessing
    from mediapipe.python.solutions import drawing_utils as mp_drawing
    import matplotlib.pyplot as plt
    import statistics
    import talib                        #EMA
    # Open output video. // 07360541/Videoname
    out_video = cv2.VideoWriter('./Video_out/'+video_path, cv2.VideoWriter_fourcc(*'mp4v'), video_fps, (video_width, video_height))

    frame_idx = 0
    output_frame = None
    n=count=flag=0
    n_repeats=[]
    list_n=np.array([])
    with tqdm.tqdm(total=video_n_frames, position=0, leave=True) as pbar:
      while True:
        # 將影片切割成圖片處理
        success, input_frame = video_cap.read()
        if not success:
          break
          
        # 呼叫姿勢追蹤API
        input_frame = cv2.cvtColor(input_frame, cv2.COLOR_BGR2RGB)
        result = pose_tracker.process(image=input_frame)
        pose_landmarks = result.pose_landmarks

        # 將關節畫在圖片上面
        output_frame = input_frame.copy()
        if pose_landmarks is not None:
          mp_drawing.draw_landmarks(
              image=output_frame,
              landmark_list=pose_landmarks,
              connections=mp_pose.POSE_CONNECTIONS)
        
        if pose_landmarks is not None:
          # 取得關節座標
          frame_height, frame_width = output_frame.shape[0], output_frame.shape[1]
          pose_landmarks = np.array([[lmk.x * frame_width, lmk.y * frame_height, lmk.z * frame_width]
                                     for lmk in pose_landmarks.landmark], dtype=np.float32)
          assert pose_landmarks.shape == (33, 3), 'Unexpected landmarks shape: {}'.format(pose_landmarks.shape)
        else:
          continue

        nk=video_height-((pose_landmarks[23][1]+pose_landmarks[24][1])/2)
        pose_classification = pose_classifier(pose_landmarks)
        
        #n=上次的Y座標、nk=目前的Y座標
        if(frame_idx==0):
          n=nk
          
        
        if(pose_classification.get('jump', 0)<5): 
          flag=0
          n_repeats.clear()
          
        else:  
          list_n=np.append(list_n, nk)
          if(len(list_n)>=4):#每次刪除list_n第一個元素，做EMA
            ema=talib.EMA(list_n, 4)
            list_n=np.delete(list_n, 0)
            nk=ema[3]
          if(n<=nk):#判斷正在上升
            if(flag==1):#跳繩狀態轉換
              if(len(n_repeats)>=4):
                area=calc_triangle_area(count, n_repeats)
                list_area.append(area)
                count+=1
                n_repeats.clear()
              flag=0
          else:
            flag=1
          n_repeats.append(nk)
          n=nk
        # 畫圖且輸出圖片
        cv2.putText(output_frame, 'pose=' +str(pose_classification), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(output_frame, 'frame=' +str(frame_idx), (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(output_frame, 'count=' +str(count), (10, 160), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
        out_video.write(cv2.cvtColor(np.array(output_frame), cv2.COLOR_RGB2BGR))
      

        frame_idx += 1
        pbar.update()
    list_area_NotSort=list_area.copy()
    np_array=np.array(list_area)

    #if z_score < -1.645
    #標準常態分布的機率值小於5%
    #將其判斷為異常值扣除
    z_score=preprocessing.scale(np_array, axis=0, with_mean=True, with_std=True, copy=True)
    error=[i for i in z_score if i<-1.645]
    print(len(error))


     
    print("=================================")
    print("video counted")
    print("=================================")    
    # Close output video.
    out_video.release()

    # Release MediaPipe resources.
    pose_tracker.close()
    return (count-len(error))