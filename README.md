
## Excel Data Upload and Bulk Insert

This project allows users to upload Excel files containing asset data, validate the contents, and bulk insert the data into a Django-based database. It handles missing values, parses date fields, and stores data in appropriate models based on the selected group. Efficient error handling ensures smooth operation even with incomplete or invalid data, skipping erroneous rows.

## Key Features:
Upload and process Excel files
Validate and fill missing data
Parse dates correctly
Bulk insert data into Django models
Dynamic group model assignment
Error logging and handling
Requirements:
Django
pandas
Usage:
## Upload an Excel file through the form, and the data will be validated and stored in the corresponding database model.


## Install virtualenv inside vmspm directory
$ pip install virtualenv

## Create virtualenv inside this folder
$ python -m venv env 

## Then Activate the virtualenv
##### $ .\env\Scripts\activate   -----> for Window
##### $  source env/bin/activate  ----> for Linux

## Install django and restframework 
(env) $ pip install django , (env)  $ pip install djangorestframework

## Create django project 
(env)  $ django-admin startproject project_name

## Change diectory to project_name
(env)  $ cd project_name

## MySQL database used so install mysqlclient
(env) $ project_name> pip install mysqlclient

## Then create migration file
(env) $ project_name> python manage.py makemigrations

## Then create tables in database
(env) $ project_name> python manage.py migrate

## Then create superuser
(env) $ project_name> python manage.py createsuperuser

## Runserver
(env) $ project_name> python manage.py runserver
