import pymongo
import pandas as pd
import numpy as np
import random
items  = ['A', 'B', 'C']
grades = ['1', '2', '3', '4', '5', '6', '7', '8']
groups = ['1', '2', '3']

file_name='110跳繩比賽v04_個人_成績登錄_0430_1355.xlsx'



myclient=pymongo.MongoClient('mongodb://192.168.50.10:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false')
mydb = myclient['djongo_test']
mycol=mydb['catalog_student']

list_ = []
mycol.delete_many({})
for i in range(1, 500, 1):
    list_.append({"school":str(i),"std_No":str(i), "item":str(i), "grade":str(i), "group":str(i),"coach":str(i),"name":str(i), "score":0})
    #print(list_[i])


x=mycol.insert_many(list_)


