# 函数基础语法

本节介绍Python函数的基础语法，包括函数的定义、调用、参数传递和返回值等核心概念。

## 学习目标

- 掌握函数的定义语法
- 理解函数的调用机制
- 学会使用参数和返回值
- 了解函数命名规范
- 理解函数的执行流程

## 1. 最简单的函数定义

函数是组织代码的基本单位，使用`def`关键字定义：

```python
def greet():
    """最简单的函数，没有参数，没有返回值"""
    print("Hello, World!")

# 调用函数
greet()  # 输出：Hello, World!
```

**要点说明：**
- `def`关键字用于定义函数
- 函数名后面必须有括号`()`
- 冒号`:`表示函数体开始
- 函数体需要缩进

## 2. 带参数的函数

函数可以接收参数，使代码更加灵活：

```python
def greet_person(name):
    """带一个参数的函数"""
    print(f"Hello, {name}!")

# 调用带参数的函数
greet_person('Alice')  # 输出：Hello, Alice!
greet_person('Bob')    # 输出：Hello, Bob!
```

### 多个参数的函数

```python
def introduce(name, age):
    """带两个参数的函数"""
    print(f"我叫{name}，今年{age}岁")

# 调用带多个参数的函数
introduce('张三', 25)  # 输出：我叫张三，今年25岁
introduce('李四', 30)  # 输出：我叫李四，今年30岁
```

## 3. 带返回值的函数

函数可以使用`return`语句返回结果：

```python
def add_numbers(a, b):
    """计算两个数的和并返回结果"""
    result = a + b
    return result

# 调用带返回值的函数
sum_result = add_numbers(3, 5)
print(f"结果：{sum_result}")  # 输出：结果：8

# 也可以直接使用返回值
print(f"结果：{add_numbers(10, 20)}")  # 输出：结果：30
```

## 4. 函数的完整结构

一个完整的函数通常包含文档字符串、参数处理和返回值：

```python
def calculate_area(length, width):
    """
    计算矩形面积
    
    参数:
        length (float): 矩形的长
        width (float): 矩形的宽
    
    返回:
        float: 矩形的面积
    """
    # 函数体：执行计算
    area = length * width
    
    # 返回结果
    return area

# 使用函数
length = 5.0
width = 3.0
area = calculate_area(length, width)
print(f"长{length}，宽{width}的矩形面积是：{area}")  # 输出：长5.0，宽3.0的矩形面积是：15.0
```

## 5. 函数命名规范

Python函数命名应遵循以下规范：

```python
# 好的函数命名（使用小写字母和下划线）
def get_user_name():
    """获取用户名"""
    return "用户123"

def calculate_total_price(price, quantity):
    """计算总价"""
    return price * quantity

def is_valid_email(email):
    """检查邮箱是否有效"""
    return "@" in email

# 使用这些函数
print(f"用户名：{get_user_name()}")                    # 输出：用户名：用户123
print(f"总价：{calculate_total_price(10.5, 3)}")        # 输出：总价：31.5
print(f"邮箱有效性：{is_valid_email('test@example.com')}")  # 输出：邮箱有效性：True
```

**命名规范要点：**
- 使用小写字母和下划线
- 函数名应该描述函数的功能
- 动词开头的函数名表示执行动作
- `is_`开头的函数名通常返回布尔值

## 6. 函数调用其他函数

函数可以调用其他函数，实现代码复用：

```python
def get_full_name(first_name, last_name):
    """获取全名"""
    return f"{first_name} {last_name}"

def create_greeting(first_name, last_name):
    """创建问候语，调用其他函数"""
    full_name = get_full_name(first_name, last_name)
    return f"欢迎，{full_name}！"

# 使用函数
greeting = create_greeting("张", "三")
print(greeting)  # 输出：欢迎，张 三！
```

## 7. 函数执行流程

理解函数的执行流程对调试很重要：

```python
def demo_function(x):
    """演示函数执行流程"""
    print(f"  函数开始执行，参数x = {x}")
    result = x * 2
    print(f"  计算结果：{x} * 2 = {result}")
    print("  函数即将返回")
    return result

print("主程序：调用demo_function(5)")
result = demo_function(5)
print(f"主程序：函数返回值为 {result}")
```

**输出：**
```
主程序：调用demo_function(5)
  函数开始执行，参数x = 5
  计算结果：5 * 2 = 10
  函数即将返回
主程序：函数返回值为 10
```

## 8. 实用函数示例

以下是一些实用的函数示例：

```python
def celsius_to_fahrenheit(celsius):
    """摄氏度转华氏度"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """华氏度转摄氏度"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# 温度转换示例
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")  # 输出：25°C = 77.0°F

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.1f}°C")  # 输出：77°F = 25.0°C
```

## 运行示例

你可以运行以下代码来测试函数基础语法：

```bash
python3 01_function_basics.py
```

## 关键知识点总结

1. **函数定义**：使用`def`关键字定义函数
2. **函数命名**：使用小写字母和下划线，名称应描述功能
3. **参数传递**：函数可以接收零个或多个参数
4. **返回值**：使用`return`语句返回结果
5. **函数调用**：通过函数名和括号调用函数
6. **代码复用**：函数可以调用其他函数，实现代码模块化

## 练习建议

1. 编写一个计算圆面积的函数
2. 创建一个判断数字是否为偶数的函数
3. 实现一个简单的计算器函数
4. 练习函数的嵌套调用

函数是Python编程的基础，掌握好函数的基本语法对后续学习非常重要。