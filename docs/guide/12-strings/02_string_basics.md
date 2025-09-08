# 字符串基础

字符串是Python中最重要的数据类型之一，用于存储和处理文本数据。本节将详细介绍字符串的基础概念、创建方法和基本属性。

## 学习目标

- 理解字符串的定义和特性
- 掌握不同的字符串创建方式
- 理解字符串的不可变性
- 学会使用多行字符串和原始字符串
- 掌握字符串的基本操作

## 字符串创建方法

### 基本创建方式

Python提供了多种创建字符串的方法：

```python
# 使用单引号
single_quote_str = 'Hello, World!'
print(f"单引号字符串: {single_quote_str}")
print(f"类型: {type(single_quote_str)}")

# 使用双引号
double_quote_str = "Python Programming"
print(f"双引号字符串: {double_quote_str}")

# 包含引号的字符串
quote_in_string1 = "He said 'Hello'"
quote_in_string2 = 'She replied "Hi there"'
print(f"包含单引号: {quote_in_string1}")
print(f"包含双引号: {quote_in_string2}")
```

### 转义字符

当需要在字符串中包含特殊字符时，可以使用转义字符：

```python
# 使用转义字符
escaped_string = "He said \"Hello\" and she replied 'Hi'"
print(f"转义字符: {escaped_string}")

# 常用转义字符
special_chars = "换行符: \n制表符: \t反斜杠: \\"
print(special_chars)
```

### 空字符串

```python
# 创建空字符串
empty_string1 = ""
empty_string2 = ''
print(f"空字符串1: '{empty_string1}', 长度: {len(empty_string1)}")
print(f"空字符串2: '{empty_string2}', 长度: {len(empty_string2)}")
```

## 多行字符串

### 三重引号

使用三重引号可以创建跨越多行的字符串：

```python
# 使用三重双引号
multiline_str1 = """这是一个
多行字符串
可以包含换行符"""
print("三重双引号多行字符串:")
print(multiline_str1)

# 使用三重单引号
multiline_str2 = '''这也是一个
多行字符串
使用三重单引号'''
print("\n三重单引号多行字符串:")
print(multiline_str2)
```

### 保持格式的多行字符串

```python
# 多行字符串保持原有格式
formatted_multiline = """第一行
    第二行（有缩进）
        第三行（更多缩进）
第四行（无缩进）"""
print("格式化多行字符串:")
print(formatted_multiline)
```

### 使用换行符

```python
# 使用\n创建多行效果
newline_string = "第一行\n第二行\n第三行"
print("使用\\n的多行字符串:")
print(newline_string)
```

## 字符串属性

### 基本属性

```python
sample_string = "Python编程学习"

# 字符串长度
print(f"字符串: {sample_string}")
print(f"长度: {len(sample_string)}")

# 字符串是否为空
print(f"是否为空: {len(sample_string) == 0}")
print(f"布尔值: {bool(sample_string)}")

# 空字符串的布尔值
empty_str = ""
print(f"空字符串的布尔值: {bool(empty_str)}")
```

### 字符类型检查

```python
# 检查字符串包含的字符类型
mixed_string = "Hello123世界!"
print(f"混合字符串: {mixed_string}")
print(f"长度: {len(mixed_string)}")
print(f"包含字母: {any(c.isalpha() for c in mixed_string)}")
print(f"包含数字: {any(c.isdigit() for c in mixed_string)}")
print(f"包含中文: {any('\u4e00' <= c <= '\u9fff' for c in mixed_string)}")
```

## 字符串不可变性

字符串是不可变的数据类型，这意味着一旦创建就不能修改：

```python
original_string = "Hello"
print(f"原始字符串: {original_string}")
print(f"字符串ID: {id(original_string)}")

# 字符串连接会创建新的字符串对象
new_string = original_string + " World"
print(f"连接后字符串: {new_string}")
print(f"新字符串ID: {id(new_string)}")
print(f"原字符串ID: {id(original_string)}")
print(f"ID是否相同: {id(original_string) == id(new_string)}")
```

### 不能直接修改字符

```python
# 尝试修改字符串会产生错误
try:
    original_string[0] = 'h'  # 这会报错
except TypeError as e:
    print(f"错误: {e}")

# 正确的修改方式是创建新字符串
modified_string = 'h' + original_string[1:]
print(f"正确的修改方式: {modified_string}")
```

## 字符串连接

### 基本连接方法

```python
str1 = "Hello"
str2 = "World"

# 使用+操作符
result1 = str1 + " " + str2
print(f"使用+连接: {result1}")

# 使用+=操作符
str3 = "Python"
str3 += " Programming"
print(f"使用+=连接: {str3}")

# 使用*操作符重复
repeated = "Ha" * 3
print(f"使用*重复: {repeated}")
```

### 连接不同类型

```python
# 连接数字和字符串（需要转换）
number = 42
text = "The answer is "
result = text + str(number)
print(f"连接数字: {result}")
```

## 原始字符串

原始字符串使用`r`前缀，可以避免转义字符的解释：

```python
# 普通字符串中的转义字符
normal_string = "C:\\Users\\name\\file.txt"
print(f"普通字符串: {normal_string}")

# 原始字符串（r前缀）
raw_string = r"C:\Users\name\file.txt"
print(f"原始字符串: {raw_string}")

# 原始字符串在正则表达式中很有用
regex_pattern = r"\d+\.\d+"  # 匹配小数的正则表达式
print(f"正则表达式模式: {regex_pattern}")
```

### 原始字符串的限制

```python
# 原始字符串不能以单个反斜杠结尾
# raw_invalid = r"path\"  # 这会报错

# 正确的方式
raw_valid = r"path" + "\\"
print(f"正确的方式: {raw_valid}")
```

## 完整示例代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def demonstrate_string_basics():
    """演示字符串基础概念"""
    print("=== 字符串基础演示 ===")
    
    # 1. 字符串创建
    single_str = 'Hello'
    double_str = "World"
    multiline_str = """这是
    多行字符串"""
    raw_str = r"C:\path\to\file"
    
    print(f"单引号: {single_str}")
    print(f"双引号: {double_str}")
    print(f"多行字符串: {multiline_str}")
    print(f"原始字符串: {raw_str}")
    
    # 2. 字符串属性
    sample = "Python编程"
    print(f"\n字符串: {sample}")
    print(f"长度: {len(sample)}")
    print(f"类型: {type(sample)}")
    print(f"布尔值: {bool(sample)}")
    
    # 3. 字符串不可变性
    original = "Hello"
    modified = original + " World"
    print(f"\n原始: {original} (ID: {id(original)})")
    print(f"修改后: {modified} (ID: {id(modified)})")
    print(f"ID相同: {id(original) == id(modified)}")
    
    # 4. 字符串连接
    result = "Python" + " " + "Programming"
    repeated = "Ha" * 3
    print(f"\n连接: {result}")
    print(f"重复: {repeated}")

if __name__ == "__main__":
    demonstrate_string_basics()
```

## 运行示例

```bash
python3 01_string_basics.py
```

## 学习要点

### 重要概念
1. **字符串不可变性**：字符串一旦创建就不能修改，任何"修改"操作都会创建新的字符串对象
2. **引号的选择**：单引号和双引号功能相同，选择时考虑字符串内容中包含的引号类型
3. **多行字符串**：使用三重引号可以创建包含换行符的字符串
4. **原始字符串**：使用`r`前缀可以避免转义字符的解释，特别适用于正则表达式和文件路径

### 最佳实践
1. **一致性**：在项目中保持引号使用的一致性
2. **可读性**：对于包含引号的字符串，选择合适的外层引号类型
3. **性能考虑**：大量字符串连接时，考虑使用`join()`方法而不是`+`操作符
4. **编码规范**：在文件开头声明编码格式，特别是包含中文字符时

### 注意事项
1. 字符串是不可变的，修改操作会创建新对象
2. 原始字符串不能以单个反斜杠结尾
3. 空字符串的布尔值为`False`
4. 字符串长度包括所有字符，包括空格和特殊字符

## 下一步

学习完字符串基础后，建议继续学习：
- [字符串索引和切片](./03_string_indexing.md)
- [字符串方法](./04_string_methods.md)
- [字符串格式化](./05_string_formatting.md)