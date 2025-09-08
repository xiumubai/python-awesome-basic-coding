# 嵌套列表和多维列表

## 学习目标

通过本节学习，你将掌握：
- 嵌套列表的创建和初始化方法
- 访问和修改嵌套列表元素的技巧
- 二维列表（矩阵）的各种操作
- 三维和多维列表的处理方法
- 嵌套列表的遍历和处理算法
- 实际应用场景和性能优化

## 基本概念

嵌套列表是指列表中包含其他列表作为元素的数据结构。它可以用来表示多维数据，如矩阵、表格、游戏地图等。

### 关键特点
- **多维结构**：可以创建二维、三维甚至更高维度的数据结构
- **灵活性**：每个子列表可以有不同的长度
- **索引访问**：使用多重索引访问元素
- **内存效率**：需要注意浅拷贝和深拷贝的区别

## 创建嵌套列表

### 基本创建方法

```python
# 直接创建二维列表
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"直接创建的矩阵: {matrix1}")

# 使用列表推导式创建
matrix2 = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
print(f"推导式创建的矩阵: {matrix2}")

# 使用循环创建
matrix3 = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i + j)
    matrix3.append(row)
print(f"循环创建的矩阵: {matrix3}")
```

### 避免浅拷贝陷阱

```python
# ❌ 错误的创建方式（浅拷贝问题）
wrong_matrix = [[0] * 3] * 3  # 所有行都是同一个对象
wrong_matrix[0][0] = 1
print(f"错误矩阵: {wrong_matrix}")  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# ✅ 正确的创建方式
correct_matrix = [[0] * 3 for _ in range(3)]  # 每行都是独立对象
correct_matrix[0][0] = 1
print(f"正确矩阵: {correct_matrix}")  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### 不规则嵌套列表

```python
# 不规则嵌套列表
irregular_list = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
print(f"不规则嵌套列表: {irregular_list}")

# 混合数据类型的嵌套列表
mixed_list = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
print(f"混合数据类型: {mixed_list}")
```

## 访问嵌套列表元素

### 基本访问方法

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 基本访问
print(f"第一行: {matrix[0]}")                    # [1, 2, 3, 4]
print(f"第一行第一列: {matrix[0][0]}")            # 1
print(f"第二行第三列: {matrix[1][2]}")            # 7
print(f"最后一行最后一列: {matrix[-1][-1]}")      # 12
```

### 切片访问

```python
# 切片访问
print(f"前两行: {matrix[:2]}")
print(f"每行的前两列: {[row[:2] for row in matrix]}")
print(f"第二列: {[row[1] for row in matrix]}")
```

### 安全访问

```python
def safe_get(matrix, row, col, default=None):
    """安全获取矩阵元素"""
    try:
        return matrix[row][col]
    except (IndexError, TypeError):
        return default

print(f"安全访问存在的元素: {safe_get(matrix, 1, 2)}")      # 7
print(f"安全访问不存在的元素: {safe_get(matrix, 10, 10, 'N/A')}")  # N/A
```

## 修改嵌套列表

### 基本修改操作

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 修改单个元素
matrix[1][1] = 99
print(f"修改中心元素后: {matrix}")

# 修改整行
matrix[0] = [10, 20, 30]
print(f"修改第一行后: {matrix}")

# 修改整列
for i in range(len(matrix)):
    matrix[i][2] = i * 10
print(f"修改第三列后: {matrix}")
```

### 添加和删除操作

```python
# 添加行
matrix.append([40, 50, 60])
print(f"添加行后: {matrix}")

# 添加列
for row in matrix:
    row.append(0)
print(f"添加列后: {matrix}")

# 删除行
del matrix[0]
print(f"删除第一行后: {matrix}")

# 删除列
for row in matrix:
    del row[1]
print(f"删除第二列后: {matrix}")
```

## 矩阵操作

### 矩阵运算

```python
# 矩阵加法
def matrix_add(m1, m2):
    """矩阵加法"""
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result

# 矩阵转置
def matrix_transpose(matrix):
    """矩阵转置"""
    return [[matrix[j][i] for j in range(len(matrix))] 
            for i in range(len(matrix[0]))]

# 矩阵乘法
def matrix_multiply(m1, m2):
    """矩阵乘法"""
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            sum_val = 0
            for k in range(len(m2)):
                sum_val += m1[i][k] * m2[k][j]
            row.append(sum_val)
        result.append(row)
    return result
```

### 矩阵统计

```python
# 查找矩阵中的最大值和最小值
def matrix_min_max(matrix):
    """查找矩阵的最大值和最小值"""
    flat = [element for row in matrix for element in row]
    return min(flat), max(flat)

# 矩阵求和
def matrix_sum(matrix):
    """计算矩阵所有元素的和"""
    return sum(sum(row) for row in matrix)
```

## 三维列表操作

### 创建和访问三维列表

```python
# 创建三维列表（立方体）
cube = [[[i + j + k for k in range(2)] for j in range(2)] for i in range(2)]
print(f"2x2x2立方体: {cube}")

# 更直观的三维列表
classroom = [
    [  # 第一层（第一个班级）
        ['Alice', 'Bob'],      # 第一排
        ['Charlie', 'Diana']   # 第二排
    ],
    [  # 第二层（第二个班级）
        ['Eve', 'Frank'],      # 第一排
        ['Grace', 'Henry']     # 第二排
    ]
]

# 访问三维列表元素
print(f"第一个班级第一排第一个学生: {classroom[0][0][0]}")
print(f"第二个班级第二排第二个学生: {classroom[1][1][1]}")
```

### 遍历三维列表

```python
# 遍历三维列表
for class_idx, classroom_class in enumerate(classroom):
    print(f"班级 {class_idx + 1}:")
    for row_idx, row in enumerate(classroom_class):
        print(f"  第{row_idx + 1}排: {row}")
        for seat_idx, student in enumerate(row):
            print(f"    座位{seat_idx + 1}: {student}")
```

## 嵌套列表遍历

### 递归遍历

```python
def recursive_traverse(lst, depth=0):
    """递归遍历嵌套列表"""
    indent = "  " * depth
    for i, item in enumerate(lst):
        if isinstance(item, list):
            print(f"{indent}索引{i}: [列表]")
            recursive_traverse(item, depth + 1)
        else:
            print(f"{indent}索引{i}: {item}")

complex_nested = [
    [1, 2, [3, 4]],
    [5, [6, 7, [8, 9]]],
    [10, 11, 12]
]

recursive_traverse(complex_nested)
```

### 扁平化处理

```python
# 递归扁平化
def flatten_list(lst):
    """扁平化嵌套列表"""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

# 使用生成器扁平化
def flatten_generator(lst):
    """使用生成器扁平化"""
    for item in lst:
        if isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item

flattened = flatten_list(complex_nested)
gen_flattened = list(flatten_generator(complex_nested))
```

### 深度计算和路径查找

```python
# 计算嵌套深度
def calculate_depth(lst):
    """计算嵌套列表的最大深度"""
    if not isinstance(lst, list):
        return 0
    if not lst:
        return 1
    return 1 + max(calculate_depth(item) for item in lst)

# 查找特定元素的路径
def find_path(lst, target, path=[]):
    """查找元素在嵌套列表中的路径"""
    for i, item in enumerate(lst):
        current_path = path + [i]
        if item == target:
            return current_path
        elif isinstance(item, list):
            result = find_path(item, target, current_path)
            if result:
                return result
    return None
```

## 实际应用场景

### 学生成绩管理

```python
students_grades = [
    ['Alice', [85, 92, 78, 96]],
    ['Bob', [88, 85, 90, 87]],
    ['Charlie', [92, 89, 94, 91]]
]

for student, grades in students_grades:
    average = sum(grades) / len(grades)
    print(f"{student}: 成绩{grades}, 平均分{average:.1f}")
```

### 购物车系统

```python
shopping_cart = [
    ['Electronics', [
        ['Laptop', 1000, 1],
        ['Mouse', 25, 2]
    ]],
    ['Books', [
        ['Python Guide', 30, 1],
        ['Data Science', 45, 1]
    ]]
]

total_cost = 0
for category, items in shopping_cart:
    print(f"{category}:")
    category_cost = 0
    for item_name, price, quantity in items:
        item_cost = price * quantity
        category_cost += item_cost
        print(f"  {item_name}: ${price} x {quantity} = ${item_cost}")
    print(f"  {category}小计: ${category_cost}")
    total_cost += category_cost
print(f"总计: ${total_cost}")
```

### 游戏地图

```python
game_map = [
    ['#', '#', '#', '#', '#'],  # 墙
    ['#', '.', '.', '.', '#'],  # 空地
    ['#', '.', 'P', '.', '#'],  # 玩家位置
    ['#', '.', '.', 'E', '#'],  # 敌人位置
    ['#', '#', '#', '#', '#']   # 墙
]

# 显示地图
for row in game_map:
    print(' '.join(row))

# 查找特定符号的位置
def find_positions(game_map, symbol):
    """查找地图中特定符号的位置"""
    positions = []
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell == symbol:
                positions.append((x, y))
    return positions

player_pos = find_positions(game_map, 'P')
enemy_pos = find_positions(game_map, 'E')
```

### 数据表格处理

```python
data_table = [
    ['Name', 'Age', 'City', 'Salary'],
    ['Alice', 25, 'New York', 50000],
    ['Bob', 30, 'London', 60000],
    ['Charlie', 35, 'Tokyo', 70000]
]

headers = data_table[0]
data_rows = data_table[1:]

# 打印表格
print(' | '.join(f"{header:>10}" for header in headers))
print('-' * (len(headers) * 13 - 1))
for row in data_rows:
    print(' | '.join(f"{str(cell):>10}" for cell in row))

# 计算平均工资
salary_column = 3
salaries = [row[salary_column] for row in data_rows]
avg_salary = sum(salaries) / len(salaries)
print(f"平均工资: ${avg_salary:,.0f}")
```

## 学习要点

### 关键概念
1. **嵌套结构**：理解多层列表的组织方式
2. **索引访问**：掌握多重索引的使用方法
3. **浅拷贝陷阱**：避免创建时的常见错误
4. **递归处理**：学会处理不规则嵌套结构

### 操作技巧
1. **创建方法**：选择合适的创建方式
2. **访问模式**：使用安全访问避免错误
3. **遍历策略**：根据需求选择遍历方法
4. **修改操作**：理解行列操作的区别

### 性能考虑
1. **访问效率**：按行访问比按列访问更快
2. **内存使用**：避免不必要的深拷贝
3. **算法选择**：列表推导式通常比循环更快
4. **数据规模**：大数据集考虑使用NumPy

### 常见陷阱
1. **浅拷贝问题**：`[[0] * 3] * 3`会创建相同的行对象
2. **索引错误**：访问不存在的索引会抛出异常
3. **内存泄漏**：大型嵌套结构要及时清理
4. **性能问题**：过深的嵌套会影响访问效率

## 练习建议

1. **基础练习**：
   - 创建不同大小的矩阵
   - 实现矩阵的基本运算
   - 练习多种遍历方法

2. **进阶练习**：
   - 实现矩阵转置和乘法
   - 创建三维数据结构
   - 编写递归遍历函数

3. **应用练习**：
   - 设计学生成绩管理系统
   - 实现简单的游戏地图
   - 处理CSV格式的表格数据

4. **性能练习**：
   - 比较不同创建方法的效率
   - 测试访问模式的性能差异
   - 优化大型嵌套结构的处理

通过这些练习，你将能够熟练掌握嵌套列表的各种操作，并能在实际项目中灵活运用这些技巧。