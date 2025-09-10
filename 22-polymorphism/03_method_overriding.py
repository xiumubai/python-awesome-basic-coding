#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
方法重写实现多态

方法重写（Method Overriding）是面向对象编程中实现多态的重要机制。
子类可以重写父类的方法，提供不同的实现，从而实现多态行为。

核心概念：
1. 子类重写父类方法
2. 运行时动态绑定
3. 相同接口，不同实现
4. 支持扩展和定制
"""

# 1. 基本方法重写示例
class Animal:
    """动物基类"""
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        """发出声音 - 基类方法"""
        return f"{self.name} 发出声音"
    
    def move(self):
        """移动 - 基类方法"""
        return f"{self.name} 在移动"
    
    def eat(self):
        """吃东西 - 基类方法"""
        return f"{self.name} 在吃东西"
    
    def sleep(self):
        """睡觉 - 基类方法"""
        return f"{self.name} 在睡觉"

class Dog(Animal):
    """狗类 - 重写部分方法"""
    def make_sound(self):
        """重写发声方法"""
        return f"{self.name} 汪汪叫"
    
    def move(self):
        """重写移动方法"""
        return f"{self.name} 跑来跑去"
    
    def fetch(self):
        """狗特有的方法"""
        return f"{self.name} 去捡球"

class Cat(Animal):
    """猫类 - 重写部分方法"""
    def make_sound(self):
        """重写发声方法"""
        return f"{self.name} 喵喵叫"
    
    def move(self):
        """重写移动方法"""
        return f"{self.name} 优雅地走动"
    
    def climb(self):
        """猫特有的方法"""
        return f"{self.name} 爬树"

class Bird(Animal):
    """鸟类 - 重写部分方法"""
    def make_sound(self):
        """重写发声方法"""
        return f"{self.name} 啾啾叫"
    
    def move(self):
        """重写移动方法"""
        return f"{self.name} 在天空中飞翔"
    
    def fly(self):
        """鸟特有的方法"""
        return f"{self.name} 展翅高飞"

# 2. 使用super()调用父类方法
class Fish(Animal):
    """鱼类 - 使用super()扩展父类方法"""
    def __init__(self, name, water_type="淡水"):
        super().__init__(name)  # 调用父类构造方法
        self.water_type = water_type
    
    def make_sound(self):
        """鱼通常不发声，但可以有水泡声"""
        base_sound = super().make_sound()  # 调用父类方法
        return f"{base_sound}（水泡声）"
    
    def move(self):
        """重写移动方法，但保留父类信息"""
        base_move = super().move()
        return f"{base_move}，在{self.water_type}中游泳"
    
    def swim(self):
        """鱼特有的方法"""
        return f"{self.name} 在{self.water_type}中自由游泳"

# 3. 多态的实际应用
def animal_behavior(animal):
    """展示动物行为 - 多态应用"""
    print(f"=== {animal.name} 的行为 ===")
    print(f"声音: {animal.make_sound()}")
    print(f"移动: {animal.move()}")
    print(f"吃饭: {animal.eat()}")
    print(f"睡觉: {animal.sleep()}")
    
    # 调用特有方法（如果存在）
    if hasattr(animal, 'fetch'):
        print(f"特技: {animal.fetch()}")
    elif hasattr(animal, 'climb'):
        print(f"特技: {animal.climb()}")
    elif hasattr(animal, 'fly'):
        print(f"特技: {animal.fly()}")
    elif hasattr(animal, 'swim'):
        print(f"特技: {animal.swim()}")
    print()

# 4. 形状类的方法重写示例
class Shape:
    """形状基类"""
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """计算面积 - 基类方法"""
        raise NotImplementedError("子类必须实现area方法")
    
    def perimeter(self):
        """计算周长 - 基类方法"""
        raise NotImplementedError("子类必须实现perimeter方法")
    
    def describe(self):
        """描述形状 - 基类方法"""
        return f"这是一个{self.name}"

class Rectangle(Shape):
    """矩形类"""
    def __init__(self, width, height):
        super().__init__("矩形")
        self.width = width
        self.height = height
    
    def area(self):
        """重写面积计算"""
        return self.width * self.height
    
    def perimeter(self):
        """重写周长计算"""
        return 2 * (self.width + self.height)
    
    def describe(self):
        """重写描述方法"""
        base_desc = super().describe()
        return f"{base_desc}，宽度: {self.width}, 高度: {self.height}"

class Circle(Shape):
    """圆形类"""
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius = radius
    
    def area(self):
        """重写面积计算"""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """重写周长计算"""
        import math
        return 2 * math.pi * self.radius
    
    def describe(self):
        """重写描述方法"""
        base_desc = super().describe()
        return f"{base_desc}，半径: {self.radius}"

class Triangle(Shape):
    """三角形类"""
    def __init__(self, a, b, c):
        super().__init__("三角形")
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        """重写面积计算（海伦公式）"""
        import math
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        """重写周长计算"""
        return self.a + self.b + self.c
    
    def describe(self):
        """重写描述方法"""
        base_desc = super().describe()
        return f"{base_desc}，边长: {self.a}, {self.b}, {self.c}"

# 5. 计算形状属性的多态函数
def calculate_shape_properties(shapes):
    """计算形状属性 - 多态应用"""
    print("=== 形状属性计算 ===")
    total_area = 0
    total_perimeter = 0
    
    for shape in shapes:
        area = shape.area()
        perimeter = shape.perimeter()
        total_area += area
        total_perimeter += perimeter
        
        print(f"{shape.describe()}")
        print(f"  面积: {area:.2f}")
        print(f"  周长: {perimeter:.2f}")
        print()
    
    print(f"总面积: {total_area:.2f}")
    print(f"总周长: {total_perimeter:.2f}")
    print()

# 6. 车辆类的方法重写示例
class Vehicle:
    """车辆基类"""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    def start_engine(self):
        """启动引擎"""
        return f"{self.brand} {self.model} 引擎启动"
    
    def stop_engine(self):
        """停止引擎"""
        self.speed = 0
        return f"{self.brand} {self.model} 引擎停止"
    
    def accelerate(self, speed_increase):
        """加速"""
        self.speed += speed_increase
        return f"{self.brand} {self.model} 加速到 {self.speed} km/h"
    
    def brake(self, speed_decrease):
        """刹车"""
        self.speed = max(0, self.speed - speed_decrease)
        return f"{self.brand} {self.model} 减速到 {self.speed} km/h"
    
    def get_info(self):
        """获取车辆信息"""
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    """汽车类"""
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
    
    def start_engine(self):
        """重写启动方法"""
        base_start = super().start_engine()
        return f"{base_start}，汽车准备就绪"
    
    def honk(self):
        """汽车特有方法"""
        return f"{self.brand} {self.model} 鸣笛：嘀嘀！"
    
    def get_info(self):
        """重写信息获取"""
        base_info = super().get_info()
        return f"{base_info}，{self.doors}门汽车"

class Motorcycle(Vehicle):
    """摩托车类"""
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size
    
    def start_engine(self):
        """重写启动方法"""
        base_start = super().start_engine()
        return f"{base_start}，摩托车轰鸣声响起"
    
    def wheelie(self):
        """摩托车特有方法"""
        return f"{self.brand} {self.model} 做后轮着地特技"
    
    def get_info(self):
        """重写信息获取"""
        base_info = super().get_info()
        return f"{base_info}，{self.engine_size}cc摩托车"

class Truck(Vehicle):
    """卡车类"""
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity
        self.current_load = 0
    
    def start_engine(self):
        """重写启动方法"""
        base_start = super().start_engine()
        return f"{base_start}，卡车柴油引擎启动"
    
    def load_cargo(self, weight):
        """装载货物"""
        if self.current_load + weight <= self.load_capacity:
            self.current_load += weight
            return f"装载 {weight}kg 货物，当前载重: {self.current_load}kg"
        else:
            return f"超载！无法装载 {weight}kg 货物"
    
    def unload_cargo(self, weight):
        """卸载货物"""
        if weight <= self.current_load:
            self.current_load -= weight
            return f"卸载 {weight}kg 货物，当前载重: {self.current_load}kg"
        else:
            return f"卸载重量超过当前载重"
    
    def get_info(self):
        """重写信息获取"""
        base_info = super().get_info()
        return f"{base_info}，载重: {self.load_capacity}kg 卡车"

# 7. 车辆操作的多态函数
def operate_vehicle(vehicle):
    """操作车辆 - 多态应用"""
    print(f"=== 操作 {vehicle.get_info()} ===")
    print(vehicle.start_engine())
    print(vehicle.accelerate(50))
    print(vehicle.brake(20))
    
    # 调用特有方法
    if hasattr(vehicle, 'honk'):
        print(vehicle.honk())
    elif hasattr(vehicle, 'wheelie'):
        print(vehicle.wheelie())
    elif hasattr(vehicle, 'load_cargo'):
        print(vehicle.load_cargo(1000))
    
    print(vehicle.stop_engine())
    print()

# 8. 方法重写的高级示例
class Employee:
    """员工基类"""
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
    
    def calculate_salary(self):
        """计算薪资 - 基类方法"""
        return self.base_salary
    
    def get_work_description(self):
        """获取工作描述"""
        return f"{self.name} 是一名员工"
    
    def get_benefits(self):
        """获取福利"""
        return ["基本医疗保险", "年假"]

class Manager(Employee):
    """经理类"""
    def __init__(self, name, employee_id, base_salary, team_size):
        super().__init__(name, employee_id, base_salary)
        self.team_size = team_size
    
    def calculate_salary(self):
        """重写薪资计算 - 包含管理津贴"""
        base_salary = super().calculate_salary()
        management_bonus = self.team_size * 1000
        return base_salary + management_bonus
    
    def get_work_description(self):
        """重写工作描述"""
        return f"{self.name} 是一名经理，管理 {self.team_size} 人的团队"
    
    def get_benefits(self):
        """重写福利获取"""
        base_benefits = super().get_benefits()
        manager_benefits = ["管理培训", "额外年假", "公司车辆"]
        return base_benefits + manager_benefits

class Developer(Employee):
    """开发者类"""
    def __init__(self, name, employee_id, base_salary, programming_languages):
        super().__init__(name, employee_id, base_salary)
        self.programming_languages = programming_languages
    
    def calculate_salary(self):
        """重写薪资计算 - 包含技能津贴"""
        base_salary = super().calculate_salary()
        skill_bonus = len(self.programming_languages) * 500
        return base_salary + skill_bonus
    
    def get_work_description(self):
        """重写工作描述"""
        languages = ", ".join(self.programming_languages)
        return f"{self.name} 是一名开发者，掌握: {languages}"
    
    def get_benefits(self):
        """重写福利获取"""
        base_benefits = super().get_benefits()
        dev_benefits = ["技术培训", "会议参与", "设备津贴"]
        return base_benefits + dev_benefits

class Salesperson(Employee):
    """销售员类"""
    def __init__(self, name, employee_id, base_salary, sales_target):
        super().__init__(name, employee_id, base_salary)
        self.sales_target = sales_target
        self.sales_achieved = 0
    
    def calculate_salary(self):
        """重写薪资计算 - 包含销售提成"""
        base_salary = super().calculate_salary()
        commission_rate = 0.05  # 5%提成
        commission = self.sales_achieved * commission_rate
        return base_salary + commission
    
    def record_sale(self, amount):
        """记录销售"""
        self.sales_achieved += amount
        return f"{self.name} 完成 {amount} 元销售，总销售额: {self.sales_achieved} 元"
    
    def get_work_description(self):
        """重写工作描述"""
        progress = (self.sales_achieved / self.sales_target) * 100
        return f"{self.name} 是一名销售员，目标完成度: {progress:.1f}%"
    
    def get_benefits(self):
        """重写福利获取"""
        base_benefits = super().get_benefits()
        sales_benefits = ["销售培训", "客户招待费", "业绩奖金"]
        return base_benefits + sales_benefits

# 9. 员工管理的多态函数
def process_employee(employee):
    """处理员工信息 - 多态应用"""
    print(f"=== {employee.name} 的信息 ===")
    print(f"描述: {employee.get_work_description()}")
    print(f"薪资: {employee.calculate_salary()} 元")
    print(f"福利: {', '.join(employee.get_benefits())}")
    
    # 特有方法
    if hasattr(employee, 'record_sale'):
        print(employee.record_sale(5000))
    
    print()

def demonstrate_basic_overriding():
    """演示基本方法重写"""
    print("=== 基本方法重写演示 ===")
    
    animals = [
        Dog("旺财"),
        Cat("咪咪"),
        Bird("小鸟"),
        Fish("金鱼", "海水")
    ]
    
    for animal in animals:
        animal_behavior(animal)

def demonstrate_shape_overriding():
    """演示形状类方法重写"""
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Triangle(3, 4, 5)
    ]
    
    calculate_shape_properties(shapes)

def demonstrate_vehicle_overriding():
    """演示车辆类方法重写"""
    vehicles = [
        Car("丰田", "凯美瑞", 2023, 4),
        Motorcycle("本田", "CBR600", 2023, 600),
        Truck("东风", "天龙", 2023, 10000)
    ]
    
    for vehicle in vehicles:
        operate_vehicle(vehicle)

def demonstrate_employee_overriding():
    """演示员工类方法重写"""
    employees = [
        Manager("张经理", "M001", 15000, 5),
        Developer("李开发", "D001", 12000, ["Python", "Java", "JavaScript"]),
        Salesperson("王销售", "S001", 8000, 100000)
    ]
    
    # 为销售员添加一些销售记录
    employees[2].record_sale(30000)
    
    for employee in employees:
        process_employee(employee)

if __name__ == "__main__":
    # 演示基本方法重写
    demonstrate_basic_overriding()
    
    # 演示形状类方法重写
    demonstrate_shape_overriding()
    
    # 演示车辆类方法重写
    demonstrate_vehicle_overriding()
    
    # 演示员工类方法重写
    demonstrate_employee_overriding()
    
    print("=== 方法重写的核心要点 ===")
    print("1. 子类可以重写父类方法")
    print("2. 使用super()调用父类方法")
    print("3. 运行时动态绑定")
    print("4. 相同接口，不同实现")
    print("5. 支持扩展和定制")
    print("6. 实现真正的多态行为")