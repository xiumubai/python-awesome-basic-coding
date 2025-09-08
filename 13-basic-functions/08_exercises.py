#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
函数综合练习

本文件包含各种函数练习题目，涵盖：
1. 基础函数练习
2. 参数和返回值练习
3. 作用域练习
4. 高级函数练习
5. 实际应用练习

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("Python 函数综合练习")
print("=" * 50)

# 练习1：基础函数练习
print("\n练习1：基础函数练习")
print("-" * 30)

def exercise_1():
    """
    练习1：创建基本函数
    
    任务：
    1. 创建一个函数计算圆的面积
    2. 创建一个函数判断数字是否为偶数
    3. 创建一个函数返回两个数字中的较大值
    """
    print("练习1：基础函数练习")
    
    # 1. 计算圆的面积
    def calculate_circle_area(radius):
        """
        计算圆的面积。
        
        Args:
            radius (float): 圆的半径
            
        Returns:
            float: 圆的面积
        """
        import math
        return math.pi * radius ** 2
    
    # 2. 判断是否为偶数
    def is_even(number):
        """
        判断数字是否为偶数。
        
        Args:
            number (int): 要判断的数字
            
        Returns:
            bool: 如果是偶数返回True，否则返回False
        """
        return number % 2 == 0
    
    # 3. 返回较大值
    def get_max(a, b):
        """
        返回两个数字中的较大值。
        
        Args:
            a (float): 第一个数字
            b (float): 第二个数字
            
        Returns:
            float: 较大的数字
        """
        return a if a > b else b
    
    # 测试函数
    print(f"半径为5的圆面积：{calculate_circle_area(5):.2f}")
    print(f"8是偶数吗？{is_even(8)}")
    print(f"7是偶数吗？{is_even(7)}")
    print(f"10和15中较大的是：{get_max(10, 15)}")
    
    return calculate_circle_area, is_even, get_max

exercise_1()
print()

# 练习2：参数和返回值练习
print("\n练习2：参数和返回值练习")
print("-" * 30)

def exercise_2():
    """
    练习2：复杂参数和返回值
    
    任务：
    1. 创建一个函数，接受可变数量的数字参数，返回它们的统计信息
    2. 创建一个函数，使用关键字参数创建用户信息
    3. 创建一个函数，返回多个值
    """
    print("练习2：参数和返回值练习")
    
    # 1. 数字统计函数
    def number_statistics(*numbers, **options):
        """
        计算数字的统计信息。
        
        Args:
            *numbers: 可变数量的数字
            **options: 选项参数
                - include_median (bool): 是否包含中位数
                - round_digits (int): 保留小数位数
                
        Returns:
            dict: 包含统计信息的字典
        """
        if not numbers:
            return {"error": "没有提供数字"}
        
        # 基本统计
        stats = {
            "count": len(numbers),
            "sum": sum(numbers),
            "average": sum(numbers) / len(numbers),
            "min": min(numbers),
            "max": max(numbers)
        }
        
        # 可选的中位数
        if options.get("include_median", False):
            sorted_numbers = sorted(numbers)
            n = len(sorted_numbers)
            if n % 2 == 0:
                median = (sorted_numbers[n//2-1] + sorted_numbers[n//2]) / 2
            else:
                median = sorted_numbers[n//2]
            stats["median"] = median
        
        # 四舍五入
        round_digits = options.get("round_digits")
        if round_digits is not None:
            for key in ["sum", "average", "median"]:
                if key in stats:
                    stats[key] = round(stats[key], round_digits)
        
        return stats
    
    # 2. 用户信息创建函数
    def create_user_info(name, age, email=None, phone=None, **additional_info):
        """
        创建用户信息字典。
        
        Args:
            name (str): 用户姓名
            age (int): 用户年龄
            email (str, optional): 电子邮件
            phone (str, optional): 电话号码
            **additional_info: 额外信息
            
        Returns:
            dict: 用户信息字典
        """
        user_info = {
            "name": name,
            "age": age,
            "contact": {}
        }
        
        # 添加联系信息
        if email:
            user_info["contact"]["email"] = email
        if phone:
            user_info["contact"]["phone"] = phone
        
        # 添加额外信息
        if additional_info:
            user_info["additional"] = additional_info
        
        return user_info
    
    # 3. 多返回值函数
    def analyze_text(text):
        """
        分析文本并返回多个统计信息。
        
        Args:
            text (str): 要分析的文本
            
        Returns:
            tuple: (字符数, 单词数, 行数, 最长单词)
        """
        if not text:
            return 0, 0, 0, ""
        
        char_count = len(text)
        line_count = text.count('\n') + 1
        words = text.split()
        word_count = len(words)
        longest_word = max(words, key=len) if words else ""
        
        return char_count, word_count, line_count, longest_word
    
    # 测试函数
    print("数字统计测试：")
    stats1 = number_statistics(1, 2, 3, 4, 5, include_median=True, round_digits=2)
    print(f"统计结果：{stats1}")
    
    print("\n用户信息创建测试：")
    user1 = create_user_info("张三", 25, email="zhangsan@example.com", 
                           city="北京", occupation="工程师")
    print(f"用户信息：{user1}")
    
    print("\n文本分析测试：")
    sample_text = "Hello world!\nThis is a sample text.\nPython is awesome!"
    char_count, word_count, line_count, longest_word = analyze_text(sample_text)
    print(f"字符数：{char_count}, 单词数：{word_count}, 行数：{line_count}, 最长单词：{longest_word}")
    
    return number_statistics, create_user_info, analyze_text

exercise_2()
print()

# 练习3：作用域练习
print("\n练习3：作用域练习")
print("-" * 30)

# 全局变量（在函数外部定义）
global_counter = 0
global_config = {"debug": False, "version": "1.0"}

def exercise_3():
    """
    练习3：变量作用域
    
    任务：
    1. 演示全局变量和局部变量的区别
    2. 使用global关键字修改全局变量
    3. 创建嵌套函数并使用nonlocal
    """
    print("练习3：作用域练习")
    
    # 1. 全局变量和局部变量
    def demonstrate_scope():
        """
        演示变量作用域。
        """
        # 局部变量（遮蔽全局变量）
        global_counter = 100  # 这是局部变量
        local_var = "我是局部变量"
        
        print(f"函数内的global_counter：{global_counter}")
        print(f"局部变量：{local_var}")
        
        # 访问全局变量
        print(f"全局配置：{global_config}")
    
    # 2. 使用global修改全局变量
    def modify_global_counter(increment=1):
        """
        修改全局计数器。
        
        Args:
            increment (int): 增量值
        """
        global global_counter
        global_counter += increment
        print(f"全局计数器增加{increment}，当前值：{global_counter}")
    
    def reset_global_counter():
        """
        重置全局计数器。
        """
        global global_counter
        global_counter = 0
        print("全局计数器已重置")
    
    # 3. 嵌套函数和nonlocal
    def create_counter(initial_value=0):
        """
        创建一个计数器函数。
        
        Args:
            initial_value (int): 初始值
            
        Returns:
            tuple: (increment函数, get_value函数, reset函数)
        """
        count = initial_value
        
        def increment(step=1):
            """
            增加计数器。
            
            Args:
                step (int): 步长
            """
            nonlocal count
            count += step
            return count
        
        def get_value():
            """
            获取当前值。
            
            Returns:
                int: 当前计数值
            """
            return count
        
        def reset(new_value=0):
            """
            重置计数器。
            
            Args:
                new_value (int): 新的值
            """
            nonlocal count
            count = new_value
            return count
        
        return increment, get_value, reset
    
    # 测试作用域
    print(f"初始全局计数器：{global_counter}")
    
    demonstrate_scope()
    print(f"函数调用后全局计数器：{global_counter}")
    
    modify_global_counter(5)
    modify_global_counter(3)
    
    print("\n嵌套函数测试：")
    inc, get_val, reset = create_counter(10)
    print(f"初始值：{get_val()}")
    print(f"增加5：{inc(5)}")
    print(f"增加2：{inc(2)}")
    print(f"当前值：{get_val()}")
    print(f"重置为0：{reset()}")
    
    reset_global_counter()
    
    return demonstrate_scope, modify_global_counter, create_counter

exercise_3()
print()

# 练习4：高级函数练习
print("\n练习4：高级函数练习")
print("-" * 30)

def exercise_4():
    """
    练习4：高级函数特性
    
    任务：
    1. 创建装饰器函数
    2. 实现函数作为参数和返回值
    3. 创建递归函数
    """
    print("练习4：高级函数练习")
    
    # 1. 简单装饰器
    def timer_decorator(func):
        """
        计时装饰器。
        
        Args:
            func: 要装饰的函数
            
        Returns:
            function: 装饰后的函数
        """
        import time
        
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"函数 {func.__name__} 执行时间：{end_time - start_time:.4f}秒")
            return result
        
        return wrapper
    
    def log_decorator(func):
        """
        日志装饰器。
        
        Args:
            func: 要装饰的函数
            
        Returns:
            function: 装饰后的函数
        """
        def wrapper(*args, **kwargs):
            print(f"调用函数：{func.__name__}，参数：args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"函数 {func.__name__} 返回：{result}")
            return result
        
        return wrapper
    
    # 2. 高阶函数（函数作为参数）
    def apply_operation(numbers, operation):
        """
        对数字列表应用操作。
        
        Args:
            numbers (list): 数字列表
            operation (function): 操作函数
            
        Returns:
            list: 操作后的结果列表
        """
        return [operation(num) for num in numbers]
    
    def create_multiplier(factor):
        """
        创建乘法函数。
        
        Args:
            factor (float): 乘数
            
        Returns:
            function: 乘法函数
        """
        def multiplier(x):
            return x * factor
        return multiplier
    
    def compose_functions(func1, func2):
        """
        组合两个函数。
        
        Args:
            func1: 第一个函数
            func2: 第二个函数
            
        Returns:
            function: 组合后的函数 func1(func2(x))
        """
        def composed(x):
            return func1(func2(x))
        return composed
    
    # 3. 递归函数
    def factorial(n):
        """
        计算阶乘（递归实现）。
        
        Args:
            n (int): 非负整数
            
        Returns:
            int: n的阶乘
            
        Raises:
            ValueError: 当n为负数时
        """
        if n < 0:
            raise ValueError("阶乘不能计算负数")
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    
    def fibonacci(n):
        """
        计算斐波那契数列第n项（递归实现）。
        
        Args:
            n (int): 项数（从0开始）
            
        Returns:
            int: 第n项的值
        """
        if n < 0:
            raise ValueError("项数不能为负")
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    def binary_search(arr, target, left=0, right=None):
        """
        二分查找（递归实现）。
        
        Args:
            arr (list): 已排序的数组
            target: 目标值
            left (int): 左边界
            right (int): 右边界
            
        Returns:
            int: 目标值的索引，如果不存在返回-1
        """
        if right is None:
            right = len(arr) - 1
        
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, left, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, right)
    
    # 使用装饰器
    @timer_decorator
    @log_decorator
    def slow_function(n):
        """
        模拟慢函数。
        
        Args:
            n (int): 参数
            
        Returns:
            int: 结果
        """
        import time
        time.sleep(0.1)  # 模拟耗时操作
        return n * n
    
    # 测试高级函数
    print("装饰器测试：")
    result = slow_function(5)
    
    print("\n高阶函数测试：")
    numbers = [1, 2, 3, 4, 5]
    
    # 创建不同的操作函数
    square = lambda x: x ** 2
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"原始数字：{numbers}")
    print(f"平方：{apply_operation(numbers, square)}")
    print(f"乘以2：{apply_operation(numbers, double)}")
    print(f"乘以3：{apply_operation(numbers, triple)}")
    
    # 函数组合
    square_then_double = compose_functions(double, square)
    print(f"先平方再乘以2：{apply_operation(numbers, square_then_double)}")
    
    print("\n递归函数测试：")
    print(f"5的阶乘：{factorial(5)}")
    print(f"斐波那契数列前10项：{[fibonacci(i) for i in range(10)]}")
    
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    index = binary_search(sorted_array, target)
    print(f"在{sorted_array}中查找{target}，索引：{index}")
    
    return apply_operation, create_multiplier, factorial, fibonacci, binary_search

exercise_4()
print()

# 练习5：实际应用练习
print("\n练习5：实际应用练习")
print("-" * 30)

def exercise_5():
    """
    练习5：实际应用场景
    
    任务：
    1. 创建数据处理函数
    2. 实现简单的缓存系统
    3. 创建配置管理函数
    """
    print("练习5：实际应用练习")
    
    # 1. 数据处理函数
    def process_student_data(students_data, **filters):
        """
        处理学生数据。
        
        Args:
            students_data (list): 学生数据列表
            **filters: 过滤条件
                - min_age (int): 最小年龄
                - max_age (int): 最大年龄
                - min_score (float): 最低分数
                - subject (str): 科目过滤
                
        Returns:
            dict: 处理后的数据统计
        """
        filtered_students = students_data.copy()
        
        # 应用过滤条件
        if 'min_age' in filters:
            filtered_students = [s for s in filtered_students if s.get('age', 0) >= filters['min_age']]
        
        if 'max_age' in filters:
            filtered_students = [s for s in filtered_students if s.get('age', 0) <= filters['max_age']]
        
        if 'min_score' in filters:
            filtered_students = [s for s in filtered_students 
                               if s.get('score', 0) >= filters['min_score']]
        
        if 'subject' in filters:
            filtered_students = [s for s in filtered_students 
                               if s.get('subject') == filters['subject']]
        
        # 计算统计信息
        if not filtered_students:
            return {"count": 0, "average_score": 0, "average_age": 0}
        
        total_score = sum(s.get('score', 0) for s in filtered_students)
        total_age = sum(s.get('age', 0) for s in filtered_students)
        count = len(filtered_students)
        
        return {
            "count": count,
            "average_score": total_score / count,
            "average_age": total_age / count,
            "students": filtered_students
        }
    
    # 2. 简单缓存系统
    def create_cache_system(max_size=100):
        """
        创建简单的缓存系统。
        
        Args:
            max_size (int): 缓存最大大小
            
        Returns:
            tuple: (get函数, set函数, clear函数, stats函数)
        """
        cache = {}
        access_count = {}
        
        def get(key, default=None):
            """
            获取缓存值。
            
            Args:
                key: 缓存键
                default: 默认值
                
            Returns:
                缓存的值或默认值
            """
            if key in cache:
                access_count[key] = access_count.get(key, 0) + 1
                return cache[key]
            return default
        
        def set(key, value):
            """
            设置缓存值。
            
            Args:
                key: 缓存键
                value: 缓存值
            """
            # 如果缓存已满，删除最少使用的项
            if len(cache) >= max_size and key not in cache:
                if access_count:
                    least_used_key = min(access_count.keys(), key=lambda k: access_count[k])
                    del cache[least_used_key]
                    del access_count[least_used_key]
                elif cache:
                    # 如果没有访问记录，删除第一个
                    first_key = next(iter(cache))
                    del cache[first_key]
            
            cache[key] = value
            access_count[key] = access_count.get(key, 0) + 1
        
        def clear():
            """
            清空缓存。
            """
            cache.clear()
            access_count.clear()
        
        def stats():
            """
            获取缓存统计信息。
            
            Returns:
                dict: 统计信息
            """
            return {
                "size": len(cache),
                "max_size": max_size,
                "keys": list(cache.keys()),
                "access_count": access_count.copy()
            }
        
        return get, set, clear, stats
    
    # 3. 配置管理函数
    def create_config_manager(default_config=None):
        """
        创建配置管理器。
        
        Args:
            default_config (dict): 默认配置
            
        Returns:
            tuple: (get函数, set函数, update函数, reset函数)
        """
        config = default_config.copy() if default_config else {}
        
        def get(key, default=None):
            """
            获取配置值。
            
            Args:
                key (str): 配置键，支持点号分隔的嵌套键
                default: 默认值
                
            Returns:
                配置值或默认值
            """
            keys = key.split('.')
            value = config
            
            try:
                for k in keys:
                    value = value[k]
                return value
            except (KeyError, TypeError):
                return default
        
        def set(key, value):
            """
            设置配置值。
            
            Args:
                key (str): 配置键，支持点号分隔的嵌套键
                value: 配置值
            """
            keys = key.split('.')
            current = config
            
            # 创建嵌套字典结构
            for k in keys[:-1]:
                if k not in current or not isinstance(current[k], dict):
                    current[k] = {}
                current = current[k]
            
            current[keys[-1]] = value
        
        def update(new_config):
            """
            更新配置。
            
            Args:
                new_config (dict): 新的配置字典
            """
            def deep_update(target, source):
                for key, value in source.items():
                    if key in target and isinstance(target[key], dict) and isinstance(value, dict):
                        deep_update(target[key], value)
                    else:
                        target[key] = value
            
            deep_update(config, new_config)
        
        def reset():
            """
            重置为默认配置。
            """
            config.clear()
            if default_config:
                config.update(default_config)
        
        def get_all():
            """
            获取所有配置。
            
            Returns:
                dict: 配置字典的副本
            """
            import copy
            return copy.deepcopy(config)
        
        return get, set, update, reset, get_all
    
    # 测试实际应用
    print("数据处理测试：")
    students = [
        {"name": "张三", "age": 20, "score": 85, "subject": "数学"},
        {"name": "李四", "age": 19, "score": 92, "subject": "物理"},
        {"name": "王五", "age": 21, "score": 78, "subject": "数学"},
        {"name": "赵六", "age": 20, "score": 88, "subject": "物理"},
        {"name": "钱七", "age": 22, "score": 95, "subject": "数学"}
    ]
    
    # 处理所有学生
    all_stats = process_student_data(students)
    print(f"所有学生统计：{all_stats['count']}人，平均分：{all_stats['average_score']:.1f}")
    
    # 过滤数学科目且分数>=85的学生
    math_high_score = process_student_data(students, subject="数学", min_score=85)
    print(f"数学高分学生：{math_high_score['count']}人，平均分：{math_high_score['average_score']:.1f}")
    
    print("\n缓存系统测试：")
    cache_get, cache_set, cache_clear, cache_stats = create_cache_system(3)
    
    # 设置缓存
    cache_set("user1", {"name": "张三", "age": 25})
    cache_set("user2", {"name": "李四", "age": 30})
    cache_set("user3", {"name": "王五", "age": 28})
    
    print(f"缓存统计：{cache_stats()}")
    
    # 访问缓存
    user1 = cache_get("user1")
    user1_again = cache_get("user1")  # 增加访问次数
    print(f"获取user1：{user1}")
    
    # 添加新项（应该删除最少使用的）
    cache_set("user4", {"name": "赵六", "age": 35})
    print(f"添加user4后的统计：{cache_stats()}")
    
    print("\n配置管理测试：")
    default_cfg = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "mydb"
        },
        "logging": {
            "level": "INFO",
            "file": "app.log"
        }
    }
    
    cfg_get, cfg_set, cfg_update, cfg_reset, cfg_get_all = create_config_manager(default_cfg)
    
    print(f"数据库主机：{cfg_get('database.host')}")
    print(f"日志级别：{cfg_get('logging.level')}")
    
    # 更新配置
    cfg_set("database.port", 3306)
    cfg_set("app.version", "1.0.0")
    
    print(f"更新后的端口：{cfg_get('database.port')}")
    print(f"应用版本：{cfg_get('app.version')}")
    
    # 批量更新
    cfg_update({
        "database": {"host": "remote-server"},
        "cache": {"enabled": True, "ttl": 3600}
    })
    
    print(f"最终配置：{cfg_get_all()}")
    
    return process_student_data, create_cache_system, create_config_manager

exercise_5()
print()

# 综合挑战练习
print("\n综合挑战练习")
print("-" * 30)

def challenge_exercise():
    """
    综合挑战：创建一个简单的任务调度系统
    
    要求：
    1. 支持任务的添加、执行、取消
    2. 支持任务优先级
    3. 支持任务状态跟踪
    4. 使用函数式编程思想
    """
    print("综合挑战：任务调度系统")
    
    def create_task_scheduler():
        """
        创建任务调度器。
        
        Returns:
            dict: 包含调度器操作函数的字典
        """
        tasks = {}
        task_counter = 0
        
        def add_task(name, func, priority=1, *args, **kwargs):
            """
            添加任务。
            
            Args:
                name (str): 任务名称
                func (callable): 任务函数
                priority (int): 优先级（数字越大优先级越高）
                *args: 任务函数参数
                **kwargs: 任务函数关键字参数
                
            Returns:
                int: 任务ID
            """
            nonlocal task_counter
            task_counter += 1
            
            task_id = task_counter
            tasks[task_id] = {
                "id": task_id,
                "name": name,
                "func": func,
                "args": args,
                "kwargs": kwargs,
                "priority": priority,
                "status": "pending",
                "result": None,
                "error": None,
                "created_at": "2024-01-01 00:00:00"  # 模拟时间戳
            }
            
            print(f"任务 '{name}' (ID: {task_id}) 已添加")
            return task_id
        
        def execute_task(task_id):
            """
            执行指定任务。
            
            Args:
                task_id (int): 任务ID
                
            Returns:
                bool: 执行是否成功
            """
            if task_id not in tasks:
                print(f"任务 ID {task_id} 不存在")
                return False
            
            task = tasks[task_id]
            if task["status"] != "pending":
                print(f"任务 '{task['name']}' 状态为 {task['status']}，无法执行")
                return False
            
            try:
                task["status"] = "running"
                print(f"开始执行任务 '{task['name']}'...")
                
                result = task["func"](*task["args"], **task["kwargs"])
                
                task["status"] = "completed"
                task["result"] = result
                print(f"任务 '{task['name']}' 执行完成，结果：{result}")
                return True
                
            except Exception as e:
                task["status"] = "failed"
                task["error"] = str(e)
                print(f"任务 '{task['name']}' 执行失败：{e}")
                return False
        
        def execute_all_tasks():
            """
            按优先级执行所有待执行任务。
            
            Returns:
                dict: 执行结果统计
            """
            pending_tasks = [(tid, task) for tid, task in tasks.items() 
                           if task["status"] == "pending"]
            
            # 按优先级排序（优先级高的先执行）
            pending_tasks.sort(key=lambda x: x[1]["priority"], reverse=True)
            
            results = {"completed": 0, "failed": 0}
            
            for task_id, task in pending_tasks:
                if execute_task(task_id):
                    results["completed"] += 1
                else:
                    results["failed"] += 1
            
            return results
        
        def cancel_task(task_id):
            """
            取消任务。
            
            Args:
                task_id (int): 任务ID
                
            Returns:
                bool: 取消是否成功
            """
            if task_id not in tasks:
                print(f"任务 ID {task_id} 不存在")
                return False
            
            task = tasks[task_id]
            if task["status"] in ["completed", "failed"]:
                print(f"任务 '{task['name']}' 已完成，无法取消")
                return False
            
            task["status"] = "cancelled"
            print(f"任务 '{task['name']}' 已取消")
            return True
        
        def get_task_status(task_id=None):
            """
            获取任务状态。
            
            Args:
                task_id (int, optional): 任务ID，如果为None则返回所有任务
                
            Returns:
                dict or list: 任务状态信息
            """
            if task_id is not None:
                return tasks.get(task_id, {"error": "任务不存在"})
            
            return list(tasks.values())
        
        def clear_completed_tasks():
            """
            清除已完成的任务。
            
            Returns:
                int: 清除的任务数量
            """
            completed_ids = [tid for tid, task in tasks.items() 
                           if task["status"] in ["completed", "failed", "cancelled"]]
            
            for tid in completed_ids:
                del tasks[tid]
            
            print(f"已清除 {len(completed_ids)} 个已完成的任务")
            return len(completed_ids)
        
        return {
            "add_task": add_task,
            "execute_task": execute_task,
            "execute_all_tasks": execute_all_tasks,
            "cancel_task": cancel_task,
            "get_task_status": get_task_status,
            "clear_completed_tasks": clear_completed_tasks
        }
    
    # 创建调度器
    scheduler = create_task_scheduler()
    
    # 定义一些示例任务函数
    def calculate_sum(a, b):
        """计算两数之和。"""
        import time
        time.sleep(0.1)  # 模拟耗时操作
        return a + b
    
    def process_data(data, multiplier=1):
        """处理数据。"""
        if not data:
            raise ValueError("数据不能为空")
        return [x * multiplier for x in data]
    
    def generate_report(title, items):
        """生成报告。"""
        report = f"报告：{title}\n"
        report += "=" * 20 + "\n"
        for i, item in enumerate(items, 1):
            report += f"{i}. {item}\n"
        return report
    
    # 测试任务调度器
    print("\n添加任务：")
    task1 = scheduler["add_task"]("计算1+2", calculate_sum, 2, 1, 2)
    task2 = scheduler["add_task"]("处理数据", process_data, 3, [1, 2, 3, 4], multiplier=2)
    task3 = scheduler["add_task"]("生成报告", generate_report, 1, "月度总结", ["完成项目A", "优化系统B", "培训新员工"])
    task4 = scheduler["add_task"]("错误任务", process_data, 1, None)  # 这个会失败
    
    print("\n查看所有任务状态：")
    all_tasks = scheduler["get_task_status"]()
    for task in all_tasks:
        print(f"任务 {task['id']}: {task['name']} - {task['status']} (优先级: {task['priority']})")
    
    print("\n执行所有任务：")
    results = scheduler["execute_all_tasks"]()
    print(f"执行结果：完成 {results['completed']} 个，失败 {results['failed']} 个")
    
    print("\n查看执行后的任务状态：")
    all_tasks = scheduler["get_task_status"]()
    for task in all_tasks:
        status_info = f"任务 {task['id']}: {task['name']} - {task['status']}"
        if task['result'] is not None:
            status_info += f" (结果: {task['result']})"
        if task['error']:
            status_info += f" (错误: {task['error']})"
        print(status_info)
    
    print("\n清除已完成的任务：")
    cleared_count = scheduler["clear_completed_tasks"]()
    
    return scheduler

challenge_exercise()
print()

print("=" * 50)
print("函数综合练习完成！")
print("=" * 50)
print("\n练习总结：")
print("1. 基础函数：定义、调用、参数、返回值")
print("2. 高级参数：*args、**kwargs、默认参数")
print("3. 变量作用域：全局、局部、global、nonlocal")
print("4. 高级特性：装饰器、高阶函数、递归")
print("5. 实际应用：数据处理、缓存、配置管理")
print("6. 综合项目：任务调度系统")
print("\n通过这些练习，你应该掌握了：")
print("- 函数的各种定义和使用方式")
print("- 参数传递的不同方法")
print("- 变量作用域的概念和应用")
print("- 函数式编程的基本思想")
print("- 实际项目中函数的设计模式")