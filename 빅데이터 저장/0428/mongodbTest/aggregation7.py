# project에 표현식 활용

# * 산술표현식
#  - $add       [a1 [, a2, a3 ... an]]
#  - $substract [a1, a2]
#  - $multiply  [a1 [, a2, a3 ... an]]
#  - $divide    [a1, a2]
#  - $mod       [a1, a2]

# * 날짜 표현식
#  - $year, $month, $week, $dayOfMonth, $dayOfWeek, $dayOfYear, $hour, $minute, $second

# * 문자열 표현식
#  - $substr
#  - $concat

import pymongo

username = 'admin'
password = 'admin'

connection = pymongo.MongoClient('mongodb://%s:%s@localhost:27017/' % (username, password))
db = connection.test_db

# add

result = db.zip.aggregate([
    {'$group':
        {
            '_id':'$state',
            'max':{'$max':'$pop'},
            'min':{'$min':'$pop'}
        }
    },
    {'$project':
        {
            'maxmin':{'$add':['$max','$min']}
        }
    }
])
for i in result:
    print(i)
print()


# ISODate 날짜 표현식

import datetime
from pprint import pprint

db.test_db.insert_one(
    { 'item' : 'abc', 'price' : 10, 'quantity' : 2, 'date' : datetime.datetime.utcnow() }
)
result = db.test_db.aggregate([
    {'$project' :
        {
            '_id' : 0,
            'year' : { '$year': '$date' },
            'month' : { '$month': '$date' },
            'day' : { '$dayOfMonth': "$date" },
            'hour' : { '$hour': "$date" },
            'minutes' : { '$minute': "$date" },
            'seconds' : { '$second': "$date" },
            'milliseconds' : { '$millisecond': "$date" },
            'dayOfYear' : { '$dayOfYear': "$date" },
            'dayOfWeek' : { '$dayOfWeek': "$date" },
            'week': { '$week': "$date" }
        }
    }
])
for i in result:
    pprint(i)
print(i)


# $project의 $concat operator 활용

db.test_db.insert_one(
    { 'firstname' : 'Dave', 'lastname' : 'Lee' }
)

result = db.test_db.aggregate([
    {'$project' :
        {
            '_id' : 0,
            'all_data' : { '$concat' : ['Full Name: ', '$firstname', ' ', '$lastname' ]}
        }
    }
])
for record in result:
    pprint(record)
print()