import mysql.connector
from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql.base import VARCHAR, LONGTEXT, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from bs4 import BeautifulSoup
from ast import literal_eval
mydb=mysql.connector.connect(host="localhost",user="shuvo",passwd="1234",database="data" )
mycursor=mydb.cursor()
# importing the module 
import imdb 
name=[]
# creating instance of IMDb 
ia = imdb.IMDb() 
mycursor.execute("SELECT movie FROM movies ")
myresult=mycursor.fetchall()
for i in myresult:
    name.append(i[0])

for j in range(len(name)):
    try:
        search = ia.search_movie(name[j])
        print(j)
    except:
        pass
    try:
        fetch=search[0]
        id=fetch.movieID 
        search1=ia.get_movie(id) 
        try:
            languages = search1.data['languages'] 
            h=""
            for k in range(len(languages)):
                if(k!=len(languages)-1):
                    h=h+languages[k]+','
                else:
                    h=h+languages[k]
            
            print(h)
            sql="INSERT INTO languages(idlanguage, lang) VALUES (%s, %s)"
            d=(name[j],h)
            mycursor.execute(sql,d)
            mydb.commit()
        except:
            pass
    except:
        pass
        
        
        
        