from flask import Flask, render_template,request,redirect, url_for,jsonify
from db_initiate import see
from db_initiate import random1
from filter import filter_fr_all
from feedback import feed_back
from title import title_render
app = Flask(__name__)	 

@app.route("/",methods=["POST"])
def land_page():
    resp_data0=random1()
    
    return jsonify({'data': resp_data0})
@app.route("/submit",methods=["POST"])
def submit():
    count=0
    mvname = request.json['mv_name']
    for i in mvname:
        if(i==' '):
            count=count+1
    l=len(mvname)		 
    if(mvname!="" and l!=count):
        m=mvname.lstrip()
        print(m)
        #db search
        result={}
        resp_data=see(m)
        
        return jsonify({'data': resp_data})
@app.route("/filter",methods=["POST"])	
def filter():
    filter1={}
    filter1["filters"] = request.json['filters']
    print(filter1)
    resp_data1=filter_fr_all(filter1)
        
    
    return jsonify({'data': resp_data1})

@app.route("/feedback",methods=["POST"])	
def feedback():
    feedback={}
    feedback["feedback"] = request.json['feedback']
    feed_back(feedback)
    
    return("1")    
@app.route("/title/<id_mov1>",methods=["POST"])	
def title(id_mov1):
    resp_data=title_render(id_mov1)
    return jsonify({'data': resp_data})  
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
			

    


