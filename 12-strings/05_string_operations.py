#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字符串操作和连接

本文件演示Python中字符串操作和连接的各种方法：
1. 字符串连接方法
2. 字符串重复
3. 字符串比较
4. 字符串包含检查
5. 字符串长度和计数
6. 字符串转换操作
7. 性能比较和最佳实践

作者：Python学习教程
日期：2024年
"""

import time
import sys

def demonstrate_string_concatenation():
    """演示字符串连接的各种方法"""
    print("=== 字符串连接方法 ===")
    
    # 1. 使用 + 操作符
    first = "Hello"
    second = "World"
    result1 = first + " " + second
    print(f"+ 操作符: {result1}")
    
    # 2. 使用 += 操作符
    message = "Python"
    message += " is"
    message += " awesome!"
    print(f"+= 操作符: {message}")
    
    # 3. 使用 join() 方法
    words = ["Python", "is", "a", "great", "language"]
    result2 = " ".join(words)
    print(f"join方法: {result2}")
    
    # 4. 使用 format() 方法
    template = "{} {} {}"
    result3 = template.format("Learning", "Python", "programming")
    print(f"format方法: {result3}")
    
    # 5. 使用 f-string
    name = "Alice"
    age = 25
    result4 = f"My name is {name} and I am {age} years old"
    print(f"f-string: {result4}")
    
    # 6. 使用 % 格式化
    result5 = "Hello %s, you have %d messages" % ("Bob", 5)
    print(f"% 格式化: {result5}")
    
    # 7. 多行字符串连接
    long_text = (
        "This is a very long string that "
        "spans multiple lines and is "
        "concatenated automatically by Python"
    )
    print(f"多行连接: {long_text}")
    
    # 8. 使用 StringIO（适合大量字符串操作）
    from io import StringIO
    buffer = StringIO()
    buffer.write("Hello")
    buffer.write(" ")
    buffer.write("from")
    buffer.write(" ")
    buffer.write("StringIO")
    result6 = buffer.getvalue()
    buffer.close()
    print(f"StringIO: {result6}")

def demonstrate_string_repetition():
    """演示字符串重复操作"""
    print("\n=== 字符串重复 ===")
    
    # 基本重复
    char = "*"
    line = char * 50
    print(f"重复字符: {line}")
    
    # 重复单词
    word = "Python "
    repeated = word * 5
    print(f"重复单词: {repeated}")
    
    # 创建分隔线
    separator = "-" * 30
    print(f"分隔线: {separator}")
    
    # 创建表格边框
    border = "+" + "-" * 10 + "+" + "-" * 15 + "+" + "-" * 8 + "+"
    print(f"表格边框: {border}")
    
    # 重复空格（缩进）
    indent_level = 3
    indent = "    " * indent_level  # 4个空格 * 3 = 12个空格
    code_line = indent + "print('Hello, World!')"
    print(f"缩进代码: '{code_line}'")
    
    # 创建进度条
    progress = 75  # 75%
    bar_length = 20
    filled_length = int(bar_length * progress / 100)
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    print(f"进度条: [{bar}] {progress}%")
    
    # 重复复杂字符串
    pattern = "ABC"
    repeated_pattern = pattern * 8
    print(f"重复模式: {repeated_pattern}")
    
    # 零次重复
    empty = "Hello" * 0
    print(f"零次重复: '{empty}'")
    
    # 负数重复（结果为空字符串）
    negative = "Hello" * -1
    print(f"负数重复: '{negative}'")

def demonstrate_string_comparison():
    """演示字符串比较操作"""
    print("\n=== 字符串比较 ===")
    
    # 相等比较
    str1 = "Python"
    str2 = "Python"
    str3 = "python"
    
    print(f"'{str1}' == '{str2}': {str1 == str2}")
    print(f"'{str1}' == '{str3}': {str1 == str3}")
    print(f"'{str1}' != '{str3}': {str1 != str3}")
    
    # 大小写不敏感比较
    print(f"忽略大小写比较: {str1.lower() == str3.lower()}")
    
    # 字典序比较
    words = ["apple", "banana", "cherry", "date"]
    print("\n字典序比较:")
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        print(f"'{word1}' < '{word2}': {word1 < word2}")
    
    # 长度比较
    short = "Hi"
    long_str = "Hello"
    print(f"\n长度比较:")
    print(f"'{short}' < '{long_str}': {short < long_str}")
    print(f"len('{short}') < len('{long_str}'): {len(short) < len(long_str)}")
    
    # 数字字符串比较
    num_str1 = "10"
    num_str2 = "2"
    print(f"\n数字字符串比较:")
    print(f"'{num_str1}' < '{num_str2}': {num_str1 < num_str2}")
    print(f"int('{num_str1}') < int('{num_str2}'): {int(num_str1) < int(num_str2)}")
    
    # 特殊字符比较
    special1 = "Hello!"
    special2 = "Hello?"
    print(f"\n特殊字符比较:")
    print(f"'{special1}' < '{special2}': {special1 < special2}")
    print(f"ord('!'): {ord('!')}, ord('?'): {ord('?')}")
    
    # 空字符串比较
    empty = ""
    non_empty = "a"
    print(f"\n空字符串比较:")
    print(f"'{empty}' < '{non_empty}': {empty < non_empty}")
    print(f"'{empty}' == '': {empty == ''}")

def demonstrate_string_membership():
    """演示字符串包含检查"""
    print("\n=== 字符串包含检查 ===")
    
    text = "Python is a powerful programming language"
    
    # 基本包含检查
    print(f"文本: '{text}'")
    print(f"\n基本包含检查:")
    print(f"'Python' in text: {'Python' in text}")
    print(f"'Java' in text: {'Java' in text}")
    print(f"'python' in text: {'python' in text}")
    
    # 不包含检查
    print(f"\n不包含检查:")
    print(f"'Java' not in text: {'Java' not in text}")
    print(f"'Python' not in text: {'Python' not in text}")
    
    # 大小写不敏感检查
    print(f"\n大小写不敏感检查:")
    print(f"'python' in text.lower(): {'python' in text.lower()}")
    print(f"'PYTHON' in text.upper(): {'PYTHON' in text.upper()}")
    
    # 子字符串检查
    substrings = ["Python", "power", "program", "language", "script"]
    print(f"\n子字符串检查:")
    for substring in substrings:
        result = substring in text
        print(f"'{substring}' in text: {result}")
    
    # 字符检查
    chars = ['P', 'y', 'z', '!', ' ']
    print(f"\n字符检查:")
    for char in chars:
        result = char in text
        print(f"'{char}' in text: {result}")
    
    # 多个条件检查
    keywords = ["Python", "programming"]
    all_present = all(keyword in text for keyword in keywords)
    any_present = any(keyword in text for keyword in keywords)
    
    print(f"\n多条件检查:")
    print(f"所有关键词都存在: {all_present}")
    print(f"任一关键词存在: {any_present}")
    
    # 使用正则表达式进行复杂匹配
    import re
    pattern = r'\b[Pp]ython\b'  # 匹配单词边界的Python（大小写不敏感）
    match = re.search(pattern, text)
    print(f"\n正则匹配:")
    print(f"模式 '{pattern}' 匹配: {match is not None}")
    if match:
        print(f"匹配位置: {match.start()}-{match.end()}")
        print(f"匹配内容: '{match.group()}'")

def demonstrate_string_length_and_count():
    """演示字符串长度和计数操作"""
    print("\n=== 字符串长度和计数 ===")
    
    # 基本长度
    texts = [
        "Hello",
        "Python Programming",
        "",
        "   spaces   ",
        "Hello\nWorld",
        "中文字符串",
        "Mixed中英文String"
    ]
    
    print("字符串长度:")
    for text in texts:
        print(f"'{text}' -> 长度: {len(text)}")
    
    # 字符计数
    sample_text = "Hello, World! Welcome to Python programming."
    print(f"\n示例文本: '{sample_text}'")
    print(f"总长度: {len(sample_text)}")
    
    # 统计特定字符
    char_counts = {
        'l': sample_text.count('l'),
        'o': sample_text.count('o'),
        'e': sample_text.count('e'),
        ' ': sample_text.count(' '),
        ',': sample_text.count(','),
        '.': sample_text.count('.')
    }
    
    print("\n字符计数:")
    for char, count in char_counts.items():
        print(f"'{char}': {count}次")
    
    # 统计子字符串
    substring_counts = {
        'o': sample_text.count('o'),
        'lo': sample_text.count('lo'),
        'llo': sample_text.count('llo'),
        'Python': sample_text.count('Python'),
        'python': sample_text.count('python')
    }
    
    print("\n子字符串计数:")
    for substring, count in substring_counts.items():
        print(f"'{substring}': {count}次")
    
    # 统计单词数量
    words = sample_text.split()
    print(f"\n单词统计:")
    print(f"单词列表: {words}")
    print(f"单词数量: {len(words)}")
    
    # 统计行数
    multiline_text = """第一行
第二行
第三行
最后一行"""
    lines = multiline_text.split('\n')
    print(f"\n多行文本统计:")
    print(f"行数: {len(lines)}")
    print(f"总字符数: {len(multiline_text)}")
    print(f"非空行数: {len([line for line in lines if line.strip()])}")
    
    # 字符类型统计
    mixed_text = "Hello123!@# World456"
    stats = {
        '字母': sum(1 for c in mixed_text if c.isalpha()),
        '数字': sum(1 for c in mixed_text if c.isdigit()),
        '空格': sum(1 for c in mixed_text if c.isspace()),
        '标点': sum(1 for c in mixed_text if not c.isalnum() and not c.isspace()),
        '字母数字': sum(1 for c in mixed_text if c.isalnum())
    }
    
    print(f"\n字符类型统计 ('{mixed_text}'):")
    for char_type, count in stats.items():
        print(f"{char_type}: {count}个")

def demonstrate_string_transformations():
    """演示字符串转换操作"""
    print("\n=== 字符串转换操作 ===")
    
    original = "  Hello, Python World!  "
    print(f"原始字符串: '{original}'")
    
    # 大小写转换
    print("\n大小写转换:")
    print(f"upper(): '{original.upper()}'")
    print(f"lower(): '{original.lower()}'")
    print(f"title(): '{original.title()}'")
    print(f"capitalize(): '{original.capitalize()}'")
    print(f"swapcase(): '{original.swapcase()}'")
    
    # 空白字符处理
    print("\n空白字符处理:")
    print(f"strip(): '{original.strip()}'")
    print(f"lstrip(): '{original.lstrip()}'")
    print(f"rstrip(): '{original.rstrip()}'")
    
    # 字符替换
    print("\n字符替换:")
    text = "Hello, World!"
    print(f"原文: '{text}'")
    print(f"replace('o', '0'): '{text.replace('o', '0')}'")
    print(f"replace('l', 'L', 1): '{text.replace('l', 'L', 1)}'")
    print(f"replace('Hello', 'Hi'): '{text.replace('Hello', 'Hi')}'")
    
    # 字符串分割
    print("\n字符串分割:")
    sentence = "apple,banana,cherry,date"
    print(f"原文: '{sentence}'")
    print(f"split(','): {sentence.split(',')}")
    print(f"split(',', 2): {sentence.split(',', 2)}")
    
    # 多种分隔符分割
    complex_text = "apple;banana,cherry:date"
    import re
    parts = re.split('[;,:]+', complex_text)
    print(f"复杂分割: '{complex_text}' -> {parts}")
    
    # 字符串连接
    print("\n字符串连接:")
    fruits = ['apple', 'banana', 'cherry']
    print(f"列表: {fruits}")
    print(f"join(', '): '{', '.join(fruits)}'")
    print(f"join(' | '): '{' | '.join(fruits)}'")
    # print(f"join(''): '{'.join(fruits)}'")
    
    # 字符串填充和对齐
    print("\n字符串填充和对齐:")
    word = "Python"
    width = 20
    print(f"原词: '{word}'")
    print(f"ljust({width}): '{word.ljust(width)}'")
    print(f"rjust({width}): '{word.rjust(width)}'")
    print(f"center({width}): '{word.center(width)}'")
    print(f"center({width}, '*'): '{word.center(width, '*')}'")
    print(f"zfill(10): '{word.zfill(10)}'")
    
    # 数字字符串填充
    number = "42"
    print(f"\n数字填充:")
    print(f"zfill(5): '{number.zfill(5)}'")
    print(f"rjust(5, '0'): '{number.rjust(5, '0')}'")

def demonstrate_performance_comparison():
    """演示不同字符串操作的性能比较"""
    print("\n=== 性能比较 ===")
    
    # 字符串连接性能比较
    def time_operation(operation, description):
        start_time = time.time()
        result = operation()
        end_time = time.time()
        print(f"{description}: {end_time - start_time:.6f}秒")
        return result
    
    n = 1000
    words = ["word"] * n
    
    print(f"连接{n}个字符串的性能比较:")
    
    # 方法1: 使用 + 操作符
    def concat_with_plus():
        result = ""
        for word in words:
            result = result + word
        return result
    
    # 方法2: 使用 += 操作符
    def concat_with_plus_equal():
        result = ""
        for word in words:
            result += word
        return result
    
    # 方法3: 使用 join 方法
    def concat_with_join():
        return "".join(words)
    
    # 方法4: 使用列表推导式和join
    def concat_with_list_comp():
        return "".join([word for word in words])
    
    # 性能测试
    print("\n小规模测试 (1000个字符串):")
    result1 = time_operation(concat_with_plus, "+ 操作符")
    result2 = time_operation(concat_with_plus_equal, "+= 操作符")
    result3 = time_operation(concat_with_join, "join 方法")
    result4 = time_operation(concat_with_list_comp, "列表推导+join")
    
    # 验证结果一致性
    print(f"\n结果一致性检查: {result1 == result2 == result3 == result4}")
    print(f"结果长度: {len(result1)}")
    
    # 内存使用建议
    print("\n性能建议:")
    print("1. 少量字符串连接: 使用 + 或 += 操作符")
    print("2. 大量字符串连接: 使用 join() 方法")
    print("3. 格式化字符串: 优先使用 f-string")
    print("4. 模板字符串: 使用 str.format() 或 Template")
    print("5. 避免在循环中使用 + 连接大量字符串")

def demonstrate_best_practices():
    """演示字符串操作的最佳实践"""
    print("\n=== 最佳实践 ===")
    
    # 1. 字符串不可变性
    print("1. 理解字符串不可变性:")
    original = "Hello"
    print(f"原始字符串: id={id(original)}, value='{original}'")
    
    # 这实际上创建了新字符串
    modified = original + " World"
    print(f"修改后字符串: id={id(modified)}, value='{modified}'")
    print(f"原始字符串未变: '{original}'")
    
    # 2. 选择合适的连接方法
    print("\n2. 选择合适的连接方法:")
    
    # 少量连接 - 使用 +
    name = "Alice"
    greeting = "Hello " + name + "!"
    print(f"少量连接: {greeting}")
    
    # 多个字符串 - 使用 join
    parts = ["Python", "is", "awesome"]
    sentence = " ".join(parts)
    print(f"多个连接: {sentence}")
    
    # 格式化 - 使用 f-string
    age = 25
    message = f"{name} is {age} years old"
    print(f"格式化: {message}")
    
    # 3. 避免常见错误
    print("\n3. 避免常见错误:")
    
    # 错误：在循环中使用 + 连接
    print("❌ 错误做法（性能差）:")
    # result = ""
    # for i in range(5):
    #     result = result + str(i)  # 每次都创建新字符串
    
    # 正确：使用列表收集然后join
    print("✅ 正确做法（性能好）:")
    parts = []
    for i in range(5):
        parts.append(str(i))
    result = "".join(parts)
    print(f"结果: {result}")
    
    # 4. 字符串比较最佳实践
    print("\n4. 字符串比较最佳实践:")
    
    user_input = "PYTHON"
    # 大小写不敏感比较
    if user_input.lower() == "python":
        print("✅ 正确的大小写不敏感比较")
    
    # 检查空字符串
    text = "   "
    if not text.strip():  # 比 text.strip() == "" 更pythonic
        print("✅ 正确的空字符串检查")
    
    # 5. 字符串格式化最佳实践
    print("\n5. 字符串格式化最佳实践:")
    
    data = {"name": "Bob", "score": 95.5, "rank": 1}
    
    # 使用f-string（推荐）
    report = f"{data['name']} scored {data['score']:.1f} and ranked #{data['rank']}"
    print(f"f-string: {report}")
    
    # 复杂格式使用format
    template = "{name} scored {score:.1f} and ranked #{rank}"
    report2 = template.format(**data)
    print(f"format: {report2}")
    
    print("\n总结:")
    print("- 理解字符串不可变性")
    print("- 选择合适的连接方法")
    print("- 使用f-string进行格式化")
    print("- 避免在循环中使用+连接")
    print("- 使用适当的比较方法")
    print("- 考虑性能和可读性")

def main():
    """主函数，演示所有字符串操作"""
    print("Python字符串操作和连接")
    print("=" * 50)
    
    demonstrate_string_concatenation()
    demonstrate_string_repetition()
    demonstrate_string_comparison()
    demonstrate_string_membership()
    demonstrate_string_length_and_count()
    demonstrate_string_transformations()
    demonstrate_performance_comparison()
    demonstrate_best_practices()
    
    print("\n=== 总结 ===")
    print("1. 字符串连接：+、+=、join()、format()、f-string")
    print("2. 字符串重复：* 操作符")
    print("3. 字符串比较：==、!=、<、>、字典序")
    print("4. 包含检查：in、not in 操作符")
    print("5. 长度计数：len()、count() 方法")
    print("6. 字符串转换：大小写、去空格、替换、分割")
    print("7. 性能考虑：选择合适的方法")
    print("8. 最佳实践：可读性和性能的平衡")

if __name__ == "__main__":
    main()