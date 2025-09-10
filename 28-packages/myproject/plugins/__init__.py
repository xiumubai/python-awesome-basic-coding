
"""Plugins子包 - 插件系统模块"""

print("正在初始化Plugins子包")

# 从模块导入主要功能
from .manager import PluginManager, PluginError
from .loader import PluginLoader, load_plugin
from .registry import PluginRegistry, register_plugin
from .base import BasePlugin, PluginInfo

# 公共接口
__all__ = [
    'PluginManager',
    'PluginError',
    'PluginLoader',
    'load_plugin',
    'PluginRegistry',
    'register_plugin',
    'BasePlugin',
    'PluginInfo'
]

# 插件系统配置
PLUGIN_CONFIG = {
    'plugin_dir': 'plugins',
    'auto_load': True,
    'max_plugins': 50
}
