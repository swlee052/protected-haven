from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///protected_haven'
app.config['SQLALCHEMY-TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = 'whateveryouwant'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home():


@app.route('/action/<lang>')
def action(lang): 



@app.route('/report/<lang>')
def report(lang): 



@app.route('/confirmation/<lang>')
def confirmation(lang): 



@app.route('/error/<lang>')
def error(lang):



@app.route('/admin')
def admin():

 