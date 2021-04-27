# 0426

### 04/26

- NoSQL

    ![0426%20568113e2562b4a98a6199d71418a9914/Untitled.png](0426%20568113e2562b4a98a6199d71418a9914/Untitled.png)

- CRUD

    ![0426%20568113e2562b4a98a6199d71418a9914/Untitled%201.png](0426%20568113e2562b4a98a6199d71418a9914/Untitled%201.png)

- MongoDB 설치

    ![0426%20568113e2562b4a98a6199d71418a9914/Untitled%202.png](0426%20568113e2562b4a98a6199d71418a9914/Untitled%202.png)

    - C:/ 하위에 설치
    - cd C:\MongoDB\Server\4.4\bin
    - 실행 : mongod.exe —dbpath c:\mongoDB

- CRUD 실습

    ```sql
    for(i=1;i<101;i++){
    	db.users.save({name:"nm"+i,score:99+i});
    }

    ```

    - db.users.save() ⇒ users라는 collection에 값 추가
    - db.users.find() ⇒ 조회
    - ex) db.users.find().toArray() ⇒ 갯수 많아도 다 출력
    - db.users.find({score:{"$gte":150,"$lte":160}})
        - 점수가 150이상 160이하(e는 =)
    - db.users.update({name:'nm1'},{name:'haha'}) ⇒ 수정
    - db.users.update({name:"haha"},{"$push":{language:'js'}}) ⇒ push(수정, 추가)
        - 여러개 업데이트 하려면 multi:true
    - db.users.remove() ⇒ 삭제
    - db.users.remove({}) ⇒전부 삭제
    - db.users.getIndexes()
    - db.users.ensureIndex({name:1})
    - db.users.dropIndex({name:1})
    - mongoimport -d test -c emp --file "C:\MongoDB\mongoimport.json" --legacy
        - json파일 mongodb에 넣기