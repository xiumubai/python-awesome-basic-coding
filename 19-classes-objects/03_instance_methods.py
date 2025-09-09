#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实例方法的定义和使用

本模块介绍Python中实例方法的定义、调用和各种用法。
实例方法是属于对象的函数，可以访问和修改对象的状态。

学习目标：
1. 理解实例方法的概念和作用
2. 掌握实例方法的定义语法
3. 学会使用self参数
4. 了解方法的不同类型和用法
"""

# 1. 基本实例方法定义
print("=== 1. 基本实例方法定义 ===")

class Person:
    """人类 - 演示基本实例方法"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        """自我介绍方法"""
        return f"大家好，我是{self.name}，今年{self.age}岁"
    
    def have_birthday(self):
        """过生日方法 - 修改对象状态"""
        self.age += 1
        return f"{self.name}过生日了！现在{self.age}岁"
    
    def get_age_group(self):
        """获取年龄组"""
        if self.age < 18:
            return "未成年"
        elif self.age < 60:
            return "成年人"
        else:
            return "老年人"

# 创建对象并调用方法
person = Person("小明", 16)
print(f"介绍: {person.introduce()}")
print(f"年龄组: {person.get_age_group()}")
print(f"过生日: {person.have_birthday()}")
print(f"过生日后年龄组: {person.get_age_group()}")
print()

# 2. 带参数的实例方法
print("=== 2. 带参数的实例方法 ===")

class Calculator:
    """计算器类 - 演示带参数的实例方法"""
    
    def __init__(self):
        self.history = []  # 计算历史
        self.result = 0
    
    def add(self, a, b=None):
        """加法运算"""
        if b is None:
            # 单参数：与当前结果相加
            self.result += a
            operation = f"{self.result - a} + {a} = {self.result}"
        else:
            # 双参数：两数相加
            self.result = a + b
            operation = f"{a} + {b} = {self.result}"
        
        self.history.append(operation)
        return self.result
    
    def multiply(self, *numbers):
        """乘法运算 - 可变参数"""
        if not numbers:
            return self.result
        
        result = 1
        for num in numbers:
            result *= num
        
        self.result = result
        operation = f"{' × '.join(map(str, numbers))} = {result}"
        self.history.append(operation)
        return self.result
    
    def calculate(self, expression, **kwargs):
        """通用计算方法 - 关键字参数"""
        precision = kwargs.get('precision', 2)
        show_steps = kwargs.get('show_steps', False)
        
        try:
            result = eval(expression)
            self.result = round(result, precision)
            
            operation = f"{expression} = {self.result}"
            if show_steps:
                operation += f" (精度: {precision}位)"
            
            self.history.append(operation)
            return self.result
        except Exception as e:
            return f"计算错误: {e}"
    
    def get_history(self):
        """获取计算历史"""
        return self.history.copy()
    
    def clear(self):
        """清空历史和结果"""
        self.history.clear()
        self.result = 0

# 使用计算器
calc = Calculator()
print(f"加法 5 + 3: {calc.add(5, 3)}")
print(f"累加 10: {calc.add(10)}")
print(f"乘法 2 × 3 × 4: {calc.multiply(2, 3, 4)}")
print(f"表达式计算: {calc.calculate('10 / 3', precision=3, show_steps=True)}")
print(f"计算历史: {calc.get_history()}")
print()

# 3. 方法的链式调用
print("=== 3. 方法的链式调用 ===")

class StringBuilder:
    """字符串构建器 - 演示链式调用"""
    
    def __init__(self, initial=""):
        self.content = initial
    
    def append(self, text):
        """追加文本"""
        self.content += str(text)
        return self  # 返回自身以支持链式调用
    
    def prepend(self, text):
        """前置文本"""
        self.content = str(text) + self.content
        return self
    
    def upper(self):
        """转为大写"""
        self.content = self.content.upper()
        return self
    
    def lower(self):
        """转为小写"""
        self.content = self.content.lower()
        return self
    
    def reverse(self):
        """反转字符串"""
        self.content = self.content[::-1]
        return self
    
    def replace(self, old, new):
        """替换文本"""
        self.content = self.content.replace(old, new)
        return self
    
    def build(self):
        """构建最终字符串"""
        return self.content
    
    def __str__(self):
        return self.content

# 链式调用示例
builder = StringBuilder("Hello")
result = (builder
          .append(" World")
          .append("!")
          .upper()
          .replace("WORLD", "Python")
          .build())

print(f"链式调用结果: {result}")

# 另一个链式调用
builder2 = StringBuilder()
result2 = (builder2
           .append("Python")
           .prepend("学习 ")
           .append(" 编程")
           .build())

print(f"另一个链式调用: {result2}")
print()

# 4. 私有方法和公有方法
print("=== 4. 私有方法和公有方法 ===")

class BankAccount:
    """银行账户 - 演示私有方法和公有方法"""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self._balance = initial_balance  # 受保护的属性
        self.__transaction_count = 0     # 私有属性
    
    def deposit(self, amount):
        """公有方法：存款"""
        if self._validate_amount(amount):
            self._balance += amount
            self.__record_transaction("存款", amount)
            return True
        return False
    
    def withdraw(self, amount):
        """公有方法：取款"""
        if self._validate_amount(amount) and self._check_balance(amount):
            self._balance -= amount
            self.__record_transaction("取款", amount)
            return True
        return False
    
    def get_balance(self):
        """公有方法：获取余额"""
        return self._balance
    
    def get_transaction_count(self):
        """公有方法：获取交易次数"""
        return self.__transaction_count
    
    def _validate_amount(self, amount):
        """受保护方法：验证金额"""
        return isinstance(amount, (int, float)) and amount > 0
    
    def _check_balance(self, amount):
        """受保护方法：检查余额"""
        return self._balance >= amount
    
    def __record_transaction(self, transaction_type, amount):
        """私有方法：记录交易"""
        self.__transaction_count += 1
        print(f"交易记录: {transaction_type} {amount}元，交易次数: {self.__transaction_count}")

# 使用银行账户
account = BankAccount("123456", 1000)
print(f"初始余额: {account.get_balance()}")
print(f"存款500: {account.deposit(500)}")
print(f"取款200: {account.withdraw(200)}")
print(f"尝试取款2000: {account.withdraw(2000)}")
print(f"最终余额: {account.get_balance()}")
print(f"交易次数: {account.get_transaction_count()}")
print()

# 5. 特殊方法（魔术方法）
print("=== 5. 特殊方法（魔术方法） ===")

class Vector:
    """向量类 - 演示特殊方法"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """字符串表示"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """开发者表示"""
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """加法运算"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """减法运算"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """标量乘法"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __eq__(self, other):
        """相等比较"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __len__(self):
        """向量长度"""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    
    def __bool__(self):
        """布尔值"""
        return self.x != 0 or self.y != 0
    
    def magnitude(self):
        """计算向量模长"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def normalize(self):
        """归一化向量"""
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0)
        return Vector(self.x / mag, self.y / mag)

# 使用向量类
v1 = Vector(3, 4)
v2 = Vector(1, 2)
zero_vector = Vector(0, 0)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"len(v1): {len(v1)}")
print(f"bool(v1): {bool(v1)}")
print(f"bool(zero_vector): {bool(zero_vector)}")
print(f"v1模长: {v1.magnitude():.2f}")
print(f"v1归一化: {v1.normalize()}")
print()

# 6. 类方法和静态方法
print("=== 6. 类方法和静态方法 ===")

class Employee:
    """员工类 - 演示类方法和静态方法"""
    
    company = "Python科技公司"
    employee_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    def work(self):
        """实例方法：工作"""
        return f"{self.name}正在工作"
    
    def get_annual_salary(self):
        """实例方法：获取年薪"""
        return self.salary * 12
    
    @classmethod
    def get_company_info(cls):
        """类方法：获取公司信息"""
        return f"公司: {cls.company}, 员工数: {cls.employee_count}"
    
    @classmethod
    def create_intern(cls, name):
        """类方法：创建实习生"""
        return cls(name, 3000)  # 实习生固定工资
    
    @staticmethod
    def is_workday(day):
        """静态方法：判断是否工作日"""
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        return day in weekdays
    
    @staticmethod
    def calculate_tax(salary):
        """静态方法：计算税收"""
        if salary <= 5000:
            return 0
        elif salary <= 8000:
            return (salary - 5000) * 0.03
        else:
            return 3000 * 0.03 + (salary - 8000) * 0.1
    
    def __str__(self):
        return f"Employee({self.name}, {self.salary})"

# 使用员工类
emp1 = Employee("张三", 8000)
emp2 = Employee("李四", 12000)
intern = Employee.create_intern("王五")  # 使用类方法创建

print(f"员工1: {emp1}")
print(f"员工2: {emp2}")
print(f"实习生: {intern}")
print(f"公司信息: {Employee.get_company_info()}")
print(f"张三年薪: {emp1.get_annual_salary()}")
print(f"Monday是工作日: {Employee.is_workday('Monday')}")
print(f"Sunday是工作日: {Employee.is_workday('Sunday')}")
print(f"张三税收: {Employee.calculate_tax(emp1.salary):.2f}")
print(f"李四税收: {Employee.calculate_tax(emp2.salary):.2f}")
print()

# 7. 方法重载和多态
print("=== 7. 方法重载和多态 ===")

class Shape:
    """形状基类"""
    
    def area(self):
        """计算面积 - 基类方法"""
        raise NotImplementedError("子类必须实现area方法")
    
    def perimeter(self):
        """计算周长 - 基类方法"""
        raise NotImplementedError("子类必须实现perimeter方法")
    
    def describe(self):
        """描述形状"""
        return f"这是一个{self.__class__.__name__}"

class Circle(Shape):
    """圆形类"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """重写面积计算"""
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        """重写周长计算"""
        return 2 * 3.14159 * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius})"

class Rectangle(Shape):
    """矩形类"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """重写面积计算"""
        return self.width * self.height
    
    def perimeter(self):
        """重写周长计算"""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

def print_shape_info(shape):
    """多态函数 - 处理任何形状对象"""
    print(f"形状: {shape}")
    print(f"描述: {shape.describe()}")
    print(f"面积: {shape.area():.2f}")
    print(f"周长: {shape.perimeter():.2f}")
    print()

# 多态示例
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3)
]

for shape in shapes:
    print_shape_info(shape)

# 8. 学习要点总结
print("=== 学习要点总结 ===")
print("""
实例方法的关键要点：
1. 实例方法第一个参数必须是self
2. 实例方法可以访问和修改对象状态
3. 方法可以有参数、默认参数、可变参数
4. 支持链式调用（返回self）
5. 私有方法以__开头，受保护方法以_开头
6. 特殊方法实现操作符重载
7. 类方法用@classmethod装饰，静态方法用@staticmethod装饰
8. 方法重写实现多态性
""")

if __name__ == "__main__":
    print("\n=== 程序执行完成 ===")
    print("恭喜！你已经学会了Python实例方法的定义和使用。")
    print("下一步：学习实例属性的操作和管理。")