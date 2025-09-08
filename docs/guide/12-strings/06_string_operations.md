# 字符串操作和连接

## 学习目标

通过本节学习，你将掌握：
- 各种字符串连接方法及其适用场景
- 字符串重复、比较和包含检查
- 字符串长度计数和转换操作
- 字符串操作的性能比较和最佳实践

## 字符串连接方法

### 基本连接方式

```python
# 1. 使用 + 操作符
first = "Hello"
second = "World"
result = first + " " + second
print(result)  # Hello World

# 2. 使用 += 操作符
message = "Python"
message += " is"
message += " awesome!"
print(message)  # Python is awesome!

# 3. 使用 join() 方法
words = ["Python", "is", "a", "great", "language"]
result = " ".join(words)
print(result)  # Python is a great language
```

### 格式化连接

```python
# 4. 使用 format() 方法
template = "{} {} {}"
result = template.format("Learning", "Python", "programming")
print(result)

# 5. 使用 f-string（推荐）
name = "Alice"
age = 25
result = f"My name is {name} and I am {age} years old"
print(result)

# 6. 使用 % 格式化
result = "Hello %s, you have %d messages" % ("Bob", 5)
print(result)
```

### 多行字符串连接

```python
# 自动连接（括号内）
long_text = (
    "This is a very long string that "
    "spans multiple lines and is "
    "concatenated automatically by Python"
)
print(long_text)

# 使用 StringIO（适合大量操作）
from io import StringIO

buffer = StringIO()
buffer.write("Hello")
buffer.write(" ")
buffer.write("from")
buffer.write(" ")
buffer.write("StringIO")
result = buffer.getvalue()
buffer.close()
print(result)
```

## 字符串重复

### 基本重复操作

```python
# 重复字符
char = "*"
line = char * 50
print(line)  # **************************************************

# 重复单词
word = "Python "
repeated = word * 5
print(repeated)  # Python Python Python Python Python 

# 创建分隔线
separator = "-" * 30
print(separator)  # ------------------------------
```

### 实用重复示例

```python
# 创建缩进
indent_level = 3
indent = "    " * indent_level  # 12个空格
code_line = indent + "print('Hello, World!')"
print(f"'{code_line}'")

# 创建进度条
progress = 75  # 75%
bar_length = 20
filled_length = int(bar_length * progress / 100)
bar = "█" * filled_length + "-" * (bar_length - filled_length)
print(f"进度条: [{bar}] {progress}%")

# 创建表格边框
border = "+" + "-" * 10 + "+" + "-" * 15 + "+" + "-" * 8 + "+"
print(border)
```

### 特殊情况

```python
# 零次重复
empty = "Hello" * 0
print(f"'{empty}'")  # ''

# 负数重复（结果为空字符串）
negative = "Hello" * -1
print(f"'{negative}'")  # ''
```

## 字符串比较

### 基本比较操作

```python
# 相等比较
str1 = "Python"
str2 = "Python"
str3 = "python"

print(f"'{str1}' == '{str2}': {str1 == str2}")  # True
print(f"'{str1}' == '{str3}': {str1 == str3}")  # False
print(f"'{str1}' != '{str3}': {str1 != str3}")  # True

# 大小写不敏感比较
print(f"忽略大小写: {str1.lower() == str3.lower()}")  # True
```

### 字典序比较

```python
# 字典序比较
words = ["apple", "banana", "cherry", "date"]
for i in range(len(words) - 1):
    word1, word2 = words[i], words[i + 1]
    print(f"'{word1}' < '{word2}': {word1 < word2}")

# 数字字符串比较（注意陷阱）
num_str1 = "10"
num_str2 = "2"
print(f"字符串比较: '{num_str1}' < '{num_str2}': {num_str1 < num_str2}")  # True
print(f"数值比较: {int(num_str1)} < {int(num_str2)}: {int(num_str1) < int(num_str2)}")  # False
```

### 特殊比较

```python
# 长度比较
short = "Hi"
long_str = "Hello"
print(f"'{short}' < '{long_str}': {short < long_str}")  # True
print(f"长度比较: {len(short)} < {len(long_str)}: {len(short) < len(long_str)}")  # True

# 空字符串比较
empty = ""
non_empty = "a"
print(f"'{empty}' < '{non_empty}': {empty < non_empty}")  # True
print(f"'{empty}' == '': {empty == ''}")  # True
```

## 字符串包含检查

### 基本包含操作

```python
text = "Python is a powerful programming language"

# 基本包含检查
print(f"'Python' in text: {'Python' in text}")  # True
print(f"'Java' in text: {'Java' in text}")      # False
print(f"'python' in text: {'python' in text}")  # False

# 不包含检查
print(f"'Java' not in text: {'Java' not in text}")    # True
print(f"'Python' not in text: {'Python' not in text}") # False
```

### 大小写不敏感检查

```python
# 大小写不敏感检查
print(f"'python' in text.lower(): {'python' in text.lower()}")  # True
print(f"'PYTHON' in text.upper(): {'PYTHON' in text.upper()}")  # True
```

### 多条件检查

```python
# 检查多个关键词
keywords = ["Python", "programming"]
all_present = all(keyword in text for keyword in keywords)
any_present = any(keyword in text for keyword in keywords)

print(f"所有关键词都存在: {all_present}")  # True
print(f"任一关键词存在: {any_present}")    # True

# 字符检查
chars = ['P', 'y', 'z', '!', ' ']
for char in chars:
    result = char in text
    print(f"'{char}' in text: {result}")
```

### 正则表达式匹配

```python
import re

# 复杂模式匹配
pattern = r'\b[Pp]ython\b'  # 匹配单词边界的Python
match = re.search(pattern, text)
print(f"模式匹配: {match is not None}")
if match:
    print(f"匹配位置: {match.start()}-{match.end()}")
    print(f"匹配内容: '{match.group()}'")
```

## 字符串长度和计数

### 基本长度统计

```python
# 各种字符串的长度
texts = [
    "Hello",
    "Python Programming",
    "",
    "   spaces   ",
    "Hello\nWorld",
    "中文字符串",
    "Mixed中英文String"
]

for text in texts:
    print(f"'{text}' -> 长度: {len(text)}")
```

### 字符和子字符串计数

```python
sample_text = "Hello, World! Welcome to Python programming."

# 统计特定字符
char_counts = {
    'l': sample_text.count('l'),
    'o': sample_text.count('o'),
    'e': sample_text.count('e'),
    ' ': sample_text.count(' '),
    ',': sample_text.count(','),
    '.': sample_text.count('.')
}

for char, count in char_counts.items():
    print(f"'{char}': {count}次")

# 统计子字符串
substring_counts = {
    'o': sample_text.count('o'),
    'lo': sample_text.count('lo'),
    'Python': sample_text.count('Python'),
    'python': sample_text.count('python')  # 大小写敏感
}

for substring, count in substring_counts.items():
    print(f"'{substring}': {count}次")
```

### 高级统计

```python
# 单词统计
words = sample_text.split()
print(f"单词数量: {len(words)}")
print(f"单词列表: {words}")

# 字符类型统计
mixed_text = "Hello123!@# World456"
stats = {
    '字母': sum(1 for c in mixed_text if c.isalpha()),
    '数字': sum(1 for c in mixed_text if c.isdigit()),
    '空格': sum(1 for c in mixed_text if c.isspace()),
    '标点': sum(1 for c in mixed_text if not c.isalnum() and not c.isspace()),
    '字母数字': sum(1 for c in mixed_text if c.isalnum())
}

for char_type, count in stats.items():
    print(f"{char_type}: {count}个")
```

## 字符串转换操作

### 大小写转换

```python
original = "  Hello, Python World!  "

# 各种大小写转换
print(f"upper(): '{original.upper()}'")
print(f"lower(): '{original.lower()}'")
print(f"title(): '{original.title()}'")
print(f"capitalize(): '{original.capitalize()}'")
print(f"swapcase(): '{original.swapcase()}'")
```

### 空白字符处理

```python
# 去除空白字符
print(f"strip(): '{original.strip()}'")
print(f"lstrip(): '{original.lstrip()}'")
print(f"rstrip(): '{original.rstrip()}'")
```

### 字符替换

```python
text = "Hello, World!"

# 字符和子字符串替换
print(f"replace('o', '0'): '{text.replace('o', '0')}'")
print(f"replace('l', 'L', 1): '{text.replace('l', 'L', 1)}'")
print(f"replace('Hello', 'Hi'): '{text.replace('Hello', 'Hi')}'")
```

### 字符串分割和连接

```python
# 基本分割
sentence = "apple,banana,cherry,date"
print(f"split(','): {sentence.split(',')}")
print(f"split(',', 2): {sentence.split(',', 2)}")

# 复杂分割
import re
complex_text = "apple;banana,cherry:date"
parts = re.split('[;,:]+', complex_text)
print(f"复杂分割: {parts}")

# 字符串连接
fruits = ['apple', 'banana', 'cherry']
print(f"join(', '): '{', '.join(fruits)}'")
print(f"join(' | '): '{' | '.join(fruits)}'")
```

### 字符串对齐和填充

```python
word = "Python"
width = 20

# 对齐方式
print(f"ljust({width}): '{word.ljust(width)}'")
print(f"rjust({width}): '{word.rjust(width)}'")
print(f"center({width}): '{word.center(width)}'")
print(f"center({width}, '*'): '{word.center(width, '*')}'")

# 数字填充
number = "42"
print(f"zfill(5): '{number.zfill(5)}'")
print(f"rjust(5, '0'): '{number.rjust(5, '0')}'")
```

## 性能比较

### 字符串连接性能

```python
import time

def time_operation(operation, description):
    start_time = time.time()
    result = operation()
    end_time = time.time()
    print(f"{description}: {end_time - start_time:.6f}秒")
    return result

n = 1000
words = ["word"] * n

# 不同连接方法的性能比较
def concat_with_plus():
    result = ""
    for word in words:
        result = result + word  # 性能较差
    return result

def concat_with_plus_equal():
    result = ""
    for word in words:
        result += word  # 稍好一些
    return result

def concat_with_join():
    return "".join(words)  # 性能最好

# 性能测试
result1 = time_operation(concat_with_plus, "+ 操作符")
result2 = time_operation(concat_with_plus_equal, "+= 操作符")
result3 = time_operation(concat_with_join, "join 方法")
```

## 最佳实践

### 1. 理解字符串不可变性

```python
# 字符串是不可变的
original = "Hello"
print(f"原始: id={id(original)}, value='{original}'")

# 这会创建新字符串
modified = original + " World"
print(f"修改后: id={id(modified)}, value='{modified}'")
print(f"原始未变: '{original}'")
```

### 2. 选择合适的连接方法

```python
# 少量连接 - 使用 +
name = "Alice"
greeting = "Hello " + name + "!"

# 多个字符串 - 使用 join
parts = ["Python", "is", "awesome"]
sentence = " ".join(parts)

# 格式化 - 使用 f-string
age = 25
message = f"{name} is {age} years old"
```

### 3. 避免常见错误

```python
# ❌ 错误做法（性能差）
# result = ""
# for i in range(1000):
#     result = result + str(i)  # 每次都创建新字符串

# ✅ 正确做法（性能好）
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)
```

### 4. 字符串比较最佳实践

```python
user_input = "PYTHON"

# 大小写不敏感比较
if user_input.lower() == "python":
    print("匹配成功")

# 检查空字符串
text = "   "
if not text.strip():  # 比 text.strip() == "" 更pythonic
    print("空字符串")
```

## 完整示例代码

```python
def string_operations_demo():
    """字符串操作综合演示"""
    
    print("=== 字符串操作演示 ===")
    
    # 1. 连接方法比较
    words = ["Python", "字符串", "操作"]
    
    # 不同连接方式
    result1 = " ".join(words)
    result2 = f"{words[0]} {words[1]} {words[2]}"
    result3 = words[0] + " " + words[1] + " " + words[2]
    
    print(f"join方法: {result1}")
    print(f"f-string: {result2}")
    print(f"+ 操作符: {result3}")
    
    # 2. 字符串分析
    text = "Hello, Python Programming World!"
    
    print(f"\n文本分析: '{text}'")
    print(f"长度: {len(text)}")
    print(f"单词数: {len(text.split())}")
    print(f"'o'出现次数: {text.count('o')}")
    print(f"包含'Python': {'Python' in text}")
    
    # 3. 字符串转换
    print(f"\n字符串转换:")
    print(f"大写: {text.upper()}")
    print(f"标题: {text.title()}")
    print(f"替换: {text.replace('Python', 'Java')}")
    
    # 4. 格式化输出
    data = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
    
    print(f"\n成绩表:")
    print(f"{'姓名':<10} {'分数':>6}")
    print("-" * 18)
    for name, score in data:
        print(f"{name:<10} {score:>6}")

if __name__ == "__main__":
    string_operations_demo()
```

## 运行示例

在终端中运行：

```bash
python3 05_string_operations.py
```

## 学习要点

### 1. 连接方法选择
- **少量字符串**：使用 `+` 或 `+=`
- **多个字符串**：使用 `join()` 方法
- **格式化**：优先使用 f-string
- **大量连接**：避免在循环中使用 `+`

### 2. 性能考虑
- `join()` 方法性能最好
- f-string 简洁高效
- 避免重复字符串创建
- 使用列表收集再连接

### 3. 比较操作
- 字符串比较是字典序
- 注意大小写敏感性
- 数字字符串需要转换后比较
- 使用 `lower()` 进行大小写不敏感比较

### 4. 包含检查
- 使用 `in` 和 `not in` 操作符
- 结合 `lower()` 进行大小写不敏感检查
- 使用 `all()` 和 `any()` 进行多条件检查

## 实际应用场景

1. **文本处理**：日志分析、数据清洗
2. **用户输入验证**：检查关键词、格式验证
3. **报告生成**：格式化输出、表格创建
4. **文件操作**：路径拼接、文件名处理
5. **数据转换**：格式转换、编码处理

## 注意事项

1. **不可变性**：字符串操作会创建新对象
2. **性能影响**：大量连接时选择合适方法
3. **编码问题**：处理中文等Unicode字符
4. **内存使用**：避免创建过多临时字符串
5. **可读性**：选择最清晰的表达方式

## 下一步学习

学习完字符串操作后，建议继续学习：
- 字符串查找和替换
- 字符串验证方法
- 正则表达式基础
- 字符串编码和解码