#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据验证和保护

数据验证是封装的重要组成部分，通过在数据设置时进行验证，
可以确保对象始终处于有效状态，提高程序的健壮性和安全性。

学习目标：
1. 理解数据验证的重要性
2. 掌握各种验证技术
3. 学会设计健壮的数据保护机制
4. 了解异常处理在数据验证中的应用
"""

import re
from datetime import datetime, date
from typing import List, Optional, Union
from enum import Enum
from dataclasses import dataclass


# 1. 基本数据验证
class Person:
    """人员类 - 基本数据验证"""
    
    def __init__(self, name: str, age: int, email: str):
        self.name = name  # 使用setter进行验证
        self.age = age    # 使用setter进行验证
        self.email = email  # 使用setter进行验证
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("姓名必须是字符串")
        if not value.strip():
            raise ValueError("姓名不能为空")
        if len(value) > 50:
            raise ValueError("姓名长度不能超过50个字符")
        self._name = value.strip()
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int):
        if not isinstance(value, int):
            raise TypeError("年龄必须是整数")
        if value < 0:
            raise ValueError("年龄不能为负数")
        if value > 150:
            raise ValueError("年龄不能超过150岁")
        self._age = value
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, value: str):
        if not isinstance(value, str):
            raise TypeError("邮箱必须是字符串")
        if not self._validate_email(value):
            raise ValueError("邮箱格式不正确")
        self._email = value.lower().strip()
    
    def _validate_email(self, email: str) -> bool:
        """验证邮箱格式"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"


# 2. 复杂数据验证：银行账户
class AccountType(Enum):
    """账户类型枚举"""
    SAVINGS = "储蓄账户"
    CHECKING = "支票账户"
    CREDIT = "信用账户"


class BankAccount:
    """银行账户 - 复杂数据验证"""
    
    # 类级别的验证规则
    MIN_BALANCE = 0
    MAX_BALANCE = 1000000
    MIN_TRANSACTION = 0.01
    MAX_TRANSACTION = 50000
    
    def __init__(self, account_number: str, account_type: AccountType, 
                 initial_balance: float = 0, overdraft_limit: float = 0):
        self._transaction_history = []
        self._is_frozen = False
        
        # 使用属性设置器进行验证
        self.account_number = account_number
        self.account_type = account_type
        self.overdraft_limit = overdraft_limit
        self._balance = 0  # 先设置为0，然后通过存款设置初始余额
        
        if initial_balance > 0:
            self._deposit_internal(initial_balance, "初始存款")
    
    @property
    def account_number(self) -> str:
        return self._account_number
    
    @account_number.setter
    def account_number(self, value: str):
        if not isinstance(value, str):
            raise TypeError("账户号码必须是字符串")
        if not re.match(r'^\d{10,20}$', value):
            raise ValueError("账户号码必须是10-20位数字")
        self._account_number = value
    
    @property
    def account_type(self) -> AccountType:
        return self._account_type
    
    @account_type.setter
    def account_type(self, value: AccountType):
        if not isinstance(value, AccountType):
            raise TypeError("账户类型必须是AccountType枚举")
        self._account_type = value
    
    @property
    def balance(self) -> float:
        return self._balance
    
    @property
    def overdraft_limit(self) -> float:
        return self._overdraft_limit
    
    @overdraft_limit.setter
    def overdraft_limit(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("透支限额必须是数字")
        if value < 0:
            raise ValueError("透支限额不能为负数")
        if value > 10000:
            raise ValueError("透支限额不能超过10000")
        self._overdraft_limit = float(value)
    
    @property
    def is_frozen(self) -> bool:
        return self._is_frozen
    
    def deposit(self, amount: float, description: str = "存款") -> bool:
        """存款"""
        try:
            self._validate_account_status()
            self._validate_transaction_amount(amount)
            self._deposit_internal(amount, description)
            return True
        except (ValueError, RuntimeError) as e:
            print(f"存款失败: {e}")
            return False
    
    def withdraw(self, amount: float, description: str = "取款") -> bool:
        """取款"""
        try:
            self._validate_account_status()
            self._validate_transaction_amount(amount)
            self._validate_withdrawal(amount)
            
            self._balance -= amount
            self._add_transaction("取款", -amount, description)
            return True
        except (ValueError, RuntimeError) as e:
            print(f"取款失败: {e}")
            return False
    
    def transfer(self, target_account: 'BankAccount', amount: float, 
                description: str = "转账") -> bool:
        """转账"""
        if not isinstance(target_account, BankAccount):
            print("转账失败: 目标账户无效")
            return False
        
        if self.withdraw(amount, f"转账至{target_account.account_number}"):
            if target_account.deposit(amount, f"来自{self.account_number}的转账"):
                return True
            else:
                # 如果目标账户存款失败，回滚本账户的取款
                self.deposit(amount, "转账回滚")
        return False
    
    def freeze_account(self, reason: str = "账户冻结"):
        """冻结账户"""
        self._is_frozen = True
        self._add_transaction("冻结", 0, reason)
    
    def unfreeze_account(self, reason: str = "账户解冻"):
        """解冻账户"""
        self._is_frozen = False
        self._add_transaction("解冻", 0, reason)
    
    def get_transaction_history(self, limit: int = 10) -> List[dict]:
        """获取交易历史"""
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError("限制数量必须是正整数")
        return self._transaction_history[-limit:]
    
    # 私有验证方法
    def _validate_account_status(self):
        """验证账户状态"""
        if self._is_frozen:
            raise RuntimeError("账户已冻结，无法进行交易")
    
    def _validate_transaction_amount(self, amount: float):
        """验证交易金额"""
        if not isinstance(amount, (int, float)):
            raise TypeError("交易金额必须是数字")
        if amount <= 0:
            raise ValueError("交易金额必须大于0")
        if amount < self.MIN_TRANSACTION:
            raise ValueError(f"交易金额不能少于{self.MIN_TRANSACTION}")
        if amount > self.MAX_TRANSACTION:
            raise ValueError(f"交易金额不能超过{self.MAX_TRANSACTION}")
    
    def _validate_withdrawal(self, amount: float):
        """验证取款"""
        available_balance = self._balance + self._overdraft_limit
        if amount > available_balance:
            raise ValueError(f"余额不足，可用余额: {available_balance}")
    
    def _deposit_internal(self, amount: float, description: str):
        """内部存款方法"""
        new_balance = self._balance + amount
        if new_balance > self.MAX_BALANCE:
            raise ValueError(f"余额不能超过{self.MAX_BALANCE}")
        
        self._balance = new_balance
        self._add_transaction("存款", amount, description)
    
    def _add_transaction(self, transaction_type: str, amount: float, description: str):
        """添加交易记录"""
        transaction = {
            'timestamp': datetime.now(),
            'type': transaction_type,
            'amount': amount,
            'balance': self._balance,
            'description': description
        }
        self._transaction_history.append(transaction)
    
    def __str__(self):
        return f"BankAccount({self.account_number}, {self.account_type.value}, ¥{self.balance:.2f})"


# 3. 数据类验证装饰器
class ValidationError(Exception):
    """验证错误异常"""
    pass


def validate_range(min_val=None, max_val=None):
    """范围验证装饰器"""
    def decorator(func):
        def wrapper(self, value):
            if min_val is not None and value < min_val:
                raise ValidationError(f"值不能小于{min_val}")
            if max_val is not None and value > max_val:
                raise ValidationError(f"值不能大于{max_val}")
            return func(self, value)
        return wrapper
    return decorator


def validate_type(expected_type):
    """类型验证装饰器"""
    def decorator(func):
        def wrapper(self, value):
            if not isinstance(value, expected_type):
                raise ValidationError(f"期望类型{expected_type.__name__}，实际类型{type(value).__name__}")
            return func(self, value)
        return wrapper
    return decorator


def validate_not_empty(func):
    """非空验证装饰器"""
    def wrapper(self, value):
        if not value or (isinstance(value, str) and not value.strip()):
            raise ValidationError("值不能为空")
        return func(self, value)
    return wrapper


class Product:
    """产品类 - 使用验证装饰器"""
    
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    @validate_type(str)
    @validate_not_empty
    def name(self, value: str):
        self._name = value.strip()
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    @validate_type((int, float))
    @validate_range(min_val=0, max_val=100000)
    def price(self, value: float):
        self._price = float(value)
    
    @property
    def quantity(self) -> int:
        return self._quantity
    
    @quantity.setter
    @validate_type(int)
    @validate_range(min_val=0, max_val=10000)
    def quantity(self, value: int):
        self._quantity = value
    
    @property
    def total_value(self) -> float:
        """计算总价值"""
        return self._price * self._quantity
    
    def __str__(self):
        return f"Product('{self.name}', ¥{self.price:.2f}, {self.quantity}件)"


# 4. 复合验证：用户注册系统
class UserRegistration:
    """用户注册系统 - 复合验证"""
    
    def __init__(self):
        self._registered_users = set()
        self._registered_emails = set()
    
    def register_user(self, username: str, password: str, email: str, 
                     birth_date: str, phone: str) -> bool:
        """注册用户"""
        try:
            # 验证所有字段
            self._validate_username(username)
            self._validate_password(password)
            self._validate_email(email)
            self._validate_birth_date(birth_date)
            self._validate_phone(phone)
            
            # 检查唯一性
            self._check_uniqueness(username, email)
            
            # 注册成功
            self._registered_users.add(username.lower())
            self._registered_emails.add(email.lower())
            
            print(f"用户 {username} 注册成功！")
            return True
            
        except ValidationError as e:
            print(f"注册失败: {e}")
            return False
    
    def _validate_username(self, username: str):
        """验证用户名"""
        if not isinstance(username, str):
            raise ValidationError("用户名必须是字符串")
        if not username.strip():
            raise ValidationError("用户名不能为空")
        if len(username) < 3:
            raise ValidationError("用户名长度不能少于3个字符")
        if len(username) > 20:
            raise ValidationError("用户名长度不能超过20个字符")
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValidationError("用户名只能包含字母、数字和下划线")
    
    def _validate_password(self, password: str):
        """验证密码"""
        if not isinstance(password, str):
            raise ValidationError("密码必须是字符串")
        if len(password) < 8:
            raise ValidationError("密码长度不能少于8个字符")
        if len(password) > 50:
            raise ValidationError("密码长度不能超过50个字符")
        
        # 检查密码复杂性
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)
        
        if not (has_upper and has_lower and has_digit):
            raise ValidationError("密码必须包含大写字母、小写字母和数字")
        if not has_special:
            raise ValidationError("密码必须包含至少一个特殊字符")
    
    def _validate_email(self, email: str):
        """验证邮箱"""
        if not isinstance(email, str):
            raise ValidationError("邮箱必须是字符串")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValidationError("邮箱格式不正确")
    
    def _validate_birth_date(self, birth_date: str):
        """验证出生日期"""
        try:
            birth = datetime.strptime(birth_date, '%Y-%m-%d').date()
            today = date.today()
            age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
            
            if age < 13:
                raise ValidationError("年龄不能小于13岁")
            if age > 120:
                raise ValidationError("年龄不能超过120岁")
        except ValueError:
            raise ValidationError("出生日期格式不正确，应为YYYY-MM-DD")
    
    def _validate_phone(self, phone: str):
        """验证手机号"""
        if not isinstance(phone, str):
            raise ValidationError("手机号必须是字符串")
        # 简化的中国手机号验证
        if not re.match(r'^1[3-9]\d{9}$', phone):
            raise ValidationError("手机号格式不正确")
    
    def _check_uniqueness(self, username: str, email: str):
        """检查唯一性"""
        if username.lower() in self._registered_users:
            raise ValidationError("用户名已存在")
        if email.lower() in self._registered_emails:
            raise ValidationError("邮箱已被注册")


def demonstrate_validation():
    """演示数据验证和保护"""
    print("=" * 60)
    print("数据验证和保护演示")
    print("=" * 60)
    
    # 1. 基本数据验证
    print("\n1. 基本数据验证:")
    try:
        person = Person("张三", 25, "zhangsan@example.com")
        print(f"创建成功: {person}")
        
        # 尝试设置无效数据
        person.age = -5  # 这会抛出异常
    except ValueError as e:
        print(f"验证失败: {e}")
    
    # 2. 银行账户验证
    print("\n2. 银行账户验证:")
    try:
        account = BankAccount("1234567890", AccountType.SAVINGS, 1000, 500)
        print(f"账户创建成功: {account}")
        
        # 正常操作
        account.deposit(500, "工资")
        print(f"存款后: {account}")
        
        account.withdraw(200, "购物")
        print(f"取款后: {account}")
        
        # 尝试无效操作
        account.withdraw(2000, "大额取款")  # 余额不足
        
    except (ValueError, RuntimeError) as e:
        print(f"操作失败: {e}")
    
    # 3. 产品验证装饰器
    print("\n3. 产品验证装饰器:")
    try:
        product = Product("笔记本电脑", 5999.99, 10)
        print(f"产品创建成功: {product}")
        print(f"总价值: ¥{product.total_value:.2f}")
        
        # 尝试设置无效价格
        product.price = -100  # 这会抛出异常
    except ValidationError as e:
        print(f"验证失败: {e}")
    
    # 4. 用户注册验证
    print("\n4. 用户注册验证:")
    registration = UserRegistration()
    
    # 成功注册
    registration.register_user(
        username="alice123",
        password="SecurePass123!",
        email="alice@example.com",
        birth_date="1990-05-15",
        phone="13812345678"
    )
    
    # 失败注册（密码不符合要求）
    registration.register_user(
        username="bob456",
        password="weak",  # 密码太弱
        email="bob@example.com",
        birth_date="1985-10-20",
        phone="13987654321"
    )
    
    # 5. 银行账户转账演示
    print("\n5. 银行账户转账演示:")
    account1 = BankAccount("1111111111", AccountType.CHECKING, 2000)
    account2 = BankAccount("2222222222", AccountType.SAVINGS, 500)
    
    print(f"转账前 - 账户1: {account1}")
    print(f"转账前 - 账户2: {account2}")
    
    success = account1.transfer(account2, 300, "朋友转账")
    print(f"转账结果: {'成功' if success else '失败'}")
    
    print(f"转账后 - 账户1: {account1}")
    print(f"转账后 - 账户2: {account2}")
    
    # 查看交易历史
    print("\n账户1交易历史:")
    for transaction in account1.get_transaction_history(3):
        print(f"  {transaction['timestamp'].strftime('%H:%M:%S')}: {transaction['type']} ¥{transaction['amount']:.2f} - {transaction['description']}")


def show_validation_best_practices():
    """显示数据验证最佳实践"""
    print("\n" + "=" * 60)
    print("数据验证最佳实践")
    print("=" * 60)
    
    practices = """
1. 验证原则:
   ✓ 早期验证 - 在数据进入系统时立即验证
   ✓ 完整验证 - 验证所有相关约束条件
   ✓ 明确错误 - 提供清晰的错误信息
   ✓ 一致性 - 在整个应用中使用一致的验证规则

2. 验证层次:
   ✓ 类型验证 - 确保数据类型正确
   ✓ 格式验证 - 验证数据格式（如邮箱、电话）
   ✓ 范围验证 - 检查数值范围
   ✓ 业务规则验证 - 验证业务逻辑约束
   ✓ 唯一性验证 - 确保数据唯一性

3. 实现技术:
   ✓ 属性装饰器 - 使用@property进行验证
   ✓ 验证装饰器 - 创建可重用的验证装饰器
   ✓ 验证函数 - 独立的验证函数
   ✓ 异常处理 - 适当的异常类型和消息

4. 安全考虑:
   ✓ 输入清理 - 清理和标准化输入数据
   ✓ 长度限制 - 防止缓冲区溢出
   ✓ 注入防护 - 防止SQL注入等攻击
   ✓ 敏感数据 - 特殊处理密码等敏感信息

5. 性能优化:
   ✓ 缓存验证结果 - 避免重复验证
   ✓ 延迟验证 - 在必要时才进行复杂验证
   ✓ 批量验证 - 一次验证多个字段
   ✓ 异步验证 - 对于耗时的验证使用异步处理

记住：好的验证不仅能防止错误，还能提供良好的用户体验！
    """
    
    print(practices)


if __name__ == "__main__":
    demonstrate_validation()
    show_validation_best_practices()