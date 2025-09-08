# 字典的遍历和迭代详解

## 学习目标

- 掌握字典的各种遍历方式
- 理解字典迭代的性能特点
- 学习条件遍历和过滤技巧
- 掌握字典推导式在遍历中的应用
- 了解安全遍历和修改的方法
- 学习多字典同时遍历的技巧

## 字典遍历基础

字典遍历是处理字典数据的核心操作。Python提供了多种遍历方式，每种都有其特定的用途和优势。

## 基本遍历方式

### 1. 遍历键（Keys）

```python
# 创建示例字典
student_grades = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
    "赵六": 96,
    "钱七": 88
}

print("=== 遍历键的不同方式 ===")

# 方式1：直接遍历字典（推荐）
print("方式1 - 直接遍历:")
for name in student_grades:
    print(f"  学生: {name}")

# 方式2：使用keys()方法
print("\n方式2 - 使用keys():")
for name in student_grades.keys():
    print(f"  学生: {name}")

# 方式3：转换为列表（不推荐，除非需要索引）
print("\n方式3 - 转换为列表:")
names_list = list(student_grades.keys())
for i, name in enumerate(names_list):
    print(f"  {i}: {name}")

# 获取键的数量
print(f"\n学生总数: {len(student_grades)}")

# 检查特定键是否存在
if "张三" in student_grades:
    print("张三在班级中")

# 遍历时进行条件判断
print("\n姓'王'的学生:")
for name in student_grades:
    if name.startswith("王"):
        print(f"  找到: {name}")
```

### 2. 遍历值（Values）

```python
print("\n=== 遍历值的不同方式 ===")

# 基本遍历值
print("所有成绩:")
for grade in student_grades.values():
    print(f"  成绩: {grade}")

# 值的统计分析
all_grades = list(student_grades.values())
print(f"\n成绩统计:")
print(f"  最高分: {max(all_grades)}")
print(f"  最低分: {min(all_grades)}")
print(f"  平均分: {sum(all_grades) / len(all_grades):.2f}")
print(f"  总分: {sum(all_grades)}")

# 条件统计
high_grades = [grade for grade in student_grades.values() if grade >= 90]
low_grades = [grade for grade in student_grades.values() if grade < 80]

print(f"\n优秀成绩(>=90): {high_grades}")
print(f"需要提高(<80): {low_grades}")
print(f"优秀率: {len(high_grades) / len(all_grades) * 100:.1f}%")

# 成绩分布统计
grade_ranges = {
    "优秀(90-100)": 0,
    "良好(80-89)": 0,
    "及格(60-79)": 0,
    "不及格(<60)": 0
}

for grade in student_grades.values():
    if grade >= 90:
        grade_ranges["优秀(90-100)"] += 1
    elif grade >= 80:
        grade_ranges["良好(80-89)"] += 1
    elif grade >= 60:
        grade_ranges["及格(60-79)"] += 1
    else:
        grade_ranges["不及格(<60)"] += 1

print("\n成绩分布:")
for range_name, count in grade_ranges.items():
    print(f"  {range_name}: {count}人")
```

### 3. 遍历键值对（Items）

```python
print("\n=== 遍历键值对的方式 ===")

# 基本键值对遍历
print("学生成绩单:")
for name, grade in student_grades.items():
    print(f"  {name}: {grade}分")

# 带索引的遍历
print("\n带序号的成绩单:")
for index, (name, grade) in enumerate(student_grades.items(), 1):
    print(f"  {index}. {name}: {grade}分")

# 条件遍历和处理
print("\n成绩评级:")
for name, grade in student_grades.items():
    if grade >= 90:
        level = "优秀"
    elif grade >= 80:
        level = "良好"
    elif grade >= 60:
        level = "及格"
    else:
        level = "不及格"
    
    print(f"  {name}: {grade}分 ({level})")

# 查找特定条件的学生
print("\n优秀学生名单:")
excellent_students = []
for name, grade in student_grades.items():
    if grade >= 90:
        excellent_students.append((name, grade))
        print(f"  {name}: {grade}分")

# 创建新的数据结构
student_info = {}
for name, grade in student_grades.items():
    student_info[name] = {
        "grade": grade,
        "level": "优秀" if grade >= 90 else "良好" if grade >= 80 else "及格" if grade >= 60 else "不及格",
        "pass": grade >= 60
    }

print(f"\n详细学生信息: {student_info}")
```

## 高级遍历技巧

### 1. 排序遍历

```python
print("\n=== 排序遍历 ===")

# 按键排序
print("按姓名排序:")
for name in sorted(student_grades.keys()):
    print(f"  {name}: {student_grades[name]}分")

# 按值排序（升序）
print("\n按成绩排序（低到高）:")
for name, grade in sorted(student_grades.items(), key=lambda x: x[1]):
    print(f"  {name}: {grade}分")

# 按值排序（降序）
print("\n按成绩排序（高到低）:")
for name, grade in sorted(student_grades.items(), key=lambda x: x[1], reverse=True):
    print(f"  {name}: {grade}分")

# 复杂排序：先按成绩降序，再按姓名升序
print("\n复合排序（成绩降序，姓名升序）:")
for name, grade in sorted(student_grades.items(), key=lambda x: (-x[1], x[0])):
    print(f"  {name}: {grade}分")

# 自定义排序函数
def custom_sort_key(item):
    name, grade = item
    # 优先级：成绩 > 姓名长度 > 字母顺序
    return (-grade, len(name), name)

print("\n自定义排序:")
for name, grade in sorted(student_grades.items(), key=custom_sort_key):
    print(f"  {name}: {grade}分")

# 获取前N名
top_n = 3
print(f"\n前{top_n}名:")
top_students = sorted(student_grades.items(), key=lambda x: x[1], reverse=True)[:top_n]
for rank, (name, grade) in enumerate(top_students, 1):
    print(f"  第{rank}名: {name} - {grade}分")
```

### 2. 条件遍历和过滤

```python
print("\n=== 条件遍历和过滤 ===")

# 创建更复杂的数据
student_data = {
    "张三": {"grade": 85, "age": 20, "major": "计算机"},
    "李四": {"grade": 92, "age": 19, "major": "数学"},
    "王五": {"grade": 78, "age": 21, "major": "物理"},
    "赵六": {"grade": 96, "age": 20, "major": "计算机"},
    "钱七": {"grade": 88, "age": 22, "major": "数学"}
}

# 条件过滤：计算机专业的学生
print("计算机专业学生:")
for name, info in student_data.items():
    if info["major"] == "计算机":
        print(f"  {name}: {info['grade']}分, {info['age']}岁")

# 多条件过滤：年龄20岁且成绩大于85的学生
print("\n20岁且成绩>85的学生:")
for name, info in student_data.items():
    if info["age"] == 20 and info["grade"] > 85:
        print(f"  {name}: {info}")

# 使用生成器表达式进行过滤
print("\n优秀学生（成绩>=90）:")
excellent = (name for name, info in student_data.items() if info["grade"] >= 90)
for name in excellent:
    print(f"  {name}: {student_data[name]['grade']}分")

# 复杂条件过滤函数
def filter_students(data, **criteria):
    """
    根据条件过滤学生
    """
    result = []
    for name, info in data.items():
        match = True
        for key, value in criteria.items():
            if key not in info or info[key] != value:
                match = False
                break
        if match:
            result.append((name, info))
    return result

# 使用过滤函数
cs_students = filter_students(student_data, major="计算机")
print(f"\n计算机专业学生: {cs_students}")

young_excellent = filter_students(student_data, age=20)
print(f"20岁学生: {young_excellent}")

# 范围过滤
def filter_by_range(data, field, min_val=None, max_val=None):
    """
    按范围过滤
    """
    result = []
    for name, info in data.items():
        value = info.get(field)
        if value is not None:
            if (min_val is None or value >= min_val) and (max_val is None or value <= max_val):
                result.append((name, info))
    return result

# 成绩在80-90之间的学生
good_students = filter_by_range(student_data, "grade", 80, 90)
print(f"\n成绩80-90分的学生: {len(good_students)}人")
for name, info in good_students:
    print(f"  {name}: {info['grade']}分")
```

### 3. 字典推导式遍历

```python
print("\n=== 字典推导式遍历 ===")

# 基本字典推导式
grade_levels = {name: "优秀" if grade >= 90 else "良好" if grade >= 80 else "及格" 
                for name, grade in student_grades.items()}
print(f"成绩等级: {grade_levels}")

# 条件字典推导式
excellent_grades = {name: grade for name, grade in student_grades.items() if grade >= 90}
print(f"优秀学生: {excellent_grades}")

# 值转换
grade_percentages = {name: f"{grade}%" for name, grade in student_grades.items()}
print(f"百分比格式: {grade_percentages}")

# 复杂转换
student_summary = {
    name: {
        "score": info["grade"],
        "status": "优秀" if info["grade"] >= 90 else "良好" if info["grade"] >= 80 else "及格",
        "age_group": "年轻" if info["age"] <= 20 else "成熟"
    }
    for name, info in student_data.items()
}
print(f"\n学生摘要: {student_summary}")

# 嵌套字典推导式
major_stats = {
    major: {
        "count": len([1 for info in student_data.values() if info["major"] == major]),
        "avg_grade": sum(info["grade"] for info in student_data.values() if info["major"] == major) / 
                    len([1 for info in student_data.values() if info["major"] == major])
    }
    for major in set(info["major"] for info in student_data.values())
}
print(f"\n专业统计: {major_stats}")

# 键值互换
grade_to_name = {grade: name for name, grade in student_grades.items()}
print(f"\n成绩到姓名映射: {grade_to_name}")

# 分组字典推导式
from collections import defaultdict

# 按专业分组
major_groups = defaultdict(list)
for name, info in student_data.items():
    major_groups[info["major"]].append(name)

major_groups = dict(major_groups)  # 转换为普通字典
print(f"\n按专业分组: {major_groups}")

# 使用字典推导式实现分组
major_groups_comp = {
    major: [name for name, info in student_data.items() if info["major"] == major]
    for major in set(info["major"] for info in student_data.values())
}
print(f"推导式分组: {major_groups_comp}")
```

## 嵌套字典遍历

### 1. 基本嵌套遍历

```python
print("\n=== 嵌套字典遍历 ===")

# 创建嵌套字典
company_data = {
    "技术部": {
        "张工": {"salary": 15000, "experience": 3, "skills": ["Python", "Java"]},
        "李工": {"salary": 18000, "experience": 5, "skills": ["JavaScript", "React"]}
    },
    "销售部": {
        "王经理": {"salary": 12000, "experience": 4, "skills": ["沟通", "谈判"]},
        "赵主管": {"salary": 10000, "experience": 2, "skills": ["客户服务"]}
    },
    "人事部": {
        "钱总监": {"salary": 20000, "experience": 8, "skills": ["招聘", "培训", "管理"]}
    }
}

# 基本嵌套遍历
print("公司员工信息:")
for department, employees in company_data.items():
    print(f"\n{department}:")
    for name, info in employees.items():
        print(f"  {name}: 薪资{info['salary']}, 经验{info['experience']}年")
        print(f"    技能: {', '.join(info['skills'])}")

# 统计信息
total_employees = 0
total_salary = 0
all_skills = set()

for department, employees in company_data.items():
    dept_count = len(employees)
    dept_salary = sum(emp['salary'] for emp in employees.values())
    
    print(f"\n{department}统计:")
    print(f"  员工数: {dept_count}")
    print(f"  总薪资: {dept_salary}")
    print(f"  平均薪资: {dept_salary / dept_count:.0f}")
    
    total_employees += dept_count
    total_salary += dept_salary
    
    # 收集技能
    for emp in employees.values():
        all_skills.update(emp['skills'])

print(f"\n公司总统计:")
print(f"  总员工数: {total_employees}")
print(f"  总薪资支出: {total_salary}")
print(f"  平均薪资: {total_salary / total_employees:.0f}")
print(f"  技能种类: {len(all_skills)}")
print(f"  所有技能: {sorted(all_skills)}")
```

### 2. 深度遍历和搜索

```python
print("\n=== 深度遍历和搜索 ===")

def deep_traverse(data, path=""):
    """
    深度遍历嵌套字典
    """
    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}.{key}" if path else key
            if isinstance(value, dict):
                yield from deep_traverse(value, current_path)
            else:
                yield (current_path, value)
    else:
        yield (path, data)

# 遍历所有叶子节点
print("所有数据路径:")
for path, value in deep_traverse(company_data):
    print(f"  {path}: {value}")

# 搜索特定值
def search_in_nested_dict(data, search_value, path=""):
    """
    在嵌套字典中搜索值
    """
    results = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}.{key}" if path else key
            if value == search_value:
                results.append(current_path)
            elif isinstance(value, dict):
                results.extend(search_in_nested_dict(value, search_value, current_path))
            elif isinstance(value, list) and search_value in value:
                results.append(current_path)
    
    return results

# 搜索薪资为15000的员工
salary_paths = search_in_nested_dict(company_data, 15000)
print(f"\n薪资15000的路径: {salary_paths}")

# 搜索包含Python技能的员工
python_paths = search_in_nested_dict(company_data, "Python")
print(f"Python技能路径: {python_paths}")

# 按条件搜索
def find_employees_by_condition(data, condition_func):
    """
    按条件查找员工
    """
    results = []
    
    for department, employees in data.items():
        for name, info in employees.items():
            if condition_func(info):
                results.append((department, name, info))
    
    return results

# 查找高薪员工（薪资>15000）
high_salary = find_employees_by_condition(
    company_data, 
    lambda info: info['salary'] > 15000
)
print(f"\n高薪员工:")
for dept, name, info in high_salary:
    print(f"  {dept} - {name}: {info['salary']}")

# 查找有经验的员工（经验>=5年）
experienced = find_employees_by_condition(
    company_data,
    lambda info: info['experience'] >= 5
)
print(f"\n经验丰富员工:")
for dept, name, info in experienced:
    print(f"  {dept} - {name}: {info['experience']}年经验")
```

## 安全遍历和修改

### 1. 遍历时修改的问题

```python
print("\n=== 安全遍历和修改 ===")

# 创建测试字典
test_scores = {"A": 85, "B": 45, "C": 92, "D": 38, "E": 76}
print(f"原始分数: {test_scores}")

# 错误的做法：遍历时直接修改字典
# 这会导致RuntimeError: dictionary changed size during iteration
# for key in test_scores:
#     if test_scores[key] < 60:
#         del test_scores[key]  # 错误！

# 正确做法1：先收集要删除的键
keys_to_delete = []
for key, score in test_scores.items():
    if score < 60:
        keys_to_delete.append(key)

for key in keys_to_delete:
    del test_scores[key]

print(f"删除不及格后: {test_scores}")

# 恢复测试数据
test_scores = {"A": 85, "B": 45, "C": 92, "D": 38, "E": 76}

# 正确做法2：使用字典推导式创建新字典
passing_scores = {key: score for key, score in test_scores.items() if score >= 60}
print(f"及格分数（新字典）: {passing_scores}")

# 正确做法3：使用list()创建键的副本
test_scores_copy = test_scores.copy()
for key in list(test_scores_copy.keys()):
    if test_scores_copy[key] < 60:
        del test_scores_copy[key]

print(f"删除不及格（副本方法）: {test_scores_copy}")

# 安全的修改函数
def safe_modify_dict(dictionary, condition_func, action_func):
    """
    安全地修改字典
    condition_func: 判断条件的函数
    action_func: 执行动作的函数（modify/delete）
    """
    keys_to_process = []
    
    # 第一遍：收集需要处理的键
    for key, value in dictionary.items():
        if condition_func(key, value):
            keys_to_process.append(key)
    
    # 第二遍：执行操作
    for key in keys_to_process:
        action_func(dictionary, key)

# 测试安全修改
test_data = {"item1": 10, "item2": 25, "item3": 5, "item4": 30}
print(f"\n修改前: {test_data}")

# 将小于20的值翻倍
safe_modify_dict(
    test_data,
    lambda k, v: v < 20,
    lambda d, k: d.update({k: d[k] * 2})
)
print(f"翻倍后: {test_data}")

# 删除大于40的项
safe_modify_dict(
    test_data,
    lambda k, v: v > 40,
    lambda d, k: d.pop(k)
)
print(f"删除后: {test_data}")
```

### 2. 并发安全的遍历

```python
print("\n=== 并发安全遍历 ===")

import threading
import time
from collections import defaultdict

class ThreadSafeDict:
    """
    线程安全的字典包装器
    """
    def __init__(self, initial_data=None):
        self._data = initial_data or {}
        self._lock = threading.RLock()
    
    def safe_iterate(self):
        """
        安全的迭代方法
        """
        with self._lock:
            # 创建数据的快照
            return list(self._data.items())
    
    def safe_get(self, key, default=None):
        with self._lock:
            return self._data.get(key, default)
    
    def safe_set(self, key, value):
        with self._lock:
            self._data[key] = value
    
    def safe_delete(self, key):
        with self._lock:
            return self._data.pop(key, None)
    
    def safe_update(self, updates):
        with self._lock:
            self._data.update(updates)
    
    def __str__(self):
        with self._lock:
            return str(self._data)

# 测试线程安全字典
thread_safe_dict = ThreadSafeDict({"counter": 0, "data": "initial"})

def worker_thread(thread_id, safe_dict):
    """
    工作线程函数
    """
    for i in range(5):
        # 安全读取
        current_counter = safe_dict.safe_get("counter", 0)
        
        # 模拟处理时间
        time.sleep(0.01)
        
        # 安全更新
        safe_dict.safe_set("counter", current_counter + 1)
        safe_dict.safe_set(f"thread_{thread_id}_item_{i}", f"value_{i}")
        
        print(f"线程{thread_id}: 更新计数器到 {current_counter + 1}")

# 创建并启动多个线程
threads = []
for i in range(3):
    thread = threading.Thread(target=worker_thread, args=(i, thread_safe_dict))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print(f"\n最终结果: {thread_safe_dict}")

# 安全遍历最终数据
print("\n安全遍历结果:")
for key, value in thread_safe_dict.safe_iterate():
    print(f"  {key}: {value}")
```

## 多字典同时遍历

### 1. 使用zip()同时遍历

```python
print("\n=== 多字典同时遍历 ===")

# 创建相关的字典
student_names = {1: "张三", 2: "李四", 3: "王五", 4: "赵六"}
student_grades = {1: 85, 2: 92, 3: 78, 4: 96}
student_ages = {1: 20, 2: 19, 3: 21, 4: 20}

# 同时遍历多个字典（按键）
print("学生完整信息:")
for student_id in student_names.keys():
    name = student_names.get(student_id, "未知")
    grade = student_grades.get(student_id, 0)
    age = student_ages.get(student_id, 0)
    print(f"  ID{student_id}: {name}, {age}岁, {grade}分")

# 使用zip同时遍历值
print("\n使用zip遍历:")
for name, grade, age in zip(student_names.values(), student_grades.values(), student_ages.values()):
    print(f"  {name}: {age}岁, {grade}分")

# 同时遍历键值对
print("\n同时遍历键值对:")
for (id1, name), (id2, grade), (id3, age) in zip(
    student_names.items(), 
    student_grades.items(), 
    student_ages.items()
):
    if id1 == id2 == id3:  # 确保ID一致
        print(f"  {name}(ID:{id1}): {age}岁, {grade}分")

# 处理不同长度的字典
from itertools import zip_longest

partial_info = {1: "备注1", 3: "备注3"}  # 只有部分学生有备注

print("\n处理不完整数据:")
for student_id, name in student_names.items():
    grade = student_grades.get(student_id, "无成绩")
    age = student_ages.get(student_id, "无年龄")
    note = partial_info.get(student_id, "无备注")
    print(f"  {name}: 年龄{age}, 成绩{grade}, {note}")
```

### 2. 字典合并和比较遍历

```python
print("\n=== 字典合并和比较遍历 ===")

# 创建不同版本的配置
config_v1 = {
    "debug": False,
    "timeout": 30,
    "retries": 3,
    "host": "localhost"
}

config_v2 = {
    "debug": True,
    "timeout": 60,
    "retries": 3,
    "host": "localhost",
    "ssl": True
}

# 比较两个配置
def compare_configs(config1, config2, name1="配置1", name2="配置2"):
    """
    比较两个配置字典
    """
    all_keys = set(config1.keys()) | set(config2.keys())
    
    print(f"\n{name1} vs {name2} 比较:")
    
    for key in sorted(all_keys):
        val1 = config1.get(key, "<不存在>")
        val2 = config2.get(key, "<不存在>")
        
        if val1 == val2:
            status = "相同"
        elif key not in config1:
            status = "新增"
        elif key not in config2:
            status = "删除"
        else:
            status = "修改"
        
        print(f"  {key}: {val1} -> {val2} ({status})")

compare_configs(config_v1, config_v2, "V1", "V2")

# 合并多个字典
def merge_dicts(*dicts, conflict_resolver=None):
    """
    合并多个字典，处理冲突
    """
    result = {}
    
    for i, d in enumerate(dicts):
        for key, value in d.items():
            if key in result:
                if conflict_resolver:
                    result[key] = conflict_resolver(result[key], value, key)
                else:
                    result[key] = value  # 后面的覆盖前面的
            else:
                result[key] = value
    
    return result

# 不同的冲突解决策略
def keep_first(old_val, new_val, key):
    return old_val

def keep_last(old_val, new_val, key):
    return new_val

def merge_lists(old_val, new_val, key):
    if isinstance(old_val, list) and isinstance(new_val, list):
        return old_val + new_val
    return new_val

def prefer_higher(old_val, new_val, key):
    if isinstance(old_val, (int, float)) and isinstance(new_val, (int, float)):
        return max(old_val, new_val)
    return new_val

# 测试合并策略
dict1 = {"a": 1, "b": [1, 2], "c": "old"}
dict2 = {"b": [3, 4], "c": "new", "d": 4}
dict3 = {"a": 5, "e": "extra"}

print("\n合并结果（保持最后）:")
merged_last = merge_dicts(dict1, dict2, dict3, conflict_resolver=keep_last)
print(f"  {merged_last}")

print("\n合并结果（保持最高值）:")
merged_higher = merge_dicts(dict1, dict2, dict3, conflict_resolver=prefer_higher)
print(f"  {merged_higher}")

print("\n合并结果（合并列表）:")
merged_lists = merge_dicts(dict1, dict2, dict3, conflict_resolver=merge_lists)
print(f"  {merged_lists}")
```

## 性能优化和最佳实践

### 1. 遍历性能比较

```python
print("\n=== 遍历性能优化 ===")

import time

def performance_comparison():
    # 创建大字典
    large_dict = {f"key_{i}": i for i in range(100000)}
    
    # 测试不同遍历方式的性能
    methods = {
        "直接遍历键": lambda d: [k for k in d],
        "keys()方法": lambda d: [k for k in d.keys()],
        "转换为列表": lambda d: [k for k in list(d.keys())],
        "遍历items取键": lambda d: [k for k, v in d.items()]
    }
    
    results = {}
    
    for method_name, method_func in methods.items():
        start_time = time.time()
        result = method_func(large_dict)
        end_time = time.time()
        
        results[method_name] = {
            "time": end_time - start_time,
            "count": len(result)
        }
    
    print("遍历性能比较（100,000个元素）:")
    for method, stats in sorted(results.items(), key=lambda x: x[1]["time"]):
        print(f"  {method}: {stats['time']:.4f}秒")

# performance_comparison()  # 取消注释以运行性能测试

# 内存效率的遍历
def memory_efficient_processing(large_dict):
    """
    内存高效的字典处理
    """
    # 使用生成器而不是列表
    def process_items():
        for key, value in large_dict.items():
            if value % 2 == 0:  # 只处理偶数值
                yield key, value * 2
    
    # 批量处理
    batch_size = 1000
    batch = []
    
    for key, processed_value in process_items():
        batch.append((key, processed_value))
        
        if len(batch) >= batch_size:
            # 处理批次
            yield batch
            batch = []
    
    # 处理剩余项
    if batch:
        yield batch

# 测试内存效率处理
test_dict = {f"item_{i}": i for i in range(10)}
print("\n批量处理结果:")
for batch_num, batch in enumerate(memory_efficient_processing(test_dict)):
    print(f"  批次{batch_num}: {len(batch)}项")
    for key, value in batch[:3]:  # 只显示前3项
        print(f"    {key}: {value}")
```

### 2. 最佳实践总结

```python
print("\n=== 最佳实践总结 ===")

# 1. 选择合适的遍历方式
def best_practice_iteration():
    data = {"a": 1, "b": 2, "c": 3}
    
    # 好的做法
    print("推荐的遍历方式:")
    
    # 只需要键
    for key in data:
        print(f"  键: {key}")
    
    # 只需要值
    for value in data.values():
        print(f"  值: {value}")
    
    # 需要键和值
    for key, value in data.items():
        print(f"  {key}: {value}")

# 2. 安全的修改模式
def best_practice_modification():
    data = {"a": 1, "b": 2, "c": 3, "d": 4}
    
    # 删除偶数值 - 安全方式
    keys_to_remove = [k for k, v in data.items() if v % 2 == 0]
    for key in keys_to_remove:
        del data[key]
    
    print(f"删除偶数后: {data}")
    
    # 或者使用字典推导式
    data = {"a": 1, "b": 2, "c": 3, "d": 4}
    odd_data = {k: v for k, v in data.items() if v % 2 != 0}
    print(f"保留奇数: {odd_data}")

# 3. 高效的搜索和过滤
def best_practice_filtering():
    large_data = {f"item_{i}": {"value": i, "category": "A" if i % 2 == 0 else "B"} 
                  for i in range(1000)}
    
    # 使用生成器进行大数据过滤
    def filter_category_a():
        return (k for k, v in large_data.items() if v["category"] == "A")
    
    # 只获取前10个A类别项
    a_items = []
    for key in filter_category_a():
        a_items.append(key)
        if len(a_items) >= 10:
            break
    
    print(f"前10个A类别项: {a_items[:5]}...")  # 只显示前5个

# 4. 错误处理
def best_practice_error_handling():
    data = {"a": 1, "b": None, "c": "text"}
    
    # 安全的类型检查和处理
    numeric_sum = 0
    for key, value in data.items():
        try:
            if isinstance(value, (int, float)) and value is not None:
                numeric_sum += value
        except (TypeError, ValueError) as e:
            print(f"跳过无效值 {key}: {value} ({e})")
    
    print(f"数值总和: {numeric_sum}")

# 运行最佳实践示例
best_practice_iteration()
best_practice_modification()
best_practice_filtering()
best_practice_error_handling()
```

## 实际应用案例

### 1. 日志分析器

```python
print("\n=== 实际应用：日志分析器 ===")

from collections import defaultdict, Counter
from datetime import datetime

class LogAnalyzer:
    def __init__(self):
        self.logs = []
        self.stats = defaultdict(int)
        self.error_patterns = defaultdict(list)
    
    def add_log_entry(self, timestamp, level, message, source=None):
        """
        添加日志条目
        """
        entry = {
            "timestamp": timestamp,
            "level": level,
            "message": message,
            "source": source or "unknown"
        }
        self.logs.append(entry)
        self.stats[level] += 1
    
    def analyze_by_level(self):
        """
        按日志级别分析
        """
        level_analysis = {}
        
        for level in self.stats:
            level_logs = [log for log in self.logs if log["level"] == level]
            level_analysis[level] = {
                "count": len(level_logs),
                "percentage": len(level_logs) / len(self.logs) * 100,
                "sources": list(set(log["source"] for log in level_logs))
            }
        
        return level_analysis
    
    def find_error_patterns(self):
        """
        查找错误模式
        """
        error_logs = [log for log in self.logs if log["level"] in ["ERROR", "CRITICAL"]]
        
        # 按消息关键词分组
        keyword_groups = defaultdict(list)
        
        for log in error_logs:
            message = log["message"].lower()
            # 简单的关键词提取
            if "connection" in message:
                keyword_groups["connection_errors"].append(log)
            elif "timeout" in message:
                keyword_groups["timeout_errors"].append(log)
            elif "permission" in message:
                keyword_groups["permission_errors"].append(log)
            else:
                keyword_groups["other_errors"].append(log)
        
        return dict(keyword_groups)
    
    def get_hourly_distribution(self):
        """
        获取小时分布
        """
        hourly_stats = defaultdict(lambda: defaultdict(int))
        
        for log in self.logs:
            if isinstance(log["timestamp"], str):
                # 简单解析时间戳
                hour = int(log["timestamp"].split(":")[0])
            else:
                hour = log["timestamp"].hour
            
            hourly_stats[hour][log["level"]] += 1
        
        return dict(hourly_stats)
    
    def generate_report(self):
        """
        生成分析报告
        """
        report = {
            "total_logs": len(self.logs),
            "level_analysis": self.analyze_by_level(),
            "error_patterns": self.find_error_patterns(),
            "hourly_distribution": self.get_hourly_distribution()
        }
        return report

# 测试日志分析器
analyzer = LogAnalyzer()

# 添加示例日志
sample_logs = [
    ("10:30:15", "INFO", "Application started", "app"),
    ("10:30:20", "DEBUG", "Database connection established", "db"),
    ("10:31:45", "ERROR", "Connection timeout to external API", "api"),
    ("10:32:10", "WARNING", "High memory usage detected", "system"),
    ("10:33:22", "ERROR", "Permission denied for file access", "file"),
    ("11:15:30", "INFO", "User login successful", "auth"),
    ("11:16:45", "ERROR", "Database connection failed", "db"),
    ("11:20:10", "CRITICAL", "System timeout occurred", "system")
]

for timestamp, level, message, source in sample_logs:
    analyzer.add_log_entry(timestamp, level, message, source)

# 生成并显示报告
report = analyzer.generate_report()
print(f"日志分析报告:")
print(f"  总日志数: {report['total_logs']}")

print("\n按级别统计:")
for level, stats in report['level_analysis'].items():
    print(f"  {level}: {stats['count']}条 ({stats['percentage']:.1f}%)")
    print(f"    来源: {', '.join(stats['sources'])}")

print("\n错误模式:")
for pattern, logs in report['error_patterns'].items():
    print(f"  {pattern}: {len(logs)}条")
    for log in logs[:2]:  # 只显示前2条
        print(f"    - {log['message']}")
```

### 2. 数据聚合器

```python
print("\n=== 实际应用：数据聚合器 ===")

class DataAggregator:
    def __init__(self):
        self.data_sources = {}
        self.aggregation_rules = {}
    
    def add_data_source(self, name, data):
        """
        添加数据源
        """
        self.data_sources[name] = data
    
    def add_aggregation_rule(self, name, rule_func):
        """
        添加聚合规则
        """
        self.aggregation_rules[name] = rule_func
    
    def aggregate_all(self):
        """
        执行所有聚合规则
        """
        results = {}
        
        for rule_name, rule_func in self.aggregation_rules.items():
            try:
                results[rule_name] = rule_func(self.data_sources)
            except Exception as e:
                results[rule_name] = f"错误: {e}"
        
        return results
    
    def cross_source_analysis(self):
        """
        跨数据源分析
        """
        analysis = {}
        
        # 找出所有数据源的共同键
        if len(self.data_sources) >= 2:
            source_names = list(self.data_sources.keys())
            first_source = self.data_sources[source_names[0]]
            
            if isinstance(first_source, dict):
                common_keys = set(first_source.keys())
                
                for source_name in source_names[1:]:
                    source_data = self.data_sources[source_name]
                    if isinstance(source_data, dict):
                        common_keys &= set(source_data.keys())
                
                analysis["common_keys"] = list(common_keys)
                analysis["key_coverage"] = {
                    source_name: {
                        "total_keys": len(source_data) if isinstance(source_data, dict) else 0,
                        "common_keys": len(common_keys),
                        "unique_keys": len(set(source_data.keys()) - common_keys) if isinstance(source_data, dict) else 0
                    }
                    for source_name, source_data in self.data_sources.items()
                }
        
        return analysis

# 创建聚合器实例
aggregator = DataAggregator()

# 添加示例数据源
sales_data = {
    "product_A": {"sales": 1000, "profit": 200, "region": "north"},
    "product_B": {"sales": 1500, "profit": 300, "region": "south"},
    "product_C": {"sales": 800, "profit": 150, "region": "north"}
}

inventory_data = {
    "product_A": {"stock": 50, "cost": 800, "supplier": "supplier_1"},
    "product_B": {"stock": 30, "cost": 1200, "supplier": "supplier_2"},
    "product_D": {"stock": 100, "cost": 500, "supplier": "supplier_1"}
}

customer_data = {
    "product_A": {"reviews": 4.5, "customers": 120},
    "product_B": {"reviews": 4.2, "customers": 200},
    "product_C": {"reviews": 4.0, "customers": 80}
}

aggregator.add_data_source("sales", sales_data)
aggregator.add_data_source("inventory", inventory_data)
aggregator.add_data_source("customers", customer_data)

# 定义聚合规则
def total_sales_rule(sources):
    sales = sources.get("sales", {})
    return sum(product["sales"] for product in sales.values())

def profit_margin_rule(sources):
    sales = sources.get("sales", {})
    margins = {}
    for product, data in sales.items():
        if data["sales"] > 0:
            margins[product] = (data["profit"] / data["sales"]) * 100
    return margins

def low_stock_alert_rule(sources):
    inventory = sources.get("inventory", {})
    return {product: data["stock"] for product, data in inventory.items() if data["stock"] < 40}

def product_performance_rule(sources):
    sales = sources.get("sales", {})
    customers = sources.get("customers", {})
    
    performance = {}
    for product in sales.keys():
        if product in customers:
            performance[product] = {
                "revenue_per_customer": sales[product]["sales"] / customers[product]["customers"],
                "profit_per_customer": sales[product]["profit"] / customers[product]["customers"],
                "review_score": customers[product]["reviews"]
            }
    return performance

# 添加聚合规则
aggregator.add_aggregation_rule("total_sales", total_sales_rule)
aggregator.add_aggregation_rule("profit_margins", profit_margin_rule)
aggregator.add_aggregation_rule("low_stock_alerts", low_stock_alert_rule)
aggregator.add_aggregation_rule("product_performance", product_performance_rule)

# 执行聚合
results = aggregator.aggregate_all()
print("聚合结果:")
for rule_name, result in results.items():
    print(f"\n{rule_name}:")
    if isinstance(result, dict):
        for key, value in result.items():
            print(f"  {key}: {value}")
    else:
        print(f"  {result}")

# 跨数据源分析
cross_analysis = aggregator.cross_source_analysis()
print(f"\n跨数据源分析:")
print(f"  共同产品: {cross_analysis.get('common_keys', [])}")
print(f"  数据覆盖情况:")
for source, coverage in cross_analysis.get('key_coverage', {}).items():
    print(f"    {source}: 总计{coverage['total_keys']}, 共同{coverage['common_keys']}, 独有{coverage['unique_keys']}")
```

## 学习要点

1. **基本遍历方式**
   - 直接遍历字典获取键（最常用）
   - 使用`.keys()`, `.values()`, `.items()`获取视图对象
   - 带索引的遍历使用`enumerate()`

2. **高级遍历技巧**
   - 排序遍历：使用`sorted()`函数
   - 条件遍历：结合`if`语句或生成器表达式
   - 字典推导式：简洁的过滤和转换

3. **安全遍历原则**
   - 遍历时不要直接修改字典大小
   - 先收集要修改的键，再执行修改
   - 使用字典推导式创建新字典

4. **性能优化**
   - 使用视图对象而不是转换为列表
   - 生成器表达式处理大数据
   - 批量处理减少内存占用

5. **实际应用模式**
   - 数据统计和分析
   - 配置比较和合并
   - 日志处理和模式识别
   - 多数据源聚合

## 练习题

1. 编写一个函数，统计嵌套字典中所有数值的总和
2. 实现一个字典差异比较器，找出两个字典的所有差异
3. 创建一个数据透视表生成器，将列表数据按指定字段分组
4. 编写一个配置文件合并工具，支持多种合并策略
5. 实现一个内存高效的大字典处理器，支持流式处理

## 下一步学习

掌握了字典遍历后，接下来学习：
- 嵌套字典的高级操作技巧
- 字典推导式的深入应用
- 字典在数据结构和算法中的应用
- 字典的综合实战练习

---

字典遍历是数据处理的核心技能，熟练掌握各种遍历方式和优化技巧，能让你的数据处理代码更加高效和优雅！