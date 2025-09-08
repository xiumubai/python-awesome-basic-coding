# 逻辑运算符

## 学习目标

- 掌握三种逻辑运算符的使用方法
- 理解逻辑运算符的短路求值特性
- 学会逻辑运算符与布尔值的转换
- 了解逻辑运算符的优先级和组合使用
- 掌握德摩根定律在逻辑运算中的应用

## 逻辑运算符概览

Python中有三种逻辑运算符：

| 运算符 | 名称 | 描述 | 示例 |
|--------|------|------|------|
| and | 逻辑与 | 两个操作数都为真时返回真 | True and False → False |
| or | 逻辑或 | 至少一个操作数为真时返回真 | True or False → True |
| not | 逻辑非 | 对操作数取反 | not True → False |

## 基本逻辑运算

### 布尔值的逻辑运算

```python
# and 运算符
print(f"True and True = {True and True}")      # True
print(f"True and False = {True and False}")    # False
print(f"False and True = {False and True}")    # False
print(f"False and False = {False and False}")  # False

# or 运算符
print(f"True or True = {True or True}")        # True
print(f"True or False = {True or False}")      # True
print(f"False or True = {False or True}")      # True
print(f"False or False = {False or False}")    # False

# not 运算符
print(f"not True = {not True}")                # False
print(f"not False = {not False}")              # True
```

### Python中的真值测试

Python中任何值都可以进行真值测试：

```python
# 假值（Falsy）
print(f"0 被视为: {bool(0)}")                    # False
print(f"空字符串被视为: {bool('')}")              # False
print(f"空列表被视为: {bool([])}")               # False
print(f"空字典被视为: {bool({})}")               # False
print(f"None 被视为: {bool(None)}")             # False

# 真值（Truthy）
print(f"非零数被视为: {bool(5)}")                # True
print(f"非空字符串被视为: {bool('hello')}")       # True
print(f"非空列表被视为: {bool([1, 2, 3])}")      # True
```

### 数值的逻辑运算

```python
a = 5
b = 0
c = 10

print(f"a = {a}, b = {b}, c = {c}")
print(f"a and b = {a and b}")  # 返回 0，因为 b 为假值
print(f"a and c = {a and c}")  # 返回 10，因为都为真值
print(f"a or b = {a or b}")    # 返回 5，因为 a 为真值
print(f"b or c = {b or c}")    # 返回 10，因为 b 为假值
```

## 短路求值

逻辑运算符具有短路求值特性，可以提高程序效率：

```python
def true_func():
    print("  true_func() 被调用")
    return True

def false_func():
    print("  false_func() 被调用")
    return False

# and 运算的短路求值
print("False and true_func():")
result1 = False and true_func()  # true_func() 不会被调用
print(f"结果: {result1}")

print("\nTrue and true_func():")
result2 = True and true_func()   # true_func() 会被调用
print(f"结果: {result2}")

# or 运算的短路求值
print("\nTrue or false_func():")
result3 = True or false_func()   # false_func() 不会被调用
print(f"结果: {result3}")

print("\nFalse or false_func():")
result4 = False or false_func()  # false_func() 会被调用
print(f"结果: {result4}")
```

## 逻辑运算符的优先级

逻辑运算符的优先级顺序：**not > and > or**

```python
x = True
y = False
z = True

print(f"x = {x}, y = {y}, z = {z}")

# 不使用括号
result1 = not x or y and z
print(f"not x or y and z = {result1}")
print(f"等价于: (not x) or (y and z) = {(not x) or (y and z)}")

# 使用括号改变优先级
result2 = not (x or y) and z
print(f"not (x or y) and z = {result2}")

result3 = not x or (y and z)
print(f"not x or (y and z) = {result3}")
```

## 实际应用示例

### 复杂条件判断

```python
age = 25
has_license = True
has_car = False

print(f"年龄: {age}, 有驾照: {has_license}, 有车: {has_car}")

# 可以开车的条件
can_drive = age >= 18 and has_license
print(f"可以开车: {can_drive}")

# 可以自己开车出行的条件
can_drive_alone = age >= 18 and has_license and has_car
print(f"可以自己开车出行: {can_drive_alone}")

# 可以出行的条件（开车或坐公交）
can_travel = can_drive_alone or age >= 16
print(f"可以出行: {can_travel}")
```

### 用户权限检查

```python
def check_permission(user_role, is_owner, is_admin):
    # 管理员或者是资源拥有者可以访问
    return is_admin or is_owner

# 测试示例
print("权限检查示例：")
print(f"普通用户访问自己的资源: {check_permission('user', True, False)}")
print(f"管理员访问任何资源: {check_permission('admin', False, True)}")
print(f"普通用户访问他人资源: {check_permission('user', False, False)}")
```

### 登录验证

```python
def validate_login(username, password, is_active):
    # 用户名和密码都正确，且账户激活
    return username and password and is_active

print("登录验证示例：")
print(f"正确用户名密码，账户激活: {validate_login('admin', 'password123', True)}")
print(f"正确用户名密码，账户未激活: {validate_login('admin', 'password123', False)}")
print(f"错误密码: {validate_login('admin', '', True)}")
```

### 默认值设置

```python
# 使用 or 进行默认值设置
name = ""
default_name = name or "匿名用户"
print(f"用户名: '{name}' -> 显示名: '{default_name}'")  # 匿名用户

name = "张三"
default_name = name or "匿名用户"
print(f"用户名: '{name}' -> 显示名: '{default_name}'")  # 张三
```

### 折扣计算系统

```python
def get_discount(is_member, age, purchase_amount):
    # 会员折扣
    member_discount = is_member and 0.1 or 0
    # 老年人折扣
    senior_discount = age >= 65 and 0.05 or 0
    # 大额购买折扣
    bulk_discount = purchase_amount >= 1000 and 0.05 or 0
    
    total_discount = member_discount + senior_discount + bulk_discount
    return min(total_discount, 0.3)  # 最大折扣30%

print("折扣计算示例：")
discount1 = get_discount(True, 70, 1200)
print(f"会员，70岁，购买1200元: 折扣 {discount1*100}%")

discount2 = get_discount(False, 30, 500)
print(f"非会员，30岁，购买500元: 折扣 {discount2*100}%")
```

## 德摩根定律

德摩根定律是逻辑运算中的重要规律：

```python
a = True
b = False

print(f"a = {a}, b = {b}")

# 德摩根第一定律：not (a and b) == (not a) or (not b)
print(f"not (a and b) = {not (a and b)}")
print(f"(not a) or (not b) = {(not a) or (not b)}")
print(f"两者相等: {not (a and b) == ((not a) or (not b))}")

# 德摩根第二定律：not (a or b) == (not a) and (not b)
print(f"\nnot (a or b) = {not (a or b)}")
print(f"(not a) and (not b) = {(not a) and (not b)}")
print(f"两者相等: {not (a or b) == ((not a) and (not b))}")
```

## 练习题

### 基础练习

判断以下表达式的结果：

```python
# 1. True and False or True
# 2. not True or False and True
# 3. (5 > 3) and (2 < 4)
# 4. not (10 == 10)
# 5. [] or [1, 2, 3]

# 答案
print(f"1. True and False or True = {True and False or True}")        # True
print(f"2. not True or False and True = {not True or False and True}")  # False
print(f"3. (5 > 3) and (2 < 4) = {(5 > 3) and (2 < 4)}")            # True
print(f"4. not (10 == 10) = {not (10 == 10)}")                      # False
print(f"5. [] or [1, 2, 3] = {[] or [1, 2, 3]}")                    # [1, 2, 3]
```

### 编程练习

1. **闰年判断**

```python
def is_leap_year(year):
    # 能被4整除且不能被100整除，或者能被400整除
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

test_years = [2000, 2004, 1900, 2024]
print("闰年判断：")
for year in test_years:
    result = is_leap_year(year)
    print(f"   {year} 年是闰年: {result}")
```

2. **输入验证**

```python
def validate_input(value, min_length=1, max_length=50, required=True):
    # 检查是否为空
    if required and not value:
        return False, "输入不能为空"
    
    # 检查长度
    if value and (len(value) < min_length or len(value) > max_length):
        return False, f"长度必须在 {min_length}-{max_length} 之间"
    
    return True, "输入有效"

test_inputs = ["", "a", "hello", "a" * 60]
print("输入验证：")
for inp in test_inputs:
    valid, message = validate_input(inp, 2, 20)
    print(f"   输入 '{inp}': {message}")
```

3. **权限控制系统**

```python
def check_access(user_role, resource_type, is_owner):
    # 管理员可以访问所有资源
    if user_role == "admin":
        return True
    
    # 普通用户只能访问自己的资源
    if user_role == "user" and is_owner:
        return True
    
    # 访客只能访问公共资源
    if user_role == "guest" and resource_type == "public":
        return True
    
    return False

access_tests = [
    ("admin", "private", False),
    ("user", "private", True),
    ("user", "private", False),
    ("guest", "public", False),
    ("guest", "private", False)
]

print("权限控制：")
for role, resource, owner in access_tests:
    access = check_access(role, resource, owner)
    print(f"   {role} 访问 {resource} 资源 (是否拥有: {owner}): {access}")
```

## 常见错误和注意事项

### 1. 优先级混淆

```python
# 错误理解
# not True or False and True
# 可能被理解为：not (True or False) and True

# 正确理解（按优先级）
# (not True) or (False and True)
result = not True or False and True  # False
print(f"not True or False and True = {result}")
```

### 2. 短路求值的副作用

```python
# 注意函数调用的副作用
def increment_counter():
    global counter
    counter += 1
    return True

counter = 0
result = True or increment_counter()  # increment_counter() 不会被调用
print(f"Counter: {counter}")  # 仍然是 0
```

### 3. 逻辑运算符返回值

```python
# 逻辑运算符返回的不一定是布尔值
result1 = "hello" and "world"  # 返回 "world"
result2 = "" or "default"      # 返回 "default"
result3 = 0 and 5              # 返回 0

print(f"'hello' and 'world' = {result1}")
print(f"'' or 'default' = {result2}")
print(f"0 and 5 = {result3}")
```

## 学习要点总结

1. **逻辑运算符类型**：and（与）、or（或）、not（非）
2. **短路求值**：可以提高程序效率，避免不必要的计算
3. **真值测试**：任何Python对象都可以进行真值测试
4. **优先级**：not > and > or，使用括号可以改变优先级
5. **德摩根定律**：逻辑运算的重要规律
6. **返回值**：逻辑运算符返回的是操作数本身，不一定是布尔值
7. **实际应用**：条件判断、权限控制、输入验证等场景

## 运行代码

```bash
cd 02-operators
python 03_logical_operators.py
```

通过本节学习，你应该能够熟练使用逻辑运算符，理解短路求值的特性，并能在实际编程中正确应用这些知识进行复杂的条件判断。