# 字符串查找和替换

本章节介绍Python中字符串查找和替换的各种方法，包括基本查找、前缀后缀检查、字符串替换、正则表达式以及性能优化技巧。

## 学习目标

- 掌握基本的字符串查找方法（find、index、rfind、rindex）
- 学会使用前缀和后缀检查方法
- 理解字符串替换和字符映射
- 掌握正则表达式在字符串处理中的应用
- 了解高级查找技巧和性能优化

## 1. 基本字符串查找

### find() 和 rfind() 方法

```python
text = "Python is a powerful programming language. Python is easy to learn."

# find() - 返回第一次出现的位置，未找到返回-1
pos1 = text.find("Python")  # 0
pos2 = text.find("Java")    # -1
pos3 = text.find("is")      # 7

# 指定搜索范围
pos4 = text.find("Python", 10)     # 从位置10开始搜索
pos5 = text.find("is", 10, 30)     # 在位置10-30之间搜索

# rfind() - 返回最后一次出现的位置
rpos1 = text.rfind("Python")  # 48
rpos2 = text.rfind("is")      # 55
```

### index() 和 rindex() 方法

```python
# index() - 类似find()，但未找到时抛出异常
try:
    idx1 = text.index("Python")  # 0
    idx2 = text.index("Java")    # 抛出ValueError异常
except ValueError as e:
    print(f"未找到: {e}")

# rindex() - 类似rfind()，但未找到时抛出异常
try:
    ridx1 = text.rindex("Python")  # 48
    ridx2 = text.rindex("xyz")     # 抛出ValueError异常
except ValueError as e:
    print(f"未找到: {e}")
```

### 查找所有出现位置

```python
def find_all_positions(text, substring):
    """查找子字符串的所有出现位置"""
    positions = []
    start = 0
    while True:
        pos = text.find(substring, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

text = "Python is a powerful programming language. Python is easy to learn."
all_positions = find_all_positions(text, "is")
print(f"'is' 的所有位置: {all_positions}")  # [7, 55]
```

## 2. 前缀和后缀检查

### startswith() 和 endswith() 方法

```python
filenames = [
    "document.txt",
    "image.jpg",
    "script.py",
    "data.csv",
    "backup_file.bak",
    "temp_data.tmp"
]

# 检查单个前缀
for filename in filenames:
    if filename.startswith("temp"):
        print(f"临时文件: {filename}")
    elif filename.startswith("backup"):
        print(f"备份文件: {filename}")

# 检查单个后缀
for filename in filenames:
    if filename.endswith(".txt"):
        print(f"文本文件: {filename}")
    elif filename.endswith(".py"):
        print(f"Python文件: {filename}")
```

### 多个前缀/后缀检查

```python
# 检查多个前缀
prefixes = ("temp", "backup", "old")
special_files = [f for f in filenames if f.startswith(prefixes)]

# 检查多个后缀
code_extensions = (".py", ".js", ".java", ".cpp")
code_files = [f for f in filenames if f.endswith(code_extensions)]

# 指定搜索范围
sentence = "The quick brown fox jumps over the lazy dog"
result1 = sentence.startswith("quick", 4)      # 从位置4开始
result2 = sentence.startswith("brown", 10, 15) # 在位置10-15之间
```

## 3. 字符串替换

### replace() 方法

```python
text = "Hello World! Hello Python! Hello Programming!"

# 替换所有出现
result1 = text.replace("Hello", "Hi")
print(result1)  # "Hi World! Hi Python! Hi Programming!"

# 限制替换次数
result2 = text.replace("Hello", "Hi", 2)
print(result2)  # "Hi World! Hi Python! Hello Programming!"

# 删除字符（替换为空字符串）
result3 = text.replace(" ", "")
print(result3)  # "HelloWorld!HelloPython!HelloProgramming!"
```

### 链式替换和批量替换

```python
# 链式替换
messy_text = "  Hello,,,World!!!  "
cleaned = messy_text.strip().replace(",,,", ", ").replace("!!!", "!")

# 批量替换
def multiple_replace(text, replacements):
    """使用字典进行批量替换"""
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
```

### 大小写不敏感替换

```python
import re

def case_insensitive_replace(text, old, new):
    """大小写不敏感替换"""
    return re.sub(re.escape(old), new, text, flags=re.IGNORECASE)

mixed_case = "Python python PYTHON PyThOn"
result = case_insensitive_replace(mixed_case, "python", "Java")
print(result)  # "Java Java Java Java"
```

## 4. translate() 方法进行字符映射

### 基本字符翻译

```python
import string

# 使用str.maketrans()创建翻译表
translation_table = str.maketrans("aeiou", "12345")
text = "Hello World"
result = text.translate(translation_table)
print(result)  # "H2ll4 W4rld"

# 删除字符
punctuation_table = str.maketrans("", "", string.punctuation)
sentence = "Hello, World! How are you?"
no_punct = sentence.translate(punctuation_table)
print(no_punct)  # "Hello World How are you"
```

### ROT13编码示例

```python
# 创建ROT13编码表
rot13_table = str.maketrans(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
)

message = "Hello Python Programming"
encoded = message.translate(rot13_table)
decoded = encoded.translate(rot13_table)  # ROT13是自逆的

print(f"原文: {message}")
print(f"编码: {encoded}")
print(f"解码: {decoded}")
```

## 5. 正则表达式查找和替换

### 基本正则查找

```python
import re

text = "Contact us at: john@example.com, alice@test.org, or call 123-456-7890"

# 查找邮箱地址
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
print(f"邮箱: {emails}")  # ['john@example.com', 'alice@test.org']

# 查找电话号码
phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
phones = re.findall(phone_pattern, text)
print(f"电话: {phones}")  # ['123-456-7890']
```

### 使用search()和finditer()

```python
# search() - 查找第一个匹配
email_match = re.search(email_pattern, text)
if email_match:
    print(f"第一个邮箱: {email_match.group()}")
    print(f"位置: {email_match.start()}-{email_match.end()}")

# finditer() - 获取详细匹配信息
for match in re.finditer(email_pattern, text):
    email = match.group()
    start, end = match.span()
    print(f"邮箱: '{email}', 位置: {start}-{end}")
```

### 正则表达式替换

```python
# 简单替换
hidden_emails = re.sub(email_pattern, "[EMAIL]", text)
hidden_phones = re.sub(phone_pattern, "[PHONE]", text)

# 使用捕获组进行复杂替换
names_text = "John Smith, Alice Johnson, Bob Wilson"
name_pattern = r'(\w+)\s+(\w+)'
swapped_names = re.sub(name_pattern, r'\2, \1', names_text)
print(swapped_names)  # "Smith, John, Johnson, Alice, Wilson, Bob"

# 使用函数进行替换
def format_phone(match):
    phone = match.group()
    parts = phone.split('-')
    return f"({parts[0]}) {parts[1]}-{parts[2]}"

formatted_text = re.sub(phone_pattern, format_phone, text)
```

## 6. 高级查找技巧

### 模糊匹配

```python
import difflib

def fuzzy_find(text, pattern, threshold=0.7):
    """简单的模糊匹配实现"""
    words = text.split()
    matches = []
    
    for word in words:
        similarity = difflib.SequenceMatcher(None, pattern.lower(), word.lower()).ratio()
        if similarity >= threshold:
            matches.append((word, similarity))
    
    return sorted(matches, key=lambda x: x[1], reverse=True)

text = "Python programming is powerful and pythonic"
pattern = "python"
fuzzy_matches = fuzzy_find(text, pattern)
print(f"模糊匹配结果: {fuzzy_matches}")
```

### 上下文查找

```python
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
```

### 多模式查找

```python
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
```

## 7. 性能优化技巧

### 方法选择建议

```python
# 性能比较示例
import time
import re

large_text = "Python programming " * 10000

# 简单查找：使用内置方法
start = time.time()
result1 = large_text.find("programming")
time1 = time.time() - start

# 复杂模式：使用正则表达式
start = time.time()
result2 = re.search(r"programming", large_text)
time2 = time.time() - start

# 包含检查：使用in操作符
start = time.time()
result3 = "programming" in large_text
time3 = time.time() - start

print(f"find(): {time1:.6f}秒")
print(f"re.search(): {time2:.6f}秒")
print(f"in操作符: {time3:.6f}秒")
```

### 预编译正则表达式

```python
# 预编译正则表达式提高性能
pattern = re.compile(r"\b\w+ing\b")

# 使用预编译的模式
results = pattern.findall(large_text)

# 与非预编译比较
results2 = re.findall(r"\b\w+ing\b", large_text)
```

## 完整示例代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import string
import time
import difflib

def demonstrate_string_searching():
    """演示字符串查找和替换的综合应用"""
    
    # 示例文本
    text = "Contact us at: john@example.com, alice@test.org, or call 123-456-7890"
    
    print("=== 字符串查找和替换演示 ===")
    print(f"原文本: {text}")
    
    # 1. 基本查找
    print("\n1. 基本查找:")
    pos = text.find("Contact")
    print(f"'Contact' 位置: {pos}")
    
    # 2. 正则表达式查找
    print("\n2. 正则表达式查找:")
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    print(f"找到的邮箱: {emails}")
    
    # 3. 替换操作
    print("\n3. 替换操作:")
    hidden_text = re.sub(email_pattern, "[EMAIL]", text)
    print(f"隐藏邮箱后: {hidden_text}")
    
    # 4. 字符映射
    print("\n4. 字符映射:")
    vowel_table = str.maketrans("aeiou", "12345")
    mapped_text = "Hello World".translate(vowel_table)
    print(f"元音映射: {mapped_text}")
    
    return text, emails

if __name__ == "__main__":
    demonstrate_string_searching()
```

## 运行示例

在终端中运行以下命令来测试字符串查找和替换：

```bash
python3 06_string_searching.py
```

## 学习要点

### 核心概念
1. **查找方法选择**：简单查找用find()，复杂模式用正则表达式
2. **异常处理**：find()返回-1，index()抛出异常
3. **性能考虑**：内置方法通常比正则表达式快
4. **预编译优化**：频繁使用的正则表达式应预编译

### 实际应用场景
1. **文本处理**：日志分析、数据清洗
2. **数据验证**：邮箱、电话号码格式检查
3. **内容过滤**：敏感词替换、信息脱敏
4. **代码分析**：语法高亮、关键词提取

### 注意事项
1. **大小写敏感**：默认情况下查找和替换都是大小写敏感的
2. **特殊字符转义**：在正则表达式中需要转义特殊字符
3. **性能权衡**：复杂查找可能影响性能，需要合理选择方法
4. **内存使用**：处理大文本时注意内存消耗

## 下一步学习

完成本章节后，建议继续学习：
- 字符串验证方法
- 字符串编码和解码
- 正则表达式进阶
- 文本处理最佳实践