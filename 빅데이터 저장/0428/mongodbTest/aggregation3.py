# project,limit 명령어

import pymongo

username = 'admin'
password = 'admin'

connection = pymongo.MongoClient('mongodb://%s:%s@localhost:27017/' % (username, password))
db = connection.test_db

# 기본
result = db.zip.find(limit=5)
for i in result:
    print(i)

print()

# id, city만 출력하기
result = db.zip.aggregate([
    {'$project': {'_id': 1, 'city': 1}},
    {'$limit': 5}
])
for i in result:
    print(i)
print()

# state, pop만 출력하기, id는 default 값이 1인듯?
result = db.zip.aggregate([
    {'$project': {'state': 1, 'pop': 1, '_id': 0}},
    {'$limit': 3}
])
for i in result:
    print(i)
print()

# 전체 출력하려면 $project 안쓰면 됨
result = db.zip.aggregate([
    {'$limit':5}
])
for i in result:
    print(i)