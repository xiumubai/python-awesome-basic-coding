#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
名称修饰机制 (Name Mangling)

名称修饰是Python中实现私有属性的机制，当属性或方法名以双下划线开头时，
Python解释器会自动修改其名称，使其在类外部难以直接访问。

学习目标：
1. 理解名称修饰的工作原理
2. 掌握私有属性的命名规则
3. 了解名称修饰的局限性
4. 学会正确使用私有属性
"""

# 1. 基本名称修饰示例
class BasicNameMangling:
    """演示基本的名称修饰机制"""
    
    def __init__(self):
        self.public = "公有属性"           # 公有属性
        self._protected = "保护属性"       # 保护属性（约定）
        self.__private = "私有属性"        # 私有属性（名称修饰）
    
    def show_attributes(self):
        """显示所有属性"""
        print(f"公有属性: {self.public}")
        print(f"保护属性: {self._protected}")
        print(f"私有属性: {self.__private}")
    
    def __private_method(self):
        """私有方法"""
        return "这是私有方法"
    
    def call_private_method(self):
        """调用私有方法"""
        return self.__private_method()


# 2. 名称修饰的实际效果
class NameManglingDemo:
    """演示名称修饰的实际效果"""
    
    def __init__(self):
        self.__secret = "秘密数据"
        self.__config = {"key": "value"}
    
    def get_secret(self):
        """获取秘密数据的公有方法"""
        return self.__secret
    
    def show_all_attributes(self):
        """显示对象的所有属性"""
        print("对象的所有属性:")
        for attr in dir(self):
            if not attr.startswith('__') or attr.endswith('__'):
                continue
            print(f"  {attr}")


# 3. 继承中的名称修饰
class Parent:
    """父类"""
    
    def __init__(self):
        self.public_data = "父类公有数据"
        self._protected_data = "父类保护数据"
        self.__private_data = "父类私有数据"
    
    def __private_method(self):
        return "父类私有方法"
    
    def access_private(self):
        """访问私有数据和方法"""
        return f"数据: {self.__private_data}, 方法: {self.__private_method()}"


class Child(Parent):
    """子类"""
    
    def __init__(self):
        super().__init__()
        self.__private_data = "子类私有数据"  # 不会覆盖父类的私有数据
    
    def __private_method(self):
        return "子类私有方法"
    
    def access_child_private(self):
        """访问子类私有数据"""
        return f"子类私有数据: {self.__private_data}"
    
    def show_inheritance_demo(self):
        """演示继承中的名称修饰"""
        print("=== 继承中的名称修饰演示 ===")
        print(f"父类方法访问: {self.access_private()}")
        print(f"子类方法访问: {self.access_child_private()}")
        
        # 显示所有私有属性
        print("\n所有私有属性:")
        for attr in dir(self):
            if '_Parent__' in attr or '_Child__' in attr:
                print(f"  {attr}: {getattr(self, attr)}")


# 4. 名称修饰的绕过方法
class SecurityDemo:
    """演示名称修饰的安全性"""
    
    def __init__(self):
        self.__password = "secret123"
        self.__api_key = "abc123xyz"
    
    def verify_password(self, password):
        """验证密码"""
        return self.__password == password
    
    def get_api_key(self):
        """获取API密钥（受保护的方法）"""
        return self.__api_key


# 5. 实际应用：银行账户系统
class BankAccount:
    """银行账户类 - 使用名称修饰保护敏感数据"""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number  # 公有：账户号码
        self.__balance = initial_balance      # 私有：余额
        self.__pin = None                     # 私有：PIN码
        self.__transaction_history = []       # 私有：交易历史
    
    def set_pin(self, pin):
        """设置PIN码"""
        if len(str(pin)) == 4 and str(pin).isdigit():
            self.__pin = pin
            return True
        return False
    
    def verify_pin(self, pin):
        """验证PIN码"""
        return self.__pin == pin
    
    def deposit(self, amount, pin):
        """存款"""
        if not self.verify_pin(pin):
            return "PIN码错误"
        
        if amount > 0:
            self.__balance += amount
            self.__add_transaction("存款", amount)
            return f"存款成功，当前余额: ¥{self.__balance:.2f}"
        return "存款金额必须大于0"
    
    def withdraw(self, amount, pin):
        """取款"""
        if not self.verify_pin(pin):
            return "PIN码错误"
        
        if amount > self.__balance:
            return "余额不足"
        
        if amount > 0:
            self.__balance -= amount
            self.__add_transaction("取款", amount)
            return f"取款成功，当前余额: ¥{self.__balance:.2f}"
        return "取款金额必须大于0"
    
    def get_balance(self, pin):
        """查询余额"""
        if not self.verify_pin(pin):
            return "PIN码错误"
        return f"当前余额: ¥{self.__balance:.2f}"
    
    def get_transaction_history(self, pin):
        """获取交易历史"""
        if not self.verify_pin(pin):
            return "PIN码错误"
        return self.__transaction_history.copy()
    
    def __add_transaction(self, transaction_type, amount):
        """添加交易记录（私有方法）"""
        from datetime import datetime
        self.__transaction_history.append({
            'type': transaction_type,
            'amount': amount,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'balance': self.__balance
        })
    
    def __str__(self):
        return f"BankAccount({self.account_number})"


def demonstrate_name_mangling():
    """演示名称修饰机制"""
    print("=" * 60)
    print("名称修饰机制演示")
    print("=" * 60)
    
    # 1. 基本名称修饰
    print("\n1. 基本名称修饰:")
    obj = BasicNameMangling()
    obj.show_attributes()
    
    # 尝试直接访问
    print("\n直接访问测试:")
    print(f"公有属性: {obj.public}")
    print(f"保护属性: {obj._protected}")
    
    try:
        print(f"私有属性: {obj.__private}")
    except AttributeError as e:
        print(f"访问私有属性失败: {e}")
    
    # 通过修饰后的名称访问
    print(f"通过修饰名称访问: {obj._BasicNameMangling__private}")
    
    # 2. 查看名称修饰效果
    print("\n2. 名称修饰效果:")
    demo = NameManglingDemo()
    demo.show_all_attributes()
    
    # 3. 继承中的名称修饰
    print("\n3. 继承中的名称修饰:")
    child = Child()
    child.show_inheritance_demo()
    
    # 4. 安全性演示
    print("\n4. 安全性演示:")
    security = SecurityDemo()
    
    # 正常访问
    print(f"密码验证: {security.verify_password('secret123')}")
    
    # 尝试直接访问（会失败）
    try:
        print(f"直接访问密码: {security.__password}")
    except AttributeError:
        print("直接访问私有属性失败（这是好事！）")
    
    # 通过修饰名称访问（仍然可能）
    print(f"通过修饰名称访问: {security._SecurityDemo__password}")
    
    print("\n5. 银行账户实际应用:")
    account = BankAccount("123456789", 1000)
    account.set_pin(1234)
    
    print(f"账户: {account}")
    print(account.get_balance(1234))
    print(account.deposit(500, 1234))
    print(account.withdraw(200, 1234))
    
    # 尝试错误PIN
    print(account.withdraw(100, 9999))
    
    # 查看交易历史
    history = account.get_transaction_history(1234)
    print("\n交易历史:")
    for transaction in history:
        print(f"  {transaction['timestamp']}: {transaction['type']} ¥{transaction['amount']:.2f} (余额: ¥{transaction['balance']:.2f})")


def show_name_mangling_summary():
    """显示名称修饰总结"""
    print("\n" + "=" * 60)
    print("名称修饰机制总结")
    print("=" * 60)
    
    summary = """
名称修饰规则:
1. 以双下划线开头的属性/方法会被修饰
2. 修饰格式: _ClassName__attribute_name
3. 单下划线开头表示保护属性（约定）
4. 双下划线开头和结尾的是特殊方法（不修饰）

优点:
✓ 提供了一定程度的数据隐藏
✓ 避免子类意外覆盖父类私有属性
✓ 减少命名冲突

局限性:
✗ 不是真正的私有（仍可通过修饰名访问）
✗ 主要是约定，不是强制安全机制
✗ 可能使调试变得困难

最佳实践:
1. 使用单下划线表示内部使用的属性
2. 只在确实需要时使用双下划线
3. 提供公有方法访问私有数据
4. 不要依赖名称修饰作为安全机制
5. 优先使用@property装饰器控制访问

记住: Python的哲学是"我们都是成年人"，
名称修饰更多是为了避免意外，而不是强制安全。
    """
    
    print(summary)


if __name__ == "__main__":
    demonstrate_name_mangling()
    show_name_mangling_summary()