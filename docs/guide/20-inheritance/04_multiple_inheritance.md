# 多继承

多继承是Python面向对象编程的一个强大特性，允许一个类同时继承多个父类的属性和方法。虽然功能强大，但也需要谨慎使用以避免复杂性和潜在问题。

## 多继承的基本概念

多继承允许一个子类继承多个父类，从而获得所有父类的属性和方法。

```python
# 1. 多继承的基本语法
class Flyable:
    def __init__(self):
        self.can_fly = True
        print("Flyable.__init__: 获得飞行能力")
    
    def fly(self):
        if self.can_fly:
            return "正在飞行中..."
        return "无法飞行"
    
    def take_off(self):
        return "起飞！"
    
    def land(self):
        return "着陆！"

class Swimmable:
    def __init__(self):
        self.can_swim = True
        print("Swimmable.__init__: 获得游泳能力")
    
    def swim(self):
        if self.can_swim:
            return "正在游泳中..."
        return "无法游泳"
    
    def dive(self):
        return "潜水！"
    
    def surface(self):
        return "浮出水面！"

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"Animal.__init__: 创建动物 {name} ({species})")
    
    def eat(self):
        return f"{self.name} 正在吃东西"
    
    def sleep(self):
        return f"{self.name} 正在睡觉"
    
    def make_sound(self):
        return f"{self.name} 发出声音"

# 多继承：鸭子既能飞又能游泳
class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        print(f"Duck.__init__ 开始初始化 {name}")
        
        # 注意：多继承中的初始化需要小心处理
        Animal.__init__(self, name, "鸭子")
        Flyable.__init__(self)
        Swimmable.__init__(self)
        
        self.feather_color = "棕色"
        print(f"Duck.__init__ 完成初始化 {name}")
    
    def make_sound(self):
        # 重写父类方法
        return f"{self.name} 嘎嘎叫"
    
    def show_abilities(self):
        abilities = []
        abilities.append(self.eat())
        abilities.append(self.fly())
        abilities.append(self.swim())
        return abilities

print("=== 多继承基本概念演示 ===")

# 创建鸭子实例
duck = Duck("唐老鸭")
print()

print("鸭子的基本信息:")
print(f"名字: {duck.name}")
print(f"种类: {duck.species}")
print(f"羽毛颜色: {duck.feather_color}")
print(f"声音: {duck.make_sound()}")
print()

print("鸭子的能力展示:")
for ability in duck.show_abilities():
    print(f"- {ability}")

print(f"- {duck.take_off()}")
print(f"- {duck.dive()}")
print(f"- {duck.surface()}")
print(f"- {duck.land()}")
print()
```

## 方法解析顺序（MRO）

在多继承中，Python使用C3线性化算法来确定方法解析顺序（Method Resolution Order, MRO）。

```python
# 2. 方法解析顺序演示
class A:
    def method(self):
        print("A.method")
        return "A"
    
    def only_in_a(self):
        return "这个方法只在A中"

class B:
    def method(self):
        print("B.method")
        return "B"
    
    def only_in_b(self):
        return "这个方法只在B中"

class C:
    def method(self):
        print("C.method")
        return "C"
    
    def only_in_c(self):
        return "这个方法只在C中"

# 多继承类
class MultipleInheritance(A, B, C):
    def show_mro_demo(self):
        print("调用method()方法:")
        result = self.method()  # 会调用哪个类的method？
        print(f"返回值: {result}")
        
        print("\n调用各个父类特有的方法:")
        print(f"A特有方法: {self.only_in_a()}")
        print(f"B特有方法: {self.only_in_b()}")
        print(f"C特有方法: {self.only_in_c()}")

print("=== 方法解析顺序(MRO)演示 ===")

# 查看MRO
print("MultipleInheritance类的MRO:")
for i, cls in enumerate(MultipleInheritance.__mro__):
    print(f"  {i+1}. {cls.__name__}")
print()

# 测试方法调用
mi = MultipleInheritance()
mi.show_mro_demo()
print()

# 不同继承顺序的影响
class DifferentOrder(C, B, A):
    pass

print("DifferentOrder类的MRO (继承顺序: C, B, A):")
for i, cls in enumerate(DifferentOrder.__mro__):
    print(f"  {i+1}. {cls.__name__}")

print("\n不同继承顺序的方法调用:")
do = DifferentOrder()
result = do.method()  # 现在会调用C.method
print(f"返回值: {result}")
print()
```

## 菱形继承问题

菱形继承是多继承中的一个经典问题，当多个父类继承自同一个基类时会出现。

```python
# 3. 菱形继承问题演示
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Vehicle.__init__: {brand} {model}")
    
    def start(self):
        print(f"{self.brand} {self.model} 启动")
        return True
    
    def stop(self):
        print(f"{self.brand} {self.model} 停止")
        return True
    
    def get_info(self):
        return f"{self.brand} {self.model}"

class LandVehicle(Vehicle):
    def __init__(self, brand, model, wheels):
        super().__init__(brand, model)
        self.wheels = wheels
        print(f"LandVehicle.__init__: {wheels} 个轮子")
    
    def drive(self):
        return f"{self.get_info()} 在陆地上行驶"
    
    def park(self):
        return f"{self.get_info()} 已停车"

class WaterVehicle(Vehicle):
    def __init__(self, brand, model, displacement):
        super().__init__(brand, model)
        self.displacement = displacement
        print(f"WaterVehicle.__init__: 排水量 {displacement} 吨")
    
    def sail(self):
        return f"{self.get_info()} 在水上航行"
    
    def anchor(self):
        return f"{self.get_info()} 已抛锚"

# 菱形继承：水陆两用车
class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def __init__(self, brand, model, wheels, displacement):
        print(f"AmphibiousVehicle.__init__ 开始: {brand} {model}")
        
        # 菱形继承中的初始化问题
        # 方法1：使用super()（推荐）
        # 注意：这里需要小心处理参数
        Vehicle.__init__(self, brand, model)  # 直接调用基类
        
        # 手动初始化各个父类的特有属性
        self.wheels = wheels
        self.displacement = displacement
        
        print(f"AmphibiousVehicle.__init__ 完成")
    
    def switch_to_land_mode(self):
        return f"{self.get_info()} 切换到陆地模式"
    
    def switch_to_water_mode(self):
        return f"{self.get_info()} 切换到水上模式"
    
    def show_capabilities(self):
        capabilities = []
        capabilities.append(self.drive())  # 来自LandVehicle
        capabilities.append(self.sail())   # 来自WaterVehicle
        return capabilities

print("=== 菱形继承问题演示 ===")

# 查看菱形继承的MRO
print("AmphibiousVehicle类的MRO:")
for i, cls in enumerate(AmphibiousVehicle.__mro__):
    print(f"  {i+1}. {cls.__name__}")
print()

# 创建水陆两用车
amphibious = AmphibiousVehicle("DUKW", "水陆两用车", 6, 2.5)
print()

print("水陆两用车信息:")
print(f"基本信息: {amphibious.get_info()}")
print(f"轮子数量: {amphibious.wheels}")
print(f"排水量: {amphibious.displacement} 吨")
print()

print("启动和模式切换:")
amphibious.start()
print(amphibious.switch_to_land_mode())
print(amphibious.switch_to_water_mode())
print()

print("能力展示:")
for capability in amphibious.show_capabilities():
    print(f"- {capability}")

print(f"- {amphibious.park()}")
print(f"- {amphibious.anchor()}")
amphibious.stop()
print()
```

## 使用Mixin模式

Mixin是一种设计模式，通过小的、专门的类来提供特定功能，这些类设计用于与其他类组合使用。

```python
# 4. Mixin模式演示
class TimestampMixin:
    """时间戳混入类"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from datetime import datetime
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def touch(self):
        """更新时间戳"""
        from datetime import datetime
        self.updated_at = datetime.now()
    
    def get_age(self):
        """获取对象存在时间"""
        from datetime import datetime
        age = datetime.now() - self.created_at
        return f"{age.total_seconds():.2f} 秒"

class SerializableMixin:
    """序列化混入类"""
    def to_dict(self):
        """转换为字典"""
        result = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                if hasattr(value, 'isoformat'):  # datetime对象
                    result[key] = value.isoformat()
                else:
                    result[key] = str(value)
        return result
    
    def to_json(self):
        """转换为JSON字符串"""
        import json
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)

class ValidatorMixin:
    """验证混入类"""
    def validate(self):
        """验证对象状态"""
        errors = []
        
        # 检查必需属性
        required_attrs = getattr(self, '_required_attributes', [])
        for attr in required_attrs:
            if not hasattr(self, attr) or getattr(self, attr) is None:
                errors.append(f"缺少必需属性: {attr}")
        
        # 检查属性类型
        type_constraints = getattr(self, '_type_constraints', {})
        for attr, expected_type in type_constraints.items():
            if hasattr(self, attr):
                value = getattr(self, attr)
                if value is not None and not isinstance(value, expected_type):
                    errors.append(f"属性 {attr} 类型错误: 期望 {expected_type.__name__}, 实际 {type(value).__name__}")
        
        return errors
    
    def is_valid(self):
        """检查对象是否有效"""
        return len(self.validate()) == 0

# 基础用户类
class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
        
        # 验证约束
        self._required_attributes = ['username', 'email', 'age']
        self._type_constraints = {
            'username': str,
            'email': str,
            'age': int
        }
        
        super().__init__()  # 调用mixin的初始化
    
    def update_profile(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.touch()  # 更新时间戳
    
    def __str__(self):
        return f"User(username='{self.username}', email='{self.email}', age={self.age})"

# 组合多个Mixin的增强用户类
class EnhancedUser(User, TimestampMixin, SerializableMixin, ValidatorMixin):
    def __init__(self, username, email, age):
        super().__init__(username, email, age)
    
    def get_summary(self):
        return {
            'basic_info': str(self),
            'age': self.get_age(),
            'valid': self.is_valid(),
            'validation_errors': self.validate()
        }

print("=== Mixin模式演示 ===")

# 查看EnhancedUser的MRO
print("EnhancedUser类的MRO:")
for i, cls in enumerate(EnhancedUser.__mro__):
    print(f"  {i+1}. {cls.__name__}")
print()

# 创建增强用户
user = EnhancedUser("张三", "zhangsan@example.com", 25)
print(f"创建用户: {user}")
print(f"对象年龄: {user.get_age()}")
print()

# 验证功能
print("验证结果:")
print(f"是否有效: {user.is_valid()}")
errors = user.validate()
if errors:
    for error in errors:
        print(f"- {error}")
else:
    print("- 没有验证错误")
print()

# 序列化功能
print("序列化结果:")
print("字典格式:")
user_dict = user.to_dict()
for key, value in user_dict.items():
    print(f"  {key}: {value}")

print("\nJSON格式:")
print(user.to_json())
print()

# 更新和时间戳
print("更新用户信息:")
import time
time.sleep(1)  # 等待1秒
user.update_profile(age=26, email="zhangsan_new@example.com")
print(f"更新后: {user}")
print(f"对象年龄: {user.get_age()}")
print()

# 获取摘要
print("用户摘要:")
summary = user.get_summary()
for key, value in summary.items():
    print(f"{key}: {value}")
print()
```

## 多继承的实际应用

```python
# 5. 多继承的实际应用场景
class Readable:
    """可读接口"""
    def read(self, size=-1):
        raise NotImplementedError("子类必须实现read方法")
    
    def readline(self):
        raise NotImplementedError("子类必须实现readline方法")
    
    def readlines(self):
        lines = []
        while True:
            line = self.readline()
            if not line:
                break
            lines.append(line)
        return lines

class Writable:
    """可写接口"""
    def write(self, data):
        raise NotImplementedError("子类必须实现write方法")
    
    def writelines(self, lines):
        for line in lines:
            self.write(line)
    
    def flush(self):
        pass  # 默认实现

class Seekable:
    """可定位接口"""
    def seek(self, position):
        raise NotImplementedError("子类必须实现seek方法")
    
    def tell(self):
        raise NotImplementedError("子类必须实现tell方法")

class Closable:
    """可关闭接口"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._closed = False
    
    def close(self):
        self._closed = True
    
    def closed(self):
        return self._closed
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

# 内存文件类：实现多个接口
class MemoryFile(Readable, Writable, Seekable, Closable):
    def __init__(self, initial_data=""):
        super().__init__()
        self._data = initial_data
        self._position = 0
    
    def _check_closed(self):
        if self._closed:
            raise ValueError("I/O operation on closed file")
    
    def read(self, size=-1):
        self._check_closed()
        if size == -1:
            result = self._data[self._position:]
            self._position = len(self._data)
        else:
            result = self._data[self._position:self._position + size]
            self._position += len(result)
        return result
    
    def readline(self):
        self._check_closed()
        start = self._position
        newline_pos = self._data.find('\n', start)
        
        if newline_pos == -1:
            # 没有找到换行符，读取到末尾
            result = self._data[start:]
            self._position = len(self._data)
        else:
            # 包含换行符
            result = self._data[start:newline_pos + 1]
            self._position = newline_pos + 1
        
        return result
    
    def write(self, data):
        self._check_closed()
        # 在当前位置插入数据
        self._data = self._data[:self._position] + data + self._data[self._position:]
        self._position += len(data)
        return len(data)
    
    def seek(self, position):
        self._check_closed()
        self._position = max(0, min(position, len(self._data)))
        return self._position
    
    def tell(self):
        self._check_closed()
        return self._position
    
    def truncate(self, size=None):
        self._check_closed()
        if size is None:
            size = self._position
        self._data = self._data[:size]
        self._position = min(self._position, size)
    
    def getvalue(self):
        """获取完整内容"""
        return self._data

print("=== 多继承实际应用演示 ===")

# 查看MemoryFile的MRO
print("MemoryFile类的MRO:")
for i, cls in enumerate(MemoryFile.__mro__):
    print(f"  {i+1}. {cls.__name__}")
print()

# 测试内存文件
print("内存文件操作测试:")

# 使用上下文管理器
with MemoryFile("Hello\nWorld\nPython\n") as f:
    print(f"初始内容: {repr(f.getvalue())}")
    print(f"当前位置: {f.tell()}")
    
    # 读取操作
    print(f"读取5个字符: {repr(f.read(5))}")
    print(f"当前位置: {f.tell()}")
    
    print(f"读取一行: {repr(f.readline())}")
    print(f"当前位置: {f.tell()}")
    
    # 定位操作
    f.seek(0)
    print(f"重置位置后: {f.tell()}")
    
    # 读取所有行
    f.seek(0)
    lines = f.readlines()
    print(f"所有行: {lines}")
    
    # 写入操作
    f.seek(0)
    f.write("New ")
    print(f"写入后内容: {repr(f.getvalue())}")
    
    # 追加写入
    f.seek(len(f.getvalue()))
    f.write("\nAppended line\n")
    print(f"追加后内容: {repr(f.getvalue())}")

print("文件已自动关闭")
print()
```

## 多继承的最佳实践

```python
# 6. 多继承最佳实践
print("=== 多继承最佳实践 ===")

# 实践1：使用抽象基类定义接口
from abc import ABC, abstractmethod

class Drawable(ABC):
    """可绘制接口"""
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def get_area(self):
        pass

class Movable(ABC):
    """可移动接口"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    @abstractmethod
    def move(self, dx, dy):
        pass
    
    def get_position(self):
        return (self.x, self.y)

class Resizable(ABC):
    """可调整大小接口"""
    @abstractmethod
    def resize(self, factor):
        pass

# 实践2：使用组合优于继承的原则
class Shape(Drawable, Movable):
    """形状基类"""
    def __init__(self, x=0, y=0, color="black"):
        super().__init__(x, y)
        self.color = color
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def set_color(self, color):
        self.color = color

class Rectangle(Shape, Resizable):
    """矩形类"""
    def __init__(self, width, height, x=0, y=0, color="black"):
        super().__init__(x, y, color)
        self.width = width
        self.height = height
    
    def draw(self):
        return f"绘制{self.color}矩形 at ({self.x}, {self.y}), 大小: {self.width}x{self.height}"
    
    def get_area(self):
        return self.width * self.height
    
    def resize(self, factor):
        self.width *= factor
        self.height *= factor

class Circle(Shape, Resizable):
    """圆形类"""
    def __init__(self, radius, x=0, y=0, color="black"):
        super().__init__(x, y, color)
        self.radius = radius
    
    def draw(self):
        return f"绘制{self.color}圆形 at ({self.x}, {self.y}), 半径: {self.radius}"
    
    def get_area(self):
        import math
        return math.pi * self.radius ** 2
    
    def resize(self, factor):
        self.radius *= factor

# 实践3：使用协议和类型提示
from typing import Protocol

class Printable(Protocol):
    """可打印协议"""
    def __str__(self) -> str:
        ...

def print_objects(objects: list[Printable]):
    """打印对象列表"""
    for obj in objects:
        print(f"- {obj}")

# 测试最佳实践
print("创建和操作图形:")

rect = Rectangle(10, 5, 0, 0, "红色")
circle = Circle(3, 5, 5, "蓝色")

shapes = [rect, circle]

print("初始状态:")
for shape in shapes:
    print(f"- {shape.draw()}")
    print(f"  面积: {shape.get_area():.2f}")
    print(f"  位置: {shape.get_position()}")

print("\n移动图形:")
rect.move(2, 3)
circle.move(-1, 2)

for shape in shapes:
    print(f"- {shape.draw()}")
    print(f"  位置: {shape.get_position()}")

print("\n调整大小:")
rect.resize(1.5)
circle.resize(0.8)

for shape in shapes:
    print(f"- {shape.draw()}")
    print(f"  面积: {shape.get_area():.2f}")

print("\n改变颜色:")
rect.set_color("绿色")
circle.set_color("黄色")

for shape in shapes:
    print(f"- {shape.draw()}")
print()
```

## 多继承的注意事项和陷阱

```python
# 7. 多继承的注意事项
print("=== 多继承注意事项 ===")

# 陷阱1：方法名冲突
class Parent1:
    def method(self):
        return "Parent1.method"
    
    def common_method(self):
        return "Parent1.common_method"

class Parent2:
    def method(self):
        return "Parent2.method"
    
    def common_method(self):
        return "Parent2.common_method"

class Child(Parent1, Parent2):
    def test_methods(self):
        print(f"调用method(): {self.method()}")  # 只会调用Parent1的方法
        print(f"调用common_method(): {self.common_method()}")  # 只会调用Parent1的方法
        
        # 如果需要调用特定父类的方法
        print(f"显式调用Parent1.method(): {Parent1.method(self)}")
        print(f"显式调用Parent2.method(): {Parent2.method(self)}")

print("方法名冲突演示:")
child = Child()
child.test_methods()
print()

# 陷阱2：初始化顺序问题
class Base:
    def __init__(self, value):
        self.value = value
        print(f"Base.__init__: value = {value}")

class Mixin1:
    def __init__(self, *args, **kwargs):
        print("Mixin1.__init__")
        super().__init__(*args, **kwargs)

class Mixin2:
    def __init__(self, *args, **kwargs):
        print("Mixin2.__init__")
        super().__init__(*args, **kwargs)

class GoodMultiple(Mixin1, Mixin2, Base):
    def __init__(self, value, extra):
        print("GoodMultiple.__init__ 开始")
        self.extra = extra
        super().__init__(value)  # 会按照MRO顺序调用
        print("GoodMultiple.__init__ 结束")

print("正确的初始化顺序:")
print("GoodMultiple的MRO:")
for i, cls in enumerate(GoodMultiple.__mro__):
    print(f"  {i+1}. {cls.__name__}")

good = GoodMultiple("test", "extra_data")
print(f"结果: value={good.value}, extra={good.extra}")
print()

# 陷阱3：isinstance和issubclass的复杂性
print("类型检查复杂性:")
print(f"isinstance(good, Base): {isinstance(good, Base)}")
print(f"isinstance(good, Mixin1): {isinstance(good, Mixin1)}")
print(f"isinstance(good, Mixin2): {isinstance(good, Mixin2)}")
print(f"isinstance(good, GoodMultiple): {isinstance(good, GoodMultiple)}")
print()

print(f"issubclass(GoodMultiple, Base): {issubclass(GoodMultiple, Base)}")
print(f"issubclass(GoodMultiple, Mixin1): {issubclass(GoodMultiple, Mixin1)}")
print(f"issubclass(GoodMultiple, (Base, Mixin1)): {issubclass(GoodMultiple, (Base, Mixin1))}")
print()
```

## 总结和建议

```python
print("=== 多继承总结 ===")
print("""
多继承的核心要点:

1. 基本概念
   - 允许一个类继承多个父类
   - 获得所有父类的属性和方法
   - 遵循方法解析顺序(MRO)

2. 方法解析顺序(MRO)
   - 使用C3线性化算法
   - 确保每个类只被访问一次
   - 保持继承的一致性

3. 主要优势
   - 代码重用性高
   - 可以组合多种功能
   - 支持接口的多重实现

4. 常见问题
   - 菱形继承问题
   - 方法名冲突
   - 初始化复杂性
   - 代码可读性下降

5. 最佳实践
   - 优先使用组合而非继承
   - 使用Mixin模式提供功能
   - 保持接口简单和专一
   - 使用抽象基类定义契约
   - 小心处理初始化顺序

6. 使用建议
   - 谨慎使用多继承
   - 优先考虑组合模式
   - 使用协议和类型提示
   - 保持类的职责单一
   - 充分测试继承关系

多继承是强大的工具，但需要谨慎使用。
在大多数情况下，组合模式是更好的选择！
""")
```

## 学习要点

1. **多继承语法**：`class Child(Parent1, Parent2):`的基本语法
2. **MRO理解**：方法解析顺序决定方法调用的优先级
3. **菱形继承**：理解和解决菱形继承带来的问题
4. **Mixin模式**：使用小而专一的类提供特定功能
5. **初始化处理**：在多继承中正确处理`__init__`方法
6. **方法冲突**：处理多个父类中同名方法的冲突
7. **最佳实践**：何时使用多继承，何时选择组合

## 注意事项

- 多继承会增加代码复杂性，应谨慎使用
- 理解MRO对方法调用顺序的影响
- 在多继承中使用`super()`要特别小心
- 优先考虑组合模式而非多继承
- 使用抽象基类和协议定义清晰的接口
- 保持类的职责单一，避免过度复杂的继承关系