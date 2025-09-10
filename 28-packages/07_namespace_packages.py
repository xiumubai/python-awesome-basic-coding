#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python包管理 - 命名空间包

本模块演示Python命名空间包的概念、创建和使用方法。

学习目标:
1. 理解命名空间包的概念和用途
2. 掌握命名空间包的创建方法
3. 学会使用命名空间包组织代码
4. 了解命名空间包与普通包的区别

作者: Python学习助手
日期: 2024
"""

import os
import sys
from pathlib import Path
import importlib.util
import pkgutil

def demonstrate_namespace_concepts():
    """
    演示命名空间包的基本概念
    """
    print("=== 命名空间包基本概念 ===")
    
    concepts = {
        "什么是命名空间包": [
            "- 允许将包分布在多个目录中",
            "- 不需要__init__.py文件",
            "- 支持包的分布式开发",
            "- Python 3.3+原生支持(PEP 420)"
        ],
        "命名空间包的特点": [
            "- 没有__init__.py文件",
            "- 可以跨多个路径分布",
            "- 支持动态扩展",
            "- 适合插件系统开发"
        ],
        "与普通包的区别": [
            "- 普通包: 必须有__init__.py文件",
            "- 命名空间包: 不需要__init__.py文件",
            "- 普通包: 集中在一个目录",
            "- 命名空间包: 可以分布在多个目录"
        ],
        "使用场景": [
            "- 大型项目的模块化组织",
            "- 插件系统开发",
            "- 第三方扩展包",
            "- 分布式团队开发"
        ]
    }
    
    for concept, details in concepts.items():
        print(f"\n{concept}:")
        for detail in details:
            print(f"  {detail}")

def create_namespace_package_structure():
    """
    创建命名空间包演示结构
    """
    print("\n=== 创建命名空间包结构 ===")
    
    # 创建多个路径来演示命名空间包
    base_paths = [
        Path("namespace_demo/path1"),
        Path("namespace_demo/path2"),
        Path("namespace_demo/path3")
    ]
    
    # 定义命名空间包结构
    namespace_structures = {
        "path1": {
            "myproject": {
                "core": {
                    "engine.py": '''"""核心引擎模块 - 来自path1"""

class Engine:
    """核心引擎类"""
    
    def __init__(self, name="Engine"):
        self.name = name
        self.version = "1.0.0"
        self.source = "path1"
        print(f"创建引擎: {name} (来自 {self.source})")
    
    def start(self):
        """启动引擎"""
        print(f"引擎 {self.name} 已启动 (版本: {self.version})")
    
    def get_info(self):
        """获取引擎信息"""
        return {
            "name": self.name,
            "version": self.version,
            "source": self.source,
            "type": "core_engine"
        }

# 模块级别函数
def create_engine(name="默认引擎"):
    """创建引擎实例"""
    return Engine(name)

print(f"核心引擎模块已加载 (来自 path1)")
''',
                    "database.py": '''"""数据库模块 - 来自path1"""

class Database:
    """数据库连接类"""
    
    def __init__(self, host="localhost", port=5432):
        self.host = host
        self.port = port
        self.connected = False
        self.source = "path1"
        print(f"创建数据库连接: {host}:{port} (来自 {self.source})")
    
    def connect(self):
        """连接数据库"""
        if not self.connected:
            self.connected = True
            print(f"已连接到数据库 {self.host}:{self.port}")
        else:
            print("数据库已经连接")
    
    def disconnect(self):
        """断开数据库连接"""
        if self.connected:
            self.connected = False
            print(f"已断开数据库连接 {self.host}:{self.port}")
        else:
            print("数据库未连接")
    
    def execute(self, query):
        """执行查询"""
        if self.connected:
            print(f"执行查询: {query}")
            return f"查询结果: {query} (来自 {self.source})"
        else:
            print("数据库未连接，无法执行查询")
            return None

print(f"数据库模块已加载 (来自 path1)")
'''
                }
            }
        },
        "path2": {
            "myproject": {
                "utils": {
                    "logger.py": '''"""日志工具模块 - 来自path2"""
import time

class Logger:
    """日志记录器"""
    
    def __init__(self, name="Logger"):
        self.name = name
        self.messages = []
        self.source = "path2"
        print(f"创建日志器: {name} (来自 {self.source})")
    
    def log(self, level, message):
        """记录日志"""
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message} (来源: {self.source})"
        self.messages.append(log_entry)
        print(log_entry)
    
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

# 创建默认日志器
default_logger = Logger("default")

print(f"日志工具模块已加载 (来自 path2)")
''',
                    "helper.py": '''"""辅助工具模块 - 来自path2"""

class Helper:
    """辅助工具类"""
    
    def __init__(self):
        self.source = "path2"
        self.operations_count = 0
        print(f"创建辅助工具 (来自 {self.source})")
    
    def format_text(self, text, style="normal"):
        """格式化文本"""
        self.operations_count += 1
        
        if style == "upper":
            result = text.upper()
        elif style == "lower":
            result = text.lower()
        elif style == "title":
            result = text.title()
        elif style == "reverse":
            result = text[::-1]
        else:
            result = text
        
        print(f"格式化文本: '{text}' -> '{result}' (操作#{self.operations_count})")
        return result
    
    def calculate(self, operation, a, b):
        """简单计算"""
        self.operations_count += 1
        
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            result = a / b if b != 0 else None
        else:
            result = None
        
        print(f"计算: {a} {operation} {b} = {result} (操作#{self.operations_count})")
        return result
    
    def get_stats(self):
        """获取统计信息"""
        return {
            "source": self.source,
            "operations_count": self.operations_count
        }

print(f"辅助工具模块已加载 (来自 path2)")
'''
                }
            }
        },
        "path3": {
            "myproject": {
                "plugins": {
                    "auth.py": '''"""认证插件 - 来自path3"""

class AuthPlugin:
    """认证插件类"""
    
    def __init__(self):
        self.name = "AuthPlugin"
        self.version = "1.0.0"
        self.source = "path3"
        self.users = {}
        print(f"加载认证插件 (来自 {self.source})")
    
    def register(self, username, password):
        """注册用户"""
        if username not in self.users:
            self.users[username] = password
            print(f"用户 {username} 注册成功")
            return True
        else:
            print(f"用户 {username} 已存在")
            return False
    
    def login(self, username, password):
        """用户登录"""
        if username in self.users and self.users[username] == password:
            print(f"用户 {username} 登录成功")
            return True
        else:
            print(f"用户 {username} 登录失败")
            return False
    
    def get_info(self):
        """获取插件信息"""
        return {
            "name": self.name,
            "version": self.version,
            "source": self.source,
            "users_count": len(self.users)
        }

print(f"认证插件已加载 (来自 path3)")
''',
                    "cache.py": '''"""缓存插件 - 来自path3"""
import time

class CachePlugin:
    """缓存插件类"""
    
    def __init__(self, max_size=100):
        self.name = "CachePlugin"
        self.version = "1.0.0"
        self.source = "path3"
        self.max_size = max_size
        self.cache = {}
        self.access_times = {}
        print(f"加载缓存插件 (来自 {self.source}, 最大容量: {max_size})")
    
    def set(self, key, value, ttl=None):
        """设置缓存"""
        if len(self.cache) >= self.max_size:
            # 简单的LRU清理
            oldest_key = min(self.access_times.keys(), key=lambda k: self.access_times[k])
            del self.cache[oldest_key]
            del self.access_times[oldest_key]
            print(f"缓存已满，清理最旧的键: {oldest_key}")
        
        self.cache[key] = {
            "value": value,
            "created_time": time.time(),
            "ttl": ttl
        }
        self.access_times[key] = time.time()
        print(f"设置缓存: {key} = {value}")
    
    def get(self, key):
        """获取缓存"""
        if key in self.cache:
            item = self.cache[key]
            
            # 检查TTL
            if item["ttl"] and (time.time() - item["created_time"]) > item["ttl"]:
                del self.cache[key]
                del self.access_times[key]
                print(f"缓存已过期: {key}")
                return None
            
            # 更新访问时间
            self.access_times[key] = time.time()
            print(f"获取缓存: {key} = {item['value']}")
            return item["value"]
        else:
            print(f"缓存未找到: {key}")
            return None
    
    def clear(self):
        """清空缓存"""
        count = len(self.cache)
        self.cache.clear()
        self.access_times.clear()
        print(f"清空缓存，共清理 {count} 个项目")
    
    def get_stats(self):
        """获取缓存统计"""
        return {
            "name": self.name,
            "version": self.version,
            "source": self.source,
            "size": len(self.cache),
            "max_size": self.max_size
        }

print(f"缓存插件已加载 (来自 path3)")
'''
                }
            }
        }
    }
    
    def create_structure(base_path, structure):
        """递归创建目录结构"""
        for name, content in structure.items():
            current_path = base_path / name
            
            if isinstance(content, dict):
                # 创建目录(注意：命名空间包不创建__init__.py)
                current_path.mkdir(parents=True, exist_ok=True)
                print(f"创建命名空间目录: {current_path}")
                create_structure(current_path, content)
            else:
                # 创建文件
                current_path.parent.mkdir(parents=True, exist_ok=True)
                with open(current_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"创建模块文件: {current_path}")
    
    # 创建所有路径的结构
    for i, (path_name, structure) in enumerate(namespace_structures.items()):
        base_path = base_paths[i]
        print(f"\n创建 {path_name} 结构:")
        create_structure(base_path, structure)
    
    print(f"\n命名空间包结构创建完成")
    print("注意: 命名空间包目录中没有__init__.py文件")
    
    return [path.absolute() for path in base_paths]

def demonstrate_namespace_import():
    """
    演示命名空间包的导入
    """
    print("\n=== 命名空间包导入演示 ===")
    
    # 添加命名空间包路径到sys.path
    namespace_paths = [
        "namespace_demo/path1",
        "namespace_demo/path2", 
        "namespace_demo/path3"
    ]
    
    print("\n1. 添加命名空间包路径到sys.path:")
    for path in namespace_paths:
        abs_path = os.path.abspath(path)
        if abs_path not in sys.path:
            sys.path.insert(0, abs_path)
            print(f"  添加路径: {abs_path}")
    
    print("\n2. 导入命名空间包的各个部分:")
    try:
        # 导入来自path1的核心模块
        print("\n  导入核心引擎 (来自path1):")
        from myproject.core import engine
        
        # 导入来自path1的数据库模块
        print("\n  导入数据库模块 (来自path1):")
        from myproject.core import database
        
        # 导入来自path2的工具模块
        print("\n  导入日志工具 (来自path2):")
        from myproject.utils import logger
        
        # 导入来自path2的辅助工具
        print("\n  导入辅助工具 (来自path2):")
        from myproject.utils import helper
        
        # 导入来自path3的插件
        print("\n  导入认证插件 (来自path3):")
        from myproject.plugins import auth
        
        # 导入来自path3的缓存插件
        print("\n  导入缓存插件 (来自path3):")
        from myproject.plugins import cache
        
        print("\n  所有模块导入成功！")
        
        return {
            "engine": engine,
            "database": database,
            "logger": logger,
            "helper": helper,
            "auth": auth,
            "cache": cache
        }
        
    except ImportError as e:
        print(f"  导入错误: {e}")
        return None
    except Exception as e:
        print(f"  其他错误: {e}")
        return None

def demonstrate_namespace_usage(modules):
    """
    演示命名空间包的使用
    """
    print("\n=== 命名空间包使用演示 ===")
    
    if not modules:
        print("模块导入失败，无法演示使用")
        return
    
    try:
        print("\n1. 使用核心引擎:")
        # 创建引擎
        engine_instance = modules["engine"].create_engine("演示引擎")
        engine_instance.start()
        engine_info = engine_instance.get_info()
        print(f"  引擎信息: {engine_info}")
        
        print("\n2. 使用数据库连接:")
        # 创建数据库连接
        db = modules["database"].Database("localhost", 5432)
        db.connect()
        result = db.execute("SELECT * FROM users")
        print(f"  查询结果: {result}")
        
        print("\n3. 使用日志工具:")
        # 使用日志器
        logger_instance = modules["logger"].Logger("演示日志器")
        logger_instance.info("这是一条信息日志")
        logger_instance.warning("这是一条警告日志")
        
        print("\n4. 使用辅助工具:")
        # 使用辅助工具
        helper_instance = modules["helper"].Helper()
        formatted = helper_instance.format_text("Hello World", "upper")
        calc_result = helper_instance.calculate("multiply", 8, 9)
        helper_stats = helper_instance.get_stats()
        print(f"  辅助工具统计: {helper_stats}")
        
        print("\n5. 使用认证插件:")
        # 使用认证插件
        auth_plugin = modules["auth"].AuthPlugin()
        auth_plugin.register("user1", "password123")
        auth_plugin.login("user1", "password123")
        auth_info = auth_plugin.get_info()
        print(f"  认证插件信息: {auth_info}")
        
        print("\n6. 使用缓存插件:")
        # 使用缓存插件
        cache_plugin = modules["cache"].CachePlugin(max_size=5)
        cache_plugin.set("key1", "value1")
        cache_plugin.set("key2", "value2")
        value = cache_plugin.get("key1")
        cache_stats = cache_plugin.get_stats()
        print(f"  缓存插件统计: {cache_stats}")
        
        # 断开数据库连接
        db.disconnect()
        
    except Exception as e:
        print(f"使用过程中出错: {e}")

def demonstrate_namespace_discovery():
    """
    演示命名空间包的发现机制
    """
    print("\n=== 命名空间包发现机制 ===")
    
    print("\n1. 使用pkgutil发现命名空间包:")
    try:
        # 发现myproject命名空间包的所有部分
        import myproject
        
        print("\n  发现的命名空间包路径:")
        for path in myproject.__path__:
            print(f"    {path}")
        
        print("\n  遍历命名空间包的所有模块:")
        for importer, modname, ispkg in pkgutil.walk_packages(
            myproject.__path__, 
            myproject.__name__ + "."
        ):
            print(f"    模块: {modname}, 是包: {ispkg}")
            
    except Exception as e:
        print(f"  发现过程出错: {e}")
    
    print("\n2. 检查模块的来源路径:")
    try:
        import myproject.core.engine
        import myproject.utils.logger
        import myproject.plugins.auth
        
        modules_info = [
            ("myproject.core.engine", myproject.core.engine),
            ("myproject.utils.logger", myproject.utils.logger),
            ("myproject.plugins.auth", myproject.plugins.auth)
        ]
        
        for name, module in modules_info:
            if hasattr(module, '__file__'):
                print(f"    {name}: {module.__file__}")
            else:
                print(f"    {name}: 无文件路径信息")
                
    except Exception as e:
        print(f"  检查过程出错: {e}")

def demonstrate_namespace_best_practices():
    """
    演示命名空间包的最佳实践
    """
    print("\n=== 命名空间包最佳实践 ===")
    
    practices = {
        "1. 设计原则": [
            "- 使用清晰的命名空间层次结构",
            "- 避免在不同路径中创建同名模块",
            "- 保持模块间的松耦合",
            "- 提供清晰的文档说明"
        ],
        "2. 目录组织": [
            "- 按功能模块组织不同路径",
            "- 核心功能放在主路径",
            "- 插件和扩展放在独立路径",
            "- 工具和辅助功能分组管理"
        ],
        "3. 导入策略": [
            "- 明确配置sys.path",
            "- 使用绝对导入",
            "- 避免循环依赖",
            "- 提供导入辅助函数"
        ],
        "4. 版本管理": [
            "- 为每个部分维护独立版本",
            "- 确保版本兼容性",
            "- 提供版本检查机制",
            "- 文档化版本依赖关系"
        ],
        "5. 部署考虑": [
            "- 确保所有路径在部署环境中可用",
            "- 考虑包的安装顺序",
            "- 提供环境检查工具",
            "- 支持动态路径配置"
        ]
    }
    
    for category, items in practices.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  {item}")

def demonstrate_namespace_vs_regular():
    """
    演示命名空间包与普通包的对比
    """
    print("\n=== 命名空间包 vs 普通包对比 ===")
    
    comparison = {
        "特性": ["命名空间包", "普通包"],
        "__init__.py文件": ["不需要", "必须有"],
        "目录分布": ["可以分布在多个路径", "集中在一个目录"],
        "动态扩展": ["支持运行时扩展", "结构相对固定"],
        "导入机制": ["PEP 420机制", "传统导入机制"],
        "初始化控制": ["无集中初始化", "可在__init__.py中控制"],
        "包属性": ["__path__是列表", "__path__是字符串"],
        "适用场景": ["插件系统、分布式开发", "传统包组织"],
        "Python版本": ["3.3+", "所有版本"]
    }
    
    # 打印对比表格
    print(f"\n{'特性':<15} {'命名空间包':<25} {'普通包':<20}")
    print("-" * 65)
    
    features = list(comparison.keys())[1:]  # 跳过标题行
    for feature in features:
        namespace_val = comparison[feature][0]
        regular_val = comparison[feature][1]
        print(f"{feature:<15} {namespace_val:<25} {regular_val:<20}")

def create_namespace_utility():
    """
    创建命名空间包管理工具
    """
    print("\n=== 命名空间包管理工具 ===")
    
    utility_code = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""命名空间包管理工具"""

import sys
import os
from pathlib import Path
import pkgutil
import importlib.util

class NamespaceManager:
    """命名空间包管理器"""
    
    def __init__(self):
        self.namespace_paths = {}
    
    def add_namespace_path(self, namespace, path):
        """添加命名空间路径"""
        if namespace not in self.namespace_paths:
            self.namespace_paths[namespace] = []
        
        abs_path = os.path.abspath(path)
        if abs_path not in self.namespace_paths[namespace]:
            self.namespace_paths[namespace].append(abs_path)
            
            # 添加到sys.path
            if abs_path not in sys.path:
                sys.path.insert(0, abs_path)
                print(f"添加命名空间路径: {namespace} -> {abs_path}")
    
    def discover_modules(self, namespace):
        """发现命名空间中的所有模块"""
        if namespace not in self.namespace_paths:
            return []
        
        modules = []
        try:
            # 导入命名空间包
            ns_module = importlib.import_module(namespace)
            
            # 遍历所有模块
            for importer, modname, ispkg in pkgutil.walk_packages(
                ns_module.__path__, 
                ns_module.__name__ + "."
            ):
                modules.append({
                    "name": modname,
                    "is_package": ispkg,
                    "importer": str(importer)
                })
        except Exception as e:
            print(f"发现模块时出错: {e}")
        
        return modules
    
    def get_module_info(self, module_name):
        """获取模块详细信息"""
        try:
            module = importlib.import_module(module_name)
            return {
                "name": module.__name__,
                "file": getattr(module, "__file__", "无文件"),
                "package": getattr(module, "__package__", "无包信息"),
                "path": getattr(module, "__path__", "无路径信息")
            }
        except Exception as e:
            return {"error": str(e)}
    
    def list_namespaces(self):
        """列出所有管理的命名空间"""
        return dict(self.namespace_paths)

# 使用示例
if __name__ == "__main__":
    manager = NamespaceManager()
    
    # 添加命名空间路径
    manager.add_namespace_path("myproject", "namespace_demo/path1")
    manager.add_namespace_path("myproject", "namespace_demo/path2")
    manager.add_namespace_path("myproject", "namespace_demo/path3")
    
    # 发现模块
    modules = manager.discover_modules("myproject")
    print(f"发现的模块: {len(modules)}个")
    for module in modules:
        print(f"  {module['name']} ({'包' if module['is_package'] else '模块'})")
    
    # 获取模块信息
    if modules:
        first_module = modules[0]["name"]
        info = manager.get_module_info(first_module)
        print(f"\n模块信息 ({first_module}):")
        for key, value in info.items():
            print(f"  {key}: {value}")
'''
    
    # 创建工具文件
    utility_path = Path("namespace_utility.py")
    with open(utility_path, 'w', encoding='utf-8') as f:
        f.write(utility_code)
    
    print(f"\n命名空间包管理工具已创建: {utility_path.absolute()}")
    print("可以使用此工具来管理和发现命名空间包")

def main():
    """
    主函数 - 演示命名空间包
    """
    print("Python命名空间包演示")
    print("=" * 50)
    
    # 1. 演示基本概念
    demonstrate_namespace_concepts()
    
    # 2. 创建命名空间包结构
    namespace_paths = create_namespace_package_structure()
    
    # 3. 演示导入
    modules = demonstrate_namespace_import()
    
    # 4. 演示使用
    demonstrate_namespace_usage(modules)
    
    # 5. 演示发现机制
    demonstrate_namespace_discovery()
    
    # 6. 演示最佳实践
    demonstrate_namespace_best_practices()
    
    # 7. 对比普通包
    demonstrate_namespace_vs_regular()
    
    # 8. 创建管理工具
    create_namespace_utility()
    
    print("\n=== 学习小结 ===")
    summary_points = [
        "1. 命名空间包允许将包分布在多个目录中",
        "2. 命名空间包不需要__init__.py文件",
        "3. 使用sys.path配置命名空间包的搜索路径",
        "4. pkgutil可以用来发现命名空间包中的模块",
        "5. 命名空间包适合插件系统和分布式开发",
        "6. 需要Python 3.3+版本支持PEP 420标准"
    ]
    
    for point in summary_points:
        print(point)
    
    print(f"\n命名空间包示例已创建在: namespace_demo/")
    print("管理工具已创建: namespace_utility.py")

if __name__ == "__main__":
    main()