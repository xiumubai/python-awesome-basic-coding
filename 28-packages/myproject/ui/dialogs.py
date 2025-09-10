
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
