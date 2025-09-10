# 属性装饰器：@property

@property装饰器是Python中实现属性访问控制的优雅方式，它允许我们像访问属性一样调用方法，同时提供getter、setter和deleter功能。

## @property的基本概念

@property装饰器将方法转换为属性，使得我们可以：
- 像访问属性一样调用方法
- 在获取和设置值时添加逻辑
- 创建只读、只写或读写属性
- 进行数据验证和转换

## 基本用法

### 1. 只读属性

```python
class Circle:
    """圆形类 - 演示只读属性"""
    
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """半径属性（只读）"""
        return self._radius
    
    @property
    def area(self):
        """面积属性（只读，计算得出）"""
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        """周长属性（只读，计算得出）"""
        return 2 * 3.14159 * self._radius
    
    def __str__(self):
        return f"圆形(半径={self.radius}, 面积={self.area:.2f}, 周长={self.circumference:.2f})"

# 使用示例
circle = Circle(5)
print(f"半径: {circle.radius}")
print(f"面积: {circle.area}")
print(f"周长: {circle.circumference}")
print(circle)

# 尝试修改只读属性（会失败）
try:
    circle.area = 100
except AttributeError as e:
    print(f"无法设置只读属性: {e}")
```

### 2. 读写属性

```python
class Person:
    """人员类 - 演示读写属性"""
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        """姓名属性的getter"""
        return self._name
    
    @name.setter
    def name(self, value):
        """姓名属性的setter"""
        if not isinstance(value, str):
            raise TypeError("姓名必须是字符串")
        if len(value.strip()) == 0:
            raise ValueError("姓名不能为空")
        self._name = value.strip().title()  # 自动格式化
    
    @property
    def age(self):
        """年龄属性的getter"""
        return self._age
    
    @age.setter
    def age(self, value):
        """年龄属性的setter"""
        if not isinstance(value, int):
            raise TypeError("年龄必须是整数")
        if value < 0 or value > 150:
            raise ValueError("年龄必须在0-150之间")
        self._age = value
    
    @property
    def age_group(self):
        """年龄组属性（只读，基于年龄计算）"""
        if self._age < 13:
            return "儿童"
        elif self._age < 20:
            return "青少年"
        elif self._age < 60:
            return "成年人"
        else:
            return "老年人"
    
    def __str__(self):
        return f"{self.name}({self.age}岁, {self.age_group})"

# 使用示例
person = Person("john doe", 25)
print(f"初始信息: {person}")

# 修改属性
person.name = "  alice smith  "  # 会自动格式化
person.age = 30
print(f"修改后: {person}")

# 数据验证
try:
    person.age = -5
except ValueError as e:
    print(f"年龄验证错误: {e}")

try:
    person.name = ""
except ValueError as e:
    print(f"姓名验证错误: {e}")
```

### 3. 完整的getter、setter、deleter

```python
class Temperature:
    """温度类 - 演示完整的属性控制"""
    
    def __init__(self, celsius=0):
        self._celsius = None
        self.celsius = celsius  # 使用setter进行初始化
    
    @property
    def celsius(self):
        """摄氏温度的getter"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """摄氏温度的setter"""
        if value is None:
            raise ValueError("温度不能为None")
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度(-273.15°C)")
        self._celsius = round(float(value), 2)
    
    @celsius.deleter
    def celsius(self):
        """摄氏温度的deleter"""
        print("重置温度为0°C")
        self._celsius = 0.0
    
    @property
    def fahrenheit(self):
        """华氏温度（只读）"""
        if self._celsius is None:
            return None
        return round(self._celsius * 9/5 + 32, 2)
    
    @property
    def kelvin(self):
        """开尔文温度（只读）"""
        if self._celsius is None:
            return None
        return round(self._celsius + 273.15, 2)
    
    @property
    def description(self):
        """温度描述（只读）"""
        if self._celsius is None:
            return "未设置温度"
        
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
        if self._celsius is None:
            return "温度未设置"
        return f"{self._celsius}°C = {self.fahrenheit}°F = {self.kelvin}K ({self.description})"

# 使用示例
temp = Temperature(25)
print(f"初始温度: {temp}")

# 修改温度
temp.celsius = 100
print(f"修改后: {temp}")

# 删除温度
del temp.celsius
print(f"删除后: {temp}")

# 验证错误处理
try:
    temp.celsius = -300
except ValueError as e:
    print(f"温度验证错误: {e}")
```

## 高级应用：安全的银行账户

```python
class SecureBankAccount:
    """安全银行账户 - 演示@property的高级应用"""
    
    def __init__(self, account_number, initial_balance=0, daily_limit=1000):
        self._account_number = account_number
        self._balance = 0
        self._daily_limit = daily_limit
        self._daily_withdrawn = 0
        self._is_frozen = False
        self._transaction_count = 0
        
        # 使用setter进行初始化，确保验证
        self.balance = initial_balance
    
    @property
    def account_number(self):
        """账户号码（只读）"""
        return self._account_number
    
    @property
    def balance(self):
        """余额的getter"""
        return self._balance
    
    @balance.setter
    def balance(self, value):
        """余额的setter（内部使用，有限制）"""
        if not isinstance(value, (int, float)):
            raise TypeError("余额必须是数字")
        if value < 0:
            raise ValueError("余额不能为负数")
        self._balance = round(float(value), 2)
        self._transaction_count += 1
    
    @property
    def daily_limit(self):
        """每日限额的getter"""
        return self._daily_limit
    
    @daily_limit.setter
    def daily_limit(self, value):
        """每日限额的setter"""
        if not isinstance(value, (int, float)):
            raise TypeError("限额必须是数字")
        if value <= 0:
            raise ValueError("限额必须大于0")
        if value > 10000:
            raise ValueError("单日限额不能超过10000")
        self._daily_limit = float(value)
    
    @property
    def available_daily_amount(self):
        """今日可用额度（只读）"""
        return max(0, self._daily_limit - self._daily_withdrawn)
    
    @property
    def is_frozen(self):
        """账户是否冻结（只读）"""
        return self._is_frozen
    
    @property
    def account_status(self):
        """账户状态（只读）"""
        if self._is_frozen:
            return "已冻结"
        elif self._balance == 0:
            return "零余额"
        elif self._balance < 100:
            return "低余额"
        else:
            return "正常"
    
    @property
    def transaction_count(self):
        """交易次数（只读）"""
        return self._transaction_count
    
    def deposit(self, amount):
        """存款"""
        if self._is_frozen:
            raise RuntimeError("账户已冻结，无法操作")
        
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        
        self.balance += amount  # 使用setter
        return f"存款成功，当前余额: {self.balance}"
    
    def withdraw(self, amount):
        """取款"""
        if self._is_frozen:
            raise RuntimeError("账户已冻结，无法操作")
        
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        
        if amount > self.balance:
            raise ValueError("余额不足")
        
        if amount > self.available_daily_amount:
            raise ValueError(f"超过每日限额，今日还可取款: {self.available_daily_amount}")
        
        self.balance -= amount  # 使用setter
        self._daily_withdrawn += amount
        return f"取款成功，当前余额: {self.balance}"
    
    def freeze_account(self):
        """冻结账户"""
        self._is_frozen = True
        return "账户已冻结"
    
    def unfreeze_account(self):
        """解冻账户"""
        self._is_frozen = False
        return "账户已解冻"
    
    def reset_daily_limit(self):
        """重置每日限额（模拟新的一天）"""
        self._daily_withdrawn = 0
        return "每日限额已重置"
    
    def get_account_info(self):
        """获取账户信息"""
        return {
            "账户号码": self.account_number,
            "余额": self.balance,
            "状态": self.account_status,
            "每日限额": self.daily_limit,
            "今日可用额度": self.available_daily_amount,
            "交易次数": self.transaction_count,
            "是否冻结": self.is_frozen
        }
    
    def __str__(self):
        return f"账户 {self.account_number}: {self.balance} ({self.account_status})"

# 使用示例
def demonstrate_secure_bank_account():
    """演示安全银行账户"""
    print("=== 安全银行账户演示 ===")
    
    # 创建账户
    account = SecureBankAccount("123456789", 1000, 500)
    print(f"创建账户: {account}")
    
    # 查看账户信息
    print("\n账户信息:")
    for key, value in account.get_account_info().items():
        print(f"  {key}: {value}")
    
    # 存款操作
    print("\n存款操作:")
    print(account.deposit(200))
    print(f"存款后状态: {account}")
    
    # 取款操作
    print("\n取款操作:")
    print(account.withdraw(300))
    print(f"取款后状态: {account}")
    print(f"今日剩余额度: {account.available_daily_amount}")
    
    # 尝试超限取款
    print("\n超限取款测试:")
    try:
        account.withdraw(300)  # 超过每日限额
    except ValueError as e:
        print(f"取款失败: {e}")
    
    # 修改每日限额
    print("\n修改每日限额:")
    account.daily_limit = 800
    print(f"新的每日限额: {account.daily_limit}")
    print(f"今日可用额度: {account.available_daily_amount}")
    
    # 冻结账户测试
    print("\n冻结账户测试:")
    print(account.freeze_account())
    try:
        account.deposit(100)
    except RuntimeError as e:
        print(f"冻结状态操作失败: {e}")
    
    # 解冻账户
    print(account.unfreeze_account())
    print(f"解冻后状态: {account}")
    
    # 最终账户信息
    print("\n最终账户信息:")
    for key, value in account.get_account_info().items():
        print(f"  {key}: {value}")

# 运行演示
demonstrate_secure_bank_account()
```

## @property的最佳实践

```python
class BestPracticeExample:
    """@property最佳实践示例"""
    
    def __init__(self, value):
        self._value = None
        self._computed_cache = None
        self._cache_valid = False
        self.value = value  # 使用setter初始化
    
    @property
    def value(self):
        """主要值的getter"""
        return self._value
    
    @value.setter
    def value(self, new_value):
        """主要值的setter"""
        # 1. 类型检查
        if not isinstance(new_value, (int, float)):
            raise TypeError(f"值必须是数字，得到: {type(new_value)}")
        
        # 2. 范围检查
        if new_value < 0:
            raise ValueError("值不能为负数")
        
        # 3. 只在值真正改变时更新
        if self._value != new_value:
            self._value = new_value
            self._cache_valid = False  # 使缓存失效
    
    @property
    def expensive_computation(self):
        """昂贵计算的缓存属性"""
        if not self._cache_valid:
            print("执行昂贵的计算...")
            self._computed_cache = self._value ** 2 + self._value * 10
            self._cache_valid = True
        return self._computed_cache
    
    @property
    def formatted_value(self):
        """格式化的值（只读）"""
        if self._value is None:
            return "未设置"
        return f"{self._value:,.2f}"
    
    @property
    def is_valid(self):
        """验证状态（只读）"""
        return self._value is not None and self._value >= 0
    
    def __str__(self):
        return f"值: {self.formatted_value}, 计算结果: {self.expensive_computation}"

# 最佳实践演示
def demonstrate_best_practices():
    """演示@property最佳实践"""
    print("\n=== @property最佳实践演示 ===")
    
    obj = BestPracticeExample(10)
    print(f"初始状态: {obj}")
    
    # 缓存机制测试
    print("\n缓存机制测试:")
    print(f"第一次访问: {obj.expensive_computation}")  # 会计算
    print(f"第二次访问: {obj.expensive_computation}")  # 使用缓存
    
    # 修改值使缓存失效
    print("\n修改值:")
    obj.value = 20
    print(f"修改后访问: {obj.expensive_computation}")  # 重新计算
    
    # 验证功能
    print(f"\n验证状态: {obj.is_valid}")
    print(f"格式化值: {obj.formatted_value}")

# 运行演示
demonstrate_best_practices()
```

## 学习要点

### @property的优势

1. **接口一致性**：属性访问语法保持一致
2. **数据验证**：在setter中进行输入验证
3. **计算属性**：动态计算而非存储
4. **向后兼容**：可以将简单属性升级为复杂属性
5. **缓存机制**：可以实现智能缓存

### 使用场景

- **数据验证**：需要验证输入的属性
- **计算属性**：基于其他属性计算的值
- **格式转换**：自动格式化输入输出
- **访问控制**：控制属性的读写权限
- **缓存优化**：缓存昂贵的计算结果

### 设计原则

1. **保持简单**：getter应该快速且无副作用
2. **一致性**：setter的验证应该一致
3. **文档化**：清楚地文档化属性的行为
4. **错误处理**：提供清晰的错误信息
5. **性能考虑**：避免在getter中进行昂贵操作

### 注意事项

- getter不应该有副作用
- setter应该进行适当的验证
- 避免在属性中进行复杂的计算
- 考虑使用缓存机制优化性能
- 保持属性接口的稳定性

@property装饰器是Python中实现优雅封装的重要工具，正确使用可以大大提高代码的质量和可维护性。