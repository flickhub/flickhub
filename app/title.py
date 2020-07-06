from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql.base import VARCHAR, LONGTEXT, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from db_start import db_starter
def title_render(id_mov):		
    connection=db_starter()
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
    result = connection.execute(sql_query,a=id_mov)
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
    id_mv1=[]
    for i in range(len(name)):
        th.append(name[i]+"#"+site[i])
    th=list(dict.fromkeys(th))
    th1=[]
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
                    id_mv1.append(id_mv[j])
                    
                    name.remove(name[j])
                    genre.remove(genre[j])
                    rate.remove(rate[j])
                    vt.remove(vt[j])
                    cst.remove(cst[j])
                    pl.remove(pl[j])
                    im.remove(im[j])
                    trail.remove(trail[j])
                    yr.remove(yr[j])
                    id_mv.remove(id_mv[j])
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
                    id_mv1.append(id_mv[j])
                    
                    name.remove(name[j])
                    genre.remove(genre[j])
                    rate.remove(rate[j])
                    vt.remove(vt[j])
                    cst.remove(cst[j])
                    pl.remove(pl[j])
                    im.remove(im[j])
                    trail.remove(trail[j])
                    yr.remove(yr[j])
                    id_mv.remove(id_mv[j])
                    break
            pass
    resp_data = []
      
    for i in range(len((name1))):
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
        temp_dict["id_mov"]=id_mv1[i]
        
        resp_data.append(temp_dict)
    

    
    return(resp_data)