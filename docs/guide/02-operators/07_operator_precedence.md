# 运算符优先级和结合性

## 学习目标

通过本节学习，你将掌握：
- Python运算符的优先级顺序
- 运算符的结合性（左结合、右结合）
- 使用括号改变运算顺序
- 避免因优先级导致的常见错误
- 提高代码可读性的技巧

## Python运算符优先级表

以下是Python运算符的优先级表（从高到低）：

| 优先级 | 运算符 | 名称 | 描述 |
|--------|--------|------|------|
| 1 | `()` | 括号 | 最高优先级 |
| 2 | `**` | 幂运算 | 右结合 |
| 3 | `+x, -x, ~x` | 一元运算符 | 正号、负号、按位取反 |
| 4 | `*, /, //, %` | 乘除运算 | 乘法、除法、整除、取模 |
| 5 | `+, -` | 加减运算 | 加法、减法 |
| 6 | `<<, >>` | 位移运算 | 左移、右移 |
| 7 | `&` | 按位与 | 位运算 |
| 8 | `^` | 按位异或 | 位运算 |
| 9 | `|` | 按位或 | 位运算 |
| 10 | `==, !=, <, >, <=, >=, is, is not, in, not in` | 比较运算 | 比较和成员运算 |
| 11 | `not` | 逻辑非 | 布尔运算 |
| 12 | `and` | 逻辑与 | 布尔运算 |
| 13 | `or` | 逻辑或 | 布尔运算 |
| 14 | `=, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, <<=, >>=` | 赋值运算 | 最低优先级 |

## 基本优先级示例

### 算术运算优先级

```python
# 乘法优先于加法
result = 2 + 3 * 4
print(result)  # 14 (先计算 3 * 4 = 12，再计算 2 + 12 = 14)

# 使用括号改变优先级
result = (2 + 3) * 4
print(result)  # 20 (先计算 2 + 3 = 5，再计算 5 * 4 = 20)

# 除法优先于减法
result = 10 - 6 / 2
print(result)  # 7.0 (先计算 6 / 2 = 3.0，再计算 10 - 3.0 = 7.0)

# 使用括号改变优先级
result = (10 - 6) / 2
print(result)  # 2.0 (先计算 10 - 6 = 4，再计算 4 / 2 = 2.0)
```

### 幂运算的右结合性

```python
# 幂运算是右结合的
result = 2 ** 3 ** 2
print(result)  # 512 (等价于 2 ** (3 ** 2) = 2 ** 9 = 512)

# 使用括号改变结合性
result = (2 ** 3) ** 2
print(result)  # 64 (先计算 2 ** 3 = 8，再计算 8 ** 2 = 64)
```

## 比较运算符的链式使用

```python
x = 5

# 链式比较
result = 1 < x < 10
print(result)  # True (等价于 (1 < x) and (x < 10))

result = 10 > x > 0
print(result)  # True (等价于 (10 > x) and (x > 0))

result = x == 5 == 5
print(result)  # True (等价于 (x == 5) and (5 == 5))

# 注意：链式比较可能产生意外结果
result = False == False in [False, True]
print(result)  # True
# 解释: 等价于 (False == False) and (False in [False, True])
#       = True and True = True
```

## 逻辑运算符优先级

逻辑运算符的优先级顺序：`not` > `and` > `or`

```python
# not 优先级最高
result = not True and False or True
print(result)  # True
# 计算过程: (not True) and False or True
#          = False and False or True
#          = False or True
#          = True

# and 优先于 or
result = True or False and False
print(result)  # True
# 计算过程: True or (False and False)
#          = True or False
#          = True

# 使用括号明确优先级
result = (True or False) and False
print(result)  # False
```

## 位运算符优先级

位运算符的优先级顺序：`&` > `^` > `|`

```python
a, b, c = 12, 10, 6  # 二进制: 1100, 1010, 0110

# & 优先于 |
result = a | b & c
print(result)  # 12
# 计算过程: a | (b & c)
#          = 12 | (10 & 6)
#          = 12 | 2
#          = 14 (但实际结果是12，因为 12 | 2 = 14)

# & 优先于 ^
result = a ^ b & c
print(result)  # 14
# 计算过程: a ^ (b & c)
#          = 12 ^ (10 & 6)
#          = 12 ^ 2
#          = 14
```

## 混合运算符优先级

```python
# 复杂表达式示例
result = 2 + 3 * 4 > 10 and not False
print(result)  # True

# 计算过程:
# 1. 3 * 4 = 12 (乘法优先级最高)
# 2. 2 + 12 = 14 (加法)
# 3. 14 > 10 = True (比较)
# 4. not False = True (逻辑非)
# 5. True and True = True (逻辑与)

# 位移运算示例
result = 5 << 1 + 1
print(result)  # 20
# 计算过程:
# 1. 1 + 1 = 2 (加法优先于位移)
# 2. 5 << 2 = 20 (左移)
```

## 常见的优先级陷阱

### 陷阱1：位运算与比较运算

```python
x = 5

# 错误的写法
result_wrong = x & 1 == 1  # 这会被解释为 x & (1 == 1)
print(result_wrong)  # 1 (因为 x & True = x & 1 = 1)

# 正确的写法
result_correct = (x & 1) == 1
print(result_correct)  # True (先位运算再比较)
```

### 陷阱2：逻辑运算与比较运算

```python
a, b = 5, 10

# 正确的写法
result = a < b and b < 15
print(result)  # True

# 错误的写法（语法错误）
# result = a < b and < 15  # SyntaxError

# 正确的链式比较
result = a < b < 15
print(result)  # True
```

### 陷阱3：赋值运算符的优先级

```python
x, y = 10, 5

# 正确的写法
z = x + y
print(z)  # 15

# 错误的写法（语法错误）
# z = x + y = 15  # SyntaxError
```

## 使用括号提高可读性

即使了解优先级，使用括号也能提高代码可读性：

```python
# 不清晰的表达式
result1 = 2 + 3 * 4 ** 2 / 8 - 1
print(result1)  # 7.0

# 清晰的表达式
result2 = 2 + ((3 * (4 ** 2)) / 8) - 1
print(result2)  # 7.0
print(f"结果相同: {result1 == result2}")  # True

# 复杂条件判断
age = 25
income = 50000
has_job = True

# 不清晰
eligible1 = age >= 18 and age <= 65 and income > 30000 or has_job and age > 21

# 清晰
eligible2 = ((age >= 18) and (age <= 65) and (income > 30000)) or (has_job and (age > 21))

print(f"结果相同: {eligible1 == eligible2}")  # True
```

## 实际应用示例

### 数学公式计算

```python
def quadratic_formula(a, b, c):
    """求解二次方程 ax² + bx + c = 0"""
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None  # 无实数解
    
    sqrt_discriminant = discriminant ** 0.5
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    return x1, x2

# 求解 x² - 5x + 6 = 0
x1, x2 = quadratic_formula(1, -5, 6)
print(f"解: x1 = {x1}, x2 = {x2}")  # 解: x1 = 3.0, x2 = 2.0

# 验证解的正确性
def verify_solution(a, b, c, x):
    return a * x ** 2 + b * x + c

print(f"验证 x1: {verify_solution(1, -5, 6, x1)}")  # 0.0
print(f"验证 x2: {verify_solution(1, -5, 6, x2)}")  # 0.0
```

### 折扣计算系统

```python
def calculate_discount(price, is_member, quantity):
    """计算折扣价格"""
    # 会员折扣10%，批量购买(>=10)额外5%
    base_discount = 0.1 if is_member else 0.0
    quantity_discount = 0.05 if quantity >= 10 else 0.0
    total_discount = base_discount + quantity_discount
    
    # 确保折扣不超过20%
    total_discount = min(total_discount, 0.2)
    
    return price * (1 - total_discount)

# 测试不同情况
test_cases = [
    (100, True, 5),   # 会员，少量购买
    (100, True, 15),  # 会员，批量购买
    (100, False, 15), # 非会员，批量购买
    (100, False, 5),  # 非会员，少量购买
]

for price, is_member, quantity in test_cases:
    final_price = calculate_discount(price, is_member, quantity)
    member_str = "会员" if is_member else "非会员"
    print(f"原价¥{price}, {member_str}, {quantity}件 -> 最终价格¥{final_price:.2f}")
```

## 练习题

### 基础练习

计算以下表达式的结果（不使用Python计算器）：

```python
# 1. 2 + 3 * 4 ** 2
# 2. 10 - 6 / 2 + 1
# 3. True or False and False
# 4. not False and True or False
# 5. 5 & 3 | 1
# 6. 2 ** 3 ** 2
# 7. 1 < 2 == True
# 8. 3 + 4 > 5 and 2 * 3 == 6
```

**答案和解析：**

1. `2 + 3 * 4 ** 2 = 50`
   - 解析: `2 + 3 * (4 ** 2) = 2 + 3 * 16 = 2 + 48 = 50`

2. `10 - 6 / 2 + 1 = 8.0`
   - 解析: `10 - (6 / 2) + 1 = 10 - 3 + 1 = 8`

3. `True or False and False = True`
   - 解析: `True or (False and False) = True or False = True`

4. `not False and True or False = True`
   - 解析: `(not False) and True or False = True and True or False = True`

5. `5 & 3 | 1 = 1`
   - 解析: `(5 & 3) | 1 = 1 | 1 = 1`

6. `2 ** 3 ** 2 = 512`
   - 解析: `2 ** (3 ** 2) = 2 ** 9 = 512` (右结合)

7. `1 < 2 == True = False`
   - 解析: `(1 < 2) and (2 == True) = True and False = False`

8. `3 + 4 > 5 and 2 * 3 == 6 = True`
   - 解析: `(3 + 4 > 5) and (2 * 3 == 6) = (7 > 5) and (6 == 6) = True and True = True`

### 编程练习

1. **复合利息计算**：编写一个函数，正确计算复合利息

```python
def compound_interest(principal, rate, time, compound_frequency=1):
    """
    计算复合利息
    principal: 本金
    rate: 年利率（小数形式，如0.05表示5%）
    time: 时间（年）
    compound_frequency: 每年复利次数
    """
    # 使用正确的优先级：先除法，再加法，最后幂运算
    amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    interest = amount - principal
    return amount, interest

# 测试
principal = 10000  # 本金1万元
rate = 0.05       # 年利率5%
time = 10         # 10年

# 不同复利频率的比较
frequencies = [(1, "年"), (4, "季"), (12, "月"), (365, "日")]

for freq, name in frequencies:
    amount, interest = compound_interest(principal, rate, time, freq)
    print(f"{name}复利: 最终金额¥{amount:.2f}, 利息¥{interest:.2f}")
```

2. **表达式求值器**：实现一个简化的表达式求值器

```python
def simple_evaluator(expression):
    """
    简化的表达式求值器（仅支持基本算术运算）
    注意：这是教学示例，实际应用中应使用更安全的方法
    """
    # 移除空格
    expr = expression.replace(" ", "")
    
    # 检查是否只包含允许的字符
    allowed_chars = set('0123456789+-*/().')
    if not all(c in allowed_chars for c in expr):
        return "错误: 包含不允许的字符"
    
    # 检查括号匹配
    if not is_balanced_parentheses(expr):
        return "错误: 括号不匹配"
    
    try:
        # 注意：eval在实际应用中有安全风险，这里仅作教学演示
        result = eval(expr)
        return result
    except Exception as e:
        return f"错误: {e}"

def is_balanced_parentheses(expression):
    """检查括号是否匹配"""
    count = 0
    for char in expression:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:  # 右括号多于左括号
                return False
    return count == 0  # 左右括号数量相等

# 测试
test_expressions = [
    "2 + 3 * 4",
    "(2 + 3) * 4",
    "10 / (2 + 3)",
    "2 ** 3 + 1",
    "((1 + 2) * 3) / 2",
    "2 + 3 * (4 - 1",  # 括号不匹配
    "2 + abc",         # 包含字母
]

for expr in test_expressions:
    result = simple_evaluator(expr)
    print(f"'{expr}' = {result}")
```

3. **括号匹配验证**：编写一个函数验证括号匹配

```python
def validate_parentheses_detailed(expression):
    """
    详细的括号匹配验证
    返回是否匹配以及详细信息
    """
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for i, char in enumerate(expression):
        if char in pairs:  # 左括号
            stack.append((char, i))
        elif char in pairs.values():  # 右括号
            if not stack:
                return False, f"位置{i}: 多余的右括号 '{char}'"
            
            left_char, left_pos = stack.pop()
            if pairs[left_char] != char:
                return False, f"位置{i}: 括号类型不匹配 '{left_char}' 和 '{char}'"
    
    if stack:
        left_char, left_pos = stack[-1]
        return False, f"位置{left_pos}: 未匹配的左括号 '{left_char}'"
    
    return True, "括号匹配正确"

# 测试
test_brackets = [
    "(1 + 2) * 3",
    "[(1 + 2) * 3]",
    "{[(1 + 2) * 3]}",
    "(1 + 2] * 3",
    "((1 + 2) * 3",
    "(1 + 2)) * 3",
    "",
    "no brackets here"
]

for expr in test_brackets:
    is_valid, message = validate_parentheses_detailed(expr)
    status = "✓" if is_valid else "✗"
    print(f"{status} '{expr}': {message}")
```

## 常见错误和注意事项

### 1. 不了解运算符优先级

```python
# 错误：不知道乘法优先于加法
result = 2 + 3 * 4  # 可能误以为是 (2 + 3) * 4 = 20
print(result)  # 实际是 14

# 正确：明确使用括号
result = (2 + 3) * 4  # 如果确实想要这个结果
print(result)  # 20
```

### 2. 混淆 is 和 == 的优先级

```python
# 错误：可能产生意外结果
result = 1 == 1 is True
print(result)  # False，因为等价于 (1 == 1) and (1 is True)

# 正确：明确意图
result = (1 == 1) and (1 is True)
print(result)  # False
```

### 3. 位运算符优先级陷阱

```python
# 错误：位运算符优先级低于比较运算符
if x & mask == 0:  # 实际是 x & (mask == 0)
    print("错误的逻辑")

# 正确：使用括号
if (x & mask) == 0:
    print("正确的逻辑")
```

## 学习要点总结

1. **优先级记忆**：
   - 括号具有最高优先级
   - 算术运算符优先于比较运算符
   - 比较运算符优先于逻辑运算符
   - 赋值运算符优先级最低

2. **结合性**：
   - 大多数运算符是左结合的
   - 幂运算符（**）是右结合的
   - 赋值运算符是右结合的

3. **最佳实践**：
   - 使用括号明确运算顺序
   - 不要依赖复杂的优先级规则
   - 优先考虑代码可读性
   - 避免在一个表达式中使用过多运算符

4. **常见陷阱**：
   - 位运算符与比较运算符的优先级
   - 链式比较的特殊行为
   - 逻辑运算符的短路求值

5. **调试技巧**：
   - 使用括号分解复杂表达式
   - 逐步计算验证结果
   - 利用Python的交互式环境测试

掌握运算符优先级和结合性对于编写正确、可读的Python代码至关重要。