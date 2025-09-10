#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
常用的内置装饰器

Python提供了许多内置装饰器，这些装饰器在日常开发中非常有用。
掌握这些内置装饰器可以让代码更加简洁、高效和易于维护。

学习要点：
1. @property - 属性装饰器
2. @staticmethod - 静态方法装饰器
3. @classmethod - 类方法装饰器
4. @functools.lru_cache - 缓存装饰器
5. @functools.singledispatch - 单分派装饰器
6. @dataclasses.dataclass - 数据类装饰器
7. @contextlib.contextmanager - 上下文管理器装饰器
"""

import functools
import time
import dataclasses
import contextlib
from typing import Any, Union
from datetime import datetime
import weakref
import threading


def main():
    """主函数，演示常用的内置装饰器"""
    print("=" * 50)
    print("常用的内置装饰器")
    print("=" * 50)
    
    # 1. @property 属性装饰器
    print("\n1. @property 属性装饰器")
    print("-" * 30)
    
    class Circle:
        """圆形类，演示property装饰器"""
        
        def __init__(self, radius):
            self._radius = radius
        
        @property
        def radius(self):
            """半径属性"""
            return self._radius
        
        @radius.setter
        def radius(self, value):
            """设置半径"""
            if value <= 0:
                raise ValueError("半径必须大于0")
            self._radius = value
        
        @radius.deleter
        def radius(self):
            """删除半径"""
            print("删除半径属性")
            self._radius = 0
        
        @property
        def area(self):
            """面积属性（只读）"""
            return 3.14159 * self._radius ** 2
        
        @property
        def circumference(self):
            """周长属性（只读）"""
            return 2 * 3.14159 * self._radius
        
        def __str__(self):
            return f"Circle(radius={self._radius}, area={self.area:.2f}, circumference={self.circumference:.2f})"
    
    print("Property装饰器示例：")
    circle = Circle(5)
    print(f"初始圆形: {circle}")
    
    # 访问属性
    print(f"半径: {circle.radius}")
    print(f"面积: {circle.area:.2f}")
    print(f"周长: {circle.circumference:.2f}")
    
    # 修改属性
    circle.radius = 10
    print(f"修改半径后: {circle}")
    
    # 尝试设置无效值
    try:
        circle.radius = -5
    except ValueError as e:
        print(f"设置无效半径: {e}")
    
    # 删除属性
    del circle.radius
    print(f"删除半径后: {circle}")
    
    # 2. @staticmethod 静态方法装饰器
    print("\n2. @staticmethod 静态方法装饰器")
    print("-" * 30)
    
    class MathUtils:
        """数学工具类，演示静态方法"""
        
        @staticmethod
        def add(x, y):
            """加法运算"""
            return x + y
        
        @staticmethod
        def multiply(x, y):
            """乘法运算"""
            return x * y
        
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
                raise ValueError("阶乘的参数必须非负")
            if n <= 1:
                return 1
            return n * MathUtils.factorial(n - 1)
    
    print("静态方法示例：")
    # 通过类调用
    print(f"MathUtils.add(5, 3) = {MathUtils.add(5, 3)}")
    print(f"MathUtils.multiply(4, 6) = {MathUtils.multiply(4, 6)}")
    print(f"MathUtils.is_prime(17) = {MathUtils.is_prime(17)}")
    print(f"MathUtils.factorial(5) = {MathUtils.factorial(5)}")
    
    # 通过实例调用
    math_utils = MathUtils()
    print(f"math_utils.add(2, 8) = {math_utils.add(2, 8)}")
    
    # 3. @classmethod 类方法装饰器
    print("\n3. @classmethod 类方法装饰器")
    print("-" * 30)
    
    class Person:
        """人员类，演示类方法"""
        
        species = "Homo sapiens"  # 类变量
        population = 0  # 人口计数
        
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
            """从字符串创建Person实例"""
            name, age = person_str.split('-')
            return cls(name, int(age))
        
        @classmethod
        def from_birth_year(cls, name, birth_year):
            """从出生年份创建Person实例"""
            current_year = datetime.now().year
            age = current_year - birth_year
            return cls(name, age)
        
        def __str__(self):
            return f"Person(name='{self.name}', age={self.age})"
        
        def __del__(self):
            Person.population -= 1
    
    print("类方法示例：")
    print(f"物种: {Person.get_species()}")
    print(f"初始人口: {Person.get_population()}")
    
    # 正常创建实例
    person1 = Person("Alice", 25)
    print(f"创建 {person1}")
    print(f"当前人口: {Person.get_population()}")
    
    # 使用类方法创建实例
    person2 = Person.from_string("Bob-30")
    print(f"从字符串创建: {person2}")
    
    person3 = Person.from_birth_year("Charlie", 1990)
    print(f"从出生年份创建: {person3}")
    
    print(f"最终人口: {Person.get_population()}")
    
    # 4. @functools.lru_cache 缓存装饰器
    print("\n4. @functools.lru_cache 缓存装饰器")
    print("-" * 30)
    
    @functools.lru_cache(maxsize=128)
    def fibonacci_cached(n):
        """带缓存的斐波那契数列"""
        if n < 2:
            return n
        return fibonacci_cached(n-1) + fibonacci_cached(n-2)
    
    def fibonacci_normal(n):
        """普通的斐波那契数列"""
        if n < 2:
            return n
        return fibonacci_normal(n-1) + fibonacci_normal(n-2)
    
    @functools.lru_cache(maxsize=None)  # 无限制缓存
    def expensive_calculation(x, y):
        """模拟耗时计算"""
        print(f"执行耗时计算: {x}, {y}")
        time.sleep(0.1)  # 模拟耗时操作
        return x ** 2 + y ** 2
    
    print("LRU缓存示例：")
    
    # 性能对比
    print("计算fibonacci(30):")
    
    start_time = time.time()
    result_cached = fibonacci_cached(30)
    cached_time = time.time() - start_time
    print(f"带缓存结果: {result_cached}, 耗时: {cached_time:.4f}秒")
    
    start_time = time.time()
    result_normal = fibonacci_normal(30)
    normal_time = time.time() - start_time
    print(f"普通递归结果: {result_normal}, 耗时: {normal_time:.4f}秒")
    
    print(f"性能提升: {normal_time / cached_time:.2f}倍")
    
    # 缓存信息
    print(f"\n缓存信息: {fibonacci_cached.cache_info()}")
    
    # 耗时计算缓存
    print("\n耗时计算缓存测试：")
    print("第一次调用:")
    result1 = expensive_calculation(3, 4)
    print(f"结果: {result1}")
    
    print("第二次调用（应该使用缓存）:")
    result2 = expensive_calculation(3, 4)
    print(f"结果: {result2}")
    
    print(f"缓存信息: {expensive_calculation.cache_info()}")
    
    # 清除缓存
    expensive_calculation.cache_clear()
    print(f"清除缓存后: {expensive_calculation.cache_info()}")
    
    # 5. @functools.singledispatch 单分派装饰器
    print("\n5. @functools.singledispatch 单分派装饰器")
    print("-" * 30)
    
    @functools.singledispatch
    def process_data(arg):
        """处理数据的通用函数"""
        print(f"处理未知类型: {type(arg).__name__} = {arg}")
        return str(arg)
    
    @process_data.register
    def _(arg: int):
        """处理整数"""
        print(f"处理整数: {arg}")
        return arg * 2
    
    @process_data.register
    def _(arg: float):
        """处理浮点数"""
        print(f"处理浮点数: {arg}")
        return round(arg, 2)
    
    @process_data.register
    def _(arg: str):
        """处理字符串"""
        print(f"处理字符串: {arg}")
        return arg.upper()
    
    @process_data.register
    def _(arg: list):
        """处理列表"""
        print(f"处理列表: {arg}")
        return len(arg)
    
    @process_data.register
    def _(arg: dict):
        """处理字典"""
        print(f"处理字典: {arg}")
        return list(arg.keys())
    
    print("单分派装饰器示例：")
    
    # 测试不同类型的数据
    test_data = [
        42,
        3.14159,
        "hello world",
        [1, 2, 3, 4, 5],
        {"a": 1, "b": 2, "c": 3},
        (1, 2, 3)  # 元组，没有注册处理函数
    ]
    
    for data in test_data:
        result = process_data(data)
        print(f"结果: {result}\n")
    
    # 查看注册的类型
    print(f"已注册的类型: {list(process_data.registry.keys())}")
    
    # 6. @dataclasses.dataclass 数据类装饰器
    print("\n6. @dataclasses.dataclass 数据类装饰器")
    print("-" * 30)
    
    @dataclasses.dataclass
    class Point:
        """基本数据类"""
        x: float
        y: float
    
    @dataclasses.dataclass(order=True)
    class Student:
        """学生数据类，支持排序"""
        name: str
        age: int
        grade: float
        
        def __post_init__(self):
            """初始化后处理"""
            if self.grade < 0 or self.grade > 100:
                raise ValueError("成绩必须在0-100之间")
    
    @dataclasses.dataclass(frozen=True)
    class ImmutablePoint:
        """不可变数据类"""
        x: float
        y: float
        
        def distance_from_origin(self):
            """计算到原点的距离"""
            return (self.x ** 2 + self.y ** 2) ** 0.5
    
    @dataclasses.dataclass
    class Product:
        """产品数据类，演示默认值和字段配置"""
        name: str
        price: float
        quantity: int = 0
        tags: list = dataclasses.field(default_factory=list)
        metadata: dict = dataclasses.field(default_factory=dict, repr=False)
        
        @property
        def total_value(self):
            """总价值"""
            return self.price * self.quantity
    
    print("数据类装饰器示例：")
    
    # 基本数据类
    point1 = Point(1.0, 2.0)
    point2 = Point(1.0, 2.0)
    print(f"Point1: {point1}")
    print(f"Point2: {point2}")
    print(f"相等性: {point1 == point2}")
    
    # 支持排序的数据类
    students = [
        Student("Alice", 20, 85.5),
        Student("Bob", 19, 92.0),
        Student("Charlie", 21, 78.5)
    ]
    
    print("\n学生列表（排序前）:")
    for student in students:
        print(f"  {student}")
    
    students.sort()
    print("\n学生列表（排序后）:")
    for student in students:
        print(f"  {student}")
    
    # 不可变数据类
    immutable_point = ImmutablePoint(3.0, 4.0)
    print(f"\n不可变点: {immutable_point}")
    print(f"到原点距离: {immutable_point.distance_from_origin():.2f}")
    
    # 尝试修改不可变对象
    try:
        immutable_point.x = 5.0
    except dataclasses.FrozenInstanceError as e:
        print(f"修改不可变对象失败: {e}")
    
    # 带默认值的数据类
    product = Product("笔记本电脑", 5999.99, 10)
    product.tags.extend(["电子产品", "办公用品"])
    product.metadata["brand"] = "Dell"
    
    print(f"\n产品: {product}")
    print(f"总价值: {product.total_value:.2f}")
    
    # 7. @contextlib.contextmanager 上下文管理器装饰器
    print("\n7. @contextlib.contextmanager 上下文管理器装饰器")
    print("-" * 30)
    
    @contextlib.contextmanager
    def timing_context(operation_name):
        """计时上下文管理器"""
        print(f"[{operation_name}] 开始执行")
        start_time = time.time()
        try:
            yield start_time
        except Exception as e:
            print(f"[{operation_name}] 执行出错: {e}")
            raise
        finally:
            end_time = time.time()
            duration = end_time - start_time
            print(f"[{operation_name}] 执行完成，耗时: {duration:.4f}秒")
    
    @contextlib.contextmanager
    def temporary_value(obj, attr, temp_value):
        """临时修改对象属性的上下文管理器"""
        original_value = getattr(obj, attr)
        print(f"临时修改 {attr}: {original_value} -> {temp_value}")
        setattr(obj, attr, temp_value)
        try:
            yield original_value
        finally:
            setattr(obj, attr, original_value)
            print(f"恢复 {attr}: {temp_value} -> {original_value}")
    
    @contextlib.contextmanager
    def database_transaction():
        """模拟数据库事务上下文管理器"""
        print("[事务] 开始事务")
        transaction_id = id(threading.current_thread())
        try:
            yield transaction_id
            print("[事务] 提交事务")
        except Exception as e:
            print(f"[事务] 回滚事务: {e}")
            raise
    
    print("上下文管理器装饰器示例：")
    
    # 计时上下文管理器
    with timing_context("数据处理"):
        # 模拟一些工作
        time.sleep(0.1)
        result = sum(range(1000000))
        print(f"计算结果: {result}")
    
    # 临时修改属性
    class Config:
        debug = False
        timeout = 30
    
    config = Config()
    print(f"\n原始配置: debug={config.debug}, timeout={config.timeout}")
    
    with temporary_value(config, 'debug', True):
        print(f"临时配置: debug={config.debug}, timeout={config.timeout}")
        # 在这里可以使用调试模式
    
    print(f"恢复配置: debug={config.debug}, timeout={config.timeout}")
    
    # 数据库事务模拟
    print("\n数据库事务示例：")
    
    # 成功的事务
    with database_transaction() as tx_id:
        print(f"[事务 {tx_id}] 执行数据库操作")
        print(f"[事务 {tx_id}] 插入数据")
        print(f"[事务 {tx_id}] 更新数据")
    
    # 失败的事务
    try:
        with database_transaction() as tx_id:
            print(f"[事务 {tx_id}] 执行数据库操作")
            print(f"[事务 {tx_id}] 插入数据")
            raise ValueError("数据库连接失败")
    except ValueError as e:
        print(f"事务处理完成: {e}")
    
    # 8. 组合使用内置装饰器
    print("\n8. 组合使用内置装饰器")
    print("-" * 30)
    
    @dataclasses.dataclass
    class Calculator:
        """计算器类，组合使用多个装饰器"""
        name: str = "默认计算器"
        
        @staticmethod
        @functools.lru_cache(maxsize=128)
        def power(base, exponent):
            """幂运算（静态方法 + 缓存）"""
            print(f"计算 {base}^{exponent}")
            return base ** exponent
        
        @classmethod
        def create_scientific(cls):
            """创建科学计算器"""
            return cls("科学计算器")
        
        @property
        def description(self):
            """计算器描述"""
            return f"这是一个{self.name}"
        
        @contextlib.contextmanager
        def calculation_context(self):
            """计算上下文"""
            print(f"[{self.name}] 开始计算")
            try:
                yield self
            finally:
                print(f"[{self.name}] 计算结束")
    
    print("组合装饰器示例：")
    
    # 创建计算器
    calc = Calculator.create_scientific()
    print(f"计算器: {calc}")
    print(f"描述: {calc.description}")
    
    # 使用缓存的静态方法
    with calc.calculation_context():
        result1 = Calculator.power(2, 10)
        result2 = Calculator.power(2, 10)  # 使用缓存
        print(f"2^10 = {result1}")
        print(f"缓存信息: {Calculator.power.cache_info()}")
    
    # 9. 最佳实践总结
    print("\n9. 最佳实践总结")
    print("-" * 30)
    
    print("内置装饰器最佳实践：")
    print("1. @property: 用于创建计算属性和控制属性访问")
    print("2. @staticmethod: 用于不需要访问实例或类的工具方法")
    print("3. @classmethod: 用于替代构造函数和访问类变量")
    print("4. @lru_cache: 用于缓存昂贵的计算结果")
    print("5. @singledispatch: 用于基于类型的函数重载")
    print("6. @dataclass: 用于简化数据类的定义")
    print("7. @contextmanager: 用于创建简单的上下文管理器")
    print("8. 合理组合使用多个装饰器可以提高代码质量")


if __name__ == "__main__":
    main()