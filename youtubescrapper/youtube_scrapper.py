
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep 
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="shuvo",passwd="1234",database="data" )
mycursor=mydb.cursor()
chrome_path=r"E:\chromedriver_win32\chromedriver.exe"	 
driver=webdriver.Chrome(chrome_path)
namea=[]
mycursor.execute("SELECT movie FROM movies ")
myresult=mycursor.fetchall()
for i in myresult:
    namea.append(i[0])
print(len(namea)) 
f11 = open("posa.txt", "w",encoding="utf8")
f11.write('[')
for k in range(14530,14534):

    
    try:
        url1="https://www.youtube.com/results?search_query="+namea[k].replace(' ','+')+'+trailer'
    except:
        url1="https://www.youtube.com/results?search_query="+namea[k]+'+trailer'
    driver.get(url1)
    sleep(2)
    f1=open("1.html", "w",encoding="utf8")
    f1.write(driver.page_source)
    with open('1.html', "r+",encoding="utf8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        tags = soup.findall('a',class_='yt-simple-endpoint inline-block style-scope ytd-thumbnail')
        if(t==2):
            m=str(tags)
            if(m.index('href')!=-1):
                e=list(m)
                
                f=""
                for j in range(m.index('href')+6,m.index('yt-img-shadow')-44):
                    
                    f=f+str(e[j])
                    
                print(f)    
                f11.write("'"+str(f)+'$')
            
            c2=0
            try:
                for tag in tags:
                    
                        
                    if(c2==1):
                        d=""
                        for tag2 in tag:
                            if(str(tag2)!='css-build:shady'):
                                d=d+str(tag2)
                        if(d.index('src')!=-1):
                            e=list(d)
                            f=""
                            for j in range(d.index('src')+5,d.index(' width')-1):
                                f=f+str(e[j])
                                
                            print(f)    
                            f11.write(str(f)+"'"+",")
                    
                    
                    c2=c2+1
                    
                print(k)
            except:
                pass
        t=t+1        
                
f11.write(']')    