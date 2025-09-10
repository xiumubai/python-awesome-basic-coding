# 05. 模块重新加载机制

## 学习目标

- 理解Python模块缓存机制
- 掌握importlib.reload()的使用方法
- 学会处理模块重新加载的注意事项
- 了解动态模块更新的应用场景

## 模块缓存机制

Python使用`sys.modules`字典来缓存已导入的模块。当第一次导入模块时，Python会执行模块代码并将模块对象存储在缓存中。后续的导入操作直接从缓存中获取模块对象，不会重新执行模块代码。

## 基本重新加载

### 使用importlib.reload()

```python
import importlib
import sys
import os
import time
from pathlib import Path

def demonstrate_basic_reload():
    """演示基本的模块重新加载"""
    print("=== 基本模块重新加载演示 ===")
    
    # 创建测试模块
    test_module_path = '/tmp/reload_demo.py'
    
    # 第一个版本
    version1_content = '''
"""可重新加载的演示模块 - 版本1"""

VERSION = "1.0.0"
COUNTER = 0

def get_version():
    return f"模块版本: {VERSION}"

def increment_counter():
    global COUNTER
    COUNTER += 1
    return COUNTER

def get_message():
    return f"Hello from version {VERSION}! Counter: {COUNTER}"

print(f"模块加载: {__name__} (版本 {VERSION})")
'''
    
    with open(test_module_path, 'w') as f:
        f.write(version1_content)
    
    # 添加到搜索路径
    test_dir = os.path.dirname(test_module_path)
    if test_dir not in sys.path:
        sys.path.insert(0, test_dir)
    
    try:
        print("1. 首次导入模块:")
        import reload_demo
        print(f"   {reload_demo.get_version()}")
        print(f"   {reload_demo.get_message()}")
        print(f"   模块ID: {id(reload_demo)}")
        
        # 调用函数改变状态
        print(f"   调用increment_counter(): {reload_demo.increment_counter()}")
        print(f"   调用increment_counter(): {reload_demo.increment_counter()}")
        print(f"   当前状态: {reload_demo.get_message()}")
        
        # 修改模块文件
        print("\n2. 修改模块文件...")
        version2_content = '''
"""可重新加载的演示模块 - 版本2"""

VERSION = "2.0.0"
COUNTER = 100  # 重置计数器

def get_version():
    return f"模块版本: {VERSION} (已更新!)"

def increment_counter():
    global COUNTER
    COUNTER += 2  # 每次增加2
    return COUNTER

def get_message():
    return f"Hello from UPDATED version {VERSION}! Counter: {COUNTER}"

def new_function():
    return "这是新添加的函数!"

print(f"模块重新加载: {__name__} (版本 {VERSION})")
'''
        
        with open(test_module_path, 'w') as f:
            f.write(version2_content)
        
        # 重新导入（不会重新加载）
        print("\n3. 重新导入模块（不会重新加载）:")
        import reload_demo
        print(f"   {reload_demo.get_version()}")
        print(f"   {reload_demo.get_message()}")
        print(f"   模块ID: {id(reload_demo)}")
        
        # 使用importlib.reload重新加载
        print("\n4. 使用importlib.reload重新加载:")
        importlib.reload(reload_demo)
        print(f"   {reload_demo.get_version()}")
        print(f"   {reload_demo.get_message()}")
        print(f"   模块ID: {id(reload_demo)}")
        
        # 测试新函数
        if hasattr(reload_demo, 'new_function'):
            print(f"   新函数: {reload_demo.new_function()}")
        
        # 测试计数器
        print(f"   调用increment_counter(): {reload_demo.increment_counter()}")
        print(f"   调用increment_counter(): {reload_demo.increment_counter()}")
        
    except ImportError as e:
        print(f"导入失败: {e}")
    
    finally:
        # 清理
        if test_dir in sys.path:
            sys.path.remove(test_dir)
        if 'reload_demo' in sys.modules:
            del sys.modules['reload_demo']
        try:
            os.remove(test_module_path)
        except OSError:
            pass

def explore_sys_modules():
    """探索sys.modules缓存"""
    print("\n=== sys.modules缓存探索 ===")
    
    print(f"当前缓存的模块数量: {len(sys.modules)}")
    
    # 显示一些模块信息
    sample_modules = ['sys', 'os', 'json', 'importlib']
    
    for module_name in sample_modules:
        if module_name in sys.modules:
            module = sys.modules[module_name]
            print(f"{module_name}:")
            print(f"  对象: {module}")
            print(f"  ID: {id(module)}")
            print(f"  文件: {getattr(module, '__file__', 'N/A')}")
        else:
            print(f"{module_name}: 未缓存")
    
    # 演示缓存行为
    print("\n缓存行为演示:")
    import json
    json_from_cache = sys.modules['json']
    
    print(f"导入的json模块ID: {id(json)}")
    print(f"缓存中的json模块ID: {id(json_from_cache)}")
    print(f"是同一个对象: {json is json_from_cache}")

def demonstrate_reload_limitations():
    """演示重新加载的限制"""
    print("\n=== 重新加载限制演示 ===")
    
    # 创建测试模块
    test_module_path = '/tmp/reload_limits.py'
    
    original_content = '''
"""重新加载限制演示模块"""

class OriginalClass:
    def __init__(self, value):
        self.value = value
    
    def get_info(self):
        return f"Original class, value: {self.value}"

original_function = lambda x: x * 2

ORIGINAL_CONSTANT = "original"
'''
    
    with open(test_module_path, 'w') as f:
        f.write(original_content)
    
    test_dir = os.path.dirname(test_module_path)
    if test_dir not in sys.path:
        sys.path.insert(0, test_dir)
    
    try:
        # 导入并创建实例
        print("1. 导入模块并创建对象:")
        import reload_limits
        
        # 创建类实例
        obj1 = reload_limits.OriginalClass("test1")
        print(f"   对象1: {obj1.get_info()}")
        print(f"   类: {reload_limits.OriginalClass}")
        print(f"   函数: {reload_limits.original_function(5)}")
        
        # 保存引用
        old_class = reload_limits.OriginalClass
        old_function = reload_limits.original_function
        
        # 修改模块
        print("\n2. 修改模块内容...")
        modified_content = '''
"""重新加载限制演示模块 - 修改版"""

class OriginalClass:
    def __init__(self, value):
        self.value = value
        self.version = "modified"
    
    def get_info(self):
        return f"Modified class, value: {self.value}, version: {self.version}"
    
    def new_method(self):
        return "This is a new method!"

original_function = lambda x: x * 3  # 修改行为

ORIGINAL_CONSTANT = "modified"
NEW_CONSTANT = "added"
'''
        
        with open(test_module_path, 'w') as f:
            f.write(modified_content)
        
        # 重新加载
        print("\n3. 重新加载模块:")
        importlib.reload(reload_limits)
        
        print(f"   新类: {reload_limits.OriginalClass}")
        print(f"   新函数: {reload_limits.original_function(5)}")
        print(f"   新常量: {getattr(reload_limits, 'NEW_CONSTANT', 'N/A')}")
        
        # 测试现有对象
        print("\n4. 测试现有对象的行为:")
        print(f"   旧对象1: {obj1.get_info()}")
        print(f"   旧对象的类: {type(obj1)}")
        print(f"   旧对象的类是否为新类: {type(obj1) is reload_limits.OriginalClass}")
        
        # 测试新方法
        if hasattr(obj1, 'new_method'):
            print(f"   旧对象有新方法: {obj1.new_method()}")
        else:
            print("   旧对象没有新方法")
        
        # 创建新对象
        obj2 = reload_limits.OriginalClass("test2")
        print(f"   新对象: {obj2.get_info()}")
        if hasattr(obj2, 'new_method'):
            print(f"   新对象的新方法: {obj2.new_method()}")
        
        # 比较类和函数
        print("\n5. 比较旧引用和新引用:")
        print(f"   旧类 == 新类: {old_class is reload_limits.OriginalClass}")
        print(f"   旧函数 == 新函数: {old_function is reload_limits.original_function}")
        print(f"   旧函数结果: {old_function(5)}")
        print(f"   新函数结果: {reload_limits.original_function(5)}")
        
    except ImportError as e:
        print(f"导入失败: {e}")
    
    finally:
        # 清理
        if test_dir in sys.path:
            sys.path.remove(test_dir)
        if 'reload_limits' in sys.modules:
            del sys.modules['reload_limits']
        try:
            os.remove(test_module_path)
        except OSError:
            pass

def create_reloadable_module_system():
    """创建可重新加载的模块系统"""
    print("\n=== 可重新加载模块系统 ===")
    
    # 创建模块管理器
    class ModuleManager:
        def __init__(self):
            self.watched_modules = {}
            self.module_timestamps = {}
        
        def register_module(self, module_name, file_path):
            """注册要监控的模块"""
            self.watched_modules[module_name] = file_path
            if os.path.exists(file_path):
                self.module_timestamps[module_name] = os.path.getmtime(file_path)
            print(f"注册模块: {module_name} -> {file_path}")
        
        def check_for_changes(self):
            """检查模块文件是否有变化"""
            changed_modules = []
            
            for module_name, file_path in self.watched_modules.items():
                if not os.path.exists(file_path):
                    continue
                
                current_mtime = os.path.getmtime(file_path)
                last_mtime = self.module_timestamps.get(module_name, 0)
                
                if current_mtime > last_mtime:
                    changed_modules.append(module_name)
                    self.module_timestamps[module_name] = current_mtime
            
            return changed_modules
        
        def reload_changed_modules(self):
            """重新加载已更改的模块"""
            changed = self.check_for_changes()
            reloaded = []
            
            for module_name in changed:
                if module_name in sys.modules:
                    try:
                        importlib.reload(sys.modules[module_name])
                        reloaded.append(module_name)
                        print(f"✓ 重新加载模块: {module_name}")
                    except Exception as e:
                        print(f"✗ 重新加载失败 {module_name}: {e}")
            
            return reloaded
        
        def auto_reload_loop(self, interval=1.0, max_iterations=5):
            """自动重新加载循环"""
            print(f"开始自动重新加载监控 (间隔: {interval}秒)")
            
            for i in range(max_iterations):
                reloaded = self.reload_changed_modules()
                if reloaded:
                    print(f"第{i+1}次检查: 重新加载了 {len(reloaded)} 个模块")
                else:
                    print(f"第{i+1}次检查: 没有模块需要重新加载")
                
                if i < max_iterations - 1:
                    time.sleep(interval)
    
    # 创建测试模块
    test_module_path = '/tmp/auto_reload_test.py'
    
    initial_content = '''
"""自动重新加载测试模块"""

VERSION = 1

def get_data():
    return f"数据来自版本 {VERSION}"

class DataProcessor:
    def process(self, data):
        return f"处理数据: {data} (版本 {VERSION})"
'''
    
    with open(test_module_path, 'w') as f:
        f.write(initial_content)
    
    test_dir = os.path.dirname(test_module_path)
    if test_dir not in sys.path:
        sys.path.insert(0, test_dir)
    
    try:
        # 创建管理器并注册模块
        manager = ModuleManager()
        manager.register_module('auto_reload_test', test_module_path)
        
        # 导入模块
        import auto_reload_test
        processor = auto_reload_test.DataProcessor()
        
        print(f"初始版本: {auto_reload_test.get_data()}")
        print(f"处理结果: {processor.process('test')}")
        
        # 模拟文件修改
        print("\n模拟文件修改...")
        time.sleep(1.1)  # 确保时间戳不同
        
        updated_content = '''
"""自动重新加载测试模块 - 更新版"""

VERSION = 2

def get_data():
    return f"数据来自更新版本 {VERSION}!"

def get_extra_info():
    return "这是新增的功能"

class DataProcessor:
    def process(self, data):
        return f"高级处理数据: {data} (版本 {VERSION})"
    
    def advanced_process(self, data):
        return f"高级处理: {data.upper()}"
'''
        
        with open(test_module_path, 'w') as f:
            f.write(updated_content)
        
        # 检查并重新加载
        print("\n检查模块变化...")
        reloaded = manager.reload_changed_modules()
        
        if reloaded:
            print(f"更新后版本: {auto_reload_test.get_data()}")
            if hasattr(auto_reload_test, 'get_extra_info'):
                print(f"新功能: {auto_reload_test.get_extra_info()}")
            
            # 注意：现有对象不会自动更新
            print(f"旧处理器: {processor.process('test')}")
            
            # 创建新对象
            new_processor = auto_reload_test.DataProcessor()
            print(f"新处理器: {new_processor.process('test')}")
            if hasattr(new_processor, 'advanced_process'):
                print(f"高级处理: {new_processor.advanced_process('test')}")
    
    except ImportError as e:
        print(f"导入失败: {e}")
    
    finally:
        # 清理
        if test_dir in sys.path:
            sys.path.remove(test_dir)
        if 'auto_reload_test' in sys.modules:
            del sys.modules['auto_reload_test']
        try:
            os.remove(test_module_path)
        except OSError:
            pass

def demonstrate_package_reload():
    """演示包的重新加载"""
    print("\n=== 包重新加载演示 ===")
    
    # 创建包结构
    package_dir = '/tmp/reload_package'
    os.makedirs(package_dir, exist_ok=True)
    
    # 包的__init__.py
    init_content = '''
"""可重新加载的包"""

__version__ = "1.0.0"

from .module1 import function1
from .module2 import Class2

def package_info():
    return f"包版本: {__version__}"
'''
    
    init_path = os.path.join(package_dir, '__init__.py')
    with open(init_path, 'w') as f:
        f.write(init_content)
    
    # 模块1
    module1_content = '''
"""包中的模块1"""

def function1():
    return "来自模块1的函数 (版本1)"
'''
    
    module1_path = os.path.join(package_dir, 'module1.py')
    with open(module1_path, 'w') as f:
        f.write(module1_content)
    
    # 模块2
    module2_content = '''
"""包中的模块2"""

class Class2:
    def method(self):
        return "来自类2的方法 (版本1)"
'''
    
    module2_path = os.path.join(package_dir, 'module2.py')
    with open(module2_path, 'w') as f:
        f.write(module2_content)
    
    base_dir = os.path.dirname(package_dir)
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)
    
    try:
        print("1. 导入包:")
        import reload_package
        
        print(f"   包信息: {reload_package.package_info()}")
        print(f"   函数1: {reload_package.function1()}")
        
        obj = reload_package.Class2()
        print(f"   类2方法: {obj.method()}")
        
        # 修改模块1
        print("\n2. 修改模块1...")
        module1_updated = '''
"""包中的模块1 - 更新版"""

def function1():
    return "来自模块1的函数 (版本2 - 已更新!)"

def new_function():
    return "这是新增的函数"
'''
        
        with open(module1_path, 'w') as f:
            f.write(module1_updated)
        
        # 重新加载子模块
        print("\n3. 重新加载子模块:")
        importlib.reload(reload_package.module1)
        
        # 需要重新加载包来更新导入
        importlib.reload(reload_package)
        
        print(f"   更新后函数1: {reload_package.function1()}")
        
        # 检查新函数
        if hasattr(reload_package.module1, 'new_function'):
            print(f"   新函数: {reload_package.module1.new_function()}")
        
        # 旧对象仍然使用旧版本
        print(f"   旧对象方法: {obj.method()}")
        
        # 创建新对象
        new_obj = reload_package.Class2()
        print(f"   新对象方法: {new_obj.method()}")
        
    except ImportError as e:
        print(f"导入失败: {e}")
    
    finally:
        # 清理
        if base_dir in sys.path:
            sys.path.remove(base_dir)
        
        # 清理sys.modules中的包相关模块
        modules_to_remove = []
        for module_name in sys.modules:
            if module_name.startswith('reload_package'):
                modules_to_remove.append(module_name)
        
        for module_name in modules_to_remove:
            del sys.modules[module_name]
        
        # 清理文件
        import shutil
        try:
            shutil.rmtree(package_dir)
        except OSError:
            pass

def advanced_reload_techniques():
    """高级重新加载技术"""
    print("\n=== 高级重新加载技术 ===")
    
    # 1. 深度重新加载
    def deep_reload(module):
        """深度重新加载模块及其依赖"""
        print(f"深度重新加载: {module.__name__}")
        
        # 获取模块的依赖
        dependencies = []
        if hasattr(module, '__file__') and module.__file__:
            module_dir = os.path.dirname(module.__file__)
            
            # 查找同目录下的相关模块
            for name, mod in sys.modules.items():
                if (mod is not None and 
                    hasattr(mod, '__file__') and 
                    mod.__file__ and 
                    os.path.dirname(mod.__file__) == module_dir and
                    mod is not module):
                    dependencies.append(mod)
        
        # 重新加载依赖
        for dep in dependencies:
            try:
                importlib.reload(dep)
                print(f"  重新加载依赖: {dep.__name__}")
            except Exception as e:
                print(f"  依赖重新加载失败 {dep.__name__}: {e}")
        
        # 重新加载主模块
        try:
            importlib.reload(module)
            print(f"  重新加载主模块: {module.__name__}")
        except Exception as e:
            print(f"  主模块重新加载失败: {e}")
    
    # 2. 安全重新加载
    def safe_reload(module):
        """安全的模块重新加载"""
        print(f"安全重新加载: {module.__name__}")
        
        # 备份当前模块状态
        backup = {}
        for attr_name in dir(module):
            if not attr_name.startswith('_'):
                backup[attr_name] = getattr(module, attr_name)
        
        try:
            # 尝试重新加载
            importlib.reload(module)
            print(f"  ✓ 重新加载成功")
            return True
        except Exception as e:
            print(f"  ✗ 重新加载失败: {e}")
            
            # 恢复备份状态
            for attr_name, attr_value in backup.items():
                try:
                    setattr(module, attr_name, attr_value)
                except Exception:
                    pass
            
            print(f"  ✓ 已恢复到之前状态")
            return False
    
    # 3. 条件重新加载
    def conditional_reload(module, condition_func=None):
        """条件重新加载"""
        print(f"条件重新加载: {module.__name__}")
        
        if condition_func is None:
            # 默认条件：检查文件修改时间
            def condition_func(mod):
                if not hasattr(mod, '__file__') or not mod.__file__:
                    return False
                
                file_path = mod.__file__
                if not os.path.exists(file_path):
                    return False
                
                # 检查是否有缓存的修改时间
                cache_key = f"_reload_mtime_{mod.__name__}"
                current_mtime = os.path.getmtime(file_path)
                
                if hasattr(mod, cache_key):
                    last_mtime = getattr(mod, cache_key)
                    if current_mtime <= last_mtime:
                        return False
                
                # 更新缓存时间
                setattr(mod, cache_key, current_mtime)
                return True
        
        if condition_func(module):
            print(f"  条件满足，执行重新加载")
            return safe_reload(module)
        else:
            print(f"  条件不满足，跳过重新加载")
            return False
    
    # 演示高级技术
    print("演示高级重新加载技术:")
    
    # 创建测试模块
    test_module_path = '/tmp/advanced_reload.py'
    
    content = '''
"""高级重新加载测试模块"""

import time

VERSION = 1
LOAD_TIME = time.time()

def get_info():
    return f"版本 {VERSION}, 加载时间: {LOAD_TIME}"

class TestClass:
    def __init__(self):
        self.created_at = time.time()
    
    def info(self):
        return f"对象创建于: {self.created_at}"
'''
    
    with open(test_module_path, 'w') as f:
        f.write(content)
    
    test_dir = os.path.dirname(test_module_path)
    if test_dir not in sys.path:
        sys.path.insert(0, test_dir)
    
    try:
        import advanced_reload
        
        print(f"\n初始状态: {advanced_reload.get_info()}")
        
        # 测试安全重新加载
        print("\n测试安全重新加载:")
        safe_reload(advanced_reload)
        
        # 测试条件重新加载
        print("\n测试条件重新加载:")
        conditional_reload(advanced_reload)  # 第一次应该跳过
        
        # 修改文件后再测试
        time.sleep(1.1)
        with open(test_module_path, 'w') as f:
            f.write(content.replace('VERSION = 1', 'VERSION = 2'))
        
        conditional_reload(advanced_reload)  # 这次应该重新加载
        print(f"更新后状态: {advanced_reload.get_info()}")
        
    except ImportError as e:
        print(f"导入失败: {e}")
    
    finally:
        # 清理
        if test_dir in sys.path:
            sys.path.remove(test_dir)
        if 'advanced_reload' in sys.modules:
            del sys.modules['advanced_reload']
        try:
            os.remove(test_module_path)
        except OSError:
            pass

def reload_best_practices():
    """重新加载最佳实践"""
    print("\n=== 重新加载最佳实践 ===")
    
    practices = [
        "1. 谨慎使用重新加载",
        "   - 主要用于开发和调试阶段",
        "   - 生产环境中避免使用",
        "   - 考虑使用进程重启替代",
        "",
        "2. 理解重新加载的限制",
        "   - 现有对象不会自动更新",
        "   - 类实例保持旧的类定义",
        "   - 全局变量可能不会重置",
        "   - 某些C扩展模块无法重新加载",
        "",
        "3. 处理重新加载的副作用",
        "   - 备份重要状态",
        "   - 提供回滚机制",
        "   - 验证重新加载后的模块",
        "   - 处理异常情况",
        "",
        "4. 设计可重新加载的模块",
        "   - 避免模块级的副作用",
        "   - 使用函数和类封装功能",
        "   - 提供清理函数",
        "   - 支持状态迁移",
        "",
        "5. 替代方案",
        "   - 使用importlib.import_module动态导入",
        "   - 实现插件系统",
        "   - 使用配置文件热重载",
        "   - 考虑微服务架构",
    ]
    
    for practice in practices:
        print(practice)

def cleanup_functions():
    """清理函数示例"""
    print("\n=== 清理函数示例 ===")
    
    # 创建带清理功能的模块
    cleanup_module_path = '/tmp/cleanup_example.py'
    
    content = '''
"""带清理功能的模块示例"""

import atexit
import threading
import time

# 全局资源
_resources = []
_background_thread = None
_stop_event = threading.Event()

def initialize():
    """初始化模块资源"""
    global _background_thread
    
    print("初始化模块资源...")
    
    # 创建一些资源
    _resources.extend(["resource1", "resource2", "resource3"])
    
    # 启动后台线程
    _stop_event.clear()
    _background_thread = threading.Thread(target=_background_worker, daemon=True)
    _background_thread.start()
    
    print(f"初始化完成，资源数量: {len(_resources)}")

def _background_worker():
    """后台工作线程"""
    while not _stop_event.is_set():
        time.sleep(0.1)
        # 模拟工作

def cleanup():
    """清理模块资源"""
    global _resources, _background_thread
    
    print("清理模块资源...")
    
    # 停止后台线程
    _stop_event.set()
    if _background_thread and _background_thread.is_alive():
        _background_thread.join(timeout=1.0)
        print("后台线程已停止")
    
    # 清理资源
    _resources.clear()
    print("资源已清理")

def get_status():
    """获取模块状态"""
    return {
        "resources": len(_resources),
        "thread_alive": _background_thread.is_alive() if _background_thread else False
    }

# 注册清理函数
atexit.register(cleanup)

# 自动初始化
initialize()
'''
    
    with open(cleanup_module_path, 'w') as f:
        f.write(content)
    
    test_dir = os.path.dirname(cleanup_module_path)
    if test_dir not in sys.path:
        sys.path.insert(0, test_dir)
    
    try:
        print("导入带清理功能的模块:")
        import cleanup_example
        
        print(f"初始状态: {cleanup_example.get_status()}")
        
        # 手动清理
        print("\n手动清理:")
        cleanup_example.cleanup()
        print(f"清理后状态: {cleanup_example.get_status()}")
        
        # 重新初始化
        print("\n重新初始化:")
        cleanup_example.initialize()
        print(f"重新初始化后状态: {cleanup_example.get_status()}")
        
        # 重新加载测试
        print("\n重新加载测试:")
        cleanup_example.cleanup()  # 先清理
        importlib.reload(cleanup_example)  # 重新加载会自动初始化
        print(f"重新加载后状态: {cleanup_example.get_status()}")
        
    except ImportError as e:
        print(f"导入失败: {e}")
    
    finally:
        # 清理
        if 'cleanup_example' in sys.modules:
            # 确保清理
            try:
                sys.modules['cleanup_example'].cleanup()
            except Exception:
                pass
            del sys.modules['cleanup_example']
        
        if test_dir in sys.path:
            sys.path.remove(test_dir)
        
        try:
            os.remove(cleanup_module_path)
        except OSError:
            pass

if __name__ == '__main__':
    print("=== 模块重新加载机制演示 ===")
    
    # 执行所有演示
    demonstrate_basic_reload()
    explore_sys_modules()
    demonstrate_reload_limitations()
    create_reloadable_module_system()
    demonstrate_package_reload()
    advanced_reload_techniques()
    reload_best_practices()
    cleanup_functions()
    
    print("\n=== 演示完成 ===")
```

## 重新加载的注意事项

### 1. 现有对象不会更新

重新加载模块后，已经创建的对象实例仍然使用旧的类定义：

```python
# 重新加载前创建的对象
old_obj = MyClass()

# 重新加载模块
importlib.reload(my_module)

# 旧对象仍然使用旧的类定义
print(type(old_obj) is my_module.MyClass)  # False

# 新创建的对象使用新的类定义
new_obj = my_module.MyClass()
print(type(new_obj) is my_module.MyClass)  # True
```

### 2. 全局变量的处理

重新加载会重新执行模块代码，但某些全局状态可能需要特殊处理：

```python
# 模块中的全局变量
if 'initialized' not in globals():
    initialized = True
    setup_resources()
```

### 3. C扩展模块的限制

某些C扩展模块无法重新加载：

```python
try:
    importlib.reload(numpy)
except ImportError:
    print("C扩展模块无法重新加载")
```

## 实际应用场景

### 1. 开发环境热重载

```python
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ModuleReloadHandler(FileSystemEventHandler):
    def __init__(self, modules_to_reload):
        self.modules_to_reload = modules_to_reload
    
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            module_name = os.path.basename(event.src_path)[:-3]
            if module_name in self.modules_to_reload:
                try:
                    importlib.reload(sys.modules[module_name])
                    print(f"重新加载: {module_name}")
                except Exception as e:
                    print(f"重新加载失败: {e}")

# 使用文件监控实现自动重新加载
observer = Observer()
observer.schedule(ModuleReloadHandler(['my_module']), path='.', recursive=True)
observer.start()
```

### 2. 插件系统

```python
class PluginManager:
    def __init__(self):
        self.plugins = {}
    
    def load_plugin(self, plugin_name, plugin_path):
        spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.plugins[plugin_name] = module
    
    def reload_plugin(self, plugin_name):
        if plugin_name in self.plugins:
            importlib.reload(self.plugins[plugin_name])
    
    def unload_plugin(self, plugin_name):
        if plugin_name in self.plugins:
            # 执行清理
            if hasattr(self.plugins[plugin_name], 'cleanup'):
                self.plugins[plugin_name].cleanup()
            del self.plugins[plugin_name]
```

### 3. 配置热重载

```python
class ConfigManager:
    def __init__(self, config_module_name):
        self.config_module_name = config_module_name
        self.config = None
        self.load_config()
    
    def load_config(self):
        try:
            if self.config_module_name in sys.modules:
                importlib.reload(sys.modules[self.config_module_name])
            else:
                __import__(self.config_module_name)
            
            self.config = sys.modules[self.config_module_name]
        except ImportError as e:
            print(f"配置加载失败: {e}")
    
    def get_setting(self, key, default=None):
        return getattr(self.config, key, default)
    
    def reload_config(self):
        self.load_config()
```

## 学习要点

1. **理解缓存机制**：Python模块缓存在sys.modules中
2. **掌握重新加载方法**：使用importlib.reload()
3. **了解重新加载限制**：现有对象不会自动更新
4. **处理副作用**：设计可重新加载的模块
5. **实际应用场景**：开发调试、插件系统、配置管理
6. **最佳实践**：谨慎使用，提供清理机制

## 最佳实践

1. **开发阶段使用**：主要用于开发和调试
2. **避免生产使用**：生产环境考虑进程重启
3. **设计可重新加载模块**：避免副作用，提供清理函数
4. **处理状态迁移**：保存和恢复重要状态
5. **异常处理**：提供回滚机制
6. **测试重新加载**：确保重新加载后功能正常

通过理解模块重新加载机制，你可以在开发过程中更高效地调试和测试代码，同时避免重新加载可能带来的问题。