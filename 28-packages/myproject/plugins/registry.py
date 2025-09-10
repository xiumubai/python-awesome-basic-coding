
"""插件注册表模块"""

from typing import Dict, List, Optional
from .base import PluginInfo

class PluginRegistry:
    """插件注册表"""
    
    def __init__(self):
        self.plugins: Dict[str, PluginInfo] = {}
    
    def register_plugin(self, plugin_info: PluginInfo):
        """注册插件"""
        self.plugins[plugin_info.name] = plugin_info
        print(f"插件 {plugin_info.name} 已注册")
    
    def unregister_plugin(self, plugin_name: str):
        """注销插件"""
        if plugin_name in self.plugins:
            del self.plugins[plugin_name]
            print(f"插件 {plugin_name} 已注销")
    
    def get_plugin_info(self, plugin_name: str) -> Optional[PluginInfo]:
        """获取插件信息"""
        return self.plugins.get(plugin_name)
    
    def get_all_plugins(self) -> List[PluginInfo]:
        """获取所有插件信息"""
        return list(self.plugins.values())
    
    def find_plugins_by_author(self, author: str) -> List[PluginInfo]:
        """根据作者查找插件"""
        return [info for info in self.plugins.values() if info.author == author]

def register_plugin(plugin_info: PluginInfo):
    """注册插件的便捷函数"""
    # 这里应该使用全局注册表实例
    print(f"注册插件: {plugin_info.name}")
