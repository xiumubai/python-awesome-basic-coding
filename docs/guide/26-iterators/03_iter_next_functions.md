# iter()和next()函数使用

本节详细介绍Python内置的`iter()`和`next()`函数的各种用法。这两个函数是迭代器协议的核心，掌握它们的用法对理解迭代器至关重要。

## 学习目标

1. 掌握`iter()`函数的多种用法
2. 理解`next()`函数的参数和返回值
3. 学会使用`iter()`创建自定义迭代器
4. 了解`iter()`和`next()`的高级应用

## 1. iter()函数基础用法

`iter()`函数用于从可迭代对象创建迭代器：

```python
# iter()从可迭代对象创建迭代器
my_list = [1, 2, 3, 4, 5]
list_iter = iter(my_list)
print(f"原列表: {my_list}")
print(f"迭代器类型: {type(list_iter)}")

# 使用next()获取元素
print("使用next()获取元素:")
print(f"第1个元素: {next(list_iter)}")
print(f"第2个元素: {next(list_iter)}")
print(f"第3个元素: {next(list_iter)}")
```

## 2. next()函数的默认值参数

`next()`函数可以接受第二个参数作为默认值，当迭代器耗尽时返回该值：

```python
# next()的第二个参数是默认值，当迭代器耗尽时返回
my_list = [1, 2, 3]
iterator = iter(my_list)

print("使用默认值参数:")
for i in range(5):
    value = next(iterator, "没有更多元素")
    print(f"第{i+1}次调用next(): {value}")
```

## 3. iter()函数的双参数形式

`iter(callable, sentinel)`形式会重复调用`callable`直到返回`sentinel`值：

```python
import random

# 模拟掷骰子，直到掷出6
print("掷骰子直到出现6:")
dice_iter = iter(lambda: random.randint(1, 6), 6)
rolls = []
for roll in dice_iter:
    rolls.append(roll)
    if len(rolls) > 10:  # 防止无限循环
        break
print(f"掷骰子结果: {rolls}")
```

## 4. 从文件读取示例

使用`iter()`读取文件直到遇到特定标记：

```python
# 使用iter()读取文件直到遇到"END"
print("读取文件直到遇到'END':")
with open('test_input.txt', 'r') as f:
    line_iter = iter(f.readline, 'END\n')
    for line_num, line in enumerate(line_iter, 1):
        print(f"第{line_num}行: {line.strip()}")
```

## 5. 计数器示例

创建一个可调用的计数器对象：

```python
class Counter:
    """简单计数器"""
    def __init__(self, start=0):
        self.value = start
    
    def __call__(self):
        self.value += 1
        return self.value

# 使用计数器创建迭代器
counter = Counter()
print("计数器迭代器（停止在5）:")
counter_iter = iter(counter, 5)
for count in counter_iter:
    print(f"计数: {count}")
```

## 6. 用户输入示例

模拟用户输入直到特定条件：

```python
# 模拟用户输入，直到输入"quit"
input_data = ["hello", "world", "python", "quit", "ignored"]
input_iter = iter(input_data)

# 创建一个模拟input函数
def mock_input(prompt=""):
    try:
        return next(input_iter)
    except StopIteration:
        return "quit"

print("模拟用户输入（直到输入'quit'）:")
user_iter = iter(lambda: mock_input("请输入: "), "quit")
for user_input in user_iter:
    print(f"用户输入: {user_input}")
```

## 7. 高级iter()用法

### 字符串迭代

```python
# 从字符串创建迭代器
string = "Python"
string_iter = iter(string)
print(f"字符串 '{string}' 的字符:")
for char in string_iter:
    print(f"字符: {char}")
```

### 字典迭代

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 迭代键
key_iter = iter(my_dict)
print("键迭代:")
for key in key_iter:
    print(f"键: {key}")

# 迭代值
value_iter = iter(my_dict.values())
print("值迭代:")
for value in value_iter:
    print(f"值: {value}")

# 迭代键值对
item_iter = iter(my_dict.items())
print("键值对迭代:")
for key, value in item_iter:
    print(f"键值对: {key} -> {value}")
```

## 8. next()的错误处理

处理迭代器耗尽的情况：

```python
my_list = [1, 2, 3]
iterator = iter(my_list)

# 正常获取元素
for i in range(3):
    print(f"元素: {next(iterator)}")

# 方法1: 使用默认值
value = next(iterator, "迭代器已耗尽")
print(f"使用默认值: {value}")

# 方法2: 捕获异常
try:
    value = next(iterator)
except StopIteration:
    print("捕获StopIteration异常")
```

## 9. 迭代器链

创建链接多个迭代器的自定义迭代器：

```python
class ChainIterator:
    """链接多个迭代器"""
    def __init__(self, *iterables):
        self.iterators = [iter(iterable) for iterable in iterables]
        self.current_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current_index < len(self.iterators):
            try:
                return next(self.iterators[self.current_index])
            except StopIteration:
                self.current_index += 1
        raise StopIteration

# 使用链接迭代器
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

chain_iter = ChainIterator(list1, list2, list3)
for value in chain_iter:
    print(f"链接值: {value}")
```

## 10. 迭代器的性能测试

比较不同遍历方式的性能：

```python
import time

data = list(range(100000))

# 方法1: 直接遍历列表
start_time = time.time()
count1 = 0
for item in data:
    count1 += 1
time1 = time.time() - start_time

# 方法2: 使用迭代器
start_time = time.time()
count2 = 0
iterator = iter(data)
while True:
    try:
        next(iterator)
        count2 += 1
    except StopIteration:
        break
time2 = time.time() - start_time

print(f"直接遍历列表: {count1} 个元素，耗时 {time1:.6f} 秒")
print(f"使用迭代器: {count2} 个元素，耗时 {time2:.6f} 秒")
```

## 11. 实用工具函数

### 窥视迭代器

```python
def peek_iterator(iterator, n=1):
    """窥视迭代器的前n个元素，不消耗迭代器"""
    import itertools
    iterator, peek_iter = itertools.tee(iterator)
    peeked = []
    for _ in range(n):
        try:
            peeked.append(next(peek_iter))
        except StopIteration:
            break
    return peeked, iterator
```

### 消耗迭代器

```python
def consume_iterator(iterator, n=None):
    """消耗迭代器的n个元素"""
    if n is None:
        # 消耗所有元素
        for _ in iterator:
            pass
    else:
        # 消耗n个元素
        for _ in range(n):
            try:
                next(iterator)
            except StopIteration:
                break
```

## iter()函数的两种形式

### 单参数形式
- `iter(iterable)`: 从可迭代对象创建迭代器
- 适用于列表、元组、字符串、字典等

### 双参数形式
- `iter(callable, sentinel)`: 重复调用callable直到返回sentinel
- 适用于文件读取、用户输入、随机数生成等场景

## 学习要点

1. **iter()函数**：创建迭代器的标准方法
2. **next()函数**：获取迭代器下一个元素
3. **默认值处理**：使用`next(iterator, default)`避免异常
4. **双参数iter()**：实现条件循环的优雅方式
5. **异常处理**：合理处理`StopIteration`异常

## 注意事项

- `iter()`总是返回一个新的迭代器对象
- `next()`会改变迭代器的状态，是不可逆的操作
- 使用默认值参数可以避免`StopIteration`异常
- 双参数形式的`iter()`在处理流数据时非常有用
- 迭代器的性能通常与直接遍历相当，但提供了更大的灵活性

通过掌握这些函数的用法，你可以更好地理解和使用Python的迭代器机制。