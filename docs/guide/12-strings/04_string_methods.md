# 字符串常用方法

Python提供了丰富的字符串方法，这些方法可以帮助我们高效地处理和操作字符串数据。

## 学习目标

- 掌握字符串大小写转换方法
- 学会使用字符串检查方法
- 理解字符串分割和连接操作
- 掌握字符串清理和替换方法
- 学会字符串对齐和格式化
- 了解字符串查找和匹配方法

## 大小写转换方法

### 基本转换方法

```python
def demonstrate_case_methods():
    """演示大小写转换方法"""
    text = "Hello World Python Programming"
    print(f"原字符串: {text}")
    
    # 基本大小写转换
    print(f"upper(): {text.upper()}")
    print(f"lower(): {text.lower()}")
    print(f"capitalize(): {text.capitalize()}")
    print(f"title(): {text.title()}")
    
    # swapcase() - 大小写互换
    mixed_case = "PyThOn ProGramMinG"
    print(f"swapcase(): {mixed_case.swapcase()}")
```

**运行示例：**
```bash
python3 03_string_methods.py
```

### 特殊字符处理

```python
# casefold() - 更强的小写转换（支持特殊字符）
special_text = "Straße"  # 德语街道
print(f"特殊字符: {special_text}")
print(f"lower(): {special_text.lower()}")
print(f"casefold(): {special_text.casefold()}")
```

## 字符串检查方法

### 字符类型检查

```python
def demonstrate_check_methods():
    """演示字符串检查方法"""
    test_strings = [
        "hello",      # 纯字母
        "WORLD",      # 大写字母
        "123456",     # 纯数字
        "abc123",     # 字母数字混合
        "   ",        # 空格
        "Hello123",   # 混合内容
    ]
    
    for s in test_strings:
        print(f"'{s}':")
        print(f"  isalpha(): {s.isalpha()}")
        print(f"  isdigit(): {s.isdigit()}")
        print(f"  isalnum(): {s.isalnum()}")
        print(f"  isspace(): {s.isspace()}")
        print(f"  islower(): {s.islower()}")
        print(f"  isupper(): {s.isupper()}")
        print(f"  istitle(): {s.istitle()}")
```

### 特殊检查方法

```python
# 标识符检查
identifier = "valid_variable_name"
print(f"'{identifier}' isidentifier(): {identifier.isidentifier()}")

# 可打印字符检查
printable = "Hello\tWorld\n"
print(f"'{repr(printable)}' isprintable(): {printable.isprintable()}")

# 数字类型检查
decimal_str = "123"
print(f"'{decimal_str}' isdecimal(): {decimal_str.isdecimal()}")
print(f"'{decimal_str}' isnumeric(): {decimal_str.isnumeric()}")
```

## 分割和连接方法

### 字符串分割

```python
def demonstrate_split_join_methods():
    """演示字符串分割和连接方法"""
    # 基本分割
    sentence = "Python is a powerful programming language"
    words = sentence.split()
    print(f"split(): {words}")
    
    # 指定分隔符
    csv_data = "apple,banana,orange,grape"
    fruits = csv_data.split(',')
    print(f"split(','): {fruits}")
    
    # 限制分割次数
    text = "one-two-three-four-five"
    parts = text.split('-', 2)
    print(f"split('-', 2): {parts}")
    
    # 从右边开始分割
    path = "/home/user/documents/file.txt"
    right_parts = path.rsplit('/', 1)
    print(f"rsplit('/', 1): {right_parts}")
```

### 按行分割

```python
# splitlines() - 按行分割
multiline = "第一行\n第二行\r\n第三行\r第四行"
lines = multiline.splitlines()
print(f"多行文本分割: {lines}")
```

### 字符串连接

```python
# join() 方法
words_list = ['Python', 'is', 'awesome']
joined = ' '.join(words_list)
print(f"' '.join(): {joined}")

# 不同连接符
separators = ['-', ' | ', ', ', '']
for sep in separators:
    result = sep.join(words_list)
    print(f"'{sep}'.join(): {result}")
```

## 字符串清理方法

### 基本清理操作

```python
def demonstrate_strip_methods():
    """演示字符串清理方法"""
    # 基本的strip方法
    messy_string = "   Hello World   "
    print(f"原字符串: '{messy_string}'")
    print(f"strip(): '{messy_string.strip()}'")
    print(f"lstrip(): '{messy_string.lstrip()}'")
    print(f"rstrip(): '{messy_string.rstrip()}'")
```

### 自定义清理字符

```python
# 指定要删除的字符
custom_string = "...Hello World!!!"
print(f"原字符串: '{custom_string}'")
print(f"strip('.'): '{custom_string.strip('.')}'")
print(f"strip('.!'): '{custom_string.strip('.!')}'")
print(f"lstrip('.'): '{custom_string.lstrip('.')}'")
print(f"rstrip('!'): '{custom_string.rstrip('!')}'")

# 清理多种字符
noisy_data = "###   Python Programming   @@@"
clean_data = noisy_data.strip('#@ ')
print(f"清理后: '{clean_data}'")
```

### 实际应用示例

```python
# 清理用户输入
user_inputs = [
    "  john@email.com  ",
    "\t\npassword123\n\t",
    "   Python   "
]

for inp in user_inputs:
    cleaned = inp.strip()
    print(f"'{inp}' -> '{cleaned}'")
```

## 字符串替换方法

### 基本替换操作

```python
def demonstrate_replace_methods():
    """演示字符串替换方法"""
    # 基本replace方法
    text = "I love Java programming. Java is great!"
    replaced = text.replace("Java", "Python")
    print(f"replace('Java', 'Python'): {replaced}")
    
    # 限制替换次数
    limited_replace = text.replace("Java", "Python", 1)
    print(f"replace('Java', 'Python', 1): {limited_replace}")
```

### 实用替换技巧

```python
# 替换多个空格为单个空格
spaced_text = "Python    is    awesome"
normalized = ' '.join(spaced_text.split())
print(f"标准化空格: '{normalized}'")

# 删除字符（替换为空字符串）
phone = "(123) 456-7890"
clean_phone = phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
print(f"清理后: {clean_phone}")

# 链式替换
messy_text = "Hello...World!!!How...are...you???"
clean_text = messy_text.replace("...", " ").replace("!!!", "! ").replace("???", "?")
print(f"清理后: {clean_text}")
```

## 字符串对齐方法

### 基本对齐操作

```python
def demonstrate_alignment_methods():
    """演示字符串对齐方法"""
    text = "Python"
    width = 20
    
    # 基本对齐方法
    print(f"center({width}): '{text.center(width)}'")
    print(f"ljust({width}): '{text.ljust(width)}'")
    print(f"rjust({width}): '{text.rjust(width)}'")
    
    # 指定填充字符
    print(f"center({width}, '*'): '{text.center(width, '*')}'")
    print(f"ljust({width}, '-'): '{text.ljust(width, '-')}'")
    print(f"rjust({width}, '='): '{text.rjust(width, '=')}'")
```

### 数字填充

```python
# zfill() - 用0填充
numbers = ["42", "123", "7"]
for num in numbers:
    print(f"'{num}'.zfill(5): '{num.zfill(5)}'")
```

### 表格格式化应用

```python
# 实际应用：格式化表格
data = [
    ("Name", "Age", "City"),
    ("Alice", "25", "New York"),
    ("Bob", "30", "London"),
    ("Charlie", "35", "Tokyo")
]

for row in data:
    formatted_row = f"{row[0].ljust(10)} {row[1].center(5)} {row[2].rjust(10)}"
    print(formatted_row)
```

## 字符串查找方法

### 基本查找操作

```python
def demonstrate_find_methods():
    """演示字符串查找方法"""
    text = "Python programming is fun. Python is powerful."
    
    # find() 和 rfind()
    search_term = "Python"
    first_pos = text.find(search_term)
    last_pos = text.rfind(search_term)
    
    print(f"find('{search_term}'): {first_pos}")
    print(f"rfind('{search_term}'): {last_pos}")
    
    # 查找不存在的字符串
    not_found = text.find("Java")
    print(f"find('Java'): {not_found}")  # 返回-1
```

### index方法和异常处理

```python
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
```

### 计数和范围查找

```python
# count() - 计算出现次数
count = text.count("is")
print(f"count('is'): {count}")

# 在指定范围内查找
partial_find = text.find("is", 20)  # 从索引20开始查找
range_find = text.find("Python", 10, 30)  # 在索引10-30之间查找
```

## 前缀和后缀检查

### 文件类型检查

```python
def demonstrate_startswith_endswith():
    """演示字符串开始和结束检查方法"""
    filenames = [
        "document.pdf",
        "image.jpg",
        "script.py",
        "README.md",
        "config.json"
    ]
    
    for filename in filenames:
        print(f"{filename}:")
        print(f"  是Python文件: {filename.endswith('.py')}")
        print(f"  是图片文件: {filename.endswith(('.jpg', '.png', '.gif'))}")
        print(f"  是文档文件: {filename.endswith(('.pdf', '.doc', '.txt'))}")
```

### URL协议检查

```python
# startswith() 示例
urls = [
    "https://www.example.com",
    "http://test.com",
    "ftp://files.com",
    "www.noprotocol.com"
]

for url in urls:
    print(f"{url}:")
    print(f"  安全连接: {url.startswith('https://')}")
    print(f"  HTTP协议: {url.startswith(('http://', 'https://'))}")
    print(f"  FTP协议: {url.startswith('ftp://')}")
```

## 学习要点

### 方法分类

1. **大小写转换**：
   - `upper()`, `lower()` - 基本转换
   - `capitalize()`, `title()` - 首字母大写
   - `swapcase()` - 大小写互换
   - `casefold()` - 强化小写转换

2. **字符串检查**：
   - `isalpha()`, `isdigit()`, `isalnum()` - 字符类型检查
   - `islower()`, `isupper()`, `istitle()` - 大小写检查
   - `isspace()`, `isprintable()` - 特殊字符检查
   - `isidentifier()` - 标识符检查

3. **分割和连接**：
   - `split()`, `rsplit()` - 字符串分割
   - `splitlines()` - 按行分割
   - `join()` - 字符串连接

4. **清理和替换**：
   - `strip()`, `lstrip()`, `rstrip()` - 清理空白字符
   - `replace()` - 字符串替换

5. **对齐和格式化**：
   - `center()`, `ljust()`, `rjust()` - 字符串对齐
   - `zfill()` - 数字零填充

6. **查找和匹配**：
   - `find()`, `rfind()`, `index()`, `rindex()` - 位置查找
   - `count()` - 计数
   - `startswith()`, `endswith()` - 前后缀检查

### 使用技巧

1. **链式调用**：多个方法可以链式调用
2. **异常处理**：`index()`方法找不到时会抛出异常，`find()`返回-1
3. **多参数支持**：`startswith()`和`endswith()`支持元组参数
4. **范围查找**：大部分查找方法支持指定查找范围
5. **性能考虑**：对于大量数据处理，选择合适的方法很重要

## 实际应用场景

1. **数据清理**：去除多余空格、特殊字符
2. **格式验证**：检查邮箱、电话号码格式
3. **文本处理**：分割、连接、替换文本内容
4. **文件处理**：检查文件扩展名、路径处理
5. **用户输入处理**：标准化用户输入数据

## 注意事项

1. **字符串不可变**：所有方法都返回新的字符串对象
2. **区分大小写**：大部分方法都区分大小写
3. **Unicode支持**：Python 3对Unicode有良好支持
4. **性能考虑**：频繁的字符串操作可能影响性能
5. **方法选择**：根据具体需求选择合适的方法

## 下一步学习

掌握了字符串常用方法后，建议继续学习：
- 字符串格式化（04_string_formatting.py）
- 字符串操作和连接（05_string_operations.py）
- 字符串查找和替换（06_string_searching.py）

通过实际练习这些方法，你将能够高效地处理各种字符串操作任务。