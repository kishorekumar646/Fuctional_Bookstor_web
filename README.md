# Book Store
This repo includes book store backend. 

# Pre Requisite
  - Python3
  - PostgresQL
  - NodeJS

# Installation
  - if not install virtualenv package ``` $ pip install virtualenv ```
  - ``` $ python -m virtualenv venv ```
  - Activate env ``` $ source venv/bin/acticate ```
  - Create .env file from root folder.
  - Copy the env.sample file to .env and add your db credentials.
  - For install dependencies ``` $ pip install -r requirements.txt ```

# Fix Issues
  - If getting error like `Error: That port is already in use.` use this command ``` lsof -t -i tcp:8000 | xargs kill -9 ```.
 
# How to create database with user

  create database mydb;
  create user myuser;
  GRANT permissions ON DATABASE mydb TO myuser;
  
