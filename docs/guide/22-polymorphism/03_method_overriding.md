# 方法重写实现多态

## 什么是方法重写

方法重写（Method Overriding）是面向对象编程中的一个重要概念，它允许子类重新定义父类中的方法，从而实现不同的行为。这是实现多态的主要机制之一。

## 基本的方法重写

### 动物行为示例

```python
class Animal:
    """动物基类"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        """发出声音 - 基类方法"""
        return "动物发出声音"
    
    def move(self):
        """移动 - 基类方法"""
        return "动物在移动"
    
    def eat(self):
        """进食 - 基类方法"""
        return "动物在进食"
    
    def introduce(self):
        """自我介绍"""
        return f"我是{self.name}，是一只{self.species}"

class Dog(Animal):
    """狗类 - 重写父类方法"""
    def __init__(self, name, breed):
        super().__init__(name, "狗")
        self.breed = breed
    
    def make_sound(self):
        """重写发声方法"""
        return "汪汪汪！"
    
    def move(self):
        """重写移动方法"""
        return "狗在奔跑"
    
    def fetch(self):
        """狗特有的方法"""
        return f"{self.name}去捡球了！"

class Cat(Animal):
    """猫类 - 重写父类方法"""
    def __init__(self, name, color):
        super().__init__(name, "猫")
        self.color = color
    
    def make_sound(self):
        """重写发声方法"""
        return "喵喵喵！"
    
    def move(self):
        """重写移动方法"""
        return "猫在优雅地走动"
    
    def climb(self):
        """猫特有的方法"""
        return f"{self.name}爬到了树上！"

class Bird(Animal):
    """鸟类 - 重写父类方法"""
    def __init__(self, name, wing_span):
        super().__init__(name, "鸟")
        self.wing_span = wing_span
    
    def make_sound(self):
        """重写发声方法"""
        return "啾啾啾！"
    
    def move(self):
        """重写移动方法"""
        return "鸟在天空中飞翔"
    
    def fly(self):
        """鸟特有的方法"""
        return f"{self.name}展开{self.wing_span}cm的翅膀飞翔！"

# 演示方法重写
def demonstrate_method_overriding():
    """演示方法重写"""
    print("=== 方法重写演示 ===")
    
    # 创建不同的动物对象
    animals = [
        Dog("旺财", "金毛"),
        Cat("咪咪", "橘色"),
        Bird("小鸟", 25)
    ]
    
    # 展示多态行为
    for animal in animals:
        print(f"\n{animal.introduce()}")
        print(f"声音: {animal.make_sound()}")
        print(f"移动: {animal.move()}")
        print(f"进食: {animal.eat()}")
        
        # 调用特有方法
        if isinstance(animal, Dog):
            print(f"特技: {animal.fetch()}")
        elif isinstance(animal, Cat):
            print(f"特技: {animal.climb()}")
        elif isinstance(animal, Bird):
            print(f"特技: {animal.fly()}")
    
    print("\n=== 演示完成 ===\n")

demonstrate_method_overriding()
```

## super()函数的使用

### 扩展父类方法

```python
class Vehicle:
    """交通工具基类"""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        """启动"""
        if not self.is_running:
            self.is_running = True
            return f"{self.brand} {self.model} 启动了"
        return f"{self.brand} {self.model} 已经在运行中"
    
    def stop(self):
        """停止"""
        if self.is_running:
            self.is_running = False
            return f"{self.brand} {self.model} 停止了"
        return f"{self.brand} {self.model} 已经停止"
    
    def get_info(self):
        """获取信息"""
        status = "运行中" if self.is_running else "停止"
        return f"{self.year}年 {self.brand} {self.model} - 状态: {status}"

class Car(Vehicle):
    """汽车类 - 扩展父类方法"""
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)  # 调用父类构造函数
        self.fuel_type = fuel_type
        self.fuel_level = 100
    
    def start(self):
        """重写启动方法，添加燃料检查"""
        if self.fuel_level <= 0:
            return f"{self.brand} {self.model} 燃料不足，无法启动"
        
        # 调用父类的start方法
        result = super().start()
        if self.is_running:
            return f"{result}，{self.fuel_type}引擎正在运转"
        return result
    
    def stop(self):
        """重写停止方法，添加引擎冷却"""
        result = super().stop()  # 调用父类的stop方法
        if not self.is_running:
            return f"{result}，引擎正在冷却"
        return result
    
    def refuel(self, amount):
        """加油"""
        self.fuel_level = min(100, self.fuel_level + amount)
        return f"加油完成，当前油量: {self.fuel_level}%"
    
    def get_info(self):
        """重写信息获取，添加燃料信息"""
        base_info = super().get_info()  # 调用父类方法
        return f"{base_info}, 燃料类型: {self.fuel_type}, 油量: {self.fuel_level}%"

class ElectricCar(Car):
    """电动汽车类 - 进一步重写方法"""
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year, "电动")  # 调用父类构造函数
        self.battery_capacity = battery_capacity
        self.charge_level = 100
    
    def start(self):
        """重写启动方法，检查电池"""
        if self.charge_level <= 0:
            return f"{self.brand} {self.model} 电池没电，无法启动"
        
        # 调用Vehicle的start方法（跳过Car的start）
        if not self.is_running:
            self.is_running = True
            return f"{self.brand} {self.model} 静音启动，电机开始工作"
        return f"{self.brand} {self.model} 已经在运行中"
    
    def charge(self, amount):
        """充电"""
        self.charge_level = min(100, self.charge_level + amount)
        return f"充电完成，当前电量: {self.charge_level}%"
    
    def refuel(self, amount):
        """重写加油方法，电动车不需要加油"""
        return "电动汽车不需要加油，请使用充电功能"
    
    def get_info(self):
        """重写信息获取"""
        base_info = super(Vehicle, self).get_info()  # 直接调用Vehicle的方法
        return f"{base_info}, 电池容量: {self.battery_capacity}kWh, 电量: {self.charge_level}%"

# 演示super()的使用
def demonstrate_super_usage():
    """演示super()的使用"""
    print("=== super()使用演示 ===")
    
    # 创建不同类型的车辆
    vehicles = [
        Vehicle("通用", "基础车型", 2020),
        Car("丰田", "卡罗拉", 2021, "汽油"),
        ElectricCar("特斯拉", "Model 3", 2022, 75)
    ]
    
    for vehicle in vehicles:
        print(f"\n--- {vehicle.__class__.__name__} ---")
        print(vehicle.get_info())
        print(vehicle.start())
        
        # 特殊操作
        if isinstance(vehicle, ElectricCar):
            print(vehicle.refuel(20))  # 尝试加油
            print(vehicle.charge(10))  # 充电
        elif isinstance(vehicle, Car):
            print(vehicle.refuel(20))  # 加油
        
        print(vehicle.stop())
        print(vehicle.get_info())
    
    print("\n=== 演示完成 ===\n")

demonstrate_super_usage()
```

## 方法解析顺序（MRO）

### 多重继承中的方法重写

```python
class A:
    """基类A"""
    def method(self):
        return "A的方法"
    
    def common_method(self):
        return "A的通用方法"

class B(A):
    """继承自A的类B"""
    def method(self):
        return "B的方法"
    
    def b_method(self):
        return "B特有的方法"

class C(A):
    """继承自A的类C"""
    def method(self):
        return "C的方法"
    
    def common_method(self):
        return "C的通用方法"
    
    def c_method(self):
        return "C特有的方法"

class D(B, C):
    """多重继承：同时继承B和C"""
    def d_method(self):
        return "D特有的方法"
    
    def combined_method(self):
        """组合多个父类的方法"""
        # 使用super()调用方法解析顺序中的下一个方法
        b_result = super().method()
        return f"D组合方法，调用了: {b_result}"

class E(B, C):
    """另一个多重继承类，重写方法"""
    def method(self):
        """重写方法，调用所有父类的方法"""
        results = []
        
        # 手动调用特定父类的方法
        results.append(f"B: {B.method(self)}")
        results.append(f"C: {C.method(self)}")
        results.append(f"A: {A.method(self)}")
        
        return f"E的方法，包含: {', '.join(results)}"

# 演示方法解析顺序
def demonstrate_mro():
    """演示方法解析顺序"""
    print("=== 方法解析顺序（MRO）演示 ===")
    
    # 创建对象
    d = D()
    e = E()
    
    print("1. 类的继承关系:")
    print(f"   D继承自: {[cls.__name__ for cls in D.__bases__]}")
    print(f"   E继承自: {[cls.__name__ for cls in E.__bases__]}")
    
    print("\n2. 方法解析顺序（MRO）:")
    print(f"   D的MRO: {[cls.__name__ for cls in D.__mro__]}")
    print(f"   E的MRO: {[cls.__name__ for cls in E.__mro__]}")
    
    print("\n3. 方法调用结果:")
    print(f"   d.method(): {d.method()}")
    print(f"   d.common_method(): {d.common_method()}")
    print(f"   d.combined_method(): {d.combined_method()}")
    
    print(f"\n   e.method(): {e.method()}")
    print(f"   e.common_method(): {e.common_method()}")
    
    print("\n4. 特有方法调用:")
    print(f"   d.b_method(): {d.b_method()}")
    print(f"   d.c_method(): {d.c_method()}")
    print(f"   d.d_method(): {d.d_method()}")
    
    print("\n=== 演示完成 ===\n")

demonstrate_mro()
```

## 抽象方法重写

### 模板方法模式

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """数据处理器抽象基类"""
    
    def process_data(self, data):
        """模板方法：定义处理流程"""
        print(f"开始处理数据: {self.__class__.__name__}")
        
        # 1. 验证数据
        if not self.validate_data(data):
            return "数据验证失败"
        
        # 2. 预处理
        processed_data = self.preprocess(data)
        
        # 3. 核心处理（抽象方法，子类必须实现）
        result = self.core_process(processed_data)
        
        # 4. 后处理
        final_result = self.postprocess(result)
        
        print(f"数据处理完成: {self.__class__.__name__}")
        return final_result
    
    def validate_data(self, data):
        """验证数据（可以被子类重写）"""
        return data is not None
    
    def preprocess(self, data):
        """预处理（可以被子类重写）"""
        print("  执行基础预处理")
        return data
    
    @abstractmethod
    def core_process(self, data):
        """核心处理（抽象方法，子类必须实现）"""
        pass
    
    def postprocess(self, result):
        """后处理（可以被子类重写）"""
        print("  执行基础后处理")
        return result

class TextProcessor(DataProcessor):
    """文本处理器"""
    
    def validate_data(self, data):
        """重写验证方法"""
        return isinstance(data, str) and len(data) > 0
    
    def preprocess(self, data):
        """重写预处理方法"""
        super().preprocess(data)  # 调用父类方法
        print("  执行文本预处理：去除空格")
        return data.strip()
    
    def core_process(self, data):
        """实现抽象方法：文本核心处理"""
        print("  执行文本核心处理：转换为大写")
        return data.upper()
    
    def postprocess(self, result):
        """重写后处理方法"""
        super().postprocess(result)  # 调用父类方法
        print("  执行文本后处理：添加前缀")
        return f"PROCESSED: {result}"

class NumberProcessor(DataProcessor):
    """数字处理器"""
    
    def validate_data(self, data):
        """重写验证方法"""
        try:
            float(data)
            return True
        except (ValueError, TypeError):
            return False
    
    def preprocess(self, data):
        """重写预处理方法"""
        super().preprocess(data)
        print("  执行数字预处理：转换为浮点数")
        return float(data)
    
    def core_process(self, data):
        """实现抽象方法：数字核心处理"""
        print("  执行数字核心处理：计算平方")
        return data ** 2
    
    def postprocess(self, result):
        """重写后处理方法"""
        super().postprocess(result)
        print("  执行数字后处理：格式化")
        return f"结果: {result:.2f}"

class ListProcessor(DataProcessor):
    """列表处理器"""
    
    def validate_data(self, data):
        """重写验证方法"""
        return isinstance(data, list) and len(data) > 0
    
    def preprocess(self, data):
        """重写预处理方法"""
        super().preprocess(data)
        print("  执行列表预处理：过滤None值")
        return [item for item in data if item is not None]
    
    def core_process(self, data):
        """实现抽象方法：列表核心处理"""
        print("  执行列表核心处理：排序")
        return sorted(data)
    
    def postprocess(self, result):
        """重写后处理方法"""
        super().postprocess(result)
        print("  执行列表后处理：转换为字符串")
        return f"排序结果: {result}"

# 演示抽象方法重写
def demonstrate_abstract_method_overriding():
    """演示抽象方法重写"""
    print("=== 抽象方法重写演示 ===")
    
    # 创建不同的处理器
    processors = [
        TextProcessor(),
        NumberProcessor(),
        ListProcessor()
    ]
    
    # 测试数据
    test_data = [
        "  hello world  ",
        "42",
        [3, 1, None, 4, 1, 5, None]
    ]
    
    # 处理数据
    for processor, data in zip(processors, test_data):
        print(f"\n--- 使用 {processor.__class__.__name__} ---")
        print(f"输入数据: {data}")
        result = processor.process_data(data)
        print(f"最终结果: {result}")
    
    print("\n=== 演示完成 ===\n")

demonstrate_abstract_method_overriding()
```

## 方法重写的最佳实践

### 1. 保持接口一致性

```python
class Shape:
    """图形基类"""
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """计算面积"""
        raise NotImplementedError("子类必须实现area方法")
    
    def perimeter(self):
        """计算周长"""
        raise NotImplementedError("子类必须实现perimeter方法")
    
    def describe(self):
        """描述图形"""
        return f"{self.name}: 面积={self.area():.2f}, 周长={self.perimeter():.2f}"

class Rectangle(Shape):
    """矩形类 - 正确的方法重写"""
    def __init__(self, width, height):
        super().__init__("矩形")
        self.width = width
        self.height = height
    
    def area(self):
        """重写面积计算 - 保持返回类型一致"""
        return self.width * self.height
    
    def perimeter(self):
        """重写周长计算 - 保持返回类型一致"""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """圆形类 - 正确的方法重写"""
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius = radius
    
    def area(self):
        """重写面积计算"""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """重写周长计算"""
        import math
        return 2 * math.pi * self.radius

# 错误示例：破坏接口一致性
class BadShape(Shape):
    """错误的图形类 - 破坏接口一致性"""
    def __init__(self):
        super().__init__("错误图形")
    
    def area(self):
        """错误：返回字符串而不是数字"""
        return "无法计算面积"
    
    def perimeter(self):
        """错误：抛出异常而不是返回数值"""
        raise ValueError("无法计算周长")

# 演示接口一致性
def demonstrate_interface_consistency():
    """演示接口一致性的重要性"""
    print("=== 接口一致性演示 ===")
    
    # 正确的图形
    good_shapes = [
        Rectangle(5, 3),
        Circle(4)
    ]
    
    print("1. 正确的方法重写:")
    for shape in good_shapes:
        try:
            print(f"  {shape.describe()}")
        except Exception as e:
            print(f"  错误: {e}")
    
    # 错误的图形
    bad_shape = BadShape()
    print("\n2. 错误的方法重写:")
    try:
        print(f"  {bad_shape.describe()}")
    except Exception as e:
        print(f"  错误: {e}")
    
    print("\n=== 演示完成 ===\n")

demonstrate_interface_consistency()
```

### 2. 使用装饰器增强方法重写

```python
import time
from functools import wraps

def timing_decorator(func):
    """计时装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"  {func.__name__} 执行时间: {end_time - start_time:.4f}秒")
        return result
    return wrapper

def logging_decorator(func):
    """日志装饰器"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"  调用 {self.__class__.__name__}.{func.__name__}")
        result = func(self, *args, **kwargs)
        print(f"  {self.__class__.__name__}.{func.__name__} 完成")
        return result
    return wrapper

class Worker:
    """工作者基类"""
    def __init__(self, name):
        self.name = name
    
    @logging_decorator
    def work(self):
        """工作方法"""
        return f"{self.name} 正在工作"
    
    @timing_decorator
    def calculate(self, n):
        """计算方法"""
        return sum(range(n))

class Developer(Worker):
    """开发者类"""
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
    
    @logging_decorator
    def work(self):
        """重写工作方法，保持装饰器"""
        return f"{self.name} 正在用{self.language}编程"
    
    @timing_decorator
    def calculate(self, n):
        """重写计算方法，使用更复杂的算法"""
        # 模拟更复杂的计算
        result = 0
        for i in range(n):
            result += i * i
        return result

class Designer(Worker):
    """设计师类"""
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool
    
    @logging_decorator
    def work(self):
        """重写工作方法"""
        return f"{self.name} 正在用{self.tool}设计"
    
    @timing_decorator
    def calculate(self, n):
        """重写计算方法，使用不同的算法"""
        # 模拟设计相关的计算
        import math
        return sum(math.sqrt(i) for i in range(1, n + 1))

# 演示装饰器增强的方法重写
def demonstrate_decorated_overriding():
    """演示装饰器增强的方法重写"""
    print("=== 装饰器增强的方法重写演示 ===")
    
    workers = [
        Worker("基础工作者"),
        Developer("张三", "Python"),
        Designer("李四", "Photoshop")
    ]
    
    for worker in workers:
        print(f"\n--- {worker.__class__.__name__}: {worker.name} ---")
        
        # 调用工作方法
        result = worker.work()
        print(f"工作结果: {result}")
        
        # 调用计算方法
        calc_result = worker.calculate(1000)
        print(f"计算结果: {calc_result}")
    
    print("\n=== 演示完成 ===\n")

demonstrate_decorated_overriding()
```

## 方法重写的核心要点

```python
def demonstrate_overriding_principles():
    """演示方法重写的核心要点"""
    print("=== 方法重写核心要点 ===")
    
    print("1. 里氏替换原则（LSP）")
    print("   - 子类对象应该能够替换父类对象")
    print("   - 重写的方法应该保持相同的接口")
    
    print("\n2. 方法签名一致性")
    print("   - 方法名、参数列表应该保持一致")
    print("   - 返回类型应该兼容")
    
    print("\n3. 行为一致性")
    print("   - 重写的方法应该实现相同的语义")
    print("   - 不应该改变方法的基本契约")
    
    print("\n4. super()的正确使用")
    print("   - 用于调用父类的方法")
    print("   - 支持方法解析顺序（MRO）")
    
    print("\n5. 抽象方法的实现")
    print("   - 子类必须实现所有抽象方法")
    print("   - 提供具体的实现逻辑")
    
    print("\n=== 要点总结完成 ===\n")

demonstrate_overriding_principles()
```

## 总结

方法重写是实现多态的核心机制，它允许子类提供特定的实现来替代父类的通用实现。通过方法重写，我们可以：

1. **实现多态行为**：同一接口的不同实现
2. **扩展功能**：在保持接口一致的前提下增加新功能
3. **定制行为**：根据具体需求调整方法行为
4. **支持框架设计**：通过抽象方法定义框架结构

掌握方法重写的正确使用方式，能让你设计出更加灵活和可扩展的面向对象程序。