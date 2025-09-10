"""辅助工具模块"""
import time
print(f"[{time.strftime('%H:%M:%S')}] 正在初始化 helper 模块")

class Helper:
    """辅助工具类"""
    
    def __init__(self, name="helper"):
        self.name = name
        self.operations = []
        self.created_time = time.time()
        print(f"  创建助手: {name}")
    
    def format_text(self, text, style="normal"):
        """格式化文本"""
        self.operations.append(f"format_text: {style}")
        
        if style == "upper":
            return text.upper()
        elif style == "lower":
            return text.lower()
        elif style == "title":
            return text.title()
        elif style == "reverse":
            return text[::-1]
        else:
            return text
    
    def calculate(self, operation, a, b):
        """简单计算"""
        self.operations.append(f"calculate: {operation}")
        
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b if b != 0 else None
        else:
            return None
    
    def get_operations(self):
        """获取操作历史"""
        return self.operations.copy()
    
    def reset(self):
        """重置助手"""
        count = len(self.operations)
        self.operations.clear()
        print(f"  {self.name}: 已重置，清除 {count} 个操作记录")

print(f"[{time.strftime('%H:%M:%S')}] helper 模块初始化完成")
