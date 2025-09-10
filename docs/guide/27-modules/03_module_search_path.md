# 03. 模块搜索路径机制

## 学习目标

- 理解Python模块搜索路径的工作原理
- 掌握sys.path的使用和修改方法
- 学会解决模块导入路径问题
- 了解PYTHONPATH环境变量的作用

## 模块搜索路径概述

当Python执行`import`语句时，解释器需要找到对应的模块文件。Python按照特定的顺序在一系列目录中搜索模块，这个搜索路径列表存储在`sys.path`中。

## sys.path详解

### 查看当前搜索路径

```python
import sys
import os
from pprint import pprint

def show_python_path():
    """显示Python模块搜索路径"""
    print("=== Python模块搜索路径 ===")
    print(f"总共 {len(sys.path)} 个路径:")
    print()
    
    for i, path in enumerate(sys.path, 1):
        # 检查路径是否存在
        exists = "✓" if os.path.exists(path) else "✗"
        # 检查路径类型
        if os.path.isfile(path):
            path_type = "文件"
        elif os.path.isdir(path):
            path_type = "目录"
        else:
            path_type = "不存在"
        
        print(f"{i:2d}. [{exists}] {path}")
        print(f"     类型: {path_type}")
        
        # 如果是目录，显示一些内容
        if os.path.isdir(path):
            try:
                contents = os.listdir(path)
                py_files = [f for f in contents if f.endswith('.py')][:3]
                if py_files:
                    print(f"     Python文件示例: {', '.join(py_files)}")
            except PermissionError:
                print(f"     权限不足，无法读取目录内容")
        print()

def analyze_path_sources():
    """分析路径来源"""
    print("=== 路径来源分析 ===")
    
    # 当前工作目录
    current_dir = os.getcwd()
    if current_dir in sys.path or '' in sys.path:
        print(f"✓ 当前工作目录: {current_dir}")
    
    # Python安装目录
    python_home = sys.prefix
    print(f"✓ Python安装目录: {python_home}")
    
    # 标准库目录
    import sysconfig
    stdlib_dir = sysconfig.get_path('stdlib')
    print(f"✓ 标准库目录: {stdlib_dir}")
    
    # site-packages目录
    site_packages = sysconfig.get_path('purelib')
    print(f"✓ site-packages目录: {site_packages}")
    
    # PYTHONPATH环境变量
    pythonpath = os.environ.get('PYTHONPATH')
    if pythonpath:
        print(f"✓ PYTHONPATH环境变量: {pythonpath}")
    else:
        print("✗ 未设置PYTHONPATH环境变量")
    
    print()

if __name__ == '__main__':
    show_python_path()
    analyze_path_sources()
```

### 搜索顺序详解

Python按以下顺序搜索模块：

```python
def explain_search_order():
    """解释模块搜索顺序"""
    print("=== Python模块搜索顺序 ===")
    print("1. 内置模块 (built-in modules)")
    print("   - 编译到Python解释器中的模块")
    print("   - 如: sys, os, math, json等")
    print()
    
    print("2. 当前目录 (current directory)")
    print("   - 脚本所在的目录")
    print("   - sys.path[0] 通常是当前目录或空字符串")
    print()
    
    print("3. PYTHONPATH环境变量指定的目录")
    print("   - 用户自定义的模块搜索路径")
    print("   - 可以包含多个目录，用冒号(:)分隔")
    print()
    
    print("4. Python标准库目录")
    print("   - Python安装时自带的标准库模块")
    print("   - 通常在Python安装目录下的lib/python3.x/")
    print()
    
    print("5. site-packages目录")
    print("   - 第三方包的安装目录")
    print("   - pip安装的包通常放在这里")
    print()
    
    print("6. .pth文件指定的目录")
    print("   - 通过.pth文件添加的额外路径")
    print("   - 通常在site-packages目录中")
    print()

def demonstrate_search_process(module_name):
    """演示模块搜索过程"""
    import importlib.util
    
    print(f"=== 搜索模块 '{module_name}' 的过程 ===")
    
    # 检查是否是内置模块
    if module_name in sys.builtin_module_names:
        print(f"✓ '{module_name}' 是内置模块")
        return
    
    # 使用importlib查找模块
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        print(f"✗ 模块 '{module_name}' 未找到")
        return
    
    print(f"✓ 找到模块 '{module_name}'")
    print(f"  位置: {spec.origin}")
    print(f"  类型: {type(spec.loader).__name__}")
    
    # 确定模块在哪个搜索路径中
    if spec.origin:
        module_dir = os.path.dirname(spec.origin)
        for i, path in enumerate(sys.path):
            if path and os.path.commonpath([module_dir, path]) == path:
                print(f"  搜索路径索引: {i}")
                print(f"  搜索路径: {path}")
                break
    print()

if __name__ == '__main__':
    explain_search_order()
    
    # 演示几个模块的搜索过程
    test_modules = ['sys', 'os', 'math', 'json', 'requests', 'numpy']
    for module in test_modules:
        demonstrate_search_process(module)
```

## 修改搜索路径

### 动态添加路径

```python
import sys
import os

def add_to_path(new_path, position='end'):
    """添加路径到sys.path"""
    # 转换为绝对路径
    abs_path = os.path.abspath(new_path)
    
    # 检查路径是否存在
    if not os.path.exists(abs_path):
        print(f"警告: 路径不存在 - {abs_path}")
        return False
    
    # 检查是否已经在路径中
    if abs_path in sys.path:
        print(f"路径已存在于sys.path中: {abs_path}")
        return True
    
    # 添加路径
    if position == 'start':
        sys.path.insert(0, abs_path)
        print(f"已将路径添加到开头: {abs_path}")
    else:
        sys.path.append(abs_path)
        print(f"已将路径添加到末尾: {abs_path}")
    
    return True

def remove_from_path(path_to_remove):
    """从sys.path中移除路径"""
    abs_path = os.path.abspath(path_to_remove)
    
    if abs_path in sys.path:
        sys.path.remove(abs_path)
        print(f"已从sys.path中移除: {abs_path}")
        return True
    else:
        print(f"路径不在sys.path中: {abs_path}")
        return False

def clean_path():
    """清理sys.path中的无效路径"""
    print("=== 清理sys.path ===")
    original_count = len(sys.path)
    
    # 移除不存在的路径
    valid_paths = []
    removed_paths = []
    
    for path in sys.path:
        if path == '' or os.path.exists(path):
            valid_paths.append(path)
        else:
            removed_paths.append(path)
    
    sys.path[:] = valid_paths
    
    print(f"原始路径数量: {original_count}")
    print(f"清理后路径数量: {len(sys.path)}")
    print(f"移除的路径数量: {len(removed_paths)}")
    
    if removed_paths:
        print("移除的路径:")
        for path in removed_paths:
            print(f"  - {path}")
    
    return removed_paths

def backup_and_restore_path():
    """备份和恢复sys.path"""
    # 备份当前路径
    original_path = sys.path.copy()
    print(f"已备份sys.path，包含 {len(original_path)} 个路径")
    
    # 修改路径（示例）
    sys.path.append('/tmp/test_path')
    print(f"修改后sys.path包含 {len(sys.path)} 个路径")
    
    # 恢复路径
    sys.path[:] = original_path
    print(f"已恢复sys.path，包含 {len(sys.path)} 个路径")

# 测试路径修改功能
if __name__ == '__main__':
    print("=== 路径修改测试 ===")
    
    # 显示当前路径数量
    print(f"当前sys.path包含 {len(sys.path)} 个路径")
    
    # 添加测试路径
    test_paths = [
        '/tmp',  # 通常存在的路径
        '/nonexistent/path',  # 不存在的路径
        os.path.expanduser('~'),  # 用户主目录
    ]
    
    for path in test_paths:
        add_to_path(path)
    
    print(f"\n添加后sys.path包含 {len(sys.path)} 个路径")
    
    # 清理无效路径
    clean_path()
    
    # 备份和恢复测试
    backup_and_restore_path()
```

### 使用上下文管理器临时修改路径

```python
import sys
import os
from contextlib import contextmanager

@contextmanager
def temporary_path(new_path):
    """临时添加路径到sys.path的上下文管理器"""
    abs_path = os.path.abspath(new_path)
    original_path = sys.path.copy()
    
    try:
        if abs_path not in sys.path:
            sys.path.insert(0, abs_path)
            print(f"临时添加路径: {abs_path}")
        yield abs_path
    finally:
        sys.path[:] = original_path
        print(f"已恢复原始路径")

@contextmanager
def isolated_path(paths=None):
    """创建隔离的模块搜索环境"""
    original_path = sys.path.copy()
    
    try:
        if paths is None:
            # 只保留内置模块路径
            sys.path = [path for path in sys.path if not path or 'site-packages' not in path]
        else:
            sys.path = list(paths)
        
        print(f"创建隔离环境，路径数量: {len(sys.path)}")
        yield sys.path
    finally:
        sys.path[:] = original_path
        print("已恢复原始路径")

def test_temporary_path():
    """测试临时路径功能"""
    print("=== 临时路径测试 ===")
    
    print(f"原始路径数量: {len(sys.path)}")
    
    # 使用临时路径
    with temporary_path('/tmp'):
        print(f"临时路径环境中的路径数量: {len(sys.path)}")
        print(f"第一个路径: {sys.path[0]}")
        
        # 在这里可以导入临时路径中的模块
        try:
            # 假设在/tmp中有一个test_module.py
            # import test_module
            pass
        except ImportError:
            print("临时路径中没有可导入的模块")
    
    print(f"恢复后路径数量: {len(sys.path)}")

def test_isolated_environment():
    """测试隔离环境"""
    print("\n=== 隔离环境测试 ===")
    
    print(f"原始路径数量: {len(sys.path)}")
    
    # 创建隔离环境
    with isolated_path(['', sys.prefix + '/lib/python3.9']):
        print(f"隔离环境路径数量: {len(sys.path)}")
        
        # 测试在隔离环境中导入模块
        try:
            import math  # 标准库模块应该可用
            print("✓ 可以导入标准库模块 math")
        except ImportError:
            print("✗ 无法导入标准库模块 math")
        
        try:
            import requests  # 第三方模块可能不可用
            print("✓ 可以导入第三方模块 requests")
        except ImportError:
            print("✗ 无法导入第三方模块 requests（预期行为）")
    
    print(f"恢复后路径数量: {len(sys.path)}")

if __name__ == '__main__':
    test_temporary_path()
    test_isolated_environment()
```

## PYTHONPATH环境变量

### 设置和使用PYTHONPATH

```python
import os
import sys
import subprocess

def show_pythonpath():
    """显示PYTHONPATH环境变量"""
    print("=== PYTHONPATH环境变量 ===")
    
    pythonpath = os.environ.get('PYTHONPATH')
    if pythonpath:
        print(f"PYTHONPATH: {pythonpath}")
        
        # 分解路径
        paths = pythonpath.split(os.pathsep)
        print(f"包含 {len(paths)} 个路径:")
        for i, path in enumerate(paths, 1):
            exists = "✓" if os.path.exists(path) else "✗"
            print(f"  {i}. [{exists}] {path}")
    else:
        print("未设置PYTHONPATH环境变量")
    
    print()

def set_pythonpath_example():
    """演示如何设置PYTHONPATH"""
    print("=== 设置PYTHONPATH示例 ===")
    
    # 在Python中临时设置
    original_pythonpath = os.environ.get('PYTHONPATH', '')
    
    new_paths = [
        '/path/to/my/modules',
        '/another/path/to/modules',
        os.path.expanduser('~/my_python_modules')
    ]
    
    # 构建新的PYTHONPATH
    if original_pythonpath:
        new_pythonpath = os.pathsep.join(new_paths + [original_pythonpath])
    else:
        new_pythonpath = os.pathsep.join(new_paths)
    
    print(f"新的PYTHONPATH: {new_pythonpath}")
    
    # 临时设置环境变量
    os.environ['PYTHONPATH'] = new_pythonpath
    
    print("\n在shell中设置PYTHONPATH的方法:")
    print("# Bash/Zsh:")
    print(f"export PYTHONPATH='{new_pythonpath}'")
    print("\n# Windows CMD:")
    print(f"set PYTHONPATH={new_pythonpath}")
    print("\n# Windows PowerShell:")
    print(f"$env:PYTHONPATH='{new_pythonpath}'")
    
    # 恢复原始值
    if original_pythonpath:
        os.environ['PYTHONPATH'] = original_pythonpath
    else:
        os.environ.pop('PYTHONPATH', None)

def test_pythonpath_effect():
    """测试PYTHONPATH的效果"""
    print("\n=== PYTHONPATH效果测试 ===")
    
    # 创建测试目录和模块
    test_dir = '/tmp/test_pythonpath'
    os.makedirs(test_dir, exist_ok=True)
    
    # 创建测试模块
    test_module_content = '''
"""测试模块"""

def hello():
    return "Hello from test module!"

TEST_CONSTANT = "This is a test constant"
'''
    
    test_module_path = os.path.join(test_dir, 'test_module.py')
    with open(test_module_path, 'w') as f:
        f.write(test_module_content)
    
    print(f"创建测试模块: {test_module_path}")
    
    # 测试不同的导入方式
    print("\n1. 不设置PYTHONPATH时:")
    try:
        import test_module
        print("✓ 成功导入test_module")
    except ImportError:
        print("✗ 无法导入test_module（预期行为）")
    
    print("\n2. 添加到sys.path后:")
    if test_dir not in sys.path:
        sys.path.insert(0, test_dir)
    
    try:
        import importlib
        if 'test_module' in sys.modules:
            importlib.reload(sys.modules['test_module'])
        else:
            import test_module
        print("✓ 成功导入test_module")
        print(f"  模块位置: {test_module.__file__}")
        print(f"  测试函数: {test_module.hello()}")
    except ImportError as e:
        print(f"✗ 无法导入test_module: {e}")
    
    # 清理
    if test_dir in sys.path:
        sys.path.remove(test_dir)
    
    # 清理测试文件
    try:
        os.remove(test_module_path)
        os.rmdir(test_dir)
        print(f"\n清理测试文件: {test_module_path}")
    except OSError:
        pass

if __name__ == '__main__':
    show_pythonpath()
    set_pythonpath_example()
    test_pythonpath_effect()
```

## 包和模块的搜索

### 包的搜索机制

```python
import os
import sys
import importlib.util

def find_package_path(package_name):
    """查找包的路径"""
    print(f"=== 查找包 '{package_name}' ===")
    
    # 使用importlib查找
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        print(f"✗ 包 '{package_name}' 未找到")
        return None
    
    print(f"✓ 找到包 '{package_name}'")
    
    if spec.origin:
        print(f"  __init__.py位置: {spec.origin}")
        package_dir = os.path.dirname(spec.origin)
        print(f"  包目录: {package_dir}")
    elif spec.submodule_search_locations:
        print(f"  包搜索位置: {spec.submodule_search_locations}")
        package_dir = spec.submodule_search_locations[0]
    else:
        print(f"  内置包或特殊包")
        return None
    
    # 显示包内容
    if os.path.isdir(package_dir):
        contents = os.listdir(package_dir)
        py_files = [f for f in contents if f.endswith('.py')]
        subdirs = [d for d in contents if os.path.isdir(os.path.join(package_dir, d))]
        
        print(f"  Python文件: {len(py_files)}")
        if py_files[:5]:  # 显示前5个
            print(f"    示例: {', '.join(py_files[:5])}")
        
        print(f"  子目录: {len(subdirs)}")
        if subdirs[:5]:  # 显示前5个
            print(f"    示例: {', '.join(subdirs[:5])}")
    
    return package_dir

def demonstrate_package_search():
    """演示包搜索过程"""
    print("=== 包搜索演示 ===")
    
    # 测试不同类型的包
    packages_to_test = [
        'os',           # 标准库模块
        'json',         # 标准库模块
        'email',        # 标准库包
        'urllib',       # 标准库包
        'xml',          # 标准库包
        'collections',  # 标准库模块
        'numpy',        # 第三方包（如果安装了）
        'requests',     # 第三方包（如果安装了）
    ]
    
    for package in packages_to_test:
        find_package_path(package)
        print()

def create_test_package():
    """创建测试包结构"""
    print("=== 创建测试包 ===")
    
    # 创建包目录结构
    base_dir = '/tmp/test_package_search'
    package_dir = os.path.join(base_dir, 'mypackage')
    subpackage_dir = os.path.join(package_dir, 'subpackage')
    
    # 创建目录
    os.makedirs(subpackage_dir, exist_ok=True)
    
    # 创建__init__.py文件
    init_files = [
        os.path.join(package_dir, '__init__.py'),
        os.path.join(subpackage_dir, '__init__.py')
    ]
    
    for init_file in init_files:
        with open(init_file, 'w') as f:
            f.write(f'"""测试包 - {os.path.dirname(init_file)}"""\n')
            f.write(f'__version__ = "1.0.0"\n')
    
    # 创建模块文件
    module_file = os.path.join(package_dir, 'module1.py')
    with open(module_file, 'w') as f:
        f.write('"""测试模块"""\n')
        f.write('def test_function():\n')
        f.write('    return "Hello from module1!"\n')
    
    submodule_file = os.path.join(subpackage_dir, 'submodule.py')
    with open(submodule_file, 'w') as f:
        f.write('"""测试子模块"""\n')
        f.write('def sub_function():\n')
        f.write('    return "Hello from submodule!"\n')
    
    print(f"创建测试包结构:")
    print(f"  {package_dir}/")
    print(f"    __init__.py")
    print(f"    module1.py")
    print(f"    subpackage/")
    print(f"      __init__.py")
    print(f"      submodule.py")
    
    return base_dir

def test_package_import(base_dir):
    """测试包导入"""
    print("\n=== 测试包导入 ===")
    
    # 添加到搜索路径
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)
    
    try:
        # 导入包
        import mypackage
        print(f"✓ 成功导入包 mypackage")
        print(f"  包位置: {mypackage.__file__}")
        print(f"  包版本: {mypackage.__version__}")
        
        # 导入模块
        from mypackage import module1
        print(f"✓ 成功导入模块 module1")
        print(f"  模块函数: {module1.test_function()}")
        
        # 导入子包
        from mypackage.subpackage import submodule
        print(f"✓ 成功导入子模块 submodule")
        print(f"  子模块函数: {submodule.sub_function()}")
        
    except ImportError as e:
        print(f"✗ 导入失败: {e}")
    
    # 清理
    if base_dir in sys.path:
        sys.path.remove(base_dir)

def cleanup_test_package(base_dir):
    """清理测试包"""
    import shutil
    try:
        shutil.rmtree(base_dir)
        print(f"\n清理测试包: {base_dir}")
    except OSError:
        pass

if __name__ == '__main__':
    demonstrate_package_search()
    
    # 创建和测试自定义包
    test_base_dir = create_test_package()
    test_package_import(test_base_dir)
    cleanup_test_package(test_base_dir)
```

## 模块缓存机制

### sys.modules详解

```python
import sys
import importlib
from pprint import pprint

def explore_module_cache():
    """探索模块缓存"""
    print("=== 模块缓存探索 ===")
    
    print(f"当前缓存的模块数量: {len(sys.modules)}")
    
    # 按类型分类模块
    builtin_modules = []
    stdlib_modules = []
    third_party_modules = []
    local_modules = []
    
    for name, module in sys.modules.items():
        if module is None:
            continue
            
        if name in sys.builtin_module_names:
            builtin_modules.append(name)
        elif hasattr(module, '__file__') and module.__file__:
            if 'site-packages' in module.__file__:
                third_party_modules.append(name)
            elif sys.prefix in module.__file__:
                stdlib_modules.append(name)
            else:
                local_modules.append(name)
    
    print(f"\n模块分类:")
    print(f"  内置模块: {len(builtin_modules)}")
    print(f"  标准库模块: {len(stdlib_modules)}")
    print(f"  第三方模块: {len(third_party_modules)}")
    print(f"  本地模块: {len(local_modules)}")
    
    # 显示一些示例
    print(f"\n内置模块示例: {builtin_modules[:5]}")
    print(f"标准库模块示例: {stdlib_modules[:5]}")
    if third_party_modules:
        print(f"第三方模块示例: {third_party_modules[:5]}")
    if local_modules:
        print(f"本地模块示例: {local_modules[:5]}")

def demonstrate_module_caching():
    """演示模块缓存机制"""
    print("\n=== 模块缓存机制演示 ===")
    
    # 检查模块是否已缓存
    module_name = 'json'
    print(f"检查模块 '{module_name}' 是否已缓存:")
    
    if module_name in sys.modules:
        print(f"✓ 模块 '{module_name}' 已在缓存中")
        cached_module = sys.modules[module_name]
        print(f"  模块对象: {cached_module}")
        print(f"  模块文件: {getattr(cached_module, '__file__', 'N/A')}")
    else:
        print(f"✗ 模块 '{module_name}' 不在缓存中")
    
    # 导入模块（如果未缓存）
    print(f"\n导入模块 '{module_name}':")
    import json
    print(f"✓ 导入完成")
    
    # 再次检查缓存
    if module_name in sys.modules:
        print(f"✓ 模块 '{module_name}' 现在在缓存中")
        print(f"  缓存的模块对象ID: {id(sys.modules[module_name])}")
        print(f"  导入的模块对象ID: {id(json)}")
        print(f"  是同一个对象: {sys.modules[module_name] is json}")

def test_module_reload():
    """测试模块重新加载"""
    print("\n=== 模块重新加载测试 ===")
    
    # 创建测试模块
    test_module_path = '/tmp/reload_test.py'
    
    # 第一个版本
    with open(test_module_path, 'w') as f:
        f.write('"""可重新加载的测试模块"""\n')
        f.write('VERSION = 1\n')
        f.write('def get_message():\n')
        f.write('    return f"Hello from version {VERSION}!"\n')
    
    # 添加到搜索路径
    import os
    test_dir = os.path.dirname(test_module_path)
    if test_dir not in sys.path:
        sys.path.insert(0, test_dir)
    
    try:
        # 首次导入
        import reload_test
        print(f"首次导入: {reload_test.get_message()}")
        print(f"模块ID: {id(reload_test)}")
        
        # 修改模块文件
        with open(test_module_path, 'w') as f:
            f.write('"""可重新加载的测试模块 - 修改版"""\n')
            f.write('VERSION = 2\n')
            f.write('def get_message():\n')
            f.write('    return f"Hello from version {VERSION}! (Modified)"\n')
        
        # 重新导入（不会重新加载）
        import reload_test
        print(f"重新导入: {reload_test.get_message()}")
        print(f"模块ID: {id(reload_test)}")
        
        # 使用importlib.reload重新加载
        importlib.reload(reload_test)
        print(f"重新加载后: {reload_test.get_message()}")
        print(f"模块ID: {id(reload_test)}")
        
    except ImportError as e:
        print(f"导入失败: {e}")
    
    finally:
        # 清理
        if test_dir in sys.path:
            sys.path.remove(test_dir)
        if 'reload_test' in sys.modules:
            del sys.modules['reload_test']
        try:
            os.remove(test_module_path)
        except OSError:
            pass

def manage_module_cache():
    """管理模块缓存"""
    print("\n=== 模块缓存管理 ===")
    
    # 显示缓存统计
    total_modules = len(sys.modules)
    none_modules = sum(1 for m in sys.modules.values() if m is None)
    valid_modules = total_modules - none_modules
    
    print(f"缓存统计:")
    print(f"  总模块数: {total_modules}")
    print(f"  有效模块: {valid_modules}")
    print(f"  None模块: {none_modules}")
    
    # 查找可能的内存泄漏
    large_modules = []
    for name, module in sys.modules.items():
        if module is not None and hasattr(module, '__dict__'):
            attr_count = len(module.__dict__)
            if attr_count > 100:  # 属性很多的模块
                large_modules.append((name, attr_count))
    
    if large_modules:
        print(f"\n属性较多的模块 (>100个属性):")
        for name, count in sorted(large_modules, key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {name}: {count} 个属性")
    
    # 清理None模块
    none_keys = [k for k, v in sys.modules.items() if v is None]
    if none_keys:
        print(f"\n发现 {len(none_keys)} 个None模块")
        for key in none_keys[:5]:  # 显示前5个
            print(f"  {key}")
        
        # 可以选择清理（谨慎操作）
        # for key in none_keys:
        #     del sys.modules[key]
        # print(f"已清理 {len(none_keys)} 个None模块")

if __name__ == '__main__':
    explore_module_cache()
    demonstrate_module_caching()
    test_module_reload()
    manage_module_cache()
```

## 调试搜索路径问题

### 常见问题和解决方案

```python
import sys
import os
import importlib.util
from pathlib import Path

def diagnose_import_problem(module_name):
    """诊断导入问题"""
    print(f"=== 诊断模块 '{module_name}' 的导入问题 ===")
    
    # 1. 检查是否是内置模块
    if module_name in sys.builtin_module_names:
        print(f"✓ '{module_name}' 是内置模块，应该可以直接导入")
        return
    
    # 2. 使用importlib查找
    spec = importlib.util.find_spec(module_name)
    if spec is not None:
        print(f"✓ 找到模块 '{module_name}'")
        print(f"  位置: {spec.origin}")
        print(f"  加载器: {type(spec.loader).__name__}")
        
        # 检查文件是否存在
        if spec.origin and os.path.exists(spec.origin):
            print(f"  ✓ 文件存在")
        elif spec.origin:
            print(f"  ✗ 文件不存在: {spec.origin}")
        
        return
    
    print(f"✗ 未找到模块 '{module_name}'")
    
    # 3. 搜索可能的位置
    print(f"\n搜索可能的位置:")
    possible_files = [
        f"{module_name}.py",
        f"{module_name}/__init__.py",
        f"{module_name}.so",
        f"{module_name}.pyd"
    ]
    
    found_files = []
    for search_path in sys.path:
        if not search_path or not os.path.exists(search_path):
            continue
        
        for possible_file in possible_files:
            full_path = os.path.join(search_path, possible_file)
            if os.path.exists(full_path):
                found_files.append(full_path)
    
    if found_files:
        print(f"  找到可能的文件:")
        for file_path in found_files:
            print(f"    {file_path}")
    else:
        print(f"  未找到任何可能的文件")
    
    # 4. 检查名称变体
    print(f"\n检查名称变体:")
    name_variants = [
        module_name.lower(),
        module_name.upper(),
        module_name.replace('_', '-'),
        module_name.replace('-', '_')
    ]
    
    for variant in name_variants:
        if variant != module_name:
            variant_spec = importlib.util.find_spec(variant)
            if variant_spec:
                print(f"  ✓ 找到变体 '{variant}': {variant_spec.origin}")

def check_path_permissions():
    """检查路径权限"""
    print("\n=== 检查路径权限 ===")
    
    for i, path in enumerate(sys.path):
        if not path:
            print(f"{i:2d}. [空路径] - 当前目录")
            continue
        
        if not os.path.exists(path):
            print(f"{i:2d}. [不存在] {path}")
            continue
        
        # 检查权限
        readable = os.access(path, os.R_OK)
        executable = os.access(path, os.X_OK)
        
        status = "✓" if readable and executable else "✗"
        permissions = []
        if readable:
            permissions.append("R")
        if executable:
            permissions.append("X")
        
        perm_str = "/".join(permissions) if permissions else "无权限"
        print(f"{i:2d}. [{status}] {path} ({perm_str})")

def find_similar_modules(target_name):
    """查找相似的模块名"""
    print(f"\n=== 查找与 '{target_name}' 相似的模块 ===")
    
    # 收集所有可用的模块名
    available_modules = set()
    
    # 从sys.modules收集
    available_modules.update(sys.modules.keys())
    
    # 从搜索路径收集
    for search_path in sys.path:
        if not search_path or not os.path.exists(search_path):
            continue
        
        try:
            for item in os.listdir(search_path):
                if item.endswith('.py') and not item.startswith('_'):
                    available_modules.add(item[:-3])  # 移除.py扩展名
                elif os.path.isdir(os.path.join(search_path, item)) and not item.startswith('_'):
                    init_file = os.path.join(search_path, item, '__init__.py')
                    if os.path.exists(init_file):
                        available_modules.add(item)
        except PermissionError:
            continue
    
    # 查找相似的名称
    similar_modules = []
    target_lower = target_name.lower()
    
    for module in available_modules:
        module_lower = module.lower()
        
        # 完全匹配（不同大小写）
        if module_lower == target_lower and module != target_name:
            similar_modules.append((module, "大小写不同"))
        # 包含关系
        elif target_lower in module_lower or module_lower in target_lower:
            similar_modules.append((module, "部分匹配"))
        # 编辑距离较小
        elif len(module) > 2 and abs(len(module) - len(target_name)) <= 2:
            # 简单的相似度检查
            common_chars = set(module_lower) & set(target_lower)
            if len(common_chars) >= min(len(module), len(target_name)) * 0.6:
                similar_modules.append((module, "字符相似"))
    
    if similar_modules:
        print(f"找到 {len(similar_modules)} 个相似的模块:")
        for module, reason in similar_modules[:10]:  # 显示前10个
            print(f"  {module} ({reason})")
    else:
        print("未找到相似的模块")

def comprehensive_diagnosis(module_name):
    """综合诊断"""
    print(f"{'='*60}")
    print(f"模块导入问题综合诊断: {module_name}")
    print(f"{'='*60}")
    
    diagnose_import_problem(module_name)
    check_path_permissions()
    find_similar_modules(module_name)
    
    print(f"\n=== 建议的解决方案 ===")
    print(f"1. 检查模块名拼写是否正确")
    print(f"2. 确认模块已安装 (pip list | grep {module_name})")
    print(f"3. 检查Python环境是否正确")
    print(f"4. 尝试重新安装模块 (pip install --force-reinstall {module_name})")
    print(f"5. 检查PYTHONPATH环境变量")
    print(f"6. 确认模块文件权限")
    print(f"7. 检查是否存在同名的本地文件冲突")

if __name__ == '__main__':
    # 测试诊断功能
    test_modules = [
        'os',           # 应该存在
        'requests',     # 可能存在
        'nonexistent',  # 不存在
        'numpyy',       # 拼写错误
    ]
    
    for module in test_modules:
        comprehensive_diagnosis(module)
        print("\n" + "="*60 + "\n")
```

## 学习要点

1. **理解搜索顺序**：Python按固定顺序搜索模块
2. **sys.path的重要性**：这是模块搜索的核心
3. **PYTHONPATH的作用**：环境变量影响搜索路径
4. **模块缓存机制**：已导入的模块会被缓存
5. **路径权限问题**：确保搜索路径可读可执行
6. **调试技巧**：使用工具诊断导入问题

## 最佳实践

1. **避免修改sys.path**：除非必要，不要随意修改
2. **使用虚拟环境**：隔离不同项目的依赖
3. **正确设置PYTHONPATH**：在开发环境中合理使用
4. **包结构设计**：合理组织包和模块的层次结构
5. **路径管理**：使用相对路径和绝对路径的最佳实践

通过理解模块搜索路径机制，你可以更好地组织Python项目，解决导入问题，并优化模块加载性能。