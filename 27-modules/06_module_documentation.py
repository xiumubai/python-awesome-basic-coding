#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模块文档和帮助系统演示

本文件演示Python中模块文档和帮助系统的使用，包括：
1. 文档字符串(docstring)的编写
2. help()函数的使用
3. __doc__属性的访问
4. 模块、函数、类的文档规范
5. 文档生成工具
6. 最佳实践和规范

学习目标：
- 掌握文档字符串的编写规范
- 学会使用Python内置的帮助系统
- 了解文档生成和管理工具
- 培养良好的代码文档习惯
"""

import sys
import inspect
import pydoc
import os
from datetime import datetime

# ============================================================================
# 1. 文档字符串基础
# ============================================================================

def demonstrate_docstring_basics():
    """
    演示文档字符串的基础用法
    
    文档字符串是Python中为模块、类、函数等添加文档的标准方式。
    它们存储在对象的__doc__属性中，可以通过help()函数访问。
    
    Returns:
        None
    
    Examples:
        >>> demonstrate_docstring_basics()
        # 输出文档字符串相关信息
    """
    print("=== 1. 文档字符串基础 ===")
    
    print("文档字符串(Docstring)特点：")
    print("1. 使用三重引号包围")
    print("2. 位于模块、类、函数定义的第一行")
    print("3. 存储在__doc__属性中")
    print("4. 可以通过help()函数访问")
    print("5. 支持多行文本和格式化")
    
    # 演示访问文档字符串
    print("\n访问文档字符串：")
    print(f"当前函数的文档: {demonstrate_docstring_basics.__doc__[:50]}...")
    print(f"当前模块的文档: {__doc__[:50] if __doc__ else 'None'}...")
    
    # 演示不同类型的文档字符串
    def simple_function():
        """这是一个简单的函数文档字符串。"""
        pass
    
    def detailed_function(param1, param2=None):
        """
        这是一个详细的函数文档字符串。
        
        Args:
            param1 (str): 第一个参数的描述
            param2 (int, optional): 第二个参数的描述. Defaults to None.
        
        Returns:
            bool: 返回值的描述
        
        Raises:
            ValueError: 当参数无效时抛出
        """
        return True
    
    print("\n不同风格的文档字符串：")
    print(f"简单文档: {simple_function.__doc__}")
    print(f"详细文档: {detailed_function.__doc__[:100]}...")

# ============================================================================
# 2. help()函数的使用
# ============================================================================

def demonstrate_help_function():
    """
    演示help()函数的各种用法
    
    help()函数是Python内置的帮助系统，可以显示对象的文档信息。
    """
    print("\n=== 2. help()函数的使用 ===")
    
    print("help()函数的用法：")
    print("1. help() - 进入交互式帮助系统")
    print("2. help(object) - 显示对象的帮助信息")
    print("3. help('topic') - 显示主题帮助")
    print("4. help('modules') - 显示可用模块")
    
    # 演示获取不同对象的帮助
    print("\n获取内置函数的帮助：")
    print("help(len) 的部分输出：")
    try:
        # 捕获help输出
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            help(len)
        help_output = f.getvalue()
        
        # 显示前几行
        lines = help_output.split('\n')[:10]
        for line in lines:
            print(f"  {line}")
        print("  ...")
        
    except Exception as e:
        print(f"  获取帮助信息时出错: {e}")
    
    # 演示获取模块帮助
    print("\n获取模块帮助：")
    print("sys模块的简要信息：")
    if hasattr(sys, '__doc__') and sys.__doc__:
        doc_lines = sys.__doc__.split('\n')[:3]
        for line in doc_lines:
            print(f"  {line}")
    
    # 演示自定义对象的帮助
    class DocumentedClass:
        """
        这是一个有文档的示例类。
        
        这个类演示了如何为类编写文档字符串。
        
        Attributes:
            name (str): 对象的名称
            value (int): 对象的值
        """
        
        def __init__(self, name, value=0):
            """
            初始化DocumentedClass实例。
            
            Args:
                name (str): 对象名称
                value (int): 初始值
            """
            self.name = name
            self.value = value
        
        def get_info(self):
            """
            获取对象信息。
            
            Returns:
                str: 包含对象信息的字符串
            """
            return f"{self.name}: {self.value}"
    
    print("\n自定义类的文档：")
    print(f"类文档: {DocumentedClass.__doc__[:50]}...")
    print(f"方法文档: {DocumentedClass.get_info.__doc__[:30]}...")

# ============================================================================
# 3. 文档字符串格式规范
# ============================================================================

def demonstrate_docstring_formats():
    """
    演示不同的文档字符串格式规范
    
    常见的文档字符串格式包括：
    - Google风格
    - NumPy风格
    - Sphinx风格
    - PEP 257标准
    """
    print("\n=== 3. 文档字符串格式规范 ===")
    
    print("常见的文档字符串格式：")
    
    # Google风格
    def google_style_function(param1, param2):
        """
        Google风格的文档字符串示例。
        
        Args:
            param1 (str): 第一个参数描述
            param2 (int): 第二个参数描述
        
        Returns:
            bool: 返回值描述
        
        Raises:
            ValueError: 异常描述
        
        Example:
            >>> google_style_function("test", 123)
            True
        """
        return True
    
    # NumPy风格
    def numpy_style_function(param1, param2):
        """
        NumPy风格的文档字符串示例。
        
        Parameters
        ----------
        param1 : str
            第一个参数描述
        param2 : int
            第二个参数描述
        
        Returns
        -------
        bool
            返回值描述
        
        Raises
        ------
        ValueError
            异常描述
        
        Examples
        --------
        >>> numpy_style_function("test", 123)
        True
        """
        return True
    
    # Sphinx风格
    def sphinx_style_function(param1, param2):
        """
        Sphinx风格的文档字符串示例。
        
        :param param1: 第一个参数描述
        :type param1: str
        :param param2: 第二个参数描述
        :type param2: int
        :returns: 返回值描述
        :rtype: bool
        :raises ValueError: 异常描述
        
        .. code-block:: python
        
            >>> sphinx_style_function("test", 123)
            True
        """
        return True
    
    print("\n1. Google风格 - 简洁易读")
    print(f"   {google_style_function.__doc__.split('Args:')[0].strip()}")
    
    print("\n2. NumPy风格 - 科学计算常用")
    print(f"   {numpy_style_function.__doc__.split('Parameters')[0].strip()}")
    
    print("\n3. Sphinx风格 - 文档生成工具")
    print(f"   {sphinx_style_function.__doc__.split(':param')[0].strip()}")

# ============================================================================
# 4. inspect模块的使用
# ============================================================================

def demonstrate_inspect_module():
    """
    演示inspect模块获取对象信息
    
    inspect模块提供了获取对象详细信息的功能，
    包括源代码、签名、文档等。
    """
    print("\n=== 4. inspect模块的使用 ===")
    
    print("inspect模块的主要功能：")
    print("1. 获取对象的源代码")
    print("2. 检查函数签名")
    print("3. 获取类的成员")
    print("4. 检查对象类型")
    
    # 演示函数签名检查
    def sample_function(a, b=10, *args, **kwargs):
        """
        示例函数用于演示inspect功能
        
        Args:
            a: 必需参数
            b: 可选参数，默认值为10
            *args: 可变位置参数
            **kwargs: 可变关键字参数
        """
        return a + b
    
    print("\n函数签名检查：")
    sig = inspect.signature(sample_function)
    print(f"函数签名: {sig}")
    
    print("\n参数详情：")
    for param_name, param in sig.parameters.items():
        print(f"  {param_name}: {param.kind.name}, 默认值: {param.default}")
    
    # 演示获取源代码
    print("\n获取源代码：")
    try:
        source = inspect.getsource(sample_function)
        print("函数源代码（前3行）：")
        for i, line in enumerate(source.split('\n')[:3]):
            print(f"  {i+1}: {line}")
    except Exception as e:
        print(f"获取源代码失败: {e}")
    
    # 演示类成员检查
    class SampleClass:
        """
        示例类用于演示inspect功能
        """
        class_var = "类变量"
        
        def __init__(self):
            self.instance_var = "实例变量"
        
        def method(self):
            """实例方法"""
            pass
        
        @classmethod
        def class_method(cls):
            """类方法"""
            pass
        
        @staticmethod
        def static_method():
            """静态方法"""
            pass
    
    print("\n类成员检查：")
    members = inspect.getmembers(SampleClass)
    print("类的成员（部分）：")
    for name, value in members[:5]:
        if not name.startswith('_'):
            print(f"  {name}: {type(value).__name__}")

# ============================================================================
# 5. pydoc模块的使用
# ============================================================================

def demonstrate_pydoc_module():
    """
    演示pydoc模块生成文档
    
    pydoc模块可以生成HTML格式的文档，
    也可以启动文档服务器。
    """
    print("\n=== 5. pydoc模块的使用 ===")
    
    print("pydoc模块的功能：")
    print("1. 生成HTML文档")
    print("2. 启动文档服务器")
    print("3. 在终端显示文档")
    print("4. 搜索模块文档")
    
    # 演示获取文档文本
    print("\n获取模块文档：")
    try:
        # 获取当前模块的文档
        doc_text = pydoc.getdoc(sys)
        if doc_text:
            lines = doc_text.split('\n')[:3]
            print("sys模块文档（前3行）：")
            for line in lines:
                print(f"  {line}")
        else:
            print("  未找到sys模块文档")
    except Exception as e:
        print(f"  获取文档失败: {e}")
    
    # 演示生成HTML文档
    print("\n生成HTML文档：")
    print("可以使用以下命令生成HTML文档：")
    print("  python -m pydoc -w module_name")
    print("  python -m pydoc -p 8080  # 启动文档服务器")
    
    # 创建示例模块用于文档生成
    sample_module_content = '''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例模块用于文档生成演示

这个模块包含一些示例函数和类，用于演示文档生成功能。

Author: Python学习者
Date: 2024
Version: 1.0.0
"""

def add_numbers(a, b):
    """
    计算两个数的和
    
    Args:
        a (int): 第一个数
        b (int): 第二个数
    
    Returns:
        int: 两数之和
    
    Example:
        >>> add_numbers(3, 5)
        8
    """
    return a + b

class Calculator:
    """
    简单的计算器类
    
    这个类提供基本的数学运算功能。
    
    Attributes:
        result (float): 当前计算结果
    """
    
    def __init__(self):
        """初始化计算器"""
        self.result = 0
    
    def add(self, value):
        """
        加法运算
        
        Args:
            value (float): 要加的数值
        
        Returns:
            float: 计算结果
        """
        self.result += value
        return self.result
    
    def get_result(self):
        """
        获取当前结果
        
        Returns:
            float: 当前计算结果
        """
        return self.result
'''
    
    # 创建示例模块文件
    sample_file = "sample_documented_module.py"
    try:
        with open(sample_file, 'w', encoding='utf-8') as f:
            f.write(sample_module_content)
        print(f"\n创建示例模块: {sample_file}")
        print("可以使用以下命令查看文档：")
        print(f"  python -m pydoc {sample_file[:-3]}")
        
    except Exception as e:
        print(f"创建示例模块失败: {e}")

# ============================================================================
# 6. 文档最佳实践
# ============================================================================

def demonstrate_documentation_best_practices():
    """
    演示文档编写的最佳实践
    
    良好的文档应该清晰、准确、完整，
    并遵循一致的格式规范。
    """
    print("\n=== 6. 文档最佳实践 ===")
    
    print("文档编写最佳实践：")
    
    practices = [
        "1. 为所有公共模块、类、函数编写文档",
        "2. 使用一致的文档格式（选择一种风格并坚持）",
        "3. 包含参数类型和返回值信息",
        "4. 提供使用示例",
        "5. 说明可能抛出的异常",
        "6. 保持文档与代码同步更新",
        "7. 使用清晰简洁的语言",
        "8. 避免重复代码中已经明显的信息",
        "9. 包含版本信息和作者信息",
        "10. 使用文档生成工具验证格式"
    ]
    
    for practice in practices:
        print(f"  {practice}")
    
    print("\n文档内容建议：")
    content_suggestions = [
        "模块级别: 模块用途、主要功能、使用方法",
        "类级别: 类的职责、主要属性、使用场景",
        "函数级别: 功能描述、参数说明、返回值、异常",
        "复杂算法: 算法思路、时间复杂度、注意事项"
    ]
    
    for suggestion in content_suggestions:
        print(f"  • {suggestion}")
    
    # 演示完整的文档示例
    class WellDocumentedClass:
        """
        完整文档示例类
        
        这个类演示了如何编写完整、规范的文档字符串。
        它包含了所有推荐的文档元素。
        
        Attributes:
            name (str): 对象名称
            created_at (datetime): 创建时间
            _private_var (int): 私有变量示例
        
        Example:
            >>> obj = WellDocumentedClass("test")
            >>> obj.get_age()
            0.0
        
        Note:
            这是一个教学示例，实际使用时请根据需要调整。
        
        .. versionadded:: 1.0.0
        .. versionchanged:: 1.1.0
           添加了get_age方法
        """
        
        def __init__(self, name):
            """
            初始化WellDocumentedClass实例
            
            Args:
                name (str): 对象名称，不能为空
            
            Raises:
                ValueError: 当name为空时抛出
            
            Example:
                >>> obj = WellDocumentedClass("example")
                >>> obj.name
                'example'
            """
            if not name:
                raise ValueError("名称不能为空")
            
            self.name = name
            self.created_at = datetime.now()
            self._private_var = 0
        
        def get_age(self):
            """
            获取对象存在的时间（秒）
            
            Returns:
                float: 对象存在的秒数
            
            Example:
                >>> obj = WellDocumentedClass("test")
                >>> age = obj.get_age()
                >>> isinstance(age, float)
                True
            """
            return (datetime.now() - self.created_at).total_seconds()
    
    print("\n完整文档示例：")
    print(f"类文档长度: {len(WellDocumentedClass.__doc__)} 字符")
    print(f"方法文档长度: {len(WellDocumentedClass.get_age.__doc__)} 字符")

# ============================================================================
# 7. 文档生成工具
# ============================================================================

def demonstrate_documentation_tools():
    """
    介绍常用的文档生成工具
    
    Python生态系统中有多种文档生成工具，
    可以从代码中自动生成美观的文档。
    """
    print("\n=== 7. 文档生成工具 ===")
    
    print("常用的Python文档生成工具：")
    
    tools = [
        {
            'name': 'Sphinx',
            'description': '最流行的Python文档生成工具',
            'features': ['支持多种输出格式', 'reStructuredText语法', '自动API文档', '主题丰富']
        },
        {
            'name': 'MkDocs',
            'description': '基于Markdown的文档生成器',
            'features': ['Markdown语法', '实时预览', '主题美观', '易于配置']
        },
        {
            'name': 'pdoc',
            'description': '自动生成API文档',
            'features': ['零配置', '自动扫描', 'HTML输出', '简单易用']
        },
        {
            'name': 'pydoc',
            'description': 'Python内置文档工具',
            'features': ['内置工具', '命令行使用', 'HTML生成', '文档服务器']
        }
    ]
    
    for tool in tools:
        print(f"\n{tool['name']}:")
        print(f"  描述: {tool['description']}")
        print("  特性:")
        for feature in tool['features']:
            print(f"    • {feature}")
    
    print("\n使用建议：")
    suggestions = [
        "小项目: 使用pydoc或pdoc快速生成文档",
        "中大型项目: 使用Sphinx构建完整文档系统",
        "团队协作: 使用MkDocs便于维护和更新",
        "API文档: 使用pdoc自动生成接口文档"
    ]
    
    for suggestion in suggestions:
        print(f"  • {suggestion}")

# ============================================================================
# 8. 清理和总结
# ============================================================================

def cleanup_and_summary():
    """
    清理演示文件并总结要点
    """
    print("\n=== 8. 清理和总结 ===")
    
    # 清理创建的文件
    files_to_clean = [
        "sample_documented_module.py"
    ]
    
    print("清理演示文件：")
    for file_name in files_to_clean:
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
                print(f"  清理文件: {file_name}")
        except Exception as e:
            print(f"  清理文件 {file_name} 时出错: {e}")
    
    print("\n模块文档要点总结：")
    summary_points = [
        "1. 文档字符串是Python文档的标准方式",
        "2. help()函数提供交互式帮助系统",
        "3. inspect模块可获取对象详细信息",
        "4. pydoc可生成HTML文档和启动文档服务器",
        "5. 选择合适的文档格式规范并保持一致",
        "6. 良好的文档提高代码可维护性",
        "7. 使用文档生成工具自动化文档流程",
        "8. 保持文档与代码同步更新"
    ]
    
    for point in summary_points:
        print(f"  {point}")

# ============================================================================
# 主函数
# ============================================================================

def main():
    """
    主函数：演示所有模块文档相关功能
    
    这个函数按顺序执行所有演示功能，
    展示Python模块文档系统的各个方面。
    """
    print("Python模块文档和帮助系统演示")
    print("=" * 60)
    
    try:
        demonstrate_docstring_basics()
        demonstrate_help_function()
        demonstrate_docstring_formats()
        demonstrate_inspect_module()
        demonstrate_pydoc_module()
        demonstrate_documentation_best_practices()
        demonstrate_documentation_tools()
        
    finally:
        cleanup_and_summary()
    
    print("\n" + "=" * 60)
    print("模块文档和帮助系统演示完成！")
    print("=" * 60)

if __name__ == '__main__':
    main()