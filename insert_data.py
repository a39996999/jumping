import pymongo
import pandas as pd
import numpy as np
import random
items  = ['A', 'B', 'C']
grades = ['1', '2', '3', '4', '5', '6', '7', '8']
groups = ['1', '2', '3']

file_name='110跳繩比賽v04_個人_成績登錄_0430_1355.xlsx'



#myclient=pymongo.MongoClient('mongodb://192.168.50.10:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false')
myclient=pymongo.MongoClient('mongodb://192.168.50.93:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false')
mydb = myclient['djongo_test']
mycol=mydb['catalog_student']

list_ = []
mycol.delete_many({})
list_.append({"school":str('文澳國小'),"std_No":str('A1185'), "item":str(0), "grade":str(0), "group":str(0),"coach":str(0),"name":str('劉睿哲'), "score":0})
list_.append({"school":str('文澳國小'),"std_No":str('A1186'), "item":str(0), "grade":str(0), "group":str(0),"coach":str(0),"name":str('張睿桓'), "score":0})
list_.append({"school":str('文澳國小'),"std_No":str('A1187'), "item":str(0), "grade":str(0), "group":str(0),"coach":str(0),"name":str('洪紹恆'), "score":0})
list_.append({"school":str('文澳國小'),"std_No":str('A1188'), "item":str(0), "grade":str(0), "group":str(0),"coach":str(0),"name":str('莊博勛'), "score":0})
list_.append({"school":str('文澳國小'),"std_No":str('A1189'), "item":str(0), "grade":str(0), "group":str(0),"coach":str(0),"name":str('葉明展'), "score":0})
list_.append({"school":str('文澳國小'),"std_No":str('A1190'), "item":str(0), "grade":str(0), "group":str(0),"coach":str(0),"name":str('高子龍'), "score":0})
list_.append({"school":str('文澳國小'),"std_No":str('A1191'), "item":str(0), "grade":str(0), "group":str(0),"coach":str(0),"name":str('黃群軒'), "score":0})
list_.append({"school":str('文澳國小'),"std_No":str('A1192'), "item":str(0), "grade":str(0), "group":str(0),"coach":str(0),"name":str('黃翌宸'), "score":0})

x=mycol.insert_many(list_)   
'''
for i in range(1, 500, 1):
    list_.append({"school":str(i),"std_No":str(i), "item":str(i), "grade":str(i), "group":str(i),"coach":str(i),"name":str(i), "score":0})
    #print(list_[i])


x=mycol.insert_many(list_)
'''

