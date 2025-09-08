# 综合练习

本节包含了循环相关的综合练习题，涵盖了从基础到高级的各种应用场景。通过这些练习，你可以巩固所学的循环知识，提高编程技能。

## 基础练习

### 1. 数字处理

计算1到100之间所有奇数的和：

```python
total = 0
for i in range(1, 101):
    if i % 2 == 1:
        total += i
print(f"1到100之间所有奇数的和：{total}")
```

### 2. 字符串操作

统计字符串中各种字符的数量：

```python
text = "Hello World Python Programming"
vowels = consonants = digits = spaces = others = 0

for char in text:
    if char.lower() in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == ' ':
        spaces += 1
    else:
        others += 1

print(f"元音：{vowels}, 辅音：{consonants}, 数字：{digits}, 空格：{spaces}, 其他：{others}")
```

## 中级练习

### 3. 数学计算

生成乘法表：

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} × {i} = {i * j}", end="\t")
    print()
```

### 4. 列表操作

找出列表中的重复元素：

```python
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1]
duplicates = []
checked = []

for num in numbers:
    if num in checked and num not in duplicates:
        duplicates.append(num)
    else:
        checked.append(num)

print(f"重复元素：{duplicates}")
```

## 高级练习

### 5. 算法实现

实现冒泡排序：

```python
numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(f"排序后：{numbers}")
```

### 6. 图案生成

生成数字金字塔：

```python
rows = 5
for i in range(1, rows + 1):
    # 打印空格
    for j in range(rows - i):
        print(" ", end="")
    # 打印数字
    for k in range(1, i + 1):
        print(k, end="")
    # 打印反向数字
    for l in range(i - 1, 0, -1):
        print(l, end="")
    print()
```

## 完整代码示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - 综合练习

本文件包含了循环相关的综合练习题，涵盖了从基础到高级的各种应用场景。
通过这些练习，可以巩固循环知识，提高编程技能。

练习分类：
1. 基础练习 - 简单的循环应用
2. 数学计算 - 数学相关的循环问题
3. 字符串处理 - 文本处理和分析
4. 列表操作 - 列表的各种操作
5. 图案生成 - 使用循环生成各种图案
6. 算法实现 - 经典算法的循环实现
7. 实际应用 - 解决实际问题
8. 挑战性练习 - 较难的综合题目

作者：Python学习教程
日期：2024年
"""

import random
import math

# 1. 基础练习
print("=== 1. 基础练习 ===")
print()

print("练习1.1：计算1到100之间所有奇数的和")
total_odd = 0
for i in range(1, 101):
    if i % 2 == 1:
        total_odd += i
print(f"结果：{total_odd}")
print(f"验证（公式）：{50 * 50}")
print()

print("练习1.2：打印1到20的平方数")
print("平方数：", end="")
for i in range(1, 21):
    print(f"{i}²={i**2}", end="  ")
print()
print()

print("练习1.3：倒数计时")
print("倒数计时：")
for i in range(10, 0, -1):
    print(f"{i}...", end=" ")
print("发射！")
print()

print("练习1.4：计算阶乘")
n = 6
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")
print()

# 2. 数学计算
print("=== 2. 数学计算 ===")
print()

print("练习2.1：生成斐波那契数列")
n_terms = 10
a, b = 0, 1
fib_sequence = []
for i in range(n_terms):
    fib_sequence.append(a)
    a, b = b, a + b
print(f"斐波那契数列（前{n_terms}项）：{fib_sequence}")
print()

print("练习2.2：判断质数")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

print("2到50之间的质数：")
primes = []
for num in range(2, 51):
    if is_prime(num):
        primes.append(num)
print(primes)
print()

print("练习2.3：完全数")
def is_perfect_number(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

print("1到1000之间的完全数：")
perfect_numbers = []
for num in range(1, 1001):
    if is_perfect_number(num):
        perfect_numbers.append(num)
print(perfect_numbers)
print()

print("练习2.4：最大公约数（欧几里得算法）")
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1, num2 = 48, 18
result = gcd(num1, num2)
print(f"{num1}和{num2}的最大公约数：{result}")
print()

print("练习2.5：生成乘法表")
print("九九乘法表：")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j:2d}", end="  ")
    print()
print()

# 3. 字符串处理
print("=== 3. 字符串处理 ===")
print()

print("练习3.1：字符统计")
text = "Hello World Python Programming 2024!"
print(f"文本：{text}")

vowels = consonants = digits = spaces = others = 0
for char in text:
    if char.lower() in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == ' ':
        spaces += 1
    else:
        others += 1

print(f"元音：{vowels}, 辅音：{consonants}, 数字：{digits}, 空格：{spaces}, 其他：{others}")
print()

print("练习3.2：回文检测")
def is_palindrome(s):
    # 转换为小写并移除非字母数字字符
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    
    # 检查是否为回文
    length = len(cleaned)
    for i in range(length // 2):
        if cleaned[i] != cleaned[length - 1 - i]:
            return False
    return True

test_strings = ["racecar", "A man a plan a canal Panama", "race a car", "hello"]
for s in test_strings:
    result = "是" if is_palindrome(s) else "不是"
    print(f"'{s}' {result}回文")
print()

print("练习3.3：单词频率统计")
text = "python is great python is powerful python is easy to learn"
print(f"文本：{text}")

# 分割单词
words = text.split()
word_count = {}

for word in words:
    word_lower = word.lower()
    if word_lower in word_count:
        word_count[word_lower] += 1
    else:
        word_count[word_lower] = 1

print("单词频率：")
for word, count in word_count.items():
    print(f"  '{word}': {count}次")
print()

print("练习3.4：字符串反转")
original = "Hello World"
reversed_str = ""
for char in original:
    reversed_str = char + reversed_str
print(f"原字符串：{original}")
print(f"反转后：{reversed_str}")
print()

print("练习3.5：凯撒密码")
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # 确定是大写还是小写
            start = ord('A') if char.isupper() else ord('a')
            # 应用位移
            shifted = (ord(char) - start + shift) % 26
            result += chr(start + shifted)
        else:
            result += char
    return result

original_text = "Hello World"
shift_amount = 3
encrypted = caesar_cipher(original_text, shift_amount)
decrypted = caesar_cipher(encrypted, -shift_amount)

print(f"原文：{original_text}")
print(f"加密（位移{shift_amount}）：{encrypted}")
print(f"解密：{decrypted}")
print()

# 4. 列表操作
print("=== 4. 列表操作 ===")
print()

print("练习4.1：找出重复元素")
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7, 8, 4]
print(f"原列表：{numbers}")

duplicates = []
checked = []

for num in numbers:
    if num in checked and num not in duplicates:
        duplicates.append(num)
    elif num not in checked:
        checked.append(num)

print(f"重复元素：{duplicates}")
print()

print("练习4.2：列表去重（保持顺序）")
original_list = [1, 2, 3, 2, 4, 5, 3, 6, 1]
print(f"原列表：{original_list}")

unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print(f"去重后：{unique_list}")
print()

print("练习4.3：找出两个列表的交集")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(f"列表1：{list1}")
print(f"列表2：{list2}")

intersection = []
for item in list1:
    if item in list2 and item not in intersection:
        intersection.append(item)

print(f"交集：{intersection}")
print()

print("练习4.4：列表分组")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原列表：{numbers}")

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(f"偶数：{even_numbers}")
print(f"奇数：{odd_numbers}")
print()

print("练习4.5：二维列表转置")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("原矩阵：")
for row in matrix:
    print(f"  {row}")

# 转置矩阵
transposed = []
for j in range(len(matrix[0])):
    new_row = []
    for i in range(len(matrix)):
        new_row.append(matrix[i][j])
    transposed.append(new_row)

print("转置后：")
for row in transposed:
    print(f"  {row}")
print()

# 5. 图案生成
print("=== 5. 图案生成 ===")
print()

print("练习5.1：星号三角形")
rows = 5
print(f"星号三角形（{rows}行）：")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
print()

print("练习5.2：倒立三角形")
rows = 5
print(f"倒立三角形（{rows}行）：")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
print()

print("练习5.3：等腰三角形")
rows = 5
print(f"等腰三角形（{rows}行）：")
for i in range(1, rows + 1):
    # 打印空格
    for j in range(rows - i):
        print(" ", end="")
    # 打印星号
    for k in range(2 * i - 1):
        print("*", end="")
    print()
print()

print("练习5.4：数字金字塔")
rows = 5
print(f"数字金字塔（{rows}行）：")
for i in range(1, rows + 1):
    # 打印空格
    for j in range(rows - i):
        print(" ", end="")
    # 打印递增数字
    for k in range(1, i + 1):
        print(k, end="")
    # 打印递减数字
    for l in range(i - 1, 0, -1):
        print(l, end="")
    print()
print()

print("练习5.5：菱形图案")
rows = 5
print(f"菱形图案（{rows}行）：")
# 上半部分
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
# 下半部分
for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
print()

# 6. 算法实现
print("=== 6. 算法实现 ===")
print()

print("练习6.1：冒泡排序")
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"排序前：{numbers}")

n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(f"排序后：{numbers}")
print()

print("练习6.2：选择排序")
numbers = [64, 25, 12, 22, 11]
print(f"排序前：{numbers}")

n = len(numbers)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

print(f"排序后：{numbers}")
print()

print("练习6.3：线性搜索")
numbers = [2, 3, 4, 10, 40]
target = 10
print(f"在 {numbers} 中搜索 {target}：")

found_index = -1
for i in range(len(numbers)):
    if numbers[i] == target:
        found_index = i
        break

if found_index != -1:
    print(f"找到 {target}，位置：{found_index}")
else:
    print(f"未找到 {target}")
print()

print("练习6.4：二进制转换")
def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

numbers = [10, 25, 42, 100]
print("十进制转二进制：")
for num in numbers:
    binary = decimal_to_binary(num)
    print(f"  {num} -> {binary}")
print()

print("练习6.5：最大子数组和（Kadane算法）")
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"数组：{numbers}")

max_sum = numbers[0]
current_sum = numbers[0]
start = end = temp_start = 0

for i in range(1, len(numbers)):
    if current_sum < 0:
        current_sum = numbers[i]
        temp_start = i
    else:
        current_sum += numbers[i]
    
    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start
        end = i

print(f"最大子数组和：{max_sum}")
print(f"子数组：{numbers[start:end+1]}")
print()

# 7. 实际应用
print("=== 7. 实际应用 ===")
print()

print("练习7.1：成绩统计")
scores = [85, 92, 78, 96, 88, 73, 91, 82, 95, 87]
print(f"成绩：{scores}")

total = 0
max_score = min_score = scores[0]
excellent = good = pass_grade = fail = 0

for score in scores:
    total += score
    if score > max_score:
        max_score = score
    if score < min_score:
        min_score = score
    
    if score >= 90:
        excellent += 1
    elif score >= 80:
        good += 1
    elif score >= 60:
        pass_grade += 1
    else:
        fail += 1

average = total / len(scores)

print(f"平均分：{average:.2f}")
print(f"最高分：{max_score}")
print(f"最低分：{min_score}")
print(f"优秀（90+）：{excellent}人")
print(f"良好（80-89）：{good}人")
print(f"及格（60-79）：{pass_grade}人")
print(f"不及格（<60）：{fail}人")
print()

print("练习7.2：购物车计算")
shopping_cart = [
    {"name": "苹果", "price": 5.5, "quantity": 3},
    {"name": "香蕉", "price": 3.2, "quantity": 5},
    {"name": "橙子", "price": 4.8, "quantity": 2},
    {"name": "葡萄", "price": 12.0, "quantity": 1}
]

print("购物车：")
total_amount = 0
total_items = 0

for item in shopping_cart:
    subtotal = item["price"] * item["quantity"]
    total_amount += subtotal
    total_items += item["quantity"]
    print(f"  {item['name']}: {item['price']}元 × {item['quantity']} = {subtotal}元")

print(f"\n总商品数：{total_items}")
print(f"总金额：{total_amount}元")

# 应用折扣
if total_amount > 50:
    discount = 0.1
    discount_amount = total_amount * discount
    final_amount = total_amount - discount_amount
    print(f"折扣（10%）：-{discount_amount}元")
    print(f"实付金额：{final_amount}元")
print()

print("练习7.3：密码强度检测")
def check_password_strength(password):
    score = 0
    feedback = []
    
    # 长度检查
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("密码长度至少8位")
    
    # 字符类型检查
    has_lower = has_upper = has_digit = has_special = False
    
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()_+-=[]{}|;:,.<>?":
            has_special = True
    
    if has_lower:
        score += 1
    else:
        feedback.append("需要小写字母")
    
    if has_upper:
        score += 1
    else:
        feedback.append("需要大写字母")
    
    if has_digit:
        score += 1
    else:
        feedback.append("需要数字")
    
    if has_special:
        score += 1
    else:
        feedback.append("需要特殊字符")
    
    # 评级
    if score >= 4:
        strength = "强"
    elif score >= 3:
        strength = "中等"
    elif score >= 2:
        strength = "弱"
    else:
        strength = "很弱"
    
    return strength, score, feedback

test_passwords = ["123456", "Password", "Password123", "P@ssw0rd123"]
for pwd in test_passwords:
    strength, score, feedback = check_password_strength(pwd)
    print(f"密码 '{pwd}'：")
    print(f"  强度：{strength} ({score}/5)")
    if feedback:
        print(f"  建议：{', '.join(feedback)}")
    print()

# 8. 挑战性练习
print("=== 8. 挑战性练习 ===")
print()

print("练习8.1：数独验证器")
def is_valid_sudoku(board):
    # 检查行
    for row in board:
        seen = set()
        for num in row:
            if num != 0 and num in seen:
                return False
            if num != 0:
                seen.add(num)
    
    # 检查列
    for col in range(9):
        seen = set()
        for row in range(9):
            num = board[row][col]
            if num != 0 and num in seen:
                return False
            if num != 0:
                seen.add(num)
    
    # 检查3x3方格
    for box_row in range(3):
        for box_col in range(3):
            seen = set()
            for row in range(box_row * 3, box_row * 3 + 3):
                for col in range(box_col * 3, box_col * 3 + 3):
                    num = board[row][col]
                    if num != 0 and num in seen:
                        return False
                    if num != 0:
                        seen.add(num)
    
    return True

# 测试数独（简化版，用0表示空格）
sudoku_board = [
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

print("数独验证：")
if is_valid_sudoku(sudoku_board):
    print("有效的数独")
else:
    print("无效的数独")
print()

print("练习8.2：文本相似度计算")
def calculate_similarity(text1, text2):
    # 转换为小写并分割单词
    words1 = text1.lower().split()
    words2 = text2.lower().split()
    
    # 创建词汇集合
    all_words = set(words1 + words2)
    
    # 计算词频向量
    vector1 = []
    vector2 = []
    
    for word in all_words:
        count1 = 0
        count2 = 0
        
        for w in words1:
            if w == word:
                count1 += 1
        
        for w in words2:
            if w == word:
                count2 += 1
        
        vector1.append(count1)
        vector2.append(count2)
    
    # 计算余弦相似度
    dot_product = 0
    norm1 = 0
    norm2 = 0
    
    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]
        norm1 += vector1[i] ** 2
        norm2 += vector2[i] ** 2
    
    if norm1 == 0 or norm2 == 0:
        return 0
    
    similarity = dot_product / (math.sqrt(norm1) * math.sqrt(norm2))
    return similarity

text1 = "Python is a great programming language"
text2 = "Python is an excellent programming language"
text3 = "Java is a popular programming language"

print("文本相似度计算：")
print(f"文本1：{text1}")
print(f"文本2：{text2}")
print(f"文本3：{text3}")
print(f"文本1与文本2相似度：{calculate_similarity(text1, text2):.3f}")
print(f"文本1与文本3相似度：{calculate_similarity(text1, text3):.3f}")
print(f"文本2与文本3相似度：{calculate_similarity(text2, text3):.3f}")
print()

print("练习8.3：简单推荐系统")
# 用户评分数据（用户ID -> {物品ID: 评分}）
user_ratings = {
    "用户1": {"电影A": 5, "电影B": 3, "电影C": 4, "电影D": 1},
    "用户2": {"电影A": 4, "电影B": 2, "电影C": 5, "电影E": 3},
    "用户3": {"电影A": 3, "电影C": 4, "电影D": 2, "电影E": 4},
    "用户4": {"电影B": 4, "电影C": 3, "电影D": 1, "电影E": 5}
}

def recommend_items(target_user, user_ratings, num_recommendations=2):
    target_ratings = user_ratings[target_user]
    recommendations = {}
    
    # 找到目标用户没有评分的物品
    all_items = set()
    for user_items in user_ratings.values():
        all_items.update(user_items.keys())
    
    unrated_items = all_items - set(target_ratings.keys())
    
    # 为每个未评分物品计算推荐分数
    for item in unrated_items:
        total_score = 0
        count = 0
        
        for user, ratings in user_ratings.items():
            if user != target_user and item in ratings:
                # 计算用户相似度（简化版）
                common_items = set(target_ratings.keys()) & set(ratings.keys())
                if common_items:
                    similarity = 0
                    for common_item in common_items:
                        similarity += abs(target_ratings[common_item] - ratings[common_item])
                    similarity = 1 / (1 + similarity)  # 转换为相似度
                    
                    total_score += ratings[item] * similarity
                    count += similarity
        
        if count > 0:
            recommendations[item] = total_score / count
    
    # 排序并返回前N个推荐
    sorted_recommendations = []
    for item, score in recommendations.items():
        sorted_recommendations.append((item, score))
    
    # 简单排序
    for i in range(len(sorted_recommendations)):
        for j in range(i + 1, len(sorted_recommendations)):
            if sorted_recommendations[i][1] < sorted_recommendations[j][1]:
                sorted_recommendations[i], sorted_recommendations[j] = sorted_recommendations[j], sorted_recommendations[i]
    
    return sorted_recommendations[:num_recommendations]

print("推荐系统：")
print("用户评分数据：")
for user, ratings in user_ratings.items():
    print(f"  {user}: {ratings}")

target_user = "用户1"
recommendations = recommend_items(target_user, user_ratings)
print(f"\n为{target_user}推荐：")
for item, score in recommendations:
    print(f"  {item}: {score:.3f}")
print()

if __name__ == "__main__":
    print("=== 循环综合练习总结 ===")
    print("通过这些练习，你应该掌握了：")
    print("1. 基础循环的各种应用场景")
    print("2. 数学计算和算法实现")
    print("3. 字符串处理和文本分析")
    print("4. 列表操作和数据处理")
    print("5. 图案生成和格式化输出")
    print("6. 经典算法的循环实现")
    print("7. 实际问题的解决方案")
    print("8. 复杂问题的分解和解决")
    print("\n继续练习这些题目，你的循环编程技能将得到显著提升！")
```

## 注意事项

1. **循环效率**：注意避免不必要的嵌套循环
2. **边界条件**：仔细处理循环的边界情况
3. **代码可读性**：保持代码清晰和注释完整
4. **算法复杂度**：了解不同算法的时间复杂度

## 练习建议

1. 从简单练习开始，逐步增加难度
2. 理解每个练习的核心思路和算法
3. 尝试用不同的方法解决同一个问题
4. 注意代码的优化和性能提升
5. 将练习与实际应用场景结合

通过大量的练习，你将能够熟练运用各种循环技巧，解决复杂的编程问题。