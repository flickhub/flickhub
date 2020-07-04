from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql.base import VARCHAR, LONGTEXT, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from db_start import db_starter

# function to return key for any value 
def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"
################          
#####filter#####
################
def filter_fr_all(dict12):
    db_starter()
    dict1=dict12
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
    dict_rate={'0':['0','1'],'1':['1','2'],'2':['2','3'],'3':['3','4'],'4':['4','5'],'5':['5','6'],'6':['6','7'],'7':['7','8'],'8':['8','9'],'9':['9','10']}
    dict_year={'0':['1950','1955'],'1':['1956','1960'],'2':['1961','1965'],
    '3':['1966','1970'],'4':['1971','1975'],'5':['1976','1980'],'6':['1981','1985'],
    '7':['1986','1990'],'8':['1991','1995'],'9':['1996','2000'],'10':['2001','2005'],'11':['2006','2010'],
    '12':['2011','2015'],'13':['2016','2020']}
    try:
        gen1=dict1["filters"]["genre"]
    except:
        gen1=[]
    
        pass
    try:
        yr1=dict1["filters"]["year"]
        lower_yr=[]
        upper_yr=[]       
    
        for i in yr1:
                lower_yr.append(dict_year[i][0])
                upper_yr.append(dict_year[i][1])
                
    except:
        yr1=[]
        lower_yr=[]
        upper_yr=[]
        pass
    
    
    try:
        rate1=dict1["filters"]["rating"]
    except:
        pass
    lower_rate=[]
    upper_rate=[]       
    try:
        for i in rate1:
            try:
                lower_rate.append(dict_rate[i][0])
            except:
                pass
            try:
                upper_rate.append(dict_rate[i][1])
            except:
                pass
    except:
        pass
    key_list = list(dict1["filters"].keys()) 
    val_list = list(dict1["filters"].values())
    site1=[]
    for i in range(len(val_list)):
        try:
            
            if(val_list[i]==True):
                site1.append(key_list[i])
        except:
            pass
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
    g="genre.genre IN :a "
    r=" rating.id_rate > :b AND rating.id_rate < :c  "
    y=" year.id_year > :d AND year.id_year < :e  "
    s=" site.sitename IN :f "
    if(len(gen1)!=0):
        if(len(site1)!=0):
        
            if(len(lower_rate)!=0):
                for i in range(len(lower_rate)):
                    
                    if(len(lower_yr)!=0):
                        for j in range(len(lower_yr)):
                            
                                
                                t=sql+w+g+'AND'+y+'AND'+r+'AND'+s
                                sql_query = sqlalchemy.text(t)              
                                try:
                                    result = connection.execute(sql_query,a=gen1,
                                            b=lower_rate[i],
                                            c=upper_rate[i],
                                            d=lower_yr[j],
                                            e=upper_yr[j],
                                            f=site1
                                            )
                                
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
                                except:
                                    pass    
                                    
                    else:
                        t=sql+w+g+'AND'+r+'AND'+s
                        sql_query = sqlalchemy.text(t)              
                        try:
                            result = connection.execute(sql_query,a=gen1,
                                    b=lower_rate[i],
                                    c=upper_rate[i],
                                    f=site1
                                    )
                        
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
                        except:
                            pass    
            else:
                if(len(lower_yr)!=0):
                    for j in range(len(lower_yr)):
                            
                            t=sql+w+g+'AND'+y+'AND'+s
                            sql_query = sqlalchemy.text(t)              
                            try:
                                result = connection.execute(sql_query,a=gen1,
                                        d=lower_yr[j],
                                        e=upper_yr[j],
                                        f=site1
                                        )
                            
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
                            except:
                                pass    
                else:
                    t=sql+w+g+'AND'+s
                    sql_query = sqlalchemy.text(t)              
                    try:
                        result = connection.execute(sql_query,a=gen1,
                                f=site1
                                )
                    
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
                    except:
                        pass
        else:
            if(len(lower_rate)!=0):
                for i in range(len(lower_rate)):
                    
                    if(len(lower_yr)!=0):
                        for j in range(len(lower_yr)):
                            
                                
                                t=sql+w+g+'AND'+y+'AND'+r
                                sql_query = sqlalchemy.text(t)              
                                try:
                                    result = connection.execute(sql_query,a=gen1,
                                            b=lower_rate[i],
                                            c=upper_rate[i],
                                            d=lower_yr[j],
                                            e=upper_yr[j]
                                            )
                                            
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
                                except:
                                    pass    
                    else:
                        t=sql+w+g+'AND'+r
                        sql_query = sqlalchemy.text(t)              
                        try:
                            result = connection.execute(sql_query,a=gen1,
                                    b=lower_rate[i],
                                    c=upper_rate[i]
                                    )
                        
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
                        except:
                            pass    
            else:
                if(len(lower_yr)!=0):
                    for j in range(len(lower_yr)):
                       
                            t=sql+w+g+'AND'+y
                            sql_query = sqlalchemy.text(t)              
                            try:
                                result = connection.execute(sql_query,a=gen1,
                                        d=lower_yr[j],
                                        e=upper_yr[j]
                                        )
                            
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
                            except:
                                pass    
                else:
                    t=sql+w+g
                    sql_query = sqlalchemy.text(t)              
                    try:
                        result = connection.execute(sql_query,a=gen1
                                )
                    
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
                    except:
                        pass    
    else:
        if(len(site1)!=0):
        
            if(len(lower_rate)!=0):
                for i in range(len(lower_rate)):
                    
                    if(len(lower_yr)!=0):
                        for j in range(len(lower_yr)):
                            
                                
                                t=sql+w+y+'AND'+r+'AND'+s
                                sql_query = sqlalchemy.text(t)              
                                try:
                                    result = connection.execute(sql_query,
                                            b=lower_rate[i],
                                            c=upper_rate[i],
                                            d=lower_yr[j],
                                            e=upper_yr[j],
                                            f=site1
                                            )
                                
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
                                except:
                                    pass    
                    else:
                        t=sql+w+r+'AND'+s
                        sql_query = sqlalchemy.text(t)              
                        try:
                            result = connection.execute(sql_query,
                                    b=lower_rate[i],
                                    c=upper_rate[i],
                                    f=site1
                                    )
                        
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
                        except:
                            pass    
            else:
                if(len(lower_yr)!=0):
                    for j in range(len(lower_yr)):
                       
                            t=sql+w+y+'AND'+s
                            sql_query = sqlalchemy.text(t)              
                            try:
                                result = connection.execute(sql_query,
                                        d=lower_yr[j],
                                        e=upper_yr[j],
                                        f=site1
                                        )
                            
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
                            except:
                                pass    
                else:
                    t=sql+w+s
                    sql_query = sqlalchemy.text(t)              
                    try:
                        result = connection.execute(sql_query,
                            f=site1
                            )
                    
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
                    except:
                        pass
        else:
            if(len(lower_rate)!=0):
                for i in range(len(lower_rate)):
                    
                    if(len(lower_yr)!=0):
                        for j in range(len(lower_yr)):
                            
                                
                                t=sql+w+y+'AND'+r
                                sql_query = sqlalchemy.text(t)              
                                try:
                                    result = connection.execute(sql_query,
                                            b=lower_rate[i],
                                            c=upper_rate[i],
                                            d=lower_yr[j],
                                            e=upper_yr[j]
                                            )
                                
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
                                except:
                                    pass    
                    else:
                        t=sql+w+r
                        
                        sql_query = sqlalchemy.text(t)              
                        try:
                            result = connection.execute(sql_query,
                                    b=lower_rate[i],
                                    c=upper_rate[i]
                                    )
                        
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
                        except:
                            pass    
            else:
                if(len(lower_yr)!=0):
                    for j in range(len(lower_yr)):
                       
                            t=sql+w+y
                            sql_query = sqlalchemy.text(t)              
                            try:
                                result = connection.execute(sql_query,
                                        d=lower_yr[j],
                                        e=upper_yr[j]
                                        )
                            
                            
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
                            except:
                                pass
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
  