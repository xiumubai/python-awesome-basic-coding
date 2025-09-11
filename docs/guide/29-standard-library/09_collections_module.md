# 集合和数据结构模块学习

## 学习目标

通过本节学习，你将掌握：

1. **collections模块**：特殊容器数据类型的使用
2. **heapq模块**：堆队列算法和优先级队列
3. **bisect模块**：数组二分查找算法
4. **array模块**：高效数值数组的使用
5. **queue模块**：同步队列类和线程安全
6. **enum模块**：枚举类型的创建和使用
7. **实际应用**：缓存系统、任务调度、日志分析等

## 核心概念

### 数据结构分类

- **计数和统计**：Counter用于计数统计
- **映射扩展**：defaultdict、OrderedDict、ChainMap
- **序列扩展**：deque双端队列、namedtuple命名元组
- **算法支持**：heapq堆算法、bisect二分查找
- **高效存储**：array数组、queue队列
- **类型定义**：enum枚举类型

### 性能特点

- **时间复杂度**：不同数据结构的操作效率
- **空间复杂度**：内存使用和存储效率
- **线程安全**：并发环境下的数据结构选择

## 代码示例

### 1. Counter计数器

```python
from collections import Counter

# 创建Counter
text = "hello world python programming"
char_count = Counter(text)
word_count = Counter(text.split())
list_count = Counter([1, 2, 3, 1, 2, 1, 4, 5, 4])

print(f"字符计数: {char_count}")
print(f"单词计数: {word_count}")
print(f"列表计数: {list_count}")

# Counter方法
print(f"最常见的3个字符: {char_count.most_common(3)}")
print(f"字符'o'的出现次数: {char_count['o']}")
print(f"所有元素列表: {list(char_count.elements())}")

# Counter运算
c1 = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = Counter(['a', 'b', 'b', 'c', 'c', 'c'])

print(f"c1 + c2: {c1 + c2}")
print(f"c1 - c2: {c1 - c2}")
print(f"c1 & c2 (交集): {c1 & c2}")
print(f"c1 | c2 (并集): {c1 | c2}")

# 实际应用：词频统计
article = """
Python is a powerful programming language. Python is easy to learn.
Python has many libraries. Programming with Python is fun.
"""

words = article.lower().replace('.', '').replace(',', '').split()
word_freq = Counter(words)

print("文章词频统计:")
for word, count in word_freq.most_common(5):
    print(f"  '{word}': {count}次")
```

### 2. defaultdict默认字典

```python
from collections import defaultdict

# 基本使用
dd_list = defaultdict(list)
dd_int = defaultdict(int)
dd_set = defaultdict(set)

# 不需要检查键是否存在
dd_list['fruits'].append('apple')
dd_list['fruits'].append('banana')
dd_list['vegetables'].append('carrot')

dd_int['count'] += 1
dd_int['total'] += 100

dd_set['tags'].add('python')
dd_set['tags'].add('programming')

print(f"列表默认字典: {dict(dd_list)}")
print(f"整数默认字典: {dict(dd_int)}")
print(f"集合默认字典: {dict(dd_set)}")

# 分组应用
students = [
    ('Alice', 'Math', 95),
    ('Bob', 'Math', 87),
    ('Alice', 'Science', 92),
    ('Charlie', 'Math', 78),
    ('Bob', 'Science', 89),
    ('Alice', 'English', 88)
]

# 按学生分组
student_grades = defaultdict(list)
for name, subject, grade in students:
    student_grades[name].append((subject, grade))

print("按学生分组的成绩:")
for student, grades in student_grades.items():
    print(f"  {student}: {grades}")
```

### 3. OrderedDict有序字典

```python
from collections import OrderedDict

# 保持插入顺序
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3

print(f"有序字典: {od}")
print(f"键的顺序: {list(od.keys())}")

# 移动操作
od.move_to_end('first')
print(f"移动'first'到末尾: {od}")

od.move_to_end('second', last=False)
print(f"移动'second'到开头: {od}")

# LRU缓存实现
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key in self.cache:
            # 移动到末尾（最近使用）
            self.cache.move_to_end(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        if key in self.cache:
            # 更新并移动到末尾
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # 添加新项
            if len(self.cache) >= self.capacity:
                # 删除最久未使用的项（第一个）
                self.cache.popitem(last=False)
            self.cache[key] = value

lru = LRUCache(3)
lru.put('a', 1)
lru.put('b', 2)
lru.put('c', 3)
print(f"缓存状态: {dict(lru.cache)}")

lru.get('a')  # 访问a
lru.put('d', 4)  # 添加d，应该删除b
print(f"访问a后添加d: {dict(lru.cache)}")
```

### 4. deque双端队列

```python
from collections import deque

# 创建deque
dq = deque([1, 2, 3, 4, 5])
print(f"初始deque: {dq}")

# 两端操作
dq.appendleft(0)
dq.append(6)
print(f"两端添加后: {dq}")

left = dq.popleft()
right = dq.pop()
print(f"两端删除: 左={left}, 右={right}, 剩余={dq}")

# 旋转操作
dq = deque([1, 2, 3, 4, 5])
print(f"原始: {dq}")

dq.rotate(2)
print(f"右旋转2位: {dq}")

dq.rotate(-3)
print(f"左旋转3位: {dq}")

# 限制长度的deque
limited_dq = deque(maxlen=3)
for i in range(6):
    limited_dq.append(i)
    print(f"添加{i}: {limited_dq}")

# 实际应用：滑动窗口
class MovingAverage:
    def __init__(self, window_size):
        self.window_size = window_size
        self.window = deque(maxlen=window_size)
    
    def add_value(self, value):
        self.window.append(value)
        return sum(self.window) / len(self.window)

ma = MovingAverage(3)
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("滑动窗口平均值计算:")
for value in values:
    avg = ma.add_value(value)
    print(f"  添加{value}, 窗口{list(ma.window)}, 平均值: {avg:.2f}")
```

### 5. namedtuple命名元组

```python
from collections import namedtuple

# 创建namedtuple
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')

p1 = Point(1, 2)
p2 = Point(x=3, y=4)
person = Person('Alice', 25, 'New York')

print(f"点p1: {p1}")
print(f"点p2: {p2}")
print(f"人员信息: {person}")

# 访问字段
print(f"p1.x = {p1.x}, p1.y = {p1.y}")
print(f"person.name = {person.name}")
print(f"person[1] = {person[1]}")

# namedtuple方法
print(f"字段名: {person._fields}")
print(f"转为字典: {person._asdict()}")

# 替换字段值
new_person = person._replace(age=26)
print(f"替换年龄: {new_person}")

# 从可迭代对象创建
data = ['Bob', 30, 'London']
person2 = Person._make(data)
print(f"从列表创建: {person2}")

# 实际应用：学生记录
Student = namedtuple('Student', 'id name grade subjects')

students = [
    Student(1, 'Alice', 'A', ['Math', 'Science']),
    Student(2, 'Bob', 'B', ['English', 'History']),
    Student(3, 'Charlie', 'A', ['Math', 'Physics'])
]

print("学生记录:")
for student in students:
    print(f"  ID: {student.id}, 姓名: {student.name}, 等级: {student.grade}")
```

### 6. heapq堆队列

```python
import heapq

# 创建堆
heap = []
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 添加元素
for item in data:
    heapq.heappush(heap, item)

print(f"原始数据: {data}")
print(f"堆结构: {heap}")

# 弹出最小元素
result = []
while heap:
    result.append(heapq.heappop(heap))

print(f"排序结果: {result}")

# 堆化现有列表
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"原始列表: {numbers}")

heapq.heapify(numbers)
print(f"堆化后: {numbers}")

# 获取最大/最小的n个元素
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(f"数据: {data}")
print(f"最小的3个: {heapq.nsmallest(3, data)}")
print(f"最大的3个: {heapq.nlargest(3, data)}")

# 实际应用：任务调度
class Task:
    def __init__(self, priority, name, func):
        self.priority = priority
        self.name = name
        self.func = func
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __repr__(self):
        return f'Task({self.priority}, {self.name})'

# 任务队列
task_queue = []

# 添加任务（优先级越小越重要）
heapq.heappush(task_queue, Task(3, 'backup', lambda: print('执行备份')))
heapq.heappush(task_queue, Task(1, 'critical', lambda: print('执行关键任务')))
heapq.heappush(task_queue, Task(2, 'update', lambda: print('执行更新')))
heapq.heappush(task_queue, Task(1, 'urgent', lambda: print('执行紧急任务')))

print("任务执行顺序:")
while task_queue:
    task = heapq.heappop(task_queue)
    print(f"  执行任务: {task.name} (优先级: {task.priority})")
    task.func()
```

### 7. bisect二分查找

```python
import bisect

# 二分查找
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"有序列表: {sorted_list}")

# 查找插入位置
value = 6
pos = bisect.bisect_left(sorted_list, value)
print(f"{value}的插入位置: {pos}")

pos_right = bisect.bisect_right(sorted_list, 7)
print(f"7的右插入位置: {pos_right}")

# 插入元素
new_list = sorted_list.copy()
bisect.insort(new_list, 6)
bisect.insort(new_list, 12)
print(f"插入6和12后: {new_list}")

# 实际应用：成绩等级划分
def get_grade(score):
    breakpoints = [60, 70, 80, 90]
    grades = ['F', 'D', 'C', 'B', 'A']
    index = bisect.bisect(breakpoints, score)
    return grades[index]

scores = [45, 65, 75, 85, 95, 100]
print("成绩等级:")
for score in scores:
    grade = get_grade(score)
    print(f"  {score}分: {grade}等级")

# 查找范围
data = [1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]
target = 2

left = bisect.bisect_left(data, target)
right = bisect.bisect_right(data, target)

print(f"数据: {data}")
print(f"{target}的范围: [{left}, {right})")
print(f"{target}出现的次数: {right - left}")
```

### 8. queue队列模块

```python
import queue
import time

# FIFO队列
fifo_queue = queue.Queue(maxsize=3)

# 添加元素
for i in range(3):
    fifo_queue.put(f'item_{i}')
    print(f"添加 item_{i}, 队列大小: {fifo_queue.qsize()}")

# 取出元素
while not fifo_queue.empty():
    item = fifo_queue.get()
    print(f"取出: {item}")

# LIFO队列（栈）
lifo_queue = queue.LifoQueue()

for i in range(3):
    lifo_queue.put(f'item_{i}')

print("LIFO取出顺序:")
while not lifo_queue.empty():
    item = lifo_queue.get()
    print(f"  {item}")

# 优先级队列
priority_queue = queue.PriorityQueue()

# 添加带优先级的元素（优先级, 数据）
priority_queue.put((3, 'low priority'))
priority_queue.put((1, 'high priority'))
priority_queue.put((2, 'medium priority'))

print("优先级队列取出顺序:")
while not priority_queue.empty():
    priority, item = priority_queue.get()
    print(f"  优先级{priority}: {item}")
```

### 9. enum枚举类型

```python
from enum import Enum, IntEnum, Flag, IntFlag

# 基本枚举
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(f"Color.RED: {Color.RED}")
print(f"Color.RED.name: {Color.RED.name}")
print(f"Color.RED.value: {Color.RED.value}")

# 枚举比较
print(f"Color.RED == Color.RED: {Color.RED == Color.RED}")
print(f"Color.RED is Color.RED: {Color.RED is Color.RED}")

# 遍历枚举
print("所有颜色:")
for color in Color:
    print(f"  {color.name} = {color.value}")

# 整数枚举
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

print(f"Priority.HIGH: {Priority.HIGH}")
print(f"Priority.HIGH > Priority.LOW: {Priority.HIGH > Priority.LOW}")
print(f"Priority.HIGH + 1: {Priority.HIGH + 1}")

# 标志枚举
class Permission(Flag):
    READ = 1
    WRITE = 2
    EXECUTE = 4

# 组合权限
rw = Permission.READ | Permission.WRITE
rwx = Permission.READ | Permission.WRITE | Permission.EXECUTE

print(f"读写权限: {rw}")
print(f"全部权限: {rwx}")
print(f"包含读权限: {Permission.READ in rw}")
print(f"包含执行权限: {Permission.EXECUTE in rw}")

# 实际应用：HTTP状态码
class HTTPStatus(IntEnum):
    OK = 200
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403

def handle_response(status_code):
    try:
        status = HTTPStatus(status_code)
        if status == HTTPStatus.OK:
            return "请求成功"
        elif status == HTTPStatus.NOT_FOUND:
            return "页面未找到"
        elif status.value >= 500:
            return "服务器错误"
        elif status.value >= 400:
            return "客户端错误"
    except ValueError:
        return "未知状态码"

test_codes = [200, 404, 500, 403, 999]
print("状态码处理:")
for code in test_codes:
    result = handle_response(code)
    print(f"  {code}: {result}")
```

## 重要知识点

### 1. 数据结构选择指南

| 需求 | 推荐数据结构 | 原因 |
|------|-------------|------|
| 计数统计 | Counter | 专门用于计数 |
| 分组数据 | defaultdict | 自动创建默认值 |
| 保持顺序 | OrderedDict | 记住插入顺序 |
| 两端操作 | deque | O(1)时间复杂度 |
| 轻量数据 | namedtuple | 内存效率高 |
| 优先级队列 | heapq | 堆算法实现 |
| 有序插入 | bisect | 二分查找 |
| 数值计算 | array | 内存紧凑 |
| 线程安全 | queue | 内置锁机制 |
| 常量定义 | enum | 类型安全 |

### 2. 性能特点

- **时间复杂度**：
  - deque两端操作：O(1)
  - heapq插入/删除：O(log n)
  - bisect查找：O(log n)
  - Counter计数：O(n)

- **空间复杂度**：
  - array比list节省内存
  - namedtuple比class轻量
  - deque比list在两端操作更高效

### 3. 线程安全性

- **线程安全**：queue模块的所有队列类
- **非线程安全**：collections模块的容器类
- **注意事项**：多线程环境需要额外同步

### 4. 使用场景

- **数据分析**：Counter统计、defaultdict分组
- **缓存系统**：OrderedDict实现LRU
- **算法实现**：heapq优先队列、bisect二分查找
- **系统编程**：queue线程通信、enum状态定义

## 运行方式

```bash
# 运行完整示例
python3 09_collections_module.py

# 或者在Python解释器中逐步测试
python3
>>> from collections import Counter
>>> Counter('hello world')
Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

## 练习建议

### 基础练习

1. **Counter练习**：
   - 统计文本中的词频
   - 分析日志文件中的错误类型
   - 计算列表中元素的出现次数

2. **deque练习**：
   - 实现滑动窗口算法
   - 创建回文检查器
   - 模拟队列和栈的操作

3. **heapq练习**：
   - 实现优先级任务调度
   - 找到数据流中的中位数
   - 合并多个有序列表

### 进阶练习

1. **缓存系统**：
   - 实现LRU缓存
   - 创建多级缓存系统
   - 设计缓存淘汰策略

2. **数据处理**：
   - 构建倒排索引
   - 实现数据分组和聚合
   - 创建时间序列数据结构

3. **算法应用**：
   - 实现Dijkstra算法
   - 创建事件调度系统
   - 设计状态机

## 注意事项

### 1. 性能考虑

- 根据操作类型选择合适的数据结构
- 注意时间和空间复杂度
- 大数据量时考虑内存使用

### 2. 线程安全

- 多线程环境使用queue模块
- collections模块需要额外同步
- 避免竞态条件

### 3. 内存管理

- array比list更节省内存
- namedtuple比普通类更轻量
- 注意循环引用问题

### 4. 最佳实践

- 选择最适合的数据结构
- 理解各种数据结构的特点
- 在性能关键场景进行基准测试
- 考虑代码的可读性和维护性

通过本节学习，你将掌握Python中各种高级数据结构的使用方法，能够根据不同的应用场景选择最合适的数据结构，提高程序的性能和效率。