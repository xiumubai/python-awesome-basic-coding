# 继承的基本概念和语法

继承是面向对象编程的核心特性之一，它允许我们创建新类来扩展现有类的功能，实现代码重用和层次化设计。

## 什么是继承？

继承是一种机制，允许一个类（子类/派生类）获得另一个类（父类/基类）的属性和方法。子类可以：
- 继承父类的所有属性和方法
- 添加自己特有的属性和方法
- 重写父类的方法以实现不同的行为

## 继承的优势

```python
# 1. 代码重用
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating...")
    
    def sleep(self):
        print(f"{self.name} is sleeping...")
    
    def make_sound(self):
        print(f"{self.name} makes a sound")

print("=== 继承的优势演示 ===")
print("1. 代码重用 - 基类Animal定义了通用的动物行为")
```

## 基本继承语法

```python
# 2. 基本继承语法
class Dog(Animal):  # Dog继承自Animal
    def __init__(self, name, breed):
        super().__init__(name, "犬类")  # 调用父类构造函数
        self.breed = breed
    
    def make_sound(self):  # 重写父类方法
        print(f"{self.name} barks: Woof! Woof!")
    
    def fetch(self):  # 子类特有方法
        print(f"{self.name} is fetching the ball")

class Cat(Animal):  # Cat也继承自Animal
    def __init__(self, name, color):
        super().__init__(name, "猫科")
        self.color = color
    
    def make_sound(self):  # 重写父类方法
        print(f"{self.name} meows: Meow! Meow!")
    
    def climb(self):  # 子类特有方法
        print(f"{self.name} is climbing the tree")

print("\n2. 基本继承语法演示")
print("语法：class 子类名(父类名):")
```

## 继承的实际应用

```python
# 3. 创建对象并测试继承
print("\n=== 继承的实际应用 ===")

# 创建Dog对象
dog = Dog("旺财", "金毛")
print(f"创建狗对象: {dog.name}, 品种: {dog.breed}, 物种: {dog.species}")

# 调用继承的方法
dog.eat()    # 继承自Animal
dog.sleep()  # 继承自Animal

# 调用重写的方法
dog.make_sound()  # Dog类重写的方法

# 调用子类特有方法
dog.fetch()  # Dog类特有方法

print()

# 创建Cat对象
cat = Cat("咪咪", "橘色")
print(f"创建猫对象: {cat.name}, 颜色: {cat.color}, 物种: {cat.species}")

# 调用继承的方法
cat.eat()    # 继承自Animal
cat.sleep()  # 继承自Animal

# 调用重写的方法
cat.make_sound()  # Cat类重写的方法

# 调用子类特有方法
cat.climb()  # Cat类特有方法
```

## 属性继承详解

```python
# 4. 属性继承详解
print("\n=== 属性继承详解 ===")

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand      # 公共属性
        self.model = model      # 公共属性
        self.year = year        # 公共属性
        self._mileage = 0       # 受保护属性
        self.__vin = "VIN123"   # 私有属性
    
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started")
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"
    
    def drive(self, distance):
        self._mileage += distance
        print(f"Drove {distance} km, total mileage: {self._mileage} km")

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)  # 继承父类属性
        self.doors = doors  # 子类特有属性
    
    def open_trunk(self):
        print(f"{self.brand} {self.model} trunk opened")
    
    def get_full_info(self):
        base_info = self.get_info()  # 调用继承的方法
        return f"{base_info}, {self.doors} doors, mileage: {self._mileage} km"

# 测试属性继承
car = Car("丰田", "凯美瑞", 2023, 4)
print(f"汽车信息: {car.get_full_info()}")

car.start_engine()  # 继承的方法
car.drive(100)      # 继承的方法，修改继承的属性
car.open_trunk()    # 子类特有方法

print(f"更新后信息: {car.get_full_info()}")

# 访问继承的属性
print(f"品牌: {car.brand}")        # 公共属性
print(f"里程: {car._mileage}")     # 受保护属性（可访问但不推荐）
# print(car.__vin)  # 私有属性，无法直接访问
```

## 类型检查函数

```python
# 5. isinstance()和issubclass()函数
print("\n=== 类型检查函数 ===")

# isinstance() - 检查对象是否是某个类的实例
print("isinstance() 函数用法:")
print(f"dog是Dog的实例: {isinstance(dog, Dog)}")
print(f"dog是Animal的实例: {isinstance(dog, Animal)}")
print(f"dog是Cat的实例: {isinstance(dog, Cat)}")
print(f"car是Vehicle的实例: {isinstance(car, Vehicle)}")
print(f"car是Car的实例: {isinstance(car, Car)}")

print("\nissubclass() 函数用法:")
# issubclass() - 检查一个类是否是另一个类的子类
print(f"Dog是Animal的子类: {issubclass(Dog, Animal)}")
print(f"Cat是Animal的子类: {issubclass(Cat, Animal)}")
print(f"Car是Vehicle的子类: {issubclass(Car, Vehicle)}")
print(f"Dog是Cat的子类: {issubclass(Dog, Cat)}")

# 检查多个类型
print(f"\ndog是(Dog, Cat)中任一类型的实例: {isinstance(dog, (Dog, Cat))}")
print(f"Animal是(Dog, Cat)中任一类型的子类: {issubclass(Animal, (Dog, Cat))}")
```

## 继承层次结构

```python
# 6. 多层继承
print("\n=== 多层继承演示 ===")

class Mammal(Animal):
    def __init__(self, name, species, body_temperature):
        super().__init__(name, species)
        self.body_temperature = body_temperature
        self.is_warm_blooded = True
    
    def regulate_temperature(self):
        print(f"{self.name} maintains body temperature at {self.body_temperature}°C")

class Primate(Mammal):
    def __init__(self, name, species, intelligence_level):
        super().__init__(name, species, 37.0)  # 灵长类体温约37°C
        self.intelligence_level = intelligence_level
        self.has_opposable_thumbs = True
    
    def use_tools(self):
        print(f"{self.name} can use tools (intelligence level: {self.intelligence_level})")

class Human(Primate):
    def __init__(self, name, language):
        super().__init__(name, "智人", 10)  # 人类智力水平设为10
        self.language = language
        self.can_speak = True
    
    def speak(self):
        print(f"{self.name} speaks {self.language}")
    
    def make_sound(self):  # 重写祖先类的方法
        print(f"{self.name} says: Hello!")

# 测试多层继承
human = Human("Alice", "English")
print(f"人类对象: {human.name}, 语言: {human.language}")
print(f"物种: {human.species}, 智力水平: {human.intelligence_level}")
print(f"体温: {human.body_temperature}°C, 温血动物: {human.is_warm_blooded}")

# 调用各层级的方法
human.eat()                    # 来自Animal
human.regulate_temperature()   # 来自Mammal
human.use_tools()             # 来自Primate
human.speak()                 # Human特有方法
human.make_sound()            # Human重写的方法

# 检查继承关系
print(f"\nHuman是Animal的子类: {issubclass(Human, Animal)}")
print(f"human是Mammal的实例: {isinstance(human, Mammal)}")
print(f"human是Primate的实例: {isinstance(human, Primate)}")
```

## 方法解析顺序预览

```python
# 7. 方法解析顺序（MRO）预览
print("\n=== 方法解析顺序预览 ===")

# 查看类的方法解析顺序
print("Human类的MRO:")
for i, cls in enumerate(Human.__mro__):
    print(f"  {i+1}. {cls.__name__}")

print("\nDog类的MRO:")
for i, cls in enumerate(Dog.__mro__):
    print(f"  {i+1}. {cls.__name__}")

# MRO决定了方法查找的顺序
print("\n当调用human.make_sound()时，Python按MRO顺序查找:")
print("1. 首先在Human类中查找 -> 找到Human.make_sound()")
print("2. 如果Human中没有，则在Primate中查找")
print("3. 然后在Mammal中查找")
print("4. 最后在Animal中查找")
```

## 最佳实践和注意事项

```python
# 8. 继承的最佳实践
print("\n=== 继承的最佳实践 ===")

class BestPracticeBase:
    """演示继承最佳实践的基类"""
    
    def __init__(self, name):
        self.name = name
        print(f"BestPracticeBase.__init__: {name}")
    
    def public_method(self):
        """公共方法，子类可以调用和重写"""
        return f"Base public method for {self.name}"
    
    def _protected_method(self):
        """受保护方法，建议只在类内部和子类中使用"""
        return f"Base protected method for {self.name}"
    
    def __private_method(self):
        """私有方法，子类无法直接访问"""
        return f"Base private method for {self.name}"
    
    def call_private(self):
        """通过公共方法访问私有方法"""
        return self.__private_method()

class BestPracticeChild(BestPracticeBase):
    """演示最佳实践的子类"""
    
    def __init__(self, name, child_attr):
        super().__init__(name)  # 总是调用父类构造函数
        self.child_attr = child_attr
        print(f"BestPracticeChild.__init__: {child_attr}")
    
    def public_method(self):
        """重写父类方法，但保持接口一致"""
        base_result = super().public_method()  # 调用父类方法
        return f"Child extends: {base_result} with {self.child_attr}"
    
    def child_specific_method(self):
        """子类特有方法"""
        # 可以调用受保护方法
        protected_result = self._protected_method()
        return f"Child method uses: {protected_result}"

# 测试最佳实践
child = BestPracticeChild("TestObject", "ChildAttribute")
print(f"\n公共方法调用: {child.public_method()}")
print(f"子类特有方法: {child.child_specific_method()}")
print(f"通过公共接口访问私有方法: {child.call_private()}")

# 尝试访问私有方法（会失败）
try:
    child.__private_method()
except AttributeError as e:
    print(f"\n无法直接访问私有方法: {e}")
```

## 总结

```python
print("\n=== 继承基础知识总结 ===")
print("""
1. 继承语法: class 子类(父类):
2. 子类自动获得父类的所有属性和方法
3. 使用super()调用父类方法
4. 子类可以重写父类方法
5. 子类可以添加自己的属性和方法
6. isinstance()检查对象类型
7. issubclass()检查类继承关系
8. 方法解析顺序(MRO)决定方法查找顺序

继承的核心思想:
- 代码重用: 避免重复编写相同代码
- 层次化设计: 建立清晰的类层次结构
- 多态性: 不同子类可以有不同的行为实现
- 扩展性: 容易添加新的子类和功能
""")

print("\n继承是面向对象编程的基础，掌握好继承对于理解更高级的概念至关重要！")
```

## 学习要点

1. **继承语法**：`class Child(Parent):` 是Python中定义继承的基本语法
2. **super()函数**：用于调用父类方法，特别是在构造函数中
3. **方法重写**：子类可以重新定义父类的方法来实现不同行为
4. **属性继承**：子类自动获得父类的所有属性
5. **类型检查**：使用`isinstance()`和`issubclass()`进行类型和继承关系检查
6. **访问控制**：理解公共、受保护和私有成员的继承行为
7. **最佳实践**：总是在子类构造函数中调用`super().__init__()`

## 注意事项

- 继承表示"is-a"关系，只有在逻辑上成立时才使用继承
- 避免过深的继承层次，通常不超过3-4层
- 重写方法时保持方法签名的一致性
- 合理使用访问控制，保护类的内部实现
- 理解MRO对方法查找的影响