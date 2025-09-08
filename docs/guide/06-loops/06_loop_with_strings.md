# 循环遍历字符串

字符串是Python中的基本数据类型，掌握字符串遍历技巧对于文本处理、数据清洗和字符串操作至关重要。本节将详细介绍各种字符串遍历方法和实际应用。

## 基本遍历方法

### 1. 直接遍历字符

最简单的字符串遍历：

```python
text = "Python"
for char in text:
    print(char)
```

### 2. 通过索引遍历

当需要索引信息时：

```python
text = "Python"
for i in range(len(text)):
    print(f"索引{i}: {text[i]}")
```

### 3. 使用enumerate()同时获取索引和字符

最优雅的方式：

```python
text = "Python"
for index, char in enumerate(text):
    print(f"索引{index}: {char}")
```

## 学习要点

### 1. 字符统计

统计字符出现频率：

```python
text = "hello world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
```

### 2. 字符串查找和替换

查找特定字符或模式：

```python
text = "Python Programming"
target = 'o'
positions = []
for i, char in enumerate(text):
    if char == target:
        positions.append(i)
print(f"字符'{target}'出现在位置：{positions}")
```

### 3. 字符串验证

验证字符串格式：

```python
def is_valid_email(email):
    has_at = False
    has_dot = False
    for char in email:
        if char == '@':
            has_at = True
        elif char == '.':
            has_dot = True
    return has_at and has_dot
```

## 完整代码示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - 循环遍历字符串

本文件详细介绍如何使用循环遍历和操作字符串。
字符串处理是编程中的重要技能，
掌握字符串遍历技巧对文本处理至关重要。

主要内容：
1. 基本字符串遍历方法
2. 字符统计和频率分析
3. 字符串查找和替换
4. 字符串验证和格式检查
5. 文本处理应用
6. 字符串模式匹配

作者：Python学习教程
日期：2024年
"""

import string
import random

# 1. 基本字符串遍历
print("=== 1. 基本字符串遍历 ===")
print()

print("1.1 直接遍历字符")
text = "Python编程"
print(f"字符串：{text}")
print("逐个字符输出：")
for char in text:
    print(f"  '{char}'")
print()

print("1.2 通过索引遍历")
print("通过索引访问字符：")
for i in range(len(text)):
    print(f"  索引{i}: '{text[i]}'")
print()

print("1.3 使用enumerate()")
print("同时获取索引和字符：")
for index, char in enumerate(text):
    print(f"  位置{index}: '{char}'")
print()

print("1.4 反向遍历")
print("反向遍历字符串：")
for i in range(len(text) - 1, -1, -1):
    print(f"  索引{i}: '{text[i]}'")
print()

# 2. 字符统计
print("=== 2. 字符统计 ===")
print()

print("2.1 基本字符计数")
sentence = "hello world python programming"
print(f"句子：{sentence}")

# 统计每个字符出现次数
char_count = {}
for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("字符频率统计：")
for char, count in sorted(char_count.items()):
    if char == ' ':
        print(f"  空格: {count}次")
    else:
        print(f"  '{char}': {count}次")
print()

print("2.2 字符类型统计")
text = "Hello123World!"
print(f"文本：{text}")

letters = 0
digits = 0
special = 0
uppercase = 0
lowercase = 0

for char in text:
    if char.isalpha():
        letters += 1
        if char.isupper():
            uppercase += 1
        else:
            lowercase += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1

print(f"字母数量：{letters}")
print(f"  大写字母：{uppercase}")
print(f"  小写字母：{lowercase}")
print(f"数字数量：{digits}")
print(f"特殊字符：{special}")
print()

print("2.3 元音辅音统计")
text = "Python Programming Language"
print(f"文本：{text}")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
vowel_chars = []
consonant_chars = []

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
            vowel_chars.append(char)
        else:
            consonant_count += 1
            consonant_chars.append(char)

print(f"元音字母：{vowel_count}个 - {vowel_chars}")
print(f"辅音字母：{consonant_count}个 - {consonant_chars}")
print()

# 3. 字符串查找
print("=== 3. 字符串查找 ===")
print()

print("3.1 查找单个字符")
text = "Programming with Python"
target_char = 'o'
print(f"在 '{text}' 中查找字符 '{target_char}'：")

positions = []
for i, char in enumerate(text):
    if char == target_char:
        positions.append(i)
        print(f"  找到 '{target_char}' 在位置 {i}")

if positions:
    print(f"字符 '{target_char}' 出现在位置：{positions}")
    print(f"总共出现 {len(positions)} 次")
else:
    print(f"没有找到字符 '{target_char}'")
print()

print("3.2 查找子字符串")
text = "Python is great, Python is powerful"
substring = "Python"
print(f"在 '{text}' 中查找子字符串 '{substring}'：")

occurrences = []
i = 0
while i <= len(text) - len(substring):
    match = True
    for j in range(len(substring)):
        if text[i + j] != substring[j]:
            match = False
            break
    
    if match:
        occurrences.append(i)
        print(f"  找到 '{substring}' 在位置 {i}")
        i += len(substring)  # 跳过已匹配的部分
    else:
        i += 1

print(f"子字符串 '{substring}' 出现 {len(occurrences)} 次")
print()

print("3.3 查找最长重复字符")
text = "aaabbccccdddd"
print(f"文本：{text}")

max_char = ''
max_count = 0
current_char = ''
current_count = 0

for char in text:
    if char == current_char:
        current_count += 1
    else:
        if current_count > max_count:
            max_count = current_count
            max_char = current_char
        current_char = char
        current_count = 1

# 检查最后一组
if current_count > max_count:
    max_count = current_count
    max_char = current_char

print(f"最长重复字符：'{max_char}'，连续出现 {max_count} 次")
print()

# 4. 字符串处理
print("=== 4. 字符串处理 ===")
print()

print("4.1 字符串反转")
original = "Hello World"
print(f"原字符串：{original}")

# 方法1：使用循环
reversed_str = ""
for char in original:
    reversed_str = char + reversed_str
print(f"反转结果1：{reversed_str}")

# 方法2：使用索引
reversed_str2 = ""
for i in range(len(original) - 1, -1, -1):
    reversed_str2 += original[i]
print(f"反转结果2：{reversed_str2}")
print()

print("4.2 回文检测")
test_strings = ["level", "hello", "madam", "python", "racecar"]

for test_str in test_strings:
    print(f"检测 '{test_str}'：")
    is_palindrome = True
    
    # 比较字符串的前半部分和后半部分
    for i in range(len(test_str) // 2):
        if test_str[i] != test_str[len(test_str) - 1 - i]:
            is_palindrome = False
            break
    
    print(f"  {'是' if is_palindrome else '不是'}回文")
print()

print("4.3 单词处理")
sentence = "Python is a powerful programming language"
print(f"句子：{sentence}")

# 手动分割单词
words = []
current_word = ""

for char in sentence:
    if char == ' ':
        if current_word:
            words.append(current_word)
            current_word = ""
    else:
        current_word += char

# 添加最后一个单词
if current_word:
    words.append(current_word)

print(f"分割的单词：{words}")
print(f"单词数量：{len(words)}")

# 统计单词长度
print("单词长度统计：")
for word in words:
    print(f"  '{word}': {len(word)}个字符")
print()

# 5. 字符串验证
print("=== 5. 字符串验证 ===")
print()

print("5.1 邮箱格式验证")
emails = ["user@example.com", "invalid-email", "test@domain", "name@site.org"]

def validate_email(email):
    has_at = False
    has_dot_after_at = False
    at_position = -1
    
    for i, char in enumerate(email):
        if char == '@':
            if has_at:  # 多个@符号
                return False
            has_at = True
            at_position = i
        elif char == '.' and has_at and i > at_position:
            has_dot_after_at = True
    
    return has_at and has_dot_after_at and at_position > 0 and at_position < len(email) - 1

for email in emails:
    is_valid = validate_email(email)
    print(f"  {email}: {'有效' if is_valid else '无效'}")
print()

print("5.2 密码强度检测")
passwords = ["123456", "Password123", "weak", "Strong@Pass123", "NoDigits!"]

def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()_+-=[]{}|;:,.<>?"):
            has_special = True
    
    strength = 0
    if has_upper: strength += 1
    if has_lower: strength += 1
    if has_digit: strength += 1
    if has_special: strength += 1
    if len(password) >= 8: strength += 1
    
    return strength, has_upper, has_lower, has_digit, has_special

for password in passwords:
    strength, upper, lower, digit, special = check_password_strength(password)
    print(f"  密码 '{password}':")
    print(f"    长度: {len(password)} {'✓' if len(password) >= 8 else '✗'}")
    print(f"    大写字母: {'✓' if upper else '✗'}")
    print(f"    小写字母: {'✓' if lower else '✗'}")
    print(f"    数字: {'✓' if digit else '✗'}")
    print(f"    特殊字符: {'✓' if special else '✗'}")
    
    if strength >= 4:
        level = "强"
    elif strength >= 3:
        level = "中等"
    else:
        level = "弱"
    print(f"    强度等级: {level} ({strength}/5)")
    print()

# 6. 文本处理应用
print("=== 6. 文本处理应用 ===")
print()

print("6.1 词频统计")
text = "Python is great Python is powerful Python is easy to learn"
print(f"文本：{text}")

# 转换为小写并分割单词
words = []
current_word = ""

for char in text.lower():
    if char.isalpha():
        current_word += char
    else:
        if current_word:
            words.append(current_word)
            current_word = ""

if current_word:
    words.append(current_word)

# 统计词频
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("词频统计：")
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{word}': {count}次")
print()

print("6.2 凯撒密码加密")
plaintext = "Hello World"
shift = 3
print(f"原文：{plaintext}")
print(f"位移：{shift}")

encrypted = ""
for char in plaintext:
    if char.isalpha():
        # 确定是大写还是小写
        if char.isupper():
            # 大写字母处理
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # 小写字母处理
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        encrypted += encrypted_char
    else:
        # 非字母字符保持不变
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

# 7. 字符串模式匹配
print("=== 7. 字符串模式匹配 ===")
print()

print("7.1 简单模式匹配")
text = "The quick brown fox jumps over the lazy dog"
pattern = "fox"
print(f"文本：{text}")
print(f"模式：{pattern}")

# 查找所有匹配位置
matches = []
for i in range(len(text) - len(pattern) + 1):
    match = True
    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            match = False
            break
    if match:
        matches.append(i)

if matches:
    print(f"找到匹配，位置：{matches}")
else:
    print("没有找到匹配")
print()

print("7.2 通配符匹配（简化版）")
text = "hello"
pattern = "h*o"  # *表示任意字符
print(f"文本：{text}")
print(f"模式：{pattern}（*表示任意字符）")

def simple_wildcard_match(text, pattern):
    if len(pattern) == 0:
        return len(text) == 0
    
    if len(text) == 0:
        return all(c == '*' for c in pattern)
    
    if pattern[0] == '*':
        # *可以匹配0个或多个字符
        return (simple_wildcard_match(text[1:], pattern) or 
                simple_wildcard_match(text, pattern[1:]))
    else:
        # 普通字符必须完全匹配
        return (text[0] == pattern[0] and 
                simple_wildcard_match(text[1:], pattern[1:]))

is_match = simple_wildcard_match(text, pattern)
print(f"匹配结果：{'匹配' if is_match else '不匹配'}")
print()

# 8. 综合练习
print("=== 8. 综合练习 ===")
print()

print("8.1 文本清理")
raw_text = "  Hello,   World!  Python   Programming.  "
print(f"原始文本：'{raw_text}'")

# 去除多余空格
cleaned = ""
prev_char = ''
for char in raw_text:
    if char == ' ':
        if prev_char != ' ':
            cleaned += char
    else:
        cleaned += char
    prev_char = char

# 去除首尾空格
cleaned = cleaned.strip()
print(f"清理后：'{cleaned}'")
print()

print("8.2 字符串压缩")
text = "aaabbccccdddd"
print(f"原字符串：{text}")

compressed = ""
current_char = ''
count = 0

for char in text:
    if char == current_char:
        count += 1
    else:
        if current_char:
            compressed += current_char + str(count)
        current_char = char
        count = 1

# 处理最后一组
if current_char:
    compressed += current_char + str(count)

print(f"压缩后：{compressed}")
print()

print("8.3 数字提取")
text = "我有3个苹果，5个香蕉，和12个橙子"
print(f"文本：{text}")

numbers = []
current_number = ""

for char in text:
    if char.isdigit():
        current_number += char
    else:
        if current_number:
            numbers.append(int(current_number))
            current_number = ""

# 处理最后一个数字
if current_number:
    numbers.append(int(current_number))

print(f"提取的数字：{numbers}")
print(f"数字总和：{sum(numbers)}")
print()

if __name__ == "__main__":
    print("=== 循环遍历字符串学习总结 ===")
    print("通过本节学习，你应该掌握了：")
    print("1. 字符串的基本遍历方法")
    print("2. 字符统计和频率分析技巧")
    print("3. 字符串查找和模式匹配")
    print("4. 字符串验证和格式检查")
    print("5. 文本处理和数据清洗")
    print("6. 字符串加密和解密基础")
    print("7. 实际文本处理应用")
    print("\n继续练习这些概念，你将能够熟练运用字符串处理解决各种文本相关问题！")
```

## 注意事项

1. **字符编码**：处理中文等非ASCII字符时注意编码问题
2. **性能考虑**：对于大文本，考虑使用更高效的算法
3. **内存使用**：避免创建过多临时字符串
4. **边界条件**：处理空字符串和特殊字符

## 练习建议

1. 实现各种字符串统计功能
2. 编写字符串验证函数
3. 练习文本处理和清洗
4. 实现简单的加密解密算法
5. 处理实际的文本数据分析任务

通过大量练习，你将能够熟练掌握字符串遍历和处理技巧，这是文本处理和数据分析的重要基础。