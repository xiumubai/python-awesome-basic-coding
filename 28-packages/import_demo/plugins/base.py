"""基础插件模块"""

# 相对导入核心功能
from ..core import Engine
from ..utils import helper

class BasePlugin:
    """基础插件类"""
    
    def __init__(self, name):
        self.name = name
        self.enabled = False
    
    def enable(self):
        """启用插件"""
        self.enabled = True
        print(f"插件 {self.name} 已启用")
        helper.show_info()
    
    def disable(self):
        """禁用插件"""
        self.enabled = False
        print(f"插件 {self.name} 已禁用")
