
"""插件管理器模块"""

from typing import Dict, List, Optional, Any
from .base import BasePlugin, PluginInfo
from .loader import PluginLoader
from .registry import PluginRegistry

class PluginError(Exception):
    """插件异常"""
    pass

class PluginManager:
    """插件管理器"""
    
    def __init__(self, plugin_dir: str = "plugins"):
        self.plugin_dir = plugin_dir
        self.loader = PluginLoader()
        self.registry = PluginRegistry()
        self.loaded_plugins: Dict[str, BasePlugin] = {}
        self.enabled_plugins: Dict[str, BasePlugin] = {}
        
        print(f"插件管理器初始化完成，插件目录: {plugin_dir}")
    
    def load_plugin(self, plugin_name: str) -> bool:
        """加载插件"""
        try:
            if plugin_name in self.loaded_plugins:
                print(f"插件 {plugin_name} 已经加载")
                return True
            
            plugin = self.loader.load_plugin(plugin_name, self.plugin_dir)
            if plugin:
                self.loaded_plugins[plugin_name] = plugin
                self.registry.register_plugin(plugin.get_info())
                print(f"插件 {plugin_name} 加载成功")
                return True
            
            return False
            
        except Exception as e:
            raise PluginError(f"加载插件 {plugin_name} 失败: {e}")
    
    def unload_plugin(self, plugin_name: str) -> bool:
        """卸载插件"""
        try:
            if plugin_name not in self.loaded_plugins:
                print(f"插件 {plugin_name} 未加载")
                return False
            
            # 先禁用插件
            self.disable_plugin(plugin_name)
            
            # 卸载插件
            plugin = self.loaded_plugins.pop(plugin_name)
            self.registry.unregister_plugin(plugin_name)
            
            # 调用插件的清理方法
            if hasattr(plugin, 'cleanup'):
                plugin.cleanup()
            
            print(f"插件 {plugin_name} 卸载成功")
            return True
            
        except Exception as e:
            raise PluginError(f"卸载插件 {plugin_name} 失败: {e}")
    
    def enable_plugin(self, plugin_name: str) -> bool:
        """启用插件"""
        try:
            if plugin_name not in self.loaded_plugins:
                print(f"插件 {plugin_name} 未加载，无法启用")
                return False
            
            if plugin_name in self.enabled_plugins:
                print(f"插件 {plugin_name} 已经启用")
                return True
            
            plugin = self.loaded_plugins[plugin_name]
            plugin.enable()
            self.enabled_plugins[plugin_name] = plugin
            
            print(f"插件 {plugin_name} 启用成功")
            return True
            
        except Exception as e:
            raise PluginError(f"启用插件 {plugin_name} 失败: {e}")
    
    def disable_plugin(self, plugin_name: str) -> bool:
        """禁用插件"""
        try:
            if plugin_name not in self.enabled_plugins:
                print(f"插件 {plugin_name} 未启用")
                return False
            
            plugin = self.enabled_plugins.pop(plugin_name)
            plugin.disable()
            
            print(f"插件 {plugin_name} 禁用成功")
            return True
            
        except Exception as e:
            raise PluginError(f"禁用插件 {plugin_name} 失败: {e}")
    
    def get_loaded_plugins(self) -> List[str]:
        """获取已加载的插件列表"""
        return list(self.loaded_plugins.keys())
    
    def get_enabled_plugins(self) -> List[str]:
        """获取已启用的插件列表"""
        return list(self.enabled_plugins.keys())
    
    def get_plugin_info(self, plugin_name: str) -> Optional[PluginInfo]:
        """获取插件信息"""
        return self.registry.get_plugin_info(plugin_name)
    
    def call_plugin_method(self, plugin_name: str, method_name: str, *args, **kwargs) -> Any:
        """调用插件方法"""
        if plugin_name not in self.enabled_plugins:
            raise PluginError(f"插件 {plugin_name} 未启用")
        
        plugin = self.enabled_plugins[plugin_name]
        if not hasattr(plugin, method_name):
            raise PluginError(f"插件 {plugin_name} 没有方法 {method_name}")
        
        method = getattr(plugin, method_name)
        return method(*args, **kwargs)
    
    def get_status(self) -> Dict[str, Any]:
        """获取插件管理器状态"""
        return {
            'plugin_dir': self.plugin_dir,
            'loaded_count': len(self.loaded_plugins),
            'enabled_count': len(self.enabled_plugins),
            'loaded_plugins': list(self.loaded_plugins.keys()),
            'enabled_plugins': list(self.enabled_plugins.keys())
        }
