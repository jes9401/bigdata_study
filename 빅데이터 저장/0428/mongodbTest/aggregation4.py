# group, match, sort, sum 명령어

import pymongo

username = 'admin'
password = 'admin'

connection = pymongo.MongoClient('mongodb://%s:%s@localhost:27017/' % (username, password))
db = connection.test_db

# select count(*) as count from zip을 mongodb로
result = db.zip.aggregate([
    {'$group': {
        # 전체 doc에 대한 계산이 필요하면 id 값을 null로
        '_id': 'null',
        'count:': {'$sum': 1}
    }}
])
for i in result:
    print(i)
print()

# select sum(pop) as total from zip 변경
result = db.zip.aggregate([
    {'$group':
        {
            '_id': 'null',
            'total': {'$sum':'$pop'}
        }
    }
])
for i in result:
    print(i)
print()

# select state, sum(pop) from zip group by sate
result = db.zip.aggregate([
    {'$group': {
        '_id': '$state',
        'total_pop': {'$sum': '$pop'}
    }}
])
for i in result:
    print(i)
print()

# select city, sum(pop) from zip group by city
result = db.zip.aggregate([
    {'$group': {
        '_id': '$city',
        'total_pop': {'$sum': '$pop'}
    }},
    {'$limit': 5}
])
for i in result:
    print(i)
print()

# select state, sum(pop) from zip group by state order by sum(pop)
result = db.zip.aggregate([
    {'$group':
        {
            '_id': '$state',
            'total_pop': {'$sum': '$pop'}
        }
    },
    # 1, -1 있음
    {'$sort': {'total_pop': 1}
    },
    {'$limit': 5},
    # id 제외
    {'$project': {'_id':0}}
])
for i in result:
    print(i)
print()

# select * from zip where pop>=100000
result = db.zip.aggregate([
    {'$match': {'pop':{'$gte':100000}}},
    {'$limit':10}
])
for i in result:
    print(i)
print()

# select * from zip where stat='MA'
result = db.zip.aggregate([
    {'$match': {'state': 'MA'}},
    {'$limit': 10}
])
for i in result:
    print(i)
print()

# state로 그룹핑하고 state가 MA인 pop의 합계 출력
result = db.zip.aggregate([
    {'$match': {'state': 'MA'}},
    {'$group':
         {
            '_id': '$state',
            'pop_count': {'$sum': '$pop'}
         }
     }

])
for i in result:
    print(i)
