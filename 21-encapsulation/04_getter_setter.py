#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
getter和setter方法

getter和setter方法是面向对象编程中控制属性访问的经典模式。
在Python中，我们可以通过多种方式实现getter和setter：

1. 传统的getter/setter方法
2. 使用@property装饰器（推荐）
3. 使用property()函数
4. 自定义描述符

本文件将详细演示这些不同的实现方式，以及它们的优缺点。
"""

import re
from datetime import datetime, date
from typing import Optional, List

# 示例1：传统的getter/setter方法
class TraditionalStudent:
    """传统方式的学生类 - 使用显式的getter/setter方法"""
    
    def __init__(self, name, age, student_id):
        self._name = None
        self._age = None
        self._student_id = None
        self._grades = []
        
        # 使用setter方法设置初始值
        self.set_name(name)
        self.set_age(age)
        self.set_student_id(student_id)
    
    # Name的getter和setter
    def get_name(self):
        """获取学生姓名"""
        return self._name
    
    def set_name(self, name):
        """设置学生姓名"""
        if not isinstance(name, str):
            raise TypeError("姓名必须是字符串")
        if not name.strip():
            raise ValueError("姓名不能为空")
        if len(name.strip()) < 2:
            raise ValueError("姓名至少需要2个字符")
        
        self._name = name.strip().title()
    
    # Age的getter和setter
    def get_age(self):
        """获取学生年龄"""
        return self._age
    
    def set_age(self, age):
        """设置学生年龄"""
        if not isinstance(age, int):
            raise TypeError("年龄必须是整数")
        if age < 5 or age > 100:
            raise ValueError("年龄必须在5-100之间")
        
        self._age = age
    
    # Student ID的getter和setter
    def get_student_id(self):
        """获取学号"""
        return self._student_id
    
    def set_student_id(self, student_id):
        """设置学号"""
        if not isinstance(student_id, str):
            raise TypeError("学号必须是字符串")
        
        # 学号格式验证：8位数字
        if not re.match(r'^\d{8}$', student_id):
            raise ValueError("学号必须是8位数字")
        
        self._student_id = student_id
    
    # Grades的getter和setter
    def get_grades(self):
        """获取成绩列表（返回副本）"""
        return self._grades.copy()
    
    def add_grade(self, grade):
        """添加成绩"""
        if not isinstance(grade, (int, float)):
            raise TypeError("成绩必须是数字")
        if grade < 0 or grade > 100:
            raise ValueError("成绩必须在0-100之间")
        
        self._grades.append(grade)
    
    def get_average_grade(self):
        """获取平均成绩"""
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)
    
    def __str__(self):
        return f"Student(name='{self._name}', age={self._age}, id='{self._student_id}')"


# 示例2：使用@property装饰器的现代方式
class ModernStudent:
    """现代方式的学生类 - 使用@property装饰器"""
    
    def __init__(self, name, age, student_id):
        self._name = None
        self._age = None
        self._student_id = None
        self._grades = []
        self._enrollment_date = datetime.now().date()
        
        # 通过属性设置器设置初始值
        self.name = name
        self.age = age
        self.student_id = student_id
    
    @property
    def name(self):
        """学生姓名属性"""
        return self._name
    
    @name.setter
    def name(self, value):
        """设置学生姓名"""
        if not isinstance(value, str):
            raise TypeError("姓名必须是字符串")
        if not value.strip():
            raise ValueError("姓名不能为空")
        if len(value.strip()) < 2:
            raise ValueError("姓名至少需要2个字符")
        
        self._name = value.strip().title()
    
    @property
    def age(self):
        """学生年龄属性"""
        return self._age
    
    @age.setter
    def age(self, value):
        """设置学生年龄"""
        if not isinstance(value, int):
            raise TypeError("年龄必须是整数")
        if value < 5 or value > 100:
            raise ValueError("年龄必须在5-100之间")
        
        self._age = value
    
    @property
    def student_id(self):
        """学号属性"""
        return self._student_id
    
    @student_id.setter
    def student_id(self, value):
        """设置学号"""
        if not isinstance(value, str):
            raise TypeError("学号必须是字符串")
        
        # 学号格式验证：8位数字
        if not re.match(r'^\d{8}$', value):
            raise ValueError("学号必须是8位数字")
        
        self._student_id = value
    
    @property
    def grades(self):
        """成绩列表属性（只读，返回副本）"""
        return self._grades.copy()
    
    @property
    def average_grade(self):
        """平均成绩属性（只读）"""
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)
    
    @property
    def grade_count(self):
        """成绩数量属性（只读）"""
        return len(self._grades)
    
    @property
    def enrollment_date(self):
        """入学日期属性（只读）"""
        return self._enrollment_date
    
    @property
    def academic_status(self):
        """学术状态属性（只读）"""
        if not self._grades:
            return "无成绩记录"
        
        avg = self.average_grade
        if avg >= 90:
            return "优秀"
        elif avg >= 80:
            return "良好"
        elif avg >= 70:
            return "中等"
        elif avg >= 60:
            return "及格"
        else:
            return "不及格"
    
    def add_grade(self, grade):
        """添加成绩"""
        if not isinstance(grade, (int, float)):
            raise TypeError("成绩必须是数字")
        if grade < 0 or grade > 100:
            raise ValueError("成绩必须在0-100之间")
        
        self._grades.append(grade)
    
    def remove_grade(self, index):
        """删除指定位置的成绩"""
        if 0 <= index < len(self._grades):
            return self._grades.pop(index)
        else:
            raise IndexError("成绩索引超出范围")
    
    def __str__(self):
        return f"Student(name='{self._name}', age={self._age}, id='{self._student_id}', avg={self.average_grade:.1f})"


# 示例3：使用property()函数的方式
class PropertyFunctionStudent:
    """使用property()函数的学生类"""
    
    def __init__(self, name, age):
        self._name = None
        self._age = None
        self._created_at = datetime.now()
        
        # 通过属性设置器设置初始值
        self.name = name
        self.age = age
    
    def _get_name(self):
        """姓名getter"""
        return self._name
    
    def _set_name(self, value):
        """姓名setter"""
        if not isinstance(value, str):
            raise TypeError("姓名必须是字符串")
        if not value.strip():
            raise ValueError("姓名不能为空")
        
        self._name = value.strip().title()
    
    def _del_name(self):
        """姓名deleter"""
        print(f"删除姓名: {self._name}")
        self._name = None
    
    def _get_age(self):
        """年龄getter"""
        return self._age
    
    def _set_age(self, value):
        """年龄setter"""
        if not isinstance(value, int):
            raise TypeError("年龄必须是整数")
        if value < 0 or value > 150:
            raise ValueError("年龄必须在0-150之间")
        
        self._age = value
    
    def _get_created_at(self):
        """创建时间getter（只读）"""
        return self._created_at
    
    # 使用property()函数创建属性
    name = property(_get_name, _set_name, _del_name, "学生姓名属性")
    age = property(_get_age, _set_age, None, "学生年龄属性")
    created_at = property(_get_created_at, None, None, "创建时间属性（只读）")
    
    def __str__(self):
        return f"PropertyStudent(name='{self._name}', age={self._age})"


# 示例4：自定义描述符实现getter/setter
class ValidatedAttribute:
    """自定义描述符 - 实现属性验证"""
    
    def __init__(self, name, validator=None, default=None):
        self.name = name
        self.validator = validator
        self.default = default
        self.private_name = f'_{name}'
    
    def __get__(self, obj, objtype=None):
        """描述符getter"""
        if obj is None:
            return self
        return getattr(obj, self.private_name, self.default)
    
    def __set__(self, obj, value):
        """描述符setter"""
        if self.validator:
            self.validator(value)
        setattr(obj, self.private_name, value)
    
    def __delete__(self, obj):
        """描述符deleter"""
        if hasattr(obj, self.private_name):
            delattr(obj, self.private_name)


def validate_name(value):
    """姓名验证函数"""
    if not isinstance(value, str):
        raise TypeError("姓名必须是字符串")
    if not value.strip():
        raise ValueError("姓名不能为空")
    if len(value.strip()) < 2:
        raise ValueError("姓名至少需要2个字符")


def validate_age(value):
    """年龄验证函数"""
    if not isinstance(value, int):
        raise TypeError("年龄必须是整数")
    if value < 0 or value > 150:
        raise ValueError("年龄必须在0-150之间")


def validate_email(value):
    """邮箱验证函数"""
    if not isinstance(value, str):
        raise TypeError("邮箱必须是字符串")
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
        raise ValueError("邮箱格式不正确")


class DescriptorStudent:
    """使用自定义描述符的学生类"""
    
    # 使用描述符定义属性
    name = ValidatedAttribute('name', validate_name)
    age = ValidatedAttribute('age', validate_age)
    email = ValidatedAttribute('email', validate_email)
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self._registration_time = datetime.now()
    
    @property
    def registration_time(self):
        """注册时间（只读）"""
        return self._registration_time
    
    @property
    def profile_summary(self):
        """个人资料摘要（只读）"""
        return f"{self.name} ({self.age}岁) - {self.email}"
    
    def __str__(self):
        return f"DescriptorStudent({self.profile_summary})"


# 示例5：复杂的getter/setter场景 - 购物车类
class ShoppingCart:
    """购物车类 - 演示复杂的getter/setter场景"""
    
    def __init__(self, customer_name):
        self._customer_name = customer_name
        self._items = {}  # {product_id: {'name': str, 'price': float, 'quantity': int}}
        self._discount_rate = 0.0
        self._tax_rate = 0.1  # 10%税率
        self._created_at = datetime.now()
    
    @property
    def customer_name(self):
        """客户姓名"""
        return self._customer_name
    
    @customer_name.setter
    def customer_name(self, value):
        """设置客户姓名"""
        if not isinstance(value, str):
            raise TypeError("客户姓名必须是字符串")
        if not value.strip():
            raise ValueError("客户姓名不能为空")
        
        self._customer_name = value.strip()
    
    @property
    def items(self):
        """购物车商品（只读，返回副本）"""
        return self._items.copy()
    
    @property
    def item_count(self):
        """商品种类数量"""
        return len(self._items)
    
    @property
    def total_quantity(self):
        """商品总数量"""
        return sum(item['quantity'] for item in self._items.values())
    
    @property
    def subtotal(self):
        """小计（税前）"""
        return sum(item['price'] * item['quantity'] for item in self._items.values())
    
    @property
    def discount_amount(self):
        """折扣金额"""
        return self.subtotal * self._discount_rate
    
    @property
    def tax_amount(self):
        """税额"""
        return (self.subtotal - self.discount_amount) * self._tax_rate
    
    @property
    def total(self):
        """总计"""
        return self.subtotal - self.discount_amount + self.tax_amount
    
    @property
    def discount_rate(self):
        """折扣率"""
        return self._discount_rate
    
    @discount_rate.setter
    def discount_rate(self, value):
        """设置折扣率"""
        if not isinstance(value, (int, float)):
            raise TypeError("折扣率必须是数字")
        if value < 0 or value > 1:
            raise ValueError("折扣率必须在0-1之间")
        
        self._discount_rate = value
    
    @property
    def tax_rate(self):
        """税率"""
        return self._tax_rate
    
    @tax_rate.setter
    def tax_rate(self, value):
        """设置税率"""
        if not isinstance(value, (int, float)):
            raise TypeError("税率必须是数字")
        if value < 0 or value > 1:
            raise ValueError("税率必须在0-1之间")
        
        self._tax_rate = value
    
    @property
    def is_empty(self):
        """购物车是否为空"""
        return len(self._items) == 0
    
    @property
    def created_at(self):
        """创建时间（只读）"""
        return self._created_at
    
    def add_item(self, product_id, name, price, quantity=1):
        """添加商品"""
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("价格必须是非负数")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("数量必须是正整数")
        
        if product_id in self._items:
            self._items[product_id]['quantity'] += quantity
        else:
            self._items[product_id] = {
                'name': name,
                'price': price,
                'quantity': quantity
            }
    
    def remove_item(self, product_id):
        """移除商品"""
        if product_id in self._items:
            del self._items[product_id]
        else:
            raise KeyError(f"商品 {product_id} 不在购物车中")
    
    def update_quantity(self, product_id, quantity):
        """更新商品数量"""
        if product_id not in self._items:
            raise KeyError(f"商品 {product_id} 不在购物车中")
        
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("数量必须是正整数")
        
        self._items[product_id]['quantity'] = quantity
    
    def clear(self):
        """清空购物车"""
        self._items.clear()
    
    def get_receipt(self):
        """获取购物小票"""
        receipt = []
        receipt.append(f"客户: {self.customer_name}")
        receipt.append(f"时间: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        receipt.append("-" * 40)
        
        for product_id, item in self._items.items():
            line = f"{item['name']} x{item['quantity']} @ ¥{item['price']:.2f} = ¥{item['price'] * item['quantity']:.2f}"
            receipt.append(line)
        
        receipt.append("-" * 40)
        receipt.append(f"小计: ¥{self.subtotal:.2f}")
        
        if self.discount_amount > 0:
            receipt.append(f"折扣({self.discount_rate*100:.1f}%): -¥{self.discount_amount:.2f}")
        
        receipt.append(f"税费({self.tax_rate*100:.1f}%): ¥{self.tax_amount:.2f}")
        receipt.append(f"总计: ¥{self.total:.2f}")
        
        return "\n".join(receipt)
    
    def __str__(self):
        return f"ShoppingCart(customer='{self.customer_name}', items={self.item_count}, total=¥{self.total:.2f})"


def demonstrate_traditional_getters_setters():
    """演示传统的getter/setter方法"""
    print("=" * 60)
    print("传统getter/setter方法演示")
    print("=" * 60)
    
    student = TraditionalStudent("张三", 20, "20230001")
    
    print("\n1. 使用getter方法获取属性：")
    print(f"姓名: {student.get_name()}")
    print(f"年龄: {student.get_age()}")
    print(f"学号: {student.get_student_id()}")
    
    print("\n2. 使用setter方法设置属性：")
    student.set_name("李四")
    student.set_age(22)
    print(f"修改后: {student}")
    
    print("\n3. 添加成绩：")
    student.add_grade(85)
    student.add_grade(92)
    student.add_grade(78)
    print(f"成绩列表: {student.get_grades()}")
    print(f"平均成绩: {student.get_average_grade():.1f}")
    
    print("\n4. 验证错误：")
    try:
        student.set_age(-5)
    except ValueError as e:
        print(f"年龄验证错误: {e}")
    
    try:
        student.set_student_id("123")
    except ValueError as e:
        print(f"学号验证错误: {e}")


def demonstrate_property_decorators():
    """演示@property装饰器"""
    print("\n" + "=" * 60)
    print("@property装饰器演示")
    print("=" * 60)
    
    student = ModernStudent("王五", 19, "20230002")
    
    print("\n1. 像普通属性一样访问：")
    print(f"姓名: {student.name}")
    print(f"年龄: {student.age}")
    print(f"学号: {student.student_id}")
    print(f"入学日期: {student.enrollment_date}")
    
    print("\n2. 像普通属性一样设置：")
    student.name = "赵六"
    student.age = 21
    print(f"修改后: {student}")
    
    print("\n3. 只读属性：")
    student.add_grade(88)
    student.add_grade(95)
    student.add_grade(82)
    print(f"成绩列表: {student.grades}")
    print(f"平均成绩: {student.average_grade:.1f}")
    print(f"成绩数量: {student.grade_count}")
    print(f"学术状态: {student.academic_status}")
    
    print("\n4. 尝试修改只读属性：")
    try:
        student.average_grade = 100
    except AttributeError as e:
        print(f"只读属性错误: {e}")


def demonstrate_property_function():
    """演示property()函数"""
    print("\n" + "=" * 60)
    print("property()函数演示")
    print("=" * 60)
    
    student = PropertyFunctionStudent("孙七", 18)
    
    print("\n1. 属性访问：")
    print(f"姓名: {student.name}")
    print(f"年龄: {student.age}")
    print(f"创建时间: {student.created_at}")
    
    print("\n2. 属性设置：")
    student.name = "周八"
    student.age = 20
    print(f"修改后: {student}")
    
    print("\n3. 属性删除：")
    del student.name
    print(f"删除姓名后: {student}")
    
    print("\n4. 只读属性测试：")
    try:
        student.created_at = datetime.now()
    except AttributeError as e:
        print(f"只读属性错误: {e}")


def demonstrate_descriptors():
    """演示自定义描述符"""
    print("\n" + "=" * 60)
    print("自定义描述符演示")
    print("=" * 60)
    
    student = DescriptorStudent("吴九", 22, "wujiu@example.com")
    
    print("\n1. 描述符属性访问：")
    print(f"个人资料: {student.profile_summary}")
    print(f"注册时间: {student.registration_time}")
    
    print("\n2. 描述符属性设置：")
    student.name = "郑十"
    student.age = 24
    student.email = "zhengshi@example.com"
    print(f"修改后: {student}")
    
    print("\n3. 描述符验证：")
    try:
        student.email = "invalid-email"
    except ValueError as e:
        print(f"邮箱验证错误: {e}")
    
    try:
        student.age = -10
    except ValueError as e:
        print(f"年龄验证错误: {e}")


def demonstrate_shopping_cart():
    """演示购物车复杂场景"""
    print("\n" + "=" * 60)
    print("购物车复杂场景演示")
    print("=" * 60)
    
    cart = ShoppingCart("张三")
    
    print("\n1. 添加商品：")
    cart.add_item("P001", "苹果", 5.5, 3)
    cart.add_item("P002", "香蕉", 3.2, 5)
    cart.add_item("P003", "橙子", 4.8, 2)
    
    print(f"购物车状态: {cart}")
    print(f"商品种类: {cart.item_count}")
    print(f"商品总数: {cart.total_quantity}")
    
    print("\n2. 设置折扣：")
    cart.discount_rate = 0.1  # 10%折扣
    print(f"小计: ¥{cart.subtotal:.2f}")
    print(f"折扣: ¥{cart.discount_amount:.2f}")
    print(f"税费: ¥{cart.tax_amount:.2f}")
    print(f"总计: ¥{cart.total:.2f}")
    
    print("\n3. 购物小票：")
    print(cart.get_receipt())
    
    print("\n4. 修改商品数量：")
    cart.update_quantity("P001", 5)
    print(f"修改后总计: ¥{cart.total:.2f}")
    
    print("\n5. 移除商品：")
    cart.remove_item("P002")
    print(f"移除香蕉后: {cart}")


def getter_setter_comparison():
    """getter/setter方法比较"""
    print("\n" + "=" * 60)
    print("getter/setter方法比较")
    print("=" * 60)
    
    comparison = [
        ("方法", "优点", "缺点", "适用场景"),
        ("-" * 15, "-" * 30, "-" * 30, "-" * 20),
        ("传统getter/setter", "明确的方法调用，易于理解", "语法冗长，不够Pythonic", "Java/C#背景开发者"),
        ("@property装饰器", "语法简洁，Pythonic，功能强大", "学习曲线稍陡", "推荐的Python方式"),
        ("property()函数", "灵活性高，可动态创建", "代码可读性较差", "动态属性创建"),
        ("自定义描述符", "最大灵活性，可重用", "复杂度高，过度设计", "框架开发，复杂验证")
    ]
    
    for row in comparison:
        print(f"{row[0]:<15} | {row[1]:<30} | {row[2]:<30} | {row[3]:<20}")
    
    print("\n推荐使用顺序:")
    recommendations = [
        "1. @property装饰器 - 大多数情况的首选",
        "2. 直接属性访问 - 简单场景无需验证",
        "3. property()函数 - 需要动态创建属性",
        "4. 自定义描述符 - 复杂验证逻辑重用",
        "5. 传统getter/setter - 与其他语言保持一致"
    ]
    
    for rec in recommendations:
        print(rec)


if __name__ == "__main__":
    # 运行所有演示
    demonstrate_traditional_getters_setters()
    demonstrate_property_decorators()
    demonstrate_property_function()
    demonstrate_descriptors()
    demonstrate_shopping_cart()
    getter_setter_comparison()