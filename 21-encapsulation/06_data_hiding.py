#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据隐藏和接口设计

数据隐藏是封装的核心概念，通过隐藏内部实现细节，只暴露必要的接口，
可以提高代码的安全性、可维护性和可扩展性。

学习目标：
1. 理解数据隐藏的重要性
2. 掌握接口设计的原则
3. 学会设计清晰的类接口
4. 了解信息隐藏的最佳实践
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional
import json
from datetime import datetime


# 1. 基本数据隐藏示例
class BadDesign:
    """糟糕的设计 - 没有数据隐藏"""
    
    def __init__(self):
        self.data = []  # 直接暴露内部数据
        self.count = 0  # 直接暴露计数器
        self.is_valid = True  # 直接暴露状态


class GoodDesign:
    """良好的设计 - 适当的数据隐藏"""
    
    def __init__(self):
        self._data = []  # 内部数据
        self._count = 0  # 内部计数器
        self._is_valid = True  # 内部状态
    
    def add_item(self, item):
        """添加项目 - 公有接口"""
        if self._is_valid and item is not None:
            self._data.append(item)
            self._count += 1
            return True
        return False
    
    def get_count(self):
        """获取项目数量 - 公有接口"""
        return self._count
    
    def get_items(self):
        """获取项目副本 - 公有接口"""
        return self._data.copy()
    
    def is_empty(self):
        """检查是否为空 - 公有接口"""
        return self._count == 0
    
    def clear(self):
        """清空数据 - 公有接口"""
        self._data.clear()
        self._count = 0


# 2. 抽象接口设计
class DataStorage(ABC):
    """数据存储抽象接口"""
    
    @abstractmethod
    def save(self, key: str, data: any) -> bool:
        """保存数据"""
        pass
    
    @abstractmethod
    def load(self, key: str) -> any:
        """加载数据"""
        pass
    
    @abstractmethod
    def delete(self, key: str) -> bool:
        """删除数据"""
        pass
    
    @abstractmethod
    def exists(self, key: str) -> bool:
        """检查数据是否存在"""
        pass


class MemoryStorage(DataStorage):
    """内存存储实现"""
    
    def __init__(self):
        self.__storage = {}  # 隐藏内部存储
    
    def save(self, key: str, data: any) -> bool:
        """保存数据到内存"""
        try:
            self.__storage[key] = data
            return True
        except Exception:
            return False
    
    def load(self, key: str) -> any:
        """从内存加载数据"""
        return self.__storage.get(key)
    
    def delete(self, key: str) -> bool:
        """从内存删除数据"""
        if key in self.__storage:
            del self.__storage[key]
            return True
        return False
    
    def exists(self, key: str) -> bool:
        """检查数据是否存在"""
        return key in self.__storage
    
    def get_size(self) -> int:
        """获取存储大小（额外功能）"""
        return len(self.__storage)


class FileStorage(DataStorage):
    """文件存储实现"""
    
    def __init__(self, base_path: str = "./data"):
        self.__base_path = base_path
        self.__ensure_directory()
    
    def __ensure_directory(self):
        """确保目录存在（私有方法）"""
        import os
        if not os.path.exists(self.__base_path):
            os.makedirs(self.__base_path)
    
    def __get_file_path(self, key: str) -> str:
        """获取文件路径（私有方法）"""
        import os
        return os.path.join(self.__base_path, f"{key}.json")
    
    def save(self, key: str, data: any) -> bool:
        """保存数据到文件"""
        try:
            file_path = self.__get_file_path(key)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception:
            return False
    
    def load(self, key: str) -> any:
        """从文件加载数据"""
        try:
            file_path = self.__get_file_path(key)
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return None
    
    def delete(self, key: str) -> bool:
        """删除文件"""
        try:
            import os
            file_path = self.__get_file_path(key)
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
            return False
        except Exception:
            return False
    
    def exists(self, key: str) -> bool:
        """检查文件是否存在"""
        import os
        file_path = self.__get_file_path(key)
        return os.path.exists(file_path)


# 3. 复杂的接口设计：用户管理系统
class User:
    """用户类 - 良好的数据隐藏"""
    
    def __init__(self, username: str, email: str):
        self.__username = username
        self.__email = email
        self.__password_hash = None
        self.__created_at = datetime.now()
        self.__last_login = None
        self.__is_active = True
        self.__profile = {}
    
    # 只读属性
    @property
    def username(self) -> str:
        return self.__username
    
    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def created_at(self) -> datetime:
        return self.__created_at
    
    @property
    def last_login(self) -> Optional[datetime]:
        return self.__last_login
    
    @property
    def is_active(self) -> bool:
        return self.__is_active
    
    # 受控的写操作
    def set_email(self, new_email: str) -> bool:
        """更新邮箱"""
        if self.__validate_email(new_email):
            self.__email = new_email
            return True
        return False
    
    def set_password(self, password: str) -> bool:
        """设置密码"""
        if self.__validate_password(password):
            self.__password_hash = self.__hash_password(password)
            return True
        return False
    
    def verify_password(self, password: str) -> bool:
        """验证密码"""
        if self.__password_hash is None:
            return False
        return self.__hash_password(password) == self.__password_hash
    
    def login(self, password: str) -> bool:
        """用户登录"""
        if self.verify_password(password) and self.__is_active:
            self.__last_login = datetime.now()
            return True
        return False
    
    def deactivate(self):
        """停用账户"""
        self.__is_active = False
    
    def activate(self):
        """激活账户"""
        self.__is_active = True
    
    def update_profile(self, **kwargs):
        """更新用户资料"""
        allowed_fields = {'name', 'age', 'city', 'bio'}
        for key, value in kwargs.items():
            if key in allowed_fields:
                self.__profile[key] = value
    
    def get_profile(self) -> Dict:
        """获取用户资料副本"""
        return self.__profile.copy()
    
    # 私有方法
    def __validate_email(self, email: str) -> bool:
        """验证邮箱格式"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def __validate_password(self, password: str) -> bool:
        """验证密码强度"""
        return len(password) >= 8 and any(c.isdigit() for c in password)
    
    def __hash_password(self, password: str) -> str:
        """密码哈希（简化版）"""
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()
    
    def __str__(self):
        return f"User({self.__username}, {self.__email})"


class UserManager:
    """用户管理器 - 封装用户操作"""
    
    def __init__(self, storage: DataStorage):
        self.__storage = storage
        self.__users = {}  # 内存缓存
        self.__load_users()
    
    def create_user(self, username: str, email: str, password: str) -> bool:
        """创建用户"""
        if self.__user_exists(username):
            return False
        
        user = User(username, email)
        if user.set_password(password):
            self.__users[username] = user
            self.__save_user(user)
            return True
        return False
    
    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """用户认证"""
        user = self.__users.get(username)
        if user and user.login(password):
            self.__save_user(user)  # 更新最后登录时间
            return user
        return None
    
    def get_user(self, username: str) -> Optional[User]:
        """获取用户"""
        return self.__users.get(username)
    
    def update_user_email(self, username: str, new_email: str) -> bool:
        """更新用户邮箱"""
        user = self.__users.get(username)
        if user and user.set_email(new_email):
            self.__save_user(user)
            return True
        return False
    
    def deactivate_user(self, username: str) -> bool:
        """停用用户"""
        user = self.__users.get(username)
        if user:
            user.deactivate()
            self.__save_user(user)
            return True
        return False
    
    def get_active_users(self) -> List[User]:
        """获取活跃用户列表"""
        return [user for user in self.__users.values() if user.is_active]
    
    def get_user_count(self) -> int:
        """获取用户总数"""
        return len(self.__users)
    
    # 私有方法
    def __user_exists(self, username: str) -> bool:
        """检查用户是否存在"""
        return username in self.__users
    
    def __save_user(self, user: User):
        """保存用户到存储"""
        user_data = {
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at.isoformat(),
            'last_login': user.last_login.isoformat() if user.last_login else None,
            'is_active': user.is_active,
            'profile': user.get_profile()
        }
        self.__storage.save(f"user_{user.username}", user_data)
    
    def __load_users(self):
        """从存储加载用户（简化版）"""
        # 在实际应用中，这里会从存储中加载所有用户
        pass


# 4. 接口隔离示例
class ReadOnlyInterface(ABC):
    """只读接口"""
    
    @abstractmethod
    def get(self, key: str) -> any:
        pass
    
    @abstractmethod
    def exists(self, key: str) -> bool:
        pass


class WriteOnlyInterface(ABC):
    """只写接口"""
    
    @abstractmethod
    def set(self, key: str, value: any) -> bool:
        pass
    
    @abstractmethod
    def delete(self, key: str) -> bool:
        pass


class Cache(ReadOnlyInterface, WriteOnlyInterface):
    """缓存类 - 实现多个接口"""
    
    def __init__(self, max_size: int = 100):
        self.__data = {}
        self.__max_size = max_size
        self.__access_order = []
    
    def get(self, key: str) -> any:
        """获取缓存值"""
        if key in self.__data:
            self.__update_access_order(key)
            return self.__data[key]
        return None
    
    def set(self, key: str, value: any) -> bool:
        """设置缓存值"""
        if key in self.__data:
            self.__data[key] = value
            self.__update_access_order(key)
        else:
            if len(self.__data) >= self.__max_size:
                self.__evict_least_recently_used()
            self.__data[key] = value
            self.__access_order.append(key)
        return True
    
    def delete(self, key: str) -> bool:
        """删除缓存值"""
        if key in self.__data:
            del self.__data[key]
            self.__access_order.remove(key)
            return True
        return False
    
    def exists(self, key: str) -> bool:
        """检查键是否存在"""
        return key in self.__data
    
    def __update_access_order(self, key: str):
        """更新访问顺序"""
        if key in self.__access_order:
            self.__access_order.remove(key)
        self.__access_order.append(key)
    
    def __evict_least_recently_used(self):
        """淘汰最少使用的项"""
        if self.__access_order:
            lru_key = self.__access_order.pop(0)
            del self.__data[lru_key]


def demonstrate_data_hiding():
    """演示数据隐藏和接口设计"""
    print("=" * 60)
    print("数据隐藏和接口设计演示")
    print("=" * 60)
    
    # 1. 基本数据隐藏对比
    print("\n1. 数据隐藏对比:")
    
    # 糟糕的设计
    bad = BadDesign()
    bad.data.append("直接修改内部数据")  # 危险！
    bad.count = -1  # 破坏了数据一致性！
    print(f"糟糕设计 - 数据: {bad.data}, 计数: {bad.count}")
    
    # 良好的设计
    good = GoodDesign()
    good.add_item("安全添加数据")
    good.add_item("另一个项目")
    print(f"良好设计 - 项目数: {good.get_count()}, 是否为空: {good.is_empty()}")
    print(f"项目列表: {good.get_items()}")
    
    # 2. 存储接口演示
    print("\n2. 存储接口演示:")
    
    # 内存存储
    memory_storage = MemoryStorage()
    memory_storage.save("user1", {"name": "张三", "age": 25})
    memory_storage.save("user2", {"name": "李四", "age": 30})
    
    print(f"内存存储大小: {memory_storage.get_size()}")
    print(f"用户1数据: {memory_storage.load('user1')}")
    print(f"用户3存在: {memory_storage.exists('user3')}")
    
    # 3. 用户管理系统演示
    print("\n3. 用户管理系统演示:")
    
    user_manager = UserManager(memory_storage)
    
    # 创建用户
    success = user_manager.create_user("alice", "alice@example.com", "password123")
    print(f"创建用户Alice: {success}")
    
    success = user_manager.create_user("bob", "bob@example.com", "secret456")
    print(f"创建用户Bob: {success}")
    
    # 用户认证
    user = user_manager.authenticate_user("alice", "password123")
    if user:
        print(f"认证成功: {user}")
        print(f"最后登录: {user.last_login}")
    
    # 更新用户信息
    alice = user_manager.get_user("alice")
    if alice:
        alice.update_profile(name="Alice Smith", city="北京")
        print(f"Alice的资料: {alice.get_profile()}")
    
    # 获取活跃用户
    active_users = user_manager.get_active_users()
    print(f"活跃用户数: {len(active_users)}")
    
    # 4. 缓存接口演示
    print("\n4. 缓存接口演示:")
    
    cache = Cache(max_size=3)
    
    # 作为只写接口使用
    write_interface: WriteOnlyInterface = cache
    write_interface.set("key1", "value1")
    write_interface.set("key2", "value2")
    write_interface.set("key3", "value3")
    
    # 作为只读接口使用
    read_interface: ReadOnlyInterface = cache
    print(f"key1存在: {read_interface.exists('key1')}")
    print(f"key1的值: {read_interface.get('key1')}")
    
    # 触发LRU淘汰
    cache.set("key4", "value4")  # 应该淘汰key2
    print(f"添加key4后，key2存在: {cache.exists('key2')}")
    print(f"key4的值: {cache.get('key4')}")


def show_interface_design_principles():
    """显示接口设计原则"""
    print("\n" + "=" * 60)
    print("接口设计原则")
    print("=" * 60)
    
    principles = """
1. 单一职责原则 (SRP)
   - 每个类应该只有一个改变的理由
   - 接口应该专注于单一功能

2. 开闭原则 (OCP)
   - 对扩展开放，对修改关闭
   - 通过抽象接口支持多种实现

3. 里氏替换原则 (LSP)
   - 子类应该能够替换父类
   - 实现类应该遵循接口契约

4. 接口隔离原则 (ISP)
   - 客户端不应该依赖它不需要的接口
   - 使用多个专门的接口而不是单一的通用接口

5. 依赖倒置原则 (DIP)
   - 高层模块不应该依赖低层模块
   - 都应该依赖于抽象

数据隐藏最佳实践:
✓ 使用私有属性保护内部状态
✓ 提供清晰的公有接口
✓ 验证输入数据
✓ 返回数据副本而不是原始引用
✓ 使用属性装饰器控制访问
✓ 遵循最小权限原则
✓ 文档化接口契约
    """
    
    print(principles)


if __name__ == "__main__":
    demonstrate_data_hiding()
    show_interface_design_principles()