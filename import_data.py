import pymongo
import pandas as pd
import numpy as np
import random
items  = ['A', 'B', 'C']
grades = ['1', '2', '3', '4', '5', '6', '7', '8']
groups = ['1', '2', '3']

file_name='111v04__.xlsx'



myclient=pymongo.MongoClient('mongodb://192.168.50.93:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
mydb = myclient['djongo_test']
mycol=mydb['catalog_student']


mycol.delete_many({})
for item in items:
    for grade in grades:
        for group in groups:
            try:
                df = pd.read_excel(file_name, sheet_name=item+grade+group)
                list_ = []

                for i in range(0, df.shape[0]):
                    if df['姓名'][i] is not np.nan:
                        list_.append({"school":df['學校'][i] ,"std_No":df['號碼'][i], "item":df['號碼'][i][0], "grade":df['號碼'][i][1], "group":df['號碼'][i][2],"coach":df['指導\n老師'][i],"name":df['姓名'][i], "score":0})
                        #print(list_[i])

                
                x=mycol.insert_many(list_)
            except:
               #print(item+grade+group, "ERROR!!")
               continue
