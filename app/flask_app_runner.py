from flask import Flask, render_template,request,redirect, url_for,jsonify
from db_initiate import see
from filter import filter_fr_all
from feedback import feed_back

app = Flask(__name__)	 

def run():
    
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
        
        

    app.run(debug=True,host='0.0.0.0')
    
run()			




