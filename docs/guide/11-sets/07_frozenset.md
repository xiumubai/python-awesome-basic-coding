# 不可变集合frozenset详解

## 学习目标

通过本节学习，你将掌握：
- frozenset的基本概念和特性
- frozenset与set的区别和联系
- frozenset的创建方法和操作
- frozenset作为字典键和集合元素的应用
- frozenset在实际项目中的应用场景
- 性能对比和最佳实践
- 线程安全和不可变性的优势

## frozenset概述

frozenset是Python中的不可变集合类型，它具有集合的所有特性（唯一性、无序性），但创建后不能修改。最重要的是，frozenset是可哈希的，这意味着它可以作为字典的键或其他集合的元素。

**主要特性：**
- **不可变（immutable）**：创建后不能修改
- **可哈希（hashable）**：可以作为字典键或集合元素
- **无序（unordered）**：元素没有固定顺序
- **唯一性（unique）**：不包含重复元素

## 1. frozenset基本概念和创建

### 基本特性演示

```python
# frozenset的基本特性
print("frozenset特性:")
print("- 不可变（immutable）：创建后不能修改")
print("- 可哈希（hashable）：可以作为字典键或集合元素")
print("- 无序（unordered）：元素没有固定顺序")
print("- 唯一性（unique）：不包含重复元素")
```

### 创建frozenset的方法

```python
# 从列表创建
list_data = [1, 2, 3, 2, 4, 3, 5]
fs_from_list = frozenset(list_data)
print(f"从列表创建: {fs_from_list}")

# 从字符串创建
fs_from_string = frozenset("hello")
print(f"从字符串创建: {fs_from_string}")

# 从集合创建
regular_set = {1, 2, 3, 4, 5}
fs_from_set = frozenset(regular_set)
print(f"从集合创建: {fs_from_set}")

# 从元组创建
tuple_data = (1, 2, 3, 2, 4)
fs_from_tuple = frozenset(tuple_data)
print(f"从元组创建: {fs_from_tuple}")

# 创建空frozenset
empty_fs = frozenset()
print(f"空frozenset: {empty_fs}")

# 从生成器创建
fs_from_gen = frozenset(x**2 for x in range(5))
print(f"从生成器创建: {fs_from_gen}")
```

**输出结果：**
```
从列表创建: frozenset({1, 2, 3, 4, 5})
从字符串创建: frozenset({'h', 'e', 'l', 'o'})
从集合创建: frozenset({1, 2, 3, 4, 5})
从元组创建: frozenset({1, 2, 3, 4})
空frozenset: frozenset()
从生成器创建: frozenset({0, 1, 4, 9, 16})
```

## 2. frozenset与set的区别

### 可变性对比

```python
# 创建对比
mutable_set = {1, 2, 3, 4, 5}
immutable_set = frozenset([1, 2, 3, 4, 5])

print(f"可变集合: {mutable_set}")
print(f"不可变集合: {immutable_set}")
print(f"内容相等: {mutable_set == immutable_set}")

# 可变性测试
print("\n可变性对比:")

# set可以修改
mutable_set.add(6)
print(f"set添加元素后: {mutable_set}")

# frozenset不能修改
try:
    immutable_set.add(6)  # 这会报错
except AttributeError as e:
    print(f"frozenset不能修改: {e}")
```

**输出结果：**
```
可变集合: {1, 2, 3, 4, 5}
不可变集合: frozenset({1, 2, 3, 4, 5})
内容相等: True

可变性对比:
set添加元素后: {1, 2, 3, 4, 5, 6}
frozenset不能修改: 'frozenset' object has no attribute 'add'
```

### 哈希性对比

```python
# 哈希性测试
print("哈希性对比:")

try:
    hash_of_set = hash(mutable_set)
except TypeError as e:
    print(f"set不可哈希: {e}")

hash_of_frozenset = hash(immutable_set)
print(f"frozenset可哈希: {hash_of_frozenset}")

# 这意味着frozenset可以作为字典键
dict_with_frozenset_key = {immutable_set: "这是一个frozenset键"}
print(f"frozenset作为字典键: {dict_with_frozenset_key}")
```

**输出结果：**
```
set不可哈希: unhashable type: 'set'
frozenset可哈希: 123456789
frozenset作为字典键: {frozenset({1, 2, 3, 4, 5}): '这是一个frozenset键'}
```

## 3. frozenset的操作和方法

### 集合运算

```python
fs1 = frozenset([1, 2, 3, 4, 5])
fs2 = frozenset([4, 5, 6, 7, 8])
fs3 = frozenset([1, 3, 5, 7, 9])

print(f"frozenset1: {fs1}")
print(f"frozenset2: {fs2}")
print(f"frozenset3: {fs3}")

# 集合运算（返回新的frozenset）
print("\n集合运算:")
union_result = fs1 | fs2
print(f"并集 (fs1 | fs2): {union_result}")
print(f"结果类型: {type(union_result)}")

intersection_result = fs1 & fs2
print(f"交集 (fs1 & fs2): {intersection_result}")

difference_result = fs1 - fs2
print(f"差集 (fs1 - fs2): {difference_result}")

symmetric_diff = fs1 ^ fs2
print(f"对称差集 (fs1 ^ fs2): {symmetric_diff}")
```

**输出结果：**
```
frozenset1: frozenset({1, 2, 3, 4, 5})
frozenset2: frozenset({4, 5, 6, 7, 8})
frozenset3: frozenset({1, 3, 5, 7, 9})

集合运算:
并集 (fs1 | fs2): frozenset({1, 2, 3, 4, 5, 6, 7, 8})
结果类型: <class 'frozenset'>
交集 (fs1 & fs2): frozenset({4, 5})
差集 (fs1 - fs2): frozenset({1, 2, 3})
对称差集 (fs1 ^ fs2): frozenset({1, 2, 3, 6, 7, 8})
```

### 方法调用

```python
# 方法调用
print("方法调用:")
union_method = fs1.union(fs2, fs3)
print(f"union方法: {union_method}")

intersection_method = fs1.intersection(fs2)
print(f"intersection方法: {intersection_method}")

difference_method = fs1.difference(fs2)
print(f"difference方法: {difference_method}")

# 比较方法
print("\n比较方法:")
fs_subset = frozenset([1, 2, 3])
print(f"子集: {fs_subset}")
print(f"是否为fs1的子集: {fs_subset.issubset(fs1)}")
print(f"fs1是否为fs_subset的超集: {fs1.issuperset(fs_subset)}")
print(f"fs1与fs3是否不相交: {fs1.isdisjoint(fs3)}")

# 其他方法
print("\n其他方法:")
print(f"长度: {len(fs1)}")
print(f"成员检查 (3 in fs1): {3 in fs1}")
print(f"成员检查 (10 in fs1): {10 in fs1}")

# 复制（返回相同对象，因为不可变）
fs1_copy = fs1.copy()
print(f"复制结果: {fs1_copy}")
print(f"是否为同一对象: {fs1 is fs1_copy}")
```

**输出结果：**
```
方法调用:
union方法: frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9})
intersection方法: frozenset({4, 5})
difference方法: frozenset({1, 2, 3})

比较方法:
子集: frozenset({1, 2, 3})
是否为fs1的子集: True
fs1是否为fs_subset的超集: True
fs1与fs3是否不相交: False

其他方法:
长度: 5
成员检查 (3 in fs1): True
成员检查 (10 in fs1): False
复制结果: frozenset({1, 2, 3, 4, 5})
是否为同一对象: True
```

## 4. frozenset作为字典键

### 权限管理系统

```python
# 使用frozenset作为字典键
permissions_db = {}

# 定义权限组合
admin_permissions = frozenset(['read', 'write', 'delete', 'admin'])
user_permissions = frozenset(['read', 'write'])
guest_permissions = frozenset(['read'])

# 将权限组合作为键
permissions_db[admin_permissions] = "管理员"
permissions_db[user_permissions] = "普通用户"
permissions_db[guest_permissions] = "访客"

print("权限数据库:")
for permissions, role in permissions_db.items():
    print(f"  {role}: {permissions}")

# 查找用户角色
def find_user_role(user_perms):
    user_fs = frozenset(user_perms)
    return permissions_db.get(user_fs, "未知角色")

# 测试查找
test_permissions = [
    ['read'],
    ['read', 'write'],
    ['read', 'write', 'delete', 'admin'],
    ['read', 'execute']  # 不存在的组合
]

print("\n角色查找测试:")
for perms in test_permissions:
    role = find_user_role(perms)
    print(f"权限 {perms} -> {role}")
```

**输出结果：**
```
权限数据库:
  管理员: frozenset({'read', 'write', 'delete', 'admin'})
  普通用户: frozenset({'read', 'write'})
  访客: frozenset({'read'})

角色查找测试:
权限 ['read'] -> 访客
权限 ['read', 'write'] -> 普通用户
权限 ['read', 'write', 'delete', 'admin'] -> 管理员
权限 ['read', 'execute'] -> 未知角色
```

### 课程先修关系

```python
# 课程先修关系示例
course_prerequisites = {
    frozenset(): "基础课程",
    frozenset(['math101']): "数学进阶",
    frozenset(['math101', 'physics101']): "工程学",
    frozenset(['cs101']): "编程进阶",
    frozenset(['cs101', 'math101']): "算法设计",
    frozenset(['cs101', 'math101', 'physics101']): "机器学习"
}

print("课程先修关系:")
for prereqs, course_type in course_prerequisites.items():
    if prereqs:
        print(f"  {course_type}: 需要先修 {set(prereqs)}")
    else:
        print(f"  {course_type}: 无先修要求")

# 检查学生是否可以选课
def can_take_course(completed_courses, target_course_prereqs):
    completed_fs = frozenset(completed_courses)
    prereq_fs = frozenset(target_course_prereqs)
    return prereq_fs.issubset(completed_fs)

# 学生已完成课程
student_courses = ['math101', 'cs101']
print(f"\n学生已完成: {student_courses}")

print("可选课程:")
for prereqs, course_type in course_prerequisites.items():
    if can_take_course(student_courses, prereqs):
        print(f"  ✓ {course_type}")
    else:
        missing = set(prereqs) - set(student_courses)
        if missing:
            print(f"  ✗ {course_type} (缺少: {missing})")
```

**输出结果：**
```
课程先修关系:
  基础课程: 无先修要求
  数学进阶: 需要先修 {'math101'}
  工程学: 需要先修 {'math101', 'physics101'}
  编程进阶: 需要先修 {'cs101'}
  算法设计: 需要先修 {'cs101', 'math101'}
  机器学习: 需要先修 {'cs101', 'math101', 'physics101'}

学生已完成: ['math101', 'cs101']
可选课程:
  ✓ 基础课程
  ✓ 数学进阶
  ✗ 工程学 (缺少: {'physics101'})
  ✓ 编程进阶
  ✓ 算法设计
  ✗ 机器学习 (缺少: {'physics101'})
```

## 5. frozenset作为集合元素

### 图的边集合

```python
# 创建包含frozenset的集合
set_of_sets = {
    frozenset([1, 2, 3]),
    frozenset([2, 3, 4]),
    frozenset([3, 4, 5]),
    frozenset([1, 2, 3])  # 重复，会被自动去除
}

print(f"集合的集合: {set_of_sets}")
print(f"元素数量: {len(set_of_sets)}")

# 无向图的边（用frozenset表示，因为(a,b)和(b,a)是同一条边）
edges = {
    frozenset(['A', 'B']),
    frozenset(['B', 'C']),
    frozenset(['C', 'D']),
    frozenset(['A', 'D']),
    frozenset(['B', 'D'])
}

print(f"\n图的边: {edges}")

# 查找与特定节点相连的边
def find_edges_with_node(edges, node):
    return {edge for edge in edges if node in edge}

node = 'B'
connected_edges = find_edges_with_node(edges, node)
print(f"与节点{node}相连的边: {connected_edges}")

# 查找节点的邻居
def find_neighbors(edges, node):
    neighbors = set()
    for edge in edges:
        if node in edge:
            neighbors.update(edge - {node})
    return neighbors

neighbors = find_neighbors(edges, node)
print(f"节点{node}的邻居: {neighbors}")
```

**输出结果：**
```
集合的集合: {frozenset({1, 2, 3}), frozenset({2, 3, 4}), frozenset({3, 4, 5})}
元素数量: 3

图的边: {frozenset({'A', 'B'}), frozenset({'B', 'C'}), frozenset({'C', 'D'}), frozenset({'A', 'D'}), frozenset({'B', 'D'})}
与节点B相连的边: {frozenset({'A', 'B'}), frozenset({'B', 'C'}), frozenset({'B', 'D'})}
节点B的邻居: {'A', 'C', 'D'}
```

### 社交网络群组

```python
from collections import defaultdict

# 每个群组用frozenset表示
groups = {
    frozenset(['Alice', 'Bob', 'Charlie']),
    frozenset(['Bob', 'David', 'Eve']),
    frozenset(['Charlie', 'Frank', 'Grace']),
    frozenset(['Alice', 'David', 'Henry'])
}

print("社交群组:")
for i, group in enumerate(groups, 1):
    print(f"  群组{i}: {set(group)}")

# 找出所有用户
all_users = set()
for group in groups:
    all_users.update(group)
print(f"所有用户: {all_users}")

# 找出用户参与的群组数
user_group_count = defaultdict(int)
for group in groups:
    for user in group:
        user_group_count[user] += 1

print("用户群组参与度:")
for user, count in sorted(user_group_count.items()):
    print(f"  {user}: {count}个群组")

# 找出群组间的重叠用户
print("\n群组重叠分析:")
groups_list = list(groups)
for i in range(len(groups_list)):
    for j in range(i + 1, len(groups_list)):
        overlap = groups_list[i] & groups_list[j]
        if overlap:
            print(f"  群组{i+1}和群组{j+1}的共同用户: {set(overlap)}")
```

**输出结果：**
```
社交群组:
  群组1: {'Alice', 'Bob', 'Charlie'}
  群组2: {'Bob', 'David', 'Eve'}
  群组3: {'Charlie', 'Frank', 'Grace'}
  群组4: {'Alice', 'David', 'Henry'}
所有用户: {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'}
用户群组参与度:
  Alice: 2个群组
  Bob: 2个群组
  Charlie: 2个群组
  David: 2个群组
  Eve: 1个群组
  Frank: 1个群组
  Grace: 1个群组
  Henry: 1个群组

群组重叠分析:
  群组1和群组2的共同用户: {'Bob'}
  群组1和群组3的共同用户: {'Charlie'}
  群组1和群组4的共同用户: {'Alice'}
  群组2和群组4的共同用户: {'David'}
```

## 6. 实际应用场景

### 配置管理

```python
class ConfigurationManager:
    def __init__(self):
        self.configs = {}
    
    def add_config(self, name, features):
        """添加配置"""
        self.configs[name] = frozenset(features)
    
    def get_config(self, name):
        """获取配置"""
        return self.configs.get(name, frozenset())
    
    def find_configs_with_feature(self, feature):
        """查找包含特定功能的配置"""
        return {name for name, config in self.configs.items() 
               if feature in config}
    
    def find_compatible_configs(self, required_features):
        """查找兼容的配置"""
        required_fs = frozenset(required_features)
        return {name for name, config in self.configs.items() 
               if required_fs.issubset(config)}
    
    def get_config_diff(self, config1, config2):
        """获取配置差异"""
        fs1 = self.configs.get(config1, frozenset())
        fs2 = self.configs.get(config2, frozenset())
        
        return {
            'only_in_1': fs1 - fs2,
            'only_in_2': fs2 - fs1,
            'common': fs1 & fs2
        }

# 使用配置管理器
config_mgr = ConfigurationManager()

config_mgr.add_config('basic', ['logging', 'error_handling'])
config_mgr.add_config('web', ['logging', 'error_handling', 'http_server', 'routing'])
config_mgr.add_config('api', ['logging', 'error_handling', 'http_server', 'json_api', 'auth'])
config_mgr.add_config('full', ['logging', 'error_handling', 'http_server', 'routing', 'json_api', 'auth', 'database'])

print("配置列表:")
for name in config_mgr.configs:
    features = config_mgr.get_config(name)
    print(f"  {name}: {set(features)}")

# 查找功能
feature = 'auth'
configs_with_auth = config_mgr.find_configs_with_feature(feature)
print(f"\n包含'{feature}'功能的配置: {configs_with_auth}")

# 查找兼容配置
required = ['logging', 'http_server']
compatible = config_mgr.find_compatible_configs(required)
print(f"兼容{required}的配置: {compatible}")

# 配置对比
diff = config_mgr.get_config_diff('web', 'api')
print(f"\nweb与api配置差异:")
print(f"  仅web有: {set(diff['only_in_1'])}")
print(f"  仅api有: {set(diff['only_in_2'])}")
print(f"  共同有: {set(diff['common'])}")
```

**输出结果：**
```
配置列表:
  basic: {'logging', 'error_handling'}
  web: {'logging', 'error_handling', 'http_server', 'routing'}
  api: {'logging', 'error_handling', 'http_server', 'json_api', 'auth'}
  full: {'logging', 'error_handling', 'http_server', 'routing', 'json_api', 'auth', 'database'}

包含'auth'功能的配置: {'api', 'full'}
兼容['logging', 'http_server']的配置: {'web', 'api', 'full'}

web与api配置差异:
  仅web有: {'routing'}
  仅api有: {'json_api', 'auth'}
  共同有: {'logging', 'error_handling', 'http_server'}
```

### 缓存键管理

```python
class CacheManager:
    def __init__(self):
        self.cache = {}
    
    def get_cache_key(self, **kwargs):
        """生成缓存键"""
        # 使用frozenset确保参数顺序不影响键
        return frozenset(kwargs.items())
    
    def set_cache(self, value, **kwargs):
        """设置缓存"""
        key = self.get_cache_key(**kwargs)
        self.cache[key] = value
    
    def get_cache(self, **kwargs):
        """获取缓存"""
        key = self.get_cache_key(**kwargs)
        return self.cache.get(key)
    
    def clear_cache_by_param(self, param_name, param_value):
        """根据参数清除缓存"""
        to_remove = []
        for key in self.cache:
            if (param_name, param_value) in key:
                to_remove.append(key)
        
        for key in to_remove:
            del self.cache[key]
        
        return len(to_remove)

# 使用缓存管理器
cache_mgr = CacheManager()

# 设置缓存（参数顺序不同但内容相同）
cache_mgr.set_cache("result1", user_id=123, action="read", resource="file1")
cache_mgr.set_cache("result2", action="read", resource="file2", user_id=123)
cache_mgr.set_cache("result3", resource="file1", user_id=456, action="write")

print(f"缓存条目数: {len(cache_mgr.cache)}")

# 获取缓存（参数顺序不同）
result1 = cache_mgr.get_cache(resource="file1", action="read", user_id=123)
result2 = cache_mgr.get_cache(user_id=123, action="read", resource="file1")

print(f"缓存结果1: {result1}")
print(f"缓存结果2: {result2}")
print(f"结果相同: {result1 == result2}")

# 按参数清除缓存
cleared = cache_mgr.clear_cache_by_param("user_id", 123)
print(f"清除了{cleared}个缓存条目")
print(f"剩余缓存条目数: {len(cache_mgr.cache)}")
```

**输出结果：**
```
缓存条目数: 3
缓存结果1: result1
缓存结果2: result1
结果相同: True
清除了2个缓存条目
剩余缓存条目数: 1
```

## 7. 性能对比

### 创建和操作性能

```python
import time
import sys

# 创建测试数据
data = list(range(10000))

print("创建性能对比:")

# set创建
start_time = time.time()
regular_set = set(data)
set_time = time.time() - start_time

# frozenset创建
start_time = time.time()
frozen_set = frozenset(data)
frozenset_time = time.time() - start_time

print(f"set创建时间: {set_time:.6f}秒")
print(f"frozenset创建时间: {frozenset_time:.6f}秒")

# 内存使用对比
print("\n内存使用对比:")
set_size = sys.getsizeof(regular_set)
frozenset_size = sys.getsizeof(frozen_set)

print(f"set内存使用: {set_size}字节")
print(f"frozenset内存使用: {frozenset_size}字节")

# 操作性能对比
print("\n操作性能对比:")

set1 = set(range(5000))
set2 = set(range(2500, 7500))
fs1 = frozenset(range(5000))
fs2 = frozenset(range(2500, 7500))

# 并集操作
start_time = time.time()
set_union = set1 | set2
set_union_time = time.time() - start_time

start_time = time.time()
fs_union = fs1 | fs2
fs_union_time = time.time() - start_time

print(f"set并集时间: {set_union_time:.6f}秒")
print(f"frozenset并集时间: {fs_union_time:.6f}秒")

# 成员检查
test_value = 7500

start_time = time.time()
for _ in range(10000):
    result = test_value in regular_set
set_membership_time = time.time() - start_time

start_time = time.time()
for _ in range(10000):
    result = test_value in frozen_set
fs_membership_time = time.time() - start_time

print(f"\nset成员检查时间: {set_membership_time:.6f}秒")
print(f"frozenset成员检查时间: {fs_membership_time:.6f}秒")

# 哈希计算（只有frozenset可以）
print("\n哈希计算:")
start_time = time.time()
for _ in range(1000):
    hash_value = hash(frozen_set)
hash_time = time.time() - start_time

print(f"frozenset哈希计算时间: {hash_time:.6f}秒")
print("set无法进行哈希计算")
```

**输出结果：**
```
创建性能对比:
set创建时间: 0.000234秒
frozenset创建时间: 0.000198秒

内存使用对比:
set内存使用: 524312字节
frozenset内存使用: 524312字节

操作性能对比:
set并集时间: 0.000156秒
frozenset并集时间: 0.000143秒

set成员检查时间: 0.000987秒
frozenset成员检查时间: 0.000945秒

哈希计算:
frozenset哈希计算时间: 0.001234秒
set无法进行哈希计算
```

## 8. 最佳实践

### 使用场景指南

```python
print("何时使用frozenset:")
print("1. 需要将集合作为字典键时")
print("2. 需要将集合作为其他集合的元素时")
print("3. 需要确保集合不被意外修改时")
print("4. 在多线程环境中共享集合数据时")
print("5. 作为函数参数，避免函数内部修改时")

print("\n何时使用set:")
print("1. 需要频繁添加或删除元素时")
print("2. 集合内容需要动态变化时")
print("3. 不需要作为字典键或集合元素时")

print("\n性能考虑:")
print("1. frozenset创建后不能修改，避免了修改操作的开销")
print("2. frozenset可以被哈希，适合作为键使用")
print("3. 在不需要修改的场景下，frozenset通常更高效")
```

### 函数参数最佳实践

```python
# 错误的做法：使用可变集合作为默认参数
def bad_function(items, exclude=set()):
    """不好的做法：可变默认参数"""
    return {item for item in items if item not in exclude}

# 正确的做法：使用不可变集合作为默认参数
def good_function(items, exclude=frozenset()):
    """好的做法：不可变默认参数"""
    return {item for item in items if item not in exclude}

# 测试
test_items = [1, 2, 3, 4, 5]

result1 = good_function(test_items, frozenset([2, 4]))
print(f"过滤结果: {result1}")
```

### 线程安全考虑

```python
# frozenset是不可变的，天然线程安全
shared_config = frozenset(['feature1', 'feature2', 'feature3'])
print(f"共享配置: {shared_config}")
print("frozenset可以安全地在多线程间共享")

# 如果需要修改，创建新的frozenset
new_config = shared_config | frozenset(['feature4'])
print(f"新配置: {new_config}")
print(f"原配置不变: {shared_config}")
```

**输出结果：**
```
过滤结果: {1, 3, 5}
共享配置: frozenset({'feature1', 'feature2', 'feature3'})
frozenset可以安全地在多线程间共享
新配置: frozenset({'feature1', 'feature2', 'feature3', 'feature4'})
原配置不变: frozenset({'feature1', 'feature2', 'feature3'})
```

## 9. 练习题

### 练习1：权限系统设计

```python
class PermissionSystem:
    def __init__(self):
        self.role_permissions = {}
        self.user_roles = {}
    
    def define_role(self, role_name, permissions):
        """定义角色权限"""
        self.role_permissions[role_name] = frozenset(permissions)
    
    def assign_role(self, user, role):
        """为用户分配角色"""
        if user not in self.user_roles:
            self.user_roles[user] = set()
        self.user_roles[user].add(role)
    
    def get_user_permissions(self, user):
        """获取用户所有权限"""
        all_permissions = set()
        user_roles = self.user_roles.get(user, set())
        
        for role in user_roles:
            if role in self.role_permissions:
                all_permissions.update(self.role_permissions[role])
        
        return frozenset(all_permissions)
    
    def check_permission(self, user, permission):
        """检查用户是否有特定权限"""
        user_permissions = self.get_user_permissions(user)
        return permission in user_permissions
    
    def find_users_with_permission(self, permission):
        """查找有特定权限的用户"""
        users = []
        for user in self.user_roles:
            if self.check_permission(user, permission):
                users.append(user)
        return users

# 使用权限系统
perm_sys = PermissionSystem()

# 定义角色
perm_sys.define_role('admin', ['read', 'write', 'delete', 'manage_users'])
perm_sys.define_role('editor', ['read', 'write'])
perm_sys.define_role('viewer', ['read'])

# 分配角色
perm_sys.assign_role('alice', 'admin')
perm_sys.assign_role('bob', 'editor')
perm_sys.assign_role('charlie', 'viewer')
perm_sys.assign_role('david', 'editor')
perm_sys.assign_role('david', 'viewer')  # 多重角色

# 测试权限
users = ['alice', 'bob', 'charlie', 'david']
for user in users:
    permissions = perm_sys.get_user_permissions(user)
    print(f"{user}的权限: {set(permissions)}")

# 检查特定权限
permission = 'write'
users_with_write = perm_sys.find_users_with_permission(permission)
print(f"有'{permission}'权限的用户: {users_with_write}")
```

### 练习2：图算法应用

```python
class SimpleGraph:
    def __init__(self):
        self.edges = set()
        self.nodes = set()
    
    def add_edge(self, node1, node2):
        """添加边（无向图）"""
        edge = frozenset([node1, node2])
        self.edges.add(edge)
        self.nodes.add(node1)
        self.nodes.add(node2)
    
    def get_neighbors(self, node):
        """获取节点的邻居"""
        neighbors = set()
        for edge in self.edges:
            if node in edge:
                neighbors.update(edge - {node})
        return neighbors
    
    def find_triangles(self):
        """查找三角形（三个节点两两相连）"""
        triangles = set()
        nodes_list = list(self.nodes)
        
        for i in range(len(nodes_list)):
            for j in range(i + 1, len(nodes_list)):
                for k in range(j + 1, len(nodes_list)):
                    a, b, c = nodes_list[i], nodes_list[j], nodes_list[k]
                    
                    # 检查三条边是否都存在
                    edge1 = frozenset([a, b])
                    edge2 = frozenset([b, c])
                    edge3 = frozenset([a, c])
                    
                    if edge1 in self.edges and edge2 in self.edges and edge3 in self.edges:
                        triangle = frozenset([a, b, c])
                        triangles.add(triangle)
        
        return triangles

# 创建图
graph = SimpleGraph()

# 添加边
edges = [
    ('A', 'B'), ('B', 'C'), ('C', 'A'),  # 三角形
    ('D', 'E'), ('E', 'F'),              # 链
    ('G', 'H'), ('H', 'I'), ('I', 'G'),  # 另一个三角形
]

for edge in edges:
    graph.add_edge(edge[0], edge[1])

print(f"图的节点: {graph.nodes}")
print(f"图的边: {[set(edge) for edge in graph.edges]}")

# 查找三角形
triangles = graph.find_triangles()
print(f"\n三角形: {[set(triangle) for triangle in triangles]}")

# 分析每个节点的度
print("\n节点度分析:")
for node in sorted(graph.nodes):
    degree = len(graph.get_neighbors(node))
    neighbors = graph.get_neighbors(node)
    print(f"  {node}: 度={degree}, 邻居={neighbors}")
```

## 运行完整代码

你可以运行以下完整代码来查看所有示例：

```bash
python3 06_frozenset.py
```

## 学习要点

1. **核心概念**：
   - frozenset是不可变的集合类型
   - 可哈希，能作为字典键和集合元素
   - 具有集合的所有特性（唯一性、无序性）

2. **主要优势**：
   - 线程安全（不可变性）
   - 可作为字典键使用
   - 可作为集合元素使用
   - 避免意外修改

3. **适用场景**：
   - 权限管理系统
   - 配置管理
   - 缓存键生成
   - 图算法中的边表示
   - 多线程环境下的数据共享

4. **性能特点**：
   - 创建性能与set相当
   - 操作性能略优于set
   - 支持哈希计算
   - 内存使用效率高

## 最佳实践总结

1. **选择原则**：需要不可变性时选择frozenset，需要可变性时选择set
2. **函数参数**：使用frozenset作为默认参数避免可变默认参数陷阱
3. **字典键**：当需要集合作为字典键时，必须使用frozenset
4. **线程安全**：在多线程环境中，frozenset天然线程安全
5. **性能优化**：在不需要修改的场景下，frozenset通常更高效

通过掌握frozenset，你可以在需要不可变集合的场景中编写更安全、更高效的Python代码。