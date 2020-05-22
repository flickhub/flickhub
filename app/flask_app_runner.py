from flask import Flask, render_template,request,redirect, url_for
from db_initiate import see
app = Flask(__name__)    
@app.route("/",methods=["GET","POST"])
def home():
    return render_template('index.html')  
@app.route("/submit",methods=["GET","POST"])
def submit():
        count=0
        mvname=request.form["mv_name"]
        for i in mvname:
            if(i==' '):
                count=count+1
        l=len(mvname)        
        if(mvname!="" and l!=count):
            print(mvname)
            m=mvname.lstrip()
            
            #db search
            url_name3,img3,l,name3,genre3=see(m)
            if(len(name3)!=0):
                return render_template('index1.html',u=url_name3,ie=img3,le=l,nam=name3,g=genre3,nam1=m)    
            else:
                return render_template('blank1.html',nam1=m)
        else:
            return render_template('blank1.html')
@app.route("/about")
def about():
    return render_template('about.html')  
@app.route("/contact")
def contact():
    return render_template('contact.html')


app.run(debug=True)




