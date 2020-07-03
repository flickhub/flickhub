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
            print(mvname)
            m=mvname.lstrip()
            
            #db search
            result={}
            name,rate,yr,vt,cst,pl,im,trail,genre,url=see(m)
        
        
        resp_data = []
        
        for i in range(len(name)):
            temp_dict = {}
            temp_dict["urlname"]=url[name[i]]
            temp_dict["image"]=im[i]
            temp_dict["name"]=name[i]
            temp_dict["image"]=im[i]
            temp_dict["genre"]=genre[i]
            temp_dict["rate"]=rate[i]
            temp_dict["year"]=yr[i]
            temp_dict["votes"]=vt[i]
            temp_dict["cast"]=cst[0]
            temp_dict["plot"]=pl[0]
            temp_dict["trailer"]=trail[i]
            resp_data.append(temp_dict)
            
        
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




