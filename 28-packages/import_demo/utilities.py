
# 工具模块
import datetime
import random
import string

def get_timestamp():
    """获取当前时间戳"""
    return datetime.datetime.now().isoformat()

def format_number(number, decimal_places=2):
    """格式化数字"""
    return f"{number:.{decimal_places}f}"

def generate_random_string(length=10):
    """生成随机字符串"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def is_prime(n):
    """检查是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

class Logger:
    """简单日志记录器"""
    
    def __init__(self, name):
        self.name = name
        self.logs = []
    
    def log(self, message, level="INFO"):
        """记录日志"""
        timestamp = get_timestamp()
        log_entry = f"[{timestamp}] {level}: {message}"
        self.logs.append(log_entry)
        print(f"[{self.name}] {log_entry}")
    
    def get_logs(self):
        """获取所有日志"""
        return self.logs.copy()
