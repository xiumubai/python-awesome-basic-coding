#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
循环控制 - 技巧和最佳实践

本文件包含循环控制的高级技巧、性能优化和最佳实践，
帮助编写更高效、更可读的循环代码。

学习目标：
1. 掌握循环控制的高级技巧
2. 了解循环性能优化方法
3. 学习循环代码的最佳实践
4. 避免常见的循环陷阱和错误
"""

# 1. 循环优化技巧
print("=== 1. 循环优化技巧 ===")

# 技巧1: 减少循环内的计算
print("优化前 - 循环内重复计算:")
import time

data = list(range(1000))
start_time = time.time()

result1 = []
for i in data:
    if i % 2 == 0 and len(str(i)) > 1:  # 每次都计算len(str(i))
        result1.append(i)

time1 = time.time() - start_time
print(f"耗时: {time1:.6f}秒，结果数量: {len(result1)}")

print("\n优化后 - 预计算和缓存:")
start_time = time.time()

result2 = []
for i in data:
    if i % 2 == 0:
        str_i = str(i)  # 只计算一次
        if len(str_i) > 1:
            result2.append(i)

time2 = time.time() - start_time
print(f"耗时: {time2:.6f}秒，结果数量: {len(result2)}")
print(f"性能提升: {((time1 - time2) / time1 * 100):.1f}%\n")

# 技巧2: 使用enumerate而不是range(len())
print("使用enumerate优化索引访问:")
items = ['apple', 'banana', 'cherry', 'date']

# 不推荐的方式
print("不推荐的方式:")
for i in range(len(items)):
    print(f"索引 {i}: {items[i]}")

print("\n推荐的方式:")
for i, item in enumerate(items):
    print(f"索引 {i}: {item}")
print()

# 技巧3: 使用zip处理多个列表
print("使用zip处理多个列表:")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
scores = [85, 92, 78]

# 不推荐的方式
print("不推荐的方式:")
for i in range(len(names)):
    print(f"{names[i]}, {ages[i]}岁, 分数: {scores[i]}")

print("\n推荐的方式:")
for name, age, score in zip(names, ages, scores):
    print(f"{name}, {age}岁, 分数: {score}")
print()

# 2. 循环控制模式
print("=== 2. 循环控制模式 ===")

# 模式1: 早期退出模式
print("早期退出模式 - 找到第一个满足条件的元素:")
numbers = [1, 3, 8, 15, 22, 35]

for num in numbers:
    if num > 10:
        print(f"找到第一个大于10的数: {num}")
        break
    print(f"检查: {num}")
print()

# 模式2: 计数器模式
print("计数器模式 - 限制处理数量:")
data = list(range(100))
max_process = 5
processed = 0

for item in data:
    if processed >= max_process:
        print(f"已处理{max_process}个项目，停止处理")
        break
    
    if item % 7 == 0:  # 只处理7的倍数
        print(f"处理项目: {item}")
        processed += 1
print()

# 模式3: 状态机模式
print("状态机模式 - 解析简单协议:")
commands = ['START', 'DATA', '123', 'DATA', '456', 'END', 'IGNORE']
state = 'WAITING'
data_items = []

for command in commands:
    if state == 'WAITING':
        if command == 'START':
            print("开始接收数据")
            state = 'RECEIVING'
    elif state == 'RECEIVING':
        if command == 'DATA':
            print("准备接收数据项")
            state = 'DATA_EXPECTED'
        elif command == 'END':
            print("数据接收完成")
            state = 'FINISHED'
            break
    elif state == 'DATA_EXPECTED':
        print(f"接收数据: {command}")
        data_items.append(command)
        state = 'RECEIVING'

print(f"接收到的数据: {data_items}\n")

# 3. 嵌套循环优化
print("=== 3. 嵌套循环优化 ===")

# 优化嵌套循环的break使用
print("使用标志变量控制嵌套循环:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5
found = False

for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value == target:
            print(f"在位置 ({i}, {j}) 找到目标值 {target}")
            found = True
            break
    if found:
        break
else:
    print(f"未找到目标值 {target}")
print()

# 使用函数简化嵌套循环控制
print("使用函数简化嵌套循环控制:")
def find_in_matrix(matrix, target):
    """在矩阵中查找目标值"""
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == target:
                return (i, j)
    return None

result = find_in_matrix(matrix, 8)
if result:
    print(f"在位置 {result} 找到目标值 8")
else:
    print("未找到目标值 8")
print()

# 4. 循环中的异常处理
print("=== 4. 循环中的异常处理 ===")

# 处理可能出错的操作
print("循环中的异常处理:")
data = ['10', '20', 'abc', '30', '40']
valid_numbers = []
error_count = 0

for item in data:
    try:
        number = int(item)
        valid_numbers.append(number)
        print(f"转换成功: {item} -> {number}")
    except ValueError:
        error_count += 1
        print(f"转换失败: {item} (错误 #{error_count})")
        
        # 如果错误太多，可以选择退出
        if error_count >= 2:
            print("错误过多，停止处理")
            break
        continue

print(f"有效数字: {valid_numbers}")
print(f"错误数量: {error_count}\n")

# 5. 循环性能监控
print("=== 5. 循环性能监控 ===")

# 监控循环进度
print("循环进度监控:")
import time

large_data = list(range(50))
total_items = len(large_data)
processed_items = 0
start_time = time.time()

for i, item in enumerate(large_data):
    # 模拟处理时间
    time.sleep(0.01)
    
    processed_items += 1
    
    # 每10个项目报告一次进度
    if (i + 1) % 10 == 0 or i == total_items - 1:
        elapsed_time = time.time() - start_time
        progress = (processed_items / total_items) * 100
        print(f"进度: {progress:.1f}% ({processed_items}/{total_items}), 耗时: {elapsed_time:.2f}秒")

print()

# 6. 循环内存优化
print("=== 6. 循环内存优化 ===")

# 使用生成器表达式而不是列表推导式
print("内存优化 - 使用生成器:")

# 内存占用大的方式
print("列表推导式 (占用更多内存):")
large_list = [x * 2 for x in range(10)]
print(f"列表内容: {large_list}")

# 内存优化的方式
print("\n生成器表达式 (节省内存):")
large_gen = (x * 2 for x in range(10))
print("生成器对象:", large_gen)
print("逐个获取值:")
for i, value in enumerate(large_gen):
    print(f"第{i+1}个值: {value}")
    if i >= 4:  # 只取前5个值
        print("提前退出，节省计算")
        break
print()

# 7. 循环调试技巧
print("=== 7. 循环调试技巧 ===")

# 添加调试信息
print("循环调试技巧:")
data = [1, 2, 3, 4, 5]
DEBUG = True

for i, value in enumerate(data):
    if DEBUG:
        print(f"[DEBUG] 循环 {i}: 处理值 {value}")
    
    result = value * 2
    
    if DEBUG and result > 6:
        print(f"[DEBUG] 结果 {result} 超过阈值")
    
    if result > 6:
        print(f"处理结果: {result}")
print()

# 8. 循环最佳实践总结
print("=== 8. 循环最佳实践总结 ===")

# 实践1: 选择合适的循环类型
print("选择合适的循环类型:")

# 已知迭代次数 - 使用for
print("已知次数 - for循环:")
for i in range(3):
    print(f"迭代 {i}")

# 条件控制 - 使用while
print("\n条件控制 - while循环:")
count = 0
while count < 3:
    print(f"计数 {count}")
    count += 1
print()

# 实践2: 避免无限循环
print("避免无限循环的技巧:")
max_iterations = 1000
iteration = 0
value = 100

while value > 1:
    value = value // 2
    iteration += 1
    
    # 安全检查
    if iteration >= max_iterations:
        print(f"达到最大迭代次数 {max_iterations}，强制退出")
        break
    
    print(f"迭代 {iteration}: value = {value}")

print(f"循环完成，最终值: {value}\n")

# 实践3: 使用有意义的变量名
print("使用有意义的变量名:")
student_scores = [85, 92, 78, 96, 88]
passing_grade = 80
passed_students = 0

for student_index, score in enumerate(student_scores):
    if score >= passing_grade:
        passed_students += 1
        print(f"学生 {student_index + 1}: {score}分 (通过)")
    else:
        print(f"学生 {student_index + 1}: {score}分 (未通过)")

print(f"通过人数: {passed_students}/{len(student_scores)}")

print("\n=== 循环控制技巧学习总结 ===")
print("1. 优化循环内的计算，避免重复操作")
print("2. 使用enumerate、zip等内置函数简化代码")
print("3. 合理使用break和continue控制流程")
print("4. 在嵌套循环中使用标志变量或函数")
print("5. 添加异常处理和安全检查")
print("6. 监控循环性能和进度")
print("7. 选择合适的数据结构和算法")
print("8. 使用有意义的变量名提高可读性")