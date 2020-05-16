from flask import Flask, render_template,request,redirect, url_for
from db_initiate import see
app = Flask(__name__)    
@app.route("/",methods=["GET","POST"])
def home():
    return render_template('index.html')  
@app.route("/submit",methods=["GET","POST"])
def submit():
        mvname=request.form["mv_name"]
        if(mvname!=""):
            print(mvname)
            m=mvname
            
            #db search
            url_name3,img3,l,name3,genre3=see(m)
            return render_template('index1.html',u=url_name3,ie=img3,le=l,nam=name3,g=genre3,nam1=m)    
        else:
            return render_template('blank1.html')
@app.route("/about")
def about():
    return render_template('about.html')  
@app.route("/contact")
def contact():
    return render_template('contact.html')
<<<<<<< Updated upstream


app.run(debug=True)
=======
@app.route("/tos")
def tos():
    return render_template('tos.html')       
@app.route("/pp")
def pp():
    return render_template('pp.html')

if __name__ == "__main__":
	app.run(debug=True)
>>>>>>> Stashed changes




