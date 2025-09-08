# 函数综合练习

## 学习目标

通过本节练习，你将综合运用所学的函数知识：
- 巩固函数基础语法和概念
- 练习复杂参数和返回值处理
- 深入理解变量作用域
- 掌握高级函数特性（装饰器、递归、高阶函数）
- 应用函数解决实际问题
- 完成综合项目挑战

## 练习1：基础函数练习

创建基本函数，掌握函数定义、调用和基本功能。

```python
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
```

## 练习2：参数和返回值练习

练习复杂的参数处理和多返回值函数。

```python
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
```

## 练习3：作用域练习

深入理解变量作用域，练习global和nonlocal的使用。

```python
def exercise_3():
    """
    练习3：变量作用域
    
    任务：
    1. 演示全局变量和局部变量的区别
    2. 使用global关键字修改全局变量
    3. 创建嵌套函数并使用nonlocal
    """
    print("练习3：作用域练习")
    
    # 全局变量
    global_counter = 0
    global_config = {"debug": False, "version": "1.0"}
    
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
    
    return demonstrate_scope, modify_global_counter, create_counter

exercise_3()
```

## 练习4：高级函数练习

练习装饰器、高阶函数和递归等高级特性。

```python
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
    
    print("\n递归函数测试：")
    print(f"5的阶乘：{factorial(5)}")
    print(f"斐波那契数列前10项：{[fibonacci(i) for i in range(10)]}")
    
    return apply_operation, create_multiplier, factorial, fibonacci

exercise_4()
```

## 练习5：实际应用练习

将函数应用到实际场景中，解决具体问题。

```python
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
    
    return process_student_data, create_cache_system

exercise_5()
```

## 综合挑战练习：任务调度系统

创建一个完整的任务调度系统，综合运用所有函数知识。

```python
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
        
        return {
            "add_task": add_task,
            "execute_task": execute_task,
            "execute_all_tasks": execute_all_tasks,
            "get_task_status": get_task_status
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
    
    return scheduler

challenge_exercise()
```

## 运行示例

```bash
# 运行函数综合练习
python3 08_exercises.py
```

## 练习总结

通过这些综合练习，你应该掌握了：

### 1. 基础函数技能
- 函数定义和调用
- 参数传递和返回值处理
- 函数文档编写

### 2. 高级函数特性
- 可变参数（*args, **kwargs）
- 默认参数和关键字参数
- 变量作用域（global, nonlocal）
- 装饰器的使用
- 递归函数实现
- 高阶函数概念

### 3. 实际应用能力
- 数据处理和过滤
- 缓存系统设计
- 配置管理实现
- 任务调度系统开发

### 4. 函数式编程思想
- 函数作为一等公民
- 闭包的使用
- 函数组合
- 纯函数概念

## 最佳实践建议

1. **函数设计原则**：
   - 单一职责：每个函数只做一件事
   - 参数合理：避免过多参数
   - 返回值明确：返回值类型和含义清晰

2. **代码组织**：
   - 相关函数分组
   - 使用模块化设计
   - 合理使用装饰器

3. **错误处理**：
   - 适当的异常处理
   - 参数验证
   - 边界条件检查

4. **性能考虑**：
   - 避免不必要的递归
   - 合理使用缓存
   - 优化算法复杂度

## 进阶练习建议

1. **扩展任务调度系统**：
   - 添加任务依赖关系
   - 实现任务重试机制
   - 添加任务执行时间限制

2. **创建更复杂的装饰器**：
   - 带参数的装饰器
   - 类装饰器
   - 装饰器链

3. **实现函数式编程工具**：
   - map、filter、reduce的自定义实现
   - 函数组合工具
   - 柯里化函数

4. **性能优化练习**：
   - 使用生成器优化内存使用
   - 实现LRU缓存
   - 并发函数执行