
# 使用__all__控制导入的__init__.py

# 导入子模块
from .math_ops import add, multiply
from .string_ops import reverse, capitalize

# 定义__all__变量
__all__ = ['add', 'multiply', 'reverse', 'get_version']

# 包级别的变量
__version__ = "3.0.0"

# 包级别的函数
def get_version():
    return __version__

print(f"controlled_package v{__version__} 已加载")
