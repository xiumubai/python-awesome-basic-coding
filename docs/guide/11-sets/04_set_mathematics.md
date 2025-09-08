# 集合的数学运算

## 学习目标

通过本节学习，你将掌握：
- 集合的四种基本数学运算：并集、交集、差集、对称差集
- 运算符与方法的区别和使用场景
- 就地运算的概念和应用
- 集合运算的数学性质
- 复合运算和实际应用场景

## 集合数学运算概述

集合支持四种基本的数学运算，这些运算在数据处理、逻辑分析等场景中非常有用：

- **并集（Union）**：包含两个集合中所有不重复的元素
- **交集（Intersection）**：两个集合共有的元素
- **差集（Difference）**：在第一个集合但不在第二个集合中的元素
- **对称差集（Symmetric Difference）**：在两个集合中但不在交集中的元素

## 1. 并集运算（Union）

并集包含两个或多个集合中的所有不重复元素。

### 基本用法

```python
# 准备测试数据
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {1, 3, 5, 7, 9}

print(f"集合A: {set_a}")
print(f"集合B: {set_b}")
print(f"集合C: {set_c}")

# 使用 | 操作符
union_operator = set_a | set_b
print(f"A | B = {union_operator}")

# 使用 union() 方法
union_method = set_a.union(set_b)
print(f"A.union(B) = {union_method}")
```

**输出结果：**
```
集合A: {1, 2, 3, 4, 5}
集合B: {4, 5, 6, 7, 8}
集合C: {1, 3, 5, 7, 9}
A | B = {1, 2, 3, 4, 5, 6, 7, 8}
A.union(B) = {1, 2, 3, 4, 5, 6, 7, 8}
```

### 多个集合的并集

```python
# 多个集合的并集
union_multiple = set_a | set_b | set_c
print(f"A | B | C = {union_multiple}")

# 使用方法的多参数形式
union_multiple_method = set_a.union(set_b, set_c)
print(f"A.union(B, C) = {union_multiple_method}")

# 与其他可迭代对象的并集
union_with_list = set_a.union([10, 11, 12])
print(f"A.union([10, 11, 12]) = {union_with_list}")
```

**输出结果：**
```
A | B | C = {1, 2, 3, 4, 5, 6, 7, 8, 9}
A.union(B, C) = {1, 2, 3, 4, 5, 6, 7, 8, 9}
A.union([10, 11, 12]) = {1, 2, 3, 4, 5, 10, 11, 12}
```

## 2. 交集运算（Intersection）

交集包含两个或多个集合共有的元素。

### 基本用法

```python
# 使用 & 操作符
intersection_operator = set_a & set_b
print(f"A & B = {intersection_operator}")

# 使用 intersection() 方法
intersection_method = set_a.intersection(set_b)
print(f"A.intersection(B) = {intersection_method}")

# 多个集合的交集
intersection_multiple = set_a & set_b & set_c
print(f"A & B & C = {intersection_multiple}")

intersection_multiple_method = set_a.intersection(set_b, set_c)
print(f"A.intersection(B, C) = {intersection_multiple_method}")
```

**输出结果：**
```
A & B = {4, 5}
A.intersection(B) = {4, 5}
A & B & C = {5}
A.intersection(B, C) = {5}
```

### 空交集示例

```python
# 没有共同元素的集合
set_d = {10, 11, 12}
empty_intersection = set_a & set_d
print(f"A & {{10, 11, 12}} = {empty_intersection}")
print(f"空交集的类型: {type(empty_intersection)}")
```

**输出结果：**
```
A & {10, 11, 12} = set()
空交集的类型: <class 'set'>
```

## 3. 差集运算（Difference）

差集包含在第一个集合但不在第二个集合中的元素。

### 基本用法

```python
# 使用 - 操作符
difference_operator = set_a - set_b
print(f"A - B = {difference_operator}")
print(f"B - A = {set_b - set_a}")

# 使用 difference() 方法
difference_method = set_a.difference(set_b)
print(f"A.difference(B) = {difference_method}")

# 注意：差集不满足交换律
print(f"A - B == B - A: {(set_a - set_b) == (set_b - set_a)}")
```

**输出结果：**
```
A - B = {1, 2, 3}
B - A = {6, 7, 8}
A.difference(B) = {1, 2, 3}
A - B == B - A: False
```

### 多个集合的差集

```python
# 连续差集运算
difference_multiple = set_a - set_b - set_c
print(f"A - B - C = {difference_multiple}")

# 使用方法的多参数形式
difference_multiple_method = set_a.difference(set_b, set_c)
print(f"A.difference(B, C) = {difference_multiple_method}")
```

**输出结果：**
```
A - B - C = {2}
A.difference(B, C) = {2}
```

## 4. 对称差集运算（Symmetric Difference）

对称差集包含在两个集合中但不在交集中的元素。

### 基本用法

```python
# 使用 ^ 操作符
symmetric_diff_operator = set_a ^ set_b
print(f"A ^ B = {symmetric_diff_operator}")

# 使用 symmetric_difference() 方法
symmetric_diff_method = set_a.symmetric_difference(set_b)
print(f"A.symmetric_difference(B) = {symmetric_diff_method}")

# 对称差集的等价表达式
manual_symmetric_diff = (set_a - set_b) | (set_b - set_a)
print(f"(A - B) | (B - A) = {manual_symmetric_diff}")
print(f"验证：A ^ B == (A - B) | (B - A): {symmetric_diff_operator == manual_symmetric_diff}")
```

**输出结果：**
```
A ^ B = {1, 2, 3, 6, 7, 8}
A.symmetric_difference(B) = {1, 2, 3, 6, 7, 8}
(A - B) | (B - A) = {1, 2, 3, 6, 7, 8}
验证：A ^ B == (A - B) | (B - A): True
```

## 5. 运算符 vs 方法的区别

### 类型限制

```python
# 运算符只能用于集合
try:
    result = set_a | [1, 2, 3]  # 这会报错
except TypeError as e:
    print(f"运算符与列表操作报错: {e}")

# 方法可以接受任何可迭代对象
result_method = set_a.union([1, 2, 3])
print(f"方法可以接受列表: {result_method}")

# 方法还可以接受字符串、元组等
result_string = set_a.union("abc")
print(f"方法可以接受字符串: {result_string}")

result_tuple = set_a.union((10, 20, 30))
print(f"方法可以接受元组: {result_tuple}")
```

**输出结果：**
```
运算符与列表操作报错: unsupported operand type(s) for |: 'set' and 'list'
方法可以接受列表: {1, 2, 3, 4, 5}
方法可以接受字符串: {1, 2, 3, 4, 5, 'a', 'b', 'c'}
方法可以接受元组: {1, 2, 3, 4, 5, 10, 20, 30}
```

### 性能和可读性

```python
# 运算符更简洁，适合集合间操作
result1 = set_a | set_b & set_c  # 注意运算符优先级
result2 = set_a | (set_b & set_c)  # 明确优先级

# 方法更明确，适合复杂操作
result3 = set_a.union(set_b.intersection(set_c))

print(f"运算符结果: {result1}")
print(f"加括号结果: {result2}")
print(f"方法结果: {result3}")
```

## 6. 就地运算（修改原集合）

就地运算会直接修改原集合，而不是创建新集合。

### 就地并集

```python
# 就地并集 |=
test_set = {1, 2, 3}
print(f"原集合: {test_set}")
test_set |= {4, 5, 6}
print(f"就地并集后: {test_set}")

# 使用update()方法（等同于|=）
test_set.update({7, 8})
print(f"使用update()后: {test_set}")
```

### 就地交集

```python
# 就地交集 &=
test_set &= {1, 2, 3, 4, 5}
print(f"就地交集后: {test_set}")

# 使用intersection_update()方法
test_set.intersection_update({1, 2, 3})
print(f"使用intersection_update()后: {test_set}")
```

### 就地差集

```python
# 就地差集 -=
test_set -= {2}
print(f"就地差集后: {test_set}")

# 使用difference_update()方法
test_set.difference_update({3})
print(f"使用difference_update()后: {test_set}")
```

### 就地对称差集

```python
# 就地对称差集 ^=
test_set ^= {1, 5, 6}
print(f"就地对称差集后: {test_set}")

# 使用symmetric_difference_update()方法
test_set.symmetric_difference_update({5, 7})
print(f"使用symmetric_difference_update()后: {test_set}")
```

**输出结果：**
```
原集合: {1, 2, 3}
就地并集后: {1, 2, 3, 4, 5, 6}
使用update()后: {1, 2, 3, 4, 5, 6, 7, 8}
就地交集后: {1, 2, 3, 4, 5}
使用intersection_update()后: {1, 2, 3}
就地差集后: {1, 3}
使用difference_update()后: {1}
就地对称差集后: {5, 6}
使用symmetric_difference_update()后: {6, 7}
```

## 7. 集合运算的数学性质

### 交换律

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 并集和交集满足交换律
print(f"并集交换律: A | B == B | A: {A | B == B | A}")
print(f"交集交换律: A & B == B & A: {A & B == B & A}")

# 差集不满足交换律
print(f"差集交换律: A - B == B - A: {A - B == B - A}")

# 对称差集满足交换律
print(f"对称差集交换律: A ^ B == B ^ A: {A ^ B == B ^ A}")
```

### 结合律

```python
C = {5, 6, 7, 8}

# 并集和交集满足结合律
print(f"并集结合律: (A | B) | C == A | (B | C): {(A | B) | C == A | (B | C)}")
print(f"交集结合律: (A & B) & C == A & (B & C): {(A & B) & C == A & (B & C)}")
```

### 分配律

```python
# 交集对并集的分配律
result1 = A & (B | C)
result2 = (A & B) | (A & C)
print(f"交集对并集的分配律: A & (B | C) == (A & B) | (A & C): {result1 == result2}")

# 并集对交集的分配律
result3 = A | (B & C)
result4 = (A | B) & (A | C)
print(f"并集对交集的分配律: A | (B & C) == (A | B) & (A | C): {result3 == result4}")
```

## 8. 复杂运算示例

### 学生选课分析

```python
# 多个集合的复合运算
students_math = {"Alice", "Bob", "Charlie", "David"}
students_physics = {"Bob", "Charlie", "Eve", "Frank"}
students_chemistry = {"Alice", "Charlie", "Frank", "Grace"}

print(f"数学课学生: {students_math}")
print(f"物理课学生: {students_physics}")
print(f"化学课学生: {students_chemistry}")

# 至少选修一门课的学生
all_students = students_math | students_physics | students_chemistry
print(f"至少选修一门课的学生: {all_students}")

# 三门课都选修的学生
all_three = students_math & students_physics & students_chemistry
print(f"三门课都选修的学生: {all_three}")

# 只选修数学课的学生
only_math = students_math - students_physics - students_chemistry
print(f"只选修数学课的学生: {only_math}")

# 选修数学和物理但不选化学的学生
math_physics_not_chemistry = (students_math & students_physics) - students_chemistry
print(f"选修数学和物理但不选化学的学生: {math_physics_not_chemistry}")

# 恰好选修两门课的学生
exactly_two = ((students_math & students_physics) - students_chemistry) | \
              ((students_math & students_chemistry) - students_physics) | \
              ((students_physics & students_chemistry) - students_math)
print(f"恰好选修两门课的学生: {exactly_two}")
```

## 9. 实际应用场景

### 权限管理系统

```python
# 权限管理
admin_permissions = {"read", "write", "delete", "admin"}
user_permissions = {"read", "write"}
guest_permissions = {"read"}

print("权限管理系统:")
print(f"管理员权限: {admin_permissions}")
print(f"用户权限: {user_permissions}")
print(f"访客权限: {guest_permissions}")

# 检查用户缺少的权限
missing_permissions = admin_permissions - user_permissions
print(f"用户缺少的权限: {missing_permissions}")

# 检查共同权限
common_permissions = user_permissions & guest_permissions
print(f"用户和访客的共同权限: {common_permissions}")

# 权限升级（添加新权限）
upgraded_permissions = user_permissions | {"execute"}
print(f"升级后的用户权限: {upgraded_permissions}")
```

### 客户数据分析

```python
# 客户数据分析
customers_2023 = {"Alice", "Bob", "Charlie", "David", "Eve"}
customers_2024 = {"Bob", "Charlie", "Frank", "Grace", "Henry"}

print(f"2023年客户: {customers_2023}")
print(f"2024年客户: {customers_2024}")

# 回头客户（两年都有）
returning_customers = customers_2023 & customers_2024
print(f"回头客户: {returning_customers}")

# 流失客户（2023有但2024没有）
lost_customers = customers_2023 - customers_2024
print(f"流失客户: {lost_customers}")

# 新客户（2024有但2023没有）
new_customers = customers_2024 - customers_2023
print(f"新客户: {new_customers}")

# 总客户数
total_customers = customers_2023 | customers_2024
print(f"总客户数: {len(total_customers)}")

# 客户保留率
retention_rate = len(returning_customers) / len(customers_2023) * 100
print(f"客户保留率: {retention_rate:.1f}%")
```

### 标签系统

```python
# 文章标签分析
article1_tags = {"python", "programming", "tutorial", "beginner"}
article2_tags = {"python", "web", "django", "advanced"}
article3_tags = {"javascript", "web", "frontend", "tutorial"}

print(f"文章1标签: {article1_tags}")
print(f"文章2标签: {article2_tags}")
print(f"文章3标签: {article3_tags}")

# 找到所有标签
all_tags = article1_tags | article2_tags | article3_tags
print(f"所有标签: {all_tags}")

# 找到共同标签
common_tags = article1_tags & article2_tags & article3_tags
print(f"三篇文章的共同标签: {common_tags}")

# 找到Python相关文章的标签
python_articles_tags = article1_tags | article2_tags
print(f"Python相关文章的所有标签: {python_articles_tags}")

# 找到Web相关但不是Python的标签
web_not_python_tags = (article2_tags | article3_tags) - article1_tags
print(f"Web相关但不是Python的标签: {web_not_python_tags}")
```

## 运行完整代码

你可以运行以下完整代码来查看所有示例：

```bash
python3 03_set_mathematics.py
```

## 学习要点

1. **四种基本运算**：
   - 并集（`|` 或 `union()`）：所有元素的合集
   - 交集（`&` 或 `intersection()`）：共同元素
   - 差集（`-` 或 `difference()`）：独有元素
   - 对称差集（`^` 或 `symmetric_difference()`）：非共同元素

2. **运算符 vs 方法**：
   - 运算符：简洁，只能用于集合间操作
   - 方法：灵活，可接受任何可迭代对象

3. **就地运算**：
   - `|=`, `&=`, `-=`, `^=`：修改原集合
   - 对应方法：`update()`, `intersection_update()`, `difference_update()`, `symmetric_difference_update()`

4. **数学性质**：
   - 交换律：并集、交集、对称差集满足
   - 结合律：并集、交集满足
   - 分配律：交集对并集、并集对交集都满足

5. **实际应用**：
   - 数据分析：客户分析、用户行为分析
   - 权限管理：权限检查、权限升级
   - 内容管理：标签系统、分类系统

## 最佳实践

1. **选择合适的运算方式**：
   - 集合间操作优先使用运算符
   - 与其他类型数据操作使用方法
   - 需要修改原集合时使用就地运算

2. **注意运算符优先级**：
   - `&` 的优先级高于 `|`
   - 复杂表达式使用括号明确优先级

3. **性能考虑**：
   - 就地运算比创建新集合更节省内存
   - 大数据集操作时优先考虑就地运算

4. **代码可读性**：
   - 复杂逻辑使用方法链而不是嵌套运算符
   - 为复杂运算添加注释说明业务逻辑

通过掌握集合的数学运算，你可以高效地处理各种数据分析和逻辑判断任务。