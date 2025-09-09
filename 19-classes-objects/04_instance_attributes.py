#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实例属性的操作

本文件演示Python中实例属性的各种操作：
1. 实例属性的基本概念
2. 属性的创建和初始化
3. 属性的访问和修改
4. 动态添加和删除属性
5. 属性的类型和验证
6. 使用property装饰器
7. 属性的描述符
8. 实际应用示例

作者: Python学习助手
日期: 2024
"""

print("=== Python实例属性操作学习 ===")
print()

# 1. 实例属性的基本概念
print("=== 1. 实例属性的基本概念 ===")

class Person:
    """人员类 - 演示实例属性基本概念"""
    
    def __init__(self, name, age):
        # 在构造方法中定义实例属性
        self.name = name        # 公有属性
        self.age = age          # 公有属性
        self._email = ""        # 受保护属性（约定）
        self.__id = None        # 私有属性
    
    def show_info(self):
        """显示个人信息"""
        print(f"姓名: {self.name}, 年龄: {self.age}")

# 创建对象并访问属性
person1 = Person("张三", 25)
print(f"姓名: {person1.name}")
print(f"年龄: {person1.age}")
person1.show_info()
print()

# 2. 属性的创建和初始化
print("=== 2. 属性的创建和初始化 ===")

class Student:
    """学生类 - 演示属性的不同初始化方式"""
    
    def __init__(self, name, student_id, grade=None):
        # 必需属性
        self.name = name
        self.student_id = student_id
        
        # 可选属性（有默认值）
        self.grade = grade if grade is not None else "未分配"
        
        # 初始化为空的属性
        self.courses = []           # 课程列表
        self.scores = {}            # 成绩字典
        
        # 计算属性（基于其他属性）
        self.display_name = f"学生-{self.name}"
        
        # 状态属性
        self.is_active = True
        self.enrollment_date = None

student1 = Student("李四", "S001", "高三")
print(f"学生信息: {student1.display_name}")
print(f"学号: {student1.student_id}")
print(f"年级: {student1.grade}")
print(f"课程: {student1.courses}")
print(f"状态: {'活跃' if student1.is_active else '非活跃'}")
print()

# 3. 属性的访问和修改
print("=== 3. 属性的访问和修改 ===")

# 直接访问和修改
student1.name = "李四（修改后）"
student1.grade = "大一"
print(f"修改后姓名: {student1.name}")
print(f"修改后年级: {student1.grade}")

# 修改复合属性
student1.courses.append("数学")
student1.courses.append("物理")
student1.scores["数学"] = 95
student1.scores["物理"] = 88
print(f"课程列表: {student1.courses}")
print(f"成绩记录: {student1.scores}")
print()

# 4. 动态添加和删除属性
print("=== 4. 动态添加和删除属性 ===")

class DynamicObject:
    """动态对象类 - 演示动态属性操作"""
    
    def __init__(self, name):
        self.name = name

# 创建对象
obj = DynamicObject("测试对象")
print(f"初始属性: {obj.__dict__}")

# 动态添加属性
obj.color = "红色"
obj.size = "大"
obj.price = 99.99
print(f"添加属性后: {obj.__dict__}")

# 使用setattr动态添加属性
setattr(obj, "weight", "1.5kg")
setattr(obj, "brand", "Python牌")
print(f"使用setattr后: {obj.__dict__}")

# 检查属性是否存在
print(f"是否有color属性: {hasattr(obj, 'color')}")
print(f"是否有height属性: {hasattr(obj, 'height')}")

# 获取属性值（安全方式）
color = getattr(obj, 'color', '未知')
height = getattr(obj, 'height', '未设置')
print(f"颜色: {color}")
print(f"高度: {height}")

# 删除属性
if hasattr(obj, 'price'):
    delattr(obj, 'price')
    print("已删除price属性")

print(f"删除属性后: {obj.__dict__}")
print()

# 5. 属性的类型和验证
print("=== 5. 属性的类型和验证 ===")

class ValidatedPerson:
    """带验证的人员类"""
    
    def __init__(self, name, age, email):
        self.set_name(name)
        self.set_age(age)
        self.set_email(email)
    
    def set_name(self, name):
        """设置姓名（带验证）"""
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("姓名必须是非空字符串")
        self._name = name.strip()
    
    def get_name(self):
        """获取姓名"""
        return self._name
    
    def set_age(self, age):
        """设置年龄（带验证）"""
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError("年龄必须是0-150之间的整数")
        self._age = age
    
    def get_age(self):
        """获取年龄"""
        return self._age
    
    def set_email(self, email):
        """设置邮箱（带验证）"""
        if not isinstance(email, str) or '@' not in email:
            raise ValueError("邮箱格式不正确")
        self._email = email
    
    def get_email(self):
        """获取邮箱"""
        return self._email
    
    def __str__(self):
        return f"ValidatedPerson(姓名={self._name}, 年龄={self._age}, 邮箱={self._email})"

# 创建验证对象
try:
    person = ValidatedPerson("王五", 30, "wangwu@example.com")
    print(f"创建成功: {person}")
    
    # 修改属性
    person.set_age(31)
    print(f"修改年龄后: 年龄={person.get_age()}")
    
    # 尝试设置无效值
    try:
        person.set_age(-5)
    except ValueError as e:
        print(f"年龄验证错误: {e}")
        
except ValueError as e:
    print(f"创建对象失败: {e}")

print()

# 6. 使用property装饰器
print("=== 6. 使用property装饰器 ===")

class Temperature:
    """温度类 - 演示property装饰器"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """摄氏度属性（只读）"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """设置摄氏度"""
        if not isinstance(value, (int, float)):
            raise TypeError("温度必须是数字")
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度(-273.15°C)")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """华氏度属性（计算属性）"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """通过华氏度设置温度"""
        if not isinstance(value, (int, float)):
            raise TypeError("温度必须是数字")
        celsius = (value - 32) * 5/9
        if celsius < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = celsius
    
    @property
    def kelvin(self):
        """开尔文温度（只读计算属性）"""
        return self._celsius + 273.15
    
    def __str__(self):
        return f"Temperature({self.celsius:.1f}°C, {self.fahrenheit:.1f}°F, {self.kelvin:.1f}K)"

# 使用property
temp = Temperature(25)
print(f"初始温度: {temp}")

# 通过摄氏度设置
temp.celsius = 100
print(f"设置100°C: {temp}")

# 通过华氏度设置
temp.fahrenheit = 32
print(f"设置32°F: {temp}")

# 尝试设置无效值
try:
    temp.celsius = -300
except ValueError as e:
    print(f"温度设置错误: {e}")

print()

# 7. 属性的描述符
print("=== 7. 属性的描述符 ===")

class PositiveNumber:
    """正数描述符"""
    
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)
    
    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name}必须是数字")
        if value <= 0:
            raise ValueError(f"{self.name}必须是正数")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        if self.name in obj.__dict__:
            del obj.__dict__[self.name]

class Product:
    """产品类 - 使用描述符"""
    
    price = PositiveNumber('price')
    quantity = PositiveNumber('quantity')
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price      # 使用描述符
        self.quantity = quantity # 使用描述符
    
    @property
    def total_value(self):
        """总价值（计算属性）"""
        return self.price * self.quantity
    
    def __str__(self):
        return f"Product({self.name}, 价格={self.price}, 数量={self.quantity}, 总值={self.total_value})"

# 使用描述符
product = Product("笔记本电脑", 5999.99, 10)
print(f"产品信息: {product}")

# 修改属性
product.price = 5499.99
product.quantity = 15
print(f"修改后: {product}")

# 尝试设置无效值
try:
    product.price = -100
except ValueError as e:
    print(f"价格设置错误: {e}")

try:
    product.quantity = 0
except ValueError as e:
    print(f"数量设置错误: {e}")

print()

# 8. 实际应用示例
print("=== 8. 实际应用示例 ===")

class BankAccount:
    """银行账户类 - 综合应用示例"""
    
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self._balance = initial_balance
        self._transaction_history = []
        self._is_frozen = False
        
        # 记录初始存款
        if initial_balance > 0:
            self._transaction_history.append(f"初始存款: +{initial_balance}")
    
    @property
    def balance(self):
        """余额（只读）"""
        return self._balance
    
    @property
    def is_frozen(self):
        """账户是否冻结"""
        return self._is_frozen
    
    @property
    def transaction_count(self):
        """交易次数"""
        return len(self._transaction_history)
    
    def deposit(self, amount):
        """存款"""
        if self._is_frozen:
            print("账户已冻结，无法进行交易")
            return False
            
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("存款金额必须是正数")
            return False
        
        self._balance += amount
        self._transaction_history.append(f"存款: +{amount}")
        print(f"存款成功，当前余额: {self._balance}")
        return True
    
    def withdraw(self, amount):
        """取款"""
        if self._is_frozen:
            print("账户已冻结，无法进行交易")
            return False
            
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("取款金额必须是正数")
            return False
            
        if amount > self._balance:
            print("余额不足")
            return False
        
        self._balance -= amount
        self._transaction_history.append(f"取款: -{amount}")
        print(f"取款成功，当前余额: {self._balance}")
        return True
    
    def freeze_account(self):
        """冻结账户"""
        self._is_frozen = True
        self._transaction_history.append("账户冻结")
        print("账户已冻结")
    
    def unfreeze_account(self):
        """解冻账户"""
        self._is_frozen = False
        self._transaction_history.append("账户解冻")
        print("账户已解冻")
    
    def get_transaction_history(self, limit=None):
        """获取交易历史"""
        if limit is None:
            return self._transaction_history.copy()
        return self._transaction_history[-limit:]
    
    def __str__(self):
        status = "冻结" if self._is_frozen else "正常"
        return f"BankAccount(账号={self.account_number}, 户主={self.owner_name}, 余额={self._balance}, 状态={status})"

# 创建银行账户
account = BankAccount("6222001234567890", "张三", 1000)
print(f"账户信息: {account}")
print(f"初始余额: {account.balance}")
print(f"交易次数: {account.transaction_count}")

# 进行交易
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # 余额不足

# 查看交易历史
print("\n交易历史:")
for i, transaction in enumerate(account.get_transaction_history(), 1):
    print(f"{i}. {transaction}")

# 冻结和解冻账户
print("\n冻结账户测试:")
account.freeze_account()
account.deposit(100)  # 应该失败

account.unfreeze_account()
account.deposit(100)  # 应该成功

print(f"\n最终账户信息: {account}")
print(f"最终余额: {account.balance}")
print(f"总交易次数: {account.transaction_count}")

print()
print("=== 学习要点总结 ===")
print()
print("实例属性操作的关键要点：")
print("1. 实例属性属于具体对象，每个对象都有自己的属性副本")
print("2. 可以在__init__方法中初始化属性")
print("3. 支持动态添加、修改和删除属性")
print("4. 使用hasattr()、getattr()、setattr()、delattr()进行属性操作")
print("5. 可以通过方法实现属性验证和控制")
print("6. @property装饰器提供优雅的属性访问控制")
print("7. 描述符提供更高级的属性控制机制")
print("8. 合理使用私有属性和公有属性")
print()
print("=== 程序执行完成 ===")
print("恭喜！你已经学会了Python实例属性的操作。")
print("下一步：学习构造方法__init__的详细用法。")