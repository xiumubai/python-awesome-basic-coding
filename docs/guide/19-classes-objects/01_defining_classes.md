# 类的定义基础

## 学习目标
- 理解面向对象编程的基本概念
- 掌握Python中类的定义语法
- 学会创建简单的类和对象
- 理解类和对象的关系

## 面向对象编程概念

面向对象编程（Object-Oriented Programming，OOP）是一种编程范式，它将数据和操作数据的方法组织在一起，形成对象。

### 核心概念
- **类（Class）**：对象的模板或蓝图
- **对象（Object）**：类的实例
- **属性（Attribute）**：对象的数据
- **方法（Method）**：对象的行为

## 基本类定义

### 最简单的类

```python
# 定义一个最简单的类
class Person:
    pass  # pass表示空的代码块

# 创建对象
person1 = Person()
person2 = Person()

print(f"person1的类型: {type(person1)}")
print(f"person2的类型: {type(person2)}")
print(f"person1和person2是同一个对象吗？ {person1 is person2}")
```

### 带属性的类

```python
class Student:
    # 类属性（所有实例共享）
    school = "Python学院"
    
    def __init__(self, name, age):
        # 实例属性（每个实例独有）
        self.name = name
        self.age = age

# 创建学生对象
student1 = Student("张三", 20)
student2 = Student("李四", 19)

print(f"学生1: {student1.name}, 年龄: {student1.age}, 学校: {student1.school}")
print(f"学生2: {student2.name}, 年龄: {student2.age}, 学校: {student2.school}")
```

### 带方法的类

```python
class Calculator:
    def __init__(self, name):
        self.name = name
        self.result = 0
    
    def add(self, number):
        """加法运算"""
        self.result += number
        return self.result
    
    def subtract(self, number):
        """减法运算"""
        self.result -= number
        return self.result
    
    def get_result(self):
        """获取当前结果"""
        return self.result
    
    def reset(self):
        """重置计算器"""
        self.result = 0

# 使用计算器
calc = Calculator("我的计算器")
print(f"计算器名称: {calc.name}")
print(f"初始结果: {calc.get_result()}")

print(f"加10: {calc.add(10)}")
print(f"减3: {calc.subtract(3)}")
print(f"当前结果: {calc.get_result()}")

calc.reset()
print(f"重置后结果: {calc.get_result()}")
```

## 类的命名规范

### PascalCase命名

```python
# 正确的类名命名
class BankAccount:  # 银行账户
    pass

class UserProfile:  # 用户资料
    pass

class DatabaseConnection:  # 数据库连接
    pass

# 错误的命名方式
# class bank_account:  # 不推荐：使用下划线
# class bankaccount:   # 不推荐：全小写
# class BANKACCOUNT:   # 不推荐：全大写
```

### 有意义的类名

```python
# 好的类名：清楚表达类的用途
class EmailValidator:
    def validate(self, email):
        return "@" in email and "." in email

class FileManager:
    def __init__(self, directory):
        self.directory = directory
    
    def list_files(self):
        return f"列出{self.directory}目录下的文件"

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        return f"已添加商品: {item}"

# 使用示例
validator = EmailValidator()
print(validator.validate("test@example.com"))  # True
print(validator.validate("invalid-email"))     # False

file_mgr = FileManager("/home/user/documents")
print(file_mgr.list_files())

cart = ShoppingCart()
print(cart.add_item("苹果"))
print(cart.add_item("香蕉"))
print(f"购物车商品: {cart.items}")
```

## 类和对象的关系

### 类是模板，对象是实例

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.brand} {self.model} 已启动"
        return f"{self.brand} {self.model} 已经在运行中"
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            return f"{self.brand} {self.model} 已停止"
        return f"{self.brand} {self.model} 已经停止了"
    
    def get_info(self):
        status = "运行中" if self.is_running else "已停止"
        return f"{self.year}年 {self.brand} {self.model} - 状态: {status}"

# 从同一个类创建多个不同的对象
car1 = Car("丰田", "卡罗拉", 2022)
car2 = Car("本田", "雅阁", 2023)
car3 = Car("宝马", "X5", 2024)

# 每个对象都有独立的属性和状态
print("=== 初始状态 ===")
print(car1.get_info())
print(car2.get_info())
print(car3.get_info())

print("\n=== 启动部分车辆 ===")
print(car1.start())
print(car3.start())

print("\n=== 查看状态 ===")
print(car1.get_info())
print(car2.get_info())
print(car3.get_info())

print("\n=== 停止车辆 ===")
print(car1.stop())
print(car2.stop())  # 本来就是停止状态
```

## 对象的内存和标识

### 对象的唯一性

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"《{self.title}》 - {self.author}"

# 创建多个书籍对象
book1 = Book("Python编程", "张三")
book2 = Book("Python编程", "张三")  # 内容相同但是不同的对象
book3 = book1  # 指向同一个对象

print("=== 对象内容 ===")
print(f"book1: {book1}")
print(f"book2: {book2}")
print(f"book3: {book3}")

print("\n=== 对象标识 ===")
print(f"book1的id: {id(book1)}")
print(f"book2的id: {id(book2)}")
print(f"book3的id: {id(book3)}")

print("\n=== 对象比较 ===")
print(f"book1 is book2: {book1 is book2}")  # False，不同对象
print(f"book1 is book3: {book1 is book3}")  # True，同一对象
print(f"book1 == book2: {book1 == book2}")  # False，默认比较对象标识

# 修改一个对象的属性
book1.title = "高级Python编程"
print("\n=== 修改book1后 ===")
print(f"book1: {book1}")
print(f"book2: {book2}")
print(f"book3: {book3}")  # book3和book1指向同一对象，所以也会改变
```

## 实际应用示例

### 银行账户类

```python
class BankAccount:
    # 类属性：银行名称
    bank_name = "Python银行"
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self._generate_account_number()
    
    def _generate_account_number(self):
        """生成账户号码（私有方法）"""
        import random
        return f"ACC{random.randint(100000, 999999)}"
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.balance += amount
            return f"存款成功！当前余额: ¥{self.balance}"
        return "存款金额必须大于0"
    
    def withdraw(self, amount):
        """取款"""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"取款成功！当前余额: ¥{self.balance}"
            return "余额不足"
        return "取款金额必须大于0"
    
    def get_balance(self):
        """查询余额"""
        return self.balance
    
    def get_account_info(self):
        """获取账户信息"""
        return {
            "银行": self.bank_name,
            "账户持有人": self.account_holder,
            "账户号码": self.account_number,
            "余额": self.balance
        }

# 使用银行账户类
print("=== 创建银行账户 ===")
account1 = BankAccount("张三", 1000)
account2 = BankAccount("李四")

print("账户1信息:")
for key, value in account1.get_account_info().items():
    print(f"  {key}: {value}")

print("\n账户2信息:")
for key, value in account2.get_account_info().items():
    print(f"  {key}: {value}")

print("\n=== 账户操作 ===")
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.withdraw(2000))  # 余额不足

print(account2.deposit(300))
print(account2.withdraw(100))

print("\n=== 最终账户状态 ===")
print(f"账户1余额: ¥{account1.get_balance()}")
print(f"账户2余额: ¥{account2.get_balance()}")
```

## 学习要点总结

### 关键概念
1. **类定义**：使用 `class` 关键字定义类
2. **对象创建**：通过类名()创建对象实例
3. **属性**：对象的数据，通过 `self.属性名` 访问
4. **方法**：对象的行为，第一个参数必须是 `self`
5. **构造方法**：`__init__` 方法用于初始化对象

### 最佳实践
1. **命名规范**：类名使用PascalCase（首字母大写）
2. **有意义的名称**：类名应该清楚表达类的用途
3. **封装性**：将相关的数据和方法组织在一起
4. **文档字符串**：为类和方法添加说明文档

### 注意事项
1. 每个对象都是独立的，有自己的属性值
2. 类属性被所有实例共享
3. 实例属性每个对象都有独立的副本
4. `self` 参数代表当前对象实例

## 练习建议

1. **基础练习**：创建一个 `Rectangle` 类，包含长度和宽度属性，以及计算面积和周长的方法

2. **进阶练习**：设计一个 `Student` 类，包含姓名、年龄、成绩等属性，以及添加成绩、计算平均分等方法

3. **综合练习**：实现一个简单的 `Library` 类，可以添加书籍、借书、还书等功能

## 下一步学习

掌握了类的基本定义后，接下来学习：
- [对象的创建和实例化](./02_creating_objects.md)
- [实例方法的定义和使用](./03_instance_methods.md)
- [实例属性的操作](./04_instance_attributes.md)