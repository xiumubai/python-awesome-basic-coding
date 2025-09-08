# 字典的创建和初始化

## 学习目标

- 掌握字典的基本语法和结构
- 学习多种字典创建方法
- 理解不同创建方法的适用场景
- 了解字典的特性和限制

## 字典基础概念

字典（Dictionary）是Python中的一种可变数据类型，用于存储键值对（key-value pairs）。字典具有以下特点：

- **键值对存储**：每个元素由键和值组成
- **键的唯一性**：每个键在字典中必须是唯一的
- **键的不可变性**：键必须是不可变类型（字符串、数字、元组等）
- **值的任意性**：值可以是任意类型的数据
- **无序性**：Python 3.7+保持插入顺序，但不应依赖顺序

## 创建字典的方法

### 1. 使用花括号创建字典

最常见和直观的创建方式：

```python
# 创建空字典
empty_dict = {}
print(f"空字典: {empty_dict}")
print(f"类型: {type(empty_dict)}")

# 创建包含数据的字典
student = {
    "name": "张三",
    "age": 20,
    "grade": "大二",
    "gpa": 3.8
}
print(f"学生信息: {student}")

# 混合数据类型的字典
mixed_dict = {
    "string_key": "字符串值",
    42: "数字键",
    (1, 2): "元组键",
    "list_value": [1, 2, 3],
    "dict_value": {"nested": "嵌套字典"}
}
print(f"混合类型字典: {mixed_dict}")
```

### 2. 使用dict()函数创建字典

```python
# 创建空字典
empty_dict = dict()
print(f"空字典: {empty_dict}")

# 使用关键字参数创建字典
person = dict(name="李四", age=25, city="北京")
print(f"人员信息: {person}")

# 从键值对列表创建字典
key_value_pairs = [('a', 1), ('b', 2), ('c', 3)]
dict_from_pairs = dict(key_value_pairs)
print(f"从键值对创建: {dict_from_pairs}")

# 从另一个字典创建（复制）
original = {"x": 10, "y": 20}
copied = dict(original)
print(f"复制的字典: {copied}")
```

### 3. 使用字典推导式创建字典

```python
# 基本字典推导式
squares = {x: x**2 for x in range(1, 6)}
print(f"平方数字典: {squares}")

# 带条件的字典推导式
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"偶数平方: {even_squares}")

# 从字符串创建字符计数字典
text = "hello world"
char_count = {char: text.count(char) for char in set(text) if char != ' '}
print(f"字符计数: {char_count}")

# 转换现有字典
original_prices = {"apple": 5, "banana": 3, "orange": 4}
discounted_prices = {item: price * 0.8 for item, price in original_prices.items()}
print(f"打折价格: {discounted_prices}")
```

### 4. 使用zip()函数创建字典

```python
# 从两个列表创建字典
keys = ["name", "age", "city", "job"]
values = ["王五", 30, "上海", "工程师"]
person_info = dict(zip(keys, values))
print(f"个人信息: {person_info}")

# 创建默认值字典
subjects = ["数学", "英语", "物理", "化学"]
default_scores = dict(zip(subjects, [0] * len(subjects)))
print(f"默认成绩: {default_scores}")

# 从多个列表创建复杂字典
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["北京", "上海", "广州"]
people = {name: {"age": age, "city": city} 
          for name, age, city in zip(names, ages, cities)}
print(f"人员列表: {people}")
```

### 5. 使用fromkeys()方法创建字典

```python
# 创建具有相同默认值的字典
keys = ["a", "b", "c", "d"]
default_dict = dict.fromkeys(keys, 0)
print(f"默认值字典: {default_dict}")

# 创建布尔标志字典
features = ["login", "register", "payment", "notification"]
feature_flags = dict.fromkeys(features, False)
print(f"功能标志: {feature_flags}")

# 注意：使用可变对象作为默认值的陷阱
# 错误示例
wrong_dict = dict.fromkeys(["user1", "user2"], [])
wrong_dict["user1"].append("item1")
print(f"错误示例: {wrong_dict}")  # 所有键共享同一个列表

# 正确做法
correct_dict = {key: [] for key in ["user1", "user2"]}
correct_dict["user1"].append("item1")
print(f"正确示例: {correct_dict}")
```

### 6. 字典的复制方法

```python
# 原始字典
original = {"a": 1, "b": [2, 3], "c": {"nested": 4}}

# 浅拷贝方法
shallow_copy1 = original.copy()
shallow_copy2 = dict(original)
shallow_copy3 = {**original}  # 字典解包

print(f"原始字典: {original}")
print(f"浅拷贝1: {shallow_copy1}")

# 深拷贝
import copy
deep_copy = copy.deepcopy(original)

# 测试拷贝效果
original["b"].append(5)
print(f"修改后原始: {original}")
print(f"浅拷贝受影响: {shallow_copy1}")
print(f"深拷贝不受影响: {deep_copy}")
```

### 7. 嵌套字典的创建

```python
# 手动创建嵌套字典
company = {
    "name": "科技公司",
    "departments": {
        "IT": {
            "manager": "张经理",
            "employees": ["程序员A", "程序员B"],
            "budget": 1000000
        },
        "HR": {
            "manager": "李经理",
            "employees": ["HR专员A", "HR专员B"],
            "budget": 500000
        }
    },
    "founded": 2020
}
print(f"公司信息: {company}")

# 动态创建嵌套字典
students_grades = {}
for student in ["Alice", "Bob", "Charlie"]:
    students_grades[student] = {
        "math": 0,
        "english": 0,
        "science": 0
    }
print(f"学生成绩结构: {students_grades}")
```

## 字典的特点和限制

### 键的要求

```python
# 有效的键类型
valid_keys = {
    "string_key": "字符串键",
    42: "整数键",
    3.14: "浮点数键",
    (1, 2, 3): "元组键",
    True: "布尔键"
}
print(f"有效键类型: {valid_keys}")

# 无效的键类型示例（会报错）
try:
    invalid_dict = {[1, 2, 3]: "列表键"}  # 列表不可哈希
except TypeError as e:
    print(f"错误: {e}")

try:
    invalid_dict = {{"nested": "dict"}: "字典键"}  # 字典不可哈希
except TypeError as e:
    print(f"错误: {e}")
```

### 键的唯一性

```python
# 重复键会被覆盖
dict_with_duplicate = {
    "name": "第一个值",
    "age": 25,
    "name": "第二个值"  # 会覆盖第一个
}
print(f"重复键字典: {dict_with_duplicate}")

# 不同类型但相等的键
equal_keys = {
    1: "整数1",
    1.0: "浮点数1",  # 会覆盖整数1
    True: "布尔True"  # 会覆盖浮点数1（因为1 == 1.0 == True）
}
print(f"相等键字典: {equal_keys}")
```

## 实际应用示例

### 配置管理

```python
# 应用配置字典
app_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp",
        "credentials": {
            "username": "admin",
            "password": "secret"
        }
    },
    "cache": {
        "type": "redis",
        "ttl": 3600
    },
    "features": {
        "enable_logging": True,
        "debug_mode": False,
        "max_connections": 100
    }
}
print(f"应用配置: {app_config}")
```

### 数据转换

```python
# CSV数据转字典
csv_data = [
    ["name", "age", "city"],
    ["Alice", "25", "北京"],
    ["Bob", "30", "上海"],
    ["Charlie", "35", "广州"]
]

headers = csv_data[0]
records = []
for row in csv_data[1:]:
    record = dict(zip(headers, row))
    records.append(record)

print(f"CSV转字典: {records}")
```

## 性能考虑

```python
import time

# 比较不同创建方法的性能
def time_creation_methods():
    n = 100000
    
    # 方法1：直接创建
    start = time.time()
    for i in range(n):
        d = {"key": i}
    time1 = time.time() - start
    
    # 方法2：使用dict()
    start = time.time()
    for i in range(n):
        d = dict(key=i)
    time2 = time.time() - start
    
    # 方法3：字典推导式
    start = time.time()
    d = {f"key_{i}": i for i in range(n)}
    time3 = time.time() - start
    
    print(f"直接创建: {time1:.4f}秒")
    print(f"dict()函数: {time2:.4f}秒")
    print(f"字典推导式: {time3:.4f}秒")

# time_creation_methods()  # 取消注释以运行性能测试
```

## 学习要点

1. **选择合适的创建方法**
   - 简单字典：使用花括号 `{}`
   - 动态创建：使用 `dict()` 函数
   - 批量处理：使用字典推导式
   - 默认值：使用 `fromkeys()` 方法

2. **注意键的限制**
   - 键必须是不可变类型
   - 键必须是可哈希的
   - 键在字典中是唯一的

3. **理解拷贝机制**
   - 浅拷贝：只复制字典结构
   - 深拷贝：递归复制所有嵌套对象

4. **性能优化**
   - 字典推导式通常比循环创建更快
   - 避免在循环中重复创建大字典
   - 合理使用字典的内置方法

## 练习题

1. 创建一个学生信息字典，包含姓名、年龄、成绩等信息
2. 使用字典推导式创建一个包含1-10的立方数的字典
3. 从两个列表（城市名和人口数）创建一个字典
4. 创建一个嵌套字典来表示一个简单的组织结构
5. 比较不同字典创建方法的性能差异

## 下一步学习

掌握了字典的创建方法后，接下来学习：
- 字典值的访问和键操作
- 字典内容的修改
- 字典的内置方法
- 字典的遍历和迭代

---

字典的创建是使用字典的第一步，选择合适的创建方法能让你的代码更加简洁和高效！