# 연산과 활용

# * 산술연산
#   - $sum : 각 문서에서 해당 필드의 값을 합함
#   - $avg : 각 문서에서 해당 필드의 평균을 구함
# * 극한연산
#   - $max : 입력값 중 최대값 반환
#   - $min : 입력값 중 최소값 반환
#   - $first : 그룹의 첫번째 값 반환
#   - $last : 그룹의 마지막 값 반환
#   - first, last 연산자의 경우에는 보통 sort 후 사용
# * 배열연산
#   - $addToSet : 해당 값이 없는 경우, 배열에 추가. 순서 보장 하지 않음
#   - $push : 차례대로 배열에 추가

import pymongo

username = 'admin'
password = 'admin'

connection = pymongo.MongoClient('mongodb://%s:%s@localhost:27017/' % (username, password))
db = connection.test_db

# sum
result = db.zip.aggregate([
    {'$group':
        {
            '_id':'$state',
            'total_pop':{'$sum':'$pop'}
        }
    },
    {'$limit':5}
])
for i in result:
    print(i)
print()


# avg
result = db.zip.aggregate([
    {'$group':
        {
            '_id':'null',
            'avg_pop':{'$avg':'$pop'}
        }
    }
])
for i in result:
    print(i)
print()

result = db.zip.aggregate([
    {'$group' : {'_id' : {'state' : '$state', 'city' : '$city'}, 'avg_pop' : {'$avg' : '$pop'}}},
    {'$limit' : 5}
])
for i in result:
    print(i)
print()

result = db.zip.aggregate([
    {'$group' : {'_id' : {'state' : '$state', 'city' : '$city'}, 'avg_pop' : {'$avg' : '$pop'}}},
    {'$match' : {'_id.state' : 'MA'}},
    {'$project' : {'_id' : 0, 'avg_pop':1}},
    {'$limit' : 5}
])
for i in result:
    print(i)


# max, min

result = db.zip.aggregate([
    {'$group':
        {
            '_id':'$state',
            'maximum':{'$max':'$pop'},
            'minimum':{'$min':'$pop'}
        }
    }
])
for i in result:
    print(i)
print()


# first, last

result = db.zip.aggregate([
    {'$group':
        {
            '_id':'$state',
            'first':{'$first':'$pop'},
            'last':{'$last':'$pop'},
        }
    }
])
for i in result:
    print(i)
print()


# push: 전체 값을 하나의 배열로 만들기
result = db.zip.aggregate([
    {'$group':
        {
            '_id':'$state',
            'cityset':{'$push':'$city'}
        }
    },
    {'$match':{'_id':'CA'}}
])
for i in result:
    print(i)
print()

# addToSet: 전체 값을 하나의 배열로 만들기,
# $push와 동일하지만, 중복된 데이터는 추가하지 않음

result = db.zip.aggregate([
    {'$group':
         {
             '_id':'$state',
             'cityset':{'$addToSet':'$city'}
         }
     },
    {'$match':{'_id':'CA'}}
])
for i in result:
    print(i)
print()

