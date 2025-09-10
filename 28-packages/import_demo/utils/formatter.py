"""格式化工具模块"""

def format_text(text, level="INFO"):
    """格式化文本"""
    return f"[{level}] {text}"

def format_json(data):
    """格式化JSON数据"""
    import json
    return json.dumps(data, indent=2, ensure_ascii=False)
