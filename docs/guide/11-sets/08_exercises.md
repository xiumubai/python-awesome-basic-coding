# 集合综合练习

## 学习目标

通过综合练习，掌握：
- 集合的基本操作和数学运算
- 集合推导式的高级应用
- frozenset的实际使用场景
- 集合在性能优化中的作用
- 集合在实际项目中的应用

## 概述

本章提供了一系列综合练习，涵盖集合的各个方面，从基础操作到高级应用，帮助你全面掌握Python集合的使用。

## 练习1：基础集合操作

### 去重和统计

```python
def exercise_1_basic_operations():
    """
    练习1：基础集合操作
    """
    print("练习1：基础集合操作")
    print("-" * 30)
    
    # 题目1：数据去重和统计
    def problem_1():
        print("题目1：数据去重和统计")
        
        # 原始数据（包含重复）
        raw_data = [1, 2, 3, 2, 4, 3, 5, 1, 6, 4, 7, 5, 8]
        print(f"原始数据: {raw_data}")
        print(f"原始长度: {len(raw_data)}")
        
        # 使用集合去重
        unique_data = set(raw_data)
        print(f"去重后: {sorted(unique_data)}")
        print(f"去重后长度: {len(unique_data)}")
        print(f"重复元素数量: {len(raw_data) - len(unique_data)}")
        
        # 统计重复次数
        from collections import Counter
        counter = Counter(raw_data)
        duplicates = {item: count for item, count in counter.items() if count > 1}
        print(f"重复元素统计: {duplicates}")
```

### 成员检查

```python
    # 题目2：高效成员检查
    def problem_2():
        print("\n题目2：高效成员检查")
        
        # 创建大数据集
        large_list = list(range(10000))
        large_set = set(large_list)
        
        # 测试查找性能
        import time
        
        # 在列表中查找
        start_time = time.time()
        result1 = 9999 in large_list
        list_time = time.time() - start_time
        
        # 在集合中查找
        start_time = time.time()
        result2 = 9999 in large_set
        set_time = time.time() - start_time
        
        print(f"列表查找时间: {list_time:.8f}秒")
        print(f"集合查找时间: {set_time:.8f}秒")
        if set_time > 0:
            print(f"集合比列表快: {list_time/set_time:.1f}倍")
```

### 动态集合操作

```python
    # 题目3：动态集合操作
    def problem_3():
        print("\n题目3：动态集合操作")
        
        # 模拟在线用户管理
        online_users = set()
        
        # 用户上线
        def user_login(username):
            online_users.add(username)
            print(f"{username} 上线，当前在线: {len(online_users)}人")
        
        # 用户下线
        def user_logout(username):
            if username in online_users:
                online_users.remove(username)
                print(f"{username} 下线，当前在线: {len(online_users)}人")
            else:
                print(f"{username} 不在线")
        
        # 模拟用户活动
        user_login("Alice")
        user_login("Bob")
        user_login("Charlie")
        print(f"在线用户: {sorted(online_users)}")
        
        user_logout("Bob")
        user_logout("David")  # 不存在的用户
        print(f"最终在线: {sorted(online_users)}")
```

## 练习2：集合数学运算

### 学生选课分析

```python
def exercise_2_set_mathematics():
    """
    练习2：集合数学运算
    """
    print("练习2：集合数学运算")
    print("-" * 30)
    
    # 题目1：学生选课分析
    def problem_1():
        print("题目1：学生选课分析")
        
        # 各科目选课学生
        math_students = {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}
        physics_students = {'Bob', 'Charlie', 'Frank', 'Grace'}
        chemistry_students = {'Alice', 'Charlie', 'Eve', 'Frank'}
        
        print(f"数学选课: {sorted(math_students)}")
        print(f"物理选课: {sorted(physics_students)}")
        print(f"化学选课: {sorted(chemistry_students)}")
        
        # 分析选课情况
        all_students = math_students | physics_students | chemistry_students
        print(f"\n所有学生: {sorted(all_students)}")
        print(f"总学生数: {len(all_students)}")
        
        # 同时选择多门课的学生
        math_physics = math_students & physics_students
        math_chemistry = math_students & chemistry_students
        physics_chemistry = physics_students & chemistry_students
        all_three = math_students & physics_students & chemistry_students
        
        print(f"\n数学+物理: {sorted(math_physics)}")
        print(f"数学+化学: {sorted(math_chemistry)}")
        print(f"物理+化学: {sorted(physics_chemistry)}")
        print(f"三门都选: {sorted(all_three)}")
        
        # 只选一门课的学生
        only_math = math_students - physics_students - chemistry_students
        only_physics = physics_students - math_students - chemistry_students
        only_chemistry = chemistry_students - math_students - physics_students
        
        print(f"\n只选数学: {sorted(only_math)}")
        print(f"只选物理: {sorted(only_physics)}")
        print(f"只选化学: {sorted(only_chemistry)}")
```

### 权限管理系统

```python
    # 题目2：权限管理系统
    def problem_2():
        print("\n题目2：权限管理系统")
        
        # 定义角色权限
        admin_permissions = {'read', 'write', 'delete', 'execute', 'manage_users'}
        editor_permissions = {'read', 'write', 'execute'}
        viewer_permissions = {'read'}
        guest_permissions = set()  # 空集合
        
        print("角色权限定义:")
        print(f"管理员: {sorted(admin_permissions)}")
        print(f"编辑者: {sorted(editor_permissions)}")
        print(f"查看者: {sorted(viewer_permissions)}")
        print(f"访客: {sorted(guest_permissions)}")
        
        # 用户权限分配（可能有多个角色）
        users = {
            'Alice': admin_permissions | editor_permissions,  # 管理员+编辑者
            'Bob': editor_permissions,                        # 编辑者
            'Charlie': viewer_permissions,                    # 查看者
            'David': guest_permissions                        # 访客
        }
        
        print("\n用户权限分配:")
        for user, permissions in users.items():
            print(f"{user}: {sorted(permissions)}")
        
        # 权限分析
        def analyze_permissions():
            all_permissions = set()
            for permissions in users.values():
                all_permissions.update(permissions)
            
            print(f"\n系统中所有权限: {sorted(all_permissions)}")
            
            # 找出有写权限的用户
            write_users = {user for user, perms in users.items() if 'write' in perms}
            print(f"有写权限的用户: {sorted(write_users)}")
            
            # 找出有删除权限的用户
            delete_users = {user for user, perms in users.items() if 'delete' in perms}
            print(f"有删除权限的用户: {sorted(delete_users)}")
            
            # 权限交集分析
            common_permissions = set.intersection(*[perms for perms in users.values() if perms])
            print(f"所有用户共同权限: {sorted(common_permissions)}")
        
        analyze_permissions()
```

## 练习3：集合推导式

### 数字处理

```python
def exercise_3_set_comprehensions():
    """
    练习3：集合推导式练习
    """
    print("练习3：集合推导式练习")
    print("-" * 30)
    
    # 题目1：数字处理
    def problem_1():
        print("题目1：数字处理")
        
        # 生成各种数字集合
        numbers = range(1, 101)
        
        # 完全平方数
        perfect_squares = {x for x in numbers if int(x**0.5)**2 == x}
        print(f"完全平方数: {sorted(perfect_squares)}")
        
        # 质数
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        primes = {x for x in numbers if is_prime(x)}
        print(f"质数（前10个): {sorted(list(primes)[:10])}")
        
        # 回文数
        palindromes = {x for x in numbers if str(x) == str(x)[::-1]}
        print(f"回文数: {sorted(palindromes)}")
        
        # 组合分析
        prime_squares = primes & perfect_squares
        print(f"既是质数又是完全平方数: {sorted(prime_squares)}")
        
        prime_palindromes = primes & palindromes
        print(f"既是质数又是回文数: {sorted(prime_palindromes)}")
```

### 字符串处理

```python
    # 题目2：字符串处理
    def problem_2():
        print("\n题目2：字符串处理")
        
        # 文本数据
        text = """Python is a powerful programming language.
        It is widely used in data science, web development,
        artificial intelligence, and automation."""
        
        # 提取单词
        import string
        words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
        print(f"所有单词: {words}")
        
        # 去重单词
        unique_words = {word for word in words}
        print(f"去重单词: {sorted(unique_words)}")
        
        # 长单词（超过5个字符）
        long_words = {word for word in unique_words if len(word) > 5}
        print(f"长单词: {sorted(long_words)}")
        
        # 包含特定字母的单词
        words_with_a = {word for word in unique_words if 'a' in word}
        print(f"包含'a'的单词: {sorted(words_with_a)}")
        
        # 元音字母开头的单词
        vowel_words = {word for word in unique_words if word[0] in 'aeiou'}
        print(f"元音开头的单词: {sorted(vowel_words)}")
```

### 嵌套数据处理

```python
    # 题目3：嵌套数据处理
    def problem_3():
        print("\n题目3：嵌套数据处理")
        
        # 学生成绩数据
        students_data = {
            'Alice': {'math': 95, 'physics': 87, 'chemistry': 92},
            'Bob': {'math': 78, 'physics': 85, 'chemistry': 79},
            'Charlie': {'math': 92, 'physics': 88, 'chemistry': 94},
            'David': {'math': 85, 'physics': 90, 'chemistry': 87}
        }
        
        # 优秀学生（平均分>85）
        excellent_students = {
            name for name, scores in students_data.items()
            if sum(scores.values()) / len(scores) > 85
        }
        print(f"优秀学生: {sorted(excellent_students)}")
        
        # 数学成绩优秀的学生（>90）
        math_excellent = {
            name for name, scores in students_data.items()
            if scores['math'] > 90
        }
        print(f"数学优秀: {sorted(math_excellent)}")
        
        # 全科优秀的学生（所有科目>85）
        all_excellent = {
            name for name, scores in students_data.items()
            if all(score > 85 for score in scores.values())
        }
        print(f"全科优秀: {sorted(all_excellent)}")
        
        # 需要补习的学生（任一科目<80）
        need_help = {
            name for name, scores in students_data.items()
            if any(score < 80 for score in scores.values())
        }
        print(f"需要补习: {sorted(need_help)}")
```

## 练习4：frozenset应用

### 配置管理

```python
def exercise_4_frozenset_applications():
    """
    练习4：frozenset应用练习
    """
    print("练习4：frozenset应用练习")
    print("-" * 30)
    
    # 题目1：配置管理
    def problem_1():
        print("题目1：配置管理")
        
        class ConfigManager:
            def __init__(self):
                self.configs = {}  # 使用frozenset作为键
            
            def create_config(self, name, features):
                """创建配置"""
                config_key = frozenset(features)
                self.configs[config_key] = {
                    'name': name,
                    'features': config_key,
                    'created_at': time.time()
                }
                return config_key
            
            def find_compatible_configs(self, required_features):
                """查找兼容配置"""
                required_set = frozenset(required_features)
                compatible = []
                
                for config_key, config_data in self.configs.items():
                    if required_set.issubset(config_key):
                        compatibility = len(required_set & config_key) / len(config_key)
                        compatible.append((config_data['name'], compatibility))
                
                return sorted(compatible, key=lambda x: x[1], reverse=True)
            
            def merge_configs(self, config_keys):
                """合并配置"""
                if not config_keys:
                    return frozenset()
                
                merged_features = set()
                for key in config_keys:
                    if key in self.configs:
                        merged_features.update(key)
                
                return frozenset(merged_features)
        
        # 使用配置管理器
        manager = ConfigManager()
        
        # 创建不同配置
        config1 = manager.create_config("基础版", ['login', 'view', 'search'])
        config2 = manager.create_config("专业版", ['login', 'view', 'search', 'edit', 'export'])
        config3 = manager.create_config("企业版", ['login', 'view', 'search', 'edit', 'export', 'admin', 'api'])
        
        print("已创建配置:")
        for key, config in manager.configs.items():
            print(f"  {config['name']}: {sorted(key)}")
        
        # 查找兼容配置
        required = ['login', 'edit']
        compatible = manager.find_compatible_configs(required)
        print(f"\n需要功能 {required} 的兼容配置:")
        for name, compatibility in compatible:
            print(f"  {name}: 兼容度 {compatibility:.2f}")
        
        # 合并配置
        merged = manager.merge_configs([config1, config2])
        print(f"\n合并配置功能: {sorted(merged)}")
```

### 社交网络图分析

```python
    # 题目2：社交网络图分析
    def problem_2():
        print("\n题目2：社交网络图分析")
        
        class SocialNetwork:
            def __init__(self):
                self.friendships = set()  # 存储frozenset对
                self.users = set()
            
            def add_friendship(self, user1, user2):
                """添加友谊关系"""
                friendship = frozenset([user1, user2])
                self.friendships.add(friendship)
                self.users.update([user1, user2])
            
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
                """推荐朋友"""
                user_friends = self.get_friends(user)
                suggestions = set()
                
                # 朋友的朋友
                for friend in user_friends:
                    friend_friends = self.get_friends(friend)
                    suggestions.update(friend_friends - user_friends - {user})
                
                return suggestions
        
        # 创建社交网络
        network = SocialNetwork()
        
        # 添加友谊关系
        friendships = [
            ('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'David'),
            ('Charlie', 'Eve'), ('David', 'Frank'), ('Eve', 'Frank'),
            ('Bob', 'Charlie'), ('Alice', 'Eve')
        ]
        
        for user1, user2 in friendships:
            network.add_friendship(user1, user2)
        
        print("社交网络分析:")
        print(f"总用户数: {len(network.users)}")
        print(f"友谊关系数: {len(network.friendships)}")
        
        # 显示每个用户的朋友
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
        for user in ['Alice', 'Bob']:
            suggestions = network.suggest_friends(user)
            if suggestions:
                print(f"  为{user}推荐: {sorted(suggestions)}")
```

## 练习5：性能优化

### 大数据去重

```python
def exercise_5_performance_optimization():
    """
    练习5：性能优化练习
    """
    print("练习5：性能优化练习")
    print("-" * 30)
    
    # 题目1：大数据去重
    def problem_1():
        print("题目1：大数据去重优化")
        
        import random
        import time
        
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
        
        # 测试各种方法的性能
        methods = [
            ("列表方法", dedupe_with_list),
            ("集合方法", dedupe_with_set),
            ("有序集合方法", dedupe_with_set_ordered)
        ]
        
        results = []
        for name, method in methods:
            start_time = time.time()
            result = method(small_data)
            elapsed = time.time() - start_time
            results.append((name, elapsed, len(result)))
        
        print(f"\n去重结果（前1000个元素）:")
        print(f"原始长度: {len(small_data)}")
        
        print(f"\n性能对比:")
        for name, elapsed, result_len in results:
            print(f"{name}: {elapsed:.6f}秒, 结果长度: {result_len}")
```

### 快速查找优化

```python
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
        if set_search_time > 0:
            print(f"集合比列表快: {list_search_time/set_search_time:.1f}倍")
        
        # 内存使用对比
        import sys
        list_memory = sys.getsizeof(large_list)
        set_memory = sys.getsizeof(large_set)
        
        print(f"\n内存使用对比:")
        print(f"列表内存: {list_memory:,}字节")
        print(f"集合内存: {set_memory:,}字节")
        print(f"集合内存是列表的: {set_memory/list_memory:.1f}倍")
```

## 练习6：高级应用

### 电商数据分析

```python
def exercise_6_advanced_applications():
    """
    练习6：高级应用练习
    """
    print("练习6：高级应用练习")
    print("-" * 30)
    
    # 题目1：电商数据分析
    def problem_1():
        print("题目1：电商数据分析")
        
        from collections import defaultdict
        
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
        
        # 产品推荐系统
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
```

### 文本相似度分析

```python
    # 题目2：文本相似度分析
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
        
        print("\n文档相似度分析:")
        doc_ids = list(doc_words.keys())
        
        # 找出最相似的文档对
        max_similarity = 0
        most_similar = None
        
        for i in range(len(doc_ids)):
            for j in range(i + 1, len(doc_ids)):
                doc1, doc2 = doc_ids[i], doc_ids[j]
                similarity = jaccard_similarity(doc_words[doc1], doc_words[doc2])
                print(f"  {doc1} & {doc2}: {similarity:.3f}")
                
                if similarity > max_similarity:
                    max_similarity = similarity
                    most_similar = (doc1, doc2)
        
        if most_similar:
            print(f"\n最相似文档: {most_similar[0]} & {most_similar[1]} (相似度: {max_similarity:.3f})")
            common_words = doc_words[most_similar[0]] & doc_words[most_similar[1]]
            print(f"共同关键词: {sorted(common_words)}")
```

## 终极挑战：课程推荐系统

```python
def final_challenge():
    """
    终极挑战：学生课程推荐系统
    """
    print("终极挑战：学生课程推荐系统")
    print("=" * 40)
    
    from collections import defaultdict
    
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
                
                # 检查先修要求
                if not course['prerequisites'].issubset(completed_and_enrolled):
                    continue
                
                # 计算兴趣匹配度
                interest_match = len(student_interests & course['topics'])
                if interest_match > 0:
                    # 计算推荐分数
                    score = interest_match / len(course['topics'])
                    
                    # 考虑课程热度
                    popularity = len(self.course_students[course_id])
                    score += popularity * 0.1
                    
                    recommendations.append((course_id, score, interest_match))
            
            # 按分数排序
            recommendations.sort(key=lambda x: x[1], reverse=True)
            return recommendations[:max_recommendations]
    
    # 创建推荐系统并添加数据
    system = CourseRecommendationSystem()
    
    # 添加学生
    system.add_student('alice', ['programming', 'data_science', 'math'], ['intro_cs'])
    system.add_student('bob', ['web_dev', 'programming', 'design'], ['intro_cs', 'html_css'])
    system.add_student('charlie', ['ai', 'math', 'data_science'], ['intro_cs', 'calculus'])
    
    # 添加课程
    courses_data = [
        ('python_basics', ['programming', 'python'], ['intro_cs'], 2),
        ('web_development', ['web_dev', 'programming', 'html'], ['intro_cs'], 2),
        ('machine_learning', ['ai', 'data_science', 'math'], ['python_basics', 'calculus'], 4),
        ('statistics', ['math', 'data_science'], ['calculus'], 3),
    ]
    
    for course_id, topics, prereqs, difficulty in courses_data:
        system.add_course(course_id, topics, prereqs, difficulty)
    
    print("课程推荐系统演示")
    print("-" * 30)
    
    # 为学生推荐课程
    print("课程推荐:")
    for student_id in ['alice', 'bob', 'charlie']:
        recommendations = system.recommend_courses(student_id)
        print(f"\n为{student_id}推荐:")
        for course_id, score, interest_match in recommendations:
            course = system.courses[course_id]
            print(f"  {course_id}: 分数{score:.2f}, 兴趣匹配{interest_match}, 主题{sorted(course['topics'])}")
```

## 运行代码

将代码保存为 `07_exercises.py` 文件，然后运行：

```bash
python3 07_exercises.py
```

## 学习要点

### 1. 集合基本操作
- 创建、添加、删除、查找
- 动态集合管理
- 成员检查的高效性

### 2. 集合数学运算
- 并集、交集、差集、对称差集
- 实际应用场景分析
- 权限管理系统设计

### 3. 集合推导式
- 高效数据过滤和转换
- 嵌套数据处理
- 复杂条件组合

### 4. frozenset应用
- 作为字典键使用
- 配置管理系统
- 图数据结构表示

### 5. 性能优化
- 集合vs列表的性能对比
- 大数据去重优化
- 查找操作优化

### 6. 实际应用
- 数据分析和挖掘
- 推荐系统设计
- 文本相似度计算
- 社交网络分析

## 最佳实践

### 1. 选择合适的数据结构
- 需要去重时使用集合
- 需要快速查找时使用集合
- 需要不可变集合时使用frozenset

### 2. 性能考虑
- 大数据处理优先考虑集合
- 避免在循环中重复创建集合
- 合理使用集合推导式

### 3. 代码可读性
- 使用有意义的变量名
- 适当添加注释说明
- 将复杂逻辑封装成函数

### 4. 错误处理
- 检查集合是否为空
- 处理不存在的元素
- 验证输入数据的有效性

通过这些综合练习，你将全面掌握Python集合的使用技巧，能够在实际项目中灵活运用集合解决各种问题。