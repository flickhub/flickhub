from flask import Flask, render_template,request,redirect, url_for,jsonify
from db_initiate import see
app = Flask(__name__)	 

@app.route("/submit",methods=["POST"])
def submit():
	count=0
	mvname = request.form.get('mv_name')
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
		# result["Urlname"]=url_name3
		# result["Image"]=img3
		# result["Name"]=name3
		# result["Image"]=im3
		# result["Genre"]=gen3
		# result["Rate"]=rate3
		# result["Year"]=yr3
		# result["Votes"]=vt3
		# result["Cast"]=cst3
		# result["Plot"]=pl3
	
	resp_data = []
	for i in range(len(url_name3)):
		temp_dict = {}
		temp_dict["urlname"]=url_name3[i]
		temp_dict["image"]=img3[i]
		temp_dict["name"]=name3[i]
		temp_dict["image"]=im3[i]
		temp_dict["genre"]=gen3[i]
		temp_dict["rate"]=rate3[i]
		temp_dict["year"]=yr3[i]
		temp_dict["votes"]=vt3[i]
		temp_dict["cast"]=cst3[i]
		temp_dict["plot"]=pl3[i]
		resp_data.append(temp_dict)
		
			
	return jsonify({'data': resp_data})
			
app.run(debug=True,host='0.0.0.0')




