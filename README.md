# flask를 이용한 REST API서버  
## 필요 패키지  
DB : PostgreSQL  
reference link - https://github.com/snowplow/snowplow/wiki/Setting-up-PostgreSQL
### 윈도우
```
https://www.postgresql.org/download/
다 next해서 설치
```
### 리눅스
```
$ sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs
user : postgres
pw : root
database name : test
port : 5432
```
  
## 필요한 모듈 설치  
### 윈도우
```
pip install -r requirments.txt  
```
### 리눅스  
```
pip3 install -r requirments-linux.txt  
```

## 개발서버 실행방법
### 윈도우
```
set MODE=DEV
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py runserver
```
### 리눅스
```
export MODE=DEV
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
python3 manage.py runserver
```

