#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python包管理 - 相对导入和绝对导入

本模块演示Python中相对导入和绝对导入的概念、语法和使用场景。

学习目标:
1. 理解绝对导入和相对导入的概念
2. 掌握相对导入的语法规则
3. 了解导入方式的选择原则
4. 学会处理导入相关的问题

作者: Python学习助手
日期: 2024
"""

import os
import sys
from pathlib import Path

def demonstrate_import_concepts():
    """
    演示导入概念的基础知识
    """
    print("=== 导入概念基础 ===")
    
    concepts = {
        "绝对导入 (Absolute Import)": [
            "- 使用完整的模块路径进行导入",
            "- 从sys.path中的路径开始查找",
            "- 语法: import package.module 或 from package import module",
            "- 推荐使用，更加明确和可靠"
        ],
        "相对导入 (Relative Import)": [
            "- 相对于当前模块的位置进行导入",
            "- 只能在包内部使用",
            "- 语法: from . import module 或 from ..package import module",
            "- 适用于包内部模块间的引用"
        ],
        "导入符号说明": [
            "- . (单点): 表示当前包",
            "- .. (双点): 表示父包",
            "- ... (三点): 表示祖父包",
            "- 可以组合使用: from ..parent.sibling import module"
        ]
    }
    
    for concept, details in concepts.items():
        print(f"\n{concept}:")
        for detail in details:
            print(f"  {detail}")

def create_import_demo_structure():
    """
    创建用于演示导入的包结构
    """
    print("\n=== 创建导入演示包结构 ===")
    
    # 定义包结构
    base_path = Path("import_demo")
    
    # 包结构定义
    structure = {
        "import_demo": {
            "__init__.py": '''"""导入演示主包"""
__version__ = "1.0.0"
__author__ = "Python学习助手"

print("正在初始化import_demo主包")

# 导出主要组件
__all__ = ["utils", "core", "plugins"]
''',
            "main.py": '''"""主模块 - 演示不同的导入方式"""

# 绝对导入示例
from import_demo.utils import helper
from import_demo.core.engine import Engine

def main():
    """主函数"""
    print("主模块运行中...")
    helper.show_info()
    engine = Engine()
    engine.start()

if __name__ == "__main__":
    main()
''',
            "utils": {
                "__init__.py": '''"""工具包"""
print("正在初始化utils包")

# 使用相对导入
from .helper import show_info, calculate
from .formatter import format_text

__all__ = ["show_info", "calculate", "format_text"]
''',
                "helper.py": '''"""辅助工具模块"""

# 相对导入同级模块
from .formatter import format_text

def show_info():
    """显示信息"""
    info = "这是来自helper模块的信息"
    print(format_text(info, "INFO"))

def calculate(a, b):
    """简单计算"""
    return a + b
''',
                "formatter.py": '''"""格式化工具模块"""

def format_text(text, level="INFO"):
    """格式化文本"""
    return f"[{level}] {text}"

def format_json(data):
    """格式化JSON数据"""
    import json
    return json.dumps(data, indent=2, ensure_ascii=False)
'''
            },
            "core": {
                "__init__.py": '''"""核心包"""
print("正在初始化core包")

# 相对导入子模块
from .engine import Engine
from .processor import Processor

__all__ = ["Engine", "Processor"]
''',
                "engine.py": '''"""引擎模块"""

# 相对导入同包模块
from .processor import Processor
# 相对导入父包的其他子包
from ..utils import helper

class Engine:
    """引擎类"""
    
    def __init__(self):
        self.processor = Processor()
        self.running = False
    
    def start(self):
        """启动引擎"""
        print("引擎启动中...")
        self.running = True
        self.processor.process("引擎数据")
        helper.show_info()
    
    def stop(self):
        """停止引擎"""
        print("引擎停止中...")
        self.running = False
''',
                "processor.py": '''"""处理器模块"""

# 相对导入父包的工具
from ..utils.formatter import format_text

class Processor:
    """处理器类"""
    
    def __init__(self):
        self.name = "默认处理器"
    
    def process(self, data):
        """处理数据"""
        formatted = format_text(f"处理数据: {data}", "PROCESS")
        print(formatted)
        return f"已处理: {data}"
'''
            },
            "plugins": {
                "__init__.py": '''"""插件包"""
print("正在初始化plugins包")

# 相对导入插件模块
from .base import BasePlugin
from .manager import PluginManager

__all__ = ["BasePlugin", "PluginManager"]
''',
                "base.py": '''"""基础插件模块"""

# 相对导入核心功能
from ..core import Engine
from ..utils import helper

class BasePlugin:
    """基础插件类"""
    
    def __init__(self, name):
        self.name = name
        self.enabled = False
    
    def enable(self):
        """启用插件"""
        self.enabled = True
        print(f"插件 {self.name} 已启用")
        helper.show_info()
    
    def disable(self):
        """禁用插件"""
        self.enabled = False
        print(f"插件 {self.name} 已禁用")
''',
                "manager.py": '''"""插件管理器模块"""

# 相对导入同包模块
from .base import BasePlugin
# 相对导入其他包
from ..utils.formatter import format_text

class PluginManager:
    """插件管理器"""
    
    def __init__(self):
        self.plugins = {}
    
    def register(self, plugin):
        """注册插件"""
        if isinstance(plugin, BasePlugin):
            self.plugins[plugin.name] = plugin
            msg = f"插件 {plugin.name} 注册成功"
            print(format_text(msg, "REGISTER"))
        else:
            print("错误: 插件必须继承BasePlugin类")
    
    def get_plugin(self, name):
        """获取插件"""
        return self.plugins.get(name)
    
    def list_plugins(self):
        """列出所有插件"""
        for name, plugin in self.plugins.items():
            status = "启用" if plugin.enabled else "禁用"
            print(f"  - {name}: {status}")
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

def demonstrate_absolute_import():
    """
    演示绝对导入的使用
    """
    print("\n=== 绝对导入演示 ===")
    
    print("\n1. 绝对导入的特点:")
    features = [
        "- 使用完整的模块路径",
        "- 从sys.path开始查找",
        "- 不依赖当前模块位置",
        "- 更加明确和可靠",
        "- 推荐在大型项目中使用"
    ]
    
    for feature in features:
        print(f"  {feature}")
    
    print("\n2. 绝对导入语法示例:")
    examples = [
        "import os",
        "import sys.path",
        "from collections import defaultdict",
        "from import_demo.utils import helper",
        "from import_demo.core.engine import Engine",
        "import import_demo.plugins.manager as pm"
    ]
    
    for example in examples:
        print(f"  {example}")
    
    print("\n3. 测试绝对导入:")
    try:
        # 添加当前目录到sys.path以便导入
        current_dir = os.getcwd()
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        
        # 尝试绝对导入
        print("  尝试导入import_demo包...")
        import import_demo
        print(f"  成功导入: {import_demo.__name__}")
        print(f"  包版本: {getattr(import_demo, '__version__', '未知')}")
        
        # 导入子模块
        from import_demo.utils import helper
        print("  成功导入helper模块")
        
        # 使用导入的模块
        result = helper.calculate(10, 20)
        print(f"  计算结果: {result}")
        
    except ImportError as e:
        print(f"  导入错误: {e}")
    except Exception as e:
        print(f"  运行错误: {e}")

def demonstrate_relative_import():
    """
    演示相对导入的概念和限制
    """
    print("\n=== 相对导入演示 ===")
    
    print("\n1. 相对导入的特点:")
    features = [
        "- 相对于当前模块位置",
        "- 只能在包内部使用",
        "- 不能在主模块中使用",
        "- 使用点号表示层级关系",
        "- 适用于包内部模块引用"
    ]
    
    for feature in features:
        print(f"  {feature}")
    
    print("\n2. 相对导入语法:")
    syntax_examples = [
        "from . import module          # 导入同级模块",
        "from .module import function  # 导入同级模块的函数",
        "from .. import parent_module  # 导入父级模块",
        "from ..sibling import func    # 导入兄弟包的模块",
        "from ...grandparent import x  # 导入祖父级模块"
    ]
    
    for example in syntax_examples:
        print(f"  {example}")
    
    print("\n3. 相对导入层级示例:")
    hierarchy = [
        "package/",
        "├── __init__.py",
        "├── module1.py              # from . import module2",
        "├── module2.py              # from . import module1",
        "└── subpackage/",
        "    ├── __init__.py",
        "    ├── submodule1.py       # from .. import module1",
        "    └── submodule2.py       # from . import submodule1"
    ]
    
    for line in hierarchy:
        print(f"  {line}")
    
    print("\n4. 相对导入的限制:")
    limitations = [
        "- 不能在脚本文件中直接使用",
        "- 必须在包的上下文中运行",
        "- 不能超出顶级包的范围",
        "- 调试时可能比较困难"
    ]
    
    for limitation in limitations:
        print(f"  {limitation}")

def demonstrate_import_best_practices():
    """
    演示导入的最佳实践
    """
    print("\n=== 导入最佳实践 ===")
    
    practices = {
        "1. 导入顺序": [
            "- 标准库导入",
            "- 第三方库导入",
            "- 本地应用/库导入",
            "- 每组之间用空行分隔"
        ],
        "2. 导入风格": [
            "- 优先使用绝对导入",
            "- 避免使用 from module import *",
            "- 使用明确的导入语句",
            "- 避免循环导入"
        ],
        "3. 相对导入使用场景": [
            "- 包内部模块间引用",
            "- 重构时减少修改",
            "- 包的可移植性",
            "- 避免硬编码包名"
        ],
        "4. 性能考虑": [
            "- 避免在函数内部导入(除非必要)",
            "- 使用延迟导入优化启动时间",
            "- 避免重复导入",
            "- 合理使用 __all__ 控制导入"
        ],
        "5. 错误处理": [
            "- 使用 try-except 处理导入错误",
            "- 提供友好的错误信息",
            "- 考虑可选依赖的处理",
            "- 记录导入失败的原因"
        ]
    }
    
    for category, items in practices.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  {item}")

def demonstrate_import_problems_and_solutions():
    """
    演示常见导入问题及解决方案
    """
    print("\n=== 常见导入问题及解决方案 ===")
    
    problems = {
        "1. 循环导入问题": {
            "问题描述": "两个模块相互导入导致ImportError",
            "解决方案": [
                "- 重新设计模块结构",
                "- 将共同依赖提取到第三个模块",
                "- 使用延迟导入(在函数内导入)",
                "- 使用字符串形式的类型注解"
            ],
            "示例": '''
# 错误示例:
# module_a.py
from module_b import ClassB
class ClassA: pass

# module_b.py  
from module_a import ClassA
class ClassB: pass

# 正确示例:
# module_a.py
class ClassA: 
    def method(self):
        from module_b import ClassB  # 延迟导入
        return ClassB()
'''
        },
        "2. 相对导入错误": {
            "问题描述": "attempted relative import with no known parent package",
            "解决方案": [
                "- 确保模块在包的上下文中运行",
                "- 使用 python -m package.module 运行",
                "- 避免直接运行包内模块",
                "- 改用绝对导入"
            ],
            "示例": '''
# 错误运行方式:
python package/module.py

# 正确运行方式:
python -m package.module
'''
        },
        "3. 模块未找到错误": {
            "问题描述": "ModuleNotFoundError: No module named 'xxx'",
            "解决方案": [
                "- 检查模块路径是否正确",
                "- 确保 __init__.py 文件存在",
                "- 检查 sys.path 设置",
                "- 验证包的安装状态"
            ],
            "示例": '''
# 检查和修复路径:
import sys
print(sys.path)
sys.path.insert(0, '/path/to/your/package')
'''
        }
    }
    
    for problem, details in problems.items():
        print(f"\n{problem}")
        print(f"问题: {details['问题描述']}")
        print("解决方案:")
        for solution in details['解决方案']:
            print(f"  {solution}")
        if '示例' in details:
            print("示例:")
            print(details['示例'])

def demonstrate_import_tools_and_debugging():
    """
    演示导入相关的工具和调试技巧
    """
    print("\n=== 导入工具和调试技巧 ===")
    
    print("\n1. 查看模块搜索路径:")
    print("  import sys")
    print("  print(sys.path)")
    print(f"  当前路径: {sys.path[:3]}...")  # 只显示前3个路径
    
    print("\n2. 查看已导入的模块:")
    print("  import sys")
    print("  print(list(sys.modules.keys()))")
    imported_count = len(sys.modules)
    print(f"  当前已导入模块数量: {imported_count}")
    
    print("\n3. 查看模块信息:")
    print("  import inspect")
    print("  print(inspect.getfile(module))  # 模块文件路径")
    print("  print(module.__file__)          # 模块文件路径")
    print("  print(module.__package__)       # 模块所属包")
    
    print("\n4. 动态导入:")
    dynamic_examples = [
        "importlib.import_module('package.module')",
        "__import__('package.module')",
        "getattr(__import__('package'), 'module')"
    ]
    
    for example in dynamic_examples:
        print(f"  {example}")
    
    print("\n5. 导入调试技巧:")
    debug_tips = [
        "- 使用 python -v 查看详细导入过程",
        "- 使用 python -c 'import module' 测试导入",
        "- 检查 __pycache__ 目录的字节码文件",
        "- 使用 importlib.reload() 重新加载模块",
        "- 使用 pkgutil.walk_packages() 遍历包"
    ]
    
    for tip in debug_tips:
        print(f"  {tip}")

def main():
    """
    主函数 - 演示相对导入和绝对导入
    """
    print("Python相对导入和绝对导入演示")
    print("=" * 50)
    
    # 1. 演示导入概念
    demonstrate_import_concepts()
    
    # 2. 创建演示包结构
    package_path = create_import_demo_structure()
    
    # 3. 演示绝对导入
    demonstrate_absolute_import()
    
    # 4. 演示相对导入
    demonstrate_relative_import()
    
    # 5. 演示最佳实践
    demonstrate_import_best_practices()
    
    # 6. 演示问题和解决方案
    demonstrate_import_problems_and_solutions()
    
    # 7. 演示工具和调试
    demonstrate_import_tools_and_debugging()
    
    print("\n=== 学习小结 ===")
    summary_points = [
        "1. 绝对导入使用完整路径，更加明确可靠",
        "2. 相对导入使用相对路径，适用于包内部引用",
        "3. 相对导入只能在包的上下文中使用",
        "4. 推荐优先使用绝对导入，谨慎使用相对导入",
        "5. 避免循环导入，合理设计模块结构",
        "6. 掌握导入调试技巧有助于解决问题"
    ]
    
    for point in summary_points:
        print(point)
    
    print(f"\n示例包已创建在: {package_path}")
    print("可以使用 python -m import_demo.main 运行演示")

if __name__ == "__main__":
    main()