#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
方法重写（Method Overriding）

方法重写是指子类重新定义父类中已有的方法，以提供不同的实现。
这是多态性的重要体现，允许不同的子类对同一方法有不同的行为。

学习要点：
1. 方法重写的基本概念
2. 如何重写父类方法
3. 调用父类被重写的方法
4. 重写特殊方法（魔术方法）
5. 方法重写的最佳实践
"""

# 1. 基本方法重写
print("=== 1. 基本方法重写 ===")

class Shape:
    """形状基类"""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """计算面积 - 基类提供默认实现"""
        return 0
    
    def perimeter(self):
        """计算周长 - 基类提供默认实现"""
        return 0
    
    def describe(self):
        """描述形状"""
        return f"这是一个{self.name}"
    
    def display_info(self):
        """显示形状信息"""
        print(f"形状: {self.name}")
        print(f"面积: {self.area()}")
        print(f"周长: {self.perimeter()}")
        print(f"描述: {self.describe()}")

class Rectangle(Shape):
    """矩形类 - 重写父类方法"""
    
    def __init__(self, width, height):
        super().__init__("矩形")
        self.width = width
        self.height = height
    
    def area(self):
        """重写面积计算方法"""
        return self.width * self.height
    
    def perimeter(self):
        """重写周长计算方法"""
        return 2 * (self.width + self.height)
    
    def describe(self):
        """重写描述方法"""
        return f"这是一个{self.width}x{self.height}的{self.name}"

class Circle(Shape):
    """圆形类 - 重写父类方法"""
    
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius = radius
    
    def area(self):
        """重写面积计算方法"""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """重写周长计算方法"""
        import math
        return 2 * math.pi * self.radius
    
    def describe(self):
        """重写描述方法"""
        return f"这是一个半径为{self.radius}的{self.name}"

# 创建对象并测试方法重写
shapes = [
    Shape("基本形状"),
    Rectangle(5, 3),
    Circle(4)
]

for shape in shapes:
    shape.display_info()
    print("-" * 30)

print("\n=== 2. 调用父类被重写的方法 ===")

# 2. 在重写方法中调用父类方法
class Animal:
    """动物基类"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print(f"{self.name} 发出了声音")
    
    def introduce(self):
        print(f"我是{self.species} {self.name}")

class Dog(Animal):
    """狗类"""
    
    def __init__(self, name, breed):
        super().__init__(name, "狗")
        self.breed = breed
    
    def make_sound(self):
        # 先调用父类方法
        super().make_sound()
        # 再添加子类特有的行为
        print(f"{self.name} 汪汪叫")
    
    def introduce(self):
        # 调用父类的introduce方法
        super().introduce()
        # 添加额外信息
        print(f"我是{self.breed}品种")

class Cat(Animal):
    """猫类"""
    
    def __init__(self, name, color):
        super().__init__(name, "猫")
        self.color = color
    
    def make_sound(self):
        # 完全重写，不调用父类方法
        print(f"{self.name} 喵喵叫")
    
    def introduce(self):
        super().introduce()
        print(f"我是{self.color}色的猫")

# 测试调用父类方法
dog = Dog("旺财", "金毛")
cat = Cat("咪咪", "白色")

print("狗的声音:")
dog.make_sound()
print("\n狗的自我介绍:")
dog.introduce()

print("\n猫的声音:")
cat.make_sound()
print("\n猫的自我介绍:")
cat.introduce()

print("\n=== 3. 重写特殊方法（魔术方法） ===")

# 3. 重写特殊方法
class Person:
    """人员基类"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    
    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

class Student(Person):
    """学生类 - 重写特殊方法"""
    
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade
    
    def __str__(self):
        """重写字符串表示"""
        return f"Student(name='{self.name}', age={self.age}, id='{self.student_id}', grade={self.grade})"
    
    def __repr__(self):
        """重写官方字符串表示"""
        return f"Student('{self.name}', {self.age}, '{self.student_id}', {self.grade})"
    
    def __eq__(self, other):
        """重写相等比较"""
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False
    
    def __hash__(self):
        """重写哈希方法"""
        return hash(self.student_id)

class Teacher(Person):
    """教师类 - 重写特殊方法"""
    
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject
    
    def __str__(self):
        return f"Teacher(name='{self.name}', age={self.age}, id='{self.employee_id}', subject='{self.subject}')"
    
    def __repr__(self):
        return f"Teacher('{self.name}', {self.age}, '{self.employee_id}', '{self.subject}')"
    
    def __eq__(self, other):
        if isinstance(other, Teacher):
            return self.employee_id == other.employee_id
        return False

# 测试重写的特殊方法
person = Person("张三", 25)
student1 = Student("李四", 20, "S001", 85)
student2 = Student("王五", 21, "S002", 90)
student3 = Student("李四", 22, "S001", 88)  # 同一个学生，不同信息
teacher = Teacher("赵老师", 35, "T001", "数学")

print("字符串表示:")
print(f"Person: {person}")
print(f"Student: {student1}")
print(f"Teacher: {teacher}")

print("\n官方字符串表示:")
print(f"Person repr: {repr(person)}")
print(f"Student repr: {repr(student1)}")
print(f"Teacher repr: {repr(teacher)}")

print("\n相等性比较:")
print(f"student1 == student2: {student1 == student2}")
print(f"student1 == student3: {student1 == student3}")
print(f"person == student1: {person == student1}")

print("\n年龄比较:")
people = [person, student1, student2, teacher]
people.sort()  # 使用__lt__方法排序
print("按年龄排序:")
for p in people:
    print(f"  {p}")

print("\n=== 4. 方法重写的多态性 ===")

# 4. 多态性演示
class MediaPlayer:
    """媒体播放器基类"""
    
    def __init__(self, name):
        self.name = name
        self.is_playing = False
    
    def play(self):
        self.is_playing = True
        print(f"{self.name} 开始播放")
    
    def stop(self):
        self.is_playing = False
        print(f"{self.name} 停止播放")
    
    def get_status(self):
        status = "播放中" if self.is_playing else "已停止"
        return f"{self.name} 状态: {status}"

class AudioPlayer(MediaPlayer):
    """音频播放器"""
    
    def __init__(self, name, format):
        super().__init__(name)
        self.format = format
    
    def play(self):
        print(f"正在播放{self.format}音频文件...")
        super().play()
        print("♪ 音乐响起 ♪")
    
    def adjust_volume(self, volume):
        print(f"调整音量到 {volume}%")

class VideoPlayer(MediaPlayer):
    """视频播放器"""
    
    def __init__(self, name, resolution):
        super().__init__(name)
        self.resolution = resolution
    
    def play(self):
        print(f"正在播放{self.resolution}视频文件...")
        super().play()
        print("📺 视频开始播放 📺")
    
    def toggle_fullscreen(self):
        print("切换全屏模式")

class StreamingPlayer(MediaPlayer):
    """流媒体播放器"""
    
    def __init__(self, name, url):
        super().__init__(name)
        self.url = url
    
    def play(self):
        print(f"连接到流媒体服务器: {self.url}")
        print("缓冲中...")
        super().play()
        print("🌐 在线流媒体播放中 🌐")
    
    def check_connection(self):
        print("检查网络连接状态")

# 多态性演示
def demonstrate_polymorphism(players):
    """演示多态性 - 同一接口，不同实现"""
    print("多态性演示 - 所有播放器都调用play()方法:")
    for player in players:
        print(f"\n--- {player.__class__.__name__} ---")
        player.play()
        print(player.get_status())
        player.stop()
        print()

# 创建不同类型的播放器
players = [
    AudioPlayer("MP3播放器", "MP3"),
    VideoPlayer("视频播放器", "1080P"),
    StreamingPlayer("在线播放器", "https://stream.example.com")
]

demonstrate_polymorphism(players)

print("=== 5. 方法重写的最佳实践 ===")
print("""
方法重写的最佳实践：

1. 保持方法签名一致
   - 方法名、参数列表应与父类保持一致
   - 返回类型应兼容父类方法

2. 合理使用super()
   - 需要扩展父类功能时使用super()
   - 完全替换功能时可以不调用super()

3. 文档说明
   - 在重写方法中添加文档字符串
   - 说明重写的原因和新的行为

4. 遵循里氏替换原则
   - 子类对象应该能够替换父类对象
   - 重写的方法不应该破坏父类的契约

5. 测试覆盖
   - 确保重写的方法被充分测试
   - 验证多态性的正确性
""")

if __name__ == "__main__":
    print("\n方法重写演示完成!")
    print("方法重写是实现多态性的重要机制，让不同的子类可以有不同的行为。")