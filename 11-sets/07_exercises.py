#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
集合综合练习

本文件包含了集合相关的综合练习题，涵盖：
1. 基础集合操作练习
2. 集合数学运算练习
3. 集合推导式练习
4. frozenset应用练习
5. 实际问题解决练习
6. 性能优化练习
7. 高级应用练习

作者：Python学习教程
日期：2024年
"""

import time
import random
from collections import defaultdict, Counter

def exercise_1_basic_operations():
    """
    练习1：基础集合操作
    """
    print("练习1：基础集合操作")
    print("-" * 30)
    
    # 题目1：去重和统计
    def problem_1():
        print("题目1：处理重复数据")
        
        # 原始数据（包含重复）
        data = [1, 2, 3, 2, 4, 1, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10]
        print(f"原始数据: {data}")
        
        # 任务：去重并统计原始长度和去重后长度
        unique_data = set(data)
        print(f"去重后: {sorted(unique_data)}")
        print(f"原始长度: {len(data)}")
        print(f"去重后长度: {len(unique_data)}")
        print(f"重复元素数量: {len(data) - len(unique_data)}")
        
        # 找出重复的元素
        seen = set()
        duplicates = set()
        for item in data:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
        
        print(f"重复的元素: {sorted(duplicates)}")
    
    # 题目2：集合成员检查
    def problem_2():
        print("\n题目2：快速成员检查")
        
        # 创建大型数据集
        large_dataset = set(range(0, 100000, 2))  # 偶数集合
        test_numbers = [1, 2, 99, 100, 999, 1000, 9999, 10000, 99999, 100000]
        
        print(f"数据集大小: {len(large_dataset)}")
        print("成员检查结果:")
        
        for num in test_numbers:
            is_member = num in large_dataset
            print(f"  {num}: {'存在' if is_member else '不存在'}")
        
        # 性能对比：集合 vs 列表
        large_list = list(range(0, 100000, 2))
        
        # 测试集合查找性能
        start_time = time.time()
        for _ in range(1000):
            result = 99999 in large_dataset
        set_time = time.time() - start_time
        
        # 测试列表查找性能
        start_time = time.time()
        for _ in range(1000):
            result = 99999 in large_list
        list_time = time.time() - start_time
        
        print(f"\n性能对比（1000次查找）:")
        print(f"集合查找时间: {set_time:.6f}秒")
        print(f"列表查找时间: {list_time:.6f}秒")
        print(f"集合比列表快: {list_time/set_time:.1f}倍")
    
    # 题目3：动态集合操作
    def problem_3():
        print("\n题目3：动态集合管理")
        
        # 模拟在线用户管理
        online_users = set()
        
        # 用户上线
        def user_login(user_id):
            online_users.add(user_id)
            print(f"用户{user_id}上线，当前在线: {len(online_users)}人")
        
        # 用户下线
        def user_logout(user_id):
            if user_id in online_users:
                online_users.remove(user_id)
                print(f"用户{user_id}下线，当前在线: {len(online_users)}人")
            else:
                print(f"用户{user_id}不在线")
        
        # 批量操作
        def batch_login(user_ids):
            online_users.update(user_ids)
            print(f"批量上线{len(user_ids)}人，当前在线: {len(online_users)}人")
        
        # 模拟操作
        print("模拟用户上下线:")
        user_login("user1")
        user_login("user2")
        user_login("user3")
        
        batch_login(["user4", "user5", "user6"])
        
        user_logout("user2")
        user_logout("user7")  # 不存在的用户
        
        print(f"最终在线用户: {sorted(online_users)}")
    
    problem_1()
    problem_2()
    problem_3()

def exercise_2_set_mathematics():
    """
    练习2：集合数学运算
    """
    print("\n练习2：集合数学运算")
    print("-" * 30)
    
    # 题目1：学生选课分析
    def problem_1():
        print("题目1：学生选课分析")
        
        # 课程选择数据
        courses = {
            'math': {'Alice', 'Bob', 'Charlie', 'David', 'Eve'},
            'physics': {'Bob', 'Charlie', 'Frank', 'Grace'},
            'chemistry': {'Alice', 'Charlie', 'Eve', 'Frank'},
            'biology': {'David', 'Eve', 'Grace', 'Henry'},
            'computer_science': {'Alice', 'Bob', 'Frank', 'Henry'}
        }
        
        print("各课程选课情况:")
        for course, students in courses.items():
            print(f"  {course}: {sorted(students)} ({len(students)}人)")
        
        # 分析1：找出选了数学和物理的学生
        math_and_physics = courses['math'] & courses['physics']
        print(f"\n同时选数学和物理: {sorted(math_and_physics)}")
        
        # 分析2：找出选了数学但没选物理的学生
        math_not_physics = courses['math'] - courses['physics']
        print(f"选数学但不选物理: {sorted(math_not_physics)}")
        
        # 分析3：找出选了理科课程（数学、物理、化学）的学生
        science_students = courses['math'] | courses['physics'] | courses['chemistry']
        print(f"选理科课程的学生: {sorted(science_students)}")
        
        # 分析4：找出只选一门理科的学生
        math_only = courses['math'] - courses['physics'] - courses['chemistry']
        physics_only = courses['physics'] - courses['math'] - courses['chemistry']
        chemistry_only = courses['chemistry'] - courses['math'] - courses['physics']
        
        single_science = math_only | physics_only | chemistry_only
        print(f"只选一门理科: {sorted(single_science)}")
        
        # 分析5：课程重叠度分析
        print("\n课程重叠度分析:")
        course_names = list(courses.keys())
        for i in range(len(course_names)):
            for j in range(i + 1, len(course_names)):
                course1, course2 = course_names[i], course_names[j]
                overlap = courses[course1] & courses[course2]
                if overlap:
                    overlap_rate = len(overlap) / len(courses[course1] | courses[course2]) * 100
                    print(f"  {course1} & {course2}: {len(overlap)}人 ({overlap_rate:.1f}%重叠)")
    
    # 题目2：权限管理系统
    def problem_2():
        print("\n题目2：权限管理系统")
        
        # 定义权限组
        permissions = {
            'read_users': {'admin', 'manager', 'hr', 'employee'},
            'write_users': {'admin', 'manager', 'hr'},
            'delete_users': {'admin', 'manager'},
            'read_finance': {'admin', 'manager', 'finance'},
            'write_finance': {'admin', 'finance'},
            'read_reports': {'admin', 'manager', 'hr', 'finance'},
            'system_config': {'admin'}
        }
        
        print("权限分配:")
        for perm, roles in permissions.items():
            print(f"  {perm}: {sorted(roles)}")
        
        # 分析各角色的权限
        all_roles = set()
        for roles in permissions.values():
            all_roles.update(roles)
        
        print("\n各角色权限分析:")
        for role in sorted(all_roles):
            role_permissions = {perm for perm, roles in permissions.items() if role in roles}
            print(f"  {role}: {sorted(role_permissions)}")
        
        # 找出权限交集
        print("\n权限交集分析:")
        
        # 所有角色都有的权限
        common_permissions = set(permissions.keys())
        for perm, roles in permissions.items():
            if len(roles) != len(all_roles):
                common_permissions.discard(perm)
        
        print(f"所有角色共有权限: {sorted(common_permissions)}")
        
        # 只有管理员有的权限
        admin_only = set()
        for perm, roles in permissions.items():
            if roles == {'admin'}:
                admin_only.add(perm)
        
        print(f"仅管理员权限: {sorted(admin_only)}")
        
        # 权限升级路径分析
        print("\n权限升级路径:")
        role_hierarchy = ['employee', 'hr', 'finance', 'manager', 'admin']
        
        for i in range(len(role_hierarchy) - 1):
            current_role = role_hierarchy[i]
            next_role = role_hierarchy[i + 1]
            
            current_perms = {perm for perm, roles in permissions.items() if current_role in roles}
            next_perms = {perm for perm, roles in permissions.items() if next_role in roles}
            
            new_perms = next_perms - current_perms
            if new_perms:
                print(f"  {current_role} -> {next_role}: 新增 {sorted(new_perms)}")
    
    problem_1()
    problem_2()

def exercise_3_set_comprehensions():
    """
    练习3：集合推导式练习
    """
    print("\n练习3：集合推导式练习")
    print("-" * 30)
    
    # 题目1：数字处理
    def problem_1():
        print("题目1：数字集合处理")
        
        # 生成特殊数字集合
        numbers = range(1, 101)
        
        # 完全平方数
        perfect_squares = {x for x in numbers if int(x**0.5)**2 == x}
        print(f"1-100的完全平方数: {sorted(perfect_squares)}")
        
        # 质数（简单判断）
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        primes = {x for x in numbers if is_prime(x)}
        print(f"1-100的质数: {sorted(primes)}")
        
        # 回文数
        palindromes = {x for x in numbers if str(x) == str(x)[::-1]}
        print(f"1-100的回文数: {sorted(palindromes)}")
        
        # 各位数字之和为偶数的数
        even_digit_sum = {x for x in numbers if sum(int(d) for d in str(x)) % 2 == 0}
        print(f"各位数字和为偶数: {len(even_digit_sum)}个")
        
        # 组合分析
        print("\n组合分析:")
        print(f"既是完全平方数又是质数: {perfect_squares & primes}")
        print(f"既是质数又是回文数: {primes & palindromes}")
        print(f"完全平方数中的回文数: {perfect_squares & palindromes}")
    
    # 题目2：字符串处理
    def problem_2():
        print("\n题目2：字符串集合处理")
        
        # 文本数据
        text = """
        Python is a powerful programming language.
        It is easy to learn and has great libraries.
        Python is used for web development, data science, and AI.
        Many companies use Python for their projects.
        """
        
        words = text.lower().split()
        
        # 清理标点符号
        import string
        clean_words = {word.strip(string.punctuation) for word in words if word.strip(string.punctuation)}
        print(f"唯一单词数: {len(clean_words)}")
        
        # 长单词（超过5个字符）
        long_words = {word for word in clean_words if len(word) > 5}
        print(f"长单词: {sorted(long_words)}")
        
        # 包含特定字母的单词
        words_with_p = {word for word in clean_words if 'p' in word}
        print(f"包含字母'p'的单词: {sorted(words_with_p)}")
        
        # 元音字母开头的单词
        vowels = set('aeiou')
        vowel_start = {word for word in clean_words if word and word[0] in vowels}
        print(f"元音开头的单词: {sorted(vowel_start)}")
        
        # 回文单词
        palindrome_words = {word for word in clean_words if len(word) > 2 and word == word[::-1]}
        print(f"回文单词: {sorted(palindrome_words)}")
        
        # 字母频率分析
        all_letters = {char for word in clean_words for char in word if char.isalpha()}
        print(f"使用的字母: {sorted(all_letters)}")
        print(f"字母种类数: {len(all_letters)}")
    
    # 题目3：嵌套数据处理
    def problem_3():
        print("\n题目3：嵌套数据处理")
        
        # 学生成绩数据
        students_grades = {
            'Alice': [85, 92, 78, 96, 88],
            'Bob': [79, 85, 91, 82, 87],
            'Charlie': [92, 88, 95, 89, 93],
            'David': [76, 82, 79, 85, 80],
            'Eve': [88, 91, 87, 94, 90]
        }
        
        # 平均分超过85的学生
        high_performers = {name for name, grades in students_grades.items() 
                          if sum(grades) / len(grades) > 85}
        print(f"平均分超过85的学生: {sorted(high_performers)}")
        
        # 有满分（95+）成绩的学生
        excellent_scores = {name for name, grades in students_grades.items() 
                           if any(grade >= 95 for grade in grades)}
        print(f"有满分成绩的学生: {sorted(excellent_scores)}")
        
        # 成绩稳定（标准差小于5）的学生
        def std_dev(grades):
            mean = sum(grades) / len(grades)
            variance = sum((x - mean) ** 2 for x in grades) / len(grades)
            return variance ** 0.5
        
        stable_students = {name for name, grades in students_grades.items() 
                          if std_dev(grades) < 5}
        print(f"成绩稳定的学生: {sorted(stable_students)}")
        
        # 所有出现过的分数
        all_scores = {score for grades in students_grades.values() for score in grades}
        print(f"所有分数范围: {min(all_scores)} - {max(all_scores)}")
        
        # 每个分数段的学生数
        score_ranges = {
            '90+': {name for name, grades in students_grades.items() 
                   if any(grade >= 90 for grade in grades)},
            '80-89': {name for name, grades in students_grades.items() 
                     if any(80 <= grade < 90 for grade in grades)},
            '70-79': {name for name, grades in students_grades.items() 
                     if any(70 <= grade < 80 for grade in grades)}
        }
        
        print("\n分数段分布:")
        for range_name, students in score_ranges.items():
            print(f"  {range_name}: {sorted(students)}")
    
    problem_1()
    problem_2()
    problem_3()

def exercise_4_frozenset_applications():
    """
    练习4：frozenset应用练习
    """
    print("\n练习4：frozenset应用练习")
    print("-" * 30)
    
    # 题目1：配置管理
    def problem_1():
        print("题目1：应用配置管理")
        
        class ConfigManager:
            def __init__(self):
                self.configs = {}
                self.config_history = []
            
            def create_config(self, name, features):
                """创建配置"""
                config = frozenset(features)
                self.configs[name] = config
                self.config_history.append((name, 'create', config))
                return config
            
            def update_config(self, name, new_features):
                """更新配置"""
                if name in self.configs:
                    old_config = self.configs[name]
                    new_config = frozenset(new_features)
                    self.configs[name] = new_config
                    self.config_history.append((name, 'update', new_config))
                    return old_config, new_config
                return None
            
            def merge_configs(self, config1_name, config2_name, new_name):
                """合并配置"""
                if config1_name in self.configs and config2_name in self.configs:
                    merged = self.configs[config1_name] | self.configs[config2_name]
                    self.configs[new_name] = merged
                    self.config_history.append((new_name, 'merge', merged))
                    return merged
                return None
            
            def find_compatible_configs(self, required_features):
                """查找兼容配置"""
                required = frozenset(required_features)
                compatible = {}
                for name, config in self.configs.items():
                    if required.issubset(config):
                        compatible[name] = config
                return compatible
            
            def get_config_diff(self, config1_name, config2_name):
                """获取配置差异"""
                if config1_name in self.configs and config2_name in self.configs:
                    config1 = self.configs[config1_name]
                    config2 = self.configs[config2_name]
                    
                    return {
                        'only_in_1': config1 - config2,
                        'only_in_2': config2 - config1,
                        'common': config1 & config2,
                        'all_features': config1 | config2
                    }
                return None
        
        # 使用配置管理器
        config_mgr = ConfigManager()
        
        # 创建不同的应用配置
        config_mgr.create_config('web_basic', ['http', 'logging', 'error_handling'])
        config_mgr.create_config('web_advanced', ['http', 'logging', 'error_handling', 'ssl', 'compression'])
        config_mgr.create_config('api_service', ['http', 'logging', 'json_api', 'auth', 'rate_limiting'])
        config_mgr.create_config('microservice', ['http', 'logging', 'json_api', 'auth', 'service_discovery'])
        
        print("配置列表:")
        for name, config in config_mgr.configs.items():
            print(f"  {name}: {sorted(config)}")
        
        # 查找需要特定功能的配置
        required = ['http', 'auth']
        compatible = config_mgr.find_compatible_configs(required)
        print(f"\n支持{required}的配置:")
        for name, config in compatible.items():
            print(f"  {name}: {sorted(config)}")
        
        # 配置对比
        diff = config_mgr.get_config_diff('web_advanced', 'api_service')
        if diff:
            print(f"\nweb_advanced vs api_service:")
            print(f"  仅web_advanced有: {sorted(diff['only_in_1'])}")
            print(f"  仅api_service有: {sorted(diff['only_in_2'])}")
            print(f"  共同功能: {sorted(diff['common'])}")
        
        # 合并配置
        merged = config_mgr.merge_configs('web_advanced', 'api_service', 'full_stack')
        if merged:
            print(f"\n合并后的full_stack配置: {sorted(merged)}")
    
    # 题目2：图数据结构
    def problem_2():
        print("\n题目2：社交网络图分析")
        
        class SocialNetwork:
            def __init__(self):
                self.friendships = set()  # 存储frozenset形式的友谊关系
                self.users = set()
            
            def add_friendship(self, user1, user2):
                """添加友谊关系"""
                friendship = frozenset([user1, user2])
                self.friendships.add(friendship)
                self.users.add(user1)
                self.users.add(user2)
            
            def remove_friendship(self, user1, user2):
                """移除友谊关系"""
                friendship = frozenset([user1, user2])
                self.friendships.discard(friendship)
            
            def get_friends(self, user):
                """获取用户的朋友列表"""
                friends = set()
                for friendship in self.friendships:
                    if user in friendship:
                        friends.update(friendship - {user})
                return friends
            
            def get_mutual_friends(self, user1, user2):
                """获取共同朋友"""
                friends1 = self.get_friends(user1)
                friends2 = self.get_friends(user2)
                return friends1 & friends2
            
            def suggest_friends(self, user):
                """朋友推荐（朋友的朋友）"""
                user_friends = self.get_friends(user)
                suggestions = set()
                
                for friend in user_friends:
                    friend_friends = self.get_friends(friend)
                    # 排除自己和已经是朋友的人
                    suggestions.update(friend_friends - user_friends - {user})
                
                return suggestions
            
            def find_friend_groups(self):
                """查找朋友圈（连通分量）"""
                visited = set()
                groups = []
                
                def dfs(user, group):
                    if user in visited:
                        return
                    visited.add(user)
                    group.add(user)
                    
                    for friend in self.get_friends(user):
                        dfs(friend, group)
                
                for user in self.users:
                    if user not in visited:
                        group = set()
                        dfs(user, group)
                        if group:
                            groups.append(frozenset(group))
                
                return groups
            
            def get_network_stats(self):
                """获取网络统计信息"""
                total_users = len(self.users)
                total_friendships = len(self.friendships)
                
                # 计算每个用户的朋友数
                friend_counts = {user: len(self.get_friends(user)) for user in self.users}
                
                avg_friends = sum(friend_counts.values()) / total_users if total_users > 0 else 0
                max_friends = max(friend_counts.values()) if friend_counts else 0
                min_friends = min(friend_counts.values()) if friend_counts else 0
                
                return {
                    'total_users': total_users,
                    'total_friendships': total_friendships,
                    'avg_friends': avg_friends,
                    'max_friends': max_friends,
                    'min_friends': min_friends,
                    'friend_counts': friend_counts
                }
        
        # 创建社交网络
        network = SocialNetwork()
        
        # 添加友谊关系
        friendships = [
            ('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'David'),
            ('Charlie', 'David'), ('Charlie', 'Eve'), ('David', 'Frank'),
            ('Eve', 'Frank'), ('Grace', 'Henry'), ('Grace', 'Ivy')
        ]
        
        for user1, user2 in friendships:
            network.add_friendship(user1, user2)
        
        print(f"网络用户: {sorted(network.users)}")
        print(f"友谊关系数: {len(network.friendships)}")
        
        # 分析每个用户的朋友
        print("\n用户朋友列表:")
        for user in sorted(network.users):
            friends = network.get_friends(user)
            print(f"  {user}: {sorted(friends)}")
        
        # 共同朋友分析
        print("\n共同朋友分析:")
        users_list = list(network.users)
        for i in range(len(users_list)):
            for j in range(i + 1, len(users_list)):
                user1, user2 = users_list[i], users_list[j]
                mutual = network.get_mutual_friends(user1, user2)
                if mutual:
                    print(f"  {user1} & {user2}: {sorted(mutual)}")
        
        # 朋友推荐
        print("\n朋友推荐:")
        for user in ['Alice', 'Bob', 'Grace']:
            suggestions = network.suggest_friends(user)
            if suggestions:
                print(f"  为{user}推荐: {sorted(suggestions)}")
        
        # 朋友圈分析
        groups = network.find_friend_groups()
        print(f"\n朋友圈数量: {len(groups)}")
        for i, group in enumerate(groups, 1):
            print(f"  圈子{i}: {sorted(group)}")
        
        # 网络统计
        stats = network.get_network_stats()
        print(f"\n网络统计:")
        print(f"  总用户数: {stats['total_users']}")
        print(f"  总友谊数: {stats['total_friendships']}")
        print(f"  平均朋友数: {stats['avg_friends']:.1f}")
        print(f"  最多朋友数: {stats['max_friends']}")
        print(f"  最少朋友数: {stats['min_friends']}")
    
    problem_1()
    problem_2()

def exercise_5_performance_optimization():
    """
    练习5：性能优化练习
    """
    print("\n练习5：性能优化练习")
    print("-" * 30)
    
    # 题目1：大数据去重
    def problem_1():
        print("题目1：大数据去重优化")
        
        # 生成大量重复数据
        def generate_data(size):
            return [random.randint(1, size // 10) for _ in range(size)]
        
        data_size = 100000
        test_data = generate_data(data_size)
        
        print(f"测试数据大小: {len(test_data)}")
        
        # 方法1：使用列表去重（低效）
        def dedupe_with_list(data):
            result = []
            for item in data:
                if item not in result:
                    result.append(item)
            return result
        
        # 方法2：使用集合去重（高效）
        def dedupe_with_set(data):
            return list(set(data))
        
        # 方法3：保持顺序的集合去重
        def dedupe_with_set_ordered(data):
            seen = set()
            result = []
            for item in data:
                if item not in seen:
                    seen.add(item)
                    result.append(item)
            return result
        
        # 性能测试（使用小数据集避免超时）
        small_data = test_data[:1000]
        
        # 测试列表方法
        start_time = time.time()
        result1 = dedupe_with_list(small_data)
        list_time = time.time() - start_time
        
        # 测试集合方法
        start_time = time.time()
        result2 = dedupe_with_set(small_data)
        set_time = time.time() - start_time
        
        # 测试有序集合方法
        start_time = time.time()
        result3 = dedupe_with_set_ordered(small_data)
        ordered_time = time.time() - start_time
        
        print(f"\n去重结果（前1000个元素）:")
        print(f"原始长度: {len(small_data)}")
        print(f"去重后长度: {len(result1)}")
        
        print(f"\n性能对比:")
        print(f"列表方法: {list_time:.6f}秒")
        print(f"集合方法: {set_time:.6f}秒")
        print(f"有序集合方法: {ordered_time:.6f}秒")
        
        if list_time > 0:
            print(f"集合比列表快: {list_time/set_time:.1f}倍")
    
    # 题目2：快速查找优化
    def problem_2():
        print("\n题目2：快速查找优化")
        
        # 创建测试数据
        large_list = list(range(100000))
        large_set = set(large_list)
        
        # 测试查找性能
        search_items = [99999, 50000, 1, 99998, 0]
        
        # 列表查找
        start_time = time.time()
        for item in search_items:
            for _ in range(1000):
                result = item in large_list
        list_search_time = time.time() - start_time
        
        # 集合查找
        start_time = time.time()
        for item in search_items:
            for _ in range(1000):
                result = item in large_set
        set_search_time = time.time() - start_time
        
        print(f"查找性能对比（{len(search_items)}个元素，各查找1000次）:")
        print(f"列表查找: {list_search_time:.6f}秒")
        print(f"集合查找: {set_search_time:.6f}秒")
        print(f"集合比列表快: {list_search_time/set_search_time:.1f}倍")
        
        # 内存使用对比
        import sys
        list_memory = sys.getsizeof(large_list)
        set_memory = sys.getsizeof(large_set)
        
        print(f"\n内存使用对比:")
        print(f"列表内存: {list_memory:,}字节")
        print(f"集合内存: {set_memory:,}字节")
        print(f"集合内存是列表的: {set_memory/list_memory:.1f}倍")
    
    # 题目3：集合运算优化
    def problem_3():
        print("\n题目3：集合运算优化")
        
        # 创建大型集合
        set1 = set(range(0, 50000, 2))  # 偶数
        set2 = set(range(0, 50000, 3))  # 3的倍数
        set3 = set(range(0, 50000, 5))  # 5的倍数
        
        print(f"集合大小: {len(set1)}, {len(set2)}, {len(set3)}")
        
        # 复杂运算：找出既是偶数又是3的倍数但不是5的倍数的数
        
        # 方法1：逐步运算
        start_time = time.time()
        result1 = (set1 & set2) - set3
        method1_time = time.time() - start_time
        
        # 方法2：链式运算
        start_time = time.time()
        result2 = set1.intersection(set2).difference(set3)
        method2_time = time.time() - start_time
        
        # 方法3：使用推导式
        start_time = time.time()
        result3 = {x for x in range(0, 50000) if x % 2 == 0 and x % 3 == 0 and x % 5 != 0}
        method3_time = time.time() - start_time
        
        print(f"\n运算结果大小: {len(result1)}")
        print(f"结果一致性: {result1 == result2 == result3}")
        
        print(f"\n性能对比:")
        print(f"运算符方法: {method1_time:.6f}秒")
        print(f"方法调用: {method2_time:.6f}秒")
        print(f"推导式方法: {method3_time:.6f}秒")
        
        # 显示部分结果
        sample_result = sorted(list(result1))[:10]
        print(f"结果示例: {sample_result}")
    
    problem_1()
    problem_2()
    problem_3()

def exercise_6_advanced_applications():
    """
    练习6：高级应用练习
    """
    print("\n练习6：高级应用练习")
    print("-" * 30)
    
    # 题目1：数据分析应用
    def problem_1():
        print("题目1：电商数据分析")
        
        # 模拟电商数据
        customers = {
            'customer1': {'products': {'laptop', 'mouse', 'keyboard'}, 'categories': {'electronics', 'accessories'}},
            'customer2': {'products': {'book1', 'book2', 'pen'}, 'categories': {'books', 'stationery'}},
            'customer3': {'products': {'laptop', 'book1', 'headphones'}, 'categories': {'electronics', 'books'}},
            'customer4': {'products': {'mouse', 'keyboard', 'monitor'}, 'categories': {'electronics', 'accessories'}},
            'customer5': {'products': {'book2', 'notebook', 'pen'}, 'categories': {'books', 'stationery'}}
        }
        
        print("客户购买数据:")
        for customer, data in customers.items():
            print(f"  {customer}: 产品{len(data['products'])}个, 类别{data['categories']}")
        
        # 分析1：找出购买相似产品的客户
        print("\n相似购买行为分析:")
        customer_list = list(customers.keys())
        for i in range(len(customer_list)):
            for j in range(i + 1, len(customer_list)):
                c1, c2 = customer_list[i], customer_list[j]
                
                # 产品重叠度
                products1 = customers[c1]['products']
                products2 = customers[c2]['products']
                common_products = products1 & products2
                
                # 类别重叠度
                categories1 = customers[c1]['categories']
                categories2 = customers[c2]['categories']
                common_categories = categories1 & categories2
                
                if common_products or common_categories:
                    print(f"  {c1} & {c2}:")
                    if common_products:
                        print(f"    共同产品: {common_products}")
                    if common_categories:
                        print(f"    共同类别: {common_categories}")
        
        # 分析2：产品推荐
        def recommend_products(target_customer, customers_data):
            target_products = customers_data[target_customer]['products']
            target_categories = customers_data[target_customer]['categories']
            
            recommendations = set()
            
            # 基于相似客户推荐
            for customer, data in customers_data.items():
                if customer != target_customer:
                    # 如果有共同类别，推荐该客户的其他产品
                    if data['categories'] & target_categories:
                        recommendations.update(data['products'] - target_products)
            
            return recommendations
        
        print("\n产品推荐:")
        for customer in ['customer1', 'customer3']:
            recommendations = recommend_products(customer, customers)
            print(f"  为{customer}推荐: {recommendations}")
        
        # 分析3：市场细分
        category_customers = defaultdict(set)
        for customer, data in customers.items():
            for category in data['categories']:
                category_customers[category].add(customer)
        
        print("\n市场细分:")
        for category, customer_set in category_customers.items():
            print(f"  {category}: {sorted(customer_set)}")
        
        # 交叉销售机会
        print("\n交叉销售机会:")
        categories = list(category_customers.keys())
        for i in range(len(categories)):
            for j in range(i + 1, len(categories)):
                cat1, cat2 = categories[i], categories[j]
                cross_customers = category_customers[cat1] & category_customers[cat2]
                if cross_customers:
                    print(f"  {cat1} & {cat2}: {sorted(cross_customers)}")
    
    # 题目2：文本分析应用
    def problem_2():
        print("\n题目2：文本相似度分析")
        
        # 文档数据
        documents = {
            'doc1': "Python is a powerful programming language for data science and web development",
            'doc2': "Java is a popular programming language used in enterprise applications",
            'doc3': "Data science involves statistics, machine learning, and programming",
            'doc4': "Web development requires knowledge of HTML, CSS, and JavaScript",
            'doc5': "Machine learning is a subset of artificial intelligence and data science"
        }
        
        # 预处理：提取单词集合
        import string
        
        def preprocess_text(text):
            # 转小写，移除标点，分词
            text = text.lower()
            text = text.translate(str.maketrans('', '', string.punctuation))
            words = set(text.split())
            # 移除常见停用词
            stop_words = {'is', 'a', 'and', 'the', 'of', 'in', 'for', 'used', 'with'}
            return words - stop_words
        
        doc_words = {}
        for doc_id, text in documents.items():
            doc_words[doc_id] = preprocess_text(text)
        
        print("文档关键词:")
        for doc_id, words in doc_words.items():
            print(f"  {doc_id}: {sorted(words)}")
        
        # 计算文档相似度（Jaccard相似度）
        def jaccard_similarity(set1, set2):
            intersection = len(set1 & set2)
            union = len(set1 | set2)
            return intersection / union if union > 0 else 0
        
        print("\n文档相似度矩阵:")
        doc_ids = list(doc_words.keys())
        
        # 打印表头
        print("     ", end="")
        for doc_id in doc_ids:
            print(f"{doc_id:>8}", end="")
        print()
        
        # 打印相似度矩阵
        for i, doc1 in enumerate(doc_ids):
            print(f"{doc1}: ", end="")
            for j, doc2 in enumerate(doc_ids):
                if i <= j:
                    similarity = jaccard_similarity(doc_words[doc1], doc_words[doc2])
                    print(f"{similarity:>8.3f}", end="")
                else:
                    print(f"{'':>8}", end="")
            print()
        
        # 找出最相似的文档对
        max_similarity = 0
        most_similar = None
        
        for i in range(len(doc_ids)):
            for j in range(i + 1, len(doc_ids)):
                doc1, doc2 = doc_ids[i], doc_ids[j]
                similarity = jaccard_similarity(doc_words[doc1], doc_words[doc2])
                if similarity > max_similarity:
                    max_similarity = similarity
                    most_similar = (doc1, doc2)
        
        if most_similar:
            print(f"\n最相似文档: {most_similar[0]} & {most_similar[1]} (相似度: {max_similarity:.3f})")
            common_words = doc_words[most_similar[0]] & doc_words[most_similar[1]]
            print(f"共同关键词: {sorted(common_words)}")
        
        # 主题聚类（简单版本）
        print("\n主题词分析:")
        all_words = set()
        for words in doc_words.values():
            all_words.update(words)
        
        # 统计每个词出现在多少文档中
        word_doc_count = {}
        for word in all_words:
            count = sum(1 for words in doc_words.values() if word in words)
            word_doc_count[word] = count
        
        # 找出高频词（出现在多个文档中）
        frequent_words = {word for word, count in word_doc_count.items() if count >= 2}
        print(f"高频主题词: {sorted(frequent_words)}")
        
        # 为每个文档找出独特词汇
        print("\n文档独特词汇:")
        for doc_id, words in doc_words.items():
            unique_words = words - frequent_words
            if unique_words:
                print(f"  {doc_id}: {sorted(unique_words)}")
    
    problem_1()
    problem_2()

def final_challenge():
    """
    终极挑战：综合应用
    """
    print("\n终极挑战：学生课程推荐系统")
    print("=" * 40)
    
    class CourseRecommendationSystem:
        def __init__(self):
            self.students = {}  # 学生信息
            self.courses = {}   # 课程信息
            self.enrollments = defaultdict(set)  # 学生选课记录
            self.course_students = defaultdict(set)  # 课程学生记录
        
        def add_student(self, student_id, interests, completed_courses=None):
            """添加学生"""
            self.students[student_id] = {
                'interests': frozenset(interests),
                'completed': frozenset(completed_courses or [])
            }
        
        def add_course(self, course_id, topics, prerequisites=None, difficulty=1):
            """添加课程"""
            self.courses[course_id] = {
                'topics': frozenset(topics),
                'prerequisites': frozenset(prerequisites or []),
                'difficulty': difficulty
            }
        
        def enroll_student(self, student_id, course_id):
            """学生选课"""
            if self.can_enroll(student_id, course_id):
                self.enrollments[student_id].add(course_id)
                self.course_students[course_id].add(student_id)
                return True
            return False
        
        def can_enroll(self, student_id, course_id):
            """检查是否可以选课"""
            if student_id not in self.students or course_id not in self.courses:
                return False
            
            student = self.students[student_id]
            course = self.courses[course_id]
            
            # 检查先修课程
            completed = student['completed'] | self.enrollments[student_id]
            return course['prerequisites'].issubset(completed)
        
        def recommend_courses(self, student_id, max_recommendations=5):
            """为学生推荐课程"""
            if student_id not in self.students:
                return []
            
            student = self.students[student_id]
            student_interests = student['interests']
            completed_and_enrolled = student['completed'] | self.enrollments[student_id]
            
            recommendations = []
            
            for course_id, course in self.courses.items():
                # 跳过已完成或已选的课程
                if course_id in completed_and_enrolled:
                    continue
                
                # 检查是否满足先修要求
                if not self.can_enroll(student_id, course_id):
                    continue
                
                # 计算兴趣匹配度
                interest_match = len(student_interests & course['topics'])
                if interest_match > 0:
                    # 计算推荐分数
                    score = interest_match / len(course['topics'])
                    
                    # 考虑课程热度（选课人数）
                    popularity = len(self.course_students[course_id])
                    score += popularity * 0.1
                    
                    # 考虑难度（简单课程优先推荐给新手）
                    completed_count = len(student['completed'])
                    if completed_count < 3:  # 新手
                        score += (5 - course['difficulty']) * 0.1
                    
                    recommendations.append((course_id, score, interest_match))
            
            # 按分数排序
            recommendations.sort(key=lambda x: x[1], reverse=True)
            return recommendations[:max_recommendations]
        
        def find_study_partners(self, student_id):
            """找学习伙伴"""
            if student_id not in self.students:
                return []
            
            student_courses = self.enrollments[student_id]
            partners = set()
            
            # 找选了相同课程的学生
            for course_id in student_courses:
                partners.update(self.course_students[course_id])
            
            # 移除自己
            partners.discard(student_id)
            
            # 计算相似度
            partner_scores = []
            for partner_id in partners:
                partner_courses = self.enrollments[partner_id]
                common_courses = len(student_courses & partner_courses)
                total_courses = len(student_courses | partner_courses)
                
                if total_courses > 0:
                    similarity = common_courses / total_courses
                    partner_scores.append((partner_id, similarity, common_courses))
            
            # 按相似度排序
            partner_scores.sort(key=lambda x: x[1], reverse=True)
            return partner_scores[:5]
        
        def analyze_course_popularity(self):
            """分析课程热度"""
            popularity = {}
            for course_id in self.courses:
                student_count = len(self.course_students[course_id])
                popularity[course_id] = student_count
            
            return sorted(popularity.items(), key=lambda x: x[1], reverse=True)
        
        def get_learning_path(self, student_id, target_topics):
            """生成学习路径"""
            target_set = frozenset(target_topics)
            student = self.students[student_id]
            completed = student['completed'] | self.enrollments[student_id]
            
            # 找出覆盖目标主题的课程
            relevant_courses = []
            for course_id, course in self.courses.items():
                if course_id not in completed and course['topics'] & target_set:
                    coverage = len(course['topics'] & target_set)
                    relevant_courses.append((course_id, coverage, course['difficulty']))
            
            # 按覆盖度和难度排序
            relevant_courses.sort(key=lambda x: (x[1], -x[2]), reverse=True)
            
            # 生成学习路径
            path = []
            covered_topics = set()
            
            for course_id, coverage, difficulty in relevant_courses:
                if len(covered_topics) >= len(target_set):
                    break
                
                course = self.courses[course_id]
                new_topics = course['topics'] & target_set - covered_topics
                
                if new_topics and self.can_enroll(student_id, course_id):
                    path.append((course_id, new_topics))
                    covered_topics.update(new_topics)
            
            return path, covered_topics
    
    # 创建推荐系统并添加数据
    system = CourseRecommendationSystem()
    
    # 添加学生
    system.add_student('alice', ['programming', 'data_science', 'math'], ['intro_cs'])
    system.add_student('bob', ['web_dev', 'programming', 'design'], ['intro_cs', 'html_css'])
    system.add_student('charlie', ['ai', 'math', 'data_science'], ['intro_cs', 'calculus'])
    system.add_student('david', ['programming', 'algorithms'], [])
    
    # 添加课程
    courses_data = [
        ('python_basics', ['programming', 'python'], ['intro_cs'], 2),
        ('web_development', ['web_dev', 'programming', 'html'], ['intro_cs'], 2),
        ('data_structures', ['programming', 'algorithms'], ['python_basics'], 3),
        ('machine_learning', ['ai', 'data_science', 'math'], ['python_basics', 'calculus'], 4),
        ('statistics', ['math', 'data_science'], ['calculus'], 3),
        ('database_design', ['programming', 'data_management'], ['intro_cs'], 2),
        ('advanced_algorithms', ['algorithms', 'programming'], ['data_structures'], 4),
        ('deep_learning', ['ai', 'data_science'], ['machine_learning'], 5)
    ]
    
    for course_id, topics, prereqs, difficulty in courses_data:
        system.add_course(course_id, topics, prereqs, difficulty)
    
    # 模拟一些选课
    system.enroll_student('alice', 'python_basics')
    system.enroll_student('alice', 'statistics')
    system.enroll_student('bob', 'python_basics')
    system.enroll_student('bob', 'web_development')
    system.enroll_student('charlie', 'python_basics')
    
    print("课程推荐系统演示")
    print("-" * 30)
    
    # 为学生推荐课程
    print("课程推荐:")
    for student_id in ['alice', 'bob', 'charlie', 'david']:
        recommendations = system.recommend_courses(student_id)
        print(f"\n为{student_id}推荐:")
        for course_id, score, interest_match in recommendations:
            course = system.courses[course_id]
            print(f"  {course_id}: 分数{score:.2f}, 兴趣匹配{interest_match}, 主题{sorted(course['topics'])}")
    
    # 找学习伙伴
    print("\n学习伙伴推荐:")
    for student_id in ['alice', 'bob']:
        partners = system.find_study_partners(student_id)
        if partners:
            print(f"\n{student_id}的学习伙伴:")
            for partner_id, similarity, common_count in partners:
                print(f"  {partner_id}: 相似度{similarity:.2f}, 共同课程{common_count}门")
    
    # 课程热度分析
    print("\n课程热度排行:")
    popularity = system.analyze_course_popularity()
    for course_id, student_count in popularity[:5]:
        print(f"  {course_id}: {student_count}人选课")
    
    # 学习路径规划
    print("\n学习路径规划:")
    target_topics = ['ai', 'data_science']
    for student_id in ['alice', 'charlie']:
        path, covered = system.get_learning_path(student_id, target_topics)
        print(f"\n{student_id}学习{target_topics}的路径:")
        for course_id, new_topics in path:
            print(f"  {course_id}: 学习{sorted(new_topics)}")
        print(f"  总覆盖: {sorted(covered)}")

def main():
    """
    主函数：运行所有练习
    """
    print("集合综合练习")
    print("=" * 50)
    
    try:
        exercise_1_basic_operations()
        exercise_2_set_mathematics()
        exercise_3_set_comprehensions()
        exercise_4_frozenset_applications()
        exercise_5_performance_optimization()
        exercise_6_advanced_applications()
        final_challenge()
        
        print("\n" + "=" * 50)
        print("所有练习完成！")
        print("\n学习要点总结:")
        print("1. 集合的基本操作：创建、添加、删除、查找")
        print("2. 集合数学运算：并集、交集、差集、对称差集")
        print("3. 集合推导式：高效创建和过滤集合")
        print("4. frozenset：不可变集合的应用场景")
        print("5. 性能优化：集合vs列表的查找和去重性能")
        print("6. 实际应用：数据分析、权限管理、推荐系统")
        
        print("\n练习建议:")
        print("- 多练习集合运算，理解数学概念")
        print("- 在需要去重和快速查找时优先考虑集合")
        print("- 学会使用frozenset作为字典键")
        print("- 掌握集合推导式的高级用法")
        print("- 在实际项目中应用集合解决问题")
        
    except Exception as e:
        print(f"练习过程中出现错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()