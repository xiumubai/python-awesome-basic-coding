
# 复杂的__init__.py示例
import os
import sys
from datetime import datetime

# 包信息
__version__ = "4.0.0"
__author__ = "Python学习者"
__email__ = "learner@python.org"

print(f"正在加载 {__name__} 包...")

# 动态导入模块
try:
    from .core import CoreClass
    from .helpers import helper_function
    CORE_AVAILABLE = True
except ImportError as e:
    print(f"警告：核心模块导入失败 - {e}")
    CORE_AVAILABLE = False

# 包级别的配置
CONFIG = {
    'debug': False,
    'log_level': 'INFO',
    'created_at': datetime.now().isoformat()
}

# 包级别的函数
def get_info():
    return {
        'name': __name__,
        'version': __version__,
        'author': __author__,
        'core_available': CORE_AVAILABLE,
        'config': CONFIG
    }

def configure(debug=None, log_level=None):
    if debug is not None:
        CONFIG['debug'] = debug
    if log_level is not None:
        CONFIG['log_level'] = log_level
    print(f"包配置已更新: {CONFIG}")

# 定义公共接口
__all__ = ['CoreClass', 'helper_function', 'get_info', 'configure', 'CONFIG']

print(f"{__name__} v{__version__} 加载完成")
