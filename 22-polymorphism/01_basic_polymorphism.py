#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多态的基本概念和原理

多态（Polymorphism）是面向对象编程的三大特性之一（封装、继承、多态）。
多态允许不同类的对象对同一消息做出响应，但具体的响应方式可以不同。

核心概念：
1. 同一个接口，不同的实现
2. 运行时决定调用哪个方法
3. 提高代码的灵活性和可扩展性
"""

# 1. 基本多态示例
class Animal:
    """动物基类"""
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        """发出声音 - 基类方法"""
        pass
    
    def move(self):
        """移动方式 - 基类方法"""
        pass

class Dog(Animal):
    """狗类"""
    def make_sound(self):
        return f"{self.name} 汪汪叫"
    
    def move(self):
        return f"{self.name} 在地上跑"

class Cat(Animal):
    """猫类"""
    def make_sound(self):
        return f"{self.name} 喵喵叫"
    
    def move(self):
        return f"{self.name} 轻巧地走路"

class Bird(Animal):
    """鸟类"""
    def make_sound(self):
        return f"{self.name} 啾啾叫"
    
    def move(self):
        return f"{self.name} 在天空中飞翔"

# 2. 多态的使用
def animal_behavior(animal):
    """展示动物行为 - 多态函数"""
    print(f"动物名称: {animal.name}")
    print(f"声音: {animal.make_sound()}")
    print(f"移动: {animal.move()}")
    print("-" * 30)

# 3. 多态在列表中的应用
def demonstrate_polymorphism():
    """演示多态的基本概念"""
    print("=== 多态基本概念演示 ===")
    
    # 创建不同类型的动物对象
    animals = [
        Dog("旺财"),
        Cat("咪咪"),
        Bird("小鸟"),
        Dog("大黄"),
        Cat("加菲")
    ]
    
    # 多态：同一个函数处理不同类型的对象
    for animal in animals:
        animal_behavior(animal)

# 4. 多态的优势示例
class Shape:
    """形状基类"""
    def area(self):
        """计算面积"""
        raise NotImplementedError("子类必须实现area方法")
    
    def perimeter(self):
        """计算周长"""
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
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
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
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def __str__(self):
        return f"三角形(边长:{self.a}, {self.b}, {self.c})"

def calculate_shapes_info(shapes):
    """计算形状信息 - 展示多态的优势"""
    print("\n=== 形状计算演示（多态优势） ===")
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

# 5. 多态与类型检查
def demonstrate_type_checking():
    """演示多态中的类型检查"""
    print("\n=== 多态与类型检查 ===")
    
    dog = Dog("小白")
    cat = Cat("小黑")
    
    # isinstance检查
    print(f"dog是Animal的实例: {isinstance(dog, Animal)}")
    print(f"cat是Animal的实例: {isinstance(cat, Animal)}")
    print(f"dog是Dog的实例: {isinstance(dog, Dog)}")
    print(f"cat是Dog的实例: {isinstance(cat, Dog)}")
    
    # hasattr检查方法是否存在
    print(f"dog有make_sound方法: {hasattr(dog, 'make_sound')}")
    print(f"cat有make_sound方法: {hasattr(cat, 'make_sound')}")

# 6. 多态的实际应用场景
class PaymentProcessor:
    """支付处理器基类"""
    def process_payment(self, amount):
        raise NotImplementedError("子类必须实现process_payment方法")

class CreditCardProcessor(PaymentProcessor):
    """信用卡支付处理器"""
    def process_payment(self, amount):
        return f"使用信用卡支付 {amount} 元"

class AlipayProcessor(PaymentProcessor):
    """支付宝支付处理器"""
    def process_payment(self, amount):
        return f"使用支付宝支付 {amount} 元"

class WechatPayProcessor(PaymentProcessor):
    """微信支付处理器"""
    def process_payment(self, amount):
        return f"使用微信支付 {amount} 元"

def process_order(processor, amount):
    """处理订单 - 多态应用"""
    result = processor.process_payment(amount)
    print(f"订单处理结果: {result}")

def demonstrate_payment_polymorphism():
    """演示支付系统中的多态应用"""
    print("\n=== 支付系统多态应用 ===")
    
    # 不同的支付方式
    processors = [
        CreditCardProcessor(),
        AlipayProcessor(),
        WechatPayProcessor()
    ]
    
    amount = 100
    for processor in processors:
        process_order(processor, amount)

if __name__ == "__main__":
    # 演示多态的基本概念
    demonstrate_polymorphism()
    
    # 演示形状计算中的多态
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Triangle(3, 4, 5),
        Rectangle(2, 8)
    ]
    calculate_shapes_info(shapes)
    
    # 演示类型检查
    demonstrate_type_checking()
    
    # 演示支付系统中的多态
    demonstrate_payment_polymorphism()
    
    print("\n=== 多态的核心要点 ===")
    print("1. 同一接口，不同实现")
    print("2. 运行时动态绑定")
    print("3. 提高代码灵活性和可扩展性")
    print("4. 降低代码耦合度")
    print("5. 支持开闭原则（对扩展开放，对修改封闭）")