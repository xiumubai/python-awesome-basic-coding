#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - while循环基础

本文件演示while循环的基本用法和常见应用场景。
while循环在条件为真时重复执行代码块，适用于不确定循环次数的情况。

学习目标：
1. 理解while循环的基本语法
2. 掌握while循环的执行流程
3. 学会避免无限循环
4. 了解while循环的实际应用

作者：Python学习教程
日期：2024年
"""

# 1. while循环的基本语法
print("=== 1. while循环基本语法 ===")
print("while循环语法：while 条件:")
print("    循环体")
print("当条件为True时，执行循环体；当条件为False时，退出循环")
print()

# 2. 简单的while循环
print("=== 2. 简单的while循环 ===")
count = 1
print("从1数到5：")
while count <= 5:
    print(f"  当前数字：{count}")
    count += 1  # 重要：更新循环变量，避免无限循环
print(f"循环结束，count的值是：{count}")
print()

# 3. 倒计时示例
print("=== 3. 倒计时示例 ===")
countdown = 5
print("倒计时开始：")
while countdown > 0:
    print(f"  {countdown}...")
    countdown -= 1
print("  时间到！")
print()

# 4. 累加求和
print("=== 4. 累加求和 ===")
n = 10
sum_result = 0
i = 1
print(f"计算1到{n}的和：")
while i <= n:
    sum_result += i
    i += 1
print(f"1到{n}的和是：{sum_result}")
print()

# 5. 用户输入验证
print("=== 5. 用户输入验证 ===")
print("模拟用户输入验证（这里用预设值演示）：")

# 模拟用户输入的密码列表
password_attempts = ["123", "abc", "password", "python123"]
correct_password = "python123"
attempt_count = 0
max_attempts = 3

print(f"正确密码是：{correct_password}")
print(f"模拟输入序列：{password_attempts}")

while attempt_count < max_attempts:
    # 模拟用户输入
    if attempt_count < len(password_attempts):
        user_input = password_attempts[attempt_count]
    else:
        user_input = "wrong"
    
    print(f"第{attempt_count + 1}次尝试，输入：{user_input}")
    
    if user_input == correct_password:
        print("  密码正确！登录成功！")
        break
    else:
        attempt_count += 1
        remaining = max_attempts - attempt_count
        if remaining > 0:
            print(f"  密码错误！还有{remaining}次机会")
        else:
            print("  密码错误！账户已锁定")
print()

# 6. 查找列表中的元素
print("=== 6. 查找列表中的元素 ===")
numbers = [3, 7, 1, 9, 4, 6, 2, 8, 5]
target = 6
index = 0
found = False

print(f"在列表 {numbers} 中查找 {target}：")
while index < len(numbers):
    if numbers[index] == target:
        print(f"  找到了！{target} 在索引 {index} 位置")
        found = True
        break
    index += 1

if not found:
    print(f"  没有找到 {target}")
print()

# 7. 计算阶乘
print("=== 7. 计算阶乘 ===")
n = 5
factorial = 1
i = 1

print(f"计算 {n}! (阶乘)：")
while i <= n:
    factorial *= i
    print(f"  {i}! = {factorial}")
    i += 1
print(f"最终结果：{n}! = {factorial}")
print()

# 8. 数字猜测游戏
print("=== 8. 数字猜测游戏 ===")
import random

# 设置随机种子以便结果可预测
random.seed(42)
secret_number = random.randint(1, 10)
guess_attempts = [5, 8, 7, 6]  # 模拟用户猜测
attempts = 0
max_guesses = 4

print(f"我想了一个1到10之间的数字：{secret_number}")
print(f"模拟猜测序列：{guess_attempts}")
print("开始猜测：")

while attempts < max_guesses:
    if attempts < len(guess_attempts):
        guess = guess_attempts[attempts]
    else:
        guess = 1
    
    attempts += 1
    print(f"第{attempts}次猜测：{guess}")
    
    if guess == secret_number:
        print(f"  恭喜！你猜对了！用了{attempts}次")
        break
    elif guess < secret_number:
        print("  太小了！")
    else:
        print("  太大了！")
    
    if attempts == max_guesses:
        print(f"  游戏结束！正确答案是{secret_number}")
print()

# 9. while循环与else语句
print("=== 9. while循环与else语句 ===")
print("while循环也可以配合else使用，当循环条件变为False时执行else")

# 查找第一个偶数
numbers = [1, 3, 5, 7, 8, 9]
index = 0
print(f"在列表 {numbers} 中查找第一个偶数：")

while index < len(numbers):
    if numbers[index] % 2 == 0:
        print(f"  找到第一个偶数：{numbers[index]}，位置：{index}")
        break
    index += 1
else:
    print("  没有找到偶数")
print()

# 10. 避免无限循环
print("=== 10. 避免无限循环 ===")
print("无限循环的常见原因和避免方法：")
print("1. 忘记更新循环变量")
print("2. 循环条件永远为True")
print("3. 循环变量更新方向错误")
print()

# 错误示例（注释掉避免真正的无限循环）
print("错误示例1：忘记更新循环变量")
print("# count = 1")
print("# while count <= 5:")
print("#     print(count)")
print("#     # 忘记了 count += 1，会导致无限循环")
print()

print("正确示例：")
count = 1
while count <= 3:
    print(f"  正确的循环：{count}")
    count += 1  # 记住更新循环变量
print()

# 11. while循环的实际应用
print("=== 11. 实际应用示例 ===")

# 计算数字的位数
num = 12345
original_num = num
digit_count = 0

print(f"计算数字 {original_num} 的位数：")
while num > 0:
    num //= 10  # 整数除法
    digit_count += 1
    print(f"  当前num: {num}, 位数: {digit_count}")
print(f"{original_num} 有 {digit_count} 位数字")
print()

# 反转数字
num = 12345
original_num = num
reversed_num = 0

print(f"反转数字 {original_num}：")
while num > 0:
    digit = num % 10  # 获取最后一位数字
    reversed_num = reversed_num * 10 + digit
    num //= 10
    print(f"  当前数字: {digit}, 反转结果: {reversed_num}")
print(f"{original_num} 反转后是 {reversed_num}")
print()

# 12. 练习题
print("=== 12. 练习题 ===")

print("练习1：计算斐波那契数列的前10项")
a, b = 0, 1
count = 0
fib_sequence = []
while count < 10:
    fib_sequence.append(a)
    a, b = b, a + b
    count += 1
print(f"斐波那契数列前10项：{fib_sequence}")

print("\n练习2：判断一个数是否为回文数")
num = 12321
original = num
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

if original == reversed_num:
    print(f"{original} 是回文数")
else:
    print(f"{original} 不是回文数")

print("\n练习3：计算最大公约数（欧几里得算法）")
a, b = 48, 18
original_a, original_b = a, b
while b != 0:
    temp = b
    b = a % b
    a = temp
print(f"{original_a} 和 {original_b} 的最大公约数是：{a}")

if __name__ == "__main__":
    print("\n=== while循环学习总结 ===")
    print("1. while循环在条件为True时重复执行")
    print("2. 必须确保循环条件最终会变为False")
    print("3. 记住更新循环变量，避免无限循环")
    print("4. while循环适用于不确定循环次数的情况")
    print("5. 可以配合break和continue控制循环流程")
    print("6. while循环也可以使用else语句")
    print("7. 常用于用户输入验证、查找、计算等场景")