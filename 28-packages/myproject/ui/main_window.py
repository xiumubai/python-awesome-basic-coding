
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
