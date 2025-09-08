# 嵌套循环

嵌套循环是指在一个循环内部包含另一个循环的结构。这是处理二维数据、生成复杂图案、进行多层遍历的重要技术。本节将详细介绍嵌套循环的概念、应用和最佳实践。

## 基本概念

### 1. 嵌套循环结构

最基本的嵌套循环：

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

### 2. 执行顺序

理解嵌套循环的执行顺序：
- 外层循环执行一次
- 内层循环完整执行所有迭代
- 然后外层循环进入下一次迭代

## 学习要点

### 1. 乘法表生成

经典的九九乘法表：

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} × {i} = {i * j}", end="\t")
    print()  # 换行
```

### 2. 二维列表处理

遍历和操作二维列表：

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # 换行
```

### 3. 图案生成

使用嵌套循环生成各种图案：

```python
# 生成星号三角形
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # 换行
```

## 完整代码示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - 嵌套循环

本文件详细介绍嵌套循环的概念、语法和应用。
嵌套循环是处理多维数据和复杂逻辑的重要工具，
掌握嵌套循环对于解决复杂问题至关重要。

主要内容：
1. 嵌套循环基本概念和语法
2. 乘法表和数学应用
3. 二维列表和矩阵操作
4. 图案和图形生成
5. 查找和搜索算法
6. 组合和排列问题
7. 游戏和实际应用
8. 性能优化考虑

作者：Python学习教程
日期：2024年
"""

import random
import time

# 1. 嵌套循环基础
print("=== 1. 嵌套循环基础 ===")
print()

print("1.1 基本嵌套循环")
print("简单的二重循环：")
for i in range(3):
    print(f"外层循环 i = {i}")
    for j in range(3):
        print(f"  内层循环 j = {j}，坐标({i}, {j})")
    print("  内层循环结束")
print("外层循环结束")
print()

print("1.2 不同范围的嵌套循环")
print("外层3次，内层递增：")
for i in range(3):
    print(f"第{i+1}行：", end="")
    for j in range(i + 1):
        print(f"({i},{j})", end=" ")
    print()  # 换行
print()

print("1.3 三重嵌套循环")
print("三维坐标生成：")
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"({x},{y},{z})", end=" ")
print()
print()

# 2. 乘法表应用
print("=== 2. 乘法表应用 ===")
print()

print("2.1 九九乘法表")
for i in range(1, 10):
    for j in range(1, i + 1):
        result = i * j
        print(f"{j}×{i}={result:2d}", end="  ")
    print()  # 换行
print()

print("2.2 完整乘法表（10×10）")
print("   ", end="")
# 打印表头
for i in range(1, 11):
    print(f"{i:4d}", end="")
print()

# 打印分隔线
print("   " + "-" * 40)

# 打印表格内容
for i in range(1, 11):
    print(f"{i:2d} |", end="")
    for j in range(1, 11):
        result = i * j
        print(f"{result:4d}", end="")
    print()
print()

print("2.3 加法表")
print("加法表（1-5）：")
for i in range(1, 6):
    for j in range(1, 6):
        result = i + j
        print(f"{i}+{j}={result:2d}", end="  ")
    print()
print()

# 3. 二维列表处理
print("=== 3. 二维列表处理 ===")
print()

print("3.1 创建和遍历二维列表")
# 创建3×4的二维列表
matrix = []
for i in range(3):
    row = []
    for j in range(4):
        row.append(i * 4 + j + 1)
    matrix.append(row)

print("创建的矩阵：")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"{matrix[i][j]:3d}", end=" ")
    print()
print()

print("3.2 矩阵运算")
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

print("矩阵A：")
for row in matrix_a:
    for element in row:
        print(f"{element:3d}", end=" ")
    print()

print("矩阵B：")
for row in matrix_b:
    for element in row:
        print(f"{element:3d}", end=" ")
    print()

# 矩阵加法
print("矩阵A + B：")
result = []
for i in range(len(matrix_a)):
    row = []
    for j in range(len(matrix_a[i])):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(row)

for row in result:
    for element in row:
        print(f"{element:3d}", end=" ")
    print()
print()

print("3.3 查找矩阵中的最大值")
matrix = [[3, 7, 1], [9, 2, 8], [4, 6, 5]]
print("矩阵：")
for row in matrix:
    for element in row:
        print(f"{element:3d}", end=" ")
    print()

max_value = matrix[0][0]
max_row = 0
max_col = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row = i
            max_col = j

print(f"最大值：{max_value}，位置：({max_row}, {max_col})")
print()

# 4. 图案生成
print("=== 4. 图案生成 ===")
print()

print("4.1 星号三角形")
print("直角三角形：")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
print()

print("等腰三角形：")
for i in range(1, 6):
    # 打印空格
    for j in range(5 - i):
        print(" ", end="")
    # 打印星号
    for j in range(2 * i - 1):
        print("*", end="")
    print()
print()

print("4.2 数字图案")
print("数字三角形：")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print()

print("递增数字图案：")
num = 1
for i in range(1, 5):
    for j in range(i):
        print(f"{num:2d}", end=" ")
        num += 1
    print()
print()

print("4.3 棋盘图案")
print("8×8棋盘：")
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("■", end="")
        else:
            print("□", end="")
    print()
print()

print("4.4 菱形图案")
size = 5
print(f"{size}×{size}菱形：")

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

# 5. 查找和搜索
print("=== 5. 查找和搜索 ===")
print()

print("5.1 二维列表中查找元素")
matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
target = 5

print("矩阵：")
for row in matrix:
    for element in row:
        print(f"{element:3d}", end=" ")
    print()

print(f"查找元素 {target}：")
found = False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print(f"找到 {target} 在位置 ({i}, {j})")
            found = True
            break
    if found:
        break

if not found:
    print(f"未找到元素 {target}")
print()

print("5.2 查找所有匹配元素")
matrix = [[1, 2, 3], [2, 4, 2], [3, 2, 1]]
target = 2

print("矩阵：")
for row in matrix:
    for element in row:
        print(f"{element:3d}", end=" ")
    print()

print(f"查找所有 {target}：")
positions = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            positions.append((i, j))
            print(f"找到 {target} 在位置 ({i}, {j})")

print(f"总共找到 {len(positions)} 个匹配元素")
print()

# 6. 组合和排列
print("=== 6. 组合和排列 ===")
print()

print("6.1 生成所有两位数组合")
print("所有两位数组合（十位 > 个位）：")
count = 0
for tens in range(1, 10):  # 十位数字1-9
    for ones in range(0, tens):  # 个位数字小于十位
        number = tens * 10 + ones
        print(f"{number:2d}", end=" ")
        count += 1
        if count % 10 == 0:
            print()  # 每10个换行
print(f"\n总共 {count} 个组合")
print()

print("6.2 生成密码组合")
print("3位数字密码（每位不同）：")
passwords = []
for first in range(10):
    for second in range(10):
        if second != first:
            for third in range(10):
                if third != first and third != second:
                    password = f"{first}{second}{third}"
                    passwords.append(password)

print(f"前20个密码：{passwords[:20]}")
print(f"总共可能的密码数量：{len(passwords)}")
print()

print("6.3 字符串排列")
chars = "ABC"
print(f"字符串 '{chars}' 的所有排列：")
permutations = []

for i in chars:
    for j in chars:
        if j != i:
            for k in chars:
                if k != i and k != j:
                    perm = i + j + k
                    permutations.append(perm)
                    print(perm, end=" ")
print(f"\n总共 {len(permutations)} 种排列")
print()

# 7. 游戏应用
print("=== 7. 游戏应用 ===")
print()

print("7.1 井字棋游戏板")
# 创建3×3游戏板
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(' ')
    board.append(row)

# 模拟一些棋子
board[0][0] = 'X'
board[0][1] = 'O'
board[1][1] = 'X'
board[2][2] = 'O'

print("井字棋游戏板：")
for i in range(3):
    for j in range(3):
        print(f" {board[i][j]} ", end="")
        if j < 2:
            print("|", end="")
    print()
    if i < 2:
        print("-----------")
print()

print("7.2 检查获胜条件")
def check_winner(board):
    # 检查行
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] != ' '):
            return board[i][0]
    
    # 检查列
    for j in range(3):
        if (board[0][j] == board[1][j] == board[2][j] != ' '):
            return board[0][j]
    
    # 检查对角线
    if (board[0][0] == board[1][1] == board[2][2] != ' '):
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0] != ' '):
        return board[0][2]
    
    return None

winner = check_winner(board)
if winner:
    print(f"获胜者：{winner}")
else:
    print("游戏继续")
print()

# 8. 性能考虑
print("=== 8. 性能考虑 ===")
print()

print("8.1 嵌套循环的时间复杂度")
print("测试不同规模的嵌套循环性能：")

sizes = [10, 50, 100]
for size in sizes:
    start_time = time.time()
    
    count = 0
    for i in range(size):
        for j in range(size):
            count += 1
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"规模 {size}×{size}：执行 {count} 次操作，耗时 {duration:.6f} 秒")
print()

print("8.2 优化技巧 - 提前退出")
print("在大矩阵中查找第一个偶数：")

# 创建大矩阵
size = 1000
big_matrix = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(random.randint(1, 1000))
    big_matrix.append(row)

# 在中间位置放一个偶数
big_matrix[500][500] = 42

start_time = time.time()
found = False
operations = 0

for i in range(size):
    for j in range(size):
        operations += 1
        if big_matrix[i][j] % 2 == 0:
            print(f"找到第一个偶数 {big_matrix[i][j]} 在位置 ({i}, {j})")
            found = True
            break
    if found:
        break

end_time = time.time()
print(f"执行了 {operations} 次操作，耗时 {end_time - start_time:.6f} 秒")
print()

# 9. 实际应用
print("=== 9. 实际应用 ===")
print()

print("9.1 学生成绩统计")
# 模拟学生成绩数据：3个学生，4门课程
students = ["张三", "李四", "王五"]
subjects = ["数学", "语文", "英语", "物理"]
scores = [
    [85, 92, 78, 88],  # 张三的成绩
    [90, 87, 95, 82],  # 李四的成绩
    [78, 85, 88, 90]   # 王五的成绩
]

print("学生成绩表：")
print("姓名\t", end="")
for subject in subjects:
    print(f"{subject}\t", end="")
print("平均分")

for i in range(len(students)):
    print(f"{students[i]}\t", end="")
    total = 0
    for j in range(len(subjects)):
        score = scores[i][j]
        print(f"{score}\t", end="")
        total += score
    average = total / len(subjects)
    print(f"{average:.1f}")

print("\n科目平均分：")
for j in range(len(subjects)):
    total = 0
    for i in range(len(students)):
        total += scores[i][j]
    average = total / len(students)
    print(f"{subjects[j]}：{average:.1f}分")
print()

print("9.2 图像处理模拟")
print("模拟简单的图像滤镜处理：")

# 创建5×5的"图像"（灰度值0-255）
image = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(random.randint(0, 255))
    image.append(row)

print("原始图像：")
for row in image:
    for pixel in row:
        print(f"{pixel:3d}", end=" ")
    print()

# 应用简单的模糊滤镜（3×3平均）
blurred = []
for i in range(5):
    row = []
    for j in range(5):
        # 计算周围像素的平均值
        total = 0
        count = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ni, nj = i + di, j + dj
                if 0 <= ni < 5 and 0 <= nj < 5:
                    total += image[ni][nj]
                    count += 1
        row.append(total // count)
    blurred.append(row)

print("\n模糊处理后：")
for row in blurred:
    for pixel in row:
        print(f"{pixel:3d}", end=" ")
    print()
print()

# 10. 综合练习
print("=== 10. 综合练习 ===")
print()

print("10.1 生成帕斯卡三角形")
n = 6
print(f"{n}行帕斯卡三角形：")

for i in range(n):
    # 打印前导空格
    for j in range(n - i - 1):
        print(" ", end="")
    
    # 计算并打印这一行的数字
    for j in range(i + 1):
        if j == 0 or j == i:
            value = 1
        else:
            # 帕斯卡三角形的性质：C(i,j) = C(i-1,j-1) + C(i-1,j)
            # 这里用简化计算
            value = 1
            for k in range(j):
                value = value * (i - k) // (k + 1)
        
        print(f"{value:2d}", end=" ")
    print()
print()

print("10.2 数独验证器")
# 简化的3×3数独
sudoku = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
]

print("数独网格：")
for row in sudoku:
    for num in row:
        print(f"{num} ", end="")
    print()

# 验证行
valid_rows = True
for i in range(3):
    row_nums = []
    for j in range(3):
        if sudoku[i][j] in row_nums:
            valid_rows = False
            break
        row_nums.append(sudoku[i][j])
    if not valid_rows:
        break

# 验证列
valid_cols = True
for j in range(3):
    col_nums = []
    for i in range(3):
        if sudoku[i][j] in col_nums:
            valid_cols = False
            break
        col_nums.append(sudoku[i][j])
    if not valid_cols:
        break

print(f"行验证：{'通过' if valid_rows else '失败'}")
print(f"列验证：{'通过' if valid_cols else '失败'}")
print(f"数独有效性：{'有效' if valid_rows and valid_cols else '无效'}")
print()

if __name__ == "__main__":
    print("=== 嵌套循环学习总结 ===")
    print("通过本节学习，你应该掌握了：")
    print("1. 嵌套循环的基本概念和语法")
    print("2. 二维数据结构的处理方法")
    print("3. 图案和图形的生成技巧")
    print("4. 查找和搜索算法的实现")
    print("5. 组合和排列问题的解决")
    print("6. 游戏逻辑的编程实现")
    print("7. 性能优化的基本考虑")
    print("8. 实际问题的嵌套循环应用")
    print("\n继续练习这些概念，你将能够熟练运用嵌套循环解决复杂的编程问题！")
```

## 注意事项

1. **时间复杂度**：嵌套循环的时间复杂度通常是O(n²)或更高
2. **提前退出**：使用break语句可以提高效率
3. **内存使用**：处理大型二维数据时注意内存消耗
4. **可读性**：保持代码清晰，适当添加注释

## 练习建议

1. 实现各种图案生成算法
2. 练习二维列表的操作和处理
3. 编写简单的游戏逻辑
4. 实现基本的搜索和排序算法
5. 解决组合数学问题

通过大量练习，你将能够熟练掌握嵌套循环，这是处理复杂数据结构和算法的重要基础。