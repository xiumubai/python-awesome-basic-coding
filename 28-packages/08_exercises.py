#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python包管理 - 综合练习

本模块包含Python包管理的综合练习，涵盖所有重要知识点。

练习内容:
1. 包结构设计练习
2. 导入机制练习
3. 子包管理练习
4. 相对导入和绝对导入练习
5. 包初始化练习
6. 命名空间包练习
7. 实际项目练习
8. 问题解决练习

作者: Python学习助手
日期: 2024
"""

import os
import sys
import shutil
from pathlib import Path
import importlib
import importlib.util
import pkgutil
import time

class PackageExerciseManager:
    """
    包管理练习管理器
    """
    
    def __init__(self):
        self.exercise_dir = Path("package_exercises")
        self.completed_exercises = set()
        self.exercise_results = {}
        
    def setup_exercise_environment(self):
        """
        设置练习环境
        """
        print("=== 设置练习环境 ===")
        
        # 清理旧的练习目录
        if self.exercise_dir.exists():
            shutil.rmtree(self.exercise_dir)
            print(f"清理旧的练习目录: {self.exercise_dir}")
        
        # 创建新的练习目录
        self.exercise_dir.mkdir(exist_ok=True)
        print(f"创建练习目录: {self.exercise_dir.absolute()}")
        
        # 添加到Python路径
        exercise_path = str(self.exercise_dir.absolute())
        if exercise_path not in sys.path:
            sys.path.insert(0, exercise_path)
            print(f"添加到Python路径: {exercise_path}")
        
        print("练习环境设置完成\n")
    
    def record_result(self, exercise_name, success, details=None):
        """
        记录练习结果
        """
        self.exercise_results[exercise_name] = {
            "success": success,
            "details": details or {},
            "timestamp": time.time()
        }
        
        if success:
            self.completed_exercises.add(exercise_name)
            print(f"✅ 练习完成: {exercise_name}")
        else:
            print(f"❌ 练习失败: {exercise_name}")
            if details:
                print(f"   详情: {details}")

def exercise_1_basic_package_structure():
    """
    练习1: 基本包结构设计
    
    任务: 创建一个名为'myapp'的包，包含以下结构:
    myapp/
    ├── __init__.py
    ├── config.py
    ├── utils.py
    └── models/
        ├── __init__.py
        ├── user.py
        └── product.py
    """
    print("=== 练习1: 基本包结构设计 ===")
    print("任务: 创建一个完整的应用包结构")
    
    manager = PackageExerciseManager()
    manager.setup_exercise_environment()
    
    try:
        # 定义包结构
        package_structure = {
            "myapp": {
                "__init__.py": '''"""MyApp - 示例应用包"""

__version__ = "1.0.0"
__author__ = "练习者"

# 导入主要组件
from .config import Config
from .utils import Logger, Helper
from .models import User, Product

# 定义包的公共接口
__all__ = [
    "Config",
    "Logger", 
    "Helper",
    "User",
    "Product",
    "create_app"
]

def create_app(config_name="default"):
    """创建应用实例"""
    config = Config(config_name)
    logger = Logger("myapp")
    
    logger.info(f"创建应用实例 (配置: {config_name})")
    
    return {
        "config": config,
        "logger": logger,
        "version": __version__
    }

print(f"MyApp包已初始化 (版本: {__version__})")
''',
                "config.py": '''"""应用配置模块"""

class Config:
    """配置管理类"""
    
    def __init__(self, config_name="default"):
        self.config_name = config_name
        self.settings = self._load_config(config_name)
        print(f"加载配置: {config_name}")
    
    def _load_config(self, config_name):
        """加载配置"""
        configs = {
            "default": {
                "debug": False,
                "database_url": "sqlite:///app.db",
                "secret_key": "default-secret-key"
            },
            "development": {
                "debug": True,
                "database_url": "sqlite:///dev.db",
                "secret_key": "dev-secret-key"
            },
            "production": {
                "debug": False,
                "database_url": "postgresql://prod-db",
                "secret_key": "prod-secret-key"
            }
        }
        
        return configs.get(config_name, configs["default"])
    
    def get(self, key, default=None):
        """获取配置值"""
        return self.settings.get(key, default)
    
    def set(self, key, value):
        """设置配置值"""
        self.settings[key] = value
        print(f"设置配置: {key} = {value}")
    
    def get_all(self):
        """获取所有配置"""
        return self.settings.copy()

print("配置模块已加载")
''',
                "utils.py": '''"""工具模块"""
import time

class Logger:
    """日志记录器"""
    
    def __init__(self, name="app"):
        self.name = name
        self.logs = []
        print(f"创建日志器: {name}")
    
    def _log(self, level, message):
        """记录日志"""
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] [{self.name}] [{level}] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def info(self, message):
        """信息日志"""
        self._log("INFO", message)
    
    def warning(self, message):
        """警告日志"""
        self._log("WARNING", message)
    
    def error(self, message):
        """错误日志"""
        self._log("ERROR", message)
    
    def get_logs(self):
        """获取所有日志"""
        return self.logs.copy()

class Helper:
    """辅助工具类"""
    
    @staticmethod
    def format_size(size_bytes):
        """格式化文件大小"""
        if size_bytes == 0:
            return "0B"
        
        size_names = ["B", "KB", "MB", "GB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024.0
            i += 1
        
        return f"{size_bytes:.1f}{size_names[i]}"
    
    @staticmethod
    def validate_email(email):
        """简单的邮箱验证"""
        return "@" in email and "." in email
    
    @staticmethod
    def generate_id():
        """生成简单ID"""
        return int(time.time() * 1000) % 1000000

print("工具模块已加载")
''',
                "models": {
                    "__init__.py": '''"""模型包"""

# 导入所有模型
from .user import User
from .product import Product

# 定义模型包的公共接口
__all__ = ["User", "Product"]

print("模型包已初始化")
''',
                    "user.py": '''"""用户模型"""
from ..utils import Helper

class User:
    """用户类"""
    
    def __init__(self, username, email, password):
        self.id = Helper.generate_id()
        self.username = username
        self.email = email
        self.password = password  # 实际应用中应该加密
        self.created_at = time.time()
        self.active = True
        
        print(f"创建用户: {username} (ID: {self.id})")
    
    def validate(self):
        """验证用户数据"""
        errors = []
        
        if not self.username or len(self.username) < 3:
            errors.append("用户名至少3个字符")
        
        if not Helper.validate_email(self.email):
            errors.append("邮箱格式无效")
        
        if not self.password or len(self.password) < 6:
            errors.append("密码至少6个字符")
        
        return len(errors) == 0, errors
    
    def to_dict(self):
        """转换为字典"""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
            "active": self.active
        }
    
    def __str__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"

import time
print("用户模型已加载")
''',
                    "product.py": '''"""产品模型"""
from ..utils import Helper
import time

class Product:
    """产品类"""
    
    def __init__(self, name, price, description=""):
        self.id = Helper.generate_id()
        self.name = name
        self.price = price
        self.description = description
        self.created_at = time.time()
        self.available = True
        self.stock = 0
        
        print(f"创建产品: {name} (ID: {self.id}, 价格: ${price})")
    
    def set_stock(self, quantity):
        """设置库存"""
        self.stock = max(0, quantity)
        print(f"设置产品 {self.name} 库存: {self.stock}")
    
    def purchase(self, quantity=1):
        """购买产品"""
        if not self.available:
            return False, "产品不可用"
        
        if self.stock < quantity:
            return False, f"库存不足 (当前: {self.stock}, 需要: {quantity})"
        
        self.stock -= quantity
        print(f"购买产品 {self.name} x{quantity}, 剩余库存: {self.stock}")
        return True, "购买成功"
    
    def calculate_total(self, quantity):
        """计算总价"""
        return self.price * quantity
    
    def to_dict(self):
        """转换为字典"""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "created_at": self.created_at,
            "available": self.available,
            "stock": self.stock
        }
    
    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}', price=${self.price}, stock={self.stock})"

print("产品模型已加载")
'''
                }
            }
        }
        
        # 创建包结构
        def create_structure(base_path, structure):
            for name, content in structure.items():
                current_path = base_path / name
                
                if isinstance(content, dict):
                    current_path.mkdir(parents=True, exist_ok=True)
                    create_structure(current_path, content)
                else:
                    current_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(current_path, 'w', encoding='utf-8') as f:
                        f.write(content)
        
        create_structure(manager.exercise_dir, package_structure)
        
        # 测试包导入
        print("\n测试包导入:")
        import myapp
        
        # 测试创建应用
        app = myapp.create_app("development")
        print(f"应用版本: {app['version']}")
        
        # 测试模型
        user = myapp.User("testuser", "test@example.com", "password123")
        product = myapp.Product("测试产品", 99.99, "这是一个测试产品")
        product.set_stock(10)
        
        # 验证用户
        is_valid, errors = user.validate()
        print(f"用户验证: {'通过' if is_valid else '失败'}")
        if errors:
            print(f"错误: {errors}")
        
        # 测试购买
        success, message = product.purchase(2)
        print(f"购买结果: {message}")
        
        manager.record_result("exercise_1", True, {
            "package_created": True,
            "imports_working": True,
            "models_functional": True
        })
        
    except Exception as e:
        print(f"练习1失败: {e}")
        manager.record_result("exercise_1", False, {"error": str(e)})
    
    return manager

def exercise_2_import_mechanisms():
    """
    练习2: 导入机制练习
    
    任务: 演示不同的导入方式和最佳实践
    """
    print("\n=== 练习2: 导入机制练习 ===")
    print("任务: 掌握各种导入方式")
    
    manager = PackageExerciseManager()
    manager.setup_exercise_environment()
    
    try:
        # 创建测试包结构
        test_structure = {
            "importtest": {
                "__init__.py": '''"""导入测试包"""

# 包级别的变量
PACKAGE_VERSION = "1.0.0"
PACKAGE_NAME = "importtest"

# 导入子模块
from . import basic
from . import advanced
from .utils import calculator
from .utils.formatter import format_text

# 定义__all__
__all__ = [
    "basic",
    "advanced", 
    "calculator",
    "format_text",
    "PACKAGE_VERSION",
    "PACKAGE_NAME"
]

print(f"导入测试包已初始化 (版本: {PACKAGE_VERSION})")
''',
                "basic.py": '''"""基础模块"""

def add(a, b):
    """加法"""
    result = a + b
    print(f"基础加法: {a} + {b} = {result}")
    return result

def multiply(a, b):
    """乘法"""
    result = a * b
    print(f"基础乘法: {a} * {b} = {result}")
    return result

BASIC_CONSTANT = "这是基础模块的常量"

print("基础模块已加载")
''',
                "advanced.py": '''"""高级模块"""
from .basic import add, multiply

def power(base, exponent):
    """幂运算"""
    result = base ** exponent
    print(f"幂运算: {base} ^ {exponent} = {result}")
    return result

def factorial(n):
    """阶乘"""
    if n <= 1:
        return 1
    result = multiply(n, factorial(n - 1))
    print(f"阶乘: {n}! = {result}")
    return result

def complex_calculation(a, b, c):
    """复杂计算"""
    step1 = add(a, b)
    step2 = multiply(step1, c)
    step3 = power(step2, 2)
    print(f"复杂计算: ((({a} + {b}) * {c}) ^ 2) = {step3}")
    return step3

ADVANCED_CONSTANT = "这是高级模块的常量"

print("高级模块已加载")
''',
                "utils": {
                    "__init__.py": '''"""工具包"""

# 导入工具模块
from . import calculator
from . import formatter

# 重新导出常用功能
from .calculator import Calculator
from .formatter import format_text, format_number

__all__ = [
    "calculator",
    "formatter",
    "Calculator",
    "format_text",
    "format_number"
]

print("工具包已初始化")
''',
                    "calculator.py": '''"""计算器工具"""

class Calculator:
    """计算器类"""
    
    def __init__(self):
        self.history = []
        print("创建计算器实例")
    
    def calculate(self, expression):
        """计算表达式"""
        try:
            # 简单的表达式计算（实际应用中应该更安全）
            result = eval(expression)
            self.history.append(f"{expression} = {result}")
            print(f"计算: {expression} = {result}")
            return result
        except Exception as e:
            print(f"计算错误: {e}")
            return None
    
    def get_history(self):
        """获取计算历史"""
        return self.history.copy()
    
    def clear_history(self):
        """清空历史"""
        count = len(self.history)
        self.history.clear()
        print(f"清空计算历史 ({count} 条记录)")

# 模块级别函数
def quick_calc(expression):
    """快速计算"""
    calc = Calculator()
    return calc.calculate(expression)

print("计算器工具已加载")
''',
                    "formatter.py": '''"""格式化工具"""

def format_text(text, style="normal"):
    """格式化文本"""
    styles = {
        "upper": text.upper(),
        "lower": text.lower(),
        "title": text.title(),
        "reverse": text[::-1],
        "normal": text
    }
    
    result = styles.get(style, text)
    print(f"格式化文本: '{text}' -> '{result}' (样式: {style})")
    return result

def format_number(number, precision=2):
    """格式化数字"""
    if isinstance(number, float):
        result = f"{number:.{precision}f}"
    else:
        result = str(number)
    
    print(f"格式化数字: {number} -> {result}")
    return result

def format_currency(amount, currency="$"):
    """格式化货币"""
    result = f"{currency}{amount:.2f}"
    print(f"格式化货币: {amount} -> {result}")
    return result

print("格式化工具已加载")
'''
                }
            }
        }
        
        # 创建结构
        def create_structure(base_path, structure):
            for name, content in structure.items():
                current_path = base_path / name
                
                if isinstance(content, dict):
                    current_path.mkdir(parents=True, exist_ok=True)
                    create_structure(current_path, content)
                else:
                    current_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(current_path, 'w', encoding='utf-8') as f:
                        f.write(content)
        
        create_structure(manager.exercise_dir, test_structure)
        
        print("\n测试不同的导入方式:")
        
        # 1. 基本导入
        print("\n1. 基本导入:")
        import importtest
        print(f"包版本: {importtest.PACKAGE_VERSION}")
        
        # 2. from import
        print("\n2. from import:")
        from importtest import basic
        basic.add(5, 3)
        
        # 3. 导入特定函数
        print("\n3. 导入特定函数:")
        from importtest.basic import multiply
        multiply(4, 7)
        
        # 4. 别名导入
        print("\n4. 别名导入:")
        from importtest.advanced import power as pow_func
        pow_func(2, 8)
        
        # 5. 导入子包
        print("\n5. 导入子包:")
        from importtest.utils import Calculator
        calc = Calculator()
        calc.calculate("10 + 5 * 2")
        
        # 6. 星号导入（演示，但不推荐）
        print("\n6. 星号导入演示:")
        # 注意：这里只是演示概念，实际中要谨慎使用
        print("星号导入会导入__all__中定义的所有名称")
        print(f"importtest.__all__ = {importtest.__all__}")
        
        # 7. 动态导入
        print("\n7. 动态导入:")
        module_name = "importtest.utils.formatter"
        spec = importlib.util.find_spec(module_name)
        if spec:
            formatter_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(formatter_module)
            formatted = formatter_module.format_text("Hello World", "upper")
            print(f"动态导入结果: {formatted}")
        
        manager.record_result("exercise_2", True, {
            "basic_import": True,
            "from_import": True,
            "alias_import": True,
            "dynamic_import": True
        })
        
    except Exception as e:
        print(f"练习2失败: {e}")
        manager.record_result("exercise_2", False, {"error": str(e)})
    
    return manager

def exercise_3_relative_absolute_imports():
    """
    练习3: 相对导入和绝对导入练习
    
    任务: 理解和使用相对导入与绝对导入
    """
    print("\n=== 练习3: 相对导入和绝对导入练习 ===")
    print("任务: 掌握相对导入和绝对导入的使用")
    
    manager = PackageExerciseManager()
    manager.setup_exercise_environment()
    
    try:
        # 创建复杂的包结构来演示相对导入
        import_structure = {
            "webapp": {
                "__init__.py": '''"""Web应用包"""

# 使用绝对导入
from webapp.core.app import create_app
from webapp.core.config import Config
from webapp.utils.logger import Logger

__version__ = "1.0.0"

__all__ = ["create_app", "Config", "Logger", "__version__"]

print("Web应用包已初始化")
''',
                "core": {
                    "__init__.py": '''"""核心模块包"""

# 使用相对导入
from .app import create_app
from .config import Config
from .database import Database

__all__ = ["create_app", "Config", "Database"]

print("核心模块包已初始化")
''',
                    "app.py": '''"""应用核心模块"""

# 相对导入同级模块
from .config import Config
from .database import Database

# 相对导入上级包的模块
from ..utils.logger import Logger
from ..utils.helpers import format_response

# 绝对导入（作为对比）
# from webapp.utils.logger import Logger  # 这也是可以的

def create_app(config_name="default"):
    """创建应用实例"""
    print(f"\n创建应用实例 (配置: {config_name})")
    
    # 使用相对导入的模块
    config = Config(config_name)
    database = Database(config.get("database_url"))
    logger = Logger("webapp")
    
    # 连接数据库
    database.connect()
    
    # 记录日志
    logger.info(f"应用已创建 (配置: {config_name})")
    
    app_instance = {
        "config": config,
        "database": database,
        "logger": logger,
        "status": "running"
    }
    
    # 使用辅助函数格式化响应
    response = format_response("success", "应用创建成功", app_instance)
    print(f"应用创建响应: {response['message']}")
    
    return app_instance

print("应用核心模块已加载")
''',
                    "config.py": '''"""配置模块"""

# 相对导入工具模块
from ..utils.helpers import validate_config

class Config:
    """配置类"""
    
    def __init__(self, config_name="default"):
        self.config_name = config_name
        self.settings = self._load_config(config_name)
        
        # 验证配置
        is_valid, errors = validate_config(self.settings)
        if not is_valid:
            print(f"配置验证失败: {errors}")
        else:
            print(f"配置验证通过: {config_name}")
    
    def _load_config(self, config_name):
        """加载配置"""
        configs = {
            "default": {
                "debug": False,
                "database_url": "sqlite:///app.db",
                "secret_key": "default-key",
                "port": 5000
            },
            "development": {
                "debug": True,
                "database_url": "sqlite:///dev.db",
                "secret_key": "dev-key",
                "port": 5000
            },
            "testing": {
                "debug": True,
                "database_url": "sqlite:///:memory:",
                "secret_key": "test-key",
                "port": 5001
            }
        }
        
        return configs.get(config_name, configs["default"])
    
    def get(self, key, default=None):
        """获取配置值"""
        return self.settings.get(key, default)
    
    def update(self, updates):
        """更新配置"""
        self.settings.update(updates)
        print(f"配置已更新: {list(updates.keys())}")

print("配置模块已加载")
''',
                    "database.py": '''"""数据库模块"""

# 相对导入工具模块
from ..utils.logger import Logger

class Database:
    """数据库类"""
    
    def __init__(self, database_url):
        self.database_url = database_url
        self.connected = False
        self.logger = Logger("database")
        
        print(f"创建数据库实例: {database_url}")
    
    def connect(self):
        """连接数据库"""
        if not self.connected:
            self.connected = True
            self.logger.info(f"已连接到数据库: {self.database_url}")
            print(f"数据库连接成功: {self.database_url}")
        else:
            self.logger.warning("数据库已经连接")
    
    def disconnect(self):
        """断开数据库连接"""
        if self.connected:
            self.connected = False
            self.logger.info("数据库连接已断开")
            print("数据库连接已断开")
        else:
            self.logger.warning("数据库未连接")
    
    def execute_query(self, query):
        """执行查询"""
        if not self.connected:
            self.logger.error("数据库未连接，无法执行查询")
            return None
        
        self.logger.info(f"执行查询: {query}")
        # 模拟查询结果
        result = f"查询结果: {query} (模拟数据)"
        print(result)
        return result

print("数据库模块已加载")
'''
                },
                "utils": {
                    "__init__.py": '''"""工具包"""

# 使用相对导入
from .logger import Logger
from .helpers import format_response, validate_config

__all__ = ["Logger", "format_response", "validate_config"]

print("工具包已初始化")
''',
                    "logger.py": '''"""日志工具"""
import time

class Logger:
    """日志记录器"""
    
    def __init__(self, name="app"):
        self.name = name
        self.logs = []
        print(f"创建日志器: {name}")
    
    def _log(self, level, message):
        """记录日志"""
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] [{self.name}] [{level}] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def info(self, message):
        """信息日志"""
        self._log("INFO", message)
    
    def warning(self, message):
        """警告日志"""
        self._log("WARNING", message)
    
    def error(self, message):
        """错误日志"""
        self._log("ERROR", message)
    
    def get_logs(self):
        """获取日志"""
        return self.logs.copy()

print("日志工具已加载")
''',
                    "helpers.py": '''"""辅助工具"""

def format_response(status, message, data=None):
    """格式化响应"""
    response = {
        "status": status,
        "message": message,
        "timestamp": time.time()
    }
    
    if data is not None:
        response["data"] = data
    
    print(f"格式化响应: {status} - {message}")
    return response

def validate_config(config):
    """验证配置"""
    required_keys = ["database_url", "secret_key"]
    errors = []
    
    for key in required_keys:
        if key not in config:
            errors.append(f"缺少必需的配置项: {key}")
        elif not config[key]:
            errors.append(f"配置项不能为空: {key}")
    
    # 检查端口
    if "port" in config:
        port = config["port"]
        if not isinstance(port, int) or port < 1 or port > 65535:
            errors.append("端口必须是1-65535之间的整数")
    
    is_valid = len(errors) == 0
    print(f"配置验证: {'通过' if is_valid else '失败'}")
    
    return is_valid, errors

def format_size(size_bytes):
    """格式化文件大小"""
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f}{size_names[i]}"

import time
print("辅助工具已加载")
'''
                },
                "api": {
                    "__init__.py": '''"""API包"""

# 使用绝对导入引用其他包
from webapp.core import create_app
from webapp.utils import Logger

# 使用相对导入引用同级模块
from .routes import setup_routes
from .middleware import setup_middleware

__all__ = ["create_api_app", "setup_routes", "setup_middleware"]

def create_api_app(config_name="default"):
    """创建API应用"""
    print(f"\n创建API应用 (配置: {config_name})")
    
    # 创建基础应用
    app = create_app(config_name)
    
    # 设置路由
    routes = setup_routes()
    app["routes"] = routes
    
    # 设置中间件
    middleware = setup_middleware()
    app["middleware"] = middleware
    
    app["logger"].info("API应用已创建")
    
    return app

print("API包已初始化")
''',
                    "routes.py": '''"""路由模块"""

# 相对导入同包的模块
from .middleware import log_request

# 绝对导入其他包的模块
from webapp.utils.helpers import format_response
from webapp.utils.logger import Logger

def setup_routes():
    """设置路由"""
    logger = Logger("routes")
    
    routes = {
        "/": home_handler,
        "/api/status": status_handler,
        "/api/health": health_handler
    }
    
    logger.info(f"设置路由: {list(routes.keys())}")
    print(f"路由已设置: {len(routes)} 个")
    
    return routes

def home_handler(request):
    """首页处理器"""
    log_request("GET", "/")
    return format_response("success", "欢迎使用Web应用", {
        "version": "1.0.0",
        "endpoints": ["/", "/api/status", "/api/health"]
    })

def status_handler(request):
    """状态处理器"""
    log_request("GET", "/api/status")
    return format_response("success", "应用运行正常", {
        "status": "running",
        "uptime": "1 hour"
    })

def health_handler(request):
    """健康检查处理器"""
    log_request("GET", "/api/health")
    return format_response("success", "健康检查通过", {
        "database": "connected",
        "memory": "normal",
        "disk": "normal"
    })

print("路由模块已加载")
''',
                    "middleware.py": '''"""中间件模块"""

# 绝对导入
from webapp.utils.logger import Logger

def setup_middleware():
    """设置中间件"""
    logger = Logger("middleware")
    
    middleware = {
        "request_logger": log_request,
        "response_formatter": format_response_middleware,
        "error_handler": error_handler
    }
    
    logger.info(f"设置中间件: {list(middleware.keys())}")
    print(f"中间件已设置: {len(middleware)} 个")
    
    return middleware

def log_request(method, path):
    """请求日志中间件"""
    logger = Logger("request")
    logger.info(f"{method} {path}")
    print(f"请求日志: {method} {path}")

def format_response_middleware(response):
    """响应格式化中间件"""
    logger = Logger("response")
    logger.info(f"响应状态: {response.get('status', 'unknown')}")
    print(f"响应格式化: {response.get('status', 'unknown')}")
    return response

def error_handler(error):
    """错误处理中间件"""
    logger = Logger("error")
    logger.error(f"处理错误: {error}")
    print(f"错误处理: {error}")
    
    return {
        "status": "error",
        "message": "服务器内部错误",
        "error": str(error)
    }

print("中间件模块已加载")
'''
                }
            }
        }
        
        # 创建结构
        def create_structure(base_path, structure):
            for name, content in structure.items():
                current_path = base_path / name
                
                if isinstance(content, dict):
                    current_path.mkdir(parents=True, exist_ok=True)
                    create_structure(current_path, content)
                else:
                    current_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(current_path, 'w', encoding='utf-8') as f:
                        f.write(content)
        
        create_structure(manager.exercise_dir, import_structure)
        
        print("\n测试相对导入和绝对导入:")
        
        # 测试导入
        import webapp
        
        # 创建应用（这会触发各种导入）
        app = webapp.create_app("development")
        print(f"应用状态: {app['status']}")
        
        # 创建API应用（测试更复杂的导入关系）
        from webapp.api import create_api_app
        api_app = create_api_app("development")
        
        # 测试路由
        from webapp.api.routes import home_handler
        response = home_handler({"method": "GET", "path": "/"})
        print(f"路由测试: {response['message']}")
        
        # 断开数据库连接
        app["database"].disconnect()
        api_app["database"].disconnect()
        
        manager.record_result("exercise_3", True, {
            "relative_imports": True,
            "absolute_imports": True,
            "complex_structure": True,
            "cross_package_imports": True
        })
        
    except Exception as e:
        print(f"练习3失败: {e}")
        import traceback
        traceback.print_exc()
        manager.record_result("exercise_3", False, {"error": str(e)})
    
    return manager

def exercise_4_namespace_packages():
    """
    练习4: 命名空间包练习
    
    任务: 创建和使用命名空间包
    """
    print("\n=== 练习4: 命名空间包练习 ===")
    print("任务: 创建分布式命名空间包")
    
    manager = PackageExerciseManager()
    manager.setup_exercise_environment()
    
    try:
        # 创建多个路径的命名空间包
        namespace_paths = [
            manager.exercise_dir / "ns_path1",
            manager.exercise_dir / "ns_path2",
            manager.exercise_dir / "ns_path3"
        ]
        
        # 创建命名空间包结构（注意：没有__init__.py文件）
        namespace_structures = {
            "ns_path1": {
                "company": {
                    "core": {
                        "engine.py": '''"""核心引擎 - 来自path1"""

class Engine:
    """核心引擎类"""
    
    def __init__(self, name="Engine"):
        self.name = name
        self.version = "1.0.0"
        self.source = "path1"
        print(f"创建引擎: {name} (来自 {self.source})")
    
    def start(self):
        """启动引擎"""
        print(f"引擎 {self.name} 已启动")
        return True
    
    def stop(self):
        """停止引擎"""
        print(f"引擎 {self.name} 已停止")
        return True
    
    def get_info(self):
        """获取引擎信息"""
        return {
            "name": self.name,
            "version": self.version,
            "source": self.source
        }

print(f"核心引擎模块已加载 (来自 path1)")
'''
                    }
                }
            },
            "ns_path2": {
                "company": {
                    "plugins": {
                        "auth.py": '''"""认证插件 - 来自path2"""

class AuthPlugin:
    """认证插件类"""
    
    def __init__(self):
        self.name = "AuthPlugin"
        self.version = "1.0.0"
        self.source = "path2"
        self.users = {}
        print(f"加载认证插件 (来自 {self.source})")
    
    def register(self, username, password):
        """注册用户"""
        if username not in self.users:
            self.users[username] = password
            print(f"用户 {username} 注册成功")
            return True
        return False
    
    def authenticate(self, username, password):
        """认证用户"""
        if username in self.users and self.users[username] == password:
            print(f"用户 {username} 认证成功")
            return True
        print(f"用户 {username} 认证失败")
        return False
    
    def get_info(self):
        """获取插件信息"""
        return {
            "name": self.name,
            "version": self.version,
            "source": self.source,
            "users_count": len(self.users)
        }

print(f"认证插件已加载 (来自 path2)")
''',
                        "cache.py": '''"""缓存插件 - 来自path2"""

class CachePlugin:
    """缓存插件类"""
    
    def __init__(self, max_size=100):
        self.name = "CachePlugin"
        self.version = "1.0.0"
        self.source = "path2"
        self.max_size = max_size
        self.cache = {}
        print(f"加载缓存插件 (来自 {self.source}, 最大容量: {max_size})")
    
    def set(self, key, value):
        """设置缓存"""
        if len(self.cache) >= self.max_size:
            # 简单的清理策略
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
            print(f"缓存已满，清理最旧的键: {oldest_key}")
        
        self.cache[key] = value
        print(f"设置缓存: {key} = {value}")
    
    def get(self, key):
        """获取缓存"""
        value = self.cache.get(key)
        print(f"获取缓存: {key} = {value}")
        return value
    
    def clear(self):
        """清空缓存"""
        count = len(self.cache)
        self.cache.clear()
        print(f"清空缓存，共清理 {count} 个项目")
    
    def get_info(self):
        """获取插件信息"""
        return {
            "name": self.name,
            "version": self.version,
            "source": self.source,
            "size": len(self.cache),
            "max_size": self.max_size
        }

print(f"缓存插件已加载 (来自 path2)")
'''
                    }
                }
            },
            "ns_path3": {
                "company": {
                    "utils": {
                        "logger.py": '''"""日志工具 - 来自path3"""
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
''',
                        "helpers.py": '''"""辅助工具 - 来自path3"""

class Helper:
    """辅助工具类"""
    
    def __init__(self):
        self.source = "path3"
        self.operations_count = 0
        print(f"创建辅助工具 (来自 {self.source})")
    
    def format_text(self, text, style="normal"):
        """格式化文本"""
        self.operations_count += 1
        
        styles = {
            "upper": text.upper(),
            "lower": text.lower(),
            "title": text.title(),
            "reverse": text[::-1],
            "normal": text
        }
        
        result = styles.get(style, text)
        print(f"格式化文本: '{text}' -> '{result}' (操作#{self.operations_count})")
        return result
    
    def calculate_hash(self, text):
        """计算简单哈希"""
        self.operations_count += 1
        hash_value = hash(text) % 1000000
        print(f"计算哈希: '{text}' -> {hash_value} (操作#{self.operations_count})")
        return hash_value
    
    def get_stats(self):
        """获取统计信息"""
        return {
            "source": self.source,
            "operations_count": self.operations_count
        }

print(f"辅助工具已加载 (来自 path3)")
'''
                    }
                }
            }
        }
        
        # 创建命名空间包结构
        def create_namespace_structure(base_path, structure):
            for name, content in structure.items():
                current_path = base_path / name
                
                if isinstance(content, dict):
                    # 创建目录，但不创建__init__.py（这是命名空间包的特点）
                    current_path.mkdir(parents=True, exist_ok=True)
                    create_namespace_structure(current_path, content)
                else:
                    # 创建文件
                    current_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(current_path, 'w', encoding='utf-8') as f:
                        f.write(content)
        
        # 创建所有命名空间包路径
        for i, (path_name, structure) in enumerate(namespace_structures.items()):
            base_path = namespace_paths[i]
            print(f"\n创建 {path_name} 结构:")
            create_namespace_structure(base_path, structure)
        
        # 添加命名空间包路径到sys.path
        print("\n添加命名空间包路径:")
        for path in namespace_paths:
            abs_path = str(path.absolute())
            if abs_path not in sys.path:
                sys.path.insert(0, abs_path)
                print(f"  添加路径: {abs_path}")
        
        print("\n测试命名空间包导入:")
        
        # 导入命名空间包的各个部分
        print("\n1. 导入核心引擎 (来自path1):")
        from company.core import engine
        
        print("\n2. 导入插件 (来自path2):")
        from company.plugins import auth, cache
        
        print("\n3. 导入工具 (来自path3):")
        from company.utils import logger, helpers
        
        print("\n测试命名空间包使用:")
        
        # 使用核心引擎
        print("\n1. 使用核心引擎:")
        engine_instance = engine.Engine("测试引擎")
        engine_instance.start()
        engine_info = engine_instance.get_info()
        print(f"  引擎信息: {engine_info}")
        
        # 使用认证插件
        print("\n2. 使用认证插件:")
        auth_plugin = auth.AuthPlugin()
        auth_plugin.register("user1", "password123")
        auth_result = auth_plugin.authenticate("user1", "password123")
        auth_info = auth_plugin.get_info()
        print(f"  认证插件信息: {auth_info}")
        
        # 使用缓存插件
        print("\n3. 使用缓存插件:")
        cache_plugin = cache.CachePlugin(max_size=3)
        cache_plugin.set("key1", "value1")
        cache_plugin.set("key2", "value2")
        value = cache_plugin.get("key1")
        cache_info = cache_plugin.get_info()
        print(f"  缓存插件信息: {cache_info}")
        
        # 使用日志工具
        print("\n4. 使用日志工具:")
        logger_instance = logger.Logger("测试日志器")
        logger_instance.info("这是一条测试日志")
        logger_instance.warning("这是一条警告日志")
        logger_info = logger_instance.get_info()
        print(f"  日志器信息: {logger_info}")
        
        # 使用辅助工具
        print("\n5. 使用辅助工具:")
        helper_instance = helpers.Helper()
        formatted = helper_instance.format_text("Hello World", "upper")
        hash_value = helper_instance.calculate_hash("test string")
        helper_stats = helper_instance.get_stats()
        print(f"  辅助工具统计: {helper_stats}")
        
        # 发现命名空间包
        print("\n6. 发现命名空间包结构:")
        import company
        print(f"  命名空间包路径: {list(company.__path__)}")
        
        # 使用pkgutil遍历命名空间包
        print("\n  遍历命名空间包模块:")
        for importer, modname, ispkg in pkgutil.walk_packages(
            company.__path__, 
            company.__name__ + "."
        ):
            print(f"    模块: {modname}, 是包: {ispkg}")
        
        # 停止引擎
        engine_instance.stop()
        
        manager.record_result("exercise_4", True, {
            "namespace_package_created": True,
            "multiple_paths": True,
            "modules_imported": True,
            "functionality_tested": True
        })
        
    except Exception as e:
        print(f"练习4失败: {e}")
        manager.record_result("exercise_4", False, {"error": str(e)})
    
    return manager

def main():
    """
    主函数 - 运行所有练习
    """
    print("=== Python包管理综合练习 ===")
    print("本练习将帮助你掌握Python包管理的各个方面\n")
    
    # 运行所有练习
    exercises = [
        ("练习1: 基本包结构设计", exercise_1_basic_package_structure),
        ("练习2: 导入机制练习", exercise_2_import_mechanisms),
        ("练习3: 相对和绝对导入练习", exercise_3_relative_absolute_imports),
        ("练习4: 命名空间包练习", exercise_4_namespace_packages)
    ]
    
    results = {}
    
    for exercise_name, exercise_func in exercises:
        print(f"\n{'='*60}")
        print(f"开始 {exercise_name}")
        print(f"{'='*60}")
        
        try:
            manager = exercise_func()
            results[exercise_name] = manager.exercise_results
        except Exception as e:
            print(f"练习执行失败: {e}")
            results[exercise_name] = {"error": str(e)}
        
        print(f"\n{exercise_name} 完成")
    
    # 显示总结
    print(f"\n{'='*60}")
    print("练习总结")
    print(f"{'='*60}")
    
    total_exercises = len(exercises)
    completed_exercises = 0
    
    for exercise_name, result in results.items():
        if isinstance(result, dict) and any(r.get("success", False) for r in result.values()):
            completed_exercises += 1
            print(f"✅ {exercise_name}")
        else:
            print(f"❌ {exercise_name}")
    
    print(f"\n完成度: {completed_exercises}/{total_exercises} ({completed_exercises/total_exercises*100:.1f}%)")
    
    print("\n=== 学习小结 ===")
    print("通过这些练习，你应该掌握了:")
    print("1. 包的基本结构设计和创建")
    print("2. __init__.py文件的作用和使用")
    print("3. 不同的导入机制和最佳实践")
    print("4. 子包的创建和管理")
    print("5. 相对导入和绝对导入的区别")
    print("6. 包的初始化过程和控制")
    print("7. 命名空间包的概念和应用")
    print("8. 实际项目中的包管理策略")
    
    print("\n继续学习建议:")
    print("- 在实际项目中应用这些包管理技巧")
    print("- 学习更多高级的包管理工具(如setuptools, pip)")
    print("- 了解包的分发和发布流程")
    print("- 研究大型项目的包结构设计")
    
    print(f"\n练习文件创建在: {Path('package_exercises').absolute()}")

if __name__ == "__main__":
    main()