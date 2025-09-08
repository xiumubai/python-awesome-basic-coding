# 字符串格式化

## 学习目标

通过本节学习，你将掌握：
- Python中各种字符串格式化方法
- %格式化、str.format()和f-string的使用
- 数字和日期时间的格式化
- 高级格式化技巧和字符串模板

## 旧式%格式化

### 基本用法

```python
# 基本%格式化
name = "Alice"
age = 25
print("我的名字是%s，今年%d岁" % (name, age))

# 字典格式化
data = {'name': 'Bob', 'age': 30}
print("姓名：%(name)s，年龄：%(age)d" % data)
```

### 格式说明符

```python
# 常用格式说明符
print("%s" % "字符串")      # 字符串
print("%d" % 42)           # 整数
print("%f" % 3.14159)      # 浮点数
print("%.2f" % 3.14159)    # 保留2位小数
print("%10s" % "右对齐")    # 宽度10，右对齐
print("%-10s" % "左对齐")   # 宽度10，左对齐
```

## str.format()方法

### 位置参数

```python
# 位置参数
print("Hello, {}! You are {} years old.".format("Alice", 25))
print("Hello, {0}! You are {1} years old.".format("Bob", 30))
print("Hello, {1}! You are {0} years old.".format(25, "Charlie"))
```

### 关键字参数

```python
# 关键字参数
print("Hello, {name}! You are {age} years old.".format(name="Diana", age=28))

# 混合使用
print("{0} is {age} years old and lives in {1}".format("Eve", "Beijing", age=32))
```

### 格式规范

```python
# 数字格式化
pi = 3.14159
print("Pi: {:.2f}".format(pi))        # 保留2位小数
print("Pi: {:10.2f}".format(pi))      # 宽度10，2位小数
print("Pi: {:0>10.2f}".format(pi))    # 零填充

# 对齐方式
text = "Python"
print("'{:>10}'".format(text))        # 右对齐
print("'{:<10}'".format(text))        # 左对齐
print("'{:^10}'".format(text))        # 居中对齐
print("'{:*^10}'".format(text))       # 用*填充居中
```

## f-string格式化（推荐）

### 基本语法

```python
# f-string基本用法
name = "Alice"
age = 25
print(f"我的名字是{name}，今年{age}岁")

# 表达式计算
print(f"明年我{age + 1}岁")
print(f"我的名字有{len(name)}个字符")
```

### 格式化选项

```python
# 数字格式化
pi = 3.14159
print(f"Pi: {pi:.2f}")          # 保留2位小数
print(f"Pi: {pi:10.2f}")        # 宽度10，2位小数
print(f"Pi: {pi:0>10.2f}")      # 零填充

# 对齐和填充
text = "Python"
print(f"'{text:>10}'")
print(f"'{text:<10}'")
print(f"'{text:^10}'")
print(f"'{text:*^10}'")
```

### 调试功能

```python
# Python 3.8+ 调试功能
x = 10
y = 20
print(f"{x=}, {y=}, {x+y=}")  # 输出：x=10, y=20, x+y=30
```

## 数字格式化

### 整数格式化

```python
number = 1234567
print(f"千分位分隔符: {number:,}")      # 1,234,567
print(f"零填充: {number:010d}")         # 0001234567
print(f"正号显示: {number:+d}")         # +1234567
```

### 浮点数格式化

```python
float_num = 123.456789
print(f"2位小数: {float_num:.2f}")      # 123.46
print(f"科学计数法: {float_num:.2e}")    # 1.23e+02
print(f"百分比: {float_num:.1%}")       # 12345.7%
print(f"千分位: {float_num:,.2f}")      # 123.46
```

### 进制转换

```python
number = 255
print(f"十进制: {number}")
print(f"二进制: {number:b}")           # 11111111
print(f"八进制: {number:o}")           # 377
print(f"十六进制: {number:x}")         # ff
print(f"带前缀十六进制: {number:#x}")   # 0xff
```

## 日期时间格式化

### 基本日期时间格式化

```python
import datetime

now = datetime.datetime.now()
date_only = datetime.date.today()
time_only = datetime.time(14, 30, 45)

# f-string日期格式化
print(f"年-月-日: {now:%Y-%m-%d}")
print(f"时:分:秒: {now:%H:%M:%S}")
print(f"完整格式: {now:%Y-%m-%d %H:%M:%S}")
print(f"中文格式: {now:%Y年%m月%d日 %H时%M分%S秒}")
```

### 常用日期格式

```python
# 各种日期时间格式
formats = [
    "%Y-%m-%d",           # 2024-01-15
    "%d/%m/%Y",           # 15/01/2024
    "%B %d, %Y",          # January 15, 2024
    "%A, %B %d, %Y",      # Monday, January 15, 2024
    "%Y年%m月%d日",        # 2024年01月15日
    "%H:%M:%S",           # 14:30:45
    "%I:%M %p",           # 02:30 PM
]

for fmt in formats:
    formatted = now.strftime(fmt)
    print(f"{fmt:<20} -> {formatted}")
```

## 高级格式化技巧

### 动态格式化

```python
# 使用变量控制格式
width = 15
precision = 3
number = 123.456789
print(f"动态宽度和精度: {number:{width}.{precision}f}")
```

### 表格格式化

```python
# 创建表格
students = [
    ("Alice", 85, 92, 88),
    ("Bob", 78, 85, 82),
    ("Charlie", 92, 88, 95),
]

# 表头
print(f"{'Name':<10} {'Math':>6} {'Science':>8} {'Average':>8}")
print("-" * 40)

# 数据行
for name, math, science, english in students:
    average = (math + science + english) / 3
    print(f"{name:<10} {math:>6} {science:>8} {average:>8.1f}")
```

### 条件格式化

```python
# 根据条件格式化
scores = [85, 92, 78, 96, 73]
for i, score in enumerate(scores, 1):
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
    print(f"Student {i}: {score:3d} ({grade})")
```

## 字符串模板

### Template类使用

```python
from string import Template

# 基本模板
template = Template("Hello, $name! Welcome to $place.")
result = template.substitute(name="Alice", place="Python World")
print(result)

# 使用字典
data = {'name': 'Bob', 'place': 'Programming Land'}
result = template.substitute(data)
print(result)
```

### 安全替换

```python
# 安全替换（缺少变量时不报错）
incomplete_data = {'name': 'Charlie'}
result = template.safe_substitute(incomplete_data)
print(result)  # Hello, Charlie! Welcome to $place.
```

## 完整示例代码

```python
import datetime
from string import Template

def string_formatting_demo():
    """字符串格式化综合演示"""
    
    # 1. 基本格式化比较
    name = "Alice"
    age = 25
    salary = 50000.50
    
    print("=== 格式化方法比较 ===")
    print("%%格式化: 我是%s，%d岁，月薪%.2f" % (name, age, salary))
    print("format方法: 我是{}，{}岁，月薪{:.2f}".format(name, age, salary))
    print(f"f-string: 我是{name}，{age}岁，月薪{salary:.2f}")
    
    # 2. 数字格式化
    number = 1234567.89
    print("\n=== 数字格式化 ===")
    print(f"千分位: {number:,.2f}")
    print(f"科学计数法: {number:.2e}")
    print(f"百分比: {0.1234:.1%}")
    
    # 3. 日期格式化
    now = datetime.datetime.now()
    print("\n=== 日期格式化 ===")
    print(f"标准格式: {now:%Y-%m-%d %H:%M:%S}")
    print(f"中文格式: {now:%Y年%m月%d日}")
    
    # 4. 表格格式化
    print("\n=== 表格格式化 ===")
    data = [("产品A", 100, 1200.50), ("产品B", 50, 800.00)]
    print(f"{'产品':<10} {'数量':>6} {'金额':>10}")
    print("-" * 30)
    for product, qty, amount in data:
        print(f"{product:<10} {qty:>6} {amount:>10.2f}")

if __name__ == "__main__":
    string_formatting_demo()
```

## 运行示例

在终端中运行：

```bash
python3 04_string_formatting.py
```

## 学习要点

### 1. 格式化方法选择
- **f-string**：Python 3.6+推荐使用，简洁高效
- **str.format()**：功能强大，兼容性好
- **%格式化**：旧式方法，了解即可

### 2. 常用格式说明符
- `{:d}`：整数
- `{:.2f}`：浮点数，保留2位小数
- `{:,}`：千分位分隔符
- `{:>10}`：右对齐，宽度10
- `{:0>5}`：零填充，宽度5

### 3. 日期时间格式
- `%Y`：四位年份
- `%m`：月份（01-12）
- `%d`：日期（01-31）
- `%H`：小时（00-23）
- `%M`：分钟（00-59）
- `%S`：秒（00-59）

## 实际应用场景

1. **报告生成**：格式化数据报告
2. **日志记录**：统一日志格式
3. **用户界面**：显示格式化信息
4. **文件命名**：生成规范文件名
5. **数据导出**：格式化导出数据

## 注意事项

1. **性能考虑**：f-string通常性能最好
2. **可读性**：选择最易读的格式化方法
3. **兼容性**：考虑Python版本兼容性
4. **安全性**：避免格式化用户输入的不可信数据
5. **国际化**：考虑多语言和地区格式

## 下一步学习

学习完字符串格式化后，建议继续学习：
- 字符串操作和连接
- 字符串查找和替换
- 正则表达式基础
- 字符串编码和解码