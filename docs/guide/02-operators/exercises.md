# 运算符综合练习

## 学习目标

通过本节的综合练习，你将能够：
- 熟练运用各种Python运算符
- 解决实际编程问题
- 理解运算符在不同场景下的应用
- 掌握运算符的最佳实践
- 提升代码的可读性和效率

## 练习概览

本章包含6个练习模块：
1. **基础运算练习** - 算术运算符的实际应用
2. **条件判断练习** - 比较运算符和逻辑判断
3. **逻辑运算练习** - 复杂条件的逻辑组合
4. **位运算应用** - 高效的位操作技巧
5. **综合应用题** - 多种运算符的综合运用
6. **挑战题** - 高级运算符应用

## 练习1：基础运算练习

### 题目1：计算器函数

实现一个支持多种运算的计算器：

```python
def calculator(a, b, operator):
    """
    实现一个简单的计算器函数
    支持 +, -, *, /, //, %, ** 运算
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "除数不能为0"
    elif operator == '//':
        return a // b if b != 0 else "除数不能为0"
    elif operator == '%':
        return a % b if b != 0 else "除数不能为0"
    elif operator == '**':
        return a ** b
    else:
        return "不支持的运算符"

# 测试计算器函数
test_cases = [
    (10, 3, '+'),   # 13
    (10, 3, '-'),   # 7
    (10, 3, '*'),   # 30
    (10, 3, '/'),   # 3.333...
    (10, 3, '//'),  # 3
    (10, 3, '%'),   # 1
    (2, 3, '**')    # 8
]

for a, b, op in test_cases:
    result = calculator(a, b, op)
    print(f"{a} {op} {b} = {result}")
```

### 题目2：温度转换器

实现摄氏度、华氏度、开尔文之间的转换：

```python
def temperature_converter(temp, from_unit, to_unit):
    """
    温度单位转换函数
    支持摄氏度(C)、华氏度(F)、开尔文(K)之间的转换
    """
    # 先转换为摄氏度
    if from_unit == 'F':
        celsius = (temp - 32) * 5 / 9
    elif from_unit == 'K':
        celsius = temp - 273.15
    else:  # from_unit == 'C'
        celsius = temp
    
    # 再从摄氏度转换为目标单位
    if to_unit == 'F':
        return celsius * 9 / 5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:  # to_unit == 'C'
        return celsius

# 测试温度转换
print(f"100°C = {temperature_converter(100, 'C', 'F'):.1f}°F")  # 212.0°F
print(f"32°F = {temperature_converter(32, 'F', 'C'):.1f}°C")    # 0.0°C
print(f"0°C = {temperature_converter(0, 'C', 'K'):.1f}K")       # 273.2K
```

## 练习2：条件判断练习

### 题目3：成绩等级判定

根据分数判定成绩等级：

```python
def grade_classifier(score):
    """
    根据分数判定成绩等级
    90-100: A
    80-89: B
    70-79: C
    60-69: D
    0-59: F
    """
    if not (0 <= score <= 100):
        return "无效分数"
    
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# 测试成绩等级判定
test_scores = [95, 85, 75, 65, 55, 105, -10]
for score in test_scores:
    grade = grade_classifier(score)
    print(f"分数 {score}: 等级 {grade}")
```

### 题目4：闰年判断

实现闰年判断逻辑：

```python
def is_leap_year(year):
    """
    判断是否为闰年
    闰年规则：
    1. 能被4整除但不能被100整除
    2. 或者能被400整除
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 测试闰年判断
test_years = [2000, 2004, 1900, 2020, 2021, 2024]
for year in test_years:
    is_leap = is_leap_year(year)
    print(f"{year}年: {'是' if is_leap else '不是'}闰年")
```

## 练习3：逻辑运算练习

### 题目5：用户权限检查

实现一个权限检查系统：

```python
def check_access(user_role, resource_level, is_authenticated):
    """
    检查用户是否有权限访问资源
    """
    # 必须先登录
    if not is_authenticated:
        return False, "用户未登录"
    
    # 管理员可以访问所有资源
    if user_role == 'admin':
        return True, "管理员权限"
    
    # 普通用户只能访问公开资源
    if user_role == 'user' and resource_level == 'public':
        return True, "用户权限"
    
    # VIP用户可以访问公开和VIP资源
    if user_role == 'vip' and resource_level in ['public', 'vip']:
        return True, "VIP权限"
    
    return False, "权限不足"

# 测试权限检查
access_tests = [
    ('admin', 'private', True),   # 允许 (管理员权限)
    ('user', 'public', True),     # 允许 (用户权限)
    ('user', 'private', True),    # 拒绝 (权限不足)
    ('vip', 'vip', True),         # 允许 (VIP权限)
    ('user', 'public', False),    # 拒绝 (用户未登录)
]

for role, level, auth in access_tests:
    can_access, reason = check_access(role, level, auth)
    status = "允许" if can_access else "拒绝"
    print(f"角色:{role}, 资源:{level}, 登录:{auth} -> {status} ({reason})")
```

### 题目6：数字范围检查

检查数字所在的范围：

```python
def number_range_check(num):
    """
    检查数字所在的范围
    """
    conditions = [
        (num > 0 and num <= 10, "正小数 (0-10]"),
        (num > 10 and num <= 100, "中等数 (10-100]"),
        (num > 100, "大数 (>100)"),
        (num == 0, "零"),
        (num < 0, "负数")
    ]
    
    for condition, description in conditions:
        if condition:
            return description
    
    return "未知范围"

# 测试数字范围检查
test_numbers = [5, 50, 150, 0, -10, 10, 100]
for num in test_numbers:
    range_desc = number_range_check(num)
    print(f"数字 {num}: {range_desc}")
```

## 练习4：位运算应用

### 题目7：权限系统（使用位运算）

使用位运算实现高效的权限管理：

```python
class PermissionSystem:
    """
    使用位运算实现的权限系统
    """
    # 权限常量
    READ = 1      # 0001
    WRITE = 2     # 0010
    EXECUTE = 4   # 0100
    DELETE = 8    # 1000
    
    def __init__(self):
        self.user_permissions = {}
    
    def grant_permission(self, user, permission):
        """授予权限"""
        if user not in self.user_permissions:
            self.user_permissions[user] = 0
        self.user_permissions[user] |= permission
    
    def revoke_permission(self, user, permission):
        """撤销权限"""
        if user in self.user_permissions:
            self.user_permissions[user] &= ~permission
    
    def has_permission(self, user, permission):
        """检查是否有权限"""
        if user not in self.user_permissions:
            return False
        return (self.user_permissions[user] & permission) == permission
    
    def get_permissions(self, user):
        """获取用户所有权限"""
        if user not in self.user_permissions:
            return []
        
        permissions = []
        user_perm = self.user_permissions[user]
        
        if user_perm & self.READ:
            permissions.append('READ')
        if user_perm & self.WRITE:
            permissions.append('WRITE')
        if user_perm & self.EXECUTE:
            permissions.append('EXECUTE')
        if user_perm & self.DELETE:
            permissions.append('DELETE')
        
        return permissions

# 测试权限系统
perm_sys = PermissionSystem()

# 授予权限
perm_sys.grant_permission('alice', PermissionSystem.READ)
perm_sys.grant_permission('alice', PermissionSystem.WRITE)
perm_sys.grant_permission('bob', PermissionSystem.READ | PermissionSystem.EXECUTE)

print(f"Alice的权限: {perm_sys.get_permissions('alice')}")
print(f"Bob的权限: {perm_sys.get_permissions('bob')}")

# 检查权限
print(f"Alice有读权限: {perm_sys.has_permission('alice', PermissionSystem.READ)}")
print(f"Alice有删除权限: {perm_sys.has_permission('alice', PermissionSystem.DELETE)}")
print(f"Bob有执行权限: {perm_sys.has_permission('bob', PermissionSystem.EXECUTE)}")
```

### 题目8：位运算技巧演示

展示常用的位运算技巧：

```python
def bit_operations_demo(num):
    """
    演示常用的位运算技巧
    """
    print(f"\n数字 {num} 的位运算操作：")
    print(f"二进制表示: {bin(num)}")
    
    # 检查是否为偶数
    is_even = (num & 1) == 0
    print(f"是否为偶数: {is_even}")
    
    # 乘以2（左移1位）
    multiply_by_2 = num << 1
    print(f"乘以2: {multiply_by_2}")
    
    # 除以2（右移1位）
    divide_by_2 = num >> 1
    print(f"除以2: {divide_by_2}")
    
    # 获取最低位
    lowest_bit = num & 1
    print(f"最低位: {lowest_bit}")
    
    # 清除最低位的1
    clear_lowest_1 = num & (num - 1)
    print(f"清除最低位的1: {clear_lowest_1}")
    
    # 获取最低位的1
    get_lowest_1 = num & (-num)
    print(f"获取最低位的1: {get_lowest_1}")

# 测试位运算技巧
for test_num in [12, 7, 16]:
    bit_operations_demo(test_num)
```

## 练习5：综合应用题

### 题目9：购物车计算器

实现一个完整的购物车系统：

```python
class ShoppingCart:
    """
    购物车类，演示多种运算符的综合应用
    """
    def __init__(self):
        self.items = []  # 商品列表
        self.discount_rate = 0  # 折扣率
        self.tax_rate = 0.1  # 税率10%
    
    def add_item(self, name, price, quantity=1):
        """添加商品"""
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    def remove_item(self, name):
        """移除商品"""
        self.items = [item for item in self.items if item['name'] != name]
    
    def set_discount(self, rate):
        """设置折扣率"""
        self.discount_rate = rate if 0 <= rate <= 1 else 0
    
    def calculate_subtotal(self):
        """计算小计"""
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def calculate_discount(self):
        """计算折扣金额"""
        return self.calculate_subtotal() * self.discount_rate
    
    def calculate_tax(self):
        """计算税额"""
        discounted_amount = self.calculate_subtotal() - self.calculate_discount()
        return discounted_amount * self.tax_rate
    
    def calculate_total(self):
        """计算总金额"""
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        tax = self.calculate_tax()
        return subtotal - discount + tax
    
    def get_summary(self):
        """获取购物车摘要"""
        if not self.items:
            return "购物车为空"
        
        summary = "购物车摘要:\n"
        summary += "-" * 40 + "\n"
        
        for item in self.items:
            total_price = item['price'] * item['quantity']
            summary += f"{item['name']}: ${item['price']:.2f} x {item['quantity']} = ${total_price:.2f}\n"
        
        summary += "-" * 40 + "\n"
        summary += f"小计: ${self.calculate_subtotal():.2f}\n"
        
        if self.discount_rate > 0:
            summary += f"折扣 ({self.discount_rate*100:.0f}%): -${self.calculate_discount():.2f}\n"
        
        summary += f"税费 ({self.tax_rate*100:.0f}%): ${self.calculate_tax():.2f}\n"
        summary += f"总计: ${self.calculate_total():.2f}\n"
        
        return summary

# 测试购物车
cart = ShoppingCart()

# 添加商品
cart.add_item("苹果", 2.50, 3)
cart.add_item("香蕉", 1.20, 5)
cart.add_item("牛奶", 3.80, 2)

# 设置折扣
cart.set_discount(0.1)  # 10%折扣

print(cart.get_summary())
```

### 题目10：数学表达式求值器

实现一个简单的表达式求值器：

```python
def evaluate_expression(expression):
    """
    简单的数学表达式求值器
    支持 +, -, *, /, (, ) 运算符
    注意：这是一个简化版本，实际应用中应使用更安全的方法
    """
    try:
        # 移除空格
        expression = expression.replace(' ', '')
        
        # 检查表达式是否只包含允许的字符
        allowed_chars = set('0123456789+-*/().')
        if not all(c in allowed_chars for c in expression):
            return "表达式包含非法字符"
        
        # 使用eval计算（注意：在实际应用中应避免使用eval）
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "除零错误"
    except Exception as e:
        return f"表达式错误: {str(e)}"

# 测试表达式求值
expressions = [
    "2 + 3 * 4",        # 14
    "(2 + 3) * 4",      # 20
    "10 / 2 + 3",       # 8.0
    "2 ** 3 + 1",       # 9
    "10 / 0",           # 除零错误
    "2 + 3 * (4 - 1)"   # 11
]

for expr in expressions:
    result = evaluate_expression(expr)
    print(f"{expr} = {result}")
```

## 练习6：挑战题

### 题目11：复数运算器

实现复数的基本运算：

```python
class ComplexCalculator:
    """
    复数运算器，演示运算符重载的概念
    """
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"
    
    def add(self, other):
        """复数加法"""
        return ComplexCalculator(
            self.real + other.real,
            self.imag + other.imag
        )
    
    def subtract(self, other):
        """复数减法"""
        return ComplexCalculator(
            self.real - other.real,
            self.imag - other.imag
        )
    
    def multiply(self, other):
        """复数乘法"""
        # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexCalculator(real_part, imag_part)
    
    def magnitude(self):
        """计算复数的模"""
        return (self.real ** 2 + self.imag ** 2) ** 0.5

# 测试复数运算
c1 = ComplexCalculator(3, 4)
c2 = ComplexCalculator(1, -2)

print(f"c1 = {c1}")                    # 3 + 4i
print(f"c2 = {c2}")                    # 1 - 2i
print(f"c1 + c2 = {c1.add(c2)}")       # 4 + 2i
print(f"c1 - c2 = {c1.subtract(c2)}")  # 2 + 6i
print(f"c1 * c2 = {c1.multiply(c2)}")  # 11 - 2i
print(f"|c1| = {c1.magnitude():.2f}")   # 5.00
print(f"|c2| = {c2.magnitude():.2f}")   # 2.24
```

### 题目12：位运算实现加法

不使用+运算符实现加法：

```python
def add_without_plus(a, b):
    """
    不使用+运算符实现加法（使用位运算）
    """
    while b != 0:
        # 计算进位
        carry = a & b
        
        # 计算不带进位的和
        a = a ^ b
        
        # 进位左移一位
        b = carry << 1
    
    return a

# 测试位运算加法
test_pairs = [(5, 3), (15, 7), (100, 25), (-5, 3)]
for x, y in test_pairs:
    result = add_without_plus(x, y)
    print(f"{x} + {y} = {result} (验证: {x + y})")
```

## 练习答案解析

### 关键知识点

1. **算术运算符应用**：
   - 温度转换中的公式计算
   - 购物车中的价格计算
   - 复数运算中的数学公式

2. **比较运算符技巧**：
   - 成绩等级的范围判断
   - 闰年的复合条件判断
   - 数字范围的多条件检查

3. **逻辑运算符组合**：
   - 权限检查的多重条件
   - 短路求值的性能优化
   - 复杂业务逻辑的实现

4. **位运算符优势**：
   - 权限系统的高效实现
   - 数学运算的底层优化
   - 状态标志的紧凑存储

### 性能优化技巧

1. **位运算优化**：
   ```python
   # 检查偶数：使用位运算比取模更快
   is_even = (num & 1) == 0  # 快
   is_even = num % 2 == 0    # 慢
   
   # 乘除2的幂：使用位移比乘除更快
   result = num << 1   # num * 2，快
   result = num * 2    # 慢
   ```

2. **短路求值**：
   ```python
   # 利用短路求值避免不必要的计算
   if user.is_authenticated() and user.has_permission('read'):
       # 如果用户未认证，不会检查权限
       pass
   ```

3. **运算符优先级**：
   ```python
   # 合理利用优先级减少括号
   result = a + b * c    # 清晰
   result = a + (b * c)  # 冗余的括号
   ```

## 常见错误和注意事项

### 1. 浮点数比较

```python
# 错误：直接比较浮点数
if 0.1 + 0.2 == 0.3:
    print("相等")
else:
    print("不相等")  # 实际输出

# 正确：使用精度比较
def float_equal(a, b, precision=1e-9):
    return abs(a - b) < precision

if float_equal(0.1 + 0.2, 0.3):
    print("相等")  # 正确输出
```

### 2. 整数除法陷阱

```python
# Python 3中的除法
result = 5 / 2    # 2.5 (浮点除法)
result = 5 // 2   # 2 (整数除法)

# 注意负数的整数除法
result = -5 // 2  # -3 (向下取整)
result = -5 / 2   # -2.5
```

### 3. 位运算的符号问题

```python
# 注意负数的位运算
num = -5
print(bin(num))        # -0b101
print(num >> 1)        # -3 (算术右移)
print(num & 0xFF)      # 251 (与掩码运算)
```

## 思考题

1. **为什么位运算在某些场景下比普通运算更高效？**
   - 位运算直接操作二进制位，是CPU的基本操作
   - 避免了复杂的算术逻辑单元计算
   - 特别适合2的幂次运算和标志位操作

2. **什么时候应该使用 is 而不是 == ？**
   - `is` 比较对象身份（内存地址）
   - `==` 比较对象值
   - 对于 None、True、False 等单例对象使用 `is`
   - 对于数值、字符串等使用 `==`

3. **如何利用运算符优先级写出更简洁的代码？**
   - 了解常用运算符的优先级
   - 在不影响可读性的前提下减少括号
   - 复杂表达式仍应使用括号明确意图

4. **在实际项目中，哪些运算符使用频率最高？**
   - 算术运算符：`+`, `-`, `*`, `/`
   - 比较运算符：`==`, `!=`, `<`, `>`
   - 逻辑运算符：`and`, `or`, `not`
   - 赋值运算符：`=`, `+=`, `-=`
   - 成员运算符：`in`, `not in`

5. **如何避免运算符优先级导致的逻辑错误？**
   - 使用括号明确运算顺序
   - 将复杂表达式分解为多个简单表达式
   - 编写单元测试验证逻辑正确性
   - 代码审查时重点关注复杂表达式

## 挑战练习

### 1. 高级计算器

实现一个支持复杂表达式的计算器，包括：
- 括号优先级处理
- 函数调用（sin, cos, sqrt等）
- 变量支持
- 错误处理

### 2. 位运算加密

使用位运算实现简单的加密算法：
- XOR加密/解密
- 位移密码
- 组合多种位运算

### 3. 权限管理系统

设计一个完整的权限管理系统：
- 角色继承
- 权限组合
- 动态权限检查
- 性能优化

### 4. 浮点数比较工具

编写一个函数，智能判断两个浮点数是否"相等"：
- 自动选择合适的精度
- 处理特殊值（NaN, Infinity）
- 相对误差和绝对误差

### 5. 自定义比较类

实现一个自定义类，重载所有比较运算符：
- 支持多维比较
- 自定义排序规则
- 性能优化

## 学习总结

通过这些综合练习，你应该已经掌握了：

1. **运算符的实际应用**：
   - 在不同场景下选择合适的运算符
   - 理解各种运算符的性能特点
   - 掌握运算符的最佳实践

2. **问题解决能力**：
   - 将复杂问题分解为简单的运算
   - 使用运算符实现高效的算法
   - 处理边界条件和异常情况

3. **代码质量意识**：
   - 编写可读性强的表达式
   - 合理使用括号和空格
   - 添加必要的注释和文档

4. **性能优化技巧**：
   - 利用位运算提高效率
   - 使用短路求值避免不必要计算
   - 选择合适的数据类型和算法

继续练习和探索，你将能够更加熟练地运用Python的各种运算符，编写出高效、优雅的代码！