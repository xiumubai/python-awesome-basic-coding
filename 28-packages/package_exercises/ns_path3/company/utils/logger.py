"""日志工具 - 来自path3"""
import time

class Logger:
    """日志记录器"""
    
    def __init__(self, name="app"):
        self.name = name
        self.source = "path3"
        self.logs = []
        print(f"创建日志器: {name} (来自 {self.source})")
    
    def log(self, level, message):
        """记录日志"""
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] [{self.name}] [{level}] {message} (来源: {self.source})"
        self.logs.append(log_entry)
        print(log_entry)
    
    def info(self, message):
        """信息日志"""
        self.log("INFO", message)
    
    def warning(self, message):
        """警告日志"""
        self.log("WARNING", message)
    
    def error(self, message):
        """错误日志"""
        self.log("ERROR", message)
    
    def get_logs(self):
        """获取所有日志"""
        return self.logs.copy()
    
    def get_info(self):
        """获取日志器信息"""
        return {
            "name": self.name,
            "source": self.source,
            "logs_count": len(self.logs)
        }

print(f"日志工具已加载 (来自 path3)")
