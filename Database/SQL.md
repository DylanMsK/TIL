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

2-1. Datatype​      

| Affinity | Type                                                         |
| -------- | ------------------------------------------------------------ |
| INTEGER  | TINYINT(1byte), SMALLINT(2bytes), MEDIUMINT(3bytes), INT(4bytes), <br />BIGINT(8bytes), UNSIGNED BIG INT |
| TEXT     | CHARACTER(20), VARCHAR(255), TEXT                            |
| REAL     | REAL, DOUBLE, FLOAT                                          |
| NUMERIC  | NUMERIC, DEMICAL, DATE, DATETIME                             |
| BLOB     | no datatype specified                                        |

2-2. Table 및 schema 조회

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

#### 3. 데이터 추가, 읽기, 수정, 삭제