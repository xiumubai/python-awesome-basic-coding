
"""Core子包 - 核心功能模块"""

print("正在初始化Core子包")

# 从模块导入主要类和函数
from .engine import Engine, EngineError
from .utils import get_system_info, format_size, validate_config
from .database import DatabaseManager, ConnectionError

# 子包版本
__version__ = "1.0.0"

# 公共接口
__all__ = [
    'Engine',
    'EngineError',
    'get_system_info',
    'format_size',
    'validate_config',
    'DatabaseManager',
    'ConnectionError'
]

# 子包级别的配置
CORE_CONFIG = {
    'engine_timeout': 30,
    'max_connections': 100,
    'cache_size': 1024
}
