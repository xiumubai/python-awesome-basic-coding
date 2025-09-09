#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多继承

Python支持多继承，即一个类可以同时继承多个父类。
多继承提供了强大的功能，但也带来了复杂性，需要谨慎使用。

学习要点：
1. 多继承的基本语法
2. 多继承的方法解析顺序（MRO）
3. 菱形继承问题
4. 混入类（Mixin）模式
5. 多继承的最佳实践
6. 多继承的优缺点
"""

# 1. 多继承的基本语法
print("=== 1. 多继承的基本语法 ===")

class Flyable:
    """可飞行的能力类"""
    
    def __init__(self):
        print("Flyable.__init__: 获得飞行能力")
        self.can_fly = True
    
    def fly(self):
        if self.can_fly:
            print(f"{getattr(self, 'name', '未知生物')} 正在飞行")
        else:
            print(f"{getattr(self, 'name', '未知生物')} 无法飞行")
    
    def take_off(self):
        print(f"{getattr(self, 'name', '未知生物')} 起飞")
    
    def land(self):
        print(f"{getattr(self, 'name', '未知生物')} 降落")

class Swimmable:
    """可游泳的能力类"""
    
    def __init__(self):
        print("Swimmable.__init__: 获得游泳能力")
        self.can_swim = True
    
    def swim(self):
        if self.can_swim:
            print(f"{getattr(self, 'name', '未知生物')} 正在游泳")
        else:
            print(f"{getattr(self, 'name', '未知生物')} 无法游泳")
    
    def dive(self):
        print(f"{getattr(self, 'name', '未知生物')} 潜水")
    
    def surface(self):
        print(f"{getattr(self, 'name', '未知生物')} 浮出水面")

class Animal:
    """动物基类"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"Animal.__init__: 创建{species} {name}")
    
    def eat(self):
        print(f"{self.name} 正在进食")
    
    def sleep(self):
        print(f"{self.name} 正在睡觉")
    
    def make_sound(self):
        print(f"{self.name} 发出声音")

# 多继承示例：鸭子既能飞又能游泳
class Duck(Animal, Flyable, Swimmable):
    """鸭子类 - 多继承示例"""
    
    def __init__(self, name):
        # 注意：需要显式调用所有父类的构造方法
        Animal.__init__(self, name, "鸭子")
        Flyable.__init__(self)
        Swimmable.__init__(self)
        print(f"Duck.__init__: {name} 创建完成")
    
    def make_sound(self):
        print(f"{self.name} 嘎嘎叫")
    
    def show_abilities(self):
        print(f"{self.name} 的能力:")
        print(f"  - 可以飞行: {self.can_fly}")
        print(f"  - 可以游泳: {self.can_swim}")

# 测试多继承
print("创建鸭子对象:")
duck = Duck("唐老鸭")
print("\n展示鸭子的能力:")
duck.show_abilities()
print("\n鸭子的行为:")
duck.eat()
duck.make_sound()
duck.fly()
duck.swim()
duck.take_off()
duck.dive()

# 查看继承关系
print(f"\nDuck类的父类: {Duck.__bases__}")
print(f"Duck类的MRO: {Duck.__mro__}")

print("\n=== 2. 使用super()处理多继承 ===")

# 2. 使用super()处理多继承的更好方式
class Flyable2:
    """改进的可飞行类 - 使用super()"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Flyable2.__init__: 获得飞行能力")
        self.can_fly = True
    
    def fly(self):
        print(f"{self.name} 正在飞行")

class Swimmable2:
    """改进的可游泳类 - 使用super()"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Swimmable2.__init__: 获得游泳能力")
        self.can_swim = True
    
    def swim(self):
        print(f"{self.name} 正在游泳")

class Animal2:
    """改进的动物基类 - 使用super()"""
    
    def __init__(self, name, species, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.species = species
        print(f"Animal2.__init__: 创建{species} {name}")
    
    def make_sound(self):
        print(f"{self.name} 发出声音")

class Duck2(Animal2, Flyable2, Swimmable2):
    """改进的鸭子类 - 使用super()链式调用"""
    
    def __init__(self, name, **kwargs):
        super().__init__(name=name, species="鸭子", **kwargs)
        print(f"Duck2.__init__: {name} 创建完成")
    
    def make_sound(self):
        print(f"{self.name} 嘎嘎叫")

# 测试改进的多继承
print("创建改进的鸭子对象:")
duck2 = Duck2("小黄鸭")
print("\n改进鸭子的行为:")
duck2.make_sound()
duck2.fly()
duck2.swim()

print(f"\nDuck2类的MRO: {Duck2.__mro__}")

print("\n=== 3. 菱形继承问题 ===")

# 3. 菱形继承问题（钻石问题）
class A:
    """顶层基类"""
    
    def __init__(self):
        print("A.__init__")
        self.value = "A"
    
    def method(self):
        print(f"A.method: {self.value}")

class B(A):
    """左分支"""
    
    def __init__(self):
        super().__init__()
        print("B.__init__")
        self.value += "->B"
    
    def method(self):
        super().method()
        print(f"B.method: {self.value}")

class C(A):
    """右分支"""
    
    def __init__(self):
        super().__init__()
        print("C.__init__")
        self.value += "->C"
    
    def method(self):
        super().method()
        print(f"C.method: {self.value}")

class D(B, C):
    """菱形继承的底部类"""
    
    def __init__(self):
        super().__init__()
        print("D.__init__")
        self.value += "->D"
    
    def method(self):
        super().method()
        print(f"D.method: {self.value}")

# 测试菱形继承
print("创建菱形继承对象:")
d = D()
print(f"\nD类的MRO: {D.__mro__}")
print("\n调用方法:")
d.method()
print(f"\n最终值: {d.value}")

print("\n=== 4. 混入类（Mixin）模式 ===")

# 4. 混入类（Mixin）模式
class TimestampMixin:
    """时间戳混入类"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        import datetime
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
    
    def update_timestamp(self):
        import datetime
        self.updated_at = datetime.datetime.now()
    
    def get_age(self):
        import datetime
        return datetime.datetime.now() - self.created_at

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
                    result[key] = str(value)
        return result
    
    def to_json(self):
        """转换为JSON字符串"""
        import json
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)

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
        attr_types = getattr(self, '_attr_types', {})
        for attr, expected_type in attr_types.items():
            if hasattr(self, attr):
                value = getattr(self, attr)
                if not isinstance(value, expected_type):
                    errors.append(f"属性 {attr} 类型错误: 期望 {expected_type.__name__}, 实际 {type(value).__name__}")
        
        return errors
    
    def is_valid(self):
        """检查对象是否有效"""
        return len(self.validate()) == 0

class User(TimestampMixin, SerializableMixin, ValidatableMixin):
    """用户类 - 使用多个混入类"""
    
    _required_attrs = ['username', 'email']
    _attr_types = {'username': str, 'email': str, 'age': int}
    
    def __init__(self, username, email, age=None, **kwargs):
        self.username = username
        self.email = email
        self.age = age
        super().__init__(**kwargs)
    
    def __str__(self):
        return f"User(username='{self.username}', email='{self.email}')"

# 测试混入类
print("创建用户对象（使用混入类）:")
user = User("张三", "zhangsan@example.com", 25)
print(f"用户: {user}")

print("\n验证用户:")
if user.is_valid():
    print("用户数据有效")
else:
    print(f"验证错误: {user.validate()}")

print("\n序列化用户:")
print("字典格式:")
print(user.to_dict())
print("\nJSON格式:")
print(user.to_json())

print("\n时间戳功能:")
import time
time.sleep(0.1)  # 等待一小段时间
user.update_timestamp()
print(f"创建时间: {user.created_at}")
print(f"更新时间: {user.updated_at}")
print(f"对象年龄: {user.get_age()}")

print(f"\nUser类的MRO: {User.__mro__}")

print("\n=== 5. 多继承中的方法冲突处理 ===")

# 5. 处理多继承中的方法冲突
class DatabaseMixin:
    """数据库操作混入类"""
    
    def save(self):
        print(f"DatabaseMixin: 保存 {self} 到数据库")
    
    def delete(self):
        print(f"DatabaseMixin: 从数据库删除 {self}")

class FileMixin:
    """文件操作混入类"""
    
    def save(self):
        print(f"FileMixin: 保存 {self} 到文件")
    
    def delete(self):
        print(f"FileMixin: 从文件系统删除 {self}")

class Document(DatabaseMixin, FileMixin):
    """文档类 - 演示方法冲突"""
    
    def __init__(self, title):
        self.title = title
    
    def save(self):
        # 方法1: 调用特定父类的方法
        print(f"Document.save: 保存文档 '{self.title}'")
        DatabaseMixin.save(self)  # 明确调用数据库保存
        FileMixin.save(self)      # 明确调用文件保存
    
    def __str__(self):
        return f"Document('{self.title}')"

class SmartDocument(DatabaseMixin, FileMixin):
    """智能文档类 - 使用super()处理冲突"""
    
    def __init__(self, title):
        self.title = title
        self.save_to_db = True
        self.save_to_file = True
    
    def save(self):
        print(f"SmartDocument.save: 保存文档 '{self.title}'")
        
        if self.save_to_db:
            DatabaseMixin.save(self)
        
        if self.save_to_file:
            FileMixin.save(self)
    
    def configure_save(self, to_db=True, to_file=True):
        self.save_to_db = to_db
        self.save_to_file = to_file
    
    def __str__(self):
        return f"SmartDocument('{self.title}')"

# 测试方法冲突处理
print("测试方法冲突处理:")
doc1 = Document("报告.docx")
print(f"Document的MRO: {Document.__mro__}")
print("调用save方法:")
doc1.save()

print("\n智能文档:")
doc2 = SmartDocument("智能报告.docx")
doc2.configure_save(to_db=True, to_file=False)
print("只保存到数据库:")
doc2.save()

print("\n=== 6. 多继承的最佳实践 ===")

# 6. 多继承最佳实践示例
class LoggerMixin:
    """日志混入类 - 遵循最佳实践"""
    
    def __init__(self, **kwargs):
        # 提取自己需要的参数
        self._log_enabled = kwargs.pop('log_enabled', True)
        super().__init__(**kwargs)
    
    def log(self, message, level='INFO'):
        if self._log_enabled:
            import datetime
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] {level}: {message}")
    
    def enable_logging(self):
        self._log_enabled = True
    
    def disable_logging(self):
        self._log_enabled = False

class CacheableMixin:
    """缓存混入类 - 遵循最佳实践"""
    
    def __init__(self, **kwargs):
        # 提取自己需要的参数
        self._cache_enabled = kwargs.pop('cache_enabled', True)
        self._cache = {}
        super().__init__(**kwargs)
    
    def get_from_cache(self, key):
        if self._cache_enabled and key in self._cache:
            return self._cache[key]
        return None
    
    def set_cache(self, key, value):
        if self._cache_enabled:
            self._cache[key] = value
    
    def clear_cache(self):
        self._cache.clear()
    
    def cache_info(self):
        return {
            'enabled': self._cache_enabled,
            'size': len(self._cache),
            'keys': list(self._cache.keys())
        }

class APIClient(LoggerMixin, CacheableMixin):
    """API客户端 - 多继承最佳实践示例"""
    
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        super().__init__(**kwargs)
        self.log(f"API客户端初始化: {base_url}")
    
    def get(self, endpoint):
        # 检查缓存
        cache_key = f"GET:{endpoint}"
        cached_result = self.get_from_cache(cache_key)
        
        if cached_result:
            self.log(f"从缓存获取: {endpoint}")
            return cached_result
        
        # 模拟API调用
        self.log(f"API调用: GET {self.base_url}{endpoint}")
        result = f"数据来自 {endpoint}"
        
        # 缓存结果
        self.set_cache(cache_key, result)
        
        return result
    
    def post(self, endpoint, data):
        self.log(f"API调用: POST {self.base_url}{endpoint}")
        # 清除相关缓存
        self.clear_cache()
        return f"POST到 {endpoint} 成功"
    
    def status(self):
        return {
            'base_url': self.base_url,
            'cache_info': self.cache_info()
        }

# 测试最佳实践
print("多继承最佳实践示例:")
api = APIClient("https://api.example.com", log_enabled=True, cache_enabled=True)

print("\n第一次API调用:")
result1 = api.get("/users")
print(f"结果: {result1}")

print("\n第二次相同API调用（应该从缓存获取）:")
result2 = api.get("/users")
print(f"结果: {result2}")

print("\nPOST调用（会清除缓存）:")
post_result = api.post("/users", {"name": "新用户"})
print(f"结果: {post_result}")

print("\n第三次GET调用（缓存已清除）:")
result3 = api.get("/users")
print(f"结果: {result3}")

print("\nAPI客户端状态:")
status = api.status()
for key, value in status.items():
    print(f"  {key}: {value}")

print(f"\nAPIClient的MRO: {APIClient.__mro__}")

print("\n=== 多继承总结 ===")
print("""
多继承使用指南：

优点：
1. 代码复用 - 可以组合多个类的功能
2. 灵活性 - 可以创建功能丰富的类
3. 模块化 - 通过混入类实现功能模块化

缺点：
1. 复杂性 - 增加了代码的复杂度
2. 菱形问题 - 可能导致方法调用的歧义
3. 调试困难 - MRO可能不直观

最佳实践：
1. 优先使用组合而不是多继承
2. 使用混入类（Mixin）模式
3. 保持继承层次简单
4. 使用super()确保正确的方法调用
5. 明确文档化继承关系
6. 使用**kwargs传递参数
7. 避免菱形继承
8. 测试所有继承路径

何时使用多继承：
1. 需要组合多个独立的功能
2. 使用混入类添加通用功能
3. 实现接口的多重实现
4. 框架和库的设计中
""")

if __name__ == "__main__":
    print("\n多继承演示完成!")
    print("多继承是强大的工具，但需要谨慎使用。优先考虑组合，在合适的场景下使用多继承。")