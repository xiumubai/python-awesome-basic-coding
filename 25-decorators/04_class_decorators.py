#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
类装饰器的实现

类装饰器是使用类来实现装饰器功能的高级技术。与函数装饰器相比，
类装饰器可以更好地管理状态，提供更丰富的功能，并且代码结构更清晰。

学习要点：
1. 理解类装饰器的基本概念和实现方式
2. 掌握__call__方法在装饰器中的作用
3. 学会使用类装饰器管理状态
4. 了解类装饰器与函数装饰器的区别
5. 掌握类装饰器的高级应用场景
"""

import time
import functools
from datetime import datetime
import threading
from collections import defaultdict, deque
import weakref


def main():
    """主函数，演示类装饰器的实现"""
    print("=" * 50)
    print("类装饰器的实现")
    print("=" * 50)
    
    # 1. 基本的类装饰器
    print("\n1. 基本的类装饰器")
    print("-" * 30)
    
    class SimpleDecorator:
        """简单的类装饰器示例"""
        
        def __init__(self, func):
            """初始化装饰器，保存被装饰的函数"""
            self.func = func
            self.call_count = 0
            functools.update_wrapper(self, func)
        
        def __call__(self, *args, **kwargs):
            """当装饰器被调用时执行"""
            self.call_count += 1
            print(f"第 {self.call_count} 次调用函数: {self.func.__name__}")
            result = self.func(*args, **kwargs)
            print(f"函数 {self.func.__name__} 执行完成")
            return result
        
        def get_call_count(self):
            """获取调用次数"""
            return self.call_count
    
    @SimpleDecorator
    def greet(name):
        """问候函数"""
        message = f"Hello, {name}!"
        print(message)
        return message
    
    print("调用基本类装饰器：")
    greet("Alice")
    greet("Bob")
    print(f"总调用次数: {greet.get_call_count()}")
    
    # 2. 带参数的类装饰器
    print("\n2. 带参数的类装饰器")
    print("-" * 30)
    
    class TimingDecorator:
        """计时装饰器类"""
        
        def __init__(self, unit='seconds', precision=4):
            """初始化装饰器参数"""
            self.unit = unit
            self.precision = precision
            self.times = []
        
        def __call__(self, func):
            """装饰器调用，返回包装函数"""
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                
                elapsed = end_time - start_time
                
                # 根据单位转换时间
                if self.unit == 'milliseconds':
                    elapsed *= 1000
                    unit_str = 'ms'
                elif self.unit == 'microseconds':
                    elapsed *= 1000000
                    unit_str = 'μs'
                else:
                    unit_str = 's'
                
                self.times.append(elapsed)
                print(f"函数 {func.__name__} 执行时间: {elapsed:.{self.precision}f} {unit_str}")
                
                return result
            
            # 添加统计方法
            wrapper.get_average_time = lambda: sum(self.times) / len(self.times) if self.times else 0
            wrapper.get_total_time = lambda: sum(self.times)
            wrapper.get_call_count = lambda: len(self.times)
            wrapper.get_times = lambda: self.times.copy()
            
            return wrapper
    
    @TimingDecorator(unit='milliseconds', precision=2)
    def calculate_fibonacci(n):
        """计算斐波那契数列"""
        if n <= 1:
            return n
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
    
    print("调用带参数的类装饰器：")
    result = calculate_fibonacci(10)
    print(f"斐波那契数列第10项: {result}")
    print(f"平均执行时间: {calculate_fibonacci.get_average_time():.2f} ms")
    
    # 3. 状态管理类装饰器
    print("\n3. 状态管理类装饰器")
    print("-" * 30)
    
    class CacheDecorator:
        """缓存装饰器类"""
        
        def __init__(self, max_size=128, ttl=None):
            """初始化缓存装饰器
            
            Args:
                max_size: 最大缓存大小
                ttl: 缓存生存时间（秒），None表示永不过期
            """
            self.max_size = max_size
            self.ttl = ttl
            self.cache = {}
            self.access_order = deque()  # 用于LRU
            self.access_times = {}  # 记录访问时间
        
        def __call__(self, func):
            """装饰器调用"""
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 创建缓存键
                key = self._make_key(args, kwargs)
                current_time = time.time()
                
                # 检查缓存是否存在且未过期
                if key in self.cache:
                    if self.ttl is None or (current_time - self.access_times[key]) < self.ttl:
                        # 更新访问顺序（LRU）
                        self.access_order.remove(key)
                        self.access_order.append(key)
                        self.access_times[key] = current_time
                        
                        print(f"缓存命中: {func.__name__}{args}")
                        return self.cache[key]
                    else:
                        # 缓存过期，删除
                        print(f"缓存过期: {func.__name__}{args}")
                        self._remove_from_cache(key)
                
                # 缓存未命中，执行函数
                print(f"缓存未命中，计算中: {func.__name__}{args}")
                result = func(*args, **kwargs)
                
                # 添加到缓存
                self._add_to_cache(key, result, current_time)
                
                return result
            
            # 添加缓存管理方法
            wrapper.clear_cache = self.clear_cache
            wrapper.cache_info = self.cache_info
            wrapper.cache_size = lambda: len(self.cache)
            
            return wrapper
        
        def _make_key(self, args, kwargs):
            """创建缓存键"""
            return str(args) + str(sorted(kwargs.items()))
        
        def _add_to_cache(self, key, value, timestamp):
            """添加到缓存"""
            # 如果缓存已满，删除最旧的条目
            if len(self.cache) >= self.max_size:
                oldest_key = self.access_order.popleft()
                del self.cache[oldest_key]
                del self.access_times[oldest_key]
                print(f"缓存已满，删除最旧条目")
            
            self.cache[key] = value
            self.access_times[key] = timestamp
            self.access_order.append(key)
            print(f"结果已缓存，当前缓存大小: {len(self.cache)}")
        
        def _remove_from_cache(self, key):
            """从缓存中删除"""
            if key in self.cache:
                del self.cache[key]
                del self.access_times[key]
                self.access_order.remove(key)
        
        def clear_cache(self):
            """清空缓存"""
            self.cache.clear()
            self.access_times.clear()
            self.access_order.clear()
            print("缓存已清空")
        
        def cache_info(self):
            """获取缓存信息"""
            return {
                'size': len(self.cache),
                'max_size': self.max_size,
                'ttl': self.ttl,
                'keys': list(self.cache.keys())
            }
    
    @CacheDecorator(max_size=3, ttl=2)
    def expensive_operation(x, y):
        """昂贵的操作"""
        time.sleep(0.1)  # 模拟耗时操作
        return x ** y
    
    print("调用状态管理类装饰器：")
    print(f"计算 2^3 = {expensive_operation(2, 3)}")
    print(f"计算 2^3 = {expensive_operation(2, 3)}")  # 缓存命中
    print(f"计算 3^2 = {expensive_operation(3, 2)}")
    print(f"缓存信息: {expensive_operation.cache_info()}")
    
    # 等待缓存过期
    print("等待缓存过期...")
    time.sleep(2.1)
    print(f"计算 2^3 = {expensive_operation(2, 3)}")  # 缓存过期，重新计算
    
    # 4. 多实例类装饰器
    print("\n4. 多实例类装饰器")
    print("-" * 30)
    
    class RateLimiter:
        """限流装饰器类"""
        
        def __init__(self, max_calls=5, time_window=60):
            """初始化限流器
            
            Args:
                max_calls: 时间窗口内最大调用次数
                time_window: 时间窗口大小（秒）
            """
            self.max_calls = max_calls
            self.time_window = time_window
            self.calls = defaultdict(deque)  # 每个函数的调用记录
        
        def __call__(self, func):
            """装饰器调用"""
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                current_time = time.time()
                func_name = func.__name__
                
                # 清理过期的调用记录
                while (self.calls[func_name] and 
                       current_time - self.calls[func_name][0] > self.time_window):
                    self.calls[func_name].popleft()
                
                # 检查是否超过限制
                if len(self.calls[func_name]) >= self.max_calls:
                    oldest_call = self.calls[func_name][0]
                    wait_time = self.time_window - (current_time - oldest_call)
                    print(f"限流触发: {func_name} 需要等待 {wait_time:.1f} 秒")
                    return None
                
                # 记录本次调用
                self.calls[func_name].append(current_time)
                print(f"执行 {func_name} (剩余调用次数: {self.max_calls - len(self.calls[func_name])})")
                
                return func(*args, **kwargs)
            
            # 添加状态查询方法
            wrapper.get_remaining_calls = lambda: max(0, self.max_calls - len(self.calls[func.__name__]))
            wrapper.get_reset_time = lambda: (self.calls[func.__name__][0] + self.time_window 
                                            if self.calls[func.__name__] else 0)
            
            return wrapper
    
    # 创建两个不同的限流器实例
    api_limiter = RateLimiter(max_calls=3, time_window=5)
    db_limiter = RateLimiter(max_calls=2, time_window=3)
    
    @api_limiter
    def api_request(endpoint):
        """API请求"""
        return f"API响应: {endpoint}"
    
    @db_limiter
    def database_query(table):
        """数据库查询"""
        return f"查询结果: {table}"
    
    print("调用多实例类装饰器：")
    for i in range(5):
        result = api_request(f"/endpoint{i}")
        if result:
            print(f"结果: {result}")
        print(f"API剩余调用次数: {api_request.get_remaining_calls()}")
    
    print("\n数据库查询测试：")
    for i in range(4):
        result = database_query(f"table{i}")
        if result:
            print(f"结果: {result}")
        print(f"DB剩余调用次数: {database_query.get_remaining_calls()}")
    
    # 5. 类装饰器装饰类
    print("\n5. 类装饰器装饰类")
    print("-" * 30)
    
    class SingletonDecorator:
        """单例装饰器类"""
        
        def __init__(self, cls):
            """初始化单例装饰器"""
            self.cls = cls
            self.instances = {}
            self.lock = threading.Lock()
        
        def __call__(self, *args, **kwargs):
            """创建或返回单例实例"""
            # 创建实例键
            key = (args, tuple(sorted(kwargs.items())))
            
            if key not in self.instances:
                with self.lock:
                    # 双重检查锁定
                    if key not in self.instances:
                        print(f"创建新的 {self.cls.__name__} 实例")
                        self.instances[key] = self.cls(*args, **kwargs)
                    else:
                        print(f"返回已存在的 {self.cls.__name__} 实例")
            else:
                print(f"返回已存在的 {self.cls.__name__} 实例")
            
            return self.instances[key]
        
        def get_instance_count(self):
            """获取实例数量"""
            return len(self.instances)
        
        def clear_instances(self):
            """清空所有实例"""
            self.instances.clear()
            print(f"已清空所有 {self.cls.__name__} 实例")
    
    @SingletonDecorator
    class DatabaseConnection:
        """数据库连接类"""
        
        def __init__(self, host, port=3306):
            self.host = host
            self.port = port
            self.connected = False
            print(f"初始化数据库连接: {host}:{port}")
        
        def connect(self):
            """连接数据库"""
            if not self.connected:
                print(f"连接到数据库 {self.host}:{self.port}")
                self.connected = True
            else:
                print("数据库已连接")
        
        def disconnect(self):
            """断开数据库连接"""
            if self.connected:
                print(f"断开数据库连接 {self.host}:{self.port}")
                self.connected = False
            else:
                print("数据库未连接")
    
    print("调用类装饰器装饰类：")
    db1 = DatabaseConnection("localhost", 3306)
    db2 = DatabaseConnection("localhost", 3306)  # 应该返回同一个实例
    db3 = DatabaseConnection("remote", 5432)     # 不同参数，创建新实例
    
    print(f"db1 和 db2 是同一个实例: {db1 is db2}")
    print(f"db1 和 db3 是同一个实例: {db1 is db3}")
    print(f"当前实例数量: {DatabaseConnection.get_instance_count()}")
    
    db1.connect()
    db2.connect()  # 应该显示已连接
    
    # 6. 高级类装饰器应用
    print("\n6. 高级类装饰器应用")
    print("-" * 30)
    
    class MethodProfiler:
        """方法性能分析装饰器"""
        
        def __init__(self, include_args=False, include_result=False):
            self.include_args = include_args
            self.include_result = include_result
            self.profiles = defaultdict(list)
        
        def __call__(self, func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                start_memory = self._get_memory_usage()
                
                try:
                    result = func(*args, **kwargs)
                    success = True
                    error = None
                except Exception as e:
                    result = None
                    success = False
                    error = str(e)
                    raise
                finally:
                    end_time = time.time()
                    end_memory = self._get_memory_usage()
                    
                    profile_data = {
                        'timestamp': datetime.now().isoformat(),
                        'execution_time': end_time - start_time,
                        'memory_delta': end_memory - start_memory,
                        'success': success,
                        'error': error
                    }
                    
                    if self.include_args:
                        profile_data['args'] = args
                        profile_data['kwargs'] = kwargs
                    
                    if self.include_result and success:
                        profile_data['result'] = result
                    
                    self.profiles[func.__name__].append(profile_data)
                    
                    print(f"性能分析 {func.__name__}: {end_time - start_time:.4f}s")
                
                return result
            
            wrapper.get_profile = lambda: self.profiles[func.__name__]
            wrapper.get_average_time = lambda: self._calculate_average_time(func.__name__)
            wrapper.get_success_rate = lambda: self._calculate_success_rate(func.__name__)
            
            return wrapper
        
        def _get_memory_usage(self):
            """获取内存使用量（简化版）"""
            import sys
            return sys.getsizeof({})
        
        def _calculate_average_time(self, func_name):
            """计算平均执行时间"""
            times = [p['execution_time'] for p in self.profiles[func_name]]
            return sum(times) / len(times) if times else 0
        
        def _calculate_success_rate(self, func_name):
            """计算成功率"""
            profiles = self.profiles[func_name]
            if not profiles:
                return 0
            success_count = sum(1 for p in profiles if p['success'])
            return success_count / len(profiles)
    
    profiler = MethodProfiler(include_args=True, include_result=True)
    
    @profiler
    def complex_calculation(n, multiplier=1):
        """复杂计算"""
        result = 0
        for i in range(n):
            result += i * multiplier
        return result
    
    print("调用高级类装饰器应用：")
    result1 = complex_calculation(1000, multiplier=2)
    result2 = complex_calculation(2000, multiplier=3)
    result3 = complex_calculation(500)
    
    print(f"平均执行时间: {complex_calculation.get_average_time():.6f}s")
    print(f"成功率: {complex_calculation.get_success_rate():.2%}")
    print(f"总调用次数: {len(complex_calculation.get_profile())}")


if __name__ == "__main__":
    main()