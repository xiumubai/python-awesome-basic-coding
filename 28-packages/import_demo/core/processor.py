"""处理器模块"""

# 相对导入父包的工具
from ..utils.formatter import format_text

class Processor:
    """处理器类"""
    
    def __init__(self):
        self.name = "默认处理器"
    
    def process(self, data):
        """处理数据"""
        formatted = format_text(f"处理数据: {data}", "PROCESS")
        print(formatted)
        return f"已处理: {data}"
