#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正则表达式基础

本文件演示Python中正则表达式的基础用法：
1. 正则表达式基本概念
2. re模块的主要函数
3. 基本模式和元字符
4. 字符类和量词
5. 分组和捕获
6. 常用正则表达式模式
7. 正则表达式的编译和性能优化
8. 实际应用示例

作者：Python学习教程
日期：2024年
"""

import re
import time
from typing import List, Optional, Tuple

def demonstrate_regex_basics():
    """演示正则表达式基础概念"""
    print("=== 正则表达式基础概念 ===")
    
    # 1. 什么是正则表达式
    print("1. 正则表达式简介:")
    print("正则表达式是用于匹配字符串模式的强大工具")
    print("它使用特殊字符来定义搜索模式")
    
    # 2. 基本匹配
    print("\n2. 基本匹配示例:")
    
    text = "Hello World! Python is great. Python version 3.9"
    
    # 简单字符串匹配
    patterns = [
        ("Python", "匹配单词Python"),
        ("python", "匹配单词python（区分大小写）"),
        ("\d", "匹配任意数字"),
        ("\d+", "匹配一个或多个数字"),
        ("\w+", "匹配一个或多个单词字符"),
        ("\s+", "匹配一个或多个空白字符"),
    ]
    
    print(f"测试文本: {text}")
    print(f"{'模式':<15} {'描述':<25} {'匹配结果':<20}")
    print("-" * 65)
    
    for pattern, description in patterns:
        matches = re.findall(pattern, text)
        match_display = str(matches)[:15] + "..." if len(str(matches)) > 15 else str(matches)
        print(f"{pattern:<15} {description:<25} {match_display:<20}")
    
    # 3. re模块主要函数介绍
    print("\n3. re模块主要函数:")
    
    functions_info = [
        ("re.search()", "在字符串中搜索第一个匹配"),
        ("re.match()", "从字符串开头匹配"),
        ("re.findall()", "找到所有匹配项"),
        ("re.finditer()", "返回匹配对象的迭代器"),
        ("re.sub()", "替换匹配的字符串"),
        ("re.split()", "按模式分割字符串"),
        ("re.compile()", "编译正则表达式"),
    ]
    
    for func, desc in functions_info:
        print(f"  {func:<15} - {desc}")

def demonstrate_re_functions():
    """演示re模块的主要函数"""
    print("\n=== re模块主要函数演示 ===")
    
    text = "Contact: john@example.com or call 123-456-7890. Email: mary@test.org"
    
    # 1. re.search() - 搜索第一个匹配
    print("1. re.search() - 搜索第一个匹配:")
    
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    search_result = re.search(email_pattern, text)
    if search_result:
        print(f"  找到邮箱: {search_result.group()}")
        print(f"  位置: {search_result.start()}-{search_result.end()}")
        print(f"  匹配的文本: '{text[search_result.start():search_result.end()]}'")
    else:
        print("  未找到匹配")
    
    # 2. re.match() - 从开头匹配
    print("\n2. re.match() - 从开头匹配:")
    
    match_result = re.match(r'Contact', text)
    if match_result:
        print(f"  开头匹配成功: {match_result.group()}")
    else:
        print("  开头匹配失败")
    
    # 测试不从开头开始的模式
    match_result2 = re.match(email_pattern, text)
    if match_result2:
        print(f"  邮箱开头匹配: {match_result2.group()}")
    else:
        print(f"  邮箱开头匹配失败（因为文本不是以邮箱开头）")
    
    # 3. re.findall() - 找到所有匹配
    print("\n3. re.findall() - 找到所有匹配:")
    
    all_emails = re.findall(email_pattern, text)
    print(f"  所有邮箱: {all_emails}")
    
    # 找到所有数字
    all_numbers = re.findall(r'\d+', text)
    print(f"  所有数字: {all_numbers}")
    
    # 4. re.finditer() - 返回匹配对象迭代器
    print("\n4. re.finditer() - 匹配对象迭代器:")
    
    for i, match in enumerate(re.finditer(email_pattern, text)):
        print(f"  邮箱 {i+1}: {match.group()} (位置: {match.start()}-{match.end()})")
    
    # 5. re.sub() - 替换匹配的字符串
    print("\n5. re.sub() - 替换匹配的字符串:")
    
    # 隐藏邮箱
    hidden_email = re.sub(email_pattern, '[EMAIL]', text)
    print(f"  隐藏邮箱: {hidden_email}")
    
    # 格式化电话号码
    phone_pattern = r'(\d{3})-(\d{3})-(\d{4})'
    formatted_phone = re.sub(phone_pattern, r'(\1) \2-\3', text)
    print(f"  格式化电话: {formatted_phone}")
    
    # 6. re.split() - 按模式分割字符串
    print("\n6. re.split() - 按模式分割字符串:")
    
    # 按空白字符分割
    words = re.split(r'\s+', text)
    print(f"  按空白分割: {words[:5]}...")  # 只显示前5个
    
    # 按标点符号分割
    sentences = re.split(r'[.!?]+', text)
    print(f"  按句号分割: {[s.strip() for s in sentences if s.strip()]}")

def demonstrate_basic_patterns():
    """演示基本模式和元字符"""
    print("\n=== 基本模式和元字符 ===")
    
    # 1. 基本元字符
    print("1. 基本元字符:")
    
    test_text = "Hello123 World! @#$ test_file.txt 2024-01-15"
    
    metacharacters = [
        (r'.', "匹配任意字符（除换行符）"),
        (r'\d', "匹配数字 [0-9]"),
        (r'\D', "匹配非数字"),
        (r'\w', "匹配单词字符 [a-zA-Z0-9_]"),
        (r'\W', "匹配非单词字符"),
        (r'\s', "匹配空白字符"),
        (r'\S', "匹配非空白字符"),
    ]
    
    print(f"测试文本: {test_text}")
    print(f"{'元字符':<8} {'描述':<25} {'匹配结果':<30}")
    print("-" * 70)
    
    for pattern, description in metacharacters:
        matches = re.findall(pattern, test_text)
        # 限制显示长度
        match_display = str(matches[:5]) + "..." if len(matches) > 5 else str(matches)
        if len(match_display) > 25:
            match_display = match_display[:25] + "..."
        print(f"{pattern:<8} {description:<25} {match_display:<30}")
    
    # 2. 位置锚点
    print("\n2. 位置锚点:")
    
    anchor_tests = [
        ("Hello World", r'^Hello', "匹配开头的Hello"),
        ("Hello World", r'World$', "匹配结尾的World"),
        ("Hello World", r'^World', "匹配开头的World（应该失败）"),
        ("word boundary test", r'\bword\b', "匹配完整单词word"),
        ("password", r'\bword\b', "匹配password中的word（应该失败）"),
    ]
    
    print(f"{'文本':<20} {'模式':<12} {'描述':<25} {'结果':<10}")
    print("-" * 75)
    
    for text, pattern, description in anchor_tests:
        match = re.search(pattern, text)
        result = "匹配" if match else "不匹配"
        print(f"{text:<20} {pattern:<12} {description:<25} {result:<10}")
    
    # 3. 字符类
    print("\n3. 字符类:")
    
    char_class_text = "Hello123 WORLD abc XYZ !@# test"
    
    char_classes = [
        (r'[aeiou]', "匹配小写元音字母"),
        (r'[A-Z]', "匹配大写字母"),
        (r'[0-9]', "匹配数字"),
        (r'[^0-9]', "匹配非数字字符"),
        (r'[a-zA-Z]', "匹配所有字母"),
        (r'[!@#$%]', "匹配特定符号"),
    ]
    
    print(f"测试文本: {char_class_text}")
    print(f"{'字符类':<12} {'描述':<20} {'匹配结果':<30}")
    print("-" * 70)
    
    for pattern, description in char_classes:
        matches = re.findall(pattern, char_class_text)
        match_display = str(matches)[:25] + "..." if len(str(matches)) > 25 else str(matches)
        print(f"{pattern:<12} {description:<20} {match_display:<30}")

def demonstrate_quantifiers():
    """演示量词"""
    print("\n=== 量词演示 ===")
    
    # 1. 基本量词
    print("1. 基本量词:")
    
    quantifier_text = "a aa aaa aaaa b bb bbb cccc ddddd"
    
    quantifiers = [
        (r'a*', "匹配0个或多个a"),
        (r'a+', "匹配1个或多个a"),
        (r'a?', "匹配0个或1个a"),
        (r'a{2}', "匹配恰好2个a"),
        (r'a{2,}', "匹配2个或更多a"),
        (r'a{2,4}', "匹配2到4个a"),
    ]
    
    print(f"测试文本: {quantifier_text}")
    print(f"{'量词':<10} {'描述':<20} {'匹配结果':<30}")
    print("-" * 65)
    
    for pattern, description in quantifiers:
        matches = re.findall(pattern, quantifier_text)
        match_display = str(matches)[:25] + "..." if len(str(matches)) > 25 else str(matches)
        print(f"{pattern:<10} {description:<20} {match_display:<30}")
    
    # 2. 贪婪vs非贪婪匹配
    print("\n2. 贪婪vs非贪婪匹配:")
    
    html_text = "<div>Hello</div><span>World</span>"
    
    greedy_patterns = [
        (r'<.*>', "贪婪匹配：匹配最长的"),
        (r'<.*?>', "非贪婪匹配：匹配最短的"),
        (r'<\w+>', "匹配开始标签"),
        (r'</\w+>', "匹配结束标签"),
    ]
    
    print(f"测试HTML: {html_text}")
    print(f"{'模式':<12} {'描述':<25} {'匹配结果':<30}")
    print("-" * 75)
    
    for pattern, description in greedy_patterns:
        matches = re.findall(pattern, html_text)
        print(f"{pattern:<12} {description:<25} {str(matches):<30}")
    
    # 3. 实际应用：提取数字
    print("\n3. 实际应用：提取不同格式的数字:")
    
    number_text = "Price: $123.45, Quantity: 100, Percentage: 85.5%, Code: ABC123"
    
    number_patterns = [
        (r'\d+', "整数"),
        (r'\d+\.\d+', "小数"),
        (r'\$\d+\.\d+', "货币格式"),
        (r'\d+%', "百分比"),
        (r'[A-Z]+\d+', "字母数字组合"),
    ]
    
    print(f"测试文本: {number_text}")
    print(f"{'模式':<15} {'描述':<15} {'匹配结果':<20}")
    print("-" * 55)
    
    for pattern, description in number_patterns:
        matches = re.findall(pattern, number_text)
        print(f"{pattern:<15} {description:<15} {str(matches):<20}")

def demonstrate_groups_and_capture():
    """演示分组和捕获"""
    print("\n=== 分组和捕获 ===")
    
    # 1. 基本分组
    print("1. 基本分组:")
    
    contact_text = "John Doe: john.doe@email.com, phone: (555) 123-4567"
    
    # 捕获姓名
    name_pattern = r'([A-Z][a-z]+)\s+([A-Z][a-z]+)'
    name_match = re.search(name_pattern, contact_text)
    
    if name_match:
        print(f"  完整匹配: {name_match.group(0)}")
        print(f"  第一组（名）: {name_match.group(1)}")
        print(f"  第二组（姓）: {name_match.group(2)}")
        print(f"  所有组: {name_match.groups()}")
    
    # 2. 命名分组
    print("\n2. 命名分组:")
    
    email_pattern = r'(?P<username>[a-zA-Z0-9._%+-]+)@(?P<domain>[a-zA-Z0-9.-]+)\.(?P<tld>[A-Z|a-z]{2,})'
    email_match = re.search(email_pattern, contact_text)
    
    if email_match:
        print(f"  完整邮箱: {email_match.group(0)}")
        print(f"  用户名: {email_match.group('username')}")
        print(f"  域名: {email_match.group('domain')}")
        print(f"  顶级域: {email_match.group('tld')}")
        print(f"  分组字典: {email_match.groupdict()}")
    
    # 3. 非捕获分组
    print("\n3. 非捕获分组:")
    
    # 匹配电话号码，但不捕获括号
    phone_pattern1 = r'(\()?(\d{3})(\))?\s*(\d{3})-(\d{4})'  # 捕获所有
    phone_pattern2 = r'(?:\()?(\d{3})(?:\))?\s*(\d{3})-(\d{4})'  # 不捕获括号
    
    phone_text = "Call (555) 123-4567 or 555 987-6543"
    
    print(f"  测试文本: {phone_text}")
    
    for i, match in enumerate(re.finditer(phone_pattern1, phone_text)):
        print(f"  捕获所有 - 电话{i+1}: {match.groups()}")
    
    for i, match in enumerate(re.finditer(phone_pattern2, phone_text)):
        print(f"  非捕获括号 - 电话{i+1}: {match.groups()}")
    
    # 4. 分组替换
    print("\n4. 分组替换:")
    
    # 交换姓名顺序
    name_swap = re.sub(r'([A-Z][a-z]+)\s+([A-Z][a-z]+)', r'\2, \1', contact_text)
    print(f"  原文: {contact_text}")
    print(f"  交换姓名: {name_swap}")
    
    # 格式化电话号码
    phone_format = re.sub(r'\((\d{3})\)\s*(\d{3})-(\d{4})', r'\1.\2.\3', contact_text)
    print(f"  格式化电话: {phone_format}")
    
    # 5. 条件匹配
    print("\n5. 条件匹配示例:")
    
    # 匹配可选的协议
    url_pattern = r'(?:https?://)?([a-zA-Z0-9.-]+)(?:/.*)?'
    
    urls = [
        "https://www.example.com/path",
        "http://test.org",
        "www.google.com",
        "example.com/page"
    ]
    
    print(f"  URL模式: {url_pattern}")
    for url in urls:
        match = re.search(url_pattern, url)
        if match:
            print(f"    {url} -> 域名: {match.group(1)}")

def demonstrate_common_patterns():
    """演示常用正则表达式模式"""
    print("\n=== 常用正则表达式模式 ===")
    
    # 1. 验证模式
    print("1. 常用验证模式:")
    
    validation_patterns = {
        '邮箱': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        '手机号': r'^1[3-9]\d{9}$',
        'IP地址': r'^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$',
        'URL': r'^https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?$',
        '身份证': r'^\d{17}[\dXx]$',
        '密码强度': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
    }
    
    test_data = {
        '邮箱': ['user@example.com', 'invalid.email', 'test@domain.co.uk'],
        '手机号': ['13812345678', '12345678901', '15987654321'],
        'IP地址': ['192.168.1.1', '256.1.1.1', '127.0.0.1'],
        'URL': ['https://www.example.com', 'http://test.org/path', 'invalid-url'],
        '身份证': ['110101199001011234', '11010119900101123X', '12345'],
        '密码强度': ['Password123!', 'password', 'PASSWORD123', 'Pass123!'],
    }
    
    for pattern_name, pattern in validation_patterns.items():
        print(f"\n  {pattern_name}模式: {pattern}")
        if pattern_name in test_data:
            for test_value in test_data[pattern_name]:
                is_valid = bool(re.match(pattern, test_value))
                status = "✓" if is_valid else "✗"
                print(f"    {status} {test_value}")
    
    # 2. 提取模式
    print("\n2. 常用提取模式:")
    
    extract_text = """
    联系信息：
    邮箱：admin@company.com, support@help.org
    电话：010-12345678, (021) 87654321
    网址：https://www.company.com, http://help.org/support
    日期：2024-01-15, 2024/12/31
    价格：$123.45, ￥999.99, €45.67
    """
    
    extraction_patterns = {
        '邮箱地址': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        '电话号码': r'(?:\(\d{3}\)|\d{3})[\s-]?\d{3,4}[\s-]?\d{4}',
        'URL链接': r'https?://[^\s]+',
        '日期': r'\d{4}[/-]\d{1,2}[/-]\d{1,2}',
        '货币金额': r'[¥$€]\d+(?:\.\d{2})?',
    }
    
    print(f"  测试文本: {extract_text.strip()}")
    
    for pattern_name, pattern in extraction_patterns.items():
        matches = re.findall(pattern, extract_text)
        print(f"\n  {pattern_name}: {matches}")
    
    # 3. 替换模式
    print("\n3. 常用替换模式:")
    
    replace_text = "用户输入：Hello    World!   多个空格   和   特殊字符@#$%"
    
    replacements = [
        (r'\s+', ' ', "合并多个空格为一个"),
        (r'[^\w\s]', '', "移除特殊字符"),
        (r'\b(\w)', lambda m: m.group(1).upper(), "单词首字母大写"),
    ]
    
    current_text = replace_text
    print(f"  原始文本: {current_text}")
    
    for pattern, replacement, description in replacements:
        if callable(replacement):
            current_text = re.sub(pattern, replacement, current_text)
        else:
            current_text = re.sub(pattern, replacement, current_text)
        print(f"  {description}: {current_text}")

def demonstrate_compiled_regex():
    """演示编译正则表达式和性能优化"""
    print("\n=== 编译正则表达式和性能优化 ===")
    
    # 1. 编译正则表达式
    print("1. 编译正则表达式:")
    
    # 编译常用模式
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    phone_regex = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')
    
    test_text = "Contact: john@example.com or call 123-456-7890 for support."
    
    # 使用编译后的正则表达式
    email_matches = email_regex.findall(test_text)
    phone_matches = phone_regex.findall(test_text)
    
    print(f"  测试文本: {test_text}")
    print(f"  邮箱匹配: {email_matches}")
    print(f"  电话匹配: {phone_matches}")
    
    # 2. 性能比较
    print("\n2. 性能比较:")
    
    # 准备测试数据
    test_data = ["user{}@example{}.com".format(i, i%10) for i in range(1000)]
    test_string = " ".join(test_data)
    
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    compiled_pattern = re.compile(email_pattern)
    
    # 测试未编译版本
    start_time = time.time()
    for _ in range(100):
        re.findall(email_pattern, test_string)
    uncompiled_time = time.time() - start_time
    
    # 测试编译版本
    start_time = time.time()
    for _ in range(100):
        compiled_pattern.findall(test_string)
    compiled_time = time.time() - start_time
    
    print(f"  测试数据: {len(test_data)}个邮箱地址")
    print(f"  未编译版本: {uncompiled_time:.4f}秒")
    print(f"  编译版本: {compiled_time:.4f}秒")
    print(f"  性能提升: {uncompiled_time/compiled_time:.2f}倍")
    
    # 3. 编译标志
    print("\n3. 编译标志:")
    
    flags_demo = [
        (re.IGNORECASE, "忽略大小写", "HELLO", "hello"),
        (re.MULTILINE, "多行模式", "line1\nline2", "^line"),
        (re.DOTALL, "点匹配所有字符", "hello\nworld", "hello.world"),
        (re.VERBOSE, "详细模式", "123-456", r"""\d{3}  # 区号
                                                    -     # 分隔符
                                                    \d{3} # 前三位"""),
    ]
    
    print(f"  {'标志':<15} {'描述':<15} {'测试文本':<15} {'模式':<20} {'结果':<10}")
    print("-" * 80)
    
    for flag, description, text, pattern in flags_demo:
        try:
            if flag == re.VERBOSE:
                compiled = re.compile(pattern, flag)
                result = bool(compiled.search(text))
            else:
                result = bool(re.search(pattern, text, flag))
            
            status = "匹配" if result else "不匹配"
            pattern_display = pattern[:15] + "..." if len(pattern) > 15 else pattern
            print(f"  {flag.name:<15} {description:<15} {text:<15} {pattern_display:<20} {status:<10}")
        except Exception as e:
            print(f"  {flag.name:<15} {description:<15} {text:<15} {'错误':<20} {'失败':<10}")

def demonstrate_practical_examples():
    """演示实际应用示例"""
    print("\n=== 实际应用示例 ===")
    
    # 1. 日志分析
    print("1. 日志分析:")
    
    log_entries = [
        "2024-01-15 10:30:45 [INFO] User login successful: user123",
        "2024-01-15 10:31:02 [ERROR] Database connection failed",
        "2024-01-15 10:31:15 [WARNING] High memory usage: 85%",
        "2024-01-15 10:32:00 [INFO] User logout: user123",
        "2024-01-15 10:32:30 [ERROR] File not found: /path/to/file.txt",
    ]
    
    # 日志解析模式
    log_pattern = re.compile(
        r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
        r'\[(?P<level>\w+)\] '
        r'(?P<message>.+)'
    )
    
    print("  日志解析结果:")
    for log in log_entries:
        match = log_pattern.match(log)
        if match:
            info = match.groupdict()
            print(f"    时间: {info['timestamp']}, 级别: {info['level']}, 消息: {info['message'][:30]}...")
    
    # 统计错误日志
    error_count = sum(1 for log in log_entries if re.search(r'\[ERROR\]', log))
    print(f"  错误日志数量: {error_count}")
    
    # 2. 数据清洗
    print("\n2. 数据清洗:")
    
    dirty_data = [
        "  John   Doe  ",
        "JANE@EXAMPLE.COM",
        "(555) 123-4567",
        "  $1,234.56  ",
        "2024/01/15",
    ]
    
    def clean_data(data_list):
        """清洗数据"""
        cleaned = []
        
        for item in data_list:
            # 去除首尾空白
            item = item.strip()
            
            # 标准化姓名（首字母大写）
            if re.match(r'^[A-Za-z\s]+$', item):
                item = ' '.join(word.capitalize() for word in item.split())
            
            # 标准化邮箱（小写）
            elif re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', item, re.IGNORECASE):
                item = item.lower()
            
            # 标准化电话号码
            elif re.match(r'^\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}$', item):
                digits = re.sub(r'\D', '', item)
                item = f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
            
            # 标准化货币
            elif re.match(r'^\$[\d,]+\.\d{2}$', item):
                amount = re.sub(r'[^\d.]', '', item)
                item = f"${float(amount):.2f}"
            
            # 标准化日期
            elif re.match(r'^\d{4}[/-]\d{1,2}[/-]\d{1,2}$', item):
                item = re.sub(r'/', '-', item)
            
            cleaned.append(item)
        
        return cleaned
    
    print(f"  原始数据: {dirty_data}")
    cleaned_data = clean_data(dirty_data)
    print(f"  清洗后: {cleaned_data}")
    
    # 3. 文本提取和分析
    print("\n3. 文本提取和分析:")
    
    article_text = """
    Python是一种高级编程语言，由Guido van Rossum在1989年发明。
    Python的设计哲学强调代码的可读性和简洁的语法。
    目前最新版本是Python 3.12，发布于2023年。
    Python广泛应用于Web开发、数据科学、人工智能等领域。
    联系方式：python@python.org，官网：https://www.python.org
    """
    
    # 提取关键信息
    analysis_patterns = {
        '年份': r'\b(19|20)\d{2}\b',
        '版本号': r'Python\s+(\d+\.\d+)',
        '人名': r'[A-Z][a-z]+\s+[A-Z][a-z]+\s+[A-Z][a-z]+',
        '邮箱': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'URL': r'https?://[^\s]+',
    }
    
    print(f"  分析文本: {article_text.strip()[:50]}...")
    
    for info_type, pattern in analysis_patterns.items():
        matches = re.findall(pattern, article_text)
        if matches:
            print(f"  {info_type}: {matches}")
    
    # 4. 模板替换
    print("\n4. 模板替换:")
    
    template = "Hello {{name}}, your order #{{order_id}} for ${{amount}} has been {{status}}."
    
    # 替换模板变量
    def replace_template(template_str, **kwargs):
        """替换模板中的变量"""
        def replacer(match):
            var_name = match.group(1)
            return str(kwargs.get(var_name, match.group(0)))
        
        return re.sub(r'\{\{(\w+)\}\}', replacer, template_str)
    
    # 测试模板替换
    test_data = {
        'name': 'John Doe',
        'order_id': '12345',
        'amount': '99.99',
        'status': 'confirmed'
    }
    
    result = replace_template(template, **test_data)
    print(f"  模板: {template}")
    print(f"  数据: {test_data}")
    print(f"  结果: {result}")

def main():
    """主函数，演示所有正则表达式功能"""
    print("Python正则表达式基础")
    print("=" * 50)
    
    demonstrate_regex_basics()
    demonstrate_re_functions()
    demonstrate_basic_patterns()
    demonstrate_quantifiers()
    demonstrate_groups_and_capture()
    demonstrate_common_patterns()
    demonstrate_compiled_regex()
    demonstrate_practical_examples()
    
    print("\n=== 总结 ===")
    print("1. 基础概念：模式匹配和元字符")
    print("2. re模块：search、match、findall等函数")
    print("3. 基本模式：字符类、量词、锚点")
    print("4. 高级功能：分组、捕获、命名分组")
    print("5. 常用模式：验证、提取、替换")
    print("6. 性能优化：编译正则表达式")
    print("7. 实际应用：日志分析、数据清洗、文本处理")
    print("8. 最佳实践：合理使用贪婪和非贪婪匹配")

if __name__ == "__main__":
    main()