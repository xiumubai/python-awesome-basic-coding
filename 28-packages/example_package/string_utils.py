
# 字符串工具模块
def reverse_string(s):
    """反转字符串"""
    return s[::-1]

def capitalize_words(s):
    """首字母大写"""
    return ' '.join(word.capitalize() for word in s.split())

def count_words(s):
    """统计单词数量"""
    return len(s.split())
