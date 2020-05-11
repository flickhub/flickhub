from flask import Flask, render_template,request,redirect, url_for
from db_initiate import see
app = Flask(__name__)    
@app.route("/home",methods=["GET","POST"])
def home():
    return render_template('index2.html')  
@app.route("/submit",methods=["GET","POST"])
def submit():
        mvname=request.form["mv_name"]
        if(mvname!=""):
            print(mvname)
            m="%"+mvname+"%"
            #db search
            url_name3,img3,l,name3,genre3=see(m)
            return render_template('index1.html',u=url_name3,ie=img3,le=l,nam=name3,g=genre3)    
        else:
            return redirect(url_for('home'))
        mvname=request.form["mv_name1"]
        if(mvname!=""):
            print(mvname)
            m="%"+mvname+"%"
            #db search
            url_name3,img3,l,name3,genre3=see(m)
            return redirect('index1.html',u=url_name3,ie=img3,le=l,nam=name3,g=genre3)    
        else:
            return redirect(url_for('home'))
        
app.run(debug=True)





