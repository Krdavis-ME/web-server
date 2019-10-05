

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world(username= None, post_id = None):
    return render_template('index.html', name=username, post_id = post_id)

@app.route('/blog')
def blog_page():
    return 'This is my thoughts on blogs'

@app.route('/blog/2020/dogs')
def blog_pag2e():
    return 'This is about my dog'