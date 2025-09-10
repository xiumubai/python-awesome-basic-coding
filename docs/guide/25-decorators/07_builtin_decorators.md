# 常用的内置装饰器

Python 提供了许多内置装饰器，这些装饰器在日常开发中非常有用。掌握这些内置装饰器能让我们写出更简洁、更高效的代码。

## @property 装饰器

`@property` 装饰器用于将方法转换为属性，提供了一种优雅的方式来实现getter、setter和deleter。

### 基本用法

```python
class Circle:
    """圆形类"""
    
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """半径属性的getter"""
        print("获取半径")
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """半径属性的setter"""
        if value <= 0:
            raise ValueError("半径必须大于0")
        print(f"设置半径为 {value}")
        self._radius = value
    
    @radius.deleter
    def radius(self):
        """半径属性的deleter"""
        print("删除半径属性")
        del self._radius
    
    @property
    def area(self):
        """面积属性（只读）"""
        import math
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self):
        """周长属性（只读）"""
        import math
        return 2 * math.pi * self._radius

# 使用示例
print("=== @property 装饰器示例 ===")
circle = Circle(5)

# 像访问属性一样访问方法
print(f"半径: {circle.radius}")
print(f"面积: {circle.area:.2f}")
print(f"周长: {circle.circumference:.2f}")

# 设置属性值
circle.radius = 10
print(f"新半径: {circle.radius}")
print(f"新面积: {circle.area:.2f}")

# 尝试设置无效值
try:
    circle.radius = -5
except ValueError as e:
    print(f"错误: {e}")

# 删除属性
del circle.radius
try:
    print(circle.radius)
except AttributeError as e:
    print(f"属性已删除: {e}")
```

### 高级 @property 用法

```python
class Temperature:
    """温度转换类"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """摄氏度"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度(-273.15°C)")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """华氏度"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        if value < -459.67:
            raise ValueError("温度不能低于绝对零度(-459.67°F)")
        self._celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """开尔文"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        if value < 0:
            raise ValueError("开尔文温度不能为负数")
        self._celsius = value - 273.15
    
    def __str__(self):
        return f"{self._celsius:.1f}°C = {self.fahrenheit:.1f}°F = {self.kelvin:.1f}K"

# 温度转换示例
print("\n=== 温度转换示例 ===")
temp = Temperature()

# 设置摄氏度
temp.celsius = 25
print(f"设置25°C: {temp}")

# 通过华氏度设置
temp.fahrenheit = 100
print(f"设置100°F: {temp}")

# 通过开尔文设置
temp.kelvin = 300
print(f"设置300K: {temp}")

# 测试边界条件
try:
    temp.celsius = -300
except ValueError as e:
    print(f"错误: {e}")
```

## @staticmethod 装饰器

`@staticmethod` 装饰器用于定义静态方法，这些方法不需要访问实例或类的状态。

```python
class MathUtils:
    """数学工具类"""
    
    PI = 3.14159265359
    
    @staticmethod
    def add(a, b):
        """加法运算"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """乘法运算"""
        return a * b
    
    @staticmethod
    def is_prime(n):
        """判断是否为质数"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n):
        """计算阶乘"""
        if n < 0:
            raise ValueError("阶乘不能计算负数")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def gcd(a, b):
        """计算最大公约数"""
        while b:
            a, b = b, a % b
        return abs(a)
    
    @staticmethod
    def lcm(a, b):
        """计算最小公倍数"""
        return abs(a * b) // MathUtils.gcd(a, b)

# 静态方法使用示例
print("\n=== @staticmethod 装饰器示例 ===")

# 可以通过类直接调用
print(f"5 + 3 = {MathUtils.add(5, 3)}")
print(f"4 * 6 = {MathUtils.multiply(4, 6)}")
print(f"17 是质数吗? {MathUtils.is_prime(17)}")
print(f"5! = {MathUtils.factorial(5)}")
print(f"gcd(48, 18) = {MathUtils.gcd(48, 18)}")
print(f"lcm(12, 8) = {MathUtils.lcm(12, 8)}")

# 也可以通过实例调用（但不推荐）
math_utils = MathUtils()
print(f"通过实例调用: 7 + 2 = {math_utils.add(7, 2)}")

# 静态方法不能访问实例或类变量（除非显式引用）
class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
        self.instance_id = Counter.count
    
    @staticmethod
    def get_total_count():
        """获取总计数（通过类名访问类变量）"""
        return Counter.count
    
    @staticmethod
    def reset_count():
        """重置计数"""
        Counter.count = 0

print("\n=== 静态方法访问类变量示例 ===")
c1 = Counter()
c2 = Counter()
c3 = Counter()

print(f"当前总数: {Counter.get_total_count()}")
Counter.reset_count()
print(f"重置后总数: {Counter.get_total_count()}")
```

## @classmethod 装饰器

`@classmethod` 装饰器用于定义类方法，这些方法接收类作为第一个参数（通常命名为 `cls`）。

```python
class Person:
    """人员类"""
    
    species = "Homo sapiens"
    population = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
    
    @classmethod
    def get_species(cls):
        """获取物种信息"""
        return cls.species
    
    @classmethod
    def get_population(cls):
        """获取人口数量"""
        return cls.population
    
    @classmethod
    def from_string(cls, person_str):
        """从字符串创建Person实例（替代构造函数）"""
        name, age = person_str.split('-')
        return cls(name, int(age))
    
    @classmethod
    def from_dict(cls, person_dict):
        """从字典创建Person实例"""
        return cls(person_dict['name'], person_dict['age'])
    
    @classmethod
    def create_baby(cls, name):
        """创建婴儿（年龄为0）"""
        return cls(name, 0)
    
    @classmethod
    def create_adult(cls, name):
        """创建成年人（年龄为18）"""
        return cls(name, 18)
    
    def __str__(self):
        return f"{self.name} ({self.age}岁)"
    
    def __del__(self):
        Person.population -= 1

# 类方法使用示例
print("\n=== @classmethod 装饰器示例 ===")

# 通过类直接调用
print(f"物种: {Person.get_species()}")
print(f"初始人口: {Person.get_population()}")

# 使用替代构造函数
person1 = Person.from_string("Alice-25")
person2 = Person.from_dict({'name': 'Bob', 'age': 30})
person3 = Person.create_baby("Charlie")
person4 = Person.create_adult("Diana")

print(f"创建的人员:")
print(f"  {person1}")
print(f"  {person2}")
print(f"  {person3}")
print(f"  {person4}")

print(f"当前人口: {Person.get_population()}")

# 类方法在继承中的行为
class Employee(Person):
    """员工类"""
    
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title
    
    @classmethod
    def create_manager(cls, name):
        """创建经理"""
        return cls(name, 35, "Manager")
    
    @classmethod
    def create_intern(cls, name):
        """创建实习生"""
        return cls(name, 22, "Intern")
    
    def __str__(self):
        return f"{self.name} ({self.age}岁, {self.job_title})"

print("\n=== 类方法继承示例 ===")

# 子类调用父类的类方法
employee1 = Employee.from_string("Eve-28")
employee1.job_title = "Developer"
print(f"从字符串创建员工: {employee1}")

# 子类自己的类方法
manager = Employee.create_manager("Frank")
intern = Employee.create_intern("Grace")

print(f"创建的员工:")
print(f"  {manager}")
print(f"  {intern}")

print(f"总人口: {Person.get_population()}")
```

## @functools.lru_cache 装饰器

`@functools.lru_cache` 是一个非常有用的缓存装饰器，实现了LRU（Least Recently Used）缓存策略。

```python
import functools
import time

# 基本LRU缓存使用
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    """计算斐波那契数列（带缓存）"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 无限制缓存
@functools.lru_cache(maxsize=None)
def expensive_function(x, y):
    """模拟昂贵的计算"""
    print(f"正在计算 expensive_function({x}, {y})...")
    time.sleep(0.1)  # 模拟耗时操作
    return x ** y + y ** x

# 带参数的缓存
@functools.lru_cache(maxsize=32)
def fetch_data(url, timeout=30):
    """模拟网络请求"""
    print(f"正在请求 {url} (超时: {timeout}秒)...")
    time.sleep(0.05)  # 模拟网络延迟
    return f"来自 {url} 的数据"

print("\n=== @functools.lru_cache 装饰器示例 ===")

# 测试斐波那契缓存效果
print("\n--- 斐波那契缓存测试 ---")
start_time = time.time()
result = fibonacci(30)
end_time = time.time()
print(f"fibonacci(30) = {result}")
print(f"首次计算耗时: {end_time - start_time:.4f}秒")

# 再次计算（应该很快）
start_time = time.time()
result = fibonacci(30)
end_time = time.time()
print(f"再次计算耗时: {end_time - start_time:.6f}秒")

# 查看缓存信息
print(f"缓存信息: {fibonacci.cache_info()}")

# 测试昂贵函数的缓存
print("\n--- 昂贵函数缓存测试 ---")
result1 = expensive_function(2, 3)
print(f"结果: {result1}")

result2 = expensive_function(2, 3)  # 应该命中缓存
print(f"缓存结果: {result2}")

result3 = expensive_function(3, 2)  # 不同参数，重新计算
print(f"新参数结果: {result3}")

print(f"expensive_function 缓存信息: {expensive_function.cache_info()}")

# 测试网络请求缓存
print("\n--- 网络请求缓存测试 ---")
data1 = fetch_data("https://api.example.com/users")
data2 = fetch_data("https://api.example.com/users")  # 缓存命中
data3 = fetch_data("https://api.example.com/users", timeout=60)  # 不同参数

print(f"fetch_data 缓存信息: {fetch_data.cache_info()}")

# 清空缓存
print("\n--- 缓存清空测试 ---")
fibonacci.cache_clear()
print(f"清空后的缓存信息: {fibonacci.cache_info()}")

# 高级缓存示例：带类型提示的缓存函数
from typing import List, Tuple

@functools.lru_cache(maxsize=64)
def matrix_multiply(matrix_a: Tuple[Tuple[int, ...], ...], 
                  matrix_b: Tuple[Tuple[int, ...], ...]) -> Tuple[Tuple[int, ...], ...]:
    """矩阵乘法（带缓存）
    
    注意：使用tuple而不是list，因为list不是可哈希的
    """
    print(f"正在计算矩阵乘法...")
    
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])
    
    if cols_a != rows_b:
        raise ValueError("矩阵维度不匹配")
    
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            sum_val = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(cols_a))
            row.append(sum_val)
        result.append(tuple(row))
    
    return tuple(result)

print("\n--- 矩阵乘法缓存测试 ---")
matrix1 = ((1, 2), (3, 4))
matrix2 = ((5, 6), (7, 8))

result1 = matrix_multiply(matrix1, matrix2)
print(f"矩阵乘法结果: {result1}")

result2 = matrix_multiply(matrix1, matrix2)  # 缓存命中
print(f"缓存命中: {result2}")

print(f"矩阵乘法缓存信息: {matrix_multiply.cache_info()}")
```

## @functools.singledispatch 装饰器

`@functools.singledispatch` 装饰器用于创建泛型函数，根据第一个参数的类型来选择不同的实现。

```python
import functools
from typing import Any

@functools.singledispatch
def process_data(data):
    """处理数据的泛型函数（默认实现）"""
    print(f"处理未知类型数据: {type(data).__name__}")
    return f"默认处理: {data}"

@process_data.register(str)
def _(data: str):
    """处理字符串数据"""
    print(f"处理字符串: {data}")
    return data.upper().strip()

@process_data.register(int)
def _(data: int):
    """处理整数数据"""
    print(f"处理整数: {data}")
    return data ** 2

@process_data.register(float)
def _(data: float):
    """处理浮点数数据"""
    print(f"处理浮点数: {data}")
    return round(data, 2)

@process_data.register(list)
def _(data: list):
    """处理列表数据"""
    print(f"处理列表: {data}")
    return [process_data(item) for item in data]

@process_data.register(dict)
def _(data: dict):
    """处理字典数据"""
    print(f"处理字典: {data}")
    return {k: process_data(v) for k, v in data.items()}

@process_data.register(tuple)
def _(data: tuple):
    """处理元组数据"""
    print(f"处理元组: {data}")
    return tuple(process_data(item) for item in data)

# 单分派函数使用示例
print("\n=== @functools.singledispatch 装饰器示例 ===")

# 测试不同类型的数据处理
test_data = [
    "  hello world  ",
    42,
    3.14159,
    [1, 2, "test", 3.5],
    {"name": "alice", "age": 25, "score": 95.7},
    ("python", 100, 2.718),
    None  # 未注册的类型
]

for data in test_data:
    print(f"\n输入: {data} ({type(data).__name__})")
    result = process_data(data)
    print(f"输出: {result}")

# 查看已注册的类型
print(f"\n已注册的类型: {list(process_data.registry.keys())}")

# 高级单分派示例：JSON序列化器
import json
from datetime import datetime, date
from decimal import Decimal

@functools.singledispatch
def to_json_serializable(obj):
    """将对象转换为JSON可序列化的形式"""
    # 默认情况：尝试转换为字符串
    return str(obj)

@to_json_serializable.register(datetime)
def _(obj: datetime):
    """处理datetime对象"""
    return obj.isoformat()

@to_json_serializable.register(date)
def _(obj: date):
    """处理date对象"""
    return obj.isoformat()

@to_json_serializable.register(Decimal)
def _(obj: Decimal):
    """处理Decimal对象"""
    return float(obj)

@to_json_serializable.register(set)
def _(obj: set):
    """处理set对象"""
    return list(obj)

@to_json_serializable.register(bytes)
def _(obj: bytes):
    """处理bytes对象"""
    return obj.decode('utf-8', errors='replace')

class CustomObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __str__(self):
        return f"CustomObject(name={self.name}, value={self.value})"

@to_json_serializable.register(CustomObject)
def _(obj: CustomObject):
    """处理自定义对象"""
    return {
        'type': 'CustomObject',
        'name': obj.name,
        'value': obj.value
    }

def safe_json_dumps(obj, **kwargs):
    """安全的JSON序列化函数"""
    def convert_recursive(item):
        if isinstance(item, dict):
            return {k: convert_recursive(v) for k, v in item.items()}
        elif isinstance(item, (list, tuple)):
            return [convert_recursive(i) for i in item]
        else:
            return to_json_serializable(item)
    
    converted = convert_recursive(obj)
    return json.dumps(converted, **kwargs)

print("\n=== JSON序列化器示例 ===")

# 测试复杂数据结构的JSON序列化
complex_data = {
    'timestamp': datetime.now(),
    'date': date.today(),
    'price': Decimal('19.99'),
    'tags': {'python', 'programming', 'tutorial'},
    'binary_data': b'Hello World',
    'custom': CustomObject('test', 42),
    'nested': {
        'list': [datetime.now(), Decimal('3.14'), {'a', 'b', 'c'}],
        'tuple': (date.today(), b'data', CustomObject('nested', 100))
    }
}

print("原始数据:")
for key, value in complex_data.items():
    print(f"  {key}: {value} ({type(value).__name__})")

print("\nJSON序列化结果:")
json_result = safe_json_dumps(complex_data, indent=2, ensure_ascii=False)
print(json_result)

# 验证可以正确解析
parsed = json.loads(json_result)
print(f"\n解析成功: {type(parsed).__name__}")
```

## @dataclasses.dataclass 装饰器

`@dataclasses.dataclass` 装饰器用于自动生成特殊方法，简化类的定义。

```python
import dataclasses
from typing import List, Optional
from datetime import datetime

@dataclasses.dataclass
class Point:
    """二维点类"""
    x: float
    y: float
    
    def distance_to_origin(self) -> float:
        """计算到原点的距离"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

@dataclasses.dataclass(order=True)  # 启用排序
class Student:
    """学生类"""
    name: str
    age: int
    grade: float
    subjects: List[str] = dataclasses.field(default_factory=list)
    
    def __post_init__(self):
        """初始化后处理"""
        if self.age < 0:
            raise ValueError("年龄不能为负数")
        if not 0 <= self.grade <= 100:
            raise ValueError("成绩必须在0-100之间")

@dataclasses.dataclass(frozen=True)  # 不可变类
class ImmutableConfig:
    """不可变配置类"""
    host: str
    port: int
    debug: bool = False
    timeout: float = 30.0

@dataclasses.dataclass
class BlogPost:
    """博客文章类"""
    title: str
    content: str
    author: str
    created_at: datetime = dataclasses.field(default_factory=datetime.now)
    tags: List[str] = dataclasses.field(default_factory=list)
    view_count: int = dataclasses.field(default=0, init=False)  # 不在__init__中
    
    def add_view(self):
        """增加浏览次数"""
        self.view_count += 1
    
    def add_tag(self, tag: str):
        """添加标签"""
        if tag not in self.tags:
            self.tags.append(tag)

print("\n=== @dataclasses.dataclass 装饰器示例 ===")

# 基本使用
print("\n--- 基本Point类 ---")
p1 = Point(3.0, 4.0)
p2 = Point(1.0, 2.0)

print(f"点1: {p1}")
print(f"点2: {p2}")
print(f"点1到原点距离: {p1.distance_to_origin():.2f}")
print(f"点1 == 点2: {p1 == p2}")
print(f"点1 == Point(3.0, 4.0): {p1 == Point(3.0, 4.0)}")

# 学生类（支持排序）
print("\n--- 学生类（支持排序） ---")
students = [
    Student("Alice", 20, 85.5, ["Math", "Physics"]),
    Student("Bob", 19, 92.0, ["Chemistry", "Biology"]),
    Student("Charlie", 21, 78.5, ["History", "Literature"])
]

print("原始顺序:")
for student in students:
    print(f"  {student}")

# 按字段顺序排序（name, age, grade）
sorted_students = sorted(students)
print("\n排序后:")
for student in sorted_students:
    print(f"  {student}")

# 不可变配置类
print("\n--- 不可变配置类 ---")
config = ImmutableConfig("localhost", 8080, debug=True)
print(f"配置: {config}")

# 尝试修改不可变对象（会报错）
try:
    config.port = 9000
except dataclasses.FrozenInstanceError as e:
    print(f"不可变对象修改失败: {e}")

# 博客文章类
print("\n--- 博客文章类 ---")
post = BlogPost(
    title="Python装饰器详解",
    content="装饰器是Python的强大特性...",
    author="张三"
)

print(f"文章: {post.title}")
print(f"作者: {post.author}")
print(f"创建时间: {post.created_at}")
print(f"初始浏览次数: {post.view_count}")

# 添加标签和浏览次数
post.add_tag("Python")
post.add_tag("编程")
post.add_tag("教程")
post.add_view()
post.add_view()

print(f"标签: {post.tags}")
print(f"浏览次数: {post.view_count}")

# 使用dataclasses的工具函数
print("\n--- dataclasses工具函数 ---")
print(f"Point是否为dataclass: {dataclasses.is_dataclass(Point)}")
print(f"普通类是否为dataclass: {dataclasses.is_dataclass(str)}")

# 获取字段信息
point_fields = dataclasses.fields(Point)
print(f"Point类的字段:")
for field in point_fields:
    print(f"  {field.name}: {field.type}")

# 转换为字典和元组
point_dict = dataclasses.asdict(p1)
point_tuple = dataclasses.astuple(p1)
print(f"Point转字典: {point_dict}")
print(f"Point转元组: {point_tuple}")

# 替换字段值（创建新实例）
new_point = dataclasses.replace(p1, x=10.0)
print(f"原点: {p1}")
print(f"新点: {new_point}")
```

## 其他有用的内置装饰器

### @contextlib.contextmanager

```python
import contextlib
import time

@contextlib.contextmanager
def timer_context(name):
    """计时上下文管理器"""
    print(f"开始执行: {name}")
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f"执行完成: {name}, 耗时: {end_time - start_time:.4f}秒")

@contextlib.contextmanager
def suppress_errors(*exceptions):
    """抑制指定异常的上下文管理器"""
    try:
        yield
    except exceptions as e:
        print(f"抑制异常: {type(e).__name__}: {e}")

print("\n=== @contextlib.contextmanager 装饰器示例 ===")

# 使用计时上下文管理器
with timer_context("数据处理"):
    time.sleep(0.1)
    data = [i ** 2 for i in range(1000)]
    print(f"处理了 {len(data)} 个数据")

# 使用异常抑制上下文管理器
with suppress_errors(ValueError, TypeError):
    result = int("not_a_number")  # 会抛出ValueError
    print(f"结果: {result}")  # 不会执行

print("程序继续执行...")
```

### @functools.wraps 的高级用法

```python
import functools
import inspect

def preserve_signature(func):
    """保留函数签名的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 获取原函数的签名
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        print(f"调用 {func.__name__} 参数: {dict(bound_args.arguments)}")
        return func(*args, **kwargs)
    
    # 保留原函数的签名
    wrapper.__signature__ = inspect.signature(func)
    return wrapper

@preserve_signature
def complex_function(a: int, b: str = "default", *, c: float, d: bool = True) -> str:
    """复杂参数的函数"""
    return f"a={a}, b={b}, c={c}, d={d}"

print("\n=== 保留函数签名示例 ===")
print(f"函数签名: {inspect.signature(complex_function)}")
result = complex_function(1, "test", c=3.14)
print(f"结果: {result}")
```

## 小结

Python内置装饰器的特点和用途：

1. **@property**：将方法转换为属性，提供getter/setter/deleter功能
2. **@staticmethod**：定义静态方法，不需要访问实例或类状态
3. **@classmethod**：定义类方法，接收类作为第一个参数，常用于替代构造函数
4. **@functools.lru_cache**：提供LRU缓存功能，显著提升重复计算的性能
5. **@functools.singledispatch**：创建泛型函数，根据参数类型选择实现
6. **@dataclasses.dataclass**：自动生成特殊方法，简化类定义
7. **@contextlib.contextmanager**：将生成器函数转换为上下文管理器

这些内置装饰器是Python标准库的重要组成部分，熟练掌握它们能让我们写出更简洁、更高效的代码。在下一章中，我们将通过综合练习来巩固所学的装饰器知识。