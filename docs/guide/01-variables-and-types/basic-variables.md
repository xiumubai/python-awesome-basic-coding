# 基本变量定义和赋值

::: tip 📍 导航路径
[🏠 首页](/guide/) > [📊 变量和数据类型](/guide/01-variables-and-types/) > 基本变量定义和赋值
:::

<div style="margin: 10px 0; padding: 10px; background: #f0f9ff; border-left: 4px solid #0ea5e9; border-radius: 4px;">
  <strong>🧭 快速导航：</strong>
  <a href="/guide/01-variables-and-types/" style="margin: 0 8px; color: #0ea5e9; text-decoration: none;">← 返回模块首页</a> |
  <a href="/guide/01-variables-and-types/data-types.md" style="margin: 0 8px; color: #0ea5e9; text-decoration: none;">下一节：数据类型 →</a>
</div>

## 学习目标

1. 理解什么是变量
2. 学会如何定义变量
3. 掌握变量赋值的基本语法
4. 了解变量在内存中的存储概念

## 什么是变量？

变量就像一个容器，用来存储数据。变量有名字，可以通过名字来访问存储的数据。

## 基本变量定义和赋值

### 语法规则

```python
变量名 = 值
```

- 等号左边是变量名
- 等号右边是要存储的值
- 注意：这里的等号不是数学中的等于，而是赋值操作

### 基本示例

```python
# 定义一个存储姓名的变量
name = "张三"
print(f"姓名变量：name = {name}")
print(f"变量name的值是：{name}")

# 定义一个存储年龄的变量
age = 25
print(f"年龄变量：age = {age}")
print(f"变量age的值是：{age}")

# 定义一个存储身高的变量
height = 175.5
print(f"身高变量：height = {height}")
print(f"变量height的值是：{height}")

# 定义一个存储是否是学生的变量
is_student = True
print(f"学生状态变量：is_student = {is_student}")
print(f"变量is_student的值是：{is_student}")
```

## 变量重新赋值

变量的值可以随时改变：

```python
age = 25
print(f"原来的年龄：{age}")

age = 26  # 重新赋值
print(f"更新后的年龄：{age}")
```

## 一次定义多个变量

### 方法1：分别赋值相同的值

```python
x = y = z = 0
print(f"x = {x}, y = {y}, z = {z}")
```

### 方法2：同时赋值不同的值

```python
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")
```

### 方法3：交换变量的值

```python
a, b = 1, 2
print(f"交换前：a = {a}, b = {b}")

a, b = b, a
print(f"交换后：a = {a}, b = {b}")
```

## 变量的内存概念

每个变量都有一个内存地址，可以使用 `id()` 函数查看：

```python
name = "张三"
age = 25

print(f"变量name的内存地址：{id(name)}")
print(f"变量age的内存地址：{id(age)}")
```

## 实践练习

请尝试定义以下变量：

1. 定义一个变量存储你的姓名
2. 定义一个变量存储你的年龄
3. 定义一个变量存储你的爱好
4. 打印这些变量的值

### 练习示例

```python
my_name = "李四"
my_age = 20
my_hobby = "编程"

print(f"我的姓名：{my_name}")
print(f"我的年龄：{my_age}")
print(f"我的爱好：{my_hobby}")
```

## 思考题

1. 变量名可以是中文吗？
2. 变量名可以以数字开头吗？
3. 变量名可以包含空格吗？
4. 什么是好的变量命名习惯？

### 思考题答案

1. **可以，但不推荐** - 虽然Python支持中文变量名，但在实际开发中建议使用英文
2. **不可以，会报错** - 变量名必须以字母或下划线开头
3. **不可以，会报错** - 变量名不能包含空格，可以使用下划线连接
4. **使用有意义的英文单词，遵循命名规范** - 变量名应该清晰表达其用途

## 常见错误示例

以下是一些常见的错误，请注意避免：

```python
# 错误1：变量名以数字开头
# 1name = "错误"  # SyntaxError

# 错误2：变量名包含空格
# my name = "错误"  # SyntaxError

# 错误3：使用Python关键字作为变量名
# if = 5  # SyntaxError
```

## 完整代码示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第一课：基本变量定义和赋值

学习目标：
1. 理解什么是变量
2. 学会如何定义变量
3. 掌握变量赋值的基本语法
4. 了解变量在内存中的存储概念
"""

print("=" * 50)
print("第一课：基本变量定义和赋值")
print("=" * 50)

# 1. 什么是变量？
print("\n1. 什么是变量？")
print("-" * 20)
print("变量就像一个容器，用来存储数据")
print("变量有名字，可以通过名字来访问存储的数据")

# 2. 基本变量定义和赋值
print("\n2. 基本变量定义和赋值")
print("-" * 20)

# 定义各种类型的变量
name = "张三"
age = 25
height = 175.5
is_student = True

print(f"姓名变量：name = {name}")
print(f"年龄变量：age = {age}")
print(f"身高变量：height = {height}")
print(f"学生状态变量：is_student = {is_student}")

# 3. 变量重新赋值
print("\n3. 变量可以重新赋值")
print("-" * 20)
print(f"原来的年龄：{age}")
age = 26
print(f"更新后的年龄：{age}")

# 4. 多变量赋值
print("\n4. 一次定义多个变量")
print("-" * 20)

x = y = z = 0
print(f"x = {x}, y = {y}, z = {z}")

a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# 交换变量值
print(f"交换前：a = {a}, b = {b}")
a, b = b, a
print(f"交换后：a = {a}, b = {b}")

# 5. 变量的内存地址
print("\n5. 变量的内存概念")
print("-" * 20)
print(f"变量name的内存地址：{id(name)}")
print(f"变量age的内存地址：{id(age)}")

print("\n=" * 50)
print("第一课学习完成！")
print("下一课将学习Python的数据类型")
print("=" * 50)
```

## 运行方法

在终端中输入以下命令运行代码：

```bash
python 01_basic_variables.py
```

或者在IDE中直接运行该文件。

## 学习要点

1. **变量是存储数据的容器**
2. **赋值语法：变量名 = 值**
3. **变量可以重新赋值**
4. **支持多种赋值方式**
5. **每个变量都有内存地址**
6. **遵循变量命名规范**

## 下一步

学习完基本变量定义后，继续学习：[数据类型详解](./data-types)