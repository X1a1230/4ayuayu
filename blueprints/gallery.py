import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from werkzeug.utils import secure_filename
from extensions import db
from models import GalleryImage

gallery_bp = Blueprint('gallery', __name__, url_prefix='/gallery')

@gallery_bp.route('/', methods=['GET', 'POST'])
def gallery_index():
    if request.method == 'POST':
        file = request.files['image']
        if file and file.filename:
            filename = secure_filename(file.filename)
            save_path = os.path.join(current_app.root_path, 'static/img', filename)
            file.save(save_path)
            title = request.form.get('title', '')
            desc = request.form.get('desc', '')
            new_img = GalleryImage(filename=filename, title=title, desc=desc)
            db.session.add(new_img)
            db.session.commit()
            return redirect(url_for('gallery.gallery_index'))
    images = GalleryImage.query.all()
    return render_template("gallery.html", images=images)
