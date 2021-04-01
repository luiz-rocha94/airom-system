# airom-system
Python 3.7 application with Django 3.1 webframework and MariaDB 10.5 DataBase

## Install python libs 
pip install -r requirements.txt

## Install and configure MariaDB 10.5
https://mariadb.org/download/
> UTF8 as default\
> user: root\
> password: pass

in MySQL Client MariaDB 10.5
> MariaDB [(none)]> INSTALL SONAME 'ha_connect';

## Create database.
in MySQL Client MariaDB 10.5
> MariaDB [(none)]> CREATE DATABASE 'db_aisys';\
> MariaDB [(none)]> CREATE DATABASE 'db_base'; 

## User and password settings
aisys.aisys.settings
> DATABASES = ...

## Create table.
in terminal
> python manage.py makemigrations database\
> python manage.py sqlmigrate --database=base database 0001\
> python manage.py migrate --database=base database\
> python manage.py migrate 

## Import data to table.
https://www.kaggle.com/andrewmvd/heart-failure-clinical-data

in terminal

> python manage.py shell\
> from database.models import HeartFailure\
> from database.utils import table_import\
> file = r'heart_failure_clinical_records_dataset.csv'\
> table_import(HeartFailure, file)

## MindsDB
user and password settings > mindsdb/config.json\
in terminal

> python -m mindsdb --api=http,mysql --config=config.json

in mindsdb GUI Datasets
> database\
> datasource name: heart_failure\
> database: db_base\
> query: select * from heart_failure

in mindsdb GUI Predictors
> train new\
> from: heart_failure\
> predictor_name: heart_failure_model\
> select death_event to be predicted\
> train

in mindsdb GUI Query
> new query\
> from: heart_failure_model\
> data: ...\
> run query