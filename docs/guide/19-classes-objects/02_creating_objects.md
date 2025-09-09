# 对象的创建和实例化

## 学习目标
- 深入理解对象的实例化过程
- 掌握多个对象的创建和管理
- 理解对象的独立性和内存分配
- 学会对象的引用和赋值操作

## 对象实例化过程

### 实例化的基本概念

对象实例化是从类创建具体对象的过程。每次实例化都会在内存中创建一个新的对象。

```python
class Person:
    def __init__(self, name, age):
        print(f"正在创建 {name} 的对象...")
        self.name = name
        self.age = age
        print(f"{name} 对象创建完成！")
    
    def introduce(self):
        return f"我是 {self.name}，今年 {self.age} 岁"

# 实例化过程演示
print("=== 对象实例化过程 ===")
person1 = Person("张三", 25)  # 创建第一个对象
person2 = Person("李四", 30)  # 创建第二个对象

print("\n=== 对象信息 ===")
print(person1.introduce())
print(person2.introduce())
```

### 实例化的内部机制

```python
class Product:
    # 类属性：跟踪创建的对象数量
    total_products = 0
    
    def __init__(self, name, price):
        # 实例属性
        self.name = name
        self.price = price
        self.product_id = Product.total_products + 1
        
        # 更新类属性
        Product.total_products += 1
        
        print(f"产品 '{self.name}' 已创建，ID: {self.product_id}")
    
    def get_info(self):
        return f"产品ID: {self.product_id}, 名称: {self.name}, 价格: ¥{self.price}"
    
    @classmethod
    def get_total_count(cls):
        return cls.total_products

# 创建多个产品对象
print("=== 创建产品对象 ===")
product1 = Product("笔记本电脑", 5999)
product2 = Product("无线鼠标", 199)
product3 = Product("机械键盘", 599)

print("\n=== 产品信息 ===")
print(product1.get_info())
print(product2.get_info())
print(product3.get_info())

print(f"\n总共创建了 {Product.get_total_count()} 个产品")
```

## 多个对象的创建和管理

### 批量创建对象

```python
class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject
        self.scores = []
    
    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)
            return f"{self.name} 添加成绩: {score}"
        return "成绩必须在0-100之间"
    
    def get_average(self):
        if self.scores:
            return sum(self.scores) / len(self.scores)
        return 0
    
    def get_info(self):
        avg = self.get_average()
        return f"{self.name} ({self.grade}年级, {self.subject}) - 平均分: {avg:.1f}"

# 批量创建学生对象
student_data = [
    ("张三", 9, "数学"),
    ("李四", 9, "英语"),
    ("王五", 10, "物理"),
    ("赵六", 10, "化学"),
    ("钱七", 11, "生物")
]

print("=== 批量创建学生对象 ===")
students = []
for name, grade, subject in student_data:
    student = Student(name, grade, subject)
    students.append(student)
    print(f"创建学生: {student.get_info()}")

# 为学生添加成绩
print("\n=== 添加成绩 ===")
import random
for student in students:
    # 为每个学生随机添加3-5个成绩
    num_scores = random.randint(3, 5)
    for _ in range(num_scores):
        score = random.randint(60, 100)
        student.add_score(score)

# 显示学生信息
print("\n=== 学生成绩统计 ===")
for student in students:
    print(student.get_info())
    print(f"  成绩列表: {student.scores}")
```

### 使用字典管理对象

```python
class BankAccount:
    def __init__(self, account_holder, account_type="储蓄"):
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"存款: +¥{amount}")
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"取款: -¥{amount}")
            return True
        return False
    
    def get_summary(self):
        return {
            "持有人": self.account_holder,
            "账户类型": self.account_type,
            "余额": self.balance,
            "交易次数": len(self.transaction_history)
        }

# 使用字典管理银行账户
print("=== 银行账户管理系统 ===")
accounts = {}

# 创建账户的函数
def create_account(holder_name, account_type="储蓄"):
    account_id = f"ACC{len(accounts) + 1:04d}"
    accounts[account_id] = BankAccount(holder_name, account_type)
    print(f"账户 {account_id} 创建成功 - 持有人: {holder_name}")
    return account_id

# 创建多个账户
account_holders = ["张三", "李四", "王五", "赵六"]
account_types = ["储蓄", "支票", "储蓄", "支票"]

for holder, acc_type in zip(account_holders, account_types):
    create_account(holder, acc_type)

print("\n=== 账户操作 ===")
# 对账户进行操作
operations = [
    ("ACC0001", "deposit", 1000),
    ("ACC0002", "deposit", 1500),
    ("ACC0001", "withdraw", 200),
    ("ACC0003", "deposit", 800),
    ("ACC0002", "withdraw", 300),
    ("ACC0004", "deposit", 2000),
    ("ACC0001", "deposit", 500)
]

for account_id, operation, amount in operations:
    if account_id in accounts:
        account = accounts[account_id]
        if operation == "deposit":
            success = account.deposit(amount)
            action = "存款"
        else:
            success = account.withdraw(amount)
            action = "取款"
        
        status = "成功" if success else "失败"
        print(f"{account_id} {action} ¥{amount} - {status}")

print("\n=== 账户汇总 ===")
for account_id, account in accounts.items():
    print(f"\n账户 {account_id}:")
    summary = account.get_summary()
    for key, value in summary.items():
        print(f"  {key}: {value}")
    print(f"  最近交易: {account.transaction_history[-3:] if account.transaction_history else '无'}")
```

## 对象的独立性

### 对象状态的独立性

```python
class Counter:
    def __init__(self, name, initial_value=0):
        self.name = name
        self.value = initial_value
        self.history = [initial_value]
    
    def increment(self, step=1):
        self.value += step
        self.history.append(self.value)
        return self.value
    
    def decrement(self, step=1):
        self.value -= step
        self.history.append(self.value)
        return self.value
    
    def reset(self):
        self.value = 0
        self.history.append(0)
    
    def get_status(self):
        return {
            "名称": self.name,
            "当前值": self.value,
            "操作次数": len(self.history) - 1,
            "历史记录": self.history
        }

# 创建多个独立的计数器
print("=== 对象独立性演示 ===")
counter1 = Counter("计数器A", 10)
counter2 = Counter("计数器B", 5)
counter3 = Counter("计数器C")

print("初始状态:")
for counter in [counter1, counter2, counter3]:
    status = counter.get_status()
    print(f"  {status['名称']}: {status['当前值']}")

print("\n=== 独立操作 ===")
# 对不同计数器进行不同操作
counter1.increment(5)
counter1.increment(3)
counter1.decrement(2)

counter2.decrement(2)
counter2.increment(10)
counter2.increment(1)

counter3.increment(1)
counter3.increment(1)
counter3.reset()
counter3.increment(20)

print("操作后状态:")
for counter in [counter1, counter2, counter3]:
    status = counter.get_status()
    print(f"\n{status['名称']}:")
    print(f"  当前值: {status['当前值']}")
    print(f"  操作次数: {status['操作次数']}")
    print(f"  历史记录: {status['历史记录']}")
```

### 对象属性的独立修改

```python
class Configuration:
    def __init__(self, app_name):
        self.app_name = app_name
        self.settings = {
            "debug": False,
            "port": 8000,
            "host": "localhost",
            "database_url": "sqlite:///app.db"
        }
        self.created_at = self._get_timestamp()
    
    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def update_setting(self, key, value):
        if key in self.settings:
            old_value = self.settings[key]
            self.settings[key] = value
            return f"{key}: {old_value} -> {value}"
        return f"设置项 '{key}' 不存在"
    
    def get_config_summary(self):
        return {
            "应用名称": self.app_name,
            "创建时间": self.created_at,
            "设置项数量": len(self.settings),
            "当前设置": self.settings.copy()
        }

# 创建不同应用的配置对象
print("=== 配置对象独立性 ===")
web_config = Configuration("Web应用")
api_config = Configuration("API服务")
worker_config = Configuration("后台任务")

print("初始配置:")
for config in [web_config, api_config, worker_config]:
    summary = config.get_config_summary()
    print(f"\n{summary['应用名称']}:")
    for key, value in summary['当前设置'].items():
        print(f"  {key}: {value}")

print("\n=== 独立修改配置 ===")
# 为不同应用设置不同的配置
print("Web应用配置修改:")
print(f"  {web_config.update_setting('debug', True)}")
print(f"  {web_config.update_setting('port', 3000)}")

print("\nAPI服务配置修改:")
print(f"  {api_config.update_setting('port', 8080)}")
print(f"  {api_config.update_setting('host', '0.0.0.0')}")

print("\n后台任务配置修改:")
print(f"  {worker_config.update_setting('database_url', 'postgresql://localhost/worker')}")

print("\n=== 修改后的配置 ===")
for config in [web_config, api_config, worker_config]:
    summary = config.get_config_summary()
    print(f"\n{summary['应用名称']} (创建于 {summary['创建时间']}):")
    for key, value in summary['当前设置'].items():
        print(f"  {key}: {value}")
```

## 对象的内存分配

### 内存地址和对象标识

```python
class MemoryDemo:
    def __init__(self, name, data):
        self.name = name
        self.data = data
    
    def __str__(self):
        return f"MemoryDemo(name='{self.name}', data={self.data})"
    
    def __repr__(self):
        return self.__str__()

# 创建对象并观察内存分配
print("=== 对象内存分配演示 ===")

# 创建多个对象
objects = []
for i in range(5):
    obj = MemoryDemo(f"对象{i+1}", i * 10)
    objects.append(obj)
    print(f"创建 {obj}")
    print(f"  内存地址: {hex(id(obj))}")
    print(f"  对象类型: {type(obj)}")

print("\n=== 对象引用和比较 ===")
obj1 = MemoryDemo("测试1", 100)
obj2 = MemoryDemo("测试1", 100)  # 内容相同但是不同对象
obj3 = obj1  # 引用同一个对象

print(f"obj1: {obj1} (地址: {hex(id(obj1))})")
print(f"obj2: {obj2} (地址: {hex(id(obj2))})")
print(f"obj3: {obj3} (地址: {hex(id(obj3))})")

print("\n对象比较:")
print(f"obj1 is obj2: {obj1 is obj2}")  # False - 不同对象
print(f"obj1 is obj3: {obj1 is obj3}")  # True - 同一对象
print(f"obj1 == obj2: {obj1 == obj2}")  # False - 默认比较对象标识

# 修改对象属性观察影响
print("\n=== 修改对象属性 ===")
print("修改前:")
print(f"  obj1.data: {obj1.data}")
print(f"  obj3.data: {obj3.data}")

obj1.data = 999
print("修改 obj1.data = 999 后:")
print(f"  obj1.data: {obj1.data}")
print(f"  obj3.data: {obj3.data}")  # obj3也会改变，因为指向同一对象
print(f"  obj2.data: {obj2.data}")  # obj2不变，因为是不同对象
```

### 对象的生命周期

```python
class LifecycleDemo:
    # 类属性：跟踪对象数量
    instance_count = 0
    
    def __init__(self, name):
        self.name = name
        LifecycleDemo.instance_count += 1
        self.instance_id = LifecycleDemo.instance_count
        print(f"对象 '{self.name}' 创建 (ID: {self.instance_id})")
    
    def __del__(self):
        print(f"对象 '{self.name}' 被销毁 (ID: {self.instance_id})")
    
    def get_info(self):
        return f"对象: {self.name} (ID: {self.instance_id})"
    
    @classmethod
    def get_instance_count(cls):
        return cls.instance_count

# 对象生命周期演示
print("=== 对象生命周期演示 ===")

def create_temporary_objects():
    """创建临时对象的函数"""
    print("\n在函数中创建临时对象:")
    temp1 = LifecycleDemo("临时对象1")
    temp2 = LifecycleDemo("临时对象2")
    
    print(f"函数内对象信息:")
    print(f"  {temp1.get_info()}")
    print(f"  {temp2.get_info()}")
    print(f"当前总对象数: {LifecycleDemo.get_instance_count()}")
    
    return temp1  # 只返回一个对象

# 创建持久对象
persistent_obj = LifecycleDemo("持久对象")
print(f"创建持久对象: {persistent_obj.get_info()}")

# 调用函数创建临时对象
returned_obj = create_temporary_objects()
print(f"\n函数返回的对象: {returned_obj.get_info()}")
print("注意：temp2在函数结束时被自动销毁")

# 创建对象列表
print("\n=== 创建对象列表 ===")
object_list = []
for i in range(3):
    obj = LifecycleDemo(f"列表对象{i+1}")
    object_list.append(obj)

print(f"\n当前对象列表:")
for obj in object_list:
    print(f"  {obj.get_info()}")

print(f"\n总对象数: {LifecycleDemo.get_instance_count()}")

# 删除部分对象
print("\n=== 删除对象 ===")
del object_list[1]  # 删除列表中的一个对象
print("删除列表中的第二个对象")

object_list.clear()  # 清空列表
print("清空对象列表")

print(f"\n剩余对象:")
print(f"  {persistent_obj.get_info()}")
print(f"  {returned_obj.get_info()}")
```

## 实际应用示例

### 任务管理系统

```python
from datetime import datetime, timedelta

class Task:
    # 任务状态常量
    STATUS_PENDING = "待处理"
    STATUS_IN_PROGRESS = "进行中"
    STATUS_COMPLETED = "已完成"
    STATUS_CANCELLED = "已取消"
    
    def __init__(self, title, description="", priority="中"):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = self.STATUS_PENDING
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.completed_at = None
    
    def start_task(self):
        if self.status == self.STATUS_PENDING:
            self.status = self.STATUS_IN_PROGRESS
            self.updated_at = datetime.now()
            return f"任务 '{self.title}' 已开始"
        return f"任务 '{self.title}' 无法开始，当前状态: {self.status}"
    
    def complete_task(self):
        if self.status == self.STATUS_IN_PROGRESS:
            self.status = self.STATUS_COMPLETED
            self.completed_at = datetime.now()
            self.updated_at = self.completed_at
            return f"任务 '{self.title}' 已完成"
        return f"任务 '{self.title}' 无法完成，当前状态: {self.status}"
    
    def cancel_task(self):
        if self.status in [self.STATUS_PENDING, self.STATUS_IN_PROGRESS]:
            self.status = self.STATUS_CANCELLED
            self.updated_at = datetime.now()
            return f"任务 '{self.title}' 已取消"
        return f"任务 '{self.title}' 无法取消，当前状态: {self.status}"
    
    def get_duration(self):
        if self.completed_at:
            return self.completed_at - self.created_at
        return datetime.now() - self.created_at
    
    def get_summary(self):
        duration = self.get_duration()
        return {
            "标题": self.title,
            "描述": self.description,
            "优先级": self.priority,
            "状态": self.status,
            "创建时间": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "持续时间": str(duration).split('.')[0],  # 去掉微秒
            "完成时间": self.completed_at.strftime("%Y-%m-%d %H:%M:%S") if self.completed_at else "未完成"
        }

class TaskManager:
    def __init__(self, manager_name):
        self.manager_name = manager_name
        self.tasks = []
        self.created_at = datetime.now()
    
    def add_task(self, title, description="", priority="中"):
        task = Task(title, description, priority)
        self.tasks.append(task)
        return f"任务 '{title}' 已添加"
    
    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]
    
    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]
    
    def get_statistics(self):
        total = len(self.tasks)
        pending = len(self.get_tasks_by_status(Task.STATUS_PENDING))
        in_progress = len(self.get_tasks_by_status(Task.STATUS_IN_PROGRESS))
        completed = len(self.get_tasks_by_status(Task.STATUS_COMPLETED))
        cancelled = len(self.get_tasks_by_status(Task.STATUS_CANCELLED))
        
        return {
            "管理员": self.manager_name,
            "总任务数": total,
            "待处理": pending,
            "进行中": in_progress,
            "已完成": completed,
            "已取消": cancelled,
            "完成率": f"{(completed/total*100):.1f}%" if total > 0 else "0%"
        }

# 任务管理系统演示
print("=== 任务管理系统演示 ===")

# 创建任务管理器
manager = TaskManager("项目经理")

# 添加任务
tasks_to_add = [
    ("设计数据库结构", "设计用户、订单、产品表结构", "高"),
    ("实现用户注册功能", "包括邮箱验证和密码加密", "高"),
    ("编写API文档", "使用Swagger编写接口文档", "中"),
    ("设置CI/CD流程", "配置自动化测试和部署", "中"),
    ("优化数据库查询", "分析慢查询并优化", "低")
]

print("添加任务:")
for title, desc, priority in tasks_to_add:
    print(f"  {manager.add_task(title, desc, priority)}")

# 执行任务操作
print("\n=== 任务操作 ===")
print(manager.tasks[0].start_task())  # 开始第一个任务
print(manager.tasks[1].start_task())  # 开始第二个任务
print(manager.tasks[0].complete_task())  # 完成第一个任务
print(manager.tasks[2].start_task())  # 开始第三个任务
print(manager.tasks[4].cancel_task())  # 取消第五个任务

# 显示统计信息
print("\n=== 任务统计 ===")
stats = manager.get_statistics()
for key, value in stats.items():
    print(f"{key}: {value}")

# 显示各状态任务详情
print("\n=== 任务详情 ===")
for status in [Task.STATUS_PENDING, Task.STATUS_IN_PROGRESS, Task.STATUS_COMPLETED, Task.STATUS_CANCELLED]:
    tasks = manager.get_tasks_by_status(status)
    if tasks:
        print(f"\n{status} ({len(tasks)}个):")
        for task in tasks:
            summary = task.get_summary()
            print(f"  • {summary['标题']} [{summary['优先级']}] - {summary['持续时间']}")
```

## 学习要点总结

### 核心概念
1. **实例化过程**：类名() → 调用__init__ → 创建对象
2. **对象独立性**：每个对象都有独立的属性空间
3. **内存分配**：每个对象在内存中有唯一的地址
4. **对象引用**：变量存储的是对象的引用，不是对象本身

### 重要特性
1. **对象唯一性**：每次实例化都创建新对象（除非特殊设计）
2. **属性独立性**：修改一个对象的属性不影响其他对象
3. **方法共享性**：所有对象共享类中定义的方法
4. **生命周期**：对象从创建到销毁的完整过程

### 最佳实践
1. **合理的初始化**：在__init__中设置必要的初始状态
2. **对象管理**：使用列表、字典等容器管理多个对象
3. **资源清理**：必要时实现__del__方法进行清理
4. **状态跟踪**：使用类属性跟踪全局状态

### 注意事项
1. 对象赋值是引用赋值，不是复制
2. 修改可变对象的属性会影响所有引用
3. 函数参数传递对象时传递的是引用
4. 垃圾回收会自动清理无引用的对象

## 练习建议

1. **基础练习**：创建一个 `Book` 类，实现图书的借阅管理功能

2. **进阶练习**：设计一个 `ShoppingCart` 类，支持添加商品、计算总价等功能

3. **综合练习**：实现一个简单的 `GamePlayer` 类，包含等级、经验值、装备等属性

## 下一步学习

掌握了对象的创建和实例化后，接下来学习：
- [实例方法的定义和使用](./03_instance_methods.md)
- [实例属性的操作](./04_instance_attributes.md)
- [构造方法__init__](./05_constructor_method.md)