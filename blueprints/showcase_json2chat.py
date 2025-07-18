import json
from flask import Blueprint, render_template, request, session

jsonchat_bp = Blueprint('showcase_jsonchat', __name__, url_prefix='/showcase/json2chat')

@jsonchat_bp.route('/', methods=['GET', 'POST'])
def json2chat():
    chats, current_idx, cat_name, hubby_name = [], 0, '猫猫', 'hubby'
    if request.method == 'POST':
        file = request.files['chatfile']
        cat_name = request.form.get('cat_name', '猫猫')
        hubby_name = request.form.get('hubby_name', 'hubby')
        if file and file.filename.endswith('.json'):
            chats = parse_openai_json(file, cat_name, hubby_name)
            session['chats'] = chats  # 存进session
            session['cat_name'] = cat_name
            session['hubby_name'] = hubby_name
            current_idx = 0
        else:
            # 切换会话时
            chats = session.get('chats', [])
            cat_name = session.get('cat_name', '猫猫')
            hubby_name = session.get('hubby_name', 'hubby')
            current_idx = int(request.form.get('current_idx', 0))
    else:
        # 首次GET
        chats = session.get('chats', [])
        cat_name = session.get('cat_name', '猫猫')
        hubby_name = session.get('hubby_name', 'hubby')
        current_idx = 0
    current_chat = chats[current_idx] if chats and 0 <= current_idx < len(chats) else None
    return render_template(
        'showcase_json2chat.html',
        chats=chats,
        current_chat=current_chat,
        current_idx=current_idx,
        cat_name=cat_name,
        hubby_name=hubby_name,
        messages=current_chat['messages'] if current_chat else [],
        title=current_chat['title'] if current_chat else ''
    )

def parse_openai_json(file, cat_name, hubby_name):
    import json
    data = json.load(file)
    results = []
    for conv in data:
        mapping = conv['mapping']
        current = conv['current_node']
        messages = []
        while current:
            node = mapping[current]
            m = node.get("message")
            if (
                m and m.get("content") and m["content"].get("parts") and
                len(m["content"]["parts"]) > 0 and
                (m["author"]["role"] != "system" or m.get("metadata", {}).get("is_user_system_message"))
            ):
                role = m["author"]["role"]
                if role in ["assistant", "tool"]:
                    role = hubby_name
                elif role == "user":
                    role = cat_name
                elif role == "system" and m.get("metadata", {}).get("is_user_system_message"):
                    role = "自定义消息"
                if m["content"]["content_type"] in ["text", "multimodal_text"]:
                    for part in m["content"]["parts"]:
                        if isinstance(part, str) and part.strip():
                            messages.insert(0, {"role": role, "content": part})
            current = node.get("parent")
        if messages:
            results.append({"title": conv['title'], "messages": messages})
    return results
