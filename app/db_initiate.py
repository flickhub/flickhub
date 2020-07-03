from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql.base import VARCHAR, LONGTEXT, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://shuvo:1234@localhost:3306/data', convert_unicode=True, echo=False)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
metadata = MetaData()

class User(Base):
    __tablename__ = 'movies'
    f1 = Column('idmovies', nullable=False,primary_key=True)
    f2 = Column('movie', nullable=False)
class User1(Base):
    __tablename__ = 'movie_genre'
    f1 = Column('id', nullable=False,primary_key=True)
    f3 = Column('id_movie', nullable=False)
    f4 = Column('id_genre', nullable=False)
class User2(Base):
    __tablename__ = 'genre'
    f1 = Column('idgenre', nullable=False,primary_key=True)
    f5 = Column('genre', nullable=False)
class User3(Base):
    __tablename__ = 'movie_url'
    f1 = Column('id', nullable=False,primary_key=True)
    f3 = Column('id_movie', nullable=False)
    f4 = Column('id_url', nullable=False)
class User4(Base):
    __tablename__ = 'url'
    f1 = Column('idurl', nullable=False,primary_key=True)
    f5 = Column('url', nullable=False)    
    f6 = Column('id_site', nullable=False) 
class User5(Base):
    __tablename__ = 'rating'
    f1 = Column('idrating', nullable=False,primary_key=True)
    f5 = Column('id_rate', nullable=False)    
class User6(Base):
    __tablename__ = 'year'
    f1 = Column('idyear', nullable=False,primary_key=True)
    f5 = Column('id_year', nullable=False)    
class User7(Base):
    __tablename__ = 'votes'
    f1 = Column('idvotes', nullable=False,primary_key=True)
    f5 = Column('id_votes', nullable=False)
class User8(Base):
    __tablename__ = 'cast_plot'
    f1 = Column('id_movie', nullable=False,primary_key=True)
    f5 = Column('id_cast', nullable=True)
    f6 = Column('id_plot', nullable=True)
class User9(Base):
    __tablename__ = 'trail_img'
    f1 = Column('id_movie', nullable=False,primary_key=True)
    f5 = Column('id_img', nullable=True)
    f6 = Column('id_trail', nullable=True)
class User10(Base):
    __tablename__ = 'site'
    f1 = Column('idsite', nullable=False,primary_key=True)
    f5 = Column('sitename', nullable=False)
      
def see(m1):
    
    try:
        name=[]
        genre=[]
        site=[]
        url_name=[]
        im=[]
        rate=[]
        yr=[]
        vt=[]
        gen=[]
        cst=[]
        pl=[]
        pos=[]
        trail=[]
        url_site={}
        th=[]
        m=m1
        m2=m1
        counter=1
        m41=[]
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
                        m41.append(m4[0])
                          
                    if "man" in m : 
                        counter1=0
                        m4=m.split("man")
                        l_w=len(m4)
                        if(m4[1]==""):
                            m41.append(m4[0])
                            
                    if "woman" in m : 
                        counter1=0
                        m4=m.split("woman")
                        l_w=len(m4)
                        if(m4[1]==""):
                            m41.append(m4[0])
                             
                    if "boy" in m : 
                        counter1=0
                        m4=m.split("boy")
                        l_w=len(m4)
                        if(m4[1]==""):
                            m41.append(m4[0])
                            
                    if "girl" in m : 
                        counter1=0
                        m4=m.split("girl")
                        l_w=len(m4)
                        if(m4[1]==""):
                            m41.append(m4[0])
                             
                    if "mr." in m : 
                        counter1=0
                        m4=m.split("mr.")
                        l_w=len(m4)
                        if(m4[0]==""):
                            m41.append(m4[1])
                             
                    if "mrs." in m : 
                        counter1=0
                        m4=m.split("mrs.")
                        l_w=len(m4)
                        if(m4[0]==""):
                            m41.append(m4[1])
                            
                    if (counter1!=0) :   
                        m41.append(m)
                             
                        
            else:
                if (l_w==2):
                    m41.append(m4[0])
                elif (l_w==3):
                    m41.append(m4[0])
                    
                elif (l_w==4):
                    m41.append(m4[0])
                             
        if "-" in m : 
            counter=0
            
            m4=m.split("-")
            m41.append(m4[0])
                         
        if "man" in m : 
            counter=0
            m4=m.split("man")
            l_w=len(m4)
            if(m4[1]==""):
                m41.append(m4[0])
                         
        if "woman" in m : 
            counter=0
            m4=m.split("woman")
            l_w=len(m4)
            if(m4[1]==""):
                m41.append(m4[0])
                         
        if "boy" in m : 
            counter=0
            m4=m.split("boy")
            l_w=len(m4)
            if(m4[1]==""):
                m41.append(m4[0])
                         
        if "girl" in m : 
            counter=0
            m4=m.split("girl")
            l_w=len(m4)
            if(m4[1]==""):
                m41.append(m4[0])
                         
        if "mr." in m : 
            counter=0
            m4=m.split("mr.")
            l_w=len(m4)
            if(m4[0]==""):
                m41.append(m4[1])
                         
        if "mrs." in m : 
            counter=0
            m4=m.split("mrs.")
            l_w=len(m4)
            if(m4[0]==""):
                m41.append(m4[1])
                    
        if (counter!=0) : 
            m41.append(m)
        
        
        
        
        for search in m41:
            users =session.query(User).filter(User.f2.like("%"+search+"%")).all()    
            for user in users:
                
                name.append(user.f2)          
                pos.append(user.f1)    
                pos=list(dict.fromkeys(pos))
                th=[]
            c=0
            for search1 in pos:
                d=""
                ##genre##
                u1 =session.query(User1).filter(User1.f3 == search1).all()    
                for u2 in u1:
                    u3 =session.query(User2).filter(User2.f1 == u2.f4).all()
                    for u4 in u3:
                        d=d+str(u4.f5)+" "
                    genre.append(d)
                
                ##rate##
                u1 =session.query(User5).filter(User5.f1 == search1).one()    
                rate.append(u1.f5)
                ##year##
                u1 =session.query(User6).filter(User6.f1 == search1).one()    
                yr.append(u1.f5)
                ##votes##
                u1 =session.query(User7).filter(User7.f1 == search1).one()    
                vt.append(u1.f5)
                ##image and trailer##
                u1 =session.query(User9).filter(User9.f1 ==  search1).one()   
                im.append(u1.f5)
                trail.append(u1.f6)
                #url##
                u1 =session.query(User3).filter(User3.f3 == search1).all()   
                
                
                for u2 in u1:
                    u3 =session.query(User4).filter(User4.f1 == u2.f4)
                    for u4 in u3:
                        u5 =session.query(User10).filter(User10.f1 == u4.f6).all()
                        for u6 in u5:
                            th.append(u4.f5+"#"+u6.f5)
                            break
                
                th=list(dict.fromkeys(th))
                
                url_site[name[c]]={}
                for m in th:
                    
                    url_site[name[c]][m.split('#')[1]]=m.split('#')[0]
                
                c=c+1    
                    
                
                ##cast and plot ##
                u1 =session.query(User8).filter(User8.f1 == pos[0]).one()   
                cst.append(u1.f5)
                pl.append(u1.f6)
        
        

        
  
        
    except:
        session.rollback()
        raise
    finally:
        session.close()
    
    
    return (name,rate,yr,vt,cst,pl,im,trail,genre,url_site)