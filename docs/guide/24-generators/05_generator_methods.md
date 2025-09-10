# 生成器方法：send()、throw()、close()

生成器不仅可以产生值，还可以接收值和处理异常。Python为生成器提供了三个重要的方法：`send()`、`throw()`和`close()`，这些方法使得生成器能够实现双向通信和异常处理，为协程编程奠定了基础。

## send() 方法

### 基本用法

`send()`方法允许向生成器发送值，这个值会成为当前yield表达式的返回值。

```python
def basic_send_demo():
    """send()方法基本演示"""
    print("=== send()方法基本用法 ===")
    
    def echo_generator():
        """回声生成器"""
        print("  生成器启动")
        
        while True:
            # yield表达式可以接收send()发送的值
            received = yield "等待输入..."
            print(f"  接收到: {received}")
            
            if received == 'quit':
                break
            
            yield f"回声: {received}"
    
    gen = echo_generator()
    
    # 首次调用必须使用next()或send(None)
    print("启动生成器:")
    response = next(gen)
    print(f"生成器响应: {response}")
    
    # 发送数据
    messages = ['Hello', 'World', 'Python', 'quit']
    
    for msg in messages:
        print(f"\n发送: {msg}")
        try:
            response = gen.send(msg)
            print(f"生成器响应: {response}")
            
            if msg != 'quit':
                # 获取回声
                echo = next(gen)
                print(f"回声响应: {echo}")
        except StopIteration:
            print("生成器已结束")
            break

basic_send_demo()
```

### 双向通信示例

```python
def bidirectional_communication():
    """双向通信示例"""
    print("\n=== 双向通信示例 ===")
    
    def calculator_generator():
        """计算器生成器"""
        result = 0
        print(f"  计算器启动，初始值: {result}")
        
        while True:
            # 接收操作指令
            operation = yield f"当前结果: {result}"
            
            if operation is None:
                continue
            
            if isinstance(operation, dict):
                op = operation.get('op')
                value = operation.get('value', 0)
                
                if op == 'add':
                    result += value
                    print(f"  执行加法: +{value} = {result}")
                elif op == 'subtract':
                    result -= value
                    print(f"  执行减法: -{value} = {result}")
                elif op == 'multiply':
                    result *= value
                    print(f"  执行乘法: ×{value} = {result}")
                elif op == 'divide':
                    if value != 0:
                        result /= value
                        print(f"  执行除法: ÷{value} = {result}")
                    else:
                        print(f"  错误: 除零操作")
                elif op == 'reset':
                    result = 0
                    print(f"  重置结果: {result}")
                elif op == 'quit':
                    print(f"  计算器关闭，最终结果: {result}")
                    break
    
    calc = calculator_generator()
    
    # 启动计算器
    status = next(calc)
    print(f"启动状态: {status}")
    
    # 执行一系列计算
    operations = [
        {'op': 'add', 'value': 10},
        {'op': 'multiply', 'value': 3},
        {'op': 'subtract', 'value': 5},
        {'op': 'divide', 'value': 2.5},
        {'op': 'reset'},
        {'op': 'add', 'value': 100},
        {'op': 'quit'}
    ]
    
    for op in operations:
        print(f"\n执行操作: {op}")
        try:
            status = calc.send(op)
            print(f"状态: {status}")
        except StopIteration:
            print("计算器已关闭")
            break

bidirectional_communication()
```

### 数据处理管道

```python
def data_processing_pipeline():
    """数据处理管道示例"""
    print("\n=== 数据处理管道 ===")
    
    def data_processor():
        """数据处理器生成器"""
        processed_count = 0
        total_sum = 0
        
        print("  数据处理器启动")
        
        while True:
            # 接收数据
            data = yield {
                'processed_count': processed_count,
                'total_sum': total_sum,
                'average': total_sum / processed_count if processed_count > 0 else 0
            }
            
            if data is None:
                continue
            
            if isinstance(data, (int, float)):
                processed_count += 1
                total_sum += data
                print(f"  处理数据: {data}, 累计: {processed_count}个, 总和: {total_sum}")
            elif data == 'reset':
                processed_count = 0
                total_sum = 0
                print("  重置统计数据")
            elif data == 'stop':
                print(f"  处理完成，共处理{processed_count}个数据")
                break
    
    processor = data_processor()
    
    # 启动处理器
    stats = next(processor)
    print(f"初始统计: {stats}")
    
    # 发送数据进行处理
    data_stream = [1, 2, 3, 4, 5, 'reset', 10, 20, 30, 'stop']
    
    for data in data_stream:
        print(f"\n发送数据: {data}")
        try:
            stats = processor.send(data)
            print(f"当前统计: {stats}")
        except StopIteration:
            print("数据处理器已停止")
            break

data_processing_pipeline()
```

## throw() 方法

### 基本异常处理

`throw()`方法允许向生成器发送异常，生成器可以捕获并处理这些异常。

```python
def basic_throw_demo():
    """throw()方法基本演示"""
    print("\n=== throw()方法基本用法 ===")
    
    def error_handling_generator():
        """错误处理生成器"""
        count = 0
        
        while True:
            try:
                print(f"  等待数据... (计数: {count})")
                data = yield f"准备接收第{count + 1}个数据"
                
                if data is None:
                    continue
                
                # 模拟数据处理
                if isinstance(data, (int, float)):
                    result = data * 2
                    count += 1
                    print(f"  处理成功: {data} × 2 = {result}")
                    yield f"处理结果: {result}"
                else:
                    raise ValueError(f"无效的数据类型: {type(data)}")
                    
            except ValueError as e:
                print(f"  捕获到ValueError: {e}")
                yield f"错误: {e}"
            except TypeError as e:
                print(f"  捕获到TypeError: {e}")
                yield f"类型错误: {e}"
            except Exception as e:
                print(f"  捕获到其他异常: {e}")
                yield f"未知错误: {e}"
    
    gen = error_handling_generator()
    
    # 启动生成器
    status = next(gen)
    print(f"启动状态: {status}")
    
    # 正常发送数据
    print("\n发送正常数据: 5")
    status = gen.send(5)
    print(f"状态: {status}")
    result = next(gen)
    print(f"结果: {result}")
    
    # 使用throw()发送异常
    print("\n使用throw()发送ValueError:")
    try:
        response = gen.throw(ValueError, "这是一个测试异常")
        print(f"异常处理响应: {response}")
    except StopIteration:
        print("生成器已结束")
    
    # 继续正常操作
    print("\n继续正常操作:")
    status = next(gen)
    print(f"状态: {status}")
    
    # 发送无效数据类型
    print("\n发送无效数据: 'invalid'")
    status = gen.send('invalid')
    print(f"状态: {status}")
    error_response = next(gen)
    print(f"错误响应: {error_response}")

basic_throw_demo()
```

### 异常传播和处理

```python
def exception_propagation():
    """异常传播和处理"""
    print("\n=== 异常传播和处理 ===")
    
    def nested_generator():
        """嵌套生成器异常处理"""
        try:
            print("  内层生成器启动")
            
            for i in range(5):
                try:
                    print(f"  内层循环 {i}")
                    data = yield f"内层-{i}"
                    
                    if data == 'inner_error':
                        raise RuntimeError("内层生成器错误")
                    
                    print(f"  内层接收: {data}")
                    
                except RuntimeError as e:
                    print(f"  内层捕获RuntimeError: {e}")
                    yield f"内层错误处理: {e}"
                    
        except Exception as e:
            print(f"  内层捕获其他异常: {e}")
            yield f"内层异常: {e}"
        
        print("  内层生成器结束")
    
    def outer_generator():
        """外层生成器"""
        try:
            print("外层生成器启动")
            inner_gen = nested_generator()
            
            # 启动内层生成器
            inner_status = next(inner_gen)
            
            while True:
                try:
                    print(f"外层状态: {inner_status}")
                    outer_data = yield inner_status
                    
                    if outer_data == 'outer_error':
                        raise ValueError("外层生成器错误")
                    
                    # 转发给内层生成器
                    inner_status = inner_gen.send(outer_data)
                    
                except ValueError as e:
                    print(f"外层捕获ValueError: {e}")
                    yield f"外层错误处理: {e}"
                    inner_status = next(inner_gen)
                except StopIteration:
                    print("内层生成器已结束")
                    break
                    
        except Exception as e:
            print(f"外层捕获其他异常: {e}")
            return f"外层异常结束: {e}"
    
    gen = outer_generator()
    
    # 测试异常处理
    test_data = [
        "正常数据1",
        "inner_error",  # 触发内层异常
        "正常数据2", 
        "outer_error",  # 触发外层异常
        "正常数据3"
    ]
    
    status = next(gen)
    
    for data in test_data:
        print(f"\n发送数据: {data}")
        try:
            status = gen.send(data)
            print(f"响应: {status}")
        except StopIteration as e:
            print(f"生成器结束: {e.value}")
            break

exception_propagation()
```

### 自定义异常处理

```python
def custom_exception_handling():
    """自定义异常处理"""
    print("\n=== 自定义异常处理 ===")
    
    # 自定义异常类
    class ProcessingError(Exception):
        def __init__(self, message, error_code=None):
            super().__init__(message)
            self.error_code = error_code
    
    class ValidationError(Exception):
        def __init__(self, message, field=None):
            super().__init__(message)
            self.field = field
    
    def robust_processor():
        """健壮的处理器生成器"""
        error_count = 0
        success_count = 0
        
        while True:
            try:
                data = yield {
                    'status': 'ready',
                    'success_count': success_count,
                    'error_count': error_count
                }
                
                if data is None:
                    continue
                
                # 数据验证
                if not isinstance(data, dict):
                    raise ValidationError("数据必须是字典格式", "type")
                
                if 'value' not in data:
                    raise ValidationError("缺少必需字段'value'", "value")
                
                value = data['value']
                
                # 数据处理
                if not isinstance(value, (int, float)):
                    raise ProcessingError("值必须是数字", "INVALID_TYPE")
                
                if value < 0:
                    raise ProcessingError("值不能为负数", "NEGATIVE_VALUE")
                
                # 成功处理
                result = value ** 2
                success_count += 1
                print(f"  处理成功: {value}² = {result}")
                
                yield {
                    'status': 'success',
                    'result': result,
                    'success_count': success_count,
                    'error_count': error_count
                }
                
            except ValidationError as e:
                error_count += 1
                print(f"  验证错误: {e} (字段: {e.field})")
                yield {
                    'status': 'validation_error',
                    'error': str(e),
                    'field': e.field,
                    'success_count': success_count,
                    'error_count': error_count
                }
                
            except ProcessingError as e:
                error_count += 1
                print(f"  处理错误: {e} (错误码: {e.error_code})")
                yield {
                    'status': 'processing_error',
                    'error': str(e),
                    'error_code': e.error_code,
                    'success_count': success_count,
                    'error_count': error_count
                }
    
    processor = robust_processor()
    
    # 启动处理器
    status = next(processor)
    print(f"初始状态: {status}")
    
    # 测试数据
    test_cases = [
        {'value': 5},           # 正常数据
        {'value': -3},          # 负数错误
        {'value': 'invalid'},   # 类型错误
        {'name': 'test'},       # 缺少字段
        "not_dict",             # 格式错误
        {'value': 10}           # 正常数据
    ]
    
    for i, test_data in enumerate(test_cases):
        print(f"\n测试用例 {i+1}: {test_data}")
        try:
            status = processor.send(test_data)
            print(f"处理状态: {status}")
            
            if status['status'] == 'success':
                # 获取下一个状态
                next_status = next(processor)
                print(f"下一状态: {next_status}")
                
        except StopIteration:
            print("处理器已结束")
            break
    
    # 使用throw()方法发送异常
    print("\n使用throw()发送自定义异常:")
    try:
        response = processor.throw(ProcessingError, "外部强制错误", "EXTERNAL_ERROR")
        print(f"异常处理响应: {response}")
    except StopIteration:
        print("处理器已结束")

custom_exception_handling()
```

## close() 方法

### 基本关闭操作

`close()`方法用于关闭生成器，它会在生成器的当前yield点抛出GeneratorExit异常。

```python
def basic_close_demo():
    """close()方法基本演示"""
    print("\n=== close()方法基本用法 ===")
    
    def closable_generator():
        """可关闭的生成器"""
        try:
            print("  生成器启动")
            count = 0
            
            while True:
                print(f"  生成第{count + 1}个值")
                yield f"值-{count}"
                count += 1
                
        except GeneratorExit:
            print("  接收到GeneratorExit，执行清理操作")
            # 执行清理操作
            print("  清理完成")
            raise  # 重新抛出GeneratorExit
        finally:
            print("  生成器最终清理")
    
    gen = closable_generator()
    
    # 获取几个值
    print("获取前3个值:")
    for i in range(3):
        value = next(gen)
        print(f"  获取到: {value}")
    
    # 关闭生成器
    print("\n关闭生成器:")
    gen.close()
    
    # 尝试继续使用已关闭的生成器
    print("\n尝试使用已关闭的生成器:")
    try:
        next(gen)
    except StopIteration:
        print("  生成器已关闭，抛出StopIteration")

basic_close_demo()
```

### 资源管理

```python
def resource_management():
    """资源管理示例"""
    print("\n=== 资源管理示例 ===")
    
    class MockFile:
        """模拟文件对象"""
        def __init__(self, filename):
            self.filename = filename
            self.is_open = False
        
        def open(self):
            print(f"    打开文件: {self.filename}")
            self.is_open = True
        
        def close(self):
            if self.is_open:
                print(f"    关闭文件: {self.filename}")
                self.is_open = False
        
        def read_line(self):
            if self.is_open:
                return f"来自{self.filename}的数据"
            return None
    
    def file_reader_generator(filename):
        """文件读取生成器"""
        file_obj = MockFile(filename)
        
        try:
            print(f"  初始化文件读取器: {filename}")
            file_obj.open()
            
            line_count = 0
            while line_count < 5:  # 模拟读取5行
                line = file_obj.read_line()
                if line:
                    line_count += 1
                    yield f"第{line_count}行: {line}"
                else:
                    break
                    
        except GeneratorExit:
            print(f"  接收到关闭信号，清理资源")
            raise
        finally:
            print(f"  执行最终清理")
            file_obj.close()
    
    # 正常使用
    print("正常使用文件读取器:")
    reader1 = file_reader_generator("data1.txt")
    
    for i, line in enumerate(reader1):
        print(f"  {line}")
        if i >= 2:  # 只读取前3行
            break
    
    print("\n手动关闭读取器:")
    reader1.close()
    
    # 异常情况下的资源清理
    print("\n异常情况下的资源清理:")
    reader2 = file_reader_generator("data2.txt")
    
    try:
        line1 = next(reader2)
        print(f"  {line1}")
        
        # 模拟异常
        raise RuntimeError("模拟异常")
        
    except RuntimeError as e:
        print(f"  捕获异常: {e}")
        print("  关闭资源")
        reader2.close()

resource_management()
```

### 上下文管理器集成

```python
def context_manager_integration():
    """上下文管理器集成"""
    print("\n=== 上下文管理器集成 ===")
    
    class GeneratorContextManager:
        """生成器上下文管理器"""
        def __init__(self, generator_func, *args, **kwargs):
            self.generator_func = generator_func
            self.args = args
            self.kwargs = kwargs
            self.generator = None
        
        def __enter__(self):
            print("  进入上下文管理器")
            self.generator = self.generator_func(*self.args, **self.kwargs)
            return self.generator
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("  退出上下文管理器")
            if self.generator:
                if exc_type:
                    print(f"  异常退出: {exc_type.__name__}: {exc_val}")
                    try:
                        self.generator.throw(exc_type, exc_val, exc_tb)
                    except (StopIteration, exc_type):
                        pass
                else:
                    print("  正常退出")
                
                self.generator.close()
            return False  # 不抑制异常
    
    def managed_generator(name):
        """被管理的生成器"""
        try:
            print(f"    {name} 生成器启动")
            count = 0
            
            while count < 10:
                yield f"{name}-{count}"
                count += 1
                
        except GeneratorExit:
            print(f"    {name} 接收到关闭信号")
            raise
        except Exception as e:
            print(f"    {name} 处理异常: {e}")
            raise
        finally:
            print(f"    {name} 执行清理")
    
    # 正常使用
    print("正常使用上下文管理器:")
    with GeneratorContextManager(managed_generator, "正常") as gen:
        for i, value in enumerate(gen):
            print(f"  获取: {value}")
            if i >= 2:
                break
    
    # 异常情况
    print("\n异常情况下的上下文管理器:")
    try:
        with GeneratorContextManager(managed_generator, "异常") as gen:
            value1 = next(gen)
            print(f"  获取: {value1}")
            
            # 触发异常
            raise ValueError("测试异常")
            
    except ValueError as e:
        print(f"  外部捕获异常: {e}")

context_manager_integration()
```

## 综合应用示例

### 协程式任务处理器

```python
def coroutine_task_processor():
    """协程式任务处理器"""
    print("\n=== 协程式任务处理器 ===")
    
    def task_processor():
        """任务处理协程"""
        tasks_completed = 0
        tasks_failed = 0
        
        try:
            print("  任务处理器启动")
            
            while True:
                # 等待任务
                task = yield {
                    'status': 'waiting',
                    'completed': tasks_completed,
                    'failed': tasks_failed
                }
                
                if task is None:
                    continue
                
                if task == 'shutdown':
                    print("  接收到关闭指令")
                    break
                
                # 处理任务
                try:
                    task_id = task.get('id', 'unknown')
                    task_type = task.get('type', 'default')
                    task_data = task.get('data', {})
                    
                    print(f"  处理任务 {task_id} (类型: {task_type})")
                    
                    # 模拟任务处理
                    if task_type == 'error':
                        raise RuntimeError(f"任务 {task_id} 处理失败")
                    
                    # 任务成功
                    tasks_completed += 1
                    result = f"任务 {task_id} 完成"
                    
                    yield {
                        'status': 'completed',
                        'task_id': task_id,
                        'result': result,
                        'completed': tasks_completed,
                        'failed': tasks_failed
                    }
                    
                except Exception as e:
                    tasks_failed += 1
                    print(f"  任务处理失败: {e}")
                    
                    yield {
                        'status': 'failed',
                        'task_id': task.get('id', 'unknown'),
                        'error': str(e),
                        'completed': tasks_completed,
                        'failed': tasks_failed
                    }
                    
        except GeneratorExit:
            print(f"  任务处理器关闭，完成: {tasks_completed}, 失败: {tasks_failed}")
            raise
        finally:
            print("  任务处理器清理完成")
    
    processor = task_processor()
    
    # 启动处理器
    status = next(processor)
    print(f"处理器状态: {status}")
    
    # 提交任务
    tasks = [
        {'id': 'task-1', 'type': 'normal', 'data': {'value': 10}},
        {'id': 'task-2', 'type': 'normal', 'data': {'value': 20}},
        {'id': 'task-3', 'type': 'error', 'data': {'value': 30}},  # 会失败
        {'id': 'task-4', 'type': 'normal', 'data': {'value': 40}},
        'shutdown'
    ]
    
    for task in tasks:
        print(f"\n提交任务: {task}")
        try:
            status = processor.send(task)
            print(f"处理状态: {status}")
            
            if status['status'] in ['completed', 'failed']:
                # 获取下一个等待状态
                next_status = next(processor)
                print(f"等待状态: {next_status}")
                
        except StopIteration:
            print("任务处理器已关闭")
            break
    
    # 强制关闭（如果还在运行）
    try:
        processor.close()
    except:
        pass

coroutine_task_processor()
```

## 学习要点总结

### 核心方法

1. **send(value)**：向生成器发送值，启动或恢复生成器执行
2. **throw(type, value, traceback)**：向生成器发送异常
3. **close()**：关闭生成器，发送GeneratorExit异常

### 重要概念

- **双向通信**：生成器不仅能产生值，还能接收值
- **异常处理**：生成器可以捕获和处理外部发送的异常
- **资源管理**：使用close()确保资源正确释放
- **协程基础**：这些方法是协程编程的基础

### 使用场景

- **数据处理管道**：构建可交互的数据处理流程
- **状态机**：实现复杂的状态转换逻辑
- **协程**：实现轻量级的并发处理
- **资源管理**：确保资源的正确获取和释放

### 最佳实践

1. **初始化**：首次调用生成器使用next()或send(None)
2. **异常处理**：合理处理GeneratorExit和其他异常
3. **资源清理**：在finally块中执行清理操作
4. **错误恢复**：设计合理的错误恢复机制

### 注意事项

1. **生成器状态**：了解生成器的不同状态
2. **异常传播**：理解异常在生成器中的传播机制
3. **资源泄漏**：确保生成器正确关闭以避免资源泄漏
4. **调试复杂性**：双向通信增加了调试的复杂性

## 练习建议

1. **基础练习**：实现简单的双向通信生成器
2. **异常练习**：练习使用throw()方法处理各种异常
3. **资源练习**：实现带资源管理的生成器
4. **协程练习**：使用这些方法实现简单的协程

这些方法是Python协程编程的基础，掌握它们对于理解异步编程和高级生成器应用至关重要。