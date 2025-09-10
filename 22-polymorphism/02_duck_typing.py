#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
鸭子类型（Duck Typing）

鸭子类型是Python中多态的一种重要实现方式。
名字来源于"如果它走起路来像鸭子，叫起来也像鸭子，那么它就是鸭子"。

核心思想：
1. 不关心对象的类型，只关心对象的行为
2. 如果对象有所需的方法或属性，就可以使用
3. 运行时动态检查，而不是编译时静态检查
4. 体现了Python的动态特性
"""

# 1. 鸭子类型基本示例
class Duck:
    """鸭子类"""
    def swim(self):
        return "鸭子在游泳"
    
    def fly(self):
        return "鸭子在飞翔"
    
    def quack(self):
        return "鸭子嘎嘎叫"

class Swan:
    """天鹅类 - 不继承Duck，但有相同的方法"""
    def swim(self):
        return "天鹅优雅地游泳"
    
    def fly(self):
        return "天鹅高雅地飞翔"
    
    def quack(self):
        return "天鹅轻柔地叫"

class Airplane:
    """飞机类 - 只有部分相同方法"""
    def fly(self):
        return "飞机在天空中飞行"
    
    def start_engine(self):
        return "飞机启动引擎"

class Fish:
    """鱼类 - 只有游泳方法"""
    def swim(self):
        return "鱼在水中游泳"
    
    def breathe_underwater(self):
        return "鱼在水下呼吸"

# 2. 鸭子类型的使用
def make_it_swim(obj):
    """让对象游泳 - 鸭子类型应用"""
    try:
        return obj.swim()
    except AttributeError:
        return f"{type(obj).__name__} 不会游泳"

def make_it_fly(obj):
    """让对象飞翔 - 鸭子类型应用"""
    try:
        return obj.fly()
    except AttributeError:
        return f"{type(obj).__name__} 不会飞"

def make_it_quack(obj):
    """让对象叫 - 鸭子类型应用"""
    try:
        return obj.quack()
    except AttributeError:
        return f"{type(obj).__name__} 不会叫"

def demonstrate_duck_typing():
    """演示鸭子类型的基本概念"""
    print("=== 鸭子类型基本演示 ===")
    
    # 创建不同类型的对象
    objects = [
        Duck(),
        Swan(),
        Airplane(),
        Fish()
    ]
    
    for obj in objects:
        print(f"\n{type(obj).__name__}:")
        print(f"  游泳: {make_it_swim(obj)}")
        print(f"  飞翔: {make_it_fly(obj)}")
        print(f"  叫声: {make_it_quack(obj)}")

# 3. 更优雅的鸭子类型实现
def duck_behavior(obj):
    """展示鸭子行为 - 使用hasattr检查"""
    behaviors = []
    
    if hasattr(obj, 'swim') and callable(getattr(obj, 'swim')):
        behaviors.append(obj.swim())
    
    if hasattr(obj, 'fly') and callable(getattr(obj, 'fly')):
        behaviors.append(obj.fly())
    
    if hasattr(obj, 'quack') and callable(getattr(obj, 'quack')):
        behaviors.append(obj.quack())
    
    return behaviors

# 4. 文件类对象的鸭子类型示例
class StringFile:
    """字符串文件类 - 模拟文件对象"""
    def __init__(self, content):
        self.content = content
        self.position = 0
    
    def read(self, size=-1):
        if size == -1:
            result = self.content[self.position:]
            self.position = len(self.content)
        else:
            result = self.content[self.position:self.position + size]
            self.position += len(result)
        return result
    
    def readline(self):
        start = self.position
        try:
            end = self.content.index('\n', start) + 1
        except ValueError:
            end = len(self.content)
        
        result = self.content[start:end]
        self.position = end
        return result
    
    def close(self):
        pass  # 字符串文件不需要关闭

class ListFile:
    """列表文件类 - 模拟文件对象"""
    def __init__(self, lines):
        self.lines = lines
        self.position = 0
    
    def read(self, size=-1):
        if self.position >= len(self.lines):
            return ''
        
        if size == -1:
            result = '\n'.join(self.lines[self.position:])
            self.position = len(self.lines)
        else:
            # 简化实现，按行读取
            result = '\n'.join(self.lines[self.position:self.position + size])
            self.position += size
        
        return result
    
    def readline(self):
        if self.position >= len(self.lines):
            return ''
        
        result = self.lines[self.position] + '\n'
        self.position += 1
        return result
    
    def close(self):
        pass  # 列表文件不需要关闭

def process_file_like_object(file_obj):
    """处理文件类对象 - 鸭子类型应用"""
    print(f"处理 {type(file_obj).__name__}:")
    
    # 读取第一行
    first_line = file_obj.readline()
    print(f"  第一行: {first_line.strip()}")
    
    # 读取剩余内容
    remaining = file_obj.read()
    print(f"  剩余内容: {remaining[:50]}{'...' if len(remaining) > 50 else ''}")
    
    # 关闭文件
    file_obj.close()
    print("  文件已关闭")

# 5. 迭代器的鸭子类型
class NumberRange:
    """数字范围类 - 实现迭代器协议"""
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        
        result = self.current
        self.current += self.step
        return result

class FibonacciSequence:
    """斐波那契序列类 - 实现迭代器协议"""
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        
        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b
        else:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return self.b

def iterate_sequence(sequence):
    """迭代序列 - 鸭子类型应用"""
    print(f"迭代 {type(sequence).__name__}:")
    for i, value in enumerate(sequence):
        if i >= 10:  # 限制输出数量
            print("  ...")
            break
        print(f"  {value}")

# 6. 上下文管理器的鸭子类型
class TimerContext:
    """计时器上下文管理器"""
    def __init__(self, name):
        self.name = name
        self.start_time = None
    
    def __enter__(self):
        import time
        self.start_time = time.time()
        print(f"开始计时: {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        end_time = time.time()
        duration = end_time - self.start_time
        print(f"结束计时: {self.name}, 耗时: {duration:.4f}秒")
        return False

class LogContext:
    """日志上下文管理器"""
    def __init__(self, operation):
        self.operation = operation
    
    def __enter__(self):
        print(f"[LOG] 开始操作: {self.operation}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"[LOG] 操作失败: {self.operation}, 错误: {exc_val}")
        else:
            print(f"[LOG] 操作成功: {self.operation}")
        return False

def use_context_manager(context_manager):
    """使用上下文管理器 - 鸭子类型应用"""
    with context_manager:
        import time
        time.sleep(0.1)  # 模拟一些操作
        print("  执行一些操作...")

# 7. 鸭子类型的实际应用
def demonstrate_file_like_objects():
    """演示文件类对象的鸭子类型"""
    print("\n=== 文件类对象鸭子类型演示 ===")
    
    # 不同的"文件"对象
    string_file = StringFile("第一行\n第二行\n第三行\n")
    list_file = ListFile(["列表第一行", "列表第二行", "列表第三行"])
    
    for file_obj in [string_file, list_file]:
        process_file_like_object(file_obj)
        print()

def demonstrate_iterators():
    """演示迭代器的鸭子类型"""
    print("=== 迭代器鸭子类型演示 ===")
    
    # 不同的迭代器对象
    number_range = NumberRange(1, 11, 2)
    fibonacci = FibonacciSequence(10)
    
    iterate_sequence(number_range)
    print()
    iterate_sequence(fibonacci)

def demonstrate_context_managers():
    """演示上下文管理器的鸭子类型"""
    print("\n=== 上下文管理器鸭子类型演示 ===")
    
    # 不同的上下文管理器
    timer = TimerContext("测试操作")
    logger = LogContext("数据处理")
    
    print("使用计时器:")
    use_context_manager(timer)
    
    print("\n使用日志记录器:")
    use_context_manager(logger)

# 8. 鸭子类型的优缺点
def demonstrate_duck_typing_pros_cons():
    """演示鸭子类型的优缺点"""
    print("\n=== 鸭子类型的优缺点 ===")
    
    # 优点：灵活性
    class MockLogger:
        def log(self, message):
            print(f"[MOCK] {message}")
    
    class FileLogger:
        def log(self, message):
            print(f"[FILE] {message}")
    
    def use_logger(logger):
        logger.log("这是一条日志消息")
    
    print("优点 - 灵活性:")
    use_logger(MockLogger())
    use_logger(FileLogger())
    
    # 缺点：运行时错误
    class BadObject:
        pass
    
    print("\n缺点 - 运行时错误:")
    try:
        use_logger(BadObject())
    except AttributeError as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    # 演示鸭子类型基本概念
    demonstrate_duck_typing()
    
    # 演示更优雅的实现
    print("\n=== 优雅的鸭子类型实现 ===")
    objects = [Duck(), Swan(), Airplane(), Fish()]
    for obj in objects:
        behaviors = duck_behavior(obj)
        print(f"{type(obj).__name__}: {behaviors}")
    
    # 演示文件类对象
    demonstrate_file_like_objects()
    
    # 演示迭代器
    demonstrate_iterators()
    
    # 演示上下文管理器
    demonstrate_context_managers()
    
    # 演示优缺点
    demonstrate_duck_typing_pros_cons()
    
    print("\n=== 鸭子类型的核心要点 ===")
    print("1. 关注行为而非类型")
    print("2. 运行时动态检查")
    print("3. 提供极大的灵活性")
    print("4. 体现Python的动态特性")
    print("5. 需要注意运行时错误")
    print("6. 适合快速原型开发")