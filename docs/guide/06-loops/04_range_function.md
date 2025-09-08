# range函数详解

range函数是Python中生成数字序列的内置函数，它经常与for循环配合使用。range函数生成的是一个可迭代对象，可以高效地产生指定范围内的整数序列。

## 基本语法

range函数有三种调用方式：

```python
# 方式1：只指定结束值
range(stop)

# 方式2：指定开始值和结束值
range(start, stop)

# 方式3：指定开始值、结束值和步长
range(start, stop, step)
```

## 学习要点

### 1. 基础用法

最简单的range使用：

```python
# 生成0到4的数字
for i in range(5):
    print(i)  # 输出：0, 1, 2, 3, 4

# 生成2到6的数字
for i in range(2, 7):
    print(i)  # 输出：2, 3, 4, 5, 6

# 生成1到10的奇数
for i in range(1, 11, 2):
    print(i)  # 输出：1, 3, 5, 7, 9
```

### 2. 负数步长

使用负数步长实现倒序：

```python
# 倒序输出5到1
for i in range(5, 0, -1):
    print(i)  # 输出：5, 4, 3, 2, 1

# 倒序输出偶数
for i in range(10, 0, -2):
    print(i)  # 输出：10, 8, 6, 4, 2
```

### 3. 与列表结合

range常用于访问列表元素：

```python
fruits = ["苹果", "香蕉", "橙子"]

# 通过索引访问
for i in range(len(fruits)):
    print(f"索引{i}: {fruits[i]}")

# 反向遍历
for i in range(len(fruits)-1, -1, -1):
    print(f"倒序索引{i}: {fruits[i]}")
```

### 4. 转换为列表

将range对象转换为列表：

```python
# 转换为列表查看内容
numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]

even_numbers = list(range(0, 11, 2))
print(even_numbers)  # [0, 2, 4, 6, 8, 10]
```

## 完整代码示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python循环 - range函数详解

本文件详细介绍range函数的各种用法和应用场景。
range函数是Python中生成数字序列的重要工具，
经常与for循环配合使用。

主要内容：
1. range函数的三种参数形式
2. 基本用法和常见模式
3. 负数步长和倒序生成
4. 与列表索引的结合使用
5. 实际应用场景
6. 性能特点和注意事项

作者：Python学习教程
日期：2024年
"""

# 1. range函数基本语法
print("=== 1. range函数基本语法 ===")
print()

print("1.1 单参数形式：range(stop)")
print("range(5) 生成 0 到 4：")
for i in range(5):
    print(f"  {i}", end=" ")
print("\n")

print("1.2 双参数形式：range(start, stop)")
print("range(2, 8) 生成 2 到 7：")
for i in range(2, 8):
    print(f"  {i}", end=" ")
print("\n")

print("1.3 三参数形式：range(start, stop, step)")
print("range(1, 10, 2) 生成 1 到 9 的奇数：")
for i in range(1, 10, 2):
    print(f"  {i}", end=" ")
print("\n")

print("1.4 查看range对象")
r = range(1, 6)
print(f"range对象：{r}")
print(f"转换为列表：{list(r)}")
print(f"range的长度：{len(r)}")
print(f"range的起始值：{r.start}")
print(f"range的结束值：{r.stop}")
print(f"range的步长：{r.step}")
print()

# 2. 不同步长的使用
print("=== 2. 不同步长的使用 ===")
print()

print("2.1 步长为2（偶数）")
print("range(0, 11, 2) 生成偶数：")
even_numbers = []
for i in range(0, 11, 2):
    even_numbers.append(i)
    print(f"  {i}", end=" ")
print(f"\n偶数列表：{even_numbers}")
print()

print("2.2 步长为3")
print("range(0, 20, 3) 每隔3个数取一个：")
for i in range(0, 20, 3):
    print(f"  {i}", end=" ")
print("\n")

print("2.3 步长为5")
print("range(5, 51, 5) 生成5的倍数：")
multiples_of_5 = list(range(5, 51, 5))
print(f"5的倍数：{multiples_of_5}")
print()

# 3. 负数步长和倒序
print("=== 3. 负数步长和倒序 ===")
print()

print("3.1 基本倒序")
print("range(5, 0, -1) 从5倒数到1：")
for i in range(5, 0, -1):
    print(f"  {i}", end=" ")
print("\n")

print("3.2 倒序偶数")
print("range(10, -1, -2) 从10开始的倒序偶数：")
for i in range(10, -1, -2):
    print(f"  {i}", end=" ")
print("\n")

print("3.3 倒序遍历列表索引")
fruits = ["苹果", "香蕉", "橙子", "葡萄", "草莓"]
print(f"水果列表：{fruits}")
print("倒序输出：")
for i in range(len(fruits) - 1, -1, -1):
    print(f"  索引{i}: {fruits[i]}")
print()

# 4. 与列表索引结合
print("=== 4. 与列表索引结合 ===")
print()

print("4.1 正向遍历索引")
colors = ["红色", "绿色", "蓝色", "黄色"]
print(f"颜色列表：{colors}")
print("通过索引访问：")
for i in range(len(colors)):
    print(f"  索引{i}: {colors[i]}")
print()

print("4.2 部分索引遍历")
print("只遍历前3个元素：")
for i in range(min(3, len(colors))):
    print(f"  索引{i}: {colors[i]}")
print()

print("4.3 跳跃式访问")
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"数字列表：{numbers}")
print("每隔一个元素访问：")
for i in range(0, len(numbers), 2):
    print(f"  索引{i}: {numbers[i]}")
print()

print("4.4 同时遍历多个列表")
names = ["张三", "李四", "王五"]
ages = [25, 30, 28]
scores = [85, 92, 78]

print("学生信息：")
for i in range(len(names)):
    print(f"  {names[i]}，{ages[i]}岁，分数：{scores[i]}")
print()

# 5. 实际应用场景
print("=== 5. 实际应用场景 ===")
print()

print("5.1 生成乘法表")
print("3x3乘法表：")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i}×{j}={result:2d}", end="  ")
    print()  # 换行
print()

print("5.2 计算平方数")
print("1到10的平方数：")
squares = []
for i in range(1, 11):
    square = i ** 2
    squares.append(square)
    print(f"  {i}² = {square}")
print(f"平方数列表：{squares}")
print()

print("5.3 生成等差数列")
print("首项为3，公差为4的等差数列（前8项）：")
first_term = 3
common_diff = 4
n_terms = 8

arithmetic_sequence = []
for i in range(n_terms):
    term = first_term + i * common_diff
    arithmetic_sequence.append(term)
    print(f"  第{i+1}项: {term}")
print(f"等差数列：{arithmetic_sequence}")
print()

print("5.4 字符串索引操作")
text = "Python编程"
print(f"字符串：{text}")
print("正向遍历字符：")
for i in range(len(text)):
    print(f"  索引{i}: '{text[i]}'")

print("反向遍历字符：")
for i in range(len(text) - 1, -1, -1):
    print(f"  索引{i}: '{text[i]}'")
print()

# 6. 高级技巧
print("=== 6. 高级技巧 ===")
print()

print("6.1 跳过某些元素")
numbers = list(range(1, 21))  # 1到20
print(f"原始列表：{numbers}")
print("跳过能被3整除的数：")
filtered = []
for i in range(len(numbers)):
    if numbers[i] % 3 != 0:
        filtered.append(numbers[i])
        print(f"  保留：{numbers[i]}")
print(f"过滤后：{filtered}")
print()

print("6.2 分组处理")
data = list(range(1, 13))  # 1到12
print(f"数据：{data}")
print("按3个一组处理：")
for i in range(0, len(data), 3):
    group = data[i:i+3]
    print(f"  第{i//3 + 1}组：{group}")
print()

print("6.3 创建坐标点")
print("创建3x3网格的坐标点：")
coordinates = []
for x in range(3):
    for y in range(3):
        coord = (x, y)
        coordinates.append(coord)
        print(f"  坐标：{coord}")
print(f"所有坐标：{coordinates}")
print()

# 7. 与其他函数结合
print("=== 7. 与其他函数结合 ===")
print()

print("7.1 与enumerate结合")
fruits = ["苹果", "香蕉", "橙子"]
print(f"水果列表：{fruits}")
print("使用enumerate：")
for i, fruit in enumerate(fruits):
    print(f"  索引{i}: {fruit}")

print("使用range：")
for i in range(len(fruits)):
    print(f"  索引{i}: {fruits[i]}")
print()

print("7.2 与zip结合")
names = ["张三", "李四", "王五"]
ages = [25, 30, 28]

print("使用zip：")
for name, age in zip(names, ages):
    print(f"  {name}: {age}岁")

print("使用range：")
for i in range(min(len(names), len(ages))):
    print(f"  {names[i]}: {ages[i]}岁")
print()

print("7.3 与sum结合进行数学计算")
print("计算1到100的和：")
total1 = sum(range(1, 101))
print(f"使用sum(range(1, 101))：{total1}")

# 验证结果
total2 = 0
for i in range(1, 101):
    total2 += i
print(f"使用循环累加验证：{total2}")
print(f"结果一致：{total1 == total2}")
print()

print("计算1到10的平方和：")
square_sum = sum(i**2 for i in range(1, 11))
print(f"1²+2²+...+10² = {square_sum}")
print()

# 8. 性能和内存特点
print("=== 8. 性能和内存特点 ===")
print()

print("8.1 range对象的惰性求值")
large_range = range(1000000)
print(f"创建range(1000000)：{large_range}")
print(f"range对象大小很小，不会立即生成所有数字")
print(f"只有在迭代时才会生成具体的数字")
print()

print("8.2 内存效率对比")
print("range对象 vs 列表：")
print(f"range(1000): 占用内存很少")
print(f"list(range(1000)): 占用更多内存")
print("建议：在循环中直接使用range，避免转换为列表")
print()

# 9. 综合练习
print("=== 9. 综合练习 ===")
print()

print("9.1 打印数字金字塔")
n = 5
print(f"打印{n}层数字金字塔：")
for i in range(1, n + 1):
    # 打印空格
    for j in range(n - i):
        print(" ", end="")
    # 打印数字
    for j in range(1, i + 1):
        print(j, end="")
    # 打印反向数字
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()  # 换行
print()

print("9.2 生成质数")
n = 30
print(f"生成小于{n}的所有质数：")
primes = []
for num in range(2, n):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
        print(f"  质数：{num}")
print(f"质数列表：{primes}")
print()

print("9.3 矩阵转置")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("原始矩阵：")
for row in matrix:
    print(f"  {row}")

print("转置矩阵：")
transposed = []
for j in range(len(matrix[0])):  # 列数
    new_row = []
    for i in range(len(matrix)):  # 行数
        new_row.append(matrix[i][j])
    transposed.append(new_row)
    print(f"  {new_row}")
print()

if __name__ == "__main__":
    print("=== range函数学习总结 ===")
    print("通过本节学习，你应该掌握了：")
    print("1. range函数的三种参数形式和基本用法")
    print("2. 正向和反向数字序列的生成")
    print("3. range与列表索引的结合使用")
    print("4. range在实际编程中的各种应用")
    print("5. range对象的性能特点和内存效率")
    print("6. range与其他Python函数的结合使用")
    print("\n继续练习这些概念，你将能够熟练运用range函数解决各种数值序列问题！")
```

## 注意事项

1. **左闭右开区间**：range(1, 5)生成1,2,3,4，不包含5
2. **步长不能为0**：会引发ValueError异常
3. **内存效率**：range对象不会立即生成所有数字，节省内存
4. **类型转换**：需要列表时使用list(range())转换

## 练习建议

1. 练习三种参数形式的不同用法
2. 实现各种数字序列生成（等差数列、倍数等）
3. 结合列表索引进行复杂的数据处理
4. 使用负步长实现倒序操作
5. 在嵌套循环中灵活运用range函数

通过大量练习，你将能够熟练掌握range函数的各种用法，这是Python编程中非常重要的基础技能。