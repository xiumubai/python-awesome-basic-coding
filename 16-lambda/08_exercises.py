#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lambda表达式综合练习

本文件包含Lambda表达式的各种练习题，
从基础到高级，帮助巩固Lambda表达式的使用。

练习内容：
1. 基础语法练习
2. 与内置函数结合练习
3. 数据处理练习
4. 实际应用练习
5. 高级应用练习
"""

import functools
from datetime import datetime, timedelta
import random
import json

print("=== Lambda表达式综合练习 ===")
print("通过实际练习掌握Lambda表达式的各种用法")
print()

# ==================== 练习1：基础语法练习 ====================
print("练习1：基础语法练习")
print("=" * 50)

# 练习1.1：创建基本的Lambda表达式
print("1.1 创建基本Lambda表达式")

# TODO: 创建一个Lambda表达式，计算两个数的和
add = lambda x, y: x + y
print(f"add(3, 5) = {add(3, 5)}")

# TODO: 创建一个Lambda表达式，判断数字是否为偶数
is_even = lambda x: x % 2 == 0
print(f"is_even(4) = {is_even(4)}")
print(f"is_even(7) = {is_even(7)}")

# TODO: 创建一个Lambda表达式，返回三个数中的最大值
max_of_three = lambda x, y, z: max(x, y, z)
print(f"max_of_three(10, 25, 15) = {max_of_three(10, 25, 15)}")

# TODO: 创建一个Lambda表达式，计算字符串长度
str_len = lambda s: len(s)
print(f"str_len('Hello World') = {str_len('Hello World')}")

# 练习1.2：带默认参数的Lambda
print("\n1.2 带默认参数的Lambda")

# TODO: 创建一个Lambda表达式，计算圆的面积（π默认为3.14159）
circle_area = lambda r, pi=3.14159: pi * r ** 2
print(f"circle_area(5) = {circle_area(5):.2f}")
print(f"circle_area(5, 3.14) = {circle_area(5, 3.14):.2f}")

# TODO: 创建一个Lambda表达式，格式化问候语
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(f"greet('Alice') = {greet('Alice')}")
print(f"greet('Bob', 'Hi') = {greet('Bob', 'Hi')}")
print()

# ==================== 练习2：与内置函数结合练习 ====================
print("练习2：与内置函数结合练习")
print("=" * 50)

# 练习2.1：map函数练习
print("2.1 map函数练习")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原始数字: {numbers}")

# TODO: 使用map和lambda将所有数字平方
squares = list(map(lambda x: x ** 2, numbers))
print(f"平方结果: {squares}")

# TODO: 使用map和lambda将数字转换为字符串，并添加前缀
str_numbers = list(map(lambda x: f"No.{x}", numbers))
print(f"字符串转换: {str_numbers[:5]}...")  # 只显示前5个

# TODO: 使用map处理字符串列表，转换为大写并添加感叹号
words = ['hello', 'world', 'python', 'lambda']
excited_words = list(map(lambda w: w.upper() + '!', words))
print(f"激动的单词: {excited_words}")

# 练习2.2：filter函数练习
print("\n2.2 filter函数练习")

# TODO: 使用filter和lambda筛选偶数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数: {even_numbers}")

# TODO: 使用filter和lambda筛选长度大于5的单词
long_words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
filtered_words = list(filter(lambda w: len(w) > 5, long_words))
print(f"长单词: {filtered_words}")

# TODO: 使用filter筛选正数
mixed_numbers = [-5, -2, 0, 3, -1, 8, -4, 7, 2]
positive_numbers = list(filter(lambda x: x > 0, mixed_numbers))
print(f"正数: {positive_numbers}")

# 练习2.3：reduce函数练习
print("\n2.3 reduce函数练习")

# TODO: 使用reduce和lambda计算数字列表的乘积
product = functools.reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(f"1到5的乘积: {product}")

# TODO: 使用reduce找出最大值
max_value = functools.reduce(lambda x, y: x if x > y else y, [45, 23, 78, 12, 67, 89])
print(f"最大值: {max_value}")

# TODO: 使用reduce连接字符串
sentence = functools.reduce(lambda x, y: x + ' ' + y, ['Python', 'is', 'awesome'])
print(f"连接句子: {sentence}")

# 练习2.4：sorted函数练习
print("\n2.4 sorted函数练习")

students = [
    {'name': '张三', 'age': 20, 'score': 85},
    {'name': '李四', 'age': 19, 'score': 92},
    {'name': '王五', 'age': 21, 'score': 78},
    {'name': '赵六', 'age': 20, 'score': 88}
]

# TODO: 按分数降序排序
score_sorted = sorted(students, key=lambda s: s['score'], reverse=True)
print("按分数排序:")
for s in score_sorted:
    print(f"  {s['name']}: {s['score']}分")

# TODO: 按年龄升序，分数降序排序
age_score_sorted = sorted(students, key=lambda s: (s['age'], -s['score']))
print("按年龄和分数排序:")
for s in age_score_sorted:
    print(f"  {s['name']}: {s['age']}岁, {s['score']}分")
print()

# ==================== 练习3：数据处理练习 ====================
print("练习3：数据处理练习")
print("=" * 50)

# 练习3.1：列表处理
print("3.1 列表处理")

# 销售数据
sales_data = [
    {'product': 'iPhone', 'price': 999, 'quantity': 10},
    {'product': 'iPad', 'price': 599, 'quantity': 15},
    {'product': 'MacBook', 'price': 1299, 'quantity': 5},
    {'product': 'AirPods', 'price': 179, 'quantity': 25},
    {'product': 'Apple Watch', 'price': 399, 'quantity': 12}
]

# TODO: 计算每个产品的总销售额
sales_with_total = list(map(lambda item: {
    **item, 
    'total': item['price'] * item['quantity']
}, sales_data))

print("产品销售额:")
for item in sales_with_total:
    print(f"  {item['product']}: ${item['total']}")

# TODO: 筛选销售额大于5000的产品
high_sales = list(filter(lambda item: item['total'] > 5000, sales_with_total))
print(f"\n高销售额产品: {[item['product'] for item in high_sales]}")

# TODO: 计算总销售额
total_sales = functools.reduce(lambda acc, item: acc + item['total'], sales_with_total, 0)
print(f"总销售额: ${total_sales}")

# 练习3.2：字符串处理
print("\n3.2 字符串处理")

# 日志数据
log_entries = [
    "2023-12-01 10:30:15 INFO User login successful",
    "2023-12-01 10:31:22 ERROR Database connection failed",
    "2023-12-01 10:32:10 INFO Data processing completed",
    "2023-12-01 10:33:45 WARNING Low disk space",
    "2023-12-01 10:34:12 ERROR File not found"
]

# TODO: 提取错误日志
error_logs = list(filter(lambda log: 'ERROR' in log, log_entries))
print("错误日志:")
for log in error_logs:
    print(f"  {log}")

# TODO: 提取时间戳
timestamps = list(map(lambda log: log.split()[1], log_entries))
print(f"\n时间戳: {timestamps}")

# TODO: 统计各级别日志数量
log_levels = list(map(lambda log: log.split()[2], log_entries))
level_count = {}
for level in log_levels:
    level_count[level] = level_count.get(level, 0) + 1
print(f"日志级别统计: {level_count}")

# 练习3.3：嵌套数据处理
print("\n3.3 嵌套数据处理")

# 学校数据
school_data = {
    'classes': [
        {
            'name': '高一(1)班',
            'students': [
                {'name': '张三', 'subjects': {'数学': 85, '语文': 92, '英语': 78}},
                {'name': '李四', 'subjects': {'数学': 92, '语文': 88, '英语': 95}},
                {'name': '王五', 'subjects': {'数学': 78, '语文': 85, '英语': 82}}
            ]
        },
        {
            'name': '高一(2)班',
            'students': [
                {'name': '赵六', 'subjects': {'数学': 88, '语文': 90, '英语': 87}},
                {'name': '钱七', 'subjects': {'数学': 95, '语文': 82, '英语': 89}}
            ]
        }
    ]
}

# TODO: 计算每个学生的平均分
for class_info in school_data['classes']:
    print(f"{class_info['name']}平均分:")
    students_with_avg = list(map(
        lambda student: {
            **student,
            'average': sum(student['subjects'].values()) / len(student['subjects'])
        },
        class_info['students']
    ))
    
    for student in students_with_avg:
        print(f"  {student['name']}: {student['average']:.1f}")

# TODO: 找出数学成绩最高的学生
all_students = []
for class_info in school_data['classes']:
    all_students.extend(class_info['students'])

best_math_student = max(all_students, key=lambda s: s['subjects']['数学'])
print(f"\n数学最高分: {best_math_student['name']} - {best_math_student['subjects']['数学']}分")
print()

# ==================== 练习4：实际应用练习 ====================
print("练习4：实际应用练习")
print("=" * 50)

# 练习4.1：数据分析
print("4.1 数据分析")

# 股票数据
stock_data = [
    {'symbol': 'AAPL', 'price': 150.25, 'volume': 1000000, 'change': 2.5},
    {'symbol': 'GOOGL', 'price': 2800.50, 'volume': 500000, 'change': -1.2},
    {'symbol': 'MSFT', 'price': 300.75, 'volume': 800000, 'change': 1.8},
    {'symbol': 'TSLA', 'price': 250.00, 'volume': 1200000, 'change': -3.5},
    {'symbol': 'AMZN', 'price': 3200.25, 'volume': 600000, 'change': 0.8}
]

# TODO: 筛选上涨的股票
rising_stocks = list(filter(lambda stock: stock['change'] > 0, stock_data))
print("上涨股票:")
for stock in rising_stocks:
    print(f"  {stock['symbol']}: +{stock['change']}%")

# TODO: 按交易量排序
volume_sorted = sorted(stock_data, key=lambda s: s['volume'], reverse=True)
print("\n按交易量排序:")
for stock in volume_sorted:
    print(f"  {stock['symbol']}: {stock['volume']:,}")

# TODO: 计算总市值（假设每只股票1000万股）
shares = 10000000
total_market_cap = functools.reduce(
    lambda acc, stock: acc + stock['price'] * shares,
    stock_data,
    0
)
print(f"\n总市值: ${total_market_cap:,.0f}")

# 练习4.2：文本处理
print("\n4.2 文本处理")

# 文章数据
articles = [
    {
        'title': 'Python编程入门',
        'content': 'Python是一种简单易学的编程语言，适合初学者学习。',
        'tags': ['Python', '编程', '入门'],
        'views': 1500,
        'date': '2023-12-01'
    },
    {
        'title': 'Lambda表达式详解',
        'content': 'Lambda表达式是Python中的匿名函数，可以简化代码。',
        'tags': ['Python', 'Lambda', '函数'],
        'views': 800,
        'date': '2023-12-02'
    },
    {
        'title': '数据分析实战',
        'content': '使用Python进行数据分析，包括数据清洗和可视化。',
        'tags': ['Python', '数据分析', '可视化'],
        'views': 2200,
        'date': '2023-12-03'
    }
]

# TODO: 筛选包含'Python'标签的文章
python_articles = list(filter(lambda article: 'Python' in article['tags'], articles))
print(f"Python相关文章: {len(python_articles)}篇")

# TODO: 按浏览量排序
views_sorted = sorted(articles, key=lambda a: a['views'], reverse=True)
print("\n按浏览量排序:")
for article in views_sorted:
    print(f"  {article['title']}: {article['views']}次浏览")

# TODO: 计算平均浏览量
avg_views = functools.reduce(lambda acc, a: acc + a['views'], articles, 0) / len(articles)
print(f"\n平均浏览量: {avg_views:.0f}次")

# TODO: 提取所有标签并去重
all_tags = functools.reduce(lambda acc, article: acc + article['tags'], articles, [])
unique_tags = list(set(all_tags))
print(f"所有标签: {unique_tags}")

# 练习4.3：时间数据处理
print("\n4.3 时间数据处理")

# 任务数据
tasks = [
    {'name': '项目规划', 'start': '2023-12-01', 'duration': 5, 'priority': 'high'},
    {'name': '需求分析', 'start': '2023-12-06', 'duration': 3, 'priority': 'high'},
    {'name': '系统设计', 'start': '2023-12-09', 'duration': 7, 'priority': 'medium'},
    {'name': '编码实现', 'start': '2023-12-16', 'duration': 14, 'priority': 'high'},
    {'name': '测试验证', 'start': '2023-12-30', 'duration': 5, 'priority': 'medium'}
]

# TODO: 计算每个任务的结束日期
tasks_with_end = list(map(
    lambda task: {
        **task,
        'end': (datetime.strptime(task['start'], '%Y-%m-%d') + 
               timedelta(days=task['duration'])).strftime('%Y-%m-%d')
    },
    tasks
))

print("任务时间安排:")
for task in tasks_with_end:
    print(f"  {task['name']}: {task['start']} ~ {task['end']} ({task['duration']}天)")

# TODO: 筛选高优先级任务
high_priority = list(filter(lambda task: task['priority'] == 'high', tasks))
print(f"\n高优先级任务: {[task['name'] for task in high_priority]}")

# TODO: 计算项目总工期
total_duration = functools.reduce(lambda acc, task: acc + task['duration'], tasks, 0)
print(f"项目总工期: {total_duration}天")
print()

# ==================== 练习5：高级应用练习 ====================
print("练习5：高级应用练习")
print("=" * 50)

# 练习5.1：函数组合
print("5.1 函数组合")

# TODO: 创建数据处理管道
def create_pipeline(*functions):
    """创建函数管道"""
    return lambda data: functools.reduce(lambda result, func: func(result), functions, data)

# 数据清洗管道
data_cleaning_pipeline = create_pipeline(
    lambda data: [item.strip() for item in data],  # 去除空白
    lambda data: [item.lower() for item in data],  # 转小写
    lambda data: [item for item in data if item],  # 去除空字符串
    lambda data: list(set(data)),  # 去重
    lambda data: sorted(data)  # 排序
)

raw_data = ['  Apple  ', 'BANANA', '', 'cherry', 'Apple', '  ', 'BANANA']
cleaned_data = data_cleaning_pipeline(raw_data)
print(f"原始数据: {raw_data}")
print(f"清洗结果: {cleaned_data}")

# 练习5.2：动态函数生成
print("\n5.2 动态函数生成")

# TODO: 创建验证器工厂
def create_validator(rules):
    """创建验证器"""
    def validator(data):
        results = {}
        for field, value in data.items():
            if field in rules:
                results[field] = all(rule(value) for rule in rules[field])
            else:
                results[field] = True
        return results
    return validator

# 定义验证规则
user_validation_rules = {
    'username': [
        lambda x: len(x) >= 3,
        lambda x: len(x) <= 20,
        lambda x: x.isalnum()
    ],
    'email': [
        lambda x: '@' in x,
        lambda x: '.' in x.split('@')[1]
    ],
    'age': [
        lambda x: x.isdigit(),
        lambda x: 0 <= int(x) <= 120
    ]
}

user_validator = create_validator(user_validation_rules)

# 测试数据
test_users = [
    {'username': 'john123', 'email': 'john@example.com', 'age': '25'},
    {'username': 'ab', 'email': 'invalid-email', 'age': '150'},
    {'username': 'alice_doe', 'email': 'alice@test.org', 'age': '30'}
]

print("用户数据验证:")
for i, user in enumerate(test_users, 1):
    validation_result = user_validator(user)
    print(f"用户{i}: {validation_result}")

# 练习5.3：事件处理系统
print("\n5.3 事件处理系统")

# TODO: 创建简单的事件系统
class EventEmitter:
    def __init__(self):
        self.events = {}
    
    def on(self, event, callback):
        if event not in self.events:
            self.events[event] = []
        self.events[event].append(callback)
    
    def emit(self, event, *args, **kwargs):
        if event in self.events:
            for callback in self.events[event]:
                callback(*args, **kwargs)

# 创建事件发射器
emitter = EventEmitter()

# 注册事件处理器
emitter.on('user_action', lambda action, user: print(f"用户 {user} 执行了 {action}"))
emitter.on('user_action', lambda action, user: print(f"记录日志: {action} by {user}"))
emitter.on('system_error', lambda error: print(f"系统错误: {error}"))

# 触发事件
print("事件处理示例:")
emitter.emit('user_action', '登录', 'Alice')
emitter.emit('user_action', '下单', 'Bob')
emitter.emit('system_error', '数据库连接失败')

# 练习5.4：数据转换和聚合
print("\n5.4 数据转换和聚合")

# 复杂的销售数据
sales_records = [
    {'date': '2023-12-01', 'product': 'iPhone', 'category': 'Electronics', 'amount': 999, 'quantity': 2},
    {'date': '2023-12-01', 'product': 'iPad', 'category': 'Electronics', 'amount': 599, 'quantity': 1},
    {'date': '2023-12-02', 'product': 'Book', 'category': 'Education', 'amount': 29, 'quantity': 5},
    {'date': '2023-12-02', 'product': 'iPhone', 'category': 'Electronics', 'amount': 999, 'quantity': 1},
    {'date': '2023-12-03', 'product': 'Laptop', 'category': 'Electronics', 'amount': 1299, 'quantity': 1}
]

# TODO: 按类别聚合销售额
category_sales = {}
for record in sales_records:
    category = record['category']
    total = record['amount'] * record['quantity']
    category_sales[category] = category_sales.get(category, 0) + total

print("按类别销售额:")
for category, total in category_sales.items():
    print(f"  {category}: ${total}")

# TODO: 找出每日销售冠军产品
daily_champions = {}
for record in sales_records:
    date = record['date']
    product = record['product']
    total = record['amount'] * record['quantity']
    
    if date not in daily_champions or total > daily_champions[date]['total']:
        daily_champions[date] = {'product': product, 'total': total}

print("\n每日销售冠军:")
for date, champion in daily_champions.items():
    print(f"  {date}: {champion['product']} (${champion['total']})")

# TODO: 使用Lambda进行复杂数据转换
transformed_data = list(map(
    lambda record: {
        'id': f"{record['date']}-{record['product']}",
        'revenue': record['amount'] * record['quantity'],
        'profit_margin': 0.3 if record['category'] == 'Electronics' else 0.5,
        'profit': (record['amount'] * record['quantity']) * (0.3 if record['category'] == 'Electronics' else 0.5)
    },
    sales_records
))

print("\n转换后的数据:")
for data in transformed_data[:3]:  # 只显示前3条
    print(f"  {data['id']}: 收入${data['revenue']}, 利润${data['profit']:.0f}")

# TODO: 计算总利润
total_profit = functools.reduce(lambda acc, data: acc + data['profit'], transformed_data, 0)
print(f"\n总利润: ${total_profit:.0f}")
print()

# ==================== 练习6：挑战题 ====================
print("练习6：挑战题")
print("=" * 50)

# 挑战6.1：实现简单的查询语言
print("6.1 简单查询语言")

# TODO: 创建查询构建器
class QueryBuilder:
    def __init__(self, data):
        self.data = data
        self.result = data
    
    def where(self, condition):
        self.result = list(filter(condition, self.result))
        return self
    
    def select(self, selector):
        self.result = list(map(selector, self.result))
        return self
    
    def order_by(self, key_func, reverse=False):
        self.result = sorted(self.result, key=key_func, reverse=reverse)
        return self
    
    def limit(self, n):
        self.result = self.result[:n]
        return self
    
    def execute(self):
        return self.result

# 员工数据
employees = [
    {'name': '张三', 'department': 'IT', 'salary': 8000, 'age': 25, 'experience': 3},
    {'name': '李四', 'department': 'HR', 'salary': 7000, 'age': 30, 'experience': 5},
    {'name': '王五', 'department': 'IT', 'salary': 9000, 'age': 28, 'experience': 4},
    {'name': '赵六', 'department': 'Finance', 'salary': 8500, 'age': 32, 'experience': 7},
    {'name': '钱七', 'department': 'IT', 'salary': 7500, 'age': 26, 'experience': 2},
    {'name': '孙八', 'department': 'HR', 'salary': 7200, 'age': 29, 'experience': 4}
]

# 查询示例：IT部门薪资大于8000的员工，按薪资降序排列
it_high_salary = (QueryBuilder(employees)
                 .where(lambda emp: emp['department'] == 'IT')
                 .where(lambda emp: emp['salary'] > 8000)
                 .order_by(lambda emp: emp['salary'], reverse=True)
                 .select(lambda emp: {'name': emp['name'], 'salary': emp['salary']})
                 .execute())

print("IT部门高薪员工:")
for emp in it_high_salary:
    print(f"  {emp['name']}: ${emp['salary']}")

# 挑战6.2：函数式编程工具集
print("\n6.2 函数式编程工具集")

# TODO: 实现函数式编程常用工具
class FP:
    @staticmethod
    def compose(*functions):
        """函数组合"""
        return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)
    
    @staticmethod
    def pipe(data, *functions):
        """管道操作"""
        return functools.reduce(lambda result, func: func(result), functions, data)
    
    @staticmethod
    def curry(func):
        """柯里化"""
        def curried(*args, **kwargs):
            if len(args) + len(kwargs) >= func.__code__.co_argcount:
                return func(*args, **kwargs)
            return lambda *more_args, **more_kwargs: curried(*(args + more_args), **{**kwargs, **more_kwargs})
        return curried
    
    @staticmethod
    def memoize(func):
        """记忆化"""
        cache = {}
        return lambda *args: cache.setdefault(args, func(*args))

# 使用函数式工具
print("函数式编程工具演示:")

# 组合函数
process_number = FP.compose(
    lambda x: x * 2,
    lambda x: x + 10,
    lambda x: x ** 2
)
print(f"组合函数 process_number(3) = {process_number(3)}")

# 管道操作
result = FP.pipe(
    [1, 2, 3, 4, 5],
    lambda lst: list(map(lambda x: x * 2, lst)),
    lambda lst: list(filter(lambda x: x > 5, lst)),
    lambda lst: sum(lst)
)
print(f"管道操作结果: {result}")

# 柯里化
add_three = FP.curry(lambda x, y, z: x + y + z)
print(f"柯里化 add_three(1)(2)(3) = {add_three(1)(2)(3)}")

# 记忆化
fib = FP.memoize(lambda n: n if n <= 1 else fib(n-1) + fib(n-2))
print(f"记忆化斐波那契 fib(10) = {fib(10)}")

# 挑战6.3：创建DSL（领域特定语言）
print("\n6.3 创建简单DSL")

# TODO: 创建数据验证DSL
class Validator:
    def __init__(self, value):
        self.value = value
        self.errors = []
    
    def required(self, message="字段是必需的"):
        if not self.value:
            self.errors.append(message)
        return self
    
    def min_length(self, length, message=None):
        if message is None:
            message = f"长度至少为{length}"
        if len(str(self.value)) < length:
            self.errors.append(message)
        return self
    
    def max_length(self, length, message=None):
        if message is None:
            message = f"长度不能超过{length}"
        if len(str(self.value)) > length:
            self.errors.append(message)
        return self
    
    def pattern(self, regex_pattern, message="格式不正确"):
        import re
        if not re.match(regex_pattern, str(self.value)):
            self.errors.append(message)
        return self
    
    def custom(self, validator_func, message="验证失败"):
        if not validator_func(self.value):
            self.errors.append(message)
        return self
    
    def is_valid(self):
        return len(self.errors) == 0
    
    def get_errors(self):
        return self.errors

# 使用验证DSL
print("数据验证DSL演示:")

# 验证用户名
username_validator = (Validator("ab")
                     .required()
                     .min_length(3, "用户名至少3个字符")
                     .max_length(20, "用户名不能超过20个字符")
                     .custom(lambda x: x.isalnum(), "用户名只能包含字母和数字"))

print(f"用户名验证: {'通过' if username_validator.is_valid() else '失败'}")
if not username_validator.is_valid():
    print(f"错误: {username_validator.get_errors()}")

# 验证邮箱
email_validator = (Validator("user@example.com")
                  .required()
                  .pattern(r'^[\w\.-]+@[\w\.-]+\.\w+$', "邮箱格式不正确"))

print(f"邮箱验证: {'通过' if email_validator.is_valid() else '失败'}")
print()

# ==================== 总结 ====================
print("=== 练习总结 ===")
print("恭喜完成Lambda表达式综合练习！")
print()
print("通过这些练习，你应该掌握了：")
print("✓ Lambda表达式的基本语法")
print("✓ 与map、filter、reduce、sorted等内置函数的结合使用")
print("✓ 数据处理和转换技巧")
print("✓ 函数式编程概念")
print("✓ 高级应用场景")
print("✓ 实际项目中的应用")
print()
print("继续练习建议：")
print("• 尝试在实际项目中使用Lambda表达式")
print("• 学习更多函数式编程概念")
print("• 探索其他高阶函数的使用")
print("• 关注代码的可读性和性能")
print("• 结合其他Python特性使用Lambda")

if __name__ == "__main__":
    print("\n=== Lambda表达式学习完成 ===")
    print("Lambda表达式是Python中强大而优雅的特性")
    print("合理使用可以让代码更简洁、更具表达力")
    print("记住：简洁性和可读性之间要找到平衡！")