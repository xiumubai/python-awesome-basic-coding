#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抽象方法和抽象类

抽象类是不能被实例化的类，它通常包含一个或多个抽象方法。
抽象方法是只有声明没有实现的方法，子类必须实现所有抽象方法才能被实例化。

核心概念：
1. 抽象类定义接口规范
2. 抽象方法强制子类实现
3. 提供代码复用和规范
4. 实现多态的重要机制
"""

from abc import ABC, abstractmethod
import math

# 1. 基本抽象类示例
class Animal(ABC):
    """动物抽象基类"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    @abstractmethod
    def make_sound(self):
        """抽象方法：发出声音"""
        pass
    
    @abstractmethod
    def move(self):
        """抽象方法：移动方式"""
        pass
    
    def eat(self):
        """具体方法：所有动物都会吃"""
        return f"{self.name} 正在吃东西"
    
    def sleep(self):
        """具体方法：所有动物都会睡觉"""
        return f"{self.name} 正在睡觉"
    
    def get_info(self):
        """具体方法：获取动物信息"""
        return f"{self.name} 是一只 {self.species}"

class Dog(Animal):
    """狗类 - 实现抽象方法"""
    
    def __init__(self, name, breed):
        super().__init__(name, "狗")
        self.breed = breed
    
    def make_sound(self):
        """实现抽象方法"""
        return f"{self.name} 汪汪叫"
    
    def move(self):
        """实现抽象方法"""
        return f"{self.name} 跑来跑去"
    
    def fetch(self):
        """狗特有的方法"""
        return f"{self.name} 去捡球"

class Cat(Animal):
    """猫类 - 实现抽象方法"""
    
    def __init__(self, name, color):
        super().__init__(name, "猫")
        self.color = color
    
    def make_sound(self):
        """实现抽象方法"""
        return f"{self.name} 喵喵叫"
    
    def move(self):
        """实现抽象方法"""
        return f"{self.name} 优雅地走动"
    
    def climb(self):
        """猫特有的方法"""
        return f"{self.name} 爬树"

class Bird(Animal):
    """鸟类 - 实现抽象方法"""
    
    def __init__(self, name, wingspan):
        super().__init__(name, "鸟")
        self.wingspan = wingspan
    
    def make_sound(self):
        """实现抽象方法"""
        return f"{self.name} 啾啾叫"
    
    def move(self):
        """实现抽象方法"""
        return f"{self.name} 在天空中飞翔"
    
    def fly(self):
        """鸟特有的方法"""
        return f"{self.name} 展开 {self.wingspan}cm 的翅膀飞翔"

# 2. 形状抽象类示例
class Shape(ABC):
    """形状抽象基类"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """抽象方法：计算面积"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """抽象方法：计算周长"""
        pass
    
    def describe(self):
        """具体方法：描述形状"""
        return f"这是一个{self.name}，面积: {self.area():.2f}，周长: {self.perimeter():.2f}"
    
    def compare_area(self, other_shape):
        """具体方法：比较面积"""
        if self.area() > other_shape.area():
            return f"{self.name} 的面积大于 {other_shape.name}"
        elif self.area() < other_shape.area():
            return f"{self.name} 的面积小于 {other_shape.name}"
        else:
            return f"{self.name} 的面积等于 {other_shape.name}"

class Rectangle(Shape):
    """矩形类"""
    
    def __init__(self, width, height):
        super().__init__("矩形")
        self.width = width
        self.height = height
    
    def area(self):
        """实现抽象方法"""
        return self.width * self.height
    
    def perimeter(self):
        """实现抽象方法"""
        return 2 * (self.width + self.height)
    
    def is_square(self):
        """矩形特有方法"""
        return self.width == self.height

class Circle(Shape):
    """圆形类"""
    
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius = radius
    
    def area(self):
        """实现抽象方法"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """实现抽象方法"""
        return 2 * math.pi * self.radius
    
    def diameter(self):
        """圆形特有方法"""
        return 2 * self.radius

class Triangle(Shape):
    """三角形类"""
    
    def __init__(self, a, b, c):
        super().__init__("三角形")
        self.a = a
        self.b = b
        self.c = c
        
        # 验证三角形的有效性
        if not self._is_valid_triangle():
            raise ValueError("无效的三角形边长")
    
    def _is_valid_triangle(self):
        """验证三角形是否有效"""
        return (self.a + self.b > self.c and 
                self.a + self.c > self.b and 
                self.b + self.c > self.a)
    
    def area(self):
        """实现抽象方法（海伦公式）"""
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        """实现抽象方法"""
        return self.a + self.b + self.c
    
    def triangle_type(self):
        """三角形特有方法：判断三角形类型"""
        sides = sorted([self.a, self.b, self.c])
        if sides[0] == sides[1] == sides[2]:
            return "等边三角形"
        elif sides[0] == sides[1] or sides[1] == sides[2]:
            return "等腰三角形"
        elif sides[0]**2 + sides[1]**2 == sides[2]**2:
            return "直角三角形"
        else:
            return "普通三角形"

# 3. 车辆抽象类示例
class Vehicle(ABC):
    """车辆抽象基类"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        self.is_running = False
    
    @abstractmethod
    def start_engine(self):
        """抽象方法：启动引擎"""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """抽象方法：停止引擎"""
        pass
    
    @abstractmethod
    def get_fuel_type(self):
        """抽象方法：获取燃料类型"""
        pass
    
    def accelerate(self, speed_increase):
        """具体方法：加速"""
        if not self.is_running:
            return f"{self.brand} {self.model} 引擎未启动，无法加速"
        
        self.speed += speed_increase
        return f"{self.brand} {self.model} 加速到 {self.speed} km/h"
    
    def brake(self, speed_decrease):
        """具体方法：刹车"""
        self.speed = max(0, self.speed - speed_decrease)
        return f"{self.brand} {self.model} 减速到 {self.speed} km/h"
    
    def get_info(self):
        """具体方法：获取车辆信息"""
        status = "运行中" if self.is_running else "停止"
        return f"{self.year} {self.brand} {self.model}，当前状态: {status}，速度: {self.speed} km/h"

class Car(Vehicle):
    """汽车类"""
    
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
    
    def start_engine(self):
        """实现抽象方法"""
        self.is_running = True
        return f"{self.brand} {self.model} 汽油引擎启动"
    
    def stop_engine(self):
        """实现抽象方法"""
        self.is_running = False
        self.speed = 0
        return f"{self.brand} {self.model} 引擎停止"
    
    def get_fuel_type(self):
        """实现抽象方法"""
        return "汽油"
    
    def honk(self):
        """汽车特有方法"""
        return f"{self.brand} {self.model} 鸣笛：嘀嘀！"

class ElectricCar(Vehicle):
    """电动汽车类"""
    
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        self.battery_level = 100  # 电池电量百分比
    
    def start_engine(self):
        """实现抽象方法"""
        if self.battery_level > 0:
            self.is_running = True
            return f"{self.brand} {self.model} 电动系统启动"
        else:
            return f"{self.brand} {self.model} 电池电量不足，无法启动"
    
    def stop_engine(self):
        """实现抽象方法"""
        self.is_running = False
        self.speed = 0
        return f"{self.brand} {self.model} 电动系统关闭"
    
    def get_fuel_type(self):
        """实现抽象方法"""
        return "电力"
    
    def charge_battery(self, charge_amount):
        """电动车特有方法"""
        self.battery_level = min(100, self.battery_level + charge_amount)
        return f"{self.brand} {self.model} 充电完成，电量: {self.battery_level}%"

class Motorcycle(Vehicle):
    """摩托车类"""
    
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size
    
    def start_engine(self):
        """实现抽象方法"""
        self.is_running = True
        return f"{self.brand} {self.model} {self.engine_size}cc 引擎启动"
    
    def stop_engine(self):
        """实现抽象方法"""
        self.is_running = False
        self.speed = 0
        return f"{self.brand} {self.model} 引擎停止"
    
    def get_fuel_type(self):
        """实现抽象方法"""
        return "汽油"
    
    def wheelie(self):
        """摩托车特有方法"""
        if self.speed > 30:
            return f"{self.brand} {self.model} 做后轮着地特技"
        else:
            return f"{self.brand} {self.model} 速度太慢，无法做特技"

# 4. 数据处理抽象类示例
class DataProcessor(ABC):
    """数据处理器抽象基类"""
    
    def __init__(self, name):
        self.name = name
        self.processed_count = 0
    
    @abstractmethod
    def process_data(self, data):
        """抽象方法：处理数据"""
        pass
    
    @abstractmethod
    def validate_data(self, data):
        """抽象方法：验证数据"""
        pass
    
    def process_batch(self, data_list):
        """具体方法：批量处理数据"""
        results = []
        for data in data_list:
            if self.validate_data(data):
                result = self.process_data(data)
                results.append(result)
                self.processed_count += 1
            else:
                results.append(f"无效数据: {data}")
        return results
    
    def get_stats(self):
        """具体方法：获取处理统计"""
        return f"{self.name} 已处理 {self.processed_count} 条数据"

class NumberProcessor(DataProcessor):
    """数字处理器"""
    
    def __init__(self):
        super().__init__("数字处理器")
    
    def validate_data(self, data):
        """实现抽象方法：验证数据是否为数字"""
        try:
            float(data)
            return True
        except (ValueError, TypeError):
            return False
    
    def process_data(self, data):
        """实现抽象方法：处理数字数据"""
        number = float(data)
        return {
            "original": data,
            "value": number,
            "square": number ** 2,
            "sqrt": math.sqrt(abs(number)),
            "is_positive": number > 0
        }

class TextProcessor(DataProcessor):
    """文本处理器"""
    
    def __init__(self):
        super().__init__("文本处理器")
    
    def validate_data(self, data):
        """实现抽象方法：验证数据是否为字符串"""
        return isinstance(data, str) and len(data.strip()) > 0
    
    def process_data(self, data):
        """实现抽象方法：处理文本数据"""
        text = str(data).strip()
        return {
            "original": data,
            "length": len(text),
            "uppercase": text.upper(),
            "lowercase": text.lower(),
            "word_count": len(text.split()),
            "reversed": text[::-1]
        }

class EmailProcessor(DataProcessor):
    """邮箱处理器"""
    
    def __init__(self):
        super().__init__("邮箱处理器")
    
    def validate_data(self, data):
        """实现抽象方法：验证邮箱格式"""
        import re
        if not isinstance(data, str):
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, data) is not None
    
    def process_data(self, data):
        """实现抽象方法：处理邮箱数据"""
        email = str(data).strip().lower()
        username, domain = email.split('@')
        return {
            "original": data,
            "email": email,
            "username": username,
            "domain": domain,
            "is_gmail": domain == "gmail.com",
            "domain_parts": domain.split('.')
        }

# 5. 演示函数
def demonstrate_animal_abstraction():
    """演示动物抽象类"""
    print("=== 动物抽象类演示 ===")
    
    # 尝试实例化抽象类会报错
    try:
        # animal = Animal("测试", "动物")  # 这会报错
        pass
    except TypeError as e:
        print(f"无法实例化抽象类: {e}")
    
    # 创建具体子类实例
    animals = [
        Dog("旺财", "金毛"),
        Cat("咪咪", "橘色"),
        Bird("小鸟", 25)
    ]
    
    for animal in animals:
        print(f"\n{animal.get_info()}")
        print(f"声音: {animal.make_sound()}")
        print(f"移动: {animal.move()}")
        print(f"吃饭: {animal.eat()}")
        print(f"睡觉: {animal.sleep()}")
        
        # 调用特有方法
        if hasattr(animal, 'fetch'):
            print(f"特技: {animal.fetch()}")
        elif hasattr(animal, 'climb'):
            print(f"特技: {animal.climb()}")
        elif hasattr(animal, 'fly'):
            print(f"特技: {animal.fly()}")

def demonstrate_shape_abstraction():
    """演示形状抽象类"""
    print("\n=== 形状抽象类演示 ===")
    
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Triangle(3, 4, 5)
    ]
    
    for shape in shapes:
        print(f"\n{shape.describe()}")
        
        # 调用特有方法
        if hasattr(shape, 'is_square'):
            print(f"是否为正方形: {shape.is_square()}")
        elif hasattr(shape, 'diameter'):
            print(f"直径: {shape.diameter():.2f}")
        elif hasattr(shape, 'triangle_type'):
            print(f"三角形类型: {shape.triangle_type()}")
    
    # 比较面积
    print(f"\n面积比较: {shapes[0].compare_area(shapes[1])}")

def demonstrate_vehicle_abstraction():
    """演示车辆抽象类"""
    print("\n=== 车辆抽象类演示 ===")
    
    vehicles = [
        Car("丰田", "凯美瑞", 2023, 4),
        ElectricCar("特斯拉", "Model 3", 2023, 75),
        Motorcycle("本田", "CBR600", 2023, 600)
    ]
    
    for vehicle in vehicles:
        print(f"\n=== {vehicle.get_info()} ===")
        print(f"燃料类型: {vehicle.get_fuel_type()}")
        print(vehicle.start_engine())
        print(vehicle.accelerate(50))
        
        # 调用特有方法
        if hasattr(vehicle, 'honk'):
            print(vehicle.honk())
        elif hasattr(vehicle, 'charge_battery'):
            print(vehicle.charge_battery(20))
        elif hasattr(vehicle, 'wheelie'):
            print(vehicle.wheelie())
        
        print(vehicle.brake(30))
        print(vehicle.stop_engine())

def demonstrate_data_processor_abstraction():
    """演示数据处理器抽象类"""
    print("\n=== 数据处理器抽象类演示 ===")
    
    processors = [
        NumberProcessor(),
        TextProcessor(),
        EmailProcessor()
    ]
    
    # 测试数据
    test_data = [
        ["123", "45.6", "-7.8", "abc", "0"],
        ["Hello World", "Python", "", "  ", "Programming"],
        ["user@example.com", "test@gmail.com", "invalid-email", "admin@company.org"]
    ]
    
    for i, processor in enumerate(processors):
        print(f"\n=== {processor.name} ===")
        results = processor.process_batch(test_data[i])
        
        for result in results:
            if isinstance(result, dict):
                print(f"处理结果: {result}")
            else:
                print(result)
        
        print(processor.get_stats())

# 6. 抽象类的高级特性
class AdvancedShape(ABC):
    """高级形状抽象类 - 演示更多抽象特性"""
    
    def __init__(self, name):
        self.name = name
        self._creation_time = None
    
    @abstractmethod
    def area(self):
        """抽象方法：计算面积"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """抽象方法：计算周长"""
        pass
    
    @property
    @abstractmethod
    def vertices(self):
        """抽象属性：顶点数量"""
        pass
    
    def __str__(self):
        """具体方法：字符串表示"""
        return f"{self.name}(面积: {self.area():.2f}, 周长: {self.perimeter():.2f}, 顶点: {self.vertices})"
    
    def __eq__(self, other):
        """具体方法：相等比较"""
        if not isinstance(other, AdvancedShape):
            return False
        return abs(self.area() - other.area()) < 0.001
    
    def __lt__(self, other):
        """具体方法：小于比较"""
        if not isinstance(other, AdvancedShape):
            return NotImplemented
        return self.area() < other.area()

class AdvancedRectangle(AdvancedShape):
    """高级矩形类"""
    
    def __init__(self, width, height):
        super().__init__("高级矩形")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    @property
    def vertices(self):
        return 4

class AdvancedCircle(AdvancedShape):
    """高级圆形类"""
    
    def __init__(self, radius):
        super().__init__("高级圆形")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    @property
    def vertices(self):
        return 0  # 圆形没有顶点

def demonstrate_advanced_abstraction():
    """演示高级抽象特性"""
    print("\n=== 高级抽象特性演示 ===")
    
    shapes = [
        AdvancedRectangle(4, 4),  # 正方形
        AdvancedCircle(2.26),     # 面积约等于正方形
        AdvancedRectangle(2, 8)   # 长矩形
    ]
    
    for shape in shapes:
        print(shape)
    
    # 比较形状
    print(f"\n形状比较:")
    print(f"{shapes[0].name} == {shapes[1].name}: {shapes[0] == shapes[1]}")
    print(f"{shapes[0].name} < {shapes[2].name}: {shapes[0] < shapes[2]}")
    
    # 排序
    sorted_shapes = sorted(shapes)
    print(f"\n按面积排序:")
    for shape in sorted_shapes:
        print(f"  {shape}")

if __name__ == "__main__":
    # 演示动物抽象类
    demonstrate_animal_abstraction()
    
    # 演示形状抽象类
    demonstrate_shape_abstraction()
    
    # 演示车辆抽象类
    demonstrate_vehicle_abstraction()
    
    # 演示数据处理器抽象类
    demonstrate_data_processor_abstraction()
    
    # 演示高级抽象特性
    demonstrate_advanced_abstraction()
    
    print("\n=== 抽象类的核心要点 ===")
    print("1. 抽象类不能被实例化")
    print("2. 抽象方法必须在子类中实现")
    print("3. 可以包含具体方法和抽象方法")
    print("4. 提供代码复用和接口规范")
    print("5. 强制子类实现特定方法")
    print("6. 支持多态和继承")
    print("7. 使用@abstractmethod装饰器")
    print("8. 继承自ABC类或使用ABCMeta元类")