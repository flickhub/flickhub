from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.dialects.mysql.base import VARCHAR, LONGTEXT, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from db_start import db_starter
import random

def most_frequent(List): 
    return max(set(List), key = List.count) 

def get_similar_titles(genre_list, page, language_bool):
    offset = (int(page) - 1)*42
    connection=db_starter()
    query = '''Select mm.idmovies, mm.movie, tm.id_img, tm.id_trail, group_concat(uu.url), group_concat(ss.sitename), group_concat(gg.genre)
            from movies as mm 
            left join movie_url as mu on mu.id_movie = mm.idmovies
            left join url as uu on uu.idurl = mu.id_url
            left join trail_img as tm on tm.id_movie = mm.idmovies
            left join site as ss on ss.idsite = uu.id_site
            left join movie_genre as mg on mg.id_movie = mm.idmovies
            left join genre as gg on gg.idgenre = mg.id_genre
            left join rating as rr on rr.idrating = mm.idmovies
            where gg.genre in  ('{}')'''.format("', '".join(genre_list))
            
    
    if language_bool:
        query = query + " AND ll.lang like 'Hindi%%'"
    
    query = query + ''' GROUP BY (mm.idmovies)
            ORDER BY rr.id_rate Desc
            Limit {}, 42;'''.format(offset)

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
    
    random.shuffle(data)
    connection.close()
    return data


def random_cat():
    query = '''Select mm.idmovies, mm.movie, tm.id_img, tm.id_trail, group_concat(uu.url), group_concat(ss.sitename)
        from movies as mm 
        left join movie_url as mu on mu.id_movie = mm.idmovies
        left join url as uu on uu.idurl = mu.id_url
        left join trail_img as tm on tm.id_movie = mm.idmovies
        left join site as ss on ss.idsite = uu.id_site
        left join rating as rr on rr.idrating = mm.idmovies
        join movie_genre as mg on mg.id_movie = mm.idmovies
        join genre as gg on gg.idgenre = mg.id_genre
        join movie_lang as ml on ml.id_movie = mm.idmovies
        join language as ll on ll.idlanguage = ml.id_lang
        where gg.genre like '{}%%' and ll.lang like 'Hindi%%'
        GROUP BY (mm.idmovies)
        ORDER BY rr.id_rate Desc
        limit 100
        ;'''
    
    query_fav = '''Select mm.idmovies, mm.movie, tm.id_img, tm.id_trail, group_concat(uu.url), group_concat(ss.sitename)
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
        where mm.idmovies in (2358, 6062, 293, 326, 848, 469, 905, 8749, 1166, 4162)
        GROUP BY (mm.idmovies)
        ORDER BY rr.id_rate Desc
        ;'''
    
    connection=db_starter()
    categories = ['comedy', 'animation', 'action', 'adventure', 'horror']
    
    main_data = {}
    randomlist = random.sample(range(1, 50), 10)
    
    for category in categories:
        temp_int = 0
        query_cat = query.format(category)
        data = []
        result = connection.execute(query_cat)

        for row in result:
            temp_int = temp_int + 1
            if temp_int not in randomlist:
                continue
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
        
        main_data[category] = data
    
    result_fav = connection.execute(query_fav)
    data = []

    for row in result_fav:
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
    
    main_data['flickhub_fav'] = data
    
    return {'data': main_data}


def search_movies(val, page):
    connection=db_starter()
    query = '''Select mm.idmovies, mm.movie, tm.id_img, tm.id_trail, group_concat(uu.url), group_concat(ss.sitename), group_concat(gg.genre)
            from movies as mm 
            left join movie_url as mu on mu.id_movie = mm.idmovies
            left join url as uu on uu.idurl = mu.id_url
            left join trail_img as tm on tm.id_movie = mm.idmovies
            left join site as ss on ss.idsite = uu.id_site
            left join movie_genre as mg on mg.id_movie = mm.idmovies
            left join genre as gg on gg.idgenre = mg.id_genre
            where mm.movie like '%%{}%%'
            GROUP BY (mm.idmovies);'''.format(val)

    data = []
    result = connection.execute(query)

    genre_list = []

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
        try:
            genre_list.extend(row[6].split(','))
        except:
            pass
        data.append(temp_dict)
    
    genres = []

    while(genre_list != []):
        genres.append(most_frequent(genre_list))
        genre_list = list(filter((most_frequent(genre_list)).__ne__, genre_list))
        if len(genres) == 3:
            break

    
    if genres == []:
        genres = ['action', 'comedy', 'adventure']

    similar_titles = get_similar_titles(genres, page, False)
    connection.close()
    
    return {'data': data, 'similar': similar_titles}


def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist" 
   
    
    
    