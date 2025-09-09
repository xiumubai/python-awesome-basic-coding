#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
构造方法__init__

本文件演示Python中构造方法__init__的详细用法：
1. 构造方法的基本概念
2. 基本的构造方法定义
3. 带参数的构造方法
4. 默认参数和可变参数
5. 构造方法中的验证和异常处理
6. 调用父类构造方法
7. 构造方法的重载模拟
8. 实际应用示例

作者: Python学习助手
日期: 2024
"""

print("=== Python构造方法__init__学习 ===")
print()

# 1. 构造方法的基本概念
print("=== 1. 构造方法的基本概念 ===")

class SimpleClass:
    """简单类 - 演示基本构造方法"""
    
    def __init__(self):
        """构造方法 - 在对象创建时自动调用"""
        print("SimpleClass对象正在创建...")
        self.created = True
        self.message = "Hello from SimpleClass!"
        print("SimpleClass对象创建完成")
    
    def show_info(self):
        """显示对象信息"""
        print(f"对象状态: created={self.created}, message='{self.message}'")

print("创建SimpleClass对象:")
obj1 = SimpleClass()  # 自动调用__init__方法
obj1.show_info()
print()

# 2. 基本的构造方法定义
print("=== 2. 基本的构造方法定义 ===")

class Person:
    """人员类 - 基本构造方法"""
    
    def __init__(self, name, age):
        """构造方法 - 接收姓名和年龄参数"""
        print(f"正在创建Person对象: {name}, {age}岁")
        self.name = name
        self.age = age
        self.id = id(self)  # 对象的唯一标识
        print(f"Person对象创建完成，ID: {self.id}")
    
    def introduce(self):
        """自我介绍"""
        print(f"大家好，我是{self.name}，今年{self.age}岁")
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

# 创建Person对象
print("创建Person对象:")
person1 = Person("张三", 25)
person2 = Person("李四", 30)

print(f"person1: {person1}")
print(f"person2: {person2}")
person1.introduce()
person2.introduce()
print()

# 3. 带参数的构造方法
print("=== 3. 带参数的构造方法 ===")

class Student:
    """学生类 - 带多种参数的构造方法"""
    
    def __init__(self, name, age, student_id, grade, subjects=None):
        """构造方法 - 多种类型参数"""
        # 基本信息
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grade = grade
        
        # 处理可选参数
        self.subjects = subjects if subjects is not None else []
        
        # 初始化其他属性
        self.scores = {}
        self.enrollment_date = None
        self.is_active = True
        
        print(f"学生 {self.name} (学号: {self.student_id}) 创建成功")
    
    def add_subject(self, subject):
        """添加科目"""
        if subject not in self.subjects:
            self.subjects.append(subject)
            self.scores[subject] = None
            print(f"已为 {self.name} 添加科目: {subject}")
    
    def set_score(self, subject, score):
        """设置成绩"""
        if subject in self.subjects:
            self.scores[subject] = score
            print(f"{self.name} 的 {subject} 成绩设置为: {score}")
        else:
            print(f"科目 {subject} 不存在，请先添加")
    
    def __str__(self):
        return f"Student(name='{self.name}', grade='{self.grade}', subjects={len(self.subjects)})"

# 创建学生对象
print("创建Student对象:")
student1 = Student("王五", 16, "S001", "高一", ["数学", "物理"])
student2 = Student("赵六", 17, "S002", "高二")  # 没有初始科目

print(f"student1: {student1}")
print(f"student2: {student2}")

# 操作学生对象
student1.set_score("数学", 95)
student2.add_subject("化学")
student2.set_score("化学", 88)
print()

# 4. 默认参数和可变参数
print("=== 4. 默认参数和可变参数 ===")

class Product:
    """产品类 - 演示默认参数和可变参数"""
    
    def __init__(self, name, price, category="未分类", tags=None, **kwargs):
        """构造方法 - 默认参数和关键字参数"""
        # 必需参数
        self.name = name
        self.price = price
        
        # 默认参数
        self.category = category
        
        # 可变参数处理
        self.tags = tags if tags is not None else []
        
        # 额外属性（通过**kwargs）
        self.extra_info = kwargs
        
        # 计算属性
        self.product_id = f"P{hash(name) % 10000:04d}"
        
        print(f"产品 '{self.name}' 创建成功，ID: {self.product_id}")
    
    def add_tag(self, tag):
        """添加标签"""
        if tag not in self.tags:
            self.tags.append(tag)
    
    def get_info(self):
        """获取产品信息"""
        info = {
            'name': self.name,
            'price': self.price,
            'category': self.category,
            'tags': self.tags,
            'product_id': self.product_id
        }
        info.update(self.extra_info)
        return info
    
    def __str__(self):
        return f"Product('{self.name}', ¥{self.price}, {self.category})"

# 创建产品对象
print("创建Product对象:")
product1 = Product("笔记本电脑", 5999.99)
product2 = Product("智能手机", 2999.99, "电子产品", ["智能", "通讯"])
product3 = Product(
    "游戏鼠标", 299.99, "电脑配件", 
    ["游戏", "RGB"], 
    brand="罗技", 
    warranty="2年", 
    color="黑色"
)

print(f"product1: {product1}")
print(f"product2: {product2}")
print(f"product3: {product3}")

print("\nproduct3详细信息:")
for key, value in product3.get_info().items():
    print(f"  {key}: {value}")
print()

# 5. 构造方法中的验证和异常处理
print("=== 5. 构造方法中的验证和异常处理 ===")

class BankAccount:
    """银行账户类 - 带验证的构造方法"""
    
    def __init__(self, account_number, owner_name, initial_balance=0, account_type="储蓄"):
        """构造方法 - 包含参数验证"""
        # 验证账号
        if not isinstance(account_number, str) or len(account_number) < 10:
            raise ValueError("账号必须是至少10位的字符串")
        
        # 验证户主姓名
        if not isinstance(owner_name, str) or len(owner_name.strip()) == 0:
            raise ValueError("户主姓名不能为空")
        
        # 验证初始余额
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("初始余额必须是非负数")
        
        # 验证账户类型
        valid_types = ["储蓄", "支票", "定期"]
        if account_type not in valid_types:
            raise ValueError(f"账户类型必须是: {', '.join(valid_types)}")
        
        # 设置属性
        self.account_number = account_number
        self.owner_name = owner_name.strip()
        self.balance = initial_balance
        self.account_type = account_type
        self.is_active = True
        self.transaction_count = 0
        
        # 记录创建时间
        import datetime
        self.created_at = datetime.datetime.now()
        
        print(f"银行账户创建成功: {self.account_number} ({self.owner_name})")
    
    def get_account_info(self):
        """获取账户信息"""
        return {
            'account_number': self.account_number,
            'owner_name': self.owner_name,
            'balance': self.balance,
            'account_type': self.account_type,
            'is_active': self.is_active,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def __str__(self):
        return f"BankAccount({self.account_number}, {self.owner_name}, ¥{self.balance})"

# 创建银行账户（正确的参数）
print("创建有效的银行账户:")
try:
    account1 = BankAccount("6222001234567890", "张三", 1000, "储蓄")
    print(f"账户1: {account1}")
    
    account2 = BankAccount("6222009876543210", "李四")  # 使用默认值
    print(f"账户2: {account2}")
except ValueError as e:
    print(f"创建账户失败: {e}")

# 尝试创建无效的银行账户
print("\n尝试创建无效的银行账户:")
invalid_params = [
    ("123", "王五", 500, "储蓄"),  # 账号太短
    ("6222001111111111", "", 500, "储蓄"),  # 姓名为空
    ("6222002222222222", "赵六", -100, "储蓄"),  # 负余额
    ("6222003333333333", "孙七", 500, "投资"),  # 无效账户类型
]

for params in invalid_params:
    try:
        account = BankAccount(*params)
        print(f"意外成功: {account}")
    except ValueError as e:
        print(f"验证失败 {params[1]}: {e}")

print()

# 6. 调用父类构造方法
print("=== 6. 调用父类构造方法 ===")

class Animal:
    """动物基类"""
    
    def __init__(self, name, species, age):
        """动物构造方法"""
        self.name = name
        self.species = species
        self.age = age
        self.is_alive = True
        print(f"动物 {self.name} ({self.species}) 创建完成")
    
    def make_sound(self):
        """发出声音（基类方法）"""
        print(f"{self.name} 发出了声音")
    
    def __str__(self):
        return f"Animal(name='{self.name}', species='{self.species}', age={self.age})"

class Dog(Animal):
    """狗类 - 继承自Animal"""
    
    def __init__(self, name, age, breed, owner=None):
        """狗的构造方法 - 调用父类构造方法"""
        # 调用父类构造方法
        super().__init__(name, "犬科", age)
        
        # 设置子类特有属性
        self.breed = breed
        self.owner = owner
        self.is_trained = False
        
        print(f"狗狗 {self.name} ({self.breed}) 创建完成")
    
    def make_sound(self):
        """重写父类方法"""
        print(f"{self.name} 汪汪叫")
    
    def fetch(self):
        """狗特有的方法"""
        print(f"{self.name} 去捡球了")
    
    def __str__(self):
        return f"Dog(name='{self.name}', breed='{self.breed}', age={self.age})"

class Cat(Animal):
    """猫类 - 继承自Animal"""
    
    def __init__(self, name, age, color, is_indoor=True):
        """猫的构造方法"""
        # 调用父类构造方法
        super().__init__(name, "猫科", age)
        
        # 设置子类特有属性
        self.color = color
        self.is_indoor = is_indoor
        self.lives_remaining = 9  # 猫有九条命
        
        print(f"猫咪 {self.name} ({self.color}) 创建完成")
    
    def make_sound(self):
        """重写父类方法"""
        print(f"{self.name} 喵喵叫")
    
    def climb(self):
        """猫特有的方法"""
        print(f"{self.name} 爬到了高处")
    
    def __str__(self):
        return f"Cat(name='{self.name}', color='{self.color}', age={self.age})"

# 创建动物对象
print("创建动物对象:")
dog1 = Dog("旺财", 3, "金毛", "张三")
cat1 = Cat("咪咪", 2, "橘色")

print(f"\n狗: {dog1}")
print(f"猫: {cat1}")

print("\n动物们发出声音:")
dog1.make_sound()
cat1.make_sound()

print("\n特有行为:")
dog1.fetch()
cat1.climb()
print()

# 7. 构造方法的重载模拟
print("=== 7. 构造方法的重载模拟 ===")

class Rectangle:
    """矩形类 - 模拟构造方法重载"""
    
    def __init__(self, *args, **kwargs):
        """构造方法 - 支持多种初始化方式"""
        if len(args) == 1 and isinstance(args[0], (int, float)):
            # 正方形：Rectangle(5)
            self.width = self.height = args[0]
            print(f"创建正方形: {self.width}x{self.height}")
            
        elif len(args) == 2 and all(isinstance(x, (int, float)) for x in args):
            # 矩形：Rectangle(4, 6)
            self.width, self.height = args
            print(f"创建矩形: {self.width}x{self.height}")
            
        elif len(args) == 4 and all(isinstance(x, (int, float)) for x in args):
            # 通过坐标：Rectangle(0, 0, 4, 6)
            x1, y1, x2, y2 = args
            self.width = abs(x2 - x1)
            self.height = abs(y2 - y1)
            print(f"通过坐标创建矩形: {self.width}x{self.height}")
            
        elif 'width' in kwargs and 'height' in kwargs:
            # 关键字参数：Rectangle(width=4, height=6)
            self.width = kwargs['width']
            self.height = kwargs['height']
            print(f"通过关键字创建矩形: {self.width}x{self.height}")
            
        elif 'size' in kwargs:
            # 正方形关键字：Rectangle(size=5)
            self.width = self.height = kwargs['size']
            print(f"通过size创建正方形: {self.width}x{self.height}")
            
        else:
            # 默认值
            self.width = self.height = 1
            print("创建默认矩形: 1x1")
        
        # 计算面积和周长
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)
    
    @classmethod
    def from_area_ratio(cls, area, ratio):
        """类方法 - 通过面积和宽高比创建矩形"""
        import math
        width = math.sqrt(area * ratio)
        height = area / width
        return cls(width, height)
    
    @classmethod
    def square(cls, side):
        """类方法 - 创建正方形"""
        return cls(side)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height}, 面积={self.area}, 周长={self.perimeter})"

# 测试不同的创建方式
print("不同方式创建矩形:")
rect1 = Rectangle(5)  # 正方形
rect2 = Rectangle(4, 6)  # 矩形
rect3 = Rectangle(0, 0, 3, 4)  # 通过坐标
rect4 = Rectangle(width=2, height=8)  # 关键字参数
rect5 = Rectangle(size=7)  # 正方形关键字
rect6 = Rectangle()  # 默认值

print(f"rect1: {rect1}")
print(f"rect2: {rect2}")
print(f"rect3: {rect3}")
print(f"rect4: {rect4}")
print(f"rect5: {rect5}")
print(f"rect6: {rect6}")

# 使用类方法创建
print("\n使用类方法创建:")
rect7 = Rectangle.from_area_ratio(24, 1.5)  # 面积24，宽高比1.5
rect8 = Rectangle.square(9)  # 正方形

print(f"rect7: {rect7}")
print(f"rect8: {rect8}")
print()

# 8. 实际应用示例
print("=== 8. 实际应用示例 ===")

class DatabaseConnection:
    """数据库连接类 - 实际应用示例"""
    
    # 类属性 - 连接池
    _connection_pool = []
    _max_connections = 5
    
    def __init__(self, host, port, database, username, password, 
                 timeout=30, auto_commit=True, **options):
        """数据库连接构造方法"""
        # 检查连接池是否已满
        if len(DatabaseConnection._connection_pool) >= DatabaseConnection._max_connections:
            raise RuntimeError(f"连接池已满，最大连接数: {DatabaseConnection._max_connections}")
        
        # 验证必需参数
        required_params = {'host': host, 'database': database, 'username': username}
        for param_name, param_value in required_params.items():
            if not param_value or not isinstance(param_value, str):
                raise ValueError(f"{param_name} 不能为空")
        
        # 验证端口
        if not isinstance(port, int) or not (1 <= port <= 65535):
            raise ValueError("端口必须是1-65535之间的整数")
        
        # 设置连接参数
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self._password = password  # 私有属性
        self.timeout = timeout
        self.auto_commit = auto_commit
        self.options = options
        
        # 连接状态
        self.is_connected = False
        self.connection_id = f"conn_{len(DatabaseConnection._connection_pool) + 1}"
        self.created_at = None
        self.last_activity = None
        
        # 尝试建立连接
        self._connect()
        
        # 添加到连接池
        DatabaseConnection._connection_pool.append(self)
        
        print(f"数据库连接 {self.connection_id} 创建成功")
    
    def _connect(self):
        """建立数据库连接（模拟）"""
        import datetime
        import time
        
        print(f"正在连接到 {self.host}:{self.port}/{self.database}...")
        
        # 模拟连接过程
        time.sleep(0.1)  # 模拟网络延迟
        
        # 模拟连接成功
        self.is_connected = True
        self.created_at = datetime.datetime.now()
        self.last_activity = self.created_at
        
        print(f"连接成功！连接ID: {self.connection_id}")
    
    def execute_query(self, query):
        """执行查询（模拟）"""
        if not self.is_connected:
            raise RuntimeError("数据库未连接")
        
        import datetime
        self.last_activity = datetime.datetime.now()
        
        print(f"[{self.connection_id}] 执行查询: {query[:50]}...")
        return f"查询结果 (连接: {self.connection_id})"
    
    def close(self):
        """关闭连接"""
        if self.is_connected:
            self.is_connected = False
            if self in DatabaseConnection._connection_pool:
                DatabaseConnection._connection_pool.remove(self)
            print(f"连接 {self.connection_id} 已关闭")
    
    @classmethod
    def get_connection_count(cls):
        """获取当前连接数"""
        return len(cls._connection_pool)
    
    @classmethod
    def close_all_connections(cls):
        """关闭所有连接"""
        for conn in cls._connection_pool.copy():
            conn.close()
    
    def __str__(self):
        status = "已连接" if self.is_connected else "未连接"
        return f"DatabaseConnection({self.connection_id}, {self.host}:{self.port}, {status})"
    
    def __del__(self):
        """析构方法 - 对象被销毁时自动调用"""
        if hasattr(self, 'is_connected') and self.is_connected:
            self.close()

# 创建数据库连接
print("创建数据库连接:")
try:
    # 创建有效连接
    conn1 = DatabaseConnection(
        host="localhost",
        port=3306,
        database="test_db",
        username="admin",
        password="password123",
        charset="utf8mb4",
        pool_size=10
    )
    
    conn2 = DatabaseConnection(
        host="192.168.1.100",
        port=5432,
        database="production_db",
        username="user",
        password="secret",
        timeout=60,
        auto_commit=False
    )
    
    print(f"\n当前连接数: {DatabaseConnection.get_connection_count()}")
    print(f"conn1: {conn1}")
    print(f"conn2: {conn2}")
    
    # 执行查询
    result1 = conn1.execute_query("SELECT * FROM users WHERE active = 1")
    result2 = conn2.execute_query("SELECT COUNT(*) FROM orders")
    
    print(f"查询结果1: {result1}")
    print(f"查询结果2: {result2}")
    
except (ValueError, RuntimeError) as e:
    print(f"创建连接失败: {e}")

# 尝试创建无效连接
print("\n尝试创建无效连接:")
try:
    invalid_conn = DatabaseConnection("", 3306, "test", "user", "pass")
except ValueError as e:
    print(f"连接创建失败: {e}")

# 清理连接
print("\n清理连接:")
DatabaseConnection.close_all_connections()
print(f"剩余连接数: {DatabaseConnection.get_connection_count()}")

print()
print("=== 学习要点总结 ===")
print()
print("构造方法__init__的关键要点：")
print("1. __init__方法在对象创建时自动调用")
print("2. 第一个参数必须是self，代表对象实例")
print("3. 可以接收任意数量和类型的参数")
print("4. 支持默认参数、可变参数和关键字参数")
print("5. 应该包含参数验证和异常处理")
print("6. 子类可以通过super()调用父类构造方法")
print("7. 可以通过不同参数组合模拟方法重载")
print("8. 类方法可以提供额外的对象创建方式")
print()
print("=== 程序执行完成 ===")
print("恭喜！你已经学会了Python构造方法__init__的用法。")
print("下一步：学习私有属性和访问控制。")