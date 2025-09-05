#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
比较运算符学习教程

本文件演示Python中的比较运算符的使用方法和特性
包括：等于(==)、不等于(!=)、小于(<)、大于(>)、小于等于(<=)、大于等于(>=)

学习目标：
1. 掌握所有比较运算符的使用
2. 理解比较运算符的返回值（布尔类型）
3. 学会不同数据类型之间的比较
4. 了解比较运算符的链式使用
"""

def main():
    print("="*50)
    print("Python 比较运算符学习教程")
    print("="*50)
    
    # 1. 基本比较运算符
    print("\n1. 基本比较运算符演示")
    print("-" * 30)
    
    a = 10
    b = 5
    c = 10
    
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"等于 (a == b): {a} == {b} = {a == b}")
    print(f"等于 (a == c): {a} == {c} = {a == c}")
    print(f"不等于 (a != b): {a} != {b} = {a != b}")
    print(f"不等于 (a != c): {a} != {c} = {a != c}")
    print(f"小于 (a < b): {a} < {b} = {a < b}")
    print(f"小于 (b < a): {b} < {a} = {b < a}")
    print(f"大于 (a > b): {a} > {b} = {a > b}")
    print(f"大于 (b > a): {b} > {a} = {b > a}")
    print(f"小于等于 (a <= c): {a} <= {c} = {a <= c}")
    print(f"小于等于 (b <= a): {b} <= {a} = {b <= a}")
    print(f"大于等于 (a >= c): {a} >= {c} = {a >= c}")
    print(f"大于等于 (a >= b): {a} >= {b} = {a >= b}")
    
    # 2. 字符串比较
    print("\n2. 字符串比较")
    print("-" * 30)
    
    str1 = "apple"
    str2 = "banana"
    str3 = "apple"
    
    print(f"str1 = '{str1}', str2 = '{str2}', str3 = '{str3}'")
    print(f"字符串相等: '{str1}' == '{str3}' = {str1 == str3}")
    print(f"字符串不等: '{str1}' != '{str2}' = {str1 != str2}")
    print(f"字典序比较: '{str1}' < '{str2}' = {str1 < str2}")
    print(f"字典序比较: '{str2}' > '{str1}' = {str2 > str1}")
    
    # 大小写敏感
    print(f"\n大小写敏感比较：")
    print(f"'Apple' == 'apple' = {'Apple' == 'apple'}")
    print(f"'Apple'.lower() == 'apple' = {'Apple'.lower() == 'apple'}")
    
    # 3. 数字类型比较
    print("\n3. 数字类型比较")
    print("-" * 30)
    
    int_num = 5
    float_num = 5.0
    complex_num = 5+0j
    
    print(f"整数与浮点数: {int_num} == {float_num} = {int_num == float_num}")
    print(f"整数与复数: {int_num} == {complex_num} = {int_num == complex_num}")
    print(f"浮点数与复数: {float_num} == {complex_num} = {float_num == complex_num}")
    
    # 浮点数精度问题
    print(f"\n浮点数精度问题：")
    result = 0.1 + 0.2
    print(f"0.1 + 0.2 = {result}")
    print(f"0.1 + 0.2 == 0.3 = {result == 0.3}")
    print(f"abs((0.1 + 0.2) - 0.3) < 1e-10 = {abs(result - 0.3) < 1e-10}")
    
    # 4. 列表和元组比较
    print("\n4. 列表和元组比较")
    print("-" * 30)
    
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 4]
    tuple1 = (1, 2, 3)
    
    print(f"列表相等: {list1} == {list2} = {list1 == list2}")
    print(f"列表不等: {list1} == {list3} = {list1 == list3}")
    print(f"列表字典序: {list1} < {list3} = {list1 < list3}")
    print(f"列表与元组: {list1} == {tuple1} = {list1 == tuple1}")
    
    # 5. 布尔值比较
    print("\n5. 布尔值比较")
    print("-" * 30)
    
    print(f"True == 1 = {True == 1}")
    print(f"False == 0 = {False == 0}")
    print(f"True > False = {True > False}")
    print(f"True + True = {True + True}")
    
    # 6. None 值比较
    print("\n6. None 值比较")
    print("-" * 30)
    
    value1 = None
    value2 = None
    value3 = 0
    value4 = ""
    
    print(f"None == None = {value1 == value2}")
    print(f"None == 0 = {value1 == value3}")
    print(f"None == '' = {value1 == value4}")
    print(f"None is None = {value1 is value2}")
    
    # 7. 链式比较
    print("\n7. 链式比较")
    print("-" * 30)
    
    x = 5
    print(f"x = {x}")
    print(f"1 < x < 10 = {1 < x < 10}")
    print(f"1 < x < 3 = {1 < x < 3}")
    print(f"0 <= x <= 10 = {0 <= x <= 10}")
    
    # 等价的非链式写法
    print(f"\n等价的非链式写法：")
    print(f"(1 < x) and (x < 10) = {(1 < x) and (x < 10)}")
    print(f"(1 < x) and (x < 3) = {(1 < x) and (x < 3)}")
    
    # 8. 实际应用示例
    print("\n8. 实际应用示例")
    print("-" * 30)
    
    # 成绩等级判定
    def get_grade(score):
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
    
    scores = [95, 85, 75, 65, 55]
    print("成绩等级判定：")
    for score in scores:
        grade = get_grade(score)
        print(f"分数 {score}: 等级 {grade}")
    
    # 年龄分组
    def age_group(age):
        if age < 13:
            return "儿童"
        elif 13 <= age < 20:
            return "青少年"
        elif 20 <= age < 60:
            return "成年人"
        else:
            return "老年人"
    
    ages = [8, 16, 25, 65]
    print("\n年龄分组：")
    for age in ages:
        group = age_group(age)
        print(f"年龄 {age}: {group}")
    
    # 9. 特殊比较情况
    print("\n9. 特殊比较情况")
    print("-" * 30)
    
    # 空容器比较
    empty_list = []
    empty_string = ""
    empty_dict = {}
    
    print(f"空列表 == 空列表: {empty_list == []}")
    print(f"空字符串 == 空字符串: {empty_string == ''}")
    print(f"空字典 == 空字典: {empty_dict == {}}")
    
    # 不同类型比较（Python 3中大多数会报错）
    print(f"\n类型转换比较：")
    print(f"'5' == 5 = {'5' == 5}")
    print(f"int('5') == 5 = {int('5') == 5}")
    print(f"str(5) == '5' = {str(5) == '5'}")

def practice_exercises():
    """
    练习题部分
    """
    print("\n" + "="*50)
    print("练习题")
    print("="*50)
    
    print("\n请判断以下表达式的结果（True/False）：")
    print("1. 10 > 5 and 3 < 7")
    print("2. 'hello' == 'Hello'")
    print("3. [1, 2] == [1, 2]")
    print("4. 5.0 == 5")
    print("5. 1 < 2 < 3 < 4")
    
    print("\n答案：")
    print(f"1. 10 > 5 and 3 < 7 = {10 > 5 and 3 < 7}")
    print(f"2. 'hello' == 'Hello' = {'hello' == 'Hello'}")
    print(f"3. [1, 2] == [1, 2] = {[1, 2] == [1, 2]}")
    print(f"4. 5.0 == 5 = {5.0 == 5}")
    print(f"5. 1 < 2 < 3 < 4 = {1 < 2 < 3 < 4}")
    
    print("\n编程练习：")
    print("1. 编写函数判断一个数是否在指定范围内")
    print("2. 比较两个字符串的长度")
    print("3. 找出列表中的最大值和最小值")
    
    # 示例解答
    print("\n示例解答：")
    
    # 1. 范围判断
    def in_range(num, min_val, max_val):
        return min_val <= num <= max_val
    
    test_num = 15
    print(f"1. {test_num} 是否在 10-20 范围内？{in_range(test_num, 10, 20)}")
    
    # 2. 字符串长度比较
    def compare_string_length(str1, str2):
        len1, len2 = len(str1), len(str2)
        if len1 > len2:
            return f"'{str1}' 比 '{str2}' 长"
        elif len1 < len2:
            return f"'{str1}' 比 '{str2}' 短"
        else:
            return f"'{str1}' 和 '{str2}' 长度相同"
    
    result = compare_string_length("hello", "world")
    print(f"2. {result}")
    
    # 3. 找最大值和最小值
    def find_min_max(numbers):
        if not numbers:
            return None, None
        min_val = max_val = numbers[0]
        for num in numbers[1:]:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
        return min_val, max_val
    
    test_list = [3, 7, 1, 9, 4, 6]
    min_val, max_val = find_min_max(test_list)
    print(f"3. 列表 {test_list} 中最小值: {min_val}, 最大值: {max_val}")

if __name__ == "__main__":
    main()
    practice_exercises()
    
    print("\n" + "="*50)
    print("学习小结")
    print("="*50)
    print("1. 比较运算符包括：==、!=、<、>、<=、>=")
    print("2. 比较运算符返回布尔值（True 或 False）")
    print("3. 字符串按字典序比较，区分大小写")
    print("4. 不同数字类型可以直接比较")
    print("5. 链式比较可以简化复杂的条件判断")
    print("6. 比较运算符在条件判断中应用广泛")