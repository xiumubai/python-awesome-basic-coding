
"""Widgets子包 - UI控件模块"""

print("正在初始化Widgets子包")

# 从模块导入控件类
from .basic import Button, Label, TextBox
from .advanced import ListView, TreeView, TabControl

# 公共接口
__all__ = [
    'Button',
    'Label', 
    'TextBox',
    'ListView',
    'TreeView',
    'TabControl'
]

# 控件配置
WIDGET_CONFIG = {
    'default_font': 'Arial',
    'default_size': 12,
    'theme': 'default'
}
