"""初始化演示主包"""
import time
print(f"[{time.strftime('%H:%M:%S')}] 正在初始化 init_demo 主包")

# 包级别变量
__version__ = "1.0.0"
__author__ = "Python学习助手"
_initialization_time = time.time()
_initialization_count = 0

# 初始化计数器
def _increment_init_count():
    global _initialization_count
    _initialization_count += 1
    return _initialization_count

# 包初始化
print(f"  包版本: {__version__}")
print(f"  初始化次数: {_increment_init_count()}")
print(f"  初始化时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(_initialization_time))}")

# 导入子包(延迟导入)
def get_core():
    """延迟导入core子包"""
    from . import core
    return core

def get_utils():
    """延迟导入utils子包"""
    from . import utils
    return utils

# 包级别函数
def get_package_info():
    """获取包信息"""
    return {
        "name": __name__,
        "version": __version__,
        "author": __author__,
        "init_time": _initialization_time,
        "init_count": _initialization_count
    }

print(f"[{time.strftime('%H:%M:%S')}] init_demo 主包初始化完成")
