# 嵌套字典操作详解

## 学习目标

- 掌握嵌套字典的创建和初始化
- 学习嵌套字典的访问和修改技巧
- 理解深度遍历和搜索方法
- 掌握嵌套字典的复制和合并
- 学习复杂数据结构的处理技巧
- 了解嵌套字典在实际项目中的应用

## 嵌套字典基础

嵌套字典是指字典的值本身也是字典的数据结构。这种结构在处理复杂的层次化数据时非常有用，如配置文件、JSON数据、数据库记录等。

## 创建嵌套字典

### 1. 基本创建方法

```python
print("=== 嵌套字典的创建 ===")

# 方法1：直接定义
student_info = {
    "张三": {
        "age": 20,
        "grades": {"数学": 85, "英语": 92, "物理": 78},
        "contact": {"email": "zhangsan@email.com", "phone": "123-456-7890"}
    },
    "李四": {
        "age": 19,
        "grades": {"数学": 90, "英语": 88, "物理": 95},
        "contact": {"email": "lisi@email.com", "phone": "098-765-4321"}
    }
}

print("直接定义的嵌套字典:")
for name, info in student_info.items():
    print(f"  {name}: 年龄{info['age']}, 邮箱{info['contact']['email']}")

# 方法2：逐步构建
company = {}
company["技术部"] = {}
company["技术部"]["员工"] = ["张工", "李工", "王工"]
company["技术部"]["预算"] = 500000
company["技术部"]["项目"] = {
    "项目A": {"状态": "进行中", "进度": 75},
    "项目B": {"状态": "已完成", "进度": 100}
}

company["销售部"] = {
    "员工": ["赵经理", "钱主管"],
    "预算": 300000,
    "目标": {"季度": 1000000, "年度": 4000000}
}

print(f"\n逐步构建的嵌套字典: {company}")

# 方法3：使用字典推导式
grade_structure = {
    student: {
        subject: score + 10 if score < 90 else score  # 给低分加10分
        for subject, score in grades.items()
    }
    for student, info in student_info.items()
    for grades in [info["grades"]]  # 提取grades字典
}

print(f"\n字典推导式创建: {grade_structure}")

# 方法4：从JSON样式数据创建
import json

json_data = '''
{
    "config": {
        "database": {
            "host": "localhost",
            "port": 5432,
            "credentials": {
                "username": "admin",
                "password": "secret"
            }
        },
        "cache": {
            "redis": {
                "host": "127.0.0.1",
                "port": 6379
            }
        }
    }
}
'''

config_dict = json.loads(json_data)
print(f"\n从JSON创建: {config_dict}")

# 方法5：使用defaultdict创建自动嵌套
from collections import defaultdict

def nested_dict():
    return defaultdict(nested_dict)

auto_nested = nested_dict()
auto_nested["level1"]["level2"]["level3"] = "深层值"
auto_nested["level1"]["level2"]["another"] = "另一个值"
auto_nested["level1"]["different"]["path"] = "不同路径"

# 转换为普通字典以便显示
def convert_defaultdict(d):
    if isinstance(d, defaultdict):
        d = {k: convert_defaultdict(v) for k, v in d.items()}
    return d

regular_nested = convert_defaultdict(auto_nested)
print(f"\n自动嵌套字典: {regular_nested}")
```

### 2. 复杂嵌套结构

```python
print("\n=== 复杂嵌套结构 ===")

# 创建多层嵌套的组织结构
organization = {
    "公司": {
        "名称": "科技有限公司",
        "成立年份": 2020,
        "部门": {
            "技术部": {
                "负责人": "张总监",
                "员工数": 15,
                "团队": {
                    "前端组": {
                        "组长": "李组长",
                        "成员": ["小王", "小张", "小李"],
                        "技术栈": ["React", "Vue", "Angular"],
                        "项目": {
                            "官网重构": {"状态": "进行中", "完成度": 60},
                            "移动端App": {"状态": "计划中", "完成度": 0}
                        }
                    },
                    "后端组": {
                        "组长": "王组长",
                        "成员": ["小赵", "小钱", "小孙", "小周"],
                        "技术栈": ["Python", "Java", "Go"],
                        "项目": {
                            "API服务": {"状态": "已完成", "完成度": 100},
                            "数据分析": {"状态": "进行中", "完成度": 80}
                        }
                    }
                }
            },
            "产品部": {
                "负责人": "刘总监",
                "员工数": 8,
                "产品线": {
                    "企业版": {"版本": "2.1", "用户数": 1500},
                    "个人版": {"版本": "1.8", "用户数": 50000}
                }
            }
        },
        "财务": {
            "年度预算": 5000000,
            "季度报告": {
                "Q1": {"收入": 800000, "支出": 600000, "利润": 200000},
                "Q2": {"收入": 950000, "支出": 650000, "利润": 300000},
                "Q3": {"收入": 1100000, "支出": 700000, "利润": 400000}
            }
        }
    }
}

print("组织结构创建完成")
print(f"公司名称: {organization['公司']['名称']}")
print(f"技术部员工数: {organization['公司']['部门']['技术部']['员工数']}")
print(f"前端组项目数: {len(organization['公司']['部门']['技术部']['团队']['前端组']['项目'])}")

# 混合数据类型的嵌套结构
mixed_data = {
    "用户": {
        "基本信息": {
            "姓名": "张三",
            "年龄": 25,
            "爱好": ["读书", "游泳", "编程"],
            "地址": {
                "省份": "北京市",
                "城市": "北京市",
                "详细地址": "朝阳区某某街道123号"
            }
        },
        "账户信息": {
            "余额": 15000.50,
            "积分": 2580,
            "等级": "VIP",
            "交易记录": [
                {"日期": "2024-01-15", "金额": -200, "描述": "购买商品"},
                {"日期": "2024-01-20", "金额": 1000, "描述": "工资入账"},
                {"日期": "2024-01-25", "金额": -50, "描述": "话费充值"}
            ]
        },
        "设置": {
            "通知": {
                "邮件": True,
                "短信": False,
                "推送": True
            },
            "隐私": {
                "公开资料": False,
                "允许搜索": True
            }
        }
    }
}

print(f"\n混合数据结构:")
print(f"用户姓名: {mixed_data['用户']['基本信息']['姓名']}")
print(f"账户余额: {mixed_data['用户']['账户信息']['余额']}")
print(f"交易记录数: {len(mixed_data['用户']['账户信息']['交易记录'])}")
print(f"邮件通知: {mixed_data['用户']['设置']['通知']['邮件']}")
```

## 访问嵌套字典

### 1. 基本访问方法

```python
print("\n=== 嵌套字典的访问 ===")

# 使用方括号访问（可能抛出KeyError）
try:
    tech_leader = organization["公司"]["部门"]["技术部"]["负责人"]
    print(f"技术部负责人: {tech_leader}")
    
    # 访问不存在的键会抛出异常
    # non_exist = organization["公司"]["部门"]["不存在的部门"]["负责人"]
except KeyError as e:
    print(f"访问错误: {e}")

# 使用get()方法安全访问
def safe_get_nested(data, *keys, default=None):
    """
    安全地获取嵌套字典的值
    """
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return default
    return data

# 测试安全访问
tech_leader = safe_get_nested(organization, "公司", "部门", "技术部", "负责人")
print(f"安全访问技术部负责人: {tech_leader}")

non_exist = safe_get_nested(organization, "公司", "部门", "不存在的部门", "负责人", default="未找到")
print(f"访问不存在的部门: {non_exist}")

# 使用链式get()方法
q1_profit = (organization.get("公司", {})
            .get("财务", {})
            .get("季度报告", {})
            .get("Q1", {})
            .get("利润", 0))
print(f"Q1利润: {q1_profit}")

# 批量访问多个路径
paths_to_access = [
    (["公司", "名称"], "公司名称"),
    (["公司", "部门", "技术部", "员工数"], "技术部员工数"),
    (["公司", "部门", "产品部", "负责人"], "产品部负责人"),
    (["公司", "财务", "年度预算"], "年度预算"),
    (["公司", "部门", "不存在部门", "负责人"], "不存在的信息")
]

print("\n批量访问结果:")
for path, description in paths_to_access:
    value = safe_get_nested(organization, *path, default="未找到")
    print(f"  {description}: {value}")

# 条件访问：只有满足条件才继续访问
def conditional_access(data, condition_func, *keys, default=None):
    """
    条件访问：只有满足条件才继续访问深层数据
    """
    if not condition_func(data):
        return default
    
    return safe_get_nested(data, *keys, default=default)

# 只有当公司成立年份大于2019时才访问部门信息
dept_info = conditional_access(
    organization,
    lambda x: x.get("公司", {}).get("成立年份", 0) > 2019,
    "公司", "部门", "技术部", "负责人",
    default="公司太新，无部门信息"
)
print(f"\n条件访问结果: {dept_info}")
```

### 2. 高级访问技巧

```python
print("\n=== 高级访问技巧 ===")

# 路径表达式访问
class NestedDictAccessor:
    def __init__(self, data):
        self.data = data
    
    def get_by_path(self, path_string, separator=".", default=None):
        """
        使用路径字符串访问嵌套数据
        例如: "公司.部门.技术部.负责人"
        """
        keys = path_string.split(separator)
        return safe_get_nested(self.data, *keys, default=default)
    
    def set_by_path(self, path_string, value, separator=".", create_missing=True):
        """
        使用路径字符串设置嵌套数据
        """
        keys = path_string.split(separator)
        current = self.data
        
        # 导航到倒数第二层
        for key in keys[:-1]:
            if key not in current:
                if create_missing:
                    current[key] = {}
                else:
                    raise KeyError(f"路径不存在: {key}")
            current = current[key]
        
        # 设置最后一层的值
        current[keys[-1]] = value
    
    def exists_path(self, path_string, separator="."):
        """
        检查路径是否存在
        """
        keys = path_string.split(separator)
        current = self.data
        
        for key in keys:
            if not isinstance(current, dict) or key not in current:
                return False
            current = current[key]
        
        return True
    
    def list_all_paths(self, current_path="", separator="."):
        """
        列出所有可能的路径
        """
        paths = []
        
        def _traverse(data, path):
            if isinstance(data, dict):
                for key, value in data.items():
                    new_path = f"{path}{separator}{key}" if path else key
                    paths.append(new_path)
                    _traverse(value, new_path)
        
        _traverse(self.data, current_path)
        return paths

# 测试高级访问器
accessor = NestedDictAccessor(organization)

# 路径字符串访问
tech_leader = accessor.get_by_path("公司.部门.技术部.负责人")
print(f"路径访问技术部负责人: {tech_leader}")

q2_income = accessor.get_by_path("公司.财务.季度报告.Q2.收入")
print(f"Q2收入: {q2_income}")

# 检查路径是否存在
print(f"\n路径存在性检查:")
test_paths = [
    "公司.名称",
    "公司.部门.技术部",
    "公司.部门.不存在的部门",
    "公司.财务.季度报告.Q4"
]

for path in test_paths:
    exists = accessor.exists_path(path)
    print(f"  {path}: {'存在' if exists else '不存在'}")

# 设置新值
accessor.set_by_path("公司.部门.技术部.新属性", "新值")
accessor.set_by_path("公司.新部门.负责人", "新负责人")

print(f"\n设置后的新属性: {accessor.get_by_path('公司.部门.技术部.新属性')}")
print(f"新部门负责人: {accessor.get_by_path('公司.新部门.负责人')}")

# 列出所有路径（只显示前10个）
all_paths = accessor.list_all_paths()
print(f"\n所有路径（前10个）:")
for path in all_paths[:10]:
    print(f"  {path}")
print(f"  ... 总共{len(all_paths)}个路径")

# 模糊搜索路径
def fuzzy_search_paths(accessor, keyword):
    """
    模糊搜索包含关键词的路径
    """
    all_paths = accessor.list_all_paths()
    matching_paths = [path for path in all_paths if keyword in path]
    return matching_paths

# 搜索包含"项目"的路径
project_paths = fuzzy_search_paths(accessor, "项目")
print(f"\n包含'项目'的路径:")
for path in project_paths:
    value = accessor.get_by_path(path)
    print(f"  {path}: {value}")
```

## 修改嵌套字典

### 1. 基本修改操作

```python
print("\n=== 嵌套字典的修改 ===")

# 创建测试数据的副本
test_org = {
    "部门": {
        "技术部": {
            "员工": ["张三", "李四"],
            "预算": 100000,
            "项目": {
                "项目A": {"状态": "进行中", "进度": 50},
                "项目B": {"状态": "计划中", "进度": 0}
            }
        },
        "销售部": {
            "员工": ["王五", "赵六"],
            "预算": 80000
        }
    }
}

print(f"修改前: {test_org}")

# 直接修改现有值
test_org["部门"]["技术部"]["预算"] = 120000
test_org["部门"]["技术部"]["项目"]["项目A"]["进度"] = 75

print(f"\n修改预算和进度后:")
print(f"  技术部预算: {test_org['部门']['技术部']['预算']}")
print(f"  项目A进度: {test_org['部门']['技术部']['项目']['项目A']['进度']}")

# 添加新的嵌套结构
test_org["部门"]["人事部"] = {
    "员工": ["钱七"],
    "预算": 50000,
    "职能": ["招聘", "培训", "考核"]
}

# 在现有结构中添加新项目
test_org["部门"]["技术部"]["项目"]["项目C"] = {
    "状态": "新建",
    "进度": 0,
    "负责人": "新员工"
}

print(f"\n添加人事部和项目C后:")
print(f"  人事部: {test_org['部门']['人事部']}")
print(f"  项目C: {test_org['部门']['技术部']['项目']['项目C']}")

# 修改列表类型的值
test_org["部门"]["技术部"]["员工"].append("新员工")
test_org["部门"]["人事部"]["职能"].extend(["薪酬管理", "员工关系"])

print(f"\n修改员工列表后:")
print(f"  技术部员工: {test_org['部门']['技术部']['员工']}")
print(f"  人事部职能: {test_org['部门']['人事部']['职能']}")

# 安全修改函数
def safe_set_nested(data, keys, value, create_path=True):
    """
    安全地设置嵌套字典的值
    """
    current = data
    
    # 导航到倒数第二层
    for key in keys[:-1]:
        if key not in current:
            if create_path:
                current[key] = {}
            else:
                raise KeyError(f"路径不存在: {key}")
        elif not isinstance(current[key], dict):
            raise TypeError(f"路径中的 {key} 不是字典类型")
        current = current[key]
    
    # 设置最后一层的值
    current[keys[-1]] = value

# 测试安全修改
safe_set_nested(test_org, ["部门", "技术部", "新属性"], "新值")
safe_set_nested(test_org, ["新部门", "负责人"], "新负责人")
safe_set_nested(test_org, ["新部门", "成立时间"], "2024-01-01")

print(f"\n安全修改后:")
print(f"  技术部新属性: {test_org['部门']['技术部']['新属性']}")
print(f"  新部门: {test_org['新部门']}")
```

### 2. 批量修改和更新

```python
print("\n=== 批量修改和更新 ===")

# 批量更新函数
def batch_update_nested(data, updates):
    """
    批量更新嵌套字典
    updates: [(keys_path, value), ...]
    """
    for keys, value in updates:
        safe_set_nested(data, keys, value)

# 定义批量更新
batch_updates = [
    (["部门", "技术部", "预算"], 150000),
    (["部门", "销售部", "预算"], 100000),
    (["部门", "技术部", "项目", "项目A", "状态"], "已完成"),
    (["部门", "技术部", "项目", "项目B", "进度"], 30),
    (["部门", "人事部", "预算"], 60000)
]

# 执行批量更新
batch_update_nested(test_org, batch_updates)

print("批量更新后的预算:")
for dept_name, dept_info in test_org["部门"].items():
    budget = dept_info.get("预算", "未设置")
    print(f"  {dept_name}: {budget}")

# 条件批量修改
def conditional_batch_update(data, condition_func, update_func):
    """
    根据条件批量修改嵌套字典
    """
    def _traverse_and_update(current_data, path=[]):
        if isinstance(current_data, dict):
            for key, value in current_data.items():
                current_path = path + [key]
                
                # 检查是否满足条件
                if condition_func(current_path, value):
                    # 执行更新
                    new_value = update_func(current_path, value)
                    current_data[key] = new_value
                else:
                    # 递归处理嵌套结构
                    _traverse_and_update(value, current_path)
    
    _traverse_and_update(data)

# 示例：将所有预算增加10%
def is_budget_field(path, value):
    return len(path) >= 2 and path[-1] == "预算" and isinstance(value, (int, float))

def increase_budget(path, value):
    return int(value * 1.1)

print(f"\n预算增加前: {test_org['部门']['技术部']['预算']}")
conditional_batch_update(test_org, is_budget_field, increase_budget)
print(f"预算增加后: {test_org['部门']['技术部']['预算']}")

# 示例：将所有"进行中"状态改为"审核中"
def is_in_progress_status(path, value):
    return path[-1] == "状态" and value == "进行中"

def change_to_reviewing(path, value):
    return "审核中"

conditional_batch_update(test_org, is_in_progress_status, change_to_reviewing)

print("\n状态修改后的项目:")
for project_name, project_info in test_org["部门"]["技术部"]["项目"].items():
    print(f"  {project_name}: {project_info['状态']}")

# 深度合并字典
def deep_merge_dicts(dict1, dict2):
    """
    深度合并两个字典
    """
    result = dict1.copy()
    
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    
    return result

# 测试深度合并
original_config = {
    "数据库": {
        "主库": {"host": "localhost", "port": 5432},
        "从库": {"host": "slave1", "port": 5432}
    },
    "缓存": {
        "redis": {"host": "127.0.0.1", "port": 6379}
    }
}

new_config = {
    "数据库": {
        "主库": {"password": "secret", "pool_size": 10},
        "备库": {"host": "backup", "port": 5432}
    },
    "日志": {
        "level": "INFO",
        "file": "/var/log/app.log"
    }
}

merged_config = deep_merge_dicts(original_config, new_config)
print(f"\n深度合并结果:")
for key, value in merged_config.items():
    print(f"  {key}: {value}")
```

## 嵌套字典遍历

### 1. 深度优先遍历

```python
print("\n=== 嵌套字典的深度遍历 ===")

def deep_traverse_dict(data, path=[], max_depth=None):
    """
    深度优先遍历嵌套字典
    """
    if max_depth is not None and len(path) >= max_depth:
        return
    
    if isinstance(data, dict):
        for key, value in data.items():
            current_path = path + [key]
            
            # 输出当前路径和值
            if isinstance(value, dict):
                print(f"{'  ' * len(path)}📁 {key}/")
                # 递归遍历子字典
                deep_traverse_dict(value, current_path, max_depth)
            else:
                print(f"{'  ' * len(path)}📄 {key}: {value}")
    else:
        # 非字典值
        path_str = ".".join(path) if path else "root"
        print(f"{'  ' * (len(path)-1)}📄 {path_str}: {data}")

print("组织结构深度遍历:")
deep_traverse_dict(organization["公司"], max_depth=4)

# 广度优先遍历
from collections import deque

def breadth_first_traverse(data, max_depth=None):
    """
    广度优先遍历嵌套字典
    """
    queue = deque([(data, [], 0)])  # (数据, 路径, 深度)
    
    while queue:
        current_data, path, depth = queue.popleft()
        
        if max_depth is not None and depth >= max_depth:
            continue
        
        if isinstance(current_data, dict):
            for key, value in current_data.items():
                current_path = path + [key]
                path_str = ".".join(current_path)
                
                if isinstance(value, dict):
                    print(f"深度{depth}: 📁 {path_str}/")
                    queue.append((value, current_path, depth + 1))
                else:
                    print(f"深度{depth}: 📄 {path_str}: {value}")

print("\n广度优先遍历（前20项）:")
breadth_first_traverse(organization["公司"], max_depth=3)

# 按条件遍历
def conditional_traverse(data, condition_func, action_func, path=[]):
    """
    按条件遍历嵌套字典
    """
    if isinstance(data, dict):
        for key, value in data.items():
            current_path = path + [key]
            
            # 检查条件
            if condition_func(current_path, key, value):
                action_func(current_path, key, value)
            
            # 递归遍历
            conditional_traverse(value, condition_func, action_func, current_path)

# 查找所有数值类型的字段
numeric_fields = []

def is_numeric_field(path, key, value):
    return isinstance(value, (int, float))

def collect_numeric_field(path, key, value):
    numeric_fields.append({
        "path": ".".join(path),
        "key": key,
        "value": value
    })

conditional_traverse(organization, is_numeric_field, collect_numeric_field)

print(f"\n数值字段统计:")
for field in numeric_fields[:10]:  # 只显示前10个
    print(f"  {field['path']}: {field['value']}")

# 统计信息
total_numeric_value = sum(field["value"] for field in numeric_fields)
print(f"\n数值字段总数: {len(numeric_fields)}")
print(f"数值总和: {total_numeric_value}")
print(f"平均值: {total_numeric_value / len(numeric_fields):.2f}")
```

### 2. 搜索和过滤

```python
print("\n=== 嵌套字典的搜索和过滤 ===")

class NestedDictSearcher:
    def __init__(self, data):
        self.data = data
    
    def search_by_key(self, target_key, case_sensitive=True):
        """
        按键名搜索
        """
        results = []
        
        def _search(data, path=[]):
            if isinstance(data, dict):
                for key, value in data.items():
                    current_path = path + [key]
                    
                    # 检查键名匹配
                    if case_sensitive:
                        match = key == target_key
                    else:
                        match = key.lower() == target_key.lower()
                    
                    if match:
                        results.append({
                            "path": ".".join(current_path),
                            "key": key,
                            "value": value
                        })
                    
                    # 递归搜索
                    _search(value, current_path)
        
        _search(self.data)
        return results
    
    def search_by_value(self, target_value, exact_match=True):
        """
        按值搜索
        """
        results = []
        
        def _search(data, path=[]):
            if isinstance(data, dict):
                for key, value in data.items():
                    current_path = path + [key]
                    
                    # 检查值匹配
                    if exact_match:
                        match = value == target_value
                    else:
                        # 模糊匹配（字符串包含）
                        if isinstance(value, str) and isinstance(target_value, str):
                            match = target_value.lower() in value.lower()
                        else:
                            match = value == target_value
                    
                    if match:
                        results.append({
                            "path": ".".join(current_path),
                            "key": key,
                            "value": value
                        })
                    
                    # 递归搜索
                    _search(value, current_path)
        
        _search(self.data)
        return results
    
    def search_by_pattern(self, pattern_func):
        """
        按自定义模式搜索
        """
        results = []
        
        def _search(data, path=[]):
            if isinstance(data, dict):
                for key, value in data.items():
                    current_path = path + [key]
                    
                    # 应用模式函数
                    if pattern_func(current_path, key, value):
                        results.append({
                            "path": ".".join(current_path),
                            "key": key,
                            "value": value
                        })
                    
                    # 递归搜索
                    _search(value, current_path)
        
        _search(self.data)
        return results
    
    def filter_by_depth(self, min_depth=None, max_depth=None):
        """
        按深度过滤
        """
        results = []
        
        def _filter(data, path=[], depth=0):
            if isinstance(data, dict):
                for key, value in data.items():
                    current_path = path + [key]
                    current_depth = depth + 1
                    
                    # 检查深度条件
                    depth_match = True
                    if min_depth is not None and current_depth < min_depth:
                        depth_match = False
                    if max_depth is not None and current_depth > max_depth:
                        depth_match = False
                    
                    if depth_match:
                        results.append({
                            "path": ".".join(current_path),
                            "key": key,
                            "value": value,
                            "depth": current_depth
                        })
                    
                    # 递归过滤
                    _filter(value, current_path, current_depth)
        
        _filter(self.data)
        return results

# 测试搜索器
searcher = NestedDictSearcher(organization)

# 按键名搜索
name_results = searcher.search_by_key("名称")
print(f"搜索'名称'字段:")
for result in name_results:
    print(f"  {result['path']}: {result['value']}")

# 按值搜索
status_results = searcher.search_by_value("进行中")
print(f"\n搜索'进行中'状态:")
for result in status_results:
    print(f"  {result['path']}: {result['value']}")

# 模糊搜索
tech_results = searcher.search_by_value("技术", exact_match=False)
print(f"\n模糊搜索'技术':")
for result in tech_results:
    print(f"  {result['path']}: {result['value']}")

# 自定义模式搜索：查找所有大于100000的数值
large_numbers = searcher.search_by_pattern(
    lambda path, key, value: isinstance(value, (int, float)) and value > 100000
)
print(f"\n大于100000的数值:")
for result in large_numbers:
    print(f"  {result['path']}: {result['value']}")

# 按深度过滤：只看第3层的数据
third_level = searcher.filter_by_depth(min_depth=3, max_depth=3)
print(f"\n第3层数据（前10项）:")
for result in third_level[:10]:
    print(f"  深度{result['depth']} - {result['path']}: {result['value']}")

# 复杂搜索：查找所有项目相关的信息
project_pattern = lambda path, key, value: "项目" in ".".join(path) or "项目" in str(key)
project_results = searcher.search_by_pattern(project_pattern)
print(f"\n项目相关信息:")
for result in project_results:
    print(f"  {result['path']}: {result['value']}")
```

## 嵌套字典的复制和合并

### 1. 深浅拷贝

```python
print("\n=== 嵌套字典的复制 ===")

import copy

# 创建测试数据
original_data = {
    "config": {
        "database": {
            "host": "localhost",
            "credentials": ["user", "pass"]
        },
        "features": {
            "enabled": ["feature1", "feature2"]
        }
    }
}

print(f"原始数据: {original_data}")

# 浅拷贝
shallow_copy = original_data.copy()
shallow_copy["config"]["database"]["host"] = "remote_host"
shallow_copy["config"]["database"]["credentials"].append("new_cred")

print(f"\n浅拷贝修改后:")
print(f"  原始数据host: {original_data['config']['database']['host']}")
print(f"  浅拷贝host: {shallow_copy['config']['database']['host']}")
print(f"  原始数据credentials: {original_data['config']['database']['credentials']}")
print(f"  浅拷贝credentials: {shallow_copy['config']['database']['credentials']}")

# 重置数据
original_data = {
    "config": {
        "database": {
            "host": "localhost",
            "credentials": ["user", "pass"]
        },
        "features": {
            "enabled": ["feature1", "feature2"]
        }
    }
}

# 深拷贝
deep_copy = copy.deepcopy(original_data)
deep_copy["config"]["database"]["host"] = "remote_host"
deep_copy["config"]["database"]["credentials"].append("new_cred")

print(f"\n深拷贝修改后:")
print(f"  原始数据host: {original_data['config']['database']['host']}")
print(f"  深拷贝host: {deep_copy['config']['database']['host']}")
print(f"  原始数据credentials: {original_data['config']['database']['credentials']}")
print(f"  深拷贝credentials: {deep_copy['config']['database']['credentials']}")

# 自定义深拷贝函数
def custom_deep_copy(data):
    """
    自定义深拷贝函数
    """
    if isinstance(data, dict):
        return {key: custom_deep_copy(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [custom_deep_copy(item) for item in data]
    elif isinstance(data, tuple):
        return tuple(custom_deep_copy(item) for item in data)
    else:
        # 对于不可变类型，直接返回
        return data

# 测试自定义深拷贝
custom_copy = custom_deep_copy(original_data)
custom_copy["config"]["new_section"] = {"new_key": "new_value"}

print(f"\n自定义深拷贝:")
print(f"  原始数据是否有new_section: {'new_section' in original_data['config']}")
print(f"  自定义拷贝是否有new_section: {'new_section' in custom_copy['config']}")

# 选择性深拷贝
def selective_deep_copy(data, deep_copy_keys=None):
    """
    选择性深拷贝：只对指定的键进行深拷贝
    """
    if deep_copy_keys is None:
        deep_copy_keys = set()
    
    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            if key in deep_copy_keys:
                result[key] = copy.deepcopy(value)
            else:
                result[key] = value
        return result
    else:
        return data

# 测试选择性深拷贝
selective_copy = selective_deep_copy(original_data, deep_copy_keys={"database"})
selective_copy["config"]["database"]["credentials"].append("selective_cred")
selective_copy["config"]["features"]["enabled"].append("selective_feature")

print(f"\n选择性深拷贝:")
print(f"  原始credentials: {original_data['config']['database']['credentials']}")
print(f"  选择性拷贝credentials: {selective_copy['config']['database']['credentials']}")
print(f"  原始features: {original_data['config']['features']['enabled']}")
print(f"  选择性拷贝features: {selective_copy['config']['features']['enabled']}")
```

### 2. 高级合并策略

```python
print("\n=== 高级合并策略 ===")

class NestedDictMerger:
    @staticmethod
    def merge_replace(dict1, dict2):
        """
        替换合并：dict2的值完全替换dict1的值
        """
        result = copy.deepcopy(dict1)
        
        def _merge(target, source):
            for key, value in source.items():
                target[key] = copy.deepcopy(value)
        
        _merge(result, dict2)
        return result
    
    @staticmethod
    def merge_deep(dict1, dict2):
        """
        深度合并：递归合并嵌套字典
        """
        result = copy.deepcopy(dict1)
        
        def _merge(target, source):
            for key, value in source.items():
                if (key in target and 
                    isinstance(target[key], dict) and 
                    isinstance(value, dict)):
                    _merge(target[key], value)
                else:
                    target[key] = copy.deepcopy(value)
        
        _merge(result, dict2)
        return result
    
    @staticmethod
    def merge_additive(dict1, dict2):
        """
        加法合并：数值相加，列表合并，字符串连接
        """
        result = copy.deepcopy(dict1)
        
        def _merge(target, source):
            for key, value in source.items():
                if key in target:
                    if isinstance(target[key], (int, float)) and isinstance(value, (int, float)):
                        target[key] += value
                    elif isinstance(target[key], list) and isinstance(value, list):
                        target[key].extend(value)
                    elif isinstance(target[key], str) and isinstance(value, str):
                        target[key] += value
                    elif isinstance(target[key], dict) and isinstance(value, dict):
                        _merge(target[key], value)
                    else:
                        target[key] = copy.deepcopy(value)
                else:
                    target[key] = copy.deepcopy(value)
        
        _merge(result, dict2)
        return result
    
    @staticmethod
    def merge_conditional(dict1, dict2, condition_func):
        """
        条件合并：根据条件函数决定如何合并
        """
        result = copy.deepcopy(dict1)
        
        def _merge(target, source, path=[]):
            for key, value in source.items():
                current_path = path + [key]
                
                if key in target:
                    # 应用条件函数
                    merge_action = condition_func(current_path, target[key], value)
                    
                    if merge_action == "replace":
                        target[key] = copy.deepcopy(value)
                    elif merge_action == "keep":
                        pass  # 保持原值
                    elif merge_action == "merge" and isinstance(target[key], dict) and isinstance(value, dict):
                        _merge(target[key], value, current_path)
                    elif merge_action == "add" and isinstance(target[key], (int, float)) and isinstance(value, (int, float)):
                        target[key] += value
                    else:
                        target[key] = copy.deepcopy(value)
                else:
                    target[key] = copy.deepcopy(value)
        
        _merge(result, dict2)
        return result

# 测试合并策略
config1 = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "connections": 10
    },
    "features": ["feature1", "feature2"],
    "version": "1.0",
    "debug": True
}

config2 = {
    "database": {
        "host": "remote",
        "password": "secret",
        "connections": 5
    },
    "features": ["feature3", "feature4"],
    "version": "2.0",
    "cache": {
        "enabled": True,
        "ttl": 3600
    }
}

merger = NestedDictMerger()

# 替换合并
replace_result = merger.merge_replace(config1, config2)
print(f"替换合并结果:")
print(f"  数据库host: {replace_result['database']['host']}")
print(f"  数据库port: {replace_result['database'].get('port', '不存在')}")
print(f"  features: {replace_result['features']}")

# 深度合并
deep_result = merger.merge_deep(config1, config2)
print(f"\n深度合并结果:")
print(f"  数据库host: {deep_result['database']['host']}")
print(f"  数据库port: {deep_result['database']['port']}")
print(f"  数据库password: {deep_result['database']['password']}")
print(f"  features: {deep_result['features']}")

# 加法合并
additive_result = merger.merge_additive(config1, config2)
print(f"\n加法合并结果:")
print(f"  数据库connections: {additive_result['database']['connections']}")
print(f"  features: {additive_result['features']}")
print(f"  version: {additive_result['version']}")

# 条件合并
def smart_merge_condition(path, old_value, new_value):
    """
    智能合并条件
    """
    # 数值类型：选择较大的值
    if isinstance(old_value, (int, float)) and isinstance(new_value, (int, float)):
        return "replace" if new_value > old_value else "keep"
    
    # 列表类型：合并
    if isinstance(old_value, list) and isinstance(new_value, list):
        return "add"
    
    # 字典类型：递归合并
    if isinstance(old_value, dict) and isinstance(new_value, dict):
        return "merge"
    
    # 版本号：选择较新的
    if "version" in path:
        return "replace" if new_value > old_value else "keep"
    
    # 默认替换
    return "replace"

conditional_result = merger.merge_conditional(config1, config2, smart_merge_condition)
print(f"\n条件合并结果:")
print(f"  数据库connections: {conditional_result['database']['connections']}")
print(f"  features: {conditional_result['features']}")
print(f"  version: {conditional_result['version']}")
print(f"  debug: {conditional_result['debug']}")
```

## 实际应用案例

### 1. JSON配置管理器

```python
print("\n=== 实际应用：JSON配置管理器 ===")

import json
from pathlib import Path

class ConfigManager:
    def __init__(self, config_file=None):
        self.config_file = config_file
        self.config = {}
        self.defaults = {}
        self.validators = {}
        
        if config_file and Path(config_file).exists():
            self.load_config()
    
    def set_defaults(self, defaults):
        """
        设置默认配置
        """
        self.defaults = copy.deepcopy(defaults)
    
    def add_validator(self, path, validator_func):
        """
        添加配置验证器
        """
        self.validators[path] = validator_func
    
    def get(self, path, default=None):
        """
        获取配置值
        """
        keys = path.split(".")
        
        # 首先尝试从当前配置获取
        value = safe_get_nested(self.config, *keys)
        
        # 如果没有找到，尝试从默认配置获取
        if value is None:
            value = safe_get_nested(self.defaults, *keys)
        
        # 如果还是没有，返回提供的默认值
        return value if value is not None else default
    
    def set(self, path, value, validate=True):
        """
        设置配置值
        """
        if validate and path in self.validators:
            if not self.validators[path](value):
                raise ValueError(f"配置验证失败: {path} = {value}")
        
        keys = path.split(".")
        safe_set_nested(self.config, keys, value)
    
    def merge_config(self, new_config, strategy="deep"):
        """
        合并配置
        """
        merger = NestedDictMerger()
        
        if strategy == "replace":
            self.config = merger.merge_replace(self.config, new_config)
        elif strategy == "deep":
            self.config = merger.merge_deep(self.config, new_config)
        elif strategy == "additive":
            self.config = merger.merge_additive(self.config, new_config)
    
    def validate_all(self):
        """
        验证所有配置
        """
        errors = []
        
        for path, validator in self.validators.items():
            value = self.get(path)
            if value is not None and not validator(value):
                errors.append(f"配置验证失败: {path} = {value}")
        
        return errors
    
    def get_section(self, section_path):
        """
        获取配置段
        """
        keys = section_path.split(".")
        return safe_get_nested(self.config, *keys, default={})
    
    def list_all_settings(self):
        """
        列出所有配置项
        """
        accessor = NestedDictAccessor(self.config)
        return accessor.list_all_paths()
    
    def export_config(self, include_defaults=False):
        """
        导出配置
        """
        if include_defaults:
            merger = NestedDictMerger()
            return merger.merge_deep(self.defaults, self.config)
        else:
            return copy.deepcopy(self.config)
    
    def load_config(self):
        """
        从文件加载配置
        """
        if self.config_file and Path(self.config_file).exists():
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
    
    def save_config(self):
        """
        保存配置到文件
        """
        if self.config_file:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)

# 测试配置管理器
config_manager = ConfigManager()

# 设置默认配置
default_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "timeout": 30,
        "pool_size": 10
    },
    "cache": {
        "enabled": True,
        "ttl": 3600,
        "max_size": 1000
    },
    "logging": {
        "level": "INFO",
        "file": "/var/log/app.log",
        "max_size": "10MB"
    }
}

config_manager.set_defaults(default_config)

# 添加验证器
config_manager.add_validator("database.port", lambda x: isinstance(x, int) and 1 <= x <= 65535)
config_manager.add_validator("cache.ttl", lambda x: isinstance(x, int) and x > 0)
config_manager.add_validator("logging.level", lambda x: x in ["DEBUG", "INFO", "WARNING", "ERROR"])

# 设置一些配置
config_manager.set("database.host", "production-db")
config_manager.set("database.password", "secret123")
config_manager.set("cache.enabled", False)
config_manager.set("app.name", "我的应用")
config_manager.set("app.version", "1.0.0")

print("配置管理器测试:")
print(f"  数据库主机: {config_manager.get('database.host')}")
print(f"  数据库端口: {config_manager.get('database.port')}")
print(f"  缓存启用: {config_manager.get('cache.enabled')}")
print(f"  应用名称: {config_manager.get('app.name')}")
print(f"  不存在的配置: {config_manager.get('nonexistent.config', '默认值')}")

# 验证配置
validation_errors = config_manager.validate_all()
if validation_errors:
    print(f"\n配置验证错误: {validation_errors}")
else:
    print("\n所有配置验证通过")

# 导出完整配置
full_config = config_manager.export_config(include_defaults=True)
print(f"\n完整配置项数量: {len(NestedDictAccessor(full_config).list_all_paths())}")
```

### 2. 数据转换和清洗

```python
print("\n=== 实际应用：数据转换和清洗 ===")

class DataProcessor:
    def __init__(self):
        self.transformers = {}
        self.cleaners = {}
    
    def add_transformer(self, path_pattern, transform_func):
        """
        添加数据转换器
        """
        self.transformers[path_pattern] = transform_func
    
    def add_cleaner(self, condition_func, clean_func):
        """
        添加数据清洗器
        """
        self.cleaners[condition_func] = clean_func
    
    def process_data(self, data):
        """
        处理数据
        """
        # 深拷贝以避免修改原数据
        result = copy.deepcopy(data)
        
        # 应用转换器
        self._apply_transformers(result)
        
        # 应用清洗器
        self._apply_cleaners(result)
        
        return result
    
    def _apply_transformers(self, data, path=[]):
        """
        应用转换器
        """
        if isinstance(data, dict):
            for key, value in data.items():
                current_path = path + [key]
                path_str = ".".join(current_path)
                
                # 检查是否有匹配的转换器
                for pattern, transformer in self.transformers.items():
                    if self._match_pattern(path_str, pattern):
                        data[key] = transformer(value)
                        break
                else:
                    # 递归处理嵌套结构
                    self._apply_transformers(value, current_path)
    
    def _apply_cleaners(self, data, path=[]):
        """
        应用清洗器
        """
        if isinstance(data, dict):
            keys_to_remove = []
            
            for key, value in data.items():
                current_path = path + [key]
                
                # 检查清洗条件
                for condition, cleaner in self.cleaners.items():
                    if condition(current_path, key, value):
                        cleaned_value = cleaner(current_path, key, value)
                        if cleaned_value is None:
                            keys_to_remove.append(key)
                        else:
                            data[key] = cleaned_value
                        break
                else:
                    # 递归处理嵌套结构
                    self._apply_cleaners(value, current_path)
            
            # 移除标记为删除的键
            for key in keys_to_remove:
                del data[key]
    
    def _match_pattern(self, path, pattern):
        """
        简单的路径模式匹配
        """
        if "*" in pattern:
            # 支持通配符
            import re
            regex_pattern = pattern.replace("*", ".*")
            return re.match(regex_pattern, path) is not None
        else:
            return path == pattern

# 创建测试数据
raw_data = {
    "users": {
        "user1": {
            "name": "  张三  ",
            "email": "ZHANGSAN@EMAIL.COM",
            "age": "25",
            "phone": "123-456-7890",
            "address": {
                "city": "  北京  ",
                "zipcode": "100000"
            },
            "preferences": {
                "theme": "dark",
                "language": "zh-CN",
                "notifications": "true"
            }
        },
        "user2": {
            "name": "李四",
            "email": "lisi@email.com",
            "age": "invalid_age",
            "phone": "",
            "address": {
                "city": "上海",
                "zipcode": "200000"
            },
            "preferences": {
                "theme": "light",
                "language": "en-US",
                "notifications": "false"
            }
        }
    },
    "metadata": {
        "created_at": "2024-01-01T00:00:00Z",
        "version": "1.0",
        "debug_info": "这是调试信息，生产环境应该移除"
    }
}

# 创建数据处理器
processor = DataProcessor()

# 添加转换器
processor.add_transformer("*.name", lambda x: x.strip() if isinstance(x, str) else x)
processor.add_transformer("*.email", lambda x: x.lower().strip() if isinstance(x, str) else x)
processor.add_transformer("*.age", lambda x: int(x) if isinstance(x, str) and x.isdigit() else None)
processor.add_transformer("*.city", lambda x: x.strip() if isinstance(x, str) else x)
processor.add_transformer("*.notifications", lambda x: x.lower() == "true" if isinstance(x, str) else x)

# 添加清洗器
processor.add_cleaner(
    lambda path, key, value: key == "phone" and (not value or value.strip() == ""),
    lambda path, key, value: None  # 删除空电话号码
)

processor.add_cleaner(
    lambda path, key, value: key == "age" and value is None,
    lambda path, key, value: None  # 删除无效年龄
)

processor.add_cleaner(
    lambda path, key, value: "debug" in key.lower(),
    lambda path, key, value: None  # 删除调试信息
)

# 处理数据
processed_data = processor.process_data(raw_data)

print("数据处理结果:")
print(f"原始数据: {raw_data}")
print(f"\n处理后数据: {processed_data}")

# 比较处理前后的差异
print("\n处理差异:")
print(f"  user1姓名: '{raw_data['users']['user1']['name']}' -> '{processed_data['users']['user1']['name']}'")
print(f"  user1邮箱: '{raw_data['users']['user1']['email']}' -> '{processed_data['users']['user1']['email']}'")
print(f"  user1年龄: '{raw_data['users']['user1']['age']}' -> {processed_data['users']['user1']['age']}")
print(f"  user2电话: 存在 -> {'存在' if 'phone' in processed_data['users']['user2'] else '已删除'}")
print(f"  调试信息: 存在 -> {'存在' if 'debug_info' in processed_data['metadata'] else '已删除'}")
```

## 性能考虑和最佳实践

### 1. 性能优化技巧

```python
print("\n=== 性能优化技巧 ===")

import time
from functools import lru_cache

# 创建大型嵌套字典进行性能测试
def create_large_nested_dict(depth=5, width=10):
    """
    创建大型嵌套字典
    """
    if depth == 0:
        return f"value_{width}"
    
    return {
        f"key_{i}": create_large_nested_dict(depth-1, i)
        for i in range(width)
    }

large_dict = create_large_nested_dict(4, 5)
print(f"创建了深度4，宽度5的嵌套字典")

# 性能测试：不同访问方法的比较
def time_function(func, *args, **kwargs):
    """
    测量函数执行时间
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time

# 方法1：直接访问（可能抛出异常）
def direct_access(data):
    try:
        return data["key_0"]["key_1"]["key_2"]["key_3"]
    except KeyError:
        return None

# 方法2：使用get()链
def get_chain_access(data):
    return (data.get("key_0", {})
           .get("key_1", {})
           .get("key_2", {})
           .get("key_3", None))

# 方法3：使用安全访问函数
def safe_access(data):
    return safe_get_nested(data, "key_0", "key_1", "key_2", "key_3")

# 方法4：使用缓存的访问器
class CachedAccessor:
    def __init__(self, data):
        self.data = data
        self._cache = {}
    
    @lru_cache(maxsize=1000)
    def get_cached(self, path):
        keys = path.split(".")
        return safe_get_nested(self.data, *keys)

cached_accessor = CachedAccessor(large_dict)

# 性能测试
test_iterations = 10000

print(f"\n性能测试（{test_iterations}次迭代）:")

# 测试直接访问
_, direct_time = time_function(
    lambda: [direct_access(large_dict) for _ in range(test_iterations)]
)
print(f"  直接访问: {direct_time:.4f}秒")

# 测试get链访问
_, get_chain_time = time_function(
    lambda: [get_chain_access(large_dict) for _ in range(test_iterations)]
)
print(f"  get链访问: {get_chain_time:.4f}秒")

# 测试安全访问
_, safe_time = time_function(
    lambda: [safe_access(large_dict) for _ in range(test_iterations)]
)
print(f"  安全访问: {safe_time:.4f}秒")

# 测试缓存访问
_, cached_time = time_function(
    lambda: [cached_accessor.get_cached("key_0.key_1.key_2.key_3") for _ in range(test_iterations)]
)
print(f"  缓存访问: {cached_time:.4f}秒")

# 内存使用优化
print("\n内存使用优化建议:")
print("1. 使用__slots__减少内存占用")
print("2. 避免不必要的深拷贝")
print("3. 使用生成器进行大数据遍历")
print("4. 及时清理不需要的引用")
print("5. 考虑使用更紧凑的数据结构")
```

## 学习要点

### 核心概念
1. **嵌套字典结构**：理解多层字典的组织方式
2. **安全访问**：避免KeyError的访问方法
3. **深度遍历**：递归处理嵌套结构
4. **复制策略**：深浅拷贝的区别和应用
5. **合并策略**：不同场景下的合并方法

### 实用技巧
1. **路径表达式**：使用字符串路径访问嵌套数据
2. **条件处理**：根据条件进行批量操作
3. **数据验证**：确保嵌套数据的完整性
4. **性能优化**：选择合适的访问和修改方法
5. **错误处理**：优雅地处理访问异常

### 最佳实践
1. **使用类型提示**：提高代码可读性
2. **编写测试**：确保嵌套操作的正确性
3. **文档化**：记录复杂的嵌套结构
4. **模块化**：将嵌套操作封装成可复用的函数
5. **性能监控**：关注大型嵌套结构的性能

## 练习题

### 基础练习
1. 创建一个表示学校组织结构的嵌套字典
2. 实现安全的嵌套字典访问函数
3. 编写深度遍历函数，统计所有数值的总和

### 进阶练习
1. 实现嵌套字典的扁平化和反扁平化
2. 创建支持通配符的路径搜索功能
3. 实现嵌套字典的差异比较工具

### 实战练习
1. 构建配置文件管理系统
2. 实现JSON数据的清洗和转换工具
3. 创建嵌套数据的可视化展示工具

## 下一步学习

学习完嵌套字典后，建议继续学习：
1. **字典推导式**：高效创建和转换字典
2. **综合练习**：实际项目中的字典应用
3. **高级数据结构**：collections模块的高级字典类型
4. **JSON处理**：与外部数据格式的交互
5. **数据库操作**：字典在数据持久化中的应用