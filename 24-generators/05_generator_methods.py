#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成器方法：send()、throw()、close()

本模块介绍：
1. send()方法：向生成器发送值
2. throw()方法：向生成器抛出异常
3. close()方法：关闭生成器
4. 生成器的双向通信
5. 异常处理和资源清理
"""

import sys
import traceback
from typing import Generator, Any

# 1. send()方法的基本使用
print("=== 1. send()方法的基本使用 ===")
print("send()方法可以向生成器发送值，实现双向通信")
print()

def echo_generator():
    """回声生成器，演示send()方法"""
    print("回声生成器启动")
    
    while True:
        # yield表达式可以接收send()发送的值
        received = yield "等待输入..."
        if received is None:
            print("收到None值")
        else:
            print(f"收到消息: {received}")
            yield f"回声: {received}"

print("创建回声生成器:")
echo_gen = echo_generator()

# 首次调用必须使用next()或send(None)
first_response = next(echo_gen)
print(f"首次响应: {first_response}")
print()

print("使用send()发送消息:")
messages = ["Hello", "World", "Python", "Generator"]
for msg in messages:
    response = echo_gen.send(msg)
    print(f"发送: {msg} -> 响应: {response}")
    
    # 获取下一个状态
    try:
        next_state = next(echo_gen)
        print(f"下一状态: {next_state}")
    except StopIteration:
        break
    print("---")
print()

# 2. send()方法的高级应用
print("=== 2. send()方法的高级应用 ===")

def calculator_generator():
    """计算器生成器，支持多种操作"""
    result = 0
    print(f"计算器启动，初始值: {result}")
    
    while True:
        # 接收操作指令
        operation = yield result
        
        if operation is None:
            continue
            
        try:
            if isinstance(operation, dict):
                op = operation.get('op')
                value = operation.get('value', 0)
                
                if op == 'add':
                    result += value
                    print(f"执行加法: {result - value} + {value} = {result}")
                elif op == 'subtract':
                    result -= value
                    print(f"执行减法: {result + value} - {value} = {result}")
                elif op == 'multiply':
                    old_result = result
                    result *= value
                    print(f"执行乘法: {old_result} × {value} = {result}")
                elif op == 'divide':
                    if value != 0:
                        old_result = result
                        result /= value
                        print(f"执行除法: {old_result} ÷ {value} = {result}")
                    else:
                        print("错误: 除数不能为零")
                elif op == 'reset':
                    result = 0
                    print("重置计算器")
                else:
                    print(f"未知操作: {op}")
            else:
                print(f"无效操作格式: {operation}")
                
        except Exception as e:
            print(f"计算错误: {e}")

print("计算器生成器演示:")
calc_gen = calculator_generator()
initial_value = next(calc_gen)
print(f"初始值: {initial_value}")
print()

# 执行一系列计算
operations = [
    {'op': 'add', 'value': 10},
    {'op': 'multiply', 'value': 3},
    {'op': 'subtract', 'value': 5},
    {'op': 'divide', 'value': 2.5},
    {'op': 'reset'}
]

for op in operations:
    result = calc_gen.send(op)
    print(f"当前结果: {result}")
    print("---")
print()

# 3. throw()方法的使用
print("=== 3. throw()方法的使用 ===")
print("throw()方法可以向生成器抛出异常")
print()

def exception_handler_generator():
    """异常处理生成器"""
    count = 0
    print("异常处理生成器启动")
    
    try:
        while True:
            try:
                count += 1
                print(f"第{count}次迭代开始")
                
                # 这里可能接收到异常
                value = yield f"迭代{count}完成"
                
                if value is not None:
                    print(f"收到值: {value}")
                    
            except ValueError as e:
                print(f"捕获到ValueError: {e}")
                yield f"已处理ValueError，继续执行"
                
            except TypeError as e:
                print(f"捕获到TypeError: {e}")
                yield f"已处理TypeError，继续执行"
                
            except Exception as e:
                print(f"捕获到其他异常: {e}")
                yield f"已处理异常: {type(e).__name__}"
                
    except GeneratorExit:
        print("生成器正在关闭")
        
    finally:
        print("异常处理生成器清理完成")

print("异常处理演示:")
exc_gen = exception_handler_generator()

# 正常迭代
print(f"正常迭代: {next(exc_gen)}")
print()

# 抛出不同类型的异常
exceptions_to_throw = [
    ValueError("这是一个值错误"),
    TypeError("这是一个类型错误"),
    RuntimeError("这是一个运行时错误")
]

for exc in exceptions_to_throw:
    try:
        response = exc_gen.throw(type(exc), exc, exc.__traceback__)
        print(f"异常处理响应: {response}")
        
        # 继续下一次迭代
        next_response = next(exc_gen)
        print(f"继续迭代: {next_response}")
        
    except StopIteration:
        print("生成器已停止")
        break
    print("---")
print()

# 4. close()方法的使用
print("=== 4. close()方法的使用 ===")
print("close()方法用于关闭生成器并触发清理")
print()

def resource_manager_generator():
    """资源管理生成器"""
    resources = []
    
    try:
        print("资源管理器启动")
        
        while True:
            command = yield f"管理{len(resources)}个资源"
            
            if command is None:
                continue
                
            if isinstance(command, dict):
                action = command.get('action')
                resource = command.get('resource')
                
                if action == 'acquire':
                    resources.append(resource)
                    print(f"获取资源: {resource}")
                    
                elif action == 'release':
                    if resource in resources:
                        resources.remove(resource)
                        print(f"释放资源: {resource}")
                    else:
                        print(f"资源不存在: {resource}")
                        
                elif action == 'list':
                    print(f"当前资源: {resources}")
                    
    except GeneratorExit:
        print("收到关闭信号，开始清理资源")
        for resource in resources:
            print(f"清理资源: {resource}")
        resources.clear()
        print("所有资源已清理")
        
    finally:
        print("资源管理器已关闭")

print("资源管理演示:")
resource_gen = resource_manager_generator()
print(f"初始状态: {next(resource_gen)}")
print()

# 管理资源
resource_commands = [
    {'action': 'acquire', 'resource': 'database_connection'},
    {'action': 'acquire', 'resource': 'file_handle'},
    {'action': 'acquire', 'resource': 'network_socket'},
    {'action': 'list'},
    {'action': 'release', 'resource': 'file_handle'},
    {'action': 'list'}
]

for cmd in resource_commands:
    response = resource_gen.send(cmd)
    print(f"响应: {response}")
    print("---")

print("\n手动关闭资源管理器:")
resource_gen.close()
print()

# 5. 生成器方法的组合使用
print("=== 5. 生成器方法的组合使用 ===")

def state_machine_generator():
    """状态机生成器，演示所有方法的组合使用"""
    state = "idle"
    data = {}
    
    try:
        print(f"状态机启动，初始状态: {state}")
        
        while True:
            try:
                # 返回当前状态并等待指令
                command = yield {
                    'state': state,
                    'data': data.copy(),
                    'message': f"当前状态: {state}"
                }
                
                if command is None:
                    continue
                    
                # 处理状态转换
                if isinstance(command, dict):
                    action = command.get('action')
                    payload = command.get('payload', {})
                    
                    if action == 'start' and state == 'idle':
                        state = 'running'
                        data.update(payload)
                        print(f"状态转换: idle -> running")
                        
                    elif action == 'pause' and state == 'running':
                        state = 'paused'
                        print(f"状态转换: running -> paused")
                        
                    elif action == 'resume' and state == 'paused':
                        state = 'running'
                        print(f"状态转换: paused -> running")
                        
                    elif action == 'stop':
                        state = 'idle'
                        data.clear()
                        print(f"状态转换: {state} -> idle")
                        
                    elif action == 'update' and state == 'running':
                        data.update(payload)
                        print(f"更新数据: {payload}")
                        
                    else:
                        print(f"无效的状态转换: {action} in {state}")
                        
            except ValueError as e:
                print(f"状态机错误: {e}")
                state = 'error'
                
            except Exception as e:
                print(f"未知错误: {e}")
                state = 'error'
                
    except GeneratorExit:
        print("状态机关闭")
        
    finally:
        print(f"状态机最终状态: {state}")
        print(f"最终数据: {data}")

print("状态机演示:")
state_machine = state_machine_generator()
initial_state = next(state_machine)
print(f"初始状态: {initial_state}")
print()

# 状态机操作序列
state_commands = [
    {'action': 'start', 'payload': {'task': 'processing', 'priority': 'high'}},
    {'action': 'update', 'payload': {'progress': 50}},
    {'action': 'pause'},
    {'action': 'resume'},
    {'action': 'update', 'payload': {'progress': 100}}
]

for cmd in state_commands:
    try:
        response = state_machine.send(cmd)
        print(f"命令: {cmd}")
        print(f"响应: {response}")
        print("---")
    except Exception as e:
        print(f"执行错误: {e}")

# 测试异常处理
print("\n测试异常处理:")
try:
    state_machine.throw(ValueError, ValueError("模拟错误"), None)
    error_response = next(state_machine)
    print(f"错误后状态: {error_response}")
except StopIteration:
    print("状态机已停止")

# 关闭状态机
print("\n关闭状态机:")
state_machine.close()
print()

# 6. 生成器方法的实际应用场景
print("=== 6. 生成器方法的实际应用场景 ===")

def data_pipeline_generator():
    """数据处理管道生成器"""
    pipeline_state = {
        'processed': 0,
        'errors': 0,
        'filters': [],
        'transformers': []
    }
    
    try:
        print("数据管道启动")
        
        while True:
            try:
                # 接收数据或配置命令
                input_data = yield {
                    'status': 'ready',
                    'stats': pipeline_state.copy()
                }
                
                if input_data is None:
                    continue
                    
                if isinstance(input_data, dict):
                    if 'config' in input_data:
                        # 配置管道
                        config = input_data['config']
                        if 'filters' in config:
                            pipeline_state['filters'] = config['filters']
                            print(f"更新过滤器: {config['filters']}")
                        if 'transformers' in config:
                            pipeline_state['transformers'] = config['transformers']
                            print(f"更新转换器: {config['transformers']}")
                            
                    elif 'data' in input_data:
                        # 处理数据
                        data = input_data['data']
                        processed_data = data
                        
                        # 应用过滤器
                        for filter_func in pipeline_state['filters']:
                            if filter_func == 'positive':
                                processed_data = [x for x in processed_data if x > 0]
                            elif filter_func == 'even':
                                processed_data = [x for x in processed_data if x % 2 == 0]
                        
                        # 应用转换器
                        for transformer in pipeline_state['transformers']:
                            if transformer == 'square':
                                processed_data = [x ** 2 for x in processed_data]
                            elif transformer == 'double':
                                processed_data = [x * 2 for x in processed_data]
                        
                        pipeline_state['processed'] += len(processed_data)
                        
                        yield {
                            'status': 'processed',
                            'input': data,
                            'output': processed_data,
                            'stats': pipeline_state.copy()
                        }
                        
            except Exception as e:
                pipeline_state['errors'] += 1
                print(f"管道处理错误: {e}")
                yield {
                    'status': 'error',
                    'error': str(e),
                    'stats': pipeline_state.copy()
                }
                
    except GeneratorExit:
        print("数据管道关闭")
        print(f"最终统计: {pipeline_state}")

print("数据管道演示:")
pipeline = data_pipeline_generator()
status = next(pipeline)
print(f"管道状态: {status}")
print()

# 配置管道
config_response = pipeline.send({
    'config': {
        'filters': ['positive', 'even'],
        'transformers': ['square']
    }
})
print(f"配置响应: {config_response}")
print()

# 处理数据
test_datasets = [
    [-2, -1, 0, 1, 2, 3, 4, 5],
    [10, -5, 8, -3, 6, 7],
    [1, 3, 5, 7, 9]
]

for i, dataset in enumerate(test_datasets):
    print(f"处理数据集 {i+1}: {dataset}")
    
    # 发送数据
    result = pipeline.send({'data': dataset})
    print(f"处理结果: {result}")
    
    # 获取下一个状态
    next_status = next(pipeline)
    print(f"管道状态: {next_status}")
    print("---")

# 关闭管道
print("\n关闭数据管道:")
pipeline.close()
print()

print("=== 生成器方法学习完成 ===")
print("关键要点:")
print("1. send()方法实现生成器的双向通信")
print("2. throw()方法可以向生成器抛出异常")
print("3. close()方法关闭生成器并触发清理")
print("4. 首次启动生成器必须使用next()或send(None)")
print("5. 异常处理可以让生成器更加健壮")
print("6. 资源清理应该在finally块中进行")
print("7. 生成器方法组合使用可以实现复杂的交互逻辑")

if __name__ == "__main__":
    print("\n=== 运行完成 ===")
    print("本模块演示了生成器的send()、throw()、close()方法的使用")