from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql.base import VARCHAR, LONGTEXT, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from db_start import db_starter

def random1():
    db_starter()
    c=0
    l1=[]
    while(c<25):
        n = random.randint(0,14529)
        sql="SELECT movies.movie,\
            genre.genre,url.url,site.sitename,rating.id_rate,votes.id_votes,\
            cast_plot.id_cast,cast_plot.id_plot,trail_img.id_img,trail_img.id_trail,\
            year.id_year \
            from movies \
            INNER JOIN movie_genre ON movie_genre.id_movie = movies.idmovies \
            INNER JOIN genre ON movie_genre.id_genre = genre.idgenre \
            INNER JOIN movie_url ON movies.idmovies = movie_url.id_movie \
            INNER JOIN url ON movie_url.id_url = url.idurl \
            INNER JOIN site ON url.id_site = site.idsite \
            INNER JOIN rating ON movies.idmovies = rating.idrating \
            INNER JOIN votes ON movies.idmovies = votes.idvotes \
            INNER JOIN cast_plot ON movies.idmovies = cast_plot.id_movie \
            INNER JOIN trail_img ON movies.idmovies = trail_img.id_movie \
            INNER JOIN year ON movies.idmovies = year.idyear \
             "
        w="WHERE "    
        n2="movies.idmovies = :a LIMIT 1"
        t=sql+w+n2
        sql_query = sqlalchemy.text(t)  
        result = connection.execute(sql_query,a=n)
        result_as_list = result.fetchall()
        for row in result_as_list:
            if(row[0]!=''):
                c=c+1
                r1_data=searcher(row[0])
                l1.append(r1_data[0])
    return (l1)
# function to return key for any value 
def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

      
def see(m2):
    
    
    
    counter=1
    m41=[]
    url_site={}
    if " " in m2 : 
        counter=0
        m4=m2.split(" ")
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
                         
    if "-" in m2 : 
        counter=0
        
        m4=m2.split("-")
        m41.append(m4[0])
                     
    if "man" in m2 : 
        counter=0
        m4=m2.split("man")
        l_w=len(m4)
        if(m4[1]==""):
            m41.append(m4[0])
                     
    if "woman" in m2 : 
        counter=0
        m4=m2.split("woman")
        l_w=len(m4)
        if(m4[1]==""):
            m41.append(m4[0])
                     
    if "boy" in m2 : 
        counter=0
        m4=m2.split("boy")
        l_w=len(m4)
        if(m4[1]==""):
            m41.append(m4[0])
                     
    if "girl" in m2 : 
        counter=0
        m4=m2.split("girl")
        l_w=len(m4)
        if(m4[1]==""):
            m41.append(m4[0])
                     
    if "mr." in m2 : 
        counter=0
        m4=m2.split("mr.")
        l_w=len(m4)
        if(m4[0]==""):
            m41.append(m4[1])
                     
    if "mrs." in m2 : 
        counter=0
        m4=m2.split("mrs.")
        l_w=len(m4)
        if(m4[0]==""):
            m41.append(m4[1])
                
    if (counter!=0) : 
        m41.append(m2)
    m41==list(dict.fromkeys(m41))
    m51=m41[0]
    r_data=searcher(m51)
    return (r_data)
def searcher(m61):
    name=[]
    genre=[]
    site=[]
    url=[]
    im=[]
    rate=[]
    yr=[]
    vt=[]
    cst=[]
    pl=[]
    trail=[]
    m71=m61
    sql="SELECT movies.movie,\
        genre.genre,url.url,site.sitename,rating.id_rate,votes.id_votes,\
        cast_plot.id_cast,cast_plot.id_plot,trail_img.id_img,trail_img.id_trail,\
        year.id_year \
        from movies \
        INNER JOIN movie_genre ON movie_genre.id_movie = movies.idmovies \
        INNER JOIN genre ON movie_genre.id_genre = genre.idgenre \
        INNER JOIN movie_url ON movies.idmovies = movie_url.id_movie \
        INNER JOIN url ON movie_url.id_url = url.idurl \
        INNER JOIN site ON url.id_site = site.idsite \
        INNER JOIN rating ON movies.idmovies = rating.idrating \
        INNER JOIN votes ON movies.idmovies = votes.idvotes \
        INNER JOIN cast_plot ON movies.idmovies = cast_plot.id_movie \
        INNER JOIN trail_img ON movies.idmovies = trail_img.id_movie \
        INNER JOIN year ON movies.idmovies = year.idyear \
         "
    w="WHERE "    
    n2="movies.movie LIKE :a "
    t=sql+w+n2
    name1='%'+m71+'%'
    
    sql_query = sqlalchemy.text(t)  
    
    result = connection.execute(sql_query,a=name1)
                            
    result_as_list = result.fetchall()
    for row in result_as_list:
        name.append(row[0])
        genre.append(row[1])
        url.append(row[2])
        site.append(row[3])
        rate.append(row[4])
        vt.append(row[5])
        cst.append(row[6])
        pl.append(row[7])
        im.append(row[8])
        trail.append(row[9])
        yr.append(row[10])
    ##remove duplictes##
    th=[]
    name1=[]
    genre1=[]
    
    url1_site1={}
    im1=[]
    rate1=[]
    yr1=[]
    vt1=[]
    cst1=[]
    pl1=[]
    trail1=[]
    for i in range(len(name)):
        th.append(name[i]+"#"+site[i])
    th=list(dict.fromkeys(th))
    
    for i in range(len(th)):
        try:
            
            for j in range(len(name)):
                if(th[i]==name[j]+"#"+site[j]):
                    url1_site1[name[j]][site[j]]=url[j]
                    name1.append(name[j])
                    genre1.append(genre[j])
                    rate1.append(rate[j])
                    vt1.append(vt[j])
                    cst1.append(cst[j])
                    pl1.append(pl[j])
                    im1.append(im[j])
                    trail1.append(trail[j])
                    yr1.append(yr[j])
                    break

        except:
            
            url1_site1[th[i].split("#")[0]]={}
            for j in range(len(name)):
                if(th[i]==name[j]+"#"+site[j]):
                    g2=[]
                    for k in range(len(name)):
                        
                        if(name[k]==name[j]):
                            g2.append(genre[k])
                        g2=list(dict.fromkeys(g2))    
                        g3=""
                        for m in g2:
                            g3=g3+m+' '
                    url1_site1[name[j]][site[j]]=url[j]
                    name1.append(name[j])
                    genre1.append(g3)
                    rate1.append(rate[j])
                    vt1.append(vt[j])
                    cst1.append(cst[j])
                    pl1.append(pl[j])
                    im1.append(im[j])
                    trail1.append(trail[j])
                    yr1.append(yr[j])
                    break
            pass
    resp_data = []
        
    for i in range(len((url1_site1))):
        temp_dict = {}
        temp_dict["urlname"]=url1_site1[name1[i]]
        temp_dict["image"]=im1[i]
        temp_dict["name"]=name1[i]
        temp_dict["image"]=im1[i]
        temp_dict["genre"]=genre1[i]
        temp_dict["rate"]=rate1[i]
        temp_dict["year"]=yr1[i]
        temp_dict["votes"]=vt1[i]
        temp_dict["cast"]=cst1[i]
        temp_dict["plot"]=pl1[i]
        temp_dict["trailer"]=trail1[i]
        resp_data.append(temp_dict)
    

    
    return(resp_data)
  
        
   
    
    
    