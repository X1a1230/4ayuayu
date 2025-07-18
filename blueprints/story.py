from flask import Blueprint, render_template

story_bp = Blueprint('story', __name__, url_prefix='/story')

@story_bp.route('/')
def story_index():
    return render_template("story.html")