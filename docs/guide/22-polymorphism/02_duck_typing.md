# 鸭子类型（Duck Typing）

## 什么是鸭子类型

鸭子类型（Duck Typing）是Python中一个重要的概念，它的名字来源于一句话："如果它走起路来像鸭子，叫起来也像鸭子，那么它就是鸭子。"

在编程中，鸭子类型意味着：如果一个对象具有某些方法和属性，那么它就可以被当作具有这些特征的类型来使用，而不需要显式地继承某个类或实现某个接口。

## 基本的鸭子类型示例

### 文件类对象示例

```python
class StringFile:
    """模拟文件的字符串类"""
    def __init__(self, content=""):
        self.content = content
        self.position = 0
    
    def read(self, size=-1):
        """读取内容"""
        if size == -1:
            result = self.content[self.position:]
            self.position = len(self.content)
        else:
            result = self.content[self.position:self.position + size]
            self.position += len(result)
        return result
    
    def write(self, text):
        """写入内容"""
        self.content += text
        return len(text)
    
    def close(self):
        """关闭文件（这里只是打印信息）"""
        print("StringFile closed")

class ListFile:
    """模拟文件的列表类"""
    def __init__(self):
        self.lines = []
        self.position = 0
    
    def read(self, size=-1):
        """读取内容"""
        if self.position < len(self.lines):
            result = self.lines[self.position]
            self.position += 1
            return result
        return ""
    
    def write(self, text):
        """写入内容"""
        self.lines.append(text)
        return len(text)
    
    def close(self):
        """关闭文件"""
        print("ListFile closed")

# 处理文件类对象的函数
def process_file_like_object(file_obj, data):
    """处理类文件对象 - 展示鸭子类型"""
    print(f"处理 {file_obj.__class__.__name__}:")
    
    # 写入数据
    for item in data:
        file_obj.write(item)
        print(f"  写入: {item}")
    
    # 读取数据
    print("  读取内容:")
    while True:
        content = file_obj.read()
        if not content:
            break
        print(f"    {content}")
    
    # 关闭文件
    file_obj.close()
    print()

# 演示鸭子类型
print("=== 鸭子类型演示：文件类对象 ===")

# 创建不同的"文件"对象
string_file = StringFile()
list_file = ListFile()

# 测试数据
data = ["Hello", "World", "Python"]

# 同一个函数处理不同类型的对象
process_file_like_object(string_file, data)
process_file_like_object(list_file, data)
```

### 可迭代对象示例

```python
class NumberRange:
    """数字范围类"""
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        """返回迭代器"""
        current = self.start
        while current < self.end:
            yield current
            current += self.step

class FibonacciSequence:
    """斐波那契数列类"""
    def __init__(self, max_count):
        self.max_count = max_count
    
    def __iter__(self):
        """返回迭代器"""
        count = 0
        a, b = 0, 1
        while count < self.max_count:
            yield a
            a, b = b, a + b
            count += 1

class CustomList:
    """自定义列表类"""
    def __init__(self, items):
        self.items = items
    
    def __iter__(self):
        """返回迭代器"""
        return iter(self.items)
    
    def __len__(self):
        """返回长度"""
        return len(self.items)

# 处理可迭代对象的函数
def process_iterable(iterable):
    """处理可迭代对象 - 展示鸭子类型"""
    print(f"处理 {iterable.__class__.__name__}:")
    
    # 计算总和
    total = sum(iterable)
    print(f"  总和: {total}")
    
    # 如果有长度方法，显示长度
    if hasattr(iterable, '__len__'):
        print(f"  长度: {len(iterable)}")
    
    # 显示所有元素
    print(f"  元素: {list(iterable)}")
    print()

# 演示可迭代对象的鸭子类型
print("=== 鸭子类型演示：可迭代对象 ===")

# 创建不同的可迭代对象
number_range = NumberRange(1, 10, 2)
fib_sequence = FibonacciSequence(8)
custom_list = CustomList([1, 2, 3, 4, 5])
regular_list = [10, 20, 30, 40]

# 同一个函数处理不同类型的可迭代对象
iterables = [number_range, fib_sequence, custom_list, regular_list]
for iterable in iterables:
    process_iterable(iterable)
```

## 协议和约定

### 上下文管理器协议

```python
class DatabaseConnection:
    """模拟数据库连接"""
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        """进入上下文时调用"""
        print(f"连接到数据库: {self.db_name}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文时调用"""
        print(f"断开数据库连接: {self.db_name}")
        self.connected = False
        if exc_type:
            print(f"处理异常: {exc_type.__name__}: {exc_val}")
        return False  # 不抑制异常
    
    def execute(self, query):
        """执行查询"""
        if not self.connected:
            raise RuntimeError("数据库未连接")
        print(f"执行查询: {query}")
        return f"查询结果: {query}"

class FileManager:
    """文件管理器"""
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """进入上下文时调用"""
        print(f"打开文件: {self.filename} (模式: {self.mode})")
        # 这里只是模拟，不实际打开文件
        self.file = f"模拟文件对象: {self.filename}"
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文时调用"""
        print(f"关闭文件: {self.filename}")
        self.file = None
        return False
    
    def read(self):
        """读取文件"""
        if not self.file:
            raise RuntimeError("文件未打开")
        return f"文件内容: {self.filename}"

# 使用上下文管理器协议
def demonstrate_context_managers():
    """演示上下文管理器协议"""
    print("=== 上下文管理器协议演示 ===")
    
    # 使用数据库连接
    print("1. 数据库连接:")
    with DatabaseConnection("user_db") as db:
        result = db.execute("SELECT * FROM users")
        print(f"  {result}")
    
    print("\n2. 文件管理:")
    with FileManager("data.txt", "r") as file_mgr:
        content = file_mgr.read()
        print(f"  {content}")
    
    print("=== 演示完成 ===\n")

demonstrate_context_managers()
```

### 可调用对象协议

```python
class Multiplier:
    """乘法器类"""
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        """使对象可调用"""
        return value * self.factor

class Formatter:
    """格式化器类"""
    def __init__(self, template):
        self.template = template
    
    def __call__(self, **kwargs):
        """使对象可调用"""
        return self.template.format(**kwargs)

class Counter:
    """计数器类"""
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        """使对象可调用"""
        self.count += 1
        return self.count

# 处理可调用对象的函数
def process_callable(callable_obj, *args, **kwargs):
    """处理可调用对象 - 展示鸭子类型"""
    print(f"调用 {callable_obj.__class__.__name__}:")
    try:
        result = callable_obj(*args, **kwargs)
        print(f"  参数: {args}, {kwargs}")
        print(f"  结果: {result}")
    except Exception as e:
        print(f"  错误: {e}")
    print()

# 演示可调用对象
def demonstrate_callable_objects():
    """演示可调用对象"""
    print("=== 可调用对象演示 ===")
    
    # 创建不同的可调用对象
    multiplier = Multiplier(3)
    formatter = Formatter("Hello, {name}! You are {age} years old.")
    counter = Counter()
    
    # 普通函数也是可调用对象
    def square(x):
        return x ** 2
    
    # 测试所有可调用对象
    callables = [
        (multiplier, (5,), {}),
        (formatter, (), {'name': 'Alice', 'age': 25}),
        (counter, (), {}),
        (square, (4,), {})
    ]
    
    for callable_obj, args, kwargs in callables:
        process_callable(callable_obj, *args, **kwargs)

demonstrate_callable_objects()
```

## 鸭子类型的优势

### 1. 灵活性

```python
class Logger:
    """日志记录器"""
    def log(self, message):
        print(f"[LOG] {message}")

class FileLogger:
    """文件日志记录器"""
    def __init__(self, filename):
        self.filename = filename
    
    def log(self, message):
        print(f"[FILE LOG to {self.filename}] {message}")

class DatabaseLogger:
    """数据库日志记录器"""
    def __init__(self, table):
        self.table = table
    
    def log(self, message):
        print(f"[DB LOG to {self.table}] {message}")

# 应用程序类
class Application:
    """应用程序"""
    def __init__(self, logger):
        # 接受任何有log方法的对象
        self.logger = logger
    
    def run(self):
        """运行应用程序"""
        self.logger.log("应用程序启动")
        self.logger.log("执行业务逻辑")
        self.logger.log("应用程序结束")

# 演示灵活性
def demonstrate_flexibility():
    """演示鸭子类型的灵活性"""
    print("=== 鸭子类型灵活性演示 ===")
    
    # 创建不同类型的日志记录器
    loggers = [
        Logger(),
        FileLogger("app.log"),
        DatabaseLogger("logs")
    ]
    
    # 同一个应用程序可以使用不同的日志记录器
    for i, logger in enumerate(loggers, 1):
        print(f"\n{i}. 使用 {logger.__class__.__name__}:")
        app = Application(logger)
        app.run()
    
    print("=== 演示完成 ===\n")

demonstrate_flexibility()
```

### 2. 简化测试

```python
class EmailService:
    """邮件服务"""
    def send_email(self, to, subject, body):
        print(f"发送邮件到 {to}")
        print(f"主题: {subject}")
        print(f"内容: {body}")
        return True

class MockEmailService:
    """模拟邮件服务（用于测试）"""
    def __init__(self):
        self.sent_emails = []
    
    def send_email(self, to, subject, body):
        email = {
            'to': to,
            'subject': subject,
            'body': body
        }
        self.sent_emails.append(email)
        print(f"[MOCK] 模拟发送邮件到 {to}")
        return True
    
    def get_sent_count(self):
        return len(self.sent_emails)

class NotificationSystem:
    """通知系统"""
    def __init__(self, email_service):
        self.email_service = email_service
    
    def send_welcome_email(self, user_email, username):
        """发送欢迎邮件"""
        subject = "欢迎加入我们！"
        body = f"亲爱的 {username}，欢迎加入我们的平台！"
        return self.email_service.send_email(user_email, subject, body)
    
    def send_notification(self, user_email, message):
        """发送通知"""
        subject = "系统通知"
        return self.email_service.send_email(user_email, subject, message)

# 演示测试简化
def demonstrate_testing():
    """演示鸭子类型简化测试"""
    print("=== 鸭子类型测试演示 ===")
    
    print("1. 生产环境使用真实邮件服务:")
    real_service = EmailService()
    notification_system = NotificationSystem(real_service)
    notification_system.send_welcome_email("user@example.com", "张三")
    
    print("\n2. 测试环境使用模拟邮件服务:")
    mock_service = MockEmailService()
    test_notification_system = NotificationSystem(mock_service)
    test_notification_system.send_welcome_email("test@example.com", "测试用户")
    test_notification_system.send_notification("test@example.com", "这是一条测试消息")
    
    print(f"\n测试结果: 共发送了 {mock_service.get_sent_count()} 封邮件")
    print("=== 演示完成 ===\n")

demonstrate_testing()
```

## 鸭子类型的注意事项

```python
def demonstrate_duck_typing_caveats():
    """演示鸭子类型的注意事项"""
    print("=== 鸭子类型注意事项 ===")
    
    print("1. 方法名相同但语义不同:")
    
    class BankAccount:
        def __init__(self, balance):
            self.balance = balance
        
        def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
                return f"取款 {amount}，余额 {self.balance}"
            return "余额不足"
    
    class Library:
        def __init__(self):
            self.books = ["Python编程", "算法导论", "设计模式"]
        
        def withdraw(self, book):
            if book in self.books:
                self.books.remove(book)
                return f"借出图书: {book}"
            return "图书不存在"
    
    # 虽然都有withdraw方法，但语义完全不同
    account = BankAccount(1000)
    library = Library()
    
    print(f"  银行账户: {account.withdraw(500)}")
    print(f"  图书馆: {library.withdraw('Python编程')}")
    
    print("\n2. 缺少必要的方法:")
    
    class IncompleteFile:
        def write(self, text):
            print(f"写入: {text}")
        # 缺少read和close方法
    
    def process_file(file_obj):
        file_obj.write("测试数据")
        try:
            content = file_obj.read()  # 可能会出错
            print(f"读取: {content}")
        except AttributeError as e:
            print(f"  错误: {e}")
        
        try:
            file_obj.close()  # 可能会出错
        except AttributeError as e:
            print(f"  错误: {e}")
    
    incomplete_file = IncompleteFile()
    process_file(incomplete_file)
    
    print("\n3. 使用hasattr检查方法存在:")
    
    def safe_process_file(file_obj):
        """安全地处理文件对象"""
        if hasattr(file_obj, 'write'):
            file_obj.write("安全写入")
        
        if hasattr(file_obj, 'read'):
            content = file_obj.read()
            print(f"读取: {content}")
        else:
            print("对象不支持读取操作")
        
        if hasattr(file_obj, 'close'):
            file_obj.close()
        else:
            print("对象不支持关闭操作")
    
    print("\n  安全处理:")
    safe_process_file(incomplete_file)
    
    print("=== 注意事项演示完成 ===\n")

demonstrate_duck_typing_caveats()
```

## 鸭子类型的最佳实践

```python
def demonstrate_best_practices():
    """演示鸭子类型的最佳实践"""
    print("=== 鸭子类型最佳实践 ===")
    
    print("1. 使用文档字符串说明期望的接口:")
    
    def process_drawable(drawable):
        """
        处理可绘制对象
        
        参数:
            drawable: 可绘制对象，需要有以下方法:
                - draw(): 绘制对象
                - get_area(): 获取面积
                - move(x, y): 移动对象
        """
        print(f"绘制 {drawable.__class__.__name__}:")
        drawable.draw()
        print(f"面积: {drawable.get_area()}")
        drawable.move(10, 20)
        print()
    
    print("2. 使用try-except处理方法调用:")
    
    def robust_process(obj):
        """健壮的对象处理"""
        print(f"处理 {obj.__class__.__name__}:")
        
        try:
            obj.process()
            print("  处理成功")
        except AttributeError:
            print("  对象不支持process方法")
        except Exception as e:
            print(f"  处理出错: {e}")
        print()
    
    # 测试对象
    class GoodObject:
        def process(self):
            print("  执行处理逻辑")
    
    class BadObject:
        def process(self):
            raise ValueError("处理失败")
    
    class NoMethodObject:
        pass
    
    objects = [GoodObject(), BadObject(), NoMethodObject()]
    for obj in objects:
        robust_process(obj)
    
    print("3. 使用getattr提供默认行为:")
    
    def flexible_process(obj, default_message="默认处理"):
        """灵活的对象处理"""
        # 获取方法，如果不存在则使用默认函数
        process_method = getattr(obj, 'process', lambda: print(f"  {default_message}"))
        
        print(f"处理 {obj.__class__.__name__}:")
        process_method()
        print()
    
    for obj in objects:
        flexible_process(obj)
    
    print("=== 最佳实践演示完成 ===\n")

demonstrate_best_practices()
```

## 总结

鸭子类型是Python的一个强大特性，它体现了Python"简单胜过复杂"的哲学。通过鸭子类型，我们可以：

1. **提高代码灵活性**：不需要严格的继承关系
2. **简化接口设计**：关注行为而不是类型
3. **便于测试**：容易创建模拟对象
4. **支持多态**：实现真正的多态行为

但同时也要注意：

1. **文档化接口期望**：清楚说明需要什么方法
2. **错误处理**：优雅地处理方法不存在的情况
3. **语义一致性**：确保相同方法名有相似的语义

掌握鸭子类型，能让你写出更加Pythonic和灵活的代码。