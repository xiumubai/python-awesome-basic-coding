#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
封装的基本概念和意义

封装（Encapsulation）是面向对象编程的三大特性之一（封装、继承、多态）。
封装是指将数据（属性）和操作数据的方法（函数）绑定在一起，形成一个独立的单元（类），
并对外隐藏对象的内部实现细节，只暴露必要的接口。

封装的主要目的：
1. 数据保护：防止外部代码直接访问和修改对象的内部数据
2. 接口简化：只暴露必要的方法，隐藏复杂的实现细节
3. 代码维护：内部实现的改变不会影响外部代码
4. 数据一致性：通过控制访问方式确保数据的有效性
"""

# 示例1：没有封装的类（不推荐）
class BadBankAccount:
    """没有封装的银行账户类 - 不安全的设计"""
    
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance  # 余额可以被直接访问和修改
    
    def display_info(self):
        print(f"账户号: {self.account_number}, 余额: {self.balance}")


# 示例2：使用封装的类（推荐）
class GoodBankAccount:
    """使用封装的银行账户类 - 安全的设计"""
    
    def __init__(self, account_number, initial_balance):
        self._account_number = account_number  # 使用下划线表示受保护的属性
        self._balance = initial_balance if initial_balance >= 0 else 0
    
    def get_balance(self):
        """获取账户余额"""
        return self._balance
    
    def get_account_number(self):
        """获取账户号"""
        return self._account_number
    
    def deposit(self, amount):
        """存款操作"""
        if amount > 0:
            self._balance += amount
            print(f"存款成功！存入金额: {amount}, 当前余额: {self._balance}")
            return True
        else:
            print("存款金额必须大于0")
            return False
    
    def withdraw(self, amount):
        """取款操作"""
        if amount <= 0:
            print("取款金额必须大于0")
            return False
        
        if amount > self._balance:
            print("余额不足，取款失败")
            return False
        
        self._balance -= amount
        print(f"取款成功！取出金额: {amount}, 当前余额: {self._balance}")
        return True
    
    def display_info(self):
        """显示账户信息"""
        print(f"账户号: {self._account_number}, 余额: {self._balance}")


# 示例3：更严格的封装 - 使用双下划线
class SecureBankAccount:
    """更安全的银行账户类 - 使用名称修饰"""
    
    def __init__(self, account_number, initial_balance, pin):
        self.__account_number = account_number  # 私有属性
        self.__balance = initial_balance if initial_balance >= 0 else 0
        self.__pin = pin  # 密码
        self.__transaction_history = []  # 交易历史
    
    def __verify_pin(self, pin):
        """私有方法：验证密码"""
        return self.__pin == pin
    
    def __add_transaction(self, transaction_type, amount):
        """私有方法：添加交易记录"""
        import datetime
        self.__transaction_history.append({
            'type': transaction_type,
            'amount': amount,
            'timestamp': datetime.datetime.now(),
            'balance': self.__balance
        })
    
    def get_balance(self, pin):
        """获取余额（需要密码验证）"""
        if self.__verify_pin(pin):
            return self.__balance
        else:
            print("密码错误！")
            return None
    
    def deposit(self, amount, pin):
        """存款（需要密码验证）"""
        if not self.__verify_pin(pin):
            print("密码错误！")
            return False
        
        if amount > 0:
            self.__balance += amount
            self.__add_transaction('存款', amount)
            print(f"存款成功！存入金额: {amount}, 当前余额: {self.__balance}")
            return True
        else:
            print("存款金额必须大于0")
            return False
    
    def withdraw(self, amount, pin):
        """取款（需要密码验证）"""
        if not self.__verify_pin(pin):
            print("密码错误！")
            return False
        
        if amount <= 0:
            print("取款金额必须大于0")
            return False
        
        if amount > self.__balance:
            print("余额不足，取款失败")
            return False
        
        self.__balance -= amount
        self.__add_transaction('取款', amount)
        print(f"取款成功！取出金额: {amount}, 当前余额: {self.__balance}")
        return True
    
    def get_transaction_history(self, pin):
        """获取交易历史（需要密码验证）"""
        if self.__verify_pin(pin):
            return self.__transaction_history.copy()  # 返回副本，防止外部修改
        else:
            print("密码错误！")
            return None


def demonstrate_encapsulation():
    """演示封装的重要性"""
    print("=" * 50)
    print("封装演示")
    print("=" * 50)
    
    # 1. 没有封装的问题
    print("\n1. 没有封装的问题：")
    bad_account = BadBankAccount("12345", 1000)
    print(f"初始余额: {bad_account.balance}")
    
    # 外部可以直接修改余额，这是不安全的
    bad_account.balance = -500  # 这不应该被允许！
    print(f"被恶意修改后的余额: {bad_account.balance}")
    
    # 2. 使用封装的好处
    print("\n2. 使用封装的好处：")
    good_account = GoodBankAccount("67890", 1000)
    print(f"初始余额: {good_account.get_balance()}")
    
    # 只能通过方法来操作余额
    good_account.deposit(500)
    good_account.withdraw(200)
    good_account.withdraw(2000)  # 余额不足，操作失败
    
    # 3. 更严格的封装
    print("\n3. 更严格的封装：")
    secure_account = SecureBankAccount("99999", 1000, "1234")
    
    # 需要密码才能操作
    print(f"余额查询: {secure_account.get_balance('1234')}")
    secure_account.deposit(300, "1234")
    secure_account.withdraw(100, "1234")
    
    # 错误密码
    secure_account.get_balance("0000")
    
    # 查看交易历史
    history = secure_account.get_transaction_history("1234")
    if history:
        print("\n交易历史:")
        for transaction in history:
            print(f"  {transaction['type']}: {transaction['amount']}, "
                  f"余额: {transaction['balance']}, "
                  f"时间: {transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")


def demonstrate_access_levels():
    """演示不同的访问级别"""
    print("\n" + "=" * 50)
    print("访问级别演示")
    print("=" * 50)
    
    account = SecureBankAccount("12345", 1000, "1234")
    
    # 公有方法 - 可以正常访问
    print("\n公有方法访问:")
    balance = account.get_balance("1234")
    print(f"余额: {balance}")
    
    # 尝试访问私有属性 - 会失败
    print("\n尝试访问私有属性:")
    try:
        # 这会引发 AttributeError
        print(account.__balance)
    except AttributeError as e:
        print(f"无法访问私有属性: {e}")
    
    # 通过名称修饰可以访问（不推荐）
    print("\n通过名称修饰访问（不推荐）:")
    try:
        # Python的名称修饰机制
        print(f"通过名称修饰访问余额: {account._SecureBankAccount__balance}")
        print("注意：这种访问方式破坏了封装性，不应该在实际代码中使用！")
    except AttributeError as e:
        print(f"访问失败: {e}")


if __name__ == "__main__":
    # 运行演示
    demonstrate_encapsulation()
    demonstrate_access_levels()
    
    print("\n" + "=" * 50)
    print("封装的核心原则")
    print("=" * 50)
    print("1. 隐藏内部实现细节")
    print("2. 只暴露必要的接口")
    print("3. 保护数据的完整性")
    print("4. 提高代码的可维护性")
    print("5. 降低系统的耦合度")