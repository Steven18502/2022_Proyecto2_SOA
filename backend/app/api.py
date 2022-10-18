#!/usr/bin/env python
# encoding: utf-8
from flask import Flask,render_template, request, jsonify
from flask_mysqldb import MySQL
import os
import json

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'emotions_db'

# mysql = MySQL(app)

class Person():
    
    def __init__(self, name, emotion, date):
        self.name = name
        self.emotion = emotion
        self.date = date
        
    def to_json(self):
        return {
            "name": self.name,
            "emotion": self.email,
            "date": self.date
            }
        
@app.route('/', methods=['GET'])
def get_records():
    # print("get records")
    # user = User.objects(name='name').first()
    # if not user:

    #Creating a connection cursor
    # cursor = mysql.connection.cursor()
    
    #Executing SQL Statements
    # query_string = "SELECT * FROM emotions_analysis"
    # cursor.execute(query_string)
    
    # Saving results
    # result = cursor.fetchall()
    
    # cursor.close()
    result = '[{"name": "Arthur", "emotion": "angry", "date": "17/10/2022 07:04 PM"}, {"name": "Cassandra", "emotion": "sad", "date": "17/10/2022 07:04 PM"}, {"name": "Evelyn", "emotion": "undetermined", "date": "17/10/2022 07:04 PM"}]'
    if not result:
        return jsonify({'error': 'no data'})
    return jsonify(result)
    
def create_record(data):
    
    # Parse string to JSON object
    data = json.loads(data)
    
    #Creating a connection cursor
    # cursor = mysql.connection.cursor()
    
    # Add information to the table
    print("Adding Data")
    for person in data:
        print()
        print(person['name'])
        print(person['emotion'])
        print(person['date'])

        #Executing SQL Statements
        # query_string = "INSERT INTO emotions_analysis VALUES(%s,%s,%s)"
        # cursor.execute(query_string,(name,emotion,date))\
        
    #Saving the Actions performed on the DB
    # mysql.connection.commit()
    # cursor.close()

def run():
    app.run(host='localhost', port=5000)