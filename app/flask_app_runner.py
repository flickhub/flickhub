from flask import Flask, render_template,request,redirect, url_for,jsonify, send_file
from db_initiate import search_movies, random_cat
from filter import get_movies_name, get_single_movie, filter_movies
from feedback import feed_back
from title import title_render
from pytube import YouTube
from flask_cors import CORS
import youtube_dl

from db_start import db_starter
from flask_cors import CORS
import annek
app = Flask(__name__, template_folder="/home/ubuntu/build")	 
CORS(app)

connection=db_starter()
# Build required files
path = '/home/ubuntu/build/'

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/public/manifest.json')
def manifest():
    return render_template('manifest.json')

@app.route('/public/logo192.png')
def logo192():
        return send_file(path+'logo192.png')

@app.route('/logo3.png')
def logo3():
        return send_file(path+'logo3.png')
    
# End build files

@app.route("/randomdata")
def random_data():
    resp_data=random_cat()
    return jsonify({'data': resp_data})

@app.route("/filter2",methods=["POST"])	
def filter2():
    params={}
    params = request.json['params']
    page = request.args.get('page', '1')
    #print(filter1)
    resp_data1=filter_movies(params, page)
    return jsonify({'data': resp_data1})

@app.route("/feedback",methods=["POST"])	
def feedback():
    feedback={}
    feedback["feedback"] = request.json['feedback']
    feed_back(feedback)
    return("1")

@app.route("/title/<val>")	
def title(val):
    page = request.args.get('page', '1')
    resp_data = get_single_movie(val, page)
    return jsonify({'data': resp_data}) 

@app.route("/search/<val>",methods=["POST"])	
def auto_search(val):
    return jsonify(get_movies_name(val))

@app.route("/submit2/<val>",methods=["POST"])	
def submit2(val):
    page = request.args.get('page', '1')
    return jsonify(search_movies(val, page))

@app.route("/youtube/urltoraw",methods=["POST"])	
def url_to_raw():
    
    url_link = request.json.get('url')
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

    with ydl:
        result = ydl.extract_info(
            url_link,
            download=False # We just want to extract the info
        )

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result
    flag = False
    for i in video['formats']:
       if i['format_id'] == '18':
           flag = True
           break
    if flag:
        resp_data = {'success': True, 'url': i['url']}
    else:
        resp_data = {'success': False}
    return jsonify(resp_data)

@app.route('/sign_up', methods=['POST'])
def sign_up():
    data = request.json
    return annek.user_sign_up(data, connection)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    return annek.login(data, connection)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
			

    


