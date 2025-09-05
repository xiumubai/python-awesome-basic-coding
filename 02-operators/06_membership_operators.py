#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
成员运算符和身份运算符学习教程

本文件演示Python中的成员运算符和身份运算符的使用方法和特性
包括：成员运算符(in, not in)和身份运算符(is, is not)

学习目标：
1. 掌握成员运算符的使用方法
2. 理解身份运算符与相等运算符的区别
3. 学会在不同数据结构中使用成员运算符
4. 了解对象身份和值的概念
"""

def main():
    print("="*50)
    print("Python 成员运算符和身份运算符学习教程")
    print("="*50)
    
    # 1. 成员运算符 (in, not in)
    print("\n1. 成员运算符 (in, not in)")
    print("-" * 30)
    
    # 在字符串中使用
    text = "Hello, Python!"
    print(f"字符串: '{text}'")
    print(f"'Python' in text: {'Python' in text}")
    print(f"'Java' in text: {'Java' in text}")
    print(f"'Python' not in text: {'Python' not in text}")
    print(f"'Java' not in text: {'Java' not in text}")
    
    # 在列表中使用
    print("\n在列表中使用成员运算符：")
    fruits = ['apple', 'banana', 'orange', 'grape']
    print(f"水果列表: {fruits}")
    print(f"'apple' in fruits: {'apple' in fruits}")
    print(f"'mango' in fruits: {'mango' in fruits}")
    print(f"'mango' not in fruits: {'mango' not in fruits}")
    
    # 在元组中使用
    print("\n在元组中使用成员运算符：")
    numbers = (1, 2, 3, 4, 5)
    print(f"数字元组: {numbers}")
    print(f"3 in numbers: {3 in numbers}")
    print(f"6 in numbers: {6 in numbers}")
    print(f"6 not in numbers: {6 not in numbers}")
    
    # 在集合中使用
    print("\n在集合中使用成员运算符：")
    colors = {'red', 'green', 'blue', 'yellow'}
    print(f"颜色集合: {colors}")
    print(f"'red' in colors: {'red' in colors}")
    print(f"'purple' in colors: {'purple' in colors}")
    print(f"'purple' not in colors: {'purple' not in colors}")
    
    # 在字典中使用（检查键）
    print("\n在字典中使用成员运算符（检查键）：")
    student = {'name': 'Alice', 'age': 20, 'grade': 'A'}
    print(f"学生信息: {student}")
    print(f"'name' in student: {'name' in student}")
    print(f"'score' in student: {'score' in student}")
    print(f"'score' not in student: {'score' not in student}")
    
    # 检查字典的值
    print("\n检查字典的值：")
    print(f"'Alice' in student.values(): {'Alice' in student.values()}")
    print(f"20 in student.values(): {20 in student.values()}")
    print(f"'B' in student.values(): {'B' in student.values()}")
    
    # 2. 成员运算符的性能比较
    print("\n2. 成员运算符的性能比较")
    print("-" * 30)
    
    import time
    
    # 创建测试数据
    large_list = list(range(10000))
    large_set = set(range(10000))
    large_dict = {i: f"value_{i}" for i in range(10000)}
    
    search_value = 9999
    iterations = 1000
    
    # 测试列表查找
    start = time.time()
    for _ in range(iterations):
        result = search_value in large_list
    list_time = time.time() - start
    
    # 测试集合查找
    start = time.time()
    for _ in range(iterations):
        result = search_value in large_set
    set_time = time.time() - start
    
    # 测试字典查找
    start = time.time()
    for _ in range(iterations):
        result = search_value in large_dict
    dict_time = time.time() - start
    
    print(f"查找元素 {search_value}（执行{iterations}次）：")
    print(f"列表查找耗时: {list_time:.6f} 秒")
    print(f"集合查找耗时: {set_time:.6f} 秒")
    print(f"字典查找耗时: {dict_time:.6f} 秒")
    
    if set_time > 0:
        print(f"集合比列表快约 {list_time/set_time:.1f} 倍")
    if dict_time > 0:
        print(f"字典比列表快约 {list_time/dict_time:.1f} 倍")
    
    # 3. 身份运算符 (is, is not)
    print("\n3. 身份运算符 (is, is not)")
    print("-" * 30)
    
    # 基本使用
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = a")
    print(f"a is b: {a is b} (不同的对象)")
    print(f"a is c: {a is c} (同一个对象)")
    print(f"a == b: {a == b} (值相等)")
    print(f"a == c: {a == c} (值相等)")
    
    print(f"\nid(a): {id(a)}")
    print(f"id(b): {id(b)}")
    print(f"id(c): {id(c)}")
    
    # 4. is 与 == 的区别
    print("\n4. is 与 == 的区别")
    print("-" * 30)
    
    # 小整数缓存
    print("小整数缓存（-5到256）：")
    x = 100
    y = 100
    print(f"x = 100, y = 100")
    print(f"x is y: {x is y} (小整数被缓存)")
    print(f"x == y: {x == y}")
    
    # 大整数
    print("\n大整数：")
    x = 1000
    y = 1000
    print(f"x = 1000, y = 1000")
    print(f"x is y: {x is y} (大整数不被缓存)")
    print(f"x == y: {x == y}")
    
    # 字符串
    print("\n字符串：")
    s1 = "hello"
    s2 = "hello"
    s3 = "hel" + "lo"
    print(f"s1 = 'hello'")
    print(f"s2 = 'hello'")
    print(f"s3 = 'hel' + 'lo'")
    print(f"s1 is s2: {s1 is s2} (字符串驻留)")
    print(f"s1 is s3: {s1 is s3} (编译时优化)")
    print(f"s1 == s2: {s1 == s2}")
    print(f"s1 == s3: {s1 == s3}")
    
    # 5. None 的特殊性
    print("\n5. None 的特殊性")
    print("-" * 30)
    
    value = None
    print(f"value = None")
    print(f"value is None: {value is None} (推荐用法)")
    print(f"value == None: {value == None} (不推荐)")
    print(f"value is not None: {value is not None}")
    print(f"value != None: {value != None}")
    
    # 为什么推荐使用 is None
    class CustomClass:
        def __eq__(self, other):
            return True  # 总是返回True
    
    obj = CustomClass()
    print(f"\n自定义类示例：")
    print(f"obj == None: {obj == None} (被重写的__eq__影响)")
    print(f"obj is None: {obj is None} (不受影响)")
    
    # 6. 实际应用示例
    print("\n6. 实际应用示例")
    print("-" * 30)
    
    # 应用1：检查用户输入
    def validate_user_input(data):
        required_fields = ['username', 'email', 'password']
        missing_fields = []
        
        for field in required_fields:
            if field not in data:
                missing_fields.append(field)
        
        return missing_fields
    
    print("用户输入验证：")
    user_data1 = {'username': 'alice', 'email': 'alice@example.com'}
    user_data2 = {'username': 'bob', 'email': 'bob@example.com', 'password': '123456'}
    
    missing1 = validate_user_input(user_data1)
    missing2 = validate_user_input(user_data2)
    
    print(f"用户数据1: {user_data1}")
    print(f"缺少字段: {missing1}")
    print(f"用户数据2: {user_data2}")
    print(f"缺少字段: {missing2}")
    
    # 应用2：权限检查
    def check_permissions(user_roles, required_roles):
        for role in required_roles:
            if role not in user_roles:
                return False
        return True
    
    print("\n权限检查：")
    admin_roles = ['read', 'write', 'delete', 'admin']
    user_roles = ['read', 'write']
    
    required_for_delete = ['delete']
    required_for_read = ['read']
    
    print(f"管理员角色: {admin_roles}")
    print(f"普通用户角色: {user_roles}")
    print(f"管理员可以删除: {check_permissions(admin_roles, required_for_delete)}")
    print(f"普通用户可以删除: {check_permissions(user_roles, required_for_delete)}")
    print(f"普通用户可以读取: {check_permissions(user_roles, required_for_read)}")
    
    # 应用3：缓存系统
    class SimpleCache:
        def __init__(self):
            self._cache = {}
        
        def get(self, key):
            if key in self._cache:
                print(f"缓存命中: {key}")
                return self._cache[key]
            else:
                print(f"缓存未命中: {key}")
                return None
        
        def set(self, key, value):
            self._cache[key] = value
            print(f"缓存设置: {key} = {value}")
        
        def has(self, key):
            return key in self._cache
        
        def remove(self, key):
            if key in self._cache:
                del self._cache[key]
                print(f"缓存删除: {key}")
                return True
            return False
    
    print("\n缓存系统示例：")
    cache = SimpleCache()
    cache.set('user:123', {'name': 'Alice', 'age': 25})
    cache.set('user:456', {'name': 'Bob', 'age': 30})
    
    print(f"缓存中有 user:123: {cache.has('user:123')}")
    print(f"缓存中有 user:789: {cache.has('user:789')}")
    
    user_data = cache.get('user:123')
    unknown_user = cache.get('user:789')
    
    # 应用4：单例模式检查
    class Singleton:
        _instance = None
        
        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance
    
    print("\n单例模式检查：")
    singleton1 = Singleton()
    singleton2 = Singleton()
    
    print(f"singleton1 is singleton2: {singleton1 is singleton2}")
    print(f"singleton1 == singleton2: {singleton1 == singleton2}")
    print(f"id(singleton1): {id(singleton1)}")
    print(f"id(singleton2): {id(singleton2)}")

def practice_exercises():
    """
    练习题部分
    """
    print("\n" + "="*50)
    print("练习题")
    print("="*50)
    
    print("\n请判断以下表达式的结果：")
    print("1. 'a' in 'apple'")
    print("2. 5 not in [1, 2, 3, 4]")
    print("3. 'key' in {'key': 'value'}")
    print("4. [] is []")
    print("5. None is None")
    print("6. 100 is 100")
    print("7. 1000 is 1000")
    
    print("\n答案：")
    print(f"1. 'a' in 'apple': {'a' in 'apple'}")
    print(f"2. 5 not in [1, 2, 3, 4]: {5 not in [1, 2, 3, 4]}")
    print(f"3. 'key' in {{'key': 'value'}}: {'key' in {'key': 'value'}}")
    print(f"4. [] is []: {[] is []}")
    print(f"5. None is None: {None is None}")
    print(f"6. 100 is 100: {100 is 100}")
    print(f"7. 1000 is 1000: {1000 is 1000}")
    
    print("\n编程练习：")
    print("1. 实现一个函数检查列表是否包含重复元素")
    print("2. 编写一个函数验证密码强度")
    print("3. 实现一个简单的购物车类")
    
    # 示例解答
    print("\n示例解答：")
    
    # 1. 检查重复元素
    def has_duplicates(lst):
        seen = set()
        for item in lst:
            if item in seen:
                return True
            seen.add(item)
        return False
    
    # 或者更简洁的方法
    def has_duplicates_simple(lst):
        return len(lst) != len(set(lst))
    
    print("1. 检查重复元素：")
    test_lists = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 2, 5],
        ['a', 'b', 'c'],
        ['a', 'b', 'a']
    ]
    
    for lst in test_lists:
        result1 = has_duplicates(lst)
        result2 = has_duplicates_simple(lst)
        print(f"   {lst}: {result1} (方法1), {result2} (方法2)")
    
    # 2. 密码强度验证
    def validate_password(password):
        if password is None:
            return False, "密码不能为空"
        
        issues = []
        
        if len(password) < 8:
            issues.append("长度至少8位")
        
        if not any(c.isupper() for c in password):
            issues.append("需要大写字母")
        
        if not any(c.islower() for c in password):
            issues.append("需要小写字母")
        
        if not any(c.isdigit() for c in password):
            issues.append("需要数字")
        
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if not any(c in special_chars for c in password):
            issues.append("需要特殊字符")
        
        if len(issues) == 0:
            return True, "密码强度良好"
        else:
            return False, "密码问题: " + ", ".join(issues)
    
    print("\n2. 密码强度验证：")
    test_passwords = [
        "123456",
        "Password",
        "Password123",
        "Password123!",
        None
    ]
    
    for pwd in test_passwords:
        is_valid, message = validate_password(pwd)
        print(f"   '{pwd}': {is_valid} - {message}")
    
    # 3. 购物车类
    class ShoppingCart:
        def __init__(self):
            self.items = {}
        
        def add_item(self, item, quantity=1, price=0.0):
            if item in self.items:
                self.items[item]['quantity'] += quantity
            else:
                self.items[item] = {'quantity': quantity, 'price': price}
        
        def remove_item(self, item):
            if item in self.items:
                del self.items[item]
                return True
            return False
        
        def has_item(self, item):
            return item in self.items
        
        def get_quantity(self, item):
            if item in self.items:
                return self.items[item]['quantity']
            return 0
        
        def get_total(self):
            total = 0
            for item_data in self.items.values():
                total += item_data['quantity'] * item_data['price']
            return total
        
        def is_empty(self):
            return len(self.items) == 0
        
        def __str__(self):
            if self.is_empty():
                return "购物车为空"
            
            result = "购物车内容:\n"
            for item, data in self.items.items():
                result += f"  {item}: {data['quantity']}个, 单价¥{data['price']:.2f}\n"
            result += f"总计: ¥{self.get_total():.2f}"
            return result
    
    print("\n3. 购物车示例：")
    cart = ShoppingCart()
    
    print(f"   购物车是否为空: {cart.is_empty()}")
    
    cart.add_item("苹果", 3, 5.0)
    cart.add_item("香蕉", 2, 3.0)
    cart.add_item("苹果", 1, 5.0)  # 增加数量
    
    print(f"   添加商品后:\n{cart}")
    print(f"   是否有苹果: {cart.has_item('苹果')}")
    print(f"   是否有橙子: {cart.has_item('橙子')}")
    print(f"   苹果数量: {cart.get_quantity('苹果')}")
    
    cart.remove_item("香蕉")
    print(f"   移除香蕉后:\n{cart}")

if __name__ == "__main__":
    main()
    practice_exercises()
    
    print("\n" + "="*50)
    print("学习小结")
    print("="*50)
    print("1. 成员运算符 in/not in 用于检查元素是否在容器中")
    print("2. 身份运算符 is/is not 用于检查对象身份（内存地址）")
    print("3. is 检查身份，== 检查值的相等性")
    print("4. 使用 is None 而不是 == None 来检查None值")
    print("5. 集合和字典的成员检查比列表更高效")
    print("6. 小整数和短字符串可能被Python缓存")
    print("7. 成员运算符常用于验证、权限检查等场景")