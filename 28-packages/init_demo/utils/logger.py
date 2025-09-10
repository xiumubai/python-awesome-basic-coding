"""日志工具模块"""
import time
print(f"[{time.strftime('%H:%M:%S')}] 正在初始化 logger 模块")

class Logger:
    """简单日志器"""
    
    def __init__(self, name="logger"):
        self.name = name
        self.messages = []
        self.created_time = time.time()
        print(f"  创建日志器: {name}")
    
    def log(self, level, message):
        """记录日志"""
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        self.messages.append(log_entry)
        print(f"  {self.name}: {log_entry}")
    
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
    
    def clear(self):
        """清空日志"""
        count = len(self.messages)
        self.messages.clear()
        print(f"  {self.name}: 已清空 {count} 条日志")

print(f"[{time.strftime('%H:%M:%S')}] logger 模块初始化完成")
