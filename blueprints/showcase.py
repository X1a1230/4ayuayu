from flask import Blueprint, render_template

showcase_bp = Blueprint('showcase', __name__, url_prefix='/showcase')

@showcase_bp.route('/')
def showcase_index():
    return render_template("showcase.html")