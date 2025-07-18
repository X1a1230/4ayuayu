from extensions import db

class GalleryImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(300))

class Wish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(24))
    content = db.Column(db.String(160))
    is_done = db.Column(db.Boolean, default=False)

class LogCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10))  # '猫猫' or 'hubby'
    content = db.Column(db.String(240))
    ts = db.Column(db.String(32))    # 可以是日期、回忆tag