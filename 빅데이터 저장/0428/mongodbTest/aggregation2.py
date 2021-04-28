import pymongo
from pprint import pprint

username = 'admin'
password = 'admin'

# connection = pymongo.MongoClient('mongodb://%s:%s@www.funcoding.xyz' % (username, password))
# 연결
connection = pymongo.MongoClient('mongodb://%s:%s@localhost:27017/' % (username, password))
# test_db 연결
db = connection.test_db
# test_db의 collection 목록
print(db.collection_names())
# collection "zip"의 정보
print(db.zip)

result = db.zip.find(limit=10)
for i in result:
    print(i)
print()

result = db.restaurant.find(limit=1)
for i in result:
    print(i)
print()

result = db.restaurant.find(limit=3)
for i in result:
    pprint(i)
print()

