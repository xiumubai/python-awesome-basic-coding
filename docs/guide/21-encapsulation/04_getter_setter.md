# Getter和Setter方法

Getter和Setter方法是面向对象编程中控制属性访问的传统方式。虽然Python提供了@property装饰器这种更优雅的方式，但理解传统的getter/setter方法仍然很重要，特别是在与其他编程语言交互或维护遗留代码时。

## Getter和Setter的基本概念

- **Getter方法**：用于获取私有属性的值
- **Setter方法**：用于设置私有属性的值
- **目的**：提供对私有属性的受控访问
- **优势**：可以在获取和设置时添加验证、日志、计算等逻辑

## 传统的Getter/Setter实现

### 1. 基本的Getter/Setter

```python
class Student:
    """学生类 - 传统getter/setter实现"""
    
    def __init__(self, name, age, grade):
        self._name = name
        self._age = age
        self._grade = grade
    
    # Getter方法
    def get_name(self):
        """获取学生姓名"""
        return self._name
    
    def get_age(self):
        """获取学生年龄"""
        return self._age
    
    def get_grade(self):
        """获取学生年级"""
        return self._grade
    
    # Setter方法
    def set_name(self, name):
        """设置学生姓名"""
        if not isinstance(name, str):
            raise TypeError("姓名必须是字符串")
        if len(name.strip()) == 0:
            raise ValueError("姓名不能为空")
        self._name = name.strip().title()
    
    def set_age(self, age):
        """设置学生年龄"""
        if not isinstance(age, int):
            raise TypeError("年龄必须是整数")
        if age < 5 or age > 25:
            raise ValueError("学生年龄必须在5-25岁之间")
        self._age = age
    
    def set_grade(self, grade):
        """设置学生年级"""
        if not isinstance(grade, int):
            raise TypeError("年级必须是整数")
        if grade < 1 or grade > 12:
            raise ValueError("年级必须在1-12之间")
        self._grade = grade
    
    # 计算属性的getter
    def get_age_group(self):
        """获取年龄组"""
        if self._age <= 12:
            return "小学生"
        elif self._age <= 15:
            return "初中生"
        elif self._age <= 18:
            return "高中生"
        else:
            return "大学生"
    
    def get_info(self):
        """获取学生完整信息"""
        return {
            "姓名": self.get_name(),
            "年龄": self.get_age(),
            "年级": self.get_grade(),
            "年龄组": self.get_age_group()
        }
    
    def __str__(self):
        return f"{self.get_name()}({self.get_age()}岁, {self.get_grade()}年级, {self.get_age_group()})"

# 使用示例
def demonstrate_traditional_getters_setters():
    """演示传统的getter/setter方法"""
    print("=== 传统Getter/Setter演示 ===")
    
    # 创建学生对象
    student = Student("john doe", 16, 10)
    print(f"初始信息: {student}")
    
    # 使用getter获取信息
    print(f"\n使用getter获取信息:")
    print(f"姓名: {student.get_name()}")
    print(f"年龄: {student.get_age()}")
    print(f"年级: {student.get_grade()}")
    print(f"年龄组: {student.get_age_group()}")
    
    # 使用setter修改信息
    print(f"\n使用setter修改信息:")
    student.set_name("  alice smith  ")
    student.set_age(14)
    student.set_grade(8)
    print(f"修改后: {student}")
    
    # 验证错误处理
    print(f"\n验证错误处理:")
    try:
        student.set_age(30)
    except ValueError as e:
        print(f"年龄验证错误: {e}")
    
    try:
        student.set_grade(15)
    except ValueError as e:
        print(f"年级验证错误: {e}")
    
    # 显示完整信息
    print(f"\n完整信息:")
    for key, value in student.get_info().items():
        print(f"  {key}: {value}")

# 运行演示
demonstrate_traditional_getters_setters()
```

### 2. 带有业务逻辑的Getter/Setter

```python
class BankAccount:
    """银行账户类 - 带业务逻辑的getter/setter"""
    
    def __init__(self, account_number, initial_balance=0):
        self._account_number = account_number
        self._balance = 0
        self._transaction_history = []
        self._is_active = True
        
        # 使用setter进行初始化
        self.set_balance(initial_balance, "初始存款")
    
    # Getter方法
    def get_account_number(self):
        """获取账户号码"""
        return self._account_number
    
    def get_balance(self):
        """获取账户余额"""
        if not self._is_active:
            raise RuntimeError("账户已被冻结")
        return self._balance
    
    def get_transaction_history(self):
        """获取交易历史"""
        return self._transaction_history.copy()  # 返回副本，防止外部修改
    
    def get_is_active(self):
        """获取账户状态"""
        return self._is_active
    
    def get_account_type(self):
        """获取账户类型（基于余额）"""
        balance = self._balance
        if balance >= 100000:
            return "VIP账户"
        elif balance >= 10000:
            return "金卡账户"
        elif balance >= 1000:
            return "银卡账户"
        else:
            return "普通账户"
    
    # Setter方法
    def set_balance(self, amount, description="余额调整"):
        """设置账户余额（内部方法）"""
        if not self._is_active:
            raise RuntimeError("账户已被冻结，无法操作")
        
        if not isinstance(amount, (int, float)):
            raise TypeError("金额必须是数字")
        
        if amount < 0:
            raise ValueError("余额不能为负数")
        
        old_balance = self._balance
        self._balance = round(float(amount), 2)
        
        # 记录交易历史
        self._add_transaction(description, old_balance, self._balance)
    
    def set_active_status(self, is_active):
        """设置账户状态"""
        if not isinstance(is_active, bool):
            raise TypeError("账户状态必须是布尔值")
        
        old_status = self._is_active
        self._is_active = is_active
        
        status_desc = "激活" if is_active else "冻结"
        self._add_transaction(f"账户{status_desc}", self._balance, self._balance)
        
        print(f"账户已{status_desc}")
    
    # 私有辅助方法
    def _add_transaction(self, description, old_balance, new_balance):
        """添加交易记录"""
        import datetime
        transaction = {
            "时间": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "描述": description,
            "原余额": old_balance,
            "新余额": new_balance,
            "变动": new_balance - old_balance
        }
        self._transaction_history.append(transaction)
    
    # 业务方法
    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        
        new_balance = self.get_balance() + amount
        self.set_balance(new_balance, f"存款 {amount}")
        return f"存款成功，当前余额: {self.get_balance()}"
    
    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        
        current_balance = self.get_balance()
        if amount > current_balance:
            raise ValueError("余额不足")
        
        new_balance = current_balance - amount
        self.set_balance(new_balance, f"取款 {amount}")
        return f"取款成功，当前余额: {self.get_balance()}"
    
    def transfer(self, target_account, amount):
        """转账"""
        if amount <= 0:
            raise ValueError("转账金额必须大于0")
        
        # 从当前账户扣款
        current_balance = self.get_balance()
        if amount > current_balance:
            raise ValueError("余额不足")
        
        # 执行转账
        self.set_balance(current_balance - amount, f"转账给 {target_account.get_account_number()} {amount}")
        target_account.set_balance(target_account.get_balance() + amount, f"来自 {self.get_account_number()} 的转账 {amount}")
        
        return f"转账成功，当前余额: {self.get_balance()}"
    
    def get_account_summary(self):
        """获取账户摘要"""
        return {
            "账户号码": self.get_account_number(),
            "余额": self.get_balance(),
            "账户类型": self.get_account_type(),
            "状态": "正常" if self.get_is_active() else "冻结",
            "交易次数": len(self.get_transaction_history())
        }
    
    def print_transaction_history(self, limit=5):
        """打印交易历史"""
        history = self.get_transaction_history()
        print(f"\n最近{min(limit, len(history))}笔交易:")
        for transaction in history[-limit:]:
            print(f"  {transaction['时间']} - {transaction['描述']} (余额: {transaction['原余额']} → {transaction['新余额']})")
    
    def __str__(self):
        try:
            return f"账户 {self.get_account_number()}: {self.get_balance()} ({self.get_account_type()})"
        except RuntimeError:
            return f"账户 {self.get_account_number()}: 已冻结"

# 使用示例
def demonstrate_business_logic_getters_setters():
    """演示带业务逻辑的getter/setter"""
    print("\n=== 带业务逻辑的Getter/Setter演示 ===")
    
    # 创建账户
    account1 = BankAccount("123456789", 1000)
    account2 = BankAccount("987654321", 500)
    
    print(f"账户1: {account1}")
    print(f"账户2: {account2}")
    
    # 存款操作
    print(f"\n存款操作:")
    print(account1.deposit(500))
    print(f"存款后: {account1}")
    
    # 取款操作
    print(f"\n取款操作:")
    print(account1.withdraw(200))
    print(f"取款后: {account1}")
    
    # 转账操作
    print(f"\n转账操作:")
    print(account1.transfer(account2, 300))
    print(f"转账后账户1: {account1}")
    print(f"转账后账户2: {account2}")
    
    # 查看账户摘要
    print(f"\n账户1摘要:")
    for key, value in account1.get_account_summary().items():
        print(f"  {key}: {value}")
    
    # 查看交易历史
    account1.print_transaction_history()
    
    # 冻结账户测试
    print(f"\n冻结账户测试:")
    account1.set_active_status(False)
    try:
        account1.get_balance()
    except RuntimeError as e:
        print(f"冻结账户访问错误: {e}")
    
    # 解冻账户
    account1.set_active_status(True)
    print(f"解冻后: {account1}")

# 运行演示
demonstrate_business_logic_getters_setters()
```

### 3. Getter/Setter与@property的对比

```python
class ComparisonExample:
    """对比传统getter/setter与@property"""
    
    def __init__(self, value):
        self._value = value
        self._access_count = 0
    
    # 传统getter/setter方式
    def get_value_traditional(self):
        """传统getter方式"""
        self._access_count += 1
        print(f"传统getter被调用，访问次数: {self._access_count}")
        return self._value
    
    def set_value_traditional(self, value):
        """传统setter方式"""
        if value < 0:
            raise ValueError("值不能为负数")
        print(f"传统setter被调用，设置值: {value}")
        self._value = value
    
    # @property方式
    @property
    def value_property(self):
        """@property getter方式"""
        self._access_count += 1
        print(f"@property getter被调用，访问次数: {self._access_count}")
        return self._value
    
    @value_property.setter
    def value_property(self, value):
        """@property setter方式"""
        if value < 0:
            raise ValueError("值不能为负数")
        print(f"@property setter被调用，设置值: {value}")
        self._value = value
    
    def get_access_count(self):
        """获取访问次数"""
        return self._access_count
    
    def reset_access_count(self):
        """重置访问次数"""
        self._access_count = 0

# 对比演示
def demonstrate_comparison():
    """演示传统方式与@property的对比"""
    print("\n=== 传统Getter/Setter与@property对比 ===")
    
    obj = ComparisonExample(10)
    
    print("\n1. 传统getter/setter方式:")
    print(f"获取值: {obj.get_value_traditional()}")
    obj.set_value_traditional(20)
    print(f"修改后获取值: {obj.get_value_traditional()}")
    
    print("\n2. @property方式:")
    obj.reset_access_count()
    print(f"获取值: {obj.value_property}")
    obj.value_property = 30
    print(f"修改后获取值: {obj.value_property}")
    
    print("\n语法对比:")
    print("传统方式: obj.get_value() / obj.set_value(x)")
    print("@property: obj.value / obj.value = x")
    print("@property方式更简洁，更符合Python风格")
```

### 4. 高级Getter/Setter模式

```python
class AdvancedGetterSetter:
    """高级getter/setter模式"""
    
    def __init__(self):
        self._data = {}
        self._validators = {}
        self._formatters = {}
        self._change_listeners = []
    
    def add_validator(self, field, validator_func):
        """添加字段验证器"""
        if field not in self._validators:
            self._validators[field] = []
        self._validators[field].append(validator_func)
    
    def add_formatter(self, field, formatter_func):
        """添加字段格式化器"""
        self._formatters[field] = formatter_func
    
    def add_change_listener(self, listener_func):
        """添加变更监听器"""
        self._change_listeners.append(listener_func)
    
    def get_field(self, field):
        """通用getter方法"""
        if field not in self._data:
            raise KeyError(f"字段 '{field}' 不存在")
        
        value = self._data[field]
        
        # 应用格式化器
        if field in self._formatters:
            value = self._formatters[field](value)
        
        return value
    
    def set_field(self, field, value):
        """通用setter方法"""
        # 应用验证器
        if field in self._validators:
            for validator in self._validators[field]:
                validator(value)
        
        old_value = self._data.get(field)
        self._data[field] = value
        
        # 通知变更监听器
        for listener in self._change_listeners:
            listener(field, old_value, value)
    
    def has_field(self, field):
        """检查字段是否存在"""
        return field in self._data
    
    def get_all_fields(self):
        """获取所有字段"""
        return list(self._data.keys())
    
    def get_field_info(self, field):
        """获取字段信息"""
        return {
            "值": self._data.get(field),
            "有验证器": field in self._validators,
            "有格式化器": field in self._formatters,
            "验证器数量": len(self._validators.get(field, []))
        }

# 使用高级模式的具体类
class ConfigurableUser(AdvancedGetterSetter):
    """可配置的用户类"""
    
    def __init__(self, name, email, age):
        super().__init__()
        
        # 设置验证器
        self.add_validator("name", self._validate_name)
        self.add_validator("email", self._validate_email)
        self.add_validator("age", self._validate_age)
        
        # 设置格式化器
        self.add_formatter("name", lambda x: x.title())
        self.add_formatter("email", lambda x: x.lower())
        
        # 添加变更监听器
        self.add_change_listener(self._log_change)
        
        # 初始化数据
        self.set_name(name)
        self.set_email(email)
        self.set_age(age)
    
    # 验证器方法
    def _validate_name(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("姓名必须是非空字符串")
    
    def _validate_email(self, email):
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("邮箱格式不正确")
    
    def _validate_age(self, age):
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError("年龄必须是0-150之间的整数")
    
    # 变更监听器
    def _log_change(self, field, old_value, new_value):
        print(f"字段 '{field}' 从 '{old_value}' 变更为 '{new_value}'")
    
    # 具体的getter/setter方法
    def get_name(self):
        return self.get_field("name")
    
    def set_name(self, name):
        self.set_field("name", name)
    
    def get_email(self):
        return self.get_field("email")
    
    def set_email(self, email):
        self.set_field("email", email)
    
    def get_age(self):
        return self.get_field("age")
    
    def set_age(self, age):
        self.set_field("age", age)
    
    def get_user_info(self):
        """获取用户信息"""
        return {
            "姓名": self.get_name(),
            "邮箱": self.get_email(),
            "年龄": self.get_age()
        }
    
    def __str__(self):
        return f"{self.get_name()} <{self.get_email()}> ({self.get_age()}岁)"

# 高级模式演示
def demonstrate_advanced_pattern():
    """演示高级getter/setter模式"""
    print("\n=== 高级Getter/Setter模式演示 ===")
    
    # 创建用户
    user = ConfigurableUser("john doe", "JOHN@EXAMPLE.COM", 25)
    print(f"创建用户: {user}")
    
    # 修改信息（会触发验证和格式化）
    print("\n修改用户信息:")
    user.set_name("  alice smith  ")
    user.set_email("ALICE@GMAIL.COM")
    user.set_age(30)
    
    print(f"修改后: {user}")
    
    # 查看字段信息
    print("\n字段信息:")
    for field in user.get_all_fields():
        info = user.get_field_info(field)
        print(f"  {field}: {info}")
    
    # 验证错误处理
    print("\n验证错误处理:")
    try:
        user.set_age(-5)
    except ValueError as e:
        print(f"年龄验证错误: {e}")
    
    try:
        user.set_email("invalid-email")
    except ValueError as e:
        print(f"邮箱验证错误: {e}")

# 运行演示
demonstrate_advanced_pattern()
```

## 最佳实践总结

```python
def demonstrate_best_practices():
    """演示getter/setter最佳实践"""
    print("\n=== Getter/Setter最佳实践总结 ===")
    
    print("\n1. 选择合适的方式:")
    print("   - 简单属性: 直接使用公有属性")
    print("   - 需要验证: 使用@property")
    print("   - 复杂业务逻辑: 使用传统getter/setter")
    print("   - 与其他语言交互: 使用传统getter/setter")
    
    print("\n2. 命名约定:")
    print("   - getter: get_property_name()")
    print("   - setter: set_property_name(value)")
    print("   - 布尔值getter: is_property_name()")
    
    print("\n3. 设计原则:")
    print("   - getter应该快速且无副作用")
    print("   - setter应该进行适当验证")
    print("   - 保持接口一致性")
    print("   - 提供清晰的错误信息")
    
    print("\n4. 性能考虑:")
    print("   - 避免在getter中进行昂贵操作")
    print("   - 考虑使用缓存机制")
    print("   - 延迟计算复杂属性")
    
    print("\n5. 安全性:")
    print("   - 验证所有输入")
    print("   - 返回副本而非原始对象")
    print("   - 控制访问权限")

# 运行最佳实践演示
demonstrate_best_practices()
```

## 学习要点

### 传统Getter/Setter的优势

1. **明确性**：方法名清楚表明意图
2. **灵活性**：可以实现复杂的业务逻辑
3. **兼容性**：与其他编程语言风格一致
4. **调试友好**：容易设置断点和日志

### 与@property的比较

| 特性 | 传统Getter/Setter | @property |
|------|------------------|----------|
| 语法 | obj.get_value() | obj.value |
| 可读性 | 明确但冗长 | 简洁优雅 |
| Python风格 | 不够Pythonic | 非常Pythonic |
| 复杂逻辑 | 适合 | 适合简单逻辑 |
| 调试 | 容易 | 稍难 |

### 使用建议

1. **优先使用@property**：符合Python风格
2. **复杂业务逻辑时使用传统方式**：更清晰
3. **与其他语言交互时使用传统方式**：保持一致性
4. **团队约定**：保持代码风格统一

### 注意事项

- 不要过度使用getter/setter
- 保持方法的单一职责
- 提供清晰的文档和错误信息
- 考虑性能影响
- 遵循团队编码规范

Getter和Setter方法是面向对象编程的重要概念，虽然Python提供了更优雅的@property方式，但理解传统方法仍然很重要，特别是在需要复杂业务逻辑或与其他系统交互时。