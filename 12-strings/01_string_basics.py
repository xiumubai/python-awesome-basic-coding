#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字符串基础和创建

本文件演示Python中字符串的基础概念和创建方法：
1. 字符串的定义和特性
2. 不同的字符串创建方式
3. 字符串的不可变性
4. 字符串的基本属性
5. 多行字符串的创建

作者：Python学习教程
日期：2024年
"""

def demonstrate_string_creation():
    """演示字符串的创建方法"""
    print("=== 字符串创建方法 ===")
    
    # 1. 使用单引号创建字符串
    single_quote_str = 'Hello, World!'
    print(f"单引号字符串: {single_quote_str}")
    print(f"类型: {type(single_quote_str)}")
    
    # 2. 使用双引号创建字符串
    double_quote_str = "Python Programming"
    print(f"双引号字符串: {double_quote_str}")
    
    # 3. 包含引号的字符串
    quote_in_string1 = "He said 'Hello'"
    quote_in_string2 = 'She replied "Hi there"'
    print(f"包含单引号: {quote_in_string1}")
    print(f"包含双引号: {quote_in_string2}")
    
    # 4. 使用转义字符
    escaped_string = "He said \"Hello\" and she replied 'Hi'"
    print(f"转义字符: {escaped_string}")
    
    # 5. 空字符串
    empty_string1 = ""
    empty_string2 = ''
    print(f"空字符串1: '{empty_string1}', 长度: {len(empty_string1)}")
    print(f"空字符串2: '{empty_string2}', 长度: {len(empty_string2)}")

def demonstrate_multiline_strings():
    """演示多行字符串的创建"""
    print("\n=== 多行字符串 ===")
    
    # 1. 使用三重引号创建多行字符串
    multiline_str1 = """这是一个
多行字符串
可以包含换行符"""
    print("三重双引号多行字符串:")
    print(multiline_str1)
    
    # 2. 使用三重单引号
    multiline_str2 = '''这也是一个
多行字符串
使用三重单引号'''
    print("\n三重单引号多行字符串:")
    print(multiline_str2)
    
    # 3. 多行字符串保持格式
    formatted_multiline = """第一行
    第二行（有缩进）
        第三行（更多缩进）
第四行（无缩进）"""
    print("\n格式化多行字符串:")
    print(formatted_multiline)
    
    # 4. 使用\n创建多行效果
    newline_string = "第一行\n第二行\n第三行"
    print("\n使用\\n的多行字符串:")
    print(newline_string)

def demonstrate_string_properties():
    """演示字符串的基本属性"""
    print("\n=== 字符串属性 ===")
    
    sample_string = "Python编程学习"
    
    # 1. 字符串长度
    print(f"字符串: {sample_string}")
    print(f"长度: {len(sample_string)}")
    
    # 2. 字符串是否为空
    print(f"是否为空: {len(sample_string) == 0}")
    print(f"布尔值: {bool(sample_string)}")
    
    # 3. 空字符串的布尔值
    empty_str = ""
    print(f"空字符串的布尔值: {bool(empty_str)}")
    
    # 4. 字符串包含的字符类型
    mixed_string = "Hello123世界!"
    print(f"\n混合字符串: {mixed_string}")
    print(f"长度: {len(mixed_string)}")
    print(f"包含字母: {any(c.isalpha() for c in mixed_string)}")
    print(f"包含数字: {any(c.isdigit() for c in mixed_string)}")
    # 检查是否包含中文字符
    chinese_range = lambda c: '\u4e00' <= c <= '\u9fff'
    print(f"包含中文: {any(chinese_range(c) for c in mixed_string)}")

def demonstrate_string_immutability():
    """演示字符串的不可变性"""
    print("\n=== 字符串不可变性 ===")
    
    original_string = "Hello"
    print(f"原始字符串: {original_string}")
    print(f"字符串ID: {id(original_string)}")
    
    # 字符串连接会创建新的字符串对象
    new_string = original_string + " World"
    print(f"连接后字符串: {new_string}")
    print(f"新字符串ID: {id(new_string)}")
    print(f"原字符串ID: {id(original_string)}")
    print(f"ID是否相同: {id(original_string) == id(new_string)}")
    
    # 尝试修改字符串（这会产生错误）
    print("\n字符串不能直接修改单个字符:")
    try:
        # original_string[0] = 'h'  # 这行会报错
        print("不能执行 original_string[0] = 'h'")
        print("因为字符串是不可变的")
    except TypeError as e:
        print(f"错误: {e}")
    
    # 正确的修改方式是创建新字符串
    modified_string = 'h' + original_string[1:]
    print(f"正确的修改方式: {modified_string}")

def demonstrate_string_concatenation():
    """演示字符串连接的基本方法"""
    print("\n=== 字符串连接 ===")
    
    str1 = "Hello"
    str2 = "World"
    
    # 1. 使用+操作符
    result1 = str1 + " " + str2
    print(f"使用+连接: {result1}")
    
    # 2. 使用+=操作符
    str3 = "Python"
    str3 += " Programming"
    print(f"使用+=连接: {str3}")
    
    # 3. 使用*操作符重复
    repeated = "Ha" * 3
    print(f"使用*重复: {repeated}")
    
    # 4. 连接数字和字符串（需要转换）
    number = 42
    text = "The answer is "
    result2 = text + str(number)
    print(f"连接数字: {result2}")

def demonstrate_raw_strings():
    """演示原始字符串（raw strings）"""
    print("\n=== 原始字符串 ===")
    
    # 普通字符串中的转义字符
    normal_string = "C:\\Users\\name\\file.txt"
    print(f"普通字符串: {normal_string}")
    
    # 原始字符串（r前缀）
    raw_string = r"C:\Users\name\file.txt"
    print(f"原始字符串: {raw_string}")
    
    # 原始字符串中的特殊字符
    regex_pattern = r"\d+\.\d+"  # 匹配小数的正则表达式
    print(f"正则表达式模式: {regex_pattern}")
    
    # 原始字符串的限制
    print("\n原始字符串不能以单个反斜杠结尾")
    # raw_invalid = r"path\"  # 这会报错
    raw_valid = r"path" + "\\"
    print(f"正确的方式: {raw_valid}")

def main():
    """主函数，演示所有字符串基础概念"""
    print("Python字符串基础和创建")
    print("=" * 50)
    
    demonstrate_string_creation()
    demonstrate_multiline_strings()
    demonstrate_string_properties()
    demonstrate_string_immutability()
    demonstrate_string_concatenation()
    demonstrate_raw_strings()
    
    print("\n=== 总结 ===")
    print("1. 字符串可以用单引号、双引号或三重引号创建")
    print("2. 字符串是不可变的数据类型")
    print("3. 多行字符串使用三重引号")
    print("4. 原始字符串使用r前缀，避免转义字符解释")
    print("5. 字符串连接会创建新的字符串对象")

if __name__ == "__main__":
    main()