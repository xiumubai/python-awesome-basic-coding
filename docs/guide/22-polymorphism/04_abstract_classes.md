# 抽象方法和抽象类

## 什么是抽象类

抽象类是一种不能被直接实例化的类，它通常包含一个或多个抽象方法。抽象方法是只有声明没有实现的方法，子类必须实现所有的抽象方法才能被实例化。在Python中，我们使用`abc`模块来创建抽象类。

## 基本的抽象类实现

### 图形抽象类示例

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """图形抽象基类"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """计算面积 - 抽象方法"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """计算周长 - 抽象方法"""
        pass
    
    # 具体方法（非抽象）
    def describe(self):
        """描述图形"""
        return f"{self.name}: 面积={self.area():.2f}, 周长={self.perimeter():.2f}"
    
    def get_info(self):
        """获取图形信息"""
        return {
            'name': self.name,
            'area': self.area(),
            'perimeter': self.perimeter(),
            'type': self.__class__.__name__
        }

class Rectangle(Shape):
    """矩形类 - 实现抽象方法"""
    
    def __init__(self, width, height):
        super().__init__("矩形")
        self.width = width
        self.height = height
    
    def area(self):
        """实现抽象方法：计算矩形面积"""
        return self.width * self.height
    
    def perimeter(self):
        """实现抽象方法：计算矩形周长"""
        return 2 * (self.width + self.height)
    
    def get_dimensions(self):
        """矩形特有方法"""
        return f"宽度: {self.width}, 高度: {self.height}"

class Circle(Shape):
    """圆形类 - 实现抽象方法"""
    
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius = radius
    
    def area(self):
        """实现抽象方法：计算圆形面积"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """实现抽象方法：计算圆形周长"""
        return 2 * math.pi * self.radius
    
    def get_radius(self):
        """圆形特有方法"""
        return f"半径: {self.radius}"

class Triangle(Shape):
    """三角形类 - 实现抽象方法"""
    
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
        """实现抽象方法：使用海伦公式计算三角形面积"""
        s = (self.a + self.b + self.c) / 2  # 半周长
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        """实现抽象方法：计算三角形周长"""
        return self.a + self.b + self.c
    
    def get_sides(self):
        """三角形特有方法"""
        return f"边长: {self.a}, {self.b}, {self.c}"

# 演示抽象类的使用
def demonstrate_abstract_classes():
    """演示抽象类的使用"""
    print("=== 抽象类演示 ===")
    
    # 尝试实例化抽象类（会失败）
    print("1. 尝试实例化抽象类:")
    try:
        shape = Shape("测试图形")
        print("   成功创建抽象类实例")
    except TypeError as e:
        print(f"   错误: {e}")
    
    # 创建具体类的实例
    print("\n2. 创建具体类实例:")
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Triangle(3, 4, 5)
    ]
    
    for shape in shapes:
        print(f"\n   {shape.__class__.__name__}:")
        print(f"   {shape.describe()}")
        
        # 调用特有方法
        if isinstance(shape, Rectangle):
            print(f"   {shape.get_dimensions()}")
        elif isinstance(shape, Circle):
            print(f"   {shape.get_radius()}")
        elif isinstance(shape, Triangle):
            print(f"   {shape.get_sides()}")
    
    print("\n=== 演示完成 ===\n")

demonstrate_abstract_classes()
```

## 抽象属性

### 使用抽象属性

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """交通工具抽象类"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0
    
    @property
    @abstractmethod
    def max_speed(self):
        """最大速度 - 抽象属性"""
        pass
    
    @property
    @abstractmethod
    def fuel_type(self):
        """燃料类型 - 抽象属性"""
        pass
    
    @abstractmethod
    def start_engine(self):
        """启动引擎 - 抽象方法"""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """停止引擎 - 抽象方法"""
        pass
    
    # 具体方法
    def accelerate(self, speed_increase):
        """加速"""
        new_speed = self._speed + speed_increase
        if new_speed <= self.max_speed:
            self._speed = new_speed
            return f"{self.brand} {self.model} 加速到 {self._speed} km/h"
        else:
            self._speed = self.max_speed
            return f"{self.brand} {self.model} 达到最大速度 {self.max_speed} km/h"
    
    def brake(self, speed_decrease):
        """刹车"""
        self._speed = max(0, self._speed - speed_decrease)
        return f"{self.brand} {self.model} 减速到 {self._speed} km/h"
    
    @property
    def current_speed(self):
        """当前速度"""
        return self._speed
    
    def get_info(self):
        """获取车辆信息"""
        return {
            'brand': self.brand,
            'model': self.model,
            'fuel_type': self.fuel_type,
            'max_speed': self.max_speed,
            'current_speed': self.current_speed
        }

class Car(Vehicle):
    """汽车类"""
    
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size
        self.engine_running = False
    
    @property
    def max_speed(self):
        """实现抽象属性：最大速度"""
        # 根据引擎大小计算最大速度
        return int(self.engine_size * 50)
    
    @property
    def fuel_type(self):
        """实现抽象属性：燃料类型"""
        return "汽油"
    
    def start_engine(self):
        """实现抽象方法：启动引擎"""
        if not self.engine_running:
            self.engine_running = True
            return f"{self.brand} {self.model} 引擎启动，{self.engine_size}L引擎开始工作"
        return f"{self.brand} {self.model} 引擎已经在运行"
    
    def stop_engine(self):
        """实现抽象方法：停止引擎"""
        if self.engine_running:
            self.engine_running = False
            self._speed = 0
            return f"{self.brand} {self.model} 引擎停止"
        return f"{self.brand} {self.model} 引擎已经停止"

class ElectricCar(Vehicle):
    """电动汽车类"""
    
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
        self.motor_running = False
        self.battery_level = 100
    
    @property
    def max_speed(self):
        """实现抽象属性：最大速度"""
        # 根据电池容量计算最大速度
        return int(self.battery_capacity * 2)
    
    @property
    def fuel_type(self):
        """实现抽象属性：燃料类型"""
        return "电力"
    
    def start_engine(self):
        """实现抽象方法：启动电机"""
        if self.battery_level > 0 and not self.motor_running:
            self.motor_running = True
            return f"{self.brand} {self.model} 电机启动，{self.battery_capacity}kWh电池供电"
        elif self.battery_level <= 0:
            return f"{self.brand} {self.model} 电池没电，无法启动"
        return f"{self.brand} {self.model} 电机已经在运行"
    
    def stop_engine(self):
        """实现抽象方法：停止电机"""
        if self.motor_running:
            self.motor_running = False
            self._speed = 0
            return f"{self.brand} {self.model} 电机停止"
        return f"{self.brand} {self.model} 电机已经停止"
    
    def charge(self, amount):
        """充电"""
        self.battery_level = min(100, self.battery_level + amount)
        return f"充电完成，当前电量: {self.battery_level}%"

class Motorcycle(Vehicle):
    """摩托车类"""
    
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc  # 排量
        self.engine_running = False
    
    @property
    def max_speed(self):
        """实现抽象属性：最大速度"""
        # 根据排量计算最大速度
        return int(self.cc * 0.3)
    
    @property
    def fuel_type(self):
        """实现抽象属性：燃料类型"""
        return "汽油"
    
    def start_engine(self):
        """实现抽象方法：启动引擎"""
        if not self.engine_running:
            self.engine_running = True
            return f"{self.brand} {self.model} 摩托车引擎启动，{self.cc}cc引擎轰鸣"
        return f"{self.brand} {self.model} 引擎已经在运行"
    
    def stop_engine(self):
        """实现抽象方法：停止引擎"""
        if self.engine_running:
            self.engine_running = False
            self._speed = 0
            return f"{self.brand} {self.model} 摩托车引擎停止"
        return f"{self.brand} {self.model} 引擎已经停止"

# 演示抽象属性
def demonstrate_abstract_properties():
    """演示抽象属性"""
    print("=== 抽象属性演示 ===")
    
    # 创建不同类型的车辆
    vehicles = [
        Car("丰田", "卡罗拉", 1.8),
        ElectricCar("特斯拉", "Model 3", 75),
        Motorcycle("本田", "CBR600", 600)
    ]
    
    for vehicle in vehicles:
        print(f"\n--- {vehicle.__class__.__name__}: {vehicle.brand} {vehicle.model} ---")
        
        # 显示车辆信息
        info = vehicle.get_info()
        print(f"燃料类型: {info['fuel_type']}")
        print(f"最大速度: {info['max_speed']} km/h")
        
        # 启动和操作
        print(vehicle.start_engine())
        print(vehicle.accelerate(50))
        print(vehicle.accelerate(100))
        print(vehicle.brake(30))
        print(f"当前速度: {vehicle.current_speed} km/h")
        print(vehicle.stop_engine())
        
        # 特殊操作
        if isinstance(vehicle, ElectricCar):
            print(vehicle.charge(20))
    
    print("\n=== 演示完成 ===\n")

demonstrate_abstract_properties()
```

## 多层抽象继承

### 分层抽象设计

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    """动物抽象基类 - 最高层抽象"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100
    
    @abstractmethod
    def make_sound(self):
        """发出声音 - 抽象方法"""
        pass
    
    @abstractmethod
    def move(self):
        """移动 - 抽象方法"""
        pass
    
    @abstractmethod
    def eat(self, food):
        """进食 - 抽象方法"""
        pass
    
    # 具体方法
    def sleep(self):
        """睡觉"""
        self.energy = min(100, self.energy + 20)
        return f"{self.name} 睡觉了，恢复体力到 {self.energy}"
    
    def get_status(self):
        """获取状态"""
        return f"{self.name}({self.species}) - 体力: {self.energy}"

class Mammal(Animal):
    """哺乳动物抽象类 - 中间层抽象"""
    
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color
        self.body_temperature = 37.0
    
    @abstractmethod
    def give_birth(self):
        """生育 - 哺乳动物特有的抽象方法"""
        pass
    
    # 部分实现的方法
    def regulate_temperature(self):
        """调节体温 - 哺乳动物的具体实现"""
        return f"{self.name} 调节体温到 {self.body_temperature}°C"
    
    def eat(self, food):
        """实现抽象方法：哺乳动物的进食方式"""
        if self.energy < 100:
            self.energy = min(100, self.energy + 15)
            return f"{self.name} 吃了 {food}，体力恢复到 {self.energy}"
        return f"{self.name} 不饿，不需要吃 {food}"

class Bird(Animal):
    """鸟类抽象类 - 中间层抽象"""
    
    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.wing_span = wing_span
        self.can_fly = True
    
    @abstractmethod
    def lay_eggs(self):
        """产卵 - 鸟类特有的抽象方法"""
        pass
    
    # 部分实现的方法
    def move(self):
        """实现抽象方法：鸟类的移动方式"""
        if self.can_fly:
            self.energy -= 5
            return f"{self.name} 展开 {self.wing_span}cm 的翅膀飞翔"
        else:
            self.energy -= 3
            return f"{self.name} 在地面上行走"
    
    def eat(self, food):
        """实现抽象方法：鸟类的进食方式"""
        if self.energy < 100:
            self.energy = min(100, self.energy + 10)
            return f"{self.name} 啄食 {food}，体力恢复到 {self.energy}"
        return f"{self.name} 不饿，不需要吃 {food}"

# 具体实现类
class Dog(Mammal):
    """狗类 - 具体实现"""
    
    def __init__(self, name, breed, fur_color):
        super().__init__(name, "狗", fur_color)
        self.breed = breed
        self.loyalty = 100
    
    def make_sound(self):
        """实现抽象方法"""
        return "汪汪汪！"
    
    def move(self):
        """实现抽象方法"""
        self.energy -= 8
        return f"{self.name} 快乐地奔跑"
    
    def give_birth(self):
        """实现抽象方法"""
        return f"{self.name} 生了一窝小狗"
    
    def fetch(self, item):
        """狗特有的方法"""
        self.energy -= 5
        self.loyalty += 5
        return f"{self.name} 去捡 {item}，忠诚度提升到 {self.loyalty}"

class Cat(Mammal):
    """猫类 - 具体实现"""
    
    def __init__(self, name, breed, fur_color):
        super().__init__(name, "猫", fur_color)
        self.breed = breed
        self.independence = 80
    
    def make_sound(self):
        """实现抽象方法"""
        return "喵喵喵！"
    
    def move(self):
        """实现抽象方法"""
        self.energy -= 5
        return f"{self.name} 优雅地踱步"
    
    def give_birth(self):
        """实现抽象方法"""
        return f"{self.name} 生了几只小猫"
    
    def climb(self):
        """猫特有的方法"""
        self.energy -= 10
        return f"{self.name} 爬到了高处"

class Eagle(Bird):
    """鹰类 - 具体实现"""
    
    def __init__(self, name, wing_span):
        super().__init__(name, "鹰", wing_span)
        self.hunting_skill = 90
    
    def make_sound(self):
        """实现抽象方法"""
        return "啸！啸！啸！"
    
    def lay_eggs(self):
        """实现抽象方法"""
        return f"{self.name} 在悬崖上产下了鹰蛋"
    
    def hunt(self, prey):
        """鹰特有的方法"""
        self.energy -= 15
        return f"{self.name} 俯冲捕获了 {prey}"

class Penguin(Bird):
    """企鹅类 - 不会飞的鸟"""
    
    def __init__(self, name):
        super().__init__(name, "企鹅", 30)
        self.can_fly = False  # 企鹅不会飞
        self.swimming_skill = 95
    
    def make_sound(self):
        """实现抽象方法"""
        return "嘎嘎嘎！"
    
    def lay_eggs(self):
        """实现抽象方法"""
        return f"{self.name} 在冰面上产下了企鹅蛋"
    
    def swim(self):
        """企鹅特有的方法"""
        self.energy -= 5
        return f"{self.name} 在水中游泳，游泳技能: {self.swimming_skill}"

# 演示多层抽象继承
def demonstrate_multilevel_abstraction():
    """演示多层抽象继承"""
    print("=== 多层抽象继承演示 ===")
    
    # 创建不同的动物
    animals = [
        Dog("旺财", "金毛", "金色"),
        Cat("咪咪", "波斯猫", "白色"),
        Eagle("雄鹰", 200),
        Penguin("波波")
    ]
    
    for animal in animals:
        print(f"\n--- {animal.__class__.__name__}: {animal.name} ---")
        print(animal.get_status())
        
        # 基本行为
        print(f"声音: {animal.make_sound()}")
        print(f"移动: {animal.move()}")
        print(f"进食: {animal.eat('食物')}")
        
        # 特殊行为
        if isinstance(animal, Mammal):
            print(f"体温调节: {animal.regulate_temperature()}")
            print(f"生育: {animal.give_birth()}")
            
            if isinstance(animal, Dog):
                print(f"特技: {animal.fetch('球')}")
            elif isinstance(animal, Cat):
                print(f"特技: {animal.climb()}")
        
        elif isinstance(animal, Bird):
            print(f"产卵: {animal.lay_eggs()}")
            
            if isinstance(animal, Eagle):
                print(f"狩猎: {animal.hunt('兔子')}")
            elif isinstance(animal, Penguin):
                print(f"游泳: {animal.swim()}")
        
        print(f"休息: {animal.sleep()}")
        print(f"最终状态: {animal.get_status()}")
    
    print("\n=== 演示完成 ===\n")

demonstrate_multilevel_abstraction()
```

## 抽象类的设计模式

### 模板方法模式

```python
from abc import ABC, abstractmethod
import time

class DataAnalyzer(ABC):
    """数据分析器抽象类 - 模板方法模式"""
    
    def analyze(self, data):
        """模板方法：定义分析流程"""
        print(f"开始分析数据 - {self.__class__.__name__}")
        
        # 1. 数据验证
        if not self.validate_data(data):
            return "数据验证失败"
        
        # 2. 数据预处理
        processed_data = self.preprocess_data(data)
        
        # 3. 核心分析（抽象方法）
        analysis_result = self.perform_analysis(processed_data)
        
        # 4. 结果后处理
        final_result = self.postprocess_result(analysis_result)
        
        # 5. 生成报告
        report = self.generate_report(final_result)
        
        print(f"分析完成 - {self.__class__.__name__}")
        return report
    
    def validate_data(self, data):
        """数据验证（可被子类重写）"""
        print("  执行基础数据验证")
        return data is not None and len(data) > 0
    
    def preprocess_data(self, data):
        """数据预处理（可被子类重写）"""
        print("  执行基础数据预处理")
        return data
    
    @abstractmethod
    def perform_analysis(self, data):
        """执行分析（抽象方法，子类必须实现）"""
        pass
    
    def postprocess_result(self, result):
        """结果后处理（可被子类重写）"""
        print("  执行基础结果后处理")
        return result
    
    @abstractmethod
    def generate_report(self, result):
        """生成报告（抽象方法，子类必须实现）"""
        pass

class StatisticalAnalyzer(DataAnalyzer):
    """统计分析器"""
    
    def validate_data(self, data):
        """重写数据验证"""
        super().validate_data(data)
        print("  执行统计数据验证：检查数值类型")
        return all(isinstance(x, (int, float)) for x in data)
    
    def preprocess_data(self, data):
        """重写数据预处理"""
        super().preprocess_data(data)
        print("  执行统计预处理：排序和去重")
        return sorted(set(data))
    
    def perform_analysis(self, data):
        """实现抽象方法：统计分析"""
        print("  执行统计分析")
        return {
            'count': len(data),
            'sum': sum(data),
            'mean': sum(data) / len(data),
            'min': min(data),
            'max': max(data)
        }
    
    def generate_report(self, result):
        """实现抽象方法：生成统计报告"""
        print("  生成统计报告")
        return f"""统计分析报告:
        数据量: {result['count']}
        总和: {result['sum']}
        平均值: {result['mean']:.2f}
        最小值: {result['min']}
        最大值: {result['max']}"""

class TextAnalyzer(DataAnalyzer):
    """文本分析器"""
    
    def validate_data(self, data):
        """重写数据验证"""
        super().validate_data(data)
        print("  执行文本数据验证：检查字符串类型")
        return all(isinstance(x, str) for x in data)
    
    def preprocess_data(self, data):
        """重写数据预处理"""
        super().preprocess_data(data)
        print("  执行文本预处理：转换为小写并去除空格")
        return [text.lower().strip() for text in data]
    
    def perform_analysis(self, data):
        """实现抽象方法：文本分析"""
        print("  执行文本分析")
        word_count = {}
        total_chars = 0
        
        for text in data:
            words = text.split()
            total_chars += len(text)
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
        
        return {
            'text_count': len(data),
            'total_chars': total_chars,
            'word_count': word_count,
            'unique_words': len(word_count),
            'most_common': max(word_count.items(), key=lambda x: x[1]) if word_count else None
        }
    
    def generate_report(self, result):
        """实现抽象方法：生成文本报告"""
        print("  生成文本分析报告")
        most_common = result['most_common']
        return f"""文本分析报告:
        文本数量: {result['text_count']}
        总字符数: {result['total_chars']}
        唯一单词数: {result['unique_words']}
        最常见单词: {most_common[0] if most_common else 'N/A'} (出现 {most_common[1] if most_common else 0} 次)"""

class PerformanceAnalyzer(DataAnalyzer):
    """性能分析器"""
    
    def __init__(self):
        self.start_time = None
        self.end_time = None
    
    def preprocess_data(self, data):
        """重写数据预处理，添加性能监控"""
        self.start_time = time.time()
        result = super().preprocess_data(data)
        print(f"  预处理耗时: {time.time() - self.start_time:.4f}秒")
        return result
    
    def perform_analysis(self, data):
        """实现抽象方法：性能分析"""
        print("  执行性能分析")
        analysis_start = time.time()
        
        # 模拟复杂计算
        result = sum(x * x for x in range(len(data) * 1000))
        
        analysis_time = time.time() - analysis_start
        return {
            'data_size': len(data),
            'calculation_result': result,
            'analysis_time': analysis_time
        }
    
    def postprocess_result(self, result):
        """重写结果后处理"""
        super().postprocess_result(result)
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        result['total_time'] = total_time
        print(f"  总处理时间: {total_time:.4f}秒")
        return result
    
    def generate_report(self, result):
        """实现抽象方法：生成性能报告"""
        print("  生成性能分析报告")
        return f"""性能分析报告:
        数据大小: {result['data_size']}
        计算结果: {result['calculation_result']}
        分析耗时: {result['analysis_time']:.4f}秒
        总耗时: {result['total_time']:.4f}秒"""

# 演示模板方法模式
def demonstrate_template_method():
    """演示模板方法模式"""
    print("=== 模板方法模式演示 ===")
    
    # 创建不同的分析器
    analyzers = [
        StatisticalAnalyzer(),
        TextAnalyzer(),
        PerformanceAnalyzer()
    ]
    
    # 测试数据
    test_data = [
        [1, 2, 3, 4, 5, 3, 2, 1],
        ["hello world", "python programming", "abstract classes", "hello python"],
        [10, 20, 30, 40, 50]
    ]
    
    for analyzer, data in zip(analyzers, test_data):
        print(f"\n--- {analyzer.__class__.__name__} ---")
        print(f"输入数据: {data}")
        
        try:
            report = analyzer.analyze(data)
            print(f"\n{report}")
        except Exception as e:
            print(f"分析失败: {e}")
    
    print("\n=== 演示完成 ===\n")

demonstrate_template_method()
```

## 抽象类的最佳实践

### 设计原则和注意事项

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class PaymentProcessor(ABC):
    """支付处理器抽象类 - 最佳实践示例"""
    
    def __init__(self, merchant_id: str):
        self.merchant_id = merchant_id
        self.transaction_log: List[Dict[str, Any]] = []
    
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> Dict[str, Any]:
        """处理支付 - 抽象方法
        
        Args:
            amount: 支付金额
            currency: 货币类型
            
        Returns:
            包含支付结果的字典
        """
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float = None) -> Dict[str, Any]:
        """退款 - 抽象方法
        
        Args:
            transaction_id: 交易ID
            amount: 退款金额（None表示全额退款）
            
        Returns:
            包含退款结果的字典
        """
        pass
    
    @abstractmethod
    def get_transaction_status(self, transaction_id: str) -> str:
        """获取交易状态 - 抽象方法"""
        pass
    
    # 具体方法 - 通用功能
    def log_transaction(self, transaction_data: Dict[str, Any]) -> None:
        """记录交易日志"""
        self.transaction_log.append(transaction_data)
    
    def get_transaction_history(self) -> List[Dict[str, Any]]:
        """获取交易历史"""
        return self.transaction_log.copy()
    
    def validate_amount(self, amount: float) -> bool:
        """验证金额"""
        return amount > 0 and amount <= 10000  # 最大限额
    
    def generate_transaction_id(self) -> str:
        """生成交易ID"""
        import uuid
        return str(uuid.uuid4())

class CreditCardProcessor(PaymentProcessor):
    """信用卡支付处理器"""
    
    def __init__(self, merchant_id: str, gateway_url: str):
        super().__init__(merchant_id)
        self.gateway_url = gateway_url
        self.supported_cards = ["VISA", "MASTERCARD", "AMEX"]
    
    def process_payment(self, amount: float, currency: str = "USD", 
                      card_number: str = None, cvv: str = None) -> Dict[str, Any]:
        """实现信用卡支付处理"""
        if not self.validate_amount(amount):
            return {"status": "failed", "error": "Invalid amount"}
        
        transaction_id = self.generate_transaction_id()
        
        # 模拟信用卡处理
        transaction_data = {
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency,
            "payment_method": "credit_card",
            "status": "completed",
            "merchant_id": self.merchant_id
        }
        
        self.log_transaction(transaction_data)
        
        return {
            "status": "success",
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency
        }
    
    def refund_payment(self, transaction_id: str, amount: float = None) -> Dict[str, Any]:
        """实现信用卡退款"""
        # 查找原交易
        original_transaction = None
        for transaction in self.transaction_log:
            if transaction.get("transaction_id") == transaction_id:
                original_transaction = transaction
                break
        
        if not original_transaction:
            return {"status": "failed", "error": "Transaction not found"}
        
        refund_amount = amount or original_transaction["amount"]
        refund_id = self.generate_transaction_id()
        
        refund_data = {
            "transaction_id": refund_id,
            "original_transaction_id": transaction_id,
            "amount": refund_amount,
            "currency": original_transaction["currency"],
            "payment_method": "credit_card_refund",
            "status": "completed",
            "merchant_id": self.merchant_id
        }
        
        self.log_transaction(refund_data)
        
        return {
            "status": "success",
            "refund_id": refund_id,
            "amount": refund_amount
        }
    
    def get_transaction_status(self, transaction_id: str) -> str:
        """获取信用卡交易状态"""
        for transaction in self.transaction_log:
            if transaction.get("transaction_id") == transaction_id:
                return transaction.get("status", "unknown")
        return "not_found"

class PayPalProcessor(PaymentProcessor):
    """PayPal支付处理器"""
    
    def __init__(self, merchant_id: str, api_key: str):
        super().__init__(merchant_id)
        self.api_key = api_key
    
    def process_payment(self, amount: float, currency: str = "USD", 
                      email: str = None) -> Dict[str, Any]:
        """实现PayPal支付处理"""
        if not self.validate_amount(amount):
            return {"status": "failed", "error": "Invalid amount"}
        
        transaction_id = self.generate_transaction_id()
        
        # 模拟PayPal处理
        transaction_data = {
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency,
            "payment_method": "paypal",
            "status": "completed",
            "merchant_id": self.merchant_id,
            "payer_email": email
        }
        
        self.log_transaction(transaction_data)
        
        return {
            "status": "success",
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency,
            "paypal_fee": amount * 0.029  # PayPal手续费
        }
    
    def refund_payment(self, transaction_id: str, amount: float = None) -> Dict[str, Any]:
        """实现PayPal退款"""
        # 查找原交易
        original_transaction = None
        for transaction in self.transaction_log:
            if transaction.get("transaction_id") == transaction_id:
                original_transaction = transaction
                break
        
        if not original_transaction:
            return {"status": "failed", "error": "Transaction not found"}
        
        refund_amount = amount or original_transaction["amount"]
        refund_id = self.generate_transaction_id()
        
        refund_data = {
            "transaction_id": refund_id,
            "original_transaction_id": transaction_id,
            "amount": refund_amount,
            "currency": original_transaction["currency"],
            "payment_method": "paypal_refund",
            "status": "completed",
            "merchant_id": self.merchant_id
        }
        
        self.log_transaction(refund_data)
        
        return {
            "status": "success",
            "refund_id": refund_id,
            "amount": refund_amount
        }
    
    def get_transaction_status(self, transaction_id: str) -> str:
        """获取PayPal交易状态"""
        for transaction in self.transaction_log:
            if transaction.get("transaction_id") == transaction_id:
                return transaction.get("status", "unknown")
        return "not_found"

class CryptocurrencyProcessor(PaymentProcessor):
    """加密货币支付处理器"""
    
    def __init__(self, merchant_id: str, wallet_address: str):
        super().__init__(merchant_id)
        self.wallet_address = wallet_address
        self.supported_currencies = ["BTC", "ETH", "LTC"]
    
    def process_payment(self, amount: float, currency: str = "BTC", 
                      from_address: str = None) -> Dict[str, Any]:
        """实现加密货币支付处理"""
        if currency not in self.supported_currencies:
            return {"status": "failed", "error": f"Unsupported currency: {currency}"}
        
        if not self.validate_amount(amount):
            return {"status": "failed", "error": "Invalid amount"}
        
        transaction_id = self.generate_transaction_id()
        
        # 模拟区块链交易
        transaction_data = {
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency,
            "payment_method": "cryptocurrency",
            "status": "pending",  # 加密货币交易需要确认
            "merchant_id": self.merchant_id,
            "from_address": from_address,
            "to_address": self.wallet_address,
            "confirmations": 0
        }
        
        self.log_transaction(transaction_data)
        
        return {
            "status": "pending",
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency,
            "confirmations_required": 6
        }
    
    def refund_payment(self, transaction_id: str, amount: float = None) -> Dict[str, Any]:
        """实现加密货币退款（实际上是新的转账）"""
        # 查找原交易
        original_transaction = None
        for transaction in self.transaction_log:
            if transaction.get("transaction_id") == transaction_id:
                original_transaction = transaction
                break
        
        if not original_transaction:
            return {"status": "failed", "error": "Transaction not found"}
        
        if original_transaction["status"] != "completed":
            return {"status": "failed", "error": "Original transaction not completed"}
        
        refund_amount = amount or original_transaction["amount"]
        refund_id = self.generate_transaction_id()
        
        refund_data = {
            "transaction_id": refund_id,
            "original_transaction_id": transaction_id,
            "amount": refund_amount,
            "currency": original_transaction["currency"],
            "payment_method": "cryptocurrency_refund",
            "status": "pending",
            "merchant_id": self.merchant_id,
            "from_address": self.wallet_address,
            "to_address": original_transaction["from_address"]
        }
        
        self.log_transaction(refund_data)
        
        return {
            "status": "pending",
            "refund_id": refund_id,
            "amount": refund_amount
        }
    
    def get_transaction_status(self, transaction_id: str) -> str:
        """获取加密货币交易状态"""
        for transaction in self.transaction_log:
            if transaction.get("transaction_id") == transaction_id:
                return transaction.get("status", "unknown")
        return "not_found"
    
    def confirm_transaction(self, transaction_id: str) -> bool:
        """确认交易（模拟区块链确认）"""
        for transaction in self.transaction_log:
            if transaction.get("transaction_id") == transaction_id:
                if transaction["status"] == "pending":
                    transaction["status"] = "completed"
                    transaction["confirmations"] = 6
                    return True
        return False

# 演示抽象类的最佳实践
def demonstrate_best_practices():
    """演示抽象类的最佳实践"""
    print("=== 抽象类最佳实践演示 ===")
    
    # 创建不同的支付处理器
    processors = [
        CreditCardProcessor("MERCHANT_001", "https://gateway.example.com"),
        PayPalProcessor("MERCHANT_002", "api_key_12345"),
        CryptocurrencyProcessor("MERCHANT_003", "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    ]
    
    # 测试支付处理
    for processor in processors:
        print(f"\n--- {processor.__class__.__name__} ---")
        
        # 处理支付
        if isinstance(processor, CreditCardProcessor):
            result = processor.process_payment(100.0, "USD", "4111111111111111", "123")
        elif isinstance(processor, PayPalProcessor):
            result = processor.process_payment(150.0, "USD", "user@example.com")
        elif isinstance(processor, CryptocurrencyProcessor):
            result = processor.process_payment(0.001, "BTC", "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2")
        
        print(f"支付结果: {result}")
        
        if result["status"] in ["success", "pending"]:
            transaction_id = result.get("transaction_id")
            
            # 检查交易状态
            status = processor.get_transaction_status(transaction_id)
            print(f"交易状态: {status}")
            
            # 对于加密货币，模拟确认过程
            if isinstance(processor, CryptocurrencyProcessor) and status == "pending":
                print("模拟区块链确认...")
                processor.confirm_transaction(transaction_id)
                status = processor.get_transaction_status(transaction_id)
                print(f"确认后状态: {status}")
            
            # 测试退款
            if status == "completed":
                refund_result = processor.refund_payment(transaction_id, 50.0)
                print(f"退款结果: {refund_result}")
        
        # 显示交易历史
        history = processor.get_transaction_history()
        print(f"交易历史记录数: {len(history)}")
    
    print("\n=== 演示完成 ===\n")

demonstrate_best_practices()
```

## 抽象类的核心要点

```python
def demonstrate_abstract_class_principles():
    """演示抽象类的核心要点"""
    print("=== 抽象类核心要点 ===")
    
    print("1. 抽象类的特点")
    print("   - 不能被直接实例化")
    print("   - 可以包含抽象方法和具体方法")
    print("   - 子类必须实现所有抽象方法")
    
    print("\n2. 抽象方法的作用")
    print("   - 定义接口契约")
    print("   - 强制子类实现特定方法")
    print("   - 提供统一的方法签名")
    
    print("\n3. 设计原则")
    print("   - 单一职责原则：每个抽象类专注一个领域")
    print("   - 开闭原则：对扩展开放，对修改封闭")
    print("   - 里氏替换原则：子类可以替换父类")
    
    print("\n4. 使用场景")
    print("   - 定义框架和模板")
    print("   - 实现模板方法模式")
    print("   - 提供公共接口和部分实现")
    
    print("\n5. 最佳实践")
    print("   - 合理设计抽象层次")
    print("   - 提供清晰的文档说明")
    print("   - 保持接口稳定性")
    
    print("\n=== 要点总结完成 ===\n")

demonstrate_abstract_class_principles()
```

## 总结

抽象类是面向对象编程中的重要概念，它提供了一种定义接口契约和共享代码的机制。通过抽象类，我们可以：

1. **定义统一接口**：确保所有子类实现相同的方法
2. **共享通用代码**：在抽象类中实现公共功能
3. **强制实现规范**：通过抽象方法确保子类提供必要的实现
4. **支持多态性**：不同的子类可以有不同的实现
5. **提高代码质量**：通过抽象设计提高代码的可维护性和扩展性

掌握抽象类的正确使用方式，能让你设计出更加健壮和灵活的面向对象程序。