#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模块搜索路径演示

本文件演示Python如何搜索和定位模块，包括：
1. sys.path的作用和内容
2. 模块搜索顺序
3. 动态修改搜索路径
4. PYTHONPATH环境变量
5. .pth文件的使用
6. 包的搜索机制

学习目标：
- 理解Python模块搜索机制
- 掌握如何查看和修改搜索路径
- 了解不同搜索路径的优先级
- 学会解决模块导入问题
"""

import sys
import os
from pathlib import Path

# ============================================================================
# 1. 查看当前的模块搜索路径
# ============================================================================

def show_current_search_paths():
    """
    显示当前的模块搜索路径
    """
    print("=== 1. 当前模块搜索路径 ===")
    print("Python在以下路径中按顺序搜索模块：\n")
    
    for i, path in enumerate(sys.path, 1):
        print(f"{i:2d}. {path}")
        
        # 检查路径是否存在
        if os.path.exists(path):
            path_type = "目录" if os.path.isdir(path) else "文件"
            print(f"    └─ [{path_type}] 存在")
        else:
            print(f"    └─ [不存在]")
    
    print(f"\n总共 {len(sys.path)} 个搜索路径")

# ============================================================================
# 2. 分析搜索路径的来源
# ============================================================================

def analyze_path_sources():
    """
    分析各个搜索路径的来源
    """
    print("\n=== 2. 搜索路径来源分析 ===")
    
    # 当前工作目录
    current_dir = os.getcwd()
    print(f"当前工作目录: {current_dir}")
    
    # 脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"脚本所在目录: {script_dir}")
    
    # Python安装目录
    python_home = sys.prefix
    print(f"Python安装目录: {python_home}")
    
    # 标准库目录
    stdlib_dir = os.path.dirname(os.__file__)
    print(f"标准库目录: {stdlib_dir}")
    
    # site-packages目录
    import site
    site_packages = site.getsitepackages()
    print(f"site-packages目录: {site_packages}")
    
    # PYTHONPATH环境变量
    pythonpath = os.environ.get('PYTHONPATH', '')
    if pythonpath:
        print(f"PYTHONPATH环境变量: {pythonpath}")
    else:
        print("PYTHONPATH环境变量: 未设置")

# ============================================================================
# 3. 演示模块搜索顺序
# ============================================================================

def demonstrate_search_order():
    """
    演示模块搜索的优先级顺序
    """
    print("\n=== 3. 模块搜索顺序 ===")
    
    print("Python按以下顺序搜索模块：")
    print("1. 内置模块 (built-in modules)")
    print("2. 当前目录或脚本所在目录")
    print("3. PYTHONPATH环境变量指定的目录")
    print("4. Python标准库目录")
    print("5. site-packages目录")
    print("6. .pth文件指定的目录")
    
    # 演示内置模块
    print("\n内置模块示例：")
    builtin_modules = sys.builtin_module_names
    print(f"内置模块数量: {len(builtin_modules)}")
    print(f"部分内置模块: {list(builtin_modules)[:10]}...")
    
    # 检查特定模块的位置
    modules_to_check = ['os', 'sys', 'json', 'datetime']
    print("\n标准库模块位置：")
    for module_name in modules_to_check:
        try:
            module = __import__(module_name)
            if hasattr(module, '__file__') and module.__file__:
                print(f"{module_name:10s}: {module.__file__}")
            else:
                print(f"{module_name:10s}: [内置模块]")
        except ImportError:
            print(f"{module_name:10s}: [未找到]")

# ============================================================================
# 4. 动态修改搜索路径
# ============================================================================

def demonstrate_path_modification():
    """
    演示如何动态修改模块搜索路径
    """
    print("\n=== 4. 动态修改搜索路径 ===")
    
    # 保存原始路径
    original_path = sys.path.copy()
    print(f"原始路径数量: {len(original_path)}")
    
    # 添加新路径到开头（最高优先级）
    new_path = "/tmp/my_modules"
    sys.path.insert(0, new_path)
    print(f"\n在开头添加路径: {new_path}")
    print(f"新的第一个搜索路径: {sys.path[0]}")
    
    # 添加路径到末尾（最低优先级）
    another_path = "/tmp/low_priority"
    sys.path.append(another_path)
    print(f"\n在末尾添加路径: {another_path}")
    print(f"当前路径数量: {len(sys.path)}")
    
    # 移除添加的路径
    if new_path in sys.path:
        sys.path.remove(new_path)
        print(f"\n移除路径: {new_path}")
    
    if another_path in sys.path:
        sys.path.remove(another_path)
        print(f"移除路径: {another_path}")
    
    # 恢复原始路径
    sys.path = original_path
    print(f"\n恢复原始路径，当前数量: {len(sys.path)}")

# ============================================================================
# 5. 创建和使用临时模块
# ============================================================================

def create_temporary_module():
    """
    创建临时模块来演示搜索路径
    """
    print("\n=== 5. 创建临时模块演示 ===")
    
    # 创建临时目录
    temp_dir = "/tmp/python_module_demo"
    os.makedirs(temp_dir, exist_ok=True)
    
    # 创建临时模块文件
    module_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
临时演示模块
"""

TEMP_MODULE_NAME = "临时模块"
TEMP_MODULE_VERSION = "1.0.0"

def temp_function():
    return "这是临时模块中的函数"

class TempClass:
    def __init__(self):
        self.name = "临时类"
    
    def get_info(self):
        return f"我是{self.name}"
'''
    
    module_file = os.path.join(temp_dir, "temp_module.py")
    with open(module_file, 'w', encoding='utf-8') as f:
        f.write(module_content)
    
    print(f"创建临时模块: {module_file}")
    
    # 将临时目录添加到搜索路径
    if temp_dir not in sys.path:
        sys.path.insert(0, temp_dir)
        print(f"添加到搜索路径: {temp_dir}")
    
    # 尝试导入临时模块
    try:
        import temp_module
        print(f"\n成功导入临时模块: {temp_module.TEMP_MODULE_NAME}")
        print(f"模块版本: {temp_module.TEMP_MODULE_VERSION}")
        print(f"调用函数: {temp_module.temp_function()}")
        
        # 使用临时类
        temp_obj = temp_module.TempClass()
        print(f"使用临时类: {temp_obj.get_info()}")
        
        # 显示模块文件位置
        print(f"模块文件位置: {temp_module.__file__}")
        
    except ImportError as e:
        print(f"导入临时模块失败: {e}")
    
    # 清理：移除搜索路径
    if temp_dir in sys.path:
        sys.path.remove(temp_dir)
        print(f"\n从搜索路径移除: {temp_dir}")
    
    # 清理：删除临时文件
    try:
        os.remove(module_file)
        os.rmdir(temp_dir)
        print(f"清理临时文件: {module_file}")
    except OSError:
        print(f"清理临时文件时出错")

# ============================================================================
# 6. 包的搜索机制
# ============================================================================

def demonstrate_package_search():
    """
    演示包的搜索机制
    """
    print("\n=== 6. 包的搜索机制 ===")
    
    print("包搜索规则：")
    print("1. 包必须是包含__init__.py文件的目录")
    print("2. 包的搜索遵循与模块相同的路径规则")
    print("3. 子包通过点号分隔的路径访问")
    print("4. 相对导入只能在包内部使用")
    
    # 检查一些常见包的位置
    packages_to_check = [
        'json',
        'urllib',
        'xml',
        'email',
        'collections'
    ]
    
    print("\n常见包的位置：")
    for package_name in packages_to_check:
        try:
            package = __import__(package_name)
            if hasattr(package, '__path__'):
                print(f"{package_name:12s}: {package.__path__}")
            elif hasattr(package, '__file__'):
                print(f"{package_name:12s}: {package.__file__}")
            else:
                print(f"{package_name:12s}: [内置]")
        except ImportError:
            print(f"{package_name:12s}: [未找到]")

# ============================================================================
# 7. 搜索路径问题诊断
# ============================================================================

def diagnose_import_issues():
    """
    诊断常见的导入问题
    """
    print("\n=== 7. 导入问题诊断 ===")
    
    print("常见导入问题及解决方案：")
    print("\n1. ModuleNotFoundError:")
    print("   - 检查模块名拼写")
    print("   - 确认模块在搜索路径中")
    print("   - 检查PYTHONPATH设置")
    
    print("\n2. 相对导入问题:")
    print("   - 相对导入只能在包内使用")
    print("   - 使用绝对导入更安全")
    
    print("\n3. 循环导入:")
    print("   - 重新设计模块结构")
    print("   - 使用延迟导入")
    
    print("\n4. 路径问题:")
    print("   - 检查当前工作目录")
    print("   - 使用绝对路径")
    print("   - 正确设置PYTHONPATH")
    
    # 提供诊断工具
    print("\n诊断工具函数：")
    
    def find_module_path(module_name):
        """查找模块的实际路径"""
        try:
            import importlib.util
            spec = importlib.util.find_spec(module_name)
            if spec:
                return spec.origin or spec.submodule_search_locations
            else:
                return None
        except ImportError:
            return None
    
    # 测试诊断工具
    test_modules = ['os', 'sys', 'nonexistent_module']
    for module in test_modules:
        path = find_module_path(module)
        if path:
            print(f"  {module}: {path}")
        else:
            print(f"  {module}: [未找到]")

# ============================================================================
# 8. 最佳实践建议
# ============================================================================

def show_best_practices():
    """
    显示模块搜索路径的最佳实践
    """
    print("\n=== 8. 最佳实践建议 ===")
    
    practices = [
        "1. 使用虚拟环境管理项目依赖",
        "2. 避免修改sys.path，除非绝对必要",
        "3. 使用相对于项目根目录的导入",
        "4. 在setup.py或pyproject.toml中声明依赖",
        "5. 使用绝对导入而不是相对导入",
        "6. 保持模块结构简单清晰",
        "7. 使用包来组织相关模块",
        "8. 避免在运行时动态修改搜索路径",
        "9. 使用importlib进行动态导入",
        "10. 定期清理不需要的模块和包"
    ]
    
    for practice in practices:
        print(f"  {practice}")
    
    print("\n推荐的项目结构：")
    print("""
  my_project/
  ├── setup.py
  ├── requirements.txt
  ├── my_package/
  │   ├── __init__.py
  │   ├── module1.py
  │   └── subpackage/
  │       ├── __init__.py
  │       └── module2.py
  ├── tests/
  │   └── test_module1.py
  └── docs/
      └── README.md
    """)

# ============================================================================
# 主函数
# ============================================================================

def main():
    """
    主函数：演示所有模块搜索路径相关功能
    """
    print("Python模块搜索路径演示")
    print("=" * 60)
    
    show_current_search_paths()
    analyze_path_sources()
    demonstrate_search_order()
    demonstrate_path_modification()
    create_temporary_module()
    demonstrate_package_search()
    diagnose_import_issues()
    show_best_practices()
    
    print("\n" + "=" * 60)
    print("模块搜索路径演示完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()