#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - 嵌套循环

本文件演示嵌套循环的用法和各种应用场景。
嵌套循环是在一个循环内部包含另一个循环，常用于处理二维数据、生成图案等。

学习目标：
1. 理解嵌套循环的概念和执行流程
2. 掌握二维数据的处理方法
3. 学会使用嵌套循环生成图案
4. 了解嵌套循环的性能考虑

作者：Python学习教程
日期：2024年
"""

# 1. 嵌套循环基础
print("=== 1. 嵌套循环基础 ===")
print("嵌套循环是在一个循环内部包含另一个循环")
print("外层循环每执行一次，内层循环会完整执行一遍")
print()

print("简单的嵌套循环示例：")
for i in range(3):
    print(f"外层循环 i = {i}")
    for j in range(2):
        print(f"  内层循环 j = {j}")
    print()

# 2. 乘法表
print("=== 2. 乘法表 ===")
print("使用嵌套循环生成乘法表：")
print()

print("完整的9x9乘法表：")
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f"{i}×{j}={result:2d}", end="  ")
    print()  # 换行
print()

print("三角形乘法表（更常见的形式）：")
for i in range(1, 10):
    for j in range(1, i + 1):
        result = i * j
        print(f"{j}×{i}={result:2d}", end=" ")
    print()  # 换行
print()

# 3. 二维列表处理
print("=== 3. 二维列表处理 ===")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("原始矩阵：")
for row in matrix:
    print(f"  {row}")
print()

print("使用嵌套循环遍历每个元素：")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"  matrix[{i}][{j}] = {matrix[i][j]}")
print()

print("计算矩阵的行和列的和：")
# 计算每行的和
print("每行的和：")
for i, row in enumerate(matrix):
    row_sum = 0
    for element in row:
        row_sum += element
    print(f"  第{i+1}行：{row_sum}")

# 计算每列的和
print("每列的和：")
for j in range(len(matrix[0])):
    col_sum = 0
    for i in range(len(matrix)):
        col_sum += matrix[i][j]
    print(f"  第{j+1}列：{col_sum}")
print()

# 4. 图案生成
print("=== 4. 图案生成 ===")

print("图案1：直角三角形")
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()
print()

print("图案2：倒直角三角形")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
print()

print("图案3：等腰三角形")
height = 5
for i in range(height):
    # 打印空格
    for j in range(height - i - 1):
        print(" ", end="")
    # 打印星号
    for j in range(2 * i + 1):
        print("*", end="")
    print()
print()

print("图案4：空心正方形")
size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

print("图案5：菱形")
size = 5
# 上半部分（包括中间）
for i in range(size):
    # 打印空格
    for j in range(size - i - 1):
        print(" ", end="")
    # 打印星号
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# 下半部分
for i in range(size - 2, -1, -1):
    # 打印空格
    for j in range(size - i - 1):
        print(" ", end="")
    # 打印星号
    for j in range(2 * i + 1):
        print("*", end="")
    print()
print()

# 5. 数字图案
print("=== 5. 数字图案 ===")

print("数字三角形1：")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()

print("数字三角形2：")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
print()

print("数字金字塔：")
for i in range(1, 6):
    # 打印空格
    for j in range(5 - i):
        print(" ", end="")
    # 打印递增数字
    for j in range(1, i + 1):
        print(j, end="")
    # 打印递减数字
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
print()

# 6. 查找和搜索
print("=== 6. 查找和搜索 ===")
data = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]

print("二维数组：")
for row in data:
    print(f"  {row}")
print()

target = 9
print(f"查找数字 {target}：")
found = False
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == target:
            print(f"  找到了！位置：({i}, {j})")
            found = True
            break
    if found:
        break

if not found:
    print(f"  没有找到 {target}")
print()

# 查找最大值和最小值
print("查找最大值和最小值：")
max_val = data[0][0]
min_val = data[0][0]
max_pos = (0, 0)
min_pos = (0, 0)

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] > max_val:
            max_val = data[i][j]
            max_pos = (i, j)
        if data[i][j] < min_val:
            min_val = data[i][j]
            min_pos = (i, j)

print(f"  最大值：{max_val}，位置：{max_pos}")
print(f"  最小值：{min_val}，位置：{min_pos}")
print()

# 7. 矩阵运算
print("=== 7. 矩阵运算 ===")

# 矩阵转置
original = [
    [1, 2, 3],
    [4, 5, 6]
]

print("原矩阵：")
for row in original:
    print(f"  {row}")

# 创建转置矩阵
rows = len(original)
cols = len(original[0])
transposed = []

for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(original[i][j])
    transposed.append(new_row)

print("转置矩阵：")
for row in transposed:
    print(f"  {row}")
print()

# 矩阵加法
matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
    [7, 8, 9],
    [10, 11, 12]
]

print("矩阵A：")
for row in matrix_a:
    print(f"  {row}")

print("矩阵B：")
for row in matrix_b:
    print(f"  {row}")

# 计算矩阵和
matrix_sum = []
for i in range(len(matrix_a)):
    row_sum = []
    for j in range(len(matrix_a[i])):
        row_sum.append(matrix_a[i][j] + matrix_b[i][j])
    matrix_sum.append(row_sum)

print("矩阵A + B：")
for row in matrix_sum:
    print(f"  {row}")
print()

# 8. 组合和排列
print("=== 8. 组合和排列 ===")

print("生成所有两位数的组合（十位和个位不同）：")
count = 0
for tens in range(1, 10):  # 十位数字1-9
    for ones in range(0, 10):  # 个位数字0-9
        if tens != ones:  # 十位和个位不同
            number = tens * 10 + ones
            print(f"{number:2d}", end=" ")
            count += 1
            if count % 10 == 0:  # 每10个数字换行
                print()
print(f"\n总共有 {count} 个这样的两位数")
print()

print("生成简单的密码组合（2位数字+2位字母）：")
digits = "0123456789"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
password_count = 0

print("前20个密码示例：")
for d1 in digits[:3]:  # 限制范围以减少输出
    for d2 in digits[:3]:
        for l1 in letters[:3]:
            for l2 in letters[:3]:
                password = d1 + d2 + l1 + l2
                print(password, end=" ")
                password_count += 1
                if password_count >= 20:
                    break
            if password_count >= 20:
                break
        if password_count >= 20:
            break
    if password_count >= 20:
        break
print(f"\n（实际可生成 {len(digits)**2 * len(letters)**2} 个密码）")
print()

# 9. 游戏应用
print("=== 9. 游戏应用 ===")

# 井字棋棋盘
print("井字棋棋盘初始化：")
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    board.append(row)

# 显示棋盘
def show_board(board):
    for i in range(3):
        for j in range(3):
            print(f"[{board[i][j]}]", end="")
        print()

show_board(board)
print()

# 模拟几步棋
board[0][0] = "X"
board[1][1] = "O"
board[2][2] = "X"
board[0][2] = "O"

print("游戏进行中：")
show_board(board)
print()

# 检查获胜条件
def check_winner(board):
    # 检查行
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
    
    # 检查列
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != " ":
            return board[0][j]
    
    # 检查对角线
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

winner = check_winner(board)
if winner:
    print(f"获胜者：{winner}")
else:
    print("游戏继续...")
print()

# 10. 性能考虑
print("=== 10. 性能考虑 ===")
print("嵌套循环的时间复杂度分析：")
print("- 两层循环，每层n次：O(n²)")
print("- 三层循环，每层n次：O(n³)")
print("- 要注意避免不必要的嵌套")
print()

# 演示性能差异
import time

print("性能测试：计算1000以内所有数对的和")

# 方法1：嵌套循环
start_time = time.time()
sum1 = 0
for i in range(100):  # 减小范围以便快速演示
    for j in range(100):
        sum1 += i + j
end_time = time.time()
time1 = end_time - start_time

print(f"嵌套循环方法：结果={sum1}，耗时={time1:.6f}秒")

# 方法2：数学公式（更高效）
start_time = time.time()
n = 100
sum2 = n * n * (2 * n - 2)  # 数学推导的结果
end_time = time.time()
time2 = end_time - start_time

print(f"数学公式方法：结果={sum2}，耗时={time2:.6f}秒")
if time2 > 0:
    print(f"性能提升：{time1/time2:.2f}倍")
else:
    print("数学公式方法执行时间太短，无法准确测量性能提升")
print()

# 11. 实际应用
print("=== 11. 实际应用 ===")

# 应用1：学生成绩统计
print("应用1：班级成绩统计")
students = ["张三", "李四", "王五", "赵六"]
subjects = ["语文", "数学", "英语"]
scores = [
    [85, 92, 78],  # 张三的成绩
    [90, 88, 85],  # 李四的成绩
    [78, 85, 92],  # 王五的成绩
    [88, 90, 87]   # 赵六的成绩
]

print("成绩表：")
print("姓名\t", end="")
for subject in subjects:
    print(f"{subject}\t", end="")
print("总分\t平均分")

for i, student in enumerate(students):
    print(f"{student}\t", end="")
    total = 0
    for j, score in enumerate(scores[i]):
        print(f"{score}\t", end="")
        total += score
    average = total / len(subjects)
    print(f"{total}\t{average:.1f}")

# 计算每科平均分
print("\n各科平均分：")
for j, subject in enumerate(subjects):
    subject_total = 0
    for i in range(len(students)):
        subject_total += scores[i][j]
    subject_average = subject_total / len(students)
    print(f"{subject}：{subject_average:.1f}分")
print()

# 应用2：简单的图像处理
print("应用2：简单的图像处理（用数字表示像素）")
# 创建一个简单的"图像"（5x5的数字矩阵）
image = [
    [100, 120, 110, 130, 140],
    [110, 125, 115, 135, 145],
    [105, 115, 120, 125, 130],
    [115, 130, 125, 140, 150],
    [120, 135, 130, 145, 155]
]

print("原始图像：")
for row in image:
    for pixel in row:
        print(f"{pixel:3d}", end=" ")
    print()

# 应用简单的滤镜（增加亮度）
brightness_increase = 20
print(f"\n增加亮度 +{brightness_increase}：")
for i in range(len(image)):
    for j in range(len(image[i])):
        new_value = min(255, image[i][j] + brightness_increase)  # 限制最大值为255
        print(f"{new_value:3d}", end=" ")
    print()
print()

# 12. 练习题
print("=== 12. 练习题 ===")

print("练习1：生成帕斯卡三角形（杨辉三角）")
rows = 6
print(f"帕斯卡三角形（{rows}行）：")
for i in range(rows):
    # 打印前导空格
    for j in range(rows - i - 1):
        print(" ", end="")
    
    # 计算并打印每行的数字
    for j in range(i + 1):
        if j == 0 or j == i:
            value = 1
        else:
            # 这里简化处理，实际应该用组合数公式
            value = 1
            for k in range(j):
                value = value * (i - k) // (k + 1)
        print(f"{value:2d}", end=" ")
    print()
print()

print("练习2：找出矩阵中的鞍点（行最大，列最小）")
test_matrix = [
    [1, 3, 2, 4],
    [5, 7, 6, 8],
    [9, 11, 10, 12]
]

print("测试矩阵：")
for row in test_matrix:
    print(f"  {row}")

print("查找鞍点：")
for i in range(len(test_matrix)):
    for j in range(len(test_matrix[i])):
        value = test_matrix[i][j]
        
        # 检查是否为行最大值
        is_row_max = True
        for k in range(len(test_matrix[i])):
            if test_matrix[i][k] > value:
                is_row_max = False
                break
        
        # 检查是否为列最小值
        is_col_min = True
        for k in range(len(test_matrix)):
            if test_matrix[k][j] < value:
                is_col_min = False
                break
        
        if is_row_max and is_col_min:
            print(f"  找到鞍点：{value} 在位置 ({i}, {j})")

if __name__ == "__main__":
    print("\n=== 嵌套循环学习总结 ===")
    print("1. 嵌套循环：循环内部包含另一个循环")
    print("2. 执行次数：外层n次，内层m次，总共n×m次")
    print("3. 常用场景：二维数据处理、图案生成、矩阵运算")
    print("4. 时间复杂度：通常为O(n²)或更高")
    print("5. 性能考虑：避免不必要的嵌套，考虑算法优化")
    print("6. 实际应用：游戏开发、图像处理、数据分析")
    print("7. 调试技巧：逐层检查，使用print语句跟踪执行")
    print("8. 优化方向：减少循环层数，使用更高效的算法")