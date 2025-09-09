#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
类的定义基础

本模块介绍Python中类的基本定义语法和概念。
类是面向对象编程的核心概念，它是创建对象的模板。

学习目标：
1. 理解类的概念和作用
2. 掌握类的基本定义语法
3. 了解类的命名规范
4. 学会创建简单的类
"""

# 1. 最简单的类定义
print("=== 1. 最简单的类定义 ===")

class Person:
    """人类 - 最简单的类定义"""
    pass  # pass关键字表示空的代码块

print(f"Person类已定义: {Person}")
print(f"Person类的类型: {type(Person)}")
print(f"Person类的文档字符串: {Person.__doc__}")
print()

# 2. 带有属性的类定义
print("=== 2. 带有属性的类定义 ===")

class Student:
    """学生类 - 包含类属性"""
    # 类属性 - 所有实例共享
    school = "Python编程学院"
    student_count = 0
    
    def display_info(self):
        """显示学生信息的方法"""
        print(f"学校: {self.school}")
        print(f"学生总数: {self.student_count}")

print(f"Student类已定义: {Student}")
print(f"Student.school: {Student.school}")
print(f"Student.student_count: {Student.student_count}")
print()

# 3. 类的命名规范
print("=== 3. 类的命名规范 ===")

# 正确的类命名（使用PascalCase/驼峰命名法）
class BankAccount:
    """银行账户类 - 正确的命名示例"""
    pass

class CarEngine:
    """汽车引擎类 - 正确的命名示例"""
    pass

class HTTPServer:
    """HTTP服务器类 - 缩写词保持大写"""
    pass

print("正确的类命名示例:")
print(f"- BankAccount: {BankAccount}")
print(f"- CarEngine: {CarEngine}")
print(f"- HTTPServer: {HTTPServer}")
print()

# 4. 类的基本结构
print("=== 4. 类的基本结构 ===")

class Animal:
    """动物类 - 展示类的基本结构"""
    
    # 类属性
    kingdom = "动物界"
    
    def __init__(self, name, species):
        """构造方法 - 初始化实例"""
        self.name = name      # 实例属性
        self.species = species # 实例属性
    
    def make_sound(self):
        """实例方法 - 发出声音"""
        return f"{self.name}发出了声音"
    
    def get_info(self):
        """实例方法 - 获取信息"""
        return f"名字: {self.name}, 种类: {self.species}, 界: {self.kingdom}"
    
    @classmethod
    def get_kingdom(cls):
        """类方法 - 获取动物界信息"""
        return cls.kingdom
    
    @staticmethod
    def is_living():
        """静态方法 - 判断是否为生物"""
        return True

print("Animal类的结构:")
print(f"- 类属性 kingdom: {Animal.kingdom}")
print(f"- 类方法 get_kingdom(): {Animal.get_kingdom()}")
print(f"- 静态方法 is_living(): {Animal.is_living()}")
print()

# 5. 类的内省（反射）
print("=== 5. 类的内省（反射） ===")

class Book:
    """书籍类 - 用于演示类的内省"""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def read(self):
        return f"正在阅读《{self.title}》"

print("Book类的内省信息:")
print(f"- 类名: {Book.__name__}")
print(f"- 模块: {Book.__module__}")
print(f"- 文档字符串: {Book.__doc__}")
print(f"- 基类: {Book.__bases__}")
print(f"- 字典: {list(Book.__dict__.keys())}")
print()

# 6. 类的比较和身份
print("=== 6. 类的比较和身份 ===")

class Car:
    pass

class Bicycle:
    pass

# 另一个Car类定义
class Car2:
    pass

print("类的比较:")
print(f"Car is Car: {Car is Car}")
print(f"Car is Bicycle: {Car is Bicycle}")
print(f"Car is Car2: {Car is Car2}")
print(f"Car == Car: {Car == Car}")
print(f"Car == Bicycle: {Car == Bicycle}")
print()

# 7. 实际应用示例
print("=== 7. 实际应用示例 ===")

class Rectangle:
    """矩形类 - 实际应用示例"""
    
    def __init__(self, width, height):
        """初始化矩形"""
        self.width = width
        self.height = height
    
    def area(self):
        """计算面积"""
        return self.width * self.height
    
    def perimeter(self):
        """计算周长"""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """字符串表示"""
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def __repr__(self):
        """开发者表示"""
        return f"Rectangle({self.width}, {self.height})"

# 创建矩形实例
rect = Rectangle(5, 3)
print(f"矩形: {rect}")
print(f"面积: {rect.area()}")
print(f"周长: {rect.perimeter()}")
print()

# 8. 学习要点总结
print("=== 学习要点总结 ===")
print("""
类定义的关键要点：
1. 使用 class 关键字定义类
2. 类名使用 PascalCase 命名规范
3. 类可以包含属性和方法
4. pass 关键字用于创建空类
5. 类是对象的模板和蓝图
6. 类本身也是对象（类对象）
7. 可以通过内省获取类的信息
8. 类定义后就可以创建实例
""")

if __name__ == "__main__":
    print("\n=== 程序执行完成 ===")
    print("恭喜！你已经学会了Python类的基本定义。")
    print("下一步：学习如何创建和使用类的实例（对象）。")