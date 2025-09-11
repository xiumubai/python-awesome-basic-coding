#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
集合和数据结构模块学习

本模块演示Python标准库中集合和数据结构相关的模块：
- collections: 特殊容器数据类型
- heapq: 堆队列算法
- bisect: 数组二分查找算法
- array: 高效数值数组
- queue: 同步队列类
- enum: 枚举类型

学习目标：
1. 掌握collections模块的各种容器类型
2. 理解堆队列的使用场景
3. 学会使用二分查找算法
4. 了解高效数组的使用
5. 掌握队列的不同实现
6. 学会创建和使用枚举类型
"""

import collections
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap
import heapq
import bisect
import array
import queue
import enum
from enum import Enum, IntEnum, Flag, IntFlag
import threading
import time


def counter_demo():
    """演示Counter类的使用"""
    print("=" * 50)
    print("Counter类演示")
    print("=" * 50)
    
    # 创建Counter
    print("1. 创建Counter:")
    text = "hello world python programming"
    char_count = Counter(text)
    word_count = Counter(text.split())
    list_count = Counter([1, 2, 3, 1, 2, 1, 4, 5, 4])
    
    print(f"  字符计数: {char_count}")
    print(f"  单词计数: {word_count}")
    print(f"  列表计数: {list_count}")
    
    # Counter方法
    print("\n2. Counter方法:")
    print(f"  最常见的3个字符: {char_count.most_common(3)}")
    print(f"  字符'o'的出现次数: {char_count['o']}")
    print(f"  所有元素列表: {list(char_count.elements())}")
    
    # Counter运算
    print("\n3. Counter运算:")
    c1 = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
    c2 = Counter(['a', 'b', 'b', 'c', 'c', 'c'])
    
    print(f"  c1: {c1}")
    print(f"  c2: {c2}")
    print(f"  c1 + c2: {c1 + c2}")
    print(f"  c1 - c2: {c1 - c2}")
    print(f"  c1 & c2 (交集): {c1 & c2}")
    print(f"  c1 | c2 (并集): {c1 | c2}")
    
    # 实际应用：词频统计
    print("\n4. 实际应用 - 词频统计:")
    article = """
    Python is a powerful programming language. Python is easy to learn.
    Python has many libraries. Programming with Python is fun.
    """
    
    words = article.lower().replace('.', '').replace(',', '').split()
    word_freq = Counter(words)
    
    print(f"  文章词频统计:")
    for word, count in word_freq.most_common(5):
        print(f"    '{word}': {count}次")


def defaultdict_demo():
    """演示defaultdict类的使用"""
    print("\n" + "=" * 50)
    print("defaultdict类演示")
    print("=" * 50)
    
    # 基本使用
    print("1. 基本使用:")
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
    
    print(f"  列表默认字典: {dict(dd_list)}")
    print(f"  整数默认字典: {dict(dd_int)}")
    print(f"  集合默认字典: {dict(dd_set)}")
    
    # 分组应用
    print("\n2. 分组应用:")
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
    
    print("  按学生分组的成绩:")
    for student, grades in student_grades.items():
        print(f"    {student}: {grades}")
    
    # 按科目分组
    subject_grades = defaultdict(list)
    for name, subject, grade in students:
        subject_grades[subject].append((name, grade))
    
    print("\n  按科目分组的成绩:")
    for subject, grades in subject_grades.items():
        print(f"    {subject}: {grades}")


def ordereddict_demo():
    """演示OrderedDict类的使用"""
    print("\n" + "=" * 50)
    print("OrderedDict类演示")
    print("=" * 50)
    
    # 保持插入顺序
    print("1. 保持插入顺序:")
    od = OrderedDict()
    od['first'] = 1
    od['second'] = 2
    od['third'] = 3
    
    print(f"  有序字典: {od}")
    print(f"  键的顺序: {list(od.keys())}")
    
    # 移动到末尾
    print("\n2. 移动操作:")
    od.move_to_end('first')
    print(f"  移动'first'到末尾: {od}")
    
    od.move_to_end('second', last=False)
    print(f"  移动'second'到开头: {od}")
    
    # LRU缓存实现
    print("\n3. LRU缓存实现:")
    
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
    print(f"  缓存状态: {dict(lru.cache)}")
    
    lru.get('a')  # 访问a
    lru.put('d', 4)  # 添加d，应该删除b
    print(f"  访问a后添加d: {dict(lru.cache)}")


def deque_demo():
    """演示deque类的使用"""
    print("\n" + "=" * 50)
    print("deque类演示")
    print("=" * 50)
    
    # 创建deque
    print("1. 创建和基本操作:")
    dq = deque([1, 2, 3, 4, 5])
    print(f"  初始deque: {dq}")
    
    # 两端操作
    dq.appendleft(0)
    dq.append(6)
    print(f"  两端添加后: {dq}")
    
    left = dq.popleft()
    right = dq.pop()
    print(f"  两端删除: 左={left}, 右={right}, 剩余={dq}")
    
    # 旋转操作
    print("\n2. 旋转操作:")
    dq = deque([1, 2, 3, 4, 5])
    print(f"  原始: {dq}")
    
    dq.rotate(2)
    print(f"  右旋转2位: {dq}")
    
    dq.rotate(-3)
    print(f"  左旋转3位: {dq}")
    
    # 限制长度的deque
    print("\n3. 限制长度的deque:")
    limited_dq = deque(maxlen=3)
    for i in range(6):
        limited_dq.append(i)
        print(f"  添加{i}: {limited_dq}")
    
    # 实际应用：滑动窗口
    print("\n4. 实际应用 - 滑动窗口平均值:")
    
    class MovingAverage:
        def __init__(self, window_size):
            self.window_size = window_size
            self.window = deque(maxlen=window_size)
        
        def add_value(self, value):
            self.window.append(value)
            return sum(self.window) / len(self.window)
    
    ma = MovingAverage(3)
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("  滑动窗口平均值计算:")
    for value in values:
        avg = ma.add_value(value)
        print(f"    添加{value}, 窗口{list(ma.window)}, 平均值: {avg:.2f}")


def namedtuple_demo():
    """演示namedtuple的使用"""
    print("\n" + "=" * 50)
    print("namedtuple演示")
    print("=" * 50)
    
    # 创建namedtuple
    print("1. 创建namedtuple:")
    Point = namedtuple('Point', ['x', 'y'])
    Person = namedtuple('Person', 'name age city')
    
    p1 = Point(1, 2)
    p2 = Point(x=3, y=4)
    person = Person('Alice', 25, 'New York')
    
    print(f"  点p1: {p1}")
    print(f"  点p2: {p2}")
    print(f"  人员信息: {person}")
    
    # 访问字段
    print("\n2. 访问字段:")
    print(f"  p1.x = {p1.x}, p1.y = {p1.y}")
    print(f"  person.name = {person.name}")
    print(f"  person[1] = {person[1]}")
    
    # namedtuple方法
    print("\n3. namedtuple方法:")
    print(f"  字段名: {person._fields}")
    print(f"  转为字典: {person._asdict()}")
    
    # 替换字段值
    new_person = person._replace(age=26)
    print(f"  替换年龄: {new_person}")
    
    # 从可迭代对象创建
    data = ['Bob', 30, 'London']
    person2 = Person._make(data)
    print(f"  从列表创建: {person2}")
    
    # 实际应用：数据记录
    print("\n4. 实际应用 - 学生记录:")
    Student = namedtuple('Student', 'id name grade subjects')
    
    students = [
        Student(1, 'Alice', 'A', ['Math', 'Science']),
        Student(2, 'Bob', 'B', ['English', 'History']),
        Student(3, 'Charlie', 'A', ['Math', 'Physics'])
    ]
    
    print("  学生记录:")
    for student in students:
        print(f"    ID: {student.id}, 姓名: {student.name}, 等级: {student.grade}")
    
    # 按等级分组
    grade_groups = defaultdict(list)
    for student in students:
        grade_groups[student.grade].append(student.name)
    
    print("\n  按等级分组:")
    for grade, names in grade_groups.items():
        print(f"    等级{grade}: {names}")


def chainmap_demo():
    """演示ChainMap的使用"""
    print("\n" + "=" * 50)
    print("ChainMap演示")
    print("=" * 50)
    
    # 创建ChainMap
    print("1. 创建ChainMap:")
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    dict3 = {'c': 5, 'd': 6}
    
    cm = ChainMap(dict1, dict2, dict3)
    print(f"  dict1: {dict1}")
    print(f"  dict2: {dict2}")
    print(f"  dict3: {dict3}")
    print(f"  ChainMap: {cm}")
    
    # 查找顺序
    print("\n2. 查找顺序:")
    print(f"  cm['a'] = {cm['a']} (来自dict1)")
    print(f"  cm['b'] = {cm['b']} (来自dict1，优先级高)")
    print(f"  cm['c'] = {cm['c']} (来自dict2，优先级高)")
    print(f"  cm['d'] = {cm['d']} (来自dict3)")
    
    # 修改操作
    print("\n3. 修改操作:")
    cm['e'] = 7  # 添加到第一个字典
    print(f"  添加'e'后 dict1: {dict1}")
    print(f"  ChainMap: {cm}")
    
    # 新建子上下文
    print("\n4. 新建子上下文:")
    child = cm.new_child({'x': 100})
    print(f"  子上下文: {child}")
    print(f"  child['x'] = {child['x']}")
    print(f"  child['a'] = {child['a']} (继承自父上下文)")
    
    # 实际应用：配置管理
    print("\n5. 实际应用 - 配置管理:")
    
    # 默认配置
    default_config = {
        'host': 'localhost',
        'port': 8000,
        'debug': False,
        'timeout': 30
    }
    
    # 用户配置
    user_config = {
        'port': 9000,
        'debug': True
    }
    
    # 环境变量配置
    env_config = {
        'host': '0.0.0.0'
    }
    
    # 配置优先级：环境变量 > 用户配置 > 默认配置
    config = ChainMap(env_config, user_config, default_config)
    
    print("  最终配置:")
    for key, value in config.items():
        print(f"    {key}: {value}")


def heapq_demo():
    """演示heapq模块的使用"""
    print("\n" + "=" * 50)
    print("heapq模块演示")
    print("=" * 50)
    
    # 创建堆
    print("1. 创建和操作堆:")
    heap = []
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    
    # 添加元素
    for item in data:
        heapq.heappush(heap, item)
    
    print(f"  原始数据: {data}")
    print(f"  堆结构: {heap}")
    
    # 弹出最小元素
    print("\n2. 弹出元素:")
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    
    print(f"  排序结果: {result}")
    
    # 堆化现有列表
    print("\n3. 堆化现有列表:")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"  原始列表: {numbers}")
    
    heapq.heapify(numbers)
    print(f"  堆化后: {numbers}")
    
    # 获取最大/最小的n个元素
    print("\n4. 获取最大/最小的n个元素:")
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(f"  数据: {data}")
    print(f"  最小的3个: {heapq.nsmallest(3, data)}")
    print(f"  最大的3个: {heapq.nlargest(3, data)}")
    
    # 实际应用：任务调度
    print("\n5. 实际应用 - 任务调度:")
    
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
    
    print("  任务执行顺序:")
    while task_queue:
        task = heapq.heappop(task_queue)
        print(f"    执行任务: {task.name} (优先级: {task.priority})")
        task.func()


def bisect_demo():
    """演示bisect模块的使用"""
    print("\n" + "=" * 50)
    print("bisect模块演示")
    print("=" * 50)
    
    # 二分查找
    print("1. 二分查找:")
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    print(f"  有序列表: {sorted_list}")
    
    # 查找插入位置
    value = 6
    pos = bisect.bisect_left(sorted_list, value)
    print(f"  {value}的插入位置: {pos}")
    
    pos_right = bisect.bisect_right(sorted_list, 7)
    print(f"  7的右插入位置: {pos_right}")
    
    # 插入元素
    print("\n2. 插入元素:")
    new_list = sorted_list.copy()
    bisect.insort(new_list, 6)
    bisect.insort(new_list, 12)
    print(f"  插入6和12后: {new_list}")
    
    # 实际应用：成绩等级划分
    print("\n3. 实际应用 - 成绩等级划分:")
    
    def get_grade(score):
        breakpoints = [60, 70, 80, 90]
        grades = ['F', 'D', 'C', 'B', 'A']
        index = bisect.bisect(breakpoints, score)
        return grades[index]
    
    scores = [45, 65, 75, 85, 95, 100]
    print("  成绩等级:")
    for score in scores:
        grade = get_grade(score)
        print(f"    {score}分: {grade}等级")
    
    # 查找范围
    print("\n4. 查找范围:")
    data = [1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]
    target = 2
    
    left = bisect.bisect_left(data, target)
    right = bisect.bisect_right(data, target)
    
    print(f"  数据: {data}")
    print(f"  {target}的范围: [{left}, {right})")
    print(f"  {target}出现的次数: {right - left}")


def array_demo():
    """演示array模块的使用"""
    print("\n" + "=" * 50)
    print("array模块演示")
    print("=" * 50)
    
    # 创建数组
    print("1. 创建数组:")
    int_array = array.array('i', [1, 2, 3, 4, 5])  # 整数数组
    float_array = array.array('f', [1.1, 2.2, 3.3])  # 浮点数组
    
    print(f"  整数数组: {int_array}")
    print(f"  浮点数组: {float_array}")
    print(f"  数组类型码: {int_array.typecode}")
    print(f"  元素大小: {int_array.itemsize}字节")
    
    # 数组操作
    print("\n2. 数组操作:")
    int_array.append(6)
    int_array.extend([7, 8, 9])
    print(f"  添加元素后: {int_array}")
    
    int_array.insert(0, 0)
    print(f"  插入元素后: {int_array}")
    
    removed = int_array.pop()
    print(f"  删除元素: {removed}, 剩余: {int_array}")
    
    # 数组与列表的性能比较
    print("\n3. 性能比较:")
    import sys
    
    # 内存使用比较
    list_data = list(range(1000))
    array_data = array.array('i', range(1000))
    
    print(f"  列表内存使用: {sys.getsizeof(list_data)}字节")
    print(f"  数组内存使用: {sys.getsizeof(array_data)}字节")
    print(f"  内存节省: {(sys.getsizeof(list_data) - sys.getsizeof(array_data)) / sys.getsizeof(list_data) * 100:.1f}%")
    
    # 文件操作
    print("\n4. 文件操作:")
    # 注意：这里只演示方法，不实际写文件
    print("  数组可以高效地读写二进制文件")
    print(f"  tobytes()方法: {int_array.tobytes()[:20]}...")
    print(f"  tolist()方法: {int_array.tolist()}")


def queue_demo():
    """演示queue模块的使用"""
    print("\n" + "=" * 50)
    print("queue模块演示")
    print("=" * 50)
    
    # FIFO队列
    print("1. FIFO队列:")
    fifo_queue = queue.Queue(maxsize=3)
    
    # 添加元素
    for i in range(3):
        fifo_queue.put(f'item_{i}')
        print(f"  添加 item_{i}, 队列大小: {fifo_queue.qsize()}")
    
    # 取出元素
    while not fifo_queue.empty():
        item = fifo_queue.get()
        print(f"  取出: {item}")
    
    # LIFO队列（栈）
    print("\n2. LIFO队列（栈）:")
    lifo_queue = queue.LifoQueue()
    
    for i in range(3):
        lifo_queue.put(f'item_{i}')
    
    print("  LIFO取出顺序:")
    while not lifo_queue.empty():
        item = lifo_queue.get()
        print(f"    {item}")
    
    # 优先级队列
    print("\n3. 优先级队列:")
    priority_queue = queue.PriorityQueue()
    
    # 添加带优先级的元素（优先级, 数据）
    priority_queue.put((3, 'low priority'))
    priority_queue.put((1, 'high priority'))
    priority_queue.put((2, 'medium priority'))
    
    print("  优先级队列取出顺序:")
    while not priority_queue.empty():
        priority, item = priority_queue.get()
        print(f"    优先级{priority}: {item}")
    
    # 实际应用：生产者消费者模式
    print("\n4. 实际应用 - 生产者消费者:")
    
    def producer(q, name, items):
        for item in items:
            q.put(f'{name}_{item}')
            print(f"  生产者{name}生产: {item}")
            time.sleep(0.1)
    
    def consumer(q, name):
        while True:
            try:
                item = q.get(timeout=1)
                print(f"  消费者{name}消费: {item}")
                q.task_done()
                time.sleep(0.1)
            except queue.Empty:
                break
    
    # 创建队列
    work_queue = queue.Queue()
    
    # 模拟生产和消费
    producer(work_queue, 'P1', ['task1', 'task2', 'task3'])
    consumer(work_queue, 'C1')


def enum_demo():
    """演示enum模块的使用"""
    print("\n" + "=" * 50)
    print("enum模块演示")
    print("=" * 50)
    
    # 基本枚举
    print("1. 基本枚举:")
    
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    print(f"  Color.RED: {Color.RED}")
    print(f"  Color.RED.name: {Color.RED.name}")
    print(f"  Color.RED.value: {Color.RED.value}")
    
    # 枚举比较
    print("\n2. 枚举比较:")
    print(f"  Color.RED == Color.RED: {Color.RED == Color.RED}")
    print(f"  Color.RED is Color.RED: {Color.RED is Color.RED}")
    
    # 遍历枚举
    print("\n3. 遍历枚举:")
    print("  所有颜色:")
    for color in Color:
        print(f"    {color.name} = {color.value}")
    
    # 整数枚举
    print("\n4. 整数枚举:")
    
    class Priority(IntEnum):
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        CRITICAL = 4
    
    print(f"  Priority.HIGH: {Priority.HIGH}")
    print(f"  Priority.HIGH > Priority.LOW: {Priority.HIGH > Priority.LOW}")
    print(f"  Priority.HIGH + 1: {Priority.HIGH + 1}")
    
    # 标志枚举
    print("\n5. 标志枚举:")
    
    class Permission(Flag):
        READ = 1
        WRITE = 2
        EXECUTE = 4
    
    # 组合权限
    rw = Permission.READ | Permission.WRITE
    rwx = Permission.READ | Permission.WRITE | Permission.EXECUTE
    
    print(f"  读写权限: {rw}")
    print(f"  全部权限: {rwx}")
    print(f"  包含读权限: {Permission.READ in rw}")
    print(f"  包含执行权限: {Permission.EXECUTE in rw}")
    
    # 实际应用：HTTP状态码
    print("\n6. 实际应用 - HTTP状态码:")
    
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
    print("  状态码处理:")
    for code in test_codes:
        result = handle_response(code)
        print(f"    {code}: {result}")


def practical_applications():
    """集合和数据结构的实际应用"""
    print("\n" + "=" * 50)
    print("实际应用综合示例")
    print("=" * 50)
    
    # 1. 日志分析系统
    print("1. 日志分析系统:")
    
    # 模拟日志数据
    log_entries = [
        "2024-01-15 10:30:15 INFO User login: alice",
        "2024-01-15 10:31:22 ERROR Database connection failed",
        "2024-01-15 10:32:10 INFO User login: bob",
        "2024-01-15 10:33:45 WARNING High memory usage",
        "2024-01-15 10:34:12 INFO User logout: alice",
        "2024-01-15 10:35:33 ERROR File not found",
        "2024-01-15 10:36:21 INFO User login: charlie",
    ]
    
    # 使用Counter统计日志级别
    log_levels = Counter()
    user_actions = defaultdict(list)
    
    for entry in log_entries:
        parts = entry.split()
        timestamp = f"{parts[0]} {parts[1]}"
        level = parts[2]
        message = " ".join(parts[3:])
        
        log_levels[level] += 1
        
        if "User" in message:
            if "login" in message:
                user = message.split(": ")[1]
                user_actions[user].append((timestamp, "login"))
            elif "logout" in message:
                user = message.split(": ")[1]
                user_actions[user].append((timestamp, "logout"))
    
    print("  日志级别统计:")
    for level, count in log_levels.most_common():
        print(f"    {level}: {count}次")
    
    print("\n  用户活动:")
    for user, actions in user_actions.items():
        print(f"    {user}: {actions}")
    
    # 2. 缓存系统
    print("\n2. 多级缓存系统:")
    
    class MultiLevelCache:
        def __init__(self, l1_size=3, l2_size=5):
            self.l1_cache = OrderedDict()  # L1缓存（最快）
            self.l2_cache = OrderedDict()  # L2缓存（较快）
            self.l1_size = l1_size
            self.l2_size = l2_size
            self.stats = Counter()
        
        def get(self, key):
            # 检查L1缓存
            if key in self.l1_cache:
                self.l1_cache.move_to_end(key)
                self.stats['l1_hit'] += 1
                return self.l1_cache[key]
            
            # 检查L2缓存
            if key in self.l2_cache:
                value = self.l2_cache[key]
                # 提升到L1缓存
                self._put_l1(key, value)
                del self.l2_cache[key]
                self.stats['l2_hit'] += 1
                return value
            
            # 缓存未命中
            self.stats['miss'] += 1
            return None
        
        def put(self, key, value):
            self._put_l1(key, value)
        
        def _put_l1(self, key, value):
            if key in self.l1_cache:
                self.l1_cache[key] = value
                self.l1_cache.move_to_end(key)
            else:
                if len(self.l1_cache) >= self.l1_size:
                    # L1满了，移动到L2
                    old_key, old_value = self.l1_cache.popitem(last=False)
                    self._put_l2(old_key, old_value)
                self.l1_cache[key] = value
        
        def _put_l2(self, key, value):
            if len(self.l2_cache) >= self.l2_size:
                self.l2_cache.popitem(last=False)
            self.l2_cache[key] = value
    
    cache = MultiLevelCache()
    
    # 模拟缓存操作
    operations = [
        ('put', 'a', 1), ('put', 'b', 2), ('put', 'c', 3), ('put', 'd', 4),
        ('get', 'a'), ('get', 'b'), ('put', 'e', 5), ('get', 'c'), ('get', 'd')
    ]
    
    print("  缓存操作:")
    for op in operations:
        if op[0] == 'put':
            cache.put(op[1], op[2])
            print(f"    PUT {op[1]}={op[2]}")
        else:
            result = cache.get(op[1])
            print(f"    GET {op[1]} -> {result}")
    
    print(f"\n  缓存统计: {dict(cache.stats)}")


def main():
    """主函数"""
    print("Python标准库 - 集合和数据结构模块学习")
    print("=" * 60)
    
    # 演示各个模块
    counter_demo()
    defaultdict_demo()
    ordereddict_demo()
    deque_demo()
    namedtuple_demo()
    chainmap_demo()
    heapq_demo()
    bisect_demo()
    array_demo()
    queue_demo()
    enum_demo()
    practical_applications()
    
    print("\n" + "=" * 50)
    print("学习要点总结")
    print("=" * 50)
    print("1. Counter: 计数器，统计可哈希对象")
    print("2. defaultdict: 带默认值的字典")
    print("3. OrderedDict: 有序字典，记住插入顺序")
    print("4. deque: 双端队列，两端操作高效")
    print("5. namedtuple: 命名元组，轻量级数据容器")
    print("6. ChainMap: 链式映射，多字典视图")
    print("7. heapq: 堆队列，优先级队列实现")
    print("8. bisect: 二分查找，维护有序列表")
    print("9. array: 高效数值数组，节省内存")
    print("10. queue: 线程安全队列，多线程通信")
    print("11. enum: 枚举类型，定义常量集合")
    print("12. 选择合适的数据结构提高程序效率")
    print("13. 了解各种数据结构的时间复杂度")
    print("14. 在并发编程中使用线程安全的数据结构")
    print("15. 集合和数据结构是算法实现的基础")


if __name__ == "__main__":
    main()