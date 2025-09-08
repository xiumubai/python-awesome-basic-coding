# 变量和数据类型综合练习

## 学习目标

通过这些综合练习，你将：
- 巩固变量定义和数据类型的知识
- 掌握类型转换和验证的实际应用
- 学会处理复杂的数据结构
- 提高代码的健壮性和可维护性
- 了解实际项目中的应用场景

## 基础练习

### 练习1：变量定义和基本操作

**任务**：定义不同类型的变量并进行基本操作

```python
# 定义各种类型的变量
name = "Alice"           # 字符串
age = 25                 # 整数
height = 1.68           # 浮点数
is_student = True       # 布尔值
hobbies = ["reading", "swimming", "coding"]  # 列表

# 输出变量信息
print(f"姓名：{name} (类型：{type(name).__name__})")
print(f"年龄：{age} (类型：{type(age).__name__})")
print(f"身高：{height} (类型：{type(height).__name__})")
print(f"是否学生：{is_student} (类型：{type(is_student).__name__})")
print(f"爱好：{hobbies} (类型：{type(hobbies).__name__})")
```

### 练习2：数据类型识别

**任务**：创建一个函数来识别和分析数据类型

```python
def analyze_data_type(data):
    """分析数据类型并提供详细信息"""
    data_type = type(data).__name__
    
    print(f"值：{data}")
    print(f"类型：{data_type}")
    
    # 根据类型提供额外信息
    if isinstance(data, str):
        print(f"长度：{len(data)}")
        print(f"是否为数字：{data.isdigit()}")
    elif isinstance(data, (int, float)):
        print(f"是否为正数：{data > 0}")
        print(f"绝对值：{abs(data)}")
    elif isinstance(data, list):
        print(f"元素个数：{len(data)}")
        print(f"是否为空：{len(data) == 0}")
    elif isinstance(data, bool):
        print(f"逻辑值：{'真' if data else '假'}")
    
    print("-" * 30)

# 测试不同类型的数据
test_data = ["Hello", 42, 3.14, True, [], [1, 2, 3], "", 0, -5]
for item in test_data:
    analyze_data_type(item)
```

### 练习3：变量重新赋值和类型变化

**任务**：演示Python动态类型的特性

```python
# 创建一个变量并多次重新赋值
variable = "开始是字符串"
print(f"初始值：{variable} (类型：{type(variable).__name__})")

variable = 100
print(f"重新赋值：{variable} (类型：{type(variable).__name__})")

variable = 3.14
print(f"再次赋值：{variable} (类型：{type(variable).__name__})")

variable = [1, 2, 3]
print(f"最后赋值：{variable} (类型：{type(variable).__name__})")

# 演示类型变化对操作的影响
def demonstrate_type_effects():
    """演示类型变化对操作的影响"""
    x = "5"
    y = "3"
    print(f"字符串相加：{x} + {y} = {x + y}")
    
    x = int(x)
    y = int(y)
    print(f"整数相加：{x} + {y} = {x + y}")
    
    x = float(x)
    y = float(y)
    print(f"浮点数相加：{x} + {y} = {x + y}")

demonstrate_type_effects()
```

### 练习4：类型转换练习

**任务**：实现安全的类型转换函数

```python
def safe_convert(value, target_type):
    """安全的类型转换函数"""
    try:
        if target_type == 'int':
            result = int(value)
        elif target_type == 'float':
            result = float(value)
        elif target_type == 'str':
            result = str(value)
        elif target_type == 'bool':
            if isinstance(value, str):
                result = value.lower() in ['true', '1', 'yes']
            else:
                result = bool(value)
        else:
            return None, f"不支持的目标类型：{target_type}"
        
        return result, "转换成功"
    
    except ValueError as e:
        return None, f"转换失败：{e}"

# 测试类型转换
test_cases = [
    ("123", "int"),
    ("3.14", "float"),
    (42, "str"),
    ("true", "bool"),
    ("abc", "int"),  # 这个会失败
    (0, "bool"),
]

for value, target in test_cases:
    result, message = safe_convert(value, target)
    print(f"{value} -> {target}: {result} ({message})")
```

### 练习5：变量命名规范检查

**任务**：创建一个函数检查变量名是否符合Python命名规范

```python
import keyword
import re

def check_variable_name(name):
    """检查变量名是否符合Python命名规范"""
    issues = []
    
    # 检查是否为空
    if not name:
        issues.append("变量名不能为空")
        return issues
    
    # 检查是否以数字开头
    if name[0].isdigit():
        issues.append("变量名不能以数字开头")
    
    # 检查是否包含非法字符
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name):
        issues.append("变量名只能包含字母、数字和下划线")
    
    # 检查是否为关键字
    if keyword.iskeyword(name):
        issues.append(f"'{name}' 是Python关键字，不能用作变量名")
    
    # 检查命名风格建议
    if name.isupper() and len(name) > 1:
        issues.append("建议：常量使用全大写，普通变量使用小写")
    
    if '-' in name:
        issues.append("建议：使用下划线而不是连字符")
    
    if name != name.lower() and '_' not in name:
        issues.append("建议：使用snake_case命名风格")
    
    return issues if issues else ["变量名符合规范"]

# 测试变量名
test_names = [
    "good_name",
    "123invalid",
    "class",
    "userName",
    "user-name",
    "CONSTANT_VALUE",
    "_private",
    "valid123",
    "",
    "name with space"
]

for name in test_names:
    issues = check_variable_name(name)
    print(f"'{name}': {', '.join(issues)}")
```

## 进阶练习

### 练习6：用户信息管理系统

**任务**：创建一个简单的用户信息管理系统

```python
# 用户信息管理系统
users = {}
next_user_id = 1

def add_user(name, age, email):
    """添加用户"""
    global next_user_id
    
    # 验证输入
    if not isinstance(name, str) or not name.strip():
        return False, "姓名必须是非空字符串"
    
    try:
        age = int(age)
        if age < 0 or age > 150:
            return False, "年龄必须在0-150之间"
    except ValueError:
        return False, "年龄必须是数字"
    
    if not isinstance(email, str) or '@' not in email:
        return False, "邮箱格式不正确"
    
    # 添加用户
    user_id = next_user_id
    users[user_id] = {
        'name': name.strip(),
        'age': age,
        'email': email.strip().lower(),
        'created_at': 'now',  # 简化处理
        'is_active': True
    }
    next_user_id += 1
    
    return True, f"用户添加成功，ID: {user_id}"

def display_user(user_id):
    """显示用户信息"""
    if user_id not in users:
        print(f"用户ID {user_id} 不存在")
        return
    
    user = users[user_id]
    status = "活跃" if user['is_active'] else "非活跃"
    
    print(f"用户ID: {user_id}")
    print(f"姓名: {user['name']}")
    print(f"年龄: {user['age']}")
    print(f"邮箱: {user['email']}")
    print(f"状态: {status}")
    print("-" * 30)

def update_user_age(user_id, new_age):
    """更新用户年龄"""
    if user_id not in users:
        return False, "用户不存在"
    
    try:
        new_age = int(new_age)
        if new_age < 0 or new_age > 150:
            return False, "年龄必须在0-150之间"
    except ValueError:
        return False, "年龄必须是数字"
    
    old_age = users[user_id]['age']
    users[user_id]['age'] = new_age
    
    return True, f"年龄已从 {old_age} 更新为 {new_age}"

def update_user_salary(user_id, salary):
    """更新用户薪资（新增字段）"""
    if user_id not in users:
        return False, "用户不存在"
    
    try:
        salary = float(salary)
        if salary < 0:
            return False, "薪资不能为负数"
    except ValueError:
        return False, "薪资必须是数字"
    
    users[user_id]['salary'] = salary
    return True, f"薪资已设置为 {salary}"

# 演示用户管理系统
print("用户信息管理系统演示")
print("=" * 40)

# 添加用户
result, message = add_user("张三", "25", "zhangsan@email.com")
print(f"添加用户1: {message}")

result, message = add_user("李四", 30, "lisi@email.com")
print(f"添加用户2: {message}")

result, message = add_user("", "abc", "invalid")
print(f"添加无效用户: {message}")

# 显示用户信息
print("\n显示用户信息:")
display_user(1)
display_user(2)

# 更新用户信息
result, message = update_user_age(1, "26")
print(f"更新年龄: {message}")

result, message = update_user_salary(1, "8000.50")
print(f"设置薪资: {message}")

# 显示更新后的信息
print("\n更新后的用户信息:")
display_user(1)
```

### 练习7：智能数据类型转换器

**任务**：创建一个智能的数据类型转换器

```python
def smart_convert(value):
    """智能数据类型转换器"""
    if not isinstance(value, str):
        return value, type(value).__name__, "无需转换"
    
    original = value
    value = value.strip()
    
    # 空字符串
    if not value:
        return "", "str", "空字符串"
    
    # 布尔值
    if value.lower() in ['true', 'false']:
        return value.lower() == 'true', "bool", "转换为布尔值"
    
    # 整数
    try:
        if '.' not in value and 'e' not in value.lower():
            result = int(value)
            return result, "int", "转换为整数"
    except ValueError:
        pass
    
    # 浮点数
    try:
        result = float(value)
        return result, "float", "转换为浮点数"
    except ValueError:
        pass
    
    # 列表（简单的逗号分隔）
    if ',' in value:
        items = [item.strip() for item in value.split(',')]
        converted_items = []
        for item in items:
            converted_item, _, _ = smart_convert(item)
            converted_items.append(converted_item)
        return converted_items, "list", "转换为列表"
    
    # 保持为字符串
    return value, "str", "保持为字符串"

# 测试智能转换器
test_values = [
    "123",
    "3.14",
    "true",
    "false",
    "hello",
    "1,2,3,4",
    "apple,banana,orange",
    "  42  ",
    "",
    "1.5e2",
    "not a number"
]

print("智能数据类型转换器测试")
print("=" * 50)

for value in test_values:
    result, result_type, message = smart_convert(value)
    print(f"'{value}' -> {result} ({result_type}) - {message}")
```

### 练习8：变量作用域演示

**任务**：演示不同作用域中的变量行为

```python
# 全局变量
global_var = "我是全局变量"
counter = 0

def demonstrate_scope():
    """演示变量作用域"""
    # 局部变量
    local_var = "我是局部变量"
    
    # 访问全局变量
    print(f"函数内访问全局变量: {global_var}")
    print(f"函数内访问局部变量: {local_var}")
    
    # 修改全局变量需要global关键字
    global counter
    counter += 1
    print(f"修改后的计数器: {counter}")
    
    # 内部函数
    def inner_function():
        inner_var = "我是内部函数的变量"
        print(f"内部函数访问外部局部变量: {local_var}")
        print(f"内部函数访问全局变量: {global_var}")
        print(f"内部函数的变量: {inner_var}")
        
        # 修改外部函数的变量需要nonlocal
        nonlocal local_var
        local_var = "被内部函数修改了"
    
    print("\n调用内部函数前:")
    print(f"local_var = {local_var}")
    
    inner_function()
    
    print("\n调用内部函数后:")
    print(f"local_var = {local_var}")

# 演示作用域
print("变量作用域演示")
print("=" * 30)

print(f"调用函数前的全局变量: {global_var}")
print(f"调用函数前的计数器: {counter}")

demonstrate_scope()

print(f"\n调用函数后的全局变量: {global_var}")
print(f"调用函数后的计数器: {counter}")

# 尝试访问局部变量会出错
try:
    print(local_var)  # 这会引发NameError
except NameError as e:
    print(f"\n错误: {e}")
    print("局部变量在函数外部不可访问")
```

### 练习9：学生成绩管理系统

**任务**：创建一个复杂的学生成绩管理系统

```python
# 学生成绩管理系统
students_data = {
    "张三": {
        "id": "S001",
        "age": 20,
        "grades": {"数学": 85, "英语": 92, "物理": 78},
        "is_active": True
    },
    "李四": {
        "id": "S002",
        "age": 19,
        "grades": {"数学": 90, "英语": 88, "物理": 95},
        "is_active": True
    },
    "王五": {
        "id": "S003",
        "age": 21,
        "grades": {"数学": 76, "英语": 85},
        "is_active": False
    }
}

def calculate_student_average(student_name):
    """计算学生平均分"""
    if student_name not in students_data:
        return None
    
    grades = students_data[student_name]["grades"]
    if not grades:
        return 0
    
    total = sum(grades.values())
    count = len(grades)
    return round(total / count, 2)

def get_subject_statistics(subject):
    """获取某科目的统计信息"""
    scores = []
    for student_name, student_info in students_data.items():
        if subject in student_info["grades"]:
            scores.append(student_info["grades"][subject])
    
    if not scores:
        return None
    
    return {
        "average": round(sum(scores) / len(scores), 2),
        "max": max(scores),
        "min": min(scores),
        "count": len(scores)
    }

def add_grade(student_name, subject, score_str):
    """添加成绩（带验证）"""
    try:
        score = float(score_str)
        if not (0 <= score <= 100):
            print(f"成绩无效：{score}（应在0-100之间）")
            return False
        
        if student_name not in students_data:
            print(f"学生不存在：{student_name}")
            return False
        
        students_data[student_name]["grades"][subject] = score
        print(f"成绩添加成功：{student_name} {subject} {score}")
        return True
    
    except ValueError:
        print(f"成绩格式错误：'{score_str}'（应为数字）")
        return False

def display_all_students():
    """显示所有学生信息"""
    print("\n所有学生信息：")
    print("-" * 60)
    
    for student_name, student_info in students_data.items():
        status = "活跃" if student_info["is_active"] else "非活跃"
        average = calculate_student_average(student_name)
        
        print(f"姓名：{student_name} (ID: {student_info['id']}, 年龄: {student_info['age']}, 状态: {status})")
        print(f"  成绩：{student_info['grades']}")
        print(f"  平均分：{average}")
        print()

# 演示成绩管理系统
display_all_students()

print("科目统计信息：")
subjects = ["数学", "英语", "物理"]
for subject in subjects:
    stats = get_subject_statistics(subject)
    if stats:
        print(f"{subject}：平均分 {stats['average']}, 最高分 {stats['max']}, 最低分 {stats['min']}, 人数 {stats['count']}")

print("\n测试添加成绩：")
add_grade("张三", "化学", "88")
add_grade("张三", "化学", "105")  # 无效分数
add_grade("张三", "化学", "abc")  # 无效格式
add_grade("不存在", "数学", "90")  # 不存在的学生
```

### 练习10：类型安全的配置管理器

**任务**：创建一个类型安全的配置管理器

```python
class ConfigManager:
    """类型安全的配置管理器"""
    
    def __init__(self):
        self.config = {}
        self.schema = {}
    
    def define_config(self, key, default_value, value_type, description=""):
        """定义配置项"""
        self.schema[key] = {
            "type": value_type,
            "default": default_value,
            "description": description
        }
        self.config[key] = default_value
    
    def set_config(self, key, value):
        """设置配置项（带类型验证）"""
        if key not in self.schema:
            print(f"未知的配置项：{key}")
            return False
        
        expected_type = self.schema[key]["type"]
        
        # 尝试类型转换
        try:
            if expected_type == bool:
                if isinstance(value, str):
                    converted_value = value.lower() in ['true', '1', 'yes', 'on']
                else:
                    converted_value = bool(value)
            elif expected_type == int:
                converted_value = int(value)
            elif expected_type == float:
                converted_value = float(value)
            elif expected_type == str:
                converted_value = str(value)
            else:
                converted_value = value
            
            self.config[key] = converted_value
            print(f"配置更新：{key} = {converted_value} ({type(converted_value).__name__})")
            return True
        
        except (ValueError, TypeError) as e:
            print(f"配置设置失败：{key} = {value} (期望类型: {expected_type.__name__}, 错误: {e})")
            return False
    
    def get_config(self, key):
        """获取配置项"""
        return self.config.get(key, None)
    
    def display_config(self):
        """显示所有配置"""
        print("\n当前配置：")
        print("-" * 50)
        for key, value in self.config.items():
            schema_info = self.schema[key]
            print(f"{key}: {value} ({type(value).__name__})")
            print(f"  描述: {schema_info['description']}")
            print(f"  默认值: {schema_info['default']}")
            print()

# 创建配置管理器实例
config_manager = ConfigManager()

# 定义配置项
config_manager.define_config("server_port", 8080, int, "服务器端口号")
config_manager.define_config("debug_mode", False, bool, "是否启用调试模式")
config_manager.define_config("app_name", "MyApp", str, "应用程序名称")
config_manager.define_config("timeout", 30.0, float, "超时时间（秒）")
config_manager.define_config("max_connections", 100, int, "最大连接数")

# 显示初始配置
config_manager.display_config()

# 测试配置设置
print("测试配置设置：")
config_manager.set_config("server_port", "9000")      # 字符串转整数
config_manager.set_config("debug_mode", "true")       # 字符串转布尔
config_manager.set_config("timeout", "45.5")          # 字符串转浮点
config_manager.set_config("app_name", 123)            # 数字转字符串
config_manager.set_config("server_port", "abc")       # 无效转换
config_manager.set_config("unknown_key", "value")     # 未知配置项

# 显示最终配置
config_manager.display_config()
```

## 完整代码示例

以上所有练习的完整代码可以在 `06_exercises.py` 文件中找到。

## 运行方法

```bash
# 在终端中运行
python 06_exercises.py

# 或者在IDE中直接运行
```

## 学习总结

通过这些练习，你应该掌握了：

✅ **变量的定义和赋值**
- 不同数据类型的变量定义
- 变量的重新赋值和类型变化

✅ **Python的基本数据类型**
- 字符串、整数、浮点数、布尔值
- 复杂数据类型（列表、字典）

✅ **动态类型的特性**
- 类型的运行时确定
- 类型变化对操作的影响

✅ **类型转换的方法和注意事项**
- 显式类型转换
- 异常处理和验证

✅ **变量命名的规范和最佳实践**
- Python命名规则
- 代码可读性和维护性

✅ **复杂数据结构的处理**
- 嵌套数据结构
- 数据验证和处理

✅ **异常处理和输入验证**
- 健壮的代码编写
- 用户输入的安全处理

✅ **实际项目中的应用场景**
- 用户管理系统
- 配置管理
- 数据处理和分析

## 下一步学习建议

1. **继续学习控制结构**：if语句、循环结构
2. **深入学习函数和模块**：函数定义、参数传递、模块化编程
3. **学习面向对象编程**：类和对象、继承、多态
4. **实践更多的项目案例**：结合实际需求进行编程练习

## 额外挑战

1. **扩展ConfigManager类**：添加配置的保存和加载功能
2. **增强学生成绩管理系统**：添加成绩排名、及格率统计等功能
3. **创建数据验证器**：支持更复杂的验证规则和自定义验证函数
4. **实现类型提示**：为所有函数添加类型注解，提高代码质量

---

**恭喜完成变量和数据类型的所有练习！** 🎉

这些练习涵盖了Python变量和数据类型的核心概念，为后续的学习打下了坚实的基础。继续保持学习的热情，探索Python编程的更多精彩内容！