"""核心包"""
print("正在初始化core包")

# 相对导入子模块
from .engine import Engine
from .processor import Processor

__all__ = ["Engine", "Processor"]
