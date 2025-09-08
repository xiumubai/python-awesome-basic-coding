# 条件语句中的逻辑运算符

## 概述

逻辑运算符是条件语句中的重要组成部分，它们允许我们组合多个条件表达式，创建更复杂和精确的判断逻辑。Python提供了三个主要的逻辑运算符：`and`、`or`和`not`。掌握这些运算符的使用方法和特性，能够让我们编写更加灵活和强大的条件判断代码。

## 基本逻辑运算符

### 1. and 运算符

`and`运算符要求所有条件都为True时，整个表达式才为True。

```python
# and 运算符基础示例
age = 25
income = 50000
has_job = True

print("=== and 运算符示例 ===")

# 基本用法
if age >= 18 and income >= 30000:
    print("✅ 符合贷款基本条件")
else:
    print("❌ 不符合贷款基本条件")

# 多个条件组合
if age >= 18 and income >= 30000 and has_job:
    print("✅ 符合所有贷款条件")
else:
    print("❌ 不符合所有贷款条件")

# 复杂条件组合
if (age >= 18 and age <= 65) and (income >= 30000 and income <= 200000):
    print("✅ 年龄和收入都在合理范围内")

# 字符串条件
username = "admin"
password = "secure123"
if username == "admin" and password == "secure123":
    print("✅ 登录成功")
else:
    print("❌ 用户名或密码错误")
```

### 2. or 运算符

`or`运算符只要有一个条件为True，整个表达式就为True。

```python
# or 运算符基础示例
weather = "sunny"
temperature = 22
is_weekend = True

print("\n=== or 运算符示例 ===")

# 基本用法
if weather == "sunny" or temperature > 20:
    print("✅ 适合外出")
else:
    print("❌ 不适合外出")

# 多个条件选择
if is_weekend or weather == "sunny" or temperature > 25:
    print("✅ 今天是个好日子")

# 用户权限检查
user_role = "editor"
user_id = 123
if user_role == "admin" or user_role == "editor" or user_id == 1:
    print("✅ 有编辑权限")
else:
    print("❌ 无编辑权限")

# 输入验证
user_input = "yes"
if user_input == "yes" or user_input == "y" or user_input == "YES":
    print("✅ 用户确认")
else:
    print("❌ 用户取消")
```

### 3. not 运算符

`not`运算符用于取反，将True变为False，False变为True。

```python
# not 运算符基础示例
is_logged_in = False
is_banned = False
is_maintenance = False

print("\n=== not 运算符示例 ===")

# 基本用法
if not is_logged_in:
    print("❌ 用户未登录")
else:
    print("✅ 用户已登录")

# 与其他运算符组合
if not is_banned and not is_maintenance:
    print("✅ 系统正常，用户可以访问")
else:
    print("❌ 系统维护中或用户被禁用")

# 复杂条件
if not (is_banned or is_maintenance):
    print("✅ 使用括号简化复杂条件")

# 列表和字符串的not用法
user_list = []
user_name = ""

if not user_list:
    print("📝 用户列表为空")

if not user_name:
    print("📝 用户名为空")

if not user_name.strip():  # 检查是否只包含空白字符
    print("📝 用户名只包含空白字符")
```

## 逻辑运算符的组合使用

### 1. 复杂条件组合

```python
# 复杂的逻辑组合示例
age = 28
income = 75000
credit_score = 720
has_collateral = True
is_first_time = False
employment_years = 3

print("\n=== 复杂逻辑组合示例 ===")

# 贷款审批复杂逻辑
if (age >= 18 and age <= 65) and (income >= 50000 or has_collateral) and not (credit_score < 650):
    print("✅ 通过初步审核")
    
    # 进一步细化条件
    if (credit_score >= 700 and employment_years >= 2) or (has_collateral and income >= 60000):
        print("✅ 获得优惠利率")
        
        # 首次购房者额外优惠
        if is_first_time and (age <= 35 or income >= 80000):
            print("🎉 首次购房者特别优惠")
    else:
        print("⚠️ 标准利率")
else:
    print("❌ 未通过初步审核")

# 用户权限复杂验证
user_role = "manager"
department = "sales"
is_active = True
last_login_days = 5
has_2fa = True

if (user_role == "admin" or (user_role == "manager" and department in ["sales", "marketing"])) and is_active and not (last_login_days > 30):
    print("\n✅ 基础权限验证通过")
    
    if has_2fa or user_role == "admin":
        print("✅ 安全验证通过")
        print("🔓 允许访问敏感数据")
    else:
        print("⚠️ 建议启用双因素认证")
        print("🔒 限制访问敏感数据")
else:
    print("\n❌ 权限验证失败")
```

### 2. 短路求值（Short-circuit Evaluation）

```python
# 短路求值示例
print("\n=== 短路求值示例 ===")

def expensive_operation():
    """模拟耗时操作"""
    print("执行了耗时操作")
    return True

def quick_check():
    """模拟快速检查"""
    print("执行了快速检查")
    return False

# and 短路：如果第一个条件为False，不会执行第二个条件
print("\nand 短路测试：")
if quick_check() and expensive_operation():
    print("两个条件都为True")
else:
    print("至少有一个条件为False")

# or 短路：如果第一个条件为True，不会执行第二个条件
print("\nor 短路测试：")
if True or expensive_operation():
    print("至少有一个条件为True")

# 实际应用：安全的属性访问
user_data = None

# 错误的做法（会报错）
# if user_data.get('name') == 'admin':  # AttributeError

# 正确的做法（利用短路求值）
if user_data and user_data.get('name') == 'admin':
    print("管理员用户")
else:
    print("非管理员用户或用户数据为空")

# 列表安全访问
my_list = []
if my_list and my_list[0] > 10:  # 安全访问列表第一个元素
    print("第一个元素大于10")
else:
    print("列表为空或第一个元素不大于10")
```

### 3. 运算符优先级

```python
# 运算符优先级示例
print("\n=== 运算符优先级示例 ===")

a = True
b = False
c = True

# 优先级：not > and > or
result1 = a or b and c  # 等价于 a or (b and c)
result2 = (a or b) and c

print(f"a or b and c = {result1}")  # True
print(f"(a or b) and c = {result2}")  # True

# 复杂表达式
x = 5
y = 10
z = 15

# 不使用括号（依赖优先级）
result3 = x > 3 and y < 20 or z == 15
print(f"x > 3 and y < 20 or z == 15 = {result3}")

# 使用括号（更清晰）
result4 = (x > 3 and y < 20) or (z == 15)
print(f"(x > 3 and y < 20) or (z == 15) = {result4}")

# 建议：复杂表达式总是使用括号
age = 25
income = 60000
experience = 3

# 不清晰的表达式
if age >= 18 and income >= 50000 or experience >= 5 and age <= 65:
    print("条件1满足")

# 清晰的表达式
if (age >= 18 and income >= 50000) or (experience >= 5 and age <= 65):
    print("条件2满足")
```

## 实际应用场景

### 1. 用户权限验证系统

```python
# 完整的用户权限验证系统
class UserPermissionSystem:
    def __init__(self):
        self.users = {
            'admin': {
                'role': 'administrator',
                'department': 'IT',
                'is_active': True,
                'permissions': ['read', 'write', 'delete', 'admin'],
                'last_login': 1,
                'has_2fa': True
            },
            'manager': {
                'role': 'manager',
                'department': 'sales',
                'is_active': True,
                'permissions': ['read', 'write'],
                'last_login': 3,
                'has_2fa': False
            },
            'employee': {
                'role': 'employee',
                'department': 'sales',
                'is_active': True,
                'permissions': ['read'],
                'last_login': 7,
                'has_2fa': False
            },
            'intern': {
                'role': 'intern',
                'department': 'marketing',
                'is_active': False,
                'permissions': ['read'],
                'last_login': 45,
                'has_2fa': False
            }
        }
    
    def check_basic_access(self, username):
        """检查基础访问权限"""
        if username not in self.users:
            return False, "用户不存在"
        
        user = self.users[username]
        
        # 基础条件：用户激活且最近登录过
        if user['is_active'] and user['last_login'] <= 30:
            return True, "基础访问权限通过"
        else:
            return False, "用户未激活或长时间未登录"
    
    def check_data_access(self, username, data_type):
        """检查数据访问权限"""
        basic_ok, basic_msg = self.check_basic_access(username)
        if not basic_ok:
            return False, basic_msg
        
        user = self.users[username]
        
        # 数据访问逻辑
        if data_type == "public":
            # 公开数据：所有激活用户都可以访问
            return True, "公开数据访问权限通过"
        
        elif data_type == "internal":
            # 内部数据：员工级别以上且有读权限
            if (user['role'] in ['employee', 'manager', 'administrator'] and 
                'read' in user['permissions']):
                return True, "内部数据访问权限通过"
            else:
                return False, "权限不足，无法访问内部数据"
        
        elif data_type == "confidential":
            # 机密数据：管理层且有写权限，或管理员
            if (user['role'] == 'administrator' or 
                (user['role'] == 'manager' and 'write' in user['permissions'])):
                return True, "机密数据访问权限通过"
            else:
                return False, "权限不足，无法访问机密数据"
        
        elif data_type == "sensitive":
            # 敏感数据：需要双因素认证且是管理员或高级管理者
            if ((user['role'] == 'administrator' and user['has_2fa']) or 
                (user['role'] == 'manager' and user['has_2fa'] and 
                 user['department'] in ['IT', 'finance'])):
                return True, "敏感数据访问权限通过"
            else:
                return False, "需要双因素认证或更高权限"
        
        return False, "未知数据类型"
    
    def check_operation_permission(self, username, operation, target_department=None):
        """检查操作权限"""
        basic_ok, basic_msg = self.check_basic_access(username)
        if not basic_ok:
            return False, basic_msg
        
        user = self.users[username]
        
        if operation == "read":
            # 读操作：基础权限即可
            return True, "读操作权限通过"
        
        elif operation == "write":
            # 写操作：需要写权限且最近活跃
            if ('write' in user['permissions'] and user['last_login'] <= 7):
                return True, "写操作权限通过"
            else:
                return False, "需要写权限且最近需要活跃"
        
        elif operation == "delete":
            # 删除操作：需要删除权限且双因素认证
            if ('delete' in user['permissions'] and user['has_2fa']):
                return True, "删除操作权限通过"
            else:
                return False, "需要删除权限和双因素认证"
        
        elif operation == "cross_department":
            # 跨部门操作：管理员或同部门管理者
            if (user['role'] == 'administrator' or 
                (user['role'] == 'manager' and 
                 (target_department is None or user['department'] == target_department))):
                return True, "跨部门操作权限通过"
            else:
                return False, "需要管理员权限或同部门管理权限"
        
        return False, "未知操作类型"

# 测试权限系统
print("\n=== 用户权限验证系统测试 ===")
perm_system = UserPermissionSystem()

# 测试不同用户的权限
test_users = ['admin', 'manager', 'employee', 'intern']
test_data_types = ['public', 'internal', 'confidential', 'sensitive']
test_operations = ['read', 'write', 'delete', 'cross_department']

for username in test_users:
    print(f"\n--- {username} 权限测试 ---")
    
    # 测试数据访问
    for data_type in test_data_types:
        ok, msg = perm_system.check_data_access(username, data_type)
        status = "✅" if ok else "❌"
        print(f"{status} {data_type}: {msg}")
    
    # 测试操作权限
    for operation in test_operations:
        ok, msg = perm_system.check_operation_permission(username, operation)
        status = "✅" if ok else "❌"
        print(f"{status} {operation}: {msg}")
```

### 2. 表单验证系统

```python
# 复杂表单验证系统
class FormValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        """邮箱验证"""
        if not email:
            return False, "邮箱不能为空"
        
        if not ("@" in email and "." in email and 
                len(email) >= 5 and len(email) <= 100):
            return False, "邮箱格式不正确"
        
        # 简单的邮箱格式检查
        parts = email.split("@")
        if not (len(parts) == 2 and len(parts[0]) >= 1 and len(parts[1]) >= 3):
            return False, "邮箱格式不正确"
        
        return True, "邮箱格式正确"
    
    def validate_password(self, password):
        """密码强度验证"""
        if not password:
            return False, "密码不能为空"
        
        # 密码长度检查
        if not (8 <= len(password) <= 50):
            return False, "密码长度必须在8-50个字符之间"
        
        # 密码复杂度检查
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        complexity_count = sum([has_upper, has_lower, has_digit, has_special])
        
        if not (complexity_count >= 3):
            return False, "密码必须包含大写字母、小写字母、数字、特殊字符中的至少3种"
        
        # 检查常见弱密码
        weak_passwords = ['password', '123456', 'qwerty', 'admin']
        if password.lower() in weak_passwords:
            return False, "不能使用常见弱密码"
        
        return True, "密码强度符合要求"
    
    def validate_phone(self, phone):
        """手机号验证"""
        if not phone:
            return False, "手机号不能为空"
        
        # 移除所有非数字字符
        digits_only = ''.join(filter(str.isdigit, phone))
        
        # 中国手机号验证
        if not (len(digits_only) == 11 and digits_only.startswith('1')):
            return False, "手机号格式不正确"
        
        # 检查第二位数字（运营商号段）
        if not digits_only[1] in '3456789':
            return False, "手机号号段不正确"
        
        return True, "手机号格式正确"
    
    def validate_age(self, age_str, min_age=0, max_age=150):
        """年龄验证"""
        if not age_str:
            return False, "年龄不能为空"
        
        try:
            age = int(age_str)
        except ValueError:
            return False, "年龄必须是数字"
        
        if not (min_age <= age <= max_age):
            return False, f"年龄必须在{min_age}-{max_age}岁之间"
        
        return True, "年龄格式正确"
    
    def validate_registration_form(self, form_data):
        """注册表单综合验证"""
        self.errors = []
        is_valid = True
        
        # 基础字段验证
        email_ok, email_msg = self.validate_email(form_data.get('email', ''))
        if not email_ok:
            self.errors.append(f"邮箱: {email_msg}")
            is_valid = False
        
        password_ok, password_msg = self.validate_password(form_data.get('password', ''))
        if not password_ok:
            self.errors.append(f"密码: {password_msg}")
            is_valid = False
        
        phone_ok, phone_msg = self.validate_phone(form_data.get('phone', ''))
        if not phone_ok:
            self.errors.append(f"手机号: {phone_msg}")
            is_valid = False
        
        age_ok, age_msg = self.validate_age(form_data.get('age', ''), 13, 100)
        if not age_ok:
            self.errors.append(f"年龄: {age_msg}")
            is_valid = False
        
        # 密码确认验证
        password = form_data.get('password', '')
        confirm_password = form_data.get('confirm_password', '')
        if password and confirm_password and password != confirm_password:
            self.errors.append("密码: 两次输入的密码不一致")
            is_valid = False
        
        # 服务条款同意验证
        agree_terms = form_data.get('agree_terms', False)
        if not agree_terms:
            self.errors.append("服务条款: 必须同意服务条款")
            is_valid = False
        
        # 年龄相关的额外验证
        if age_ok:
            age = int(form_data.get('age', '0'))
            parent_consent = form_data.get('parent_consent', False)
            
            # 未成年人需要监护人同意
            if age < 18 and not parent_consent:
                self.errors.append("监护人同意: 未成年人注册需要监护人同意")
                is_valid = False
            
            # 老年人特殊提醒
            if age >= 70:
                emergency_contact = form_data.get('emergency_contact', '')
                if not emergency_contact:
                    self.errors.append("紧急联系人: 建议填写紧急联系人信息")
                    # 这里不设为无效，只是警告
        
        # 营销邮件订阅逻辑验证
        subscribe_marketing = form_data.get('subscribe_marketing', False)
        marketing_frequency = form_data.get('marketing_frequency', '')
        
        if subscribe_marketing and not marketing_frequency:
            self.errors.append("营销邮件: 订阅营销邮件需要选择接收频率")
            is_valid = False
        
        return is_valid, self.errors

# 测试表单验证
print("\n=== 表单验证系统测试 ===")
validator = FormValidator()

# 测试数据
test_forms = [
    {
        'name': '有效表单',
        'data': {
            'email': 'user@example.com',
            'password': 'SecurePass123!',
            'confirm_password': 'SecurePass123!',
            'phone': '13812345678',
            'age': '25',
            'agree_terms': True,
            'parent_consent': False,
            'subscribe_marketing': True,
            'marketing_frequency': 'weekly'
        }
    },
    {
        'name': '无效表单',
        'data': {
            'email': 'invalid-email',
            'password': '123',
            'confirm_password': '456',
            'phone': '123',
            'age': '200',
            'agree_terms': False,
            'parent_consent': False,
            'subscribe_marketing': True,
            'marketing_frequency': ''
        }
    },
    {
        'name': '未成年人表单',
        'data': {
            'email': 'teen@example.com',
            'password': 'TeenPass123!',
            'confirm_password': 'TeenPass123!',
            'phone': '13987654321',
            'age': '16',
            'agree_terms': True,
            'parent_consent': True,
            'subscribe_marketing': False
        }
    }
]

for test_form in test_forms:
    print(f"\n--- {test_form['name']} ---")
    is_valid, errors = validator.validate_registration_form(test_form['data'])
    
    if is_valid:
        print("✅ 表单验证通过")
    else:
        print("❌ 表单验证失败")
        for error in errors:
            print(f"  • {error}")
```

### 3. 游戏角色状态判断

```python
# 游戏角色状态管理系统
class GameCharacter:
    def __init__(self, name, level=1, hp=100, mp=50, stamina=100):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.stamina = stamina
        self.max_stamina = stamina
        self.status_effects = set()
        self.equipment = {
            'weapon': None,
            'armor': None,
            'accessory': None
        }
        self.skills = set()
    
    def add_status_effect(self, effect):
        """添加状态效果"""
        self.status_effects.add(effect)
    
    def remove_status_effect(self, effect):
        """移除状态效果"""
        self.status_effects.discard(effect)
    
    def equip_item(self, item_type, item_name):
        """装备物品"""
        self.equipment[item_type] = item_name
    
    def learn_skill(self, skill_name):
        """学习技能"""
        self.skills.add(skill_name)
    
    def can_use_skill(self, skill_name, required_mp=20, required_stamina=10):
        """检查是否可以使用技能"""
        # 基础条件检查
        if not (skill_name in self.skills):
            return False, "未学会该技能"
        
        if self.hp <= 0:
            return False, "角色已死亡"
        
        # 资源检查
        if not (self.mp >= required_mp and self.stamina >= required_stamina):
            return False, "MP或体力不足"
        
        # 状态效果检查
        if 'silenced' in self.status_effects and skill_name in ['fireball', 'heal', 'lightning']:
            return False, "沉默状态无法使用魔法技能"
        
        if 'paralyzed' in self.status_effects:
            return False, "麻痹状态无法行动"
        
        if 'confused' in self.status_effects and skill_name in ['attack', 'defend']:
            return False, "混乱状态无法使用基础技能"
        
        return True, "可以使用技能"
    
    def can_enter_battle(self):
        """检查是否可以进入战斗"""
        # 基础生命值检查
        if self.hp <= 0:
            return False, "角色已死亡，无法战斗"
        
        # 严重状态检查
        if 'petrified' in self.status_effects:
            return False, "石化状态无法战斗"
        
        if 'sleeping' in self.status_effects:
            return False, "睡眠状态无法战斗"
        
        # 装备检查
        if not self.equipment['weapon']:
            return False, "未装备武器，建议装备后再战斗"
        
        # 等级和状态综合判断
        if self.level < 5 and self.hp < self.max_hp * 0.3:
            return False, "等级过低且生命值不足，不建议战斗"
        
        return True, "可以进入战斗"
    
    def can_use_item(self, item_type):
        """检查是否可以使用物品"""
        # 基础状态检查
        if self.hp <= 0:
            return False, "角色已死亡"
        
        # 特殊状态检查
        if item_type == 'potion':
            if 'poisoned' in self.status_effects and 'cursed' in self.status_effects:
                return False, "中毒且被诅咒状态下药水效果减半，不建议使用"
            
            if self.hp == self.max_hp and item_type == 'health_potion':
                return False, "生命值已满，无需使用生命药水"
        
        elif item_type == 'scroll':
            if 'silenced' in self.status_effects:
                return False, "沉默状态无法使用魔法卷轴"
        
        elif item_type == 'food':
            if 'nausea' in self.status_effects:
                return False, "恶心状态无法进食"
        
        return True, "可以使用物品"
    
    def get_combat_effectiveness(self):
        """计算战斗力"""
        base_power = self.level * 10
        
        # 生命值影响
        hp_ratio = self.hp / self.max_hp
        if hp_ratio >= 0.8:
            hp_bonus = 1.2
        elif hp_ratio >= 0.5:
            hp_bonus = 1.0
        elif hp_ratio >= 0.2:
            hp_bonus = 0.7
        else:
            hp_bonus = 0.3
        
        # 装备加成
        equipment_bonus = 1.0
        if self.equipment['weapon']:
            equipment_bonus += 0.3
        if self.equipment['armor']:
            equipment_bonus += 0.2
        if self.equipment['accessory']:
            equipment_bonus += 0.1
        
        # 状态效果影响
        status_modifier = 1.0
        if 'blessed' in self.status_effects:
            status_modifier += 0.2
        if 'cursed' in self.status_effects:
            status_modifier -= 0.3
        if 'weakened' in self.status_effects:
            status_modifier -= 0.2
        if 'strengthened' in self.status_effects:
            status_modifier += 0.3
        
        # 技能加成
        skill_bonus = 1.0 + len(self.skills) * 0.05
        
        final_power = base_power * hp_bonus * equipment_bonus * status_modifier * skill_bonus
        return max(1, int(final_power))
    
    def get_status_summary(self):
        """获取角色状态摘要"""
        summary = {
            'name': self.name,
            'level': self.level,
            'hp': f"{self.hp}/{self.max_hp}",
            'mp': f"{self.mp}/{self.max_mp}",
            'stamina': f"{self.stamina}/{self.max_stamina}",
            'status_effects': list(self.status_effects),
            'equipment': self.equipment,
            'skills': list(self.skills),
            'combat_power': self.get_combat_effectiveness()
        }
        return summary

# 测试游戏角色系统
print("\n=== 游戏角色状态系统测试 ===")

# 创建测试角色
hero = GameCharacter("勇者", level=10, hp=150, mp=80, stamina=120)
hero.learn_skill("fireball")
hero.learn_skill("heal")
hero.learn_skill("attack")
hero.equip_item("weapon", "魔法剑")
hero.equip_item("armor", "龙鳞甲")

print(f"角色创建完成: {hero.name}")
print(f"战斗力: {hero.get_combat_effectiveness()}")

# 测试不同状态下的能力
test_scenarios = [
    {
        'name': '正常状态',
        'hp': 150,
        'mp': 80,
        'stamina': 120,
        'effects': []
    },
    {
        'name': '重伤状态',
        'hp': 30,
        'mp': 80,
        'stamina': 120,
        'effects': ['bleeding']
    },
    {
        'name': '沉默状态',
        'hp': 150,
        'mp': 80,
        'stamina': 120,
        'effects': ['silenced']
    },
    {
        'name': '麻痹状态',
        'hp': 150,
        'mp': 80,
        'stamina': 120,
        'effects': ['paralyzed']
    },
    {
        'name': '增益状态',
        'hp': 150,
        'mp': 80,
        'stamina': 120,
        'effects': ['blessed', 'strengthened']
    },
    {
        'name': '复合负面状态',
        'hp': 50,
        'mp': 20,
        'stamina': 30,
        'effects': ['cursed', 'weakened', 'poisoned']
    }
]

for scenario in test_scenarios:
    print(f"\n--- {scenario['name']} ---")
    
    # 设置角色状态
    hero.hp = scenario['hp']
    hero.mp = scenario['mp']
    hero.stamina = scenario['stamina']
    hero.status_effects = set(scenario['effects'])
    
    print(f"HP: {hero.hp}/{hero.max_hp}, MP: {hero.mp}/{hero.max_mp}, 体力: {hero.stamina}/{hero.max_stamina}")
    print(f"状态效果: {list(hero.status_effects) if hero.status_effects else '无'}")
    print(f"当前战斗力: {hero.get_combat_effectiveness()}")
    
    # 测试各种能力
    can_battle, battle_msg = hero.can_enter_battle()
    print(f"进入战斗: {'✅' if can_battle else '❌'} {battle_msg}")
    
    can_fireball, fireball_msg = hero.can_use_skill("fireball", 25, 15)
    print(f"使用火球术: {'✅' if can_fireball else '❌'} {fireball_msg}")
    
    can_heal, heal_msg = hero.can_use_skill("heal", 30, 10)
    print(f"使用治疗术: {'✅' if can_heal else '❌'} {heal_msg}")
    
    can_potion, potion_msg = hero.can_use_item("health_potion")
    print(f"使用生命药水: {'✅' if can_potion else '❌'} {potion_msg}")
    
    can_scroll, scroll_msg = hero.can_use_item("scroll")
    print(f"使用魔法卷轴: {'✅' if can_scroll else '❌'} {scroll_msg}")
```

## 性能优化技巧

### 1. 条件顺序优化

```python
# 条件顺序优化示例
import time

def expensive_check():
    """模拟耗时检查"""
    time.sleep(0.001)  # 模拟1毫秒延迟
    return True

def quick_check():
    """模拟快速检查"""
    return False

# 不好的做法：耗时操作在前
start_time = time.time()
for i in range(1000):
    if expensive_check() and quick_check():
        pass
bad_time = time.time() - start_time

# 好的做法：快速检查在前（利用短路求值）
start_time = time.time()
for i in range(1000):
    if quick_check() and expensive_check():
        pass
good_time = time.time() - start_time

print(f"\n=== 条件顺序优化 ===")
print(f"耗时操作在前: {bad_time:.3f}秒")
print(f"快速检查在前: {good_time:.3f}秒")
print(f"性能提升: {(bad_time/good_time):.1f}倍")
```

### 2. 避免重复计算

```python
# 避免重复计算示例
def calculate_score(data):
    """模拟复杂计算"""
    return sum(data) * len(data) / max(data)

data = [1, 2, 3, 4, 5] * 100

# 不好的做法：重复计算
if calculate_score(data) > 100 and calculate_score(data) < 1000:
    result1 = calculate_score(data) * 2
else:
    result1 = 0

# 好的做法：计算一次，存储结果
score = calculate_score(data)
if score > 100 and score < 1000:
    result2 = score * 2
else:
    result2 = 0

print(f"\n=== 避免重复计算 ===")
print(f"结果相同: {result1 == result2}")
print("优化后避免了重复的复杂计算")
```

## 常见错误和调试

### 1. 逻辑运算符优先级错误

```python
# 常见的优先级错误
print("\n=== 逻辑运算符优先级错误 ===")

a, b, c = True, False, True

# 错误理解：以为是 (a or b) and c
result1 = a or b and c
print(f"a or b and c = {result1}")  # True

# 实际执行：a or (b and c)
result2 = a or (b and c)
print(f"a or (b and c) = {result2}")  # True

# 期望的逻辑：(a or b) and c
result3 = (a or b) and c
print(f"(a or b) and c = {result3}")  # True

# 当a为False时的区别
a = False
result1 = a or b and c  # False or (False and True) = False
result3 = (a or b) and c  # (False or False) and True = False

print(f"\n当a=False时:")
print(f"a or b and c = {result1}")  # False
print(f"(a or b) and c = {result3}")  # False
```

### 2. 短路求值的意外行为

```python
# 短路求值的意外行为
print("\n=== 短路求值意外行为 ===")

counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"计数器增加到: {counter}")
    return True

# 期望两个函数都被调用
print("测试 True or increment_counter():")
result = True or increment_counter()  # increment_counter不会被调用
print(f"结果: {result}, 计数器: {counter}")

# 重置计数器
counter = 0
print("\n测试 False or increment_counter():")
result = False or increment_counter()  # increment_counter会被调用
print(f"结果: {result}, 计数器: {counter}")

# 如果需要确保所有函数都被调用
counter = 0
print("\n确保所有函数都被调用:")
func1_result = increment_counter()
func2_result = increment_counter()
result = func1_result or func2_result
print(f"结果: {result}, 计数器: {counter}")
```

### 3. 调试复杂逻辑表达式

```python
# 调试复杂逻辑表达式
def debug_complex_condition(user_age, user_income, user_score, has_collateral, is_first_time):
    """调试复杂条件的示例"""
    print(f"\n=== 调试复杂条件 ===")
    print(f"输入参数:")
    print(f"  年龄: {user_age}")
    print(f"  收入: {user_income}")
    print(f"  信用分: {user_score}")
    print(f"  有抵押: {has_collateral}")
    print(f"  首次购房: {is_first_time}")
    
    # 分步骤调试复杂条件
    age_ok = 18 <= user_age <= 65
    print(f"\n条件分解:")
    print(f"  年龄符合 (18-65): {age_ok}")
    
    income_ok = user_income >= 50000
    print(f"  收入符合 (>=50000): {income_ok}")
    
    score_ok = user_score >= 650
    print(f"  信用分符合 (>=650): {score_ok}")
    
    collateral_bonus = has_collateral and user_income >= 40000
    print(f"  抵押加分 (有抵押且收入>=40000): {collateral_bonus}")
    
    first_time_bonus = is_first_time and user_age <= 35
    print(f"  首次购房加分 (首次且年龄<=35): {first_time_bonus}")
    
    # 组合条件
    basic_condition = age_ok and (income_ok or collateral_bonus)
    print(f"\n基础条件 (年龄OK且(收入OK或抵押加分)): {basic_condition}")
    
    credit_condition = score_ok or (has_collateral and user_score >= 600)
    print(f"信用条件 (信用分OK或(有抵押且分数>=600)): {credit_condition}")
    
    final_result = basic_condition and credit_condition
    print(f"\n最终结果: {final_result}")
    
    # 给出具体的改进建议
    if not final_result:
        print("\n改进建议:")
        if not age_ok:
            print("  - 年龄不符合要求")
        if not income_ok and not collateral_bonus:
            print("  - 提高收入至50000以上，或提供抵押物")
        if not credit_condition:
            if not score_ok:
                print("  - 提高信用分至650以上")
            if not has_collateral:
                print("  - 考虑提供抵押物")
    
    return final_result

# 测试调试函数
test_cases = [
    (30, 60000, 700, False, True),   # 应该通过
    (25, 40000, 620, True, True),    # 应该通过（抵押加分）
    (70, 80000, 750, False, False),  # 年龄不符合
    (30, 30000, 600, False, True),   # 收入和信用分都不够
]

for i, test_case in enumerate(test_cases, 1):
    print(f"\n{'='*50}")
    print(f"测试案例 {i}")
    result = debug_complex_condition(*test_case)
    print(f"最终审批结果: {'✅ 通过' if result else '❌ 拒绝'}")
```

## 练习题

### 基础练习

1. **用户登录验证**：
   - 实现用户名、密码、验证码的综合验证
   - 考虑账户锁定、密码过期等情况

2. **商品折扣计算**：
   - 根据会员等级、购买金额、商品类别计算折扣
   - 实现复杂的优惠叠加逻辑

3. **学生成绩评定**：
   - 综合考试成绩、作业完成情况、出勤率
   - 给出详细的评级和建议

### 进阶练习

1. **智能推荐系统**：
   - 根据用户历史、偏好、当前行为推荐内容
   - 实现多维度的推荐逻辑

2. **风险评估系统**：
   - 评估贷款、投资等金融产品的风险
   - 考虑多种风险因素的组合

3. **游戏平衡系统**：
   - 根据玩家等级、装备、技能调整游戏难度
   - 实现动态平衡算法

### 挑战练习

1. **智能交通控制**：
   - 根据车流量、天气、时间等因素控制交通信号
   - 优化交通流量和安全性

2. **医疗诊断辅助**：
   - 根据症状、检查结果、病史给出诊断建议
   - 实现多层次的诊断逻辑

## 学习要点

1. **运算符理解**：深入理解and、or、not的工作原理
2. **短路求值**：掌握短路求值的特性和应用
3. **优先级规则**：熟记运算符优先级，合理使用括号
4. **性能优化**：学会优化条件判断的性能
5. **调试技巧**：掌握调试复杂逻辑表达式的方法
6. **实际应用**：能够将逻辑运算符应用到实际项目中

通过掌握逻辑运算符在条件语句中的使用，你可以构建更加复杂和精确的判断逻辑。接下来学习比较运算符，进一步完善条件判断的工具箱。