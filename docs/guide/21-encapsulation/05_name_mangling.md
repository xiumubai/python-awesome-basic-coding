# 名称修饰机制

名称修饰（Name Mangling）是Python中一种特殊的机制，用于实现更强的封装。当类中的属性或方法名以双下划线开头时，Python会自动对其进行名称修饰，使其在类外部更难被直接访问。

## 名称修饰的基本概念

- **触发条件**：属性或方法名以双下划线（__）开头，但不以双下划线结尾
- **修饰规则**：`__attribute` 会被修饰为 `_ClassName__attribute`
- **目的**：提供更强的封装，防止意外的属性访问和子类中的名称冲突
- **注意**：这不是真正的私有化，仍然可以通过修饰后的名称访问

## 基本名称修饰示例

### 1. 基本的名称修饰

```python
class BasicExample:
    """基本名称修饰示例"""
    
    def __init__(self):
        self.public_attr = "公有属性"          # 公有属性
        self._protected_attr = "保护属性"       # 保护属性（约定）
        self.__private_attr = "私有属性"        # 私有属性（名称修饰）
    
    def public_method(self):
        """公有方法"""
        return "这是公有方法"
    
    def _protected_method(self):
        """保护方法（约定）"""
        return "这是保护方法"
    
    def __private_method(self):
        """私有方法（名称修饰）"""
        return "这是私有方法"
    
    def access_private(self):
        """在类内部访问私有属性和方法"""
        return {
            "私有属性": self.__private_attr,
            "私有方法结果": self.__private_method()
        }
    
    def show_all_attributes(self):
        """显示所有属性"""
        print("类内部可以访问所有属性:")
        print(f"  公有属性: {self.public_attr}")
        print(f"  保护属性: {self._protected_attr}")
        print(f"  私有属性: {self.__private_attr}")

# 演示基本名称修饰
def demonstrate_basic_name_mangling():
    """演示基本名称修饰"""
    print("=== 基本名称修饰演示 ===")
    
    obj = BasicExample()
    
    # 访问公有属性和方法
    print("\n1. 访问公有成员:")
    print(f"公有属性: {obj.public_attr}")
    print(f"公有方法: {obj.public_method()}")
    
    # 访问保护属性和方法（可以访问，但不推荐）
    print("\n2. 访问保护成员:")
    print(f"保护属性: {obj._protected_attr}")
    print(f"保护方法: {obj._protected_method()}")
    
    # 尝试访问私有属性和方法（会失败）
    print("\n3. 尝试直接访问私有成员:")
    try:
        print(obj.__private_attr)
    except AttributeError as e:
        print(f"访问私有属性失败: {e}")
    
    try:
        print(obj.__private_method())
    except AttributeError as e:
        print(f"访问私有方法失败: {e}")
    
    # 在类内部访问私有成员
    print("\n4. 通过类内部方法访问私有成员:")
    private_data = obj.access_private()
    for key, value in private_data.items():
        print(f"  {key}: {value}")
    
    # 显示所有属性
    print("\n5. 类内部访问:")
    obj.show_all_attributes()

# 运行演示
demonstrate_basic_name_mangling()
```

### 2. 名称修饰的实际效果

```python
class NameManglingDemo:
    """名称修饰机制演示"""
    
    def __init__(self):
        self.__secret = "这是秘密数据"
        self.__count = 0
    
    def __secret_method(self):
        """私有方法"""
        self.__count += 1
        return f"秘密方法被调用了 {self.__count} 次"
    
    def get_secret_info(self):
        """获取秘密信息"""
        return {
            "秘密数据": self.__secret,
            "调用结果": self.__secret_method()
        }
    
    def show_actual_attributes(self):
        """显示实际的属性名称"""
        print("\n对象的实际属性:")
        for attr in dir(self):
            if not attr.startswith('__') or attr.endswith('__'):
                continue
            print(f"  {attr}")

# 演示名称修饰的实际效果
def demonstrate_actual_name_mangling():
    """演示名称修饰的实际效果"""
    print("\n=== 名称修饰的实际效果演示 ===")
    
    obj = NameManglingDemo()
    
    # 查看对象的所有属性
    print("\n1. 对象的所有属性:")
    all_attrs = [attr for attr in dir(obj) if not attr.startswith('_NameManglingDemo__') and not attr.startswith('__')]
    private_attrs = [attr for attr in dir(obj) if attr.startswith('_NameManglingDemo__')]
    
    print("普通属性和方法:")
    for attr in all_attrs:
        print(f"  {attr}")
    
    print("\n修饰后的私有属性和方法:")
    for attr in private_attrs:
        print(f"  {attr}")
    
    # 通过修饰后的名称访问私有成员
    print("\n2. 通过修饰后的名称访问:")
    print(f"私有属性: {obj._NameManglingDemo__secret}")
    print(f"私有方法: {obj._NameManglingDemo__secret_method()}")
    
    # 正常的类内部访问
    print("\n3. 正常的类内部访问:")
    secret_info = obj.get_secret_info()
    for key, value in secret_info.items():
        print(f"  {key}: {value}")
    
    # 显示实际属性
    obj.show_actual_attributes()

# 运行演示
demonstrate_actual_name_mangling()
```

### 3. 继承中的名称修饰

```python
class Parent:
    """父类"""
    
    def __init__(self):
        self.public_data = "父类公有数据"
        self._protected_data = "父类保护数据"
        self.__private_data = "父类私有数据"
    
    def public_method(self):
        return "父类公有方法"
    
    def _protected_method(self):
        return "父类保护方法"
    
    def __private_method(self):
        return "父类私有方法"
    
    def access_own_private(self):
        """访问自己的私有成员"""
        return {
            "私有数据": self.__private_data,
            "私有方法": self.__private_method()
        }
    
    def show_parent_info(self):
        """显示父类信息"""
        print("父类内部访问:")
        print(f"  公有数据: {self.public_data}")
        print(f"  保护数据: {self._protected_data}")
        print(f"  私有数据: {self.__private_data}")

class Child(Parent):
    """子类"""
    
    def __init__(self):
        super().__init__()
        self.child_public = "子类公有数据"
        self._child_protected = "子类保护数据"
        self.__child_private = "子类私有数据"  # 会被修饰为 _Child__child_private
    
    def child_method(self):
        return "子类方法"
    
    def __child_private_method(self):
        return "子类私有方法"
    
    def access_inherited(self):
        """访问继承的成员"""
        result = {
            "可访问的公有数据": self.public_data,
            "可访问的保护数据": self._protected_data,
            "可访问的公有方法": self.public_method(),
            "可访问的保护方法": self._protected_method()
        }
        
        # 尝试访问父类的私有成员（会失败）
        try:
            result["父类私有数据"] = self.__private_data
        except AttributeError:
            result["父类私有数据"] = "无法访问（名称修饰）"
        
        try:
            result["父类私有方法"] = self.__private_method()
        except AttributeError:
            result["父类私有方法"] = "无法访问（名称修饰）"
        
        return result
    
    def access_own_private(self):
        """访问自己的私有成员"""
        return {
            "子类私有数据": self.__child_private,
            "子类私有方法": self.__child_private_method()
        }
    
    def show_all_accessible(self):
        """显示所有可访问的成员"""
        print("\n子类中可访问的成员:")
        print(f"  继承的公有数据: {self.public_data}")
        print(f"  继承的保护数据: {self._protected_data}")
        print(f"  自己的公有数据: {self.child_public}")
        print(f"  自己的保护数据: {self._child_protected}")
        print(f"  自己的私有数据: {self.__child_private}")
        
        # 尝试访问父类私有数据
        try:
            print(f"  父类私有数据: {self.__private_data}")
        except AttributeError:
            print("  父类私有数据: 无法访问（名称修饰保护）")
    
    def show_mangled_names(self):
        """显示修饰后的名称"""
        print("\n修饰后的属性名称:")
        for attr in dir(self):
            if '_Parent__' in attr or '_Child__' in attr:
                print(f"  {attr}")

# 演示继承中的名称修饰
def demonstrate_inheritance_name_mangling():
    """演示继承中的名称修饰"""
    print("\n=== 继承中的名称修饰演示 ===")
    
    child = Child()
    
    # 显示子类可访问的成员
    child.show_all_accessible()
    
    # 显示修饰后的名称
    child.show_mangled_names()
    
    # 访问继承的成员
    print("\n子类访问继承成员的结果:")
    inherited_access = child.access_inherited()
    for key, value in inherited_access.items():
        print(f"  {key}: {value}")
    
    # 访问自己的私有成员
    print("\n子类访问自己私有成员的结果:")
    own_private = child.access_own_private()
    for key, value in own_private.items():
        print(f"  {key}: {value}")
    
    # 通过修饰后的名称访问父类私有成员
    print("\n通过修饰后名称访问父类私有成员:")
    print(f"父类私有数据: {child._Parent__private_data}")
    print(f"父类私有方法: {child._Parent__private_method()}")
    
    # 父类访问自己的私有成员
    print("\n父类访问自己的私有成员:")
    parent_private = child.access_own_private()  # 这是父类的方法
    for key, value in parent_private.items():
        print(f"  {key}: {value}")

# 运行演示
demonstrate_inheritance_name_mangling()
```

### 4. 绕过名称修饰的方法

```python
class SecretClass:
    """包含秘密数据的类"""
    
    def __init__(self):
        self.__secret_key = "top_secret_123"
        self.__secret_data = {"password": "admin123", "token": "abc123xyz"}
        self.__secret_count = 0
    
    def __secret_operation(self):
        """秘密操作"""
        self.__secret_count += 1
        return f"秘密操作执行了 {self.__secret_count} 次"
    
    def get_public_info(self):
        """获取公开信息"""
        return "这是公开信息"
    
    def _get_protected_info(self):
        """获取保护信息"""
        return "这是保护信息"

# 演示绕过名称修饰的各种方法
def demonstrate_bypassing_name_mangling():
    """演示绕过名称修饰的方法"""
    print("\n=== 绕过名称修饰的方法演示 ===")
    
    obj = SecretClass()
    
    print("\n1. 正常访问（会失败）:")
    try:
        print(obj.__secret_key)
    except AttributeError as e:
        print(f"直接访问失败: {e}")
    
    print("\n2. 通过dir()查看所有属性:")
    all_attrs = dir(obj)
    secret_attrs = [attr for attr in all_attrs if 'secret' in attr.lower()]
    print("包含'secret'的属性:")
    for attr in secret_attrs:
        print(f"  {attr}")
    
    print("\n3. 通过修饰后的名称访问:")
    print(f"秘密密钥: {obj._SecretClass__secret_key}")
    print(f"秘密数据: {obj._SecretClass__secret_data}")
    print(f"秘密操作: {obj._SecretClass__secret_operation()}")
    
    print("\n4. 通过getattr()访问:")
    secret_key = getattr(obj, '_SecretClass__secret_key')
    print(f"通过getattr获取秘密密钥: {secret_key}")
    
    print("\n5. 通过__dict__访问:")
    print("对象的__dict__内容:")
    for key, value in obj.__dict__.items():
        print(f"  {key}: {value}")
    
    print("\n6. 动态修改私有属性:")
    setattr(obj, '_SecretClass__secret_key', 'new_secret_456')
    print(f"修改后的秘密密钥: {obj._SecretClass__secret_key}")
    
    print("\n7. 使用vars()函数:")
    obj_vars = vars(obj)
    for key, value in obj_vars.items():
        if 'secret' in key.lower():
            print(f"  {key}: {value}")
    
    print("\n8. 反射机制访问:")
    import inspect
    members = inspect.getmembers(obj)
    secret_members = [(name, value) for name, value in members if 'secret' in name.lower()]
    print("通过反射找到的秘密成员:")
    for name, value in secret_members:
        print(f"  {name}: {type(value)}")

# 运行演示
demonstrate_bypassing_name_mangling()
```

### 5. 银行账户系统中的名称修饰应用

```python
class SecureBankAccount:
    """安全银行账户 - 使用名称修饰保护敏感数据"""
    
    def __init__(self, account_number, pin, initial_balance=0):
        # 公有信息
        self.account_number = account_number
        self.creation_date = self.__get_current_time()
        
        # 保护信息（约定私有）
        self._balance = 0
        self._transaction_history = []
        
        # 高度敏感信息（名称修饰保护）
        self.__pin = pin
        self.__security_key = self.__generate_security_key()
        self.__failed_attempts = 0
        self.__is_locked = False
        self.__last_access_time = self.__get_current_time()
        
        # 初始化余额
        if initial_balance > 0:
            self._add_transaction("初始存款", 0, initial_balance)
            self._balance = initial_balance
    
    def __get_current_time(self):
        """获取当前时间（私有方法）"""
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __generate_security_key(self):
        """生成安全密钥（私有方法）"""
        import hashlib
        import random
        data = f"{self.account_number}_{random.randint(1000, 9999)}"
        return hashlib.md5(data.encode()).hexdigest()[:16]
    
    def __verify_pin(self, pin):
        """验证PIN码（私有方法）"""
        if self.__is_locked:
            raise RuntimeError("账户已被锁定，请联系银行")
        
        if pin != self.__pin:
            self.__failed_attempts += 1
            if self.__failed_attempts >= 3:
                self.__is_locked = True
                raise RuntimeError("PIN码错误次数过多，账户已被锁定")
            raise ValueError(f"PIN码错误，剩余尝试次数: {3 - self.__failed_attempts}")
        
        # PIN验证成功，重置失败次数
        self.__failed_attempts = 0
        self.__last_access_time = self.__get_current_time()
    
    def __log_security_event(self, event):
        """记录安全事件（私有方法）"""
        timestamp = self.__get_current_time()
        print(f"[安全日志 {timestamp}] {event}")
    
    def _add_transaction(self, description, old_balance, new_balance):
        """添加交易记录（保护方法）"""
        transaction = {
            "时间": self.__get_current_time(),
            "描述": description,
            "原余额": old_balance,
            "新余额": new_balance,
            "变动": new_balance - old_balance
        }
        self._transaction_history.append(transaction)
    
    def get_balance(self, pin):
        """获取余额（需要PIN验证）"""
        self.__verify_pin(pin)
        self.__log_security_event(f"余额查询 - 账户: {self.account_number}")
        return self._balance
    
    def deposit(self, amount, pin):
        """存款（需要PIN验证）"""
        self.__verify_pin(pin)
        
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        
        old_balance = self._balance
        self._balance += amount
        self._add_transaction(f"存款 {amount}", old_balance, self._balance)
        
        self.__log_security_event(f"存款操作 - 账户: {self.account_number}, 金额: {amount}")
        return f"存款成功，当前余额: {self._balance}"
    
    def withdraw(self, amount, pin):
        """取款（需要PIN验证）"""
        self.__verify_pin(pin)
        
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        
        if amount > self._balance:
            raise ValueError("余额不足")
        
        old_balance = self._balance
        self._balance -= amount
        self._add_transaction(f"取款 {amount}", old_balance, self._balance)
        
        self.__log_security_event(f"取款操作 - 账户: {self.account_number}, 金额: {amount}")
        return f"取款成功，当前余额: {self._balance}"
    
    def change_pin(self, old_pin, new_pin):
        """修改PIN码"""
        self.__verify_pin(old_pin)
        
        if len(str(new_pin)) != 4 or not str(new_pin).isdigit():
            raise ValueError("新PIN码必须是4位数字")
        
        self.__pin = new_pin
        self.__log_security_event(f"PIN码修改 - 账户: {self.account_number}")
        return "PIN码修改成功"
    
    def get_transaction_history(self, pin, limit=5):
        """获取交易历史（需要PIN验证）"""
        self.__verify_pin(pin)
        self.__log_security_event(f"交易历史查询 - 账户: {self.account_number}")
        return self._transaction_history[-limit:]
    
    def get_account_info(self, pin):
        """获取账户信息（需要PIN验证）"""
        self.__verify_pin(pin)
        return {
            "账户号码": self.account_number,
            "创建日期": self.creation_date,
            "余额": self._balance,
            "交易次数": len(self._transaction_history),
            "最后访问时间": self.__last_access_time,
            "账户状态": "正常" if not self.__is_locked else "已锁定"
        }
    
    def unlock_account(self, security_key):
        """解锁账户（需要安全密钥）"""
        if security_key != self.__security_key:
            raise ValueError("安全密钥错误")
        
        self.__is_locked = False
        self.__failed_attempts = 0
        self.__log_security_event(f"账户解锁 - 账户: {self.account_number}")
        return "账户解锁成功"
    
    def get_security_key(self, pin):
        """获取安全密钥（紧急情况使用）"""
        self.__verify_pin(pin)
        self.__log_security_event(f"安全密钥获取 - 账户: {self.account_number}")
        return self.__security_key
    
    def __str__(self):
        status = "正常" if not self.__is_locked else "已锁定"
        return f"银行账户 {self.account_number} ({status})"

# 演示银行账户系统中的名称修饰
def demonstrate_bank_account_name_mangling():
    """演示银行账户系统中的名称修饰应用"""
    print("\n=== 银行账户系统名称修饰应用演示 ===")
    
    # 创建账户
    account = SecureBankAccount("123456789", 1234, 1000)
    print(f"创建账户: {account}")
    
    # 正常操作
    print("\n1. 正常银行操作:")
    print(f"余额查询: {account.get_balance(1234)}")
    print(account.deposit(500, 1234))
    print(account.withdraw(200, 1234))
    
    # 查看账户信息
    print("\n2. 账户信息:")
    info = account.get_account_info(1234)
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    # 尝试错误的PIN
    print("\n3. PIN码错误测试:")
    try:
        account.get_balance(9999)
    except ValueError as e:
        print(f"PIN错误: {e}")
    
    try:
        account.get_balance(8888)
    except ValueError as e:
        print(f"PIN错误: {e}")
    
    try:
        account.get_balance(7777)  # 第三次错误，会锁定账户
    except RuntimeError as e:
        print(f"账户锁定: {e}")
    
    # 尝试在锁定状态下操作
    print("\n4. 锁定状态下的操作:")
    try:
        account.get_balance(1234)  # 即使PIN正确也无法访问
    except RuntimeError as e:
        print(f"锁定状态访问: {e}")
    
    # 获取安全密钥并解锁（这里我们需要绕过名称修饰来演示）
    print("\n5. 紧急解锁:")
    # 在实际应用中，安全密钥应该通过其他安全渠道获取
    security_key = getattr(account, '_SecureBankAccount__security_key')
    print(f"安全密钥: {security_key}")
    print(account.unlock_account(security_key))
    
    # 解锁后正常操作
    print("\n6. 解锁后操作:")
    print(f"余额查询: {account.get_balance(1234)}")
    
    # 修改PIN码
    print("\n7. 修改PIN码:")
    print(account.change_pin(1234, 5678))
    print(f"新PIN码余额查询: {account.get_balance(5678)}")
    
    # 查看交易历史
    print("\n8. 交易历史:")
    history = account.get_transaction_history(5678, 3)
    for transaction in history:
        print(f"  {transaction['时间']} - {transaction['描述']} (余额: {transaction['原余额']} → {transaction['新余额']})")
    
    # 显示名称修饰的保护效果
    print("\n9. 名称修饰保护效果:")
    print("尝试直接访问敏感数据:")
    try:
        print(account.__pin)
    except AttributeError:
        print("  无法直接访问 __pin")
    
    try:
        print(account.__security_key)
    except AttributeError:
        print("  无法直接访问 __security_key")
    
    print("\n但仍可通过修饰后的名称访问（需要知道类名）:")
    print(f"  PIN码: {account._SecureBankAccount__pin}")
    print(f"  安全密钥: {account._SecureBankAccount__security_key}")
    print(f"  失败次数: {account._SecureBankAccount__failed_attempts}")
    print(f"  锁定状态: {account._SecureBankAccount__is_locked}")

# 运行演示
demonstrate_bank_account_name_mangling()
```

## 名称修饰的总结

```python
def demonstrate_name_mangling_summary():
    """名称修饰机制总结"""
    print("\n=== 名称修饰机制总结 ===")
    
    print("\n1. 名称修饰规则:")
    print("   - 以双下划线开头，不以双下划线结尾的属性/方法")
    print("   - __attribute → _ClassName__attribute")
    print("   - 只在类定义内部进行修饰")
    
    print("\n2. 名称修饰的优点:")
    print("   - 防止意外的属性访问")
    print("   - 避免子类中的名称冲突")
    print("   - 提供更强的封装保护")
    print("   - 清楚地表明设计意图")
    
    print("\n3. 名称修饰的局限性:")
    print("   - 不是真正的私有化")
    print("   - 仍可通过修饰后的名称访问")
    print("   - 可以通过反射机制绕过")
    print("   - 主要依赖开发者的自觉性")
    
    print("\n4. 最佳实践:")
    print("   - 用于真正需要隐藏的内部实现")
    print("   - 避免在子类中意外覆盖")
    print("   - 保护敏感数据和关键算法")
    print("   - 配合其他安全措施使用")
    
    print("\n5. 使用场景:")
    print("   - 框架和库的内部实现")
    print("   - 敏感数据的保护")
    print("   - 避免继承中的名称冲突")
    print("   - 实现设计模式中的私有成员")
    
    print("\n6. 注意事项:")
    print("   - 不要过度使用")
    print("   - 文档化私有接口的用途")
    print("   - 考虑使用单下划线作为约定")
    print("   - 测试时可能需要访问私有成员")

# 运行总结
demonstrate_name_mangling_summary()
```

## 学习要点

### 名称修饰的工作原理

1. **触发条件**：`__attribute`（双下划线开头，非双下划线结尾）
2. **修饰规则**：`__attribute` → `_ClassName__attribute`
3. **作用范围**：只在类定义内部生效
4. **继承行为**：每个类的私有属性独立修饰

### 与其他访问控制的比较

| 类型 | 语法 | 保护级别 | 继承访问 | 外部访问 |
|------|------|----------|----------|----------|
| 公有 | `attribute` | 无保护 | 可访问 | 可访问 |
| 保护 | `_attribute` | 约定保护 | 可访问 | 不推荐 |
| 私有 | `__attribute` | 名称修饰 | 不可直接访问 | 需要修饰名 |

### 实际应用建议

1. **适度使用**：不要过度依赖名称修饰
2. **明确意图**：用于真正需要隐藏的实现细节
3. **文档化**：清楚地说明私有成员的用途
4. **测试考虑**：测试代码可能需要访问私有成员
5. **安全意识**：名称修饰不是安全机制，只是封装工具

### 常见误区

- **不是安全机制**：仍可通过修饰后的名称访问
- **不是绝对私有**：Python没有真正的私有成员
- **不要滥用**：简单的内部属性使用单下划线即可
- **继承复杂性**：在复杂继承结构中要小心使用

名称修饰是Python提供的一种封装机制，虽然不是绝对的私有化，但在适当的场景下能够有效地保护内部实现，防止意外访问和名称冲突。正确理解和使用名称修饰，可以编写出更加健壮和可维护的代码。