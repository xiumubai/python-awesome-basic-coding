"""工具子包初始化"""
import time
print(f"[{time.strftime('%H:%M:%S')}] 正在初始化 init_demo.utils 子包")

# 工具包配置
UTILS_CONFIG = {
    "log_level": "INFO",
    "date_format": "%Y-%m-%d %H:%M:%S",
    "encoding": "utf-8"
}

# 导入工具模块
from .logger import Logger
from .helper import Helper

# 创建默认实例
default_logger = Logger("default")
default_helper = Helper()

print(f"  创建默认日志器: {default_logger.name}")
print(f"  创建默认助手: {default_helper.name}")

# 导出接口
__all__ = ["Logger", "Helper", "default_logger", "default_helper", "UTILS_CONFIG"]

print(f"[{time.strftime('%H:%M:%S')}] init_demo.utils 子包初始化完成")
