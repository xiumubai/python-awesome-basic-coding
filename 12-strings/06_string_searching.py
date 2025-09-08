#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字符串查找和替换

本文件演示Python中字符串查找和替换的各种方法：
1. 基本查找方法（find、index、rfind、rindex）
2. 字符串替换（replace、translate）
3. 前缀和后缀检查（startswith、endswith）
4. 正则表达式查找和替换
5. 高级查找技巧
6. 性能优化和最佳实践

作者：Python学习教程
日期：2024年
"""

import re
import string

def demonstrate_basic_searching():
    """演示基本的字符串查找方法"""
    print("=== 基本字符串查找 ===")
    
    text = "Python is a powerful programming language. Python is easy to learn."
    print(f"示例文本: '{text}'")
    
    # find() 方法 - 返回第一次出现的位置，未找到返回-1
    print("\n1. find() 方法:")
    pos1 = text.find("Python")
    pos2 = text.find("Java")
    pos3 = text.find("is")
    
    print(f"find('Python'): {pos1}")
    print(f"find('Java'): {pos2}")
    print(f"find('is'): {pos3}")
    
    # 指定搜索范围
    pos4 = text.find("Python", 10)  # 从位置10开始搜索
    pos5 = text.find("is", 10, 30)  # 在位置10-30之间搜索
    print(f"find('Python', 10): {pos4}")
    print(f"find('is', 10, 30): {pos5}")
    
    # rfind() 方法 - 返回最后一次出现的位置
    print("\n2. rfind() 方法:")
    rpos1 = text.rfind("Python")
    rpos2 = text.rfind("is")
    rpos3 = text.rfind("xyz")
    
    print(f"rfind('Python'): {rpos1}")
    print(f"rfind('is'): {rpos2}")
    print(f"rfind('xyz'): {rpos3}")
    
    # index() 方法 - 类似find()，但未找到时抛出异常
    print("\n3. index() 方法:")
    try:
        idx1 = text.index("Python")
        print(f"index('Python'): {idx1}")
        
        idx2 = text.index("Java")  # 这会抛出异常
    except ValueError as e:
        print(f"index('Java') 抛出异常: {e}")
    
    # rindex() 方法 - 类似rfind()，但未找到时抛出异常
    print("\n4. rindex() 方法:")
    try:
        ridx1 = text.rindex("Python")
        print(f"rindex('Python'): {ridx1}")
        
        ridx2 = text.rindex("xyz")  # 这会抛出异常
    except ValueError as e:
        print(f"rindex('xyz') 抛出异常: {e}")
    
    # 查找所有出现位置
    print("\n5. 查找所有出现位置:")
    def find_all_positions(text, substring):
        positions = []
        start = 0
        while True:
            pos = text.find(substring, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1
        return positions
    
    all_positions = find_all_positions(text, "is")
    print(f"'is' 的所有位置: {all_positions}")
    
    # 验证找到的位置
    for pos in all_positions:
        found_text = text[pos:pos+2]
        print(f"  位置 {pos}: '{found_text}'")

def demonstrate_prefix_suffix_checking():
    """演示前缀和后缀检查"""
    print("\n=== 前缀和后缀检查 ===")
    
    # 单个前缀/后缀检查
    filenames = [
        "document.txt",
        "image.jpg",
        "script.py",
        "data.csv",
        "backup_file.bak",
        "temp_data.tmp"
    ]
    
    print("文件名列表:", filenames)
    
    # startswith() 检查前缀
    print("\n1. startswith() 检查前缀:")
    for filename in filenames:
        if filename.startswith("temp"):
            print(f"  临时文件: {filename}")
        elif filename.startswith("backup"):
            print(f"  备份文件: {filename}")
        else:
            print(f"  普通文件: {filename}")
    
    # endswith() 检查后缀
    print("\n2. endswith() 检查后缀:")
    for filename in filenames:
        if filename.endswith(".txt"):
            print(f"  文本文件: {filename}")
        elif filename.endswith(".py"):
            print(f"  Python文件: {filename}")
        elif filename.endswith((".jpg", ".png", ".gif")):
            print(f"  图片文件: {filename}")
        else:
            print(f"  其他文件: {filename}")
    
    # 多个前缀/后缀检查
    print("\n3. 多个前缀/后缀检查:")
    
    # 检查多个前缀
    prefixes = ("temp", "backup", "old")
    special_files = [f for f in filenames if f.startswith(prefixes)]
    print(f"特殊前缀文件: {special_files}")
    
    # 检查多个后缀
    code_extensions = (".py", ".js", ".java", ".cpp")
    code_files = [f for f in filenames if f.endswith(code_extensions)]
    print(f"代码文件: {code_files}")
    
    # 大小写敏感性
    print("\n4. 大小写敏感性:")
    text = "Hello World"
    print(f"文本: '{text}'")
    print(f"startswith('Hello'): {text.startswith('Hello')}")
    print(f"startswith('hello'): {text.startswith('hello')}")
    print(f"startswith('hello') (忽略大小写): {text.lower().startswith('hello')}")
    
    # 指定搜索范围
    print("\n5. 指定搜索范围:")
    sentence = "The quick brown fox jumps over the lazy dog"
    print(f"句子: '{sentence}'")
    
    # 在指定范围内检查前缀
    result1 = sentence.startswith("quick", 4)  # 从位置4开始
    result2 = sentence.startswith("brown", 10, 15)  # 在位置10-15之间
    
    print(f"startswith('quick', 4): {result1}")
    print(f"startswith('brown', 10, 15): {result2}")

def demonstrate_string_replacement():
    """演示字符串替换操作"""
    print("\n=== 字符串替换 ===")
    
    # 基本替换
    text = "Hello World! Hello Python! Hello Programming!"
    print(f"原文: '{text}'")
    
    # replace() 方法
    print("\n1. replace() 方法:")
    
    # 替换所有出现
    result1 = text.replace("Hello", "Hi")
    print(f"replace('Hello', 'Hi'): '{result1}'")
    
    # 限制替换次数
    result2 = text.replace("Hello", "Hi", 2)
    print(f"replace('Hello', 'Hi', 2): '{result2}'")
    
    # 替换单个字符
    result3 = text.replace("!", ".")
    print(f"replace('!', '.'): '{result3}'")
    
    # 删除字符（替换为空字符串）
    result4 = text.replace(" ", "")
    print(f"删除空格: '{result4}'")
    
    # 链式替换
    print("\n2. 链式替换:")
    messy_text = "  Hello,,,World!!!  "
    cleaned = messy_text.strip().replace(",,,", ", ").replace("!!!", "!")
    print(f"原文: '{messy_text}'")
    print(f"清理后: '{cleaned}'")
    
    # 大小写敏感替换
    print("\n3. 大小写敏感替换:")
    mixed_case = "Python python PYTHON PyThOn"
    print(f"原文: '{mixed_case}'")
    
    # 只替换精确匹配
    result5 = mixed_case.replace("python", "Java")
    print(f"精确替换: '{result5}'")
    
    # 大小写不敏感替换（需要额外处理）
    def case_insensitive_replace(text, old, new):
        # 使用正则表达式进行大小写不敏感替换
        import re
        return re.sub(re.escape(old), new, text, flags=re.IGNORECASE)
    
    result6 = case_insensitive_replace(mixed_case, "python", "Java")
    print(f"忽略大小写替换: '{result6}'")
    
    # 多个替换
    print("\n4. 多个替换:")
    
    # 方法1：连续替换
    code = "var x = 10; var y = 20; var z = x + y;"
    js_to_py = code.replace("var ", "").replace(";", "").replace(" = ", " = ")
    print(f"JS代码: '{code}'")
    print(f"转换后: '{js_to_py}'")
    
    # 方法2：使用字典批量替换
    def multiple_replace(text, replacements):
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text
    
    replacements = {
        "var ": "",
        ";": "",
        "let ": "",
        "const ": ""
    }
    
    js_code = "let name = 'Alice'; const age = 25; var city = 'New York';"
    py_code = multiple_replace(js_code, replacements)
    print(f"\nJS代码: '{js_code}'")
    print(f"Python风格: '{py_code}'")

def demonstrate_translate_method():
    """演示translate()方法进行字符映射"""
    print("\n=== translate() 方法 ===")
    
    # 创建翻译表
    print("1. 基本字符翻译:")
    
    # 使用str.maketrans()创建翻译表
    translation_table = str.maketrans("aeiou", "12345")
    text = "Hello World"
    result = text.translate(translation_table)
    
    print(f"原文: '{text}'")
    print(f"元音替换为数字: '{result}'")
    
    # 删除字符
    print("\n2. 删除字符:")
    
    # 删除标点符号
    punctuation_table = str.maketrans("", "", string.punctuation)
    sentence = "Hello, World! How are you?"
    no_punct = sentence.translate(punctuation_table)
    
    print(f"原文: '{sentence}'")
    print(f"删除标点: '{no_punct}'")
    
    # 复杂翻译
    print("\n3. 复杂字符翻译:")
    
    # 创建ROT13编码
    rot13_table = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    )
    
    message = "Hello Python Programming"
    encoded = message.translate(rot13_table)
    decoded = encoded.translate(rot13_table)  # ROT13是自逆的
    
    print(f"原文: '{message}'")
    print(f"ROT13编码: '{encoded}'")
    print(f"ROT13解码: '{decoded}'")
    
    # 数字和字母分离
    print("\n4. 字符分类翻译:")
    
    # 将数字替换为#，字母替换为*
    mixed_text = "abc123def456ghi"
    digit_to_hash = str.maketrans("0123456789", "##########")
    alpha_to_star = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "*" * 52
    )
    
    print(f"原文: '{mixed_text}'")
    print(f"数字->井号: '{mixed_text.translate(digit_to_hash)}'")
    print(f"字母->星号: '{mixed_text.translate(alpha_to_star)}'")
    
    # 组合翻译表
    combined_table = str.maketrans(
        "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "##########" + "*" * 52
    )
    combined_result = mixed_text.translate(combined_table)
    print(f"组合翻译: '{combined_result}'")

def demonstrate_regex_searching():
    """演示正则表达式查找和替换"""
    print("\n=== 正则表达式查找替换 ===")
    
    text = "Contact us at: john@example.com, alice@test.org, or call 123-456-7890"
    print(f"示例文本: '{text}'")
    
    # 查找邮箱地址
    print("\n1. 查找邮箱地址:")
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    print(f"找到的邮箱: {emails}")
    
    # 查找电话号码
    print("\n2. 查找电话号码:")
    phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    phones = re.findall(phone_pattern, text)
    print(f"找到的电话: {phones}")
    
    # 使用search()查找第一个匹配
    print("\n3. search() 查找第一个匹配:")
    email_match = re.search(email_pattern, text)
    if email_match:
        print(f"第一个邮箱: '{email_match.group()}'")
        print(f"位置: {email_match.start()}-{email_match.end()}")
    
    # 使用finditer()获取详细信息
    print("\n4. finditer() 获取详细匹配信息:")
    for match in re.finditer(email_pattern, text):
        email = match.group()
        start, end = match.span()
        print(f"邮箱: '{email}', 位置: {start}-{end}")
    
    # 正则替换
    print("\n5. 正则表达式替换:")
    
    # 隐藏邮箱地址
    hidden_emails = re.sub(email_pattern, "[EMAIL]", text)
    print(f"隐藏邮箱: '{hidden_emails}'")
    
    # 隐藏电话号码
    hidden_phones = re.sub(phone_pattern, "[PHONE]", text)
    print(f"隐藏电话: '{hidden_phones}'")
    
    # 使用捕获组进行复杂替换
    print("\n6. 使用捕获组替换:")
    
    # 交换名字和姓氏
    names_text = "John Smith, Alice Johnson, Bob Wilson"
    name_pattern = r'(\w+)\s+(\w+)'
    swapped_names = re.sub(name_pattern, r'\2, \1', names_text)
    print(f"原文: '{names_text}'")
    print(f"交换后: '{swapped_names}'")
    
    # 格式化日期
    date_text = "Today is 2024-01-15 and tomorrow is 2024-01-16"
    date_pattern = r'(\d{4})-(\d{2})-(\d{2})'
    formatted_dates = re.sub(date_pattern, r'\3/\2/\1', date_text)
    print(f"\n原日期: '{date_text}'")
    print(f"格式化后: '{formatted_dates}'")
    
    # 使用函数进行替换
    print("\n7. 使用函数进行替换:")
    
    def format_phone(match):
        phone = match.group()
        # 将 123-456-7890 格式化为 (123) 456-7890
        parts = phone.split('-')
        return f"({parts[0]}) {parts[1]}-{parts[2]}"
    
    formatted_text = re.sub(phone_pattern, format_phone, text)
    print(f"格式化电话: '{formatted_text}'")

def demonstrate_advanced_searching():
    """演示高级查找技巧"""
    print("\n=== 高级查找技巧 ===")
    
    # 1. 模糊匹配
    print("1. 模糊匹配:")
    
    def fuzzy_find(text, pattern, max_errors=1):
        """简单的模糊匹配实现"""
        import difflib
        words = text.split()
        matches = []
        
        for word in words:
            similarity = difflib.SequenceMatcher(None, pattern.lower(), word.lower()).ratio()
            if similarity >= 0.7:  # 70%相似度
                matches.append((word, similarity))
        
        return sorted(matches, key=lambda x: x[1], reverse=True)
    
    text = "Python programming is powerful and pythonic"
    pattern = "python"
    fuzzy_matches = fuzzy_find(text, pattern)
    print(f"文本: '{text}'")
    print(f"模糊匹配 '{pattern}': {fuzzy_matches}")
    
    # 2. 上下文查找
    print("\n2. 上下文查找:")
    
    def find_with_context(text, pattern, context_size=10):
        """查找并返回上下文"""
        matches = []
        start = 0
        
        while True:
            pos = text.find(pattern, start)
            if pos == -1:
                break
            
            # 获取上下文
            context_start = max(0, pos - context_size)
            context_end = min(len(text), pos + len(pattern) + context_size)
            context = text[context_start:context_end]
            
            matches.append({
                'position': pos,
                'context': context,
                'match': pattern
            })
            
            start = pos + 1
        
        return matches
    
    long_text = "Python is a programming language. Python is easy to learn. Many developers love Python."
    context_matches = find_with_context(long_text, "Python", 15)
    
    print(f"文本: '{long_text}'")
    print(f"查找 'Python' 的上下文:")
    for i, match in enumerate(context_matches, 1):
        print(f"  匹配{i}: 位置{match['position']}, 上下文: '{match['context']}'")
    
    # 3. 多模式查找
    print("\n3. 多模式查找:")
    
    def multi_pattern_search(text, patterns):
        """同时查找多个模式"""
        results = {}
        
        for pattern in patterns:
            positions = []
            start = 0
            while True:
                pos = text.find(pattern, start)
                if pos == -1:
                    break
                positions.append(pos)
                start = pos + 1
            results[pattern] = positions
        
        return results
    
    code_text = "def function(): return value + variable"
    keywords = ["def", "return", "value", "variable"]
    multi_results = multi_pattern_search(code_text, keywords)
    
    print(f"代码: '{code_text}'")
    print("多模式查找结果:")
    for pattern, positions in multi_results.items():
        print(f"  '{pattern}': {positions}")
    
    # 4. 统计和分析
    print("\n4. 查找统计分析:")
    
    def analyze_text_patterns(text):
        """分析文本中的模式"""
        import collections
        
        # 单词频率
        words = re.findall(r'\b\w+\b', text.lower())
        word_freq = collections.Counter(words)
        
        # 字符频率
        chars = [c for c in text.lower() if c.isalpha()]
        char_freq = collections.Counter(chars)
        
        # 长度统计
        word_lengths = [len(word) for word in words]
        avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
        
        return {
            'word_count': len(words),
            'unique_words': len(word_freq),
            'most_common_words': word_freq.most_common(5),
            'most_common_chars': char_freq.most_common(5),
            'average_word_length': avg_length
        }
    
    sample_text = "Python programming is fun. Python is powerful. Programming with Python is enjoyable."
    analysis = analyze_text_patterns(sample_text)
    
    print(f"分析文本: '{sample_text}'")
    print(f"单词总数: {analysis['word_count']}")
    print(f"唯一单词: {analysis['unique_words']}")
    print(f"最常见单词: {analysis['most_common_words']}")
    print(f"最常见字符: {analysis['most_common_chars']}")
    print(f"平均单词长度: {analysis['average_word_length']:.2f}")

def demonstrate_performance_tips():
    """演示查找和替换的性能优化技巧"""
    print("\n=== 性能优化技巧 ===")
    
    import time
    
    # 创建测试数据
    large_text = "Python programming " * 10000
    
    def time_operation(func, description):
        start = time.time()
        result = func()
        end = time.time()
        print(f"{description}: {end - start:.6f}秒")
        return result
    
    print("性能比较（处理大文本）:")
    
    # 1. 字符串查找性能
    print("\n1. 查找性能比较:")
    
    def find_method():
        return large_text.find("programming")
    
    def regex_method():
        return re.search(r"programming", large_text)
    
    def in_operator():
        return "programming" in large_text
    
    time_operation(find_method, "str.find()")
    time_operation(regex_method, "re.search()")
    time_operation(in_operator, "in 操作符")
    
    # 2. 替换性能比较
    print("\n2. 替换性能比较:")
    
    def str_replace():
        return large_text.replace("Python", "Java")
    
    def regex_replace():
        return re.sub(r"Python", "Java", large_text)
    
    time_operation(str_replace, "str.replace()")
    time_operation(regex_replace, "re.sub()")
    
    # 3. 性能建议
    print("\n性能建议:")
    print("1. 简单查找：使用 str.find() 或 in 操作符")
    print("2. 简单替换：使用 str.replace()")
    print("3. 复杂模式：使用正则表达式")
    print("4. 大量操作：预编译正则表达式")
    print("5. 频繁查找：考虑使用索引或数据结构优化")
    
    # 4. 预编译正则表达式
    print("\n4. 预编译正则表达式:")
    
    pattern = re.compile(r"\b\w+ing\b")
    
    def compiled_regex():
        return pattern.findall(large_text)
    
    def non_compiled_regex():
        return re.findall(r"\b\w+ing\b", large_text)
    
    time_operation(compiled_regex, "预编译正则")
    time_operation(non_compiled_regex, "非预编译正则")

def main():
    """主函数，演示所有字符串查找和替换方法"""
    print("Python字符串查找和替换")
    print("=" * 50)
    
    demonstrate_basic_searching()
    demonstrate_prefix_suffix_checking()
    demonstrate_string_replacement()
    demonstrate_translate_method()
    demonstrate_regex_searching()
    demonstrate_advanced_searching()
    demonstrate_performance_tips()
    
    print("\n=== 总结 ===")
    print("1. 基本查找：find()、rfind()、index()、rindex()")
    print("2. 前缀后缀：startswith()、endswith()")
    print("3. 字符串替换：replace()、translate()")
    print("4. 正则表达式：re.search()、re.findall()、re.sub()")
    print("5. 高级技巧：模糊匹配、上下文查找、多模式")
    print("6. 性能优化：选择合适方法、预编译正则")
    print("7. 最佳实践：简单用内置方法，复杂用正则")

if __name__ == "__main__":
    main()