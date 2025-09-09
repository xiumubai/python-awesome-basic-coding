# Lambda表达式与排序函数

Lambda表达式在排序操作中扮演着重要角色，特别是作为`key`函数来定义排序规则。本节将详细介绍Lambda表达式与各种排序函数的结合使用。

## 排序函数基础

### sorted()函数基础

```python
# sorted()函数的基本用法

# 1. 基本排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(f"原列表: {numbers}")
print(f"排序后: {sorted_numbers}")

# 2. 逆序排序
reverse_sorted = sorted(numbers, reverse=True)
print(f"逆序排序: {reverse_sorted}")

# 3. 字符串排序
words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words)
print(f"字符串排序: {sorted_words}")

# 4. 原地排序 vs 返回新列表
original_list = [3, 1, 4, 1, 5]
print(f"原始列表: {original_list}")

# sorted()返回新列表，不修改原列表
new_sorted = sorted(original_list)
print(f"sorted()后原列表: {original_list}")
print(f"新排序列表: {new_sorted}")

# list.sort()原地排序，修改原列表
original_list.sort()
print(f"sort()后原列表: {original_list}")
```

### key参数的作用

```python
# key参数的重要性

# 1. 按绝对值排序
numbers = [-5, -1, 3, -2, 4]

# 默认排序
default_sort = sorted(numbers)
print(f"默认排序: {default_sort}")

# 按绝对值排序
abs_sort = sorted(numbers, key=abs)
print(f"按绝对值排序: {abs_sort}")

# 使用lambda实现相同效果
lambda_abs_sort = sorted(numbers, key=lambda x: abs(x))
print(f"Lambda绝对值排序: {lambda_abs_sort}")

# 2. 字符串长度排序
words = ['python', 'java', 'c', 'javascript', 'go']

# 按长度排序
length_sort = sorted(words, key=len)
print(f"按长度排序: {length_sort}")

# 使用lambda实现
lambda_length_sort = sorted(words, key=lambda word: len(word))
print(f"Lambda长度排序: {lambda_length_sort}")

# 3. 复合排序条件
# 先按长度排序，长度相同则按字母顺序
complex_sort = sorted(words, key=lambda word: (len(word), word))
print(f"复合排序: {complex_sort}")
```

## Lambda作为key函数

### 数值排序的高级用法

```python
# 数值排序的各种Lambda应用

# 1. 按数字的某个特征排序
numbers = [123, 456, 789, 12, 34, 567]

# 按个位数排序
ones_digit_sort = sorted(numbers, key=lambda x: x % 10)
print(f"按个位数排序: {ones_digit_sort}")

# 按十位数排序
tens_digit_sort = sorted(numbers, key=lambda x: (x // 10) % 10)
print(f"按十位数排序: {tens_digit_sort}")

# 按数字位数排序
digit_count_sort = sorted(numbers, key=lambda x: len(str(x)))
print(f"按位数排序: {digit_count_sort}")

# 按数字各位数字之和排序
digit_sum_sort = sorted(numbers, key=lambda x: sum(int(digit) for digit in str(x)))
print(f"按各位数字和排序: {digit_sum_sort}")

# 2. 浮点数的特殊排序
float_numbers = [3.14, 2.71, 1.41, 1.73, 0.57]

# 按小数部分排序
fractional_sort = sorted(float_numbers, key=lambda x: x - int(x))
print(f"按小数部分排序: {fractional_sort}")

# 按与某个值的距离排序
target = 2.0
distance_sort = sorted(float_numbers, key=lambda x: abs(x - target))
print(f"按与{target}的距离排序: {distance_sort}")

# 3. 复数排序
complex_numbers = [3+4j, 1+2j, 2+1j, 4+3j, 1+1j]

# 按模长排序
modulus_sort = sorted(complex_numbers, key=lambda x: abs(x))
print(f"按模长排序: {modulus_sort}")

# 按实部排序
real_sort = sorted(complex_numbers, key=lambda x: x.real)
print(f"按实部排序: {real_sort}")

# 按虚部排序
imag_sort = sorted(complex_numbers, key=lambda x: x.imag)
print(f"按虚部排序: {imag_sort}")
```

### 字符串排序的高级技巧

```python
# 字符串排序的Lambda应用

# 1. 忽略大小写排序
words = ['Apple', 'banana', 'Cherry', 'date', 'Elderberry']

# 默认排序（区分大小写）
default_sort = sorted(words)
print(f"默认排序: {default_sort}")

# 忽略大小写排序
case_insensitive = sorted(words, key=lambda x: x.lower())
print(f"忽略大小写: {case_insensitive}")

# 2. 按字符串的特定部分排序
filenames = ['file1.txt', 'file10.txt', 'file2.txt', 'file20.txt']

# 按文件名中的数字排序
import re
numeric_sort = sorted(filenames, key=lambda x: int(re.search(r'\d+', x).group()))
print(f"按数字排序: {numeric_sort}")

# 3. 按字符串中特定字符的出现次数排序
sentences = [
    "Hello world",
    "Python programming",
    "Lambda expressions",
    "Sorting algorithms"
]

# 按元音字母数量排序
vowel_count_sort = sorted(sentences, key=lambda x: sum(1 for char in x.lower() if char in 'aeiou'))
print(f"按元音数量排序: {vowel_count_sort}")

# 按空格数量排序
space_count_sort = sorted(sentences, key=lambda x: x.count(' '))
print(f"按空格数量排序: {space_count_sort}")

# 4. 自定义字符串排序规则
# 按字符串的"重要性"排序（自定义权重）
def string_importance(s):
    """计算字符串的重要性分数"""
    score = 0
    score += len(s) * 0.1  # 长度权重
    score += s.count('a') * 2  # 'a'字符权重
    score += s.count('e') * 1.5  # 'e'字符权重
    return score

importance_sort = sorted(sentences, key=lambda x: string_importance(x), reverse=True)
print(f"按重要性排序: {importance_sort}")

# 使用lambda直接实现
lambda_importance = sorted(sentences, 
                          key=lambda x: len(x) * 0.1 + x.count('a') * 2 + x.count('e') * 1.5, 
                          reverse=True)
print(f"Lambda重要性排序: {lambda_importance}")
```

## 复杂数据结构排序

### 字典排序

```python
# 字典数据的排序

# 1. 学生信息排序
students = [
    {'name': 'Alice', 'age': 20, 'grade': 85, 'city': 'New York'},
    {'name': 'Bob', 'age': 19, 'grade': 92, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 21, 'grade': 78, 'city': 'Chicago'},
    {'name': 'Diana', 'age': 20, 'grade': 95, 'city': 'New York'},
    {'name': 'Eve', 'age': 22, 'grade': 88, 'city': 'Boston'}
]

# 按姓名排序
name_sort = sorted(students, key=lambda x: x['name'])
print("按姓名排序:")
for student in name_sort:
    print(f"  {student['name']}: {student['grade']}")

# 按年龄排序
age_sort = sorted(students, key=lambda x: x['age'])
print("\n按年龄排序:")
for student in age_sort:
    print(f"  {student['name']} ({student['age']}岁): {student['grade']}")

# 按成绩排序（降序）
grade_sort = sorted(students, key=lambda x: x['grade'], reverse=True)
print("\n按成绩排序（降序）:")
for student in grade_sort:
    print(f"  {student['name']}: {student['grade']}")

# 2. 多级排序
# 先按城市排序，再按成绩排序
multi_sort = sorted(students, key=lambda x: (x['city'], -x['grade']))
print("\n按城市和成绩排序:")
for student in multi_sort:
    print(f"  {student['city']} - {student['name']}: {student['grade']}")

# 先按年龄排序，年龄相同则按成绩降序排序
age_grade_sort = sorted(students, key=lambda x: (x['age'], -x['grade']))
print("\n按年龄和成绩排序:")
for student in age_grade_sort:
    print(f"  {student['name']} ({student['age']}岁): {student['grade']}")

# 3. 复杂计算排序
# 按综合评分排序（年龄越小越好，成绩越高越好）
comprehensive_sort = sorted(students, 
                           key=lambda x: x['grade'] - x['age'] * 2,  # 成绩减去年龄的两倍
                           reverse=True)
print("\n按综合评分排序:")
for student in comprehensive_sort:
    score = student['grade'] - student['age'] * 2
    print(f"  {student['name']}: 综合分 {score}")
```

### 嵌套数据结构排序

```python
# 嵌套数据结构的排序

# 1. 嵌套列表排序
matrix = [
    [3, 1, 4],
    [1, 5, 9],
    [2, 6, 5],
    [3, 5, 8]
]

# 按第一个元素排序
first_element_sort = sorted(matrix, key=lambda row: row[0])
print("按第一个元素排序:")
for row in first_element_sort:
    print(f"  {row}")

# 按行的和排序
sum_sort = sorted(matrix, key=lambda row: sum(row))
print("\n按行和排序:")
for row in sum_sort:
    print(f"  {row} (和: {sum(row)})")

# 按最大值排序
max_sort = sorted(matrix, key=lambda row: max(row))
print("\n按最大值排序:")
for row in max_sort:
    print(f"  {row} (最大值: {max(row)})")

# 2. 复杂嵌套结构
companies = [
    {
        'name': 'TechCorp',
        'employees': [
            {'name': 'Alice', 'salary': 70000},
            {'name': 'Bob', 'salary': 80000}
        ],
        'founded': 2010
    },
    {
        'name': 'InnovateLtd',
        'employees': [
            {'name': 'Charlie', 'salary': 75000},
            {'name': 'Diana', 'salary': 85000},
            {'name': 'Eve', 'salary': 90000}
        ],
        'founded': 2015
    },
    {
        'name': 'StartupInc',
        'employees': [
            {'name': 'Frank', 'salary': 60000}
        ],
        'founded': 2020
    }
]

# 按员工数量排序
employee_count_sort = sorted(companies, key=lambda x: len(x['employees']))
print("\n按员工数量排序:")
for company in employee_count_sort:
    print(f"  {company['name']}: {len(company['employees'])}名员工")

# 按平均薪资排序
avg_salary_sort = sorted(companies, 
                        key=lambda x: sum(emp['salary'] for emp in x['employees']) / len(x['employees']),
                        reverse=True)
print("\n按平均薪资排序:")
for company in avg_salary_sort:
    avg_salary = sum(emp['salary'] for emp in company['employees']) / len(company['employees'])
    print(f"  {company['name']}: 平均薪资 ${avg_salary:,.0f}")

# 按成立年份和最高薪资排序
complex_sort = sorted(companies, 
                     key=lambda x: (x['founded'], -max(emp['salary'] for emp in x['employees'])))
print("\n按成立年份和最高薪资排序:")
for company in complex_sort:
    max_salary = max(emp['salary'] for emp in company['employees'])
    print(f"  {company['name']} ({company['founded']}): 最高薪资 ${max_salary:,}")
```

## 元组和列表排序

### 元组排序的特殊性

```python
# 元组排序的特点和应用

# 1. 元组的自然排序
tuples = [(3, 'apple'), (1, 'banana'), (2, 'cherry'), (1, 'date')]

# 默认按第一个元素排序，相同则按第二个元素排序
default_sort = sorted(tuples)
print(f"默认元组排序: {default_sort}")

# 2. 自定义元组排序
# 按第二个元素排序
second_element_sort = sorted(tuples, key=lambda x: x[1])
print(f"按第二个元素排序: {second_element_sort}")

# 按元组长度排序（如果元组长度不同）
variable_tuples = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
length_sort = sorted(variable_tuples, key=lambda x: len(x))
print(f"按元组长度排序: {length_sort}")

# 3. 坐标点排序
points = [(3, 4), (1, 2), (5, 1), (2, 3), (4, 2)]

# 按到原点的距离排序
distance_sort = sorted(points, key=lambda p: (p[0]**2 + p[1]**2)**0.5)
print(f"按距离原点排序: {distance_sort}")

# 按x坐标排序
x_sort = sorted(points, key=lambda p: p[0])
print(f"按x坐标排序: {x_sort}")

# 按y坐标排序
y_sort = sorted(points, key=lambda p: p[1])
print(f"按y坐标排序: {y_sort}")

# 按象限排序
def get_quadrant(point):
    x, y = point
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

quadrant_points = [(3, 4), (-1, 2), (-5, -1), (2, -3), (4, 2)]
quadrant_sort = sorted(quadrant_points, key=lambda p: get_quadrant(p))
print(f"按象限排序: {quadrant_sort}")

# 使用lambda直接实现象限排序
lambda_quadrant_sort = sorted(quadrant_points, 
                             key=lambda p: (1 if p[0] > 0 and p[1] > 0 else
                                           2 if p[0] < 0 and p[1] > 0 else
                                           3 if p[0] < 0 and p[1] < 0 else 4))
print(f"Lambda象限排序: {lambda_quadrant_sort}")
```

### 多维列表排序

```python
# 多维列表的排序技巧

# 1. 成绩表排序
grades = [
    ['Alice', 85, 92, 78],
    ['Bob', 76, 85, 90],
    ['Charlie', 95, 87, 92],
    ['Diana', 68, 75, 82]
]

# 按姓名排序
name_sort = sorted(grades, key=lambda x: x[0])
print("按姓名排序:")
for grade in name_sort:
    print(f"  {grade}")

# 按总分排序
total_sort = sorted(grades, key=lambda x: sum(x[1:]), reverse=True)
print("\n按总分排序:")
for grade in total_sort:
    total = sum(grade[1:])
    print(f"  {grade[0]}: {total}")

# 按平均分排序
average_sort = sorted(grades, key=lambda x: sum(x[1:]) / len(x[1:]), reverse=True)
print("\n按平均分排序:")
for grade in average_sort:
    average = sum(grade[1:]) / len(grade[1:])
    print(f"  {grade[0]}: {average:.2f}")

# 按第一科成绩排序
first_subject_sort = sorted(grades, key=lambda x: x[1], reverse=True)
print("\n按第一科成绩排序:")
for grade in first_subject_sort:
    print(f"  {grade[0]}: {grade[1]}")

# 2. 矩阵行排序
matrix = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1],
    [1, 3, 5]
]

# 按行的方差排序
def variance(row):
    mean = sum(row) / len(row)
    return sum((x - mean) ** 2 for x in row) / len(row)

variance_sort = sorted(matrix, key=lambda row: variance(row))
print("\n按方差排序:")
for row in variance_sort:
    var = variance(row)
    print(f"  {row} (方差: {var:.2f})")

# 按行的中位数排序
def median(row):
    sorted_row = sorted(row)
    n = len(sorted_row)
    if n % 2 == 0:
        return (sorted_row[n//2-1] + sorted_row[n//2]) / 2
    else:
        return sorted_row[n//2]

median_sort = sorted(matrix, key=lambda row: median(row))
print("\n按中位数排序:")
for row in median_sort:
    med = median(row)
    print(f"  {row} (中位数: {med})")
```

## 日期和时间排序

### 日期字符串排序

```python
# 日期和时间的排序处理

from datetime import datetime, date
import time

# 1. 日期字符串排序
date_strings = [
    '2024-03-15',
    '2024-01-20',
    '2024-12-05',
    '2024-06-30',
    '2024-09-12'
]

# 字符串形式的日期可以直接排序（ISO格式）
string_date_sort = sorted(date_strings)
print(f"字符串日期排序: {string_date_sort}")

# 转换为日期对象后排序
date_object_sort = sorted(date_strings, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))
print(f"日期对象排序: {date_object_sort}")

# 2. 不同格式的日期字符串
mixed_date_formats = [
    '15/03/2024',
    '2024-01-20',
    'March 15, 2024',
    '06/30/2024',
    '2024.09.12'
]

def parse_date(date_str):
    """解析不同格式的日期字符串"""
    formats = [
        '%d/%m/%Y',
        '%Y-%m-%d',
        '%B %d, %Y',
        '%m/%d/%Y',
        '%Y.%m.%d'
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"无法解析日期: {date_str}")

mixed_date_sort = sorted(mixed_date_formats, key=lambda x: parse_date(x))
print(f"\n混合格式日期排序: {mixed_date_sort}")

# 3. 时间戳排序
timestamps = [1640995200, 1609459200, 1672531200, 1656633600, 1688169600]

# 按时间戳排序
timestamp_sort = sorted(timestamps)
print(f"\n时间戳排序: {timestamp_sort}")

# 转换为可读日期显示
readable_dates = [(ts, datetime.fromtimestamp(ts).strftime('%Y-%m-%d')) for ts in timestamp_sort]
print("可读日期:")
for ts, date_str in readable_dates:
    print(f"  {ts} -> {date_str}")
```

### 复杂时间数据排序

```python
# 复杂时间数据的排序

# 1. 事件数据排序
events = [
    {'name': '会议A', 'start': '2024-03-15 09:00', 'duration': 120},
    {'name': '会议B', 'start': '2024-03-15 14:30', 'duration': 90},
    {'name': '会议C', 'start': '2024-03-15 09:00', 'duration': 60},
    {'name': '培训', 'start': '2024-03-16 10:00', 'duration': 180},
    {'name': '讨论', 'start': '2024-03-15 16:00', 'duration': 45}
]

# 按开始时间排序
start_time_sort = sorted(events, key=lambda x: datetime.strptime(x['start'], '%Y-%m-%d %H:%M'))
print("按开始时间排序:")
for event in start_time_sort:
    print(f"  {event['name']}: {event['start']}")

# 按持续时间排序
duration_sort = sorted(events, key=lambda x: x['duration'], reverse=True)
print("\n按持续时间排序:")
for event in duration_sort:
    print(f"  {event['name']}: {event['duration']}分钟")

# 按结束时间排序
def get_end_time(event):
    start = datetime.strptime(event['start'], '%Y-%m-%d %H:%M')
    end = start + timedelta(minutes=event['duration'])
    return end

from datetime import timedelta
end_time_sort = sorted(events, key=lambda x: get_end_time(x))
print("\n按结束时间排序:")
for event in end_time_sort:
    end_time = get_end_time(event)
    print(f"  {event['name']}: 结束于 {end_time.strftime('%Y-%m-%d %H:%M')}")

# 2. 日志数据排序
logs = [
    {'timestamp': '2024-03-15 10:30:45', 'level': 'ERROR', 'message': '数据库连接失败'},
    {'timestamp': '2024-03-15 10:30:42', 'level': 'INFO', 'message': '用户登录'},
    {'timestamp': '2024-03-15 10:30:47', 'level': 'WARNING', 'message': '内存使用率高'},
    {'timestamp': '2024-03-15 10:30:40', 'level': 'DEBUG', 'message': '调试信息'},
    {'timestamp': '2024-03-15 10:30:46', 'level': 'ERROR', 'message': '文件读取失败'}
]

# 按时间戳排序
time_sort = sorted(logs, key=lambda x: datetime.strptime(x['timestamp'], '%Y-%m-%d %H:%M:%S'))
print("\n按时间排序的日志:")
for log in time_sort:
    print(f"  {log['timestamp']} [{log['level']}] {log['message']}")

# 按日志级别重要性排序
level_priority = {'DEBUG': 1, 'INFO': 2, 'WARNING': 3, 'ERROR': 4}
level_sort = sorted(logs, key=lambda x: level_priority[x['level']], reverse=True)
print("\n按重要性排序的日志:")
for log in level_sort:
    print(f"  [{log['level']}] {log['message']}")

# 综合排序：先按级别，再按时间
complex_log_sort = sorted(logs, 
                         key=lambda x: (level_priority[x['level']], 
                                       datetime.strptime(x['timestamp'], '%Y-%m-%d %H:%M:%S')),
                         reverse=True)
print("\n按级别和时间综合排序:")
for log in complex_log_sort:
    print(f"  {log['timestamp']} [{log['level']}] {log['message']}")
```

## 自定义排序规则

### 业务逻辑排序

```python
# 基于业务逻辑的自定义排序

# 1. 优先级排序
tasks = [
    {'name': '修复bug', 'priority': 'high', 'estimated_hours': 4},
    {'name': '写文档', 'priority': 'low', 'estimated_hours': 2},
    {'name': '代码审查', 'priority': 'medium', 'estimated_hours': 1},
    {'name': '部署上线', 'priority': 'high', 'estimated_hours': 3},
    {'name': '测试功能', 'priority': 'medium', 'estimated_hours': 5}
]

# 定义优先级权重
priority_weight = {'high': 3, 'medium': 2, 'low': 1}

# 按优先级排序
priority_sort = sorted(tasks, key=lambda x: priority_weight[x['priority']], reverse=True)
print("按优先级排序:")
for task in priority_sort:
    print(f"  [{task['priority'].upper()}] {task['name']} ({task['estimated_hours']}h)")

# 按优先级和工作量综合排序（优先级高且工作量小的优先）
complex_priority_sort = sorted(tasks, 
                              key=lambda x: (priority_weight[x['priority']], -x['estimated_hours']),
                              reverse=True)
print("\n按优先级和工作量排序:")
for task in complex_priority_sort:
    print(f"  [{task['priority'].upper()}] {task['name']} ({task['estimated_hours']}h)")

# 2. 状态排序
orders = [
    {'id': 1001, 'status': 'shipped', 'amount': 150.00},
    {'id': 1002, 'status': 'pending', 'amount': 200.00},
    {'id': 1003, 'status': 'delivered', 'amount': 75.00},
    {'id': 1004, 'status': 'cancelled', 'amount': 300.00},
    {'id': 1005, 'status': 'processing', 'amount': 120.00}
]

# 定义状态优先级
status_priority = {
    'pending': 1,
    'processing': 2,
    'shipped': 3,
    'delivered': 4,
    'cancelled': 5
}

# 按状态优先级排序
status_sort = sorted(orders, key=lambda x: status_priority[x['status']])
print("\n按状态排序:")
for order in status_sort:
    print(f"  订单{order['id']}: {order['status']} - ${order['amount']}")

# 3. 地理位置排序
cities = [
    {'name': '北京', 'lat': 39.9042, 'lon': 116.4074},
    {'name': '上海', 'lat': 31.2304, 'lon': 121.4737},
    {'name': '广州', 'lat': 23.1291, 'lon': 113.2644},
    {'name': '深圳', 'lat': 22.5431, 'lon': 114.0579},
    {'name': '杭州', 'lat': 30.2741, 'lon': 120.1551}
]

# 参考点（比如用户当前位置）
user_location = {'lat': 30.0000, 'lon': 120.0000}  # 假设在杭州附近

# 计算距离的简化公式（实际应用中应使用更精确的地理距离计算）
def calculate_distance(city, reference):
    lat_diff = city['lat'] - reference['lat']
    lon_diff = city['lon'] - reference['lon']
    return (lat_diff ** 2 + lon_diff ** 2) ** 0.5

# 按距离排序
distance_sort = sorted(cities, key=lambda x: calculate_distance(x, user_location))
print("\n按距离排序:")
for city in distance_sort:
    distance = calculate_distance(city, user_location)
    print(f"  {city['name']}: 距离 {distance:.2f}")
```

### 多条件复合排序

```python
# 多条件复合排序的高级应用

# 1. 员工绩效排序
employees = [
    {'name': 'Alice', 'department': 'Engineering', 'salary': 80000, 'performance': 4.5, 'years': 3},
    {'name': 'Bob', 'department': 'Sales', 'salary': 70000, 'performance': 4.2, 'years': 5},
    {'name': 'Charlie', 'department': 'Engineering', 'salary': 90000, 'performance': 4.8, 'years': 2},
    {'name': 'Diana', 'department': 'Marketing', 'salary': 65000, 'performance': 4.0, 'years': 4},
    {'name': 'Eve', 'department': 'Engineering', 'salary': 85000, 'performance': 4.6, 'years': 6}
]

# 部门优先级
dept_priority = {'Engineering': 1, 'Sales': 2, 'Marketing': 3}

# 复合排序：部门 -> 绩效 -> 工作年限
complex_sort = sorted(employees, 
                     key=lambda x: (dept_priority[x['department']], 
                                   -x['performance'],  # 绩效降序
                                   -x['years']),       # 年限降序
                     )
print("复合排序结果:")
for emp in complex_sort:
    print(f"  {emp['name']} ({emp['department']}): 绩效{emp['performance']}, {emp['years']}年")

# 2. 加权评分排序
def calculate_score(employee):
    """计算员工综合评分"""
    # 绩效权重40%，薪资权重30%，经验权重30%
    performance_score = employee['performance'] * 0.4
    salary_score = (employee['salary'] / 100000) * 0.3  # 标准化薪资
    experience_score = min(employee['years'] / 10, 1) * 0.3  # 经验最高10年
    return performance_score + salary_score + experience_score

score_sort = sorted(employees, key=lambda x: calculate_score(x), reverse=True)
print("\n按综合评分排序:")
for emp in score_sort:
    score = calculate_score(emp)
    print(f"  {emp['name']}: 综合评分 {score:.2f}")

# 3. 条件分组排序
# 先按部门分组，每个部门内按绩效排序
dept_performance_sort = sorted(employees, 
                              key=lambda x: (x['department'], -x['performance']))
print("\n按部门分组，部门内按绩效排序:")
current_dept = None
for emp in dept_performance_sort:
    if emp['department'] != current_dept:
        current_dept = emp['department']
        print(f"\n{current_dept}部门:")
    print(f"  {emp['name']}: 绩效{emp['performance']}")
```

## 稳定排序和多级排序

### 稳定排序的重要性

```python
# 稳定排序的演示和应用

# 1. 稳定排序的概念
students = [
    {'name': 'Alice', 'grade': 85, 'id': 1},
    {'name': 'Bob', 'grade': 90, 'id': 2},
    {'name': 'Charlie', 'grade': 85, 'id': 3},
    {'name': 'Diana', 'grade': 90, 'id': 4},
    {'name': 'Eve', 'grade': 85, 'id': 5}
]

print("原始顺序:")
for student in students:
    print(f"  {student['name']} (ID: {student['id']}, 成绩: {student['grade']})")

# Python的sorted()是稳定排序
grade_sort = sorted(students, key=lambda x: x['grade'], reverse=True)
print("\n按成绩排序（稳定排序）:")
for student in grade_sort:
    print(f"  {student['name']} (ID: {student['id']}, 成绩: {student['grade']})")

# 2. 多级排序的实现
# 方法1：使用元组进行多级排序
multi_level_sort = sorted(students, key=lambda x: (-x['grade'], x['name']))
print("\n多级排序（成绩降序，姓名升序）:")
for student in multi_level_sort:
    print(f"  {student['name']} (成绩: {student['grade']})")

# 方法2：连续排序（利用稳定排序特性）
# 先按次要条件排序，再按主要条件排序
step1 = sorted(students, key=lambda x: x['name'])  # 先按姓名排序
step2 = sorted(step1, key=lambda x: x['grade'], reverse=True)  # 再按成绩排序
print("\n连续排序结果:")
for student in step2:
    print(f"  {student['name']} (成绩: {student['grade']})")

# 3. 复杂多级排序示例
sales_data = [
    {'region': 'North', 'quarter': 'Q1', 'sales': 100000, 'rep': 'Alice'},
    {'region': 'South', 'quarter': 'Q1', 'sales': 120000, 'rep': 'Bob'},
    {'region': 'North', 'quarter': 'Q2', 'sales': 110000, 'rep': 'Alice'},
    {'region': 'South', 'quarter': 'Q2', 'sales': 115000, 'rep': 'Bob'},
    {'region': 'North', 'quarter': 'Q1', 'sales': 95000, 'rep': 'Charlie'},
    {'region': 'South', 'quarter': 'Q1', 'sales': 125000, 'rep': 'Diana'}
]

# 多级排序：地区 -> 季度 -> 销售额（降序）
quarter_order = {'Q1': 1, 'Q2': 2, 'Q3': 3, 'Q4': 4}
complex_multi_sort = sorted(sales_data, 
                           key=lambda x: (x['region'], 
                                         quarter_order[x['quarter']], 
                                         -x['sales']))
print("\n销售数据多级排序:")
current_region = None
current_quarter = None
for data in complex_multi_sort:
    if data['region'] != current_region:
        current_region = data['region']
        print(f"\n{current_region}地区:")
    if data['quarter'] != current_quarter:
        current_quarter = data['quarter']
        print(f"  {current_quarter}:")
    print(f"    {data['rep']}: ${data['sales']:,}")
```

### 自定义稳定排序算法

```python
# 自定义稳定排序的实现

def stable_sort_with_original_order(data, key_func, reverse=False):
    """带原始顺序信息的稳定排序"""
    # 为每个元素添加原始索引
    indexed_data = [(item, index) for index, item in enumerate(data)]
    
    # 排序时同时考虑key值和原始索引
    sorted_data = sorted(indexed_data, 
                        key=lambda x: (key_func(x[0]), x[1]),
                        reverse=reverse)
    
    # 返回排序后的数据（去掉索引）
    return [item for item, _ in sorted_data]

# 测试自定义稳定排序
test_data = [
    {'name': 'A', 'score': 85},
    {'name': 'B', 'score': 90},
    {'name': 'C', 'score': 85},
    {'name': 'D', 'score': 90},
    {'name': 'E', 'score': 85}
]

print("自定义稳定排序测试:")
custom_sorted = stable_sort_with_original_order(test_data, 
                                               key_func=lambda x: x['score'], 
                                               reverse=True)
for item in custom_sorted:
    print(f"  {item['name']}: {item['score']}")

# 4. 排序稳定性验证
def verify_stability(original, sorted_data, key_func):
    """验证排序的稳定性"""
    # 找出具有相同key值的元素组
    key_groups = {}
    for i, item in enumerate(original):
        key_val = key_func(item)
        if key_val not in key_groups:
            key_groups[key_val] = []
        key_groups[key_val].append((item, i))
    
    # 检查每组内元素的相对顺序是否保持
    for key_val, group in key_groups.items():
        if len(group) > 1:
            # 在排序后的数据中找到这些元素的位置
            sorted_positions = []
            for item, orig_pos in group:
                for j, sorted_item in enumerate(sorted_data):
                    if sorted_item is item:  # 使用is比较对象身份
                        sorted_positions.append((orig_pos, j))
                        break
            
            # 检查原始顺序是否保持
            sorted_positions.sort(key=lambda x: x[1])  # 按排序后位置排序
            original_order = [pos[0] for pos in sorted_positions]
            
            if original_order != sorted(original_order):
                return False, f"Key {key_val} 的元素顺序不稳定"
    
    return True, "排序是稳定的"

# 验证Python内置排序的稳定性
original_list = test_data.copy()
sorted_list = sorted(original_list, key=lambda x: x['score'], reverse=True)
is_stable, message = verify_stability(original_list, sorted_list, lambda x: x['score'])
print(f"\n稳定性验证: {message}")
```

## 排序性能和优化

### 性能比较和分析

```python
# 排序性能比较和优化技巧

import time
import random
from functools import cmp_to_key

# 1. 不同排序方法的性能比较
def performance_comparison():
    """比较不同排序方法的性能"""
    # 生成测试数据
    data_sizes = [1000, 5000, 10000]
    
    for size in data_sizes:
        print(f"\n数据量: {size}")
        
        # 生成随机数据
        random_data = [random.randint(1, 1000) for _ in range(size)]
        
        # 测试内置sorted函数
        start_time = time.perf_counter()
        sorted_result = sorted(random_data)
        sorted_time = time.perf_counter() - start_time
        print(f"  sorted(): {sorted_time:.4f}秒")
        
        # 测试list.sort()方法
        test_data = random_data.copy()
        start_time = time.perf_counter()
        test_data.sort()
        sort_time = time.perf_counter() - start_time
        print(f"  list.sort(): {sort_time:.4f}秒")
        
        # 测试带key函数的排序
        start_time = time.perf_counter()
        key_sorted = sorted(random_data, key=lambda x: x)
        key_time = time.perf_counter() - start_time
        print(f"  带key的sorted(): {key_time:.4f}秒")
        
        # 测试复杂key函数的排序
        start_time = time.perf_counter()
        complex_key_sorted = sorted(random_data, key=lambda x: (x % 10, x // 10))
        complex_key_time = time.perf_counter() - start_time
        print(f"  复杂key的sorted(): {complex_key_time:.4f}秒")

performance_comparison()

# 2. 排序优化技巧
class SortOptimization:
    """排序优化技巧演示"""
    
    @staticmethod
    def precompute_keys(data, key_func):
        """预计算key值以提高性能"""
        # 为大量数据排序时，预计算key可以提高性能
        keyed_data = [(key_func(item), item) for item in data]
        keyed_data.sort(key=lambda x: x[0])
        return [item for key, item in keyed_data]
    
    @staticmethod
    def cached_key_function(expensive_key_func):
        """缓存昂贵的key计算"""
        cache = {}
        
        def cached_key(item):
            # 使用item的id作为缓存键（假设item是不可变的）
            item_id = id(item)
            if item_id not in cache:
                cache[item_id] = expensive_key_func(item)
            return cache[item_id]
        
        return cached_key
    
    @staticmethod
    def partial_sort(data, k):
        """部分排序：只需要前k个最小元素"""
        import heapq
        return heapq.nsmallest(k, data)

# 3. 性能优化示例
def expensive_calculation(x):
    """模拟昂贵的计算"""
    time.sleep(0.001)  # 模拟耗时操作
    return sum(int(digit) for digit in str(x))

# 测试数据
test_numbers = [random.randint(100, 999) for _ in range(100)]

print("\n性能优化测试:")

# 普通排序
start_time = time.perf_counter()
normal_sort = sorted(test_numbers, key=expensive_calculation)
normal_time = time.perf_counter() - start_time
print(f"普通排序: {normal_time:.4f}秒")

# 预计算key值
start_time = time.perf_counter()
precomputed_sort = SortOptimization.precompute_keys(test_numbers, expensive_calculation)
precomputed_time = time.perf_counter() - start_time
print(f"预计算key: {precomputed_time:.4f}秒")

# 缓存key函数
cached_key = SortOptimization.cached_key_function(expensive_calculation)
start_time = time.perf_counter()
cached_sort = sorted(test_numbers, key=cached_key)
cached_time = time.perf_counter() - start_time
print(f"缓存key函数: {cached_time:.4f}秒")

# 部分排序（只要前10个）
start_time = time.perf_counter()
partial_result = SortOptimization.partial_sort(test_numbers, 10)
partial_time = time.perf_counter() - start_time
print(f"部分排序(前10个): {partial_time:.4f}秒")

# 4. 内存使用优化
def memory_efficient_sort(data, key_func, reverse=False):
    """内存高效的排序方法"""
    # 对于大数据集，使用生成器可以节省内存
    def keyed_items():
        for item in data:
            yield (key_func(item), item)
    
    # 排序
    sorted_items = sorted(keyed_items(), key=lambda x: x[0], reverse=reverse)
    
    # 返回生成器而不是列表
    for key, item in sorted_items:
        yield item

# 测试内存效率
print("\n内存效率测试:")
large_data = list(range(10000))
random.shuffle(large_data)

# 普通排序（返回列表）
import sys
normal_result = sorted(large_data, key=lambda x: -x)
print(f"普通排序结果大小: {sys.getsizeof(normal_result)} bytes")

# 内存高效排序（返回生成器）
efficient_result = memory_efficient_sort(large_data, lambda x: -x)
print(f"生成器结果大小: {sys.getsizeof(efficient_result)} bytes")

# 验证结果正确性
efficient_list = list(efficient_result)
print(f"结果是否相同: {normal_result == efficient_list}")
```

## operator模块的使用

### operator模块简介

```python
# operator模块在排序中的应用

import operator
from operator import itemgetter, attrgetter, methodcaller

# 1. itemgetter的使用
students = [
    ('Alice', 85, 20),
    ('Bob', 90, 19),
    ('Charlie', 78, 21),
    ('Diana', 92, 20)
]

print("使用itemgetter排序:")

# 按第二个元素（成绩）排序
grade_sort = sorted(students, key=itemgetter(1), reverse=True)
print(f"按成绩排序: {grade_sort}")

# 按第三个元素（年龄）排序
age_sort = sorted(students, key=itemgetter(2))
print(f"按年龄排序: {age_sort}")

# 多字段排序
multi_sort = sorted(students, key=itemgetter(2, 1))  # 先按年龄，再按成绩
print(f"按年龄和成绩排序: {multi_sort}")

# 2. 字典数据的itemgetter
student_dicts = [
    {'name': 'Alice', 'grade': 85, 'age': 20},
    {'name': 'Bob', 'grade': 90, 'age': 19},
    {'name': 'Charlie', 'grade': 78, 'age': 21},
    {'name': 'Diana', 'grade': 92, 'age': 20}
]

print("\n字典数据排序:")

# 按姓名排序
name_sort = sorted(student_dicts, key=itemgetter('name'))
print("按姓名排序:")
for student in name_sort:
    print(f"  {student['name']}: {student['grade']}")

# 按成绩排序
dict_grade_sort = sorted(student_dicts, key=itemgetter('grade'), reverse=True)
print("\n按成绩排序:")
for student in dict_grade_sort:
    print(f"  {student['name']}: {student['grade']}")

# 多字段排序
dict_multi_sort = sorted(student_dicts, key=itemgetter('age', 'grade'))
print("\n按年龄和成绩排序:")
for student in dict_multi_sort:
    print(f"  {student['name']} ({student['age']}岁): {student['grade']}")
```

### attrgetter的使用

```python
# attrgetter用于对象属性排序

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    
    def __repr__(self):
        return f"Student('{self.name}', {self.grade}, {self.age})"

class Course:
    def __init__(self, name, credits, difficulty):
        self.name = name
        self.credits = credits
        self.difficulty = difficulty
    
    def __repr__(self):
        return f"Course('{self.name}', {self.credits}, {self.difficulty})"

# 创建学生对象
student_objects = [
    Student('Alice', 85, 20),
    Student('Bob', 90, 19),
    Student('Charlie', 78, 21),
    Student('Diana', 92, 20)
]

print("使用attrgetter排序对象:")

# 按姓名排序
name_sort = sorted(student_objects, key=attrgetter('name'))
print(f"按姓名排序: {name_sort}")

# 按成绩排序
grade_sort = sorted(student_objects, key=attrgetter('grade'), reverse=True)
print(f"按成绩排序: {grade_sort}")

# 多属性排序
multi_attr_sort = sorted(student_objects, key=attrgetter('age', 'grade'))
print(f"按年龄和成绩排序: {multi_attr_sort}")

# 嵌套属性排序
class StudentWithCourse:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
    def __repr__(self):
        return f"StudentWithCourse('{self.name}', {self.course})"

# 创建带课程的学生对象
students_with_courses = [
    StudentWithCourse('Alice', Course('Math', 3, 'Hard')),
    StudentWithCourse('Bob', Course('Physics', 4, 'Medium')),
    StudentWithCourse('Charlie', Course('Chemistry', 3, 'Hard')),
    StudentWithCourse('Diana', Course('Biology', 2, 'Easy'))
]

print("\n嵌套属性排序:")

# 按课程学分排序
credit_sort = sorted(students_with_courses, key=attrgetter('course.credits'), reverse=True)
print("按课程学分排序:")
for student in credit_sort:
    print(f"  {student.name}: {student.course.name} ({student.course.credits}学分)")

# 按课程难度排序
difficulty_order = {'Easy': 1, 'Medium': 2, 'Hard': 3}
difficulty_sort = sorted(students_with_courses, 
                        key=lambda x: difficulty_order[x.course.difficulty])
print("\n按课程难度排序:")
for student in difficulty_sort:
    print(f"  {student.name}: {student.course.name} ({student.course.difficulty})")
```

### methodcaller的使用

```python
# methodcaller用于调用对象方法进行排序

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.reviews = []
    
    def add_review(self, rating):
        self.reviews.append(rating)
    
    def average_rating(self):
        return sum(self.reviews) / len(self.reviews) if self.reviews else 0
    
    def get_discount_price(self, discount_rate=0.1):
        return self.price * (1 - discount_rate)
    
    def category_priority(self):
        priorities = {'Electronics': 1, 'Books': 2, 'Clothing': 3}
        return priorities.get(self.category, 4)
    
    def __repr__(self):
        return f"Product('{self.name}', ${self.price}, '{self.category}')"

# 创建产品对象
products = [
    Product('Laptop', 1200, 'Electronics'),
    Product('Book', 25, 'Books'),
    Product('Shirt', 50, 'Clothing'),
    Product('Phone', 800, 'Electronics')
]

# 添加评价
products[0].add_review(4.5)
products[0].add_review(4.2)
products[0].add_review(4.8)

products[1].add_review(4.0)
products[1].add_review(4.3)

products[2].add_review(3.8)
products[2].add_review(4.1)
products[2].add_review(3.9)

products[3].add_review(4.6)
products[3].add_review(4.4)

print("使用methodcaller排序:")

# 按平均评分排序
rating_sort = sorted(products, key=methodcaller('average_rating'), reverse=True)
print("按平均评分排序:")
for product in rating_sort:
    print(f"  {product.name}: {product.average_rating():.2f}")

# 按折扣价格排序
discount_sort = sorted(products, key=methodcaller('get_discount_price', 0.2))
print("\n按20%折扣价格排序:")
for product in discount_sort:
    discount_price = product.get_discount_price(0.2)
    print(f"  {product.name}: ${discount_price:.2f}")

# 按类别优先级排序
priority_sort = sorted(products, key=methodcaller('category_priority'))
print("\n按类别优先级排序:")
for product in priority_sort:
    print(f"  {product.name} ({product.category})")
```

### operator模块与lambda的比较

```python
# operator模块与lambda表达式的性能和可读性比较

import time
import random
from operator import itemgetter, attrgetter

# 测试数据
test_data = [{'name': f'Item{i}', 'value': random.randint(1, 1000)} for i in range(10000)]

print("性能比较测试:")

# 使用lambda
start_time = time.perf_counter()
lambda_result = sorted(test_data, key=lambda x: x['value'])
lambda_time = time.perf_counter() - start_time
print(f"Lambda排序: {lambda_time:.4f}秒")

# 使用itemgetter
start_time = time.perf_counter()
itemgetter_result = sorted(test_data, key=itemgetter('value'))
itemgetter_time = time.perf_counter() - start_time
print(f"itemgetter排序: {itemgetter_time:.4f}秒")

print(f"性能提升: {(lambda_time - itemgetter_time) / lambda_time * 100:.1f}%")

# 可读性比较
print("\n可读性比较:")

# 复杂的lambda表达式
complex_lambda = sorted(test_data, key=lambda x: (x['name'], -x['value']))
print("复杂lambda: key=lambda x: (x['name'], -x['value'])")

# 使用itemgetter的等价表达
complex_itemgetter = sorted(test_data, key=itemgetter('name', 'value'))
# 注意：itemgetter不能直接处理负值，需要额外处理
print("itemgetter: key=itemgetter('name', 'value')")

# 对于需要变换的情况，lambda更灵活
print("\n灵活性比较:")
print("Lambda (灵活): key=lambda x: x['value'] ** 2")
print("itemgetter (受限): 无法直接实现平方运算")
```

## 实际应用案例

### 数据分析中的排序

```python
# 数据分析场景中的排序应用

# 1. 销售数据分析
sales_records = [
    {'date': '2024-01-15', 'product': 'Laptop', 'quantity': 5, 'price': 1200, 'region': 'North'},
    {'date': '2024-01-16', 'product': 'Phone', 'quantity': 10, 'price': 800, 'region': 'South'},
    {'date': '2024-01-17', 'product': 'Tablet', 'quantity': 8, 'price': 500, 'region': 'East'},
    {'date': '2024-01-18', 'product': 'Laptop', 'quantity': 3, 'price': 1200, 'region': 'West'},
    {'date': '2024-01-19', 'product': 'Phone', 'quantity': 15, 'price': 800, 'region': 'North'}
]

print("销售数据分析:")

# 按销售额排序（数量 × 价格）
revenue_sort = sorted(sales_records, 
                     key=lambda x: x['quantity'] * x['price'], 
                     reverse=True)
print("按销售额排序:")
for record in revenue_sort:
    revenue = record['quantity'] * record['price']
    print(f"  {record['product']} ({record['region']}): ${revenue:,}")

# 按日期和地区排序
date_region_sort = sorted(sales_records, key=lambda x: (x['date'], x['region']))
print("\n按日期和地区排序:")
for record in date_region_sort:
    print(f"  {record['date']} - {record['region']}: {record['product']}")

# 2. 学生成绩分析
student_scores = [
    {'name': 'Alice', 'math': 85, 'english': 92, 'science': 78},
    {'name': 'Bob', 'math': 76, 'english': 85, 'science': 90},
    {'name': 'Charlie', 'math': 95, 'english': 87, 'science': 92},
    {'name': 'Diana', 'math': 68, 'english': 75, 'science': 82}
]

print("\n学生成绩分析:")

# 按总分排序
total_score_sort = sorted(student_scores, 
                         key=lambda x: x['math'] + x['english'] + x['science'], 
                         reverse=True)
print("按总分排序:")
for student in total_score_sort:
    total = student['math'] + student['english'] + student['science']
    print(f"  {student['name']}: {total}")

# 按数学成绩排序
math_sort = sorted(student_scores, key=lambda x: x['math'], reverse=True)
print("\n按数学成绩排序:")
for student in math_sort:
    print(f"  {student['name']}: {student['math']}")

# 按成绩方差排序（找出成绩最均衡的学生）
def score_variance(student):
    scores = [student['math'], student['english'], student['science']]
    mean = sum(scores) / len(scores)
    return sum((score - mean) ** 2 for score in scores) / len(scores)

variance_sort = sorted(student_scores, key=lambda x: score_variance(x))
print("\n按成绩均衡性排序（方差从小到大）:")
for student in variance_sort:
    variance = score_variance(student)
    print(f"  {student['name']}: 方差 {variance:.2f}")
```

### 文件和系统管理

```python
# 文件和系统管理中的排序应用

import os
from datetime import datetime

# 模拟文件信息
file_info = [
    {'name': 'document.pdf', 'size': 2048576, 'modified': '2024-01-15 10:30:00', 'type': 'pdf'},
    {'name': 'image.jpg', 'size': 1024000, 'modified': '2024-01-16 14:20:00', 'type': 'jpg'},
    {'name': 'script.py', 'size': 4096, 'modified': '2024-01-17 09:15:00', 'type': 'py'},
    {'name': 'data.csv', 'size': 512000, 'modified': '2024-01-14 16:45:00', 'type': 'csv'},
    {'name': 'readme.txt', 'size': 2048, 'modified': '2024-01-18 11:00:00', 'type': 'txt'}
]

print("文件管理排序:")

# 按文件大小排序
size_sort = sorted(file_info, key=lambda x: x['size'], reverse=True)
print("按文件大小排序:")
for file in size_sort:
    size_mb = file['size'] / 1024 / 1024
    print(f"  {file['name']}: {size_mb:.2f} MB")

# 按修改时间排序
time_sort = sorted(file_info, 
                  key=lambda x: datetime.strptime(x['modified'], '%Y-%m-%d %H:%M:%S'), 
                  reverse=True)
print("\n按修改时间排序（最新优先）:")
for file in time_sort:
    print(f"  {file['name']}: {file['modified']}")

# 按文件类型和大小排序
type_size_sort = sorted(file_info, key=lambda x: (x['type'], -x['size']))
print("\n按文件类型和大小排序:")
current_type = None
for file in type_size_sort:
    if file['type'] != current_type:
        current_type = file['type']
        print(f"\n{current_type.upper()}文件:")
    size_kb = file['size'] / 1024
    print(f"  {file['name']}: {size_kb:.1f} KB")

# 按文件名长度和字母顺序排序
name_sort = sorted(file_info, key=lambda x: (len(x['name']), x['name']))
print("\n按文件名长度和字母顺序排序:")
for file in name_sort:
    print(f"  {file['name']} (长度: {len(file['name'])})")
```

## 最佳实践和注意事项

### 排序最佳实践

```python
# 排序的最佳实践

# 1. 选择合适的排序方法
print("排序方法选择指南:")
print("- 简单数据类型: 直接使用sorted()或list.sort()")
print("- 字典/列表索引: 使用itemgetter")
print("- 对象属性: 使用attrgetter")
print("- 对象方法: 使用methodcaller")
print("- 复杂逻辑: 使用lambda表达式")

# 2. 性能考虑
print("\n性能优化建议:")
print("- 大数据集: 预计算key值")
print("- 重复排序: 缓存key函数结果")
print("- 部分排序: 使用heapq.nsmallest/nlargest")
print("- 原地排序: 使用list.sort()而不是sorted()")

# 3. 稳定性考虑
print("\n稳定性注意事项:")
print("- Python的排序是稳定的")
print("- 多级排序可以利用稳定性")
print("- 连续排序: 先次要条件，后主要条件")

# 4. 常见错误和陷阱
print("\n常见错误:")

# 错误1: 修改正在排序的列表
original_list = [3, 1, 4, 1, 5]
print(f"原始列表: {original_list}")

# 错误的做法（不要这样做）
# sorted_list = sorted(original_list, key=lambda x: original_list.append(x) or x)

# 正确的做法
sorted_list = sorted(original_list)
print(f"正确排序: {sorted_list}")

# 错误2: key函数返回不一致的类型
mixed_data = [1, '2', 3.0, '4']
print(f"\n混合类型数据: {mixed_data}")

# 错误的做法（可能导致TypeError）
try:
    wrong_sort = sorted(mixed_data)
except TypeError as e:
    print(f"类型错误: {e}")

# 正确的做法：统一转换类型
correct_sort = sorted(mixed_data, key=lambda x: str(x))
print(f"正确排序（转为字符串）: {correct_sort}")

# 错误3: 忘记reverse参数
scores = [85, 92, 78, 95, 88]
print(f"\n成绩列表: {scores}")

# 降序排序的正确方法
desc_sort = sorted(scores, reverse=True)
print(f"降序排序: {desc_sort}")

# 不推荐的方法（效率较低）
manual_desc = sorted(scores, key=lambda x: -x)
print(f"手动降序: {manual_desc}")
```

### 调试和测试

```python
# 排序调试和测试技巧

# 1. 调试排序逻辑
def debug_sort(data, key_func, description=""):
    """带调试信息的排序函数"""
    print(f"\n调试排序: {description}")
    print(f"原始数据: {data}")
    
    # 显示每个元素的key值
    print("Key值:")
    for item in data:
        key_val = key_func(item)
        print(f"  {item} -> {key_val}")
    
    # 执行排序
    result = sorted(data, key=key_func)
    print(f"排序结果: {result}")
    
    return result

# 测试调试函数
test_data = [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 92}, {'name': 'Charlie', 'score': 78}]
debug_result = debug_sort(test_data, lambda x: x['score'], "按分数排序")

# 2. 验证排序正确性
def verify_sort(original, sorted_data, key_func, reverse=False):
    """验证排序结果的正确性"""
    # 检查长度
    if len(original) != len(sorted_data):
        return False, "长度不匹配"
    
    # 检查所有元素都存在
    if set(id(x) for x in original) != set(id(x) for x in sorted_data):
        return False, "元素不匹配"
    
    # 检查排序顺序
    for i in range(len(sorted_data) - 1):
        key1 = key_func(sorted_data[i])
        key2 = key_func(sorted_data[i + 1])
        
        if reverse:
            if key1 < key2:
                return False, f"顺序错误: {key1} < {key2} at position {i}"
        else:
            if key1 > key2:
                return False, f"顺序错误: {key1} > {key2} at position {i}"
    
    return True, "排序正确"

# 测试验证函数
original_data = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_data = sorted(original_data)
is_correct, message = verify_sort(original_data, sorted_data, lambda x: x)
print(f"\n排序验证: {message}")

# 3. 性能测试框架
def benchmark_sort_methods(data, methods, iterations=1000):
    """比较不同排序方法的性能"""
    import time
    
    results = {}
    
    for name, sort_func in methods.items():
        total_time = 0
        
        for _ in range(iterations):
            test_data = data.copy()
            start_time = time.perf_counter()
            sort_func(test_data)
            total_time += time.perf_counter() - start_time
        
        avg_time = total_time / iterations
        results[name] = avg_time
    
    return results

# 测试不同排序方法
test_data = [random.randint(1, 1000) for _ in range(1000)]

sort_methods = {
    'sorted()': lambda data: sorted(data),
    'list.sort()': lambda data: data.sort(),
    'sorted() with key': lambda data: sorted(data, key=lambda x: x),
    'heapq.nsmallest': lambda data: __import__('heapq').nsmallest(len(data), data)
}

performance_results = benchmark_sort_methods(test_data, sort_methods, 100)
print("\n性能测试结果:")
for method, time_taken in sorted(performance_results.items(), key=lambda x: x[1]):
    print(f"  {method}: {time_taken:.6f}秒")
```

## 总结

Lambda表达式与排序函数的结合使用是Python编程中的重要技能。通过本节的学习，你应该掌握：

### 核心概念
1. **sorted()函数和list.sort()方法的区别和使用场景**
2. **key参数的作用和重要性**
3. **Lambda表达式作为key函数的各种应用**
4. **多级排序和复合排序条件**
5. **稳定排序的概念和应用**

### 实用技巧
1. **使用operator模块提高性能和可读性**
2. **针对不同数据类型的排序策略**
3. **性能优化和内存管理**
4. **调试和测试排序逻辑**

### 最佳实践
1. **根据数据特点选择合适的排序方法**
2. **注意类型一致性和错误处理**
3. **利用稳定排序特性实现复杂排序需求**
4. **在性能关键场景中进行优化**

## 运行代码

将代码保存为Python文件并运行：

```bash
python3 06_lambda_with_sort.py
```

每个代码块都是独立的示例，你可以单独运行来理解特定的概念和技巧。建议按顺序学习，并尝试修改参数来观察不同的排序效果。