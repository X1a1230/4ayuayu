from flask import Flask, render_template
from blueprints import blueprint_list
from extensions import db

def create_app():
    app = Flask(__name__)
    app.secret_key = 'catcat_x_hubby_secret_2025'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)
    # 注册所有蓝图
    for bp in blueprint_list:
        app.register_blueprint(bp)
    return app

app = create_app()

# 首页
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5002)
