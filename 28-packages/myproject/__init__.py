
"""MyProject - 演示复杂包结构的项目"""

print("正在初始化MyProject主包")

# 包信息
__version__ = "1.0.0"
__author__ = "Python学习者"
__description__ = "演示子包管理的示例项目"

# 从子包导入主要功能
from .core import Engine, get_system_info
from .ui import create_main_window, show_dialog
from .plugins import PluginManager

# 定义公共接口
__all__ = [
    'Engine',
    'get_system_info',
    'create_main_window',
    'show_dialog',
    'PluginManager',
    'get_project_info'
]

def get_project_info():
    """获取项目信息"""
    return {
        'name': 'MyProject',
        'version': __version__,
        'author': __author__,
        'description': __description__
    }

# 包级别配置
class Config:
    """项目配置"""
    DEBUG = True
    LOG_LEVEL = 'INFO'
    MAX_PLUGINS = 10
    
    @classmethod
    def get_config(cls):
        return {
            'debug': cls.DEBUG,
            'log_level': cls.LOG_LEVEL,
            'max_plugins': cls.MAX_PLUGINS
        }
