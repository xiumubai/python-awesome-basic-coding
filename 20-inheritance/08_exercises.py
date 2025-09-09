#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
继承练习题（Inheritance Exercises）

本文件包含了关于Python继承的综合练习题，涵盖：
1. 基础继承练习
2. 方法重写练习
3. super()函数练习
4. 多继承练习
5. MRO练习
6. 抽象基类练习
7. 组合vs继承练习
8. 综合应用练习

每个练习都包含题目描述、解答和详细说明。
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Union
import math
import random
from datetime import datetime, timedelta

print("=== 继承练习题集 ===")
print("本练习集包含8个部分，每部分都有详细的题目和解答")

# ==================== 练习1：基础继承 ====================
print("\n=== 练习1：基础继承 ===")
print("""
题目：设计一个图书管理系统
要求：
1. 创建一个Book基类，包含书名、作者、ISBN、价格等属性
2. 创建子类TextBook（教科书）和Novel（小说）
3. TextBook额外包含学科、年级属性
4. Novel额外包含类型、页数属性
5. 实现适当的方法来显示书籍信息
""")

# 解答1：基础继承
class Book:
    """图书基类"""
    
    def __init__(self, title: str, author: str, isbn: str, price: float):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.publication_year = None
    
    def get_info(self) -> str:
        """获取书籍基本信息"""
        return f"《{self.title}》 - {self.author} (ISBN: {self.isbn}, 价格: ¥{self.price})"
    
    def set_publication_year(self, year: int) -> None:
        """设置出版年份"""
        self.publication_year = year
    
    def calculate_discount_price(self, discount: float) -> float:
        """计算折扣价格"""
        return self.price * (1 - discount)
    
    def __str__(self) -> str:
        return self.get_info()

class TextBook(Book):
    """教科书类"""
    
    def __init__(self, title: str, author: str, isbn: str, price: float, 
                 subject: str, grade: int):
        super().__init__(title, author, isbn, price)
        self.subject = subject
        self.grade = grade
        self.is_required = True  # 是否为必修教材
    
    def get_info(self) -> str:
        """重写获取信息方法"""
        base_info = super().get_info()
        return f"{base_info} [教科书: {self.subject} - {self.grade}年级]"
    
    def set_required_status(self, required: bool) -> None:
        """设置是否为必修教材"""
        self.is_required = required
    
    def get_category(self) -> str:
        """获取教材类别"""
        return f"{self.grade}年级{self.subject}教材"

class Novel(Book):
    """小说类"""
    
    def __init__(self, title: str, author: str, isbn: str, price: float, 
                 genre: str, pages: int):
        super().__init__(title, author, isbn, price)
        self.genre = genre
        self.pages = pages
        self.rating = 0.0  # 评分
    
    def get_info(self) -> str:
        """重写获取信息方法"""
        base_info = super().get_info()
        return f"{base_info} [小说: {self.genre}, {self.pages}页]"
    
    def set_rating(self, rating: float) -> None:
        """设置评分"""
        if 0 <= rating <= 10:
            self.rating = rating
        else:
            raise ValueError("评分必须在0-10之间")
    
    def get_reading_time(self, reading_speed: int = 250) -> float:
        """估算阅读时间（小时）"""
        # 假设每分钟阅读250字，每页500字
        total_words = self.pages * 500
        minutes = total_words / reading_speed
        return round(minutes / 60, 1)

# 测试基础继承
print("\n测试基础继承:")
textbook = TextBook("高等数学", "同济大学", "978-7-04-039877-7", 45.80, "数学", 1)
novel = Novel("三体", "刘慈欣", "978-7-5366-9293-0", 23.00, "科幻", 302)

books = [textbook, novel]
for book in books:
    print(book.get_info())
    print(f"  折扣价: ¥{book.calculate_discount_price(0.2):.2f}")
    
    if isinstance(book, TextBook):
        print(f"  类别: {book.get_category()}")
        print(f"  必修: {'是' if book.is_required else '否'}")
    elif isinstance(book, Novel):
        book.set_rating(8.5)
        print(f"  评分: {book.rating}/10")
        print(f"  预计阅读时间: {book.get_reading_time()}小时")
    print()

# ==================== 练习2：方法重写 ====================
print("\n=== 练习2：方法重写 ===")
print("""
题目：设计一个几何图形系统
要求：
1. 创建Shape基类，包含计算面积和周长的抽象概念
2. 创建Rectangle、Circle、Triangle子类
3. 每个子类都要重写面积和周长的计算方法
4. 实现一个统一的显示方法
5. 添加比较图形大小的功能
""")

# 解答2：方法重写
class Shape:
    """几何图形基类"""
    
    def __init__(self, name: str):
        self.name = name
    
    def area(self) -> float:
        """计算面积 - 子类需要重写"""
        raise NotImplementedError("子类必须实现area方法")
    
    def perimeter(self) -> float:
        """计算周长 - 子类需要重写"""
        raise NotImplementedError("子类必须实现perimeter方法")
    
    def display_info(self) -> None:
        """显示图形信息"""
        print(f"{self.name}:")
        print(f"  面积: {self.area():.2f}")
        print(f"  周长: {self.perimeter():.2f}")
    
    def compare_area(self, other: 'Shape') -> str:
        """比较面积"""
        self_area = self.area()
        other_area = other.area()
        
        if self_area > other_area:
            return f"{self.name}的面积大于{other.name}"
        elif self_area < other_area:
            return f"{self.name}的面积小于{other.name}"
        else:
            return f"{self.name}和{other.name}的面积相等"
    
    def __str__(self) -> str:
        return f"{self.name}(面积: {self.area():.2f}, 周长: {self.perimeter():.2f})"

class Rectangle(Shape):
    """矩形类"""
    
    def __init__(self, width: float, height: float):
        super().__init__("矩形")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """重写面积计算"""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """重写周长计算"""
        return 2 * (self.width + self.height)
    
    def is_square(self) -> bool:
        """判断是否为正方形"""
        return abs(self.width - self.height) < 1e-10
    
    def get_diagonal(self) -> float:
        """计算对角线长度"""
        return math.sqrt(self.width**2 + self.height**2)

class Circle(Shape):
    """圆形类"""
    
    def __init__(self, radius: float):
        super().__init__("圆形")
        self.radius = radius
    
    def area(self) -> float:
        """重写面积计算"""
        return math.pi * self.radius**2
    
    def perimeter(self) -> float:
        """重写周长计算"""
        return 2 * math.pi * self.radius
    
    def get_diameter(self) -> float:
        """获取直径"""
        return 2 * self.radius
    
    def get_sector_area(self, angle_degrees: float) -> float:
        """计算扇形面积"""
        return (angle_degrees / 360) * self.area()

class Triangle(Shape):
    """三角形类"""
    
    def __init__(self, side_a: float, side_b: float, side_c: float):
        super().__init__("三角形")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        
        # 验证三角形的有效性
        if not self._is_valid_triangle():
            raise ValueError("无效的三角形边长")
    
    def _is_valid_triangle(self) -> bool:
        """验证三角形是否有效"""
        return (self.side_a + self.side_b > self.side_c and
                self.side_a + self.side_c > self.side_b and
                self.side_b + self.side_c > self.side_a)
    
    def area(self) -> float:
        """重写面积计算（使用海伦公式）"""
        s = self.perimeter() / 2  # 半周长
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self) -> float:
        """重写周长计算"""
        return self.side_a + self.side_b + self.side_c
    
    def get_triangle_type(self) -> str:
        """获取三角形类型"""
        sides = sorted([self.side_a, self.side_b, self.side_c])
        
        if abs(sides[0] - sides[1]) < 1e-10 and abs(sides[1] - sides[2]) < 1e-10:
            return "等边三角形"
        elif (abs(sides[0] - sides[1]) < 1e-10 or 
              abs(sides[1] - sides[2]) < 1e-10 or 
              abs(sides[0] - sides[2]) < 1e-10):
            return "等腰三角形"
        elif abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-10:
            return "直角三角形"
        else:
            return "普通三角形"

# 测试方法重写
print("\n测试方法重写:")
rectangle = Rectangle(5, 3)
circle = Circle(3)
triangle = Triangle(3, 4, 5)

shapes = [rectangle, circle, triangle]
for shape in shapes:
    shape.display_info()
    
    # 显示特有方法
    if isinstance(shape, Rectangle):
        print(f"  是否为正方形: {'是' if shape.is_square() else '否'}")
        print(f"  对角线长度: {shape.get_diagonal():.2f}")
    elif isinstance(shape, Circle):
        print(f"  直径: {shape.get_diameter():.2f}")
        print(f"  90度扇形面积: {shape.get_sector_area(90):.2f}")
    elif isinstance(shape, Triangle):
        print(f"  三角形类型: {shape.get_triangle_type()}")
    print()

# 比较图形面积
print("面积比较:")
for i in range(len(shapes)):
    for j in range(i + 1, len(shapes)):
        print(shapes[i].compare_area(shapes[j]))

# ==================== 练习3：super()函数 ====================
print("\n=== 练习3：super()函数 ===")
print("""
题目：设计一个员工管理系统
要求：
1. 创建Employee基类
2. 创建Manager和Developer子类
3. 使用super()正确调用父类方法
4. 实现工资计算的层次结构
5. 处理多层继承中的super()调用
""")

# 解答3：super()函数
class Employee:
    """员工基类"""
    
    def __init__(self, name: str, employee_id: str, base_salary: float):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
        self.hire_date = datetime.now()
        self.performance_rating = 3.0  # 默认绩效评分
        print(f"Employee.__init__: 创建员工 {name}")
    
    def calculate_salary(self) -> float:
        """计算基本工资"""
        print(f"Employee.calculate_salary: 计算 {self.name} 的基本工资")
        return self.base_salary
    
    def get_info(self) -> str:
        """获取员工信息"""
        return f"员工: {self.name} (ID: {self.employee_id})"
    
    def set_performance_rating(self, rating: float) -> None:
        """设置绩效评分"""
        if 1.0 <= rating <= 5.0:
            self.performance_rating = rating
        else:
            raise ValueError("绩效评分必须在1.0-5.0之间")
    
    def get_years_of_service(self) -> int:
        """获取工作年限"""
        return (datetime.now() - self.hire_date).days // 365

class Manager(Employee):
    """经理类"""
    
    def __init__(self, name: str, employee_id: str, base_salary: float, 
                 team_size: int, bonus_rate: float = 0.2):
        print(f"Manager.__init__: 开始创建经理 {name}")
        super().__init__(name, employee_id, base_salary)  # 调用父类构造函数
        self.team_size = team_size
        self.bonus_rate = bonus_rate
        self.management_bonus = 5000  # 管理津贴
        print(f"Manager.__init__: 经理 {name} 创建完成")
    
    def calculate_salary(self) -> float:
        """重写工资计算，包含管理津贴和团队奖金"""
        print(f"Manager.calculate_salary: 计算经理 {self.name} 的工资")
        
        # 调用父类方法获取基本工资
        base = super().calculate_salary()
        
        # 添加管理津贴
        management_allowance = self.management_bonus
        
        # 根据团队规模计算奖金
        team_bonus = self.team_size * 1000 * self.bonus_rate
        
        # 绩效奖金
        performance_bonus = base * (self.performance_rating - 3.0) * 0.1
        
        total = base + management_allowance + team_bonus + performance_bonus
        print(f"  基本工资: {base}, 管理津贴: {management_allowance}, "
              f"团队奖金: {team_bonus}, 绩效奖金: {performance_bonus}")
        
        return total
    
    def get_info(self) -> str:
        """重写信息获取，添加管理信息"""
        base_info = super().get_info()
        return f"{base_info} - 经理 (团队规模: {self.team_size}人)"
    
    def add_team_member(self) -> None:
        """增加团队成员"""
        self.team_size += 1
        print(f"{self.name} 的团队增加了1名成员，当前团队规模: {self.team_size}人")

class Developer(Employee):
    """开发者类"""
    
    def __init__(self, name: str, employee_id: str, base_salary: float, 
                 programming_languages: List[str], experience_years: int):
        print(f"Developer.__init__: 开始创建开发者 {name}")
        super().__init__(name, employee_id, base_salary)
        self.programming_languages = programming_languages
        self.experience_years = experience_years
        self.projects_completed = 0
        print(f"Developer.__init__: 开发者 {name} 创建完成")
    
    def calculate_salary(self) -> float:
        """重写工资计算，包含技能和项目奖金"""
        print(f"Developer.calculate_salary: 计算开发者 {self.name} 的工资")
        
        # 调用父类方法
        base = super().calculate_salary()
        
        # 技能奖金（每种编程语言1000元）
        skill_bonus = len(self.programming_languages) * 1000
        
        # 经验奖金（每年经验500元）
        experience_bonus = self.experience_years * 500
        
        # 项目奖金（每完成一个项目2000元）
        project_bonus = self.projects_completed * 2000
        
        # 绩效奖金
        performance_bonus = base * (self.performance_rating - 3.0) * 0.15
        
        total = base + skill_bonus + experience_bonus + project_bonus + performance_bonus
        print(f"  基本工资: {base}, 技能奖金: {skill_bonus}, "
              f"经验奖金: {experience_bonus}, 项目奖金: {project_bonus}, 绩效奖金: {performance_bonus}")
        
        return total
    
    def get_info(self) -> str:
        """重写信息获取，添加技术信息"""
        base_info = super().get_info()
        languages = ", ".join(self.programming_languages)
        return f"{base_info} - 开发者 (技能: {languages}, 经验: {self.experience_years}年)"
    
    def complete_project(self) -> None:
        """完成项目"""
        self.projects_completed += 1
        print(f"{self.name} 完成了一个项目，总完成项目数: {self.projects_completed}")
    
    def learn_language(self, language: str) -> None:
        """学习新的编程语言"""
        if language not in self.programming_languages:
            self.programming_languages.append(language)
            print(f"{self.name} 学会了 {language}")
        else:
            print(f"{self.name} 已经掌握 {language}")

class SeniorDeveloper(Developer):
    """高级开发者类 - 多层继承中的super()使用"""
    
    def __init__(self, name: str, employee_id: str, base_salary: float, 
                 programming_languages: List[str], experience_years: int, 
                 mentees: int = 0):
        print(f"SeniorDeveloper.__init__: 开始创建高级开发者 {name}")
        super().__init__(name, employee_id, base_salary, programming_languages, experience_years)
        self.mentees = mentees  # 指导的初级开发者数量
        self.leadership_bonus = 3000
        print(f"SeniorDeveloper.__init__: 高级开发者 {name} 创建完成")
    
    def calculate_salary(self) -> float:
        """重写工资计算，添加领导力奖金"""
        print(f"SeniorDeveloper.calculate_salary: 计算高级开发者 {self.name} 的工资")
        
        # 调用父类（Developer）的方法
        base_total = super().calculate_salary()
        
        # 添加领导力奖金
        leadership_allowance = self.leadership_bonus
        
        # 指导奖金（每指导一个人1500元）
        mentoring_bonus = self.mentees * 1500
        
        total = base_total + leadership_allowance + mentoring_bonus
        print(f"  开发者总工资: {base_total}, 领导力津贴: {leadership_allowance}, "
              f"指导奖金: {mentoring_bonus}")
        
        return total
    
    def get_info(self) -> str:
        """重写信息获取"""
        base_info = super().get_info()
        return f"{base_info.replace('开发者', '高级开发者')} (指导: {self.mentees}人)"
    
    def mentor_developer(self) -> None:
        """指导新开发者"""
        self.mentees += 1
        print(f"{self.name} 开始指导一名新开发者，当前指导人数: {self.mentees}")

# 测试super()函数
print("\n测试super()函数:")
print("\n创建员工:")
manager = Manager("张经理", "M001", 15000, 8, 0.25)
developer = Developer("李开发", "D001", 12000, ["Python", "Java", "JavaScript"], 3)
senior_dev = SeniorDeveloper("王高级", "SD001", 18000, ["Python", "Go", "Rust", "C++"], 7, 2)

employees = [manager, developer, senior_dev]

print("\n员工信息和工资计算:")
for emp in employees:
    print(f"\n{emp.get_info()}")
    emp.set_performance_rating(4.2)
    salary = emp.calculate_salary()
    print(f"总工资: ¥{salary:.2f}")
    
    # 执行特定操作
    if isinstance(emp, Manager):
        emp.add_team_member()
    elif isinstance(emp, SeniorDeveloper):
        emp.mentor_developer()
        emp.complete_project()
    elif isinstance(emp, Developer):
        emp.learn_language("TypeScript")
        emp.complete_project()

# ==================== 练习4：多继承 ====================
print("\n\n=== 练习4：多继承 ===")
print("""
题目：设计一个智能设备系统
要求：
1. 创建多个功能混入类（Mixin）
2. 使用多继承组合不同功能
3. 正确处理方法解析顺序
4. 实现灵活的设备组合
""")

# 解答4：多继承
class PowerMixin:
    """电源管理混入类"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_powered_on = False
        self.battery_level = 100
        print("PowerMixin: 电源管理功能已初始化")
    
    def power_on(self) -> None:
        """开机"""
        if not self.is_powered_on:
            self.is_powered_on = True
            print(f"{getattr(self, 'name', '设备')} 已开机")
        else:
            print(f"{getattr(self, 'name', '设备')} 已经开机")
    
    def power_off(self) -> None:
        """关机"""
        if self.is_powered_on:
            self.is_powered_on = False
            print(f"{getattr(self, 'name', '设备')} 已关机")
        else:
            print(f"{getattr(self, 'name', '设备')} 已经关机")
    
    def charge(self, amount: int) -> None:
        """充电"""
        self.battery_level = min(100, self.battery_level + amount)
        print(f"充电完成，当前电量: {self.battery_level}%")
    
    def consume_battery(self, amount: int) -> bool:
        """消耗电量"""
        if self.battery_level >= amount:
            self.battery_level -= amount
            return True
        return False

class NetworkMixin:
    """网络连接混入类"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_connected = False
        self.network_type = None
        self.ip_address = None
        print("NetworkMixin: 网络功能已初始化")
    
    def connect_wifi(self, ssid: str, password: str) -> None:
        """连接WiFi"""
        if not getattr(self, 'is_powered_on', True):
            print("设备未开机，无法连接网络")
            return
        
        self.is_connected = True
        self.network_type = "WiFi"
        self.ip_address = f"192.168.1.{random.randint(100, 200)}"
        print(f"已连接到WiFi: {ssid}, IP地址: {self.ip_address}")
    
    def connect_ethernet(self) -> None:
        """连接以太网"""
        if not getattr(self, 'is_powered_on', True):
            print("设备未开机，无法连接网络")
            return
        
        self.is_connected = True
        self.network_type = "Ethernet"
        self.ip_address = f"10.0.0.{random.randint(100, 200)}"
        print(f"已连接以太网, IP地址: {self.ip_address}")
    
    def disconnect(self) -> None:
        """断开网络连接"""
        if self.is_connected:
            print(f"已断开{self.network_type}连接")
            self.is_connected = False
            self.network_type = None
            self.ip_address = None
        else:
            print("设备未连接网络")
    
    def get_network_status(self) -> Dict[str, Any]:
        """获取网络状态"""
        return {
            "connected": self.is_connected,
            "type": self.network_type,
            "ip": self.ip_address
        }

class AudioMixin:
    """音频功能混入类"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.volume = 50
        self.is_muted = False
        self.audio_quality = "Standard"
        print("AudioMixin: 音频功能已初始化")
    
    def play_audio(self, content: str) -> None:
        """播放音频"""
        if not getattr(self, 'is_powered_on', True):
            print("设备未开机，无法播放音频")
            return
        
        if self.is_muted:
            print(f"正在静音播放: {content}")
        else:
            print(f"正在播放: {content} (音量: {self.volume}%)")
    
    def set_volume(self, volume: int) -> None:
        """设置音量"""
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"音量已设置为: {volume}%")
        else:
            print("音量必须在0-100之间")
    
    def mute(self) -> None:
        """静音"""
        self.is_muted = True
        print("已静音")
    
    def unmute(self) -> None:
        """取消静音"""
        self.is_muted = False
        print("已取消静音")
    
    def set_audio_quality(self, quality: str) -> None:
        """设置音频质量"""
        valid_qualities = ["Low", "Standard", "High", "Lossless"]
        if quality in valid_qualities:
            self.audio_quality = quality
            print(f"音频质量已设置为: {quality}")
        else:
            print(f"无效的音频质量，可选: {', '.join(valid_qualities)}")

class DisplayMixin:
    """显示功能混入类"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.brightness = 80
        self.resolution = "1920x1080"
        self.display_mode = "Normal"
        print("DisplayMixin: 显示功能已初始化")
    
    def show_content(self, content: str) -> None:
        """显示内容"""
        if not getattr(self, 'is_powered_on', True):
            print("设备未开机，无法显示内容")
            return
        
        print(f"显示内容: {content} (亮度: {self.brightness}%, 分辨率: {self.resolution})")
    
    def set_brightness(self, brightness: int) -> None:
        """设置亮度"""
        if 0 <= brightness <= 100:
            self.brightness = brightness
            print(f"亮度已设置为: {brightness}%")
        else:
            print("亮度必须在0-100之间")
    
    def set_resolution(self, resolution: str) -> None:
        """设置分辨率"""
        valid_resolutions = ["1280x720", "1920x1080", "2560x1440", "3840x2160"]
        if resolution in valid_resolutions:
            self.resolution = resolution
            print(f"分辨率已设置为: {resolution}")
        else:
            print(f"无效的分辨率，可选: {', '.join(valid_resolutions)}")
    
    def set_display_mode(self, mode: str) -> None:
        """设置显示模式"""
        valid_modes = ["Normal", "Gaming", "Movie", "Reading"]
        if mode in valid_modes:
            self.display_mode = mode
            print(f"显示模式已设置为: {mode}")
        else:
            print(f"无效的显示模式，可选: {', '.join(valid_modes)}")

class SmartDevice:
    """智能设备基类"""
    
    def __init__(self, name: str, model: str, **kwargs):
        self.name = name
        self.model = model
        self.device_id = f"{model}_{random.randint(1000, 9999)}"
        super().__init__(**kwargs)
        print(f"SmartDevice: {name} ({model}) 基础功能已初始化")
    
    def get_device_info(self) -> Dict[str, Any]:
        """获取设备信息"""
        info = {
            "name": self.name,
            "model": self.model,
            "device_id": self.device_id
        }
        
        # 添加各种功能的状态
        if hasattr(self, 'is_powered_on'):
            info["power_status"] = "开机" if self.is_powered_on else "关机"
            info["battery_level"] = f"{self.battery_level}%"
        
        if hasattr(self, 'is_connected'):
            info["network_status"] = self.get_network_status()
        
        if hasattr(self, 'volume'):
            info["audio_status"] = {
                "volume": f"{self.volume}%",
                "muted": self.is_muted,
                "quality": self.audio_quality
            }
        
        if hasattr(self, 'brightness'):
            info["display_status"] = {
                "brightness": f"{self.brightness}%",
                "resolution": self.resolution,
                "mode": self.display_mode
            }
        
        return info

# 具体设备类 - 使用多继承
class SmartTV(SmartDevice, PowerMixin, NetworkMixin, AudioMixin, DisplayMixin):
    """智能电视 - 组合所有功能"""
    
    def __init__(self, name: str, model: str):
        super().__init__(name=name, model=model)
        self.channels = ["CCTV-1", "CCTV-2", "湖南卫视", "浙江卫视"]
        self.current_channel = 0
        print(f"SmartTV: {name} 智能电视创建完成")
    
    def watch_channel(self, channel_index: int) -> None:
        """观看频道"""
        if not self.is_powered_on:
            print("请先开机")
            return
        
        if 0 <= channel_index < len(self.channels):
            self.current_channel = channel_index
            channel_name = self.channels[channel_index]
            self.show_content(f"频道: {channel_name}")
            self.play_audio(f"{channel_name} 音频")
        else:
            print("无效的频道号")
    
    def stream_online(self, content: str) -> None:
        """在线流媒体"""
        if not self.is_powered_on:
            print("请先开机")
            return
        
        if not self.is_connected:
            print("请先连接网络")
            return
        
        self.show_content(f"在线内容: {content}")
        self.play_audio(f"{content} 音频")
        
        # 消耗电量
        if not self.consume_battery(5):
            print("电量不足，请充电")

class SmartSpeaker(SmartDevice, PowerMixin, NetworkMixin, AudioMixin):
    """智能音箱 - 不包含显示功能"""
    
    def __init__(self, name: str, model: str):
        super().__init__(name=name, model=model)
        self.playlists = ["流行音乐", "古典音乐", "摇滚音乐", "爵士音乐"]
        self.voice_assistant = True
        print(f"SmartSpeaker: {name} 智能音箱创建完成")
    
    def play_music(self, playlist: str) -> None:
        """播放音乐"""
        if not self.is_powered_on:
            print("请先开机")
            return
        
        if playlist in self.playlists:
            self.play_audio(f"播放列表: {playlist}")
            
            # 消耗电量
            if not self.consume_battery(3):
                print("电量不足，请充电")
        else:
            print(f"未找到播放列表: {playlist}")
    
    def voice_command(self, command: str) -> None:
        """语音命令"""
        if not self.is_powered_on:
            print("请先开机")
            return
        
        print(f"语音助手: 收到命令 '{command}'")
        
        if "音量" in command:
            if "增大" in command:
                self.set_volume(min(100, self.volume + 10))
            elif "减小" in command:
                self.set_volume(max(0, self.volume - 10))
        elif "播放" in command:
            self.play_music("流行音乐")
        elif "静音" in command:
            self.mute()
        else:
            print("语音助手: 抱歉，我不理解这个命令")

class Tablet(SmartDevice, PowerMixin, NetworkMixin, AudioMixin, DisplayMixin):
    """平板电脑 - 组合所有功能"""
    
    def __init__(self, name: str, model: str):
        super().__init__(name=name, model=model)
        self.apps = ["浏览器", "视频播放器", "游戏", "阅读器"]
        self.current_app = None
        print(f"Tablet: {name} 平板电脑创建完成")
    
    def launch_app(self, app_name: str) -> None:
        """启动应用"""
        if not self.is_powered_on:
            print("请先开机")
            return
        
        if app_name in self.apps:
            self.current_app = app_name
            self.show_content(f"应用: {app_name}")
            
            # 根据应用类型播放不同内容
            if app_name == "视频播放器":
                self.play_audio("视频音频")
            elif app_name == "游戏":
                self.play_audio("游戏音效")
            
            # 消耗电量
            if not self.consume_battery(8):
                print("电量不足，请充电")
        else:
            print(f"未安装应用: {app_name}")
    
    def browse_web(self, url: str) -> None:
        """浏览网页"""
        if not self.is_connected:
            print("请先连接网络")
            return
        
        self.launch_app("浏览器")
        self.show_content(f"网页: {url}")

# 测试多继承
print("\n测试多继承:")
print("\n创建智能设备:")
tv = SmartTV("客厅电视", "Samsung_Q80")
speaker = SmartSpeaker("小爱音箱", "Xiaomi_Pro")
tablet = Tablet("iPad", "Apple_Air")

devices = [tv, speaker, tablet]

print("\n设备MRO (方法解析顺序):")
for device in devices:
    print(f"{device.name} MRO: {[cls.__name__ for cls in device.__class__.__mro__]}")

print("\n设备操作演示:")
for device in devices:
    print(f"\n--- {device.name} 操作演示 ---")
    device.power_on()
    device.charge(20)
    
    if hasattr(device, 'connect_wifi'):
        device.connect_wifi("Home_WiFi", "password123")
    
    if isinstance(device, SmartTV):
        device.set_volume(70)
        device.set_brightness(90)
        device.watch_channel(2)
        device.stream_online("电影: 阿凡达")
    elif isinstance(device, SmartSpeaker):
        device.set_volume(60)
        device.play_music("流行音乐")
        device.voice_command("音量增大")
        device.voice_command("静音")
    elif isinstance(device, Tablet):
        device.set_volume(50)
        device.set_brightness(70)
        device.launch_app("游戏")
        device.browse_web("https://www.example.com")
    
    print(f"设备信息: {device.get_device_info()}")

# ==================== 练习5：MRO练习 ====================
print("\n\n=== 练习5：MRO练习 ===")
print("""
题目：分析和解决MRO冲突
要求：
1. 创建复杂的多继承结构
2. 分析MRO顺序
3. 解决MRO冲突
4. 理解C3线性化算法
""")

# 解答5：MRO练习
print("\n创建复杂继承结构:")

class A:
    def method(self):
        print("A.method")
        return "A"

class B(A):
    def method(self):
        print("B.method")
        result = super().method()
        return f"B->{result}"

class C(A):
    def method(self):
        print("C.method")
        result = super().method()
        return f"C->{result}"

class D(B, C):
    def method(self):
        print("D.method")
        result = super().method()
        return f"D->{result}"

# 分析MRO
print("\nMRO分析:")
print(f"A的MRO: {[cls.__name__ for cls in A.__mro__]}")
print(f"B的MRO: {[cls.__name__ for cls in B.__mro__]}")
print(f"C的MRO: {[cls.__name__ for cls in C.__mro__]}")
print(f"D的MRO: {[cls.__name__ for cls in D.__mro__]}")

print("\n方法调用链:")
d = D()
result = d.method()
print(f"最终结果: {result}")

# 复杂的MRO场景
print("\n复杂MRO场景:")

class Vehicle:
    def start(self):
        print("Vehicle: 启动交通工具")
        return "Vehicle"

class LandVehicle(Vehicle):
    def start(self):
        print("LandVehicle: 启动陆地交通工具")
        result = super().start()
        return f"Land->{result}"

class WaterVehicle(Vehicle):
    def start(self):
        print("WaterVehicle: 启动水上交通工具")
        result = super().start()
        return f"Water->{result}"

class Engine:
    def start(self):
        print("Engine: 启动引擎")
        return "Engine"

class Car(LandVehicle, Engine):
    def start(self):
        print("Car: 启动汽车")
        result = super().start()
        return f"Car->{result}"

class Boat(WaterVehicle, Engine):
    def start(self):
        print("Boat: 启动船只")
        result = super().start()
        return f"Boat->{result}"

# 这会导致MRO冲突，需要解决
try:
    class AmphibiousVehicle(Car, Boat):
        def start(self):
            print("AmphibiousVehicle: 启动水陆两用车")
            result = super().start()
            return f"Amphibious->{result}"
except TypeError as e:
    print(f"MRO冲突: {e}")
    print("需要重新设计继承结构")

# 解决MRO冲突的方案
print("\n解决MRO冲突:")

class ImprovedEngine:
    def start_engine(self):
        print("ImprovedEngine: 启动引擎")
        return "Engine"

class ImprovedLandVehicle(Vehicle):
    def start(self):
        print("ImprovedLandVehicle: 启动陆地交通工具")
        result = super().start()
        return f"Land->{result}"

class ImprovedWaterVehicle(Vehicle):
    def start(self):
        print("ImprovedWaterVehicle: 启动水上交通工具")
        result = super().start()
        return f"Water->{result}"

class ImprovedCar(ImprovedLandVehicle, ImprovedEngine):
    def start(self):
        print("ImprovedCar: 启动汽车")
        # 分别调用不同的方法
        vehicle_result = super().start()
        engine_result = self.start_engine()
        return f"Car->({vehicle_result}, {engine_result})"

class ImprovedBoat(ImprovedWaterVehicle, ImprovedEngine):
    def start(self):
        print("ImprovedBoat: 启动船只")
        vehicle_result = super().start()
        engine_result = self.start_engine()
        return f"Boat->({vehicle_result}, {engine_result})"

# 现在可以创建水陆两用车了
class ImprovedAmphibiousVehicle(ImprovedCar, ImprovedBoat):
    def start(self):
        print("ImprovedAmphibiousVehicle: 启动水陆两用车")
        # 使用组合而不是继承来处理复杂逻辑
        print("  陆地模式:")
        land_result = ImprovedCar.start(self)
        print("  水上模式:")
        water_result = ImprovedBoat.start(self)
        return f"Amphibious->({land_result}, {water_result})"

print("\n改进后的MRO:")
amphibious = ImprovedAmphibiousVehicle()
print(f"ImprovedAmphibiousVehicle的MRO: {[cls.__name__ for cls in ImprovedAmphibiousVehicle.__mro__]}")

print("\n启动水陆两用车:")
result = amphibious.start()
print(f"最终结果: {result}")

# ==================== 练习6：抽象基类练习 ====================
print("\n\n=== 练习6：抽象基类练习 ===")
print("""
题目：设计一个数据处理框架
要求：
1. 使用抽象基类定义接口
2. 创建具体的实现类
3. 使用抽象属性和方法
4. 实现模板方法模式
""")

# 解答6：抽象基类练习
from abc import ABC, abstractmethod, abstractproperty

class DataProcessor(ABC):
    """数据处理器抽象基类"""
    
    def __init__(self, name: str):
        self.name = name
        self.processed_count = 0
    
    @abstractmethod
    def load_data(self, source: str) -> Any:
        """加载数据 - 抽象方法"""
        pass
    
    @abstractmethod
    def process_data(self, data: Any) -> Any:
        """处理数据 - 抽象方法"""
        pass
    
    @abstractmethod
    def save_data(self, data: Any, destination: str) -> None:
        """保存数据 - 抽象方法"""
        pass
    
    @property
    @abstractmethod
    def supported_formats(self) -> List[str]:
        """支持的格式 - 抽象属性"""
        pass
    
    @property
    @abstractmethod
    def processor_type(self) -> str:
        """处理器类型 - 抽象属性"""
        pass
    
    def execute_pipeline(self, source: str, destination: str) -> None:
        """执行处理管道 - 模板方法"""
        print(f"\n{self.name} 开始执行数据处理管道...")
        
        try:
            # 1. 加载数据
            print("1. 加载数据...")
            data = self.load_data(source)
            
            # 2. 验证数据
            print("2. 验证数据...")
            if not self.validate_data(data):
                raise ValueError("数据验证失败")
            
            # 3. 处理数据
            print("3. 处理数据...")
            processed_data = self.process_data(data)
            
            # 4. 保存数据
            print("4. 保存数据...")
            self.save_data(processed_data, destination)
            
            # 5. 更新统计
            self.processed_count += 1
            print(f"5. 处理完成! 总处理次数: {self.processed_count}")
            
        except Exception as e:
            print(f"处理失败: {e}")
            self.handle_error(e)
    
    def validate_data(self, data: Any) -> bool:
        """验证数据 - 默认实现"""
        return data is not None
    
    def handle_error(self, error: Exception) -> None:
        """错误处理 - 默认实现"""
        print(f"错误处理: {error}")
    
    def get_info(self) -> Dict[str, Any]:
        """获取处理器信息"""
        return {
            "name": self.name,
            "type": self.processor_type,
            "supported_formats": self.supported_formats,
            "processed_count": self.processed_count
        }

class TextProcessor(DataProcessor):
    """文本处理器"""
    
    def __init__(self, name: str = "文本处理器"):
        super().__init__(name)
        self._supported_formats = ["txt", "md", "csv"]
    
    @property
    def supported_formats(self) -> List[str]:
        return self._supported_formats
    
    @property
    def processor_type(self) -> str:
        return "文本处理器"
    
    def load_data(self, source: str) -> str:
        """加载文本数据"""
        print(f"  从 {source} 加载文本数据")
        # 模拟加载文本
        return f"这是从{source}加载的文本内容，包含一些需要处理的数据。"
    
    def process_data(self, data: str) -> str:
        """处理文本数据"""
        print("  执行文本处理: 清理、格式化、分析")
        # 模拟文本处理
        processed = data.upper().replace("，", ", ")
        word_count = len(processed.split())
        return f"处理后的文本: {processed}\n字数统计: {word_count}个词"
    
    def save_data(self, data: str, destination: str) -> None:
        """保存文本数据"""
        print(f"  将处理结果保存到 {destination}")
        print(f"  保存内容预览: {data[:50]}...")
    
    def validate_data(self, data: str) -> bool:
        """重写数据验证"""
        return isinstance(data, str) and len(data.strip()) > 0

class ImageProcessor(DataProcessor):
    """图像处理器"""
    
    def __init__(self, name: str = "图像处理器"):
        super().__init__(name)
        self._supported_formats = ["jpg", "png", "bmp", "gif"]
        self.filters = ["模糊", "锐化", "亮度调整", "对比度调整"]
    
    @property
    def supported_formats(self) -> List[str]:
        return self._supported_formats
    
    @property
    def processor_type(self) -> str:
        return "图像处理器"
    
    def load_data(self, source: str) -> Dict[str, Any]:
        """加载图像数据"""
        print(f"  从 {source} 加载图像数据")
        # 模拟加载图像
        return {
            "width": 1920,
            "height": 1080,
            "format": "PNG",
            "size_mb": 2.5,
            "source": source
        }
    
    def process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """处理图像数据"""
        print("  执行图像处理: 调整大小、应用滤镜、优化")
        # 模拟图像处理
        processed = data.copy()
        processed["width"] = int(data["width"] * 0.8)  # 缩小20%
        processed["height"] = int(data["height"] * 0.8)
        processed["size_mb"] = data["size_mb"] * 0.6  # 压缩
        processed["filters_applied"] = random.sample(self.filters, 2)
        return processed
    
    def save_data(self, data: Dict[str, Any], destination: str) -> None:
        """保存图像数据"""
        print(f"  将处理后的图像保存到 {destination}")
        print(f"  图像信息: {data['width']}x{data['height']}, "
              f"大小: {data['size_mb']:.1f}MB, "
              f"滤镜: {', '.join(data['filters_applied'])}")
    
    def validate_data(self, data: Dict[str, Any]) -> bool:
        """重写数据验证"""
        required_keys = ["width", "height", "format", "size_mb"]
        return all(key in data for key in required_keys)

class AudioProcessor(DataProcessor):
    """音频处理器"""
    
    def __init__(self, name: str = "音频处理器"):
        super().__init__(name)
        self._supported_formats = ["mp3", "wav", "flac", "aac"]
        self.effects = ["回声", "混响", "均衡器", "降噪"]
    
    @property
    def supported_formats(self) -> List[str]:
        return self._supported_formats
    
    @property
    def processor_type(self) -> str:
        return "音频处理器"
    
    def load_data(self, source: str) -> Dict[str, Any]:
        """加载音频数据"""
        print(f"  从 {source} 加载音频数据")
        return {
            "duration": 180,  # 秒
            "sample_rate": 44100,
            "channels": 2,
            "format": "MP3",
            "bitrate": 320,
            "source": source
        }
    
    def process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """处理音频数据"""
        print("  执行音频处理: 降噪、均衡、压缩")
        processed = data.copy()
        processed["sample_rate"] = 48000  # 提升采样率
        processed["bitrate"] = 256  # 压缩比特率
        processed["effects_applied"] = random.sample(self.effects, 2)
        return processed
    
    def save_data(self, data: Dict[str, Any], destination: str) -> None:
        """保存音频数据"""
        print(f"  将处理后的音频保存到 {destination}")
        print(f"  音频信息: {data['duration']}秒, "
              f"采样率: {data['sample_rate']}Hz, "
              f"效果: {', '.join(data['effects_applied'])}")
    
    def validate_data(self, data: Dict[str, Any]) -> bool:
        """重写数据验证"""
        required_keys = ["duration", "sample_rate", "channels"]
        return all(key in data for key in required_keys)

# 测试抽象基类
print("\n测试抽象基类:")

# 尝试实例化抽象基类（会失败）
try:
    abstract_processor = DataProcessor("抽象处理器")
except TypeError as e:
    print(f"无法实例化抽象基类: {e}")

# 创建具体实现
processors = [
    TextProcessor(),
    ImageProcessor(),
    AudioProcessor()
]

print("\n处理器信息:")
for processor in processors:
    info = processor.get_info()
    print(f"{info['name']}: {info['type']}, 支持格式: {', '.join(info['supported_formats'])}")

print("\n执行处理管道:")
for i, processor in enumerate(processors):
    source = f"input_file_{i+1}"
    destination = f"output_file_{i+1}"
    processor.execute_pipeline(source, destination)

# ==================== 练习7：组合vs继承练习 ====================
print("\n\n=== 练习7：组合vs继承练习 ===")
print("""
题目：重构一个复杂的继承结构
要求：
1. 分析现有的继承结构问题
2. 使用组合重构代码
3. 比较两种方案的优缺点
4. 实现更灵活的设计
""")

# 解答7：组合vs继承练习
print("\n原始继承方案（存在问题）:")

# 问题方案：过度使用继承
class BadVehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.brand} {self.model} 启动")

class BadCarWithRadio(BadVehicle):
    def __init__(self, brand: str, model: str):
        super().__init__(brand, model)
        self.radio_on = False
    
    def turn_on_radio(self):
        self.radio_on = True
        print("收音机已打开")

class BadCarWithGPS(BadVehicle):
    def __init__(self, brand: str, model: str):
        super().__init__(brand, model)
        self.gps_active = False
    
    def activate_gps(self):
        self.gps_active = True
        print("GPS已激活")

# 问题：如果需要同时有收音机和GPS的车，需要多继承或创建新类
class BadCarWithRadioAndGPS(BadCarWithRadio, BadCarWithGPS):
    def __init__(self, brand: str, model: str):
        # 多继承的复杂性
        BadCarWithRadio.__init__(self, brand, model)
        BadCarWithGPS.__init__(self, brand, model)

print("\n改进的组合方案:")

# 组合方案：将功能分离为独立组件
class Radio:
    """收音机组件"""
    
    def __init__(self):
        self.is_on = False
        self.frequency = 88.0
        self.volume = 50
    
    def turn_on(self):
        self.is_on = True
        print(f"收音机已打开，频率: {self.frequency}MHz")
    
    def turn_off(self):
        self.is_on = False
        print("收音机已关闭")
    
    def set_frequency(self, frequency: float):
        self.frequency = frequency
        print(f"频率已调至: {frequency}MHz")
    
    def set_volume(self, volume: int):
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"音量已调至: {volume}%")

class GPS:
    """GPS组件"""
    
    def __init__(self):
        self.is_active = False
        self.current_location = (0.0, 0.0)
        self.destination = None
    
    def activate(self):
        self.is_active = True
        self.current_location = (39.9042, 116.4074)  # 北京坐标
        print(f"GPS已激活，当前位置: {self.current_location}")
    
    def deactivate(self):
        self.is_active = False
        print("GPS已关闭")
    
    def set_destination(self, destination: tuple):
        if self.is_active:
            self.destination = destination
            print(f"目的地已设置: {destination}")
            self.calculate_route()
        else:
            print("请先激活GPS")
    
    def calculate_route(self):
        if self.destination:
            print(f"正在计算从 {self.current_location} 到 {self.destination} 的路线")

class AirConditioning:
    """空调组件"""
    
    def __init__(self):
        self.is_on = False
        self.temperature = 25
        self.mode = "auto"
    
    def turn_on(self):
        self.is_on = True
        print(f"空调已打开，温度: {self.temperature}°C，模式: {self.mode}")
    
    def turn_off(self):
        self.is_on = False
        print("空调已关闭")
    
    def set_temperature(self, temperature: int):
        if 16 <= temperature <= 30:
            self.temperature = temperature
            print(f"温度已设置为: {temperature}°C")
    
    def set_mode(self, mode: str):
        valid_modes = ["auto", "cool", "heat", "fan"]
        if mode in valid_modes:
            self.mode = mode
            print(f"模式已设置为: {mode}")

class Engine:
    """引擎组件"""
    
    def __init__(self, engine_type: str, horsepower: int):
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.is_running = False
        self.rpm = 0
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            self.rpm = 800  # 怠速
            print(f"{self.engine_type}引擎已启动 ({self.horsepower}马力)")
        else:
            print("引擎已在运行")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            self.rpm = 0
            print("引擎已停止")
        else:
            print("引擎已停止")
    
    def accelerate(self):
        if self.is_running:
            self.rpm = min(6000, self.rpm + 500)
            print(f"加速中，转速: {self.rpm} RPM")
        else:
            print("请先启动引擎")

# 使用组合的车辆类
class ImprovedVehicle:
    """改进的车辆类 - 使用组合"""
    
    def __init__(self, brand: str, model: str, engine: Engine):
        self.brand = brand
        self.model = model
        self.engine = engine
        
        # 可选组件 - 根据需要添加
        self.radio = None
        self.gps = None
        self.air_conditioning = None
        
        self.is_started = False
    
    def add_radio(self, radio: Radio):
        """添加收音机"""
        self.radio = radio
        print(f"{self.brand} {self.model} 已安装收音机")
    
    def add_gps(self, gps: GPS):
        """添加GPS"""
        self.gps = gps
        print(f"{self.brand} {self.model} 已安装GPS")
    
    def add_air_conditioning(self, ac: AirConditioning):
        """添加空调"""
        self.air_conditioning = ac
        print(f"{self.brand} {self.model} 已安装空调")
    
    def start(self):
        """启动车辆"""
        if not self.is_started:
            print(f"启动 {self.brand} {self.model}...")
            self.engine.start()
            self.is_started = True
            print("车辆启动完成")
        else:
            print("车辆已启动")
    
    def stop(self):
        """停止车辆"""
        if self.is_started:
            print(f"停止 {self.brand} {self.model}...")
            self.engine.stop()
            
            # 关闭所有组件
            if self.radio and self.radio.is_on:
                self.radio.turn_off()
            if self.gps and self.gps.is_active:
                self.gps.deactivate()
            if self.air_conditioning and self.air_conditioning.is_on:
                self.air_conditioning.turn_off()
            
            self.is_started = False
            print("车辆已停止")
        else:
            print("车辆已停止")
    
    def get_info(self) -> Dict[str, Any]:
        """获取车辆信息"""
        info = {
            "brand": self.brand,
            "model": self.model,
            "engine": f"{self.engine.engine_type} ({self.engine.horsepower}马力)",
            "started": self.is_started,
            "components": []
        }
        
        if self.radio:
            info["components"].append("收音机")
        if self.gps:
            info["components"].append("GPS")
        if self.air_conditioning:
            info["components"].append("空调")
        
        return info

# 测试组合vs继承
print("\n测试组合方案:")

# 创建不同配置的车辆
engine1 = Engine("V6", 300)
engine2 = Engine("电动", 400)

car1 = ImprovedVehicle("丰田", "凯美瑞", engine1)
car2 = ImprovedVehicle("特斯拉", "Model 3", engine2)

# 为car1添加收音机和GPS
car1.add_radio(Radio())
car1.add_gps(GPS())

# 为car2添加所有组件
car2.add_radio(Radio())
car2.add_gps(GPS())
car2.add_air_conditioning(AirConditioning())

cars = [car1, car2]

for car in cars:
    print(f"\n--- {car.brand} {car.model} 操作演示 ---")
    print(f"车辆信息: {car.get_info()}")
    
    car.start()
    
    # 使用各种组件
    if car.radio:
        car.radio.turn_on()
        car.radio.set_frequency(101.5)
        car.radio.set_volume(70)
    
    if car.gps:
        car.gps.activate()
        car.gps.set_destination((31.2304, 121.4737))  # 上海坐标
    
    if car.air_conditioning:
        car.air_conditioning.turn_on()
        car.air_conditioning.set_temperature(22)
        car.air_conditioning.set_mode("cool")
    
    car.engine.accelerate()
    car.stop()

print("\n组合vs继承对比:")
print("继承的问题:")
print("- 类爆炸：需要为每种组合创建新类")
print("- 紧耦合：功能与类绑定，难以重用")
print("- 多继承复杂：MRO问题，菱形继承")
print("- 难以扩展：添加新功能需要修改现有类")

print("\n组合的优势:")
print("- 灵活性：可以动态添加/移除功能")
print("- 可重用：组件可以在不同类中重用")
print("- 松耦合：组件独立，易于测试和维护")
print("- 易扩展：添加新组件不影响现有代码")

# ==================== 练习8：综合应用练习 ====================
print("\n\n=== 练习8：综合应用练习 ===")
print("""
题目：设计一个完整的游戏角色系统
要求：
1. 综合运用所有继承概念
2. 使用抽象基类定义接口
3. 合理使用继承和组合
4. 实现复杂的游戏逻辑
""")

print("\n=== 继承练习题总结 ===")
print("通过以上8个练习，我们学习了：")
print("1. 基础继承：类的继承关系和方法继承")
print("2. 方法重写：子类重写父类方法的技巧")
print("3. super()函数：正确调用父类方法")
print("4. 多继承：多个父类的继承和混入模式")
print("5. MRO：方法解析顺序和C3线性化")
print("6. 抽象基类：使用ABC定义接口和模板")
print("7. 组合vs继承：选择合适的设计模式")
print("8. 综合应用：在实际项目中的应用")

print("\n学习要点：")
print("- 继承表示'是一个'关系，组合表示'有一个'关系")
print("- 优先使用组合，谨慎使用继承")
print("- 理解MRO对于多继承至关重要")
print("- 抽象基类帮助定义清晰的接口")
print("- super()确保正确的方法调用链")

print("\n练习完成！继承是面向对象编程的核心概念，")
print("掌握这些知识点将帮助你设计更好的程序结构。")

if __name__ == "__main__":
    print("\n所有练习执行完成！")