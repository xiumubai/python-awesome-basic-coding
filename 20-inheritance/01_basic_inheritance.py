#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
继承的基本概念和语法

继承是面向对象编程的核心概念之一，它允许一个类（子类）继承另一个类（父类）的属性和方法。
继承实现了代码的重用，建立了类之间的层次关系。

学习要点：
1. 继承的基本语法
2. 父类和子类的关系
3. 属性和方法的继承
4. isinstance()和issubclass()函数的使用
"""

# 1. 基本继承语法
print("=== 1. 基本继承语法 ===")

class Animal:
    """动物基类"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"创建了一个动物: {name}")
    
    def eat(self):
        print(f"{self.name} 正在吃东西")
    
    def sleep(self):
        print(f"{self.name} 正在睡觉")
    
    def make_sound(self):
        print(f"{self.name} 发出了声音")
    
    def __str__(self):
        return f"{self.species}: {self.name}"

# 子类继承父类
class Dog(Animal):
    """狗类，继承自Animal"""
    
    def __init__(self, name, breed):
        # 调用父类的构造方法
        super().__init__(name, "狗")
        self.breed = breed
    
    def make_sound(self):
        print(f"{self.name} 汪汪叫")
    
    def fetch(self):
        print(f"{self.name} 去捡球")

class Cat(Animal):
    """猫类，继承自Animal"""
    
    def __init__(self, name, color):
        super().__init__(name, "猫")
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} 喵喵叫")
    
    def climb(self):
        print(f"{self.name} 爬树")

# 创建对象并测试继承
dog = Dog("旺财", "金毛")
cat = Cat("咪咪", "白色")

print(f"狗: {dog}")
print(f"猫: {cat}")

# 调用继承的方法
dog.eat()  # 继承自Animal
dog.sleep()  # 继承自Animal
dog.make_sound()  # 重写的方法
dog.fetch()  # 子类特有的方法

print()
cat.eat()  # 继承自Animal
cat.sleep()  # 继承自Animal
cat.make_sound()  # 重写的方法
cat.climb()  # 子类特有的方法

print("\n=== 2. 属性继承 ===")

# 2. 属性继承示例
class Vehicle:
    """交通工具基类"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        self.is_running = True
        print(f"{self.brand} {self.model} 启动了")
    
    def stop(self):
        self.is_running = False
        print(f"{self.brand} {self.model} 停止了")
    
    def get_info(self):
        return f"{self.year}年 {self.brand} {self.model}"

class Car(Vehicle):
    """汽车类"""
    
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors  # 子类特有属性
    
    def honk(self):
        print(f"{self.brand} {self.model} 按喇叭: 嘀嘀!")

class Motorcycle(Vehicle):
    """摩托车类"""
    
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size
    
    def wheelie(self):
        print(f"{self.brand} {self.model} 做后轮着地特技!")

# 创建对象
car = Car("丰田", "卡罗拉", 2023, 4)
motorcycle = Motorcycle("本田", "CBR600", 2022, 600)

# 访问继承的属性和方法
print(f"汽车信息: {car.get_info()}, 门数: {car.doors}")
print(f"摩托车信息: {motorcycle.get_info()}, 排量: {motorcycle.engine_size}cc")

car.start()
car.honk()
car.stop()

print()
motorcycle.start()
motorcycle.wheelie()
motorcycle.stop()

print("\n=== 3. isinstance()和issubclass()函数 ===")

# 3. 类型检查
print(f"dog是Dog的实例吗? {isinstance(dog, Dog)}")
print(f"dog是Animal的实例吗? {isinstance(dog, Animal)}")
print(f"dog是Cat的实例吗? {isinstance(dog, Cat)}")

print(f"Dog是Animal的子类吗? {issubclass(Dog, Animal)}")
print(f"Cat是Animal的子类吗? {issubclass(Cat, Animal)}")
print(f"Dog是Cat的子类吗? {issubclass(Dog, Cat)}")

# 检查多个类型
print(f"car是Vehicle或Car的实例吗? {isinstance(car, (Vehicle, Car))}")

print("\n=== 4. 继承层次示例 ===")

# 4. 多层继承
class LivingThing:
    """生物基类"""
    
    def __init__(self, name):
        self.name = name
        self.alive = True
    
    def breathe(self):
        print(f"{self.name} 正在呼吸")

class Animal2(LivingThing):
    """动物类，继承自生物"""
    
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
    
    def move(self):
        print(f"{self.name} 正在移动")

class Mammal(Animal2):
    """哺乳动物类，继承自动物"""
    
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color
    
    def feed_milk(self):
        print(f"{self.name} 正在哺乳")

class Dog2(Mammal):
    """狗类，继承自哺乳动物"""
    
    def __init__(self, name, breed, fur_color):
        super().__init__(name, "狗", fur_color)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} 汪汪叫")

# 创建多层继承的对象
dog2 = Dog2("小白", "拉布拉多", "白色")

print(f"狗的信息: {dog2.name}, 品种: {dog2.breed}, 毛色: {dog2.fur_color}")

# 调用各层继承的方法
dog2.breathe()    # 来自LivingThing
dog2.move()       # 来自Animal2
dog2.feed_milk()  # 来自Mammal
dog2.bark()       # 来自Dog2

# 检查继承关系
print(f"\nDog2的继承关系:")
print(f"Dog2是Mammal的子类: {issubclass(Dog2, Mammal)}")
print(f"Dog2是Animal2的子类: {issubclass(Dog2, Animal2)}")
print(f"Dog2是LivingThing的子类: {issubclass(Dog2, LivingThing)}")

print(f"\ndog2的类型检查:")
print(f"dog2是Dog2的实例: {isinstance(dog2, Dog2)}")
print(f"dog2是Mammal的实例: {isinstance(dog2, Mammal)}")
print(f"dog2是Animal2的实例: {isinstance(dog2, Animal2)}")
print(f"dog2是LivingThing的实例: {isinstance(dog2, LivingThing)}")

print("\n=== 5. 继承的优势 ===")
print("""
继承的主要优势：
1. 代码重用：子类可以使用父类的属性和方法
2. 扩展性：可以在不修改父类的情况下扩展功能
3. 多态性：不同的子类可以有不同的实现
4. 维护性：修改父类会影响所有子类
5. 层次结构：建立清晰的类层次关系
""")

if __name__ == "__main__":
    print("\n继承基础概念演示完成!")
    print("继承让我们能够创建具有层次关系的类，实现代码重用和扩展。")