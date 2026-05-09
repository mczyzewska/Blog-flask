from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
def dashboard():
    db = get_db()
    users = db.execute('SELECT id, username, is_admin FROM user').fetchall()
    posts = db.execute('SELECT id, title FROM post').fetchall()
    return render_template('admin/dashboard.html', users=users, posts=posts)

@bp.route('/delete_user/<int:user_id>', methods=('POST',))
def delete_user(user_id):
    db = get_db()
    db.execute('DELETE FROM user WHERE id = ?', (user_id,))
    db.commit()
    flash(f'User with ID {user_id} deleted successfully.')
    return redirect(url_for('admin.dashboard'))

@bp.route('/delete_post/<int:post_id>', methods=('POST',))
def delete_post(post_id):
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (post_id,))
    db.commit()
    flash(f'Post with ID {post_id} deleted successfully.')
    return redirect(url_for('admin.dashboard'))
