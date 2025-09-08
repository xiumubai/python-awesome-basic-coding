# 字符串索引和切片

字符串索引和切片是Python中处理字符串的基础技能，掌握这些操作对于字符串处理至关重要。

## 学习目标

- 理解字符串索引的概念和规则
- 掌握正向索引和反向索引的使用
- 学会字符串切片的基本语法
- 掌握高级切片操作和步长使用
- 了解索引和切片的实际应用场景

## 字符串索引基础

### 索引概念

```python
def demonstrate_string_indexing():
    """演示字符串索引的基本概念"""
    print("=== 字符串索引 ===")
    
    sample_string = "Python"
    print(f"字符串: {sample_string}")
    print(f"长度: {len(sample_string)}")
    
    # 正向索引（从0开始）
    print("\n正向索引:")
    for i in range(len(sample_string)):
        print(f"索引 {i}: '{sample_string[i]}'")
    
    # 反向索引（从-1开始）
    print("\n反向索引:")
    for i in range(-1, -len(sample_string)-1, -1):
        print(f"索引 {i}: '{sample_string[i]}'")
```

**运行示例：**
```bash
python3 02_string_indexing.py
```

### 索引错误处理

```python
def demonstrate_index_errors():
    """演示索引错误和边界情况"""
    text = "Hello"
    print(f"字符串: {text}")
    print(f"有效索引范围: 0 到 {len(text)-1} 或 -{len(text)} 到 -1")
    
    # 无效索引会引发错误
    invalid_indices = [5, -6, 10]
    
    for index in invalid_indices:
        try:
            result = text[index]
            print(f"text[{index}] = '{result}'")
        except IndexError as e:
            print(f"text[{index}] -> 错误: {e}")
```

## 字符串切片操作

### 基本切片语法

```python
def demonstrate_basic_slicing():
    """演示基本的字符串切片"""
    text = "Programming"
    print(f"字符串: {text}")
    
    # 基本切片语法: string[start:end]
    print("\n基本切片 [start:end]:")
    print(f"text[0:4] = '{text[0:4]}'  # 从索引0到3")
    print(f"text[2:7] = '{text[2:7]}'  # 从索引2到6")
    
    # 省略开始或结束索引
    print("\n省略索引:")
    print(f"text[:4] = '{text[:4]}'    # 从开始到索引3")
    print(f"text[4:] = '{text[4:]}'    # 从索引4到结束")
    print(f"text[:] = '{text[:]}'      # 完整字符串")
    
    # 使用负数索引
    print("\n负数索引切片:")
    print(f"text[-4:] = '{text[-4:]}'   # 最后4个字符")
    print(f"text[:-4] = '{text[:-4]}'   # 除了最后4个字符")
```

### 高级切片操作

```python
def demonstrate_advanced_slicing():
    """演示高级切片操作"""
    text = "abcdefghijk"
    print(f"字符串: {text}")
    
    # 带步长的切片: string[start:end:step]
    print("\n带步长的切片 [start:end:step]:")
    print(f"text[::2] = '{text[::2]}'     # 每隔一个字符")
    print(f"text[1::2] = '{text[1::2]}'   # 从索引1开始，每隔一个")
    print(f"text[::3] = '{text[::3]}'     # 每隔两个字符")
    
    # 反向切片
    print("\n反向切片:")
    print(f"text[::-1] = '{text[::-1]}'   # 反转字符串")
    print(f"text[::-2] = '{text[::-2]}'   # 反向每隔一个")
    print(f"text[8:2:-1] = '{text[8:2:-1]}' # 从索引8到3反向")
```

### 切片边界情况

```python
def demonstrate_slicing_edge_cases():
    """演示切片的边界情况"""
    text = "Python"
    print(f"字符串: {text}")
    
    # 超出范围的切片不会报错
    print("\n超出范围的切片:")
    print(f"text[2:100] = '{text[2:100]}'  # 结束索引超出范围")
    print(f"text[-100:4] = '{text[-100:4]}' # 开始索引超出范围")
    
    # 开始索引大于结束索引
    print("\n开始索引大于结束索引:")
    print(f"text[4:2] = '{text[4:2]}'      # 返回空字符串")
    
    # 步长为0会报错
    try:
        result = text[::0]
    except ValueError as e:
        print(f"text[::0] -> 错误: {e}")
```

## 实际应用示例

### 文件名处理

```python
# 获取文件扩展名
filename = "document.pdf"
extension = filename[filename.rfind('.'):]
name_only = filename[:filename.rfind('.')]

print(f"文件名: {filename}")
print(f"扩展名: {extension}")
print(f"文件名（无扩展名）: {name_only}")
```

### 邮箱地址解析

```python
# 提取域名和用户名
email = "user@example.com"
domain = email[email.find('@')+1:]
username = email[:email.find('@')]

print(f"邮箱: {email}")
print(f"用户名: {username}")
print(f"域名: {domain}")
```

### 字符串反转和提取

```python
# 字符串反转
original = "Hello World"
reversed_str = original[::-1]
print(f"原字符串: {original}")
print(f"反转后: {reversed_str}")

# 提取特定部分
text = "Programming is fun"
first_5 = text[:5]
last_5 = text[-5:]
middle = text[5:-5]

print(f"前5个字符: '{first_5}'")
print(f"后5个字符: '{last_5}'")
print(f"中间部分: '{middle}'")
```

### 数据分离

```python
# 每隔n个字符提取
data = "a1b2c3d4e5f6g7h8"
letters = data[::2]  # 提取字母
numbers = data[1::2]  # 提取数字

print(f"原数据: {data}")
print(f"字母: {letters}")
print(f"数字: {numbers}")
```

## 学习要点

### 索引规则
- **正向索引**：从0开始，到len(string)-1结束
- **反向索引**：从-1开始，到-len(string)结束
- **索引错误**：超出范围会引发IndexError

### 切片语法
- **基本语法**：`string[start:end:step]`
- **默认值**：start=0, end=len(string), step=1
- **边界处理**：自动处理超出范围的索引
- **空切片**：start >= end时返回空字符串

### 实用技巧
- **字符串反转**：使用`[::-1]`
- **获取最后n个字符**：使用`[-n:]`
- **获取除最后n个字符**：使用`[:-n]`
- **每隔n个字符**：使用`[::n]`

## 注意事项

1. **索引从0开始**：这是Python的基本规则
2. **切片不包含结束索引**：`[start:end]`不包含end位置的字符
3. **切片创建新对象**：切片操作会创建新的字符串对象
4. **负数索引很有用**：特别适合从字符串末尾开始操作
5. **步长可以为负数**：用于反向遍历

## 下一步学习

掌握了字符串索引和切片后，建议继续学习：
- 字符串常用方法（03_string_methods.py）
- 字符串格式化（04_string_formatting.py）
- 字符串操作和连接（05_string_operations.py）

通过大量练习，你将能够熟练运用索引和切片来处理各种字符串操作任务。