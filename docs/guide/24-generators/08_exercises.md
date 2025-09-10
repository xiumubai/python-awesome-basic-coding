# 生成器综合练习

本章提供了一系列综合练习，帮助你巩固和深化对生成器的理解。这些练习涵盖了从基础概念到高级应用的各个方面，通过实际编程来掌握生成器的强大功能。

## 基础练习

### 练习1：基础生成器实现

**目标**：实现各种基础生成器，理解yield的工作原理。

```python
def basic_generator_exercises():
    """基础生成器练习"""
    print("=== 基础生成器练习 ===")
    
    # 练习1.1：数字序列生成器
    def number_sequence(start, end, step=1):
        """生成数字序列"""
        current = start
        while current < end:
            yield current
            current += step
    
    print("\n1.1 数字序列生成器:")
    seq = number_sequence(1, 10, 2)
    print(f"奇数序列: {list(seq)}")
    
    # 练习1.2：字符串处理生成器
    def word_generator(text):
        """逐词生成器"""
        words = text.split()
        for word in words:
            yield word.lower().strip('.,!?')
    
    print("\n1.2 字符串处理生成器:")
    text = "Hello, World! How are you today?"
    words = word_generator(text)
    print(f"处理后的单词: {list(words)}")
    
    # 练习1.3：条件生成器
    def conditional_generator(data, condition):
        """条件过滤生成器"""
        for item in data:
            if condition(item):
                yield item
    
    print("\n1.3 条件生成器:")
    numbers = range(1, 21)
    even_numbers = conditional_generator(numbers, lambda x: x % 2 == 0)
    print(f"偶数: {list(even_numbers)}")
    
    # 练习1.4：累积生成器
    def accumulator_generator(data, operation):
        """累积计算生成器"""
        accumulator = 0
        for item in data:
            accumulator = operation(accumulator, item)
            yield accumulator
    
    print("\n1.4 累积生成器:")
    numbers = [1, 2, 3, 4, 5]
    cumulative_sum = accumulator_generator(numbers, lambda acc, x: acc + x)
    print(f"累积和: {list(cumulative_sum)}")
    
    cumulative_product = accumulator_generator(numbers, lambda acc, x: acc * x if acc != 0 else x)
    print(f"累积积: {list(cumulative_product)}")

basic_generator_exercises()
```

### 练习2：生成器表达式应用

**目标**：熟练使用生成器表达式解决实际问题。

```python
def generator_expression_exercises():
    """生成器表达式练习"""
    print("\n=== 生成器表达式练习 ===")
    
    # 练习2.1：数据转换
    print("\n2.1 数据转换:")
    
    # 温度转换（摄氏度到华氏度）
    celsius_temps = [0, 10, 20, 30, 40]
    fahrenheit_temps = (c * 9/5 + 32 for c in celsius_temps)
    print(f"摄氏度: {celsius_temps}")
    print(f"华氏度: {list(fahrenheit_temps)}")
    
    # 练习2.2：嵌套数据处理
    print("\n2.2 嵌套数据处理:")
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # 展平矩阵
    flattened = (item for row in matrix for item in row)
    print(f"原矩阵: {matrix}")
    print(f"展平后: {list(flattened)}")
    
    # 对角线元素
    diagonal = (matrix[i][i] for i in range(len(matrix)))
    print(f"对角线: {list(diagonal)}")
    
    # 练习2.3：条件筛选和转换
    print("\n2.3 条件筛选和转换:")
    
    students = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 92},
        {'name': 'Charlie', 'score': 78},
        {'name': 'Diana', 'score': 96}
    ]
    
    # 优秀学生（分数>=90）的姓名
    excellent_students = (s['name'] for s in students if s['score'] >= 90)
    print(f"优秀学生: {list(excellent_students)}")
    
    # 所有学生的等级
    def get_grade(score):
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        else: return 'D'
    
    student_grades = ((s['name'], get_grade(s['score'])) for s in students)
    print(f"学生等级: {list(student_grades)}")
    
    # 练习2.4：文件路径处理
    print("\n2.4 文件路径处理:")
    
    file_paths = [
        '/home/user/document.txt',
        '/home/user/image.jpg',
        '/home/user/script.py',
        '/home/user/data.csv'
    ]
    
    # 提取文件名
    filenames = (path.split('/')[-1] for path in file_paths)
    print(f"文件名: {list(filenames)}")
    
    # 提取文件扩展名
    extensions = (path.split('.')[-1] for path in file_paths if '.' in path)
    print(f"扩展名: {list(extensions)}")
    
    # Python文件路径
    python_files = (path for path in file_paths if path.endswith('.py'))
    print(f"Python文件: {list(python_files)}")

generator_expression_exercises()
```

## 进阶练习

### 练习3：生成器方法应用

**目标**：掌握send()、throw()、close()方法的使用。

```python
def generator_methods_exercises():
    """生成器方法练习"""
    print("\n=== 生成器方法练习 ===")
    
    # 练习3.1：双向通信计算器
    def calculator_generator():
        """支持双向通信的计算器"""
        result = 0
        operation = yield result  # 初始值
        
        while True:
            try:
                if operation is None:
                    operation = yield result
                    continue
                
                op_type, value = operation
                
                if op_type == 'add':
                    result += value
                elif op_type == 'subtract':
                    result -= value
                elif op_type == 'multiply':
                    result *= value
                elif op_type == 'divide':
                    if value != 0:
                        result /= value
                    else:
                        raise ValueError("除零错误")
                elif op_type == 'reset':
                    result = 0
                else:
                    raise ValueError(f"未知操作: {op_type}")
                
                operation = yield result
                
            except Exception as e:
                print(f"    计算器错误: {e}")
                operation = yield result
    
    print("\n3.1 双向通信计算器:")
    calc = calculator_generator()
    
    # 启动生成器
    current_result = next(calc)
    print(f"初始值: {current_result}")
    
    # 执行计算
    operations = [
        ('add', 10),
        ('multiply', 3),
        ('subtract', 5),
        ('divide', 5)
    ]
    
    for op in operations:
        current_result = calc.send(op)
        print(f"执行 {op[0]} {op[1]}: 结果 = {current_result}")
    
    # 测试错误处理
    try:
        calc.send(('divide', 0))
    except StopIteration:
        pass
    
    # 重置
    current_result = calc.send(('reset', 0))
    print(f"重置后: {current_result}")
    
    calc.close()
    
    # 练习3.2：状态机生成器
    def state_machine_generator():
        """简单状态机"""
        state = 'idle'
        
        while True:
            try:
                action = yield state
                
                if state == 'idle':
                    if action == 'start':
                        state = 'running'
                    elif action == 'configure':
                        state = 'configuring'
                
                elif state == 'running':
                    if action == 'pause':
                        state = 'paused'
                    elif action == 'stop':
                        state = 'idle'
                
                elif state == 'paused':
                    if action == 'resume':
                        state = 'running'
                    elif action == 'stop':
                        state = 'idle'
                
                elif state == 'configuring':
                    if action == 'save':
                        state = 'idle'
                    elif action == 'cancel':
                        state = 'idle'
                
            except GeneratorExit:
                print("    状态机关闭")
                break
    
    print("\n3.2 状态机生成器:")
    sm = state_machine_generator()
    
    current_state = next(sm)
    print(f"初始状态: {current_state}")
    
    # 状态转换
    transitions = ['start', 'pause', 'resume', 'stop', 'configure', 'save']
    
    for action in transitions:
        current_state = sm.send(action)
        print(f"执行 '{action}' -> 状态: {current_state}")
    
    sm.close()
    
    # 练习3.3：异常处理生成器
    def error_handling_generator():
        """错误处理生成器"""
        count = 0
        
        while True:
            try:
                value = yield count
                
                if value is None:
                    continue
                
                if isinstance(value, (int, float)):
                    count += value
                else:
                    raise TypeError(f"期望数字，得到 {type(value)}")
                
            except TypeError as e:
                print(f"    类型错误: {e}")
                yield f"错误: {e}"
            
            except ValueError as e:
                print(f"    值错误: {e}")
                yield f"错误: {e}"
            
            except Exception as e:
                print(f"    未知错误: {e}")
                yield f"错误: {e}"
    
    print("\n3.3 异常处理生成器:")
    error_gen = error_handling_generator()
    
    current_count = next(error_gen)
    print(f"初始计数: {current_count}")
    
    # 测试正常值
    test_values = [5, 3.14, "invalid", -2, None, 10]
    
    for value in test_values:
        try:
            result = error_gen.send(value)
            print(f"发送 {value}: 结果 = {result}")
        except StopIteration:
            break
    
    # 测试throw方法
    try:
        error_gen.throw(ValueError, "手动抛出的错误")
    except StopIteration:
        pass
    
    error_gen.close()

generator_methods_exercises()
```

### 练习4：数据流处理

**目标**：构建复杂的数据处理管道。

```python
def data_pipeline_exercises():
    """数据流处理练习"""
    print("\n=== 数据流处理练习 ===")
    
    # 练习4.1：日志处理管道
    def log_parser(log_lines):
        """日志解析器"""
        import re
        
        # 日志格式：时间戳 [级别] 来源: 消息
        pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (\w+): (.+)'
        
        for line in log_lines:
            line = line.strip()
            if not line:
                continue
            
            match = re.match(pattern, line)
            if match:
                timestamp, level, source, message = match.groups()
                yield {
                    'timestamp': timestamp,
                    'level': level,
                    'source': source,
                    'message': message,
                    'raw': line
                }
    
    def log_filter(parsed_logs, level_filter=None, source_filter=None):
        """日志过滤器"""
        for log_entry in parsed_logs:
            if level_filter and log_entry['level'] not in level_filter:
                continue
            
            if source_filter and log_entry['source'] not in source_filter:
                continue
            
            yield log_entry
    
    def log_aggregator(filtered_logs, group_by='level'):
        """日志聚合器"""
        stats = {}
        
        for log_entry in filtered_logs:
            key = log_entry[group_by]
            
            if key not in stats:
                stats[key] = {
                    'count': 0,
                    'first_seen': log_entry['timestamp'],
                    'last_seen': log_entry['timestamp'],
                    'sources': set(),
                    'sample_messages': []
                }
            
            stats[key]['count'] += 1
            stats[key]['last_seen'] = log_entry['timestamp']
            stats[key]['sources'].add(log_entry['source'])
            
            if len(stats[key]['sample_messages']) < 3:
                stats[key]['sample_messages'].append(log_entry['message'])
            
            # 定期产出统计结果
            if sum(s['count'] for s in stats.values()) % 5 == 0:
                yield stats.copy()
        
        # 最终统计结果
        yield stats
    
    print("\n4.1 日志处理管道:")
    
    # 模拟日志数据
    sample_logs = [
        "2024-01-15 10:30:15 [INFO] web_server: Request processed successfully",
        "2024-01-15 10:30:16 [ERROR] database: Connection timeout",
        "2024-01-15 10:30:17 [WARNING] cache: Memory usage high",
        "2024-01-15 10:30:18 [INFO] auth_service: User login successful",
        "2024-01-15 10:30:19 [ERROR] web_server: 404 Not Found",
        "2024-01-15 10:30:20 [INFO] database: Query executed",
        "2024-01-15 10:30:21 [WARNING] web_server: Slow response time",
        "2024-01-15 10:30:22 [ERROR] cache: Cache miss rate high",
        "2024-01-15 10:30:23 [INFO] auth_service: Token refreshed",
        "2024-01-15 10:30:24 [ERROR] database: Deadlock detected"
    ]
    
    # 构建处理管道
    parsed = log_parser(sample_logs)
    filtered = log_filter(parsed, level_filter=['ERROR', 'WARNING'])
    aggregated = log_aggregator(filtered, group_by='level')
    
    # 处理结果
    for stats in aggregated:
        print("\n  当前统计:")
        for level, info in stats.items():
            sources_list = list(info['sources'])
            print(f"    {level}: {info['count']} 条，来源: {sources_list}")
            print(f"      示例消息: {info['sample_messages'][:2]}")
    
    # 练习4.2：数据清洗管道
    def data_cleaner(raw_data):
        """数据清洗器"""
        for record in raw_data:
            # 移除空值和无效数据
            if not record or not isinstance(record, dict):
                continue
            
            cleaned_record = {}
            
            for key, value in record.items():
                # 清理字符串
                if isinstance(value, str):
                    value = value.strip()
                    if value.lower() in ['null', 'none', 'n/a', '']:
                        continue
                
                # 转换数字
                elif isinstance(value, str) and value.replace('.', '').replace('-', '').isdigit():
                    try:
                        value = float(value) if '.' in value else int(value)
                    except ValueError:
                        continue
                
                cleaned_record[key] = value
            
            if cleaned_record:  # 只产出非空记录
                yield cleaned_record
    
    def data_validator(cleaned_data, required_fields=None):
        """数据验证器"""
        required_fields = required_fields or []
        
        for record in cleaned_data:
            # 检查必需字段
            if all(field in record for field in required_fields):
                # 添加验证标记
                record['_validated'] = True
                yield record
            else:
                # 记录验证失败
                missing_fields = [f for f in required_fields if f not in record]
                record['_validation_error'] = f"缺少字段: {missing_fields}"
                yield record
    
    def data_enricher(validated_data):
        """数据丰富器"""
        for record in validated_data:
            if record.get('_validated'):
                # 添加计算字段
                if 'age' in record:
                    if record['age'] < 18:
                        record['category'] = 'minor'
                    elif record['age'] < 65:
                        record['category'] = 'adult'
                    else:
                        record['category'] = 'senior'
                
                # 添加处理时间戳
                from datetime import datetime
                record['processed_at'] = datetime.now().isoformat()
            
            yield record
    
    print("\n4.2 数据清洗管道:")
    
    # 模拟原始数据
    raw_records = [
        {'name': 'Alice', 'age': '25', 'email': 'alice@example.com'},
        {'name': '  Bob  ', 'age': 'null', 'email': 'bob@example.com'},
        {'name': 'Charlie', 'age': '17', 'email': ''},
        None,  # 无效记录
        {'name': '', 'age': '45', 'email': 'diana@example.com'},
        {'name': 'Eve', 'age': '70', 'email': 'eve@example.com'},
        {'age': '30'},  # 缺少name字段
    ]
    
    # 构建清洗管道
    cleaned = data_cleaner(raw_records)
    validated = data_validator(cleaned, required_fields=['name', 'email'])
    enriched = data_enricher(validated)
    
    # 处理结果
    print("  清洗后的数据:")
    for i, record in enumerate(enriched, 1):
        print(f"    记录 {i}: {record}")

data_pipeline_exercises()
```

## 高级练习

### 练习5：协程应用

**目标**：实现基于生成器的协程系统。

```python
def coroutine_exercises():
    """协程应用练习"""
    print("\n=== 协程应用练习 ===")
    
    # 练习5.1：任务调度器
    class TaskScheduler:
        """简单的任务调度器"""
        
        def __init__(self):
            self.tasks = []
            self.task_id = 0
        
        def add_task(self, task_gen):
            """添加任务"""
            self.task_id += 1
            task = {
                'id': self.task_id,
                'generator': task_gen,
                'status': 'ready'
            }
            self.tasks.append(task)
            return self.task_id
        
        def run(self, max_iterations=100):
            """运行调度器"""
            iteration = 0
            
            while self.tasks and iteration < max_iterations:
                iteration += 1
                print(f"\n  调度轮次 {iteration}:")
                
                completed_tasks = []
                
                for task in self.tasks[:]:
                    try:
                        # 执行任务的下一步
                        result = next(task['generator'])
                        task['status'] = 'running'
                        print(f"    任务 {task['id']}: {result}")
                        
                    except StopIteration:
                        task['status'] = 'completed'
                        completed_tasks.append(task)
                        print(f"    任务 {task['id']}: 已完成")
                    
                    except Exception as e:
                        task['status'] = 'error'
                        completed_tasks.append(task)
                        print(f"    任务 {task['id']}: 错误 - {e}")
                
                # 移除已完成的任务
                for task in completed_tasks:
                    self.tasks.remove(task)
                
                if not self.tasks:
                    print("  所有任务已完成")
                    break
    
    def countdown_task(name, count):
        """倒计时任务"""
        for i in range(count, 0, -1):
            yield f"{name} 倒计时: {i}"
        yield f"{name} 完成！"
    
    def fibonacci_task(name, count):
        """斐波那契任务"""
        a, b = 0, 1
        for i in range(count):
            yield f"{name} 斐波那契: {a}"
            a, b = b, a + b
    
    def calculation_task(name, operations):
        """计算任务"""
        result = 0
        for op, value in operations:
            if op == 'add':
                result += value
            elif op == 'multiply':
                result *= value
            yield f"{name} 计算: {op} {value} = {result}"
    
    print("\n5.1 任务调度器:")
    
    scheduler = TaskScheduler()
    
    # 添加任务
    scheduler.add_task(countdown_task("任务A", 3))
    scheduler.add_task(fibonacci_task("任务B", 4))
    scheduler.add_task(calculation_task("任务C", [('add', 10), ('multiply', 2), ('add', 5)]))
    
    # 运行调度器
    scheduler.run()
    
    # 练习5.2：生产者-消费者模式
    def producer_consumer_exercise():
        """生产者-消费者练习"""
        
        def producer(name, items):
            """生产者协程"""
            for item in items:
                print(f"    {name} 生产: {item}")
                received = yield item
                if received:
                    print(f"    {name} 收到确认: {received}")
        
        def consumer(name):
            """消费者协程"""
            consumed_items = []
            
            while True:
                try:
                    item = yield
                    if item is not None:
                        consumed_items.append(item)
                        print(f"    {name} 消费: {item}")
                        # 发送确认
                        confirmation = f"已处理 {item}"
                        yield confirmation
                except GeneratorExit:
                    print(f"    {name} 总共消费了 {len(consumed_items)} 个项目")
                    break
        
        def mediator(producers, consumers):
            """中介者协程"""
            # 启动消费者
            for consumer_gen in consumers:
                next(consumer_gen)
            
            # 处理生产者的产品
            for producer_gen in producers:
                try:
                    while True:
                        item = next(producer_gen)
                        
                        # 轮询分配给消费者
                        consumer_gen = consumers[len(consumers) % len(consumers)]
                        confirmation = consumer_gen.send(item)
                        
                        # 将确认发送回生产者
                        try:
                            producer_gen.send(confirmation)
                        except StopIteration:
                            break
                
                except StopIteration:
                    continue
            
            # 关闭消费者
            for consumer_gen in consumers:
                consumer_gen.close()
        
        print("\n5.2 生产者-消费者模式:")
        
        # 创建生产者
        producer1 = producer("生产者1", ["苹果", "香蕉", "橙子"])
        producer2 = producer("生产者2", ["面包", "牛奶", "鸡蛋"])
        
        # 创建消费者
        consumer1 = consumer("消费者1")
        consumer2 = consumer("消费者2")
        
        # 运行中介者
        mediator([producer1, producer2], [consumer1, consumer2])
    
    producer_consumer_exercise()
    
    # 练习5.3：状态机协程
    def state_machine_coroutine():
        """状态机协程"""
        
        def traffic_light():
            """交通灯状态机"""
            states = ['red', 'green', 'yellow']
            current_state = 0
            
            while True:
                state = states[current_state]
                action = yield state
                
                if action == 'next':
                    current_state = (current_state + 1) % len(states)
                elif action == 'reset':
                    current_state = 0
                elif action == 'stop':
                    break
        
        def elevator_controller():
            """电梯控制器"""
            floor = 1
            direction = 'idle'
            
            while True:
                status = f"楼层 {floor}, 状态: {direction}"
                command = yield status
                
                if command is None:
                    continue
                
                cmd_type, target = command
                
                if cmd_type == 'goto':
                    if target > floor:
                        direction = 'up'
                        floor += 1
                    elif target < floor:
                        direction = 'down'
                        floor -= 1
                    else:
                        direction = 'idle'
                
                elif cmd_type == 'emergency':
                    direction = 'emergency_stop'
                
                elif cmd_type == 'reset':
                    floor = 1
                    direction = 'idle'
        
        print("\n5.3 状态机协程:")
        
        # 交通灯测试
        print("  交通灯状态机:")
        traffic = traffic_light()
        
        current_light = next(traffic)
        print(f"    初始状态: {current_light}")
        
        for _ in range(5):
            current_light = traffic.send('next')
            print(f"    切换后: {current_light}")
        
        traffic.send('stop')
        
        # 电梯测试
        print("\n  电梯控制器:")
        elevator = elevator_controller()
        
        current_status = next(elevator)
        print(f"    初始状态: {current_status}")
        
        commands = [
            ('goto', 5),
            ('goto', 5),
            ('goto', 5),
            ('goto', 5),
            ('goto', 3),
            ('goto', 3),
            ('emergency', None),
            ('reset', None)
        ]
        
        for cmd in commands:
            current_status = elevator.send(cmd)
            print(f"    执行 {cmd}: {current_status}")
        
        elevator.close()
    
    state_machine_coroutine()

coroutine_exercises()
```

### 练习6：性能优化

**目标**：通过生成器优化程序性能。

```python
def performance_optimization_exercises():
    """性能优化练习"""
    print("\n=== 性能优化练习 ===")
    
    import time
    import gc
    
    # 练习6.1：大数据集处理优化
    def large_dataset_optimization():
        """大数据集处理优化"""
        
        def traditional_approach(size):
            """传统方法"""
            # 生成所有数据
            data = list(range(size))
            
            # 处理所有数据
            processed = []
            for item in data:
                if item % 2 == 0:
                    result = item ** 2 + item
                    processed.append(result)
            
            # 只返回前10个结果
            return processed[:10]
        
        def generator_approach(size):
            """生成器方法"""
            def data_generator():
                for i in range(size):
                    yield i
            
            def process_generator(data_gen):
                for item in data_gen:
                    if item % 2 == 0:
                        yield item ** 2 + item
            
            # 创建处理管道
            data_gen = data_generator()
            processed_gen = process_generator(data_gen)
            
            # 只获取前10个结果
            results = []
            for i, result in enumerate(processed_gen):
                if i >= 10:
                    break
                results.append(result)
            
            return results
        
        print("\n6.1 大数据集处理优化:")
        
        test_size = 1000000
        
        # 测试传统方法
        print(f"  处理 {test_size:,} 个元素，只需要前10个结果")
        
        gc.collect()
        start_time = time.time()
        traditional_results = traditional_approach(test_size)
        traditional_time = time.time() - start_time
        
        print(f"  传统方法: {traditional_time:.4f}秒")
        print(f"  结果: {traditional_results}")
        
        # 测试生成器方法
        gc.collect()
        start_time = time.time()
        generator_results = generator_approach(test_size)
        generator_time = time.time() - start_time
        
        print(f"  生成器方法: {generator_time:.4f}秒")
        print(f"  结果: {generator_results}")
        
        # 性能对比
        if generator_time > 0:
            speedup = traditional_time / generator_time
            print(f"  性能提升: {speedup:.2f}倍")
    
    large_dataset_optimization()
    
    # 练习6.2：内存使用优化
    def memory_optimization():
        """内存使用优化"""
        
        def memory_intensive_function(data_size):
            """内存密集型函数"""
            # 创建大量数据
            large_list = []
            for i in range(data_size):
                item = {
                    'id': i,
                    'data': f"item_{i}" * 10,  # 较大的字符串
                    'values': list(range(i % 100))  # 变长列表
                }
                large_list.append(item)
            
            # 处理数据
            results = []
            for item in large_list:
                if item['id'] % 1000 == 0:  # 只处理部分数据
                    processed = {
                        'id': item['id'],
                        'summary': len(item['data']),
                        'count': len(item['values'])
                    }
                    results.append(processed)
            
            return results
        
        def memory_efficient_function(data_size):
            """内存高效函数"""
            def data_generator():
                for i in range(data_size):
                    yield {
                        'id': i,
                        'data': f"item_{i}" * 10,
                        'values': list(range(i % 100))
                    }
            
            def process_generator(data_gen):
                for item in data_gen:
                    if item['id'] % 1000 == 0:
                        yield {
                            'id': item['id'],
                            'summary': len(item['data']),
                            'count': len(item['values'])
                        }
            
            # 使用生成器管道
            data_gen = data_generator()
            processed_gen = process_generator(data_gen)
            
            return list(processed_gen)
        
        print("\n6.2 内存使用优化:")
        
        test_size = 100000
        
        # 测试内存密集型方法
        print(f"  处理 {test_size:,} 个项目")
        
        gc.collect()
        before_objects = len(gc.get_objects())
        start_time = time.time()
        
        intensive_results = memory_intensive_function(test_size)
        
        intensive_time = time.time() - start_time
        after_objects = len(gc.get_objects())
        intensive_objects = after_objects - before_objects
        
        print(f"  内存密集型: {intensive_time:.4f}秒")
        print(f"  创建对象: {intensive_objects:,} 个")
        print(f"  结果数量: {len(intensive_results)}")
        
        # 清理
        del intensive_results
        gc.collect()
        
        # 测试内存高效方法
        before_objects = len(gc.get_objects())
        start_time = time.time()
        
        efficient_results = memory_efficient_function(test_size)
        
        efficient_time = time.time() - start_time
        after_objects = len(gc.get_objects())
        efficient_objects = after_objects - before_objects
        
        print(f"  内存高效型: {efficient_time:.4f}秒")
        print(f"  创建对象: {efficient_objects:,} 个")
        print(f"  结果数量: {len(efficient_results)}")
        
        # 性能对比
        if efficient_objects > 0:
            memory_efficiency = intensive_objects / efficient_objects
            print(f"  内存效率提升: {memory_efficiency:.2f}倍")
        
        if efficient_time > 0:
            time_efficiency = intensive_time / efficient_time
            print(f"  时间效率提升: {time_efficiency:.2f}倍")
    
    memory_optimization()
    
    # 练习6.3：缓存和惰性计算
    def caching_and_lazy_computation():
        """缓存和惰性计算"""
        
        class LazyCache:
            """惰性缓存"""
            
            def __init__(self):
                self._cache = {}
                self._generators = {}
            
            def get_or_create(self, key, generator_func, *args, **kwargs):
                """获取或创建缓存项"""
                if key not in self._cache:
                    print(f"    创建生成器: {key}")
                    self._generators[key] = generator_func(*args, **kwargs)
                    self._cache[key] = []
                
                return self._get_cached_generator(key)
            
            def _get_cached_generator(self, key):
                """获取缓存的生成器"""
                cached_items = self._cache[key]
                generator = self._generators[key]
                
                # 先返回已缓存的项目
                for item in cached_items:
                    yield item
                
                # 然后从生成器获取新项目并缓存
                try:
                    while True:
                        item = next(generator)
                        cached_items.append(item)
                        yield item
                except StopIteration:
                    pass
        
        def expensive_computation(n, delay=0.01):
            """昂贵的计算"""
            for i in range(n):
                time.sleep(delay)  # 模拟计算时间
                yield i ** 3
        
        def fibonacci_sequence(n):
            """斐波那契序列"""
            a, b = 0, 1
            for _ in range(n):
                yield a
                a, b = b, a + b
        
        print("\n6.3 缓存和惰性计算:")
        
        cache = LazyCache()
        
        # 第一次访问 - 需要计算
        print("  第一次访问昂贵计算:")
        start_time = time.time()
        
        expensive_gen = cache.get_or_create('expensive', expensive_computation, 5, 0.1)
        first_three = [next(expensive_gen) for _ in range(3)]
        
        first_time = time.time() - start_time
        print(f"    前3个结果: {first_three}")
        print(f"    耗时: {first_time:.3f}秒")
        
        # 第二次访问相同数据 - 使用缓存
        print("\n  第二次访问相同数据:")
        start_time = time.time()
        
        expensive_gen2 = cache.get_or_create('expensive', expensive_computation, 5, 0.1)
        cached_three = [next(expensive_gen2) for _ in range(3)]
        
        cached_time = time.time() - start_time
        print(f"    前3个结果: {cached_three}")
        print(f"    耗时: {cached_time:.3f}秒")
        
        # 继续获取更多数据
        print("\n  继续获取更多数据:")
        start_time = time.time()
        
        remaining = [next(expensive_gen2) for _ in range(2)]
        
        remaining_time = time.time() - start_time
        print(f"    剩余结果: {remaining}")
        print(f"    耗时: {remaining_time:.3f}秒")
        
        # 性能对比
        print(f"\n  性能对比:")
        print(f"    首次计算: {first_time:.3f}秒")
        print(f"    缓存访问: {cached_time:.3f}秒")
        print(f"    继续计算: {remaining_time:.3f}秒")
        
        if cached_time > 0:
            cache_speedup = first_time / cached_time
            print(f"    缓存加速: {cache_speedup:.2f}倍")
    
    caching_and_lazy_computation()

performance_optimization_exercises()
```

## 实战项目

### 练习7：数据分析工具

**目标**：构建一个基于生成器的数据分析工具。

```python
def data_analysis_tool():
    """数据分析工具实战项目"""
    print("\n=== 数据分析工具实战项目 ===")
    
    import json
    import tempfile
    import os
    from datetime import datetime, timedelta
    
    class StreamingDataAnalyzer:
        """流式数据分析器"""
        
        def __init__(self):
            self.processors = []
        
        def add_processor(self, processor):
            """添加处理器"""
            self.processors.append(processor)
        
        def analyze(self, data_source):
            """分析数据"""
            # 构建处理管道
            current_stream = data_source
            
            for processor in self.processors:
                current_stream = processor(current_stream)
            
            # 返回最终结果
            return current_stream
    
    # 数据源生成器
    def sales_data_generator(filename):
        """销售数据生成器"""
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    data = json.loads(line.strip())
                    data['_line_number'] = line_num
                    yield data
                except json.JSONDecodeError as e:
                    print(f"    跳过无效行 {line_num}: {e}")
                    continue
    
    # 数据处理器
    def date_filter(data_stream, start_date=None, end_date=None):
        """日期过滤器"""
        for record in data_stream:
            record_date = datetime.fromisoformat(record['date'])
            
            if start_date and record_date < start_date:
                continue
            
            if end_date and record_date > end_date:
                continue
            
            yield record
    
    def product_filter(data_stream, categories=None, min_price=None, max_price=None):
        """产品过滤器"""
        for record in data_stream:
            # 类别过滤
            if categories and record['category'] not in categories:
                continue
            
            # 价格过滤
            if min_price and record['price'] < min_price:
                continue
            
            if max_price and record['price'] > max_price:
                continue
            
            yield record
    
    def sales_aggregator(data_stream, group_by='category'):
        """销售聚合器"""
        aggregates = {}
        
        for record in data_stream:
            key = record[group_by]
            
            if key not in aggregates:
                aggregates[key] = {
                    'count': 0,
                    'total_revenue': 0,
                    'total_quantity': 0,
                    'avg_price': 0,
                    'first_sale': record['date'],
                    'last_sale': record['date']
                }
            
            agg = aggregates[key]
            agg['count'] += 1
            agg['total_revenue'] += record['price'] * record['quantity']
            agg['total_quantity'] += record['quantity']
            agg['avg_price'] = agg['total_revenue'] / agg['total_quantity']
            
            if record['date'] > agg['last_sale']:
                agg['last_sale'] = record['date']
            
            if record['date'] < agg['first_sale']:
                agg['first_sale'] = record['date']
            
            # 定期产出中间结果
            if sum(a['count'] for a in aggregates.values()) % 10 == 0:
                yield aggregates.copy()
        
        # 最终结果
        yield aggregates
    
    def trend_analyzer(data_stream, window_size=7):
        """趋势分析器"""
        daily_sales = {}
        
        for record in data_stream:
            date = record['date'][:10]  # 只取日期部分
            
            if date not in daily_sales:
                daily_sales[date] = {
                    'revenue': 0,
                    'quantity': 0,
                    'transactions': 0
                }
            
            daily_sales[date]['revenue'] += record['price'] * record['quantity']
            daily_sales[date]['quantity'] += record['quantity']
            daily_sales[date]['transactions'] += 1
        
        # 计算移动平均
        sorted_dates = sorted(daily_sales.keys())
        
        for i in range(len(sorted_dates)):
            current_date = sorted_dates[i]
            
            # 计算窗口范围
            start_idx = max(0, i - window_size + 1)
            window_dates = sorted_dates[start_idx:i + 1]
            
            # 计算移动平均
            window_revenue = sum(daily_sales[d]['revenue'] for d in window_dates)
            window_quantity = sum(daily_sales[d]['quantity'] for d in window_dates)
            window_transactions = sum(daily_sales[d]['transactions'] for d in window_dates)
            
            avg_revenue = window_revenue / len(window_dates)
            avg_quantity = window_quantity / len(window_dates)
            avg_transactions = window_transactions / len(window_dates)
            
            yield {
                'date': current_date,
                'daily_revenue': daily_sales[current_date]['revenue'],
                'avg_revenue': avg_revenue,
                'daily_quantity': daily_sales[current_date]['quantity'],
                'avg_quantity': avg_quantity,
                'daily_transactions': daily_sales[current_date]['transactions'],
                'avg_transactions': avg_transactions,
                'trend': 'up' if daily_sales[current_date]['revenue'] > avg_revenue else 'down'
            }
    
    # 创建测试数据
    def create_sample_data(filename, days=30, records_per_day=50):
        """创建示例销售数据"""
        categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']
        products = {
            'Electronics': ['Laptop', 'Phone', 'Tablet', 'Headphones'],
            'Clothing': ['Shirt', 'Pants', 'Dress', 'Shoes'],
            'Books': ['Novel', 'Textbook', 'Magazine', 'Comic'],
            'Home': ['Chair', 'Table', 'Lamp', 'Curtain'],
            'Sports': ['Ball', 'Racket', 'Shoes', 'Equipment']
        }
        
        import random
        
        with open(filename, 'w', encoding='utf-8') as f:
            base_date = datetime.now() - timedelta(days=days)
            
            for day in range(days):
                current_date = base_date + timedelta(days=day)
                
                for _ in range(records_per_day):
                    category = random.choice(categories)
                    product = random.choice(products[category])
                    
                    record = {
                        'date': current_date.isoformat(),
                        'category': category,
                        'product': product,
                        'price': round(random.uniform(10, 500), 2),
                        'quantity': random.randint(1, 10),
                        'customer_id': f"CUST_{random.randint(1000, 9999)}"
                    }
                    
                    f.write(json.dumps(record) + '\n')
        
        print(f"  创建了 {days} 天的销售数据，共 {days * records_per_day} 条记录")
    
    # 运行分析
    print("\n7. 数据分析工具实战:")
    
    # 创建临时数据文件
    temp_dir = tempfile.mkdtemp()
    data_file = os.path.join(temp_dir, 'sales_data.jsonl')
    
    try:
        # 生成测试数据
        create_sample_data(data_file, days=14, records_per_day=20)
        
        # 创建分析器
        analyzer = StreamingDataAnalyzer()
        
        # 分析1：按类别聚合销售数据
        print("\n  分析1：按类别聚合销售数据")
        
        data_source = sales_data_generator(data_file)
        
        # 添加处理器
        filtered_data = product_filter(data_source, min_price=50)
        aggregated_data = sales_aggregator(filtered_data, group_by='category')
        
        # 获取结果
        final_aggregates = None
        for result in aggregated_data:
            final_aggregates = result
        
        print("    按类别聚合结果:")
        for category, stats in final_aggregates.items():
            print(f"      {category}:")
            print(f"        交易数: {stats['count']}")
            print(f"        总收入: ${stats['total_revenue']:.2f}")
            print(f"        平均价格: ${stats['avg_price']:.2f}")
        
        # 分析2：趋势分析
        print("\n  分析2：销售趋势分析")
        
        data_source = sales_data_generator(data_file)
        trend_data = trend_analyzer(data_source, window_size=3)
        
        print("    最近几天的趋势:")
        trend_results = list(trend_data)
        
        for trend in trend_results[-7:]:  # 显示最后7天
            print(f"      {trend['date']}: ")
            print(f"        日收入: ${trend['daily_revenue']:.2f} ")
            print(f"        (平均: ${trend['avg_revenue']:.2f}, 趋势: {trend['trend']})")
        
        # 分析3：组合分析
        print("\n  分析3：高价值产品分析")
        
        data_source = sales_data_generator(data_file)
        
        # 过滤高价值交易
        high_value = product_filter(data_source, min_price=100)
        
        # 按产品聚合
        product_aggregates = sales_aggregator(high_value, group_by='product')
        
        final_products = None
        for result in product_aggregates:
            final_products = result
        
        # 找出最有价值的产品
        if final_products:
            sorted_products = sorted(
                final_products.items(),
                key=lambda x: x[1]['total_revenue'],
                reverse=True
            )
            
            print("    高价值产品排行:")
            for i, (product, stats) in enumerate(sorted_products[:5], 1):
                print(f"      {i}. {product}:")
                print(f"         总收入: ${stats['total_revenue']:.2f}")
                print(f"         交易数: {stats['count']}")
                print(f"         平均价格: ${stats['avg_price']:.2f}")
    
    finally:
        # 清理临时文件
        if os.path.exists(data_file):
            os.remove(data_file)
        os.rmdir(temp_dir)
        print(f"\n  清理临时文件: {data_file}")

data_analysis_tool()
```

## 练习总结

### 学习成果检验

```python
def exercise_summary():
    """练习总结和学习成果检验"""
    print("\n=== 练习总结 ===")
    
    print("\n通过这些练习，你应该掌握了:")
    
    skills = [
        "1. 基础生成器的创建和使用",
        "2. 生成器表达式的灵活应用",
        "3. 生成器方法(send, throw, close)的使用",
        "4. 复杂数据处理管道的构建",
        "5. 基于生成器的协程编程",
        "6. 性能优化和内存管理",
        "7. 实际项目中的生成器应用"
    ]
    
    for skill in skills:
        print(f"  ✓ {skill}")
    
    print("\n下一步学习建议:")
    
    next_steps = [
        "1. 深入学习asyncio和异步编程",
        "2. 探索更多的函数式编程概念",
        "3. 学习装饰器和上下文管理器",
        "4. 研究Python的内存管理机制",
        "5. 实践更多的数据处理项目"
    ]
    
    for step in next_steps:
        print(f"  → {step}")
    
    print("\n恭喜你完成了生成器的综合练习！")
    print("继续保持学习的热情，探索Python的更多高级特性。")

exercise_summary()
```

## 学习要点总结

### 核心技能

1. **生成器基础**：能够创建和使用各种类型的生成器
2. **表达式应用**：熟练使用生成器表达式处理数据
3. **方法掌握**：理解并能使用send()、throw()、close()方法
4. **管道构建**：能够构建复杂的数据处理管道
5. **协程编程**：掌握基于生成器的协程编程模式
6. **性能优化**：能够使用生成器优化程序性能
7. **实战应用**：能够在实际项目中合理使用生成器

### 最佳实践

1. **合理选择**：在适当的场景使用生成器
2. **错误处理**：妥善处理生成器中的异常
3. **资源管理**：确保生成器资源的正确释放
4. **性能考虑**：平衡内存使用和计算效率
5. **代码可读性**：保持生成器代码的清晰和可维护性

### 实际应用

1. **数据处理**：大数据集的流式处理
2. **文件操作**：大文件的逐行处理
3. **网络编程**：流式数据的处理
4. **算法实现**：内存高效的算法实现
5. **系统编程**：协程和异步处理

## 练习建议

### 基础练习

1. **从简单开始**：先掌握基本的生成器创建和使用
2. **逐步深入**：循序渐进地学习高级特性
3. **多做实践**：通过编写代码来加深理解
4. **对比学习**：比较生成器和传统方法的差异

### 进阶练习

1. **组合应用**：将多个概念结合使用
2. **性能测试**：测量和比较不同实现的性能
3. **错误处理**：学习处理各种异常情况
4. **代码重构**：将现有代码改写为生成器版本

### 实战项目

1. **选择合适的项目**：找到适合使用生成器的实际问题
2. **完整实现**：从需求分析到代码实现的完整过程
3. **性能优化**：持续改进和优化代码性能
4. **文档编写**：为你的生成器代码编写清晰的文档

## 学习目标

完成这些练习后，你将能够：

- 熟练创建和使用各种类型的生成器
- 理解生成器的内部工作机制
- 在适当的场景选择使用生成器
- 构建高效的数据处理管道
- 编写基于生成器的协程程序
- 优化程序的内存使用和性能
- 在实际项目中应用生成器技术

## 下一步学习

- [返回生成器学习首页](./index.md)
- [学习装饰器](../25-decorators/index.md)
- [探索上下文管理器](../26-context-managers/index.md)
- [深入异步编程](../27-async-programming/index.md)**系