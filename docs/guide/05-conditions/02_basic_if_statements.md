# 基础if语句

## 概述

if语句是Python中最基本的条件控制结构，它允许程序根据条件的真假来决定是否执行特定的代码块。这是编程逻辑的基础，几乎所有的程序都会用到条件判断。

## 基本语法

```python
if condition:
    # 当条件为True时执行的代码
    statement1
    statement2
    ...
```

### 语法要点

1. **关键字**：使用`if`关键字开始条件语句
2. **条件表达式**：`condition`是一个返回布尔值（True或False）的表达式
3. **冒号**：条件后必须跟一个冒号`:`
4. **缩进**：条件成立时执行的代码必须缩进（通常使用4个空格）
5. **代码块**：所有缩进相同的语句组成一个代码块

## 基础示例

### 1. 简单的数值比较

```python
# 年龄判断
age = 18
if age >= 18:
    print("你已经成年了！")
    print("可以投票和工作")

# 分数判断
score = 85
if score >= 60:
    print("恭喜你，考试及格了！")

# 温度判断
temperature = 30
if temperature > 25:
    print("今天天气很热，记得多喝水")
```

### 2. 字符串条件判断

```python
# 用户名验证
username = "admin"
if username == "admin":
    print("管理员登录成功")
    print("欢迎使用管理系统")

# 密码长度检查
password = "mypassword123"
if len(password) >= 8:
    print("密码长度符合要求")

# 文件扩展名检查
filename = "document.pdf"
if filename.endswith(".pdf"):
    print("这是一个PDF文件")
```

### 3. 布尔值直接判断

```python
# 直接使用布尔变量
is_logged_in = True
if is_logged_in:
    print("用户已登录")
    print("显示用户面板")

# 函数返回值判断
def is_weekend():
    import datetime
    return datetime.datetime.now().weekday() >= 5

if is_weekend():
    print("今天是周末，好好休息！")
```

## 条件表达式详解

### 1. 比较运算符

```python
number = 42

# 等于
if number == 42:
    print("答案是42")

# 不等于
if number != 0:
    print("数字不是零")

# 大于
if number > 40:
    print("数字大于40")

# 小于
if number < 50:
    print("数字小于50")

# 大于等于
if number >= 42:
    print("数字大于等于42")

# 小于等于
if number <= 100:
    print("数字小于等于100")
```

### 2. 成员运算符

```python
# 检查元素是否在列表中
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("苹果在水果列表中")

# 检查字符是否在字符串中
text = "Hello World"
if "World" in text:
    print("找到了'World'")

# 检查键是否在字典中
user_info = {"name": "Alice", "age": 25}
if "name" in user_info:
    print(f"用户名是: {user_info['name']}")
```

### 3. 类型检查

```python
value = 42

# 检查数据类型
if isinstance(value, int):
    print("这是一个整数")

if isinstance(value, (int, float)):
    print("这是一个数字")

# 检查是否为None
data = None
if data is None:
    print("数据为空")
```

## 复杂条件表达式

### 1. 数学表达式

```python
x = 10
y = 5

# 使用数学运算的结果作为条件
if x + y > 10:
    print("x和y的和大于10")

if x % 2 == 0:
    print("x是偶数")

if abs(x - y) < 10:
    print("x和y的差的绝对值小于10")
```

### 2. 函数调用结果

```python
# 使用内置函数
text = "Hello"
if len(text) > 3:
    print("文本长度大于3")

if text.isupper():
    print("文本全是大写")
else:
    print("文本不全是大写")

# 使用自定义函数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 17
if is_prime(number):
    print(f"{number}是质数")
```

## 实际应用场景

### 1. 用户输入验证

```python
# 年龄验证
age_input = input("请输入您的年龄: ")
if age_input.isdigit():
    age = int(age_input)
    if age >= 0 and age <= 150:
        print(f"您的年龄是{age}岁")
        if age >= 18:
            print("您已成年")
        if age >= 65:
            print("您可以享受老年优惠")
    else:
        print("请输入有效的年龄（0-150）")
else:
    print("请输入数字")
```

### 2. 文件处理

```python
import os

filename = "data.txt"

# 检查文件是否存在
if os.path.exists(filename):
    print(f"文件{filename}存在")
    
    # 检查文件大小
    file_size = os.path.getsize(filename)
    if file_size > 0:
        print(f"文件大小: {file_size}字节")
    else:
        print("文件为空")
else:
    print(f"文件{filename}不存在")
```

### 3. 权限检查系统

```python
# 用户权限系统
user_role = "admin"
user_active = True
user_verified = True

if user_role == "admin":
    print("管理员权限")
    if user_active:
        print("账户状态：激活")
        if user_verified:
            print("账户已验证，可以访问所有功能")
        else:
            print("请先验证账户")
    else:
        print("账户已被禁用")
elif user_role == "user":
    print("普通用户权限")
else:
    print("未知用户角色")
```

## 常见错误和注意事项

### 1. 缩进错误

```python
# 错误示例
age = 20
if age >= 18:
print("成年了")  # 缺少缩进，会报错

# 正确示例
age = 20
if age >= 18:
    print("成年了")  # 正确的缩进
```

### 2. 条件表达式错误

```python
# 错误：使用赋值运算符而不是比较运算符
age = 18
if age = 18:  # 错误，应该使用 ==
    print("18岁")

# 正确
if age == 18:
    print("18岁")
```

### 3. 类型比较错误

```python
# 可能出现的问题
user_input = input("请输入数字: ")  # input()返回字符串
if user_input > 10:  # 字符串和数字比较可能不符合预期
    print("大于10")

# 正确的做法
user_input = input("请输入数字: ")
if user_input.isdigit() and int(user_input) > 10:
    print("大于10")
```

## 性能考虑

### 1. 条件顺序优化

```python
# 将最可能为真的条件放在前面
user_type = "regular"  # 大多数用户是普通用户

# 优化前
if user_type == "admin":
    print("管理员")
elif user_type == "vip":
    print("VIP用户")
elif user_type == "regular":
    print("普通用户")

# 优化后（将最常见的情况放在前面）
if user_type == "regular":
    print("普通用户")
elif user_type == "vip":
    print("VIP用户")
elif user_type == "admin":
    print("管理员")
```

### 2. 避免重复计算

```python
# 低效的写法
if len(some_list) > 0:
    print("列表不为空")
if len(some_list) > 10:
    print("列表很长")

# 高效的写法
list_length = len(some_list)
if list_length > 0:
    print("列表不为空")
if list_length > 10:
    print("列表很长")
```

## 练习题

### 基础练习

1. **年龄分类**：编写程序判断一个人的年龄段
   - 0-12岁：儿童
   - 13-17岁：青少年
   - 18-59岁：成年人
   - 60岁以上：老年人

2. **成绩等级**：根据分数判断等级
   - 90-100：优秀
   - 80-89：良好
   - 70-79：中等
   - 60-69：及格
   - 0-59：不及格

3. **密码强度检查**：检查密码是否满足以下条件
   - 长度至少8位
   - 包含大写字母
   - 包含小写字母
   - 包含数字

### 进阶练习

1. **BMI计算器**：根据身高体重计算BMI并给出健康建议
2. **文件类型识别**：根据文件扩展名判断文件类型
3. **简单计算器**：实现基本的四则运算，包含除零检查

## 学习要点

1. **语法掌握**：熟练掌握if语句的基本语法
2. **缩进规范**：严格遵守Python的缩进规则
3. **条件设计**：学会设计清晰、准确的条件表达式
4. **实际应用**：将条件判断应用到实际问题中
5. **错误避免**：了解常见错误并学会避免

通过掌握基础if语句，你已经具备了编写简单条件判断程序的能力。接下来可以学习if-else语句，进一步扩展条件控制的能力。