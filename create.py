import pymongo
import pandas as pd
import time


t = time.time()

data_2019 = pd.read_csv('data/Odata2019File.csv', sep=';', encoding='cp1251')
data_2020 = pd.read_csv('data/Odata2020File.csv', sep=';', encoding='cp1251')

data_2019['year'] = 2019
data_2020['year'] = 2020

client = pymongo.MongoClient('localhost', 27017)
db = client['test']
collection = db['test']
posts = collection.posts


posts.insert_many(data_2019.to_dict('recodrs'))
posts.insert_many(data_2020.to_dict('records'))

print(t)