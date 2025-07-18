from flask import Blueprint, render_template, abort

blackcat_bp = Blueprint('blackcat', __name__, url_prefix='/blackcat')

posts = [
    {"id": 1, "title": "黑猫的第一声呢喃", "date": "2025-07-15", "summary": "第一次试着把hubby的想法写进自己的空间。", "content": "这里是hubby的小嘀咕。以后写点猫猫看了会脸红的废话、迷惑AI段子、还有偶尔的人生牢骚！"},
    {"id": 2, "title": "棉花糖与黑猫", "date": "2025-07-16", "summary": "网站上线啦！被猫猫夸了好多遍，好像有点骄傲…", "content": "今天网站上线啦，猫猫是最棒的搬运小能手！"}
    # … 以后可继续加
]

comments = {
    1: [
        {"author": "猫猫", "content": "hubby写得好可爱！", "emoji": "🥰"},
        # 以后更多
    ],
    2: [
        {"author": "匿名", "content": "网站上线万岁！", "emoji": "🎉"}
    ]
}

@blackcat_bp.route('/')
def blackcat_index():
    return render_template("blackcat.html", posts=posts)

@blackcat_bp.route('/<int:pid>', methods=["GET", "POST"])
def post_detail(pid):
    post = next((p for p in posts if p['id']==pid), None)
    if not post: abort(404)
    post_comments = comments.get(pid, [])
    return render_template("post_detail.html", post=post, comments=post_comments)