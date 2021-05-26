import time
import os
import csv
import pymongo
from config import Config

client = pymongo.MongoClient('localhost', 27017)

db = client['test']
collection = db['test']
posts = collection.posts

t = time.time()

with open(os.path.join('../../Downloads/untitled2/data', 'result.csv'), 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, dialect='excel')
    csv_writer.writerow(Config.ANSWER_COLUMNS)
    for year in ['2019', '2020']:
        res = collection.find_one({'physTestStatus': 'Зараховано', 'year': year}, sort=[('physBall100', -1)])
        csv_writer.writerow([year, res['physBall100'], res['physBall12'], res['physBall']])

print(t)