# 访问控制：公有、私有、保护属性

Python中的访问控制是基于命名约定的，通过不同的命名方式来表示不同的访问级别。

## 访问控制级别

### 1. 公有属性（Public）

公有属性没有特殊的命名约定，可以被任何地方访问。

```python
class PublicExample:
    def __init__(self):
        self.public_attr = "我是公有属性"  # 公有属性
        self.name = "张三"                # 公有属性
        self.age = 25                     # 公有属性
    
    def public_method(self):
        """公有方法"""
        return "我是公有方法"
    
    def get_info(self):
        """获取信息的公有方法"""
        return f"姓名: {self.name}, 年龄: {self.age}"

# 使用示例
obj = PublicExample()
print(obj.public_attr)      # 直接访问
print(obj.name)             # 直接访问
print(obj.public_method())  # 直接调用
print(obj.get_info())       # 直接调用

# 可以直接修改
obj.name = "李四"
obj.age = 30
print(obj.get_info())
```

### 2. 保护属性（Protected）

保护属性使用单下划线前缀，表示这是内部使用的属性，外部不应该直接访问。

```python
class ProtectedExample:
    def __init__(self):
        self._protected_attr = "我是保护属性"  # 保护属性
        self._internal_state = 0            # 内部状态
        self.public_counter = 0             # 公有计数器
    
    def _protected_method(self):
        """保护方法 - 内部使用"""
        self._internal_state += 1
        return f"内部状态: {self._internal_state}"
    
    def public_operation(self):
        """公有操作 - 调用保护方法"""
        result = self._protected_method()  # 内部调用保护方法
        self.public_counter += 1
        return f"操作完成: {result}, 公有计数: {self.public_counter}"
    
    def get_protected_info(self):
        """通过公有方法访问保护属性"""
        return self._protected_attr

# 使用示例
obj = ProtectedExample()

# 推荐的使用方式
print(obj.public_operation())
print(obj.get_protected_info())

# 技术上可以访问，但不推荐
print(obj._protected_attr)    # 可以访问，但违反约定
print(obj._protected_method()) # 可以调用，但违反约定

# 外部修改保护属性（不推荐）
obj._protected_attr = "被外部修改了"
print(obj.get_protected_info())
```

### 3. 私有属性（Private）

私有属性使用双下划线前缀，Python会对其进行名称修饰（Name Mangling）。

```python
class PrivateExample:
    def __init__(self):
        self.__private_attr = "我是私有属性"  # 私有属性
        self.__secret_key = "secret123"     # 私有密钥
        self._protected_attr = "保护属性"    # 保护属性
        self.public_attr = "公有属性"        # 公有属性
    
    def __private_method(self):
        """私有方法"""
        return f"私有方法访问: {self.__private_attr}"
    
    def public_access_private(self):
        """通过公有方法访问私有成员"""
        return self.__private_method()
    
    def validate_key(self, key):
        """验证密钥"""
        return key == self.__secret_key
    
    def get_all_attrs(self):
        """获取所有属性信息"""
        return {
            'public': self.public_attr,
            'protected': self._protected_attr,
            'private': self.__private_attr
        }

# 使用示例
obj = PrivateExample()

# 正常访问
print(obj.public_attr)              # 公有属性
print(obj._protected_attr)          # 保护属性（可访问但不推荐）
print(obj.public_access_private())  # 通过公有方法访问私有成员

# 尝试直接访问私有属性（会失败）
try:
    print(obj.__private_attr)  # AttributeError
except AttributeError as e:
    print(f"无法访问私有属性: {e}")

try:
    print(obj.__private_method())  # AttributeError
except AttributeError as e:
    print(f"无法调用私有方法: {e}")

# 通过名称修饰可以访问（不推荐）
print(f"通过名称修饰访问: {obj._PrivateExample__private_attr}")

# 验证功能
print(f"密钥验证: {obj.validate_key('secret123')}")
print(f"错误密钥: {obj.validate_key('wrong')}")

# 获取属性信息
print(f"所有属性: {obj.get_all_attrs()}")
```

## 实际应用示例：用户账户系统

```python
class UserAccount:
    """用户账户系统 - 展示不同访问控制级别的应用"""
    
    def __init__(self, username, email, password):
        # 公有属性
        self.username = username
        self.created_at = "2024-01-01"
        self.is_active = True
        
        # 保护属性（子类可能需要访问）
        self._email = email
        self._login_attempts = 0
        self._last_login = None
        
        # 私有属性（严格保密）
        self.__password_hash = self.__hash_password(password)
        self.__session_token = None
        self.__security_questions = {}
    
    def __hash_password(self, password):
        """私有方法：密码哈希（简化版）"""
        return f"hashed_{password}_salt"
    
    def __generate_token(self):
        """私有方法：生成会话令牌"""
        import random
        return f"token_{random.randint(1000, 9999)}"
    
    def _validate_password(self, password):
        """保护方法：验证密码"""
        return self.__hash_password(password) == self.__password_hash
    
    def _log_login_attempt(self, success):
        """保护方法：记录登录尝试"""
        if success:
            self._login_attempts = 0
            self._last_login = "2024-01-01 12:00:00"
        else:
            self._login_attempts += 1
    
    # 公有接口
    def login(self, password):
        """用户登录"""
        if self._login_attempts >= 3:
            return {"success": False, "message": "账户已锁定"}
        
        if self._validate_password(password):
            self.__session_token = self.__generate_token()
            self._log_login_attempt(True)
            return {
                "success": True, 
                "message": "登录成功",
                "token": self.__session_token
            }
        else:
            self._log_login_attempt(False)
            return {
                "success": False, 
                "message": f"密码错误，剩余尝试次数: {3 - self._login_attempts}"
            }
    
    def logout(self):
        """用户登出"""
        self.__session_token = None
        return "已安全登出"
    
    def change_password(self, old_password, new_password):
        """修改密码"""
        if not self._validate_password(old_password):
            return "原密码错误"
        
        self.__password_hash = self.__hash_password(new_password)
        self.__session_token = None  # 清除会话
        return "密码修改成功，请重新登录"
    
    def get_public_info(self):
        """获取公开信息"""
        return {
            "username": self.username,
            "created_at": self.created_at,
            "is_active": self.is_active,
            "last_login": self._last_login
        }
    
    def get_email(self):
        """获取邮箱（需要权限）"""
        if self.__session_token:
            return self._email
        return "请先登录"
    
    def __str__(self):
        return f"用户: {self.username} ({'活跃' if self.is_active else '非活跃'})"

# 使用示例
def demonstrate_access_control():
    """演示访问控制"""
    print("=== 用户账户访问控制演示 ===")
    
    # 创建用户账户
    user = UserAccount("alice", "alice@example.com", "password123")
    print(f"创建用户: {user}")
    
    # 公有属性访问
    print(f"\n公有信息: {user.get_public_info()}")
    
    # 登录尝试
    print("\n登录测试:")
    result = user.login("wrong_password")
    print(f"错误密码: {result}")
    
    result = user.login("password123")
    print(f"正确密码: {result}")
    
    # 登录后访问保护信息
    print(f"\n登录后邮箱: {user.get_email()}")
    
    # 修改密码
    print("\n修改密码:")
    result = user.change_password("password123", "new_password456")
    print(result)
    
    # 重新登录
    result = user.login("new_password456")
    print(f"新密码登录: {result}")
    
    # 访问控制测试
    print("\n访问控制测试:")
    print(f"公有属性 username: {user.username}")
    print(f"保护属性 _email: {user._email}")
    
    # 尝试访问私有属性（会失败）
    try:
        print(user.__password_hash)
    except AttributeError:
        print("无法直接访问私有属性 __password_hash")
    
    # 通过名称修饰访问（不推荐）
    print(f"通过名称修饰访问密码哈希: {user._UserAccount__password_hash}")

# 运行演示
demonstrate_access_control()
```

## 继承中的访问控制

```python
class BaseUser:
    """基础用户类"""
    
    def __init__(self, name):
        self.name = name                    # 公有
        self._user_id = id(self)           # 保护
        self.__creation_time = "2024-01-01" # 私有
    
    def _generate_report(self):
        """保护方法 - 子类可以重写"""
        return f"基础报告: {self.name}"
    
    def __internal_log(self, message):
        """私有方法 - 子类无法访问"""
        print(f"[LOG] {message}")
    
    def public_action(self):
        """公有方法"""
        self.__internal_log(f"用户 {self.name} 执行操作")
        return self._generate_report()

class AdminUser(BaseUser):
    """管理员用户类"""
    
    def __init__(self, name, permissions):
        super().__init__(name)
        self._permissions = permissions  # 保护属性
        self.__admin_key = "admin_secret"  # 私有属性
    
    def _generate_report(self):
        """重写保护方法"""
        base_report = super()._generate_report()
        return f"{base_report} + 管理员权限: {self._permissions}"
    
    def admin_action(self):
        """管理员专用操作"""
        # 可以访问父类的保护属性和方法
        print(f"管理员 {self.name} (ID: {self._user_id}) 执行管理操作")
        
        # 无法访问父类的私有属性
        # print(self.__creation_time)  # AttributeError
        
        # 可以通过名称修饰访问（不推荐）
        try:
            print(f"创建时间: {self._BaseUser__creation_time}")
        except AttributeError:
            print("无法访问父类私有属性")
        
        return self._generate_report()

# 继承演示
def demonstrate_inheritance_access():
    """演示继承中的访问控制"""
    print("\n=== 继承中的访问控制演示 ===")
    
    # 基础用户
    user = BaseUser("普通用户")
    print(f"基础用户操作: {user.public_action()}")
    
    # 管理员用户
    admin = AdminUser("管理员", ["读取", "写入", "删除"])
    print(f"\n管理员操作: {admin.public_action()}")
    print(f"管理员专用: {admin.admin_action()}")
    
    # 访问测试
    print(f"\n访问测试:")
    print(f"公有属性 - 用户名: {admin.name}")
    print(f"保护属性 - 用户ID: {admin._user_id}")
    print(f"保护属性 - 权限: {admin._permissions}")

# 运行演示
demonstrate_inheritance_access()
```

## 学习要点

### Python访问控制特点

1. **约定优于强制**：Python依赖命名约定而非语法强制
2. **灵活性**：技术上可以访问所有属性，但应遵循约定
3. **名称修饰**：双下划线属性会被自动重命名
4. **继承影响**：不同访问级别在继承中的表现不同

### 访问控制最佳实践

1. **公有属性**：
   - 用于外部需要直接访问的数据
   - 提供稳定的接口
   - 考虑数据验证

2. **保护属性**：
   - 用于子类可能需要的内部数据
   - 表示"内部使用，但不完全私有"
   - 在继承设计中很有用

3. **私有属性**：
   - 用于严格的内部实现细节
   - 防止意外的外部访问
   - 在类的重构中提供更多自由

### 设计建议

- **最小暴露原则**：只暴露必要的接口
- **一致性**：在整个项目中保持一致的命名约定
- **文档化**：清楚地文档化公有接口
- **渐进式封装**：从公有开始，根据需要增加封装

访问控制是封装的重要组成部分，正确使用可以提高代码的安全性和可维护性。