#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
super()函数的使用

super()函数是Python中用于调用父类方法的内置函数。
它提供了一种优雅的方式来访问父类的方法和属性，特别是在多继承的情况下。

学习要点：
1. super()的基本用法
2. 在构造方法中使用super()
3. 在普通方法中使用super()
4. super()在多继承中的作用
5. super()的高级用法
6. super()的注意事项
"""

# 1. super()的基本用法
print("=== 1. super()的基本用法 ===")

class Animal:
    """动物基类"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"Animal.__init__: 创建了{species} {name}")
    
    def speak(self):
        print(f"{self.name} 发出声音")
    
    def move(self):
        print(f"{self.name} 正在移动")

class Dog(Animal):
    """狗类 - 演示super()基本用法"""
    
    def __init__(self, name, breed):
        # 使用super()调用父类构造方法
        super().__init__(name, "狗")
        self.breed = breed
        print(f"Dog.__init__: 设置品种为{breed}")
    
    def speak(self):
        # 先调用父类方法
        super().speak()
        # 再添加子类特有行为
        print(f"{self.name} 汪汪叫")
    
    def move(self):
        super().move()
        print(f"{self.name} 摇着尾巴跑")

# 测试基本用法
print("创建狗对象:")
dog = Dog("旺财", "金毛")
print("\n调用方法:")
dog.speak()
dog.move()

print("\n=== 2. 不同的super()调用方式 ===")

# 2. super()的不同调用方式
class Vehicle:
    """交通工具基类"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Vehicle.__init__: {brand} {model}")
    
    def start(self):
        print(f"{self.brand} {self.model} 启动")
    
    def info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    """汽车类 - 演示不同的super()用法"""
    
    def __init__(self, brand, model, doors):
        # 方式1: 推荐的super()用法（Python 3+）
        super().__init__(brand, model)
        self.doors = doors
        print(f"Car.__init__: {doors}门汽车")
    
    def start(self):
        # 方式1: 无参数super()
        super().start()
        print("检查安全带")
        print("汽车准备就绪")
    
    def start_with_explicit_super(self):
        # 方式2: 显式指定类和实例的super()（Python 2兼容）
        super(Car, self).start()
        print("使用显式super()启动")
    
    def info(self):
        # 获取父类方法的返回值
        parent_info = super().info()
        return f"{parent_info} ({self.doors}门)"

# 测试不同的super()用法
print("创建汽车对象:")
car = Car("丰田", "卡罗拉", 4)
print("\n使用super()启动:")
car.start()
print("\n使用显式super()启动:")
car.start_with_explicit_super()
print(f"\n汽车信息: {car.info()}")

print("\n=== 3. 多层继承中的super() ===")

# 3. 多层继承中的super()
class LivingThing:
    """生物基类"""
    
    def __init__(self, name):
        self.name = name
        print(f"LivingThing.__init__: {name}")
    
    def breathe(self):
        print(f"{self.name} 正在呼吸")

class Animal2(LivingThing):
    """动物类"""
    
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
        print(f"Animal2.__init__: {species}")
    
    def breathe(self):
        super().breathe()
        print(f"{self.name} 用肺呼吸")
    
    def move(self):
        print(f"{self.name} 正在移动")

class Mammal(Animal2):
    """哺乳动物类"""
    
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color
        print(f"Mammal.__init__: {fur_color}色毛发")
    
    def breathe(self):
        super().breathe()
        print(f"{self.name} 是温血动物")
    
    def feed_young(self):
        print(f"{self.name} 给幼崽喂奶")

class Cat(Mammal):
    """猫类"""
    
    def __init__(self, name, fur_color, breed):
        super().__init__(name, "猫", fur_color)
        self.breed = breed
        print(f"Cat.__init__: {breed}品种")
    
    def breathe(self):
        super().breathe()
        print(f"{self.name} 安静地呼吸")
    
    def purr(self):
        print(f"{self.name} 发出呼噜声")

# 测试多层继承
print("创建猫对象（多层继承）:")
cat = Cat("咪咪", "白色", "波斯猫")
print("\n调用呼吸方法（展示super()链式调用）:")
cat.breathe()
print("\n调用其他方法:")
cat.move()
cat.feed_young()
cat.purr()

print("\n=== 4. super()在多继承中的应用 ===")

# 4. 多继承中的super()
class Flyable:
    """可飞行的混入类"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Flyable.__init__: 获得飞行能力")
    
    def fly(self):
        print("正在飞行")

class Swimmable:
    """可游泳的混入类"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Swimmable.__init__: 获得游泳能力")
    
    def swim(self):
        print("正在游泳")

class Bird(Animal, Flyable):
    """鸟类 - 多继承示例"""
    
    def __init__(self, name, wing_span):
        # 使用super()确保所有父类都被正确初始化
        super().__init__(name=name, species="鸟")
        self.wing_span = wing_span
        print(f"Bird.__init__: 翼展{wing_span}cm")
    
    def speak(self):
        super().speak()
        print(f"{self.name} 啁啾鸣叫")

class Duck(Bird, Swimmable):
    """鸭子类 - 多重继承"""
    
    def __init__(self, name, wing_span, webbed_feet=True):
        super().__init__(name=name, wing_span=wing_span)
        self.webbed_feet = webbed_feet
        print(f"Duck.__init__: 蹼足={webbed_feet}")
    
    def speak(self):
        print(f"{self.name} 嘎嘎叫")
        # 注意：这里没有调用super()，完全重写了方法

# 测试多继承
print("创建鸭子对象（多重继承）:")
duck = Duck("唐老鸭", 60)
print("\n鸭子的能力:")
duck.speak()
duck.fly()
duck.swim()
duck.move()

# 查看方法解析顺序
print(f"\nDuck类的MRO: {Duck.__mro__}")

print("\n=== 5. super()的高级用法 ===")

# 5. super()的高级用法
class ConfigurableClass:
    """可配置的基类"""
    
    def __init__(self, **kwargs):
        # 处理自己的参数
        self.config = kwargs.pop('config', {})
        # 将剩余参数传递给下一个类
        super().__init__(**kwargs)
        print(f"ConfigurableClass.__init__: config={self.config}")
    
    def configure(self, key, value):
        self.config[key] = value
        print(f"配置 {key} = {value}")

class LoggableClass:
    """可记录日志的基类"""
    
    def __init__(self, **kwargs):
        self.log_enabled = kwargs.pop('log_enabled', True)
        super().__init__(**kwargs)
        print(f"LoggableClass.__init__: log_enabled={self.log_enabled}")
    
    def log(self, message):
        if self.log_enabled:
            print(f"[LOG] {message}")

class DatabaseConnection(ConfigurableClass, LoggableClass):
    """数据库连接类 - 演示复杂的多继承"""
    
    def __init__(self, host, port, **kwargs):
        self.host = host
        self.port = port
        # 使用super()确保所有父类都被初始化
        super().__init__(**kwargs)
        print(f"DatabaseConnection.__init__: {host}:{port}")
    
    def connect(self):
        self.log(f"连接到数据库 {self.host}:{self.port}")
        return True
    
    def query(self, sql):
        self.log(f"执行查询: {sql}")
        return "查询结果"

# 测试高级用法
print("创建数据库连接对象:")
db = DatabaseConnection(
    host="localhost",
    port=5432,
    config={'timeout': 30, 'pool_size': 10},
    log_enabled=True
)

print("\n使用数据库连接:")
db.connect()
db.configure('retry_count', 3)
result = db.query("SELECT * FROM users")
print(f"查询结果: {result}")

print(f"\nDatabaseConnection的MRO: {DatabaseConnection.__mro__}")

print("\n=== 6. super()的注意事项和最佳实践 ===")

# 6. super()的注意事项
class ProblematicBase:
    """演示super()使用中的问题"""
    
    def __init__(self, value):
        self.value = value
        print(f"ProblematicBase.__init__: {value}")
    
    def method(self):
        print(f"ProblematicBase.method: {self.value}")

class GoodChild(ProblematicBase):
    """正确使用super()的子类"""
    
    def __init__(self, value, extra):
        super().__init__(value)  # 正确：调用父类构造方法
        self.extra = extra
        print(f"GoodChild.__init__: {extra}")
    
    def method(self):
        super().method()  # 正确：先调用父类方法
        print(f"GoodChild.method: {self.extra}")

class BadChild(ProblematicBase):
    """错误使用super()的示例（仅用于演示）"""
    
    def __init__(self, value, extra):
        # 错误：忘记调用父类构造方法
        # super().__init__(value)  # 这行被注释掉了
        self.extra = extra
        print(f"BadChild.__init__: {extra}")
    
    def method(self):
        # 错误：没有调用父类方法，可能丢失重要功能
        print(f"BadChild.method: {self.extra}")

# 演示正确和错误的用法
print("正确使用super()的示例:")
good = GoodChild("基础值", "额外值")
good.method()

print("\n错误使用super()的示例:")
try:
    bad = BadChild("基础值", "额外值")
    bad.method()
    # 注意：BadChild没有调用父类构造方法，所以没有value属性
    print(f"BadChild的value属性: {getattr(bad, 'value', '未设置')}")
except Exception as e:
    print(f"错误: {e}")

print("\n=== super()使用最佳实践 ===")
print("""
super()使用最佳实践：

1. 构造方法中总是调用super().__init__()
   - 确保父类被正确初始化
   - 在多继承中特别重要

2. 在重写方法时考虑是否需要调用super()
   - 扩展功能时调用super()
   - 完全替换功能时可以不调用

3. 多继承时使用**kwargs传递参数
   - 确保参数能正确传递给所有父类
   - 避免参数冲突

4. 理解MRO（方法解析顺序）
   - super()按照MRO顺序调用方法
   - 使用ClassName.__mro__查看顺序

5. 保持一致的调用模式
   - 在整个继承链中保持一致的super()使用
   - 避免混合使用super()和直接调用

6. 文档化super()的使用
   - 说明为什么调用或不调用super()
   - 记录参数传递的约定
""")

if __name__ == "__main__":
    print("\nsuper()函数使用演示完成!")
    print("super()是Python继承机制中的重要工具，正确使用能让代码更加优雅和可维护。")