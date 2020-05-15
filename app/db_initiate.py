from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql.base import VARCHAR, LONGTEXT, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from remove_duplicate import dup
engine = create_engine('mysql://shuvo:1234@localhost:3306/data', convert_unicode=True, echo=False)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
metadata = MetaData()

class User(Base):
    __tablename__ = 'Connect'
    f1 = Column('idconnect', INTEGER(display_width=11), primary_key=True, nullable=False)
    f2 = Column('id_site', nullable=False)
    f3 = Column('id_url', nullable=False)
    f4 = Column('id_movie', nullable=False)
    f5 = Column('id_gen', nullable=False) 


def see(m1):
        m=m1.split(" ")
        l_w=len(m)
        name=[]
        genre=[]
        site=[]
        url_name=[]
        th=[]
        for j in range(l_w):
            users =session.query(User).filter(User.f4.like("%"+m[j]+"%")).all()
            
            for user in users:
                name.append(user.f4)
                genre.append(user.f5)
                site.append(user.f2)
                url_name.append(user.f3)
                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3)
        m=m1.split("-")
        l_w=len(m)
        
        for j in range(l_w):
            users =session.query(User).filter(User.f4.like("%"+m[j]+"%")).all()
            
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
        return (url_name3,img3,l,name3,genre3)
