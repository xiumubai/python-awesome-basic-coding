# 私有属性和访问控制

## 学习目标
- 理解Python中的访问控制机制
- 掌握私有属性和私有方法的定义和使用
- 学会名称修饰（Name Mangling）的原理
- 了解属性访问的最佳实践
- 掌握使用属性装饰器控制访问

## Python访问控制基础

### 访问控制约定

Python使用命名约定来表示不同的访问级别：
- **公共属性**：正常命名，如 `name`
- **受保护属性**：单下划线开头，如 `_protected`
- **私有属性**：双下划线开头，如 `__private`

```python
class AccessControlDemo:
    """访问控制演示类"""
    
    def __init__(self, name, age, salary):
        """构造方法 - 演示不同访问级别的属性"""
        # 公共属性 - 可以自由访问
        self.name = name
        self.age = age
        
        # 受保护属性 - 约定为内部使用，但仍可访问
        self._department = "未分配"
        self._employee_id = self._generate_employee_id()
        
        # 私有属性 - 通过名称修饰隐藏
        self.__salary = salary
        self.__social_security = self._generate_ssn()
        self.__access_log = []
        
        # 记录创建日志
        self._log_access("对象创建")
        
        print(f"员工 {self.name} 创建成功，ID: {self._employee_id}")
    
    def _generate_employee_id(self):
        """受保护方法 - 生成员工ID"""
        import random
        return f"EMP{random.randint(10000, 99999)}"
    
    def _generate_ssn(self):
        """受保护方法 - 生成社会保险号"""
        import random
        return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"
    
    def __validate_salary(self, salary):
        """私有方法 - 验证薪资"""
        if not isinstance(salary, (int, float)):
            raise TypeError("薪资必须是数字")
        if salary < 0:
            raise ValueError("薪资不能为负数")
        if salary > 1000000:
            raise ValueError("薪资超出合理范围")
        return True
    
    def _log_access(self, action):
        """受保护方法 - 记录访问日志"""
        from datetime import datetime
        log_entry = {
            "action": action,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "employee": self.name
        }
        self.__access_log.append(log_entry)
    
    # 公共方法 - 提供安全的访问接口
    def get_basic_info(self):
        """获取基本信息（公共方法）"""
        self._log_access("查看基本信息")
        return {
            "姓名": self.name,
            "年龄": self.age,
            "部门": self._department,
            "员工ID": self._employee_id
        }
    
    def get_salary(self):
        """获取薪资（受控访问）"""
        self._log_access("查看薪资")
        # 在实际应用中，这里可能需要权限验证
        return f"¥{self.__salary:,.2f}"
    
    def set_salary(self, new_salary):
        """设置薪资（受控修改）"""
        self.__validate_salary(new_salary)
        old_salary = self.__salary
        self.__salary = new_salary
        self._log_access(f"薪资修改: {old_salary} -> {new_salary}")
        return f"薪资已更新为: ¥{new_salary:,.2f}"
    
    def get_sensitive_info(self, authorized=False):
        """获取敏感信息（需要授权）"""
        if not authorized:
            self._log_access("未授权访问敏感信息")
            return "访问被拒绝：需要授权"
        
        self._log_access("授权访问敏感信息")
        return {
            "社会保险号": self.__social_security,
            "薪资": self.__salary,
            "访问日志条数": len(self.__access_log)
        }
    
    def get_access_log(self, authorized=False):
        """获取访问日志（需要授权）"""
        if not authorized:
            return "访问被拒绝：需要授权"
        
        return self.__access_log.copy()
    
    def update_department(self, department):
        """更新部门信息"""
        old_dept = self._department
        self._department = department
        self._log_access(f"部门变更: {old_dept} -> {department}")
        return f"部门已更新为: {department}"
    
    # 演示直接访问的结果
    def demonstrate_access_levels(self):
        """演示不同访问级别"""
        print("=== 访问级别演示 ===")
        print(f"公共属性 name: {self.name}")
        print(f"受保护属性 _department: {self._department}")
        print(f"私有属性 __salary (内部访问): {self.__salary}")
        print(f"私有属性 __social_security (内部访问): {self.__social_security}")
        
        # 显示实际的属性名称
        print("\n=== 实际属性名称 ===")
        for attr in dir(self):
            if not attr.startswith('__') or attr.endswith('__'):
                continue
            print(f"修饰后的属性名: {attr}")
    
    def __str__(self):
        return f"Employee: {self.name} ({self._employee_id})"
    
    def __repr__(self):
        return f"AccessControlDemo(name='{self.name}', age={self.age})"

# 访问控制基础演示
print("=== 访问控制基础演示 ===")

# 创建员工对象
employee = AccessControlDemo("张三", 30, 15000)

print("\n1. 公共属性访问:")
print(f"姓名: {employee.name}")
print(f"年龄: {employee.age}")

# 修改公共属性
employee.name = "张三丰"
employee.age = 31
print(f"修改后 - 姓名: {employee.name}, 年龄: {employee.age}")

print("\n2. 受保护属性访问（约定为内部使用，但仍可访问）:")
print(f"部门: {employee._department}")
print(f"员工ID: {employee._employee_id}")

# 修改受保护属性（不推荐，但可以）
employee._department = "技术部"
print(f"修改后部门: {employee._department}")

print("\n3. 私有属性访问尝试:")
try:
    print(f"尝试直接访问 __salary: {employee.__salary}")
except AttributeError as e:
    print(f"直接访问失败: {e}")

try:
    print(f"尝试直接访问 __social_security: {employee.__social_security}")
except AttributeError as e:
    print(f"直接访问失败: {e}")

print("\n4. 通过名称修饰访问私有属性:")
print(f"通过修饰名访问薪资: {employee._AccessControlDemo__salary}")
print(f"通过修饰名访问社保号: {employee._AccessControlDemo__social_security}")

print("\n5. 通过公共方法安全访问:")
print(f"基本信息: {employee.get_basic_info()}")
print(f"薪资信息: {employee.get_salary()}")
print(f"更新薪资: {employee.set_salary(16000)}")
print(f"更新部门: {employee.update_department('研发部')}")

print("\n6. 敏感信息访问控制:")
print(f"未授权访问: {employee.get_sensitive_info()}")
print(f"授权访问: {employee.get_sensitive_info(authorized=True)}")

print("\n7. 访问级别演示:")
employee.demonstrate_access_levels()
```

### 名称修饰（Name Mangling）详解

```python
class NameManglingDemo:
    """名称修饰演示类"""
    
    def __init__(self):
        # 不同类型的属性
        self.public = "公共属性"
        self._protected = "受保护属性"
        self.__private = "私有属性"
        self.__another_private = "另一个私有属性"
        
        # 特殊情况
        self.__special__ = "特殊方法格式（不会被修饰）"
        self.__ = "双下划线（不会被修饰）"
        self.___ = "三下划线（不会被修饰）"
    
    def __private_method(self):
        """私有方法"""
        return "这是私有方法的返回值"
    
    def _protected_method(self):
        """受保护方法"""
        return "这是受保护方法的返回值"
    
    def public_method(self):
        """公共方法"""
        return "这是公共方法的返回值"
    
    def access_private_internally(self):
        """在类内部访问私有成员"""
        print("=== 类内部访问私有成员 ===")
        print(f"私有属性: {self.__private}")
        print(f"私有方法: {self.__private_method()}")
        
        # 修改私有属性
        self.__private = "修改后的私有属性"
        print(f"修改后的私有属性: {self.__private}")
    
    def show_all_attributes(self):
        """显示所有属性"""
        print("=== 所有属性列表 ===")
        for attr in sorted(dir(self)):
            if not callable(getattr(self, attr)):
                try:
                    value = getattr(self, attr)
                    print(f"{attr}: {value}")
                except:
                    print(f"{attr}: <无法访问>")
    
    def show_mangled_names(self):
        """显示名称修饰结果"""
        print("=== 名称修饰结果 ===")
        
        # 获取所有以下划线开头的属性
        mangled_attrs = [attr for attr in dir(self) if attr.startswith('_NameManglingDemo__')]
        
        print("修饰后的私有属性:")
        for attr in mangled_attrs:
            original_name = attr.replace('_NameManglingDemo__', '__')
            print(f"  原始名称: {original_name} -> 修饰后: {attr}")
            try:
                value = getattr(self, attr)
                print(f"    值: {value}")
            except:
                print(f"    值: <无法访问>")

class ChildClass(NameManglingDemo):
    """子类 - 演示继承中的名称修饰"""
    
    def __init__(self):
        super().__init__()
        
        # 子类的私有属性
        self.__child_private = "子类私有属性"
        self._child_protected = "子类受保护属性"
        
        # 尝试访问父类私有属性
        print("\n=== 子类中访问父类属性 ===")
        print(f"父类公共属性: {self.public}")
        print(f"父类受保护属性: {self._protected}")
        
        try:
            print(f"父类私有属性: {self.__private}")
        except AttributeError as e:
            print(f"无法直接访问父类私有属性: {e}")
            print(f"通过修饰名访问: {self._NameManglingDemo__private}")
    
    def __child_private_method(self):
        """子类私有方法"""
        return "子类私有方法"
    
    def show_child_attributes(self):
        """显示子类属性"""
        print("\n=== 子类属性分析 ===")
        
        # 父类修饰的属性
        parent_mangled = [attr for attr in dir(self) if attr.startswith('_NameManglingDemo__')]
        print("父类修饰的属性:")
        for attr in parent_mangled:
            print(f"  {attr}")
        
        # 子类修饰的属性
        child_mangled = [attr for attr in dir(self) if attr.startswith('_ChildClass__')]
        print("子类修饰的属性:")
        for attr in child_mangled:
            print(f"  {attr}")
        
        # 访问各自的私有属性
        print("\n访问测试:")
        print(f"子类私有属性: {self.__child_private}")
        print(f"子类私有方法: {self.__child_private_method()}")
        print(f"父类私有属性（通过修饰名）: {self._NameManglingDemo__private}")

# 名称修饰演示
print("\n=== 名称修饰详解演示 ===")

# 创建父类对象
print("创建父类对象:")
parent_obj = NameManglingDemo()

print("\n父类内部访问:")
parent_obj.access_private_internally()

print("\n显示所有属性:")
parent_obj.show_all_attributes()

print("\n名称修饰结果:")
parent_obj.show_mangled_names()

print("\n创建子类对象:")
child_obj = ChildClass()

print("\n子类属性分析:")
child_obj.show_child_attributes()

print("\n=== 外部访问测试 ===")
print("公共属性访问:")
print(f"parent_obj.public = {parent_obj.public}")
print(f"child_obj.public = {child_obj.public}")

print("\n受保护属性访问（约定不推荐，但可以）:")
print(f"parent_obj._protected = {parent_obj._protected}")
print(f"child_obj._protected = {child_obj._protected}")

print("\n私有属性访问（通过修饰名）:")
print(f"parent_obj._NameManglingDemo__private = {parent_obj._NameManglingDemo__private}")
print(f"child_obj._NameManglingDemo__private = {child_obj._NameManglingDemo__private}")
print(f"child_obj._ChildClass__child_private = {child_obj._ChildClass__child_private}")

print("\n直接访问私有属性（会失败）:")
try:
    print(parent_obj.__private)
except AttributeError as e:
    print(f"访问失败: {e}")

try:
    print(child_obj.__child_private)
except AttributeError as e:
    print(f"访问失败: {e}")
```

### 使用属性装饰器控制访问

```python
class PropertyDemo:
    """属性装饰器演示类"""
    
    def __init__(self, name, age, salary):
        """构造方法"""
        self._name = name
        self._age = age
        self._salary = salary
        self._access_count = 0
        self._modification_log = []
        
        print(f"PropertyDemo 对象创建: {name}")
    
    # 使用 @property 装饰器创建只读属性
    @property
    def name(self):
        """姓名属性（只读）"""
        self._access_count += 1
        return self._name
    
    # 年龄属性 - 可读可写，带验证
    @property
    def age(self):
        """年龄属性（可读）"""
        self._access_count += 1
        return self._age
    
    @age.setter
    def age(self, value):
        """年龄属性设置器（带验证）"""
        if not isinstance(value, int):
            raise TypeError("年龄必须是整数")
        if not 0 <= value <= 150:
            raise ValueError("年龄必须在0-150之间")
        
        old_age = self._age
        self._age = value
        self._log_modification("age", old_age, value)
        print(f"年龄已更新: {old_age} -> {value}")
    
    # 薪资属性 - 可读可写可删除，带复杂验证
    @property
    def salary(self):
        """薪资属性（可读）"""
        self._access_count += 1
        return self._salary
    
    @salary.setter
    def salary(self, value):
        """薪资属性设置器（带验证和日志）"""
        if not isinstance(value, (int, float)):
            raise TypeError("薪资必须是数字")
        if value < 0:
            raise ValueError("薪资不能为负数")
        if value > 1000000:
            raise ValueError("薪资超出合理范围")
        
        old_salary = self._salary
        self._salary = float(value)
        self._log_modification("salary", old_salary, value)
        print(f"薪资已更新: ¥{old_salary:,.2f} -> ¥{value:,.2f}")
    
    @salary.deleter
    def salary(self):
        """薪资属性删除器"""
        old_salary = self._salary
        self._salary = 0.0
        self._log_modification("salary", old_salary, "已删除")
        print("薪资信息已删除")
    
    # 计算属性 - 基于其他属性计算得出
    @property
    def annual_salary(self):
        """年薪（计算属性）"""
        return self._salary * 12
    
    @property
    def salary_level(self):
        """薪资等级（计算属性）"""
        if self._salary < 5000:
            return "初级"
        elif self._salary < 15000:
            return "中级"
        elif self._salary < 30000:
            return "高级"
        else:
            return "专家级"
    
    # 只写属性（不常见，但可能有用）
    @property
    def password(self):
        """密码属性（只写，不可读）"""
        raise AttributeError("密码不可读取")
    
    @password.setter
    def password(self, value):
        """密码设置器"""
        if len(value) < 8:
            raise ValueError("密码长度至少8位")
        
        # 在实际应用中，这里会进行加密存储
        import hashlib
        self._password_hash = hashlib.sha256(value.encode()).hexdigest()
        self._log_modification("password", "***", "已更新")
        print("密码已设置")
    
    def verify_password(self, password):
        """验证密码"""
        import hashlib
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return hasattr(self, '_password_hash') and self._password_hash == password_hash
    
    # 缓存属性 - 计算一次后缓存结果
    @property
    def expensive_calculation(self):
        """昂贵计算（带缓存）"""
        if not hasattr(self, '_cached_result'):
            print("执行昂贵计算...")
            # 模拟复杂计算
            import time
            time.sleep(0.1)  # 模拟计算时间
            self._cached_result = sum(range(1000000))
            print("计算完成并缓存")
        else:
            print("使用缓存结果")
        
        return self._cached_result
    
    def clear_cache(self):
        """清除缓存"""
        if hasattr(self, '_cached_result'):
            delattr(self, '_cached_result')
            print("缓存已清除")
    
    def _log_modification(self, attr_name, old_value, new_value):
        """记录修改日志"""
        from datetime import datetime
        log_entry = {
            "attribute": attr_name,
            "old_value": old_value,
            "new_value": new_value,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self._modification_log.append(log_entry)
    
    # 访问统计
    @property
    def access_count(self):
        """访问次数统计"""
        return self._access_count
    
    @property
    def modification_log(self):
        """修改日志"""
        return self._modification_log.copy()
    
    # 综合信息
    def get_summary(self):
        """获取对象摘要"""
        return {
            "姓名": self.name,
            "年龄": self.age,
            "月薪": f"¥{self.salary:,.2f}",
            "年薪": f"¥{self.annual_salary:,.2f}",
            "薪资等级": self.salary_level,
            "访问次数": self.access_count,
            "修改次数": len(self.modification_log)
        }
    
    def __str__(self):
        return f"PropertyDemo: {self.name}, 年龄: {self.age}, 薪资: ¥{self.salary:,.2f}"
    
    def __repr__(self):
        return f"PropertyDemo(name='{self.name}', age={self.age}, salary={self.salary})"

# 属性装饰器演示
print("\n=== 属性装饰器演示 ===")

# 创建对象
print("创建员工对象:")
employee = PropertyDemo("李四", 28, 12000)

print("\n1. 属性读取:")
print(f"姓名: {employee.name}")
print(f"年龄: {employee.age}")
print(f"薪资: ¥{employee.salary:,.2f}")
print(f"年薪: ¥{employee.annual_salary:,.2f}")
print(f"薪资等级: {employee.salary_level}")

print("\n2. 属性修改:")
employee.age = 29
employee.salary = 15000

print("\n3. 尝试修改只读属性:")
try:
    employee.name = "王五"
except AttributeError as e:
    print(f"修改只读属性失败: {e}")

print("\n4. 属性验证:")
try:
    employee.age = -5
except ValueError as e:
    print(f"年龄验证失败: {e}")

try:
    employee.salary = "不是数字"
except TypeError as e:
    print(f"薪资类型验证失败: {e}")

try:
    employee.salary = 2000000
except ValueError as e:
    print(f"薪资范围验证失败: {e}")

print("\n5. 计算属性:")
print(f"当前年薪: ¥{employee.annual_salary:,.2f}")
print(f"当前薪资等级: {employee.salary_level}")

# 修改薪资后重新查看计算属性
employee.salary = 8000
print(f"降薪后年薪: ¥{employee.annual_salary:,.2f}")
print(f"降薪后薪资等级: {employee.salary_level}")

print("\n6. 只写属性（密码）:")
employee.password = "secure123456"

try:
    print(f"尝试读取密码: {employee.password}")
except AttributeError as e:
    print(f"读取密码失败: {e}")

print(f"密码验证（正确）: {employee.verify_password('secure123456')}")
print(f"密码验证（错误）: {employee.verify_password('wrong')}")

print("\n7. 属性删除:")
print(f"删除前薪资: ¥{employee.salary:,.2f}")
del employee.salary
print(f"删除后薪资: ¥{employee.salary:,.2f}")

print("\n8. 缓存属性:")
print("第一次访问（会计算）:")
result1 = employee.expensive_calculation
print(f"结果: {result1}")

print("\n第二次访问（使用缓存）:")
result2 = employee.expensive_calculation
print(f"结果: {result2}")

print("\n清除缓存后再次访问:")
employee.clear_cache()
result3 = employee.expensive_calculation
print(f"结果: {result3}")

print("\n9. 访问统计和修改日志:")
print(f"总访问次数: {employee.access_count}")
print("修改日志:")
for i, log in enumerate(employee.modification_log, 1):
    print(f"  {i}. {log['timestamp']} - {log['attribute']}: {log['old_value']} -> {log['new_value']}")

print("\n10. 对象摘要:")
summary = employee.get_summary()
for key, value in summary.items():
    print(f"  {key}: {value}")

print(f"\n最终对象状态: {employee}")
```

### 实际应用示例：银行账户类

```python
class BankAccount:
    """银行账户类 - 综合应用私有属性和访问控制"""
    
    # 类属性
    _account_counter = 1000
    _all_accounts = {}
    
    def __init__(self, owner_name, initial_balance=0, account_type="储蓄账户"):
        """创建银行账户"""
        # 公共信息
        self.owner_name = owner_name
        self.account_type = account_type
        self.creation_date = self._get_current_date()
        
        # 受保护信息
        self._account_number = self._generate_account_number()
        self._status = "正常"
        
        # 私有敏感信息
        self.__balance = 0.0
        self.__pin = None
        self.__transaction_history = []
        self.__daily_limit = 10000.0
        self.__failed_attempts = 0
        self.__is_locked = False
        
        # 初始存款
        if initial_balance > 0:
            self.__deposit(initial_balance, "开户存款")
        
        # 注册账户
        BankAccount._all_accounts[self._account_number] = self
        
        print(f"账户创建成功: {self._account_number} - {owner_name}")
    
    def _get_current_date(self):
        """获取当前日期"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d")
    
    def _get_current_datetime(self):
        """获取当前日期时间"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _generate_account_number(self):
        """生成账户号码"""
        BankAccount._account_counter += 1
        return f"ACC{BankAccount._account_counter:06d}"
    
    def __validate_pin(self, pin):
        """验证PIN码"""
        if self.__is_locked:
            raise Exception("账户已锁定，请联系银行")
        
        if self.__pin is None:
            raise Exception("请先设置PIN码")
        
        if pin != self.__pin:
            self.__failed_attempts += 1
            if self.__failed_attempts >= 3:
                self.__is_locked = True
                self.__log_transaction("账户锁定", 0, "PIN码错误次数过多")
                raise Exception("PIN码错误次数过多，账户已锁定")
            raise Exception(f"PIN码错误，剩余尝试次数: {3 - self.__failed_attempts}")
        
        # PIN码正确，重置失败次数
        self.__failed_attempts = 0
    
    def __log_transaction(self, transaction_type, amount, description=""):
        """记录交易日志"""
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance_after": self.__balance,
            "description": description,
            "timestamp": self._get_current_datetime()
        }
        self.__transaction_history.append(transaction)
    
    def __deposit(self, amount, description="存款"):
        """内部存款方法"""
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        
        self.__balance += amount
        self.__log_transaction("存款", amount, description)
        return self.__balance
    
    def __withdraw(self, amount, description="取款"):
        """内部取款方法"""
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        
        if amount > self.__balance:
            raise Exception("余额不足")
        
        if amount > self.__daily_limit:
            raise Exception(f"超出每日限额 ¥{self.__daily_limit:,.2f}")
        
        self.__balance -= amount
        self.__log_transaction("取款", -amount, description)
        return self.__balance
    
    # 公共接口方法
    def set_pin(self, new_pin, old_pin=None):
        """设置PIN码"""
        if self.__pin is not None:
            self.__validate_pin(old_pin)
        
        if not isinstance(new_pin, str) or len(new_pin) != 4 or not new_pin.isdigit():
            raise ValueError("PIN码必须是4位数字")
        
        self.__pin = new_pin
        self.__log_transaction("PIN码设置", 0, "PIN码已更新")
        return "PIN码设置成功"
    
    def deposit(self, amount, pin, description="存款"):
        """存款（需要PIN码验证）"""
        self.__validate_pin(pin)
        balance = self.__deposit(amount, description)
        return f"存款成功，当前余额: ¥{balance:,.2f}"
    
    def withdraw(self, amount, pin, description="取款"):
        """取款（需要PIN码验证）"""
        self.__validate_pin(pin)
        balance = self.__withdraw(amount, description)
        return f"取款成功，当前余额: ¥{balance:,.2f}"
    
    def transfer(self, target_account, amount, pin, description="转账"):
        """转账"""
        self.__validate_pin(pin)
        
        if not isinstance(target_account, BankAccount):
            raise TypeError("目标必须是BankAccount对象")
        
        if target_account._status != "正常" or self._status != "正常":
            raise Exception("账户状态异常，无法转账")
        
        # 从本账户扣款
        self.__withdraw(amount, f"转账至{target_account._account_number}")
        
        # 向目标账户存款
        target_account.__deposit(amount, f"来自{self._account_number}的转账")
        
        return f"转账成功，向 {target_account._account_number} 转账 ¥{amount:,.2f}"
    
    # 属性访问器
    @property
    def balance(self):
        """余额查询（只读）"""
        return f"¥{self.__balance:,.2f}"
    
    def get_balance(self, pin):
        """获取余额（需要PIN码）"""
        self.__validate_pin(pin)
        return self.__balance
    
    @property
    def account_number(self):
        """账户号码（只读）"""
        return self._account_number
    
    @property
    def status(self):
        """账户状态（只读）"""
        if self.__is_locked:
            return "已锁定"
        return self._status
    
    @property
    def daily_limit(self):
        """每日限额（只读）"""
        return f"¥{self.__daily_limit:,.2f}"
    
    def set_daily_limit(self, new_limit, pin):
        """设置每日限额"""
        self.__validate_pin(pin)
        
        if new_limit < 0:
            raise ValueError("限额不能为负数")
        
        old_limit = self.__daily_limit
        self.__daily_limit = new_limit
        self.__log_transaction("限额修改", 0, f"从¥{old_limit:,.2f}修改为¥{new_limit:,.2f}")
        return f"每日限额已设置为: ¥{new_limit:,.2f}"
    
    def get_transaction_history(self, pin, limit=10):
        """获取交易历史"""
        self.__validate_pin(pin)
        
        # 返回最近的交易记录
        recent_transactions = self.__transaction_history[-limit:]
        return recent_transactions.copy()
    
    def get_account_info(self, pin):
        """获取账户完整信息"""
        self.__validate_pin(pin)
        
        return {
            "账户号码": self._account_number,
            "户主姓名": self.owner_name,
            "账户类型": self.account_type,
            "开户日期": self.creation_date,
            "当前余额": f"¥{self.__balance:,.2f}",
            "账户状态": self.status,
            "每日限额": f"¥{self.__daily_limit:,.2f}",
            "交易次数": len(self.__transaction_history),
            "失败尝试次数": self.__failed_attempts
        }
    
    def unlock_account(self, admin_code="ADMIN123"):
        """解锁账户（管理员功能）"""
        if admin_code != "ADMIN123":
            raise Exception("管理员代码错误")
        
        self.__is_locked = False
        self.__failed_attempts = 0
        self.__log_transaction("账户解锁", 0, "管理员解锁")
        return "账户已解锁"
    
    @classmethod
    def find_account(cls, account_number):
        """查找账户"""
        return cls._all_accounts.get(account_number)
    
    @classmethod
    def get_total_accounts(cls):
        """获取账户总数"""
        return len(cls._all_accounts)
    
    def __str__(self):
        return f"BankAccount({self._account_number}) - {self.owner_name}"
    
    def __repr__(self):
        return f"BankAccount(owner_name='{self.owner_name}', account_number='{self._account_number}')"

# 银行账户综合演示
print("\n=== 银行账户综合演示 ===")

# 创建账户
print("1. 创建银行账户:")
account1 = BankAccount("张三", 5000, "储蓄账户")
account2 = BankAccount("李四", 3000, "支票账户")

print(f"\n账户1: {account1}")
print(f"账户2: {account2}")
print(f"总账户数: {BankAccount.get_total_accounts()}")

print("\n2. 设置PIN码:")
print(account1.set_pin("1234"))
print(account2.set_pin("5678"))

print("\n3. 查看余额:")
print(f"账户1余额（公开显示）: {account1.balance}")
print(f"账户1余额（PIN验证）: ¥{account1.get_balance('1234'):,.2f}")

print("\n4. 存取款操作:")
print(account1.deposit(2000, "1234", "工资存款"))
print(account1.withdraw(500, "1234", "ATM取款"))

print("\n5. 转账操作:")
print(account1.transfer(account2, 1000, "1234", "朋友转账"))

print("\n6. 查看账户信息:")
info1 = account1.get_account_info("1234")
for key, value in info1.items():
    print(f"  {key}: {value}")

print("\n7. 查看交易历史:")
history = account1.get_transaction_history("1234", 5)
for i, transaction in enumerate(history, 1):
    print(f"  {i}. {transaction['timestamp']} - {transaction['type']}: ¥{abs(transaction['amount']):,.2f}")
    print(f"     {transaction['description']}, 余额: ¥{transaction['balance_after']:,.2f}")

print("\n8. 错误处理演示:")

# PIN码错误
try:
    account1.get_balance("0000")
except Exception as e:
    print(f"PIN码错误: {e}")

# 余额不足
try:
    account2.withdraw(10000, "5678")
except Exception as e:
    print(f"余额不足: {e}")

# 超出限额
try:
    account1.withdraw(15000, "1234")
except Exception as e:
    print(f"超出限额: {e}")

print("\n9. 账户锁定演示:")
# 连续错误PIN码
for i in range(3):
    try:
        account2.get_balance("0000")
    except Exception as e:
        print(f"第{i+1}次错误: {e}")

# 尝试解锁
print(account2.unlock_account())
print(f"解锁后状态: {account2.status}")

print("\n10. 修改限额:")
print(account1.set_daily_limit(20000, "1234"))
print(f"新限额: {account1.daily_limit}")

print("\n11. 最终账户状态:")
print(f"账户1: {account1.balance}")
print(f"账户2: {account2.balance}")

print("\n=== 访问控制验证 ===")
print("尝试直接访问私有属性:")
try:
    print(account1.__balance)
except AttributeError as e:
    print(f"直接访问失败: {e}")

print("\n通过名称修饰访问（不推荐）:")
print(f"通过修饰名访问余额: {account1._BankAccount__balance}")

print("\n受保护属性访问（约定不推荐）:")
print(f"账户号码: {account1._account_number}")
print(f"账户状态: {account1._status}")
```

## 学习要点总结

### 访问控制级别
1. **公共属性**：正常命名，可以自由访问和修改
2. **受保护属性**：单下划线开头，约定为内部使用
3. **私有属性**：双下划线开头，通过名称修饰隐藏

### 名称修饰机制
1. **修饰规则**：`__attribute` → `_ClassName__attribute`
2. **适用范围**：只对双下划线开头且不以双下划线结尾的名称
3. **继承影响**：每个类的私有属性都有独立的修饰

### 属性装饰器
1. **@property**：创建只读属性
2. **@attribute.setter**：创建属性设置器
3. **@attribute.deleter**：创建属性删除器
4. **计算属性**：基于其他属性动态计算

### 访问控制最佳实践
1. **合理使用**：根据实际需要选择访问级别
2. **提供接口**：为私有属性提供安全的访问方法
3. **参数验证**：在设置器中进行参数验证
4. **日志记录**：记录敏感操作的访问日志

### 安全考虑
1. **不是真正的私有**：Python的私有属性仍可通过修饰名访问
2. **约定大于强制**：更多依赖编程约定而非语言强制
3. **合理设计**：通过良好的接口设计保护数据安全

## 练习建议

1. **基础练习**：创建一个 `Person` 类，使用不同访问级别的属性

2. **进阶练习**：设计一个 `ConfigManager` 类，使用属性装饰器控制配置访问

3. **高级练习**：实现一个完整的用户账户系统，包含密码加密、访问日志等功能

## 下一步学习

掌握了私有属性和访问控制后，接下来学习：
- [类属性和类方法](./07_class_attributes.md)
- [综合练习](./08_exercises.md)