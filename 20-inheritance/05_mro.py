#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
方法解析顺序（MRO - Method Resolution Order）

MRO是Python中确定在多继承情况下方法调用顺序的算法。
Python使用C3线性化算法来计算MRO，确保方法调用的一致性和可预测性。

学习要点：
1. MRO的基本概念
2. C3线性化算法
3. 查看和理解MRO
4. MRO在单继承中的表现
5. MRO在多继承中的表现
6. MRO的实际应用
7. MRO相关的问题和解决方案
"""

# 1. MRO的基本概念
print("=== 1. MRO的基本概念 ===")

class A:
    """基类A"""
    
    def method(self):
        print("A.method")
    
    def show_mro(self):
        print(f"A的MRO: {A.__mro__}")

class B(A):
    """继承自A的类B"""
    
    def method(self):
        print("B.method")
        super().method()

class C(A):
    """继承自A的类C"""
    
    def method(self):
        print("C.method")
        super().method()

class D(B, C):
    """多继承类D"""
    
    def method(self):
        print("D.method")
        super().method()

# 查看各类的MRO
print("各类的MRO:")
for cls in [A, B, C, D]:
    print(f"{cls.__name__}: {cls.__mro__}")

print("\n调用D的方法:")
d = D()
d.method()

print("\n=== 2. MRO的查看方法 ===")

# 2. 查看MRO的不同方法
print("查看MRO的方法:")
print(f"1. 使用__mro__属性: {D.__mro__}")
print(f"2. 使用mro()方法: {D.mro()}")
print("3. 使用help()函数查看继承关系:")
# help(D)  # 这会输出很多信息，在演示中注释掉

# 自定义函数显示MRO
def show_mro(cls):
    """显示类的MRO信息"""
    print(f"\n{cls.__name__}的方法解析顺序:")
    for i, base in enumerate(cls.__mro__):
        print(f"  {i+1}. {base.__name__} ({base.__module__}.{base.__qualname__})")

show_mro(D)

print("\n=== 3. 单继承中的MRO ===")

# 3. 单继承链中的MRO
class Animal:
    """动物基类"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name}: 动物发声")
    
    def move(self):
        print(f"{self.name}: 动物移动")

class Mammal(Animal):
    """哺乳动物"""
    
    def speak(self):
        print(f"{self.name}: 哺乳动物发声")
        super().speak()
    
    def breathe(self):
        print(f"{self.name}: 用肺呼吸")

class Dog(Mammal):
    """狗类"""
    
    def speak(self):
        print(f"{self.name}: 汪汪叫")
        super().speak()
    
    def move(self):
        print(f"{self.name}: 四腿奔跑")
        super().move()

class Poodle(Dog):
    """贵宾犬"""
    
    def speak(self):
        print(f"{self.name}: 优雅地叫")
        super().speak()

# 测试单继承MRO
print("单继承链的MRO:")
for cls in [Animal, Mammal, Dog, Poodle]:
    print(f"{cls.__name__}: {[c.__name__ for c in cls.__mro__]}")

print("\n创建贵宾犬并调用方法:")
poodle = Poodle("泰迪")
poodle.speak()
print()
poodle.move()

print("\n=== 4. 复杂多继承中的MRO ===")

# 4. 复杂多继承场景
class Base:
    """基础类"""
    
    def method(self):
        print("Base.method")

class Left(Base):
    """左分支"""
    
    def method(self):
        print("Left.method")
        super().method()

class Right(Base):
    """右分支"""
    
    def method(self):
        print("Right.method")
        super().method()

class LeftChild(Left):
    """左分支的子类"""
    
    def method(self):
        print("LeftChild.method")
        super().method()

class RightChild(Right):
    """右分支的子类"""
    
    def method(self):
        print("RightChild.method")
        super().method()

class Diamond(LeftChild, RightChild):
    """菱形继承的底部类"""
    
    def method(self):
        print("Diamond.method")
        super().method()

# 分析复杂继承的MRO
print("复杂多继承的MRO分析:")
show_mro(Diamond)

print("\n方法调用顺序:")
diamond = Diamond()
diamond.method()

print("\n=== 5. MRO的C3线性化算法演示 ===")

# 5. 演示C3算法的工作原理
def calculate_mro_manually(cls):
    """手动演示MRO计算过程（简化版）"""
    print(f"\n计算 {cls.__name__} 的MRO:")
    
    # 获取直接父类
    bases = cls.__bases__
    print(f"直接父类: {[base.__name__ for base in bases]}")
    
    # 显示各父类的MRO
    for base in bases:
        print(f"{base.__name__}的MRO: {[c.__name__ for c in base.__mro__]}")
    
    # 显示实际计算结果
    print(f"最终MRO: {[c.__name__ for c in cls.__mro__]}")

# 演示几个类的MRO计算
for cls in [Diamond, D]:
    calculate_mro_manually(cls)

print("\n=== 6. MRO冲突和解决方案 ===")

# 6. MRO冲突示例
class X:
    pass

class Y:
    pass

class A1(X, Y):
    pass

class B1(Y, X):  # 注意：这里Y和X的顺序与A1相反
    pass

# 尝试创建会导致MRO冲突的类
print("MRO冲突示例:")
try:
    class Conflict(A1, B1):
        pass
    print("没有冲突")
except TypeError as e:
    print(f"MRO冲突: {e}")

# 解决MRO冲突的方法
print("\n解决MRO冲突:")

# 方法1: 调整继承顺序
class A2(X, Y):
    pass

class B2(X, Y):  # 保持相同的顺序
    pass

class NoConflict1(A2, B2):
    pass

print(f"解决方案1 - NoConflict1的MRO: {[c.__name__ for c in NoConflict1.__mro__]}")

# 方法2: 使用中间类
class Intermediate(X, Y):  # 保持与A3相同的顺序
    pass

class A3(X, Y):
    pass

class B3(Intermediate):
    pass

class NoConflict2(A3, B3):
    pass

print(f"解决方案2 - NoConflict2的MRO: {[c.__name__ for c in NoConflict2.__mro__]}")

print("\n=== 7. MRO在实际开发中的应用 ===")

# 7. 实际应用场景
class Loggable:
    """日志功能混入"""
    
    def log(self, message):
        print(f"[LOG] {self.__class__.__name__}: {message}")

class Cacheable:
    """缓存功能混入"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cache = {}
    
    def get_cache(self, key):
        return self._cache.get(key)
    
    def set_cache(self, key, value):
        self._cache[key] = value
        self.log(f"缓存设置: {key} = {value}")

class Validatable:
    """验证功能混入"""
    
    def validate(self):
        self.log("执行验证")
        return True

class DataProcessor(Loggable, Cacheable, Validatable):
    """数据处理器 - 组合多个功能"""
    
    def __init__(self, name):
        self.name = name
        super().__init__()
        self.log(f"数据处理器 '{name}' 初始化完成")
    
    def process(self, data):
        # 检查缓存
        cached = self.get_cache(data)
        if cached:
            self.log(f"从缓存获取结果: {cached}")
            return cached
        
        # 验证数据
        if not self.validate():
            self.log("数据验证失败")
            return None
        
        # 处理数据
        result = f"处理结果: {data.upper()}"
        self.set_cache(data, result)
        
        return result

# 测试实际应用
print("实际应用示例:")
show_mro(DataProcessor)

processor = DataProcessor("文本处理器")
print("\n处理数据:")
result1 = processor.process("hello")
print(f"结果1: {result1}")

result2 = processor.process("hello")  # 应该从缓存获取
print(f"结果2: {result2}")

print("\n=== 8. MRO调试技巧 ===")

# 8. MRO调试和分析工具
def analyze_mro(cls):
    """分析类的MRO并提供详细信息"""
    print(f"\n=== {cls.__name__} MRO分析 ===")
    
    mro = cls.__mro__
    print(f"MRO长度: {len(mro)}")
    print(f"继承深度: {len(mro) - 1}")
    
    print("\nMRO详细信息:")
    for i, base in enumerate(mro):
        indent = "  " * i
        methods = [name for name in dir(base) 
                  if not name.startswith('_') and callable(getattr(base, name))]
        print(f"{indent}{i+1}. {base.__name__}")
        if methods:
            print(f"{indent}   方法: {', '.join(methods[:5])}{'...' if len(methods) > 5 else ''}")
    
    # 检查方法重写
    print("\n方法重写分析:")
    all_methods = set()
    for base in mro:
        all_methods.update(name for name in dir(base) 
                          if not name.startswith('_') and callable(getattr(base, name)))
    
    for method_name in sorted(all_methods):
        defining_classes = []
        for base in mro:
            if method_name in base.__dict__:
                defining_classes.append(base.__name__)
        
        if len(defining_classes) > 1:
            print(f"  {method_name}: {' -> '.join(defining_classes)}")

def trace_method_calls(cls, method_name):
    """追踪方法调用路径"""
    print(f"\n追踪 {cls.__name__}.{method_name} 的调用路径:")
    
    for i, base in enumerate(cls.__mro__):
        if hasattr(base, method_name) and method_name in base.__dict__:
            print(f"  {i+1}. {base.__name__}.{method_name}")

# 使用调试工具
analyze_mro(DataProcessor)
trace_method_calls(DataProcessor, '__init__')
trace_method_calls(Diamond, 'method')

print("\n=== MRO最佳实践 ===")
print("""
MRO最佳实践和注意事项：

1. 理解MRO的重要性
   - MRO决定了方法调用的顺序
   - 影响super()的行为
   - 关系到多继承的正确性

2. 设计继承层次时的考虑
   - 保持继承层次简单
   - 避免复杂的菱形继承
   - 使用组合替代复杂继承

3. 使用工具分析MRO
   - 使用__mro__属性查看顺序
   - 使用mro()方法获取列表
   - 编写调试函数分析复杂情况

4. 多继承设计原则
   - 混入类应该是无状态的
   - 使用抽象基类定义接口
   - 保持一致的参数传递模式

5. 调试MRO问题
   - 理解C3线性化算法
   - 分析继承冲突的原因
   - 重新设计继承结构

6. 文档化继承关系
   - 记录设计决策
   - 说明MRO的预期行为
   - 提供使用示例
""")

# 实用的MRO检查函数
def check_mro_consistency(*classes):
    """检查多个类的MRO一致性"""
    print("\nMRO一致性检查:")
    
    for cls in classes:
        print(f"{cls.__name__}: {[c.__name__ for c in cls.__mro__]}")
    
    # 检查是否有冲突的继承顺序
    common_bases = set(classes[0].__mro__)
    for cls in classes[1:]:
        common_bases &= set(cls.__mro__)
    
    if len(common_bases) > 1:  # 除了object
        print(f"共同基类: {[c.__name__ for c in common_bases if c != object]}")
        
        # 检查顺序一致性
        for base1 in common_bases:
            for base2 in common_bases:
                if base1 != base2:
                    orders = []
                    for cls in classes:
                        mro = cls.__mro__
                        if base1 in mro and base2 in mro:
                            idx1 = mro.index(base1)
                            idx2 = mro.index(base2)
                            orders.append(idx1 < idx2)
                    
                    if len(set(orders)) > 1:
                        print(f"警告: {base1.__name__} 和 {base2.__name__} 的顺序不一致")

# 测试MRO一致性
check_mro_consistency(Diamond, DataProcessor, NoConflict1)

if __name__ == "__main__":
    print("\nMRO（方法解析顺序）演示完成!")
    print("理解MRO对于掌握Python的多继承机制至关重要。")
    print("在设计复杂的继承层次时，始终要考虑MRO的影响。")