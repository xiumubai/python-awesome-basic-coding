#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不可变集合frozenset详解

本文件详细演示了Python不可变集合frozenset的使用：
1. frozenset的基本概念和特性
2. frozenset的创建方法
3. frozenset与set的区别
4. frozenset的操作和方法
5. frozenset作为字典键和集合元素
6. frozenset的实际应用场景
7. 性能对比和最佳实践

作者：Python学习教程
日期：2024年
"""

import time
import sys
from collections import defaultdict

def main():
    print("=" * 50)
    print("不可变集合frozenset详解")
    print("=" * 50)
    
    # 1. frozenset的基本概念
    print("\n1. frozenset基本概念")
    print("-" * 30)
    
    print("frozenset特性:")
    print("- 不可变（immutable）：创建后不能修改")
    print("- 可哈希（hashable）：可以作为字典键或集合元素")
    print("- 无序（unordered）：元素没有固定顺序")
    print("- 唯一性（unique）：不包含重复元素")
    
    # 2. frozenset的创建方法
    print("\n2. frozenset创建方法")
    print("-" * 30)
    
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
    
    # 3. frozenset与set的区别
    print("\n3. frozenset与set的区别")
    print("-" * 30)
    
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
    
    # 哈希性测试
    print("\n哈希性对比:")
    
    try:
        hash_of_set = hash(mutable_set)
    except TypeError as e:
        print(f"set不可哈希: {e}")
    
    hash_of_frozenset = hash(immutable_set)
    print(f"frozenset可哈希: {hash_of_frozenset}")
    
    # 4. frozenset的操作和方法
    print("\n4. frozenset操作和方法")
    print("-" * 30)
    
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
    
    # 方法调用
    print("\n方法调用:")
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
    
    print("\n=" * 50)
    print("frozenset基础演示完成！")
    print("=" * 50)

def demonstrate_as_dict_keys():
    """
    演示frozenset作为字典键
    """
    print("\nfrozenset作为字典键")
    print("-" * 30)
    
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
    
    # 复杂示例：课程先修关系
    print("\n课程先修关系示例:")
    
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

def demonstrate_as_set_elements():
    """
    演示frozenset作为集合元素
    """
    print("\nfrozenset作为集合元素")
    print("-" * 30)
    
    # 创建包含frozenset的集合
    set_of_sets = {
        frozenset([1, 2, 3]),
        frozenset([2, 3, 4]),
        frozenset([3, 4, 5]),
        frozenset([1, 2, 3])  # 重复，会被自动去除
    }
    
    print(f"集合的集合: {set_of_sets}")
    print(f"元素数量: {len(set_of_sets)}")
    
    # 实际应用：图的边集合
    print("\n图的边集合示例:")
    
    # 无向图的边（用frozenset表示，因为(a,b)和(b,a)是同一条边）
    edges = {
        frozenset(['A', 'B']),
        frozenset(['B', 'C']),
        frozenset(['C', 'D']),
        frozenset(['A', 'D']),
        frozenset(['B', 'D'])
    }
    
    print(f"图的边: {edges}")
    
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
    
    # 复杂示例：社交网络群组
    print("\n社交网络群组示例:")
    
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

def demonstrate_practical_applications():
    """
    实际应用场景演示
    """
    print("\n实际应用场景")
    print("-" * 30)
    
    # 1. 配置管理
    print("1. 配置管理:")
    
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
    
    # 2. 缓存键管理
    print("\n2. 缓存键管理:")
    
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

def demonstrate_performance_comparison():
    """
    性能对比
    """
    print("\n性能对比")
    print("-" * 30)
    
    # 创建测试数据
    data = list(range(10000))
    
    # 测试创建性能
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
    
    # 测试内存使用
    print("\n内存使用对比:")
    set_size = sys.getsizeof(regular_set)
    frozenset_size = sys.getsizeof(frozen_set)
    
    print(f"set内存使用: {set_size}字节")
    print(f"frozenset内存使用: {frozenset_size}字节")
    
    # 测试操作性能
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

def best_practices():
    """
    最佳实践
    """
    print("\n最佳实践")
    print("-" * 30)
    
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
    
    # 实际示例
    print("\n实际应用示例:")
    
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
    
    # 线程安全示例
    print("\n线程安全考虑:")
    
    # frozenset是不可变的，天然线程安全
    shared_config = frozenset(['feature1', 'feature2', 'feature3'])
    print(f"共享配置: {shared_config}")
    print("frozenset可以安全地在多线程间共享")
    
    # 如果需要修改，创建新的frozenset
    new_config = shared_config | frozenset(['feature4'])
    print(f"新配置: {new_config}")
    print("原配置不变: {}".format(shared_config))

def practice_exercises():
    """
    练习题
    """
    print("\n练习题")
    print("-" * 20)
    
    # 练习1：权限系统
    def exercise_1():
        print("1. 权限系统设计:")
        
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
    
    # 练习2：数据分组
    def exercise_2():
        print("\n2. 数据分组分析:")
        
        # 学生选课数据
        student_courses = {
            'Alice': ['Math', 'Physics', 'Chemistry'],
            'Bob': ['Math', 'Computer Science', 'Physics'],
            'Charlie': ['Chemistry', 'Biology', 'Math'],
            'David': ['Computer Science', 'Math', 'Statistics'],
            'Eve': ['Physics', 'Chemistry', 'Biology']
        }
        
        print("学生选课情况:")
        for student, courses in student_courses.items():
            print(f"  {student}: {courses}")
        
        # 将课程组合转换为frozenset，用作分组键
        course_groups = {}
        for student, courses in student_courses.items():
            course_set = frozenset(courses)
            if course_set not in course_groups:
                course_groups[course_set] = []
            course_groups[course_set].append(student)
        
        print("\n相同选课组合的学生:")
        for courses, students in course_groups.items():
            if len(students) > 1:
                print(f"  课程{set(courses)}: {students}")
        
        # 找出课程重叠度
        print("\n学生间课程重叠分析:")
        students = list(student_courses.keys())
        for i in range(len(students)):
            for j in range(i + 1, len(students)):
                student1, student2 = students[i], students[j]
                courses1 = frozenset(student_courses[student1])
                courses2 = frozenset(student_courses[student2])
                
                overlap = courses1 & courses2
                if overlap:
                    print(f"  {student1}和{student2}的共同课程: {set(overlap)}")
    
    # 练习3：图算法应用
    def exercise_3():
        print("\n3. 图算法应用:")
        
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
            
            def get_connected_components(self):
                """获取连通分量"""
                visited = set()
                components = []
                
                def dfs(node, component):
                    if node in visited:
                        return
                    visited.add(node)
                    component.add(node)
                    
                    for neighbor in self.get_neighbors(node):
                        dfs(neighbor, component)
                
                for node in self.nodes:
                    if node not in visited:
                        component = set()
                        dfs(node, component)
                        components.append(frozenset(component))
                
                return components
        
        # 创建图
        graph = SimpleGraph()
        
        # 添加边
        edges = [
            ('A', 'B'), ('B', 'C'), ('C', 'A'),  # 三角形
            ('D', 'E'), ('E', 'F'),              # 链
            ('G', 'H'), ('H', 'I'), ('I', 'G'),  # 另一个三角形
            ('J',)  # 孤立节点（通过添加自环模拟）
        ]
        
        for edge in edges:
            if len(edge) == 2:
                graph.add_edge(edge[0], edge[1])
            else:
                graph.nodes.add(edge[0])  # 孤立节点
        
        print(f"图的节点: {graph.nodes}")
        print(f"图的边: {[set(edge) for edge in graph.edges]}")
        
        # 查找三角形
        triangles = graph.find_triangles()
        print(f"\n三角形: {[set(triangle) for triangle in triangles]}")
        
        # 查找连通分量
        components = graph.get_connected_components()
        print(f"连通分量: {[set(comp) for comp in components]}")
        
        # 分析每个节点的度
        print("\n节点度分析:")
        for node in sorted(graph.nodes):
            degree = len(graph.get_neighbors(node))
            neighbors = graph.get_neighbors(node)
            print(f"  {node}: 度={degree}, 邻居={neighbors}")
    
    exercise_1()
    exercise_2()
    exercise_3()

if __name__ == "__main__":
    main()
    demonstrate_as_dict_keys()
    demonstrate_as_set_elements()
    demonstrate_practical_applications()
    demonstrate_performance_comparison()
    best_practices()
    practice_exercises()