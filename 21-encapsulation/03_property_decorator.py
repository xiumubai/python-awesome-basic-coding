#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
属性装饰器：@property

@property装饰器是Python中实现属性访问控制的重要工具。它允许我们：
1. 将方法调用伪装成属性访问
2. 在获取和设置属性时添加逻辑控制
3. 实现只读、只写或读写属性
4. 在属性访问时进行数据验证和转换

@property装饰器的三种用法：
- @property：定义getter方法
- @属性名.setter：定义setter方法
- @属性名.deleter：定义deleter方法
"""

import math
from datetime import datetime, date

# 示例1：基本的@property使用
class Circle:
    """圆形类 - 演示@property的基本用法"""
    
    def __init__(self, radius):
        self._radius = radius  # 使用保护属性存储实际值
    
    @property
    def radius(self):
        """半径属性的getter"""
        print("获取半径")
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """半径属性的setter"""
        print(f"设置半径为: {value}")
        if value <= 0:
            raise ValueError("半径必须大于0")
        self._radius = value
    
    @radius.deleter
    def radius(self):
        """半径属性的deleter"""
        print("删除半径属性")
        self._radius = 0
    
    @property
    def diameter(self):
        """直径属性（只读）"""
        return self._radius * 2
    
    @property
    def area(self):
        """面积属性（只读）"""
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self):
        """周长属性（只读）"""
        return 2 * math.pi * self._radius
    
    def __str__(self):
        return f"Circle(radius={self._radius})"


# 示例2：复杂的属性验证
class Person:
    """人员类 - 演示复杂的属性验证"""
    
    def __init__(self, name, age, email):
        self._name = None
        self._age = None
        self._email = None
        self._birth_year = None
        
        # 通过属性设置器来设置初始值，确保验证
        self.name = name
        self.age = age
        self.email = email
    
    @property
    def name(self):
        """姓名属性"""
        return self._name
    
    @name.setter
    def name(self, value):
        """姓名设置器 - 验证姓名格式"""
        if not isinstance(value, str):
            raise TypeError("姓名必须是字符串")
        
        if not value.strip():
            raise ValueError("姓名不能为空")
        
        if len(value.strip()) < 2:
            raise ValueError("姓名至少需要2个字符")
        
        # 移除多余空格并首字母大写
        self._name = value.strip().title()
    
    @property
    def age(self):
        """年龄属性"""
        return self._age
    
    @age.setter
    def age(self, value):
        """年龄设置器 - 验证年龄范围"""
        if not isinstance(value, int):
            raise TypeError("年龄必须是整数")
        
        if value < 0 or value > 150:
            raise ValueError("年龄必须在0-150之间")
        
        self._age = value
        # 自动计算出生年份
        current_year = datetime.now().year
        self._birth_year = current_year - value
    
    @property
    def email(self):
        """邮箱属性"""
        return self._email
    
    @email.setter
    def email(self, value):
        """邮箱设置器 - 验证邮箱格式"""
        if not isinstance(value, str):
            raise TypeError("邮箱必须是字符串")
        
        # 简单的邮箱格式验证
        if '@' not in value or '.' not in value.split('@')[-1]:
            raise ValueError("邮箱格式不正确")
        
        self._email = value.lower().strip()
    
    @property
    def birth_year(self):
        """出生年份属性（只读）"""
        return self._birth_year
    
    @property
    def is_adult(self):
        """是否成年属性（只读）"""
        return self._age >= 18
    
    @property
    def age_category(self):
        """年龄分类属性（只读）"""
        if self._age < 13:
            return "儿童"
        elif self._age < 18:
            return "青少年"
        elif self._age < 60:
            return "成年人"
        else:
            return "老年人"
    
    def __str__(self):
        return f"Person(name='{self._name}', age={self._age}, email='{self._email}')"


# 示例3：温度转换类
class Temperature:
    """温度类 - 演示属性之间的相互转换"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """摄氏度属性"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """摄氏度设置器"""
        if not isinstance(value, (int, float)):
            raise TypeError("温度必须是数字")
        
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度(-273.15°C)")
        
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """华氏度属性（通过摄氏度计算）"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """华氏度设置器（转换为摄氏度存储）"""
        if not isinstance(value, (int, float)):
            raise TypeError("温度必须是数字")
        
        celsius_value = (value - 32) * 5/9
        if celsius_value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        
        self._celsius = celsius_value
    
    @property
    def kelvin(self):
        """开尔文温度属性（通过摄氏度计算）"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """开尔文温度设置器（转换为摄氏度存储）"""
        if not isinstance(value, (int, float)):
            raise TypeError("温度必须是数字")
        
        if value < 0:
            raise ValueError("开尔文温度不能为负数")
        
        self._celsius = value - 273.15
    
    @property
    def description(self):
        """温度描述属性（只读）"""
        if self._celsius < 0:
            return "冰点以下"
        elif self._celsius == 0:
            return "冰点"
        elif self._celsius < 100:
            return "常温"
        elif self._celsius == 100:
            return "沸点"
        else:
            return "沸点以上"
    
    def __str__(self):
        return f"Temperature({self._celsius:.2f}°C, {self.fahrenheit:.2f}°F, {self.kelvin:.2f}K)"


# 示例4：银行账户类（使用@property实现安全访问）
class SecureBankAccount:
    """安全银行账户类 - 使用@property实现访问控制"""
    
    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = account_holder
        self._balance = 0
        self._transaction_history = []
        self._is_frozen = False
        
        # 通过属性设置器设置初始余额
        if initial_balance > 0:
            self.balance = initial_balance
    
    @property
    def account_holder(self):
        """账户持有人（只读）"""
        return self._account_holder
    
    @property
    def balance(self):
        """余额属性"""
        if self._is_frozen:
            raise RuntimeError("账户已冻结，无法查询余额")
        return self._balance
    
    @balance.setter
    def balance(self, value):
        """余额设置器（仅用于内部调整）"""
        if self._is_frozen:
            raise RuntimeError("账户已冻结，无法修改余额")
        
        if not isinstance(value, (int, float)):
            raise TypeError("余额必须是数字")
        
        if value < 0:
            raise ValueError("余额不能为负数")
        
        old_balance = self._balance
        self._balance = value
        
        # 记录余额变化
        self._add_transaction("余额调整", value - old_balance)
    
    @property
    def is_frozen(self):
        """账户冻结状态（只读）"""
        return self._is_frozen
    
    @property
    def transaction_count(self):
        """交易次数（只读）"""
        return len(self._transaction_history)
    
    @property
    def last_transaction(self):
        """最后一次交易（只读）"""
        if self._transaction_history:
            return self._transaction_history[-1].copy()
        return None
    
    @property
    def account_status(self):
        """账户状态描述（只读）"""
        if self._is_frozen:
            return "冻结"
        elif self._balance == 0:
            return "零余额"
        elif self._balance < 100:
            return "低余额"
        else:
            return "正常"
    
    def _add_transaction(self, transaction_type, amount):
        """添加交易记录（私有方法）"""
        self._transaction_history.append({
            'type': transaction_type,
            'amount': amount,
            'balance_after': self._balance,
            'timestamp': datetime.now()
        })
    
    def deposit(self, amount):
        """存款方法"""
        if self._is_frozen:
            raise RuntimeError("账户已冻结，无法存款")
        
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        
        self._balance += amount
        self._add_transaction("存款", amount)
        return self._balance
    
    def withdraw(self, amount):
        """取款方法"""
        if self._is_frozen:
            raise RuntimeError("账户已冻结，无法取款")
        
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        
        if amount > self._balance:
            raise ValueError("余额不足")
        
        self._balance -= amount
        self._add_transaction("取款", -amount)
        return self._balance
    
    def freeze_account(self):
        """冻结账户"""
        self._is_frozen = True
        self._add_transaction("账户冻结", 0)
    
    def unfreeze_account(self):
        """解冻账户"""
        self._is_frozen = False
        self._add_transaction("账户解冻", 0)


def demonstrate_basic_property():
    """演示基本的@property使用"""
    print("=" * 60)
    print("基本@property演示 - 圆形类")
    print("=" * 60)
    
    # 创建圆形对象
    circle = Circle(5)
    
    print("\n1. 属性访问（像普通属性一样）：")
    print(f"半径: {circle.radius}")  # 调用getter
    print(f"直径: {circle.diameter}")  # 只读属性
    print(f"面积: {circle.area:.2f}")
    print(f"周长: {circle.circumference:.2f}")
    
    print("\n2. 属性设置：")
    circle.radius = 10  # 调用setter
    print(f"新半径: {circle.radius}")
    print(f"新面积: {circle.area:.2f}")
    
    print("\n3. 属性验证：")
    try:
        circle.radius = -5  # 触发验证错误
    except ValueError as e:
        print(f"验证错误: {e}")
    
    print("\n4. 只读属性：")
    try:
        circle.area = 100  # 尝试设置只读属性
    except AttributeError as e:
        print(f"只读属性错误: {e}")
    
    print("\n5. 属性删除：")
    del circle.radius  # 调用deleter
    print(f"删除后的半径: {circle.radius}")


def demonstrate_complex_validation():
    """演示复杂的属性验证"""
    print("\n" + "=" * 60)
    print("复杂属性验证演示 - 人员类")
    print("=" * 60)
    
    print("\n1. 正常创建：")
    person = Person("张三", 25, "zhangsan@example.com")
    print(person)
    print(f"出生年份: {person.birth_year}")
    print(f"是否成年: {person.is_adult}")
    print(f"年龄分类: {person.age_category}")
    
    print("\n2. 属性修改：")
    person.name = "  李四  "  # 测试空格处理
    person.age = 17
    print(person)
    print(f"是否成年: {person.is_adult}")
    print(f"年龄分类: {person.age_category}")
    
    print("\n3. 验证错误演示：")
    validation_tests = [
        ("设置空姓名", lambda: setattr(person, 'name', '')),
        ("设置无效年龄", lambda: setattr(person, 'age', -5)),
        ("设置无效邮箱", lambda: setattr(person, 'email', 'invalid-email')),
        ("设置错误类型", lambda: setattr(person, 'age', '25'))
    ]
    
    for test_name, test_func in validation_tests:
        try:
            test_func()
        except (ValueError, TypeError) as e:
            print(f"{test_name}: {e}")


def demonstrate_temperature_conversion():
    """演示温度转换"""
    print("\n" + "=" * 60)
    print("温度转换演示")
    print("=" * 60)
    
    temp = Temperature()
    
    print("\n1. 设置摄氏度：")
    temp.celsius = 25
    print(temp)
    print(f"描述: {temp.description}")
    
    print("\n2. 设置华氏度：")
    temp.fahrenheit = 100
    print(temp)
    print(f"描述: {temp.description}")
    
    print("\n3. 设置开尔文温度：")
    temp.kelvin = 273.15
    print(temp)
    print(f"描述: {temp.description}")
    
    print("\n4. 特殊温度点：")
    special_temps = [
        ("绝对零度", -273.15),
        ("冰点", 0),
        ("室温", 20),
        ("体温", 37),
        ("沸点", 100)
    ]
    
    for name, celsius in special_temps:
        temp.celsius = celsius
        print(f"{name}: {temp}")


def demonstrate_secure_bank_account():
    """演示安全银行账户"""
    print("\n" + "=" * 60)
    print("安全银行账户演示")
    print("=" * 60)
    
    account = SecureBankAccount("王五", 1000)
    
    print("\n1. 账户信息：")
    print(f"账户持有人: {account.account_holder}")
    print(f"余额: {account.balance}")
    print(f"账户状态: {account.account_status}")
    print(f"交易次数: {account.transaction_count}")
    
    print("\n2. 存取款操作：")
    account.deposit(500)
    print(f"存款后余额: {account.balance}")
    
    account.withdraw(200)
    print(f"取款后余额: {account.balance}")
    
    print(f"最后一次交易: {account.last_transaction}")
    
    print("\n3. 账户冻结测试：")
    account.freeze_account()
    print(f"冻结状态: {account.is_frozen}")
    print(f"账户状态: {account.account_status}")
    
    try:
        balance = account.balance  # 尝试查询冻结账户余额
    except RuntimeError as e:
        print(f"冻结账户访问错误: {e}")
    
    account.unfreeze_account()
    print(f"解冻后余额: {account.balance}")
    
    print("\n4. 错误操作演示：")
    try:
        account.withdraw(10000)  # 余额不足
    except ValueError as e:
        print(f"取款错误: {e}")
    
    try:
        account.balance = -100  # 尝试设置负余额
    except ValueError as e:
        print(f"余额设置错误: {e}")


def property_best_practices():
    """@property最佳实践"""
    print("\n" + "=" * 60)
    print("@property最佳实践")
    print("=" * 60)
    
    practices = [
        "1. 使用@property来控制属性访问",
        "2. 在setter中进行数据验证",
        "3. 使用只读属性来暴露计算结果",
        "4. 保持属性访问的简单性，避免复杂计算",
        "5. 使用保护属性(_attribute)存储实际数据",
        "6. 在属性变化时维护数据一致性",
        "7. 提供清晰的错误消息",
        "8. 考虑属性之间的依赖关系",
        "9. 避免在getter中产生副作用",
        "10. 合理使用deleter来清理资源"
    ]
    
    for practice in practices:
        print(practice)
    
    print("\n@property的优势:")
    advantages = [
        "• 提供了类似属性的简洁访问语法",
        "• 可以在不改变接口的情况下添加逻辑",
        "• 支持数据验证和转换",
        "• 可以创建只读、只写或读写属性",
        "• 保持了封装性和数据安全性"
    ]
    
    for advantage in advantages:
        print(advantage)


if __name__ == "__main__":
    # 运行所有演示
    demonstrate_basic_property()
    demonstrate_complex_validation()
    demonstrate_temperature_conversion()
    demonstrate_secure_bank_account()
    property_best_practices()