"""引擎模块"""

# 相对导入同包模块
from .processor import Processor
# 相对导入父包的其他子包
from ..utils import helper

class Engine:
    """引擎类"""
    
    def __init__(self):
        self.processor = Processor()
        self.running = False
    
    def start(self):
        """启动引擎"""
        print("引擎启动中...")
        self.running = True
        self.processor.process("引擎数据")
        helper.show_info()
    
    def stop(self):
        """停止引擎"""
        print("引擎停止中...")
        self.running = False
