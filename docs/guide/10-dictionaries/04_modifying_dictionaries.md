# 字典的修改操作

## 学习目标

- 掌握字典元素的添加、修改和删除
- 学习字典的批量更新操作
- 理解字典合并的不同方式
- 掌握条件修改和安全操作
- 了解嵌套字典的修改技巧

## 字典修改基础

字典是可变对象，支持动态添加、修改和删除元素。正确的修改操作能让数据处理更加灵活和高效。

## 基本修改操作

### 1. 添加和修改元素

```python
# 创建初始字典
student = {
    "name": "张三",
    "age": 20,
    "grade": "大二"
}

print(f"初始字典: {student}")

# 添加新元素
student["gpa"] = 3.8
student["major"] = "计算机科学"
print(f"添加元素后: {student}")

# 修改现有元素
student["age"] = 21
student["grade"] = "大三"
print(f"修改元素后: {student}")

# 同时添加和修改
student["phone"] = "138-0000-0000"  # 新增
student["gpa"] = 3.9  # 修改
print(f"混合操作后: {student}")
```

### 2. 条件修改

```python
# 只在键不存在时添加
if "email" not in student:
    student["email"] = "zhangsan@example.com"
    print("添加了邮箱")

# 只在键存在时修改
if "gpa" in student:
    student["gpa"] = round(student["gpa"] + 0.1, 2)
    print(f"更新GPA: {student['gpa']}")

# 使用get()进行条件修改
current_gpa = student.get("gpa", 0.0)
if current_gpa > 0:
    student["gpa"] = min(current_gpa + 0.1, 4.0)
    print(f"调整后GPA: {student['gpa']}")
```

### 3. 使用setdefault()方法

```python
# setdefault()：如果键不存在则设置，存在则返回现有值
default_courses = student.setdefault("courses", [])
default_courses.append("数学")
default_courses.append("物理")
print(f"添加课程后: {student}")

# 再次使用setdefault()不会覆盖现有值
existing_courses = student.setdefault("courses", ["默认课程"])
existing_courses.append("化学")
print(f"继续添加课程: {student}")

# 为嵌套结构使用setdefault()
scores = student.setdefault("scores", {})
scores["数学"] = 95
scores["物理"] = 88
print(f"添加成绩后: {student}")
```

## 删除操作

### 1. 使用del语句

```python
# 创建测试字典
test_dict = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5
}

print(f"原始字典: {test_dict}")

# 删除指定键
del test_dict["c"]
print(f"删除'c'后: {test_dict}")

# 删除多个键（需要逐个删除）
keys_to_delete = ["a", "e"]
for key in keys_to_delete:
    if key in test_dict:
        del test_dict[key]
print(f"删除多个键后: {test_dict}")

# 尝试删除不存在的键会引发KeyError
try:
    del test_dict["x"]
except KeyError as e:
    print(f"删除失败: {e}")
```

### 2. 使用pop()方法

```python
# 重新创建测试字典
test_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

# pop()删除并返回值
value_b = test_dict.pop("b")
print(f"删除'b'，返回值: {value_b}")
print(f"删除后字典: {test_dict}")

# pop()提供默认值
value_x = test_dict.pop("x", "不存在")
print(f"删除不存在的键: {value_x}")

# 使用pop()进行条件删除
if "c" in test_dict:
    removed_value = test_dict.pop("c")
    print(f"条件删除'c': {removed_value}")

print(f"最终字典: {test_dict}")
```

### 3. 使用popitem()方法

```python
# popitem()删除并返回最后插入的键值对（Python 3.7+保证顺序）
test_dict = {"first": 1, "second": 2, "third": 3}
print(f"原始字典: {test_dict}")

# 删除最后一个项
last_item = test_dict.popitem()
print(f"删除的项: {last_item}")
print(f"删除后字典: {test_dict}")

# 继续删除
while test_dict:
    item = test_dict.popitem()
    print(f"删除: {item}")

print(f"清空后字典: {test_dict}")

# 对空字典使用popitem()会引发KeyError
try:
    test_dict.popitem()
except KeyError:
    print("空字典无法popitem()")
```

### 4. 使用clear()方法

```python
# 清空整个字典
test_dict = {"a": 1, "b": 2, "c": 3}
print(f"清空前: {test_dict}")

test_dict.clear()
print(f"清空后: {test_dict}")
print(f"字典类型: {type(test_dict)}")
print(f"字典长度: {len(test_dict)}")
```

## 批量更新操作

### 1. 使用update()方法

```python
# 创建基础字典
base_dict = {"a": 1, "b": 2}
print(f"基础字典: {base_dict}")

# 使用字典更新
update_dict = {"c": 3, "d": 4, "b": 20}  # 注意'b'会被覆盖
base_dict.update(update_dict)
print(f"字典更新后: {base_dict}")

# 使用关键字参数更新
base_dict.update(e=5, f=6, a=10)
print(f"关键字更新后: {base_dict}")

# 使用键值对列表更新
kv_pairs = [("g", 7), ("h", 8)]
base_dict.update(kv_pairs)
print(f"列表更新后: {base_dict}")

# 混合更新方式
base_dict.update({"i": 9}, j=10, k=11)
print(f"混合更新后: {base_dict}")
```

### 2. 字典合并操作（Python 3.9+）

```python
# 使用|操作符合并字典（Python 3.9+）
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 20, "e": 5}  # 注意'b'的冲突

# 合并创建新字典
merged = dict1 | dict2 | dict3
print(f"合并结果: {merged}")
print(f"原字典1: {dict1}")  # 原字典不变

# 使用|=操作符就地更新
dict1 |= dict2
print(f"就地合并后dict1: {dict1}")

# 传统合并方式（兼容旧版本）
dict_a = {"x": 1, "y": 2}
dict_b = {"z": 3, "y": 20}
merged_traditional = {**dict_a, **dict_b}
print(f"传统合并: {merged_traditional}")
```

### 3. 条件批量更新

```python
def conditional_update(target_dict, source_dict, condition_func=None):
    """
    条件批量更新字典
    """
    for key, value in source_dict.items():
        if condition_func is None or condition_func(key, value, target_dict):
            target_dict[key] = value

# 示例：只更新不存在的键
def only_new_keys(key, value, target):
    return key not in target

# 示例：只更新数值更大的值
def only_larger_values(key, value, target):
    return key not in target or (isinstance(value, (int, float)) and 
                                isinstance(target.get(key), (int, float)) and 
                                value > target[key])

# 测试条件更新
target = {"a": 1, "b": 5, "c": 3}
source = {"a": 2, "b": 3, "d": 4, "e": 6}

print(f"目标字典: {target}")
print(f"源字典: {source}")

# 只添加新键
target_copy1 = target.copy()
conditional_update(target_copy1, source, only_new_keys)
print(f"只添加新键: {target_copy1}")

# 只更新更大的值
target_copy2 = target.copy()
conditional_update(target_copy2, source, only_larger_values)
print(f"只更新更大值: {target_copy2}")
```

## 嵌套字典的修改

### 1. 基本嵌套修改

```python
# 创建嵌套字典
company = {
    "name": "科技公司",
    "departments": {
        "IT": {
            "manager": "张经理",
            "budget": 1000000,
            "employees": ["程序员A", "程序员B"]
        },
        "HR": {
            "manager": "李经理",
            "budget": 500000,
            "employees": ["HR专员A"]
        }
    }
}

print(f"原始公司信息: {company}")

# 修改嵌套值
company["departments"]["IT"]["budget"] = 1200000
print(f"更新IT预算后: {company['departments']['IT']['budget']}")

# 添加新部门
company["departments"]["Finance"] = {
    "manager": "王经理",
    "budget": 800000,
    "employees": ["会计A", "会计B"]
}
print(f"添加财务部门后: {list(company['departments'].keys())}")

# 修改嵌套列表
company["departments"]["IT"]["employees"].append("程序员C")
print(f"IT部门员工: {company['departments']['IT']['employees']}")
```

### 2. 安全的嵌套修改

```python
def safe_nested_set(dictionary, keys, value):
    """
    安全地设置嵌套字典的值
    """
    for key in keys[:-1]:
        if key not in dictionary:
            dictionary[key] = {}
        dictionary = dictionary[key]
    dictionary[keys[-1]] = value

def safe_nested_update(dictionary, keys, update_dict):
    """
    安全地更新嵌套字典
    """
    target = dictionary
    for key in keys:
        if key not in target:
            target[key] = {}
        target = target[key]
    target.update(update_dict)

# 测试安全嵌套操作
test_dict = {}

# 创建深层嵌套结构
safe_nested_set(test_dict, ["level1", "level2", "level3"], "深层值")
print(f"创建嵌套结构: {test_dict}")

# 安全更新嵌套字典
safe_nested_update(test_dict, ["level1", "level2"], {
    "new_key": "新值",
    "another_key": "另一个值"
})
print(f"更新嵌套字典: {test_dict}")
```

### 3. 嵌套字典的深度修改

```python
def deep_update(base_dict, update_dict):
    """
    深度更新字典（递归合并）
    """
    for key, value in update_dict.items():
        if (key in base_dict and 
            isinstance(base_dict[key], dict) and 
            isinstance(value, dict)):
            deep_update(base_dict[key], value)
        else:
            base_dict[key] = value

# 测试深度更新
original = {
    "config": {
        "database": {
            "host": "localhost",
            "port": 5432
        },
        "cache": {
            "type": "redis"
        }
    },
    "debug": True
}

update_data = {
    "config": {
        "database": {
            "port": 3306,  # 修改端口
            "name": "myapp"  # 添加数据库名
        },
        "logging": {  # 添加新配置
            "level": "INFO"
        }
    },
    "version": "1.0"  # 添加版本信息
}

print(f"原始配置: {original}")
deep_update(original, update_data)
print(f"深度更新后: {original}")
```

## 高级修改技巧

### 1. 批量键重命名

```python
def rename_keys(dictionary, key_mapping):
    """
    批量重命名字典的键
    """
    for old_key, new_key in key_mapping.items():
        if old_key in dictionary:
            dictionary[new_key] = dictionary.pop(old_key)

# 测试键重命名
data = {
    "fname": "张",
    "lname": "三",
    "age": 25,
    "addr": "北京市"
}

print(f"重命名前: {data}")

# 定义重命名映射
rename_map = {
    "fname": "first_name",
    "lname": "last_name",
    "addr": "address"
}

rename_keys(data, rename_map)
print(f"重命名后: {data}")
```

### 2. 值的批量转换

```python
def transform_values(dictionary, transform_func, key_filter=None):
    """
    批量转换字典的值
    """
    for key, value in dictionary.items():
        if key_filter is None or key_filter(key):
            dictionary[key] = transform_func(value)

# 示例转换函数
def to_uppercase(value):
    return value.upper() if isinstance(value, str) else value

def multiply_by_two(value):
    return value * 2 if isinstance(value, (int, float)) else value

# 测试值转换
test_data = {
    "name": "zhang san",
    "city": "beijing",
    "age": 25,
    "score": 85.5,
    "active": True
}

print(f"转换前: {test_data}")

# 转换字符串为大写
data_copy1 = test_data.copy()
transform_values(data_copy1, to_uppercase, 
                lambda k: isinstance(test_data[k], str))
print(f"字符串大写: {data_copy1}")

# 数值乘以2
data_copy2 = test_data.copy()
transform_values(data_copy2, multiply_by_two, 
                lambda k: isinstance(test_data[k], (int, float)))
print(f"数值翻倍: {data_copy2}")
```

### 3. 字典过滤和清理

```python
def filter_dict(dictionary, condition_func):
    """
    根据条件过滤字典
    """
    return {k: v for k, v in dictionary.items() if condition_func(k, v)}

def remove_none_values(dictionary):
    """
    移除值为None的项
    """
    keys_to_remove = [k for k, v in dictionary.items() if v is None]
    for key in keys_to_remove:
        del dictionary[key]

def remove_empty_values(dictionary):
    """
    移除空值（None、空字符串、空列表等）
    """
    keys_to_remove = []
    for k, v in dictionary.items():
        if v is None or v == "" or v == [] or v == {}:
            keys_to_remove.append(k)
    
    for key in keys_to_remove:
        del dictionary[key]

# 测试过滤和清理
test_data = {
    "name": "张三",
    "age": 25,
    "email": None,
    "phone": "",
    "hobbies": [],
    "address": "北京市",
    "score": 0,
    "metadata": {}
}

print(f"原始数据: {test_data}")

# 过滤出非空字符串
filtered = filter_dict(test_data, 
                      lambda k, v: isinstance(v, str) and v != "")
print(f"非空字符串: {filtered}")

# 移除None值
data_copy1 = test_data.copy()
remove_none_values(data_copy1)
print(f"移除None后: {data_copy1}")

# 移除所有空值
data_copy2 = test_data.copy()
remove_empty_values(data_copy2)
print(f"移除空值后: {data_copy2}")
```

## 实际应用示例

### 1. 配置管理系统

```python
class ConfigManager:
    def __init__(self, initial_config=None):
        self.config = initial_config or {}
        self.history = [self.config.copy()]
    
    def set(self, key_path, value):
        """
        使用点分隔路径设置配置值
        """
        keys = key_path.split('.')
        target = self.config
        
        # 创建嵌套结构
        for key in keys[:-1]:
            if key not in target:
                target[key] = {}
            target = target[key]
        
        # 设置最终值
        target[keys[-1]] = value
        self.history.append(self.config.copy())
    
    def update_section(self, section_path, updates):
        """
        更新配置段
        """
        keys = section_path.split('.') if section_path else []
        target = self.config
        
        for key in keys:
            if key not in target:
                target[key] = {}
            target = target[key]
        
        target.update(updates)
        self.history.append(self.config.copy())
    
    def remove(self, key_path):
        """
        删除配置项
        """
        keys = key_path.split('.')
        target = self.config
        
        # 导航到父级
        for key in keys[:-1]:
            if key not in target:
                return False
            target = target[key]
        
        # 删除最终键
        if keys[-1] in target:
            del target[keys[-1]]
            self.history.append(self.config.copy())
            return True
        return False
    
    def rollback(self):
        """
        回滚到上一个状态
        """
        if len(self.history) > 1:
            self.history.pop()  # 移除当前状态
            self.config = self.history[-1].copy()
            return True
        return False
    
    def get_config(self):
        return self.config.copy()

# 使用配置管理器
config_mgr = ConfigManager()

# 设置基础配置
config_mgr.set("database.host", "localhost")
config_mgr.set("database.port", 5432)
config_mgr.set("database.name", "myapp")
print(f"基础配置: {config_mgr.get_config()}")

# 批量更新
config_mgr.update_section("cache", {
    "type": "redis",
    "host": "localhost",
    "port": 6379
})
print(f"添加缓存配置: {config_mgr.get_config()}")

# 修改配置
config_mgr.set("database.port", 3306)
print(f"修改端口: {config_mgr.get_config()}")

# 回滚操作
config_mgr.rollback()
print(f"回滚后: {config_mgr.get_config()}")
```

### 2. 数据清洗和转换

```python
def clean_user_data(user_data):
    """
    清洗用户数据
    """
    cleaned = user_data.copy()
    
    # 标准化姓名
    if "name" in cleaned:
        cleaned["name"] = cleaned["name"].strip().title()
    
    # 标准化邮箱
    if "email" in cleaned:
        cleaned["email"] = cleaned["email"].strip().lower()
    
    # 标准化电话号码
    if "phone" in cleaned:
        phone = cleaned["phone"]
        # 移除非数字字符
        phone = ''.join(filter(str.isdigit, phone))
        if len(phone) == 11 and phone.startswith('1'):
            cleaned["phone"] = f"{phone[:3]}-{phone[3:7]}-{phone[7:]}"
        else:
            cleaned["phone"] = "无效号码"
    
    # 移除空值
    keys_to_remove = [k for k, v in cleaned.items() 
                     if v is None or v == "" or v == []]
    for key in keys_to_remove:
        del cleaned[key]
    
    return cleaned

# 测试数据清洗
raw_users = [
    {
        "name": "  zhang san  ",
        "email": "  ZHANG@EXAMPLE.COM  ",
        "phone": "138-0000-0000",
        "address": "",
        "notes": None
    },
    {
        "name": "li si",
        "email": "lisi@test.com",
        "phone": "13900001111",
        "age": 25
    }
]

print("原始用户数据:")
for i, user in enumerate(raw_users):
    print(f"  用户{i+1}: {user}")

print("\n清洗后数据:")
for i, user in enumerate(raw_users):
    cleaned = clean_user_data(user)
    print(f"  用户{i+1}: {cleaned}")
```

## 性能考虑

### 1. 修改操作的性能比较

```python
import time

def performance_comparison():
    # 创建大字典
    large_dict = {f"key_{i}": i for i in range(100000)}
    n = 10000
    
    # 测试直接赋值
    start = time.time()
    test_dict1 = large_dict.copy()
    for i in range(n):
        test_dict1[f"new_key_{i}"] = i
    time1 = time.time() - start
    
    # 测试update()方法
    start = time.time()
    test_dict2 = large_dict.copy()
    update_data = {f"new_key_{i}": i for i in range(n)}
    test_dict2.update(update_data)
    time2 = time.time() - start
    
    # 测试setdefault()方法
    start = time.time()
    test_dict3 = large_dict.copy()
    for i in range(n):
        test_dict3.setdefault(f"new_key_{i}", i)
    time3 = time.time() - start
    
    print(f"直接赋值: {time1:.4f}秒")
    print(f"update()方法: {time2:.4f}秒")
    print(f"setdefault()方法: {time3:.4f}秒")

# performance_comparison()  # 取消注释以运行性能测试
```

### 2. 最佳实践建议

```python
# 1. 批量操作优于逐个操作
def good_batch_update(target_dict, updates):
    # 好的做法：使用update()
    target_dict.update(updates)

def bad_individual_update(target_dict, updates):
    # 不好的做法：逐个赋值
    for key, value in updates.items():
        target_dict[key] = value

# 2. 使用适当的删除方法
def safe_remove(dictionary, key):
    # 安全删除：使用pop()提供默认值
    return dictionary.pop(key, None)

def unsafe_remove(dictionary, key):
    # 不安全：直接使用del
    del dictionary[key]  # 可能引发KeyError

# 3. 嵌套操作的最佳实践
def safe_nested_operation(data, keys, operation):
    """
    安全的嵌套操作
    """
    target = data
    for key in keys[:-1]:
        if not isinstance(target, dict) or key not in target:
            return False
        target = target[key]
    
    if isinstance(target, dict) and keys[-1] in target:
        operation(target, keys[-1])
        return True
    return False

# 示例使用
test_data = {"level1": {"level2": {"target": "value"}}}

# 安全修改嵌套值
success = safe_nested_operation(
    test_data, 
    ["level1", "level2", "target"], 
    lambda d, k: d.update({k: "new_value"})
)
print(f"修改成功: {success}, 结果: {test_data}")
```

## 学习要点

1. **选择合适的修改方法**
   - 单个元素：直接赋值 `dict[key] = value`
   - 批量更新：使用 `update()` 方法
   - 条件添加：使用 `setdefault()` 方法

2. **安全的删除策略**
   - 使用 `pop()` 方法提供默认值
   - 删除前检查键是否存在
   - 使用 `clear()` 清空整个字典

3. **嵌套字典操作**
   - 逐层检查结构的存在性
   - 使用递归函数处理深层嵌套
   - 提供安全的访问和修改接口

4. **性能优化**
   - 批量操作比逐个操作更高效
   - `update()` 比循环赋值更快
   - 避免不必要的字典复制

## 练习题

1. 编写一个函数来安全地修改嵌套字典的值
2. 实现一个字典合并函数，支持自定义冲突解决策略
3. 创建一个配置管理类，支持配置的增删改查和历史记录
4. 编写代码来批量清理和标准化用户输入数据
5. 实现一个字典修改操作的性能测试工具

## 下一步学习

掌握了字典的修改操作后，接下来学习：
- 字典的内置方法详解
- 字典的遍历和迭代技巧
- 嵌套字典的高级操作
- 字典推导式的使用

---

灵活的字典修改操作是数据处理的核心技能，掌握这些技巧能让你的代码更加高效和健壮！