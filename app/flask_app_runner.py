from flask import Flask, render_template,request,redirect, url_for,jsonify
from db_initiate import see
app = Flask(__name__)	 

@app.route("/submit/<mvname>",methods=["POST","GET"])
def submit(mvname):
		count=0
		
            
		if (request.method == 'GET'): 
			
			for i in mvname:
				if(i==' '):
					count=count+1
			l=len(mvname)		 
			if(mvname!="" and l!=count):
				print(mvname)
				m=mvname.lstrip()
				
				#db search
				result={}
				url_name3,img3,l,name3,genre3,im3,rate3,yr3,vt3,gen3,cst3,pl3=see(m)
				result["Urlname"]=url_name3
				result["Image"]=img3
				result["Name"]=name3
				result["Image"]=im3
				result["Genre"]=gen3
				result["Rate"]=rate3
				result["Year"]=yr3
				result["Votes"]=vt3
				result["Cast"]=cst3
				result["Plot"]=pl3
				
					
				return jsonify(result)
			
app.run(debug=True,host='0.0.0.0')




