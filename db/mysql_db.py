import mysql.connector

mydb = mysql.connector.connect(
  database='mydb',
  host="localhost",
  port=27017,
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS EMPLEADO_EMOTIONS(id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key', create_time DATETIME COMMENT 'Create Time', name VARCHAR(255), emotion VARCHAR(255));")