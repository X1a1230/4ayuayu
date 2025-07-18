import json
import os

with open("chat.json", encoding="utf-8") as f:
    data = json.load(f)

os.makedirs("splits", exist_ok=True)
for idx, conv in enumerate(data):
    filename = f"splits/conv_{idx+1:03d}_{conv.get('title','untitled')[:20].replace(' ', '_')}.json"
    with open(filename, "w", encoding="utf-8") as wf:
        # 注意：OpenAI每个会话也是个list（所以加[]包起来）
        json.dump([conv], wf, ensure_ascii=False, indent=2)
print(f"一共拆分为 {len(data)} 个小json，保存在splits/文件夹！")
