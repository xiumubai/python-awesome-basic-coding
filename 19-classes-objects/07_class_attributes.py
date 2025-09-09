#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
类属性和类方法

本文件演示Python中类属性和类方法的详细用法：
1. 类属性的定义和使用
2. 类属性与实例属性的区别
3. 类方法(@classmethod)的定义和使用
4. 静态方法(@staticmethod)的定义和使用
5. 类方法、静态方法和实例方法的比较
6. 类属性的继承和重写
7. 类方法的实际应用场景
8. 综合应用示例

作者: Python学习助手
日期: 2024
"""

print("=== Python类属性和类方法学习 ===")
print()

# 1. 类属性的定义和使用
print("=== 1. 类属性的定义和使用 ===")

class Student:
    """学生类 - 演示类属性的基本用法"""
    
    # 类属性 - 属于类本身，所有实例共享
    school_name = "Python编程学院"
    total_students = 0
    grade_levels = ["一年级", "二年级", "三年级", "四年级"]
    
    def __init__(self, name, age, grade):
        """初始化学生实例"""
        # 实例属性 - 属于具体实例
        self.name = name
        self.age = age
        self.grade = grade
        
        # 修改类属性
        Student.total_students += 1
        
        print(f"学生 {self.name} 创建成功，当前总学生数: {Student.total_students}")
    
    def introduce(self):
        """学生自我介绍"""
        return f"我是{self.name}，{self.age}岁，{self.grade}，来自{Student.school_name}"
    
    def __str__(self):
        return f"Student({self.name}, {self.age}, {self.grade})"

# 测试类属性
print("访问类属性（通过类名）:")
print(f"学校名称: {Student.school_name}")
print(f"总学生数: {Student.total_students}")
print(f"年级列表: {Student.grade_levels}")

print("\n创建学生实例:")
student1 = Student("张三", 18, "二年级")
student2 = Student("李四", 19, "三年级")
student3 = Student("王五", 17, "一年级")

print(f"\n创建实例后的总学生数: {Student.total_students}")

print("\n通过实例访问类属性:")
print(f"student1访问学校名称: {student1.school_name}")
print(f"student2访问总学生数: {student2.total_students}")

print("\n学生自我介绍:")
for i, student in enumerate([student1, student2, student3], 1):
    print(f"{i}. {student.introduce()}")
print()

# 2. 类属性与实例属性的区别
print("=== 2. 类属性与实例属性的区别 ===")

class AttributeDemo:
    """属性演示类"""
    
    # 类属性
    class_attr = "这是类属性"
    shared_list = []  # 注意：可变类属性的陷阱
    
    def __init__(self, name):
        # 实例属性
        self.name = name
        self.instance_attr = f"{name}的实例属性"
    
    def add_to_shared_list(self, item):
        """向共享列表添加项目"""
        self.shared_list.append(item)
        print(f"{self.name} 添加了 '{item}' 到共享列表")
    
    def show_attributes(self):
        """显示所有属性"""
        print(f"实例 {self.name}:")
        print(f"  实例属性: {self.instance_attr}")
        print(f"  类属性: {self.class_attr}")
        print(f"  共享列表: {self.shared_list}")

# 创建多个实例测试属性共享
print("创建AttributeDemo实例:")
obj1 = AttributeDemo("对象1")
obj2 = AttributeDemo("对象2")

print("\n初始状态:")
obj1.show_attributes()
obj2.show_attributes()

print("\n修改类属性（通过类名）:")
AttributeDemo.class_attr = "修改后的类属性"
print("修改后的状态:")
obj1.show_attributes()
obj2.show_attributes()

print("\n修改实例的类属性（创建实例属性）:")
obj1.class_attr = "obj1的专属属性"
print("修改后的状态:")
obj1.show_attributes()
obj2.show_attributes()
print(f"通过类名访问: {AttributeDemo.class_attr}")

print("\n测试可变类属性的共享:")
obj1.add_to_shared_list("项目1")
obj2.add_to_shared_list("项目2")
print("添加后的状态:")
obj1.show_attributes()
obj2.show_attributes()
print()

# 3. 类方法(@classmethod)的定义和使用
print("=== 3. 类方法(@classmethod)的定义和使用 ===")

class Person:
    """人员类 - 演示类方法的使用"""
    
    # 类属性
    population = 0
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """初始化人员实例"""
        self.name = name
        self.age = age
        Person.population += 1
        print(f"人员 {self.name} 创建成功")
    
    @classmethod
    def get_population(cls):
        """获取人口总数（类方法）"""
        return cls.population
    
    @classmethod
    def get_species(cls):
        """获取物种信息（类方法）"""
        return cls.species
    
    @classmethod
    def create_baby(cls, name):
        """创建婴儿（类方法作为替代构造器）"""
        return cls(name, 0)
    
    @classmethod
    def create_adult(cls, name):
        """创建成年人（类方法作为替代构造器）"""
        return cls(name, 18)
    
    @classmethod
    def from_string(cls, person_str):
        """从字符串创建人员对象（类方法解析器）"""
        try:
            name, age_str = person_str.split('-')
            age = int(age_str)
            return cls(name.strip(), age)
        except ValueError:
            raise ValueError(f"无效的人员字符串格式: {person_str}")
    
    @classmethod
    def reset_population(cls):
        """重置人口计数（类方法）"""
        old_population = cls.population
        cls.population = 0
        print(f"人口计数已重置，从 {old_population} 重置为 {cls.population}")
    
    def celebrate_birthday(self):
        """庆祝生日（实例方法）"""
        self.age += 1
        print(f"{self.name} 庆祝生日，现在 {self.age} 岁了！")
    
    def __str__(self):
        return f"Person({self.name}, {self.age})"

# 测试类方法
print("使用类方法获取类信息:")
print(f"初始人口: {Person.get_population()}")
print(f"物种: {Person.get_species()}")

print("\n使用普通构造器创建对象:")
person1 = Person("张三", 25)
person2 = Person("李四", 30)

print(f"\n当前人口: {Person.get_population()}")

print("\n使用类方法作为替代构造器:")
baby = Person.create_baby("小明")
adult = Person.create_adult("王五")

print(f"创建后人口: {Person.get_population()}")

print("\n使用类方法解析字符串:")
try:
    person3 = Person.from_string("赵六 - 28")
    person4 = Person.from_string("孙七-35")
    print(f"解析成功: {person3}, {person4}")
except ValueError as e:
    print(f"解析失败: {e}")

print(f"\n最终人口: {Person.get_population()}")

print("\n重置人口计数:")
Person.reset_population()
print()

# 4. 静态方法(@staticmethod)的定义和使用
print("=== 4. 静态方法(@staticmethod)的定义和使用 ===")

class MathUtils:
    """数学工具类 - 演示静态方法的使用"""
    
    # 类属性
    PI = 3.14159265359
    E = 2.71828182846
    
    @staticmethod
    def add(a, b):
        """加法运算（静态方法）"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """乘法运算（静态方法）"""
        return a * b
    
    @staticmethod
    def is_even(number):
        """判断是否为偶数（静态方法）"""
        return number % 2 == 0
    
    @staticmethod
    def is_prime(number):
        """判断是否为质数（静态方法）"""
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n):
        """计算阶乘（静态方法）"""
        if n < 0:
            raise ValueError("阶乘不能计算负数")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def circle_area(radius):
        """计算圆形面积（静态方法）"""
        return MathUtils.PI * radius ** 2
    
    @staticmethod
    def validate_positive(value, name="值"):
        """验证正数（静态方法）"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name}必须是数字")
        if value <= 0:
            raise ValueError(f"{name}必须是正数")
        return True
    
    @classmethod
    def get_constants(cls):
        """获取数学常数（类方法）"""
        return {
            'PI': cls.PI,
            'E': cls.E
        }

# 测试静态方法
print("使用静态方法进行数学运算:")
print(f"5 + 3 = {MathUtils.add(5, 3)}")
print(f"4 * 7 = {MathUtils.multiply(4, 7)}")

print("\n使用静态方法进行数字判断:")
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for num in numbers:
    even_status = "偶数" if MathUtils.is_even(num) else "奇数"
    prime_status = "质数" if MathUtils.is_prime(num) else "合数"
    print(f"{num}: {even_status}, {prime_status}")

print("\n使用静态方法计算阶乘:")
for i in range(6):
    print(f"{i}! = {MathUtils.factorial(i)}")

print("\n使用静态方法计算圆形面积:")
radii = [1, 2, 3, 5]
for r in radii:
    area = MathUtils.circle_area(r)
    print(f"半径 {r} 的圆形面积: {area:.2f}")

print("\n获取数学常数:")
constants = MathUtils.get_constants()
for name, value in constants.items():
    print(f"{name}: {value}")

# 静态方法可以通过类名或实例调用
print("\n静态方法的不同调用方式:")
math_obj = MathUtils()
print(f"通过类名调用: {MathUtils.add(10, 20)}")
print(f"通过实例调用: {math_obj.add(10, 20)}")
print()

# 5. 类方法、静态方法和实例方法的比较
print("=== 5. 类方法、静态方法和实例方法的比较 ===")

class MethodComparison:
    """方法比较演示类"""
    
    class_variable = "类变量"
    
    def __init__(self, name):
        self.name = name
        self.instance_variable = f"{name}的实例变量"
    
    def instance_method(self):
        """实例方法 - 可以访问实例和类属性"""
        return {
            'method_type': '实例方法',
            'can_access_instance': True,
            'can_access_class': True,
            'instance_variable': self.instance_variable,
            'class_variable': self.class_variable,
            'self': str(self)
        }
    
    @classmethod
    def class_method(cls):
        """类方法 - 只能访问类属性，不能访问实例属性"""
        return {
            'method_type': '类方法',
            'can_access_instance': False,
            'can_access_class': True,
            'class_variable': cls.class_variable,
            'cls': str(cls)
        }
    
    @staticmethod
    def static_method():
        """静态方法 - 不能访问实例或类属性"""
        return {
            'method_type': '静态方法',
            'can_access_instance': False,
            'can_access_class': False,
            'note': '静态方法是独立的函数，与类的状态无关'
        }
    
    def __str__(self):
        return f"MethodComparison({self.name})"

# 创建实例并测试不同类型的方法
print("创建MethodComparison实例:")
obj = MethodComparison("测试对象")

print("\n调用实例方法:")
instance_result = obj.instance_method()
for key, value in instance_result.items():
    print(f"  {key}: {value}")

print("\n调用类方法（通过实例）:")
class_result = obj.class_method()
for key, value in class_result.items():
    print(f"  {key}: {value}")

print("\n调用类方法（通过类名）:")
class_result2 = MethodComparison.class_method()
for key, value in class_result2.items():
    print(f"  {key}: {value}")

print("\n调用静态方法（通过实例）:")
static_result = obj.static_method()
for key, value in static_result.items():
    print(f"  {key}: {value}")

print("\n调用静态方法（通过类名）:")
static_result2 = MethodComparison.static_method()
for key, value in static_result2.items():
    print(f"  {key}: {value}")

print("\n方法调用总结:")
print("1. 实例方法：需要实例，可以访问实例和类属性")
print("2. 类方法：不需要实例，只能访问类属性，接收cls参数")
print("3. 静态方法：不需要实例，不能访问任何属性，独立函数")
print()

# 6. 类属性的继承和重写
print("=== 6. 类属性的继承和重写 ===")

class Animal:
    """动物基类"""
    
    # 类属性
    kingdom = "动物界"
    total_animals = 0
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.total_animals += 1
        print(f"动物 {self.name}({self.species}) 创建成功")
    
    @classmethod
    def get_total_animals(cls):
        """获取动物总数"""
        return cls.total_animals
    
    @classmethod
    def get_kingdom(cls):
        """获取界别"""
        return cls.kingdom
    
    def make_sound(self):
        """发出声音（基类方法）"""
        return f"{self.name} 发出了声音"
    
    def __str__(self):
        return f"Animal({self.name}, {self.species})"

class Dog(Animal):
    """狗类 - 继承Animal"""
    
    # 重写类属性
    species_name = "犬科"
    total_dogs = 0
    
    def __init__(self, name, breed):
        super().__init__(name, "狗")
        self.breed = breed
        Dog.total_dogs += 1
    
    @classmethod
    def get_total_dogs(cls):
        """获取狗的总数"""
        return cls.total_dogs
    
    @classmethod
    def get_species_name(cls):
        """获取物种名称"""
        return cls.species_name
    
    def make_sound(self):
        """重写发声方法"""
        return f"{self.name} 汪汪叫"
    
    def __str__(self):
        return f"Dog({self.name}, {self.breed})"

class Cat(Animal):
    """猫类 - 继承Animal"""
    
    # 重写类属性
    species_name = "猫科"
    total_cats = 0
    
    def __init__(self, name, color):
        super().__init__(name, "猫")
        self.color = color
        Cat.total_cats += 1
    
    @classmethod
    def get_total_cats(cls):
        """获取猫的总数"""
        return cls.total_cats
    
    @classmethod
    def get_species_name(cls):
        """获取物种名称"""
        return cls.species_name
    
    def make_sound(self):
        """重写发声方法"""
        return f"{self.name} 喵喵叫"
    
    def __str__(self):
        return f"Cat({self.name}, {self.color})"

# 测试继承和重写
print("创建动物实例:")
dog1 = Dog("旺财", "金毛")
dog2 = Dog("小黑", "拉布拉多")
cat1 = Cat("咪咪", "白色")
cat2 = Cat("花花", "花色")

print("\n测试类属性继承:")
print(f"Animal总数: {Animal.get_total_animals()}")
print(f"Dog总数: {Dog.get_total_dogs()}")
print(f"Cat总数: {Cat.get_total_cats()}")

print("\n测试类方法继承:")
print(f"Animal界别: {Animal.get_kingdom()}")
print(f"Dog界别: {Dog.get_kingdom()}")
print(f"Cat界别: {Cat.get_kingdom()}")

print("\n测试重写的类属性:")
print(f"Dog物种: {Dog.get_species_name()}")
print(f"Cat物种: {Cat.get_species_name()}")

print("\n测试方法重写:")
animals = [dog1, dog2, cat1, cat2]
for animal in animals:
    print(f"{animal}: {animal.make_sound()}")
print()

# 7. 类方法的实际应用场景
print("=== 7. 类方法的实际应用场景 ===")

class DatabaseConnection:
    """数据库连接类 - 演示类方法的实际应用"""
    
    # 类属性
    _instance = None
    _connection_count = 0
    default_config = {
        'host': 'localhost',
        'port': 3306,
        'database': 'test',
        'charset': 'utf8'
    }
    
    def __init__(self, host, port, database, username, password):
        """初始化数据库连接"""
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.is_connected = False
        
        DatabaseConnection._connection_count += 1
        print(f"数据库连接创建: {self.username}@{self.host}:{self.port}/{self.database}")
    
    @classmethod
    def from_url(cls, url):
        """从URL创建连接（类方法作为替代构造器）"""
        # 简化的URL解析
        # 格式: mysql://username:password@host:port/database
        try:
            if not url.startswith('mysql://'):
                raise ValueError("URL必须以mysql://开头")
            
            url = url[8:]  # 移除mysql://
            auth_part, host_part = url.split('@')
            username, password = auth_part.split(':')
            host_db_part = host_part.split('/')
            host_port = host_db_part[0]
            database = host_db_part[1] if len(host_db_part) > 1 else 'test'
            
            if ':' in host_port:
                host, port = host_port.split(':')
                port = int(port)
            else:
                host = host_port
                port = 3306
            
            return cls(host, port, database, username, password)
        except Exception as e:
            raise ValueError(f"无效的数据库URL: {e}")
    
    @classmethod
    def from_config(cls, config):
        """从配置字典创建连接（类方法）"""
        required_keys = ['host', 'port', 'database', 'username', 'password']
        for key in required_keys:
            if key not in config:
                raise ValueError(f"配置中缺少必需的键: {key}")
        
        return cls(
            config['host'],
            config['port'],
            config['database'],
            config['username'],
            config['password']
        )
    
    @classmethod
    def create_default(cls, username, password):
        """创建默认配置的连接（类方法）"""
        return cls(
            cls.default_config['host'],
            cls.default_config['port'],
            cls.default_config['database'],
            username,
            password
        )
    
    @classmethod
    def get_connection_count(cls):
        """获取连接总数（类方法）"""
        return cls._connection_count
    
    @classmethod
    def get_default_config(cls):
        """获取默认配置（类方法）"""
        return cls.default_config.copy()
    
    def connect(self):
        """连接数据库"""
        if not self.is_connected:
            print(f"正在连接到 {self.host}:{self.port}/{self.database}...")
            # 模拟连接过程
            self.is_connected = True
            print("连接成功！")
        else:
            print("已经连接")
    
    def disconnect(self):
        """断开连接"""
        if self.is_connected:
            print(f"断开与 {self.host}:{self.port}/{self.database} 的连接")
            self.is_connected = False
        else:
            print("未连接")
    
    def execute_query(self, query):
        """执行查询"""
        if not self.is_connected:
            raise RuntimeError("未连接到数据库")
        
        print(f"执行查询: {query}")
        return f"查询结果: {query} (模拟结果)"
    
    def __str__(self):
        status = "已连接" if self.is_connected else "未连接"
        return f"DatabaseConnection({self.username}@{self.host}:{self.port}/{self.database}, {status})"

# 测试类方法的实际应用
print("使用不同的类方法创建数据库连接:")

print("\n1. 使用普通构造器:")
db1 = DatabaseConnection('localhost', 3306, 'myapp', 'user1', 'pass1')

print("\n2. 使用from_url类方法:")
try:
    db2 = DatabaseConnection.from_url('mysql://user2:pass2@192.168.1.100:3306/webapp')
except ValueError as e:
    print(f"URL解析失败: {e}")

print("\n3. 使用from_config类方法:")
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'testdb',
    'username': 'user3',
    'password': 'pass3'
}
db3 = DatabaseConnection.from_config(config)

print("\n4. 使用create_default类方法:")
db4 = DatabaseConnection.create_default('user4', 'pass4')

print(f"\n当前连接总数: {DatabaseConnection.get_connection_count()}")

print("\n默认配置:")
default_config = DatabaseConnection.get_default_config()
for key, value in default_config.items():
    print(f"  {key}: {value}")

print("\n测试数据库操作:")
db1.connect()
result = db1.execute_query("SELECT * FROM users")
print(result)
db1.disconnect()
print()

# 8. 综合应用示例
print("=== 8. 综合应用示例 ===")

class Product:
    """产品类 - 综合应用示例"""
    
    # 类属性
    total_products = 0
    categories = ['电子产品', '服装', '食品', '图书', '家居']
    tax_rate = 0.1  # 10%税率
    
    def __init__(self, name, price, category, stock=0):
        """初始化产品"""
        self.validate_category(category)
        self.validate_price(price)
        
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        
        Product.total_products += 1
        self.product_id = Product.total_products
        
        print(f"产品 '{self.name}' 创建成功，ID: {self.product_id}")
    
    @classmethod
    def from_string(cls, product_str):
        """从字符串创建产品（类方法）"""
        # 格式: "产品名-价格-类别-库存"
        try:
            parts = product_str.split('-')
            if len(parts) != 4:
                raise ValueError("格式应为: 产品名-价格-类别-库存")
            
            name = parts[0].strip()
            price = float(parts[1].strip())
            category = parts[2].strip()
            stock = int(parts[3].strip())
            
            return cls(name, price, category, stock)
        except (ValueError, IndexError) as e:
            raise ValueError(f"无效的产品字符串: {e}")
    
    @classmethod
    def create_electronic(cls, name, price, stock=0):
        """创建电子产品（类方法）"""
        return cls(name, price, '电子产品', stock)
    
    @classmethod
    def create_book(cls, name, price, stock=0):
        """创建图书产品（类方法）"""
        return cls(name, price, '图书', stock)
    
    @classmethod
    def get_total_products(cls):
        """获取产品总数（类方法）"""
        return cls.total_products
    
    @classmethod
    def get_categories(cls):
        """获取所有类别（类方法）"""
        return cls.categories.copy()
    
    @classmethod
    def set_tax_rate(cls, rate):
        """设置税率（类方法）"""
        if not 0 <= rate <= 1:
            raise ValueError("税率必须在0-1之间")
        cls.tax_rate = rate
        print(f"税率已设置为: {rate*100}%")
    
    @staticmethod
    def validate_price(price):
        """验证价格（静态方法）"""
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("价格必须是非负数")
        return True
    
    @staticmethod
    def validate_category(category):
        """验证类别（静态方法）"""
        if category not in Product.categories:
            raise ValueError(f"无效的类别，可选类别: {Product.categories}")
        return True
    
    @staticmethod
    def calculate_discount(price, discount_rate):
        """计算折扣价格（静态方法）"""
        if not 0 <= discount_rate <= 1:
            raise ValueError("折扣率必须在0-1之间")
        return price * (1 - discount_rate)
    
    def get_price_with_tax(self):
        """获取含税价格"""
        return self.price * (1 + Product.tax_rate)
    
    def add_stock(self, quantity):
        """增加库存"""
        if quantity < 0:
            raise ValueError("数量不能为负数")
        self.stock += quantity
        print(f"{self.name} 库存增加 {quantity}，当前库存: {self.stock}")
    
    def sell(self, quantity):
        """销售产品"""
        if quantity < 0:
            raise ValueError("销售数量不能为负数")
        if quantity > self.stock:
            raise ValueError(f"库存不足，当前库存: {self.stock}")
        
        self.stock -= quantity
        total_price = self.price * quantity
        total_with_tax = self.get_price_with_tax() * quantity
        
        print(f"销售 {self.name} x{quantity}")
        print(f"  单价: ¥{self.price:.2f}")
        print(f"  小计: ¥{total_price:.2f}")
        print(f"  含税总计: ¥{total_with_tax:.2f}")
        print(f"  剩余库存: {self.stock}")
        
        return total_with_tax
    
    def __str__(self):
        return f"Product({self.product_id}: {self.name}, ¥{self.price}, {self.category}, 库存:{self.stock})"

# 测试综合应用
print("创建产品:")

print("\n1. 使用普通构造器:")
product1 = Product("iPhone 15", 6999, "电子产品", 50)
product2 = Product("Python编程书", 89, "图书", 100)

print("\n2. 使用类方法创建:")
product3 = Product.create_electronic("MacBook Pro", 12999, 20)
product4 = Product.create_book("算法导论", 128, 30)

print("\n3. 从字符串创建:")
try:
    product5 = Product.from_string("Nike运动鞋-599-服装-80")
except ValueError as e:
    print(f"创建失败: {e}")

print(f"\n当前产品总数: {Product.get_total_products()}")

print("\n所有产品:")
products = [product1, product2, product3, product4]
for product in products:
    print(f"  {product}")

print("\n设置税率和进行销售:")
Product.set_tax_rate(0.13)  # 设置13%税率

print("\n销售测试:")
product1.sell(2)  # 销售2台iPhone
product2.sell(5)  # 销售5本书

print("\n补充库存:")
product1.add_stock(10)

print("\n使用静态方法计算折扣:")
original_price = 1000
discount_rate = 0.2  # 20%折扣
discounted_price = Product.calculate_discount(original_price, discount_rate)
print(f"原价: ¥{original_price}, 折扣率: {discount_rate*100}%, 折后价: ¥{discounted_price}")

print("\n获取产品类别:")
categories = Product.get_categories()
print(f"可用类别: {categories}")

print()
print("=== 学习要点总结 ===")
print()
print("类属性和类方法的关键要点：")
print("1. 类属性属于类本身，所有实例共享")
print("2. 类方法使用@classmethod装饰器，接收cls参数")
print("3. 静态方法使用@staticmethod装饰器，不接收特殊参数")
print("4. 类方法常用作替代构造器和工厂方法")
print("5. 静态方法用于与类相关但不需要访问类状态的功能")
print("6. 类属性在继承中可以被重写")
print("7. 合理使用类方法和静态方法可以提高代码的组织性")
print("8. 类方法和静态方法都可以通过类名或实例调用")
print()
print("=== 程序执行完成 ===")
print("恭喜！你已经学会了Python类属性和类方法。")
print("下一步：学习综合练习。")