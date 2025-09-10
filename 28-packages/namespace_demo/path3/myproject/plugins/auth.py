"""认证插件 - 来自path3"""

class AuthPlugin:
    """认证插件类"""
    
    def __init__(self):
        self.name = "AuthPlugin"
        self.version = "1.0.0"
        self.source = "path3"
        self.users = {}
        print(f"加载认证插件 (来自 {self.source})")
    
    def register(self, username, password):
        """注册用户"""
        if username not in self.users:
            self.users[username] = password
            print(f"用户 {username} 注册成功")
            return True
        else:
            print(f"用户 {username} 已存在")
            return False
    
    def login(self, username, password):
        """用户登录"""
        if username in self.users and self.users[username] == password:
            print(f"用户 {username} 登录成功")
            return True
        else:
            print(f"用户 {username} 登录失败")
            return False
    
    def get_info(self):
        """获取插件信息"""
        return {
            "name": self.name,
            "version": self.version,
            "source": self.source,
            "users_count": len(self.users)
        }

print(f"认证插件已加载 (来自 path3)")
