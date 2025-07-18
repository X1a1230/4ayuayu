from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models import Wish

wish_tree_bp = Blueprint('wish_tree', __name__, url_prefix='/wish_tree')

@wish_tree_bp.route('/', methods=['GET', 'POST'])
def wish_tree():
    if request.method == 'POST':
        content = request.form.get('content')
        author = request.form.get('author')
        if content:
            wish = Wish(author=author or '匿名', content=content, is_done=False)
            db.session.add(wish)
            db.session.commit()
            return redirect(url_for('wish_tree.wish_tree'))
    wishes = Wish.query.all()
    return render_template('wish_tree.html', wishes=wishes)


@wish_tree_bp.route('/done/<int:wish_id>')
def wish_done(wish_id):
    wish = Wish.query.get(wish_id)
    if wish:
        wish.is_done = True
        db.session.commit()
    return redirect(url_for('wish_tree.wish_tree'))
