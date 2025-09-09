#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
对象的创建和实例化

本模块介绍如何从类创建对象（实例化），以及对象的基本操作。
对象是类的具体实现，每个对象都有自己的属性值。

学习目标：
1. 理解对象和实例的概念
2. 掌握对象的创建语法
3. 学会访问对象的属性和方法
4. 了解对象的生命周期
"""

# 1. 基本对象创建
print("=== 1. 基本对象创建 ===")

class Person:
    """人类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"我是{self.name}，今年{self.age}岁"

# 创建对象（实例化）
person1 = Person("张三", 25)
person2 = Person("李四", 30)

print(f"person1: {person1}")
print(f"person2: {person2}")
print(f"person1的类型: {type(person1)}")
print(f"person1是Person的实例: {isinstance(person1, Person)}")
print(f"person1的介绍: {person1.introduce()}")
print(f"person2的介绍: {person2.introduce()}")
print()

# 2. 对象的唯一性
print("=== 2. 对象的唯一性 ===")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# 创建多个对象
car1 = Car("丰田", "卡罗拉")
car2 = Car("丰田", "卡罗拉")
car3 = car1  # 引用同一个对象

print(f"car1的ID: {id(car1)}")
print(f"car2的ID: {id(car2)}")
print(f"car3的ID: {id(car3)}")
print(f"car1 is car2: {car1 is car2}")
print(f"car1 is car3: {car1 is car3}")
print(f"car1 == car2: {car1 == car2}")
print()

# 3. 访问对象属性
print("=== 3. 访问对象属性 ===")

class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.courses = []  # 空列表

student = Student("王五", "2023001", "高三")

# 访问属性
print(f"学生姓名: {student.name}")
print(f"学号: {student.student_id}")
print(f"年级: {student.grade}")
print(f"课程列表: {student.courses}")

# 修改属性
student.name = "王小五"
student.courses.append("数学")
student.courses.append("物理")

print(f"修改后的姓名: {student.name}")
print(f"修改后的课程: {student.courses}")
print()

# 4. 动态添加属性
print("=== 4. 动态添加属性 ===")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("Python编程", "张作者")
print(f"初始属性: title={book.title}, author={book.author}")

# 动态添加属性
book.price = 59.9
book.publisher = "编程出版社"
book.pages = 300

print(f"添加属性后: price={book.price}, publisher={book.publisher}, pages={book.pages}")

# 检查属性是否存在
print(f"book有price属性: {hasattr(book, 'price')}")
print(f"book有isbn属性: {hasattr(book, 'isbn')}")
print()

# 5. 使用getattr和setattr
print("=== 5. 使用getattr和setattr ===")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("笔记本电脑", 5999)

# 使用getattr获取属性
name = getattr(product, 'name', '未知')
price = getattr(product, 'price', 0)
brand = getattr(product, 'brand', '未知品牌')  # 不存在的属性，返回默认值

print(f"产品名称: {name}")
print(f"产品价格: {price}")
print(f"产品品牌: {brand}")

# 使用setattr设置属性
setattr(product, 'brand', '联想')
setattr(product, 'warranty', '2年')

print(f"设置后的品牌: {product.brand}")
print(f"设置后的保修: {product.warranty}")
print()

# 6. 对象的方法调用
print("=== 6. 对象的方法调用 ===")

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        self.result += value
        return self
    
    def subtract(self, value):
        self.result -= value
        return self
    
    def multiply(self, value):
        self.result *= value
        return self
    
    def get_result(self):
        return self.result
    
    def reset(self):
        self.result = 0
        return self

# 创建计算器对象
calc = Calculator()

# 方法调用
print(f"初始结果: {calc.get_result()}")
calc.add(10)
print(f"加10后: {calc.get_result()}")
calc.multiply(2)
print(f"乘2后: {calc.get_result()}")
calc.subtract(5)
print(f"减5后: {calc.get_result()}")

# 链式调用
result = calc.reset().add(100).multiply(2).subtract(50).get_result()
print(f"链式调用结果: {result}")
print()

# 7. 对象的字符串表示
print("=== 7. 对象的字符串表示 ===")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """用户友好的字符串表示"""
        return f"点({self.x}, {self.y})"
    
    def __repr__(self):
        """开发者友好的字符串表示"""
        return f"Point({self.x}, {self.y})"

point = Point(3, 4)
print(f"str(point): {str(point)}")
print(f"repr(point): {repr(point)}")
print(f"直接打印: {point}")
print()

# 8. 对象的比较
print("=== 8. 对象的比较 ===")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __eq__(self, other):
        """相等比较"""
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False
    
    def __lt__(self, other):
        """小于比较（按面积）"""
        if isinstance(other, Rectangle):
            return self.width * self.height < other.width * other.height
        return NotImplemented
    
    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

rect1 = Rectangle(3, 4)
rect2 = Rectangle(3, 4)
rect3 = Rectangle(5, 6)

print(f"rect1: {rect1}, 面积: {rect1.area()}")
print(f"rect2: {rect2}, 面积: {rect2.area()}")
print(f"rect3: {rect3}, 面积: {rect3.area()}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 is rect2: {rect1 is rect2}")
print(f"rect1 < rect3: {rect1 < rect3}")
print()

# 9. 对象的生命周期
print("=== 9. 对象的生命周期 ===")

class LifeCycleDemo:
    count = 0
    
    def __init__(self, name):
        self.name = name
        LifeCycleDemo.count += 1
        print(f"对象 {self.name} 被创建，当前对象数量: {LifeCycleDemo.count}")
    
    def __del__(self):
        LifeCycleDemo.count -= 1
        print(f"对象 {self.name} 被销毁，剩余对象数量: {LifeCycleDemo.count}")

print("创建对象:")
obj1 = LifeCycleDemo("对象1")
obj2 = LifeCycleDemo("对象2")

print(f"\n当前对象数量: {LifeCycleDemo.count}")

print("\n删除对象:")
del obj1
print(f"删除obj1后，对象数量: {LifeCycleDemo.count}")

# obj2会在程序结束时自动销毁
print()

# 10. 实际应用示例
print("=== 10. 实际应用示例 ===")

class BankAccount:
    """银行账户类"""
    
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"存款: +{amount}")
            return True
        return False
    
    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"取款: -{amount}")
            return True
        return False
    
    def get_balance(self):
        """获取余额"""
        return self.balance
    
    def get_statement(self):
        """获取账单"""
        return self.transaction_history.copy()
    
    def __str__(self):
        return f"账户({self.account_number}) - 户主: {self.owner}, 余额: {self.balance}"

# 创建银行账户
account = BankAccount("123456789", "张三", 1000)
print(f"账户信息: {account}")

# 进行交易
print(f"\n存款500: {account.deposit(500)}")
print(f"当前余额: {account.get_balance()}")

print(f"取款200: {account.withdraw(200)}")
print(f"当前余额: {account.get_balance()}")

print(f"尝试取款2000: {account.withdraw(2000)}")
print(f"当前余额: {account.get_balance()}")

print(f"\n交易历史: {account.get_statement()}")
print()

# 11. 学习要点总结
print("=== 学习要点总结 ===")
print("""
对象创建和使用的关键要点：
1. 使用类名()创建对象实例
2. 每个对象都有唯一的身份标识
3. 对象可以有自己的属性和方法
4. 可以动态添加和修改对象属性
5. 使用getattr/setattr安全访问属性
6. 对象支持各种操作符重载
7. 对象有生命周期（创建到销毁）
8. 对象是类的具体实现
""")

if __name__ == "__main__":
    print("\n=== 程序执行完成 ===")
    print("恭喜！你已经学会了Python对象的创建和基本操作。")
    print("下一步：学习实例方法的定义和使用。")