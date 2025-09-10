
# 计算器模块
class Calculator:
    """简单计算器类"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """加法"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """减法"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """乘法"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """获取计算历史"""
        return self.history.copy()
    
    def clear_history(self):
        """清空历史"""
        self.history.clear()

# 模块级别的函数
def quick_add(a, b):
    """快速加法"""
    return a + b

def quick_multiply(a, b):
    """快速乘法"""
    return a * b
