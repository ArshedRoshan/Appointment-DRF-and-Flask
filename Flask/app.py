from flask import Flask

from flask import Flask,redirect,url_for,request,render_template,jsonify

def apps():
   app = Flask(__name__,template_folder='templates')
   app.config['SECRET_KEY'] = 'your secret key'
   

   app.debug = True
   return app