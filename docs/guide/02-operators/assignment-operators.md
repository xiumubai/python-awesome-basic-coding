# 赋值运算符

## 学习目标

通过本节学习，你将掌握：
- 基本赋值运算符的使用
- 复合赋值运算符的便利性
- 多重赋值和解包赋值的技巧
- 赋值运算符的注意事项和性能考虑

## 赋值运算符概览

Python中的赋值运算符用于给变量赋值，包括：

| 运算符 | 名称 | 示例 | 等价形式 |
|--------|------|------|----------|
| = | 基本赋值 | x = 5 | - |
| += | 加法赋值 | x += 3 | x = x + 3 |
| -= | 减法赋值 | x -= 2 | x = x - 2 |
| *= | 乘法赋值 | x *= 4 | x = x * 4 |
| /= | 除法赋值 | x /= 2 | x = x / 2 |
| //= | 整除赋值 | x //= 3 | x = x // 3 |
| %= | 取模赋值 | x %= 5 | x = x % 5 |
| **= | 幂运算赋值 | x **= 2 | x = x ** 2 |
| &= | 按位与赋值 | x &= y | x = x & y |
| \|= | 按位或赋值 | x \|= y | x = x \| y |
| ^= | 按位异或赋值 | x ^= y | x = x ^ y |
| <<= | 左移赋值 | x <<= 2 | x = x << 2 |
| >>= | 右移赋值 | x >>= 1 | x = x >> 1 |

## 基本赋值运算符

### 简单赋值

```python
# 基本赋值
x = 10
y = 20
name = "Python"
is_valid = True

print(f"x = {x}")
print(f"y = {y}")
print(f"name = '{name}'")
print(f"is_valid = {is_valid}")

# 变量重新赋值
x = 30
print(f"x 重新赋值后: {x}")
```

## 复合赋值运算符

### 算术复合赋值

```python
a = 10
print(f"初始值 a = {a}")

a += 5  # 等价于 a = a + 5
print(f"a += 5 后: a = {a}")  # 15

a -= 3  # 等价于 a = a - 3
print(f"a -= 3 后: a = {a}")  # 12

a *= 2  # 等价于 a = a * 2
print(f"a *= 2 后: a = {a}")  # 24

a /= 4  # 等价于 a = a / 4
print(f"a /= 4 后: a = {a}")  # 6.0

a //= 2  # 等价于 a = a // 2
print(f"a //= 2 后: a = {a}")  # 3.0

a %= 3  # 等价于 a = a % 3
print(f"a %= 3 后: a = {a}")  # 0.0

a = 2
a **= 3  # 等价于 a = a ** 3
print(f"a **= 3 后: a = {a}")  # 8
```

### 字符串和列表的复合赋值

```python
# 字符串复合赋值
text = "Hello"
print(f"初始字符串: '{text}'")

text += " World"  # 字符串连接
print(f"text += ' World' 后: '{text}'")  # Hello World

text *= 2  # 字符串重复
print(f"text *= 2 后: '{text}'")  # Hello WorldHello World

# 列表复合赋值
numbers = [1, 2, 3]
print(f"初始列表: {numbers}")

numbers += [4, 5]  # 列表扩展
print(f"numbers += [4, 5] 后: {numbers}")  # [1, 2, 3, 4, 5]

numbers *= 2  # 列表重复
print(f"numbers *= 2 后: {numbers}")  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
```

## 多重赋值

### 同时赋值

```python
# 同时给多个变量赋相同值
x = y = z = 100
print(f"x = y = z = 100: x={x}, y={y}, z={z}")

# 修改其中一个变量
x = 200
print(f"x = 200 后: x={x}, y={y}, z={z}")  # x=200, y=100, z=100
```

### 可变对象的陷阱

```python
# 注意：可变对象的多重赋值陷阱
list_a = list_b = [1, 2, 3]  # 两个变量指向同一个列表
print(f"初始: list_a={list_a}, list_b={list_b}")

list_a.append(4)  # 修改列表
print(f"list_a.append(4) 后: list_a={list_a}, list_b={list_b}")
# 输出：list_a=[1, 2, 3, 4], list_b=[1, 2, 3, 4]

# 正确的方式：创建独立的列表
list_c = [1, 2, 3]
list_d = [1, 2, 3]  # 或者 list_d = list_c.copy()
print(f"独立列表: list_c={list_c}, list_d={list_d}")

list_c.append(4)
print(f"list_c.append(4) 后: list_c={list_c}, list_d={list_d}")
# 输出：list_c=[1, 2, 3, 4], list_d=[1, 2, 3]
```

## 解包赋值

### 基本解包

```python
# 元组解包
point = (3, 4)
x, y = point
print(f"点坐标 {point} 解包: x={x}, y={y}")

# 列表解包
colors = ['red', 'green', 'blue']
color1, color2, color3 = colors
print(f"颜色列表 {colors} 解包: {color1}, {color2}, {color3}")

# 变量交换
a, b = 10, 20
print(f"交换前: a={a}, b={b}")
a, b = b, a  # 优雅的变量交换
print(f"交换后: a={a}, b={b}")
```

### 扩展解包

```python
# 扩展解包（Python 3.0+）
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"扩展解包 {numbers}:")
print(f"first={first}, middle={middle}, last={last}")
# 输出：first=1, middle=[2, 3, 4], last=5

# 忽略不需要的值
data = ('Alice', 25, 'Engineer', 'New York')
name, age, _, city = data  # 使用 _ 忽略职业
print(f"忽略部分值: name={name}, age={age}, city={city}")
```

## 位赋值运算符

```python
# 位运算复合赋值
num = 12  # 二进制: 1100
print(f"初始值 num = {num} (二进制: {bin(num)})")

num &= 10  # 按位与，10的二进制是1010
print(f"num &= 10 后: {num} (二进制: {bin(num)})")  # 8 (1000)

num |= 5   # 按位或，5的二进制是101
print(f"num |= 5 后: {num} (二进制: {bin(num)})")   # 13 (1101)

num ^= 3   # 按位异或，3的二进制是11
print(f"num ^= 3 后: {num} (二进制: {bin(num)})")   # 14 (1110)

num <<= 2  # 左移2位
print(f"num <<= 2 后: {num} (二进制: {bin(num)})")  # 56 (111000)

num >>= 1  # 右移1位
print(f"num >>= 1 后: {num} (二进制: {bin(num)})")  # 28 (11100)
```

## 实际应用示例

### 计数器和累加器

```python
# 计数器
counter = 0
items = ['apple', 'banana', 'cherry', 'date']

for item in items:
    counter += 1
    print(f"处理第 {counter} 个项目: {item}")

# 累加器
total = 0
prices = [10.5, 25.0, 15.75, 8.25]

for price in prices:
    total += price
    print(f"当前总价: {total:.2f}")
```

### 字符串构建

```python
message = ""
words = ['Hello', 'beautiful', 'world']

for word in words:
    if message:  # 如果不是第一个词，添加空格
        message += " "
    message += word
    print(f"当前消息: '{message}'")
```

### 银行账户示例

```python
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("余额不足")
            return self.balance
    
    def get_balance(self):
        return self.balance

# 使用示例
account = BankAccount(1000)
print(f"初始余额: {account.get_balance()}")
account.deposit(500)
print(f"存款500后: {account.get_balance()}")
account.withdraw(200)
print(f"取款200后: {account.get_balance()}")
```

## 练习题

### 基础练习

1. 预测以下代码的输出：
```python
x = 5
x += 3
x *= 2
print(x)  # ?
```

2. 预测以下代码的输出：
```python
s = 'Hello'
s += ' World'
s *= 2
print(len(s))  # ?
```

3. 预测以下代码的输出：
```python
a = [1, 2]
b = a
a += [3]
print(b)  # ?
```

### 编程练习

1. 创建一个购物车类，支持添加商品、移除商品和计算总价
2. 实现一个简单的文本处理器，统计字符数和单词数
3. 编写一个程序，使用位运算符实现简单的权限管理系统

## 常见错误和注意事项

### 1. 可变对象的多重赋值

```python
# 错误：多个变量指向同一个可变对象
list1 = list2 = []
list1.append(1)
print(list2)  # [1] - 意外的结果

# 正确：创建独立的对象
list1 = []
list2 = []
list1.append(1)
print(list2)  # [] - 预期的结果
```

### 2. += 和 + 的区别

```python
# 对于可变对象，+= 修改原对象
list1 = [1, 2]
original = list1
list1 += [3]  # 修改原列表
print(original)  # [1, 2, 3]

# + 创建新对象
list2 = [1, 2]
original = list2
list2 = list2 + [3]  # 创建新列表
print(original)  # [1, 2]
```

### 3. 性能考虑

```python
# 字符串连接：join() 比 += 更高效
# 低效的方式
result = ""
for i in range(1000):
    result += str(i)

# 高效的方式
parts = []
for i in range(1000):
    parts.append(str(i))
result = ''.join(parts)
```

## 学习要点总结

1. **基本赋值**：使用 = 给变量赋值
2. **复合赋值**：使用 +=、-=、*= 等简化代码
3. **多重赋值**：注意可变对象的陷阱
4. **解包赋值**：优雅地处理多个值的赋值
5. **位赋值**：用于位操作的复合赋值
6. **性能考虑**：选择合适的方法提高效率
7. **实际应用**：在计数、累加、字符串构建等场景中灵活运用

赋值运算符是Python编程的基础，掌握它们的正确使用方法对编写高效、清晰的代码非常重要。