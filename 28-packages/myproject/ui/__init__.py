
"""UI子包 - 用户界面模块"""

print("正在初始化UI子包")

# 从模块导入主要功能
from .main_window import create_main_window, MainWindow
from .dialogs import show_dialog, MessageDialog, InputDialog
from .widgets import Button, Label, TextBox

# 子包版本
__version__ = "1.0.0"

# 公共接口
__all__ = [
    'create_main_window',
    'MainWindow',
    'show_dialog',
    'MessageDialog',
    'InputDialog',
    'Button',
    'Label',
    'TextBox'
]

# UI配置
UI_CONFIG = {
    'theme': 'default',
    'window_size': (800, 600),
    'font_size': 12
}
