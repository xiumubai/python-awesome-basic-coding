"""核心子包初始化"""
import time
print(f"[{time.strftime('%H:%M:%S')}] 正在初始化 init_demo.core 子包")

# 子包初始化时间
_core_init_time = time.time()

# 导入父包信息
from .. import get_package_info
parent_info = get_package_info()
print(f"  父包版本: {parent_info['version']}")
print(f"  父包初始化时间: {time.strftime('%H:%M:%S', time.localtime(parent_info['init_time']))}")

# 子包配置
CORE_CONFIG = {
    "debug": True,
    "max_workers": 4,
    "timeout": 30
}

# 延迟导入模块
def get_engine():
    """延迟导入engine模块"""
    from .engine import Engine
    return Engine

def get_processor():
    """延迟导入processor模块"""
    from .processor import Processor
    return Processor

print(f"[{time.strftime('%H:%M:%S')}] init_demo.core 子包初始化完成")
