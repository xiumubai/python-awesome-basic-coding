# 继承练习题

本文档包含了关于Python继承的综合练习题，涵盖从基础到高级的各个方面。通过这些练习，你将深入理解继承的概念和应用。

## 练习1：基础继承

### 题目描述
创建一个动物类层次结构，包括基类Animal和子类Dog、Cat。实现基本的继承关系和方法重写。

### 要求
1. Animal类包含name、age属性和speak()、info()方法
2. Dog类继承Animal，重写speak()方法，添加breed属性
3. Cat类继承Animal，重写speak()方法，添加color属性
4. 实现多态性演示

### 解答

```python
class Animal:
    """动物基类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return f"{self.name} 发出声音"
    
    def info(self):
        return f"动物信息: {self.name}, {self.age}岁"
    
    def sleep(self):
        return f"{self.name} 正在睡觉"

class Dog(Animal):
    """狗类"""
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def speak(self):
        return f"{self.name} 汪汪叫"
    
    def info(self):
        base_info = super().info()
        return f"{base_info}, 品种: {self.breed}"
    
    def fetch(self, item):
        return f"{self.name} 去捡 {item}"

class Cat(Animal):
    """猫类"""
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        return f"{self.name} 喵喵叫"
    
    def info(self):
        base_info = super().info()
        return f"{base_info}, 颜色: {self.color}"
    
    def climb(self, target):
        return f"{self.name} 爬到 {target} 上"

# 多态性演示
def animal_sounds(animals):
    """演示多态性"""
    for animal in animals:
        print(f"{animal.speak()} - {animal.info()}")

# 测试代码
dog = Dog("旺财", 3, "金毛")
cat = Cat("咪咪", 2, "橘色")

print("=== 练习1：基础继承 ===")
print(dog.speak())
print(dog.info())
print(dog.fetch("球"))
print()

print(cat.speak())
print(cat.info())
print(cat.climb("树"))
print()

print("多态性演示:")
animal_sounds([dog, cat])
```

## 练习2：方法重写和super()函数

### 题目描述
创建一个员工管理系统，展示方法重写和super()函数的使用。

### 要求
1. Employee基类包含基本信息和salary计算
2. Manager类继承Employee，有额外的bonus
3. Developer类继承Employee，有技能列表
4. 正确使用super()调用父类方法

### 解答

```python
class Employee:
    """员工基类"""
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
        self.department = "未分配"
    
    def calculate_salary(self):
        """计算工资"""
        return self.base_salary
    
    def get_info(self):
        """获取员工信息"""
        return f"员工: {self.name} (ID: {self.employee_id}), 部门: {self.department}"
    
    def work(self):
        """工作方法"""
        return f"{self.name} 正在工作"

class Manager(Employee):
    """经理类"""
    def __init__(self, name, employee_id, base_salary, bonus_rate=0.2):
        super().__init__(name, employee_id, base_salary)
        self.bonus_rate = bonus_rate
        self.department = "管理部"
        self.team_size = 0
    
    def calculate_salary(self):
        """重写工资计算，包含奖金"""
        base = super().calculate_salary()
        bonus = base * self.bonus_rate
        return base + bonus
    
    def get_info(self):
        """重写信息获取，添加团队信息"""
        base_info = super().get_info()
        return f"{base_info}, 团队规模: {self.team_size}人, 奖金率: {self.bonus_rate*100}%"
    
    def manage_team(self, team_size):
        """管理团队"""
        self.team_size = team_size
        return f"{self.name} 管理 {team_size} 人的团队"
    
    def work(self):
        """重写工作方法"""
        base_work = super().work()
        return f"{base_work} - 管理团队和制定策略"

class Developer(Employee):
    """开发者类"""
    def __init__(self, name, employee_id, base_salary, programming_languages=None):
        super().__init__(name, employee_id, base_salary)
        self.programming_languages = programming_languages or []
        self.department = "技术部"
        self.projects_completed = 0
    
    def calculate_salary(self):
        """重写工资计算，根据技能数量调整"""
        base = super().calculate_salary()
        skill_bonus = len(self.programming_languages) * 1000
        project_bonus = self.projects_completed * 500
        return base + skill_bonus + project_bonus
    
    def get_info(self):
        """重写信息获取，添加技能信息"""
        base_info = super().get_info()
        skills = ", ".join(self.programming_languages) if self.programming_languages else "无"
        return f"{base_info}, 技能: {skills}, 完成项目: {self.projects_completed}个"
    
    def add_skill(self, language):
        """添加编程技能"""
        if language not in self.programming_languages:
            self.programming_languages.append(language)
            return f"{self.name} 学会了 {language}"
        return f"{self.name} 已经掌握 {language}"
    
    def complete_project(self):
        """完成项目"""
        self.projects_completed += 1
        return f"{self.name} 完成了第 {self.projects_completed} 个项目"
    
    def work(self):
        """重写工作方法"""
        base_work = super().work()
        return f"{base_work} - 编写代码和解决技术问题"

# 测试代码
print("\n=== 练习2：方法重写和super()函数 ===")

# 创建员工
employee = Employee("张三", "E001", 5000)
manager = Manager("李四", "M001", 8000, 0.25)
developer = Developer("王五", "D001", 7000, ["Python", "JavaScript"])

# 测试基本功能
print("基本信息:")
print(employee.get_info())
print(f"工资: {employee.calculate_salary()}元")
print(employee.work())
print()

print(manager.get_info())
print(manager.manage_team(5))
print(f"工资: {manager.calculate_salary()}元")
print(manager.work())
print()

print(developer.get_info())
print(developer.add_skill("Java"))
print(developer.complete_project())
print(developer.complete_project())
print(f"更新后工资: {developer.calculate_salary()}元")
print(developer.work())
```

## 练习3：多继承和MRO

### 题目描述
创建一个多继承的类层次结构，演示方法解析顺序（MRO）和多继承的使用。

### 要求
1. 创建多个基类（Mixin类）
2. 使用多继承组合功能
3. 理解和演示MRO
4. 正确使用super()在多继承中

### 解答

```python
# Mixin类 - 提供特定功能
class TimestampMixin:
    """时间戳混入类"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from datetime import datetime
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_timestamp(self):
        from datetime import datetime
        self.updated_at = datetime.now()
        return f"时间戳已更新: {self.updated_at}"
    
    def get_age(self):
        from datetime import datetime
        age = datetime.now() - self.created_at
        return f"存在时间: {age.total_seconds():.2f}秒"

class SerializableMixin:
    """序列化混入类"""
    def to_dict(self):
        """转换为字典"""
        result = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                if hasattr(value, 'isoformat'):  # datetime对象
                    result[key] = value.isoformat()
                else:
                    result[key] = value
        return result
    
    def from_dict(self, data):
        """从字典恢复"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return "数据已恢复"

class ValidatableMixin:
    """验证混入类"""
    def validate(self):
        """验证对象状态"""
        errors = []
        
        # 检查必需属性
        required_attrs = getattr(self, '_required_attrs', [])
        for attr in required_attrs:
            if not hasattr(self, attr) or getattr(self, attr) is None:
                errors.append(f"缺少必需属性: {attr}")
        
        # 检查属性类型
        type_checks = getattr(self, '_type_checks', {})
        for attr, expected_type in type_checks.items():
            if hasattr(self, attr):
                value = getattr(self, attr)
                if value is not None and not isinstance(value, expected_type):
                    errors.append(f"属性 {attr} 类型错误，期望 {expected_type.__name__}")
        
        return errors if errors else ["验证通过"]

# 基础类
class BaseModel:
    """基础模型类"""
    def __init__(self, name):
        self.name = name
        super().__init__()  # 重要：调用super()以支持多继承
    
    def __str__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

# 使用多继承的具体类
class User(BaseModel, TimestampMixin, SerializableMixin, ValidatableMixin):
    """用户类 - 多继承示例"""
    _required_attrs = ['name', 'email']
    _type_checks = {'name': str, 'email': str, 'age': int}
    
    def __init__(self, name, email, age=None):
        self.email = email
        self.age = age
        super().__init__(name)  # 调用所有父类的__init__
    
    def get_info(self):
        return f"用户: {self.name}, 邮箱: {self.email}, 年龄: {self.age}"

class Product(BaseModel, TimestampMixin, SerializableMixin, ValidatableMixin):
    """产品类 - 不同的多继承组合"""
    _required_attrs = ['name', 'price']
    _type_checks = {'name': str, 'price': (int, float), 'stock': int}
    
    def __init__(self, name, price, stock=0):
        self.price = price
        self.stock = stock
        super().__init__(name)
    
    def get_info(self):
        return f"产品: {self.name}, 价格: {self.price}元, 库存: {self.stock}"

# 测试代码
print("\n=== 练习3：多继承和MRO ===")

# 查看MRO
print("User类的MRO:")
for i, cls in enumerate(User.__mro__):
    print(f"  {i+1}. {cls.__name__}")
print()

print("Product类的MRO:")
for i, cls in enumerate(Product.__mro__):
    print(f"  {i+1}. {cls.__name__}")
print()

# 创建对象并测试功能
user = User("张三", "zhangsan@example.com", 25)
product = Product("笔记本电脑", 5999.99, 10)

print("用户对象测试:")
print(user.get_info())
print(user.get_age())
print("验证结果:", user.validate())
print("序列化:", user.to_dict())
print()

print("产品对象测试:")
print(product.get_info())
print(product.update_timestamp())
print("验证结果:", product.validate())
print()

# 测试验证失败的情况
invalid_user = User("", "invalid-email", "not-a-number")
print("无效用户验证:")
for error in invalid_user.validate():
    print(f"  - {error}")
```

## 练习4：抽象基类

### 题目描述
使用抽象基类创建一个图形计算系统，定义接口契约。

### 要求
1. 创建抽象基类Shape
2. 定义抽象方法area()和perimeter()
3. 实现具体的图形类
4. 使用抽象属性

### 解答

```python
from abc import ABC, abstractmethod, abstractproperty
import math

class Shape(ABC):
    """抽象图形基类"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """计算面积 - 抽象方法"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """计算周长 - 抽象方法"""
        pass
    
    @property
    @abstractmethod
    def shape_type(self):
        """图形类型 - 抽象属性"""
        pass
    
    def get_info(self):
        """获取图形信息 - 具体方法"""
        return f"{self.shape_type}: {self.name}"
    
    def compare_area(self, other):
        """比较面积"""
        if not isinstance(other, Shape):
            return "无法比较：不是图形对象"
        
        self_area = self.area()
        other_area = other.area()
        
        if self_area > other_area:
            return f"{self.name} 的面积大于 {other.name}"
        elif self_area < other_area:
            return f"{self.name} 的面积小于 {other.name}"
        else:
            return f"{self.name} 和 {other.name} 的面积相等"

class Rectangle(Shape):
    """矩形类"""
    
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    @property
    def shape_type(self):
        return "矩形"
    
    def is_square(self):
        """判断是否为正方形"""
        return self.width == self.height

class Circle(Shape):
    """圆形类"""
    
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    @property
    def shape_type(self):
        return "圆形"
    
    def diameter(self):
        """计算直径"""
        return 2 * self.radius

class Triangle(Shape):
    """三角形类"""
    
    def __init__(self, name, side_a, side_b, side_c):
        super().__init__(name)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        
        # 验证三角形的有效性
        if not self._is_valid_triangle():
            raise ValueError("无效的三角形边长")
    
    def _is_valid_triangle(self):
        """验证三角形三边关系"""
        return (self.side_a + self.side_b > self.side_c and
                self.side_a + self.side_c > self.side_b and
                self.side_b + self.side_c > self.side_a)
    
    def area(self):
        """使用海伦公式计算面积"""
        s = self.perimeter() / 2  # 半周长
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
    
    @property
    def shape_type(self):
        return "三角形"
    
    def triangle_type(self):
        """判断三角形类型"""
        sides = sorted([self.side_a, self.side_b, self.side_c])
        if sides[0] == sides[1] == sides[2]:
            return "等边三角形"
        elif sides[0] == sides[1] or sides[1] == sides[2]:
            return "等腰三角形"
        else:
            return "普通三角形"

# 图形管理器
class ShapeManager:
    """图形管理器"""
    
    def __init__(self):
        self.shapes = []
    
    def add_shape(self, shape):
        """添加图形"""
        if not isinstance(shape, Shape):
            raise TypeError("只能添加Shape的子类实例")
        self.shapes.append(shape)
        return f"已添加图形: {shape.get_info()}"
    
    def total_area(self):
        """计算总面积"""
        return sum(shape.area() for shape in self.shapes)
    
    def largest_shape(self):
        """找到面积最大的图形"""
        if not self.shapes:
            return None
        return max(self.shapes, key=lambda s: s.area())
    
    def shapes_by_type(self):
        """按类型分组图形"""
        type_groups = {}
        for shape in self.shapes:
            shape_type = shape.shape_type
            if shape_type not in type_groups:
                type_groups[shape_type] = []
            type_groups[shape_type].append(shape)
        return type_groups
    
    def get_summary(self):
        """获取摘要信息"""
        if not self.shapes:
            return "没有图形"
        
        summary = [f"图形总数: {len(self.shapes)}"]
        summary.append(f"总面积: {self.total_area():.2f}")
        
        largest = self.largest_shape()
        if largest:
            summary.append(f"最大图形: {largest.get_info()} (面积: {largest.area():.2f})")
        
        type_groups = self.shapes_by_type()
        summary.append("图形类型分布:")
        for shape_type, shapes in type_groups.items():
            summary.append(f"  {shape_type}: {len(shapes)}个")
        
        return "\n".join(summary)

# 测试代码
print("\n=== 练习4：抽象基类 ===")

# 创建图形
rectangle = Rectangle("矩形A", 5, 3)
circle = Circle("圆形B", 4)
triangle = Triangle("三角形C", 3, 4, 5)
square = Rectangle("正方形D", 4, 4)

# 测试图形功能
shapes = [rectangle, circle, triangle, square]

print("图形信息:")
for shape in shapes:
    print(f"{shape.get_info()}:")
    print(f"  面积: {shape.area():.2f}")
    print(f"  周长: {shape.perimeter():.2f}")
    
    # 特殊方法测试
    if isinstance(shape, Rectangle):
        print(f"  是否为正方形: {shape.is_square()}")
    elif isinstance(shape, Circle):
        print(f"  直径: {shape.diameter():.2f}")
    elif isinstance(shape, Triangle):
        print(f"  三角形类型: {shape.triangle_type()}")
    print()

# 使用图形管理器
manager = ShapeManager()
for shape in shapes:
    print(manager.add_shape(shape))

print("\n管理器摘要:")
print(manager.get_summary())

# 图形比较
print("\n图形面积比较:")
print(rectangle.compare_area(circle))
print(triangle.compare_area(square))
```

## 练习5：组合vs继承设计

### 题目描述
设计一个媒体播放器系统，对比继承和组合两种设计方案。

### 要求
1. 先用继承方式设计
2. 再用组合方式重新设计
3. 对比两种方案的优缺点
4. 展示组合的灵活性

### 解答

```python
print("\n=== 练习5：组合vs继承设计 ===")

# 方案1：继承方式设计
print("--- 方案1：继承方式 ---")

class MediaPlayer:
    """媒体播放器基类"""
    def __init__(self, name):
        self.name = name
        self.is_playing = False
        self.volume = 50
    
    def play(self):
        self.is_playing = True
        return f"{self.name} 开始播放"
    
    def pause(self):
        self.is_playing = False
        return f"{self.name} 暂停播放"
    
    def set_volume(self, volume):
        self.volume = max(0, min(100, volume))
        return f"{self.name} 音量设置为 {self.volume}"

class AudioPlayer(MediaPlayer):
    """音频播放器"""
    def __init__(self, name):
        super().__init__(name)
        self.equalizer_enabled = False
    
    def enable_equalizer(self):
        self.equalizer_enabled = True
        return f"{self.name} 均衡器已启用"
    
    def play_audio(self, audio_file):
        play_msg = self.play()
        return f"{play_msg} - 音频文件: {audio_file}"

class VideoPlayer(MediaPlayer):
    """视频播放器"""
    def __init__(self, name):
        super().__init__(name)
        self.subtitle_enabled = False
        self.quality = "720p"
    
    def enable_subtitle(self):
        self.subtitle_enabled = True
        return f"{self.name} 字幕已启用"
    
    def set_quality(self, quality):
        self.quality = quality
        return f"{self.name} 画质设置为 {quality}"
    
    def play_video(self, video_file):
        play_msg = self.play()
        return f"{play_msg} - 视频文件: {video_file} ({self.quality})"

# 问题：如果需要一个既能播放音频又能播放视频的播放器怎么办？
# 继承方式很难解决这个问题

# 测试继承方式
audio_player = AudioPlayer("音频播放器")
video_player = VideoPlayer("视频播放器")

print(audio_player.play_audio("music.mp3"))
print(audio_player.enable_equalizer())
print()

print(video_player.play_video("movie.mp4"))
print(video_player.enable_subtitle())
print(video_player.set_quality("1080p"))
print()

# 方案2：组合方式设计
print("--- 方案2：组合方式 ---")

# 功能组件
class AudioProcessor:
    """音频处理组件"""
    def __init__(self):
        self.equalizer_enabled = False
        self.bass_boost = False
    
    def play_audio(self, audio_file):
        effects = []
        if self.equalizer_enabled:
            effects.append("均衡器")
        if self.bass_boost:
            effects.append("低音增强")
        
        effect_str = f" (效果: {', '.join(effects)})" if effects else ""
        return f"播放音频: {audio_file}{effect_str}"
    
    def enable_equalizer(self):
        self.equalizer_enabled = True
        return "音频均衡器已启用"
    
    def enable_bass_boost(self):
        self.bass_boost = True
        return "低音增强已启用"

class VideoProcessor:
    """视频处理组件"""
    def __init__(self):
        self.subtitle_enabled = False
        self.quality = "720p"
        self.brightness = 50
    
    def play_video(self, video_file):
        settings = [f"画质: {self.quality}"]
        if self.subtitle_enabled:
            settings.append("字幕: 开")
        settings.append(f"亮度: {self.brightness}%")
        
        return f"播放视频: {video_file} ({', '.join(settings)})"
    
    def enable_subtitle(self):
        self.subtitle_enabled = True
        return "视频字幕已启用"
    
    def set_quality(self, quality):
        self.quality = quality
        return f"视频画质设置为 {quality}"
    
    def set_brightness(self, brightness):
        self.brightness = max(0, min(100, brightness))
        return f"视频亮度设置为 {self.brightness}%"

class PlaybackController:
    """播放控制组件"""
    def __init__(self):
        self.is_playing = False
        self.volume = 50
        self.position = 0
    
    def play(self):
        self.is_playing = True
        return "开始播放"
    
    def pause(self):
        self.is_playing = False
        return "暂停播放"
    
    def stop(self):
        self.is_playing = False
        self.position = 0
        return "停止播放"
    
    def set_volume(self, volume):
        self.volume = max(0, min(100, volume))
        return f"音量设置为 {self.volume}"
    
    def seek(self, position):
        self.position = position
        return f"跳转到 {position}秒"

class FlexibleMediaPlayer:
    """灵活的媒体播放器 - 使用组合"""
    def __init__(self, name):
        self.name = name
        self.controller = PlaybackController()
        self.audio_processor = None
        self.video_processor = None
    
    def add_audio_support(self):
        """添加音频支持"""
        self.audio_processor = AudioProcessor()
        return f"{self.name} 已添加音频支持"
    
    def add_video_support(self):
        """添加视频支持"""
        self.video_processor = VideoProcessor()
        return f"{self.name} 已添加视频支持"
    
    def play_media(self, media_file, media_type):
        """播放媒体文件"""
        control_msg = self.controller.play()
        
        if media_type == "audio" and self.audio_processor:
            media_msg = self.audio_processor.play_audio(media_file)
        elif media_type == "video" and self.video_processor:
            media_msg = self.video_processor.play_video(media_file)
        else:
            return f"{self.name} 不支持 {media_type} 格式"
        
        return f"{self.name}: {control_msg} - {media_msg}"
    
    def get_capabilities(self):
        """获取播放器能力"""
        capabilities = ["基础播放控制"]
        if self.audio_processor:
            capabilities.append("音频播放")
        if self.video_processor:
            capabilities.append("视频播放")
        return f"{self.name} 支持: {', '.join(capabilities)}"

# 测试组合方式
print("创建不同类型的播放器:")

# 纯音频播放器
audio_only = FlexibleMediaPlayer("纯音频播放器")
print(audio_only.add_audio_support())
print(audio_only.get_capabilities())
print(audio_only.play_media("song.mp3", "audio"))
if audio_only.audio_processor:
    print(audio_only.audio_processor.enable_equalizer())
print()

# 纯视频播放器
video_only = FlexibleMediaPlayer("纯视频播放器")
print(video_only.add_video_support())
print(video_only.get_capabilities())
print(video_only.play_media("movie.mp4", "video"))
if video_only.video_processor:
    print(video_only.video_processor.set_quality("4K"))
print()

# 多媒体播放器（既支持音频又支持视频）
multimedia = FlexibleMediaPlayer("多媒体播放器")
print(multimedia.add_audio_support())
print(multimedia.add_video_support())
print(multimedia.get_capabilities())
print(multimedia.play_media("music.mp3", "audio"))
print(multimedia.play_media("video.mp4", "video"))
print()

# 基础播放器（只有控制功能）
basic = FlexibleMediaPlayer("基础播放器")
print(basic.get_capabilities())
print(basic.play_media("file.mp3", "audio"))  # 不支持
print()

print("--- 设计方案对比 ---")
print("""
继承方式的问题:
1. 难以支持多种媒体类型的组合
2. 类层次结构固定，扩展困难
3. 代码重复（如果需要AudioVideoPlayer）
4. 违反单一职责原则

组合方式的优势:
1. 灵活的功能组合
2. 运行时可以改变行为
3. 符合单一职责原则
4. 易于测试和维护
5. 支持渐进式功能添加

结论：对于需要灵活功能组合的场景，组合优于继承
""")
```

## 练习6：综合应用

### 题目描述
设计一个完整的学生管理系统，综合运用继承、组合、抽象基类等概念。

### 要求
1. 使用抽象基类定义接口
2. 合理使用继承和组合
3. 实现多态性
4. 包含完整的功能演示

### 解答

```python
from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import List, Dict, Optional

print("\n=== 练习6：综合应用 - 学生管理系统 ===")

# 抽象基类
class Person(ABC):
    """人员抽象基类"""
    def __init__(self, name: str, age: int, id_number: str):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.created_at = datetime.now()
    
    @abstractmethod
    def get_role(self) -> str:
        """获取角色"""
        pass
    
    @abstractmethod
    def get_info(self) -> str:
        """获取详细信息"""
        pass
    
    def get_basic_info(self) -> str:
        """获取基本信息"""
        return f"{self.get_role()}: {self.name} (年龄: {self.age}, ID: {self.id_number})"

# 成绩管理组件
class GradeManager:
    """成绩管理组件"""
    def __init__(self):
        self.grades: Dict[str, float] = {}  # 科目 -> 成绩
    
    def add_grade(self, subject: str, score: float) -> str:
        """添加成绩"""
        if 0 <= score <= 100:
            self.grades[subject] = score
            return f"已添加 {subject} 成绩: {score}分"
        return "成绩必须在0-100之间"
    
    def get_average(self) -> float:
        """计算平均分"""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
    
    def get_grade_level(self) -> str:
        """获取成绩等级"""
        avg = self.get_average()
        if avg >= 90:
            return "优秀"
        elif avg >= 80:
            return "良好"
        elif avg >= 70:
            return "中等"
        elif avg >= 60:
            return "及格"
        else:
            return "不及格"
    
    def get_grades_summary(self) -> str:
        """获取成绩摘要"""
        if not self.grades:
            return "暂无成绩记录"
        
        summary = ["成绩详情:"]
        for subject, score in self.grades.items():
            summary.append(f"  {subject}: {score}分")
        summary.append(f"平均分: {self.get_average():.2f}分")
        summary.append(f"等级: {self.get_grade_level()}")
        return "\n".join(summary)

# 出勤管理组件
class AttendanceManager:
    """出勤管理组件"""
    def __init__(self):
        self.attendance_records: List[Dict] = []  # 出勤记录
    
    def mark_attendance(self, date_str: str, status: str) -> str:
        """标记出勤"""
        valid_statuses = ["出勤", "缺勤", "迟到", "早退", "请假"]
        if status not in valid_statuses:
            return f"无效的出勤状态，有效值: {', '.join(valid_statuses)}"
        
        # 检查是否已有当天记录
        for record in self.attendance_records:
            if record['date'] == date_str:
                record['status'] = status
                return f"已更新 {date_str} 的出勤状态为: {status}"
        
        # 添加新记录
        self.attendance_records.append({
            'date': date_str,
            'status': status,
            'timestamp': datetime.now()
        })
        return f"已记录 {date_str} 的出勤状态: {status}"
    
    def get_attendance_rate(self) -> float:
        """计算出勤率"""
        if not self.attendance_records:
            return 0.0
        
        present_count = sum(1 for record in self.attendance_records 
                          if record['status'] in ["出勤", "迟到"])
        return (present_count / len(self.attendance_records)) * 100
    
    def get_attendance_summary(self) -> str:
        """获取出勤摘要"""
        if not self.attendance_records:
            return "暂无出勤记录"
        
        status_count = {}
        for record in self.attendance_records:
            status = record['status']
            status_count[status] = status_count.get(status, 0) + 1
        
        summary = ["出勤统计:"]
        for status, count in status_count.items():
            summary.append(f"  {status}: {count}天")
        summary.append(f"出勤率: {self.get_attendance_rate():.1f}%")
        return "\n".join(summary)

# 学生类
class Student(Person):
    """学生类"""
    def __init__(self, name: str, age: int, student_id: str, class_name: str):
        super().__init__(name, age, student_id)
        self.class_name = class_name
        self.grade_manager = GradeManager()  # 组合：成绩管理
        self.attendance_manager = AttendanceManager()  # 组合：出勤管理
    
    def get_role(self) -> str:
        return "学生"
    
    def get_info(self) -> str:
        basic = self.get_basic_info()
        return f"{basic}, 班级: {self.class_name}"
    
    def add_grade(self, subject: str, score: float) -> str:
        return self.grade_manager.add_grade(subject, score)
    
    def mark_attendance(self, date_str: str, status: str) -> str:
        return self.attendance_manager.mark_attendance(date_str, status)
    
    def get_full_report(self) -> str:
        """获取完整报告"""
        report = [self.get_info()]
        report.append(self.grade_manager.get_grades_summary())
        report.append(self.attendance_manager.get_attendance_summary())
        return "\n\n".join(report)

# 教师类
class Teacher(Person):
    """教师类"""
    def __init__(self, name: str, age: int, teacher_id: str, subject: str, department: str):
        super().__init__(name, age, teacher_id)
        self.subject = subject
        self.department = department
        self.students: List[Student] = []  # 管理的学生列表
    
    def get_role(self) -> str:
        return "教师"
    
    def get_info(self) -> str:
        basic = self.get_basic_info()
        return f"{basic}, 科目: {self.subject}, 部门: {self.department}"
    
    def add_student(self, student: Student) -> str:
        """添加学生"""
        if student not in self.students:
            self.students.append(student)
            return f"已将学生 {student.name} 添加到 {self.name} 老师的班级"
        return f"学生 {student.name} 已在班级中"
    
    def grade_student(self, student_name: str, score: float) -> str:
        """给学生打分"""
        for student in self.students:
            if student.name == student_name:
                return student.add_grade(self.subject, score)
        return f"未找到学生: {student_name}"
    
    def get_class_average(self) -> float:
        """获取班级平均分"""
        if not self.students:
            return 0.0
        
        total_avg = 0
        count = 0
        for student in self.students:
            if self.subject in student.grade_manager.grades:
                total_avg += student.grade_manager.grades[self.subject]
                count += 1
        
        return total_avg / count if count > 0 else 0.0
    
    def get_class_report(self) -> str:
        """获取班级报告"""
        if not self.students:
            return f"{self.name} 老师暂无学生"
        
        report = [f"{self.name} 老师的 {self.subject} 课程报告:"]
        report.append(f"学生人数: {len(self.students)}")
        report.append(f"班级平均分: {self.get_class_average():.2f}分")
        report.append("\n学生详情:")
        
        for student in self.students:
            grade = student.grade_manager.grades.get(self.subject, "未评分")
            attendance_rate = student.attendance_manager.get_attendance_rate()
            report.append(f"  {student.name}: {grade}分, 出勤率: {attendance_rate:.1f}%")
        
        return "\n".join(report)

# 学校管理系统
class SchoolManagementSystem:
    """学校管理系统"""
    def __init__(self, school_name: str):
        self.school_name = school_name
        self.students: List[Student] = []
        self.teachers: List[Teacher] = []
    
    def add_student(self, student: Student) -> str:
        """添加学生"""
        self.students.append(student)
        return f"已添加学生: {student.name}"
    
    def add_teacher(self, teacher: Teacher) -> str:
        """添加教师"""
        self.teachers.append(teacher)
        return f"已添加教师: {teacher.name}"
    
    def find_student(self, name: str) -> Optional[Student]:
        """查找学生"""
        for student in self.students:
            if student.name == name:
                return student
        return None
    
    def find_teacher(self, name: str) -> Optional[Teacher]:
        """查找教师"""
        for teacher in self.teachers:
            if teacher.name == name:
                return teacher
        return None
    
    def get_school_summary(self) -> str:
        """获取学校摘要"""
        summary = [f"{self.school_name} 管理系统摘要:"]
        summary.append(f"学生总数: {len(self.students)}")
        summary.append(f"教师总数: {len(self.teachers)}")
        
        if self.students:
            total_avg = sum(s.grade_manager.get_average() for s in self.students)
            school_avg = total_avg / len(self.students)
            summary.append(f"学校平均分: {school_avg:.2f}分")
        
        return "\n".join(summary)

# 测试综合应用
print("创建学校管理系统...")
school = SchoolManagementSystem("阳光中学")

# 创建学生
students_data = [
    ("张三", 16, "S001", "高一(1)班"),
    ("李四", 17, "S002", "高一(1)班"),
    ("王五", 16, "S003", "高一(2)班"),
]

students = []
for name, age, sid, class_name in students_data:
    student = Student(name, age, sid, class_name)
    students.append(student)
    print(school.add_student(student))

# 创建教师
math_teacher = Teacher("陈老师", 35, "T001", "数学", "数学系")
english_teacher = Teacher("刘老师", 32, "T002", "英语", "外语系")

print(school.add_teacher(math_teacher))
print(school.add_teacher(english_teacher))
print()

# 建立师生关系
for student in students:
    print(math_teacher.add_student(student))
    print(english_teacher.add_student(student))
print()

# 添加成绩
print("添加成绩...")
grade_data = [
    ("张三", [("数学", 85), ("英语", 78)]),
    ("李四", [("数学", 92), ("英语", 88)]),
    ("王五", [("数学", 76), ("英语", 82)]),
]

for student_name, grades in grade_data:
    student = school.find_student(student_name)
    if student:
        for subject, score in grades:
            print(student.add_grade(subject, score))
print()

# 添加出勤记录
print("添加出勤记录...")
attendance_data = [
    ("张三", [("2024-01-15", "出勤"), ("2024-01-16", "迟到"), ("2024-01-17", "出勤")]),
    ("李四", [("2024-01-15", "出勤"), ("2024-01-16", "出勤"), ("2024-01-17", "请假")]),
    ("王五", [("2024-01-15", "缺勤"), ("2024-01-16", "出勤"), ("2024-01-17", "出勤")]),
]

for student_name, records in attendance_data:
    student = school.find_student(student_name)
    if student:
        for date_str, status in records:
            print(student.mark_attendance(date_str, status))
print()

# 生成报告
print("=== 学生个人报告 ===")
for student in students:
    print(student.get_full_report())
    print("-" * 50)

print("\n=== 教师班级报告 ===")
print(math_teacher.get_class_report())
print()
print(english_teacher.get_class_report())
print()

print("=== 学校总体摘要 ===")
print(school.get_school_summary())
```

## 总结

通过这些练习，我们深入学习了Python继承的各个方面：

### 核心概念
1. **基础继承**：理解is-a关系，掌握基本语法
2. **方法重写**：学会重写父类方法，正确使用super()
3. **多继承**：理解MRO，掌握多继承的使用技巧
4. **抽象基类**：使用ABC定义接口契约
5. **组合vs继承**：理解两种设计方式的优缺点

### 设计原则
1. **里氏替换原则**：子类应该能够替换父类
2. **单一职责原则**：每个类应该只有一个改变的理由
3. **组合优于继承**：优先考虑组合，谨慎使用继承
4. **接口隔离原则**：使用抽象基类定义清晰的接口

### 最佳实践
1. **合理使用继承**：确保真正的is-a关系
2. **正确使用super()**：特别是在多继承中
3. **灵活运用组合**：提高代码的灵活性和可维护性
4. **混合使用**：在合适的场景下结合继承和组合

### 实际应用
通过综合练习，我们看到了如何在实际项目中：
- 设计合理的类层次结构
- 使用组合提供灵活的功能组合
- 应用抽象基类确保接口一致性
- 实现多态性提高代码的可扩展性

这些练习涵盖了从基础到高级的各个层面，帮助你全面掌握Python继承的概念和应用。