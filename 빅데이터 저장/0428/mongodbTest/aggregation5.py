# group, match, sort, sum 실습

import pymongo

username = 'admin'
password = 'admin'

connection = pymongo.MongoClient('mongodb://%s:%s@localhost:27017/' % (username, password))
db = connection.test_db

# select state, sum(pop) from zip group by state having sum(pop)>10000000
result = db.zip.aggregate([
    {'$group':
        { # state로 그룹핑
            '_id': '$state',
            'total_pop': {'$sum': '$pop'}
        }
    },
    # total_pop이 10~ 보다 큰 경우
    {'$match': {'total_pop': {'$gte': 10000000}}},
    # 역정렬
    {'$sort': {'total_pop': -1}},
    # 5개만
    {'$limit': 5},
    # id 제외
    {'$project': {'_id': 0}}
])
for i in result:
    print(i)
print()


# 1000만 이상의 state 의 총 인구를 state_pop 필드명으로 출력하고 _id는 출력하지 않으며,
# 가장 많은 인구를 가진 3개만 출력하기

result = db.zip.aggregate([
    {'$group':
        {
            '_id': '$state',
            'state_pop': {'$sum': '$pop'}
        }
    },
    {'$match': {'state_pop': {'$gte': 10000000}}},
    {'$sort': {'state_pop': -1}},
    {'$limit': 3},
    {'$project': {'_id': 0}},
])
for i in result:
    print(i)

