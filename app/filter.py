from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql.base import VARCHAR, LONGTEXT, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from db_start import db_starter

def filter_movies(params, page):
    offset = (int(page) - 1)*21
    connection=db_starter()
    query_init = '''Select mm.idmovies, mm.movie, tm.id_img, tm.id_trail, group_concat(uu.url), group_concat(ss.sitename)
        from movies as mm 
        left join movie_url as mu on mu.id_movie = mm.idmovies
        left join url as uu on uu.idurl = mu.id_url
        left join trail_img as tm on tm.id_movie = mm.idmovies
        left join site as ss on ss.idsite = uu.id_site
        left join rating as rr on rr.idrating = mm.idmovies
        left join movie_genre as mg on mg.id_movie = mm.idmovies
        left join genre as gg on gg.idgenre = mg.id_genre
        left join movie_lang as ml on ml.id_movie = mm.idmovies
        left join language as ll on ll.idlanguage = ml.id_lang
        left join year as yy on yy.idyear = mm.idmovies'''
    
       
    filter_param = "where "  
    if params.get('genre_bool', False):
        filter_param = filter_param + "gg.genre IN ({}) AND".format(params['genres'])
    if params.get('rating_bool', False):
        filter_param = filter_param + " rr.id_rate >= {} AND rr.id_rate <= {} AND".format(params['rating'][0], int(params['rating'][0])+1)
    if params.get('platform_bool', False):
        filter_param = filter_param + " ss.sitename IN ({}) AND".format(params['platforms'])
    if params.get('year_bool', False):
        filter_param = filter_param + " yy.id_year IN ({}) AND".format(params['years'])

    
    ending = '''GROUP BY (mm.idmovies)
    ORDER BY rr.id_rate Desc
    limit {}, 21
    ;'''.format(offset)
    
    query = query_init + ' ' + filter_param.strip('AND') + ' ' + ending
    data = []
    result = connection.execute(query)

    for row in result:
        temp_dict = {}
        temp_dict['movie_id'] = row[0]
        temp_dict['movie_name'] = row[1]
        temp_dict['img'] = row[2]
        temp_dict['y_src'] = row[3]
        try:
            urls = list(set(row[4].split(',')))
        except:
            urls = []
        try:
            platforms = list(set(row[5].split(',')))
        except:
            platforms = []
        
        plat_dict = {}
        for pp in platforms:
            for url in urls:
                if pp.lower() in url:
                    plat_dict[pp] = url
                    break
        temp_dict['platforms'] = plat_dict
        data.append(temp_dict)
    
    connection.close()
    return {'data': data}


def get_single_movie(val):
    connection=db_starter()
    query = '''Select mm.idmovies, mm.movie, tm.id_img, tm.id_trail, group_concat(uu.url), group_concat(ss.sitename), cp.id_cast, cp.id_plot, group_concat(gg.genre)
        from movies as mm 
        left join cast_plot as cp on cp.id_movie = mm.idmovies
        left join movie_genre as mg on mg.id_movie = mm.idmovies
        left join genre as gg on gg.idgenre = mg.id_genre
        left join movie_url as mu on mu.id_movie = mm.idmovies
        left join url as uu on uu.idurl = mu.id_url
        left join trail_img as tm on tm.id_movie = mm.idmovies
        left join site as ss on ss.idsite = uu.id_site
        where mm.idmovies = {}
        GROUP BY (mm.idmovies);'''.format(val)

    data = []
    result = connection.execute(query)

    for row in result:
        temp_dict = {}
        temp_dict['movie_id'] = row[0]
        temp_dict['movie_name'] = row[1]
        temp_dict['img'] = row[2]
        temp_dict['y_src'] = row[3]
        try:
            urls = list(set(row[4].split(',')))
        except:
            urls = []
        try:
            platforms = list(set(row[5].split(',')))
        except:
            platforms = []
        
        temp_dict['cast'] = row[6]
        temp_dict['plot'] = row[7]
        try:
            temp_dict['genres'] = list(set(row[8].split(',')))
        except:
            temp_dict['genres'] = []
        
        plat_dict = {}
        for pp in platforms:
            for url in urls:
                if pp.lower() in url:
                    plat_dict[pp] = url
                    break
        temp_dict['platforms'] = plat_dict
        data.append(temp_dict)
    
    connection.close()
    return {'data': data}


def get_movies_name(val):
    connection=db_starter()
    sql_query= 'Select movie from movies where movie like '+'"%%'+val+'%%";'
    data = []
    result = connection.execute(sql_query)
    for row in result:
        data.append(row[0])

    connection.close()
    return {"data": data}


# function to return key for any value 
def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"
