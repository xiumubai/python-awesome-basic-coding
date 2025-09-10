"""辅助工具模块"""

# 相对导入同级模块
from .formatter import format_text

def show_info():
    """显示信息"""
    info = "这是来自helper模块的信息"
    print(format_text(info, "INFO"))

def calculate(a, b):
    """简单计算"""
    return a + b
