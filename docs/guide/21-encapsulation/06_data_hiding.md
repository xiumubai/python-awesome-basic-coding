# 数据隐藏和接口设计

数据隐藏是面向对象编程中的核心概念，它通过封装将对象的内部状态隐藏起来，只通过定义良好的接口与外界交互。这种设计方式提高了代码的安全性、可维护性和可扩展性。

## 数据隐藏的基本概念

- **数据隐藏**：将对象的内部数据和实现细节隐藏起来，不允许外部直接访问
- **接口设计**：提供清晰、一致的公共方法来操作对象
- **封装边界**：明确定义什么是公开的，什么是私有的
- **抽象层次**：通过接口提供不同层次的抽象

## 基本数据隐藏示例

### 1. 简单的数据隐藏

```python
class BankAccount:
    """银行账户 - 基本数据隐藏示例"""
    
    def __init__(self, account_number, initial_balance=0):
        # 公开信息
        self.account_number = account_number
        
        # 隐藏的内部数据
        self._balance = initial_balance  # 保护属性
        self._transaction_count = 0      # 内部计数器
    
    # 公共接口方法
    def deposit(self, amount):
        """存款接口"""
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        
        self._balance += amount
        self._transaction_count += 1
        return f"存款成功，当前余额: {self._balance}"
    
    def withdraw(self, amount):
        """取款接口"""
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        if amount > self._balance:
            raise ValueError("余额不足")
        
        self._balance -= amount
        self._transaction_count += 1
        return f"取款成功，当前余额: {self._balance}"
    
    def get_balance(self):
        """获取余额接口"""
        return self._balance
    
    def get_transaction_count(self):
        """获取交易次数接口"""
        return self._transaction_count
    
    def __str__(self):
        return f"账户 {self.account_number}: 余额 {self._balance}, 交易次数 {self._transaction_count}"

# 演示基本数据隐藏
def demonstrate_basic_data_hiding():
    """演示基本数据隐藏"""
    print("=== 基本数据隐藏演示 ===")
    
    account = BankAccount("123456", 1000)
    print(f"初始状态: {account}")
    
    # 通过公共接口操作
    print("\n通过公共接口操作:")
    print(account.deposit(500))
    print(account.withdraw(200))
    print(f"当前余额: {account.get_balance()}")
    print(f"交易次数: {account.get_transaction_count()}")
    
    # 直接访问内部数据（不推荐，但可以）
    print("\n直接访问内部数据:")
    print(f"直接访问余额: {account._balance}")
    print(f"直接修改余额: ", end="")
    account._balance = 999999  # 绕过了业务逻辑
    print(f"{account._balance}")
    print(f"修改后状态: {account}")
    
    print("\n数据隐藏的意义:")
    print("- 通过接口操作保证了业务逻辑的完整性")
    print("- 直接修改内部数据可能破坏对象的一致性")
    print("- 接口提供了统一的操作方式")

# 运行演示
demonstrate_basic_data_hiding()
```

### 2. 抽象接口设计

```python
from abc import ABC, abstractmethod

class Storage(ABC):
    """存储接口抽象类"""
    
    @abstractmethod
    def save(self, key, data):
        """保存数据"""
        pass
    
    @abstractmethod
    def load(self, key):
        """加载数据"""
        pass
    
    @abstractmethod
    def delete(self, key):
        """删除数据"""
        pass
    
    @abstractmethod
    def exists(self, key):
        """检查数据是否存在"""
        pass

class MemoryStorage(Storage):
    """内存存储实现"""
    
    def __init__(self):
        self._data = {}  # 隐藏的内部存储
        self._access_count = {}  # 隐藏的访问计数
    
    def save(self, key, data):
        """保存数据到内存"""
        if not isinstance(key, str):
            raise TypeError("键必须是字符串")
        
        self._data[key] = data
        self._access_count[key] = self._access_count.get(key, 0)
        return f"数据已保存: {key}"
    
    def load(self, key):
        """从内存加载数据"""
        if key not in self._data:
            raise KeyError(f"数据不存在: {key}")
        
        self._access_count[key] = self._access_count.get(key, 0) + 1
        return self._data[key]
    
    def delete(self, key):
        """从内存删除数据"""
        if key not in self._data:
            raise KeyError(f"数据不存在: {key}")
        
        del self._data[key]
        del self._access_count[key]
        return f"数据已删除: {key}"
    
    def exists(self, key):
        """检查数据是否存在"""
        return key in self._data
    
    def get_stats(self):
        """获取统计信息（额外的公共接口）"""
        return {
            "总数据量": len(self._data),
            "访问统计": dict(self._access_count)
        }
    
    def clear(self):
        """清空所有数据"""
        count = len(self._data)
        self._data.clear()
        self._access_count.clear()
        return f"已清空 {count} 条数据"

class FileStorage(Storage):
    """文件存储实现"""
    
    def __init__(self, base_path="./data"):
        self._base_path = base_path  # 隐藏的基础路径
        self._file_handles = {}      # 隐藏的文件句柄缓存
        self._ensure_directory()
    
    def _ensure_directory(self):
        """确保目录存在（私有方法）"""
        import os
        if not os.path.exists(self._base_path):
            os.makedirs(self._base_path)
    
    def _get_file_path(self, key):
        """获取文件路径（私有方法）"""
        import os
        return os.path.join(self._base_path, f"{key}.txt")
    
    def save(self, key, data):
        """保存数据到文件"""
        if not isinstance(key, str):
            raise TypeError("键必须是字符串")
        
        file_path = self._get_file_path(key)
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(data))
            return f"数据已保存到文件: {key}"
        except Exception as e:
            raise RuntimeError(f"保存失败: {e}")
    
    def load(self, key):
        """从文件加载数据"""
        file_path = self._get_file_path(key)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise KeyError(f"数据不存在: {key}")
        except Exception as e:
            raise RuntimeError(f"加载失败: {e}")
    
    def delete(self, key):
        """删除文件数据"""
        file_path = self._get_file_path(key)
        try:
            import os
            os.remove(file_path)
            return f"数据已删除: {key}"
        except FileNotFoundError:
            raise KeyError(f"数据不存在: {key}")
        except Exception as e:
            raise RuntimeError(f"删除失败: {e}")
    
    def exists(self, key):
        """检查文件是否存在"""
        import os
        file_path = self._get_file_path(key)
        return os.path.exists(file_path)
    
    def list_keys(self):
        """列出所有键（额外的公共接口）"""
        import os
        if not os.path.exists(self._base_path):
            return []
        
        files = os.listdir(self._base_path)
        return [f[:-4] for f in files if f.endswith('.txt')]

# 演示抽象接口设计
def demonstrate_abstract_interface():
    """演示抽象接口设计"""
    print("\n=== 抽象接口设计演示 ===")
    
    # 使用不同的存储实现
    storages = {
        "内存存储": MemoryStorage(),
        "文件存储": FileStorage()
    }
    
    for name, storage in storages.items():
        print(f"\n--- {name} ---")
        
        # 统一的接口操作
        print(storage.save("user1", "张三的数据"))
        print(storage.save("user2", "李四的数据"))
        
        print(f"user1存在: {storage.exists('user1')}")
        print(f"user3存在: {storage.exists('user3')}")
        
        print(f"加载user1: {storage.load('user1')}")
        print(f"加载user2: {storage.load('user2')}")
        
        # 特定实现的额外功能
        if isinstance(storage, MemoryStorage):
            stats = storage.get_stats()
            print(f"内存存储统计: {stats}")
        elif isinstance(storage, FileStorage):
            keys = storage.list_keys()
            print(f"文件存储键列表: {keys}")
        
        print(storage.delete("user1"))
        print(f"删除后user1存在: {storage.exists('user1')}")
        
        # 清理
        if isinstance(storage, MemoryStorage):
            print(storage.clear())
        elif isinstance(storage, FileStorage):
            for key in storage.list_keys():
                storage.delete(key)
    
    print("\n接口设计的优势:")
    print("- 统一的操作方式，易于使用")
    print("- 可以轻松切换不同的实现")
    print("- 隐藏了具体的实现细节")
    print("- 便于测试和维护")

# 运行演示
demonstrate_abstract_interface()
```

### 3. 复杂的用户管理系统

```python
import hashlib
import datetime
from enum import Enum

class UserRole(Enum):
    """用户角色枚举"""
    GUEST = "guest"
    USER = "user"
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"

class UserStatus(Enum):
    """用户状态枚举"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    DELETED = "deleted"

class User:
    """用户类 - 复杂数据隐藏示例"""
    
    def __init__(self, username, email, password):
        # 公开信息
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.now()
        
        # 保护信息（内部使用）
        self._user_id = self._generate_user_id()
        self._role = UserRole.USER
        self._status = UserStatus.ACTIVE
        self._last_login = None
        self._login_attempts = 0
        
        # 私有信息（高度敏感）
        self.__password_hash = self._hash_password(password)
        self.__salt = self._generate_salt()
        self.__session_token = None
        self.__failed_login_count = 0
        self.__last_password_change = datetime.datetime.now()
    
    def _generate_user_id(self):
        """生成用户ID（保护方法）"""
        import uuid
        return str(uuid.uuid4())[:8]
    
    def _hash_password(self, password):
        """密码哈希（保护方法）"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _generate_salt(self):
        """生成盐值（保护方法）"""
        import secrets
        return secrets.token_hex(16)
    
    def __generate_session_token(self):
        """生成会话令牌（私有方法）"""
        import secrets
        return secrets.token_urlsafe(32)
    
    def __verify_password(self, password):
        """验证密码（私有方法）"""
        return self.__password_hash == self._hash_password(password)
    
    def __reset_failed_attempts(self):
        """重置失败尝试次数（私有方法）"""
        self.__failed_login_count = 0
        self._login_attempts = 0
    
    def __increment_failed_attempts(self):
        """增加失败尝试次数（私有方法）"""
        self.__failed_login_count += 1
        self._login_attempts += 1
        
        if self.__failed_login_count >= 5:
            self._status = UserStatus.SUSPENDED
            return True
        return False
    
    # 公共接口方法
    def login(self, password):
        """用户登录接口"""
        if self._status == UserStatus.SUSPENDED:
            raise RuntimeError("账户已被暂停，请联系管理员")
        
        if self._status != UserStatus.ACTIVE:
            raise RuntimeError("账户状态异常，无法登录")
        
        if not self.__verify_password(password):
            is_suspended = self.__increment_failed_attempts()
            if is_suspended:
                raise RuntimeError("登录失败次数过多，账户已被暂停")
            
            remaining = 5 - self.__failed_login_count
            raise ValueError(f"密码错误，剩余尝试次数: {remaining}")
        
        # 登录成功
        self.__reset_failed_attempts()
        self._last_login = datetime.datetime.now()
        self.__session_token = self.__generate_session_token()
        
        return {
            "success": True,
            "message": "登录成功",
            "session_token": self.__session_token,
            "user_id": self._user_id
        }
    
    def logout(self):
        """用户登出接口"""
        if self.__session_token is None:
            return {"success": False, "message": "用户未登录"}
        
        self.__session_token = None
        return {"success": True, "message": "登出成功"}
    
    def change_password(self, old_password, new_password):
        """修改密码接口"""
        if not self.__verify_password(old_password):
            self.__increment_failed_attempts()
            raise ValueError("原密码错误")
        
        if len(new_password) < 8:
            raise ValueError("新密码长度至少8位")
        
        if new_password == old_password:
            raise ValueError("新密码不能与原密码相同")
        
        self.__password_hash = self._hash_password(new_password)
        self.__last_password_change = datetime.datetime.now()
        self.__session_token = None  # 强制重新登录
        
        return {"success": True, "message": "密码修改成功，请重新登录"}
    
    def get_profile(self):
        """获取用户资料接口"""
        return {
            "user_id": self._user_id,
            "username": self.username,
            "email": self.email,
            "role": self._role.value,
            "status": self._status.value,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "last_login": self._last_login.strftime("%Y-%m-%d %H:%M:%S") if self._last_login else None,
            "is_logged_in": self.__session_token is not None
        }
    
    def update_profile(self, email=None):
        """更新用户资料接口"""
        if email is not None:
            if "@" not in email:
                raise ValueError("邮箱格式不正确")
            self.email = email
        
        return {"success": True, "message": "资料更新成功"}
    
    def is_authenticated(self, session_token):
        """验证会话令牌接口"""
        return self.__session_token is not None and self.__session_token == session_token
    
    def get_security_info(self):
        """获取安全信息接口（管理员用）"""
        if self._role not in [UserRole.ADMIN, UserRole.SUPER_ADMIN]:
            raise PermissionError("权限不足")
        
        return {
            "failed_login_count": self.__failed_login_count,
            "total_login_attempts": self._login_attempts,
            "last_password_change": self.__last_password_change.strftime("%Y-%m-%d %H:%M:%S"),
            "has_active_session": self.__session_token is not None
        }
    
    def set_role(self, new_role):
        """设置用户角色接口（管理员用）"""
        if not isinstance(new_role, UserRole):
            raise TypeError("角色必须是UserRole枚举")
        
        self._role = new_role
        return {"success": True, "message": f"角色已设置为 {new_role.value}"}
    
    def set_status(self, new_status):
        """设置用户状态接口（管理员用）"""
        if not isinstance(new_status, UserStatus):
            raise TypeError("状态必须是UserStatus枚举")
        
        old_status = self._status
        self._status = new_status
        
        # 状态变更时的特殊处理
        if new_status == UserStatus.ACTIVE and old_status == UserStatus.SUSPENDED:
            self.__reset_failed_attempts()
        elif new_status in [UserStatus.SUSPENDED, UserStatus.DELETED]:
            self.__session_token = None  # 强制登出
        
        return {"success": True, "message": f"状态已从 {old_status.value} 更改为 {new_status.value}"}
    
    def __str__(self):
        return f"User({self.username}, {self._role.value}, {self._status.value})"

class UserManager:
    """用户管理器 - 演示接口隔离"""
    
    def __init__(self):
        self._users = {}  # 隐藏的用户存储
        self._admin_users = set()  # 隐藏的管理员列表
    
    def register_user(self, username, email, password):
        """注册用户接口"""
        if username in self._users:
            raise ValueError("用户名已存在")
        
        user = User(username, email, password)
        self._users[username] = user
        
        return {
            "success": True,
            "message": "用户注册成功",
            "user_id": user._user_id
        }
    
    def authenticate_user(self, username, password):
        """用户认证接口"""
        if username not in self._users:
            raise ValueError("用户不存在")
        
        user = self._users[username]
        return user.login(password)
    
    def get_user(self, username):
        """获取用户接口"""
        if username not in self._users:
            raise ValueError("用户不存在")
        
        return self._users[username]
    
    def promote_to_admin(self, username):
        """提升为管理员接口"""
        if username not in self._users:
            raise ValueError("用户不存在")
        
        user = self._users[username]
        user.set_role(UserRole.ADMIN)
        self._admin_users.add(username)
        
        return {"success": True, "message": f"{username} 已提升为管理员"}
    
    def list_users(self):
        """列出所有用户接口"""
        return {
            "total_users": len(self._users),
            "users": [user.get_profile() for user in self._users.values()]
        }

# 演示复杂用户管理系统
def demonstrate_user_management_system():
    """演示复杂用户管理系统"""
    print("\n=== 复杂用户管理系统演示 ===")
    
    manager = UserManager()
    
    # 注册用户
    print("\n1. 用户注册:")
    result = manager.register_user("alice", "alice@example.com", "password123")
    print(f"注册结果: {result}")
    
    result = manager.register_user("bob", "bob@example.com", "secret456")
    print(f"注册结果: {result}")
    
    # 用户登录
    print("\n2. 用户登录:")
    alice = manager.get_user("alice")
    login_result = alice.login("password123")
    print(f"Alice登录: {login_result}")
    
    # 查看用户资料
    print("\n3. 用户资料:")
    profile = alice.get_profile()
    for key, value in profile.items():
        print(f"  {key}: {value}")
    
    # 修改密码
    print("\n4. 修改密码:")
    change_result = alice.change_password("password123", "newpassword789")
    print(f"密码修改: {change_result}")
    
    # 重新登录
    print("\n5. 重新登录:")
    login_result = alice.login("newpassword789")
    print(f"新密码登录: {login_result}")
    
    # 错误密码尝试
    print("\n6. 错误密码尝试:")
    bob = manager.get_user("bob")
    for i in range(3):
        try:
            bob.login("wrongpassword")
        except ValueError as e:
            print(f"  尝试 {i+1}: {e}")
    
    # 提升为管理员
    print("\n7. 提升为管理员:")
    promote_result = manager.promote_to_admin("alice")
    print(f"提升结果: {promote_result}")
    
    # 管理员查看安全信息
    print("\n8. 管理员查看安全信息:")
    try:
        security_info = alice.get_security_info()
        print(f"Alice安全信息: {security_info}")
    except PermissionError as e:
        print(f"权限错误: {e}")
    
    # 列出所有用户
    print("\n9. 用户列表:")
    users_list = manager.list_users()
    print(f"总用户数: {users_list['total_users']}")
    for user_info in users_list['users']:
        print(f"  {user_info['username']} ({user_info['role']}, {user_info['status']})")
    
    # 演示数据隐藏的保护效果
    print("\n10. 数据隐藏保护效果:")
    print("尝试直接访问敏感数据:")
    try:
        print(alice.__password_hash)
    except AttributeError:
        print("  无法直接访问密码哈希")
    
    try:
        print(alice.__session_token)
    except AttributeError:
        print("  无法直接访问会话令牌")
    
    print("\n但可以通过修饰后的名称访问（需要知道类名）:")
    print(f"  密码哈希: {alice._User__password_hash[:20]}...")
    print(f"  会话令牌: {alice._User__session_token[:20] if alice._User__session_token else 'None'}...")

# 运行演示
demonstrate_user_management_system()
```

### 4. 接口隔离示例

```python
from abc import ABC, abstractmethod

# 接口隔离原则 - 将大接口拆分为小接口

class Readable(ABC):
    """可读接口"""
    
    @abstractmethod
    def read(self, key):
        pass

class Writable(ABC):
    """可写接口"""
    
    @abstractmethod
    def write(self, key, data):
        pass

class Deletable(ABC):
    """可删除接口"""
    
    @abstractmethod
    def delete(self, key):
        pass

class Cacheable(ABC):
    """可缓存接口"""
    
    @abstractmethod
    def get_cache_info(self):
        pass
    
    @abstractmethod
    def clear_cache(self):
        pass

class ReadOnlyCache(Readable, Cacheable):
    """只读缓存 - 只实现读取和缓存接口"""
    
    def __init__(self):
        self._cache = {}  # 隐藏的缓存存储
        self._hit_count = 0  # 隐藏的命中计数
        self._miss_count = 0  # 隐藏的未命中计数
    
    def read(self, key):
        """读取数据"""
        if key in self._cache:
            self._hit_count += 1
            return self._cache[key]
        else:
            self._miss_count += 1
            raise KeyError(f"缓存中不存在: {key}")
    
    def _load_data(self, key, data):
        """内部方法：加载数据到缓存"""
        self._cache[key] = data
    
    def get_cache_info(self):
        """获取缓存信息"""
        total = self._hit_count + self._miss_count
        hit_rate = self._hit_count / total if total > 0 else 0
        
        return {
            "缓存大小": len(self._cache),
            "命中次数": self._hit_count,
            "未命中次数": self._miss_count,
            "命中率": f"{hit_rate:.2%}"
        }
    
    def clear_cache(self):
        """清空缓存"""
        count = len(self._cache)
        self._cache.clear()
        self._hit_count = 0
        self._miss_count = 0
        return f"已清空 {count} 条缓存数据"

class ReadWriteCache(Readable, Writable, Deletable, Cacheable):
    """读写缓存 - 实现所有接口"""
    
    def __init__(self, max_size=100):
        self._cache = {}  # 隐藏的缓存存储
        self._access_order = []  # 隐藏的访问顺序（LRU）
        self._max_size = max_size  # 隐藏的最大大小
        self._hit_count = 0
        self._miss_count = 0
        self._write_count = 0
        self._delete_count = 0
    
    def _update_access_order(self, key):
        """更新访问顺序（私有方法）"""
        if key in self._access_order:
            self._access_order.remove(key)
        self._access_order.append(key)
    
    def _evict_if_needed(self):
        """如果需要则驱逐数据（私有方法）"""
        while len(self._cache) >= self._max_size and self._access_order:
            oldest_key = self._access_order.pop(0)
            if oldest_key in self._cache:
                del self._cache[oldest_key]
    
    def read(self, key):
        """读取数据"""
        if key in self._cache:
            self._hit_count += 1
            self._update_access_order(key)
            return self._cache[key]
        else:
            self._miss_count += 1
            raise KeyError(f"缓存中不存在: {key}")
    
    def write(self, key, data):
        """写入数据"""
        self._evict_if_needed()
        self._cache[key] = data
        self._update_access_order(key)
        self._write_count += 1
        return f"数据已写入: {key}"
    
    def delete(self, key):
        """删除数据"""
        if key not in self._cache:
            raise KeyError(f"缓存中不存在: {key}")
        
        del self._cache[key]
        if key in self._access_order:
            self._access_order.remove(key)
        self._delete_count += 1
        return f"数据已删除: {key}"
    
    def get_cache_info(self):
        """获取缓存信息"""
        total_reads = self._hit_count + self._miss_count
        hit_rate = self._hit_count / total_reads if total_reads > 0 else 0
        
        return {
            "缓存大小": len(self._cache),
            "最大大小": self._max_size,
            "命中次数": self._hit_count,
            "未命中次数": self._miss_count,
            "写入次数": self._write_count,
            "删除次数": self._delete_count,
            "命中率": f"{hit_rate:.2%}",
            "访问顺序": self._access_order[-5:]  # 显示最近5个
        }
    
    def clear_cache(self):
        """清空缓存"""
        count = len(self._cache)
        self._cache.clear()
        self._access_order.clear()
        self._hit_count = 0
        self._miss_count = 0
        self._write_count = 0
        self._delete_count = 0
        return f"已清空 {count} 条缓存数据"

# 演示接口隔离
def demonstrate_interface_segregation():
    """演示接口隔离原则"""
    print("\n=== 接口隔离原则演示 ===")
    
    # 只读缓存
    print("\n1. 只读缓存:")
    readonly_cache = ReadOnlyCache()
    
    # 预加载一些数据
    readonly_cache._load_data("config1", "配置数据1")
    readonly_cache._load_data("config2", "配置数据2")
    
    print(f"读取config1: {readonly_cache.read('config1')}")
    print(f"读取config2: {readonly_cache.read('config2')}")
    
    try:
        readonly_cache.read('config3')
    except KeyError as e:
        print(f"读取不存在的数据: {e}")
    
    cache_info = readonly_cache.get_cache_info()
    print(f"只读缓存信息: {cache_info}")
    
    # 读写缓存
    print("\n2. 读写缓存:")
    readwrite_cache = ReadWriteCache(max_size=3)
    
    # 写入数据
    print(readwrite_cache.write("user1", "用户1数据"))
    print(readwrite_cache.write("user2", "用户2数据"))
    print(readwrite_cache.write("user3", "用户3数据"))
    
    # 读取数据
    print(f"读取user1: {readwrite_cache.read('user1')}")
    print(f"读取user2: {readwrite_cache.read('user2')}")
    
    # 写入更多数据（触发LRU驱逐）
    print(readwrite_cache.write("user4", "用户4数据"))
    
    try:
        readwrite_cache.read('user3')  # user3可能被驱逐了
    except KeyError as e:
        print(f"读取被驱逐的数据: {e}")
    
    # 删除数据
    print(readwrite_cache.delete("user1"))
    
    cache_info = readwrite_cache.get_cache_info()
    print(f"读写缓存信息:")
    for key, value in cache_info.items():
        print(f"  {key}: {value}")
    
    # 清空缓存
    print(f"\n清空缓存: {readwrite_cache.clear_cache()}")
    
    print("\n3. 接口隔离的优势:")
    print("- 客户端只依赖它需要的接口")
    print("- 不同的实现可以选择实现不同的接口组合")
    print("- 接口更加内聚，职责单一")
    print("- 便于测试和维护")
    
    # 演示接口的灵活使用
    print("\n4. 接口的灵活使用:")
    
    def use_readable(readable_obj: Readable, key):
        """使用可读接口的函数"""
        try:
            return readable_obj.read(key)
        except KeyError:
            return None
    
    def use_cacheable(cacheable_obj: Cacheable):
        """使用可缓存接口的函数"""
        return cacheable_obj.get_cache_info()
    
    # 重新创建一些数据
    readwrite_cache.write("test1", "测试数据1")
    readwrite_cache.write("test2", "测试数据2")
    
    print(f"通过Readable接口读取: {use_readable(readwrite_cache, 'test1')}")
    print(f"通过Cacheable接口获取信息: {use_cacheable(readwrite_cache)}")

# 运行演示
demonstrate_interface_segregation()
```

## 数据隐藏和接口设计的总结

```python
def demonstrate_data_hiding_summary():
    """数据隐藏和接口设计总结"""
    print("\n=== 数据隐藏和接口设计总结 ===")
    
    print("\n1. 数据隐藏的核心原则:")
    print("   - 隐藏实现细节，暴露必要接口")
    print("   - 保护对象的内部状态")
    print("   - 提供统一的操作方式")
    print("   - 确保数据的一致性和完整性")
    
    print("\n2. 接口设计的最佳实践:")
    print("   - 单一职责原则：每个接口只负责一个功能")
    print("   - 开闭原则：对扩展开放，对修改封闭")
    print("   - 里氏替换原则：子类可以替换父类")
    print("   - 接口隔离原则：客户端不应依赖不需要的接口")
    print("   - 依赖倒置原则：依赖抽象而不是具体实现")
    
    print("\n3. 数据隐藏的实现技术:")
    print("   - 使用私有属性（_attribute, __attribute）")
    print("   - 提供公有接口方法")
    print("   - 输入验证和错误处理")
    print("   - 状态管理和业务逻辑封装")
    
    print("\n4. 接口设计的层次:")
    print("   - 抽象接口：定义契约和规范")
    print("   - 具体实现：实现具体的业务逻辑")
    print("   - 适配器模式：适配不同的接口")
    print("   - 门面模式：提供简化的接口")
    
    print("\n5. 实际应用场景:")
    print("   - 数据库访问层")
    print("   - 网络通信模块")
    print("   - 用户认证系统")
    print("   - 缓存管理系统")
    print("   - 配置管理模块")
    
    print("\n6. 设计考虑因素:")
    print("   - 安全性：保护敏感数据")
    print("   - 可维护性：便于修改和扩展")
    print("   - 可测试性：便于单元测试")
    print("   - 性能：避免不必要的开销")
    print("   - 易用性：提供直观的接口")

# 运行总结
demonstrate_data_hiding_summary()
```

## 学习要点

### 数据隐藏的核心概念

1. **封装边界**：明确定义什么是公开的，什么是私有的
2. **接口契约**：定义清晰的输入输出规范
3. **状态保护**：确保对象状态的一致性和完整性
4. **实现隐藏**：隐藏具体的实现细节

### 接口设计原则

1. **单一职责**：每个接口只负责一个明确的功能
2. **最小接口**：只暴露必要的操作
3. **一致性**：保持接口的命名和行为一致
4. **可扩展性**：设计时考虑未来的扩展需求

### 实现技术

1. **访问控制**：使用私有属性和方法
2. **输入验证**：在接口层进行参数验证
3. **错误处理**：提供清晰的错误信息
4. **状态管理**：维护对象的内部状态

### 设计模式应用

1. **门面模式**：为复杂系统提供简单接口
2. **适配器模式**：适配不同的接口规范
3. **策略模式**：封装不同的算法实现
4. **观察者模式**：隐藏通知机制的实现

### 实际应用建议

1. **渐进式设计**：从简单开始，逐步完善
2. **文档化**：清楚地记录接口的用途和限制
3. **版本管理**：考虑接口的向后兼容性
4. **测试驱动**：通过测试验证接口的正确性
5. **性能考虑**：平衡封装和性能需求

数据隐藏和接口设计是面向对象编程的核心技能，通过合理的封装和接口设计，可以创建出安全、可维护、可扩展的软件系统。