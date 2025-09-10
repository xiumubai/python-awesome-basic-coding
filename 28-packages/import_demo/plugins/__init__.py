"""插件包"""
print("正在初始化plugins包")

# 相对导入插件模块
from .base import BasePlugin
from .manager import PluginManager

__all__ = ["BasePlugin", "PluginManager"]
