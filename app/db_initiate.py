from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql.base import VARCHAR, LONGTEXT, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from remove_duplicate import dup
engine = create_engine('mysql://root:FlickHub123@localhost:3306/flickhub', convert_unicode=True, echo=False)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
metadata = MetaData()

class User(Base):
    __tablename__ = 'connect'
    f1 = Column('idconnect', INTEGER(display_width=11), primary_key=True, nullable=False)
    f2 = Column('id_site', nullable=False)
    f3 = Column('id_url', nullable=False)
    f4 = Column('id_movie', nullable=False)
    f5 = Column('id_gen', nullable=False) 


def see(m1):
    try:
        name=[]
        genre=[]
        site=[]
        url_name=[]
        th=[]
        m=m1
        m2=m1
        counter=1
        
        if " " in m : 
            counter=0
            m4=m.split(" ")
            l_w=len(m4)
            counter1=1
            if(m4[l_w-1]==""):
                #check here
                    counter1=1
                    m=m4[0]
                    if "-" in m : 
                        counter1=0
                        
                        m4=m.split("-")
                        users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).all()    
                        for user in users:
                            name.append(user.f4)
                            genre.append(user.f5)
                            site.append(user.f2)
                            url_name.append(user.f3)
                            th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
                    if "man" in m : 
                        counter1=0
                        m4=m.split("man")
                        l_w=len(m4)
                        if(m4[1]==""):
                            users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).filter(User.f4.like("%"+"man"+"%")).all()    
                            for user in users:
                                name.append(user.f4)
                                genre.append(user.f5)
                                site.append(user.f2)
                                url_name.append(user.f3)
                                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
                    if "woman" in m : 
                        counter1=0
                        m4=m.split("woman")
                        l_w=len(m4)
                        if(m4[1]==""):
                            users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).filter(User.f4.like("%"+"woman"+"%")).all()    
                            for user in users:
                                name.append(user.f4)
                                genre.append(user.f5)
                                site.append(user.f2)
                                url_name.append(user.f3)
                                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
                    if "boy" in m : 
                        counter1=0
                        m4=m.split("boy")
                        l_w=len(m4)
                        if(m4[1]==""):
                            users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).filter(User.f4.like("%"+"boy"+"%")).all()    
                            for user in users:
                                name.append(user.f4)
                                genre.append(user.f5)
                                site.append(user.f2)
                                url_name.append(user.f3)
                                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
                    if "girl" in m : 
                        counter1=0
                        m4=m.split("girl")
                        l_w=len(m4)
                        if(m4[1]==""):
                            users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).filter(User.f4.like("%"+"girl"+"%")).all()    
                            for user in users:
                                name.append(user.f4)
                                genre.append(user.f5)
                                site.append(user.f2)
                                url_name.append(user.f3)
                                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
                    if "mr." in m : 
                        counter1=0
                        m4=m.split("mr.")
                        l_w=len(m4)
                        if(m4[0]==""):
                            users =session.query(User).filter(User.f4.like("%"+m4[1]+"%")).filter(User.f4.like("%"+"mr."+"%")).all()    
                            for user in users:
                                name.append(user.f4)
                                genre.append(user.f5)
                                site.append(user.f2)
                                url_name.append(user.f3)
                                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
                    if "mrs." in m : 
                        counter1=0
                        m4=m.split("mrs.")
                        l_w=len(m4)
                        if(m4[0]==""):
                            users =session.query(User).filter(User.f4.like("%"+m4[1]+"%")).filter(User.f4.like("%"+"mrs."+"%")).all()    
                            for user in users:
                                name.append(user.f4)
                                genre.append(user.f5)
                                site.append(user.f2)
                                url_name.append(user.f3)
                                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
                    if (counter1!=0) :        
                        users =session.query(User).filter(User.f4.like("%"+m+"%")).all()    
                        for user in users:
                            name.append(user.f4)
                            genre.append(user.f5)
                            site.append(user.f2)
                            url_name.append(user.f3)
                            th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
                        
            else:
                if (l_w==2):
                    users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).filter(User.f4.like("%"+m4[1]+"%")).all()    
                elif (l_w==3):
                    users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).filter(User.f4.like("%"+m4[1]+"%")).filter(User.f4.like("%"+m4[2]+"%")).all()
                elif (l_w==4):
                    users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).filter(User.f4.like("%"+m4[1]+"%")).filter(User.f4.like("%"+m4[2]+"%")).filter(User.f4.like("%"+m4[2]+"%")).all()
                for user in users:
                    name.append(user.f4)
                    genre.append(user.f5)
                    site.append(user.f2)
                    url_name.append(user.f3)
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
        if "-" in m : 
            counter=0
            
            m4=m.split("-")
            users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).all()    
            for user in users:
                name.append(user.f4)
                genre.append(user.f5)
                site.append(user.f2)
                url_name.append(user.f3)
                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
        if "man" in m : 
            counter=0
            m4=m.split("man")
            l_w=len(m4)
            if(m4[1]==""):
                users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).filter(User.f4.like("%"+"man"+"%")).all()    
                for user in users:
                    name.append(user.f4)
                    genre.append(user.f5)
                    site.append(user.f2)
                    url_name.append(user.f3)
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
        if "woman" in m : 
            counter=0
            m4=m.split("woman")
            l_w=len(m4)
            if(m4[1]==""):
                users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).filter(User.f4.like("%"+"woman"+"%")).all()    
                for user in users:
                    name.append(user.f4)
                    genre.append(user.f5)
                    site.append(user.f2)
                    url_name.append(user.f3)
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
        if "boy" in m : 
            counter=0
            m4=m.split("boy")
            l_w=len(m4)
            if(m4[1]==""):
                users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).filter(User.f4.like("%"+"boy"+"%")).all()    
                for user in users:
                    name.append(user.f4)
                    genre.append(user.f5)
                    site.append(user.f2)
                    url_name.append(user.f3)
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
        if "girl" in m : 
            counter=0
            m4=m.split("girl")
            l_w=len(m4)
            if(m4[1]==""):
                users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).filter(User.f4.like("%"+"girl"+"%")).all()    
                for user in users:
                    name.append(user.f4)
                    genre.append(user.f5)
                    site.append(user.f2)
                    url_name.append(user.f3)
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
        if "mr." in m : 
            counter=0
            m4=m.split("mr.")
            l_w=len(m4)
            if(m4[0]==""):
                users =session.query(User).filter(User.f4.like("%"+m4[1]+"%")).filter(User.f4.like("%"+"mr."+"%")).all()    
                for user in users:
                    name.append(user.f4)
                    genre.append(user.f5)
                    site.append(user.f2)
                    url_name.append(user.f3)
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
        if "mrs." in m : 
            counter=0
            m4=m.split("mrs.")
            l_w=len(m4)
            if(m4[0]==""):
                users =session.query(User).filter(User.f4.like("%"+m4[1]+"%")).filter(User.f4.like("%"+"mrs."+"%")).all()    
                for user in users:
                    name.append(user.f4)
                    genre.append(user.f5)
                    site.append(user.f2)
                    url_name.append(user.f3)
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
        if (counter!=0) :   
            users =session.query(User).filter(User.f4.like("%"+m+"%")).all()    
            for user in users:
                name.append(user.f4)
                genre.append(user.f5)
                site.append(user.f2)
                url_name.append(user.f3)
                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
         
        
        th=list(dict.fromkeys(th))
            
        
        name2=[]
        genre2=[]
        site2=[]
        url_name2=[]


        for m in range(len(th)):
            name2.append((th[m].split("#"))[0])
            genre2.append((th[m].split("#"))[1])
            site2.append((th[m].split("#"))[2])
            url_name2.append((th[m].split("#"))[3])
        
        
        #removing duplicate
        url_name3,img3,site3,name3,genre3=dup(name2,genre2,site2,url_name2)
        l=len(site3)
    except:
        session.rollback()
        raise
    finally:
        session.close()
    
    
    return (url_name3,img3,l,name3,genre3)
