#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - 综合练习

本文件包含循环相关的综合练习题，涵盖各种循环应用场景。
通过这些练习，可以巩固和提高循环编程技能。

练习内容：
1. 基础循环练习
2. 数学计算练习
3. 字符串处理练习
4. 列表操作练习
5. 图案生成练习
6. 算法实现练习
7. 实际应用练习
8. 挑战性练习

作者：Python学习教程
日期：2024年
"""

# 练习1：基础循环练习
print("=== 练习1：基础循环练习 ===")
print()

print("1.1 打印1到100中所有3的倍数")
print("解答：")
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=" ")
print("\n")

print("1.2 计算1到50中所有偶数的平方和")
print("解答：")
sum_of_squares = 0
for i in range(2, 51, 2):  # 直接遍历偶数
    sum_of_squares += i ** 2
print(f"1到50中所有偶数的平方和：{sum_of_squares}")
print()

print("1.3 使用while循环实现倒计时")
print("解答：")
countdown = 10
print("倒计时开始：")
while countdown > 0:
    print(f"{countdown}...", end=" ")
    countdown -= 1
print("时间到！")
print()

# 练习2：数学计算练习
print("=== 练习2：数学计算练习 ===")
print()

print("2.1 计算圆周率π的近似值（使用莱布尼茨公式）")
print("公式：π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...")
print("解答：")
pi_approximation = 0
terms = 100000  # 使用的项数
for i in range(terms):
    term = (-1) ** i / (2 * i + 1)
    pi_approximation += term
pi_approximation *= 4
print(f"使用{terms}项计算的π近似值：{pi_approximation}")
print(f"与真实π值的差异：{abs(pi_approximation - 3.141592653589793)}")
print()

print("2.2 生成前20个斐波那契数列")
print("解答：")
fib_sequence = []
a, b = 0, 1
for i in range(20):
    fib_sequence.append(a)
    a, b = b, a + b
print(f"前20个斐波那契数：{fib_sequence}")
print()

print("2.3 判断一个数是否为完全数")
print("完全数：等于其所有真因数之和的正整数")
print("解答：")
def is_perfect_number(n):
    if n <= 1:
        return False
    
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    
    return divisors_sum == n

# 测试前1000个数中的完全数
print("1000以内的完全数：")
for num in range(1, 1001):
    if is_perfect_number(num):
        print(f"{num} 是完全数")
print()

print("2.4 计算最大公约数（欧几里得算法）")
print("解答：")
def gcd(a, b):
    print(f"计算 gcd({a}, {b})：")
    while b != 0:
        print(f"  {a} = {a // b} × {b} + {a % b}")
        a, b = b, a % b
    print(f"  最大公约数：{a}")
    return a

gcd(48, 18)
print()

# 练习3：字符串处理练习
print("=== 练习3：字符串处理练习 ===")
print()

print("3.1 统计字符串中每个字符的出现次数")
print("解答：")
text = "hello world python programming"
print(f"文本：{text}")
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("字符统计：")
for char, count in sorted(char_count.items()):
    if char == ' ':
        print(f"  空格: {count}")
    else:
        print(f"  '{char}': {count}")
print()

print("3.2 检查字符串是否为回文")
print("解答：")
def is_palindrome(s):
    # 转换为小写并去除空格和标点
    cleaned = ""
    for char in s.lower():
        if char.isalnum():
            cleaned += char
    
    # 检查是否为回文
    length = len(cleaned)
    for i in range(length // 2):
        if cleaned[i] != cleaned[length - 1 - i]:
            return False
    return True

test_strings = [
    "racecar",
    "A man a plan a canal Panama",
    "race a car",
    "hello",
    "Madam"
]

for test_str in test_strings:
    result = is_palindrome(test_str)
    print(f"'{test_str}' 是回文：{result}")
print()

print("3.3 实现简单的凯撒密码加密")
print("解答：")
def caesar_cipher(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            # 确定是大写还是小写
            if char.isupper():
                # 大写字母
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # 小写字母
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # 非字母字符保持不变
            encrypted += char
    return encrypted

original_text = "Hello World Python"
shift_value = 3
encrypted_text = caesar_cipher(original_text, shift_value)
decrypted_text = caesar_cipher(encrypted_text, -shift_value)

print(f"原文：{original_text}")
print(f"加密（位移{shift_value}）：{encrypted_text}")
print(f"解密：{decrypted_text}")
print()

# 练习4：列表操作练习
print("=== 练习4：列表操作练习 ===")
print()

print("4.1 实现冒泡排序")
print("解答：")
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    print(f"原始数组：{arr}")
    
    for i in range(n):
        swapped = False
        print(f"\n第{i+1}轮排序：")
        
        for j in range(0, n - i - 1):
            comparisons += 1
            print(f"  比较 {arr[j]} 和 {arr[j+1]}", end="")
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
                print(f" -> 交换")
            else:
                print(f" -> 不交换")
        
        print(f"  本轮结果：{arr}")
        
        if not swapped:
            print(f"  数组已排序，提前结束")
            break
    
    print(f"\n最终结果：{arr}")
    print(f"总比较次数：{comparisons}")
    print(f"总交换次数：{swaps}")
    return arr

test_array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(test_array.copy())
print()

print("4.2 找出数组中的第二大数")
print("解答：")
def find_second_largest(arr):
    if len(arr) < 2:
        return None
    
    largest = second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest if second_largest != float('-inf') else None

test_arrays = [
    [1, 2, 3, 4, 5],
    [5, 5, 5, 5],
    [10, 20, 4, 45, 99, 99],
    [1]
]

for arr in test_arrays:
    second_largest = find_second_largest(arr)
    print(f"数组 {arr} 的第二大数：{second_largest}")
print()

print("4.3 实现数组的旋转")
print("解答：")
def rotate_array(arr, k):
    """向右旋转数组k个位置"""
    if not arr or k == 0:
        return arr
    
    n = len(arr)
    k = k % n  # 处理k大于数组长度的情况
    
    print(f"原数组：{arr}")
    print(f"向右旋转{k}个位置")
    
    # 方法1：使用额外空间
    rotated = [0] * n
    for i in range(n):
        rotated[(i + k) % n] = arr[i]
    
    print(f"结果：{rotated}")
    return rotated

test_array = [1, 2, 3, 4, 5, 6, 7]
for k in [1, 3, 7, 10]:
    rotate_array(test_array.copy(), k)
    print()

# 练习5：图案生成练习
print("=== 练习5：图案生成练习 ===")
print()

print("5.1 生成数字金字塔")
print("解答：")
def number_pyramid(height):
    for i in range(1, height + 1):
        # 打印前导空格
        for j in range(height - i):
            print(" ", end="")
        
        # 打印递增数字
        for j in range(1, i + 1):
            print(j, end="")
        
        # 打印递减数字
        for j in range(i - 1, 0, -1):
            print(j, end="")
        
        print()  # 换行

print("数字金字塔（高度5）：")
number_pyramid(5)
print()

print("5.2 生成螺旋矩阵")
print("解答：")
def spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    
    while top <= bottom and left <= right:
        # 从左到右填充上行
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1
        
        # 从上到下填充右列
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1
        
        # 从右到左填充下行
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
        
        # 从下到上填充左列
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
    
    return matrix

print("4x4螺旋矩阵：")
spiral = spiral_matrix(4)
for row in spiral:
    for num in row:
        print(f"{num:2d}", end=" ")
    print()
print()

print("5.3 生成帕斯卡三角形")
print("解答：")
def pascal_triangle(rows):
    triangle = []
    
    for i in range(rows):
        row = [1]  # 每行第一个数字是1
        
        if triangle:  # 如果不是第一行
            for j in range(len(triangle[-1]) - 1):
                # 当前位置的值等于上一行相邻两个数的和
                row.append(triangle[-1][j] + triangle[-1][j + 1])
            row.append(1)  # 每行最后一个数字是1
        
        triangle.append(row)
    
    return triangle

print("帕斯卡三角形（8行）：")
triangle = pascal_triangle(8)
max_width = len(' '.join(map(str, triangle[-1])))

for row in triangle:
    row_str = ' '.join(map(str, row))
    spaces = (max_width - len(row_str)) // 2
    print(' ' * spaces + row_str)
print()

# 练习6：算法实现练习
print("=== 练习6：算法实现练习 ===")
print()

print("6.1 实现选择排序")
print("解答：")
def selection_sort(arr):
    n = len(arr)
    print(f"原始数组：{arr}")
    
    for i in range(n):
        min_idx = i
        print(f"\n第{i+1}轮，寻找位置{i}的最小值：")
        
        # 找到剩余部分的最小值
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        print(f"  最小值 {arr[min_idx]} 在位置 {min_idx}")
        
        # 交换
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"  交换位置 {i} 和 {min_idx}")
        
        print(f"  当前数组：{arr}")
    
    print(f"\n最终排序结果：{arr}")
    return arr

test_array = [64, 25, 12, 22, 11]
selection_sort(test_array.copy())
print()

print("6.2 实现二分查找")
print("解答：")
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    steps = 0
    
    print(f"在数组 {arr} 中查找 {target}")
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        print(f"第{steps}步：left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"找到目标值 {target}，位置：{mid}")
            return mid
        elif arr[mid] < target:
            left = mid + 1
            print(f"  目标值较大，搜索右半部分")
        else:
            right = mid - 1
            print(f"  目标值较小，搜索左半部分")
    
    print(f"未找到目标值 {target}")
    return -1

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
for target in [7, 15, 4, 20]:
    binary_search(sorted_array, target)
    print()

print("6.3 实现插入排序")
print("解答：")
def insertion_sort(arr):
    print(f"原始数组：{arr}")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        print(f"\n第{i}轮，插入元素 {key}：")
        print(f"  当前数组：{arr}")
        
        # 将key插入到已排序部分的正确位置
        while j >= 0 and arr[j] > key:
            print(f"  {arr[j]} > {key}，向右移动")
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        print(f"  插入 {key} 到位置 {j + 1}")
        print(f"  结果：{arr}")
    
    print(f"\n最终排序结果：{arr}")
    return arr

test_array = [12, 11, 13, 5, 6]
insertion_sort(test_array.copy())
print()

# 练习7：实际应用练习
print("=== 练习7：实际应用练习 ===")
print()

print("7.1 学生成绩管理系统")
print("解答：")
class StudentGradeManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, grades):
        self.students[name] = grades
    
    def calculate_average(self, name):
        if name in self.students:
            grades = self.students[name]
            return sum(grades) / len(grades)
        return None
    
    def find_top_student(self):
        if not self.students:
            return None
        
        top_student = None
        highest_avg = -1
        
        for name in self.students:
            avg = self.calculate_average(name)
            if avg > highest_avg:
                highest_avg = avg
                top_student = name
        
        return top_student, highest_avg
    
    def generate_report(self):
        print("学生成绩报告：")
        print("-" * 50)
        
        for name, grades in self.students.items():
            avg = self.calculate_average(name)
            print(f"{name:10s} | 成绩: {grades} | 平均分: {avg:.2f}")
        
        top_student, top_avg = self.find_top_student()
        if top_student:
            print("-" * 50)
            print(f"最高分学生：{top_student}，平均分：{top_avg:.2f}")

# 使用示例
manager = StudentGradeManager()
manager.add_student("张三", [85, 92, 78, 90])
manager.add_student("李四", [88, 85, 92, 87])
manager.add_student("王五", [92, 88, 85, 94])
manager.add_student("赵六", [78, 82, 80, 85])

manager.generate_report()
print()

print("7.2 简单的库存管理")
print("解答：")
class InventoryManager:
    def __init__(self):
        self.inventory = {}
    
    def add_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
    
    def sell_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name]['quantity'] >= quantity:
                self.inventory[item_name]['quantity'] -= quantity
                return True
        return False
    
    def check_low_stock(self, threshold=10):
        low_stock_items = []
        for item_name, info in self.inventory.items():
            if info['quantity'] < threshold:
                low_stock_items.append((item_name, info['quantity']))
        return low_stock_items
    
    def calculate_total_value(self):
        total_value = 0
        for item_name, info in self.inventory.items():
            total_value += info['quantity'] * info['price']
        return total_value
    
    def generate_report(self):
        print("库存报告：")
        print("-" * 60)
        print(f"{'商品名称':15s} | {'数量':8s} | {'单价':8s} | {'总价值':10s}")
        print("-" * 60)
        
        for item_name, info in self.inventory.items():
            total_value = info['quantity'] * info['price']
            print(f"{item_name:15s} | {info['quantity']:8d} | {info['price']:8.2f} | {total_value:10.2f}")
        
        print("-" * 60)
        print(f"库存总价值：{self.calculate_total_value():.2f}")
        
        low_stock = self.check_low_stock()
        if low_stock:
            print("\n库存不足警告：")
            for item_name, quantity in low_stock:
                print(f"  {item_name}: {quantity} 件")

# 使用示例
inventory = InventoryManager()
inventory.add_item("苹果", 50, 3.5)
inventory.add_item("香蕉", 30, 2.8)
inventory.add_item("橙子", 8, 4.2)
inventory.add_item("葡萄", 25, 8.5)

# 模拟销售
inventory.sell_item("苹果", 15)
inventory.sell_item("橙子", 3)

inventory.generate_report()
print()

print("7.3 文本词频分析器")
print("解答：")
class TextAnalyzer:
    def __init__(self, text):
        self.text = text.lower()
        self.words = self._extract_words()
        self.word_count = self._count_words()
    
    def _extract_words(self):
        # 简单的单词提取（去除标点符号）
        cleaned_text = ""
        for char in self.text:
            if char.isalnum() or char.isspace():
                cleaned_text += char
            else:
                cleaned_text += " "
        
        words = cleaned_text.split()
        return [word for word in words if word]  # 过滤空字符串
    
    def _count_words(self):
        word_count = {}
        for word in self.words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count
    
    def get_most_frequent(self, n=10):
        # 按频率排序
        sorted_words = []
        for word, count in self.word_count.items():
            sorted_words.append((count, word))
        
        # 简单排序
        for i in range(len(sorted_words)):
            for j in range(len(sorted_words) - 1 - i):
                if sorted_words[j][0] < sorted_words[j + 1][0]:
                    sorted_words[j], sorted_words[j + 1] = sorted_words[j + 1], sorted_words[j]
        
        return sorted_words[:n]
    
    def generate_report(self):
        print("文本分析报告：")
        print("-" * 40)
        print(f"总字符数：{len(self.text)}")
        print(f"总单词数：{len(self.words)}")
        print(f"不重复单词数：{len(self.word_count)}")
        
        print("\n词频统计（前10个）：")
        most_frequent = self.get_most_frequent(10)
        for count, word in most_frequent:
            print(f"  {word:15s}: {count:3d} 次")

# 使用示例
sample_text = """
Python is a powerful programming language. Python is easy to learn and use.
Many developers choose Python for web development, data science, and automation.
Python's syntax is clean and readable, making Python a great choice for beginners.
"""

analyzer = TextAnalyzer(sample_text)
analyzer.generate_report()
print()

# 练习8：挑战性练习
print("=== 练习8：挑战性练习 ===")
print()

print("8.1 实现简单的数独验证器")
print("解答：")
def validate_sudoku(board):
    """验证9x9数独是否有效"""
    
    def is_valid_unit(unit):
        # 检查一个单元（行、列或3x3方格）是否有效
        seen = set()
        for num in unit:
            if num != 0:  # 0表示空格
                if num in seen or num < 1 or num > 9:
                    return False
                seen.add(num)
        return True
    
    # 检查所有行
    for row in board:
        if not is_valid_unit(row):
            return False, "行验证失败"
    
    # 检查所有列
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_unit(column):
            return False, "列验证失败"
    
    # 检查所有3x3方格
    for box_row in range(3):
        for box_col in range(3):
            box = []
            for row in range(box_row * 3, (box_row + 1) * 3):
                for col in range(box_col * 3, (box_col + 1) * 3):
                    box.append(board[row][col])
            if not is_valid_unit(box):
                return False, "3x3方格验证失败"
    
    return True, "数独有效"

# 测试用例
valid_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

invalid_sudoku = [
    [5, 3, 5, 0, 7, 0, 0, 0, 0],  # 第一行有重复的5
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("测试有效数独：")
result, message = validate_sudoku(valid_sudoku)
print(f"结果：{result}，信息：{message}")

print("\n测试无效数独：")
result, message = validate_sudoku(invalid_sudoku)
print(f"结果：{result}，信息：{message}")
print()

print("8.2 实现简单的表达式计算器")
print("解答：")
class SimpleCalculator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    def tokenize(self, expression):
        """将表达式分解为标记"""
        tokens = []
        current_number = ""
        
        for char in expression:
            if char.isdigit() or char == '.':
                current_number += char
            else:
                if current_number:
                    tokens.append(float(current_number))
                    current_number = ""
                if char in self.operators or char in '()':
                    tokens.append(char)
        
        if current_number:
            tokens.append(float(current_number))
        
        return tokens
    
    def infix_to_postfix(self, tokens):
        """将中缀表达式转换为后缀表达式"""
        output = []
        operator_stack = []
        
        for token in tokens:
            if isinstance(token, (int, float)):
                output.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()  # 移除 '('
            elif token in self.operators:
                while (operator_stack and 
                       operator_stack[-1] != '(' and
                       operator_stack[-1] in self.operators and
                       self.operators[operator_stack[-1]] >= self.operators[token]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
        
        while operator_stack:
            output.append(operator_stack.pop())
        
        return output
    
    def evaluate_postfix(self, postfix):
        """计算后缀表达式的值"""
        stack = []
        
        for token in postfix:
            if isinstance(token, (int, float)):
                stack.append(token)
            elif token in self.operators:
                if len(stack) < 2:
                    raise ValueError("表达式无效")
                
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        raise ValueError("除零错误")
                    result = a / b
                
                stack.append(result)
        
        if len(stack) != 1:
            raise ValueError("表达式无效")
        
        return stack[0]
    
    def calculate(self, expression):
        """计算表达式的值"""
        try:
            # 去除空格
            expression = expression.replace(' ', '')
            print(f"原表达式：{expression}")
            
            # 分词
            tokens = self.tokenize(expression)
            print(f"分词结果：{tokens}")
            
            # 转换为后缀表达式
            postfix = self.infix_to_postfix(tokens)
            print(f"后缀表达式：{postfix}")
            
            # 计算结果
            result = self.evaluate_postfix(postfix)
            print(f"计算结果：{result}")
            
            return result
        
        except Exception as e:
            print(f"计算错误：{e}")
            return None

# 使用示例
calculator = SimpleCalculator()

test_expressions = [
    "3 + 4 * 2",
    "(3 + 4) * 2",
    "10 - 2 * 3",
    "15 / 3 + 2 * 4",
    "(10 + 2) * (5 - 3)"
]

for expr in test_expressions:
    print(f"\n{'='*50}")
    calculator.calculate(expr)

if __name__ == "__main__":
    print("\n=== 循环综合练习总结 ===")
    print("通过这些练习，你应该掌握了：")
    print("1. 基础循环：for循环、while循环的各种用法")
    print("2. 数学计算：数值计算、数学公式实现")
    print("3. 字符串处理：字符统计、模式匹配、加密解密")
    print("4. 列表操作：排序算法、查找算法、数组操作")
    print("5. 图案生成：各种数学图案和矩阵")
    print("6. 算法实现：经典排序和查找算法")
    print("7. 实际应用：管理系统、数据分析")
    print("8. 挑战练习：复杂算法和数据结构")
    print("\n继续练习这些模式，你的编程技能会不断提高！")