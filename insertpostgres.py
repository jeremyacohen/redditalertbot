#!/usr/bin/python
import psycopg2
from config import config
 
 
def insert_name(username, email, phrases):
    """ insert a new vendor into the vendors table """
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        if len(phrases) == 1:
            postgres_insert_query = """ INSERT INTO usernames (username, email, phrase1) VALUES (%s,%s,%s)"""
            record_to_insert = (username, email, phrases[0])
        elif len(phrases) == 2:
            postgres_insert_query = """ INSERT INTO usernames (username, email, phrase1, phrase2) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (username, email, phrases[0], phrases[1])
        elif len(phrases) == 3:
            postgres_insert_query = """ INSERT INTO usernames (username, email, phrase1, phrase2, phrase3) VALUES (%s,%s,%s,%s,%s)"""
            record_to_insert = (username, email, phrases[0], phrases[1], phrases[2])
        # execute the INSERT statement
        cur.execute(postgres_insert_query, record_to_insert)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def updateInfo(username, newInfo, command):
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        if command == "phone":
            postgres_insert_query = """UPDATE usernames SET phonenumber = %s where username = %s;"""
            record_to_insert = (newInfo, username)
            cur.execute(postgres_insert_query, record_to_insert)
        elif command == "email":
            postgres_insert_query = """UPDATE usernames SET email = %s where username = %s;"""
            record_to_insert = (newInfo, username)
            cur.execute(postgres_insert_query, record_to_insert)
        
        # execute the INSERT statement
        
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def deleteuser(user):
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        postgres_insert_query = """DELETE FROM usernames where username = %s;"""
        record_to_insert = (user,)
        # execute the INSERT statement
        cur.execute(postgres_insert_query, record_to_insert)
        postgres_insert_query = """DELETE FROM phrasestouser where username = %s;"""
        record_to_insert = (user,)
        # execute the INSERT statement
        cur.execute(postgres_insert_query, record_to_insert)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def getInfo(user):
    conn = None
    try:
        # read database configuration
        params = config()
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        postgres_insert_query = """SELECT * FROM usernames where username = %s;"""
        record = [user, ]
        cur.execute(postgres_insert_query, record)
        results = cur.fetchone()
        return results
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def userExist(username):
    try:
        # read database configuration
        params = config()
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        postgres_insert_query = """SELECT count(username) FROM usernames WHERE username = %s;"""
        record = [username,]
        cur.execute(postgres_insert_query, record)
        count = cur.fetchone()
        return count[0]
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def insertPhrasesUsers(phrases, username):
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()

        if len(phrases) >= 1:
            postgres_insert_query = """ INSERT INTO phrasestouser (phrases, username) VALUES (%s,%s)"""
            record_to_insert = (phrases[0],username)
            cur.execute(postgres_insert_query, record_to_insert)
        if len(phrases) >= 2:
            postgres_insert_query = """ INSERT INTO phrasestouser (phrases, username) VALUES (%s,%s)"""
            record_to_insert = (phrases[1],username)
            cur.execute(postgres_insert_query, record_to_insert)
        if len(phrases) == 3:
            postgres_insert_query = """ INSERT INTO phrasestouser (phrases, username) VALUES (%s,%s)"""
            record_to_insert = (phrases[2],username)
            cur.execute(postgres_insert_query, record_to_insert)   
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def getAllEmails(phrase):
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        postgres_insert_query = """SELECT usernames.email from usernames join phrasestouser on phrasestouser.username = usernames.username where phrasestouser.phrases = %s;"""
        record_to_insert = [phrase,]
        cur.execute(postgres_insert_query, record_to_insert)
        emails = cur.fetchall()
        return emails
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def getAllPhrases():
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        postgres_insert_query = """SELECT phrases from phrasestouser;"""
        record_to_insert = []
        cur.execute(postgres_insert_query, record_to_insert)
        phrases = set(cur.fetchall())
        return phrases
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # insert one vendor
    #insert_name("jaboydar'", "3107280895")
    # update_phone("3107280895", "jaboyda")
    emails = getAllEmails("sure")
    for item in emails:
        print (item[0])
    #deleteuser("jaboydar;")
    # insert multiple vendors