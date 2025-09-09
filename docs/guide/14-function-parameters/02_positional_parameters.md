# 位置参数 (Positional Parameters)

位置参数是Python函数中最基础的参数类型，参数的值根据在函数调用时的位置顺序来确定。这是函数参数的基础，理解位置参数对掌握其他参数类型至关重要。

## 核心概念

### 什么是位置参数？
位置参数是按照在函数定义中的位置顺序来传递的参数。调用函数时，参数值会按照位置顺序分配给对应的形参。

### 特点
- **顺序敏感**：参数的顺序不能改变
- **必须提供**：所有位置参数都必须在调用时提供值
- **简洁明了**：最直观的参数传递方式

## 基础用法

### 简单的位置参数

```python
def greet(name, age):
    """
    使用位置参数的简单问候函数
    
    Args:
        name: 姓名（字符串）
        age: 年龄（整数）
    """
    print(f"你好，{name}！你今年{age}岁了。")

# 正确调用 - 按位置传递参数
greet("小明", 25)  # 输出: 你好，小明！你今年25岁了。

# 错误调用 - 参数顺序错误
# greet(25, "小明")  # 会产生意外结果
```

### 多个位置参数

```python
def calculate_rectangle_area(length, width, height=None):
    """
    计算矩形面积或长方体体积
    
    Args:
        length: 长度
        width: 宽度  
        height: 高度（可选，如果提供则计算体积）
    """
    area = length * width
    if height is not None:
        volume = area * height
        print(f"长方体体积: {volume}")
        return volume
    else:
        print(f"矩形面积: {area}")
        return area

# 计算面积
calculate_rectangle_area(10, 5)  # 输出: 矩形面积: 50

# 计算体积
calculate_rectangle_area(10, 5, 3)  # 输出: 长方体体积: 150
```

## 实际应用示例

### 数学运算函数

```python
def add_numbers(a, b):
    """加法运算"""
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

def multiply_three_numbers(x, y, z):
    """三个数相乘"""
    result = x * y * z
    print(f"{x} × {y} × {z} = {result}")
    return result

def power_calculation(base, exponent):
    """幂运算"""
    result = base ** exponent
    print(f"{base}^{exponent} = {result}")
    return result

# 使用示例
add_numbers(15, 25)  # 输出: 15 + 25 = 40
multiply_three_numbers(2, 3, 4)  # 输出: 2 × 3 × 4 = 24
power_calculation(2, 8)  # 输出: 2^8 = 256
```

### 字符串处理函数

```python
def format_name(first_name, last_name):
    """格式化姓名"""
    full_name = f"{last_name} {first_name}"
    print(f"格式化后的姓名: {full_name}")
    return full_name

def create_email(username, domain):
    """创建邮箱地址"""
    email = f"{username}@{domain}"
    print(f"邮箱地址: {email}")
    return email

def repeat_string(text, count):
    """重复字符串"""
    result = text * count
    print(f"重复结果: {result}")
    return result

# 使用示例
format_name("明", "李")  # 输出: 格式化后的姓名: 李 明
create_email("user123", "example.com")  # 输出: 邮箱地址: user123@example.com
repeat_string("Hello ", 3)  # 输出: 重复结果: Hello Hello Hello 
```

### 数据处理函数

```python
def find_max_min(numbers):
    """找出列表中的最大值和最小值"""
    if not numbers:
        return None, None
    
    max_val = max(numbers)
    min_val = min(numbers)
    print(f"最大值: {max_val}, 最小值: {min_val}")
    return max_val, min_val

def calculate_average(numbers):
    """计算平均值"""
    if not numbers:
        return 0
    
    average = sum(numbers) / len(numbers)
    print(f"平均值: {average:.2f}")
    return average

def compare_lists(list1, list2):
    """比较两个列表"""
    common = set(list1) & set(list2)
    unique_to_first = set(list1) - set(list2)
    unique_to_second = set(list2) - set(list1)
    
    print(f"共同元素: {common}")
    print(f"第一个列表独有: {unique_to_first}")
    print(f"第二个列表独有: {unique_to_second}")
    
    return common, unique_to_first, unique_to_second

# 使用示例
numbers = [1, 5, 3, 9, 2, 8]
find_max_min(numbers)  # 输出: 最大值: 9, 最小值: 1
calculate_average(numbers)  # 输出: 平均值: 4.67

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
compare_lists(list_a, list_b)
# 输出: 
# 共同元素: {4, 5}
# 第一个列表独有: {1, 2, 3}
# 第二个列表独有: {8, 6, 7}
```

## 注意事项和最佳实践

### 1. 参数顺序的重要性

```python
# 好的做法：参数顺序有逻辑性
def transfer_money(from_account, to_account, amount):
    """转账函数 - 参数顺序符合逻辑"""
    print(f"从 {from_account} 转账 {amount} 元到 {to_account}")

# 不好的做法：参数顺序混乱
def bad_transfer(amount, from_account, to_account):
    """不推荐的参数顺序"""
    print(f"从 {from_account} 转账 {amount} 元到 {to_account}")

# 使用时容易出错
transfer_money("账户A", "账户B", 1000)  # 清晰明了
# bad_transfer("账户A", "账户B", 1000)  # 容易搞错参数含义
```

### 2. 参数数量的控制

```python
# 好的做法：参数数量适中
def create_user(name, email, age):
    """创建用户 - 参数数量合理"""
    return {"name": name, "email": email, "age": age}

# 不推荐：参数过多
def create_user_bad(name, email, age, phone, address, city, country, postal_code):
    """参数过多，难以记忆和使用"""
    pass  # 考虑使用字典或类来组织这些参数
```

### 3. 参数验证

```python
def divide_numbers(dividend, divisor):
    """
    除法运算，包含参数验证
    
    Args:
        dividend: 被除数
        divisor: 除数
    
    Returns:
        float: 除法结果
    
    Raises:
        ValueError: 当除数为0时抛出异常
    """
    if divisor == 0:
        raise ValueError("除数不能为0")
    
    result = dividend / divisor
    print(f"{dividend} ÷ {divisor} = {result}")
    return result

# 正常使用
divide_numbers(10, 2)  # 输出: 10 ÷ 2 = 5.0

# 异常情况
try:
    divide_numbers(10, 0)
except ValueError as e:
    print(f"错误: {e}")  # 输出: 错误: 除数不能为0
```

## 运行示例

要运行这些示例，请使用以下命令：

```bash
python3 01_positional_parameters.py
```

## 学习要点

1. **理解位置的重要性**：参数的位置决定了值的分配
2. **保持参数顺序的逻辑性**：让参数顺序符合直觉
3. **控制参数数量**：避免参数过多导致的复杂性
4. **添加适当的验证**：确保函数的健壮性
5. **编写清晰的文档**：说明每个参数的含义和类型

## 下一步

掌握了位置参数后，接下来学习[关键字参数](03_keyword_parameters.md)，了解如何通过参数名来传递值，提高代码的可读性和灵活性。