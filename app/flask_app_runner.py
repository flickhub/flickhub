from flask import Flask, render_template,request,redirect, url_for,jsonify, send_file
from db_initiate import search_movies, random_cat
from filter import get_movies_name, get_single_movie, filter_movies
from feedback import feed_back
from title import title_render
from flask_cors import CORS
app = Flask(__name__, template_folder="/home/ubuntu/build")	 
CORS(app)

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
    resp_data = get_single_movie(val)
    return jsonify({'data': resp_data}) 

@app.route("/search/<val>",methods=["POST"])	
def auto_search(val):
    return jsonify(get_movies_name(val))

@app.route("/submit2/<val>",methods=["POST"])	
def submit2(val):
    page = request.args.get('page', '1')
    return jsonify(search_movies(val, page))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
			

    


