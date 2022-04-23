import pymongo
import pandas as pd
import numpy as np
import os 
import shutil
import xlrd
from xlutils.copy import copy
import openpyxl
from win32com.client import Dispatch
items  = ['A']
grades = ['1', '2']
groups = ['1', '2', '3']

file_name='110跳繩比賽v04_個人_成績登錄_0430_1355.xlsx'
export_file_name='110跳繩比賽v04_個人_成績登錄_0430_1355_未排序.xlsx'
#export_file_name2='110跳繩比賽v04_個人_成績登錄_0430_1355_未排序2.xlsx'
myclient=pymongo.MongoClient('mongodb://192.168.88.12:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
mydb = myclient['djongo_test']
mycol=mydb['catalog_student']

#def export_csv_nsort():

if (os.path.isfile(file_name)):
    shutil.copyfile(file_name, export_file_name)        

#writer = pd.ExcelWriter(export_file_name, engine='openpyxl')

def just_open(filename=file_name):
    xlApp = Dispatch("Excel.Application")
    xlApp.Visible = False
    xlBook = xlApp.Workbooks.Open(filename)
    xlBook.Save()
    xlBook.Close()

for item in items:
    for grade in grades:
        for group in groups:
            try:
                #table=export_file.sheet_by_name(sheet_name)
                df = pd.read_excel(export_file_name, sheet_name=item+grade+group)
                print(df)
                for i in range(0, df.shape[0]):
                    if df['姓名'][i] is not np.nan:
                        df['成績'][i] = 1
                        print(df['成績'][i])
                

                '''
                for i in range(0, df.shape[0]):
                    if df['姓名'][i] is not np.nan:
                        people = mycol.find({}, {"std_No":})
                        #print(list_[i])
                '''
                #df.to_excel(writer, sheet_name=item+grade+group)
                #writer.save()
             
                with pd.ExcelWriter(export_file_name, engine='openpyxl', mode = 'r+', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name=item+grade+group)
                    #writer.save()
                    just_open(export_file_name)
            except Exception as e:
               print(item+grade+group, "ERROR!!")
               print(e)
               continue
