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
    f6 = Column('id_img', nullable=True)
    f7 = Column('id_rate', nullable=True)
    f8 = Column('id_year', nullable=True)
    f9 = Column('id_votes', nullable=True)
    f10 = Column('id_genr', nullable=True)
    f11 = Column('id_cast', nullable=True)
    f12 = Column('id_plot', nullable=True)
    
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
                            im.append(user.f6)
                            rate.append(user.f7)
                            yr.append(user.f8)
                            vt.append(user.f9)
                            gen.append(user.f10)
                            cst.append(user.f11)
                            pl.append(user.f12)
                            
                            
                            th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                              
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
                                im.append(user.f6)
                                rate.append(user.f7)
                                yr.append(user.f8)
                                vt.append(user.f9)
                                gen.append(user.f10)
                                cst.append(user.f11)
                                pl.append(user.f12)
                                
                                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
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
                                im.append(user.f6)
                                rate.append(user.f7)
                                yr.append(user.f8)
                                vt.append(user.f9)
                                gen.append(user.f10)
                                cst.append(user.f11)
                                pl.append(user.f12)
                                
                                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
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
                                im.append(user.f6)
                                rate.append(user.f7)
                                yr.append(user.f8)
                                vt.append(user.f9)
                                gen.append(user.f10)
                                cst.append(user.f11)
                                pl.append(user.f12)
                                
                                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
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
                                im.append(user.f6)
                                rate.append(user.f7)
                                yr.append(user.f8)
                                vt.append(user.f9)
                                gen.append(user.f10)
                                cst.append(user.f11)
                                pl.append(user.f12)
                                
                                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
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
                                im.append(user.f6)
                                rate.append(user.f7)
                                yr.append(user.f8)
                                vt.append(user.f9)
                                gen.append(user.f10)
                                cst.append(user.f11)
                                pl.append(user.f12)
                                
                                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
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
                                im.append(user.f6)
                                rate.append(user.f7)
                                yr.append(user.f8)
                                vt.append(user.f9)
                                gen.append(user.f10)
                                cst.append(user.f11)
                                pl.append(user.f12)
                                
                                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
                    if (counter1!=0) :        
                        users =session.query(User).filter(User.f4.like("%"+m+"%")).all()    
                        for user in users:
                            name.append(user.f4)
                            genre.append(user.f5)
                            site.append(user.f2)
                            url_name.append(user.f3)
                            im.append(user.f6)
                            rate.append(user.f7)
                            yr.append(user.f8)
                            vt.append(user.f9)
                            gen.append(user.f10)
                            cst.append(user.f11)
                            pl.append(user.f12)
                            
                            th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
                        
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
                    im.append(user.f6)
                    rate.append(user.f7)
                    yr.append(user.f8)
                    vt.append(user.f9)
                    gen.append(user.f10)
                    cst.append(user.f11)
                    pl.append(user.f12)
                    
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
        if "-" in m : 
            counter=0
            
            m4=m.split("-")
            users =session.query(User).filter(User.f4.like("%"+m4[0]+"%")).all()    
            for user in users:
                name.append(user.f4)
                genre.append(user.f5)
                site.append(user.f2)
                url_name.append(user.f3)
                im.append(user.f6)
                rate.append(user.f7)
                yr.append(user.f8)
                vt.append(user.f9)
                gen.append(user.f10)
                cst.append(user.f11)
                pl.append(user.f12)
                
                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
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
                    im.append(user.f6)
                    rate.append(user.f7)
                    yr.append(user.f8)
                    vt.append(user.f9)
                    gen.append(user.f10)
                    cst.append(user.f11)
                    pl.append(user.f12)
                    
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
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
                    im.append(user.f6)
                    rate.append(user.f7)
                    yr.append(user.f8)
                    vt.append(user.f9)
                    gen.append(user.f10)
                    cst.append(user.f11)
                    pl.append(user.f12)
                    
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
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
                    im.append(user.f6)
                    rate.append(user.f7)
                    yr.append(user.f8)
                    vt.append(user.f9)
                    gen.append(user.f10)
                    cst.append(user.f11)
                    pl.append(user.f12)
                    
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
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
                    im.append(user.f6)
                    rate.append(user.f7)
                    yr.append(user.f8)
                    vt.append(user.f9)
                    gen.append(user.f10)
                    cst.append(user.f11)
                    pl.append(user.f12)
                    
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
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
                    im.append(user.f6)
                    rate.append(user.f7)
                    yr.append(user.f8)
                    vt.append(user.f9)
                    gen.append(user.f10)
                    cst.append(user.f11)
                    pl.append(user.f12)
                    
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
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
                    im.append(user.f6)
                    rate.append(user.f7)
                    yr.append(user.f8)
                    vt.append(user.f9)
                    gen.append(user.f10)
                    cst.append(user.f11)
                    pl.append(user.f12)
                    
                    th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
        if (counter!=0) :   
            users =session.query(User).filter(User.f4.like("%"+m+"%")).all()    
            for user in users:
                name.append(user.f4)
                genre.append(user.f5)
                site.append(user.f2)
                url_name.append(user.f3)
                im.append(user.f6)
                rate.append(user.f7)
                yr.append(user.f8)
                vt.append(user.f9)
                gen.append(user.f10)
                cst.append(user.f11)
                pl.append(user.f12)
                
                th.append(user.f4+"#"+user.f5+"#"+user.f2+"#"+user.f3+"#"+str(user.f6)+"#"+str(user.f7)+"#"+str(user.f8)+"#"+str(user.f9)+"#"+str(user.f10)+"#"+str(user.f11)+"#"+str(user.f12))
                             
         
        
        th=list(dict.fromkeys(th))
         
        
        name2=[]
        genre2=[]
        site2=[]
        url_name2=[]
        im2=[]
        rate2=[]
        yr2=[]
        vt2=[]
        gen2=[]
        cst2=[]
        pl2=[]
        
        
        for m in range(len(th)):
            name2.append((th[m].split("#"))[0])
            genre2.append((th[m].split("#"))[1])
            site2.append((th[m].split("#"))[2])
            url_name2.append((th[m].split("#"))[3])
            im2.append((th[m].split("#"))[4])
            rate2.append((th[m].split("#"))[5])
            yr2.append((th[m].split("#"))[6])
            vt2.append((th[m].split("#"))[7])
            gen2.append((th[m].split("#"))[8])
            cst2.append((th[m].split("#"))[9])
            pl2.append((th[m].split("#"))[10])
            
        #removing duplicate
        url_name3,img3,site3,name3,genre3,im3,rate3,yr3,vt3,gen3,cst3,pl3=dup(name2,genre2,site2,url_name2,im2,rate2,yr2,vt2,gen2,cst2,pl2)
        l=len(site3)
    except:
        session.rollback()
        raise
    finally:
        session.close()
    
    
    return (url_name3,img3,l,name3,genre3,im3,rate3,yr3,vt3,gen3,cst3,pl3)
