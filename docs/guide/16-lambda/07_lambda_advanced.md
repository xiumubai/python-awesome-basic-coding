# Lambda高级用法

Lambda表达式虽然语法简洁，但在高级应用中可以实现非常强大的功能。本节将深入探讨Lambda表达式的高级用法，包括闭包、装饰器、函数式编程模式等。

## 闭包与Lambda

### 基础闭包概念

```python
# 闭包的基本概念

def outer_function(x):
    """外部函数"""
    def inner_function(y):
        """内部函数，形成闭包"""
        return x + y
    return inner_function

# 使用普通函数创建闭包
add_10 = outer_function(10)
print(f"add_10(5) = {add_10(5)}")  # 输出: 15

# 使用Lambda创建闭包
create_adder = lambda x: lambda y: x + y
add_20 = create_adder(20)
print(f"add_20(5) = {add_20(5)}")  # 输出: 25

# 更复杂的闭包示例
create_multiplier = lambda factor: lambda value: value * factor
double = create_multiplier(2)
triple = create_multiplier(3)

print(f"double(7) = {double(7)}")  # 输出: 14
print(f"triple(7) = {triple(7)}")  # 输出: 21

# 闭包中的状态保持
def create_counter():
    count = [0]  # 使用列表来保持可变状态
    return lambda: count.__setitem__(0, count[0] + 1) or count[0]

counter1 = create_counter()
counter2 = create_counter()

print(f"counter1: {counter1()}, {counter1()}, {counter1()}")  # 1, 2, 3
print(f"counter2: {counter2()}, {counter2()}")  # 1, 2
```

### 闭包的实际应用

```python
# 配置函数生成器
create_validator = lambda min_val, max_val: lambda x: min_val <= x <= max_val

# 创建不同的验证器
age_validator = create_validator(0, 120)
percentage_validator = create_validator(0, 100)
temperature_validator = create_validator(-273, 1000)

print(f"年龄25有效: {age_validator(25)}")  # True
print(f"年龄150有效: {age_validator(150)}")  # False
print(f"百分比50有效: {percentage_validator(50)}")  # True
print(f"百分比150有效: {percentage_validator(150)}")  # False

# 事件处理器生成
create_event_handler = lambda event_type: lambda data: print(f"处理{event_type}事件: {data}")

click_handler = create_event_handler("点击")
hover_handler = create_event_handler("悬停")
keypress_handler = create_event_handler("按键")

click_handler("按钮A")  # 处理点击事件: 按钮A
hover_handler("菜单项")  # 处理悬停事件: 菜单项
keypress_handler("Enter")  # 处理按键事件: Enter

# 缓存函数生成器
def create_cached_function(func):
    cache = {}
    return lambda *args: cache.setdefault(args, func(*args))

# 创建缓存版本的函数
def expensive_calculation(n):
    print(f"计算 {n} 的平方...")
    return n ** 2

cached_calc = create_cached_function(expensive_calculation)

print(f"第一次调用: {cached_calc(5)}")  # 计算 5 的平方... 25
print(f"第二次调用: {cached_calc(5)}")  # 25 (从缓存获取)
print(f"第三次调用: {cached_calc(3)}")  # 计算 3 的平方... 9
```

## Lambda与装饰器

### 使用Lambda创建简单装饰器

```python
# 简单的装饰器模式
timing_decorator = lambda func: lambda *args, **kwargs: (
    __import__('time').perf_counter(),
    func(*args, **kwargs),
    print(f"{func.__name__} 执行时间: {__import__('time').perf_counter() - __import__('time').perf_counter():.4f}秒")
)[1]

# 注意：上面的装饰器有问题，下面是正确的实现
def create_timing_decorator():
    import time
    return lambda func: lambda *args, **kwargs: (
        lambda start_time: (
            func(*args, **kwargs),
            print(f"{func.__name__} 执行时间: {time.perf_counter() - start_time:.4f}秒")
        )[0]
    )(time.perf_counter())

timing_decorator = create_timing_decorator()

@timing_decorator
def slow_function():
    import time
    time.sleep(0.1)
    return "完成"

result = slow_function()
print(f"结果: {result}")

# 日志装饰器
log_decorator = lambda prefix: lambda func: lambda *args, **kwargs: (
    print(f"{prefix}: 调用 {func.__name__} 参数: {args}, {kwargs}"),
    func(*args, **kwargs)
)[1]

@log_decorator("DEBUG")
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(f"结果: {result}")

# 重试装饰器
def create_retry_decorator(max_attempts=3):
    return lambda func: lambda *args, **kwargs: (
        lambda: [
            (lambda attempt: (
                func(*args, **kwargs) if attempt == 0 else None,
                print(f"第{attempt + 1}次尝试失败，重试中...") if attempt < max_attempts - 1 else print("所有尝试都失败了")
            )[0] if attempt == 0 else func(*args, **kwargs))(attempt)
            for attempt in range(max_attempts)
            if True  # 这里应该有异常处理逻辑
        ][-1]
    )()

# 更实用的重试装饰器实现
def retry_decorator(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"第{attempt + 1}次尝试失败: {e}，重试中...")
        return wrapper
    return decorator

@retry_decorator(3)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("随机失败")
    return "成功"

try:
    result = unreliable_function()
    print(f"最终结果: {result}")
except Exception as e:
    print(f"最终失败: {e}")
```

### 参数化装饰器

```python
# 使用Lambda创建参数化装饰器

# 权限检查装饰器
create_permission_decorator = lambda required_role: lambda func: lambda *args, **kwargs: (
    func(*args, **kwargs) if kwargs.get('user_role') == required_role 
    else print(f"权限不足，需要 {required_role} 权限")
)

admin_required = create_permission_decorator('admin')
user_required = create_permission_decorator('user')

@admin_required
def delete_user(user_id, user_role=None):
    return f"删除用户 {user_id}"

@user_required
def view_profile(user_id, user_role=None):
    return f"查看用户 {user_id} 的资料"

print(delete_user(123, user_role='admin'))  # 删除用户 123
print(delete_user(123, user_role='user'))   # 权限不足，需要 admin 权限
print(view_profile(123, user_role='user'))  # 查看用户 123 的资料

# 缓存装饰器
create_cache_decorator = lambda cache_size=100: (
    lambda cache: lambda func: lambda *args: (
        cache.setdefault(args, func(*args)) if len(cache) < cache_size
        else (cache.clear(), cache.setdefault(args, func(*args)))[1]
    )
)({})

cache_decorator = create_cache_decorator(50)

@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"fibonacci(10) = {fibonacci(10)}")
print(f"fibonacci(15) = {fibonacci(15)}")

# 频率限制装饰器
def create_rate_limit_decorator(calls_per_second=1):
    import time
    last_called = [0]
    
    return lambda func: lambda *args, **kwargs: (
        time.sleep(max(0, 1/calls_per_second - (time.time() - last_called[0]))),
        last_called.__setitem__(0, time.time()),
        func(*args, **kwargs)
    )[2]

rate_limit = create_rate_limit_decorator(2)  # 每秒最多2次调用

@rate_limit
def api_call(data):
    import time
    print(f"API调用: {data} at {time.strftime('%H:%M:%S')}")
    return f"处理 {data}"

# 测试频率限制
for i in range(5):
    result = api_call(f"数据{i}")
```

## 函数式编程模式

### 高阶函数组合

```python
# 函数组合
compose = lambda f, g: lambda x: f(g(x))
compose3 = lambda f, g, h: lambda x: f(g(h(x)))

# 基础函数
add_one = lambda x: x + 1
multiply_by_two = lambda x: x * 2
square = lambda x: x ** 2

# 组合函数
add_then_multiply = compose(multiply_by_two, add_one)
multiply_then_square = compose(square, multiply_by_two)
complex_operation = compose3(square, multiply_by_two, add_one)

print(f"add_then_multiply(5) = {add_then_multiply(5)}")  # (5+1)*2 = 12
print(f"multiply_then_square(3) = {multiply_then_square(3)}")  # (3*2)^2 = 36
print(f"complex_operation(4) = {complex_operation(4)}")  # ((4+1)*2)^2 = 100

# 管道操作
def pipe(*functions):
    return lambda x: __import__('functools').reduce(lambda acc, f: f(acc), functions, x)

# 使用管道
process_number = pipe(
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x - 10
)

print(f"pipe处理5: {process_number(5)}")  # ((5+1)*2)^2-10 = 134

# 条件函数组合
cond = lambda predicate, true_func, false_func: lambda x: true_func(x) if predicate(x) else false_func(x)

# 条件处理
process_even_odd = cond(
    lambda x: x % 2 == 0,
    lambda x: x // 2,      # 偶数除以2
    lambda x: x * 3 + 1    # 奇数乘3加1
)

print(f"处理偶数8: {process_even_odd(8)}")  # 4
print(f"处理奇数7: {process_even_odd(7)}")  # 22

# 函数列表应用
apply_all = lambda funcs: lambda x: [f(x) for f in funcs]

mathematical_operations = apply_all([
    lambda x: x + 10,
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x / 2
])

results = mathematical_operations(5)
print(f"对5应用所有操作: {results}")  # [15, 10, 25, 2.5]
```

### 柯里化和偏函数

```python
# 柯里化 (Currying)
curry2 = lambda f: lambda x: lambda y: f(x, y)
curry3 = lambda f: lambda x: lambda y: lambda z: f(x, y, z)

# 基础函数
def add(x, y):
    return x + y

def multiply(x, y, z):
    return x * y * z

# 柯里化版本
curried_add = curry2(add)
curried_multiply = curry3(multiply)

# 使用柯里化
add_5 = curried_add(5)
print(f"add_5(3) = {add_5(3)}")  # 8

multiply_by_2_and_3 = curried_multiply(2)(3)
print(f"multiply_by_2_and_3(4) = {multiply_by_2_and_3(4)}")  # 24

# 偏函数应用
partial = lambda func, *args: lambda *remaining_args: func(*(args + remaining_args))

# 创建偏函数
def greet(greeting, name, punctuation):
    return f"{greeting}, {name}{punctuation}"

say_hello = partial(greet, "Hello")
say_hello_excited = partial(greet, "Hello", punctuation="!")

print(say_hello("Alice", "."))  # Hello, Alice.
print(say_hello_excited("Bob"))  # Hello, Bob!

# 更复杂的偏函数示例
def calculate_discount(price, discount_rate, tax_rate, shipping):
    discounted = price * (1 - discount_rate)
    with_tax = discounted * (1 + tax_rate)
    return with_tax + shipping

# 为VIP客户创建专用计算函数
vip_calculator = partial(calculate_discount, discount_rate=0.2, tax_rate=0.08)
regular_calculator = partial(calculate_discount, discount_rate=0.1, tax_rate=0.08)

print(f"VIP客户100元商品: {vip_calculator(100, 5)}")  # 91.4
print(f"普通客户100元商品: {regular_calculator(100, 5)}")  # 102.2
```

### 函数式数据处理

```python
# 函数式数据处理管道

# 数据转换函数
filter_even = lambda data: filter(lambda x: x % 2 == 0, data)
filter_positive = lambda data: filter(lambda x: x > 0, data)
map_square = lambda data: map(lambda x: x ** 2, data)
map_double = lambda data: map(lambda x: x * 2, data)

# 聚合函数
sum_all = lambda data: sum(data)
max_value = lambda data: max(data) if data else None
min_value = lambda data: min(data) if data else None
average = lambda data: sum(data) / len(list(data)) if data else 0

# 数据处理管道
def create_pipeline(*operations):
    return lambda data: __import__('functools').reduce(
        lambda result, operation: operation(result), 
        operations, 
        data
    )

# 创建不同的处理管道
even_squares_pipeline = create_pipeline(
    filter_even,
    map_square,
    list  # 转换为列表
)

positive_doubles_sum_pipeline = create_pipeline(
    filter_positive,
    map_double,
    sum_all
)

# 测试数据
test_data = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]

even_squares = even_squares_pipeline(test_data)
positive_doubles_sum = positive_doubles_sum_pipeline(test_data)

print(f"原始数据: {test_data}")
print(f"偶数的平方: {even_squares}")
print(f"正数翻倍后的和: {positive_doubles_sum}")

# 复杂数据处理示例
students = [
    {'name': 'Alice', 'age': 20, 'grades': [85, 90, 78]},
    {'name': 'Bob', 'age': 22, 'grades': [92, 88, 95]},
    {'name': 'Charlie', 'age': 19, 'grades': [76, 82, 89]},
    {'name': 'Diana', 'age': 21, 'grades': [94, 87, 91]}
]

# 函数式数据分析
get_average_grade = lambda student: sum(student['grades']) / len(student['grades'])
filter_high_performers = lambda students: filter(lambda s: get_average_grade(s) >= 85, students)
map_student_summary = lambda students: map(
    lambda s: {
        'name': s['name'], 
        'age': s['age'], 
        'average': get_average_grade(s)
    }, 
    students
)

# 创建学生分析管道
student_analysis_pipeline = create_pipeline(
    filter_high_performers,
    map_student_summary,
    list
)

high_performers = student_analysis_pipeline(students)
print("\n高分学生分析:")
for student in high_performers:
    print(f"  {student['name']} (年龄{student['age']}): 平均分 {student['average']:.1f}")

# 分组和聚合
from itertools import groupby

# 按年龄分组
age_groups = groupby(
    sorted(students, key=lambda s: s['age']), 
    key=lambda s: s['age']
)

print("\n按年龄分组:")
for age, group in age_groups:
    group_list = list(group)
    avg_grade = sum(get_average_grade(s) for s in group_list) / len(group_list)
    print(f"  年龄{age}: {len(group_list)}人, 平均成绩 {avg_grade:.1f}")
```

## 递归与Lambda

### Lambda递归模式

```python
# Lambda递归的实现

# Y组合子（用于实现Lambda递归）
Y = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))

# 使用Y组合子实现阶乘
factorial_lambda = Y(lambda f: lambda n: 1 if n <= 1 else n * f(n - 1))

print(f"5! = {factorial_lambda(5)}")  # 120
print(f"7! = {factorial_lambda(7)}")  # 5040

# 使用Y组合子实现斐波那契
fibonacci_lambda = Y(lambda f: lambda n: n if n <= 1 else f(n-1) + f(n-2))

print(f"fibonacci(10) = {fibonacci_lambda(10)}")  # 55
print(f"fibonacci(15) = {fibonacci_lambda(15)}")  # 610

# 更简单的递归实现（使用默认参数技巧）
factorial_simple = (lambda f, n: 1 if n <= 1 else n * f(f, n-1))
print(f"简单递归5! = {factorial_simple(factorial_simple, 5)}")  # 120

# 列表递归处理
list_sum = Y(lambda f: lambda lst: 0 if not lst else lst[0] + f(lst[1:]))
print(f"列表求和 [1,2,3,4,5] = {list_sum([1,2,3,4,5])}")  # 15

list_max = Y(lambda f: lambda lst: lst[0] if len(lst) == 1 else max(lst[0], f(lst[1:])))
print(f"列表最大值 [3,7,2,9,1] = {list_max([3,7,2,9,1])}")  # 9

# 树结构递归
# 二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"

# 创建测试树
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 树的递归遍历
tree_sum = Y(lambda f: lambda node: 0 if not node else node.val + f(node.left) + f(node.right))
tree_height = Y(lambda f: lambda node: 0 if not node else 1 + max(f(node.left), f(node.right)))
tree_count = Y(lambda f: lambda node: 0 if not node else 1 + f(node.left) + f(node.right))

print(f"\n树的总和: {tree_sum(root)}")  # 15
print(f"树的高度: {tree_height(root)}")  # 3
print(f"树的节点数: {tree_count(root)}")  # 5
```

### 尾递归优化

```python
# 尾递归优化模式

# 传统递归（可能导致栈溢出）
def factorial_traditional(n):
    return 1 if n <= 1 else n * factorial_traditional(n - 1)

# 尾递归版本
def factorial_tail_recursive(n, acc=1):
    return acc if n <= 1 else factorial_tail_recursive(n - 1, n * acc)

# Lambda版本的尾递归
factorial_tail_lambda = Y(lambda f: lambda n, acc=1: acc if n <= 1 else f(n-1, n*acc))

print(f"尾递归阶乘10! = {factorial_tail_lambda(10)}")  # 3628800

# 尾递归斐波那契
fibonacci_tail = Y(lambda f: lambda n, a=0, b=1: a if n == 0 else f(n-1, b, a+b))

print(f"尾递归fibonacci(20) = {fibonacci_tail(20)}")  # 6765

# 列表反转（尾递归）
reverse_list = Y(lambda f: lambda lst, acc=[]: acc if not lst else f(lst[1:], [lst[0]] + acc))

original = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original)
print(f"反转列表 {original} -> {reversed_list}")

# 快速排序（尾递归风格）
def quicksort_functional(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[0]
    less = [x for x in lst[1:] if x <= pivot]
    greater = [x for x in lst[1:] if x > pivot]
    
    return quicksort_functional(less) + [pivot] + quicksort_functional(greater)

# Lambda版本的快速排序
quicksort_lambda = Y(lambda f: lambda lst: 
    lst if len(lst) <= 1 else 
    f([x for x in lst[1:] if x <= lst[0]]) + [lst[0]] + f([x for x in lst[1:] if x > lst[0]])
)

unsorted = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quicksort_lambda(unsorted)
print(f"快速排序 {unsorted} -> {sorted_list}")
```

## 异步Lambda和生成器

### Lambda与生成器

```python
# Lambda与生成器表达式

# 创建生成器的Lambda
create_range = lambda start, end, step=1: (x for x in range(start, end, step))
create_fibonacci = lambda: (a for a, b in __import__('itertools').accumulate(
    __import__('itertools').repeat(1), 
    lambda ab, _: (ab[1], ab[0] + ab[1]), 
    initial=(0, 1)
))

# 使用生成器
my_range = create_range(1, 10, 2)
print(f"自定义范围: {list(my_range)}")  # [1, 3, 5, 7, 9]

fib_gen = create_fibonacci()
fib_numbers = [next(fib_gen) for _ in range(10)]
print(f"斐波那契前10项: {fib_numbers}")

# 无限生成器
create_counter = lambda start=0, step=1: __import__('itertools').count(start, step)
create_cycle = lambda items: __import__('itertools').cycle(items)
create_repeat = lambda item, times=None: __import__('itertools').repeat(item, times)

# 使用无限生成器
counter = create_counter(10, 3)
print(f"计数器前5项: {[next(counter) for _ in range(5)]}")  # [10, 13, 16, 19, 22]

cycle_gen = create_cycle(['A', 'B', 'C'])
print(f"循环前8项: {[next(cycle_gen) for _ in range(8)]}")  # ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']

# 生成器组合
filter_gen = lambda predicate, gen: (x for x in gen if predicate(x))
map_gen = lambda func, gen: (func(x) for x in gen)
take_gen = lambda n, gen: (next(gen) for _ in range(n))

# 组合使用
numbers = create_range(1, 100)
even_numbers = filter_gen(lambda x: x % 2 == 0, numbers)
squared_evens = map_gen(lambda x: x ** 2, even_numbers)
first_5_squared_evens = list(take_gen(5, squared_evens))

print(f"前5个偶数的平方: {first_5_squared_evens}")  # [4, 16, 36, 64, 100]
```

### 异步Lambda模式

```python
# 异步编程中的Lambda应用

import asyncio
import time

# 异步任务创建器
create_async_task = lambda delay, result: asyncio.create_task(
    (lambda: asyncio.sleep(delay) or result)()
)

# 注意：上面的代码有问题，正确的异步Lambda实现：
async def create_delayed_result(delay, result):
    await asyncio.sleep(delay)
    return result

# 异步映射
async def async_map(func, items, max_concurrent=5):
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def bounded_func(item):
        async with semaphore:
            return await func(item)
    
    tasks = [bounded_func(item) for item in items]
    return await asyncio.gather(*tasks)

# 异步过滤
async def async_filter(predicate, items):
    results = await async_map(predicate, items)
    return [item for item, keep in zip(items, results) if keep]

# 使用示例
async def async_example():
    # 模拟异步操作
    async def slow_square(x):
        await asyncio.sleep(0.1)  # 模拟网络延迟
        return x ** 2
    
    async def is_even_async(x):
        await asyncio.sleep(0.05)  # 模拟异步检查
        return x % 2 == 0
    
    numbers = list(range(1, 11))
    
    print("开始异步处理...")
    start_time = time.time()
    
    # 异步映射
    squared = await async_map(slow_square, numbers)
    print(f"平方结果: {squared}")
    
    # 异步过滤
    evens = await async_filter(is_even_async, numbers)
    print(f"偶数: {evens}")
    
    end_time = time.time()
    print(f"总耗时: {end_time - start_time:.2f}秒")

# 运行异步示例（在支持asyncio的环境中）
# asyncio.run(async_example())
print("异步示例代码已定义（需要在支持asyncio的环境中运行）")
```

## 性能优化和最佳实践

### Lambda性能优化

```python
# Lambda性能优化技巧

import time
import functools

# 1. 避免重复计算
# 低效的Lambda
slow_lambda = lambda x: sum(range(x)) ** 2

# 优化的Lambda（预计算）
fast_lambda = lambda x, _cache={}: _cache.setdefault(x, sum(range(x)) ** 2)

# 性能测试
def benchmark_lambda(func, test_values, iterations=1000):
    start_time = time.perf_counter()
    for _ in range(iterations):
        for value in test_values:
            func(value)
    end_time = time.perf_counter()
    return end_time - start_time

test_values = [10, 20, 30, 40, 50]

slow_time = benchmark_lambda(slow_lambda, test_values, 100)
fast_time = benchmark_lambda(fast_lambda, test_values, 100)

print(f"慢速Lambda: {slow_time:.4f}秒")
print(f"快速Lambda: {fast_time:.4f}秒")
print(f"性能提升: {(slow_time - fast_time) / slow_time * 100:.1f}%")

# 2. 使用operator模块替代简单Lambda
from operator import add, mul, itemgetter

# 低效
sum_with_lambda = lambda data: functools.reduce(lambda x, y: x + y, data)

# 高效
sum_with_operator = lambda data: functools.reduce(add, data)

# 测试数据
large_data = list(range(10000))

lambda_time = benchmark_lambda(sum_with_lambda, [large_data], 10)
operator_time = benchmark_lambda(sum_with_operator, [large_data], 10)

print(f"\nLambda求和: {lambda_time:.4f}秒")
print(f"Operator求和: {operator_time:.4f}秒")
print(f"性能提升: {(lambda_time - operator_time) / lambda_time * 100:.1f}%")

# 3. 内存优化
# 避免创建不必要的中间列表
# 低效（创建中间列表）
process_inefficient = lambda data: sum([x**2 for x in data if x % 2 == 0])

# 高效（使用生成器）
process_efficient = lambda data: sum(x**2 for x in data if x % 2 == 0)

# 内存使用比较
import sys

def get_memory_usage(func, data):
    import tracemalloc
    tracemalloc.start()
    result = func(data)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, peak

test_data = list(range(100000))

result1, memory1 = get_memory_usage(process_inefficient, test_data)
result2, memory2 = get_memory_usage(process_efficient, test_data)

print(f"\n低效方法内存使用: {memory1 / 1024 / 1024:.2f} MB")
print(f"高效方法内存使用: {memory2 / 1024 / 1024:.2f} MB")
print(f"内存节省: {(memory1 - memory2) / memory1 * 100:.1f}%")
```

### Lambda最佳实践

```python
# Lambda最佳实践指南

print("Lambda最佳实践:")
print("\n1. 保持简洁")
print("   好: lambda x: x * 2")
print("   坏: lambda x: x * 2 if x > 0 else -x * 2 if x < 0 else 0")

print("\n2. 使用有意义的变量名")
print("   好: lambda student: student.grade > 80")
print("   坏: lambda s: s.g > 80")

print("\n3. 避免副作用")
print("   好: lambda x: x ** 2")
print("   坏: lambda x: print(x) or x ** 2")

print("\n4. 考虑可读性")
# 复杂逻辑应该使用普通函数
def complex_validation(data):
    """复杂的数据验证逻辑"""
    if not isinstance(data, dict):
        return False
    
    required_fields = ['name', 'age', 'email']
    if not all(field in data for field in required_fields):
        return False
    
    if not (0 <= data['age'] <= 120):
        return False
    
    if '@' not in data['email']:
        return False
    
    return True

# 而不是使用复杂的Lambda
# 坏的例子（不要这样做）
# complex_lambda = lambda data: (
#     isinstance(data, dict) and 
#     all(field in data for field in ['name', 'age', 'email']) and
#     0 <= data['age'] <= 120 and
#     '@' in data['email']
# )

print("\n5. 性能考虑")
print("   - 对于简单操作，优先使用operator模块")
print("   - 避免在Lambda中进行重复计算")
print("   - 考虑使用functools.partial替代复杂的Lambda")

# 示例：何时使用Lambda vs 普通函数
print("\n使用场景指南:")

# 适合使用Lambda的场景
print("\n适合Lambda:")
numbers = [1, 2, 3, 4, 5]

# 简单的映射
squares = list(map(lambda x: x**2, numbers))
print(f"  简单映射: {squares}")

# 简单的过滤
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"  简单过滤: {evens}")

# 简单的排序
words = ['apple', 'pie', 'a', 'longer']
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"  简单排序: {sorted_by_length}")

print("\n不适合Lambda（应使用普通函数）:")
print("  - 复杂的业务逻辑")
print("  - 需要多行代码的操作")
print("  - 需要异常处理的操作")
print("  - 需要文档说明的操作")
print("  - 会被多次重用的操作")

# 错误处理示例
print("\n错误处理:")

# Lambda中的错误处理很困难
safe_divide = lambda x, y: x / y if y != 0 else float('inf')
print(f"  安全除法: 10/2 = {safe_divide(10, 2)}, 10/0 = {safe_divide(10, 0)}")

# 更好的方法是使用普通函数
def safe_divide_function(x, y):
    """安全的除法操作，处理除零错误"""
    try:
        return x / y
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
        raise ValueError("参数必须是数字")

print(f"  函数版本: 10/2 = {safe_divide_function(10, 2)}")

# 代码组织建议
print("\n代码组织建议:")
print("  1. 将相关的Lambda组织在一起")
print("  2. 为复杂的Lambda添加注释")
print("  3. 考虑将常用的Lambda提取为变量")
print("  4. 在模块级别定义可重用的Lambda")

# 常用Lambda的提取
IS_EVEN = lambda x: x % 2 == 0
IS_POSITIVE = lambda x: x > 0
SQUARE = lambda x: x ** 2
DOUBLE = lambda x: x * 2

# 使用提取的Lambda
test_numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
print(f"\n测试数据: {test_numbers}")
print(f"偶数: {list(filter(IS_EVEN, test_numbers))}")
print(f"正数: {list(filter(IS_POSITIVE, test_numbers))}")
print(f"正偶数的平方: {list(map(SQUARE, filter(lambda x: IS_EVEN(x) and IS_POSITIVE(x), test_numbers)))}")
```

## 总结

Lambda表达式的高级用法展现了函数式编程的强大威力。通过本节的学习，你应该掌握：

### 核心概念
1. **闭包与Lambda的结合使用**
2. **Lambda在装饰器模式中的应用**
3. **函数式编程的基本模式和技巧**
4. **递归与Lambda的结合**
5. **异步编程中的Lambda应用**

### 高级技巧
1. **函数组合和管道操作**
2. **柯里化和偏函数应用**
3. **Y组合子和递归模式**
4. **生成器与Lambda的结合**
5. **性能优化策略**

### 最佳实践
1. **何时使用Lambda vs 普通函数**
2. **代码可读性和维护性考虑**
3. **性能优化和内存管理**
4. **错误处理和调试技巧**

## 运行代码

将代码保存为Python文件并运行：

```bash
python3 07_lambda_advanced.py
```

每个代码块都展示了Lambda表达式的不同高级应用。建议按顺序学习，并尝试修改代码来深入理解这些高级概念和模式。记住，虽然Lambda很强大，但要在适当的场景中使用，保持代码的可读性和可维护性。