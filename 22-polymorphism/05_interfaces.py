#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
接口的概念和实现

接口定义了类应该实现的方法，但不提供具体实现。
在Python中，接口通常通过抽象基类（ABC）来实现。
接口是实现多态的重要机制，确保不同类具有相同的方法签名。

核心概念：
1. 接口定义契约和规范
2. 实现类必须遵循接口
3. 支持多重继承
4. 提供代码的可扩展性
"""

from abc import ABC, abstractmethod
from typing import List, Any, Optional
import json
import csv
import io

# 1. 基本接口示例
class Drawable(ABC):
    """可绘制接口"""
    
    @abstractmethod
    def draw(self):
        """绘制方法"""
        pass
    
    @abstractmethod
    def get_area(self):
        """获取面积"""
        pass

class Movable(ABC):
    """可移动接口"""
    
    @abstractmethod
    def move(self, x, y):
        """移动到指定位置"""
        pass
    
    @abstractmethod
    def get_position(self):
        """获取当前位置"""
        pass

class Resizable(ABC):
    """可调整大小接口"""
    
    @abstractmethod
    def resize(self, scale_factor):
        """调整大小"""
        pass
    
    @abstractmethod
    def get_size(self):
        """获取当前大小"""
        pass

# 实现多个接口的类
class Circle(Drawable, Movable, Resizable):
    """圆形类 - 实现多个接口"""
    
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self):
        """实现Drawable接口"""
        return f"在位置({self.x}, {self.y})绘制半径为{self.radius}的圆形"
    
    def get_area(self):
        """实现Drawable接口"""
        import math
        return math.pi * self.radius ** 2
    
    def move(self, x, y):
        """实现Movable接口"""
        old_pos = (self.x, self.y)
        self.x = x
        self.y = y
        return f"圆形从{old_pos}移动到({self.x}, {self.y})"
    
    def get_position(self):
        """实现Movable接口"""
        return (self.x, self.y)
    
    def resize(self, scale_factor):
        """实现Resizable接口"""
        old_radius = self.radius
        self.radius *= scale_factor
        return f"圆形半径从{old_radius}调整为{self.radius}"
    
    def get_size(self):
        """实现Resizable接口"""
        return {"radius": self.radius, "diameter": 2 * self.radius}

class Rectangle(Drawable, Movable, Resizable):
    """矩形类 - 实现多个接口"""
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self):
        """实现Drawable接口"""
        return f"在位置({self.x}, {self.y})绘制{self.width}x{self.height}的矩形"
    
    def get_area(self):
        """实现Drawable接口"""
        return self.width * self.height
    
    def move(self, x, y):
        """实现Movable接口"""
        old_pos = (self.x, self.y)
        self.x = x
        self.y = y
        return f"矩形从{old_pos}移动到({self.x}, {self.y})"
    
    def get_position(self):
        """实现Movable接口"""
        return (self.x, self.y)
    
    def resize(self, scale_factor):
        """实现Resizable接口"""
        old_size = (self.width, self.height)
        self.width *= scale_factor
        self.height *= scale_factor
        return f"矩形从{old_size}调整为({self.width}, {self.height})"
    
    def get_size(self):
        """实现Resizable接口"""
        return {"width": self.width, "height": self.height}

# 2. 数据存储接口示例
class DataStorage(ABC):
    """数据存储接口"""
    
    @abstractmethod
    def save(self, data: Any, identifier: str) -> bool:
        """保存数据"""
        pass
    
    @abstractmethod
    def load(self, identifier: str) -> Any:
        """加载数据"""
        pass
    
    @abstractmethod
    def delete(self, identifier: str) -> bool:
        """删除数据"""
        pass
    
    @abstractmethod
    def exists(self, identifier: str) -> bool:
        """检查数据是否存在"""
        pass
    
    @abstractmethod
    def list_all(self) -> List[str]:
        """列出所有数据标识符"""
        pass

class MemoryStorage(DataStorage):
    """内存存储实现"""
    
    def __init__(self):
        self._data = {}
    
    def save(self, data: Any, identifier: str) -> bool:
        """保存到内存"""
        try:
            self._data[identifier] = data
            return True
        except Exception:
            return False
    
    def load(self, identifier: str) -> Any:
        """从内存加载"""
        if identifier in self._data:
            return self._data[identifier]
        raise KeyError(f"数据 '{identifier}' 不存在")
    
    def delete(self, identifier: str) -> bool:
        """从内存删除"""
        if identifier in self._data:
            del self._data[identifier]
            return True
        return False
    
    def exists(self, identifier: str) -> bool:
        """检查是否存在"""
        return identifier in self._data
    
    def list_all(self) -> List[str]:
        """列出所有标识符"""
        return list(self._data.keys())
    
    def get_memory_usage(self):
        """内存存储特有方法"""
        import sys
        return sum(sys.getsizeof(v) for v in self._data.values())

class FileStorage(DataStorage):
    """文件存储实现"""
    
    def __init__(self, base_path="./data"):
        self.base_path = base_path
        self._ensure_directory()
    
    def _ensure_directory(self):
        """确保目录存在"""
        import os
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
    
    def _get_file_path(self, identifier: str) -> str:
        """获取文件路径"""
        import os
        return os.path.join(self.base_path, f"{identifier}.json")
    
    def save(self, data: Any, identifier: str) -> bool:
        """保存到文件"""
        try:
            file_path = self._get_file_path(identifier)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"保存失败: {e}")
            return False
    
    def load(self, identifier: str) -> Any:
        """从文件加载"""
        file_path = self._get_file_path(identifier)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise KeyError(f"文件 '{identifier}' 不存在")
        except Exception as e:
            raise ValueError(f"加载文件失败: {e}")
    
    def delete(self, identifier: str) -> bool:
        """删除文件"""
        import os
        file_path = self._get_file_path(identifier)
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
            return False
        except Exception:
            return False
    
    def exists(self, identifier: str) -> bool:
        """检查文件是否存在"""
        import os
        return os.path.exists(self._get_file_path(identifier))
    
    def list_all(self) -> List[str]:
        """列出所有文件"""
        import os
        if not os.path.exists(self.base_path):
            return []
        
        files = []
        for filename in os.listdir(self.base_path):
            if filename.endswith('.json'):
                files.append(filename[:-5])  # 移除.json扩展名
        return files
    
    def get_file_size(self, identifier: str) -> int:
        """文件存储特有方法"""
        import os
        file_path = self._get_file_path(identifier)
        if os.path.exists(file_path):
            return os.path.getsize(file_path)
        return 0

# 3. 序列化接口示例
class Serializable(ABC):
    """可序列化接口"""
    
    @abstractmethod
    def serialize(self) -> str:
        """序列化为字符串"""
        pass
    
    @abstractmethod
    def deserialize(self, data: str):
        """从字符串反序列化"""
        pass

class Exportable(ABC):
    """可导出接口"""
    
    @abstractmethod
    def export_to_dict(self) -> dict:
        """导出为字典"""
        pass
    
    @abstractmethod
    def import_from_dict(self, data: dict):
        """从字典导入"""
        pass

class Student(Serializable, Exportable):
    """学生类 - 实现序列化和导出接口"""
    
    def __init__(self, name="", age=0, student_id="", grades=None):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = grades or {}
    
    def serialize(self) -> str:
        """序列化为JSON字符串"""
        data = {
            "name": self.name,
            "age": self.age,
            "student_id": self.student_id,
            "grades": self.grades
        }
        return json.dumps(data, ensure_ascii=False)
    
    def deserialize(self, data: str):
        """从JSON字符串反序列化"""
        obj_data = json.loads(data)
        self.name = obj_data["name"]
        self.age = obj_data["age"]
        self.student_id = obj_data["student_id"]
        self.grades = obj_data["grades"]
    
    def export_to_dict(self) -> dict:
        """导出为字典"""
        return {
            "name": self.name,
            "age": self.age,
            "student_id": self.student_id,
            "grades": self.grades,
            "average_grade": self.get_average_grade()
        }
    
    def import_from_dict(self, data: dict):
        """从字典导入"""
        self.name = data.get("name", "")
        self.age = data.get("age", 0)
        self.student_id = data.get("student_id", "")
        self.grades = data.get("grades", {})
    
    def add_grade(self, subject: str, grade: float):
        """添加成绩"""
        self.grades[subject] = grade
    
    def get_average_grade(self) -> float:
        """计算平均成绩"""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
    
    def __str__(self):
        return f"学生: {self.name} (ID: {self.student_id}, 年龄: {self.age}, 平均分: {self.get_average_grade():.2f})"

# 4. 通知接口示例
class NotificationSender(ABC):
    """通知发送接口"""
    
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        """发送通知"""
        pass
    
    @abstractmethod
    def get_delivery_status(self, message_id: str) -> str:
        """获取投递状态"""
        pass

class EmailSender(NotificationSender):
    """邮件发送器"""
    
    def __init__(self):
        self.sent_messages = {}
        self.message_counter = 0
    
    def send(self, recipient: str, message: str) -> bool:
        """发送邮件（模拟）"""
        try:
            self.message_counter += 1
            message_id = f"email_{self.message_counter}"
            
            # 模拟邮件发送
            self.sent_messages[message_id] = {
                "recipient": recipient,
                "message": message,
                "status": "已发送",
                "type": "邮件"
            }
            
            print(f"邮件已发送到 {recipient}: {message[:30]}...")
            return True
        except Exception as e:
            print(f"邮件发送失败: {e}")
            return False
    
    def get_delivery_status(self, message_id: str) -> str:
        """获取邮件投递状态"""
        if message_id in self.sent_messages:
            return self.sent_messages[message_id]["status"]
        return "消息不存在"

class SMSSender(NotificationSender):
    """短信发送器"""
    
    def __init__(self):
        self.sent_messages = {}
        self.message_counter = 0
    
    def send(self, recipient: str, message: str) -> bool:
        """发送短信（模拟）"""
        try:
            self.message_counter += 1
            message_id = f"sms_{self.message_counter}"
            
            # 模拟短信发送
            self.sent_messages[message_id] = {
                "recipient": recipient,
                "message": message,
                "status": "已投递",
                "type": "短信"
            }
            
            print(f"短信已发送到 {recipient}: {message[:20]}...")
            return True
        except Exception as e:
            print(f"短信发送失败: {e}")
            return False
    
    def get_delivery_status(self, message_id: str) -> str:
        """获取短信投递状态"""
        if message_id in self.sent_messages:
            return self.sent_messages[message_id]["status"]
        return "消息不存在"

class PushNotificationSender(NotificationSender):
    """推送通知发送器"""
    
    def __init__(self):
        self.sent_messages = {}
        self.message_counter = 0
    
    def send(self, recipient: str, message: str) -> bool:
        """发送推送通知（模拟）"""
        try:
            self.message_counter += 1
            message_id = f"push_{self.message_counter}"
            
            # 模拟推送通知发送
            self.sent_messages[message_id] = {
                "recipient": recipient,
                "message": message,
                "status": "已推送",
                "type": "推送通知"
            }
            
            print(f"推送通知已发送到 {recipient}: {message[:25]}...")
            return True
        except Exception as e:
            print(f"推送通知发送失败: {e}")
            return False
    
    def get_delivery_status(self, message_id: str) -> str:
        """获取推送通知投递状态"""
        if message_id in self.sent_messages:
            return self.sent_messages[message_id]["status"]
        return "消息不存在"

# 5. 支付接口示例
class PaymentProcessor(ABC):
    """支付处理接口"""
    
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "CNY") -> dict:
        """处理支付"""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """退款"""
        pass
    
    @abstractmethod
    def get_transaction_status(self, transaction_id: str) -> str:
        """获取交易状态"""
        pass

class CreditCardProcessor(PaymentProcessor):
    """信用卡支付处理器"""
    
    def __init__(self):
        self.transactions = {}
        self.transaction_counter = 0
    
    def process_payment(self, amount: float, currency: str = "CNY") -> dict:
        """处理信用卡支付"""
        self.transaction_counter += 1
        transaction_id = f"cc_{self.transaction_counter}"
        
        # 模拟信用卡支付处理
        transaction = {
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency,
            "status": "成功",
            "method": "信用卡",
            "fee": amount * 0.03  # 3% 手续费
        }
        
        self.transactions[transaction_id] = transaction
        return transaction
    
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """信用卡退款"""
        if transaction_id in self.transactions:
            refund_id = f"refund_{transaction_id}"
            refund = {
                "refund_id": refund_id,
                "original_transaction": transaction_id,
                "amount": amount,
                "status": "退款成功",
                "method": "信用卡退款"
            }
            return refund
        return {"status": "失败", "reason": "交易不存在"}
    
    def get_transaction_status(self, transaction_id: str) -> str:
        """获取信用卡交易状态"""
        if transaction_id in self.transactions:
            return self.transactions[transaction_id]["status"]
        return "交易不存在"

class AlipayProcessor(PaymentProcessor):
    """支付宝支付处理器"""
    
    def __init__(self):
        self.transactions = {}
        self.transaction_counter = 0
    
    def process_payment(self, amount: float, currency: str = "CNY") -> dict:
        """处理支付宝支付"""
        self.transaction_counter += 1
        transaction_id = f"alipay_{self.transaction_counter}"
        
        # 模拟支付宝支付处理
        transaction = {
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency,
            "status": "成功",
            "method": "支付宝",
            "fee": amount * 0.006  # 0.6% 手续费
        }
        
        self.transactions[transaction_id] = transaction
        return transaction
    
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """支付宝退款"""
        if transaction_id in self.transactions:
            refund_id = f"refund_{transaction_id}"
            refund = {
                "refund_id": refund_id,
                "original_transaction": transaction_id,
                "amount": amount,
                "status": "退款成功",
                "method": "支付宝退款"
            }
            return refund
        return {"status": "失败", "reason": "交易不存在"}
    
    def get_transaction_status(self, transaction_id: str) -> str:
        """获取支付宝交易状态"""
        if transaction_id in self.transactions:
            return self.transactions[transaction_id]["status"]
        return "交易不存在"

# 6. 演示函数
def demonstrate_shape_interfaces():
    """演示形状接口"""
    print("=== 形状接口演示 ===")
    
    shapes = [
        Circle(10, 20, 5),
        Rectangle(0, 0, 8, 6)
    ]
    
    for shape in shapes:
        print(f"\n=== {shape.__class__.__name__} ===")
        
        # 使用Drawable接口
        print(f"绘制: {shape.draw()}")
        print(f"面积: {shape.get_area():.2f}")
        
        # 使用Movable接口
        print(f"当前位置: {shape.get_position()}")
        print(shape.move(50, 60))
        
        # 使用Resizable接口
        print(f"当前大小: {shape.get_size()}")
        print(shape.resize(1.5))
        print(f"调整后大小: {shape.get_size()}")

def demonstrate_storage_interfaces():
    """演示存储接口"""
    print("\n=== 存储接口演示 ===")
    
    storages = [
        MemoryStorage(),
        # FileStorage()  # 注释掉文件存储以避免创建文件
    ]
    
    test_data = {
        "user1": {"name": "张三", "age": 25},
        "user2": {"name": "李四", "age": 30},
        "config": {"theme": "dark", "language": "zh-CN"}
    }
    
    for storage in storages:
        print(f"\n=== {storage.__class__.__name__} ===")
        
        # 保存数据
        for key, value in test_data.items():
            result = storage.save(value, key)
            print(f"保存 {key}: {'成功' if result else '失败'}")
        
        # 列出所有数据
        print(f"所有数据: {storage.list_all()}")
        
        # 加载数据
        for key in ["user1", "config"]:
            if storage.exists(key):
                data = storage.load(key)
                print(f"加载 {key}: {data}")
        
        # 删除数据
        result = storage.delete("user2")
        print(f"删除 user2: {'成功' if result else '失败'}")
        print(f"删除后数据: {storage.list_all()}")
        
        # 调用特有方法
        if hasattr(storage, 'get_memory_usage'):
            print(f"内存使用: {storage.get_memory_usage()} 字节")

def demonstrate_serialization_interfaces():
    """演示序列化接口"""
    print("\n=== 序列化接口演示 ===")
    
    # 创建学生对象
    student = Student("王五", 20, "S001")
    student.add_grade("数学", 95.0)
    student.add_grade("英语", 88.5)
    student.add_grade("物理", 92.0)
    
    print(f"原始学生: {student}")
    
    # 序列化
    serialized = student.serialize()
    print(f"序列化结果: {serialized}")
    
    # 反序列化
    new_student = Student()
    new_student.deserialize(serialized)
    print(f"反序列化学生: {new_student}")
    
    # 导出为字典
    exported = student.export_to_dict()
    print(f"导出字典: {exported}")
    
    # 从字典导入
    another_student = Student()
    another_student.import_from_dict(exported)
    print(f"导入学生: {another_student}")

def demonstrate_notification_interfaces():
    """演示通知接口"""
    print("\n=== 通知接口演示 ===")
    
    senders = [
        EmailSender(),
        SMSSender(),
        PushNotificationSender()
    ]
    
    message = "您有一条新消息，请及时查看！"
    recipients = ["user@example.com", "13800138000", "device_token_123"]
    
    for i, sender in enumerate(senders):
        print(f"\n=== {sender.__class__.__name__} ===")
        
        # 发送通知
        success = sender.send(recipients[i], message)
        print(f"发送结果: {'成功' if success else '失败'}")

def demonstrate_payment_interfaces():
    """演示支付接口"""
    print("\n=== 支付接口演示 ===")
    
    processors = [
        CreditCardProcessor(),
        AlipayProcessor()
    ]
    
    amount = 199.99
    
    for processor in processors:
        print(f"\n=== {processor.__class__.__name__} ===")
        
        # 处理支付
        transaction = processor.process_payment(amount)
        print(f"支付结果: {transaction}")
        
        # 查询状态
        status = processor.get_transaction_status(transaction["transaction_id"])
        print(f"交易状态: {status}")
        
        # 退款
        refund = processor.refund_payment(transaction["transaction_id"], 50.0)
        print(f"退款结果: {refund}")

def demonstrate_interface_polymorphism():
    """演示接口多态性"""
    print("\n=== 接口多态性演示 ===")
    
    # 使用接口类型的变量
    drawable_objects: List[Drawable] = [
        Circle(0, 0, 3),
        Rectangle(0, 0, 4, 5)
    ]
    
    print("多态绘制:")
    for obj in drawable_objects:
        print(f"  {obj.draw()}")
        print(f"  面积: {obj.get_area():.2f}")
    
    # 存储接口多态
    storage_systems: List[DataStorage] = [
        MemoryStorage()
    ]
    
    print("\n多态存储:")
    for storage in storage_systems:
        storage.save({"test": "data"}, "test_key")
        print(f"  {storage.__class__.__name__}: {storage.list_all()}")
    
    # 支付接口多态
    payment_systems: List[PaymentProcessor] = [
        CreditCardProcessor(),
        AlipayProcessor()
    ]
    
    print("\n多态支付:")
    for processor in payment_systems:
        result = processor.process_payment(100.0)
        print(f"  {processor.__class__.__name__}: {result['status']}")

if __name__ == "__main__":
    # 演示形状接口
    demonstrate_shape_interfaces()
    
    # 演示存储接口
    demonstrate_storage_interfaces()
    
    # 演示序列化接口
    demonstrate_serialization_interfaces()
    
    # 演示通知接口
    demonstrate_notification_interfaces()
    
    # 演示支付接口
    demonstrate_payment_interfaces()
    
    # 演示接口多态性
    demonstrate_interface_polymorphism()
    
    print("\n=== 接口的核心要点 ===")
    print("1. 接口定义契约和规范")
    print("2. 实现类必须遵循接口")
    print("3. 支持多重继承")
    print("4. 提供代码的可扩展性")
    print("5. 实现多态的重要机制")
    print("6. 使用抽象基类（ABC）实现")
    print("7. 促进松耦合设计")
    print("8. 便于单元测试和模拟")