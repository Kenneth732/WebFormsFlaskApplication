from pyexpat.errors import messages
from flask import Flask, render_template, request, url_for, flash, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd96eeaee39a7aaf82d02dc9e3dc10407b2d9b97883b5c8b5'

message = [
    {
        "title": "MessageOne", "content": 'MessageOne Content'
    },{
        "title": "MessageTwo", "content": 'MessageTwo Content'
    }
]
app.route('/')
def index():
        return render_template('index.html', messages=messages)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')