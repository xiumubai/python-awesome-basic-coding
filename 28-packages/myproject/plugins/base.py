
"""插件基类模块"""

from abc import ABC, abstractmethod
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class PluginInfo:
    """插件信息"""
    name: str
    version: str
    description: str
    author: str
    dependencies: list = None
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []

class BasePlugin(ABC):
    """插件基类"""
    
    def __init__(self):
        self.enabled = False
        self.initialized = False
    
    @abstractmethod
    def get_info(self) -> PluginInfo:
        """获取插件信息"""
        pass
    
    @abstractmethod
    def initialize(self) -> bool:
        """初始化插件"""
        pass
    
    def enable(self) -> bool:
        """启用插件"""
        if not self.initialized:
            if not self.initialize():
                return False
            self.initialized = True
        
        self.enabled = True
        self.on_enable()
        return True
    
    def disable(self) -> bool:
        """禁用插件"""
        self.enabled = False
        self.on_disable()
        return True
    
    def cleanup(self):
        """清理插件资源"""
        self.on_cleanup()
        self.initialized = False
        self.enabled = False
    
    def on_enable(self):
        """插件启用时的回调"""
        pass
    
    def on_disable(self):
        """插件禁用时的回调"""
        pass
    
    def on_cleanup(self):
        """插件清理时的回调"""
        pass
    
    def is_enabled(self) -> bool:
        """检查插件是否启用"""
        return self.enabled
    
    def is_initialized(self) -> bool:
        """检查插件是否已初始化"""
        return self.initialized
