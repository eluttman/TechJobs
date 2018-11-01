from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:launchcode@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.String(1200))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def is_valid(self):
        if self.title and self.content:
            return True
        else:
            return False
    
    

@app.route('/blogs', methods=['POST', 'GET'])
def blog():

    blog_id = request.args.get('id')

    if blog_id:
        blog = Blog.query.get(blog_id)
        return render_template('new_post_display.html', blog=blog)
    else:
        blog = Blog.query.all()
        return render_template('blog.html', blogs=blog)
@app.route('/', methods=['POST', 'GET'])
def index():
    # look inside the request to figure out what the user typed

    blog_posts = Blog.query.all()

    
    return render_template('blog.html', blogs=blog_posts, title='List O-Blogs')
   


@app.route('/addpost', methods=['POST', 'GET'])
def add_post():

    # blog_posts = Blog.query.all()
    if request.method == 'POST':
        title = request.form['post_title']
        content = request.form['post_content']
        new_blog_post = Blog(title, content)
        if new_blog_post.is_valid():
            db.session.add(new_blog_post)
            db.session.commit()
        # return render_template('add_blog_post.html')
            return redirect('/blogs?id=' + str(new_blog_post.id))
    else:
        return render_template('add_blog_post.html')

    def Determine_title_error(post_title):
        if title == '':
            return True
        else:
            return False
    def Determine_content_error(content):
        if post_content == '':
            return True
        else:
            return False
    
    title_error = Determine_title_error(title)
    content_error = Determine_content_error

    if content_error or title_error:
        return render_template('add_blog_post.html', title=title, content=content, title_error=title_error, content_error=content_error)

if __name__ == '__main__':
    app.run()
