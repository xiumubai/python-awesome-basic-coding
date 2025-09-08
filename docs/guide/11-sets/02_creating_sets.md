# 创建集合

## 学习目标

通过本节学习，你将掌握：
- 使用花括号创建集合的方法
- 使用set()函数创建集合
- 从其他数据类型创建集合
- 理解集合的唯一性和无序性特征
- 掌握集合在数据去重中的应用

## 集合的基本概念

集合（Set）是Python中的一种数据类型，具有以下特点：
- **唯一性**：集合中不能有重复元素
- **无序性**：集合中的元素没有固定的顺序
- **可变性**：可以添加和删除元素（frozenset除外）
- **可哈希元素**：集合中的元素必须是可哈希的（如数字、字符串、元组）

## 创建集合的方法

### 1. 使用花括号创建集合

最直观的创建集合的方法是使用花括号 `{}`：

```python
# 创建包含数字的集合
numbers = {1, 2, 3, 4, 5}
print(f"数字集合: {numbers}")
print(f"集合类型: {type(numbers)}")

# 创建包含字符串的集合
fruits = {"apple", "banana", "orange", "grape"}
print(f"水果集合: {fruits}")

# 创建混合类型的集合
mixed = {1, "hello", 3.14, True}
print(f"混合类型集合: {mixed}")
```

**输出结果：**
```
数字集合: {1, 2, 3, 4, 5}
集合类型: <class 'set'>
水果集合: {'banana', 'orange', 'apple', 'grape'}
混合类型集合: {1, 3.14, 'hello'}
```

### 2. 使用set()函数创建集合

`set()` 函数可以将其他可迭代对象转换为集合：

```python
# 从列表创建集合
list_data = [1, 2, 3, 4, 5, 3, 2, 1]  # 包含重复元素
set_from_list = set(list_data)
print(f"原始列表: {list_data}")
print(f"从列表创建的集合: {set_from_list}")
print("注意：重复元素被自动去除")

# 从字符串创建集合
string_data = "hello world"
set_from_string = set(string_data)
print(f"原始字符串: '{string_data}'")
print(f"从字符串创建的集合: {set_from_string}")
print("注意：每个字符成为集合的一个元素")

# 从元组创建集合
tuple_data = (1, 2, 3, 2, 1, 4)
set_from_tuple = set(tuple_data)
print(f"原始元组: {tuple_data}")
print(f"从元组创建的集合: {set_from_tuple}")
```

**输出结果：**
```
原始列表: [1, 2, 3, 4, 5, 3, 2, 1]
从列表创建的集合: {1, 2, 3, 4, 5}
注意：重复元素被自动去除

原始字符串: 'hello world'
从字符串创建的集合: {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}
注意：每个字符成为集合的一个元素

原始元组: (1, 2, 3, 2, 1, 4)
从元组创建的集合: {1, 2, 3, 4}
```

### 3. 创建空集合

创建空集合需要特别注意：

```python
# 正确的方式：使用set()
empty_set = set()
print(f"空集合: {empty_set}")
print(f"空集合类型: {type(empty_set)}")
print(f"空集合长度: {len(empty_set)}")

# 错误的方式：使用{}
empty_dict = {}
print(f"使用{{}}创建的是: {type(empty_dict)}")
print("注意：{}创建的是字典，不是集合！")
```

**输出结果：**
```
空集合: set()
空集合类型: <class 'set'>
空集合长度: 0

使用{}创建的是: <class 'dict'>
注意：{}创建的是字典，不是集合！
```

## 集合的特性演示

### 唯一性：自动去重

```python
# 唯一性：自动去重
duplicate_data = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
unique_set = set(duplicate_data)
print(f"包含重复元素的列表: {duplicate_data}")
print(f"转换为集合后: {unique_set}")
print(f"原始长度: {len(duplicate_data)}, 集合长度: {len(unique_set)}")
```

**输出结果：**
```
包含重复元素的列表: [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
转换为集合后: {1, 2, 3, 4, 5}
原始长度: 10, 集合长度: 5
```

### 无序性：元素没有固定顺序

```python
# 无序性：集合中的元素没有固定顺序
print("无序性演示：")
for i in range(3):
    temp_set = {5, 1, 3, 2, 4}
    print(f"第{i+1}次创建同样的集合: {temp_set}")
print("注意：集合的显示顺序可能不同，这是正常的")
```

**输出结果：**
```
无序性演示：
第1次创建同样的集合: {1, 2, 3, 4, 5}
第2次创建同样的集合: {1, 2, 3, 4, 5}
第3次创建同样的集合: {1, 2, 3, 4, 5}
注意：集合的显示顺序可能不同，这是正常的
```

## 实际应用示例

### 数据去重

```python
# 去除列表中的重复元素
original_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
print(f"原始列表: {original_list}")

# 方法1：转换为集合再转回列表
unique_list1 = list(set(original_list))
print(f"去重后的列表: {unique_list1}")

# 方法2：保持原有顺序的去重
unique_list2 = []
seen = set()
for item in original_list:
    if item not in seen:
        unique_list2.append(item)
        seen.add(item)
print(f"保持顺序的去重列表: {unique_list2}")
```

**输出结果：**
```
原始列表: ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
去重后的列表: ['banana', 'orange', 'apple', 'grape']
保持顺序的去重列表: ['apple', 'banana', 'orange', 'grape']
```

### 文本分析

```python
# 统计文本中的唯一单词
text = "python is great python is powerful python is easy"
words = text.split()
unique_words = set(words)
print(f"原始文本: {text}")
print(f"所有单词: {words}")
print(f"唯一单词: {unique_words}")
print(f"总单词数: {len(words)}, 唯一单词数: {len(unique_words)}")
```

**输出结果：**
```
原始文本: python is great python is powerful python is easy
所有单词: ['python', 'is', 'great', 'python', 'is', 'powerful', 'python', 'is', 'easy']
唯一单词: {'powerful', 'great', 'python', 'easy', 'is'}
总单词数: 9, 唯一单词数: 5
```

### 查找共同元素

```python
# 检查两个列表的共同元素
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1)
set2 = set(list2)
common_elements = set1 & set2  # 交集
print(f"列表1: {list1}")
print(f"列表2: {list2}")
print(f"共同元素: {common_elements}")
```

**输出结果：**
```
列表1: [1, 2, 3, 4, 5]
列表2: [4, 5, 6, 7, 8]
共同元素: {4, 5}
```

## 更多创建方法

### 集合推导式

```python
# 使用集合推导式创建平方数集合
squares = {x**2 for x in range(1, 6)}
print(f"使用集合推导式创建平方数集合: {squares}")
```

### 从字典创建集合

```python
# 从字典的键创建集合
person = {"name": "Alice", "age": 25, "city": "Beijing"}
keys_set = set(person.keys())
print(f"从字典键创建集合: {keys_set}")

# 从字典的值创建集合
values_set = set(person.values())
print(f"从字典值创建集合: {values_set}")
```

## 练习题

### 基础练习

```python
# 练习1：创建一个包含1到10的偶数的集合
even_numbers = {x for x in range(1, 11) if x % 2 == 0}
print(f"1. 1到10的偶数集合: {even_numbers}")

# 练习2：从两个列表创建集合并找出不同元素
colors1 = ["red", "blue", "green", "yellow"]
colors2 = ["blue", "green", "purple", "orange"]
set_colors1 = set(colors1)
set_colors2 = set(colors2)
different_colors = set_colors1 ^ set_colors2  # 对称差集
print(f"2. 两个颜色列表的不同元素: {different_colors}")

# 练习3：统计字符串中的唯一字符数量
text = "programming"
unique_chars = set(text)
print(f"3. 字符串'{text}'中的唯一字符: {unique_chars}")
print(f"   唯一字符数量: {len(unique_chars)}")
```

## 运行完整代码

你可以运行以下完整代码来查看所有示例：

```bash
python3 01_creating_sets.py
```

## 学习要点

1. **创建方法**：
   - 使用 `{}` 创建非空集合
   - 使用 `set()` 创建空集合或从其他类型转换
   - 注意 `{}` 创建的是字典，不是空集合

2. **集合特性**：
   - 自动去重：重复元素只保留一个
   - 无序性：元素没有固定的索引位置
   - 元素必须是可哈希的

3. **实际应用**：
   - 数据去重是集合最常见的应用
   - 快速查找共同元素或不同元素
   - 统计唯一元素的数量

4. **性能优势**：
   - 成员检测（`in` 操作）比列表快得多
   - 去重操作比手动循环效率高

## 注意事项

- 集合中不能包含可变对象（如列表、字典）
- 集合本身是可变的，但元素必须是不可变的
- 集合的显示顺序可能因Python版本而异
- 空集合必须用 `set()` 创建，不能用 `{}`

通过掌握这些集合创建方法，你就可以在各种场景中灵活使用集合来解决数据处理问题了。