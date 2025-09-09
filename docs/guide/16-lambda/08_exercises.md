# Lambda表达式综合练习

本节提供了一系列由浅入深的练习题，帮助你巩固和深化对Lambda表达式的理解。每个练习都包含问题描述、解决方案和详细解释。

## 基础练习

### 练习1：基本Lambda操作

```python
# 练习1：创建基本的Lambda函数
print("=== 练习1：基本Lambda操作 ===")

# 1.1 创建一个Lambda函数，计算两个数的和
add = lambda x, y: x + y
print(f"add(3, 5) = {add(3, 5)}")  # 8

# 1.2 创建一个Lambda函数，判断数字是否为偶数
is_even = lambda x: x % 2 == 0
print(f"is_even(4) = {is_even(4)}")  # True
print(f"is_even(7) = {is_even(7)}")  # False

# 1.3 创建一个Lambda函数，返回三个数中的最大值
max_of_three = lambda a, b, c: max(a, max(b, c))
print(f"max_of_three(3, 7, 5) = {max_of_three(3, 7, 5)}")  # 7

# 1.4 创建一个Lambda函数，计算字符串长度
string_length = lambda s: len(s)
print(f"string_length('Hello') = {string_length('Hello')}")  # 5

# 1.5 创建一个Lambda函数，将摄氏度转换为华氏度
celsius_to_fahrenheit = lambda c: c * 9/5 + 32
print(f"25°C = {celsius_to_fahrenheit(25)}°F")  # 77.0
```

### 练习2：Lambda与内置函数

```python
# 练习2：Lambda与map、filter、reduce的结合使用
print("\n=== 练习2：Lambda与内置函数 ===")

from functools import reduce

# 2.1 使用map和Lambda将列表中的每个数字平方
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(f"原数字: {numbers}")
print(f"平方后: {squares}")

# 2.2 使用filter和Lambda筛选出大于10的数字
data = [5, 12, 8, 15, 3, 20, 7]
greater_than_10 = list(filter(lambda x: x > 10, data))
print(f"原数据: {data}")
print(f"大于10的数: {greater_than_10}")

# 2.3 使用reduce和Lambda计算列表中所有数字的乘积
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(f"1到5的乘积: {product}")  # 120

# 2.4 组合使用：找出偶数，平方后求和
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(1, 11)))
)
print(f"1-10中偶数的平方和: {result}")  # 2²+4²+6²+8²+10² = 220

# 2.5 使用Lambda对字符串列表按长度排序
words = ['python', 'java', 'c', 'javascript', 'go']
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"按长度排序: {sorted_by_length}")
```

### 练习3：复杂数据结构处理

```python
# 练习3：处理复杂数据结构
print("\n=== 练习3：复杂数据结构处理 ===")

# 3.1 学生成绩处理
students = [
    {'name': 'Alice', 'age': 20, 'scores': [85, 90, 78, 92]},
    {'name': 'Bob', 'age': 22, 'scores': [88, 85, 90, 87]},
    {'name': 'Charlie', 'age': 19, 'scores': [92, 88, 85, 90]},
    {'name': 'Diana', 'age': 21, 'scores': [78, 82, 88, 85]}
]

# 计算每个学生的平均分
average_scores = list(map(
    lambda student: {
        'name': student['name'],
        'average': sum(student['scores']) / len(student['scores'])
    },
    students
))

print("学生平均分:")
for student in average_scores:
    print(f"  {student['name']}: {student['average']:.1f}")

# 找出平均分最高的学生
top_student = max(average_scores, key=lambda x: x['average'])
print(f"最高平均分: {top_student['name']} ({top_student['average']:.1f})")

# 筛选出平均分大于85的学生
high_performers = list(filter(
    lambda student: sum(student['scores']) / len(student['scores']) > 85,
    students
))

print(f"高分学生: {[s['name'] for s in high_performers]}")

# 3.2 商品数据处理
products = [
    {'name': '笔记本电脑', 'price': 5999, 'category': '电子产品', 'stock': 15},
    {'name': '手机', 'price': 3999, 'category': '电子产品', 'stock': 25},
    {'name': '书籍', 'price': 29, 'category': '图书', 'stock': 100},
    {'name': '耳机', 'price': 299, 'category': '电子产品', 'stock': 50},
    {'name': '键盘', 'price': 199, 'category': '电子产品', 'stock': 30}
]

# 按价格排序
sorted_by_price = sorted(products, key=lambda x: x['price'], reverse=True)
print("\n按价格排序（从高到低）:")
for product in sorted_by_price:
    print(f"  {product['name']}: ¥{product['price']}")

# 筛选电子产品并计算总价值
electronics = list(filter(lambda x: x['category'] == '电子产品', products))
total_electronics_value = sum(map(lambda x: x['price'] * x['stock'], electronics))
print(f"\n电子产品总库存价值: ¥{total_electronics_value:,}")

# 找出库存最少的商品
min_stock_product = min(products, key=lambda x: x['stock'])
print(f"库存最少的商品: {min_stock_product['name']} (库存: {min_stock_product['stock']})")
```

## 中级练习

### 练习4：函数式编程模式

```python
# 练习4：函数式编程模式
print("\n=== 练习4：函数式编程模式 ===")

# 4.1 函数组合
compose = lambda f, g: lambda x: f(g(x))

# 创建基础函数
add_one = lambda x: x + 1
multiply_by_two = lambda x: x * 2
square = lambda x: x ** 2

# 组合函数
add_then_multiply = compose(multiply_by_two, add_one)
multiply_then_square = compose(square, multiply_by_two)

print(f"add_then_multiply(5) = {add_then_multiply(5)}")  # (5+1)*2 = 12
print(f"multiply_then_square(3) = {multiply_then_square(3)}")  # (3*2)² = 36

# 4.2 柯里化
curry_add = lambda x: lambda y: x + y
curry_multiply = lambda x: lambda y: lambda z: x * y * z

add_10 = curry_add(10)
multiply_2_3 = curry_multiply(2)(3)

print(f"add_10(5) = {add_10(5)}")  # 15
print(f"multiply_2_3(4) = {multiply_2_3(4)}")  # 24

# 4.3 管道操作
def pipe(*functions):
    return lambda x: reduce(lambda acc, f: f(acc), functions, x)

# 创建处理管道
process_pipeline = pipe(
    lambda x: x + 1,      # 加1
    lambda x: x * 2,      # 乘2
    lambda x: x ** 2,     # 平方
    lambda x: x - 5       # 减5
)

result = process_pipeline(3)  # ((3+1)*2)²-5 = 64-5 = 59
print(f"管道处理3: {result}")

# 4.4 条件函数
cond = lambda predicate, true_func, false_func: lambda x: true_func(x) if predicate(x) else false_func(x)

# 处理正负数
process_number = cond(
    lambda x: x >= 0,
    lambda x: x ** 2,     # 正数平方
    lambda x: abs(x) * 2  # 负数取绝对值乘2
)

print(f"处理5: {process_number(5)}")    # 25
print(f"处理-3: {process_number(-3)}")  # 6

# 4.5 递归模式（使用Y组合子）
Y = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))

# 递归阶乘
factorial = Y(lambda f: lambda n: 1 if n <= 1 else n * f(n - 1))
print(f"factorial(5) = {factorial(5)}")  # 120

# 递归斐波那契
fibonacci = Y(lambda f: lambda n: n if n <= 1 else f(n-1) + f(n-2))
print(f"fibonacci(8) = {fibonacci(8)}")  # 21
```

### 练习5：数据分析任务

```python
# 练习5：数据分析任务
print("\n=== 练习5：数据分析任务 ===")

# 5.1 销售数据分析
sales_data = [
    {'date': '2024-01-01', 'product': 'A', 'amount': 1200, 'quantity': 10},
    {'date': '2024-01-01', 'product': 'B', 'amount': 800, 'quantity': 5},
    {'date': '2024-01-02', 'product': 'A', 'amount': 1500, 'quantity': 12},
    {'date': '2024-01-02', 'product': 'C', 'amount': 600, 'quantity': 8},
    {'date': '2024-01-03', 'product': 'B', 'amount': 1000, 'quantity': 6},
    {'date': '2024-01-03', 'product': 'C', 'amount': 750, 'quantity': 10}
]

# 计算总销售额
total_sales = sum(map(lambda x: x['amount'], sales_data))
print(f"总销售额: ¥{total_sales:,}")

# 按产品分组计算销售额
from itertools import groupby

# 按产品排序后分组
sorted_by_product = sorted(sales_data, key=lambda x: x['product'])
product_sales = {
    product: sum(map(lambda x: x['amount'], list(group)))
    for product, group in groupby(sorted_by_product, key=lambda x: x['product'])
}

print("\n各产品销售额:")
for product, amount in product_sales.items():
    print(f"  产品{product}: ¥{amount:,}")

# 找出销售额最高的产品
best_product = max(product_sales.items(), key=lambda x: x[1])
print(f"销售额最高的产品: {best_product[0]} (¥{best_product[1]:,})")

# 计算平均单价
average_prices = list(map(
    lambda x: {
        'product': x['product'],
        'avg_price': x['amount'] / x['quantity']
    },
    sales_data
))

print("\n各笔交易的平均单价:")
for item in average_prices:
    print(f"  产品{item['product']}: ¥{item['avg_price']:.2f}")

# 5.2 文本数据处理
text_data = [
    "Python是一种高级编程语言",
    "Lambda表达式使代码更简洁",
    "函数式编程是一种编程范式",
    "数据分析需要处理大量数据",
    "机器学习使用Python很流行"
]

# 统计每句话的字数
word_counts = list(map(lambda x: len(x), text_data))
print(f"\n每句话的字数: {word_counts}")

# 找出最长和最短的句子
longest = max(text_data, key=lambda x: len(x))
shortest = min(text_data, key=lambda x: len(x))
print(f"最长句子: {longest} ({len(longest)}字)")
print(f"最短句子: {shortest} ({len(shortest)}字)")

# 筛选包含"Python"的句子
python_sentences = list(filter(lambda x: 'Python' in x, text_data))
print(f"包含'Python'的句子: {len(python_sentences)}句")
for sentence in python_sentences:
    print(f"  {sentence}")

# 统计所有句子的总字数
total_chars = sum(map(lambda x: len(x), text_data))
average_chars = total_chars / len(text_data)
print(f"总字数: {total_chars}, 平均字数: {average_chars:.1f}")
```

### 练习6：算法实现

```python
# 练习6：使用Lambda实现经典算法
print("\n=== 练习6：算法实现 ===")

# 6.1 快速排序
quicksort = Y(lambda f: lambda lst: 
    lst if len(lst) <= 1 else 
    f([x for x in lst[1:] if x <= lst[0]]) + [lst[0]] + f([x for x in lst[1:] if x > lst[0]])
)

unsorted_list = [3, 6, 8, 10, 1, 2, 1, 5, 7, 4]
sorted_list = quicksort(unsorted_list)
print(f"快速排序: {unsorted_list} -> {sorted_list}")

# 6.2 二分查找
def binary_search_lambda(arr, target):
    search = Y(lambda f: lambda low, high: 
        -1 if low > high else
        (lambda mid: 
            mid if arr[mid] == target else
            f(low, mid - 1) if arr[mid] > target else
            f(mid + 1, high)
        )((low + high) // 2)
    )
    return search(0, len(arr) - 1)

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
index = binary_search_lambda(sorted_array, target)
print(f"二分查找{target}在{sorted_array}中的位置: {index}")

# 6.3 最大公约数（欧几里得算法）
gcd = Y(lambda f: lambda a, b: a if b == 0 else f(b, a % b))
print(f"gcd(48, 18) = {gcd(48, 18)}")  # 6
print(f"gcd(100, 25) = {gcd(100, 25)}")  # 25

# 6.4 汉诺塔问题
def hanoi_lambda(n, source, target, auxiliary):
    hanoi = Y(lambda f: lambda n, src, tgt, aux: 
        [(src, tgt)] if n == 1 else
        f(n-1, src, aux, tgt) + [(src, tgt)] + f(n-1, aux, tgt, src)
    )
    return hanoi(n, source, target, auxiliary)

moves = hanoi_lambda(3, 'A', 'C', 'B')
print(f"\n汉诺塔3层解法 (A->C):")
for i, (from_peg, to_peg) in enumerate(moves, 1):
    print(f"  步骤{i}: {from_peg} -> {to_peg}")

# 6.5 帕斯卡三角形
def pascal_triangle(n):
    generate_row = lambda prev_row: [1] + [
        prev_row[i] + prev_row[i+1] for i in range(len(prev_row)-1)
    ] + [1] if prev_row else [1]
    
    triangle = []
    current_row = []
    for i in range(n):
        current_row = generate_row(current_row)
        triangle.append(current_row[:])
    
    return triangle

triangle = pascal_triangle(6)
print("\n帕斯卡三角形 (前6行):")
for i, row in enumerate(triangle):
    spaces = ' ' * (6 - i)
    row_str = ' '.join(map(str, row))
    print(f"{spaces}{row_str}")
```

## 高级练习

### 练习7：设计模式实现

```python
# 练习7：使用Lambda实现设计模式
print("\n=== 练习7：设计模式实现 ===")

# 7.1 策略模式
class Calculator:
    def __init__(self):
        self.strategies = {
            'add': lambda x, y: x + y,
            'subtract': lambda x, y: x - y,
            'multiply': lambda x, y: x * y,
            'divide': lambda x, y: x / y if y != 0 else float('inf'),
            'power': lambda x, y: x ** y,
            'mod': lambda x, y: x % y if y != 0 else 0
        }
    
    def calculate(self, operation, x, y):
        return self.strategies.get(operation, lambda x, y: 0)(x, y)

calc = Calculator()
print(f"10 + 5 = {calc.calculate('add', 10, 5)}")
print(f"10 - 5 = {calc.calculate('subtract', 10, 5)}")
print(f"10 * 5 = {calc.calculate('multiply', 10, 5)}")
print(f"10 / 5 = {calc.calculate('divide', 10, 5)}")
print(f"10 ^ 5 = {calc.calculate('power', 10, 5)}")

# 7.2 观察者模式
class EventManager:
    def __init__(self):
        self.listeners = {}
    
    def subscribe(self, event_type, callback):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(callback)
    
    def notify(self, event_type, data):
        if event_type in self.listeners:
            for callback in self.listeners[event_type]:
                callback(data)

# 使用Lambda作为事件处理器
event_manager = EventManager()

# 订阅事件
event_manager.subscribe('user_login', lambda user: print(f"用户 {user} 已登录"))
event_manager.subscribe('user_login', lambda user: print(f"发送欢迎邮件给 {user}"))
event_manager.subscribe('user_logout', lambda user: print(f"用户 {user} 已登出"))

# 触发事件
print("\n触发登录事件:")
event_manager.notify('user_login', 'Alice')
print("\n触发登出事件:")
event_manager.notify('user_logout', 'Alice')

# 7.3 装饰器模式
def create_decorators():
    # 日志装饰器
    log_decorator = lambda func: lambda *args, **kwargs: (
        print(f"调用函数 {func.__name__} 参数: {args}"),
        func(*args, **kwargs)
    )[1]
    
    # 缓存装饰器
    def cache_decorator(func):
        cache = {}
        return lambda *args: cache.setdefault(args, func(*args))
    
    # 重试装饰器
    def retry_decorator(max_attempts=3):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        if attempt == max_attempts - 1:
                            raise e
                        print(f"尝试 {attempt + 1} 失败，重试中...")
            return wrapper
        return decorator
    
    return log_decorator, cache_decorator, retry_decorator

log_dec, cache_dec, retry_dec = create_decorators()

# 应用装饰器
@log_dec
@cache_dec
def expensive_calculation(n):
    print(f"执行复杂计算: {n}")
    return n ** 2 + n * 10

print("\n装饰器测试:")
result1 = expensive_calculation(5)
result2 = expensive_calculation(5)  # 从缓存获取
print(f"结果: {result1}, {result2}")

# 7.4 工厂模式
create_shape_factory = lambda: {
    'circle': lambda radius: {'type': 'circle', 'area': lambda: 3.14159 * radius ** 2},
    'rectangle': lambda width, height: {'type': 'rectangle', 'area': lambda: width * height},
    'triangle': lambda base, height: {'type': 'triangle', 'area': lambda: 0.5 * base * height}
}

shape_factory = create_shape_factory()

# 创建不同形状
circle = shape_factory['circle'](5)
rectangle = shape_factory['rectangle'](4, 6)
triangle = shape_factory['triangle'](3, 8)

print(f"\n形状面积计算:")
print(f"圆形面积: {circle['area']():.2f}")
print(f"矩形面积: {rectangle['area']():.2f}")
print(f"三角形面积: {triangle['area']():.2f}")
```

### 练习8：实际应用场景

```python
# 练习8：实际应用场景
print("\n=== 练习8：实际应用场景 ===")

# 8.1 数据验证系统
class DataValidator:
    def __init__(self):
        self.validators = {
            'required': lambda value: value is not None and value != '',
            'min_length': lambda min_len: lambda value: len(str(value)) >= min_len,
            'max_length': lambda max_len: lambda value: len(str(value)) <= max_len,
            'email': lambda value: '@' in str(value) and '.' in str(value),
            'numeric': lambda value: str(value).replace('.', '').replace('-', '').isdigit(),
            'range': lambda min_val, max_val: lambda value: min_val <= float(value) <= max_val
        }
    
    def validate(self, data, rules):
        errors = []
        for field, field_rules in rules.items():
            value = data.get(field)
            for rule in field_rules:
                if isinstance(rule, tuple):
                    rule_name, *params = rule
                    validator = self.validators[rule_name](*params)
                else:
                    validator = self.validators[rule]
                
                if not validator(value):
                    errors.append(f"{field}: 验证失败 ({rule})")
        
        return errors

# 测试数据验证
validator = DataValidator()

user_data = {
    'name': 'Alice',
    'email': 'alice@example.com',
    'age': 25,
    'password': '123456'
}

validation_rules = {
    'name': ['required', ('min_length', 2), ('max_length', 50)],
    'email': ['required', 'email'],
    'age': ['required', 'numeric', ('range', 0, 120)],
    'password': ['required', ('min_length', 6)]
}

errors = validator.validate(user_data, validation_rules)
if errors:
    print("验证错误:")
    for error in errors:
        print(f"  {error}")
else:
    print("数据验证通过")

# 8.2 配置管理系统
class ConfigManager:
    def __init__(self):
        self.config = {}
        self.transformers = {
            'int': lambda x: int(x),
            'float': lambda x: float(x),
            'bool': lambda x: x.lower() in ('true', '1', 'yes', 'on'),
            'list': lambda x: x.split(',') if isinstance(x, str) else x,
            'upper': lambda x: str(x).upper(),
            'lower': lambda x: str(x).lower()
        }
    
    def set(self, key, value, transform=None):
        if transform and transform in self.transformers:
            value = self.transformers[transform](value)
        self.config[key] = value
    
    def get(self, key, default=None, transform=None):
        value = self.config.get(key, default)
        if transform and transform in self.transformers:
            value = self.transformers[transform](value)
        return value
    
    def get_all(self, prefix='', transform_map=None):
        filtered = {k: v for k, v in self.config.items() if k.startswith(prefix)}
        if transform_map:
            for key, transform in transform_map.items():
                if key in filtered and transform in self.transformers:
                    filtered[key] = self.transformers[transform](filtered[key])
        return filtered

# 测试配置管理
config = ConfigManager()

# 设置配置
config.set('app_name', 'MyApp')
config.set('debug', 'true', 'bool')
config.set('port', '8080', 'int')
config.set('allowed_hosts', 'localhost,127.0.0.1', 'list')
config.set('log_level', 'info', 'upper')

print("\n配置管理测试:")
print(f"应用名称: {config.get('app_name')}")
print(f"调试模式: {config.get('debug')}")
print(f"端口: {config.get('port')}")
print(f"允许的主机: {config.get('allowed_hosts')}")
print(f"日志级别: {config.get('log_level')}")

# 8.3 简单的查询构建器
class QueryBuilder:
    def __init__(self, table):
        self.table = table
        self.conditions = []
        self.order_by_clause = ''
        self.limit_clause = ''
    
    def where(self, condition):
        self.conditions.append(condition)
        return self
    
    def order_by(self, field, direction='ASC'):
        self.order_by_clause = f" ORDER BY {field} {direction}"
        return self
    
    def limit(self, count):
        self.limit_clause = f" LIMIT {count}"
        return self
    
    def build(self):
        query = f"SELECT * FROM {self.table}"
        if self.conditions:
            where_clause = " AND ".join(self.conditions)
            query += f" WHERE {where_clause}"
        query += self.order_by_clause + self.limit_clause
        return query

# 创建查询条件生成器
create_condition = {
    'eq': lambda field, value: f"{field} = '{value}'",
    'gt': lambda field, value: f"{field} > {value}",
    'lt': lambda field, value: f"{field} < {value}",
    'like': lambda field, pattern: f"{field} LIKE '%{pattern}%'",
    'in': lambda field, values: f"{field} IN ({','.join(map(str, values))})"
}

# 构建查询
query = (QueryBuilder('users')
         .where(create_condition['gt']('age', 18))
         .where(create_condition['like']('name', 'John'))
         .where(create_condition['in']('status', ['active', 'pending']))
         .order_by('created_at', 'DESC')
         .limit(10)
         .build())

print(f"\n生成的SQL查询:")
print(query)

# 8.4 事件驱动的状态机
class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.transitions = {}
        self.state_handlers = {}
    
    def add_transition(self, from_state, event, to_state, condition=None):
        key = (from_state, event)
        self.transitions[key] = {
            'to_state': to_state,
            'condition': condition or (lambda: True)
        }
    
    def add_state_handler(self, state, handler):
        self.state_handlers[state] = handler
    
    def trigger(self, event, context=None):
        key = (self.current_state, event)
        if key in self.transitions:
            transition = self.transitions[key]
            if transition['condition']():
                old_state = self.current_state
                self.current_state = transition['to_state']
                
                # 执行状态处理器
                if self.current_state in self.state_handlers:
                    self.state_handlers[self.current_state](context)
                
                return f"状态从 {old_state} 转换到 {self.current_state}"
        
        return f"无效的状态转换: {self.current_state} -> {event}"

# 创建订单状态机
order_sm = StateMachine('pending')

# 添加状态转换
order_sm.add_transition('pending', 'pay', 'paid')
order_sm.add_transition('paid', 'ship', 'shipped')
order_sm.add_transition('shipped', 'deliver', 'delivered')
order_sm.add_transition('delivered', 'return', 'returned')
order_sm.add_transition('paid', 'cancel', 'cancelled')

# 添加状态处理器（使用Lambda）
order_sm.add_state_handler('paid', lambda ctx: print(f"订单 {ctx['order_id']} 已支付，准备发货"))
order_sm.add_state_handler('shipped', lambda ctx: print(f"订单 {ctx['order_id']} 已发货，物流单号: {ctx.get('tracking_id', 'N/A')}"))
order_sm.add_state_handler('delivered', lambda ctx: print(f"订单 {ctx['order_id']} 已送达"))

# 测试状态机
print("\n订单状态机测试:")
order_context = {'order_id': 'ORD001', 'tracking_id': 'TRK123456'}

print(f"当前状态: {order_sm.current_state}")
print(order_sm.trigger('pay', order_context))
print(order_sm.trigger('ship', order_context))
print(order_sm.trigger('deliver', order_context))
print(f"最终状态: {order_sm.current_state}")
```

## 挑战练习

### 练习9：性能优化挑战

```python
# 练习9：性能优化挑战
print("\n=== 练习9：性能优化挑战 ===")

import time
import functools
from collections import defaultdict

# 9.1 缓存优化
class SmartCache:
    def __init__(self, max_size=100, ttl=300):
        self.max_size = max_size
        self.ttl = ttl
        self.cache = {}
        self.access_times = {}
        self.creation_times = {}
    
    def get_or_compute(self, key, compute_func):
        current_time = time.time()
        
        # 检查缓存是否存在且未过期
        if (key in self.cache and 
            current_time - self.creation_times[key] < self.ttl):
            self.access_times[key] = current_time
            return self.cache[key]
        
        # 计算新值
        value = compute_func()
        
        # 如果缓存已满，移除最久未访问的项
        if len(self.cache) >= self.max_size:
            oldest_key = min(self.access_times.keys(), 
                           key=lambda k: self.access_times[k])
            del self.cache[oldest_key]
            del self.access_times[oldest_key]
            del self.creation_times[oldest_key]
        
        # 添加到缓存
        self.cache[key] = value
        self.access_times[key] = current_time
        self.creation_times[key] = current_time
        
        return value

# 使用智能缓存优化斐波那契计算
cache = SmartCache(max_size=50)

def fibonacci_optimized(n):
    return cache.get_or_compute(
        f'fib_{n}',
        lambda: 1 if n <= 1 else fibonacci_optimized(n-1) + fibonacci_optimized(n-2)
    )

# 性能测试
print("斐波那契性能测试:")
start_time = time.perf_counter()
result = fibonacci_optimized(30)
end_time = time.perf_counter()
print(f"fibonacci(30) = {result}, 耗时: {(end_time - start_time)*1000:.2f}ms")

# 9.2 批处理优化
class BatchProcessor:
    def __init__(self, batch_size=100, flush_interval=1.0):
        self.batch_size = batch_size
        self.flush_interval = flush_interval
        self.buffer = []
        self.last_flush = time.time()
        self.processors = {
            'sum': lambda batch: sum(batch),
            'avg': lambda batch: sum(batch) / len(batch) if batch else 0,
            'max': lambda batch: max(batch) if batch else None,
            'min': lambda batch: min(batch) if batch else None,
            'count': lambda batch: len(batch)
        }
    
    def add(self, item):
        self.buffer.append(item)
        current_time = time.time()
        
        # 检查是否需要刷新
        if (len(self.buffer) >= self.batch_size or 
            current_time - self.last_flush >= self.flush_interval):
            return self.flush()
        
        return None
    
    def flush(self):
        if not self.buffer:
            return None
        
        # 处理批次
        results = {name: processor(self.buffer) 
                  for name, processor in self.processors.items()}
        
        batch_size = len(self.buffer)
        self.buffer.clear()
        self.last_flush = time.time()
        
        return {'batch_size': batch_size, 'results': results}

# 测试批处理器
processor = BatchProcessor(batch_size=5)

print("\n批处理测试:")
for i in range(12):
    result = processor.add(i * 2 + 1)
    if result:
        print(f"批次处理结果: {result}")

# 处理剩余数据
final_result = processor.flush()
if final_result:
    print(f"最终批次结果: {final_result}")

# 9.3 内存优化的数据处理
def create_memory_efficient_processor():
    # 使用生成器避免创建大型中间列表
    filter_transform_reduce = lambda data, filter_func, transform_func, reduce_func: \
        reduce_func(map(transform_func, filter(filter_func, data)))
    
    # 分块处理大数据
    def chunk_processor(data, chunk_size=1000):
        for i in range(0, len(data), chunk_size):
            yield data[i:i + chunk_size]
    
    # 流式处理
    def stream_process(data_stream, *operations):
        result = data_stream
        for operation in operations:
            result = operation(result)
        return result
    
    return filter_transform_reduce, chunk_processor, stream_process

ftr, chunk_proc, stream_proc = create_memory_efficient_processor()

# 测试内存效率
large_data = range(100000)  # 模拟大数据集

# 内存高效的处理
result = ftr(
    large_data,
    lambda x: x % 2 == 0,  # 过滤偶数
    lambda x: x ** 2,      # 平方
    lambda gen: sum(gen)   # 求和
)

print(f"\n大数据处理结果: {result}")

# 分块处理示例
chunk_results = []
for chunk in chunk_proc(list(range(25)), chunk_size=5):
    chunk_sum = sum(chunk)
    chunk_results.append(chunk_sum)
    print(f"块处理: {chunk} -> 和: {chunk_sum}")

print(f"所有块的总和: {sum(chunk_results)}")
```

### 练习10：综合项目

```python
# 练习10：综合项目 - 简单的数据分析引擎
print("\n=== 练习10：数据分析引擎 ===")

class DataAnalysisEngine:
    def __init__(self):
        # 数据转换函数
        self.transformers = {
            'normalize': lambda data: [(x - min(data)) / (max(data) - min(data)) for x in data],
            'standardize': lambda data: [(x - sum(data)/len(data)) / (sum([(x - sum(data)/len(data))**2 for x in data])/len(data))**0.5 for x in data],
            'log': lambda data: [__import__('math').log(x) if x > 0 else 0 for x in data],
            'square': lambda data: [x**2 for x in data],
            'sqrt': lambda data: [x**0.5 if x >= 0 else 0 for x in data]
        }
        
        # 聚合函数
        self.aggregators = {
            'sum': lambda data: sum(data),
            'mean': lambda data: sum(data) / len(data) if data else 0,
            'median': lambda data: sorted(data)[len(data)//2] if data else 0,
            'mode': lambda data: max(set(data), key=data.count) if data else None,
            'std': lambda data: (sum([(x - sum(data)/len(data))**2 for x in data]) / len(data))**0.5 if data else 0,
            'var': lambda data: sum([(x - sum(data)/len(data))**2 for x in data]) / len(data) if data else 0,
            'min': lambda data: min(data) if data else None,
            'max': lambda data: max(data) if data else None,
            'range': lambda data: max(data) - min(data) if data else 0,
            'count': lambda data: len(data)
        }
        
        # 过滤函数
        self.filters = {
            'positive': lambda data: [x for x in data if x > 0],
            'negative': lambda data: [x for x in data if x < 0],
            'even': lambda data: [x for x in data if x % 2 == 0],
            'odd': lambda data: [x for x in data if x % 2 != 0],
            'outliers': lambda data: self._remove_outliers(data),
            'top_n': lambda n: lambda data: sorted(data, reverse=True)[:n],
            'bottom_n': lambda n: lambda data: sorted(data)[:n],
            'range_filter': lambda min_val, max_val: lambda data: [x for x in data if min_val <= x <= max_val]
        }
    
    def _remove_outliers(self, data):
        if len(data) < 4:
            return data
        
        sorted_data = sorted(data)
        q1_idx = len(sorted_data) // 4
        q3_idx = 3 * len(sorted_data) // 4
        q1 = sorted_data[q1_idx]
        q3 = sorted_data[q3_idx]
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        return [x for x in data if lower_bound <= x <= upper_bound]
    
    def analyze(self, data, operations):
        """执行一系列数据分析操作"""
        result = data[:]
        analysis_log = []
        
        for operation in operations:
            op_type = operation['type']
            op_name = operation['name']
            op_params = operation.get('params', [])
            
            if op_type == 'transform':
                if op_name in self.transformers:
                    result = self.transformers[op_name](result)
                    analysis_log.append(f"应用转换: {op_name}")
            
            elif op_type == 'filter':
                if op_name in self.filters:
                    filter_func = self.filters[op_name]
                    if op_params:
                        filter_func = filter_func(*op_params)
                    result = filter_func(result)
                    analysis_log.append(f"应用过滤: {op_name} {op_params}")
            
            elif op_type == 'aggregate':
                if op_name in self.aggregators:
                    agg_result = self.aggregators[op_name](result)
                    analysis_log.append(f"聚合计算: {op_name} = {agg_result}")
                    return {
                        'result': agg_result,
                        'processed_data': result,
                        'log': analysis_log
                    }
        
        return {
            'result': result,
            'processed_data': result,
            'log': analysis_log
        }
    
    def batch_analyze(self, datasets, operations):
        """批量分析多个数据集"""
        results = {}
        for name, data in datasets.items():
            results[name] = self.analyze(data, operations)
        return results
    
    def compare_datasets(self, datasets, metrics):
        """比较多个数据集的指标"""
        comparison = {}
        for metric in metrics:
            comparison[metric] = {}
            for name, data in datasets.items():
                if metric in self.aggregators:
                    comparison[metric][name] = self.aggregators[metric](data)
        return comparison

# 创建分析引擎
engine = DataAnalysisEngine()

# 测试数据
test_datasets = {
    'sales_q1': [120, 150, 180, 200, 175, 160, 140, 190, 210, 185],
    'sales_q2': [180, 200, 220, 240, 210, 195, 175, 230, 250, 225],
    'sales_q3': [200, 180, 160, 140, 120, 100, 80, 90, 110, 130],
    'sales_q4': [250, 280, 300, 320, 290, 270, 260, 310, 330, 295]
}

# 定义分析操作
analysis_operations = [
    {'type': 'filter', 'name': 'outliers'},
    {'type': 'transform', 'name': 'normalize'},
    {'type': 'aggregate', 'name': 'mean'}
]

# 执行批量分析
print("季度销售数据分析:")
batch_results = engine.batch_analyze(test_datasets, analysis_operations)

for quarter, result in batch_results.items():
    print(f"\n{quarter}:")
    print(f"  标准化后的平均值: {result['result']:.4f}")
    for log_entry in result['log']:
        print(f"  {log_entry}")

# 比较数据集
comparison_metrics = ['mean', 'std', 'min', 'max', 'range']
comparison = engine.compare_datasets(test_datasets, comparison_metrics)

print("\n数据集比较:")
for metric, values in comparison.items():
    print(f"\n{metric.upper()}:")
    for dataset, value in values.items():
        print(f"  {dataset}: {value:.2f}")

# 高级分析示例
advanced_operations = [
    {'type': 'filter', 'name': 'range_filter', 'params': [100, 300]},
    {'type': 'transform', 'name': 'log'},
    {'type': 'filter', 'name': 'top_n', 'params': [5]},
    {'type': 'aggregate', 'name': 'std'}
]

print("\n高级分析示例 (Q4数据):")
advanced_result = engine.analyze(test_datasets['sales_q4'], advanced_operations)
print(f"结果: {advanced_result['result']:.4f}")
print("处理步骤:")
for log_entry in advanced_result['log']:
    print(f"  {log_entry}")

print("\n=== 所有练习完成 ===")
print("\n恭喜！你已经完成了Lambda表达式的所有练习。")
print("通过这些练习，你应该已经掌握了：")
print("1. Lambda表达式的基础语法和用法")
print("2. Lambda与内置函数的结合使用")
print("3. 函数式编程的核心概念")
print("4. Lambda在实际项目中的应用")
print("5. 性能优化和最佳实践")
print("\n继续练习和探索，成为Lambda表达式的专家！")
```

## 练习总结

### 学习成果检验

通过完成这些练习，你应该能够：

1. **熟练使用Lambda表达式的基本语法**
2. **理解Lambda与普通函数的区别和适用场景**
3. **掌握Lambda与map、filter、reduce等函数的结合使用**
4. **应用函数式编程的核心概念**
5. **在实际项目中合理使用Lambda表达式**
6. **优化Lambda表达式的性能**
7. **遵循Lambda表达式的最佳实践**

### 进阶学习建议

1. **深入学习函数式编程**：探索更多函数式编程概念
2. **研究其他语言的Lambda**：比较Python与其他语言的Lambda实现
3. **性能分析**：学习如何分析和优化Lambda表达式的性能
4. **设计模式**：学习如何在设计模式中使用Lambda表达式
5. **异步编程**：探索Lambda在异步编程中的应用

### 实践项目建议

1. **数据处理管道**：构建复杂的数据处理流水线
2. **配置系统**：开发灵活的配置管理系统
3. **事件系统**：实现基于Lambda的事件驱动架构
4. **DSL设计**：使用Lambda创建领域特定语言
5. **函数式工具库**：开发自己的函数式编程工具集

## 运行代码

将代码保存为Python文件并运行：

```bash
python3 08_exercises.py
```

建议按顺序完成所有练习，每完成一个练习后思考和总结学到的知识点。可以尝试修改练习中的参数和逻辑，加深对Lambda表达式的理解。