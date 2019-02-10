# SQL

## SQL개념

**SQL(Structured Query Language)는** 관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위해 설계된 **특수 목적의 프로그래밍 언어** 이다. 관계형 데이터베이스 관리 시스템에서 자료의 검색과 관리, 데이터베이스 스키마 생성과 수정을 데이터베이스 객체 접근 조정 관리를 위해 고안됨			--출처: 위키피디아--

#### SQL 구분

1.  **DDL - 데이터 정의 언어(Data Definition Language)**
   - 개념
     - 데이터를 정의하기 위한 언어
     - 관게형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
   - 예시:  CREATE, DROP, ALTER, ...
2. **DML - 데이터 조작 언어(Data Manipulation Language)**
   - 개념
     - 데이터를 저장, 수정, 삭제, 조회 하기 위한 언어
   - 예시: INSERT, UPDATE, DELETE, SELECT, ...
3. **DCL - 데이터 제어 언어(Data Control Language)**
   - 개념
     - 데이터베이스 사용자의 권한 제어를 위해 사용되는 언어
   - 예시: GRANT, REVOKE, COMMIT, ROLLBACK, ...





## 기본 용어 정리
#### 1. 스키마(Schema)
- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

- 데이터베이스의 구조와 제약 조건에 관련한 전반적인 명세를 기술한 것

  | Column | Datatype |
  | ------ | -------- |
  | id     | INT      |
  | age    | INT      |
  | phone  | TEXT     |
  | email  | TEXT     |
#### 2. 열(Column)
- 각 열에는 고유한 데이터 형식이 지정된다
    (INTEGER TEXT NULL 등)
#### 3. 레코드, 행(row)
- 테이블의 데이터는 행에 저장

#### 4. 기본키(PK)

- 각 레코드(행)의 고유값으로 Primary Key로 불린다
- 반드시 설정되어야 하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용된다





## Hello, DB!

###### examples

| id   | first_name | last_name | age  | country | phone         |
| ---- | ---------- | --------- | ---- | ------- | ------------- |
| 1    | 민수       | 강        | 28   | 서울    | 010-1234-5678 |

#### 1. Hello, World! Hello, SQL!

```bash
sqlite> SELECT * FROM examples;
1, "민수", "강", "28", "서울", "010-1234-5678"
```

SELECT문은 데이터베이스에서 특정한 테이블을 반환한다

```bash
sqlite> .headers on
sqlite> .mode column
sqlite> SELECT * FROM examples;
id		first_name		last_name		age		country		phone
----------	----------	----------	----------	----------	----------
1			민수			강			28			서울			010-1234-5678
```

#### 2. DB, Table 생성

1. Database 생성

```bash
$ sqlite3 tutorial.sqlite3
sqlite> 
```

2. Table 생성

```bash
sqlite> CREATE TABLE classmates (
            id INT PRIMARY KEY,
            name TEXT
        );
```

​	2-1. Datatype      

| Affinity | Type                                                         |
| -------- | ------------------------------------------------------------ |
| INTEGER  | TINYINT(1byte), SMALLINT(2bytes), MEDIUMINT(3bytes), INT(4bytes), <br />BIGINT(8bytes), UNSIGNED BIG INT |
| TEXT     | CHARACTER(20), VARCHAR(255), TEXT                            |
| REAL     | REAL, DOUBLE, FLOAT                                          |
| NUMERIC  | NUMERIC, DEMICAL, DATE, DATETIME                             |
| BLOB     | no datatype specified                                        |

​	2-2. Table 및 schema 조회

```bash
sqlite> .tables
classmates
sqlite> .schema classmates
```

3. Table 삭제(DROP)

```bash
sqlite> DROP TABLE classmates;
sqlite> .tables
```

- **Quiz. 다음과 같은 스키마를 가지고 있는 classmate 테이블을 만들어보세요.**

  | Column  | Datatype |
  | ------- | -------- |
  | id      | INT      |
  | name    | TEXT     |
  | age     | INT      |
  | address | TEXT     |

  ```bash
  sqlite> CREATE TABLE classmates (
  id INT PRIMARY KEY,
  name TEXT,
  age INT,
  address TEXT);
  ```

#### 3. 데이터 추가, 읽기, 수정, 삭제

1. data 추가(INSERT)

   ```sql
   INSERT INTO table (column1, column2, ..) 
   VALUES (value1, value2, ..)
   ```

   ```bash
   sqlite> INSERT INTO classmates (name, age)
   		VALUES ('강민수', 28);
   ```

   **QUIZ. classmates 테이블에  id가 2이고, 이름이 홍길동이고, 나이가 30이고, 주소가 서울인 데이터를 넣어봅시다.**

   ```bash
   sqlite> INSERT INTO classmates VALUES (2, '홍길동', 30, '서울');
   ```

   - **모든 데이터를 넣을때는 column을 명시할 필요가 없다!**

   1-1. NULL값은 최소화

   ```bash
   sqlite> DROP TABLE classmates;
   sqlite> CREATE TABLE classmates (
   id INTEGERT PRIMARY KEY AUTOINCREMENT,	# AUTOINCREMENT는 INTETGER일때만 가능
   name TEXT NOT NULL,
   age INT NOT NULL,
   address TEXT NOT NULL);
   sqlite> INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
   ErrorL NOT NULL constraint failed: classmates.address
   sqlite> INSERT INTO classmates VALUES (1, '홍길동', 50, '서울');
   Error: UNIQUE constraint failed: classmates.id
   ```

2. data 가져오기(SELECT)

   ```sql
   SELECT * FROM table
   SELECT column1, column2, .. FROM table
   ```

   2-1. table에서 특정 데이터 몇개만 가져오기

   ```sql
   SELECT column1, column2, .. FROM table LIMIT num
   ```

   2-2 table에서 특정 데이터 위에서 몇개만 가져오기

   ```sql
   SELECT column1, column2, .. FROM table LIMIT num OFFSET num
   ```

   **QUIZ. classmates에서 id, name column 값 중 세번째에 있는 값 하나만 가져오기**

   ```bash
   sqlite> SELECT id, name FRIM classmates LIMIT 1 OFFSET 2;
   ```

   2-3 table에서 특정한 값만 가져오기

   ```sql
   SELECT column1, column2, .. FROM table WHERE column=value
   ```

3. data 삭제(DELETE)

   ```sql
   DELETE FROM table WHERE condition
   ```

   - **일반적으로 데이터 중복이 불가능한 id값을 기준으로 삭제함!**

4. data 수정(UPDATE)

   ```sql
   UPDATE table
   SET column1=value1, column2=value2, ..
   WHERE condition
   ```

   QUIZ. classmates 테이블에 id가 4인 레코드를 수정해봅시다.

   ​		이름을 홍길동으로, 주소를 제주도로

   ```bash
   sqlite> UPDATE classmates SET name='홍길동', address="제주도" WHERE id=4;
   ```

   