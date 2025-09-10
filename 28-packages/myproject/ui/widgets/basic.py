
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
