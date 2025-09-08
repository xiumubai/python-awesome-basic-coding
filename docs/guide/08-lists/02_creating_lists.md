# 列表创建

本节介绍Python中创建列表的各种方法，从基础的方括号语法到高级的列表推导式，帮助你掌握灵活创建列表的技巧。

## 学习目标

- 掌握使用方括号创建列表的基本语法
- 学会使用`list()`函数转换其他数据类型为列表
- 理解`range()`函数在列表创建中的应用
- 掌握列表推导式的基本用法
- 了解列表复制的不同方法和注意事项
- 学会创建特殊类型的列表（嵌套列表、混合类型等）

## 基本列表创建方法

### 1. 使用方括号创建列表

最基本和常用的列表创建方法：

```python
# 创建空列表
empty_list1 = []
empty_list2 = list()
print(f"空列表1: {empty_list1}")  # []
print(f"空列表2: {empty_list2}")  # []
print(f"两个空列表相等: {empty_list1 == empty_list2}")  # True

# 创建包含元素的列表
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
mixed = [1, 'hello', 3.14, True]

print(f"数字列表: {numbers}")
print(f"水果列表: {fruits}")
print(f"混合类型列表: {mixed}")
```

### 2. 使用重复操作符创建列表

```python
# 使用重复操作符创建列表
zeros = [0] * 5
pattern = ['a', 'b'] * 3

print(f"重复创建 - 零列表: {zeros}")      # [0, 0, 0, 0, 0]
print(f"重复创建 - 模式列表: {pattern}")   # ['a', 'b', 'a', 'b', 'a', 'b']
```

**注意事项**：使用重复操作符时，如果列表包含可变对象，所有元素都会引用同一个对象。

## 使用list()函数创建列表

`list()`函数可以将其他可迭代对象转换为列表：

### 1. 从字符串创建列表

```python
# 从字符串创建列表
string_to_list = list("hello")
print(f"字符串转列表: {string_to_list}")  # ['h', 'e', 'l', 'l', 'o']
```

### 2. 从其他数据类型创建列表

```python
# 从元组创建列表
tuple_data = (1, 2, 3, 4)
tuple_to_list = list(tuple_data)
print(f"元组转列表: {tuple_to_list}")  # [1, 2, 3, 4]

# 从集合创建列表
set_data = {3, 1, 4, 1, 5}
set_to_list = list(set_data)
print(f"集合转列表: {set_to_list}")  # [1, 3, 4, 5] (顺序可能不同)

# 从字典创建列表
dict_data = {'a': 1, 'b': 2, 'c': 3}
keys_list = list(dict_data.keys())
values_list = list(dict_data.values())
items_list = list(dict_data.items())

print(f"字典键转列表: {keys_list}")    # ['a', 'b', 'c']
print(f"字典值转列表: {values_list}")  # [1, 2, 3]
print(f"字典项转列表: {items_list}")   # [('a', 1), ('b', 2), ('c', 3)]
```

## 使用range()创建数字列表

`range()`函数是创建数字序列列表的强大工具：

### 1. 基本range用法

```python
# 基本range用法
range_list1 = list(range(5))        # [0, 1, 2, 3, 4]
range_list2 = list(range(1, 6))     # [1, 2, 3, 4, 5]
range_list3 = list(range(0, 10, 2)) # [0, 2, 4, 6, 8]
range_list4 = list(range(10, 0, -1))# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(f"range(5): {range_list1}")
print(f"range(1, 6): {range_list2}")
print(f"range(0, 10, 2): {range_list3}")
print(f"range(10, 0, -1): {range_list4}")
```

### 2. 创建特殊数字序列

```python
# 创建特殊数字序列
even_numbers = list(range(0, 21, 2))    # 偶数
odd_numbers = list(range(1, 21, 2))     # 奇数
multiples_of_5 = list(range(0, 51, 5))  # 5的倍数

print(f"偶数列表(0-20): {even_numbers}")
print(f"奇数列表(1-19): {odd_numbers}")
print(f"5的倍数(0-50): {multiples_of_5}")
```

## 使用列表推导式创建列表

列表推导式是Python中创建列表的优雅方式：

### 1. 基本列表推导式

```python
# 基本列表推导式
squares = [x**2 for x in range(1, 6)]
print(f"平方数列表: {squares}")  # [1, 4, 9, 16, 25]
```

### 2. 带条件的列表推导式

```python
# 带条件的列表推导式
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"偶数的平方: {even_squares}")  # [4, 16, 36, 64, 100]
```

### 3. 字符串处理

```python
# 字符串处理
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
word_lengths = [len(word) for word in words]

print(f"大写单词: {upper_words}")   # ['HELLO', 'WORLD', 'PYTHON']
print(f"单词长度: {word_lengths}")   # [5, 5, 6]
```

### 4. 嵌套列表推导式

```python
# 嵌套列表推导式
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"乘法表矩阵: {matrix}")
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

## 创建特殊类型的列表

### 1. 嵌套列表

```python
# 嵌套列表
nested_list = [[1, 2], [3, 4], [5, 6]]
print(f"嵌套列表: {nested_list}")

# 创建二维列表（矩阵）
rows, cols = 3, 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print(f"3x4零矩阵: {matrix}")
```

### 2. 混合类型列表

```python
# 包含不同数据类型的列表
mixed_types = [42, 'hello', [1, 2, 3], {'key': 'value'}, (1, 2)]
print(f"混合类型列表: {mixed_types}")
```

### 3. 使用函数创建列表

```python
import random

# 使用函数创建列表
random_numbers = [random.randint(1, 100) for _ in range(5)]
print(f"随机数列表: {random_numbers}")

# 创建包含函数的列表
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

functions = [square, cube, lambda x: x * 2]
print("函数列表应用到数字5:")
for i, func in enumerate(functions):
    print(f"函数{i+1}(5) = {func(5)}")
```

## 列表复制方法

理解列表复制的不同方法对于避免意外的引用问题很重要：

### 1. 浅复制方法

```python
original = [1, 2, 3, 4, 5]

# 浅复制方法
copy1 = original.copy()    # 使用copy()方法
copy2 = original[:]        # 使用切片
copy3 = list(original)     # 使用list()函数

print(f"原始列表: {original}")
print(f"copy()方法: {copy1}")
print(f"切片复制: {copy2}")
print(f"list()复制: {copy3}")

# 验证是否为不同对象
print(f"copy1 is original: {copy1 is original}")  # False
print(f"copy1 == original: {copy1 == original}")  # True
```

### 2. 深复制（对于嵌套列表）

```python
import copy

nested_original = [[1, 2], [3, 4]]
shallow_copy = nested_original.copy()
deep_copy = copy.deepcopy(nested_original)

print(f"嵌套列表原始: {nested_original}")
print(f"浅复制: {shallow_copy}")
print(f"深复制: {deep_copy}")

# 修改嵌套列表测试
nested_original[0][0] = 999
print("修改原始列表后:")
print(f"原始列表: {nested_original}")  # [[999, 2], [3, 4]]
print(f"浅复制: {shallow_copy}")      # [[999, 2], [3, 4]] - 受影响
print(f"深复制: {deep_copy}")        # [[1, 2], [3, 4]] - 不受影响
```

## 完整示例代码

```python
def demonstrate_all_creation_methods():
    """演示所有列表创建方法"""
    print("Python列表创建方法大全")
    print("=" * 50)
    
    # 1. 基本创建
    basic_list = [1, 2, 3]
    empty_list = []
    
    # 2. 使用list()函数
    from_string = list("hello")
    from_range = list(range(5))
    
    # 3. 列表推导式
    squares = [x**2 for x in range(5)]
    filtered = [x for x in range(10) if x % 2 == 0]
    
    # 4. 特殊列表
    nested = [[i, i*2] for i in range(3)]
    repeated = [0] * 5
    
    print(f"基本列表: {basic_list}")
    print(f"空列表: {empty_list}")
    print(f"从字符串: {from_string}")
    print(f"从range: {from_range}")
    print(f"平方数: {squares}")
    print(f"偶数: {filtered}")
    print(f"嵌套列表: {nested}")
    print(f"重复列表: {repeated}")

if __name__ == "__main__":
    demonstrate_all_creation_methods()
```

## 学习要点

### 关键概念
1. **列表的可变性**：列表是可变对象，可以修改其内容
2. **浅复制vs深复制**：理解引用和拷贝的区别
3. **列表推导式**：简洁高效的列表创建方式
4. **类型灵活性**：列表可以包含不同类型的元素

### 最佳实践
1. **选择合适的创建方法**：根据需求选择最清晰的方式
2. **注意复制陷阱**：理解浅复制和深复制的区别
3. **使用列表推导式**：在适当时候使用以提高代码简洁性
4. **避免重复操作符陷阱**：创建嵌套列表时要小心

### 常见错误
1. **重复操作符误用**：`[[0] * 3] * 3` 会创建引用同一个列表的列表
2. **浅复制问题**：修改嵌套列表时影响原列表
3. **类型混淆**：忘记`range()`返回的不是列表，需要用`list()`转换

## 练习建议

1. **基础练习**：
   - 创建包含1-100所有偶数的列表
   - 将字符串"Python"转换为字符列表
   - 创建一个3x3的零矩阵

2. **进阶练习**：
   - 使用列表推导式创建九九乘法表
   - 创建包含前10个斐波那契数的列表
   - 从字典创建包含所有键值对的列表

3. **实战练习**：
   - 创建学生成绩管理的数据结构
   - 生成随机数据用于测试
   - 实现不同的列表初始化策略

通过掌握这些列表创建方法，你将能够灵活地根据不同场景选择最合适的方式来创建和初始化列表。