from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import cgi
import os
#where do i put the autoescape if not using jinja

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:beproductive@localhost:8889/build-a-blog'

app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Blogs(db.Model):

    id = db.Column(db.Integer, primary_key=True)
     id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(120))
    blog_content = db.Column(db.Boolean)
    

    def __init__(self, name):
        self.name = name


blog_posts = []

@app.route('/', methods=['POST', 'GET'])
def index():

    
    return render_template('base.html', title=title)

@app.route('/', methods=['POST', 'GET'])
def add_post():
    # look inside the request to figure out what the user typed
    new_blog_post = request.form['blog_post_title']

    # if the user typed nothing at all, redirect and tell them the error
    if (not new_blog_post) or (not blog_post_content):
        error = "Please specify the blog post you want to add."
        return redirect("/?error=" + error)

    blog_post = blog_posts(new_blog_post)
    db.session.add(new_blog_post)
    db.session.commit()
    return render_template('index.html', new_blog_post=new_blog_post)

if __name__ == '__main__':
    app.run()