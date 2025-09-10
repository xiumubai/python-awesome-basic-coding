"""辅助工具模块 - 来自path2"""

class Helper:
    """辅助工具类"""
    
    def __init__(self):
        self.source = "path2"
        self.operations_count = 0
        print(f"创建辅助工具 (来自 {self.source})")
    
    def format_text(self, text, style="normal"):
        """格式化文本"""
        self.operations_count += 1
        
        if style == "upper":
            result = text.upper()
        elif style == "lower":
            result = text.lower()
        elif style == "title":
            result = text.title()
        elif style == "reverse":
            result = text[::-1]
        else:
            result = text
        
        print(f"格式化文本: '{text}' -> '{result}' (操作#{self.operations_count})")
        return result
    
    def calculate(self, operation, a, b):
        """简单计算"""
        self.operations_count += 1
        
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            result = a / b if b != 0 else None
        else:
            result = None
        
        print(f"计算: {a} {operation} {b} = {result} (操作#{self.operations_count})")
        return result
    
    def get_stats(self):
        """获取统计信息"""
        return {
            "source": self.source,
            "operations_count": self.operations_count
        }

print(f"辅助工具模块已加载 (来自 path2)")
