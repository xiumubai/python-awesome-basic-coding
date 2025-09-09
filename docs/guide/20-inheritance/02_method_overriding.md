# 方法重写（Method Overriding）

方法重写是继承中的一个重要概念，它允许子类重新定义父类中已有的方法，以实现不同的行为。这是实现多态性的基础。

## 什么是方法重写？

方法重写是指在子类中重新定义父类已有的方法。当子类对象调用该方法时，会执行子类中的版本，而不是父类中的版本。

```python
# 1. 基本的方法重写
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} makes a generic animal sound"
    
    def move(self):
        return f"{self.name} moves around"
    
    def eat(self):
        return f"{self.name} eats food"

class Dog(Animal):
    def make_sound(self):  # 重写父类方法
        return f"{self.name} barks: Woof! Woof!"
    
    def move(self):  # 重写父类方法
        return f"{self.name} runs on four legs"

class Bird(Animal):
    def make_sound(self):  # 重写父类方法
        return f"{self.name} chirps: Tweet! Tweet!"
    
    def move(self):  # 重写父类方法
        return f"{self.name} flies in the sky"

print("=== 基本方法重写演示 ===")

# 创建不同类型的动物
generic_animal = Animal("Generic")
dog = Dog("旺财")
bird = Bird("小鸟")

# 调用相同的方法，但行为不同
animals = [generic_animal, dog, bird]
for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.make_sound()}")
    print(f"{animal.__class__.__name__}: {animal.move()}")
    print(f"{animal.__class__.__name__}: {animal.eat()}")  # 未重写，使用父类版本
    print()
```

## 方法重写的规则

```python
# 2. 方法重写的规则和最佳实践
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """计算面积 - 基类提供默认实现"""
        return 0
    
    def perimeter(self):
        """计算周长 - 基类提供默认实现"""
        return 0
    
    def describe(self):
        """描述形状"""
        return f"This is a {self.name} with area {self.area()} and perimeter {self.perimeter()}"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")  # 调用父类构造函数
        self.width = width
        self.height = height
    
    def area(self):  # 重写父类方法
        """重写面积计算方法"""
        return self.width * self.height
    
    def perimeter(self):  # 重写父类方法
        """重写周长计算方法"""
        return 2 * (self.width + self.height)
    
    # describe方法未重写，将使用父类版本

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):  # 重写父类方法
        """重写面积计算方法"""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):  # 重写父类方法
        """重写周长计算方法"""
        import math
        return 2 * math.pi * self.radius
    
    def describe(self):  # 重写父类方法
        """重写描述方法，提供更详细的信息"""
        base_description = super().describe()  # 调用父类方法
        return f"{base_description} (radius: {self.radius})"

print("=== 方法重写规则演示 ===")

rectangle = Rectangle(5, 3)
circle = Circle(4)

print(f"矩形: {rectangle.describe()}")
print(f"圆形: {circle.describe()}")

# 验证方法重写
print(f"\n矩形面积: {rectangle.area()}")
print(f"圆形面积: {circle.area():.2f}")
```

## 使用super()调用父类方法

```python
# 3. 使用super()扩展父类方法
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        self.salary = 0
    
    def work(self):
        return f"{self.name} is working"
    
    def get_info(self):
        return f"Employee: {self.name} (ID: {self.employee_id})"
    
    def calculate_bonus(self):
        return self.salary * 0.1  # 基础奖金为薪水的10%

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)  # 调用父类构造函数
        self.department = department
        self.team_size = 0
    
    def work(self):  # 重写工作方法
        base_work = super().work()  # 调用父类方法
        return f"{base_work} and managing {self.department} department"
    
    def get_info(self):  # 重写信息获取方法
        base_info = super().get_info()  # 调用父类方法
        return f"{base_info}, Manager of {self.department} (Team size: {self.team_size})"
    
    def calculate_bonus(self):  # 重写奖金计算方法
        base_bonus = super().calculate_bonus()  # 调用父类方法
        management_bonus = self.team_size * 1000  # 管理奖金
        return base_bonus + management_bonus
    
    def manage_team(self):
        return f"{self.name} is managing the {self.department} team"

class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language
        self.projects_completed = 0
    
    def work(self):  # 重写工作方法
        base_work = super().work()  # 调用父类方法
        return f"{base_work} with {self.programming_language}"
    
    def get_info(self):  # 重写信息获取方法
        base_info = super().get_info()  # 调用父类方法
        return f"{base_info}, Developer ({self.programming_language}, {self.projects_completed} projects)"
    
    def calculate_bonus(self):  # 重写奖金计算方法
        base_bonus = super().calculate_bonus()  # 调用父类方法
        project_bonus = self.projects_completed * 500  # 项目奖金
        return base_bonus + project_bonus
    
    def code(self):
        return f"{self.name} is coding in {self.programming_language}"

print("\n=== 使用super()扩展父类方法 ===")

# 创建员工对象
manager = Manager("Alice", "M001", "Engineering")
manager.salary = 80000
manager.team_size = 5

developer = Developer("Bob", "D001", "Python")
developer.salary = 60000
developer.projects_completed = 3

# 测试重写的方法
print(f"经理工作: {manager.work()}")
print(f"开发者工作: {developer.work()}")
print()
print(f"经理信息: {manager.get_info()}")
print(f"开发者信息: {developer.get_info()}")
print()
print(f"经理奖金: ${manager.calculate_bonus()}")
print(f"开发者奖金: ${developer.calculate_bonus()}")
```

## 方法重写与多态性

```python
# 4. 方法重写实现多态性
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return f"{self.brand} {self.model} is starting"
    
    def stop(self):
        return f"{self.brand} {self.model} is stopping"
    
    def get_fuel_type(self):
        return "Unknown fuel type"

class Car(Vehicle):
    def start(self):  # 重写启动方法
        return f"{self.brand} {self.model} car engine is starting with a roar"
    
    def get_fuel_type(self):  # 重写燃料类型方法
        return "Gasoline"

class ElectricCar(Vehicle):
    def start(self):  # 重写启动方法
        return f"{self.brand} {self.model} electric motor is starting silently"
    
    def stop(self):  # 重写停止方法
        base_stop = super().stop()
        return f"{base_stop} and regenerating energy"
    
    def get_fuel_type(self):  # 重写燃料类型方法
        return "Electricity"

class Motorcycle(Vehicle):
    def start(self):  # 重写启动方法
        return f"{self.brand} {self.model} motorcycle is starting with a loud vroom"
    
    def get_fuel_type(self):  # 重写燃料类型方法
        return "Gasoline"

print("\n=== 多态性演示 ===")

# 创建不同类型的车辆
vehicles = [
    Car("Toyota", "Camry"),
    ElectricCar("Tesla", "Model 3"),
    Motorcycle("Harley-Davidson", "Street 750")
]

# 多态性：相同的接口，不同的行为
for vehicle in vehicles:
    print(f"类型: {vehicle.__class__.__name__}")
    print(f"启动: {vehicle.start()}")
    print(f"燃料: {vehicle.get_fuel_type()}")
    print(f"停止: {vehicle.stop()}")
    print()
```

## 方法重写的高级用法

```python
# 5. 方法重写的高级用法
class DataProcessor:
    def __init__(self, name):
        self.name = name
        self.processed_count = 0
    
    def process(self, data):
        """处理数据的基础方法"""
        self.processed_count += 1
        return f"Processing {len(data)} items with {self.name}"
    
    def validate(self, data):
        """验证数据"""
        if not data:
            raise ValueError("Data cannot be empty")
        return True
    
    def log_processing(self, data, result):
        """记录处理过程"""
        print(f"[{self.name}] Processed {len(data)} items: {result}")

class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__("TextProcessor")
        self.word_count = 0
    
    def process(self, data):
        """重写处理方法，专门处理文本数据"""
        # 调用父类验证方法
        self.validate(data)
        
        # 文本特定的处理
        if isinstance(data, str):
            words = data.split()
            self.word_count += len(words)
            result = f"Processed {len(words)} words, total: {self.word_count}"
        else:
            result = super().process(data)  # 回退到父类方法
        
        # 调用父类日志方法
        self.log_processing(data, result)
        return result
    
    def validate(self, data):
        """重写验证方法，添加文本特定验证"""
        super().validate(data)  # 调用父类验证
        if isinstance(data, str) and len(data.strip()) == 0:
            raise ValueError("Text data cannot be empty or whitespace only")
        return True

class NumberProcessor(DataProcessor):
    def __init__(self):
        super().__init__("NumberProcessor")
        self.sum_total = 0
    
    def process(self, data):
        """重写处理方法，专门处理数字数据"""
        self.validate(data)
        
        if isinstance(data, (list, tuple)) and all(isinstance(x, (int, float)) for x in data):
            self.sum_total += sum(data)
            result = f"Processed {len(data)} numbers, sum: {sum(data)}, total: {self.sum_total}"
        else:
            result = super().process(data)  # 回退到父类方法
        
        self.log_processing(data, result)
        return result
    
    def validate(self, data):
        """重写验证方法，添加数字特定验证"""
        super().validate(data)  # 调用父类验证
        if isinstance(data, (list, tuple)):
            if not all(isinstance(x, (int, float)) for x in data):
                raise ValueError("All items must be numbers")
        return True

print("\n=== 方法重写高级用法演示 ===")

# 创建处理器
text_processor = TextProcessor()
number_processor = NumberProcessor()

# 测试文本处理
print("文本处理:")
text_processor.process("Hello world this is a test")
text_processor.process("Python is awesome")

print("\n数字处理:")
number_processor.process([1, 2, 3, 4, 5])
number_processor.process([10, 20, 30])

# 测试验证功能
print("\n验证功能测试:")
try:
    text_processor.process("   ")  # 空白文本
except ValueError as e:
    print(f"文本验证错误: {e}")

try:
    number_processor.process([1, 2, "three"])  # 包含非数字
except ValueError as e:
    print(f"数字验证错误: {e}")
```

## 方法重写的注意事项

```python
# 6. 方法重写的注意事项和常见错误
class Parent:
    def method_with_args(self, arg1, arg2=None):
        return f"Parent method: {arg1}, {arg2}"
    
    def method_with_kwargs(self, **kwargs):
        return f"Parent method with kwargs: {kwargs}"
    
    def important_method(self):
        return "This is important parent functionality"

# 正确的方法重写
class GoodChild(Parent):
    def method_with_args(self, arg1, arg2=None):  # 保持相同的方法签名
        # 可以添加额外的逻辑
        result = super().method_with_args(arg1, arg2)
        return f"Good child extends: {result}"
    
    def method_with_kwargs(self, **kwargs):  # 保持相同的方法签名
        # 添加子类特定的处理
        kwargs['child_info'] = 'added by child'
        return super().method_with_kwargs(**kwargs)
    
    def important_method(self):  # 重写但保留父类功能
        parent_result = super().important_method()
        return f"{parent_result} + child enhancement"

# 有问题的方法重写示例（仅用于演示，不推荐）
class ProblematicChild(Parent):
    def method_with_args(self, arg1):  # 错误：改变了方法签名
        return f"Problematic child: {arg1}"
    
    def important_method(self):  # 错误：完全忽略父类功能
        return "Child completely replaces parent functionality"

print("\n=== 方法重写注意事项演示 ===")

# 测试正确的重写
good_child = GoodChild()
print("正确的方法重写:")
print(good_child.method_with_args("test", "value"))
print(good_child.method_with_kwargs(key1="value1", key2="value2"))
print(good_child.important_method())

# 测试有问题的重写
problematic_child = ProblematicChild()
print("\n有问题的方法重写:")
print(problematic_child.method_with_args("test"))  # 只能传一个参数
# problematic_child.method_with_args("test", "value")  # 这会出错
print(problematic_child.important_method())  # 丢失了父类功能
```

## 抽象方法重写

```python
# 7. 抽象方法的重写
from abc import ABC, abstractmethod

class AbstractProcessor(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def process_data(self, data):
        """抽象方法，子类必须实现"""
        pass
    
    @abstractmethod
    def get_result_format(self):
        """抽象方法，子类必须实现"""
        pass
    
    def run(self, data):  # 具体方法，使用抽象方法
        print(f"Starting {self.name} processing...")
        result = self.process_data(data)
        format_type = self.get_result_format()
        print(f"Processing complete. Result format: {format_type}")
        return result

class JSONProcessor(AbstractProcessor):
    def __init__(self):
        super().__init__("JSON Processor")
    
    def process_data(self, data):  # 必须重写抽象方法
        import json
        if isinstance(data, dict):
            return json.dumps(data, indent=2)
        else:
            return json.dumps({"data": str(data)}, indent=2)
    
    def get_result_format(self):  # 必须重写抽象方法
        return "JSON"

class XMLProcessor(AbstractProcessor):
    def __init__(self):
        super().__init__("XML Processor")
    
    def process_data(self, data):  # 必须重写抽象方法
        if isinstance(data, dict):
            xml_parts = ["<root>"]
            for key, value in data.items():
                xml_parts.append(f"  <{key}>{value}</{key}>")
            xml_parts.append("</root>")
            return "\n".join(xml_parts)
        else:
            return f"<root><data>{data}</data></root>"
    
    def get_result_format(self):  # 必须重写抽象方法
        return "XML"

print("\n=== 抽象方法重写演示 ===")

# 创建具体的处理器
json_processor = JSONProcessor()
xml_processor = XMLProcessor()

# 测试数据
test_data = {"name": "Alice", "age": 30, "city": "New York"}

print("JSON处理器:")
json_result = json_processor.run(test_data)
print(json_result)

print("\nXML处理器:")
xml_result = xml_processor.run(test_data)
print(xml_result)

# 尝试创建抽象类实例（会出错）
try:
    abstract_processor = AbstractProcessor("Test")
except TypeError as e:
    print(f"\n无法实例化抽象类: {e}")
```

## 最佳实践总结

```python
print("\n=== 方法重写最佳实践总结 ===")
print("""
方法重写的最佳实践:

1. 保持方法签名一致
   - 参数数量、类型和默认值应该保持一致
   - 返回值类型应该兼容

2. 合理使用super()
   - 在需要扩展父类功能时使用super()
   - 在构造函数中总是调用super().__init__()

3. 文档和注释
   - 清楚地说明重写的目的和行为变化
   - 保持文档字符串的一致性

4. 遵循里氏替换原则
   - 子类对象应该能够替换父类对象
   - 不要在重写中改变方法的基本契约

5. 测试重写的方法
   - 确保重写的方法在各种情况下都能正常工作
   - 测试与父类方法的交互

6. 避免常见错误
   - 不要随意改变方法签名
   - 不要完全忽略父类的重要功能
   - 注意异常处理的一致性

方法重写是实现多态性的关键机制，正确使用能够让代码更加灵活和可扩展！
""")
```

## 学习要点

1. **方法重写概念**：子类重新定义父类的方法以实现不同行为
2. **重写语法**：在子类中定义与父类同名的方法
3. **super()使用**：调用父类方法来扩展而非完全替换功能
4. **多态性实现**：通过方法重写实现相同接口的不同行为
5. **方法签名一致性**：重写时应保持参数和返回值的兼容性
6. **抽象方法重写**：子类必须实现父类的抽象方法
7. **最佳实践**：合理使用super()，保持接口一致性，遵循设计原则

## 注意事项

- 重写方法时要保持方法签名的一致性
- 使用super()来扩展父类功能而不是完全替换
- 重写的方法应该遵循里氏替换原则
- 抽象方法必须在子类中实现
- 注意异常处理和错误情况的一致性
- 适当的文档说明重写的目的和行为变化