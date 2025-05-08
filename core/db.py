import sqlite3
from sqlite3 import Error

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def int_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS users(
            id Integer PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            hashed_password TEXT NOT NULL
        )
        '''
    )
    conn.commit()
    conn.close()

def get_user_by_username(username:str):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?',(username,)).fetchone()
    conn.close()
    return user

def add_user(username:str , email:str, hashed_password:str):
    conn = get_db_connection()
    conn.execute('INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)', (username, email, hashed_password))
    conn.commit()
    conn.close()
    