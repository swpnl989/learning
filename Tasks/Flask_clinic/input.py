# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:smt9860@localhost/PracticeDB'
# db = SQLAlchemy(app)

# class User1(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)


# from sqlalchemy import create_engine
# # import psycopg2

# engine = create_engine("postgresql+psycopg2://postgres:smt9860@localhost/PracticeDB")
# engine.connect()

# print(engine)

# PostgreSQL doesn't like capitals or spaces
# # dialect+driver://username:password@host:port/database

import pandas as pd
df = pd.read_csv('file1.csv')
df.columns = [c.lower() for c in df.columns] 

from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:smt9860@localhost/PracticeDB')

df.to_sql("clinic_data", engine)