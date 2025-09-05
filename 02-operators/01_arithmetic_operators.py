#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
算术运算符学习教程

本文件演示Python中的算术运算符的使用方法和特性
包括：加法(+)、减法(-)、乘法(*)、除法(/)、整除(//)、取模(%)、幂运算(**)

学习目标：
1. 掌握基本算术运算符的使用
2. 理解整除和取模运算的特点
3. 学会幂运算的应用
4. 了解运算符与不同数据类型的交互
"""

def main():
    print("="*50)
    print("Python 算术运算符学习教程")
    print("="*50)
    
    # 1. 基本算术运算符
    print("\n1. 基本算术运算符演示")
    print("-" * 30)
    
    a = 10
    b = 3
    
    print(f"a = {a}, b = {b}")
    print(f"加法 (a + b): {a} + {b} = {a + b}")
    print(f"减法 (a - b): {a} - {b} = {a - b}")
    print(f"乘法 (a * b): {a} * {b} = {a * b}")
    print(f"除法 (a / b): {a} / {b} = {a / b}")
    
    # 2. 整除运算符 //
    print("\n2. 整除运算符 (//) 演示")
    print("-" * 30)
    
    print(f"整除 (a // b): {a} // {b} = {a // b}")
    print(f"说明：整除运算返回商的整数部分")
    
    # 负数的整除
    print(f"\n负数整除示例：")
    print(f"7 // 3 = {7 // 3}")
    print(f"-7 // 3 = {-7 // 3}")
    print(f"7 // -3 = {7 // -3}")
    print(f"-7 // -3 = {-7 // -3}")
    
    # 3. 取模运算符 %
    print("\n3. 取模运算符 (%) 演示")
    print("-" * 30)
    
    print(f"取模 (a % b): {a} % {b} = {a % b}")
    print(f"说明：取模运算返回除法的余数")
    
    # 取模的实际应用
    print(f"\n取模运算的实际应用：")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 == 1]
    print(f"偶数：{even_numbers}")
    print(f"奇数：{odd_numbers}")
    
    # 4. 幂运算符 **
    print("\n4. 幂运算符 (**) 演示")
    print("-" * 30)
    
    print(f"幂运算 (a ** b): {a} ** {b} = {a ** b}")
    print(f"平方：5 ** 2 = {5 ** 2}")
    print(f"立方：3 ** 3 = {3 ** 3}")
    print(f"开方：9 ** 0.5 = {9 ** 0.5}")
    print(f"开立方：27 ** (1/3) = {27 ** (1/3)}")
    
    # 5. 不同数据类型的算术运算
    print("\n5. 不同数据类型的算术运算")
    print("-" * 30)
    
    # 整数和浮点数
    int_num = 5
    float_num = 2.5
    print(f"整数 + 浮点数: {int_num} + {float_num} = {int_num + float_num}")
    print(f"结果类型: {type(int_num + float_num)}")
    
    # 字符串的算术运算
    str1 = "Hello"
    str2 = "World"
    print(f"\n字符串相加: '{str1}' + ' ' + '{str2}' = '{str1 + ' ' + str2}'")
    print(f"字符串重复: '{str1}' * 3 = '{str1 * 3}'")
    
    # 列表的算术运算
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(f"\n列表相加: {list1} + {list2} = {list1 + list2}")
    print(f"列表重复: {list1} * 2 = {list1 * 2}")
    
    # 6. 运算符优先级示例
    print("\n6. 运算符优先级示例")
    print("-" * 30)
    
    expression1 = 2 + 3 * 4
    expression2 = (2 + 3) * 4
    print(f"2 + 3 * 4 = {expression1} (先乘后加)")
    print(f"(2 + 3) * 4 = {expression2} (括号优先)")
    
    expression3 = 2 ** 3 ** 2
    expression4 = (2 ** 3) ** 2
    print(f"2 ** 3 ** 2 = {expression3} (幂运算右结合)")
    print(f"(2 ** 3) ** 2 = {expression4} (括号改变结合性)")
    
    # 7. 实用示例
    print("\n7. 实用示例")
    print("-" * 30)
    
    # 计算圆的面积
    import math
    radius = 5
    area = math.pi * radius ** 2
    print(f"半径为 {radius} 的圆的面积: {area:.2f}")
    
    # 温度转换
    celsius = 25
    fahrenheit = celsius * 9 / 5 + 32
    print(f"摄氏度 {celsius}°C = 华氏度 {fahrenheit}°F")
    
    # 计算复利
    principal = 1000  # 本金
    rate = 0.05      # 年利率
    time = 3         # 年数
    amount = principal * (1 + rate) ** time
    print(f"本金 {principal}，年利率 {rate*100}%，{time} 年后金额: {amount:.2f}")

def practice_exercises():
    """
    练习题部分
    """
    print("\n" + "="*50)
    print("练习题")
    print("="*50)
    
    print("\n请计算以下表达式的结果：")
    print("1. 15 + 4 * 3 - 2 = ?")
    print("2. (8 + 2) * 3 / 5 = ?")
    print("3. 17 % 5 = ?")
    print("4. 17 // 5 = ?")
    print("5. 2 ** 3 ** 2 = ?")
    
    print("\n答案：")
    print(f"1. 15 + 4 * 3 - 2 = {15 + 4 * 3 - 2}")
    print(f"2. (8 + 2) * 3 / 5 = {(8 + 2) * 3 / 5}")
    print(f"3. 17 % 5 = {17 % 5}")
    print(f"4. 17 // 5 = {17 // 5}")
    print(f"5. 2 ** 3 ** 2 = {2 ** 3 ** 2}")
    
    print("\n编程练习：")
    print("1. 编写程序判断一个数是否为偶数")
    print("2. 计算一个数的平方和立方")
    print("3. 将秒数转换为小时、分钟和秒")
    
    # 示例解答
    print("\n示例解答：")
    
    # 1. 判断偶数
    def is_even(num):
        return num % 2 == 0
    
    test_num = 8
    print(f"1. {test_num} 是偶数吗？{is_even(test_num)}")
    
    # 2. 计算平方和立方
    def calculate_powers(num):
        square = num ** 2
        cube = num ** 3
        return square, cube
    
    test_num = 4
    square, cube = calculate_powers(test_num)
    print(f"2. {test_num} 的平方是 {square}，立方是 {cube}")
    
    # 3. 时间转换
    def convert_seconds(total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return hours, minutes, seconds
    
    test_seconds = 3661
    h, m, s = convert_seconds(test_seconds)
    print(f"3. {test_seconds} 秒 = {h} 小时 {m} 分钟 {s} 秒")

if __name__ == "__main__":
    main()
    practice_exercises()
    
    print("\n" + "="*50)
    print("学习小结")
    print("="*50)
    print("1. 算术运算符包括：+、-、*、/、//、%、**")
    print("2. 整除(//)返回商的整数部分，取模(%)返回余数")
    print("3. 幂运算(**)可以进行乘方和开方运算")
    print("4. 不同数据类型的运算会有不同的结果")
    print("5. 运算符有优先级，可以用括号改变运算顺序")
    print("6. 算术运算符在实际编程中有广泛应用")