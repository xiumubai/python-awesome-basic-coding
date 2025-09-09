# Lambda表达式与filter函数

本节将详细介绍Lambda表达式与filter函数的结合使用，这是数据筛选和过滤中最常用的组合。

## filter函数基础

### filter函数的语法

```python
# filter函数的基本语法
# filter(function, iterable)
# 返回一个filter对象（迭代器）

# 基本示例
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用filter函数筛选偶数
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(f"filter对象: {even_numbers}")
print(f"转换为列表: {list(even_numbers)}")
```

### filter函数的工作原理

```python
# filter函数的工作原理演示
def demonstrate_filter_process():
    """演示filter函数的工作过程"""
    numbers = [1, 2, 3, 4, 5, 6]
    
    print("原始数据:", numbers)
    print("\nfilter函数处理过程（筛选偶数）:")
    
    # 手动模拟filter的工作过程
    is_even = lambda x: x % 2 == 0
    result = []
    
    for i, num in enumerate(numbers):
        condition_result = is_even(num)
        if condition_result:
            result.append(num)
        print(f"步骤{i+1}: {num} -> {condition_result} -> {'保留' if condition_result else '过滤'}")
    
    print(f"\n最终结果: {result}")
    
    # 使用真正的filter函数
    filter_result = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"filter函数结果: {filter_result}")
    print(f"结果相同: {result == filter_result}")

demonstrate_filter_process()
```

## Lambda与filter的基本结合

### 数值筛选

```python
# 各种数值筛选示例
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 25]

# 1. 筛选偶数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数: {even_numbers}")

# 2. 筛选奇数
odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
print(f"奇数: {odd_numbers}")

# 3. 筛选大于10的数
greater_than_10 = list(filter(lambda x: x > 10, numbers))
print(f"大于10: {greater_than_10}")

# 4. 筛选5的倍数
multiples_of_5 = list(filter(lambda x: x % 5 == 0, numbers))
print(f"5的倍数: {multiples_of_5}")

# 5. 筛选质数（简单判断）
def is_prime_simple(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = list(filter(is_prime_simple, numbers))
print(f"质数: {primes}")

# 6. 筛选范围内的数
in_range = list(filter(lambda x: 5 <= x <= 15, numbers))
print(f"5到15之间: {in_range}")
```

### 字符串筛选

```python
# 字符串筛选示例
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

# 1. 筛选长度大于5的单词
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"长度>5的单词: {long_words}")

# 2. 筛选以特定字母开头的单词
starts_with_a = list(filter(lambda word: word.startswith('a'), words))
print(f"以'a'开头: {starts_with_a}")

# 3. 筛选包含特定字母的单词
contains_e = list(filter(lambda word: 'e' in word, words))
print(f"包含'e': {contains_e}")

# 4. 筛选元音字母开头的单词
vowel_start = list(filter(lambda word: word[0].lower() in 'aeiou', words))
print(f"元音开头: {vowel_start}")

# 5. 筛选回文单词
palindromes = list(filter(lambda word: word == word[::-1], words + ['level', 'radar', 'noon']))
print(f"回文单词: {palindromes}")

# 6. 筛选只包含字母的字符串
text_data = ['hello', 'world123', 'python', 'code!', 'lambda', 'filter2']
only_letters = list(filter(lambda text: text.isalpha(), text_data))
print(f"只包含字母: {only_letters}")
```

## 与普通函数的对比

### 使用普通函数

```python
# 使用普通函数的方式
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 定义普通函数
def is_even(x):
    return x % 2 == 0

def is_positive(x):
    return x > 0

def is_single_digit(x):
    return 0 <= x <= 9

# 使用普通函数
even_func = list(filter(is_even, numbers))
positive_func = list(filter(is_positive, numbers + [-1, -2]))
single_digit_func = list(filter(is_single_digit, numbers + [15, 20]))

print(f"普通函数 - 偶数: {even_func}")
print(f"普通函数 - 正数: {positive_func}")
print(f"普通函数 - 个位数: {single_digit_func}")
```

### 使用Lambda表达式

```python
# 使用Lambda表达式的方式
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用Lambda
even_lambda = list(filter(lambda x: x % 2 == 0, numbers))
positive_lambda = list(filter(lambda x: x > 0, numbers + [-1, -2]))
single_digit_lambda = list(filter(lambda x: 0 <= x <= 9, numbers + [15, 20]))

print(f"Lambda - 偶数: {even_lambda}")
print(f"Lambda - 正数: {positive_lambda}")
print(f"Lambda - 个位数: {single_digit_lambda}")

# 验证结果相同
print(f"\n结果验证:")
print(f"偶数结果相同: {even_func == even_lambda}")
print(f"正数结果相同: {positive_func == positive_lambda}")
print(f"个位数结果相同: {single_digit_func == single_digit_lambda}")
```

### 复杂条件的对比

```python
# 复杂筛选条件的对比
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 18, 20, 25]

# 普通函数：复杂条件更清晰
def complex_condition(x):
    """复杂的筛选条件"""
    # 条件：偶数且大于5且小于20
    is_even = x % 2 == 0
    in_range = 5 < x < 20
    return is_even and in_range

# Lambda：简单条件更简洁
simple_lambda = lambda x: x % 2 == 0 and 5 < x < 20

# 测试两种方法
complex_result = list(filter(complex_condition, data))
simple_result = list(filter(simple_lambda, data))

print(f"复杂条件筛选:")
print(f"普通函数结果: {complex_result}")
print(f"Lambda结果: {simple_result}")
print(f"结果相同: {complex_result == simple_result}")

# 更复杂的条件：普通函数的优势
def very_complex_condition(x):
    """非常复杂的筛选条件"""
    # 多重条件判断
    if x < 0:
        return False
    
    if x % 3 == 0 and x % 5 == 0:  # 15的倍数
        return True
    
    if x > 10 and x % 2 == 0:  # 大于10的偶数
        return True
    
    if 2 <= x <= 7:  # 2到7之间的数
        return True
    
    return False

very_complex_result = list(filter(very_complex_condition, data))
print(f"\n非常复杂条件结果: {very_complex_result}")
```

## 数值范围筛选

### 基本范围筛选

```python
# 数值范围筛选示例
import random

# 生成测试数据
random.seed(42)
test_numbers = [random.randint(-50, 50) for _ in range(20)]
print(f"测试数据: {test_numbers}")

# 1. 筛选正数
positive = list(filter(lambda x: x > 0, test_numbers))
print(f"正数: {positive}")

# 2. 筛选负数
negative = list(filter(lambda x: x < 0, test_numbers))
print(f"负数: {negative}")

# 3. 筛选绝对值大于20的数
abs_greater_20 = list(filter(lambda x: abs(x) > 20, test_numbers))
print(f"绝对值>20: {abs_greater_20}")

# 4. 筛选特定范围内的数
in_range_10_30 = list(filter(lambda x: 10 <= x <= 30, test_numbers))
print(f"10到30之间: {in_range_10_30}")

# 5. 筛选不在特定范围内的数
out_of_range = list(filter(lambda x: not (-10 <= x <= 10), test_numbers))
print(f"不在-10到10之间: {out_of_range}")
```

### 数学条件筛选

```python
# 数学条件筛选
import math

numbers = list(range(1, 101))  # 1到100的数字

# 1. 筛选完全平方数
perfect_squares = list(filter(lambda x: int(math.sqrt(x))**2 == x, numbers))
print(f"完全平方数: {perfect_squares}")

# 2. 筛选能被3整除但不能被9整除的数
div_by_3_not_9 = list(filter(lambda x: x % 3 == 0 and x % 9 != 0, numbers))
print(f"能被3整除但不能被9整除: {div_by_3_not_9[:10]}...")  # 只显示前10个

# 3. 筛选数字根为特定值的数
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

digital_root_5 = list(filter(lambda x: digital_root(x) == 5, numbers))
print(f"数字根为5: {digital_root_5[:10]}...")  # 只显示前10个

# 4. 筛选回文数
palindromes = list(filter(lambda x: str(x) == str(x)[::-1], numbers))
print(f"回文数: {palindromes}")

# 5. 筛选各位数字之和为特定值的数
digit_sum_10 = list(filter(lambda x: sum(int(d) for d in str(x)) == 10, numbers))
print(f"各位数字之和为10: {digit_sum_10}")
```

## 复杂条件筛选

### 多重条件组合

```python
# 多重条件组合筛选
data = list(range(1, 51))  # 1到50的数字

# 1. AND条件：偶数且大于20
even_and_gt_20 = list(filter(lambda x: x % 2 == 0 and x > 20, data))
print(f"偶数且>20: {even_and_gt_20}")

# 2. OR条件：能被3整除或能被7整除
div_3_or_7 = list(filter(lambda x: x % 3 == 0 or x % 7 == 0, data))
print(f"能被3或7整除: {div_3_or_7}")

# 3. NOT条件：不是5的倍数
not_mult_5 = list(filter(lambda x: x % 5 != 0, data))
print(f"不是5的倍数: {not_mult_5[:15]}...")  # 只显示前15个

# 4. 复杂组合：(偶数且>10) 或 (奇数且<20)
complex_condition = list(filter(
    lambda x: (x % 2 == 0 and x > 10) or (x % 2 == 1 and x < 20), 
    data
))
print(f"复杂条件: {complex_condition}")

# 5. 嵌套条件：质数且个位数是1或7
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_ending_1_or_7 = list(filter(
    lambda x: is_prime(x) and (x % 10 == 1 or x % 10 == 7), 
    data
))
print(f"质数且个位数是1或7: {prime_ending_1_or_7}")
```

### 基于函数结果的筛选

```python
# 基于函数结果的筛选
import math

numbers = list(range(1, 21))

# 1. 筛选平方根为整数的数
sqrt_integer = list(filter(lambda x: math.sqrt(x).is_integer(), numbers))
print(f"平方根为整数: {sqrt_integer}")

# 2. 筛选阶乘小于1000的数
def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

factorial_lt_1000 = list(filter(lambda x: factorial(x) < 1000, numbers))
print(f"阶乘<1000: {factorial_lt_1000}")

# 3. 筛选斐波那契数列中的数
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

fibonacci_numbers = list(filter(is_fibonacci, numbers))
print(f"斐波那契数: {fibonacci_numbers}")

# 4. 筛选各位数字乘积为偶数的数
digit_product_even = list(filter(
    lambda x: (lambda n: eval('*'.join(str(n))) if len(str(n)) > 1 else n)(x) % 2 == 0,
    numbers
))
# 更清晰的写法
def digit_product(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

digit_product_even_clear = list(filter(lambda x: digit_product(x) % 2 == 0, numbers))
print(f"各位数字乘积为偶数: {digit_product_even_clear}")
```

## 数据清洗应用

### 清理无效数据

```python
# 数据清洗示例
raw_data = [1, 2, None, 4, 0, -1, '', 'invalid', 7.5, '8', 9, [], {}, 10]

# 1. 筛选非空值
non_none = list(filter(lambda x: x is not None, raw_data))
print(f"非空值: {non_none}")

# 2. 筛选数值类型
numeric_values = list(filter(lambda x: isinstance(x, (int, float)), raw_data))
print(f"数值类型: {numeric_values}")

# 3. 筛选正数
positive_numbers = list(filter(lambda x: isinstance(x, (int, float)) and x > 0, raw_data))
print(f"正数: {positive_numbers}")

# 4. 筛选有效字符串（非空且为字符串）
valid_strings = list(filter(lambda x: isinstance(x, str) and x.strip(), raw_data + ['  ', 'valid']))
print(f"有效字符串: {valid_strings}")

# 5. 筛选可转换为数字的字符串
def is_numeric_string(s):
    if not isinstance(s, str):
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False

numeric_strings = list(filter(is_numeric_string, raw_data + ['3.14', 'abc', '42']))
print(f"可转换为数字的字符串: {numeric_strings}")
```

### 数据验证

```python
# 数据验证示例
user_data = [
    {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'},
    {'name': '', 'age': 30, 'email': 'invalid-email'},
    {'name': 'Bob', 'age': -5, 'email': 'bob@test.com'},
    {'name': 'Charlie', 'age': 35, 'email': 'charlie@domain.org'},
    {'name': 'Diana', 'age': 150, 'email': 'diana@site.net'},
    {'name': 'Eve', 'age': 28, 'email': ''},
]

# 1. 筛选有效姓名（非空）
valid_names = list(filter(lambda user: user.get('name', '').strip(), user_data))
print(f"有效姓名数量: {len(valid_names)}")

# 2. 筛选合理年龄（0-120岁）
valid_ages = list(filter(lambda user: 0 <= user.get('age', -1) <= 120, user_data))
print(f"合理年龄数量: {len(valid_ages)}")

# 3. 筛选有效邮箱（简单验证）
import re
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
valid_emails = list(filter(
    lambda user: re.match(email_pattern, user.get('email', '')), 
    user_data
))
print(f"有效邮箱数量: {len(valid_emails)}")

# 4. 筛选完全有效的用户数据
def is_valid_user(user):
    name_valid = user.get('name', '').strip()
    age_valid = 0 <= user.get('age', -1) <= 120
    email_valid = re.match(email_pattern, user.get('email', ''))
    return name_valid and age_valid and email_valid

valid_users = list(filter(is_valid_user, user_data))
print(f"完全有效的用户: {len(valid_users)}")
for user in valid_users:
    print(f"  {user['name']} ({user['age']}岁): {user['email']}")
```

## 文件和路径筛选

### 文件类型筛选

```python
# 文件路径筛选示例
file_paths = [
    'document.txt',
    'image.jpg',
    'script.py',
    'data.csv',
    'photo.png',
    'readme.md',
    'config.json',
    'style.css',
    'index.html',
    'backup.zip'
]

# 1. 筛选特定扩展名的文件
text_files = list(filter(lambda path: path.endswith('.txt'), file_paths))
print(f"文本文件: {text_files}")

image_files = list(filter(lambda path: path.endswith(('.jpg', '.png', '.gif')), file_paths))
print(f"图片文件: {image_files}")

code_files = list(filter(lambda path: path.endswith(('.py', '.js', '.html', '.css')), file_paths))
print(f"代码文件: {code_files}")

# 2. 筛选包含特定关键词的文件
config_files = list(filter(lambda path: 'config' in path.lower(), file_paths + ['app_config.ini', 'settings.conf']))
print(f"配置文件: {config_files}")

# 3. 筛选文件名长度
short_names = list(filter(lambda path: len(path.split('.')[0]) <= 5, file_paths))
print(f"短文件名: {short_names}")

# 4. 筛选不包含数字的文件名
no_digits = list(filter(lambda path: not any(c.isdigit() for c in path), file_paths + ['file1.txt', 'doc2.pdf']))
print(f"不包含数字: {no_digits}")
```

### 路径模式筛选

```python
# 路径模式筛选
file_paths_with_dirs = [
    '/home/user/documents/file.txt',
    '/var/log/system.log',
    '/usr/bin/python',
    '/home/user/pictures/photo.jpg',
    '/tmp/temp_file.tmp',
    '/etc/config.conf',
    '/home/user/downloads/archive.zip',
    '/opt/app/data.json'
]

# 1. 筛选用户目录下的文件
user_files = list(filter(lambda path: '/home/user/' in path, file_paths_with_dirs))
print(f"用户文件: {user_files}")

# 2. 筛选系统目录下的文件
system_files = list(filter(lambda path: path.startswith(('/usr/', '/var/', '/etc/')), file_paths_with_dirs))
print(f"系统文件: {system_files}")

# 3. 筛选临时文件
temp_files = list(filter(lambda path: '/tmp/' in path or path.endswith('.tmp'), file_paths_with_dirs))
print(f"临时文件: {temp_files}")

# 4. 筛选深度大于3的路径
deep_paths = list(filter(lambda path: len(path.split('/')) > 4, file_paths_with_dirs))
print(f"深层路径: {deep_paths}")
```

## 日期和时间筛选

### 日期筛选

```python
# 日期和时间筛选示例
from datetime import datetime, timedelta

# 创建测试日期数据
base_date = datetime(2024, 1, 1)
dates = [base_date + timedelta(days=i*7) for i in range(20)]  # 每周一个日期

print("测试日期（前5个）:")
for date in dates[:5]:
    print(f"  {date.strftime('%Y-%m-%d %A')}")

# 1. 筛选特定月份的日期
january_dates = list(filter(lambda date: date.month == 1, dates))
print(f"\n1月份的日期数量: {len(january_dates)}")

# 2. 筛选工作日（周一到周五）
weekdays = list(filter(lambda date: date.weekday() < 5, dates))
print(f"工作日数量: {len(weekdays)}")

# 3. 筛选周末
weekends = list(filter(lambda date: date.weekday() >= 5, dates))
print(f"周末数量: {len(weekends)}")

# 4. 筛选特定季度的日期
q1_dates = list(filter(lambda date: 1 <= date.month <= 3, dates))
print(f"第一季度日期数量: {len(q1_dates)}")

# 5. 筛选距离今天30天内的日期
today = datetime.now()
recent_dates = list(filter(lambda date: abs((date - today).days) <= 30, dates))
print(f"30天内的日期数量: {len(recent_dates)}")
```

### 时间范围筛选

```python
# 时间范围筛选
from datetime import time

# 创建时间数据
times = [time(hour, 0) for hour in range(24)]  # 每小时的整点时间

# 1. 筛选工作时间（9:00-17:00）
work_hours = list(filter(lambda t: time(9, 0) <= t <= time(17, 0), times))
print(f"工作时间: {[t.strftime('%H:%M') for t in work_hours]}")

# 2. 筛选夜间时间（22:00-06:00）
night_hours = list(filter(lambda t: t >= time(22, 0) or t <= time(6, 0), times))
print(f"夜间时间: {[t.strftime('%H:%M') for t in night_hours]}")

# 3. 筛选午餐时间（11:30-13:30）
lunch_hours = list(filter(lambda t: time(11, 30) <= t <= time(13, 30), 
                         [time(11, 0), time(11, 30), time(12, 0), time(12, 30), time(13, 0), time(13, 30), time(14, 0)]))
print(f"午餐时间: {[t.strftime('%H:%M') for t in lunch_hours]}")

# 4. 筛选偶数小时
even_hours = list(filter(lambda t: t.hour % 2 == 0, times))
print(f"偶数小时: {[t.strftime('%H:%M') for t in even_hours[:6]]}...")  # 只显示前6个
```

## 性能比较

### filter vs 列表推导式

```python
import time

# 准备测试数据
test_data = list(range(100000))

# 方法1：使用filter + lambda
start_time = time.time()
result_filter = list(filter(lambda x: x % 2 == 0, test_data))
filter_time = time.time() - start_time

# 方法2：使用列表推导式
start_time = time.time()
result_comprehension = [x for x in test_data if x % 2 == 0]
comprehension_time = time.time() - start_time

# 方法3：使用普通循环
start_time = time.time()
result_loop = []
for x in test_data:
    if x % 2 == 0:
        result_loop.append(x)
loop_time = time.time() - start_time

print(f"性能对比（处理{len(test_data)}个元素）:")
print(f"filter + lambda: {filter_time:.4f}秒")
print(f"列表推导式: {comprehension_time:.4f}秒")
print(f"普通循环: {loop_time:.4f}秒")

# 验证结果相同
print(f"\n结果验证:")
print(f"filter == 推导式: {result_filter == result_comprehension}")
print(f"filter == 循环: {result_filter == result_loop}")
print(f"结果长度: {len(result_filter)}")
```

### 惰性求值的优势

```python
# 演示filter的惰性求值
def expensive_check(x):
    """模拟耗时的检查操作"""
    print(f"检查 {x}...")
    time.sleep(0.01)  # 模拟耗时
    return x % 10 == 0

data = list(range(1, 21))

print("创建filter对象（惰性求值）:")
filter_obj = filter(expensive_check, data)
print(f"filter对象已创建: {filter_obj}")
print("注意：此时还没有执行expensive_check")

print("\n获取前3个结果:")
results = []
for i, value in enumerate(filter_obj):
    results.append(value)
    if i >= 2:  # 只获取前3个结果
        break

print(f"前3个结果: {results}")
print("注意：只处理了必要的元素")

# 对比：列表推导式会处理所有元素
print("\n使用列表推导式（立即执行所有检查）:")
result_comprehension = [x for x in data if expensive_check(x)]
print(f"所有结果: {result_comprehension}")
```

## 实际应用案例

### 日志分析

```python
# 日志分析示例
log_entries = [
    "2024-01-15 10:30:25 INFO User login successful",
    "2024-01-15 10:31:12 ERROR Database connection failed",
    "2024-01-15 10:32:05 WARNING Low disk space",
    "2024-01-15 10:33:18 INFO User logout",
    "2024-01-15 10:34:22 ERROR File not found",
    "2024-01-15 10:35:10 DEBUG Cache cleared",
    "2024-01-15 10:36:45 INFO New user registered",
    "2024-01-15 10:37:33 ERROR Network timeout",
]

# 1. 筛选错误日志
error_logs = list(filter(lambda log: 'ERROR' in log, log_entries))
print("错误日志:")
for log in error_logs:
    print(f"  {log}")

# 2. 筛选特定时间段的日志（10:32-10:36）
time_range_logs = list(filter(
    lambda log: '10:32' <= log.split()[1] <= '10:36', 
    log_entries
))
print(f"\n10:32-10:36时间段日志数量: {len(time_range_logs)}")

# 3. 筛选包含特定关键词的日志
user_logs = list(filter(lambda log: 'user' in log.lower(), log_entries))
print(f"\n用户相关日志数量: {len(user_logs)}")

# 4. 筛选非DEBUG级别的日志
non_debug_logs = list(filter(lambda log: 'DEBUG' not in log, log_entries))
print(f"非DEBUG日志数量: {len(non_debug_logs)}")
```

### 数据分析

```python
# 销售数据分析示例
sales_data = [
    {'product': 'Laptop', 'price': 1200, 'quantity': 5, 'category': 'Electronics'},
    {'product': 'Mouse', 'price': 25, 'quantity': 50, 'category': 'Electronics'},
    {'product': 'Book', 'price': 15, 'quantity': 100, 'category': 'Education'},
    {'product': 'Chair', 'price': 150, 'quantity': 20, 'category': 'Furniture'},
    {'product': 'Desk', 'price': 300, 'quantity': 10, 'category': 'Furniture'},
    {'product': 'Pen', 'price': 2, 'quantity': 200, 'category': 'Office'},
    {'product': 'Monitor', 'price': 400, 'quantity': 8, 'category': 'Electronics'},
]

# 1. 筛选高价值商品（价格>100）
high_value = list(filter(lambda item: item['price'] > 100, sales_data))
print(f"高价值商品数量: {len(high_value)}")

# 2. 筛选电子产品
electronics = list(filter(lambda item: item['category'] == 'Electronics', sales_data))
print(f"电子产品数量: {len(electronics)}")

# 3. 筛选库存充足的商品（数量>15）
high_stock = list(filter(lambda item: item['quantity'] > 15, sales_data))
print(f"库存充足商品: {[item['product'] for item in high_stock]}")

# 4. 筛选总价值高的商品（价格*数量>1000）
high_total_value = list(filter(
    lambda item: item['price'] * item['quantity'] > 1000, 
    sales_data
))
print("高总价值商品:")
for item in high_total_value:
    total = item['price'] * item['quantity']
    print(f"  {item['product']}: ${total}")

# 5. 筛选特定价格范围的商品
mid_range_price = list(filter(
    lambda item: 50 <= item['price'] <= 200, 
    sales_data
))
print(f"\n中等价位商品: {[item['product'] for item in mid_range_price]}")
```

### 文本处理和搜索

```python
# 文本搜索和过滤示例
articles = [
    "Python is a powerful programming language",
    "JavaScript is widely used for web development",
    "Machine learning with Python is very popular",
    "Data science requires statistical knowledge",
    "Web development using JavaScript frameworks",
    "Python libraries for data analysis",
    "Artificial intelligence and machine learning",
    "Database design and optimization techniques"
]

# 1. 搜索包含特定关键词的文章
python_articles = list(filter(lambda article: 'Python' in article, articles))
print(f"包含'Python'的文章: {len(python_articles)}")
for article in python_articles:
    print(f"  {article}")

# 2. 搜索包含多个关键词的文章（AND搜索）
ml_python_articles = list(filter(
    lambda article: 'machine learning' in article.lower() and 'python' in article.lower(), 
    articles
))
print(f"\n包含'machine learning'和'Python'的文章: {len(ml_python_articles)}")

# 3. 搜索包含任一关键词的文章（OR搜索）
tech_articles = list(filter(
    lambda article: any(keyword in article.lower() for keyword in ['python', 'javascript', 'database']), 
    articles
))
print(f"\n包含技术关键词的文章数量: {len(tech_articles)}")

# 4. 筛选长度适中的文章（30-60字符）
medium_length = list(filter(lambda article: 30 <= len(article) <= 60, articles))
print(f"\n中等长度文章数量: {len(medium_length)}")

# 5. 筛选单词数量在特定范围的文章
word_count_filter = list(filter(lambda article: 5 <= len(article.split()) <= 8, articles))
print(f"5-8个单词的文章数量: {len(word_count_filter)}")
```

## 最佳实践

### 何时使用filter + lambda

```python
# ✅ 适合使用filter + lambda的场景

# 1. 简单的条件筛选
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # 简洁明了

# 2. 基于属性的筛选
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
adults = list(filter(lambda person: person['age'] >= 18, people))

# 3. 字符串模式匹配
files = ['doc.txt', 'image.jpg', 'script.py']
text_files = list(filter(lambda f: f.endswith('.txt'), files))

# 4. 数值范围筛选
scores = [85, 92, 78, 96, 88]
high_scores = list(filter(lambda score: score >= 90, scores))

print(f"适合的场景:")
print(f"偶数: {even_numbers}")
print(f"成年人: {len(adults)}")
print(f"文本文件: {text_files}")
print(f"高分: {high_scores}")
```

### 何时避免使用filter + lambda

```python
# ❌ 不适合使用filter + lambda的场景

# 1. 复杂的条件逻辑 - 应该使用普通函数
def complex_validation(user):
    """复杂的用户验证"""
    # 多重条件检查
    if not user.get('name', '').strip():
        return False
    
    age = user.get('age', 0)
    if not (18 <= age <= 100):
        return False
    
    email = user.get('email', '')
    if '@' not in email or '.' not in email:
        return False
    
    return True

users = [
    {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'},
    {'name': '', 'age': 30, 'email': 'invalid'},
    {'name': 'Bob', 'age': 150, 'email': 'bob@test.com'},
]

# 好的做法：使用普通函数
valid_users = list(filter(complex_validation, users))

# 2. 需要错误处理的情况
def safe_number_check(value):
    """安全的数字检查"""
    try:
        num = float(value)
        return 0 <= num <= 100
    except (ValueError, TypeError):
        return False

mixed_data = [50, '75', 'invalid', 25, None, '150']
valid_numbers = list(filter(safe_number_check, mixed_data))

# 3. 需要多个步骤的处理
def multi_step_filter(text):
    """多步骤文本过滤"""
    # 步骤1：检查类型
    if not isinstance(text, str):
        return False
    
    # 步骤2：清理空格
    cleaned = text.strip()
    if not cleaned:
        return False
    
    # 步骤3：检查长度
    if len(cleaned) < 3:
        return False
    
    # 步骤4：检查内容
    return cleaned.isalpha()

text_data = ['hello', '  ', 'ab', 'world123', '  valid  ', None]
filtered_texts = list(filter(multi_step_filter, text_data))

print(f"\n复杂场景处理:")
print(f"有效用户: {len(valid_users)}")
print(f"有效数字: {valid_numbers}")
print(f"过滤后文本: {filtered_texts}")
```

### 性能优化建议

```python
# 性能优化建议

# 1. 对于简单条件，考虑使用内置函数
data = [1, 2, 3, 4, 5, None, 6, 7, 8, None, 9, 10]

# 较慢：使用lambda
non_none_lambda = list(filter(lambda x: x is not None, data))

# 更快：使用内置函数（如果适用）
# 注意：filter(None, data) 会过滤所有假值，不只是None
non_falsy = list(filter(None, data))  # 过滤所有假值

# 对于只过滤None，还是需要lambda或函数
non_none_correct = list(filter(lambda x: x is not None, data))

print(f"过滤None: {non_none_correct}")
print(f"过滤假值: {non_falsy}")

# 2. 对于大数据集，考虑使用生成器
def filter_large_dataset(data, condition):
    """为大数据集创建过滤生成器"""
    return filter(condition, data)

large_data = range(1000000)
filtered_generator = filter_large_dataset(large_data, lambda x: x % 1000 == 0)

# 只在需要时消费数据
first_5_results = [next(filtered_generator) for _ in range(5)]
print(f"大数据集前5个结果: {first_5_results}")

# 3. 组合多个filter vs 单个复杂filter
test_numbers = list(range(1, 101))

# 方法1：多个简单filter
step1 = filter(lambda x: x % 2 == 0, test_numbers)  # 偶数
step2 = filter(lambda x: x > 20, step1)  # 大于20
step3 = filter(lambda x: x < 80, step2)  # 小于80
result_multi = list(step3)

# 方法2：单个复杂filter
result_single = list(filter(
    lambda x: x % 2 == 0 and 20 < x < 80, 
    test_numbers
))

print(f"多步过滤结果: {len(result_multi)}")
print(f"单步过滤结果: {len(result_single)}")
print(f"结果相同: {result_multi == result_single}")
```

## 运行代码

要运行本节的示例代码，请执行：

```bash
python3 04_lambda_with_filter.py
```

## 小结

Lambda表达式与filter函数的结合是数据筛选的强大工具。主要要点包括：

### 优势：
- 代码简洁，适合简单的条件筛选
- 惰性求值，节省内存和计算资源
- 函数式编程风格，代码更加声明式
- 可以轻松组合多个筛选条件

### 适用场景：
- 数值范围筛选
- 字符串模式匹配
- 数据清洗和验证
- 基于属性的对象筛选

### 注意事项：
- 复杂条件应使用普通函数
- 需要错误处理时要谨慎
- 记住将filter对象转换为列表
- 考虑性能和可读性的平衡

### 最佳实践：
- 简单条件使用Lambda
- 复杂逻辑使用普通函数
- 大数据集考虑惰性求值
- 适当组合多个筛选步骤

在下一节中，我们将学习Lambda表达式与reduce函数的结合使用。