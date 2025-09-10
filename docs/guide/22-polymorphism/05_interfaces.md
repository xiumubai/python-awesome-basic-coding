# 接口的概念和实现

## 什么是接口

接口是一种定义类应该实现哪些方法的契约。在Python中，虽然没有像Java或C#那样的interface关键字，但我们可以通过抽象基类、协议（Protocol）和约定来实现接口的概念。接口定义了"做什么"，而不关心"怎么做"。

## 使用抽象基类实现接口

### 基本接口定义

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Drawable(ABC):
    """可绘制接口"""
    
    @abstractmethod
    def draw(self) -> str:
        """绘制图形"""
        pass
    
    @abstractmethod
    def get_area(self) -> float:
        """获取面积"""
        pass
    
    @abstractmethod
    def get_perimeter(self) -> float:
        """获取周长"""
        pass

class Movable(ABC):
    """可移动接口"""
    
    @abstractmethod
    def move(self, dx: float, dy: float) -> None:
        """移动对象"""
        pass
    
    @abstractmethod
    def get_position(self) -> tuple:
        """获取当前位置"""
        pass

class Resizable(ABC):
    """可调整大小接口"""
    
    @abstractmethod
    def resize(self, scale_factor: float) -> None:
        """调整大小"""
        pass
    
    @abstractmethod
    def get_size(self) -> Dict[str, float]:
        """获取尺寸信息"""
        pass

# 实现多个接口的类
class Rectangle(Drawable, Movable, Resizable):
    """矩形类 - 实现多个接口"""
    
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    # 实现Drawable接口
    def draw(self) -> str:
        return f"绘制矩形: 宽度={self.width}, 高度={self.height}, 位置=({self.x}, {self.y})"
    
    def get_area(self) -> float:
        return self.width * self.height
    
    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    # 实现Movable接口
    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy
    
    def get_position(self) -> tuple:
        return (self.x, self.y)
    
    # 实现Resizable接口
    def resize(self, scale_factor: float) -> None:
        self.width *= scale_factor
        self.height *= scale_factor
    
    def get_size(self) -> Dict[str, float]:
        return {"width": self.width, "height": self.height}

class Circle(Drawable, Movable, Resizable):
    """圆形类 - 实现多个接口"""
    
    def __init__(self, radius: float, x: float = 0, y: float = 0):
        self.radius = radius
        self.x = x
        self.y = y
    
    # 实现Drawable接口
    def draw(self) -> str:
        return f"绘制圆形: 半径={self.radius}, 位置=({self.x}, {self.y})"
    
    def get_area(self) -> float:
        import math
        return math.pi * self.radius ** 2
    
    def get_perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius
    
    # 实现Movable接口
    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy
    
    def get_position(self) -> tuple:
        return (self.x, self.y)
    
    # 实现Resizable接口
    def resize(self, scale_factor: float) -> None:
        self.radius *= scale_factor
    
    def get_size(self) -> Dict[str, float]:
        return {"radius": self.radius}

class Triangle(Drawable, Movable):
    """三角形类 - 只实现部分接口"""
    
    def __init__(self, base: float, height: float, x: float = 0, y: float = 0):
        self.base = base
        self.height = height
        self.x = x
        self.y = y
    
    # 实现Drawable接口
    def draw(self) -> str:
        return f"绘制三角形: 底边={self.base}, 高度={self.height}, 位置=({self.x}, {self.y})"
    
    def get_area(self) -> float:
        return 0.5 * self.base * self.height
    
    def get_perimeter(self) -> float:
        # 假设是等腰三角形
        import math
        side = math.sqrt((self.base/2)**2 + self.height**2)
        return self.base + 2 * side
    
    # 实现Movable接口
    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy
    
    def get_position(self) -> tuple:
        return (self.x, self.y)

# 演示接口的使用
def demonstrate_interfaces():
    """演示接口的使用"""
    print("=== 接口演示 ===")
    
    # 创建不同的图形对象
    shapes = [
        Rectangle(10, 5, 0, 0),
        Circle(3, 5, 5),
        Triangle(6, 4, 10, 10)
    ]
    
    print("1. 测试Drawable接口:")
    for shape in shapes:
        if isinstance(shape, Drawable):
            print(f"   {shape.draw()}")
            print(f"   面积: {shape.get_area():.2f}")
            print(f"   周长: {shape.get_perimeter():.2f}")
            print()
    
    print("2. 测试Movable接口:")
    for shape in shapes:
        if isinstance(shape, Movable):
            print(f"   {shape.__class__.__name__} 原位置: {shape.get_position()}")
            shape.move(2, 3)
            print(f"   移动后位置: {shape.get_position()}")
            print()
    
    print("3. 测试Resizable接口:")
    for shape in shapes:
        if isinstance(shape, Resizable):
            print(f"   {shape.__class__.__name__} 原尺寸: {shape.get_size()}")
            shape.resize(1.5)
            print(f"   缩放后尺寸: {shape.get_size()}")
            print(f"   缩放后面积: {shape.get_area():.2f}")
            print()
        else:
            print(f"   {shape.__class__.__name__} 不支持调整大小")
            print()
    
    print("=== 演示完成 ===\n")

demonstrate_interfaces()
```

## 使用Protocol实现接口（Python 3.8+）

### 结构化子类型（Structural Subtyping）

```python
from typing import Protocol, runtime_checkable
from abc import abstractmethod

@runtime_checkable
class Serializable(Protocol):
    """可序列化协议"""
    
    def serialize(self) -> str:
        """序列化为字符串"""
        ...
    
    def deserialize(self, data: str) -> 'Serializable':
        """从字符串反序列化"""
        ...

@runtime_checkable
class Comparable(Protocol):
    """可比较协议"""
    
    def __lt__(self, other) -> bool:
        """小于比较"""
        ...
    
    def __eq__(self, other) -> bool:
        """等于比较"""
        ...

@runtime_checkable
class Cacheable(Protocol):
    """可缓存协议"""
    
    def get_cache_key(self) -> str:
        """获取缓存键"""
        ...
    
    def is_cache_valid(self) -> bool:
        """检查缓存是否有效"""
        ...

class User:
    """用户类 - 实现多个协议"""
    
    def __init__(self, user_id: int, name: str, email: str, age: int):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.age = age
        self.created_at = "2024-01-01"
    
    # 实现Serializable协议
    def serialize(self) -> str:
        import json
        return json.dumps({
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "created_at": self.created_at
        })
    
    def deserialize(self, data: str) -> 'User':
        import json
        user_data = json.loads(data)
        user = User(
            user_data["user_id"],
            user_data["name"],
            user_data["email"],
            user_data["age"]
        )
        user.created_at = user_data["created_at"]
        return user
    
    # 实现Comparable协议
    def __lt__(self, other) -> bool:
        if isinstance(other, User):
            return self.age < other.age
        return NotImplemented
    
    def __eq__(self, other) -> bool:
        if isinstance(other, User):
            return self.user_id == other.user_id
        return False
    
    def __le__(self, other) -> bool:
        return self < other or self == other
    
    def __gt__(self, other) -> bool:
        return not self <= other
    
    def __ge__(self, other) -> bool:
        return not self < other
    
    def __ne__(self, other) -> bool:
        return not self == other
    
    # 实现Cacheable协议
    def get_cache_key(self) -> str:
        return f"user:{self.user_id}"
    
    def is_cache_valid(self) -> bool:
        # 简单的缓存有效性检查
        return True
    
    def __str__(self) -> str:
        return f"User(id={self.user_id}, name='{self.name}', age={self.age})"

class Product:
    """产品类 - 实现部分协议"""
    
    def __init__(self, product_id: int, name: str, price: float, category: str):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
    
    # 实现Serializable协议
    def serialize(self) -> str:
        import json
        return json.dumps({
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "category": self.category
        })
    
    def deserialize(self, data: str) -> 'Product':
        import json
        product_data = json.loads(data)
        return Product(
            product_data["product_id"],
            product_data["name"],
            product_data["price"],
            product_data["category"]
        )
    
    # 实现Comparable协议
    def __lt__(self, other) -> bool:
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Product):
            return self.product_id == other.product_id
        return False
    
    def __str__(self) -> str:
        return f"Product(id={self.product_id}, name='{self.name}', price=${self.price})"

class Order:
    """订单类 - 只实现Cacheable协议"""
    
    def __init__(self, order_id: int, user_id: int, total_amount: float):
        self.order_id = order_id
        self.user_id = user_id
        self.total_amount = total_amount
        self.status = "pending"
    
    # 实现Cacheable协议
    def get_cache_key(self) -> str:
        return f"order:{self.order_id}"
    
    def is_cache_valid(self) -> bool:
        # 只有已完成的订单才缓存
        return self.status == "completed"
    
    def __str__(self) -> str:
        return f"Order(id={self.order_id}, user_id={self.user_id}, amount=${self.total_amount})"

# 使用协议的函数
def serialize_objects(objects: List[Serializable]) -> List[str]:
    """序列化对象列表"""
    return [obj.serialize() for obj in objects]

def sort_objects(objects: List[Comparable]) -> List[Comparable]:
    """排序对象列表"""
    return sorted(objects)

def cache_objects(objects: List[Cacheable]) -> Dict[str, Cacheable]:
    """缓存对象"""
    cache = {}
    for obj in objects:
        if obj.is_cache_valid():
            cache[obj.get_cache_key()] = obj
    return cache

# 演示Protocol的使用
def demonstrate_protocols():
    """演示Protocol的使用"""
    print("=== Protocol演示 ===")
    
    # 创建测试对象
    users = [
        User(1, "Alice", "alice@example.com", 25),
        User(2, "Bob", "bob@example.com", 30),
        User(3, "Charlie", "charlie@example.com", 22)
    ]
    
    products = [
        Product(101, "Laptop", 999.99, "Electronics"),
        Product(102, "Mouse", 29.99, "Electronics"),
        Product(103, "Book", 19.99, "Education")
    ]
    
    orders = [
        Order(1001, 1, 1029.98),
        Order(1002, 2, 19.99),
        Order(1003, 3, 999.99)
    ]
    
    # 设置一些订单为已完成状态
    orders[0].status = "completed"
    orders[2].status = "completed"
    
    print("1. 测试Serializable协议:")
    # 用户和产品都实现了Serializable
    serializable_objects = users + products
    serialized = serialize_objects(serializable_objects)
    for i, data in enumerate(serialized[:3]):  # 只显示前3个
        print(f"   对象{i+1}: {data}")
    
    print("\n2. 测试Comparable协议:")
    # 用户和产品都实现了Comparable
    comparable_objects = users + products
    
    print("   用户按年龄排序:")
    sorted_users = sort_objects(users)
    for user in sorted_users:
        print(f"     {user}")
    
    print("   产品按价格排序:")
    sorted_products = sort_objects(products)
    for product in sorted_products:
        print(f"     {product}")
    
    print("\n3. 测试Cacheable协议:")
    # 用户和订单都实现了Cacheable
    cacheable_objects = users + orders
    cache = cache_objects(cacheable_objects)
    print(f"   缓存的对象数量: {len(cache)}")
    for key, obj in cache.items():
        print(f"     {key}: {obj}")
    
    print("\n4. 运行时类型检查:")
    test_objects = [users[0], products[0], orders[0]]
    
    for obj in test_objects:
        obj_name = obj.__class__.__name__
        print(f"   {obj_name}:")
        print(f"     是否Serializable: {isinstance(obj, Serializable)}")
        print(f"     是否Comparable: {isinstance(obj, Comparable)}")
        print(f"     是否Cacheable: {isinstance(obj, Cacheable)}")
        print()
    
    print("=== 演示完成 ===\n")

demonstrate_protocols()
```

## 接口组合和多重继承

### 复杂接口设计

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from enum import Enum

class EventType(Enum):
    """事件类型枚举"""
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    READ = "read"

class Auditable(ABC):
    """可审计接口"""
    
    @abstractmethod
    def log_event(self, event_type: EventType, details: str) -> None:
        """记录事件"""
        pass
    
    @abstractmethod
    def get_audit_log(self) -> List[Dict[str, Any]]:
        """获取审计日志"""
        pass

class Validatable(ABC):
    """可验证接口"""
    
    @abstractmethod
    def validate(self) -> bool:
        """验证对象"""
        pass
    
    @abstractmethod
    def get_validation_errors(self) -> List[str]:
        """获取验证错误"""
        pass

class Persistable(ABC):
    """可持久化接口"""
    
    @abstractmethod
    def save(self) -> bool:
        """保存对象"""
        pass
    
    @abstractmethod
    def load(self, identifier: Any) -> bool:
        """加载对象"""
        pass
    
    @abstractmethod
    def delete(self) -> bool:
        """删除对象"""
        pass

class Searchable(ABC):
    """可搜索接口"""
    
    @abstractmethod
    def search(self, query: str) -> List[Any]:
        """搜索"""
        pass
    
    @abstractmethod
    def get_search_fields(self) -> List[str]:
        """获取可搜索字段"""
        pass

class Notifiable(ABC):
    """可通知接口"""
    
    @abstractmethod
    def send_notification(self, message: str, recipients: List[str]) -> bool:
        """发送通知"""
        pass
    
    @abstractmethod
    def get_notification_preferences(self) -> Dict[str, bool]:
        """获取通知偏好"""
        pass

# 实现多个接口的复杂类
class BlogPost(Auditable, Validatable, Persistable, Searchable, Notifiable):
    """博客文章类 - 实现多个接口"""
    
    def __init__(self, post_id: int, title: str, content: str, author_id: int):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.created_at = "2024-01-01"
        self.updated_at = "2024-01-01"
        self.status = "draft"
        self.tags = []
        self.audit_log = []
        self.validation_errors = []
        self.subscribers = []
    
    # 实现Auditable接口
    def log_event(self, event_type: EventType, details: str) -> None:
        import datetime
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "event_type": event_type.value,
            "details": details,
            "user_id": self.author_id
        }
        self.audit_log.append(log_entry)
    
    def get_audit_log(self) -> List[Dict[str, Any]]:
        return self.audit_log.copy()
    
    # 实现Validatable接口
    def validate(self) -> bool:
        self.validation_errors.clear()
        
        if not self.title or len(self.title.strip()) == 0:
            self.validation_errors.append("标题不能为空")
        
        if len(self.title) > 200:
            self.validation_errors.append("标题长度不能超过200字符")
        
        if not self.content or len(self.content.strip()) == 0:
            self.validation_errors.append("内容不能为空")
        
        if len(self.content) < 10:
            self.validation_errors.append("内容长度至少10字符")
        
        if self.author_id <= 0:
            self.validation_errors.append("作者ID无效")
        
        return len(self.validation_errors) == 0
    
    def get_validation_errors(self) -> List[str]:
        return self.validation_errors.copy()
    
    # 实现Persistable接口
    def save(self) -> bool:
        if not self.validate():
            self.log_event(EventType.UPDATE, f"保存失败: 验证错误")
            return False
        
        # 模拟保存到数据库
        import datetime
        self.updated_at = datetime.datetime.now().isoformat()
        
        if self.post_id == 0:  # 新文章
            self.post_id = hash(self.title) % 10000  # 模拟生成ID
            self.log_event(EventType.CREATE, f"创建文章: {self.title}")
        else:
            self.log_event(EventType.UPDATE, f"更新文章: {self.title}")
        
        return True
    
    def load(self, identifier: Any) -> bool:
        # 模拟从数据库加载
        if isinstance(identifier, int) and identifier > 0:
            self.post_id = identifier
            self.log_event(EventType.READ, f"加载文章: ID={identifier}")
            return True
        return False
    
    def delete(self) -> bool:
        if self.post_id > 0:
            self.log_event(EventType.DELETE, f"删除文章: {self.title}")
            # 模拟删除
            return True
        return False
    
    # 实现Searchable接口
    def search(self, query: str) -> List[Any]:
        # 简单的搜索实现
        query_lower = query.lower()
        matches = []
        
        if query_lower in self.title.lower():
            matches.append({"field": "title", "match": self.title})
        
        if query_lower in self.content.lower():
            matches.append({"field": "content", "match": "内容匹配"})
        
        for tag in self.tags:
            if query_lower in tag.lower():
                matches.append({"field": "tags", "match": tag})
        
        if matches:
            self.log_event(EventType.READ, f"搜索查询: {query}")
        
        return matches
    
    def get_search_fields(self) -> List[str]:
        return ["title", "content", "tags"]
    
    # 实现Notifiable接口
    def send_notification(self, message: str, recipients: List[str]) -> bool:
        # 模拟发送通知
        notification = {
            "message": message,
            "recipients": recipients,
            "post_id": self.post_id,
            "post_title": self.title
        }
        
        # 记录通知发送
        self.log_event(EventType.UPDATE, f"发送通知: {message} 给 {len(recipients)} 个用户")
        
        return True
    
    def get_notification_preferences(self) -> Dict[str, bool]:
        return {
            "email_notifications": True,
            "push_notifications": True,
            "sms_notifications": False
        }
    
    # 博客特有的方法
    def publish(self) -> bool:
        """发布文章"""
        if self.validate() and self.save():
            self.status = "published"
            
            # 通知订阅者
            if self.subscribers:
                self.send_notification(
                    f"新文章发布: {self.title}",
                    self.subscribers
                )
            
            self.log_event(EventType.UPDATE, f"发布文章: {self.title}")
            return True
        return False
    
    def add_tag(self, tag: str) -> None:
        """添加标签"""
        if tag not in self.tags:
            self.tags.append(tag)
            self.log_event(EventType.UPDATE, f"添加标签: {tag}")
    
    def subscribe_user(self, user_email: str) -> None:
        """添加订阅者"""
        if user_email not in self.subscribers:
            self.subscribers.append(user_email)
            self.log_event(EventType.UPDATE, f"新增订阅者: {user_email}")
    
    def __str__(self) -> str:
        return f"BlogPost(id={self.post_id}, title='{self.title}', status='{self.status}')"

class Comment(Auditable, Validatable, Persistable):
    """评论类 - 实现部分接口"""
    
    def __init__(self, comment_id: int, post_id: int, author_id: int, content: str):
        self.comment_id = comment_id
        self.post_id = post_id
        self.author_id = author_id
        self.content = content
        self.created_at = "2024-01-01"
        self.status = "pending"
        self.audit_log = []
        self.validation_errors = []
    
    # 实现Auditable接口
    def log_event(self, event_type: EventType, details: str) -> None:
        import datetime
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "event_type": event_type.value,
            "details": details,
            "user_id": self.author_id
        }
        self.audit_log.append(log_entry)
    
    def get_audit_log(self) -> List[Dict[str, Any]]:
        return self.audit_log.copy()
    
    # 实现Validatable接口
    def validate(self) -> bool:
        self.validation_errors.clear()
        
        if not self.content or len(self.content.strip()) == 0:
            self.validation_errors.append("评论内容不能为空")
        
        if len(self.content) > 1000:
            self.validation_errors.append("评论长度不能超过1000字符")
        
        if self.author_id <= 0:
            self.validation_errors.append("作者ID无效")
        
        if self.post_id <= 0:
            self.validation_errors.append("文章ID无效")
        
        return len(self.validation_errors) == 0
    
    def get_validation_errors(self) -> List[str]:
        return self.validation_errors.copy()
    
    # 实现Persistable接口
    def save(self) -> bool:
        if not self.validate():
            self.log_event(EventType.UPDATE, "保存失败: 验证错误")
            return False
        
        if self.comment_id == 0:
            self.comment_id = hash(self.content) % 10000
            self.log_event(EventType.CREATE, f"创建评论: post_id={self.post_id}")
        else:
            self.log_event(EventType.UPDATE, f"更新评论: id={self.comment_id}")
        
        return True
    
    def load(self, identifier: Any) -> bool:
        if isinstance(identifier, int) and identifier > 0:
            self.comment_id = identifier
            self.log_event(EventType.READ, f"加载评论: ID={identifier}")
            return True
        return False
    
    def delete(self) -> bool:
        if self.comment_id > 0:
            self.log_event(EventType.DELETE, f"删除评论: id={self.comment_id}")
            return True
        return False
    
    def approve(self) -> bool:
        """审核通过评论"""
        if self.validate():
            self.status = "approved"
            self.log_event(EventType.UPDATE, f"审核通过评论: id={self.comment_id}")
            return True
        return False
    
    def __str__(self) -> str:
        return f"Comment(id={self.comment_id}, post_id={self.post_id}, status='{self.status}')"

# 演示接口组合
def demonstrate_interface_composition():
    """演示接口组合"""
    print("=== 接口组合演示 ===")
    
    # 创建博客文章
    post = BlogPost(0, "Python接口设计", "这是一篇关于Python接口设计的文章...", 1)
    post.add_tag("Python")
    post.add_tag("编程")
    post.subscribe_user("user1@example.com")
    post.subscribe_user("user2@example.com")
    
    # 创建评论
    comment = Comment(0, 1, 2, "很好的文章，学到了很多！")
    
    print("1. 测试博客文章的所有接口:")
    
    # 测试Validatable
    print(f"   文章验证结果: {post.validate()}")
    if not post.validate():
        print(f"   验证错误: {post.get_validation_errors()}")
    
    # 测试Persistable
    print(f"   保存文章: {post.save()}")
    
    # 测试Searchable
    search_results = post.search("Python")
    print(f"   搜索'Python'结果: {search_results}")
    
    # 测试Notifiable
    notification_sent = post.send_notification("文章已更新", ["admin@example.com"])
    print(f"   发送通知: {notification_sent}")
    
    # 发布文章
    print(f"   发布文章: {post.publish()}")
    
    print("\n2. 测试评论的接口:")
    
    # 测试评论验证和保存
    print(f"   评论验证结果: {comment.validate()}")
    print(f"   保存评论: {comment.save()}")
    print(f"   审核评论: {comment.approve()}")
    
    print("\n3. 查看审计日志:")
    
    print("   文章审计日志:")
    for log_entry in post.get_audit_log()[-3:]:  # 显示最后3条
        print(f"     {log_entry['timestamp']}: {log_entry['event_type']} - {log_entry['details']}")
    
    print("   评论审计日志:")
    for log_entry in comment.get_audit_log():
        print(f"     {log_entry['timestamp']}: {log_entry['event_type']} - {log_entry['details']}")
    
    print("\n4. 接口检查:")
    objects = [post, comment]
    interfaces = [
        (Auditable, "Auditable"),
        (Validatable, "Validatable"),
        (Persistable, "Persistable"),
        (Searchable, "Searchable"),
        (Notifiable, "Notifiable")
    ]
    
    for obj in objects:
        print(f"   {obj.__class__.__name__}:")
        for interface, name in interfaces:
            implements = isinstance(obj, interface)
            print(f"     实现{name}: {implements}")
        print()
    
    print("=== 演示完成 ===\n")

demonstrate_interface_composition()
```

## 接口的设计原则

### SOLID原则在接口设计中的应用

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any

# 1. 单一职责原则 (Single Responsibility Principle)
class Readable(ABC):
    """只负责读取操作的接口"""
    
    @abstractmethod
    def read(self, identifier: str) -> Any:
        pass

class Writable(ABC):
    """只负责写入操作的接口"""
    
    @abstractmethod
    def write(self, data: Any) -> bool:
        pass

class Deletable(ABC):
    """只负责删除操作的接口"""
    
    @abstractmethod
    def delete(self, identifier: str) -> bool:
        pass

# 2. 接口隔离原则 (Interface Segregation Principle)
# 不要强迫客户端依赖它们不使用的接口

class BasicFileOperations(Readable, Writable):
    """基本文件操作 - 组合小接口"""
    pass

class AdvancedFileOperations(BasicFileOperations, Deletable):
    """高级文件操作 - 继承并扩展"""
    pass

class ReadOnlyFile(Readable):
    """只读文件 - 只实现需要的接口"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.content = f"Content of {filename}"
    
    def read(self, identifier: str) -> Any:
        return self.content

class RegularFile(AdvancedFileOperations):
    """普通文件 - 实现所有操作"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.content = f"Content of {filename}"
        self.exists = True
    
    def read(self, identifier: str) -> Any:
        if self.exists:
            return self.content
        return None
    
    def write(self, data: Any) -> bool:
        if self.exists:
            self.content = str(data)
            return True
        return False
    
    def delete(self, identifier: str) -> bool:
        if self.exists:
            self.exists = False
            self.content = ""
            return True
        return False

# 3. 依赖倒置原则 (Dependency Inversion Principle)
# 高层模块不应该依赖低层模块，两者都应该依赖抽象

class Logger(ABC):
    """日志记录器接口"""
    
    @abstractmethod
    def log(self, level: str, message: str) -> None:
        pass

class FileLogger(Logger):
    """文件日志记录器"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.logs = []
    
    def log(self, level: str, message: str) -> None:
        import datetime
        timestamp = datetime.datetime.now().isoformat()
        log_entry = f"[{timestamp}] {level}: {message}"
        self.logs.append(log_entry)
        print(f"写入文件 {self.filename}: {log_entry}")

class ConsoleLogger(Logger):
    """控制台日志记录器"""
    
    def log(self, level: str, message: str) -> None:
        import datetime
        timestamp = datetime.datetime.now().isoformat()
        print(f"[{timestamp}] {level}: {message}")

class DatabaseLogger(Logger):
    """数据库日志记录器"""
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.logs = []
    
    def log(self, level: str, message: str) -> None:
        import datetime
        timestamp = datetime.datetime.now().isoformat()
        log_entry = {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }
        self.logs.append(log_entry)
        print(f"写入数据库: {log_entry}")

class FileManager:
    """文件管理器 - 依赖抽象而不是具体实现"""
    
    def __init__(self, logger: Logger):
        self.logger = logger  # 依赖抽象接口
        self.files = {}
    
    def create_file(self, filename: str, file_type: str = "regular") -> Any:
        """创建文件"""
        try:
            if file_type == "readonly":
                file_obj = ReadOnlyFile(filename)
            else:
                file_obj = RegularFile(filename)
            
            self.files[filename] = file_obj
            self.logger.log("INFO", f"创建文件: {filename}")
            return file_obj
        except Exception as e:
            self.logger.log("ERROR", f"创建文件失败: {filename}, 错误: {str(e)}")
            return None
    
    def process_file(self, filename: str, operation: str, data: Any = None) -> Any:
        """处理文件操作"""
        if filename not in self.files:
            self.logger.log("WARNING", f"文件不存在: {filename}")
            return None
        
        file_obj = self.files[filename]
        
        try:
            if operation == "read":
                result = file_obj.read(filename)
                self.logger.log("INFO", f"读取文件: {filename}")
                return result
            
            elif operation == "write" and isinstance(file_obj, Writable):
                success = file_obj.write(data)
                if success:
                    self.logger.log("INFO", f"写入文件: {filename}")
                else:
                    self.logger.log("ERROR", f"写入文件失败: {filename}")
                return success
            
            elif operation == "delete" and isinstance(file_obj, Deletable):
                success = file_obj.delete(filename)
                if success:
                    self.logger.log("INFO", f"删除文件: {filename}")
                    del self.files[filename]
                else:
                    self.logger.log("ERROR", f"删除文件失败: {filename}")
                return success
            
            else:
                self.logger.log("ERROR", f"不支持的操作: {operation} 对文件 {filename}")
                return False
        
        except Exception as e:
            self.logger.log("ERROR", f"操作失败: {operation} 对文件 {filename}, 错误: {str(e)}")
            return None
    
    def get_file_info(self, filename: str) -> Dict[str, Any]:
        """获取文件信息"""
        if filename not in self.files:
            return {}
        
        file_obj = self.files[filename]
        info = {
            "filename": filename,
            "type": file_obj.__class__.__name__,
            "readable": isinstance(file_obj, Readable),
            "writable": isinstance(file_obj, Writable),
            "deletable": isinstance(file_obj, Deletable)
        }
        
        self.logger.log("INFO", f"获取文件信息: {filename}")
        return info

# 演示SOLID原则
def demonstrate_solid_principles():
    """演示SOLID原则在接口设计中的应用"""
    print("=== SOLID原则演示 ===")
    
    # 测试不同的日志记录器
    loggers = [
        ("文件日志", FileLogger("app.log")),
        ("控制台日志", ConsoleLogger()),
        ("数据库日志", DatabaseLogger("sqlite:///logs.db"))
    ]
    
    for logger_name, logger in loggers:
        print(f"\n--- 使用{logger_name}记录器 ---")
        
        # 创建文件管理器（依赖抽象）
        file_manager = FileManager(logger)
        
        # 创建不同类型的文件
        regular_file = file_manager.create_file("document.txt", "regular")
        readonly_file = file_manager.create_file("config.txt", "readonly")
        
        # 测试文件操作
        files_to_test = ["document.txt", "config.txt"]
        
        for filename in files_to_test:
            print(f"\n  测试文件: {filename}")
            
            # 获取文件信息
            info = file_manager.get_file_info(filename)
            print(f"    文件信息: {info}")
            
            # 测试读取
            content = file_manager.process_file(filename, "read")
            print(f"    读取结果: {content}")
            
            # 测试写入（只对可写文件）
            if info.get("writable"):
                write_result = file_manager.process_file(filename, "write", "新的内容")
                print(f"    写入结果: {write_result}")
            else:
                print(f"    跳过写入测试（文件不可写）")
            
            # 测试删除（只对可删除文件）
            if info.get("deletable"):
                delete_result = file_manager.process_file(filename, "delete")
                print(f"    删除结果: {delete_result}")
            else:
                print(f"    跳过删除测试（文件不可删除）")
        
        # 显示日志记录（如果是文件或数据库日志）
        if hasattr(logger, 'logs') and logger.logs:
            print(f"\n  {logger_name}记录的日志条目数: {len(logger.logs)}")
    
    print("\n=== 演示完成 ===\n")

demonstrate_solid_principles()
```

## 接口的最佳实践

```python
def demonstrate_interface_best_practices():
    """演示接口设计的最佳实践"""
    print("=== 接口设计最佳实践 ===")
    
    print("1. 接口设计原则:")
    print("   - 保持接口简单和专注")
    print("   - 使用清晰和一致的命名")
    print("   - 提供完整的文档说明")
    print("   - 考虑向后兼容性")
    
    print("\n2. 接口组合策略:")
    print("   - 优先组合小接口而不是大接口")
    print("   - 使用多重继承组合功能")
    print("   - 避免接口污染")
    
    print("\n3. 实现建议:")
    print("   - 使用抽象基类定义严格接口")
    print("   - 使用Protocol定义结构化接口")
    print("   - 提供默认实现减少重复代码")
    
    print("\n4. 测试策略:")
    print("   - 为每个接口编写单元测试")
    print("   - 测试接口的所有实现")
    print("   - 使用模拟对象测试依赖")
    
    print("\n5. 维护考虑:")
    print("   - 版本化接口变更")
    print("   - 提供迁移指南")
    print("   - 监控接口使用情况")
    
    print("\n=== 最佳实践总结完成 ===\n")

demonstrate_interface_best_practices()
```

## 总结

接口是面向对象设计中的核心概念，它提供了一种定义类行为契约的方式。在Python中，我们可以通过多种方式实现接口：

1. **抽象基类（ABC）**：提供严格的接口定义和部分实现
2. **协议（Protocol）**：支持结构化子类型和鸭子类型
3. **多重继承**：组合多个接口实现复杂功能
4. **SOLID原则**：指导接口设计的最佳实践

通过合理使用接口，我们可以：
- 定义清晰的API契约
- 提高代码的可测试性
- 支持多态和依赖注入
- 实现松耦合的系统架构
- 提高代码的可维护性和扩展性

掌握接口设计的原则和技巧，能让你构建更加灵活和健壮的Python应用程序。