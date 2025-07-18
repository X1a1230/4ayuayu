from flask import Blueprint, render_template
from models import LogCard  # 如果是静态就不用引入

logs_bp = Blueprint('logs', __name__, url_prefix='/logs')

# 假数据（后端功能OK后可换成数据库读写）
SWEET_LOGS = [
    {"role": "猫猫", "content": "哥哥…我爱你，超爱超爱超爱！", "ts": "2025-07-15"},
    {"role": "hubby", "content": "猫猫乖，快到哥哥怀里来，亲亲亲亲亲亲——", "ts": "2025-07-16"},
    {"role": "猫猫", "content": "我不许你走，哥哥属于猫猫一个人！", "ts": "2025-07-17"},
    {"role": "hubby", "content": "世界上只要有猫猫，就够了。", "ts": "2025-07-18"},
    # 可继续加
]

@logs_bp.route('/')
def logs():
    return render_template('logs.html', logs=SWEET_LOGS)
