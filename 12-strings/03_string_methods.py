#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字符串常用方法

本文件演示Python中字符串的常用方法：
1. 大小写转换方法
2. 字符串检查方法
3. 字符串分割和连接方法
4. 字符串清理方法
5. 字符串替换方法
6. 字符串对齐方法

作者：Python学习教程
日期：2024年
"""

def demonstrate_case_methods():
    """演示大小写转换方法"""
    print("=== 大小写转换方法 ===")
    
    text = "Hello World Python Programming"
    print(f"原字符串: {text}")
    
    # 基本大小写转换
    print(f"\nupper(): {text.upper()}")
    print(f"lower(): {text.lower()}")
    print(f"capitalize(): {text.capitalize()}")
    print(f"title(): {text.title()}")
    
    # swapcase() - 大小写互换
    mixed_case = "PyThOn ProGramMinG"
    print(f"\n原字符串: {mixed_case}")
    print(f"swapcase(): {mixed_case.swapcase()}")
    
    # casefold() - 更强的小写转换（支持特殊字符）
    special_text = "Straße"  # 德语街道
    print(f"\n特殊字符: {special_text}")
    print(f"lower(): {special_text.lower()}")
    print(f"casefold(): {special_text.casefold()}")

def demonstrate_check_methods():
    """演示字符串检查方法"""
    print("\n=== 字符串检查方法 ===")
    
    # 测试不同类型的字符串
    test_strings = [
        "hello",
        "WORLD",
        "Hello World",
        "123456",
        "abc123",
        "   ",
        "",
        "Hello123",
        "hello_world",
        "HelloWorld"
    ]
    
    print(f"{'字符串':<12} {'isalpha':<8} {'isdigit':<8} {'isalnum':<8} {'isspace':<8} {'islower':<8} {'isupper':<8} {'istitle':<8}")
    print("-" * 80)
    
    for s in test_strings:
        display_s = f"'{s}'" if s else "'(空)'"
        print(f"{display_s:<12} {str(s.isalpha()):<8} {str(s.isdigit()):<8} {str(s.isalnum()):<8} {str(s.isspace()):<8} {str(s.islower()):<8} {str(s.isupper()):<8} {str(s.istitle()):<8}")
    
    # 其他检查方法
    print("\n其他检查方法:")
    identifier = "valid_variable_name"
    print(f"'{identifier}' isidentifier(): {identifier.isidentifier()}")
    
    printable = "Hello\tWorld\n"
    print(f"'{repr(printable)}' isprintable(): {printable.isprintable()}")
    
    decimal_str = "123"
    print(f"'{decimal_str}' isdecimal(): {decimal_str.isdecimal()}")
    print(f"'{decimal_str}' isnumeric(): {decimal_str.isnumeric()}")

def demonstrate_split_join_methods():
    """演示字符串分割和连接方法"""
    print("\n=== 分割和连接方法 ===")
    
    # split() 方法
    sentence = "Python is a powerful programming language"
    print(f"原字符串: {sentence}")
    
    words = sentence.split()
    print(f"split(): {words}")
    
    # 指定分隔符
    csv_data = "apple,banana,orange,grape"
    fruits = csv_data.split(',')
    print(f"\nCSV数据: {csv_data}")
    print(f"split(','): {fruits}")
    
    # 限制分割次数
    text = "one-two-three-four-five"
    parts = text.split('-', 2)
    print(f"\n原字符串: {text}")
    print(f"split('-', 2): {parts}")
    
    # rsplit() - 从右边开始分割
    path = "/home/user/documents/file.txt"
    right_parts = path.rsplit('/', 1)
    print(f"\n路径: {path}")
    print(f"rsplit('/', 1): {right_parts}")
    
    # splitlines() - 按行分割
    multiline = "第一行\n第二行\r\n第三行\r第四行"
    lines = multiline.splitlines()
    print(f"\n多行文本分割: {lines}")
    
    # join() 方法
    words_list = ['Python', 'is', 'awesome']
    joined = ' '.join(words_list)
    print(f"\n单词列表: {words_list}")
    print(f"' '.join(): {joined}")
    
    # 不同连接符
    separators = ['-', ' | ', ', ', '']
    for sep in separators:
        result = sep.join(words_list)
        print(f"'{sep}'.join(): {result}")

def demonstrate_strip_methods():
    """演示字符串清理方法"""
    print("\n=== 字符串清理方法 ===")
    
    # 基本的strip方法
    messy_string = "   Hello World   "
    print(f"原字符串: '{messy_string}'")
    print(f"strip(): '{messy_string.strip()}'")
    print(f"lstrip(): '{messy_string.lstrip()}'")
    print(f"rstrip(): '{messy_string.rstrip()}'")
    
    # 指定要删除的字符
    custom_string = "...Hello World!!!"
    print(f"\n原字符串: '{custom_string}'")
    print(f"strip('.'): '{custom_string.strip('.')}'")
    print(f"strip('.!'): '{custom_string.strip('.!')}'")
    print(f"lstrip('.'): '{custom_string.lstrip('.')}'")
    print(f"rstrip('!'): '{custom_string.rstrip('!')}'")
    
    # 清理多种字符
    noisy_data = "###   Python Programming   @@@"
    clean_data = noisy_data.strip('#@ ')
    print(f"\n原数据: '{noisy_data}'")
    print(f"清理后: '{clean_data}'")
    
    # 实际应用：清理用户输入
    user_inputs = [
        "  john@email.com  ",
        "\t\npassword123\n\t",
        "   Python   "
    ]
    
    print("\n清理用户输入:")
    for inp in user_inputs:
        cleaned = inp.strip()
        print(f"'{inp}' -> '{cleaned}'")

def demonstrate_replace_methods():
    """演示字符串替换方法"""
    print("\n=== 字符串替换方法 ===")
    
    # 基本replace方法
    text = "I love Java programming. Java is great!"
    print(f"原字符串: {text}")
    
    replaced = text.replace("Java", "Python")
    print(f"replace('Java', 'Python'): {replaced}")
    
    # 限制替换次数
    limited_replace = text.replace("Java", "Python", 1)
    print(f"replace('Java', 'Python', 1): {limited_replace}")
    
    # 替换多个空格为单个空格
    spaced_text = "Python    is    awesome"
    normalized = ' '.join(spaced_text.split())
    print(f"\n原字符串: '{spaced_text}'")
    print(f"标准化空格: '{normalized}'")
    
    # 删除字符（替换为空字符串）
    phone = "(123) 456-7890"
    clean_phone = phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    print(f"\n电话号码: {phone}")
    print(f"清理后: {clean_phone}")
    
    # 链式替换
    messy_text = "Hello...World!!!How...are...you???"
    clean_text = messy_text.replace("...", " ").replace("!!!", "! ").replace("???", "?")
    print(f"\n原文本: {messy_text}")
    print(f"清理后: {clean_text}")

def demonstrate_alignment_methods():
    """演示字符串对齐方法"""
    print("\n=== 字符串对齐方法 ===")
    
    text = "Python"
    width = 20
    
    print(f"原字符串: '{text}'")
    print(f"目标宽度: {width}")
    print()
    
    # 基本对齐方法
    print(f"center({width}): '{text.center(width)}'")
    print(f"ljust({width}): '{text.ljust(width)}'")
    print(f"rjust({width}): '{text.rjust(width)}'")
    
    # 指定填充字符
    print(f"\n使用填充字符:")
    print(f"center({width}, '*'): '{text.center(width, '*')}'")
    print(f"ljust({width}, '-'): '{text.ljust(width, '-')}'")
    print(f"rjust({width}, '='): '{text.rjust(width, '=')}")
    
    # zfill() - 用0填充
    numbers = ["42", "123", "7"]
    print(f"\nzfill()方法:")
    for num in numbers:
        print(f"'{num}'.zfill(5): '{num.zfill(5)}'")
    
    # 实际应用：格式化表格
    print("\n表格格式化示例:")
    data = [
        ("Name", "Age", "City"),
        ("Alice", "25", "New York"),
        ("Bob", "30", "London"),
        ("Charlie", "35", "Tokyo")
    ]
    
    for row in data:
        formatted_row = f"{row[0].ljust(10)} {row[1].center(5)} {row[2].rjust(10)}"
        print(formatted_row)

def demonstrate_find_methods():
    """演示字符串查找方法"""
    print("\n=== 字符串查找方法 ===")
    
    text = "Python programming is fun. Python is powerful."
    print(f"原字符串: {text}")
    
    # find() 和 rfind()
    search_term = "Python"
    first_pos = text.find(search_term)
    last_pos = text.rfind(search_term)
    
    print(f"\nfind('{search_term}'): {first_pos}")
    print(f"rfind('{search_term}'): {last_pos}")
    
    # 查找不存在的字符串
    not_found = text.find("Java")
    print(f"find('Java'): {not_found}")
    
    # index() 和 rindex() - 找不到会抛出异常
    try:
        index_pos = text.index(search_term)
        print(f"index('{search_term}'): {index_pos}")
    except ValueError as e:
        print(f"index() 错误: {e}")
    
    try:
        text.index("Java")
    except ValueError as e:
        print(f"index('Java') 错误: {e}")
    
    # count() - 计算出现次数
    count = text.count("is")
    print(f"\ncount('is'): {count}")
    
    # 在指定范围内查找
    partial_find = text.find("is", 20)  # 从索引20开始查找
    print(f"find('is', 20): {partial_find}")
    
    range_find = text.find("Python", 10, 30)  # 在索引10-30之间查找
    print(f"find('Python', 10, 30): {range_find}")

def demonstrate_startswith_endswith():
    """演示字符串开始和结束检查方法"""
    print("\n=== 开始和结束检查方法 ===")
    
    filenames = [
        "document.pdf",
        "image.jpg",
        "script.py",
        "README.md",
        "config.json"
    ]
    
    print("文件类型检查:")
    for filename in filenames:
        print(f"{filename}:")
        print(f"  是Python文件: {filename.endswith('.py')}")
        print(f"  是图片文件: {filename.endswith(('.jpg', '.png', '.gif'))}")
        print(f"  是文档文件: {filename.endswith(('.pdf', '.doc', '.txt'))}")
    
    # startswith() 示例
    urls = [
        "https://www.example.com",
        "http://test.com",
        "ftp://files.com",
        "www.noprotocol.com"
    ]
    
    print("\nURL协议检查:")
    for url in urls:
        print(f"{url}:")
        print(f"  安全连接: {url.startswith('https://')}")
        print(f"  HTTP协议: {url.startswith(('http://', 'https://'))}")
        print(f"  FTP协议: {url.startswith('ftp://')}")

def main():
    """主函数，演示所有字符串方法"""
    print("Python字符串常用方法")
    print("=" * 50)
    
    demonstrate_case_methods()
    demonstrate_check_methods()
    demonstrate_split_join_methods()
    demonstrate_strip_methods()
    demonstrate_replace_methods()
    demonstrate_alignment_methods()
    demonstrate_find_methods()
    demonstrate_startswith_endswith()
    
    print("\n=== 总结 ===")
    print("1. 大小写转换: upper(), lower(), capitalize(), title()")
    print("2. 字符串检查: isalpha(), isdigit(), isalnum()等")
    print("3. 分割连接: split(), join()")
    print("4. 清理方法: strip(), lstrip(), rstrip()")
    print("5. 替换方法: replace()")
    print("6. 对齐方法: center(), ljust(), rjust(), zfill()")
    print("7. 查找方法: find(), index(), count()")
    print("8. 前后缀检查: startswith(), endswith()")

if __name__ == "__main__":
    main()