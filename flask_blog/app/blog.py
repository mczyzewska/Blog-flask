from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute('SELECT * FROM post').fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        author_id = session['user_id']
        db = get_db()
        db.execute(
            'INSERT INTO post (author_id, title, body) VALUES (?, ?, ?)',
            (author_id, title, body)
        )
        db.commit()
        flash('Post successfully created!')
        return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
