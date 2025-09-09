#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
私有属性和访问控制

本文件演示Python中私有属性和访问控制的详细用法：
1. Python中的访问控制概念
2. 命名约定：公有、保护、私有
3. 私有属性的实现机制
4. getter和setter方法
5. property装饰器的使用
6. 访问控制的最佳实践
7. 名称修饰（Name Mangling）
8. 实际应用示例

作者: Python学习助手
日期: 2024
"""

print("=== Python私有属性和访问控制学习 ===")
print()

# 1. Python中的访问控制概念
print("=== 1. Python中的访问控制概念 ===")

class AccessControlDemo:
    """访问控制演示类"""
    
    def __init__(self):
        # 公有属性 - 可以直接访问
        self.public_attr = "这是公有属性"
        
        # 保护属性 - 约定不应该直接访问（单下划线）
        self._protected_attr = "这是保护属性"
        
        # 私有属性 - 强制不能直接访问（双下划线）
        self.__private_attr = "这是私有属性"
        
        print("AccessControlDemo对象创建完成")
    
    def show_attributes(self):
        """显示所有属性"""
        print(f"公有属性: {self.public_attr}")
        print(f"保护属性: {self._protected_attr}")
        print(f"私有属性: {self.__private_attr}")
    
    def _protected_method(self):
        """保护方法 - 约定不应该直接调用"""
        return "这是保护方法的返回值"
    
    def __private_method(self):
        """私有方法 - 不能直接调用"""
        return "这是私有方法的返回值"
    
    def call_private_method(self):
        """公有方法调用私有方法"""
        return self.__private_method()

# 创建对象并测试访问控制
print("创建AccessControlDemo对象:")
obj = AccessControlDemo()
obj.show_attributes()

print("\n测试属性访问:")
# 公有属性 - 可以直接访问
print(f"直接访问公有属性: {obj.public_attr}")

# 保护属性 - 可以访问但不推荐
print(f"直接访问保护属性: {obj._protected_attr}")

# 私有属性 - 不能直接访问
try:
    print(f"尝试直接访问私有属性: {obj.__private_attr}")
except AttributeError as e:
    print(f"访问私有属性失败: {e}")

print("\n测试方法调用:")
# 保护方法 - 可以调用但不推荐
print(f"调用保护方法: {obj._protected_method()}")

# 私有方法 - 不能直接调用
try:
    print(f"尝试直接调用私有方法: {obj.__private_method()}")
except AttributeError as e:
    print(f"调用私有方法失败: {e}")

# 通过公有方法调用私有方法
print(f"通过公有方法调用私有方法: {obj.call_private_method()}")
print()

# 2. 命名约定：公有、保护、私有
print("=== 2. 命名约定：公有、保护、私有 ===")

class NamingConventions:
    """命名约定演示类"""
    
    # 类属性的命名约定
    class_public = "类的公有属性"
    _class_protected = "类的保护属性"
    __class_private = "类的私有属性"
    
    def __init__(self, name):
        # 实例属性的命名约定
        self.name = name  # 公有：任何地方都可以访问
        self._id = id(self)  # 保护：约定仅在类内部和子类中使用
        self.__secret = "secret_key_123"  # 私有：仅在当前类内部使用
        
        # 特殊属性（双下划线开头和结尾）
        self.__version__ = "1.0.0"  # 特殊属性，不会被名称修饰
    
    def public_method(self):
        """公有方法 - 对外提供的接口"""
        return f"公有方法被调用，name={self.name}"
    
    def _protected_method(self):
        """保护方法 - 约定仅供内部和子类使用"""
        return f"保护方法被调用，id={self._id}"
    
    def __private_method(self):
        """私有方法 - 仅供当前类内部使用"""
        return f"私有方法被调用，secret={self.__secret}"
    
    def get_all_info(self):
        """获取所有信息的公有方法"""
        return {
            'public': self.public_method(),
            'protected': self._protected_method(),
            'private': self.__private_method(),
            'version': self.__version__
        }
    
    @classmethod
    def get_class_info(cls):
        """获取类属性信息"""
        return {
            'public': cls.class_public,
            'protected': cls._class_protected,
            # 'private': cls.__class_private,  # 这里无法直接访问
        }

# 测试命名约定
print("创建NamingConventions对象:")
obj2 = NamingConventions("测试对象")

print("\n访问不同类型的属性和方法:")
info = obj2.get_all_info()
for key, value in info.items():
    print(f"{key}: {value}")

print("\n类属性信息:")
class_info = NamingConventions.get_class_info()
for key, value in class_info.items():
    print(f"{key}: {value}")

# 查看对象的所有属性
print("\n对象的所有属性:")
for attr in dir(obj2):
    if not attr.startswith('__') or attr.endswith('__'):
        try:
            value = getattr(obj2, attr)
            if not callable(value):
                print(f"{attr}: {value}")
        except AttributeError:
            print(f"{attr}: 无法访问")
print()

# 3. 私有属性的实现机制
print("=== 3. 私有属性的实现机制 ===")

class PrivateDemo:
    """私有属性实现机制演示"""
    
    def __init__(self):
        self.public = "公有属性"
        self._protected = "保护属性"
        self.__private = "私有属性"
        self.__another_private = "另一个私有属性"
    
    def show_private(self):
        """在类内部访问私有属性"""
        print(f"类内部访问私有属性: {self.__private}")
        print(f"类内部访问另一个私有属性: {self.__another_private}")

# 创建对象并查看名称修饰
print("创建PrivateDemo对象:")
obj3 = PrivateDemo()
obj3.show_private()

print("\n查看对象的所有属性（包括修饰后的名称）:")
for attr in sorted(dir(obj3)):
    if not attr.startswith('_') or attr.startswith('_PrivateDemo__'):
        try:
            value = getattr(obj3, attr)
            if not callable(value):
                print(f"{attr}: {value}")
        except AttributeError:
            print(f"{attr}: 无法访问")

print("\n通过修饰后的名称访问私有属性:")
print(f"obj3._PrivateDemo__private: {obj3._PrivateDemo__private}")
print(f"obj3._PrivateDemo__another_private: {obj3._PrivateDemo__another_private}")

print("\n注意：这种访问方式不推荐使用！")
print()

# 4. getter和setter方法
print("=== 4. getter和setter方法 ===")

class Temperature:
    """温度类 - 演示getter和setter方法"""
    
    def __init__(self, celsius=0):
        """初始化温度（摄氏度）"""
        self.__celsius = 0  # 私有属性
        self.set_celsius(celsius)  # 使用setter设置初始值
    
    def get_celsius(self):
        """获取摄氏温度"""
        return self.__celsius
    
    def set_celsius(self, value):
        """设置摄氏温度"""
        if not isinstance(value, (int, float)):
            raise TypeError("温度必须是数字")
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度(-273.15°C)")
        
        self.__celsius = value
        print(f"温度设置为: {self.__celsius}°C")
    
    def get_fahrenheit(self):
        """获取华氏温度"""
        return self.__celsius * 9/5 + 32
    
    def set_fahrenheit(self, value):
        """设置华氏温度"""
        celsius = (value - 32) * 5/9
        self.set_celsius(celsius)
    
    def get_kelvin(self):
        """获取开尔文温度"""
        return self.__celsius + 273.15
    
    def set_kelvin(self, value):
        """设置开尔文温度"""
        celsius = value - 273.15
        self.set_celsius(celsius)
    
    def __str__(self):
        return f"Temperature({self.__celsius}°C)"

# 测试getter和setter方法
print("创建Temperature对象:")
temp = Temperature(25)

print(f"\n当前温度: {temp}")
print(f"摄氏度: {temp.get_celsius()}°C")
print(f"华氏度: {temp.get_fahrenheit()}°F")
print(f"开尔文: {temp.get_kelvin()}K")

print("\n设置不同单位的温度:")
temp.set_fahrenheit(100)  # 设置为100°F
print(f"设置100°F后，摄氏度: {temp.get_celsius()}°C")

temp.set_kelvin(300)  # 设置为300K
print(f"设置300K后，摄氏度: {temp.get_celsius()}°C")

# 测试异常处理
print("\n测试异常处理:")
try:
    temp.set_celsius(-300)  # 低于绝对零度
except ValueError as e:
    print(f"设置无效温度: {e}")

try:
    temp.set_celsius("热")  # 非数字类型
except TypeError as e:
    print(f"设置无效类型: {e}")
print()

# 5. property装饰器的使用
print("=== 5. property装饰器的使用 ===")

class Circle:
    """圆形类 - 演示property装饰器"""
    
    def __init__(self, radius):
        """初始化圆形"""
        self.__radius = 0
        self.radius = radius  # 使用property setter
    
    @property
    def radius(self):
        """半径属性的getter"""
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        """半径属性的setter"""
        if not isinstance(value, (int, float)):
            raise TypeError("半径必须是数字")
        if value <= 0:
            raise ValueError("半径必须大于0")
        
        self.__radius = value
        print(f"圆形半径设置为: {self.__radius}")
    
    @property
    def diameter(self):
        """直径属性（只读）"""
        return self.__radius * 2
    
    @property
    def area(self):
        """面积属性（只读）"""
        import math
        return math.pi * self.__radius ** 2
    
    @property
    def circumference(self):
        """周长属性（只读）"""
        import math
        return 2 * math.pi * self.__radius
    
    def __str__(self):
        return f"Circle(radius={self.__radius})"

# 测试property装饰器
print("创建Circle对象:")
circle = Circle(5)

print(f"\n圆形信息: {circle}")
print(f"半径: {circle.radius}")
print(f"直径: {circle.diameter}")
print(f"面积: {circle.area:.2f}")
print(f"周长: {circle.circumference:.2f}")

print("\n修改半径:")
circle.radius = 10  # 使用property setter
print(f"新半径: {circle.radius}")
print(f"新面积: {circle.area:.2f}")

# 尝试设置只读属性
print("\n尝试设置只读属性:")
try:
    circle.area = 100  # 尝试设置面积
except AttributeError as e:
    print(f"设置只读属性失败: {e}")

# 测试异常处理
print("\n测试property的异常处理:")
try:
    circle.radius = -5  # 负半径
except ValueError as e:
    print(f"设置无效半径: {e}")
print()

# 6. 访问控制的最佳实践
print("=== 6. 访问控制的最佳实践 ===")

class BankAccount:
    """银行账户类 - 访问控制最佳实践"""
    
    def __init__(self, account_number, owner_name, initial_balance=0):
        """初始化银行账户"""
        # 公有属性 - 对外接口
        self.account_number = account_number
        self.owner_name = owner_name
        
        # 私有属性 - 内部状态
        self.__balance = 0
        self.__transaction_history = []
        self.__is_frozen = False
        
        # 保护属性 - 子类可能需要访问
        self._created_at = None
        self._last_transaction = None
        
        # 使用方法设置初始余额（包含验证）
        if initial_balance > 0:
            self.deposit(initial_balance)
        
        import datetime
        self._created_at = datetime.datetime.now()
        
        print(f"银行账户 {self.account_number} 创建成功")
    
    @property
    def balance(self):
        """余额属性（只读）"""
        return self.__balance
    
    @property
    def is_frozen(self):
        """账户冻结状态（只读）"""
        return self.__is_frozen
    
    @property
    def transaction_count(self):
        """交易次数（只读）"""
        return len(self.__transaction_history)
    
    def deposit(self, amount):
        """存款"""
        if self.__is_frozen:
            raise RuntimeError("账户已冻结，无法进行交易")
        
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("存款金额必须是正数")
        
        self.__balance += amount
        self.__add_transaction("存款", amount)
        print(f"存款成功: +¥{amount}, 余额: ¥{self.__balance}")
    
    def withdraw(self, amount):
        """取款"""
        if self.__is_frozen:
            raise RuntimeError("账户已冻结，无法进行交易")
        
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("取款金额必须是正数")
        
        if amount > self.__balance:
            raise ValueError("余额不足")
        
        self.__balance -= amount
        self.__add_transaction("取款", -amount)
        print(f"取款成功: -¥{amount}, 余额: ¥{self.__balance}")
    
    def freeze_account(self):
        """冻结账户"""
        self.__is_frozen = True
        self.__add_transaction("冻结账户", 0)
        print("账户已冻结")
    
    def unfreeze_account(self):
        """解冻账户"""
        self.__is_frozen = False
        self.__add_transaction("解冻账户", 0)
        print("账户已解冻")
    
    def get_transaction_history(self, limit=None):
        """获取交易历史"""
        history = self.__transaction_history.copy()
        if limit:
            history = history[-limit:]
        return history
    
    def __add_transaction(self, transaction_type, amount):
        """添加交易记录（私有方法）"""
        import datetime
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'balance_after': self.__balance,
            'timestamp': datetime.datetime.now()
        }
        self.__transaction_history.append(transaction)
        self._last_transaction = transaction
    
    def _get_internal_state(self):
        """获取内部状态（保护方法，供子类使用）"""
        return {
            'balance': self.__balance,
            'is_frozen': self.__is_frozen,
            'transaction_count': len(self.__transaction_history),
            'created_at': self._created_at,
            'last_transaction': self._last_transaction
        }
    
    def __str__(self):
        status = "冻结" if self.__is_frozen else "正常"
        return f"BankAccount({self.account_number}, {self.owner_name}, ¥{self.__balance}, {status})"

# 测试银行账户类
print("创建银行账户:")
account = BankAccount("6222001234567890", "张三", 1000)

print(f"\n账户信息: {account}")
print(f"余额: ¥{account.balance}")
print(f"交易次数: {account.transaction_count}")

print("\n进行交易:")
account.deposit(500)
account.withdraw(200)
account.deposit(100)

print(f"\n交易后余额: ¥{account.balance}")
print(f"交易次数: {account.transaction_count}")

print("\n最近3笔交易:")
for i, transaction in enumerate(account.get_transaction_history(3), 1):
    print(f"{i}. {transaction['type']}: ¥{transaction['amount']}, "
          f"余额: ¥{transaction['balance_after']}, "
          f"时间: {transaction['timestamp'].strftime('%H:%M:%S')}")

print("\n测试账户冻结:")
account.freeze_account()
print(f"冻结状态: {account.is_frozen}")

try:
    account.withdraw(100)  # 尝试在冻结状态下取款
except RuntimeError as e:
    print(f"冻结状态下取款失败: {e}")

account.unfreeze_account()
print(f"解冻后状态: {account.is_frozen}")
print()

# 7. 名称修饰（Name Mangling）
print("=== 7. 名称修饰（Name Mangling） ===")

class Parent:
    """父类 - 演示名称修饰"""
    
    def __init__(self):
        self.public = "父类公有属性"
        self._protected = "父类保护属性"
        self.__private = "父类私有属性"
    
    def show_parent_private(self):
        """显示父类私有属性"""
        print(f"父类私有属性: {self.__private}")
    
    def __parent_private_method(self):
        """父类私有方法"""
        return "父类私有方法被调用"
    
    def call_parent_private(self):
        """调用父类私有方法"""
        return self.__parent_private_method()

class Child(Parent):
    """子类 - 演示名称修饰的继承行为"""
    
    def __init__(self):
        super().__init__()
        self.child_public = "子类公有属性"
        self._child_protected = "子类保护属性"
        self.__child_private = "子类私有属性"
    
    def show_child_private(self):
        """显示子类私有属性"""
        print(f"子类私有属性: {self.__child_private}")
    
    def show_inherited_attributes(self):
        """显示继承的属性"""
        print(f"继承的公有属性: {self.public}")
        print(f"继承的保护属性: {self._protected}")
        
        # 尝试访问父类私有属性（会失败）
        try:
            print(f"尝试访问父类私有属性: {self.__private}")
        except AttributeError as e:
            print(f"无法访问父类私有属性: {e}")
    
    def __child_private_method(self):
        """子类私有方法"""
        return "子类私有方法被调用"
    
    def call_child_private(self):
        """调用子类私有方法"""
        return self.__child_private_method()

# 测试名称修饰
print("创建Child对象:")
child = Child()

print("\n显示各类属性:")
child.show_parent_private()
child.show_child_private()
child.show_inherited_attributes()

print("\n调用私有方法:")
print(child.call_parent_private())
print(child.call_child_private())

print("\n查看名称修饰后的属性:")
for attr in sorted(dir(child)):
    if '__private' in attr or '__child_private' in attr:
        try:
            value = getattr(child, attr)
            if not callable(value):
                print(f"{attr}: {value}")
        except AttributeError:
            print(f"{attr}: 无法访问")

print("\n通过修饰后的名称访问:")
print(f"父类私有属性: {child._Parent__private}")
print(f"子类私有属性: {child._Child__child_private}")
print()

# 8. 实际应用示例
print("=== 8. 实际应用示例 ===")

class User:
    """用户类 - 综合应用示例"""
    
    # 类属性
    _user_count = 0
    __max_login_attempts = 3
    
    def __init__(self, username, email, password):
        """初始化用户"""
        # 验证输入
        self.__validate_username(username)
        self.__validate_email(email)
        self.__validate_password(password)
        
        # 公有属性
        self.username = username
        self.email = email
        
        # 私有属性
        self.__password_hash = self.__hash_password(password)
        self.__login_attempts = 0
        self.__is_locked = False
        self.__is_active = True
        
        # 保护属性
        self._user_id = User._user_count + 1
        self._created_at = None
        self._last_login = None
        
        # 更新用户计数
        User._user_count += 1
        
        import datetime
        self._created_at = datetime.datetime.now()
        
        print(f"用户 {self.username} 创建成功，ID: {self._user_id}")
    
    @property
    def user_id(self):
        """用户ID（只读）"""
        return self._user_id
    
    @property
    def is_active(self):
        """用户激活状态（只读）"""
        return self.__is_active
    
    @property
    def is_locked(self):
        """用户锁定状态（只读）"""
        return self.__is_locked
    
    @property
    def login_attempts(self):
        """登录尝试次数（只读）"""
        return self.__login_attempts
    
    def change_password(self, old_password, new_password):
        """修改密码"""
        if not self.__verify_password(old_password):
            raise ValueError("原密码错误")
        
        self.__validate_password(new_password)
        self.__password_hash = self.__hash_password(new_password)
        print("密码修改成功")
    
    def login(self, password):
        """用户登录"""
        if self.__is_locked:
            raise RuntimeError("账户已锁定，请联系管理员")
        
        if not self.__is_active:
            raise RuntimeError("账户未激活")
        
        if self.__verify_password(password):
            self.__login_attempts = 0
            import datetime
            self._last_login = datetime.datetime.now()
            print(f"用户 {self.username} 登录成功")
            return True
        else:
            self.__login_attempts += 1
            print(f"密码错误，剩余尝试次数: {User.__max_login_attempts - self.__login_attempts}")
            
            if self.__login_attempts >= User.__max_login_attempts:
                self.__is_locked = True
                print("账户已锁定")
            
            return False
    
    def deactivate(self):
        """停用账户"""
        self.__is_active = False
        print(f"用户 {self.username} 已停用")
    
    def activate(self):
        """激活账户"""
        self.__is_active = True
        print(f"用户 {self.username} 已激活")
    
    def unlock(self):
        """解锁账户（管理员功能）"""
        self.__is_locked = False
        self.__login_attempts = 0
        print(f"用户 {self.username} 已解锁")
    
    @staticmethod
    def __validate_username(username):
        """验证用户名"""
        if not isinstance(username, str) or len(username) < 3:
            raise ValueError("用户名至少3个字符")
        if not username.isalnum():
            raise ValueError("用户名只能包含字母和数字")
    
    @staticmethod
    def __validate_email(email):
        """验证邮箱"""
        if not isinstance(email, str) or '@' not in email:
            raise ValueError("邮箱格式无效")
    
    @staticmethod
    def __validate_password(password):
        """验证密码"""
        if not isinstance(password, str) or len(password) < 6:
            raise ValueError("密码至少6个字符")
    
    @staticmethod
    def __hash_password(password):
        """密码哈希（简化版）"""
        return f"hashed_{hash(password)}"
    
    def __verify_password(self, password):
        """验证密码"""
        return self.__password_hash == self.__hash_password(password)
    
    @classmethod
    def get_user_count(cls):
        """获取用户总数"""
        return cls._user_count
    
    def get_user_info(self):
        """获取用户信息"""
        return {
            'user_id': self._user_id,
            'username': self.username,
            'email': self.email,
            'is_active': self.__is_active,
            'is_locked': self.__is_locked,
            'login_attempts': self.__login_attempts,
            'created_at': self._created_at.strftime('%Y-%m-%d %H:%M:%S') if self._created_at else None,
            'last_login': self._last_login.strftime('%Y-%m-%d %H:%M:%S') if self._last_login else None
        }
    
    def __str__(self):
        status = []
        if not self.__is_active:
            status.append("未激活")
        if self.__is_locked:
            status.append("已锁定")
        status_str = f" ({', '.join(status)})" if status else ""
        return f"User({self.username}, {self.email}){status_str}"

# 测试用户类
print("创建用户:")
user1 = User("alice", "alice@example.com", "password123")
user2 = User("bob", "bob@example.com", "secret456")

print(f"\n用户总数: {User.get_user_count()}")
print(f"user1: {user1}")
print(f"user2: {user2}")

print("\n用户登录测试:")
# 正确密码登录
user1.login("password123")

# 错误密码登录
print("\n错误密码登录测试:")
for i in range(4):  # 尝试4次错误密码
    try:
        result = user1.login("wrong_password")
        if not result:
            print(f"第{i+1}次登录失败")
    except RuntimeError as e:
        print(f"第{i+1}次登录异常: {e}")
        break

print(f"\n用户状态: {user1}")
print(f"登录尝试次数: {user1.login_attempts}")
print(f"是否锁定: {user1.is_locked}")

# 解锁用户
print("\n解锁用户:")
user1.unlock()
print(f"解锁后状态: {user1}")

# 修改密码
print("\n修改密码:")
user1.change_password("password123", "new_password789")
user1.login("new_password789")

print("\n用户详细信息:")
for key, value in user1.get_user_info().items():
    print(f"{key}: {value}")

print()
print("=== 学习要点总结 ===")
print()
print("私有属性和访问控制的关键要点：")
print("1. Python使用命名约定来表示访问级别")
print("2. 单下划线(_)表示保护属性，约定不直接访问")
print("3. 双下划线(__)表示私有属性，会进行名称修饰")
print("4. 使用getter/setter方法控制属性访问")
print("5. property装饰器提供更优雅的属性访问方式")
print("6. 名称修饰确保私有属性在继承中的独立性")
print("7. 访问控制是为了封装和数据保护")
print("8. 合理的访问控制提高代码的可维护性")
print()
print("=== 程序执行完成 ===")
print("恭喜！你已经学会了Python私有属性和访问控制。")
print("下一步：学习类属性和类方法。")