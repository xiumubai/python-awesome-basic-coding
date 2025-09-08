#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - 循环遍历字符串

本文件演示各种遍历字符串的方法和字符串处理技巧。
字符串是Python中重要的数据类型，掌握字符串的遍历和处理对文本处理非常重要。

学习目标：
1. 掌握遍历字符串的基本方法
2. 学会字符串的查找、统计和替换
3. 了解字符串的分割和连接
4. 掌握字符串的格式化和验证

作者：Python学习教程
日期：2024年
"""

# 1. 基本的字符串遍历
print("=== 1. 基本的字符串遍历 ===")
text = "Python编程"
print(f"字符串：{text}")
print()

print("方法1：直接遍历字符")
for char in text:
    print(f"  字符：'{char}'")
print()

print("方法2：使用索引遍历")
for i in range(len(text)):
    print(f"  索引{i}：'{text[i]}'")
print()

print("方法3：使用enumerate获取索引和字符")
for i, char in enumerate(text):
    print(f"  位置{i}：'{char}'")
print()

# 2. 字符统计
print("=== 2. 字符统计 ===")
sentence = "Hello World! Welcome to Python programming."
print(f"句子：{sentence}")
print()

print("统计各类字符数量：")
letters = 0
digits = 0
spaces = 0
punctuation = 0
other = 0

for char in sentence:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    elif char in ".,!?;:":
        punctuation += 1
    else:
        other += 1

print(f"  字母：{letters}个")
print(f"  数字：{digits}个")
print(f"  空格：{spaces}个")
print(f"  标点：{punctuation}个")
print(f"  其他：{other}个")
print()

# 3. 字符频率统计
print("=== 3. 字符频率统计 ===")
text = "programming"
print(f"单词：{text}")
print()

print("方法1：使用字典统计")
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("字符频率：")
for char, count in sorted(char_count.items()):
    print(f"  '{char}': {count}次")
print()

print("方法2：找出出现最多的字符")
max_char = ''
max_count = 0
for char, count in char_count.items():
    if count > max_count:
        max_count = count
        max_char = char
print(f"出现最多的字符：'{max_char}'，出现{max_count}次")
print()

# 4. 字符串查找和替换
print("=== 4. 字符串查找和替换 ===")
text = "Python is great. Python is powerful. Python is easy."
print(f"原文：{text}")
print()

print("查找所有'Python'的位置：")
target = "Python"
positions = []
for i in range(len(text) - len(target) + 1):
    if text[i:i+len(target)] == target:
        positions.append(i)
print(f"'{target}'出现的位置：{positions}")
print()

print("手动替换'Python'为'Java'：")
replacement = "Java"
new_text = ""
i = 0
while i < len(text):
    if i <= len(text) - len(target) and text[i:i+len(target)] == target:
        new_text += replacement
        i += len(target)
    else:
        new_text += text[i]
        i += 1
print(f"替换后：{new_text}")
print()

# 5. 字符串反转
print("=== 5. 字符串反转 ===")
original = "Hello World"
print(f"原字符串：{original}")
print()

print("方法1：使用循环反转")
reversed_str = ""
for char in original:
    reversed_str = char + reversed_str
print(f"反转结果：{reversed_str}")
print()

print("方法2：使用索引反转")
reversed_str2 = ""
for i in range(len(original) - 1, -1, -1):
    reversed_str2 += original[i]
print(f"反转结果：{reversed_str2}")
print()

print("方法3：使用切片（最简单）")
reversed_str3 = original[::-1]
print(f"反转结果：{reversed_str3}")
print()

# 6. 回文检测
print("=== 6. 回文检测 ===")
test_strings = ["level", "hello", "madam", "python", "racecar", "A man a plan a canal Panama"]

for test_str in test_strings:
    print(f"\n检测：'{test_str}'")
    
    # 清理字符串（去除空格和标点，转为小写）
    cleaned = ""
    for char in test_str:
        if char.isalnum():
            cleaned += char.lower()
    
    print(f"清理后：'{cleaned}'")
    
    # 检测是否为回文
    is_palindrome = True
    for i in range(len(cleaned) // 2):
        if cleaned[i] != cleaned[len(cleaned) - 1 - i]:
            is_palindrome = False
            break
    
    if is_palindrome:
        print("  结果：是回文")
    else:
        print("  结果：不是回文")
print()

# 7. 单词处理
print("=== 7. 单词处理 ===")
sentence = "Python is a powerful programming language"
print(f"句子：{sentence}")
print()

print("方法1：手动分割单词")
words = []
current_word = ""
for char in sentence:
    if char.isspace():
        if current_word:
            words.append(current_word)
            current_word = ""
    else:
        current_word += char
# 添加最后一个单词
if current_word:
    words.append(current_word)

print(f"单词列表：{words}")
print(f"单词数量：{len(words)}")
print()

print("统计每个单词的长度：")
for word in words:
    print(f"  '{word}': {len(word)}个字符")
print()

print("找出最长的单词：")
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"最长单词：'{longest_word}'，长度：{len(longest_word)}")
print()

# 8. 字符串格式验证
print("=== 8. 字符串格式验证 ===")

# 验证邮箱格式（简单版本）
def is_valid_email(email):
    """简单的邮箱格式验证"""
    at_count = 0
    dot_count = 0
    at_position = -1
    
    for i, char in enumerate(email):
        if char == '@':
            at_count += 1
            at_position = i
        elif char == '.':
            dot_count += 1
    
    # 基本验证：有且仅有一个@，至少有一个点，@不在开头或结尾
    if at_count == 1 and dot_count >= 1 and 0 < at_position < len(email) - 1:
        return True
    return False

email_tests = [
    "user@example.com",
    "invalid.email",
    "@example.com",
    "user@",
    "user@example.",
    "test.user@domain.co.uk"
]

print("邮箱格式验证：")
for email in email_tests:
    result = "有效" if is_valid_email(email) else "无效"
    print(f"  {email}: {result}")
print()

# 验证密码强度
def check_password_strength(password):
    """检查密码强度"""
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    length_ok = len(password) >= 8
    
    return {
        'length': length_ok,
        'has_upper': has_upper,
        'has_lower': has_lower,
        'has_digit': has_digit,
        'has_special': has_special,
        'score': score,
        'strength': 'weak' if score < 2 or not length_ok else 'medium' if score < 4 else 'strong'
    }

password_tests = [
    "123456",
    "password",
    "Password123",
    "MyP@ssw0rd!",
    "abc"
]

print("密码强度检测：")
for pwd in password_tests:
    result = check_password_strength(pwd)
    print(f"  密码：'{pwd}'")
    print(f"    长度≥8: {'✓' if result['length'] else '✗'}")
    print(f"    大写字母: {'✓' if result['has_upper'] else '✗'}")
    print(f"    小写字母: {'✓' if result['has_lower'] else '✗'}")
    print(f"    数字: {'✓' if result['has_digit'] else '✗'}")
    print(f"    特殊字符: {'✓' if result['has_special'] else '✗'}")
    print(f"    强度: {result['strength']}")
    print()

# 9. 文本处理应用
print("=== 9. 文本处理应用 ===")

# 应用1：统计文章词频
print("应用1：文章词频统计")
article = """
Python is a high-level programming language. 
Python is easy to learn and powerful to use.
Many developers choose Python for web development, 
data analysis, and artificial intelligence.
"""

print("原文：")
print(article.strip())
print()

# 清理文本并分割单词
cleaned_text = ""
for char in article.lower():
    if char.isalnum() or char.isspace():
        cleaned_text += char
    else:
        cleaned_text += " "

# 分割单词
words = []
current_word = ""
for char in cleaned_text:
    if char.isspace():
        if current_word:
            words.append(current_word)
            current_word = ""
    else:
        current_word += char
if current_word:
    words.append(current_word)

# 统计词频
word_count = {}
for word in words:
    if len(word) > 2:  # 只统计长度大于2的单词
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print("词频统计（长度>2的单词）：")
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}次")
print()

# 应用2：简单的文本加密（凯撒密码）
print("应用2：凯撒密码加密")
plaintext = "Hello World"
shift = 3
print(f"原文：{plaintext}")
print(f"位移：{shift}")

encrypted = ""
for char in plaintext:
    if char.isalpha():
        # 确定是大写还是小写
        if char.isupper():
            # 大写字母A-Z (ASCII 65-90)
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # 小写字母a-z (ASCII 97-122)
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        encrypted += encrypted_char
    else:
        encrypted += char

print(f"加密后：{encrypted}")

# 解密
decrypted = ""
for char in encrypted:
    if char.isalpha():
        if char.isupper():
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        decrypted += decrypted_char
    else:
        decrypted += char

print(f"解密后：{decrypted}")
print()

# 10. 字符串模式匹配
print("=== 10. 字符串模式匹配 ===")

# 简单的通配符匹配（只支持*）
def simple_match(pattern, text):
    """简单的通配符匹配，*表示任意字符序列"""
    if '*' not in pattern:
        return pattern == text
    
    parts = []
    current_part = ""
    for char in pattern:
        if char == '*':
            if current_part:
                parts.append(current_part)
                current_part = ""
            parts.append('*')
        else:
            current_part += char
    if current_part:
        parts.append(current_part)
    
    # 简化版匹配逻辑
    if len(parts) == 1:
        return parts[0] == '*' or parts[0] == text
    
    # 这里只演示简单情况
    if parts[0] != '*' and not text.startswith(parts[0]):
        return False
    if parts[-1] != '*' and not text.endswith(parts[-1]):
        return False
    
    return True

test_cases = [
    ("hello", "hello"),
    ("hello", "world"),
    ("*world", "hello world"),
    ("hello*", "hello world"),
    ("*", "anything"),
]

print("通配符匹配测试：")
for pattern, text in test_cases:
    result = simple_match(pattern, text)
    print(f"  模式'{pattern}' 匹配 '{text}': {'✓' if result else '✗'}")
print()

# 11. 练习题
print("=== 11. 练习题 ===")

print("练习1：统计字符串中每个单词的首字母")
sentence = "The Quick Brown Fox Jumps Over The Lazy Dog"
print(f"句子：{sentence}")

first_letters = []
words = sentence.split()
for word in words:
    if word:
        first_letters.append(word[0].upper())

print(f"首字母：{first_letters}")
print(f"首字母组成的字符串：{''.join(first_letters)}")
print()

print("练习2：检查字符串是否只包含数字和字母")
test_strings = ["Hello123", "Hello World", "Python3", "Test@123", "OnlyLetters"]
for test_str in test_strings:
    is_alnum = True
    for char in test_str:
        if not char.isalnum():
            is_alnum = False
            break
    result = "是" if is_alnum else "否"
    print(f"  '{test_str}': {result}")
print()

print("练习3：计算字符串的'数字值'（所有数字字符的和）")
test_string = "abc123def456ghi"
print(f"字符串：{test_string}")
digit_sum = 0
digits_found = []
for char in test_string:
    if char.isdigit():
        digit_value = int(char)
        digit_sum += digit_value
        digits_found.append(char)
print(f"找到的数字：{digits_found}")
print(f"数字和：{digit_sum}")

if __name__ == "__main__":
    print("\n=== 字符串遍历学习总结 ===")
    print("1. 基本遍历：for char in string")
    print("2. 索引遍历：for i in range(len(string))")
    print("3. enumerate：同时获取索引和字符")
    print("4. 字符统计：统计字母、数字、空格等")
    print("5. 频率分析：统计每个字符出现次数")
    print("6. 查找替换：在字符串中查找和替换子串")
    print("7. 字符串反转：多种反转方法")
    print("8. 回文检测：判断字符串是否为回文")
    print("9. 格式验证：验证邮箱、密码等格式")
    print("10. 文本处理：词频统计、加密解密等")
    print("11. 模式匹配：简单的通配符匹配")
    print("12. 实际应用：文本分析、数据清理等")