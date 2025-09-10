# 生成器的协程应用

协程（Coroutine）是一种特殊的函数，它可以在执行过程中暂停和恢复，允许多个协程之间协作式地共享CPU时间。Python的生成器为协程提供了基础实现，通过`yield`、`send()`、`throw()`和`close()`方法，我们可以实现强大的协程功能。

## 协程基础概念

### 什么是协程

协程是一种用户态的轻量级线程，由用户程序自己控制调度。与传统的抢占式多任务不同，协程采用协作式多任务，函数可以主动让出控制权。

```python
def coroutine_basics():
    """协程基础概念演示"""
    print("=== 协程基础概念 ===")
    
    def simple_coroutine():
        """简单协程示例"""
        print("  协程启动")
        
        while True:
            # 接收数据并处理
            data = yield
            if data is None:
                continue
            
            print(f"  协程处理数据: {data}")
            
            if data == 'stop':
                print("  协程停止")
                break
    
    # 创建协程
    coro = simple_coroutine()
    
    # 启动协程（预激活）
    next(coro)  # 或者 coro.send(None)
    
    # 向协程发送数据
    test_data = ['hello', 'world', 'python', 'stop']
    
    for data in test_data:
        print(f"发送数据: {data}")
        try:
            coro.send(data)
        except StopIteration:
            print("协程已结束")
            break

coroutine_basics()
```

### 协程装饰器

为了简化协程的使用，我们可以创建一个装饰器来自动预激活协程。

```python
def coroutine_decorator():
    """协程装饰器演示"""
    print("\n=== 协程装饰器 ===")
    
    def coroutine(func):
        """协程装饰器 - 自动预激活"""
        def wrapper(*args, **kwargs):
            gen = func(*args, **kwargs)
            next(gen)  # 预激活
            return gen
        return wrapper
    
    @coroutine
    def echo_coroutine(prefix="Echo"):
        """回声协程"""
        print(f"  {prefix} 协程启动")
        
        try:
            while True:
                data = yield
                if data:
                    print(f"  {prefix}: {data}")
        except GeneratorExit:
            print(f"  {prefix} 协程关闭")
    
    @coroutine
    def filter_coroutine(condition):
        """过滤协程"""
        print(f"  过滤协程启动，条件: {condition.__name__}")
        
        try:
            while True:
                data = yield
                if data is not None and condition(data):
                    print(f"  过滤通过: {data}")
                elif data is not None:
                    print(f"  过滤拒绝: {data}")
        except GeneratorExit:
            print("  过滤协程关闭")
    
    # 使用装饰器创建的协程
    echo = echo_coroutine("回声")
    
    # 创建过滤协程
    def is_positive(x):
        return isinstance(x, (int, float)) and x > 0
    
    filter_coro = filter_coroutine(is_positive)
    
    # 测试数据
    test_data = ["hello", 5, -3, 10, "world", 0, 7]
    
    print("\n测试回声协程:")
    for data in test_data[:3]:
        echo.send(data)
    
    print("\n测试过滤协程:")
    for data in test_data:
        filter_coro.send(data)
    
    # 关闭协程
    echo.close()
    filter_coro.close()

coroutine_decorator()
```

## 协程管道

### 数据处理管道

协程的一个重要应用是构建数据处理管道，每个协程负责一个处理步骤。

```python
def coroutine_pipeline():
    """协程管道演示"""
    print("\n=== 协程管道 ===")
    
    def coroutine(func):
        """协程装饰器"""
        def wrapper(*args, **kwargs):
            gen = func(*args, **kwargs)
            next(gen)
            return gen
        return wrapper
    
    @coroutine
    def data_source(target):
        """数据源协程"""
        print("  数据源启动")
        
        try:
            while True:
                data = yield
                if data is not None:
                    print(f"  数据源接收: {data}")
                    target.send(data)
        except GeneratorExit:
            print("  数据源关闭")
            target.close()
    
    @coroutine
    def data_filter(condition, target):
        """数据过滤协程"""
        print(f"  过滤器启动")
        
        try:
            while True:
                data = yield
                if data is not None:
                    if condition(data):
                        print(f"  过滤器通过: {data}")
                        target.send(data)
                    else:
                        print(f"  过滤器拒绝: {data}")
        except GeneratorExit:
            print("  过滤器关闭")
            target.close()
    
    @coroutine
    def data_transformer(transform_func, target):
        """数据转换协程"""
        print("  转换器启动")
        
        try:
            while True:
                data = yield
                if data is not None:
                    transformed = transform_func(data)
                    print(f"  转换器: {data} -> {transformed}")
                    target.send(transformed)
        except GeneratorExit:
            print("  转换器关闭")
            target.close()
    
    @coroutine
    def data_sink():
        """数据接收器协程"""
        print("  接收器启动")
        results = []
        
        try:
            while True:
                data = yield
                if data is not None:
                    results.append(data)
                    print(f"  接收器存储: {data}")
        except GeneratorExit:
            print(f"  接收器关闭，共收到 {len(results)} 个数据")
            print(f"  最终结果: {results}")
    
    # 构建处理管道
    # 数据流: 源 -> 过滤器 -> 转换器 -> 接收器
    
    sink = data_sink()
    transformer = data_transformer(lambda x: x ** 2, sink)
    filter_coro = data_filter(lambda x: isinstance(x, (int, float)) and x > 0, transformer)
    source = data_source(filter_coro)
    
    # 发送测试数据
    test_data = [1, -2, 3, "hello", 4, 0, 5, -1, 6]
    
    print("\n开始数据处理:")
    for data in test_data:
        print(f"\n输入数据: {data}")
        source.send(data)
    
    # 关闭管道
    print("\n关闭管道:")
    source.close()

coroutine_pipeline()
```

### 分支管道

```python
def branching_pipeline():
    """分支管道演示"""
    print("\n=== 分支管道 ===")
    
    def coroutine(func):
        """协程装饰器"""
        def wrapper(*args, **kwargs):
            gen = func(*args, **kwargs)
            next(gen)
            return gen
        return wrapper
    
    @coroutine
    def broadcaster(*targets):
        """广播器 - 将数据发送给多个目标"""
        print(f"  广播器启动，目标数量: {len(targets)}")
        
        try:
            while True:
                data = yield
                if data is not None:
                    print(f"  广播数据: {data}")
                    for target in targets:
                        target.send(data)
        except GeneratorExit:
            print("  广播器关闭")
            for target in targets:
                target.close()
    
    @coroutine
    def number_processor(name):
        """数字处理器"""
        print(f"  {name}处理器启动")
        
        try:
            while True:
                data = yield
                if isinstance(data, (int, float)):
                    if name == "平方":
                        result = data ** 2
                    elif name == "立方":
                        result = data ** 3
                    elif name == "双倍":
                        result = data * 2
                    else:
                        result = data
                    
                    print(f"  {name}处理器: {data} -> {result}")
        except GeneratorExit:
            print(f"  {name}处理器关闭")
    
    @coroutine
    def string_processor():
        """字符串处理器"""
        print("  字符串处理器启动")
        
        try:
            while True:
                data = yield
                if isinstance(data, str):
                    result = data.upper()
                    print(f"  字符串处理器: {data} -> {result}")
        except GeneratorExit:
            print("  字符串处理器关闭")
    
    @coroutine
    def conditional_router(condition_func, true_target, false_target):
        """条件路由器"""
        print("  条件路由器启动")
        
        try:
            while True:
                data = yield
                if data is not None:
                    if condition_func(data):
                        print(f"  路由到真分支: {data}")
                        true_target.send(data)
                    else:
                        print(f"  路由到假分支: {data}")
                        false_target.send(data)
        except GeneratorExit:
            print("  条件路由器关闭")
            true_target.close()
            false_target.close()
    
    # 构建分支管道
    square_proc = number_processor("平方")
    cube_proc = number_processor("立方")
    double_proc = number_processor("双倍")
    string_proc = string_processor()
    
    # 数字广播器
    number_broadcaster = broadcaster(square_proc, cube_proc, double_proc)
    
    # 条件路由器：数字 vs 字符串
    def is_number(x):
        return isinstance(x, (int, float))
    
    router = conditional_router(is_number, number_broadcaster, string_proc)
    
    # 测试数据
    test_data = [3, "hello", 5, "world", 2, "python"]
    
    print("\n开始分支处理:")
    for data in test_data:
        print(f"\n输入数据: {data}")
        router.send(data)
    
    # 关闭管道
    print("\n关闭分支管道:")
    router.close()

branching_pipeline()
```

## 协程状态机

### 简单状态机

```python
def coroutine_state_machine():
    """协程状态机演示"""
    print("\n=== 协程状态机 ===")
    
    def coroutine(func):
        """协程装饰器"""
        def wrapper(*args, **kwargs):
            gen = func(*args, **kwargs)
            next(gen)
            return gen
        return wrapper
    
    @coroutine
    def traffic_light_fsm():
        """交通灯状态机"""
        print("  交通灯状态机启动")
        
        # 状态定义
        states = {
            'red': {'duration': 30, 'next': 'green', 'action': '停止'},
            'green': {'duration': 25, 'next': 'yellow', 'action': '通行'},
            'yellow': {'duration': 5, 'next': 'red', 'action': '准备停止'}
        }
        
        current_state = 'red'
        remaining_time = states[current_state]['duration']
        
        try:
            while True:
                command = yield {
                    'state': current_state,
                    'action': states[current_state]['action'],
                    'remaining_time': remaining_time
                }
                
                if command == 'tick':
                    # 时间流逝
                    remaining_time -= 1
                    print(f"  {current_state.upper()} - {states[current_state]['action']} (剩余: {remaining_time}s)")
                    
                    if remaining_time <= 0:
                        # 状态转换
                        old_state = current_state
                        current_state = states[current_state]['next']
                        remaining_time = states[current_state]['duration']
                        print(f"  状态转换: {old_state.upper()} -> {current_state.upper()}")
                
                elif command == 'emergency':
                    # 紧急情况 - 切换到红灯
                    print(f"  紧急情况！从 {current_state.upper()} 切换到 RED")
                    current_state = 'red'
                    remaining_time = states[current_state]['duration']
                
                elif command == 'status':
                    # 查询状态
                    print(f"  当前状态: {current_state.upper()} - {states[current_state]['action']} (剩余: {remaining_time}s)")
                
                elif command == 'reset':
                    # 重置
                    print("  重置交通灯")
                    current_state = 'red'
                    remaining_time = states[current_state]['duration']
        
        except GeneratorExit:
            print("  交通灯状态机关闭")
    
    # 创建交通灯状态机
    traffic_light = traffic_light_fsm()
    
    # 模拟交通灯运行
    print("\n模拟交通灯运行:")
    
    # 运行30个时间单位
    for i in range(35):
        if i == 15:
            # 模拟紧急情况
            status = traffic_light.send('emergency')
        elif i == 20:
            # 查询状态
            status = traffic_light.send('status')
        else:
            # 正常时间流逝
            status = traffic_light.send('tick')
        
        # 每5个时间单位显示一次状态
        if i % 5 == 0:
            print(f"  第{i}秒状态: {status}")
    
    # 关闭状态机
    traffic_light.close()

coroutine_state_machine()
```

### 复杂状态机

```python
def complex_state_machine():
    """复杂状态机演示"""
    print("\n=== 复杂状态机 - 订单处理 ===")
    
    def coroutine(func):
        """协程装饰器"""
        def wrapper(*args, **kwargs):
            gen = func(*args, **kwargs)
            next(gen)
            return gen
        return wrapper
    
    @coroutine
    def order_processing_fsm(order_id):
        """订单处理状态机"""
        print(f"  订单 {order_id} 处理状态机启动")
        
        # 状态转换表
        transitions = {
            'pending': {
                'confirm': 'confirmed',
                'cancel': 'cancelled'
            },
            'confirmed': {
                'pay': 'paid',
                'cancel': 'cancelled'
            },
            'paid': {
                'ship': 'shipped',
                'refund': 'refunded'
            },
            'shipped': {
                'deliver': 'delivered',
                'return': 'returned'
            },
            'delivered': {
                'complete': 'completed',
                'return': 'returned'
            },
            'returned': {
                'refund': 'refunded',
                'reship': 'shipped'
            },
            'cancelled': {},  # 终态
            'completed': {},  # 终态
            'refunded': {}    # 终态
        }
        
        # 状态描述
        state_descriptions = {
            'pending': '等待确认',
            'confirmed': '已确认',
            'paid': '已付款',
            'shipped': '已发货',
            'delivered': '已送达',
            'returned': '已退货',
            'cancelled': '已取消',
            'completed': '已完成',
            'refunded': '已退款'
        }
        
        current_state = 'pending'
        history = [('pending', '订单创建')]
        
        try:
            while True:
                action = yield {
                    'order_id': order_id,
                    'current_state': current_state,
                    'description': state_descriptions[current_state],
                    'available_actions': list(transitions[current_state].keys()),
                    'history': history[-3:]  # 最近3个状态
                }
                
                if action in transitions[current_state]:
                    old_state = current_state
                    current_state = transitions[current_state][action]
                    
                    # 记录状态变化
                    history.append((current_state, f"执行动作: {action}"))
                    
                    print(f"  订单 {order_id}: {old_state} --[{action}]--> {current_state}")
                    
                    # 检查是否到达终态
                    if not transitions[current_state]:
                        print(f"  订单 {order_id} 到达终态: {current_state}")
                        break
                
                elif action == 'status':
                    print(f"  订单 {order_id} 当前状态: {current_state} ({state_descriptions[current_state]})")
                    print(f"  可用操作: {list(transitions[current_state].keys())}")
                
                elif action == 'history':
                    print(f"  订单 {order_id} 状态历史:")
                    for state, desc in history:
                        print(f"    - {state}: {desc}")
                
                else:
                    print(f"  订单 {order_id} 无效操作: {action}")
                    print(f"  当前状态 {current_state} 可用操作: {list(transitions[current_state].keys())}")
        
        except GeneratorExit:
            print(f"  订单 {order_id} 状态机关闭")
    
    # 创建多个订单状态机
    order1 = order_processing_fsm("ORD-001")
    order2 = order_processing_fsm("ORD-002")
    
    # 模拟订单1的正常流程
    print("\n模拟订单1正常流程:")
    order1_actions = ['confirm', 'pay', 'ship', 'deliver', 'complete']
    
    for action in order1_actions:
        print(f"\n执行操作: {action}")
        try:
            status = order1.send(action)
            print(f"状态: {status}")
        except StopIteration:
            print("订单1处理完成")
            break
    
    # 模拟订单2的异常流程
    print("\n\n模拟订单2异常流程:")
    order2_actions = ['confirm', 'pay', 'ship', 'return', 'refund']
    
    for action in order2_actions:
        print(f"\n执行操作: {action}")
        try:
            status = order2.send(action)
            print(f"状态: {status}")
        except StopIteration:
            print("订单2处理完成")
            break
    
    # 关闭状态机
    try:
        order1.close()
        order2.close()
    except:
        pass

complex_state_machine()
```

## 协程通信

### 协程间消息传递

```python
def coroutine_communication():
    """协程间通信演示"""
    print("\n=== 协程间通信 ===")
    
    def coroutine(func):
        """协程装饰器"""
        def wrapper(*args, **kwargs):
            gen = func(*args, **kwargs)
            next(gen)
            return gen
        return wrapper
    
    class MessageQueue:
        """简单消息队列"""
        def __init__(self):
            self.queues = {}
        
        def send_message(self, recipient, message):
            """发送消息"""
            if recipient not in self.queues:
                self.queues[recipient] = []
            self.queues[recipient].append(message)
            print(f"  消息队列: 发送给 {recipient} -> {message}")
        
        def get_messages(self, recipient):
            """获取消息"""
            messages = self.queues.get(recipient, [])
            self.queues[recipient] = []
            return messages
    
    # 全局消息队列
    message_queue = MessageQueue()
    
    @coroutine
    def worker_coroutine(name, message_queue):
        """工作协程"""
        print(f"  工作协程 {name} 启动")
        
        try:
            while True:
                command = yield
                
                if command == 'check_messages':
                    # 检查消息
                    messages = message_queue.get_messages(name)
                    if messages:
                        print(f"  {name} 收到消息: {messages}")
                        
                        # 处理消息
                        for msg in messages:
                            if msg['type'] == 'task':
                                result = f"任务 {msg['data']} 完成"
                                print(f"  {name} 处理任务: {msg['data']} -> {result}")
                                
                                # 发送结果给发送者
                                if 'sender' in msg:
                                    message_queue.send_message(
                                        msg['sender'],
                                        {'type': 'result', 'data': result, 'sender': name}
                                    )
                            
                            elif msg['type'] == 'result':
                                print(f"  {name} 收到结果: {msg['data']} (来自 {msg['sender']})")
                    else:
                        print(f"  {name} 无新消息")
                
                elif isinstance(command, dict) and command.get('action') == 'send':
                    # 发送消息给其他协程
                    recipient = command['to']
                    message = command['message']
                    message['sender'] = name
                    message_queue.send_message(recipient, message)
        
        except GeneratorExit:
            print(f"  工作协程 {name} 关闭")
    
    @coroutine
    def coordinator_coroutine(message_queue, workers):
        """协调器协程"""
        print("  协调器启动")
        task_counter = 0
        
        try:
            while True:
                command = yield
                
                if command == 'distribute_tasks':
                    # 分发任务给工作协程
                    tasks = [f"task-{i}" for i in range(task_counter, task_counter + 3)]
                    task_counter += 3
                    
                    for i, task in enumerate(tasks):
                        worker = workers[i % len(workers)]
                        message_queue.send_message(
                            worker,
                            {'type': 'task', 'data': task, 'sender': 'coordinator'}
                        )
                    
                    print(f"  协调器分发了 {len(tasks)} 个任务")
                
                elif command == 'check_messages':
                    # 检查消息
                    messages = message_queue.get_messages('coordinator')
                    if messages:
                        print(f"  协调器收到消息: {len(messages)} 条")
                        for msg in messages:
                            if msg['type'] == 'result':
                                print(f"  协调器收到结果: {msg['data']} (来自 {msg['sender']})")
        
        except GeneratorExit:
            print("  协调器关闭")
    
    # 创建协程
    workers = ['worker1', 'worker2', 'worker3']
    worker_coroutines = {}
    
    for worker in workers:
        worker_coroutines[worker] = worker_coroutine(worker, message_queue)
    
    coordinator = coordinator_coroutine(message_queue, workers)
    
    # 模拟协程通信
    print("\n开始协程通信模拟:")
    
    # 分发任务
    print("\n1. 分发任务")
    coordinator.send('distribute_tasks')
    
    # 让工作协程检查消息
    print("\n2. 工作协程检查消息")
    for worker in workers:
        worker_coroutines[worker].send('check_messages')
    
    # 协调器检查结果
    print("\n3. 协调器检查结果")
    coordinator.send('check_messages')
    
    # 工作协程之间直接通信
    print("\n4. 工作协程间直接通信")
    worker_coroutines['worker1'].send({
        'action': 'send',
        'to': 'worker2',
        'message': {'type': 'greeting', 'data': 'Hello from worker1'}
    })
    
    worker_coroutines['worker2'].send('check_messages')
    
    # 关闭所有协程
    print("\n关闭协程:")
    coordinator.close()
    for worker_coro in worker_coroutines.values():
        worker_coro.close()

coroutine_communication()
```

## 协程池

### 简单协程池

```python
def coroutine_pool():
    """协程池演示"""
    print("\n=== 协程池 ===")
    
    def coroutine(func):
        """协程装饰器"""
        def wrapper(*args, **kwargs):
            gen = func(*args, **kwargs)
            next(gen)
            return gen
        return wrapper
    
    class CoroutinePool:
        """协程池"""
        def __init__(self, size=3):
            self.size = size
            self.workers = []
            self.task_queue = []
            self.results = []
            self.active_tasks = 0
        
        def create_workers(self):
            """创建工作协程"""
            @coroutine
            def worker(worker_id):
                print(f"    工作协程 {worker_id} 启动")
                
                try:
                    while True:
                        task = yield
                        if task is None:
                            continue
                        
                        if task == 'shutdown':
                            print(f"    工作协程 {worker_id} 关闭")
                            break
                        
                        # 处理任务
                        task_id = task.get('id')
                        task_data = task.get('data')
                        task_func = task.get('func')
                        
                        print(f"    工作协程 {worker_id} 处理任务 {task_id}")
                        
                        try:
                            result = task_func(task_data)
                            self.results.append({
                                'task_id': task_id,
                                'worker_id': worker_id,
                                'result': result,
                                'status': 'success'
                            })
                            print(f"    工作协程 {worker_id} 完成任务 {task_id}: {result}")
                        
                        except Exception as e:
                            self.results.append({
                                'task_id': task_id,
                                'worker_id': worker_id,
                                'error': str(e),
                                'status': 'error'
                            })
                            print(f"    工作协程 {worker_id} 任务 {task_id} 失败: {e}")
                        
                        self.active_tasks -= 1
                
                except GeneratorExit:
                    print(f"    工作协程 {worker_id} 被强制关闭")
            
            for i in range(self.size):
                self.workers.append(worker(f"W{i+1}"))
        
        def submit_task(self, task_id, func, data):
            """提交任务"""
            task = {
                'id': task_id,
                'func': func,
                'data': data
            }
            self.task_queue.append(task)
            print(f"  提交任务 {task_id}")
        
        def process_tasks(self):
            """处理任务队列"""
            worker_index = 0
            
            while self.task_queue:
                task = self.task_queue.pop(0)
                worker = self.workers[worker_index]
                
                print(f"  分配任务 {task['id']} 给工作协程 W{worker_index + 1}")
                worker.send(task)
                self.active_tasks += 1
                
                worker_index = (worker_index + 1) % len(self.workers)
        
        def wait_completion(self):
            """等待所有任务完成"""
            print(f"  等待 {self.active_tasks} 个任务完成...")
            
            # 简单的等待模拟（实际应用中可能需要更复杂的同步机制）
            import time
            while self.active_tasks > 0:
                time.sleep(0.1)  # 模拟等待
            
            print("  所有任务完成")
        
        def get_results(self):
            """获取结果"""
            return self.results.copy()
        
        def shutdown(self):
            """关闭协程池"""
            print("  关闭协程池")
            for worker in self.workers:
                worker.send('shutdown')
    
    # 定义任务函数
    def square_task(x):
        """平方任务"""
        return x ** 2
    
    def factorial_task(n):
        """阶乘任务"""
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def fibonacci_task(n):
        """斐波那契任务"""
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def error_task(x):
        """错误任务"""
        if x < 0:
            raise ValueError("负数不支持")
        return x * 10
    
    # 创建协程池
    pool = CoroutinePool(size=3)
    pool.create_workers()
    
    # 提交任务
    print("\n提交任务到协程池:")
    tasks = [
        ('task-1', square_task, 5),
        ('task-2', factorial_task, 6),
        ('task-3', fibonacci_task, 10),
        ('task-4', square_task, 8),
        ('task-5', error_task, -1),  # 会出错
        ('task-6', fibonacci_task, 15),
        ('task-7', factorial_task, 4),
        ('task-8', error_task, 3)
    ]
    
    for task_id, func, data in tasks:
        pool.submit_task(task_id, func, data)
    
    # 处理任务
    print("\n开始处理任务:")
    pool.process_tasks()
    
    # 等待完成
    pool.wait_completion()
    
    # 获取结果
    print("\n任务结果:")
    results = pool.get_results()
    for result in results:
        if result['status'] == 'success':
            print(f"  {result['task_id']} (W{result['worker_id'][-1]}): {result['result']}")
        else:
            print(f"  {result['task_id']} (W{result['worker_id'][-1]}): 错误 - {result['error']}")
    
    # 关闭协程池
    pool.shutdown()

coroutine_pool()
```

## 学习要点总结

### 核心概念

1. **协程定义**：可以暂停和恢复执行的函数
2. **协作式多任务**：函数主动让出控制权
3. **双向通信**：使用send()方法实现数据交换
4. **状态保持**：协程可以保持局部状态

### 重要特性

- **轻量级**：比线程更轻量，开销更小
- **无锁编程**：避免了线程同步问题
- **可组合性**：可以构建复杂的处理管道
- **异常处理**：支持异常的传播和处理

### 应用场景

- **数据处理管道**：构建流式数据处理系统
- **状态机**：实现复杂的状态转换逻辑
- **事件处理**：处理异步事件和消息
- **协作式任务**：实现任务间的协作

### 设计模式

1. **管道模式**：数据在协程间流动
2. **生产者-消费者**：协程间的数据传递
3. **状态机模式**：使用协程实现状态转换
4. **观察者模式**：事件通知和处理

### 最佳实践

1. **预激活**：使用装饰器自动预激活协程
2. **异常处理**：合理处理协程中的异常
3. **资源管理**：确保协程正确关闭
4. **错误恢复**：设计健壮的错误处理机制

### 注意事项

1. **调试复杂性**：协程的执行流程可能难以跟踪
2. **异常传播**：理解异常在协程中的传播
3. **内存管理**：避免协程引用循环导致内存泄漏
4. **性能考虑**：协程切换也有开销

## 练习建议

1. **基础练习**：实现简单的协程通信
2. **管道练习**：构建数据处理管道
3. **状态机练习**：使用协程实现状态机
4. **实际项目**：在真实项目中应用协程

协程是Python异步编程的基础，虽然现代Python更多使用async/await语法，但理解基于生成器的协程对于深入理解异步编程原理非常重要。