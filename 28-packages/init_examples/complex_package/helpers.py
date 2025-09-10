
# 辅助函数模块
def helper_function(data):
    """辅助函数"""
    if isinstance(data, str):
        return data.strip().title()
    elif isinstance(data, (list, tuple)):
        return len(data)
    else:
        return str(data)
