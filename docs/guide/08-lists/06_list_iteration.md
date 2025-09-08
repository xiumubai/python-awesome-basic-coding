# 列表遍历

## 学习目标

通过本节学习，你将掌握：
- Python中遍历列表的各种方法
- 使用enumerate()和zip()函数进行高级遍历
- 反向遍历和条件遍历技巧
- 嵌套列表的遍历方法
- 高级遍历模式和性能优化

## 基本遍历方法

### 1. 直接遍历元素

最简单和常用的遍历方式：

```python
fruits = ['apple', 'banana', 'orange', 'grape']

# 直接遍历元素
for fruit in fruits:
    print(fruit)
```

### 2. 使用索引遍历

当需要访问元素索引时：

```python
# 使用range()和len()
for i in range(len(fruits)):
    print(f"索引{i}: {fruits[i]}")

# 使用while循环
i = 0
while i < len(fruits):
    print(f"索引{i}: {fruits[i]}")
    i += 1
```

## 使用enumerate()函数

`enumerate()`函数同时返回索引和元素，是最优雅的遍历方式：

```python
colors = ['red', 'green', 'blue', 'yellow']

# 基本用法
for index, color in enumerate(colors):
    print(f"索引{index}: {color}")

# 指定起始索引
for index, color in enumerate(colors, 1):
    print(f"第{index}个颜色: {color}")

# 实际应用：查找特定元素的所有位置
numbers = [1, 3, 2, 3, 4, 3, 5]
target = 3
positions = []

for index, number in enumerate(numbers):
    if number == target:
        positions.append(index)

print(f"数字{target}的所有位置: {positions}")  # [1, 3, 5]
```

## 使用zip()函数同时遍历多个列表

`zip()`函数可以同时遍历多个列表：

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['New York', 'London', 'Tokyo']

# 同时遍历多个列表
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}岁, 住在{city}")

# 创建字典
person_dict = dict(zip(['name', 'age', 'city'], ['David', 28, 'Paris']))
print(person_dict)  # {'name': 'David', 'age': 28, 'city': 'Paris'}

# zip的逆操作
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(letters)  # ('a', 'b', 'c')
print(numbers)  # (1, 2, 3)
```

## 反向遍历

### 使用reversed()函数

```python
numbers = [1, 2, 3, 4, 5]

# 使用reversed()
for num in reversed(numbers):
    print(num)  # 5, 4, 3, 2, 1

# 使用切片
for num in numbers[::-1]:
    print(num)  # 5, 4, 3, 2, 1

# 反向enumerate
for index, num in enumerate(reversed(numbers)):
    original_index = len(numbers) - 1 - index
    print(f"反向索引{index}(原索引{original_index}): {num}")
```

## 条件遍历

### 基本条件遍历

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 遍历偶数
for num in numbers:
    if num % 2 == 0:
        print(f"偶数: {num}")

# 使用列表推导式过滤
large_numbers = [num for num in numbers if num > 5]
for num in large_numbers:
    print(f"大数: {num}")

# 使用filter()函数
odd_numbers = filter(lambda x: x % 2 == 1, numbers)
for num in odd_numbers:
    print(f"奇数: {num}")
```

### 复杂条件遍历

```python
students = [
    {'name': 'Alice', 'grade': 85, 'subject': 'Math'},
    {'name': 'Bob', 'grade': 92, 'subject': 'Science'},
    {'name': 'Charlie', 'grade': 78, 'subject': 'Math'},
    {'name': 'Diana', 'grade': 96, 'subject': 'Science'}
]

# 条件遍历
for student in students:
    if student['subject'] == 'Math' and student['grade'] >= 85:
        print(f"{student['name']}: {student['grade']}分")
```

## 嵌套列表遍历

### 二维列表遍历

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 遍历所有元素
for row in matrix:
    for element in row:
        print(element, end=' ')

# 使用索引遍历
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

# 使用enumerate遍历
for row_idx, row in enumerate(matrix):
    for col_idx, element in enumerate(row):
        print(f"位置({row_idx},{col_idx}): {element}")
```

### 三维列表遍历

```python
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

for i, plane in enumerate(cube):
    for j, row in enumerate(plane):
        for k, element in enumerate(row):
            print(f"cube[{i}][{j}][{k}] = {element}")
```

### 不规则嵌套列表

```python
irregular = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]

for i, sublist in enumerate(irregular):
    print(f"子列表{i} (长度{len(sublist)}): ", end='')
    for element in sublist:
        print(f"{element} ", end='')
    print()  # 换行
```

## 高级遍历模式

### 分组遍历

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
group_size = 3

for i in range(0, len(numbers), group_size):
    group = numbers[i:i + group_size]
    print(f"组{i//group_size + 1}: {group}")
```

### 滑动窗口遍历

```python
window_size = 3
for i in range(len(numbers) - window_size + 1):
    window = numbers[i:i + window_size]
    print(f"窗口{i+1}: {window}")
```

### 配对遍历

```python
# 相邻元素配对
for i in range(len(numbers) - 1):
    pair = (numbers[i], numbers[i + 1])
    print(f"配对{i+1}: {pair}")
```

### 使用itertools进行高级遍历

```python
import itertools

letters = ['A', 'B', 'C']

# 排列
for perm in itertools.permutations(letters, 2):
    print(perm)  # ('A', 'B'), ('A', 'C'), ('B', 'A'), ...

# 组合
for comb in itertools.combinations(letters, 2):
    print(comb)  # ('A', 'B'), ('A', 'C'), ('B', 'C')
```

### 扁平化遍历

```python
nested_list = [[1, 2], [3, [4, 5]], [6, 7, [8, [9, 10]]]]

def flatten_and_iterate(lst):
    """递归扁平化并遍历嵌套列表"""
    for item in lst:
        if isinstance(item, list):
            yield from flatten_and_iterate(item)
        else:
            yield item

for item in flatten_and_iterate(nested_list):
    print(item)  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

## 完整示例代码

```python
def demonstrate_all_iterations():
    """演示所有遍历方法"""
    
    # 基本数据
    fruits = ['apple', 'banana', 'orange']
    numbers = [1, 2, 3, 4, 5]
    
    print("=== 基本遍历 ===")
    for fruit in fruits:
        print(fruit)
    
    print("\n=== enumerate遍历 ===")
    for i, fruit in enumerate(fruits):
        print(f"{i}: {fruit}")
    
    print("\n=== zip遍历 ===")
    for fruit, num in zip(fruits, numbers):
        print(f"{fruit} - {num}")
    
    print("\n=== 反向遍历 ===")
    for fruit in reversed(fruits):
        print(fruit)
    
    print("\n=== 条件遍历 ===")
    for num in numbers:
        if num % 2 == 0:
            print(f"偶数: {num}")
    
    # 嵌套列表
    matrix = [[1, 2], [3, 4], [5, 6]]
    print("\n=== 嵌套遍历 ===")
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

if __name__ == "__main__":
    demonstrate_all_iterations()
```

## 学习要点

### 关键概念

1. **直接遍历**：最简单高效的方式
2. **索引遍历**：需要索引信息时使用
3. **enumerate()**：同时获取索引和元素
4. **zip()**：同时遍历多个序列
5. **条件遍历**：结合条件判断进行筛选

### 方法选择指南

| 场景 | 推荐方法 | 原因 |
|------|----------|------|
| 只需要元素值 | `for item in list` | 最简洁高效 |
| 需要索引和元素 | `enumerate(list)` | 优雅且高效 |
| 遍历多个列表 | `zip(list1, list2)` | 自动处理长度 |
| 反向遍历 | `reversed(list)` | 内存效率高 |
| 条件筛选 | 列表推导式或filter | 简洁明了 |
| 嵌套结构 | 多层循环或递归 | 根据结构选择 |

### 性能考虑

1. **直接遍历**通常最快
2. **避免不必要的索引访问**
3. **使用生成器**节省内存
4. **列表推导式**适合创建新列表
5. **生成器表达式**内存效率高

### 常见陷阱

1. **修改正在遍历的列表**
```python
# 错误：遍历时删除元素
for item in my_list:
    if condition:
        my_list.remove(item)  # 可能跳过元素

# 正确：反向遍历或创建新列表
for i in range(len(my_list) - 1, -1, -1):
    if condition:
        del my_list[i]
```

2. **zip()长度不一致**
```python
# zip会在最短列表结束时停止
list1 = [1, 2, 3]
list2 = [4, 5]  # 较短
for a, b in zip(list1, list2):
    print(a, b)  # 只输出 (1,4) 和 (2,5)
```

3. **enumerate起始值**
```python
# 注意enumerate的起始值
for i, item in enumerate(items, 1):  # 从1开始
    print(f"第{i}个: {item}")
```

## 练习建议

### 基础练习

1. 使用不同方法遍历一个数字列表
2. 同时遍历姓名和年龄两个列表
3. 反向打印一个字符串列表
4. 找出列表中所有偶数的位置

### 进阶练习

1. 遍历二维矩阵并计算每行的和
2. 实现一个函数，扁平化任意嵌套的列表
3. 使用滑动窗口计算移动平均值
4. 比较不同遍历方法的性能

### 实战练习

1. 处理学生成绩数据，按条件筛选和统计
2. 遍历文件路径列表，分类不同类型的文件
3. 实现一个通用的数据表格遍历器
4. 创建一个支持多种遍历模式的列表工具类

通过掌握这些遍历方法，你将能够高效地处理各种列表操作任务！