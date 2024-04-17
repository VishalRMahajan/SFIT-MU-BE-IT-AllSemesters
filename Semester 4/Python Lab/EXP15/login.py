from flask import *  
app = Flask(__name__)  
  
@app.route('/login',methods = ['Post'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="Vishal" and passwrd=="Mahajan":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)  
