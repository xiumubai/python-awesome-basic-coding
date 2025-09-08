# while循环基础

while循环是Python中另一种重要的循环结构，它会在指定条件为真时重复执行代码块。与for循环不同，while循环更适合处理不确定次数的循环情况。

## 基本语法

while循环的基本语法结构：

```python
while 条件表达式:
    # 循环体代码
    pass
```

## 学习要点

### 1. 基础while循环

最简单的while循环：

```python
# 倒计时
count = 5
while count > 0:
    print(f"倒计时：{count}")
    count -= 1
print("时间到！")
```

### 2. 循环控制

使用break和continue控制循环：

```python
# 使用break退出循环
num = 1
while True:
    if num > 5:
        break
    print(num)
    num += 1

# 使用continue跳过当前迭代
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(f"奇数：{num}")
```

### 3. 用户输入验证

while循环常用于输入验证：

```python
while True:
    age = input("请输入您的年龄：")
    if age.isdigit() and 0 <= int(age) <= 120:
        print(f"您的年龄是{age}岁")
        break
    else:
        print("请输入有效的年龄（0-120）")
```

### 4. 累加和计算

使用while循环进行数值计算：

```python
# 计算1到100的和
total = 0
num = 1
while num <= 100:
    total += num
    num += 1
print(f"1到100的和是：{total}")
```

### 5. while-else语句

while循环也可以配合else使用：

```python
num = 1
while num <= 5:
    print(num)
    num += 1
else:
    print("循环正常结束")
```

## 完整代码示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - while循环基础

本文件详细介绍while循环的各种用法和应用场景。
while循环在条件为真时重复执行，适合处理不确定次数的循环。

主要内容：
1. while循环基本语法和执行流程
2. 循环条件的设计
3. 避免无限循环的方法
4. break和continue的使用
5. while-else语句
6. 实际应用示例

作者：Python学习教程
日期：2024年
"""

import random
import time

# 1. while循环基本语法
print("=== 1. while循环基本语法 ===")
print()

print("1.1 简单的倒计时")
count = 5
print(f"开始倒计时，从{count}开始：")
while count > 0:
    print(f"  倒计时：{count}")
    count -= 1
print("  时间到！")
print()

print("1.2 累加计算")
total = 0
num = 1
print("计算1到10的和：")
while num <= 10:
    print(f"  当前数字：{num}，累计和：{total + num}")
    total += num
    num += 1
print(f"最终结果：{total}")
print()

print("1.3 字符串处理")
text = "Hello"
index = 0
print(f"逐个输出字符串 '{text}' 的字符：")
while index < len(text):
    print(f"  索引{index}: {text[index]}")
    index += 1
print()

# 2. 循环条件的设计
print("=== 2. 循环条件的设计 ===")
print()

print("2.1 数值条件")
num = 1
print("输出小于20的2的幂：")
while num < 20:
    print(f"  2的{num//2 if num > 1 else 0}次方 = {num}")
    num *= 2
print()

print("2.2 布尔条件")
found = False
numbers = [3, 7, 12, 8, 15]
target = 12
index = 0
print(f"在列表 {numbers} 中查找 {target}：")

while index < len(numbers) and not found:
    if numbers[index] == target:
        found = True
        print(f"  在索引 {index} 处找到了 {target}")
    else:
        print(f"  索引 {index}: {numbers[index]} != {target}")
    index += 1

if not found:
    print(f"  没有找到 {target}")
print()

print("2.3 列表条件")
items = ["苹果", "香蕉", "橙子"]
print(f"购物清单：{items}")
print("逐个购买物品：")
while items:
    item = items.pop(0)  # 取出第一个物品
    print(f"  购买了：{item}，剩余：{items}")
print("  购物完成！")
print()

# 3. 避免无限循环
print("=== 3. 避免无限循环 ===")
print()

print("3.1 确保循环变量会改变")
num = 10
print("正确的递减循环：")
while num > 0:
    print(f"  当前值：{num}")
    num -= 1  # 确保循环变量递减
    if num <= 5:  # 提前退出演示
        print("  （为了演示，提前退出）")
        break
print()

print("3.2 设置最大循环次数")
max_attempts = 5
attempts = 0
print(f"最多尝试{max_attempts}次：")

while attempts < max_attempts:
    attempts += 1
    success = random.choice([True, False])  # 随机成功或失败
    print(f"  第{attempts}次尝试：{'成功' if success else '失败'}")
    
    if success:
        print("  任务完成！")
        break
else:
    print(f"  尝试了{max_attempts}次都失败了")
print()

# 4. break和continue的使用
print("=== 4. break和continue的使用 ===")
print()

print("4.1 使用break退出循环")
num = 1
print("查找第一个大于50的平方数：")
while True:
    square = num ** 2
    print(f"  {num}的平方是{square}")
    if square > 50:
        print(f"  找到了！{num}的平方{square}大于50")
        break
    num += 1
print()

print("4.2 使用continue跳过")
num = 0
print("输出1到10之间的奇数：")
while num < 10:
    num += 1
    if num % 2 == 0:  # 如果是偶数，跳过
        continue
    print(f"  奇数：{num}")
print()

print("4.3 综合使用break和continue")
print("处理数字列表，跳过负数，遇到0停止：")
numbers = [1, 3, -2, 5, -1, 0, 7, 9]
index = 0

while index < len(numbers):
    num = numbers[index]
    index += 1
    
    if num < 0:
        print(f"  跳过负数：{num}")
        continue
    
    if num == 0:
        print(f"  遇到0，停止处理")
        break
    
    print(f"  处理正数：{num}")
print()

# 5. 实际应用示例
print("=== 5. 实际应用示例 ===")
print()

print("5.1 用户输入验证")
print("模拟用户输入验证（自动输入演示）：")
# 模拟用户输入
inputs = ["abc", "-5", "150", "25"]
input_index = 0

while input_index < len(inputs):
    user_input = inputs[input_index]
    input_index += 1
    print(f"  用户输入：{user_input}")
    
    if user_input.isdigit():
        age = int(user_input)
        if 0 <= age <= 120:
            print(f"  有效年龄：{age}岁")
            break
        else:
            print(f"  年龄超出范围，请输入0-120之间的数字")
    else:
        print(f"  输入无效，请输入数字")
print()

print("5.2 数字猜测游戏")
secret_number = 42
guesses = [30, 50, 40, 42]  # 模拟猜测
guess_index = 0
attempts = 0
max_attempts = 5

print(f"猜数字游戏开始！数字范围1-100，最多{max_attempts}次机会")
print(f"（提示：答案是{secret_number}）")

while attempts < max_attempts and guess_index < len(guesses):
    attempts += 1
    guess = guesses[guess_index]
    guess_index += 1
    
    print(f"  第{attempts}次猜测：{guess}")
    
    if guess == secret_number:
        print(f"  恭喜！你猜对了！答案就是{secret_number}")
        print(f"  你用了{attempts}次猜测")
        break
    elif guess < secret_number:
        print(f"  太小了！")
    else:
        print(f"  太大了！")
else:
    if attempts >= max_attempts:
        print(f"  游戏结束！你用完了{max_attempts}次机会")
        print(f"  正确答案是{secret_number}")
print()

print("5.3 计算阶乘")
n = 5
print(f"计算{n}的阶乘：")
factorial = 1
i = 1
while i <= n:
    print(f"  {factorial} × {i} = {factorial * i}")
    factorial *= i
    i += 1
print(f"{n}! = {factorial}")
print()

print("5.4 查找列表中的元素")
numbers = [12, 45, 23, 67, 34, 89, 15]
target = 67
index = 0
found = False

print(f"在列表 {numbers} 中查找 {target}：")
while index < len(numbers):
    print(f"  检查索引{index}: {numbers[index]}")
    if numbers[index] == target:
        found = True
        print(f"  找到了！{target}在索引{index}处")
        break
    index += 1

if not found:
    print(f"  没有找到{target}")
print()

# 6. while-else语句
print("=== 6. while-else语句 ===")
print()

print("6.1 正常结束的循环")
num = 1
print("输出1到5：")
while num <= 5:
    print(f"  数字：{num}")
    num += 1
else:
    print("  循环正常结束")
print()

print("6.2 被break中断的循环")
numbers = [2, 4, 6, 7, 8]
index = 0
print(f"检查列表 {numbers} 是否都是偶数：")

while index < len(numbers):
    num = numbers[index]
    print(f"  检查 {num}")
    if num % 2 != 0:
        print(f"  发现奇数 {num}，不是所有数都是偶数")
        break
    index += 1
else:
    print("  所有数字都是偶数！")
print()

# 7. 综合练习
print("=== 7. 综合练习 ===")
print()

print("7.1 斐波那契数列")
n = 10
print(f"生成前{n}个斐波那契数：")
a, b = 0, 1
count = 0
fib_sequence = []

while count < n:
    fib_sequence.append(a)
    print(f"  第{count + 1}个：{a}")
    a, b = b, a + b
    count += 1

print(f"斐波那契数列：{fib_sequence}")
print()

print("7.2 数字反转")
num = 12345
original = num
reversed_num = 0

print(f"反转数字 {original}：")
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
    print(f"  当前位数字：{digit}，反转后：{reversed_num}")

print(f"最终结果：{original} -> {reversed_num}")
print()

print("7.3 质数判断")
num = 17
print(f"判断 {num} 是否为质数：")

if num < 2:
    is_prime = False
else:
    is_prime = True
    divisor = 2
    while divisor * divisor <= num:
        print(f"  检查 {num} 是否能被 {divisor} 整除")
        if num % divisor == 0:
            is_prime = False
            print(f"  {num} 能被 {divisor} 整除，不是质数")
            break
        divisor += 1
    else:
        print(f"  没有找到 {num} 的因数")

print(f"{num} {'是' if is_prime else '不是'}质数")
print()

if __name__ == "__main__":
    print("=== while循环学习总结 ===")
    print("通过本节学习，你应该掌握了：")
    print("1. while循环的基本语法和执行流程")
    print("2. 如何设计合适的循环条件")
    print("3. 避免无限循环的方法和技巧")
    print("4. break和continue语句的使用")
    print("5. while-else语句的特殊用法")
    print("6. while循环在实际编程中的应用")
    print("\n继续练习这些概念，你将能够熟练运用while循环解决各种问题！")
```

## 注意事项

1. **避免无限循环**：确保循环条件最终会变为假
2. **循环变量更新**：在循环体内正确更新控制变量
3. **条件设计**：设计清晰、准确的循环条件
4. **性能考虑**：避免在循环条件中进行复杂计算

## 练习建议

1. 实现各种数学计算（阶乘、斐波那契数列等）
2. 编写用户输入验证程序
3. 实现简单的游戏逻辑
4. 练习使用break和continue控制循环流程
5. 尝试while-else语句的不同应用场景

通过大量练习，你将能够熟练掌握while循环的各种用法，并能根据具体需求选择合适的循环结构。