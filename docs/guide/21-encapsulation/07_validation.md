# 数据验证和保护

数据验证是确保程序健壮性和安全性的重要手段。通过在数据进入系统时进行严格的验证，我们可以防止无效数据破坏程序状态，提高系统的可靠性和安全性。

## 数据验证的重要性

- **数据完整性**：确保数据符合预期的格式和约束
- **安全防护**：防止恶意输入和注入攻击
- **错误预防**：在早期发现和处理错误
- **用户体验**：提供清晰的错误提示
- **系统稳定性**：避免因无效数据导致的程序崩溃

## 基本数据验证

### 1. 简单的属性验证

```python
class Person:
    """人员类 - 基本数据验证示例"""
    
    def __init__(self, name, age, email):
        # 使用setter进行初始化验证
        self.name = name
        self.age = age
        self.email = email
    
    @property
    def name(self):
        """姓名属性"""
        return self._name
    
    @name.setter
    def name(self, value):
        """姓名验证"""
        if not isinstance(value, str):
            raise TypeError("姓名必须是字符串")
        
        if not value.strip():
            raise ValueError("姓名不能为空")
        
        if len(value.strip()) < 2:
            raise ValueError("姓名长度至少2个字符")
        
        if len(value.strip()) > 50:
            raise ValueError("姓名长度不能超过50个字符")
        
        # 检查是否包含特殊字符
        import re
        if not re.match(r'^[\u4e00-\u9fa5a-zA-Z\s]+$', value.strip()):
            raise ValueError("姓名只能包含中文、英文字母和空格")
        
        self._name = value.strip()
    
    @property
    def age(self):
        """年龄属性"""
        return self._age
    
    @age.setter
    def age(self, value):
        """年龄验证"""
        if not isinstance(value, int):
            raise TypeError("年龄必须是整数")
        
        if value < 0:
            raise ValueError("年龄不能为负数")
        
        if value > 150:
            raise ValueError("年龄不能超过150岁")
        
        self._age = value
    
    @property
    def email(self):
        """邮箱属性"""
        return self._email
    
    @email.setter
    def email(self, value):
        """邮箱验证"""
        if not isinstance(value, str):
            raise TypeError("邮箱必须是字符串")
        
        if not value.strip():
            raise ValueError("邮箱不能为空")
        
        # 简单的邮箱格式验证
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, value.strip()):
            raise ValueError("邮箱格式不正确")
        
        self._email = value.strip().lower()
    
    def update_info(self, name=None, age=None, email=None):
        """更新信息方法"""
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if email is not None:
            self.email = email
        
        return "信息更新成功"
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"

# 演示基本数据验证
def demonstrate_basic_validation():
    """演示基本数据验证"""
    print("=== 基本数据验证演示 ===")
    
    # 正确的数据
    print("\n1. 创建有效的Person对象:")
    person = Person("张三", 25, "zhangsan@example.com")
    print(f"创建成功: {person}")
    
    # 测试各种无效数据
    print("\n2. 测试无效数据:")
    
    # 无效姓名
    invalid_names = [
        ("", "空姓名"),
        ("   ", "空白姓名"),
        ("a", "姓名太短"),
        ("a" * 51, "姓名太长"),
        ("张三123", "包含数字"),
        ("张三@", "包含特殊字符")
    ]
    
    for invalid_name, description in invalid_names:
        try:
            Person(invalid_name, 25, "test@example.com")
            print(f"  {description}: 验证失败（应该抛出异常）")
        except (ValueError, TypeError) as e:
            print(f"  {description}: {e}")
    
    # 无效年龄
    invalid_ages = [
        (-1, "负数年龄"),
        (151, "年龄过大"),
        ("25", "字符串年龄"),
        (25.5, "浮点数年龄")
    ]
    
    for invalid_age, description in invalid_ages:
        try:
            Person("张三", invalid_age, "test@example.com")
            print(f"  {description}: 验证失败（应该抛出异常）")
        except (ValueError, TypeError) as e:
            print(f"  {description}: {e}")
    
    # 无效邮箱
    invalid_emails = [
        ("", "空邮箱"),
        ("invalid", "无@符号"),
        ("invalid@", "缺少域名"),
        ("@example.com", "缺少用户名"),
        ("invalid@.com", "域名格式错误"),
        ("invalid@example", "缺少顶级域名")
    ]
    
    for invalid_email, description in invalid_emails:
        try:
            Person("张三", 25, invalid_email)
            print(f"  {description}: 验证失败（应该抛出异常）")
        except (ValueError, TypeError) as e:
            print(f"  {description}: {e}")
    
    # 测试更新信息
    print("\n3. 测试信息更新:")
    try:
        result = person.update_info(name="李四", age=30)
        print(f"更新成功: {result}")
        print(f"更新后: {person}")
    except (ValueError, TypeError) as e:
        print(f"更新失败: {e}")
    
    try:
        person.update_info(email="invalid-email")
    except ValueError as e:
        print(f"邮箱更新失败: {e}")

# 运行演示
demonstrate_basic_validation()
```

### 2. 复杂的业务逻辑验证

```python
import datetime
from decimal import Decimal, InvalidOperation
from enum import Enum

class AccountType(Enum):
    """账户类型枚举"""
    SAVINGS = "savings"
    CHECKING = "checking"
    CREDIT = "credit"

class TransactionType(Enum):
    """交易类型枚举"""
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"

class BankAccount:
    """银行账户 - 复杂数据验证示例"""
    
    def __init__(self, account_number, account_type, initial_balance=0, credit_limit=0):
        # 验证并设置基本信息
        self.account_number = account_number
        self.account_type = account_type
        self.credit_limit = credit_limit
        
        # 内部状态
        self._balance = Decimal('0')
        self._transaction_history = []
        self._daily_withdrawal_limit = Decimal('5000')
        self._daily_withdrawal_amount = Decimal('0')
        self._last_transaction_date = None
        self._is_frozen = False
        self._failed_transaction_count = 0
        
        # 设置初始余额
        if initial_balance > 0:
            self._add_transaction(TransactionType.DEPOSIT, initial_balance, "初始存款")
    
    @property
    def account_number(self):
        return self._account_number
    
    @account_number.setter
    def account_number(self, value):
        """账户号码验证"""
        if not isinstance(value, str):
            raise TypeError("账户号码必须是字符串")
        
        if not value.strip():
            raise ValueError("账户号码不能为空")
        
        # 账户号码格式验证（假设为12位数字）
        import re
        if not re.match(r'^\d{12}$', value.strip()):
            raise ValueError("账户号码必须是12位数字")
        
        self._account_number = value.strip()
    
    @property
    def account_type(self):
        return self._account_type
    
    @account_type.setter
    def account_type(self, value):
        """账户类型验证"""
        if not isinstance(value, AccountType):
            raise TypeError("账户类型必须是AccountType枚举")
        
        self._account_type = value
    
    @property
    def credit_limit(self):
        return self._credit_limit
    
    @credit_limit.setter
    def credit_limit(self, value):
        """信用额度验证"""
        try:
            credit_limit = Decimal(str(value))
        except (InvalidOperation, TypeError):
            raise TypeError("信用额度必须是数字")
        
        if credit_limit < 0:
            raise ValueError("信用额度不能为负数")
        
        if self._account_type != AccountType.CREDIT and credit_limit > 0:
            raise ValueError("只有信用账户才能设置信用额度")
        
        if credit_limit > Decimal('100000'):
            raise ValueError("信用额度不能超过100,000")
        
        self._credit_limit = credit_limit
    
    def _validate_amount(self, amount, operation="操作"):
        """金额验证（私有方法）"""
        try:
            amount = Decimal(str(amount))
        except (InvalidOperation, TypeError):
            raise TypeError(f"{operation}金额必须是数字")
        
        if amount <= 0:
            raise ValueError(f"{operation}金额必须大于0")
        
        if amount > Decimal('1000000'):
            raise ValueError(f"{operation}金额不能超过1,000,000")
        
        # 检查小数位数（最多2位）
        if amount.as_tuple().exponent < -2:
            raise ValueError(f"{operation}金额最多保留2位小数")
        
        return amount
    
    def _check_account_status(self):
        """检查账户状态（私有方法）"""
        if self._is_frozen:
            raise RuntimeError("账户已被冻结，无法进行交易")
        
        if self._failed_transaction_count >= 5:
            self._is_frozen = True
            raise RuntimeError("连续失败交易过多，账户已被冻结")
    
    def _reset_daily_limits_if_needed(self):
        """如果需要则重置每日限额（私有方法）"""
        today = datetime.date.today()
        if self._last_transaction_date != today:
            self._daily_withdrawal_amount = Decimal('0')
            self._last_transaction_date = today
    
    def _add_transaction(self, transaction_type, amount, description=""):
        """添加交易记录（私有方法）"""
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance_after": self._balance,
            "timestamp": datetime.datetime.now(),
            "description": description
        }
        self._transaction_history.append(transaction)
        
        # 限制交易历史记录数量
        if len(self._transaction_history) > 1000:
            self._transaction_history = self._transaction_history[-1000:]
    
    def deposit(self, amount, description="存款"):
        """存款方法"""
        self._check_account_status()
        amount = self._validate_amount(amount, "存款")
        
        # 存款限制检查
        if amount > Decimal('50000'):
            raise ValueError("单次存款金额不能超过50,000")
        
        self._balance += amount
        self._add_transaction(TransactionType.DEPOSIT, amount, description)
        self._failed_transaction_count = 0  # 重置失败计数
        
        return {
            "success": True,
            "message": f"存款成功，金额: {amount}",
            "balance": self._balance
        }
    
    def withdraw(self, amount, description="取款"):
        """取款方法"""
        self._check_account_status()
        amount = self._validate_amount(amount, "取款")
        self._reset_daily_limits_if_needed()
        
        # 取款限制检查
        if amount > Decimal('10000'):
            raise ValueError("单次取款金额不能超过10,000")
        
        # 每日取款限额检查
        if self._daily_withdrawal_amount + amount > self._daily_withdrawal_limit:
            remaining = self._daily_withdrawal_limit - self._daily_withdrawal_amount
            raise ValueError(f"超过每日取款限额，今日剩余额度: {remaining}")
        
        # 余额检查
        available_balance = self._balance
        if self._account_type == AccountType.CREDIT:
            available_balance += self._credit_limit
        
        if amount > available_balance:
            self._failed_transaction_count += 1
            raise ValueError(f"余额不足，可用余额: {available_balance}")
        
        # 执行取款
        self._balance -= amount
        self._daily_withdrawal_amount += amount
        self._add_transaction(TransactionType.WITHDRAWAL, amount, description)
        self._failed_transaction_count = 0
        
        return {
            "success": True,
            "message": f"取款成功，金额: {amount}",
            "balance": self._balance,
            "daily_remaining": self._daily_withdrawal_limit - self._daily_withdrawal_amount
        }
    
    def transfer(self, target_account, amount, description="转账"):
        """转账方法"""
        if not isinstance(target_account, BankAccount):
            raise TypeError("目标账户必须是BankAccount实例")
        
        if target_account.account_number == self.account_number:
            raise ValueError("不能向自己的账户转账")
        
        # 先从本账户取款
        withdraw_result = self.withdraw(amount, f"转账至{target_account.account_number}")
        
        try:
            # 向目标账户存款
            deposit_result = target_account.deposit(amount, f"来自{self.account_number}的转账")
            
            # 更新交易类型
            if self._transaction_history:
                self._transaction_history[-1]["type"] = TransactionType.TRANSFER
            
            return {
                "success": True,
                "message": f"转账成功，金额: {amount}",
                "from_balance": self._balance,
                "to_balance": target_account._balance
            }
        
        except Exception as e:
            # 转账失败，回滚取款操作
            self._balance += amount
            self._daily_withdrawal_amount -= amount
            if self._transaction_history:
                self._transaction_history.pop()  # 移除失败的取款记录
            
            raise RuntimeError(f"转账失败: {e}")
    
    def get_balance(self):
        """获取余额"""
        return self._balance
    
    def get_available_balance(self):
        """获取可用余额"""
        if self._account_type == AccountType.CREDIT:
            return self._balance + self._credit_limit
        return self._balance
    
    def get_transaction_history(self, limit=10):
        """获取交易历史"""
        return self._transaction_history[-limit:] if limit > 0 else self._transaction_history
    
    def freeze_account(self, reason="管理员操作"):
        """冻结账户"""
        self._is_frozen = True
        return f"账户已冻结，原因: {reason}"
    
    def unfreeze_account(self):
        """解冻账户"""
        self._is_frozen = False
        self._failed_transaction_count = 0
        return "账户已解冻"
    
    def __str__(self):
        return f"BankAccount({self.account_number}, {self.account_type.value}, balance={self._balance})"

# 演示复杂业务逻辑验证
def demonstrate_complex_validation():
    """演示复杂业务逻辑验证"""
    print("\n=== 复杂业务逻辑验证演示 ===")
    
    # 创建不同类型的账户
    print("\n1. 创建银行账户:")
    savings_account = BankAccount("123456789012", AccountType.SAVINGS, 10000)
    checking_account = BankAccount("123456789013", AccountType.CHECKING, 5000)
    credit_account = BankAccount("123456789014", AccountType.CREDIT, 0, 20000)
    
    print(f"储蓄账户: {savings_account}")
    print(f"支票账户: {checking_account}")
    print(f"信用账户: {credit_account}")
    
    # 测试存款验证
    print("\n2. 测试存款验证:")
    try:
        result = savings_account.deposit(1000, "工资存款")
        print(f"存款成功: {result}")
    except (ValueError, TypeError) as e:
        print(f"存款失败: {e}")
    
    # 测试无效存款
    invalid_deposits = [
        (-100, "负数存款"),
        (0, "零金额存款"),
        (60000, "超额存款"),
        ("abc", "非数字存款"),
        (100.123, "超过2位小数")
    ]
    
    for amount, description in invalid_deposits:
        try:
            savings_account.deposit(amount)
            print(f"  {description}: 验证失败（应该抛出异常）")
        except (ValueError, TypeError) as e:
            print(f"  {description}: {e}")
    
    # 测试取款验证
    print("\n3. 测试取款验证:")
    try:
        result = savings_account.withdraw(2000, "生活费")
        print(f"取款成功: {result}")
    except (ValueError, TypeError) as e:
        print(f"取款失败: {e}")
    
    # 测试余额不足
    try:
        savings_account.withdraw(50000)
    except ValueError as e:
        print(f"余额不足: {e}")
    
    # 测试每日限额
    print("\n4. 测试每日取款限额:")
    try:
        # 尝试取款接近限额
        savings_account.withdraw(4000)
        print("取款4000成功")
        
        # 再次取款应该失败
        savings_account.withdraw(2000)
    except ValueError as e:
        print(f"超过每日限额: {e}")
    
    # 测试转账验证
    print("\n5. 测试转账验证:")
    try:
        result = checking_account.transfer(savings_account, 1000, "转账测试")
        print(f"转账成功: {result}")
    except (ValueError, TypeError, RuntimeError) as e:
        print(f"转账失败: {e}")
    
    # 测试信用账户
    print("\n6. 测试信用账户:")
    print(f"信用账户余额: {credit_account.get_balance()}")
    print(f"信用账户可用余额: {credit_account.get_available_balance()}")
    
    try:
        result = credit_account.withdraw(5000, "信用取款")
        print(f"信用取款成功: {result}")
        print(f"取款后余额: {credit_account.get_balance()}")
    except ValueError as e:
        print(f"信用取款失败: {e}")
    
    # 测试账户冻结
    print("\n7. 测试账户冻结:")
    freeze_result = credit_account.freeze_account("可疑交易")
    print(freeze_result)
    
    try:
        credit_account.deposit(1000)
    except RuntimeError as e:
        print(f"冻结账户操作失败: {e}")
    
    unfreeze_result = credit_account.unfreeze_account()
    print(unfreeze_result)
    
    # 查看交易历史
    print("\n8. 交易历史:")
    history = savings_account.get_transaction_history(5)
    for i, transaction in enumerate(history, 1):
        print(f"  {i}. {transaction['type'].value}: {transaction['amount']} - {transaction['description']}")

# 运行演示
demonstrate_complex_validation()
```

### 3. 数据类验证装饰器

```python
from dataclasses import dataclass, field
from typing import List, Optional
import re
from datetime import datetime, date

def validate_string(min_length=0, max_length=None, pattern=None, not_empty=True):
    """字符串验证装饰器"""
    def validator(value):
        if not isinstance(value, str):
            raise TypeError("值必须是字符串")
        
        if not_empty and not value.strip():
            raise ValueError("字符串不能为空")
        
        if len(value) < min_length:
            raise ValueError(f"字符串长度不能少于{min_length}个字符")
        
        if max_length is not None and len(value) > max_length:
            raise ValueError(f"字符串长度不能超过{max_length}个字符")
        
        if pattern is not None and not re.match(pattern, value):
            raise ValueError(f"字符串格式不符合要求")
        
        return value.strip()
    
    return validator

def validate_number(min_value=None, max_value=None, integer_only=False):
    """数字验证装饰器"""
    def validator(value):
        if integer_only and not isinstance(value, int):
            raise TypeError("值必须是整数")
        
        if not isinstance(value, (int, float)):
            raise TypeError("值必须是数字")
        
        if min_value is not None and value < min_value:
            raise ValueError(f"值不能小于{min_value}")
        
        if max_value is not None and value > max_value:
            raise ValueError(f"值不能大于{max_value}")
        
        return value
    
    return validator

def validate_email():
    """邮箱验证装饰器"""
    def validator(value):
        if not isinstance(value, str):
            raise TypeError("邮箱必须是字符串")
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, value.strip()):
            raise ValueError("邮箱格式不正确")
        
        return value.strip().lower()
    
    return validator

def validate_phone():
    """手机号验证装饰器"""
    def validator(value):
        if not isinstance(value, str):
            raise TypeError("手机号必须是字符串")
        
        # 简单的中国手机号验证
        phone_pattern = r'^1[3-9]\d{9}$'
        if not re.match(phone_pattern, value.strip()):
            raise ValueError("手机号格式不正确")
        
        return value.strip()
    
    return validator

class ValidatedField:
    """验证字段描述符"""
    
    def __init__(self, validator, default=None):
        self.validator = validator
        self.default = default
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f'_{name}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, self.default)
    
    def __set__(self, obj, value):
        if value is not None:
            value = self.validator(value)
        setattr(obj, self.name, value)

@dataclass
class Product:
    """产品类 - 使用数据类和验证装饰器"""
    
    # 使用验证字段
    name: str = field(default="")
    description: str = field(default="")
    price: float = field(default=0.0)
    stock: int = field(default=0)
    category: str = field(default="")
    sku: str = field(default="")
    tags: List[str] = field(default_factory=list)
    
    # 验证字段定义
    _name_validator = ValidatedField(validate_string(min_length=2, max_length=100))
    _description_validator = ValidatedField(validate_string(max_length=500, not_empty=False))
    _price_validator = ValidatedField(validate_number(min_value=0, max_value=999999))
    _stock_validator = ValidatedField(validate_number(min_value=0, integer_only=True))
    _category_validator = ValidatedField(validate_string(min_length=2, max_length=50))
    _sku_validator = ValidatedField(validate_string(pattern=r'^[A-Z0-9]{6,12}$'))
    
    def __post_init__(self):
        """初始化后验证"""
        # 使用验证器验证所有字段
        self._name_validator.__set__(self, self.name)
        self._description_validator.__set__(self, self.description)
        self._price_validator.__set__(self, self.price)
        self._stock_validator.__set__(self, self.stock)
        self._category_validator.__set__(self, self.category)
        self._sku_validator.__set__(self, self.sku)
        
        # 验证标签
        if not isinstance(self.tags, list):
            raise TypeError("标签必须是列表")
        
        for tag in self.tags:
            if not isinstance(tag, str) or not tag.strip():
                raise ValueError("标签必须是非空字符串")
        
        # 去重并排序标签
        self.tags = sorted(list(set(tag.strip().lower() for tag in self.tags)))
    
    def update_price(self, new_price):
        """更新价格"""
        self._price_validator.__set__(self, new_price)
        self.price = self._price_validator.__get__(self, type(self))
        return f"价格已更新为: {self.price}"
    
    def update_stock(self, new_stock):
        """更新库存"""
        self._stock_validator.__set__(self, new_stock)
        self.stock = self._stock_validator.__get__(self, type(self))
        return f"库存已更新为: {self.stock}"
    
    def add_tag(self, tag):
        """添加标签"""
        if not isinstance(tag, str) or not tag.strip():
            raise ValueError("标签必须是非空字符串")
        
        tag = tag.strip().lower()
        if tag not in self.tags:
            self.tags.append(tag)
            self.tags.sort()
        
        return f"标签已添加: {tag}"
    
    def remove_tag(self, tag):
        """移除标签"""
        tag = tag.strip().lower()
        if tag in self.tags:
            self.tags.remove(tag)
            return f"标签已移除: {tag}"
        else:
            raise ValueError(f"标签不存在: {tag}")
    
    def get_info(self):
        """获取产品信息"""
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "category": self.category,
            "sku": self.sku,
            "tags": self.tags
        }

# 演示数据类验证
def demonstrate_dataclass_validation():
    """演示数据类验证"""
    print("\n=== 数据类验证演示 ===")
    
    # 创建有效的产品
    print("\n1. 创建有效产品:")
    try:
        product = Product(
            name="智能手机",
            description="最新款智能手机，功能强大",
            price=2999.99,
            stock=100,
            category="电子产品",
            sku="PHONE001",
            tags=["智能", "手机", "电子", "通讯"]
        )
        print(f"产品创建成功: {product.name}")
        print(f"产品信息: {product.get_info()}")
    except (ValueError, TypeError) as e:
        print(f"产品创建失败: {e}")
    
    # 测试无效数据
    print("\n2. 测试无效产品数据:")
    
    invalid_products = [
        {
            "data": {"name": "a", "price": 100, "stock": 10, "category": "测试", "sku": "TEST01"},
            "description": "名称太短"
        },
        {
            "data": {"name": "测试产品", "price": -100, "stock": 10, "category": "测试", "sku": "TEST01"},
            "description": "价格为负数"
        },
        {
            "data": {"name": "测试产品", "price": 100, "stock": -10, "category": "测试", "sku": "TEST01"},
            "description": "库存为负数"
        },
        {
            "data": {"name": "测试产品", "price": 100, "stock": 10, "category": "测试", "sku": "invalid"},
            "description": "SKU格式错误"
        },
        {
            "data": {"name": "测试产品", "price": 100, "stock": 10, "category": "测试", "sku": "TEST01", "tags": ["有效标签", ""]},
            "description": "包含空标签"
        }
    ]
    
    for item in invalid_products:
        try:
            Product(**item["data"])
            print(f"  {item['description']}: 验证失败（应该抛出异常）")
        except (ValueError, TypeError) as e:
            print(f"  {item['description']}: {e}")
    
    # 测试更新操作
    print("\n3. 测试产品更新:")
    try:
        result = product.update_price(3299.99)
        print(result)
        
        result = product.update_stock(80)
        print(result)
        
        result = product.add_tag("新品")
        print(result)
        
        result = product.remove_tag("电子")
        print(result)
        
        print(f"更新后的标签: {product.tags}")
    except (ValueError, TypeError) as e:
        print(f"更新失败: {e}")
    
    # 测试无效更新
    print("\n4. 测试无效更新:")
    try:
        product.update_price(-100)
    except ValueError as e:
        print(f"价格更新失败: {e}")
    
    try:
        product.add_tag("")
    except ValueError as e:
        print(f"标签添加失败: {e}")
    
    try:
        product.remove_tag("不存在的标签")
    except ValueError as e:
        print(f"标签移除失败: {e}")

# 运行演示
demonstrate_dataclass_validation()
```

### 4. 复合验证系统

```python
from typing import Dict, Any, Callable, List
import json
from datetime import datetime, date

class ValidationError(Exception):
    """验证错误异常"""
    
    def __init__(self, field, message, value=None):
        self.field = field
        self.message = message
        self.value = value
        super().__init__(f"{field}: {message}")

class ValidationResult:
    """验证结果"""
    
    def __init__(self):
        self.is_valid = True
        self.errors = []
        self.warnings = []
        self.cleaned_data = {}
    
    def add_error(self, field, message, value=None):
        """添加错误"""
        self.is_valid = False
        self.errors.append(ValidationError(field, message, value))
    
    def add_warning(self, field, message):
        """添加警告"""
        self.warnings.append({"field": field, "message": message})
    
    def get_error_summary(self):
        """获取错误摘要"""
        return {
            "is_valid": self.is_valid,
            "error_count": len(self.errors),
            "warning_count": len(self.warnings),
            "errors": [str(error) for error in self.errors],
            "warnings": self.warnings
        }

class Validator:
    """验证器基类"""
    
    def __init__(self, required=True, allow_none=False):
        self.required = required
        self.allow_none = allow_none
    
    def validate(self, value, field_name="field"):
        """验证值"""
        if value is None:
            if self.required and not self.allow_none:
                raise ValidationError(field_name, "字段是必需的")
            return None
        
        return self._validate_value(value, field_name)
    
    def _validate_value(self, value, field_name):
        """子类需要实现的验证逻辑"""
        raise NotImplementedError

class StringValidator(Validator):
    """字符串验证器"""
    
    def __init__(self, min_length=0, max_length=None, pattern=None, 
                 choices=None, strip=True, **kwargs):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length
        self.pattern = pattern
        self.choices = choices
        self.strip = strip
    
    def _validate_value(self, value, field_name):
        if not isinstance(value, str):
            raise ValidationError(field_name, "必须是字符串", value)
        
        if self.strip:
            value = value.strip()
        
        if len(value) < self.min_length:
            raise ValidationError(field_name, f"长度不能少于{self.min_length}个字符", value)
        
        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError(field_name, f"长度不能超过{self.max_length}个字符", value)
        
        if self.pattern is not None:
            import re
            if not re.match(self.pattern, value):
                raise ValidationError(field_name, "格式不正确", value)
        
        if self.choices is not None and value not in self.choices:
            raise ValidationError(field_name, f"必须是以下选项之一: {self.choices}", value)
        
        return value

class NumberValidator(Validator):
    """数字验证器"""
    
    def __init__(self, min_value=None, max_value=None, integer_only=False, **kwargs):
        super().__init__(**kwargs)
        self.min_value = min_value
        self.max_value = max_value
        self.integer_only = integer_only
    
    def _validate_value(self, value, field_name):
        if self.integer_only and not isinstance(value, int):
            raise ValidationError(field_name, "必须是整数", value)
        
        if not isinstance(value, (int, float)):
            raise ValidationError(field_name, "必须是数字", value)
        
        if self.min_value is not None and value < self.min_value:
            raise ValidationError(field_name, f"不能小于{self.min_value}", value)
        
        if self.max_value is not None and value > self.max_value:
            raise ValidationError(field_name, f"不能大于{self.max_value}", value)
        
        return value

class EmailValidator(Validator):
    """邮箱验证器"""
    
    def _validate_value(self, value, field_name):
        if not isinstance(value, str):
            raise ValidationError(field_name, "邮箱必须是字符串", value)
        
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, value.strip()):
            raise ValidationError(field_name, "邮箱格式不正确", value)
        
        return value.strip().lower()

class DateValidator(Validator):
    """日期验证器"""
    
    def __init__(self, min_date=None, max_date=None, **kwargs):
        super().__init__(**kwargs)
        self.min_date = min_date
        self.max_date = max_date
    
    def _validate_value(self, value, field_name):
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                raise ValidationError(field_name, "日期格式不正确，应为YYYY-MM-DD", value)
        
        if not isinstance(value, date):
            raise ValidationError(field_name, "必须是日期类型", value)
        
        if self.min_date is not None and value < self.min_date:
            raise ValidationError(field_name, f"日期不能早于{self.min_date}", value)
        
        if self.max_date is not None and value > self.max_date:
            raise ValidationError(field_name, f"日期不能晚于{self.max_date}", value)
        
        return value

class ListValidator(Validator):
    """列表验证器"""
    
    def __init__(self, item_validator=None, min_length=0, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.item_validator = item_validator
        self.min_length = min_length
        self.max_length = max_length
    
    def _validate_value(self, value, field_name):
        if not isinstance(value, list):
            raise ValidationError(field_name, "必须是列表", value)
        
        if len(value) < self.min_length:
            raise ValidationError(field_name, f"列表长度不能少于{self.min_length}", value)
        
        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError(field_name, f"列表长度不能超过{self.max_length}", value)
        
        if self.item_validator is not None:
            validated_items = []
            for i, item in enumerate(value):
                try:
                    validated_item = self.item_validator.validate(item, f"{field_name}[{i}]")
                    validated_items.append(validated_item)
                except ValidationError as e:
                    raise ValidationError(field_name, f"第{i+1}个元素验证失败: {e.message}", item)
            return validated_items
        
        return value

class Schema:
    """验证模式"""
    
    def __init__(self, fields: Dict[str, Validator]):
        self.fields = fields
    
    def validate(self, data: Dict[str, Any], strict=True) -> ValidationResult:
        """验证数据"""
        result = ValidationResult()
        
        # 检查必需字段
        for field_name, validator in self.fields.items():
            if field_name not in data:
                if validator.required:
                    result.add_error(field_name, "缺少必需字段")
                continue
            
            try:
                cleaned_value = validator.validate(data[field_name], field_name)
                result.cleaned_data[field_name] = cleaned_value
            except ValidationError as e:
                result.add_error(e.field, e.message, e.value)
        
        # 检查额外字段
        if strict:
            for field_name in data:
                if field_name not in self.fields:
                    result.add_warning(field_name, "未知字段")
        
        return result

class UserRegistration:
    """用户注册 - 复合验证示例"""
    
    # 定义验证模式
    SCHEMA = Schema({
        "username": StringValidator(
            min_length=3, 
            max_length=20, 
            pattern=r'^[a-zA-Z0-9_]+$'
        ),
        "email": EmailValidator(),
        "password": StringValidator(
            min_length=8, 
            max_length=128
        ),
        "confirm_password": StringValidator(
            min_length=8, 
            max_length=128
        ),
        "age": NumberValidator(
            min_value=13, 
            max_value=120, 
            integer_only=True
        ),
        "birth_date": DateValidator(
            min_date=date(1900, 1, 1),
            max_date=date.today()
        ),
        "interests": ListValidator(
            item_validator=StringValidator(min_length=1, max_length=50),
            min_length=1,
            max_length=10
        ),
        "gender": StringValidator(
            choices=["male", "female", "other", "prefer_not_to_say"]
        ),
        "phone": StringValidator(
            pattern=r'^1[3-9]\d{9}$',
            required=False
        )
    })
    
    def __init__(self):
        self._users = {}  # 存储已注册用户
    
    def register(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """注册用户"""
        # 基本验证
        validation_result = self.SCHEMA.validate(user_data)
        
        if not validation_result.is_valid:
            return {
                "success": False,
                "message": "数据验证失败",
                "validation_result": validation_result.get_error_summary()
            }
        
        cleaned_data = validation_result.cleaned_data
        
        # 业务逻辑验证
        try:
            self._validate_business_rules(cleaned_data)
        except ValidationError as e:
            return {
                "success": False,
                "message": "业务规则验证失败",
                "error": str(e)
            }
        
        # 注册用户
        user_id = self._create_user(cleaned_data)
        
        return {
            "success": True,
            "message": "用户注册成功",
            "user_id": user_id,
            "warnings": validation_result.warnings
        }
    
    def _validate_business_rules(self, data: Dict[str, Any]):
        """验证业务规则"""
        # 检查用户名是否已存在
        if data["username"] in self._users:
            raise ValidationError("username", "用户名已存在")
        
        # 检查邮箱是否已存在
        for user in self._users.values():
            if user["email"] == data["email"]:
                raise ValidationError("email", "邮箱已被注册")
        
        # 检查密码确认
        if data["password"] != data["confirm_password"]:
            raise ValidationError("confirm_password", "密码确认不匹配")
        
        # 检查密码强度
        password = data["password"]
        if not any(c.isupper() for c in password):
            raise ValidationError("password", "密码必须包含至少一个大写字母")
        
        if not any(c.islower() for c in password):
            raise ValidationError("password", "密码必须包含至少一个小写字母")
        
        if not any(c.isdigit() for c in password):
            raise ValidationError("password", "密码必须包含至少一个数字")
        
        # 检查年龄与生日的一致性
        today = date.today()
        birth_date = data["birth_date"]
        calculated_age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            calculated_age -= 1
        
        if abs(calculated_age - data["age"]) > 1:
            raise ValidationError("age", "年龄与生日不匹配")
    
    def _create_user(self, data: Dict[str, Any]) -> str:
        """创建用户"""
        import uuid
        user_id = str(uuid.uuid4())[:8]
        
        # 移除确认密码，不存储
        user_data = data.copy()
        del user_data["confirm_password"]
        
        # 添加元数据
        user_data.update({
            "user_id": user_id,
            "created_at": datetime.now(),
            "is_active": True
        })
        
        self._users[data["username"]] = user_data
        return user_id
    
    def get_user(self, username: str) -> Dict[str, Any]:
        """获取用户信息"""
        if username not in self._users:
            raise ValueError("用户不存在")
        
        user_data = self._users[username].copy()
        # 不返回密码
        del user_data["password"]
        return user_data
    
    def list_users(self) -> List[Dict[str, Any]]:
        """列出所有用户"""
        users = []
        for user_data in self._users.values():
            user_info = user_data.copy()
            del user_info["password"]  # 不返回密码
            users.append(user_info)
        return users

# 演示复合验证系统
def demonstrate_composite_validation():
    """演示复合验证系统"""
    print("\n=== 复合验证系统演示 ===")
    
    registration = UserRegistration()
    
    # 测试有效注册
    print("\n1. 测试有效用户注册:")
    valid_user_data = {
        "username": "alice_2024",
        "email": "alice@example.com",
        "password": "SecurePass123",
        "confirm_password": "SecurePass123",
        "age": 25,
        "birth_date": "1998-05-15",
        "interests": ["编程", "阅读", "旅行"],
        "gender": "female",
        "phone": "13812345678"
    }
    
    result = registration.register(valid_user_data)
    print(f"注册结果: {result}")
    
    if result["success"]:
        user_info = registration.get_user("alice_2024")
        print(f"用户信息: {user_info}")
    
    # 测试无效注册
    print("\n2. 测试无效用户注册:")
    
    invalid_user_data_list = [
        {
            "data": {
                "username": "ab",  # 用户名太短
                "email": "alice@example.com",
                "password": "SecurePass123",
                "confirm_password": "SecurePass123",
                "age": 25,
                "birth_date": "1998-05-15",
                "interests": ["编程"],
                "gender": "female"
            },
            "description": "用户名太短"
        },
        {
            "data": {
                "username": "bob_2024",
                "email": "invalid-email",  # 邮箱格式错误
                "password": "SecurePass123",
                "confirm_password": "SecurePass123",
                "age": 25,
                "birth_date": "1998-05-15",
                "interests": ["编程"],
                "gender": "male"
            },
            "description": "邮箱格式错误"
        },
        {
            "data": {
                "username": "charlie_2024",
                "email": "charlie@example.com",
                "password": "weak",  # 密码太弱
                "confirm_password": "weak",
                "age": 25,
                "birth_date": "1998-05-15",
                "interests": ["编程"],
                "gender": "male"
            },
            "description": "密码太弱"
        },
        {
            "data": {
                "username": "david_2024",
                "email": "david@example.com",
                "password": "SecurePass123",
                "confirm_password": "DifferentPass123",  # 密码确认不匹配
                "age": 25,
                "birth_date": "1998-05-15",
                "interests": ["编程"],
                "gender": "male"
            },
            "description": "密码确认不匹配"
        },
        {
            "data": {
                "username": "eve_2024",
                "email": "eve@example.com",
                "password": "SecurePass123",
                "confirm_password": "SecurePass123",
                "age": 30,
                "birth_date": "1998-05-15",  # 年龄与生日不匹配
                "interests": ["编程"],
                "gender": "female"
            },
            "description": "年龄与生日不匹配"
        }
    ]
    
    for item in invalid_user_data_list:
        result = registration.register(item["data"])
        print(f"\n  {item['description']}:")
        print(f"    成功: {result['success']}")
        print(f"    消息: {result['message']}")
        if "validation_result" in result:
            errors = result["validation_result"]["errors"]
            for error in errors:
                print(f"    错误: {error}")
        elif "error" in result:
            print(f"    错误: {result['error']}")
    
    # 测试重复注册
    print("\n3. 测试重复注册:")
    duplicate_user_data = {
        "username": "alice_2024",  # 重复用户名
        "email": "alice2@example.com",
        "password": "SecurePass123",
        "confirm_password": "SecurePass123",
        "age": 25,
        "birth_date": "1998-05-15",
        "interests": ["编程"],
        "gender": "female"
    }
    
    result = registration.register(duplicate_user_data)
    print(f"重复用户名注册: {result}")
    
    # 列出所有用户
    print("\n4. 用户列表:")
    users = registration.list_users()
    for user in users:
        print(f"  用户: {user['username']} ({user['email']})")

# 运行演示
demonstrate_composite_validation()
```

## 数据验证和保护的总结

```python
def demonstrate_validation_summary():
    """数据验证和保护总结"""
    print("\n=== 数据验证和保护总结 ===")
    
    print("\n1. 数据验证的核心原则:")
    print("   - 早期验证：在数据进入系统时立即验证")
    print("   - 多层验证：类型验证、格式验证、业务规则验证")
    print("   - 清晰错误：提供明确的错误信息")
    print("   - 安全防护：防止恶意输入和注入攻击")
    print("   - 用户友好：提供有用的错误提示")
    
    print("\n2. 验证层次结构:")
    print("   - 语法验证：数据类型、格式检查")
    print("   - 语义验证：业务规则、逻辑约束")
    print("   - 安全验证：权限检查、恶意输入防护")
    
    print("\n3. 实现技术:")
    print("   - 属性装饰器：@property getter/setter")
    print("   - 描述符：自定义验证逻辑")
    print("   - 数据类：dataclass + 验证")
    print("   - 验证器模式：可复用的验证组件")
    
    print("\n4. 安全考虑:")
    print("   - 输入清理：去除危险字符")
    print("   - 长度限制：防止缓冲区溢出")
    print("   - 类型检查：确保数据类型正确")
    print("   - 范围验证：确保数值在合理范围内")
    
    print("\n5. 性能优化:")
    print("   - 早期退出：第一个错误时停止验证")
    print("   - 缓存验证：避免重复验证")
    print("   - 批量验证：一次性验证多个字段")
    print("   - 异步验证：不阻塞主线程")
    
    print("\n6. 最佳实践:")
    print("   - 明确的错误消息")
    print("   - 一致的验证规则")
    print("   - 可测试的验证逻辑")
    print("   - 文档化的验证要求")
    print("   - 国际化的错误信息")

# 运行总结演示
demonstrate_validation_summary()

if __name__ == "__main__":
    print("数据验证和保护模块演示")
    print("=" * 50)
    
    # 运行所有演示
    demonstrate_basic_validation()
    demonstrate_complex_validation()
    demonstrate_dataclass_validation()
    demonstrate_composite_validation()
    demonstrate_validation_summary()
    
    print("\n" + "=" * 50)
    print("演示完成！")