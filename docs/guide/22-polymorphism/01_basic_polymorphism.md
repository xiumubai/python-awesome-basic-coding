# 多态的基本概念和原理

## 什么是多态

多态（Polymorphism）是面向对象编程的核心概念之一，它允许不同的对象对同一消息做出不同的响应。简单来说，多态就是"同一接口，不同实现"。

## 多态的基本示例

### 动物叫声示例

```python
class Animal:
    """动物基类"""
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        """动物发出声音的方法"""
        pass
    
    def introduce(self):
        """介绍动物"""
        return f"我是{self.name}"

class Dog(Animal):
    """狗类"""
    def make_sound(self):
        return "汪汪汪！"

class Cat(Animal):
    """猫类"""
    def make_sound(self):
        return "喵喵喵！"

class Cow(Animal):
    """牛类"""
    def make_sound(self):
        return "哞哞哞！"

# 多态的体现：同一个函数处理不同类型的对象
def animal_concert(animals):
    """动物音乐会 - 展示多态"""
    print("=== 动物音乐会开始 ===")
    for animal in animals:
        print(f"{animal.introduce()}，我的叫声是：{animal.make_sound()}")
    print("=== 音乐会结束 ===\n")

# 创建不同的动物对象
dog = Dog("小黄")
cat = Cat("小花")
cow = Cow("大壮")

# 将不同类型的对象放在同一个列表中
animals = [dog, cat, cow]

# 同一个函数处理不同类型的对象
animal_concert(animals)
```

### 图形面积计算示例

```python
import math

class Shape:
    """图形基类"""
    def area(self):
        """计算面积的方法"""
        raise NotImplementedError("子类必须实现area方法")
    
    def perimeter(self):
        """计算周长的方法"""
        raise NotImplementedError("子类必须实现perimeter方法")

class Rectangle(Shape):
    """矩形类"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"矩形(宽:{self.width}, 高:{self.height})"

class Circle(Shape):
    """圆形类"""
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"圆形(半径:{self.radius})"

class Triangle(Shape):
    """三角形类"""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # 使用海伦公式计算面积
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def __str__(self):
        return f"三角形(边长:{self.a}, {self.b}, {self.c})"

# 多态函数：计算图形信息
def calculate_shape_info(shapes):
    """计算图形信息 - 展示多态"""
    print("=== 图形计算结果 ===")
    total_area = 0
    total_perimeter = 0
    
    for shape in shapes:
        area = shape.area()
        perimeter = shape.perimeter()
        total_area += area
        total_perimeter += perimeter
        
        print(f"{shape}:")
        print(f"  面积: {area:.2f}")
        print(f"  周长: {perimeter:.2f}")
        print()
    
    print(f"总面积: {total_area:.2f}")
    print(f"总周长: {total_perimeter:.2f}")
    print("=== 计算完成 ===\n")

# 创建不同的图形对象
rectangle = Rectangle(5, 3)
circle = Circle(4)
triangle = Triangle(3, 4, 5)

# 将不同类型的图形对象放在同一个列表中
shapes = [rectangle, circle, triangle]

# 同一个函数处理不同类型的图形对象
calculate_shape_info(shapes)
```

## 多态的优势

### 1. 代码复用

```python
class Vehicle:
    """交通工具基类"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return "启动中..."
    
    def stop(self):
        return "停止中..."
    
    def get_info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    """汽车类"""
    def start(self):
        return f"{self.get_info()} 汽车引擎启动，准备上路！"
    
    def stop(self):
        return f"{self.get_info()} 汽车停车，引擎关闭。"

class Motorcycle(Vehicle):
    """摩托车类"""
    def start(self):
        return f"{self.get_info()} 摩托车引擎轰鸣，准备出发！"
    
    def stop(self):
        return f"{self.get_info()} 摩托车停车，引擎熄火。"

class Bicycle(Vehicle):
    """自行车类"""
    def start(self):
        return f"{self.get_info()} 开始踩踏板，自行车前进！"
    
    def stop(self):
        return f"{self.get_info()} 停止踩踏，自行车停下。"

# 通用的交通工具管理函数
def manage_vehicles(vehicles):
    """管理交通工具 - 展示代码复用的优势"""
    print("=== 交通工具管理系统 ===")
    
    # 启动所有交通工具
    print("启动所有交通工具:")
    for vehicle in vehicles:
        print(f"  {vehicle.start()}")
    
    print("\n所有交通工具正在运行...\n")
    
    # 停止所有交通工具
    print("停止所有交通工具:")
    for vehicle in vehicles:
        print(f"  {vehicle.stop()}")
    
    print("=== 管理完成 ===\n")

# 创建不同类型的交通工具
car = Car("丰田", "卡罗拉")
motorcycle = Motorcycle("本田", "CBR600")
bicycle = Bicycle("捷安特", "ATX770")

vehicles = [car, motorcycle, bicycle]
manage_vehicles(vehicles)
```

### 2. 可扩展性

```python
# 添加新的交通工具类型，无需修改现有代码
class Boat(Vehicle):
    """船类"""
    def start(self):
        return f"{self.get_info()} 船只启动，准备航行！"
    
    def stop(self):
        return f"{self.get_info()} 船只停靠，引擎关闭。"

class Airplane(Vehicle):
    """飞机类"""
    def start(self):
        return f"{self.get_info()} 飞机引擎启动，准备起飞！"
    
    def stop(self):
        return f"{self.get_info()} 飞机降落，引擎关闭。"

# 扩展交通工具列表
boat = Boat("雅马哈", "快艇200")
airplane = Airplane("波音", "737")

# 原有的管理函数无需修改，就能处理新的交通工具类型
all_vehicles = [car, motorcycle, bicycle, boat, airplane]
manage_vehicles(all_vehicles)
```

## 多态的实现机制

### 1. 方法重写（Method Overriding）

```python
class Processor:
    """处理器基类"""
    def process(self, data):
        """处理数据的方法"""
        return f"基础处理: {data}"

class TextProcessor(Processor):
    """文本处理器"""
    def process(self, data):
        """重写处理方法"""
        return f"文本处理: {data.upper()}"

class NumberProcessor(Processor):
    """数字处理器"""
    def process(self, data):
        """重写处理方法"""
        return f"数字处理: {data * 2}"

class ListProcessor(Processor):
    """列表处理器"""
    def process(self, data):
        """重写处理方法"""
        return f"列表处理: {sorted(data)}"

# 演示方法重写的多态
def demonstrate_method_overriding():
    """演示方法重写"""
    print("=== 方法重写演示 ===")
    
    processors = [
        TextProcessor(),
        NumberProcessor(),
        ListProcessor()
    ]
    
    test_data = [
        "hello world",
        42,
        [3, 1, 4, 1, 5]
    ]
    
    for processor, data in zip(processors, test_data):
        result = processor.process(data)
        print(f"{processor.__class__.__name__}: {result}")
    
    print("=== 演示完成 ===\n")

demonstrate_method_overriding()
```

### 2. 动态绑定

```python
class Calculator:
    """计算器基类"""
    def calculate(self, a, b):
        """计算方法"""
        raise NotImplementedError("子类必须实现calculate方法")
    
    def get_operation_name(self):
        """获取操作名称"""
        return "未知操作"

class AddCalculator(Calculator):
    """加法计算器"""
    def calculate(self, a, b):
        return a + b
    
    def get_operation_name(self):
        return "加法"

class MultiplyCalculator(Calculator):
    """乘法计算器"""
    def calculate(self, a, b):
        return a * b
    
    def get_operation_name(self):
        return "乘法"

class PowerCalculator(Calculator):
    """幂运算计算器"""
    def calculate(self, a, b):
        return a ** b
    
    def get_operation_name(self):
        return "幂运算"

# 动态绑定演示
def demonstrate_dynamic_binding():
    """演示动态绑定"""
    print("=== 动态绑定演示 ===")
    
    # 在运行时决定使用哪个计算器
    calculators = [
        AddCalculator(),
        MultiplyCalculator(),
        PowerCalculator()
    ]
    
    a, b = 3, 4
    
    for calc in calculators:
        # 动态绑定：在运行时确定调用哪个方法
        result = calc.calculate(a, b)
        operation = calc.get_operation_name()
        print(f"{operation}: {a} 和 {b} 的结果是 {result}")
    
    print("=== 演示完成 ===\n")

demonstrate_dynamic_binding()
```

## 多态的核心要点

```python
def demonstrate_polymorphism_principles():
    """演示多态的核心要点"""
    print("=== 多态核心要点 ===")
    
    print("1. 同一接口，不同实现")
    print("   - 所有动物都有make_sound方法，但实现不同")
    
    print("\n2. 运行时绑定")
    print("   - 程序在运行时决定调用哪个具体的方法")
    
    print("\n3. 代码复用")
    print("   - 同一个函数可以处理不同类型的对象")
    
    print("\n4. 可扩展性")
    print("   - 添加新类型无需修改现有代码")
    
    print("\n5. 抽象性")
    print("   - 客户端代码不需要知道具体的实现细节")
    
    print("=== 要点总结完成 ===\n")

demonstrate_polymorphism_principles()
```

## 运行示例

当你运行这个文件时，你会看到多态在不同场景下的应用：

1. **动物音乐会**：展示基本的多态概念
2. **图形计算**：展示多态在数学计算中的应用
3. **交通工具管理**：展示多态的代码复用优势
4. **处理器系统**：展示方法重写的多态实现
5. **计算器系统**：展示动态绑定的概念

## 学习要点

1. **理解概念**：多态是"同一接口，不同实现"
2. **掌握优势**：代码复用、可扩展性、抽象性
3. **学会应用**：在设计类层次结构时考虑多态
4. **注意原则**：遵循里氏替换原则和开闭原则

多态是面向对象编程的精髓，掌握多态能让你写出更加灵活和可维护的代码。