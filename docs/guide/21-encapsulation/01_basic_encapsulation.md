# 封装的基本概念和意义

封装（Encapsulation）是面向对象编程的核心概念之一，它将数据和操作数据的方法绑定在一起，并隐藏对象的内部实现细节。

## 什么是封装？

封装是一种编程技术，它：
- **数据隐藏**：将对象的内部状态隐藏起来
- **接口暴露**：只暴露必要的操作接口
- **实现保护**：防止外部代码直接修改内部数据
- **职责分离**：将数据和操作数据的方法组织在一起

## 基本示例：没有封装的问题

```python
# 没有封装的银行账户类
class BankAccountBad:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance  # 余额可以被直接访问和修改

# 使用示例
account = BankAccountBad("123456", 1000)
print(f"初始余额: {account.balance}")

# 问题：可以直接修改余额，绕过任何验证
account.balance = -500  # 这是不合理的！
print(f"修改后余额: {account.balance}")

# 问题：可以直接修改账户号码
account.account_number = "999999"  # 这也是不合理的！
print(f"修改后账户号: {account.account_number}")
```

## 基本封装实现

```python
# 使用封装的银行账户类
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self._account_number = account_number  # 受保护的属性
        self._balance = initial_balance        # 受保护的属性
        self._transaction_history = []         # 私有数据
    
    # 公共接口：获取账户信息
    def get_account_number(self):
        """获取账户号码"""
        return self._account_number
    
    def get_balance(self):
        """获取当前余额"""
        return self._balance
    
    # 公共接口：安全的操作方法
    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        
        self._balance += amount
        self._transaction_history.append(f"存款: +{amount}")
        return self._balance
    
    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        
        if amount > self._balance:
            raise ValueError("余额不足")
        
        self._balance -= amount
        self._transaction_history.append(f"取款: -{amount}")
        return self._balance
    
    def get_transaction_history(self):
        """获取交易历史（只读）"""
        return self._transaction_history.copy()  # 返回副本，防止外部修改
    
    def __str__(self):
        return f"账户 {self._account_number}: 余额 {self._balance}"
```

## 封装的优势演示

```python
def demonstrate_encapsulation_benefits():
    """演示封装的优势"""
    print("=== 封装的优势演示 ===")
    
    # 创建账户
    account = BankAccount("123456789", 1000)
    print(f"创建账户: {account}")
    
    # 1. 数据验证
    print("\n1. 数据验证:")
    try:
        account.deposit(-100)  # 尝试存入负数
    except ValueError as e:
        print(f"存款验证: {e}")
    
    try:
        account.withdraw(2000)  # 尝试取出超过余额的金额
    except ValueError as e:
        print(f"取款验证: {e}")
    
    # 2. 安全操作
    print("\n2. 安全操作:")
    account.deposit(500)
    print(f"存款后: {account}")
    
    account.withdraw(200)
    print(f"取款后: {account}")
    
    # 3. 数据保护
    print("\n3. 数据保护:")
    # 无法直接修改内部数据
    # account._balance = 999999  # 虽然技术上可行，但违反了封装原则
    
    # 4. 接口一致性
    print("\n4. 接口一致性:")
    print(f"账户号码: {account.get_account_number()}")
    print(f"当前余额: {account.get_balance()}")
    
    # 5. 内部状态管理
    print("\n5. 交易历史:")
    for transaction in account.get_transaction_history():
        print(f"  {transaction}")

# 运行演示
demonstrate_encapsulation_benefits()
```

## 封装的层次

```python
# 演示不同层次的封装
class Student:
    def __init__(self, name, student_id):
        # 公有属性（约定）
        self.name = name
        
        # 受保护属性（约定：单下划线）
        self._student_id = student_id
        
        # 私有属性（约定：双下划线）
        self.__grades = []
        
        # 内部状态
        self.__total_credits = 0
    
    # 公有方法
    def get_info(self):
        """获取学生基本信息"""
        return f"学生: {self.name} (ID: {self._student_id})"
    
    # 受保护方法（约定：单下划线）
    def _calculate_gpa(self):
        """计算GPA（内部使用）"""
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)
    
    # 私有方法（约定：双下划线）
    def __validate_grade(self, grade):
        """验证成绩（严格内部使用）"""
        return 0 <= grade <= 100
    
    # 公有接口
    def add_grade(self, grade, credits=3):
        """添加成绩"""
        if not self.__validate_grade(grade):
            raise ValueError("成绩必须在0-100之间")
        
        self.__grades.append(grade)
        self.__total_credits += credits
        print(f"添加成绩: {grade} (学分: {credits})")
    
    def get_gpa(self):
        """获取GPA"""
        return self._calculate_gpa()
    
    def get_summary(self):
        """获取学习总结"""
        return {
            'name': self.name,
            'student_id': self._student_id,
            'gpa': self._calculate_gpa(),
            'total_credits': self.__total_credits,
            'courses_taken': len(self.__grades)
        }

# 使用示例
def demonstrate_encapsulation_levels():
    """演示封装层次"""
    print("\n=== 封装层次演示 ===")
    
    student = Student("张三", "2023001")
    print(student.get_info())
    
    # 添加成绩
    student.add_grade(85, 4)
    student.add_grade(92, 3)
    student.add_grade(78, 2)
    
    # 获取总结
    summary = student.get_summary()
    print(f"\n学习总结:")
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    # 访问不同层次的属性
    print(f"\n访问测试:")
    print(f"公有属性 name: {student.name}")
    print(f"受保护属性 _student_id: {student._student_id}")
    
    # 私有属性无法直接访问（会报错）
    # print(student.__grades)  # AttributeError
    
    # 但可以通过名称修饰访问（不推荐）
    print(f"私有属性（通过名称修饰）: {student._Student__grades}")

# 运行演示
demonstrate_encapsulation_levels()
```

## 封装的设计原则

```python
# 良好封装设计的示例
class TemperatureConverter:
    """温度转换器 - 展示良好的封装设计"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    # 使用属性装饰器提供清晰的接口
    @property
    def celsius(self):
        """摄氏温度"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """设置摄氏温度"""
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度(-273.15°C)")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """华氏温度（只读）"""
        return self._celsius * 9/5 + 32
    
    @property
    def kelvin(self):
        """开尔文温度（只读）"""
        return self._celsius + 273.15
    
    def __str__(self):
        return f"{self._celsius}°C = {self.fahrenheit}°F = {self.kelvin}K"

# 使用示例
def demonstrate_good_encapsulation():
    """演示良好的封装设计"""
    print("\n=== 良好封装设计演示 ===")
    
    temp = TemperatureConverter(25)
    print(f"初始温度: {temp}")
    
    # 修改温度
    temp.celsius = 100
    print(f"修改后: {temp}")
    
    # 尝试设置无效温度
    try:
        temp.celsius = -300
    except ValueError as e:
        print(f"验证错误: {e}")
    
    # 只能读取计算属性
    print(f"华氏温度: {temp.fahrenheit}")
    print(f"开尔文温度: {temp.kelvin}")

# 运行演示
demonstrate_good_encapsulation()
```

## 学习要点

### 封装的核心原则

1. **隐藏实现细节**：外部代码不需要知道内部如何工作
2. **提供清晰接口**：通过方法提供对数据的受控访问
3. **数据验证**：在修改数据时进行必要的验证
4. **职责分离**：将相关的数据和方法组织在一起

### 封装的优势

- **数据安全**：防止无效数据破坏对象状态
- **代码维护**：内部实现可以改变而不影响外部代码
- **接口稳定**：提供一致的操作接口
- **错误减少**：通过验证减少程序错误

### 注意事项

- Python的封装是基于约定的，不是强制的
- 合理使用不同层次的访问控制
- 平衡封装和灵活性
- 重视接口设计的易用性

## 最佳实践

1. **使用下划线约定**：`_protected`、`__private`
2. **提供清晰的公共接口**：方法名要有意义
3. **进行数据验证**：在setter中验证输入
4. **返回副本而非原始数据**：防止外部修改内部状态
5. **文档化接口**：为公共方法提供清晰的文档

封装是面向对象编程的基础，掌握好封装技术是编写高质量Python代码的关键。