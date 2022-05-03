#!/usr/bin/python3
"""This module initialize mysql database"""
import mysql.connector

def init_database():
    mydb = mysql.connector.connect(
        user= 'root',
        password = 'p@ssw0rd1',
        host = 'mysqldb'
    )
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS appflask")
    cursor.close()
    mydb.close()

    mydb = mysql.connector.connect(
        user= 'root',
        password = 'p@ssw0rd1',
        host = 'mysqldb',
        database = "appflask"
    )
    cursor = mydb.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(256) NOT NULL, age INT NOT NULL, color VARCHAR(256) NOT NULL)"
    )

    cursor.close()
    mydb.close()