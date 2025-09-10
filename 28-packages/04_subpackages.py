#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
子包的创建和管理

本模块演示Python子包的创建、组织和管理，包括：
- 子包的概念和结构
- 多层次包的设计
- 子包之间的相互导入
- 子包的初始化和配置

学习要点：
1. 子包的层次结构设计
2. 子包的__init__.py文件
3. 跨子包的模块导入
4. 子包的独立性和耦合性
5. 大型项目的包组织策略
"""

import os
import sys
import shutil
from pathlib import Path

def demonstrate_subpackage_concept():
    """
    演示子包的概念
    """
    print("=== 子包概念 ===")
    
    concepts = [
        "子包（Subpackage）是包内部的包，用于进一步组织代码",
        "",
        "特点：",
        "1. 子包也是包，必须包含__init__.py文件",
        "2. 可以有多层嵌套结构",
        "3. 每个层级都可以有自己的模块和子包",
        "4. 支持独立的命名空间",
        "",
        "使用场景：",
        "1. 大型项目的模块化组织",
        "2. 功能模块的分类管理",
        "3. 不同版本或实现的隔离",
        "4. 插件系统的架构设计",
        "",
        "典型结构：",
        "myproject/",
        "├── __init__.py",
        "├── core/              # 核心功能子包",
        "│   ├── __init__.py",
        "│   ├── engine.py",
        "│   └── utils.py",
        "├── ui/               # 用户界面子包",
        "│   ├── __init__.py",
        "│   ├── widgets/      # 嵌套子包",
        "│   │   ├── __init__.py",
        "│   │   └── buttons.py",
        "│   └── dialogs.py",
        "└── plugins/          # 插件子包",
        "    ├── __init__.py",
        "    ├── loader.py",
        "    └── registry.py"
    ]
    
    for line in concepts:
        print(line)

def create_complex_package_structure():
    """
    创建复杂的包结构示例
    """
    print("\n=== 创建复杂包结构 ===")
    
    base_path = os.path.dirname(__file__)
    project_path = os.path.join(base_path, 'myproject')
    
    # 清理已存在的目录
    if os.path.exists(project_path):
        shutil.rmtree(project_path)
    
    # 创建主包
    os.makedirs(project_path, exist_ok=True)
    
    # 主包的__init__.py
    with open(os.path.join(project_path, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('''
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
''')
    
    # 创建core子包
    core_path = os.path.join(project_path, 'core')
    os.makedirs(core_path, exist_ok=True)
    
    # core/__init__.py
    with open(os.path.join(core_path, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('''
"""Core子包 - 核心功能模块"""

print("正在初始化Core子包")

# 从模块导入主要类和函数
from .engine import Engine, EngineError
from .utils import get_system_info, format_size, validate_config
from .database import DatabaseManager, ConnectionError

# 子包版本
__version__ = "1.0.0"

# 公共接口
__all__ = [
    'Engine',
    'EngineError',
    'get_system_info',
    'format_size',
    'validate_config',
    'DatabaseManager',
    'ConnectionError'
]

# 子包级别的配置
CORE_CONFIG = {
    'engine_timeout': 30,
    'max_connections': 100,
    'cache_size': 1024
}
''')
    
    # core/engine.py
    with open(os.path.join(core_path, 'engine.py'), 'w', encoding='utf-8') as f:
        f.write('''
"""核心引擎模块"""

import time
import threading
from typing import Dict, Any, Optional

class EngineError(Exception):
    """引擎异常"""
    pass

class Engine:
    """核心引擎类"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.is_running = False
        self.start_time = None
        self.tasks = []
        self._lock = threading.Lock()
        
        print(f"引擎初始化完成，配置: {self.config}")
    
    def start(self):
        """启动引擎"""
        with self._lock:
            if self.is_running:
                raise EngineError("引擎已经在运行")
            
            self.is_running = True
            self.start_time = time.time()
            print("引擎启动成功")
    
    def stop(self):
        """停止引擎"""
        with self._lock:
            if not self.is_running:
                raise EngineError("引擎未运行")
            
            self.is_running = False
            self.start_time = None
            print("引擎已停止")
    
    def add_task(self, task_name: str, task_data: Any = None):
        """添加任务"""
        if not self.is_running:
            raise EngineError("引擎未运行，无法添加任务")
        
        task = {
            'name': task_name,
            'data': task_data,
            'created_at': time.time()
        }
        
        with self._lock:
            self.tasks.append(task)
        
        print(f"任务已添加: {task_name}")
        return len(self.tasks) - 1  # 返回任务ID
    
    def get_status(self):
        """获取引擎状态"""
        with self._lock:
            return {
                'running': self.is_running,
                'uptime': time.time() - self.start_time if self.start_time else 0,
                'task_count': len(self.tasks),
                'config': self.config.copy()
            }
    
    def process_tasks(self):
        """处理任务（模拟）"""
        if not self.is_running:
            raise EngineError("引擎未运行")
        
        with self._lock:
            processed = len(self.tasks)
            self.tasks.clear()
        
        print(f"处理了 {processed} 个任务")
        return processed
''')
    
    # core/utils.py
    with open(os.path.join(core_path, 'utils.py'), 'w', encoding='utf-8') as f:
        f.write('''
"""核心工具模块"""

import platform
import psutil
import json
from typing import Dict, Any

def get_system_info() -> Dict[str, Any]:
    """获取系统信息"""
    try:
        return {
            'platform': platform.platform(),
            'python_version': platform.python_version(),
            'cpu_count': psutil.cpu_count() if 'psutil' in globals() else 'N/A',
            'memory_total': 'N/A',  # 简化实现
            'disk_usage': 'N/A'     # 简化实现
        }
    except:
        return {
            'platform': platform.platform(),
            'python_version': platform.python_version(),
            'cpu_count': 'N/A',
            'memory_total': 'N/A',
            'disk_usage': 'N/A'
        }

def format_size(bytes_size: int) -> str:
    """格式化文件大小"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.1f} PB"

def validate_config(config: Dict[str, Any]) -> bool:
    """验证配置"""
    required_keys = ['engine_timeout', 'max_connections']
    
    for key in required_keys:
        if key not in config:
            print(f"缺少必需的配置项: {key}")
            return False
    
    if config.get('engine_timeout', 0) <= 0:
        print("engine_timeout必须大于0")
        return False
    
    if config.get('max_connections', 0) <= 0:
        print("max_connections必须大于0")
        return False
    
    return True

def save_config(config: Dict[str, Any], filename: str) -> bool:
    """保存配置到文件"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"保存配置失败: {e}")
        return False

def load_config(filename: str) -> Dict[str, Any]:
    """从文件加载配置"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载配置失败: {e}")
        return {}
''')
    
    # core/database.py
    with open(os.path.join(core_path, 'database.py'), 'w', encoding='utf-8') as f:
        f.write('''
"""数据库管理模块"""

import sqlite3
import threading
from typing import List, Dict, Any, Optional

class ConnectionError(Exception):
    """连接异常"""
    pass

class DatabaseManager:
    """数据库管理器"""
    
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.connection = None
        self._lock = threading.Lock()
        
    def connect(self):
        """连接数据库"""
        try:
            with self._lock:
                if self.connection:
                    raise ConnectionError("数据库已连接")
                
                self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
                self.connection.row_factory = sqlite3.Row
                print(f"数据库连接成功: {self.db_path}")
                
        except sqlite3.Error as e:
            raise ConnectionError(f"数据库连接失败: {e}")
    
    def disconnect(self):
        """断开数据库连接"""
        with self._lock:
            if self.connection:
                self.connection.close()
                self.connection = None
                print("数据库连接已断开")
    
    def execute(self, sql: str, params: tuple = ()) -> sqlite3.Cursor:
        """执行SQL语句"""
        if not self.connection:
            raise ConnectionError("数据库未连接")
        
        try:
            with self._lock:
                cursor = self.connection.cursor()
                cursor.execute(sql, params)
                self.connection.commit()
                return cursor
        except sqlite3.Error as e:
            raise ConnectionError(f"SQL执行失败: {e}")
    
    def fetch_all(self, sql: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """查询所有结果"""
        cursor = self.execute(sql, params)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    
    def fetch_one(self, sql: str, params: tuple = ()) -> Optional[Dict[str, Any]]:
        """查询单个结果"""
        cursor = self.execute(sql, params)
        row = cursor.fetchone()
        return dict(row) if row else None
    
    def create_table(self, table_name: str, columns: Dict[str, str]):
        """创建表"""
        column_defs = [f"{name} {type_def}" for name, type_def in columns.items()]
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_defs)})"
        self.execute(sql)
        print(f"表 {table_name} 创建成功")
''')
    
    # 创建ui子包
    ui_path = os.path.join(project_path, 'ui')
    os.makedirs(ui_path, exist_ok=True)
    
    # ui/__init__.py
    with open(os.path.join(ui_path, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('''
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
''')
    
    # ui/main_window.py
    with open(os.path.join(ui_path, 'main_window.py'), 'w', encoding='utf-8') as f:
        f.write('''
"""主窗口模块"""

from typing import Dict, Any, Optional

class MainWindow:
    """主窗口类"""
    
    def __init__(self, title: str = "MyProject", size: tuple = (800, 600)):
        self.title = title
        self.size = size
        self.is_visible = False
        self.widgets = []
        
        print(f"创建主窗口: {title} ({size[0]}x{size[1]})")
    
    def show(self):
        """显示窗口"""
        self.is_visible = True
        print(f"显示窗口: {self.title}")
    
    def hide(self):
        """隐藏窗口"""
        self.is_visible = False
        print(f"隐藏窗口: {self.title}")
    
    def add_widget(self, widget):
        """添加控件"""
        self.widgets.append(widget)
        print(f"添加控件: {widget.__class__.__name__}")
    
    def set_title(self, title: str):
        """设置标题"""
        self.title = title
        print(f"设置窗口标题: {title}")
    
    def resize(self, width: int, height: int):
        """调整大小"""
        self.size = (width, height)
        print(f"调整窗口大小: {width}x{height}")
    
    def get_info(self) -> Dict[str, Any]:
        """获取窗口信息"""
        return {
            'title': self.title,
            'size': self.size,
            'visible': self.is_visible,
            'widget_count': len(self.widgets)
        }

def create_main_window(title: str = "MyProject", **kwargs) -> MainWindow:
    """创建主窗口的工厂函数"""
    size = kwargs.get('size', (800, 600))
    window = MainWindow(title, size)
    
    # 添加默认控件
    from .widgets import Button, Label
    
    window.add_widget(Label("欢迎使用MyProject"))
    window.add_widget(Button("开始", lambda: print("开始按钮被点击")))
    
    return window
''')
    
    # ui/dialogs.py
    with open(os.path.join(ui_path, 'dialogs.py'), 'w', encoding='utf-8') as f:
        f.write('''
"""对话框模块"""

from typing import Optional, Callable, Any

class BaseDialog:
    """对话框基类"""
    
    def __init__(self, title: str, modal: bool = True):
        self.title = title
        self.modal = modal
        self.result = None
        self.is_open = False
    
    def show(self):
        """显示对话框"""
        self.is_open = True
        print(f"显示对话框: {self.title}")
    
    def close(self, result: Any = None):
        """关闭对话框"""
        self.result = result
        self.is_open = False
        print(f"关闭对话框: {self.title}")

class MessageDialog(BaseDialog):
    """消息对话框"""
    
    def __init__(self, title: str, message: str, dialog_type: str = "info"):
        super().__init__(title)
        self.message = message
        self.dialog_type = dialog_type  # info, warning, error, question
    
    def show(self):
        super().show()
        print(f"消息类型: {self.dialog_type}")
        print(f"消息内容: {self.message}")
        
        # 模拟用户点击确定
        self.close("ok")
        return self.result

class InputDialog(BaseDialog):
    """输入对话框"""
    
    def __init__(self, title: str, prompt: str, default_value: str = ""):
        super().__init__(title)
        self.prompt = prompt
        self.default_value = default_value
        self.input_value = default_value
    
    def show(self):
        super().show()
        print(f"提示: {self.prompt}")
        print(f"默认值: {self.default_value}")
        
        # 模拟用户输入
        self.input_value = f"用户输入_{self.default_value}"
        self.close(self.input_value)
        return self.result

class ConfirmDialog(BaseDialog):
    """确认对话框"""
    
    def __init__(self, title: str, message: str):
        super().__init__(title)
        self.message = message
    
    def show(self):
        super().show()
        print(f"确认消息: {self.message}")
        
        # 模拟用户选择
        self.close(True)  # 假设用户点击了确定
        return self.result

def show_dialog(dialog_type: str, title: str, message: str, **kwargs):
    """显示对话框的便捷函数"""
    if dialog_type == "message":
        dialog = MessageDialog(title, message, kwargs.get('msg_type', 'info'))
    elif dialog_type == "input":
        dialog = InputDialog(title, message, kwargs.get('default', ''))
    elif dialog_type == "confirm":
        dialog = ConfirmDialog(title, message)
    else:
        raise ValueError(f"不支持的对话框类型: {dialog_type}")
    
    return dialog.show()
''')
    
    # 创建ui/widgets子包
    widgets_path = os.path.join(ui_path, 'widgets')
    os.makedirs(widgets_path, exist_ok=True)
    
    # ui/widgets/__init__.py
    with open(os.path.join(widgets_path, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('''
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
''')
    
    # ui/widgets/basic.py
    with open(os.path.join(widgets_path, 'basic.py'), 'w', encoding='utf-8') as f:
        f.write('''
"""基础控件模块"""

from typing import Callable, Optional, Any

class Widget:
    """控件基类"""
    
    def __init__(self, name: str = ""):
        self.name = name
        self.visible = True
        self.enabled = True
        self.parent = None
    
    def show(self):
        """显示控件"""
        self.visible = True
        print(f"{self.__class__.__name__} '{self.name}' 已显示")
    
    def hide(self):
        """隐藏控件"""
        self.visible = False
        print(f"{self.__class__.__name__} '{self.name}' 已隐藏")
    
    def enable(self):
        """启用控件"""
        self.enabled = True
        print(f"{self.__class__.__name__} '{self.name}' 已启用")
    
    def disable(self):
        """禁用控件"""
        self.enabled = False
        print(f"{self.__class__.__name__} '{self.name}' 已禁用")

class Button(Widget):
    """按钮控件"""
    
    def __init__(self, text: str, click_handler: Optional[Callable] = None, name: str = ""):
        super().__init__(name or f"button_{text}")
        self.text = text
        self.click_handler = click_handler
    
    def click(self):
        """点击按钮"""
        if not self.enabled:
            print(f"按钮 '{self.text}' 已禁用，无法点击")
            return
        
        print(f"按钮 '{self.text}' 被点击")
        if self.click_handler:
            self.click_handler()
    
    def set_text(self, text: str):
        """设置按钮文本"""
        self.text = text
        print(f"按钮文本已更改为: '{text}'")

class Label(Widget):
    """标签控件"""
    
    def __init__(self, text: str, name: str = ""):
        super().__init__(name or f"label_{text[:10]}")
        self.text = text
    
    def set_text(self, text: str):
        """设置标签文本"""
        self.text = text
        print(f"标签文本已更改为: '{text}'")
    
    def get_text(self) -> str:
        """获取标签文本"""
        return self.text

class TextBox(Widget):
    """文本框控件"""
    
    def __init__(self, placeholder: str = "", name: str = ""):
        super().__init__(name or "textbox")
        self.placeholder = placeholder
        self.text = ""
        self.max_length = 0  # 0表示无限制
    
    def set_text(self, text: str):
        """设置文本"""
        if self.max_length > 0 and len(text) > self.max_length:
            text = text[:self.max_length]
            print(f"文本被截断到 {self.max_length} 个字符")
        
        self.text = text
        print(f"文本框内容已设置为: '{text}'")
    
    def get_text(self) -> str:
        """获取文本"""
        return self.text
    
    def clear(self):
        """清空文本"""
        self.text = ""
        print("文本框已清空")
    
    def set_max_length(self, length: int):
        """设置最大长度"""
        self.max_length = length
        print(f"文本框最大长度设置为: {length}")
''')
    
    # ui/widgets/advanced.py
    with open(os.path.join(widgets_path, 'advanced.py'), 'w', encoding='utf-8') as f:
        f.write('''
"""高级控件模块"""

from typing import List, Dict, Any, Optional
from .basic import Widget

class ListView(Widget):
    """列表视图控件"""
    
    def __init__(self, name: str = "listview"):
        super().__init__(name)
        self.items = []
        self.selected_index = -1
    
    def add_item(self, item: Any):
        """添加项目"""
        self.items.append(item)
        print(f"添加列表项: {item}")
    
    def remove_item(self, index: int):
        """移除项目"""
        if 0 <= index < len(self.items):
            item = self.items.pop(index)
            print(f"移除列表项: {item}")
            if self.selected_index == index:
                self.selected_index = -1
    
    def select_item(self, index: int):
        """选择项目"""
        if 0 <= index < len(self.items):
            self.selected_index = index
            print(f"选择列表项: {self.items[index]}")
    
    def get_selected_item(self) -> Optional[Any]:
        """获取选中项目"""
        if 0 <= self.selected_index < len(self.items):
            return self.items[self.selected_index]
        return None
    
    def clear(self):
        """清空列表"""
        self.items.clear()
        self.selected_index = -1
        print("列表已清空")

class TreeView(Widget):
    """树视图控件"""
    
    def __init__(self, name: str = "treeview"):
        super().__init__(name)
        self.root_nodes = []
    
    def add_root_node(self, text: str, data: Any = None) -> 'TreeNode':
        """添加根节点"""
        node = TreeNode(text, data)
        self.root_nodes.append(node)
        print(f"添加根节点: {text}")
        return node
    
    def get_all_nodes(self) -> List['TreeNode']:
        """获取所有节点"""
        nodes = []
        for root in self.root_nodes:
            nodes.extend(root.get_all_descendants())
        return nodes
    
    def clear(self):
        """清空树"""
        self.root_nodes.clear()
        print("树视图已清空")

class TreeNode:
    """树节点"""
    
    def __init__(self, text: str, data: Any = None):
        self.text = text
        self.data = data
        self.children = []
        self.parent = None
        self.expanded = False
    
    def add_child(self, text: str, data: Any = None) -> 'TreeNode':
        """添加子节点"""
        child = TreeNode(text, data)
        child.parent = self
        self.children.append(child)
        print(f"添加子节点: {text} (父节点: {self.text})")
        return child
    
    def remove_child(self, child: 'TreeNode'):
        """移除子节点"""
        if child in self.children:
            child.parent = None
            self.children.remove(child)
            print(f"移除子节点: {child.text}")
    
    def expand(self):
        """展开节点"""
        self.expanded = True
        print(f"展开节点: {self.text}")
    
    def collapse(self):
        """折叠节点"""
        self.expanded = False
        print(f"折叠节点: {self.text}")
    
    def get_all_descendants(self) -> List['TreeNode']:
        """获取所有后代节点"""
        descendants = [self]
        for child in self.children:
            descendants.extend(child.get_all_descendants())
        return descendants

class TabControl(Widget):
    """标签页控件"""
    
    def __init__(self, name: str = "tabcontrol"):
        super().__init__(name)
        self.tabs = []
        self.selected_index = 0
    
    def add_tab(self, title: str, content: Any = None) -> 'Tab':
        """添加标签页"""
        tab = Tab(title, content)
        self.tabs.append(tab)
        print(f"添加标签页: {title}")
        return tab
    
    def remove_tab(self, index: int):
        """移除标签页"""
        if 0 <= index < len(self.tabs):
            tab = self.tabs.pop(index)
            print(f"移除标签页: {tab.title}")
            if self.selected_index >= len(self.tabs) and self.tabs:
                self.selected_index = len(self.tabs) - 1
    
    def select_tab(self, index: int):
        """选择标签页"""
        if 0 <= index < len(self.tabs):
            self.selected_index = index
            print(f"选择标签页: {self.tabs[index].title}")
    
    def get_selected_tab(self) -> Optional['Tab']:
        """获取当前选中的标签页"""
        if 0 <= self.selected_index < len(self.tabs):
            return self.tabs[self.selected_index]
        return None

class Tab:
    """标签页"""
    
    def __init__(self, title: str, content: Any = None):
        self.title = title
        self.content = content
        self.visible = True
    
    def set_title(self, title: str):
        """设置标题"""
        self.title = title
        print(f"标签页标题已更改为: {title}")
    
    def set_content(self, content: Any):
        """设置内容"""
        self.content = content
        print(f"标签页内容已更新")
''')
    
    # 创建plugins子包
    plugins_path = os.path.join(project_path, 'plugins')
    os.makedirs(plugins_path, exist_ok=True)
    
    # plugins/__init__.py
    with open(os.path.join(plugins_path, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('''
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
''')
    
    # plugins/manager.py
    with open(os.path.join(plugins_path, 'manager.py'), 'w', encoding='utf-8') as f:
        f.write('''
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
''')
    
    # plugins/base.py
    with open(os.path.join(plugins_path, 'base.py'), 'w', encoding='utf-8') as f:
        f.write('''
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
''')
    
    # plugins/loader.py 和 registry.py（简化版本）
    with open(os.path.join(plugins_path, 'loader.py'), 'w', encoding='utf-8') as f:
        f.write('''
"""插件加载器模块"""

import os
from typing import Optional
from .base import BasePlugin, PluginInfo

class PluginLoader:
    """插件加载器"""
    
    def load_plugin(self, plugin_name: str, plugin_dir: str) -> Optional[BasePlugin]:
        """加载插件（模拟实现）"""
        print(f"正在加载插件: {plugin_name}")
        
        # 这里是模拟实现，实际应该动态导入插件模块
        if plugin_name == "sample_plugin":
            return SamplePlugin()
        
        print(f"插件 {plugin_name} 不存在")
        return None

class SamplePlugin(BasePlugin):
    """示例插件"""
    
    def get_info(self) -> PluginInfo:
        return PluginInfo(
            name="sample_plugin",
            version="1.0.0",
            description="示例插件",
            author="Python学习者"
        )
    
    def initialize(self) -> bool:
        print("示例插件初始化")
        return True
    
    def on_enable(self):
        print("示例插件已启用")
    
    def on_disable(self):
        print("示例插件已禁用")
    
    def do_something(self, message: str):
        """插件功能方法"""
        print(f"示例插件执行: {message}")
        return f"处理完成: {message}"

def load_plugin(plugin_name: str, plugin_dir: str = "plugins") -> Optional[BasePlugin]:
    """加载插件的便捷函数"""
    loader = PluginLoader()
    return loader.load_plugin(plugin_name, plugin_dir)
''')
    
    with open(os.path.join(plugins_path, 'registry.py'), 'w', encoding='utf-8') as f:
        f.write('''
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
''')
    
    print(f"\n复杂包结构创建完成: {project_path}")
    print("\n包结构:")
    print("myproject/")
    print("├── __init__.py")
    print("├── core/")
    print("│   ├── __init__.py")
    print("│   ├── engine.py")
    print("│   ├── utils.py")
    print("│   └── database.py")
    print("├── ui/")
    print("│   ├── __init__.py")
    print("│   ├── main_window.py")
    print("│   ├── dialogs.py")
    print("│   └── widgets/")
    print("│       ├── __init__.py")
    print("│       ├── basic.py")
    print("│       └── advanced.py")
    print("└── plugins/")
    print("    ├── __init__.py")
    print("    ├── manager.py")
    print("    ├── base.py")
    print("    ├── loader.py")
    print("    └── registry.py")
    
    return project_path

def demonstrate_subpackage_usage():
    """
    演示子包的使用
    """
    print("\n=== 子包使用演示 ===")
    
    # 添加路径
    base_path = os.path.dirname(__file__)
    if base_path not in sys.path:
        sys.path.insert(0, base_path)
    
    try:
        print("\n1. 导入主包:")
        import myproject
        
        info = myproject.get_project_info()
        print(f"   项目信息: {info}")
        
        print("\n2. 使用core子包:")
        from myproject.core import Engine, get_system_info
        
        # 创建引擎
        engine = Engine({'timeout': 60})
        engine.start()
        engine.add_task("测试任务1")
        engine.add_task("测试任务2")
        
        status = engine.get_status()
        print(f"   引擎状态: 运行={status['running']}, 任务数={status['task_count']}")
        
        processed = engine.process_tasks()
        print(f"   处理了 {processed} 个任务")
        
        engine.stop()
        
        # 获取系统信息
        sys_info = get_system_info()
        print(f"   系统信息: {sys_info['platform']}, Python {sys_info['python_version']}")
        
        print("\n3. 使用ui子包:")
        from myproject.ui import create_main_window, show_dialog
        
        # 创建主窗口
        window = create_main_window("演示窗口")
        window.show()
        
        window_info = window.get_info()
        print(f"   窗口信息: {window_info}")
        
        # 显示对话框
        result = show_dialog("message", "提示", "这是一个消息对话框")
        print(f"   对话框结果: {result}")
        
        window.hide()
        
        print("\n4. 使用嵌套子包 ui.widgets:")
        from myproject.ui.widgets import Button, ListView, TreeView
        
        # 创建按钮
        button = Button("点击我", lambda: print("按钮被点击了！"))
        button.click()
        
        # 创建列表视图
        listview = ListView()
        listview.add_item("项目1")
        listview.add_item("项目2")
        listview.select_item(0)
        selected = listview.get_selected_item()
        print(f"   选中的列表项: {selected}")
        
        # 创建树视图
        treeview = TreeView()
        root = treeview.add_root_node("根节点")
        child1 = root.add_child("子节点1")
        child2 = root.add_child("子节点2")
        grandchild = child1.add_child("孙节点")
        
        all_nodes = treeview.get_all_nodes()
        print(f"   树节点总数: {len(all_nodes)}")
        
        print("\n5. 使用plugins子包:")
        from myproject.plugins import PluginManager
        
        # 创建插件管理器
        plugin_manager = PluginManager()
        
        # 加载示例插件
        success = plugin_manager.load_plugin("sample_plugin")
        if success:
            plugin_manager.enable_plugin("sample_plugin")
            
            # 调用插件方法
            result = plugin_manager.call_plugin_method(
                "sample_plugin", "do_something", "Hello from plugin!"
            )
            print(f"   插件调用结果: {result}")
            
            # 获取插件状态
            status = plugin_manager.get_status()
            print(f"   插件管理器状态: {status}")
        
    except ImportError as e:
        print(f"导入错误: {e}")
    except Exception as e:
        print(f"运行错误: {e}")

def demonstrate_cross_subpackage_import():
    """
    演示跨子包导入
    """
    print("\n=== 跨子包导入演示 ===")
    
    try:
        # 在ui模块中使用core模块的功能
        print("\n1. UI模块使用Core模块:")
        from myproject.core import Engine
        from myproject.ui import MainWindow
        
        # 创建带引擎的窗口类
        class EngineWindow(MainWindow):
            def __init__(self, title="引擎窗口"):
                super().__init__(title)
                self.engine = Engine({'ui_mode': True})
                print("   创建了集成引擎的窗口")
            
            def start_engine(self):
                self.engine.start()
                print("   窗口中的引擎已启动")
            
            def stop_engine(self):
                if self.engine.is_running:
                    self.engine.stop()
                    print("   窗口中的引擎已停止")
        
        # 使用集成窗口
        engine_window = EngineWindow()
        engine_window.show()
        engine_window.start_engine()
        engine_window.stop_engine()
        engine_window.hide()
        
        print("\n2. Plugins模块使用Core和UI模块:")
        from myproject.plugins.base import BasePlugin, PluginInfo
        from myproject.core import get_system_info
        from myproject.ui.widgets import Button
        
        # 创建UI插件
        class UIPlugin(BasePlugin):
            def __init__(self):
                super().__init__()
                self.button = None
            
            def get_info(self) -> PluginInfo:
                return PluginInfo(
                    name="ui_plugin",
                    version="1.0.0",
                    description="UI功能插件",
                    author="Python学习者"
                )
            
            def initialize(self) -> bool:
                # 使用系统信息
                sys_info = get_system_info()
                print(f"   插件初始化，系统: {sys_info['platform']}")
                
                # 创建UI组件
                self.button = Button("插件按钮", self.on_button_click)
                print("   插件UI组件创建完成")
                return True
            
            def on_button_click(self):
                print("   插件按钮被点击")
            
            def on_enable(self):
                print("   UI插件已启用")
            
            def on_disable(self):
                print("   UI插件已禁用")
        
        # 使用UI插件
        ui_plugin = UIPlugin()
        ui_plugin.enable()
        if ui_plugin.button:
            ui_plugin.button.click()
        ui_plugin.disable()
        
    except ImportError as e:
        print(f"导入错误: {e}")
    except Exception as e:
        print(f"运行错误: {e}")

def demonstrate_subpackage_best_practices():
    """
    演示子包的最佳实践
    """
    print("\n=== 子包最佳实践 ===")
    
    practices = [
        "1. 包结构设计原则:",
        "   - 按功能模块划分子包",
        "   - 保持包的单一职责",
        "   - 避免循环依赖",
        "   - 合理控制包的深度",
        "",
        "2. __init__.py文件管理:",
        "   - 明确定义公共接口(__all__)",
        "   - 提供便捷的导入路径",
        "   - 包含必要的初始化代码",
        "   - 添加版本和作者信息",
        "",
        "3. 导入策略:",
        "   - 优先使用绝对导入",
        "   - 谨慎使用相对导入",
        "   - 避免在__init__.py中导入过多模块",
        "   - 使用延迟导入优化性能",
        "",
        "4. 命名规范:",
        "   - 包名使用小写字母和下划线",
        "   - 避免与标准库冲突",
        "   - 保持命名的一致性",
        "   - 使用有意义的名称",
        "",
        "5. 文档和测试:",
        "   - 为每个包提供详细文档",
        "   - 编写单元测试",
        "   - 提供使用示例",
        "   - 维护更新日志",
        "",
        "6. 版本管理:",
        "   - 使用语义化版本号",
        "   - 保持向后兼容性",
        "   - 及时更新依赖关系",
        "   - 提供迁移指南"
    ]
    
    for line in practices:
        print(line)

def main():
    """
    主函数 - 演示子包的创建和管理
    """
    print("Python子包创建和管理演示")
    print("=" * 50)
    
    # 1. 演示子包概念
    demonstrate_subpackage_concept()
    
    # 2. 创建复杂包结构
    project_path = create_complex_package_structure()
    
    # 3. 演示子包使用
    demonstrate_subpackage_usage()
    
    # 4. 演示跨子包导入
    demonstrate_cross_subpackage_import()
    
    # 5. 演示最佳实践
    demonstrate_subpackage_best_practices()
    
    print("\n=== 学习小结 ===")
    summary_points = [
        "1. 子包是包内部的包，用于进一步组织代码结构",
        "2. 每个子包都必须包含__init__.py文件",
        "3. 子包可以有多层嵌套，形成树状结构",
        "4. 合理的包结构有助于代码的维护和扩展",
        "5. 跨子包导入需要注意避免循环依赖",
        "6. 遵循最佳实践可以提高代码质量和可维护性"
    ]
    
    for point in summary_points:
        print(point)
    
    print(f"\n示例包已创建在: {project_path}")
    print("可以通过导入myproject包来使用这些功能")

if __name__ == "__main__":
    main()