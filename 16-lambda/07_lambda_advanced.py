#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lambda表达式高级用法

本文件介绍Lambda表达式的高级应用场景，
包括闭包、装饰器、函数式编程等高级概念。

学习目标：
1. 理解Lambda表达式与闭包的结合
2. 掌握Lambda在装饰器中的应用
3. 学习函数式编程中的Lambda用法
4. 了解Lambda的高级技巧和最佳实践
"""

import functools
from collections import defaultdict
import time
import threading

# 1. Lambda与闭包
print("=== 1. Lambda与闭包 ===")
print("闭包：内部函数引用外部函数的变量")
print("Lambda可以创建简单的闭包")
print()

# 基本闭包示例
def make_multiplier(n):
    """创建乘法器函数"""
    return lambda x: x * n

# 创建不同的乘法器
double = make_multiplier(2)
triple = make_multiplier(3)
square = make_multiplier(lambda x: x)  # 这里lambda作为参数

print("乘法器闭包示例：")
print(f"double(5) = {double(5)}")
print(f"triple(4) = {triple(4)}")

# 累加器闭包
def make_accumulator(initial=0):
    """创建累加器"""
    total = [initial]  # 使用列表避免nonlocal
    return lambda x: total.__setitem__(0, total[0] + x) or total[0]

acc1 = make_accumulator()
acc2 = make_accumulator(100)

print("\n累加器闭包示例：")
print(f"acc1(10) = {acc1(10)}")
print(f"acc1(5) = {acc1(5)}")
print(f"acc2(20) = {acc2(20)}")
print(f"acc2(30) = {acc2(30)}")

# 配置函数生成器
def make_validator(min_val, max_val):
    """创建验证器函数"""
    return lambda x: min_val <= x <= max_val

age_validator = make_validator(0, 120)
score_validator = make_validator(0, 100)

print("\n验证器闭包示例：")
test_ages = [25, -5, 150, 80]
for age in test_ages:
    print(f"年龄{age}有效: {age_validator(age)}")

test_scores = [85, 105, -10, 95]
for score in test_scores:
    print(f"分数{score}有效: {score_validator(score)}")
print()

# 2. Lambda与装饰器
print("=== 2. Lambda与装饰器 ===")

# 简单的Lambda装饰器
def simple_timer(func):
    """简单的计时装饰器"""
    return lambda *args, **kwargs: (
        lambda start: (
            lambda result: (
                print(f"函数 {func.__name__} 执行时间: {time.time() - start:.4f}秒"),
                result
            )[1]
        )(func(*args, **kwargs))
    )(time.time())

@simple_timer
def slow_function():
    """模拟慢函数"""
    time.sleep(0.1)
    return "完成"

print("Lambda装饰器示例：")
result = slow_function()
print(f"函数返回: {result}")

# 参数化Lambda装饰器
def repeat_decorator(times):
    """重复执行装饰器"""
    return lambda func: lambda *args, **kwargs: [
        func(*args, **kwargs) for _ in range(times)
    ][-1]  # 返回最后一次执行结果

@repeat_decorator(3)
def greet(name):
    print(f"Hello, {name}!")
    return f"Greeted {name}"

print("\n重复执行装饰器：")
result = greet("Alice")
print(f"最终结果: {result}")

# 条件执行装饰器
def conditional_execute(condition):
    """条件执行装饰器"""
    return lambda func: lambda *args, **kwargs: (
        func(*args, **kwargs) if condition(*args, **kwargs) 
        else print(f"条件不满足，跳过执行 {func.__name__}")
    )

@conditional_execute(lambda x: x > 0)
def positive_sqrt(x):
    return x ** 0.5

print("\n条件执行装饰器：")
print(f"positive_sqrt(16) = {positive_sqrt(16)}")
print(f"positive_sqrt(-4) = {positive_sqrt(-4)}")
print()

# 3. 函数式编程高级技巧
print("=== 3. 函数式编程高级技巧 ===")

# 函数组合
def compose(*functions):
    """函数组合器"""
    return functools.reduce(
        lambda f, g: lambda x: f(g(x)),
        functions,
        lambda x: x
    )

# 创建函数管道
add_one = lambda x: x + 1
multiply_two = lambda x: x * 2
square = lambda x: x ** 2

pipeline = compose(square, multiply_two, add_one)

print("函数组合示例：")
test_value = 3
print(f"输入: {test_value}")
print(f"add_one: {add_one(test_value)}")
print(f"multiply_two(add_one): {multiply_two(add_one(test_value))}")
print(f"square(multiply_two(add_one)): {square(multiply_two(add_one(test_value)))}")
print(f"组合函数结果: {pipeline(test_value)}")

# 柯里化（Currying）
def curry(func):
    """柯里化函数"""
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *more_args, **more_kwargs: curried(*(args + more_args), **{**kwargs, **more_kwargs})
    return curried

# 使用Lambda创建柯里化函数
add_three = lambda x, y, z: x + y + z
curried_add = curry(add_three)

print("\n柯里化示例：")
print(f"普通调用: add_three(1, 2, 3) = {add_three(1, 2, 3)}")
print(f"柯里化调用: curried_add(1)(2)(3) = {curried_add(1)(2)(3)}")
print(f"部分应用: curried_add(1, 2)(3) = {curried_add(1, 2)(3)}")

# 偏函数应用
from functools import partial

# 使用Lambda创建偏函数
multiply = lambda x, y: x * y
double_lambda = lambda x: multiply(x, 2)
triple_lambda = lambda x: multiply(x, 3)

# 使用partial创建偏函数
double_partial = partial(multiply, y=2)
triple_partial = partial(multiply, y=3)

print("\n偏函数应用：")
test_num = 5
print(f"Lambda偏函数: double_lambda({test_num}) = {double_lambda(test_num)}")
print(f"partial偏函数: double_partial({test_num}) = {double_partial(test_num)}")
print()

# 4. 高阶函数应用
print("=== 4. 高阶函数应用 ===")

# 函数工厂
def make_operation(operation):
    """创建操作函数"""
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else float('inf'),
        'power': lambda x, y: x ** y,
        'mod': lambda x, y: x % y if y != 0 else 0
    }
    return operations.get(operation, lambda x, y: None)

print("函数工厂示例：")
operations = ['add', 'multiply', 'power']
for op_name in operations:
    op_func = make_operation(op_name)
    result = op_func(3, 4)
    print(f"{op_name}(3, 4) = {result}")

# 条件函数选择器
def select_function(*conditions_and_functions):
    """根据条件选择函数"""
    def selector(x):
        for condition, function in conditions_and_functions:
            if condition(x):
                return function(x)
        return x  # 默认返回原值
    return selector

# 创建数字处理器
number_processor = select_function(
    (lambda x: x < 0, lambda x: abs(x)),  # 负数取绝对值
    (lambda x: x > 100, lambda x: 100),   # 大于100的限制为100
    (lambda x: x % 2 == 0, lambda x: x // 2),  # 偶数除以2
    (lambda x: True, lambda x: x * 3)     # 其他情况乘以3
)

print("\n条件函数选择器：")
test_numbers = [-5, 150, 8, 7]
for num in test_numbers:
    result = number_processor(num)
    print(f"处理 {num} -> {result}")

# 函数缓存装饰器
def memoize_lambda(func):
    """使用Lambda的记忆化装饰器"""
    cache = {}
    return lambda *args: cache.setdefault(args, func(*args))

@memoize_lambda
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\n函数缓存示例：")
print(f"fibonacci(10) = {fibonacci(10)}")
print(f"fibonacci(15) = {fibonacci(15)}")
print()

# 5. 事件处理和回调
print("=== 5. 事件处理和回调 ===")

# 事件系统
class EventSystem:
    def __init__(self):
        self.listeners = defaultdict(list)
    
    def on(self, event, callback):
        """注册事件监听器"""
        self.listeners[event].append(callback)
    
    def emit(self, event, *args, **kwargs):
        """触发事件"""
        for callback in self.listeners[event]:
            callback(*args, **kwargs)

# 创建事件系统
events = EventSystem()

# 注册Lambda回调
events.on('user_login', lambda user: print(f"用户 {user} 登录了"))
events.on('user_login', lambda user: print(f"记录登录日志: {user}"))
events.on('user_logout', lambda user: print(f"用户 {user} 退出了"))

# 注册复杂回调
events.on('data_update', lambda data, timestamp: (
    print(f"数据更新: {data}"),
    print(f"时间戳: {timestamp}")
))

print("事件系统示例：")
events.emit('user_login', 'Alice')
events.emit('data_update', {'count': 100}, '2023-12-01 10:30:00')
events.emit('user_logout', 'Alice')

# 异步回调模拟
def async_operation(callback):
    """模拟异步操作"""
    def worker():
        time.sleep(0.1)  # 模拟耗时操作
        callback("操作完成")
    
    thread = threading.Thread(target=worker)
    thread.start()
    return thread

print("\n异步回调示例：")
thread = async_operation(lambda result: print(f"回调收到: {result}"))
thread.join()  # 等待完成
print()

# 6. 数据处理管道
print("=== 6. 数据处理管道 ===")

# 数据处理管道
class DataPipeline:
    def __init__(self, data):
        self.data = data
    
    def map(self, func):
        """映射操作"""
        self.data = list(map(func, self.data))
        return self
    
    def filter(self, func):
        """过滤操作"""
        self.data = list(filter(func, self.data))
        return self
    
    def reduce(self, func, initial=None):
        """归约操作"""
        if initial is not None:
            return functools.reduce(func, self.data, initial)
        return functools.reduce(func, self.data)
    
    def sort(self, key=None, reverse=False):
        """排序操作"""
        self.data = sorted(self.data, key=key, reverse=reverse)
        return self
    
    def get(self):
        """获取结果"""
        return self.data

# 使用数据管道
raw_data = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

result = (DataPipeline(raw_data)
          .map(lambda x: abs(x))           # 取绝对值
          .filter(lambda x: x > 3)         # 过滤大于3的数
          .map(lambda x: x ** 2)           # 平方
          .sort(key=lambda x: x, reverse=True)  # 降序排序
          .get())

print("数据处理管道示例：")
print(f"原始数据: {raw_data}")
print(f"处理结果: {result}")
print("处理步骤: 取绝对值 -> 过滤>3 -> 平方 -> 降序排序")

# 复杂数据处理
students_data = [
    {'name': '张三', 'age': 20, 'scores': [85, 92, 78]},
    {'name': '李四', 'age': 19, 'scores': [90, 88, 95]},
    {'name': '王五', 'age': 21, 'scores': [76, 82, 89]},
    {'name': '赵六', 'age': 20, 'scores': [88, 91, 87]}
]

# 计算平均分并筛选优秀学生
excellent_students = (DataPipeline(students_data)
                     .map(lambda s: {**s, 'avg_score': sum(s['scores']) / len(s['scores'])})
                     .filter(lambda s: s['avg_score'] >= 85)
                     .sort(key=lambda s: s['avg_score'], reverse=True)
                     .get())

print("\n学生数据处理：")
for student in excellent_students:
    print(f"{student['name']}: 平均分 {student['avg_score']:.1f}")
print()

# 7. 动态函数生成
print("=== 7. 动态函数生成 ===")

# 数学函数生成器
def make_math_function(expression):
    """根据表达式创建数学函数"""
    # 安全的数学表达式求值
    allowed_names = {
        'x': None, 'abs': abs, 'pow': pow, 'max': max, 'min': min,
        'sin': lambda x: __import__('math').sin(x),
        'cos': lambda x: __import__('math').cos(x),
        'sqrt': lambda x: __import__('math').sqrt(x),
        'log': lambda x: __import__('math').log(x),
        'exp': lambda x: __import__('math').exp(x)
    }
    
    def safe_eval(expr, x_val):
        allowed_names['x'] = x_val
        try:
            return eval(expr, {"__builtins__": {}}, allowed_names)
        except:
            return None
    
    return lambda x: safe_eval(expression, x)

# 创建动态函数
functions = {
    'linear': make_math_function('2 * x + 1'),
    'quadratic': make_math_function('x ** 2 - 3 * x + 2'),
    'cubic': make_math_function('x ** 3 - 2 * x ** 2 + x - 1'),
    'trigonometric': make_math_function('sin(x) + cos(x)'),
    'exponential': make_math_function('exp(x / 10)')
}

print("动态函数生成示例：")
test_x = 2
for name, func in functions.items():
    result = func(test_x)
    print(f"{name}({test_x}) = {result}")

# 条件函数生成器
def make_conditional_function(conditions):
    """创建条件函数"""
    def conditional_func(x):
        for condition, action in conditions:
            if condition(x):
                return action(x)
        return x
    return conditional_func

# 创建分段函数
piecewise_func = make_conditional_function([
    (lambda x: x < 0, lambda x: -x),      # x < 0: 返回 -x
    (lambda x: x == 0, lambda x: 0),      # x = 0: 返回 0
    (lambda x: x <= 10, lambda x: x ** 2), # 0 < x <= 10: 返回 x²
    (lambda x: True, lambda x: 100)       # x > 10: 返回 100
])

print("\n分段函数示例：")
test_values = [-3, 0, 5, 15]
for val in test_values:
    result = piecewise_func(val)
    print(f"f({val}) = {result}")
print()

# 8. 性能优化技巧
print("=== 8. 性能优化技巧 ===")

# Lambda vs 普通函数性能比较
def performance_comparison():
    data = list(range(10000))
    
    # 测试Lambda
    start_time = time.time()
    lambda_result = list(map(lambda x: x * 2, data))
    lambda_time = time.time() - start_time
    
    # 测试普通函数
    def double(x):
        return x * 2
    
    start_time = time.time()
    func_result = list(map(double, data))
    func_time = time.time() - start_time
    
    # 测试列表推导式
    start_time = time.time()
    list_comp_result = [x * 2 for x in data]
    list_comp_time = time.time() - start_time
    
    return lambda_time, func_time, list_comp_time

lambda_t, func_t, list_t = performance_comparison()
print("性能比较（处理10000个元素）：")
print(f"Lambda函数: {lambda_t:.6f} 秒")
print(f"普通函数: {func_t:.6f} 秒")
print(f"列表推导: {list_t:.6f} 秒")

# Lambda缓存优化
def cached_lambda(func):
    """为Lambda添加缓存"""
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

# 昂贵的计算函数
expensive_calc = cached_lambda(lambda x: sum(i**2 for i in range(x)))

print("\nLambda缓存优化：")
start = time.time()
result1 = expensive_calc(1000)
first_time = time.time() - start

start = time.time()
result2 = expensive_calc(1000)  # 从缓存获取
second_time = time.time() - start

print(f"首次计算: {first_time:.6f} 秒, 结果: {result1}")
print(f"缓存获取: {second_time:.6f} 秒, 结果: {result2}")
print(f"性能提升: {first_time/second_time:.1f}x")
print()

# 9. 实际应用案例
print("=== 9. 实际应用案例 ===")

# 案例1：配置驱动的数据验证
validation_rules = {
    'email': lambda x: '@' in x and '.' in x.split('@')[1],
    'phone': lambda x: x.isdigit() and len(x) in [10, 11],
    'age': lambda x: x.isdigit() and 0 <= int(x) <= 120,
    'password': lambda x: len(x) >= 8 and any(c.isdigit() for c in x)
}

def validate_data(data, rules):
    """验证数据"""
    results = {}
    for field, value in data.items():
        if field in rules:
            results[field] = rules[field](value)
        else:
            results[field] = True  # 无规则默认通过
    return results

test_data = {
    'email': 'user@example.com',
    'phone': '13812345678',
    'age': '25',
    'password': 'password123'
}

print("数据验证案例：")
validation_results = validate_data(test_data, validation_rules)
for field, is_valid in validation_results.items():
    status = "✓" if is_valid else "✗"
    print(f"{status} {field}: {test_data[field]}")

# 案例2：动态API路由
class SimpleRouter:
    def __init__(self):
        self.routes = {}
    
    def route(self, path, handler):
        """注册路由"""
        self.routes[path] = handler
    
    def handle(self, path, *args, **kwargs):
        """处理请求"""
        if path in self.routes:
            return self.routes[path](*args, **kwargs)
        return "404 Not Found"

# 创建路由器
router = SimpleRouter()

# 使用Lambda注册路由
router.route('/hello', lambda name='World': f"Hello, {name}!")
router.route('/add', lambda a, b: a + b)
router.route('/user', lambda user_id: f"User ID: {user_id}")
router.route('/calc', lambda op, x, y: {
    'add': x + y,
    'sub': x - y,
    'mul': x * y,
    'div': x / y if y != 0 else 'Error: Division by zero'
}.get(op, 'Unknown operation'))

print("\n动态路由案例：")
print(router.handle('/hello', 'Alice'))
print(router.handle('/add', 10, 20))
print(router.handle('/user', 123))
print(router.handle('/calc', 'mul', 6, 7))
print(router.handle('/unknown'))

# 案例3：函数式数据转换
def transform_data(data, transformations):
    """应用一系列转换"""
    result = data
    for transform in transformations:
        result = transform(result)
    return result

# 定义转换函数
transformations = [
    lambda data: [item.strip() for item in data],  # 去除空白
    lambda data: [item.lower() for item in data],  # 转小写
    lambda data: [item for item in data if len(item) > 2],  # 过滤短字符串
    lambda data: sorted(data),  # 排序
    lambda data: list(set(data))  # 去重
]

raw_text_data = ['  Apple  ', 'BANANA', 'cherry', 'date', 'APPLE', 'fig', 'grape', '  ']
processed_data = transform_data(raw_text_data, transformations)

print("\n数据转换案例：")
print(f"原始数据: {raw_text_data}")
print(f"处理结果: {processed_data}")
print()

# 10. 最佳实践总结
print("=== 10. 最佳实践总结 ===")
print("Lambda高级用法的优点：")
print("✓ 代码简洁，适合函数式编程")
print("✓ 可以创建灵活的回调和事件处理")
print("✓ 支持动态函数生成")
print("✓ 与高阶函数配合使用效果好")
print()
print("使用注意事项：")
print("⚠ 避免过度复杂的Lambda表达式")
print("⚠ 注意性能影响，必要时使用缓存")
print("⚠ 复杂逻辑建议使用普通函数")
print("⚠ 注意Lambda的作用域和闭包陷阱")
print()
print("适用场景：")
print("• 事件处理和回调函数")
print("• 函数式编程和数据处理")
print("• 动态函数生成")
print("• 配置驱动的应用")
print("• 简单的装饰器和中间件")
print()
print("设计原则：")
print("• 保持Lambda简单明了")
print("• 优先考虑可读性")
print("• 合理使用闭包")
print("• 注意性能和内存使用")
print("• 结合其他函数式编程工具")

if __name__ == "__main__":
    print("\n=== Lambda表达式高级用法学习完成 ===")
    print("Lambda表达式是函数式编程的重要工具")
    print("掌握高级用法可以写出更优雅的代码")
    print("下一步：完成Lambda表达式的综合练习")