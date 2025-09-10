"""日志工具模块 - 来自path2"""
import time

class Logger:
    """日志记录器"""
    
    def __init__(self, name="Logger"):
        self.name = name
        self.messages = []
        self.source = "path2"
        print(f"创建日志器: {name} (来自 {self.source})")
    
    def log(self, level, message):
        """记录日志"""
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message} (来源: {self.source})"
        self.messages.append(log_entry)
        print(log_entry)
    
    def info(self, message):
        """记录信息日志"""
        self.log("INFO", message)
    
    def warning(self, message):
        """记录警告日志"""
        self.log("WARNING", message)
    
    def error(self, message):
        """记录错误日志"""
        self.log("ERROR", message)
    
    def get_logs(self):
        """获取所有日志"""
        return self.messages.copy()

# 创建默认日志器
default_logger = Logger("default")

print(f"日志工具模块已加载 (来自 path2)")
