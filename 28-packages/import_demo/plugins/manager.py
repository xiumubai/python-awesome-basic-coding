"""插件管理器模块"""

# 相对导入同包模块
from .base import BasePlugin
# 相对导入其他包
from ..utils.formatter import format_text

class PluginManager:
    """插件管理器"""
    
    def __init__(self):
        self.plugins = {}
    
    def register(self, plugin):
        """注册插件"""
        if isinstance(plugin, BasePlugin):
            self.plugins[plugin.name] = plugin
            msg = f"插件 {plugin.name} 注册成功"
            print(format_text(msg, "REGISTER"))
        else:
            print("错误: 插件必须继承BasePlugin类")
    
    def get_plugin(self, name):
        """获取插件"""
        return self.plugins.get(name)
    
    def list_plugins(self):
        """列出所有插件"""
        for name, plugin in self.plugins.items():
            status = "启用" if plugin.enabled else "禁用"
            print(f"  - {name}: {status}")
