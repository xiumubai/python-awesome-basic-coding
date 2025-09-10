#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python包管理 - 包的初始化过程

本模块演示Python包的初始化过程、机制和最佳实践。

学习目标:
1. 理解包的初始化过程和时机
2. 掌握__init__.py文件的执行机制
3. 学会控制包的初始化行为
4. 了解初始化过程中的注意事项

作者: Python学习助手
日期: 2024
"""

import os
import sys
import time
from pathlib import Path
import importlib

def demonstrate_initialization_concepts():
    """
    演示包初始化的基本概念
    """
    print("=== 包初始化基本概念 ===")
    
    concepts = {
        "包初始化时机": [
            "- 首次导入包时执行",
            "- 只执行一次(除非重新加载)",
            "- 按照导入顺序执行",
            "- 子包初始化前先初始化父包"
        ],
        "初始化执行内容": [
            "- 执行__init__.py中的所有代码",
            "- 设置包的属性和变量",
            "- 导入子模块(如果需要)",
            "- 执行初始化逻辑"
        ],
        "初始化顺序": [
            "- 父包 -> 子包 -> 孙包",
            "- 同级包按导入顺序",
            "- 模块导入在包初始化之后",
            "- 循环依赖时可能出现问题"
        ],
        "初始化状态管理": [
            "- sys.modules记录已导入模块",
            "- 包对象存储在sys.modules中",
            "- 重复导入不会重新初始化",
            "- 可以使用importlib.reload()重新加载"
        ]
    }
    
    for concept, details in concepts.items():
        print(f"\n{concept}:")
        for detail in details:
            print(f"  {detail}")

def create_initialization_demo_structure():
    """
    创建用于演示初始化过程的包结构
    """
    print("\n=== 创建初始化演示包结构 ===")
    
    # 定义包结构
    base_path = Path("init_demo")
    
    # 包结构定义
    structure = {
        "init_demo": {
            "__init__.py": '''"""初始化演示主包"""
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
''',
            "core": {
                "__init__.py": '''"""核心子包初始化"""
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
''',
                "engine.py": '''"""引擎模块"""
import time
print(f"[{time.strftime('%H:%M:%S')}] 正在初始化 engine 模块")

# 模块级别变量
_module_init_time = time.time()

class Engine:
    """引擎类"""
    
    def __init__(self, name="默认引擎"):
        self.name = name
        self.running = False
        self.start_time = None
        print(f"  创建引擎实例: {name}")
    
    def start(self):
        """启动引擎"""
        if not self.running:
            self.running = True
            self.start_time = time.time()
            print(f"  引擎 {self.name} 已启动")
        else:
            print(f"  引擎 {self.name} 已经在运行中")
    
    def stop(self):
        """停止引擎"""
        if self.running:
            self.running = False
            run_time = time.time() - self.start_time if self.start_time else 0
            print(f"  引擎 {self.name} 已停止，运行时间: {run_time:.2f}秒")
        else:
            print(f"  引擎 {self.name} 未在运行")
    
    def get_status(self):
        """获取引擎状态"""
        return {
            "name": self.name,
            "running": self.running,
            "start_time": self.start_time,
            "module_init_time": _module_init_time
        }

print(f"[{time.strftime('%H:%M:%S')}] engine 模块初始化完成")
''',
                "processor.py": '''"""处理器模块"""
import time
print(f"[{time.strftime('%H:%M:%S')}] 正在初始化 processor 模块")

# 模块级别配置
PROCESSOR_CONFIG = {
    "batch_size": 100,
    "max_retries": 3,
    "timeout": 10
}

class Processor:
    """处理器类"""
    
    def __init__(self, name="默认处理器"):
        self.name = name
        self.processed_count = 0
        self.error_count = 0
        print(f"  创建处理器实例: {name}")
    
    def process(self, data):
        """处理数据"""
        try:
            # 模拟处理过程
            time.sleep(0.1)
            self.processed_count += 1
            result = f"已处理: {data}"
            print(f"  {self.name} 处理完成: {data}")
            return result
        except Exception as e:
            self.error_count += 1
            print(f"  {self.name} 处理错误: {e}")
            raise
    
    def get_stats(self):
        """获取处理统计"""
        return {
            "name": self.name,
            "processed": self.processed_count,
            "errors": self.error_count,
            "success_rate": self.processed_count / (self.processed_count + self.error_count) if (self.processed_count + self.error_count) > 0 else 0
        }

print(f"[{time.strftime('%H:%M:%S')}] processor 模块初始化完成")
'''
            },
            "utils": {
                "__init__.py": '''"""工具子包初始化"""
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
''',
                "logger.py": '''"""日志工具模块"""
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
''',
                "helper.py": '''"""辅助工具模块"""
import time
print(f"[{time.strftime('%H:%M:%S')}] 正在初始化 helper 模块")

class Helper:
    """辅助工具类"""
    
    def __init__(self, name="helper"):
        self.name = name
        self.operations = []
        self.created_time = time.time()
        print(f"  创建助手: {name}")
    
    def format_text(self, text, style="normal"):
        """格式化文本"""
        self.operations.append(f"format_text: {style}")
        
        if style == "upper":
            return text.upper()
        elif style == "lower":
            return text.lower()
        elif style == "title":
            return text.title()
        elif style == "reverse":
            return text[::-1]
        else:
            return text
    
    def calculate(self, operation, a, b):
        """简单计算"""
        self.operations.append(f"calculate: {operation}")
        
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b if b != 0 else None
        else:
            return None
    
    def get_operations(self):
        """获取操作历史"""
        return self.operations.copy()
    
    def reset(self):
        """重置助手"""
        count = len(self.operations)
        self.operations.clear()
        print(f"  {self.name}: 已重置，清除 {count} 个操作记录")

print(f"[{time.strftime('%H:%M:%S')}] helper 模块初始化完成")
'''
            }
        }
    }
    
    def create_structure(path, structure):
        """递归创建目录结构"""
        for name, content in structure.items():
            current_path = path / name
            
            if isinstance(content, dict):
                # 创建目录
                current_path.mkdir(parents=True, exist_ok=True)
                print(f"创建目录: {current_path}")
                create_structure(current_path, content)
            else:
                # 创建文件
                current_path.parent.mkdir(parents=True, exist_ok=True)
                with open(current_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"创建文件: {current_path}")
    
    # 创建包结构
    create_structure(Path("."), structure)
    
    print(f"\n包结构创建完成: {base_path.absolute()}")
    return base_path.absolute()

def demonstrate_initialization_order():
    """
    演示包的初始化顺序
    """
    print("\n=== 包初始化顺序演示 ===")
    
    print("\n1. 初始化顺序规则:")
    rules = [
        "- 父包先于子包初始化",
        "- 同级包按导入顺序初始化",
        "- 模块在包初始化后导入",
        "- 每个包只初始化一次"
    ]
    
    for rule in rules:
        print(f"  {rule}")
    
    print("\n2. 测试初始化顺序:")
    try:
        # 添加当前目录到sys.path
        current_dir = os.getcwd()
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        
        print("\n  步骤1: 导入主包")
        import init_demo
        
        print("\n  步骤2: 导入core子包")
        from init_demo import core
        
        print("\n  步骤3: 导入utils子包")
        from init_demo import utils
        
        print("\n  步骤4: 导入具体模块")
        from init_demo.core import engine
        
        print("\n  步骤5: 再次导入(不会重新初始化)")
        import init_demo.core
        import init_demo.utils
        
    except ImportError as e:
        print(f"  导入错误: {e}")
    except Exception as e:
        print(f"  运行错误: {e}")

def demonstrate_initialization_control():
    """
    演示如何控制包的初始化行为
    """
    print("\n=== 包初始化控制演示 ===")
    
    print("\n1. 延迟初始化技术:")
    techniques = [
        "- 使用函数包装导入语句",
        "- 在需要时才导入子模块",
        "- 避免在__init__.py中执行耗时操作",
        "- 使用属性访问触发导入"
    ]
    
    for technique in techniques:
        print(f"  {technique}")
    
    print("\n2. 测试延迟初始化:")
    try:
        # 测试延迟导入
        print("\n  获取包信息(不触发子包初始化):")
        import init_demo
        info = init_demo.get_package_info()
        print(f"    包名: {info['name']}")
        print(f"    版本: {info['version']}")
        print(f"    初始化次数: {info['init_count']}")
        
        print("\n  延迟获取core子包:")
        core = init_demo.get_core()
        print(f"    Core配置: {core.CORE_CONFIG}")
        
        print("\n  延迟获取utils子包:")
        utils = init_demo.get_utils()
        print(f"    Utils配置: {utils.UTILS_CONFIG}")
        
    except Exception as e:
        print(f"  错误: {e}")

def demonstrate_initialization_state():
    """
    演示包初始化状态的管理
    """
    print("\n=== 包初始化状态管理 ===")
    
    print("\n1. 查看已导入的包:")
    init_demo_modules = [name for name in sys.modules.keys() if 'init_demo' in name]
    if init_demo_modules:
        for module_name in sorted(init_demo_modules):
            module = sys.modules[module_name]
            print(f"  {module_name}: {type(module)}")
    else:
        print("  未找到init_demo相关模块")
    
    print("\n2. 包的属性和状态:")
    try:
        import init_demo
        
        # 显示包属性
        attrs = ['__name__', '__package__', '__file__', '__version__', '__author__']
        for attr in attrs:
            if hasattr(init_demo, attr):
                value = getattr(init_demo, attr)
                print(f"  {attr}: {value}")
        
        # 显示包的自定义属性
        if hasattr(init_demo, '_initialization_time'):
            init_time = time.strftime('%H:%M:%S', time.localtime(init_demo._initialization_time))
            print(f"  初始化时间: {init_time}")
        
        if hasattr(init_demo, '_initialization_count'):
            print(f"  初始化计数: {init_demo._initialization_count}")
            
    except Exception as e:
        print(f"  错误: {e}")

def demonstrate_reloading():
    """
    演示包的重新加载
    """
    print("\n=== 包重新加载演示 ===")
    
    print("\n1. 重新加载的概念:")
    concepts = [
        "- importlib.reload()可以重新加载模块",
        "- 重新加载会重新执行模块代码",
        "- 已存在的对象不会自动更新",
        "- 需要谨慎处理模块间的依赖关系"
    ]
    
    for concept in concepts:
        print(f"  {concept}")
    
    print("\n2. 测试重新加载:")
    try:
        import init_demo
        
        # 显示重新加载前的状态
        print("\n  重新加载前:")
        info_before = init_demo.get_package_info()
        print(f"    初始化次数: {info_before['init_count']}")
        print(f"    初始化时间: {time.strftime('%H:%M:%S', time.localtime(info_before['init_time']))}")
        
        # 等待一秒以便观察时间差异
        time.sleep(1)
        
        # 重新加载包
        print("\n  执行重新加载...")
        importlib.reload(init_demo)
        
        # 显示重新加载后的状态
        print("\n  重新加载后:")
        info_after = init_demo.get_package_info()
        print(f"    初始化次数: {info_after['init_count']}")
        print(f"    初始化时间: {time.strftime('%H:%M:%S', time.localtime(info_after['init_time']))}")
        
    except Exception as e:
        print(f"  错误: {e}")

def demonstrate_initialization_best_practices():
    """
    演示包初始化的最佳实践
    """
    print("\n=== 包初始化最佳实践 ===")
    
    practices = {
        "1. __init__.py设计原则": [
            "- 保持简洁，避免复杂逻辑",
            "- 明确定义公共接口(__all__)",
            "- 避免执行耗时操作",
            "- 提供清晰的包信息"
        ],
        "2. 导入策略": [
            "- 使用延迟导入减少启动时间",
            "- 避免循环导入",
            "- 合理组织模块依赖关系",
            "- 使用条件导入处理可选依赖"
        ],
        "3. 初始化性能优化": [
            "- 延迟创建重量级对象",
            "- 使用工厂函数按需创建实例",
            "- 避免在导入时执行网络请求",
            "- 合理使用模块级别缓存"
        ],
        "4. 错误处理": [
            "- 优雅处理导入错误",
            "- 提供有意义的错误信息",
            "- 考虑向后兼容性",
            "- 记录初始化过程中的问题"
        ],
        "5. 调试和监控": [
            "- 添加适当的日志记录",
            "- 提供包状态查询接口",
            "- 支持调试模式",
            "- 监控初始化性能"
        ]
    }
    
    for category, items in practices.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  {item}")

def demonstrate_practical_example():
    """
    演示实际的包初始化应用
    """
    print("\n=== 实际应用演示 ===")
    
    print("\n1. 创建和使用包中的组件:")
    try:
        # 导入包
        import init_demo
        
        # 获取工具组件
        utils = init_demo.get_utils()
        logger = utils.default_logger
        helper = utils.default_helper
        
        # 使用日志器
        logger.info("开始演示包的使用")
        logger.warning("这是一个警告消息")
        
        # 使用助手工具
        text = "Hello World"
        formatted = helper.format_text(text, "upper")
        logger.info(f"格式化结果: {formatted}")
        
        # 进行计算
        result = helper.calculate("multiply", 6, 7)
        logger.info(f"计算结果: 6 * 7 = {result}")
        
        # 获取核心组件
        core = init_demo.get_core()
        Engine = core.get_engine()
        Processor = core.get_processor()
        
        # 创建和使用引擎
        engine = Engine("演示引擎")
        engine.start()
        
        # 创建和使用处理器
        processor = Processor("演示处理器")
        processor.process("测试数据1")
        processor.process("测试数据2")
        
        # 获取统计信息
        stats = processor.get_stats()
        logger.info(f"处理统计: {stats}")
        
        # 停止引擎
        time.sleep(0.5)  # 模拟运行时间
        engine.stop()
        
        # 显示日志
        print("\n  日志记录:")
        logs = logger.get_logs()
        for log in logs[-5:]:  # 显示最后5条日志
            print(f"    {log}")
            
    except Exception as e:
        print(f"  错误: {e}")

def main():
    """
    主函数 - 演示包的初始化过程
    """
    print("Python包初始化过程演示")
    print("=" * 50)
    
    # 1. 演示初始化概念
    demonstrate_initialization_concepts()
    
    # 2. 创建演示包结构
    package_path = create_initialization_demo_structure()
    
    # 3. 演示初始化顺序
    demonstrate_initialization_order()
    
    # 4. 演示初始化控制
    demonstrate_initialization_control()
    
    # 5. 演示初始化状态
    demonstrate_initialization_state()
    
    # 6. 演示重新加载
    demonstrate_reloading()
    
    # 7. 演示最佳实践
    demonstrate_initialization_best_practices()
    
    # 8. 演示实际应用
    demonstrate_practical_example()
    
    print("\n=== 学习小结 ===")
    summary_points = [
        "1. 包的初始化在首次导入时执行，只执行一次",
        "2. 初始化顺序遵循父包->子包->模块的规则",
        "3. 使用延迟导入可以优化包的加载性能",
        "4. sys.modules记录了所有已导入的模块状态",
        "5. importlib.reload()可以重新加载模块",
        "6. 良好的初始化设计有助于包的性能和可维护性"
    ]
    
    for point in summary_points:
        print(point)
    
    print(f"\n示例包已创建在: {package_path}")
    print("可以通过导入init_demo包来观察初始化过程")

if __name__ == "__main__":
    main()