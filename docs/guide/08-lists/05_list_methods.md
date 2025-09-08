# 列表内置方法详解

本节详细介绍Python列表的所有内置方法，包括添加、删除、查找、排序等操作，以及这些方法的使用技巧和注意事项。

## 学习目标

- 掌握列表的所有内置方法及其用法
- 理解不同方法的返回值和副作用
- 学会选择合适的方法解决实际问题
- 掌握方法的组合使用和最佳实践
- 了解各种方法的性能特点
- 学会安全地使用列表方法，避免常见错误

## 添加和插入方法

### 1. append() - 在末尾添加元素

`append()` 方法在列表末尾添加一个元素，时间复杂度为 O(1)。

```python
# 基本用法
fruits = ['apple', 'banana']
print(f"初始列表: {fruits}")

fruits.append('orange')
print(f"append('orange')后: {fruits}")  # ['apple', 'banana', 'orange']

# append可以添加任何类型的对象
fruits.append([1, 2, 3])        # 添加列表作为单个元素
fruits.append({'key': 'value'}) # 添加字典作为单个元素
print(f"添加复杂对象后: {fruits}")
# ['apple', 'banana', 'orange', [1, 2, 3], {'key': 'value'}]
```

**重要特点**：
- `append()` 将整个对象作为一个元素添加
- 返回值为 `None`（就地修改）
- 时间复杂度：O(1)

### 2. insert() - 在指定位置插入元素

`insert()` 方法在指定索引位置插入元素。

```python
numbers = [1, 2, 4, 5]
print(f"原始列表: {numbers}")

# 在索引2处插入3
numbers.insert(2, 3)
print(f"insert(2, 3)后: {numbers}")  # [1, 2, 3, 4, 5]

# 在开头插入
numbers.insert(0, 0)
print(f"insert(0, 0)后: {numbers}")  # [0, 1, 2, 3, 4, 5]

# 在末尾插入（等同于append）
numbers.insert(len(numbers), 6)
print(f"在末尾插入6后: {numbers}")  # [0, 1, 2, 3, 4, 5, 6]

# 索引超出范围时的行为
numbers.insert(100, 'end')  # 会插入到末尾
print(f"超大索引插入后: {numbers}")
```

**重要特点**：
- 如果索引超出范围，会插入到最近的有效位置
- 时间复杂度：O(n)（需要移动后续元素）
- 返回值为 `None`

### 3. extend() - 扩展列表

`extend()` 方法将可迭代对象的所有元素添加到列表末尾。

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"列表1: {list1}")
print(f"列表2: {list2}")

list1.extend(list2)
print(f"list1.extend(list2)后: {list1}")  # [1, 2, 3, 4, 5, 6]
print(f"list2未改变: {list2}")  # [4, 5, 6]

# extend可以接受任何可迭代对象
colors = ['red', 'green']
colors.extend('blue')  # 字符串是可迭代的
print(f"extend('blue')后: {colors}")  # ['red', 'green', 'b', 'l', 'u', 'e']

colors = ['red', 'green']
colors.extend(['blue'])  # 正确的方式
print(f"extend(['blue'])后: {colors}")  # ['red', 'green', 'blue']

# 扩展其他可迭代对象
numbers = [1, 2]
numbers.extend(range(3, 6))  # 扩展range对象
print(f"extend(range(3, 6))后: {numbers}")  # [1, 2, 3, 4, 5]
```

**append vs extend vs + 操作符比较**：

```python
original = [1, 2, 3]

# 创建测试列表
list1 = original.copy()
list2 = original.copy()
list3 = original.copy()

print(f"原始列表: {original}")

# 不同添加方法的效果
list1.append([4, 5])
print(f"append([4, 5]): {list1}")  # [1, 2, 3, [4, 5]]

list2.extend([4, 5])
print(f"extend([4, 5]): {list2}")  # [1, 2, 3, 4, 5]

list3 = list3 + [4, 5]
print(f"+ [4, 5]: {list3}")        # [1, 2, 3, 4, 5]
print(f"原始列表未改变: {original}")  # [1, 2, 3]
```

## 删除方法

### 1. remove() - 删除第一个匹配的元素

`remove()` 方法删除列表中第一个匹配的元素。

```python
items = ['a', 'b', 'c', 'b', 'd']
print(f"初始列表: {items}")

items.remove('b')  # 只删除第一个'b'
print(f"remove('b')后: {items}")  # ['a', 'c', 'b', 'd']

# 删除不存在的元素会引发ValueError
try:
    items.remove('x')
except ValueError as e:
    print(f"删除不存在元素的错误: {e}")  # list.remove(x): x not in list

# 安全删除函数
def safe_remove(lst, item):
    """安全删除元素"""
    if item in lst:
        lst.remove(item)
        return True
    return False

test_list = [1, 2, 3, 4, 5]
result = safe_remove(test_list, 3)
print(f"安全删除3: {result}, 列表: {test_list}")  # True, [1, 2, 4, 5]

result = safe_remove(test_list, 10)
print(f"安全删除10: {result}, 列表: {test_list}")  # False, [1, 2, 4, 5]
```

**重要特点**：
- 只删除第一个匹配的元素
- 如果元素不存在，抛出 `ValueError`
- 时间复杂度：O(n)
- 返回值为 `None`

### 2. pop() - 删除并返回元素

`pop()` 方法删除指定位置的元素并返回该元素。

```python
numbers = [10, 20, 30, 40, 50]
print(f"初始列表: {numbers}")

# 不指定索引时删除最后一个元素
last = numbers.pop()
print(f"pop()返回: {last}, 剩余: {numbers}")  # 50, [10, 20, 30, 40]

# 指定索引删除
second = numbers.pop(1)
print(f"pop(1)返回: {second}, 剩余: {numbers}")  # 20, [10, 30, 40]

# 使用负索引
first = numbers.pop(0)
print(f"pop(0)返回: {first}, 剩余: {numbers}")  # 10, [30, 40]

# 对空列表使用pop会引发IndexError
empty_list = []
try:
    empty_list.pop()
except IndexError as e:
    print(f"空列表pop错误: {e}")  # pop from empty list

# 安全的pop函数
def safe_pop(lst, index=None):
    """安全弹出元素"""
    if not lst:
        return None
    if index is None:
        return lst.pop()
    if 0 <= index < len(lst):
        return lst.pop(index)
    return None

test_list = [1, 2, 3]
result = safe_pop(test_list)
print(f"安全pop: {result}, 列表: {test_list}")  # 3, [1, 2]
```

**重要特点**：
- 默认删除最后一个元素（索引-1）
- 返回被删除的元素
- 如果索引无效或列表为空，抛出 `IndexError`
- 时间复杂度：O(1)（末尾）或 O(n)（其他位置）

### 3. clear() - 清空列表

`clear()` 方法删除列表中的所有元素。

```python
temp_list = [1, 2, 3, 4, 5]
print(f"清空前: {temp_list}")
temp_list.clear()
print(f"clear()后: {temp_list}")  # []
print(f"列表长度: {len(temp_list)}")  # 0

# 等价操作
temp_list2 = [1, 2, 3, 4, 5]
temp_list2[:] = []  # 切片赋值清空
print(f"切片清空后: {temp_list2}")  # []
```

## 查找和计数方法

### 1. index() - 查找元素索引

`index()` 方法返回指定元素第一次出现的索引。

```python
fruits = ['apple', 'banana', 'orange', 'banana', 'grape']
print(f"水果列表: {fruits}")

# 查找第一个匹配元素的索引
banana_index = fruits.index('banana')
print(f"'banana'的索引: {banana_index}")  # 1

# 在指定范围内查找
banana_index2 = fruits.index('banana', 2)  # 从索引2开始查找
print(f"从索引2开始查找'banana': {banana_index2}")  # 3

# 在指定范围内查找（指定开始和结束）
try:
    orange_index = fruits.index('orange', 0, 3)  # 在索引0-2范围内查找
    print(f"在索引0-2范围内'orange'的索引: {orange_index}")  # 2
except ValueError:
    print("在指定范围内未找到'orange'")

# 查找不存在的元素会引发ValueError
try:
    fruits.index('kiwi')
except ValueError as e:
    print(f"查找不存在元素的错误: {e}")  # 'kiwi' is not in list

# 安全查找函数
def safe_index(lst, item, start=0, end=None):
    """安全查找元素索引"""
    try:
        if end is None:
            return lst.index(item, start)
        else:
            return lst.index(item, start, end)
    except ValueError:
        return -1  # 未找到返回-1

test_list = ['a', 'b', 'c', 'b']
result = safe_index(test_list, 'b')
print(f"安全查找'b': {result}")  # 1

result = safe_index(test_list, 'x')
print(f"安全查找'x': {result}")  # -1
```

### 2. count() - 计算元素出现次数

`count()` 方法返回指定元素在列表中出现的次数。

```python
numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"数字列表: {numbers}")

count_2 = numbers.count(2)
print(f"数字2出现次数: {count_2}")  # 3

count_6 = numbers.count(6)
print(f"数字6出现次数: {count_6}")  # 0

# 统计所有元素的出现次数
def count_all_elements(lst):
    """统计列表中所有元素的出现次数"""
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts

# 或者使用count方法
def count_all_with_count_method(lst):
    """使用count方法统计所有元素"""
    unique_items = list(set(lst))
    counts = {}
    for item in unique_items:
        counts[item] = lst.count(item)
    return counts

test_list = [1, 2, 3, 2, 4, 2, 5, 1]
result1 = count_all_elements(test_list)
result2 = count_all_with_count_method(test_list)

print(f"\n各元素出现次数（方法1）: {result1}")
print(f"各元素出现次数（方法2）: {result2}")
```

## 排序和反转方法

### 1. sort() - 就地排序

`sort()` 方法对列表进行就地排序。

```python
# 基本排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"原始数字列表: {numbers}")

# 升序排序（默认）
numbers_copy1 = numbers.copy()
numbers_copy1.sort()
print(f"升序排序后: {numbers_copy1}")  # [1, 1, 2, 3, 4, 5, 6, 9]

# 降序排序
numbers_copy2 = numbers.copy()
numbers_copy2.sort(reverse=True)
print(f"降序排序后: {numbers_copy2}")  # [9, 6, 5, 4, 3, 2, 1, 1]

# 字符串排序
words = ['banana', 'apple', 'cherry', 'date']
print(f"\n原始单词列表: {words}")

words_copy1 = words.copy()
words_copy1.sort()
print(f"字母序排序: {words_copy1}")  # ['apple', 'banana', 'cherry', 'date']

# 按长度排序
words_copy2 = words.copy()
words_copy2.sort(key=len)
print(f"按长度排序: {words_copy2}")  # ['date', 'apple', 'banana', 'cherry']

# 按长度降序排序
words_copy3 = words.copy()
words_copy3.sort(key=len, reverse=True)
print(f"按长度降序: {words_copy3}")  # ['banana', 'cherry', 'apple', 'date']
```

### 2. 自定义排序键

```python
# 复杂对象排序
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78), ('Diana', 92)]
print(f"学生成绩: {students}")

# 按成绩排序
students_by_grade = students.copy()
students_by_grade.sort(key=lambda x: x[1])
print(f"按成绩排序: {students_by_grade}")
# [('Charlie', 78), ('Alice', 85), ('Bob', 90), ('Diana', 92)]

# 按姓名排序
students_by_name = students.copy()
students_by_name.sort(key=lambda x: x[0])
print(f"按姓名排序: {students_by_name}")
# [('Alice', 85), ('Bob', 90), ('Charlie', 78), ('Diana', 92)]

# 多级排序：先按成绩，再按姓名
students_multi = [('Alice', 85), ('Bob', 85), ('Charlie', 78), ('Diana', 92)]
students_multi.sort(key=lambda x: (x[1], x[0]))  # 先按成绩，再按姓名
print(f"多级排序: {students_multi}")
# [('Charlie', 78), ('Alice', 85), ('Bob', 85), ('Diana', 92)]
```

### 3. reverse() - 反转列表

`reverse()` 方法反转列表中元素的顺序。

```python
original = [1, 2, 3, 4, 5]
print(f"原始列表: {original}")

original.reverse()
print(f"reverse()后: {original}")  # [5, 4, 3, 2, 1]

# 注意：sort()和reverse()都是就地操作，返回None
result = [3, 1, 2].sort()
print(f"sort()的返回值: {result}")  # None

# 如果需要返回新列表，使用内置函数
original2 = [1, 2, 3, 4, 5]
sorted_list = sorted(original2, reverse=True)
reversed_list = list(reversed(original2))

print(f"原列表: {original2}")        # [1, 2, 3, 4, 5]
print(f"sorted()结果: {sorted_list}")  # [5, 4, 3, 2, 1]
print(f"reversed()结果: {reversed_list}")  # [5, 4, 3, 2, 1]
```

## 复制方法

### copy() - 创建浅复制

`copy()` 方法创建列表的浅复制。

```python
# 基本复制
original = [1, 2, [3, 4], 5]
copied = original.copy()

print(f"原始列表: {original}")
print(f"复制列表: {copied}")
print(f"是否为同一对象: {original is copied}")  # False
print(f"内容是否相等: {original == copied}")    # True

# 修改复制列表的简单元素
copied[0] = 100
print(f"\n修改复制列表的第一个元素后:")
print(f"原始列表: {original}")  # [1, 2, [3, 4], 5]
print(f"复制列表: {copied}")    # [100, 2, [3, 4], 5]

# 修改嵌套列表（浅复制的限制）
copied[2][0] = 999
print(f"\n修改嵌套列表后:")
print(f"原始列表: {original}")  # [1, 2, [999, 4], 5]
print(f"复制列表: {copied}")    # [100, 2, [999, 4], 5]
print("注意：嵌套对象被共享了！")
```

### 深复制解决方案

```python
import copy as copy_module

original = [1, 2, [3, 4], 5]
shallow_copy = original.copy()
deep_copy = copy_module.deepcopy(original)

print(f"深复制演示:")
print(f"原始列表: {original}")
print(f"浅复制: {shallow_copy}")
print(f"深复制: {deep_copy}")

# 修改嵌套列表
original[2][0] = 888
print(f"\n修改原始列表的嵌套元素后:")
print(f"原始列表: {original}")     # [1, 2, [888, 4], 5]
print(f"浅复制: {shallow_copy}")   # [1, 2, [888, 4], 5] - 受影响
print(f"深复制: {deep_copy}")      # [1, 2, [3, 4], 5] - 不受影响
```

### 不同复制方法比较

```python
original = [1, 2, 3]

# 不同的复制方法
copy1 = original.copy()           # copy()方法
copy2 = original[:]               # 切片复制
copy3 = list(original)            # list()构造函数
copy4 = [x for x in original]     # 列表推导式

print(f"原始列表: {original}")
print(f"copy(): {copy1}")
print(f"切片[]: {copy2}")
print(f"list(): {copy3}")
print(f"推导式: {copy4}")

# 验证都是不同的对象
print(f"\n是否为不同对象:")
print(f"copy1 is original: {copy1 is original}")  # False
print(f"copy2 is original: {copy2 is original}")  # False
print(f"copy3 is original: {copy3 is original}")  # False
print(f"copy4 is original: {copy4 is original}")  # False
```

## 方法组合和实际应用

### 1. 去重并保持顺序

```python
def remove_duplicates_keep_order(lst):
    """去除重复元素但保持顺序"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers_with_duplicates = [1, 2, 3, 2, 4, 1, 5, 3]
unique_numbers = remove_duplicates_keep_order(numbers_with_duplicates)
print(f"原列表: {numbers_with_duplicates}")
print(f"去重后: {unique_numbers}")  # [1, 2, 3, 4, 5]
```

### 2. 统计元素频率

```python
def count_frequencies(lst):
    """统计列表中各元素的频率"""
    frequencies = {}
    for item in lst:
        frequencies[item] = frequencies.get(item, 0) + 1
    return frequencies

# 或者使用count方法（效率较低）
def count_frequencies_with_count(lst):
    """使用count方法统计频率"""
    unique_items = list(set(lst))
    return {item: lst.count(item) for item in unique_items}

text_list = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
freq1 = count_frequencies(text_list)
freq2 = count_frequencies_with_count(text_list)

print(f"文本列表: {text_list}")
print(f"频率统计1: {freq1}")  # {'apple': 3, 'banana': 2, 'cherry': 1}
print(f"频率统计2: {freq2}")  # {'apple': 3, 'banana': 2, 'cherry': 1}
```

### 3. 安全的列表操作类

```python
class SafeList:
    """安全的列表操作类"""
    
    def __init__(self, initial_list=None):
        self.data = initial_list.copy() if initial_list else []
    
    def safe_append(self, item):
        """安全添加元素"""
        self.data.append(item)
        return True
    
    def safe_remove(self, item):
        """安全删除元素"""
        if item in self.data:
            self.data.remove(item)
            return True
        return False
    
    def safe_pop(self, index=None):
        """安全弹出元素"""
        if not self.data:
            return None
        if index is None:
            return self.data.pop()
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        return None
    
    def safe_index(self, item, start=0, end=None):
        """安全查找索引"""
        try:
            if end is None:
                return self.data.index(item, start)
            else:
                return self.data.index(item, start, end)
        except ValueError:
            return -1
    
    def __str__(self):
        return str(self.data)
    
    def __len__(self):
        return len(self.data)

# 使用示例
safe_list = SafeList([1, 2, 3, 4, 5])
print(f"初始列表: {safe_list}")

print(f"添加6: {safe_list.safe_append(6)}")  # True
print(f"删除3: {safe_list.safe_remove(3)}")  # True
print(f"删除10: {safe_list.safe_remove(10)}")  # False
print(f"弹出元素: {safe_list.safe_pop()}")  # 6
print(f"查找2的索引: {safe_list.safe_index(2)}")  # 1
print(f"查找10的索引: {safe_list.safe_index(10)}")  # -1
print(f"最终列表: {safe_list}")
```

## 性能比较和最佳实践

### 1. 方法性能比较

```python
import time

def performance_comparison():
    """比较不同方法的性能"""
    # 创建大列表进行测试
    large_list = list(range(10000))
    
    # 测试append vs extend vs +
    print("性能比较（10000个元素）:")
    
    # append方法
    test_list1 = []
    start_time = time.time()
    for i in range(1000):
        test_list1.append(i)
    append_time = time.time() - start_time
    
    # extend方法
    test_list2 = []
    start_time = time.time()
    test_list2.extend(range(1000))
    extend_time = time.time() - start_time
    
    # +操作符
    test_list3 = []
    start_time = time.time()
    test_list3 = test_list3 + list(range(1000))
    plus_time = time.time() - start_time
    
    print(f"append循环: {append_time:.6f}秒")
    print(f"extend一次: {extend_time:.6f}秒")
    print(f"+操作符: {plus_time:.6f}秒")
    
    # 测试不同查找方法
    target = 5000
    
    # index方法
    start_time = time.time()
    idx = large_list.index(target)
    index_time = time.time() - start_time
    
    # 线性搜索
    start_time = time.time()
    idx2 = -1
    for i, val in enumerate(large_list):
        if val == target:
            idx2 = i
            break
    linear_time = time.time() - start_time
    
    print(f"\nindex方法: {index_time:.6f}秒")
    print(f"线性搜索: {linear_time:.6f}秒")

performance_comparison()
```

### 2. 最佳实践总结

```python
def best_practices_demo():
    """列表方法使用的最佳实践"""
    print("列表方法最佳实践:")
    print("=" * 30)
    
    # 1. 选择合适的添加方法
    print("1. 添加元素的选择:")
    print("   - 添加单个元素：使用 append()")
    print("   - 添加多个元素：使用 extend()")
    print("   - 在特定位置插入：使用 insert()")
    print("   - 创建新列表：使用 + 操作符")
    
    # 2. 安全删除
    print("\n2. 安全删除:")
    print("   - 删除前检查元素是否存在")
    print("   - 使用try-except处理异常")
    print("   - 考虑使用pop()获取被删除的值")
    
    # 3. 高效查找
    print("\n3. 高效查找:")
    print("   - 频繁查找考虑使用set或dict")
    print("   - 使用in操作符检查存在性")
    print("   - 对有序列表考虑二分查找")
    
    # 4. 排序注意事项
    print("\n4. 排序注意事项:")
    print("   - sort()是就地排序，sorted()返回新列表")
    print("   - 使用key参数进行自定义排序")
    print("   - 稳定排序保持相等元素的相对顺序")
    
    # 5. 复制选择
    print("\n5. 复制选择:")
    print("   - 简单列表使用copy()或[:]")
    print("   - 嵌套结构使用copy.deepcopy()")
    print("   - 考虑内存使用和性能需求")

best_practices_demo()
```

## 完整示例：学生成绩管理系统

```python
class StudentGradeManager:
    """学生成绩管理系统"""
    
    def __init__(self):
        self.students = []  # [(name, grade), ...]
    
    def add_student(self, name, grade):
        """添加学生"""
        self.students.append((name, grade))
        print(f"添加学生: {name}, 成绩: {grade}")
    
    def remove_student(self, name):
        """删除学生"""
        for i, (student_name, _) in enumerate(self.students):
            if student_name == name:
                removed = self.students.pop(i)
                print(f"删除学生: {removed[0]}, 成绩: {removed[1]}")
                return True
        print(f"未找到学生: {name}")
        return False
    
    def update_grade(self, name, new_grade):
        """更新成绩"""
        for i, (student_name, old_grade) in enumerate(self.students):
            if student_name == name:
                self.students[i] = (name, new_grade)
                print(f"更新{name}的成绩: {old_grade} -> {new_grade}")
                return True
        print(f"未找到学生: {name}")
        return False
    
    def find_student(self, name):
        """查找学生"""
        for student_name, grade in self.students:
            if student_name == name:
                return grade
        return None
    
    def get_statistics(self):
        """获取统计信息"""
        if not self.students:
            return "没有学生数据"
        
        grades = [grade for _, grade in self.students]
        return {
            '总人数': len(self.students),
            '平均分': sum(grades) / len(grades),
            '最高分': max(grades),
            '最低分': min(grades),
            '及格人数': sum(1 for grade in grades if grade >= 60)
        }
    
    def sort_by_grade(self, reverse=False):
        """按成绩排序"""
        self.students.sort(key=lambda x: x[1], reverse=reverse)
        order = "降序" if reverse else "升序"
        print(f"已按成绩{order}排序")
    
    def sort_by_name(self):
        """按姓名排序"""
        self.students.sort(key=lambda x: x[0])
        print("已按姓名排序")
    
    def display_all(self):
        """显示所有学生"""
        if not self.students:
            print("没有学生数据")
            return
        
        print("\n学生成绩列表:")
        print("-" * 20)
        for i, (name, grade) in enumerate(self.students, 1):
            print(f"{i}. {name}: {grade}分")
    
    def get_top_students(self, n=3):
        """获取前n名学生"""
        sorted_students = sorted(self.students, key=lambda x: x[1], reverse=True)
        return sorted_students[:n]

# 使用示例
def demo_grade_manager():
    """演示成绩管理系统"""
    manager = StudentGradeManager()
    
    # 添加学生
    manager.add_student("Alice", 85)
    manager.add_student("Bob", 92)
    manager.add_student("Charlie", 78)
    manager.add_student("Diana", 96)
    manager.add_student("Eve", 88)
    
    # 显示所有学生
    manager.display_all()
    
    # 查找学生
    grade = manager.find_student("Bob")
    print(f"\nBob的成绩: {grade}")
    
    # 更新成绩
    manager.update_grade("Charlie", 82)
    
    # 按成绩排序
    manager.sort_by_grade(reverse=True)
    manager.display_all()
    
    # 获取统计信息
    stats = manager.get_statistics()
    print(f"\n统计信息: {stats}")
    
    # 获取前3名
    top_students = manager.get_top_students(3)
    print(f"\n前3名学生: {top_students}")
    
    # 删除学生
    manager.remove_student("Eve")
    manager.display_all()

if __name__ == "__main__":
    demo_grade_manager()
```

## 学习要点总结

### 核心概念
1. **就地修改 vs 返回新对象**：大多数列表方法直接修改原列表
2. **返回值**：修改方法通常返回 `None`，查询方法返回具体值
3. **异常处理**：某些方法在特定条件下会抛出异常
4. **时间复杂度**：不同方法的性能特点不同

### 方法分类

| 类别 | 方法 | 返回值 | 时间复杂度 | 注意事项 |
|------|------|--------|------------|----------|
| 添加 | `append()` | None | O(1) | 添加单个元素 |
| 添加 | `insert()` | None | O(n) | 需要移动元素 |
| 添加 | `extend()` | None | O(k) | k为添加元素数 |
| 删除 | `remove()` | None | O(n) | 可能抛出ValueError |
| 删除 | `pop()` | 被删除元素 | O(1)/O(n) | 可能抛出IndexError |
| 删除 | `clear()` | None | O(n) | 清空所有元素 |
| 查找 | `index()` | 索引 | O(n) | 可能抛出ValueError |
| 查找 | `count()` | 次数 | O(n) | 总是成功 |
| 排序 | `sort()` | None | O(n log n) | 就地排序 |
| 排序 | `reverse()` | None | O(n) | 反转顺序 |
| 复制 | `copy()` | 新列表 | O(n) | 浅复制 |

### 最佳实践
1. **选择合适的方法**：根据需求选择最高效的方法
2. **异常处理**：对可能失败的操作进行异常处理
3. **性能考虑**：了解方法的时间复杂度，避免不必要的性能损失
4. **代码可读性**：选择最能表达意图的方法
5. **安全操作**：实现安全的包装函数避免运行时错误

### 常见陷阱
1. **忘记方法返回None**：不能链式调用修改方法
2. **浅复制问题**：嵌套对象仍然共享引用
3. **在循环中修改列表**：可能导致索引错误
4. **性能陷阱**：在大列表上频繁使用低效方法

通过掌握这些列表内置方法，你将能够高效地处理各种列表操作需求，编写出更加优雅和高性能的Python代码。