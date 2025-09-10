# 内存效率和惰性求值

生成器的最大优势之一是其出色的内存效率。通过惰性求值（Lazy Evaluation），生成器只在需要时才计算和产生值，这使得我们可以处理大量数据而不会耗尽内存。本章将深入探讨生成器的内存效率特性和惰性求值机制。

## 惰性求值概念

### 什么是惰性求值

惰性求值是一种计算策略，它延迟表达式的求值直到真正需要其值的时候。这与急切求值（Eager Evaluation）形成对比，后者会立即计算所有值。

```python
def lazy_evaluation_demo():
    """惰性求值演示"""
    print("=== 惰性求值 vs 急切求值 ===")
    
    # 急切求值 - 立即计算所有值
    def eager_squares(n):
        """急切求值：立即生成所有平方数"""
        print(f"  急切求值：开始计算 {n} 个平方数")
        result = []
        for i in range(n):
            square = i ** 2
            result.append(square)
            print(f"    计算: {i}^2 = {square}")
        print(f"  急切求值：完成，返回列表长度 {len(result)}")
        return result
    
    # 惰性求值 - 按需计算
    def lazy_squares(n):
        """惰性求值：按需生成平方数"""
        print(f"  惰性求值：准备生成 {n} 个平方数")
        for i in range(n):
            square = i ** 2
            print(f"    按需计算: {i}^2 = {square}")
            yield square
        print(f"  惰性求值：生成器创建完成")
    
    print("\n1. 急切求值示例:")
    eager_result = eager_squares(5)
    print(f"急切求值结果: {eager_result}")
    print(f"使用第一个值: {eager_result[0]}")
    
    print("\n2. 惰性求值示例:")
    lazy_result = lazy_squares(5)
    print(f"惰性求值结果: {lazy_result} (生成器对象)")
    print("获取第一个值:")
    first_value = next(lazy_result)
    print(f"第一个值: {first_value}")
    
    print("\n获取剩余值:")
    remaining_values = list(lazy_result)
    print(f"剩余值: {remaining_values}")

lazy_evaluation_demo()
```

### 惰性求值的优势

```python
def lazy_evaluation_benefits():
    """惰性求值优势演示"""
    print("\n=== 惰性求值的优势 ===")
    
    import time
    
    def expensive_computation(x):
        """模拟昂贵的计算"""
        time.sleep(0.1)  # 模拟计算时间
        return x ** 3 + x ** 2 + x
    
    def eager_expensive_computation(data):
        """急切计算"""
        print("  急切计算：开始处理所有数据")
        start_time = time.time()
        
        result = []
        for x in data:
            computed = expensive_computation(x)
            result.append(computed)
            print(f"    处理: {x} -> {computed}")
        
        end_time = time.time()
        print(f"  急切计算完成，耗时: {end_time - start_time:.2f}秒")
        return result
    
    def lazy_expensive_computation(data):
        """惰性计算"""
        print("  惰性计算：准备处理数据")
        
        for x in data:
            print(f"    按需处理: {x}")
            yield expensive_computation(x)
    
    # 测试数据
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("  优化生成器结果:")
    
    for result in optimized_generator(test_data):
        print(f"    结果: {result}")

best_practices()
```

## 学习要点总结

### 核心概念

1. **惰性求值**：生成器只在需要时才计算值，避免不必要的计算
2. **内存效率**：生成器不会一次性加载所有数据到内存
3. **流式处理**：可以处理无限大或超大数据集
4. **组合性**：生成器可以轻松组合成复杂的数据处理管道

### 性能优势

1. **内存使用**：常量级内存使用，与数据量无关
2. **启动时间**：生成器创建几乎不消耗时间
3. **响应性**：可以立即开始产生结果
4. **可扩展性**：能够处理任意大小的数据集

### 最佳实践

1. **合理使用**：在处理大数据或需要惰性求值时使用生成器
2. **避免陷阱**：注意生成器只能迭代一次的特性
3. **错误处理**：在生成器中妥善处理异常
4. **资源管理**：使用上下文管理器确保资源正确释放
5. **性能优化**：避免在生成器中进行重复计算

### 实际应用

1. **大文件处理**：逐行读取和处理大文件
2. **数据流水线**：构建复杂的数据处理管道
3. **日志分析**：实时分析大量日志数据
4. **网络数据**：处理流式网络数据
5. **批处理**：分批处理大数据集

## 练习建议

1. **基础练习**：
   - 比较列表推导式和生成器表达式的内存使用
   - 实现一个内存高效的文件处理器
   - 创建一个数据流水线处理系统

2. **进阶练习**：
   - 实现一个日志分析工具
   - 创建一个内存高效的数据聚合器
   - 构建一个流式数据处理框架

3. **实战项目**：
   - 开发一个大数据处理工具
   - 实现一个实时数据监控系统
   - 创建一个高性能的数据转换工具

通过本章的学习，你应该能够：
- 理解惰性求值的概念和优势
- 掌握生成器的内存效率特性
- 能够构建高效的数据处理管道
- 在实际项目中合理使用生成器优化性能

---

**下一步学习**：[生成器综合练习](./08_exercises.md)data = [1, 2, 3, 4, 5]
    
    print("\n1. 急切计算 - 处理所有数据:")
    start_time = time.time()
    eager_results = eager_expensive_computation(test_data)
    eager_time = time.time() - start_time
    print(f"急切计算总耗时: {eager_time:.2f}秒")
    print(f"只使用第一个结果: {eager_results[0]}")
    
    print("\n2. 惰性计算 - 只处理需要的数据:")
    start_time = time.time()
    lazy_results = lazy_expensive_computation(test_data)
    creation_time = time.time() - start_time
    print(f"生成器创建耗时: {creation_time:.4f}秒")
    
    # 只获取第一个结果
    start_time = time.time()
    first_result = next(lazy_results)
    first_time = time.time() - start_time
    print(f"获取第一个结果: {first_result}，耗时: {first_time:.2f}秒")
    
    print(f"\n性能对比:")
    print(f"  急切计算: {eager_time:.2f}秒 (处理了所有数据)")
    print(f"  惰性计算: {first_time:.2f}秒 (只处理了需要的数据)")
    print(f"  效率提升: {(eager_time / first_time):.1f}倍")

lazy_evaluation_benefits()
```

## 内存使用对比

### 内存消耗分析

```python
def memory_usage_comparison():
    """内存使用对比演示"""
    print("\n=== 内存使用对比 ===")
    
    import gc
    import sys
    
    def get_memory_usage():
        """获取当前内存使用情况（简化版）"""
        # 执行垃圾回收
        gc.collect()
        
        # 获取对象数量作为内存使用的指标
        objects = len(gc.get_objects())
        
        # 模拟内存使用量（实际应用中可以使用psutil等库）
        estimated_memory = objects * 64  # 假设每个对象平均64字节
        
        return {
            'objects': objects,
            'estimated_memory_kb': estimated_memory / 1024
        }
    
    def create_large_list(size):
        """创建大列表"""
        print(f"  创建包含 {size:,} 个元素的列表")
        return [i ** 2 for i in range(size)]
    
    def create_large_generator(size):
        """创建大生成器"""
        print(f"  创建可生成 {size:,} 个元素的生成器")
        return (i ** 2 for i in range(size))
    
    # 测试不同大小的数据
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        print(f"\n--- 测试大小: {size:,} ---")
        
        # 基准内存使用
        baseline = get_memory_usage()
        print(f"基准内存: {baseline['estimated_memory_kb']:.1f} KB")
        
        # 测试列表内存使用
        print("\n1. 列表方式:")
        large_list = create_large_list(size)
        list_memory = get_memory_usage()
        list_overhead = list_memory['estimated_memory_kb'] - baseline['estimated_memory_kb']
        print(f"列表内存: {list_memory['estimated_memory_kb']:.1f} KB")
        print(f"列表开销: {list_overhead:.1f} KB")
        print(f"列表大小: {sys.getsizeof(large_list)} 字节")
        
        # 清理列表
        del large_list
        gc.collect()
        
        # 测试生成器内存使用
        print("\n2. 生成器方式:")
        large_generator = create_large_generator(size)
        gen_memory = get_memory_usage()
        gen_overhead = gen_memory['estimated_memory_kb'] - baseline['estimated_memory_kb']
        print(f"生成器内存: {gen_memory['estimated_memory_kb']:.1f} KB")
        print(f"生成器开销: {gen_overhead:.1f} KB")
        print(f"生成器大小: {sys.getsizeof(large_generator)} 字节")
        
        # 内存效率对比
        if list_overhead > 0:
            efficiency = list_overhead / max(gen_overhead, 0.1)
            print(f"\n内存效率对比:")
            print(f"  列表开销: {list_overhead:.1f} KB")
            print(f"  生成器开销: {gen_overhead:.1f} KB")
            print(f"  生成器节省: {efficiency:.1f}倍内存")
        
        # 清理生成器
        del large_generator
        gc.collect()
        
        print("-" * 50)

memory_usage_comparison()
```

### 大数据处理示例

```python
def big_data_processing():
    """大数据处理演示"""
    print("\n=== 大数据处理 ===")
    
    def process_large_dataset_list(size):
        """使用列表处理大数据集"""
        print(f"  列表方式处理 {size:,} 条数据")
        
        # 生成数据
        data = list(range(size))
        
        # 处理数据
        processed = []
        for item in data:
            if item % 2 == 0:  # 只处理偶数
                result = item ** 2 + item
                processed.append(result)
        
        print(f"  处理完成，结果数量: {len(processed):,}")
        return processed
    
    def process_large_dataset_generator(size):
        """使用生成器处理大数据集"""
        print(f"  生成器方式处理 {size:,} 条数据")
        
        # 数据生成器
        def data_generator():
            for i in range(size):
                yield i
        
        # 处理生成器
        def process_generator(data_gen):
            for item in data_gen:
                if item % 2 == 0:  # 只处理偶数
                    result = item ** 2 + item
                    yield result
        
        # 创建处理管道
        data_gen = data_generator()
        processed_gen = process_generator(data_gen)
        
        print("  生成器管道创建完成")
        return processed_gen
    
    # 测试大小
    test_size = 100000
    
    print(f"\n处理 {test_size:,} 条数据的性能对比:")
    
    # 列表方式
    print("\n1. 列表方式:")
    import time
    start_time = time.time()
    
    try:
        list_results = process_large_dataset_list(test_size)
        list_time = time.time() - start_time
        print(f"  列表处理耗时: {list_time:.2f}秒")
        print(f"  内存中存储了 {len(list_results):,} 个结果")
        
        # 只使用前10个结果
        used_results = list_results[:10]
        print(f"  实际使用的结果: {used_results}")
        
    except MemoryError:
        print("  列表方式内存不足！")
        list_time = float('inf')
    
    # 生成器方式
    print("\n2. 生成器方式:")
    start_time = time.time()
    
    gen_results = process_large_dataset_generator(test_size)
    gen_creation_time = time.time() - start_time
    print(f"  生成器创建耗时: {gen_creation_time:.4f}秒")
    
    # 只获取前10个结果
    start_time = time.time()
    used_results = []
    for i, result in enumerate(gen_results):
        if i >= 10:
            break
        used_results.append(result)
    
    gen_usage_time = time.time() - start_time
    print(f"  获取前10个结果耗时: {gen_usage_time:.4f}秒")
    print(f"  实际使用的结果: {used_results}")
    
    # 性能总结
    print(f"\n性能总结:")
    if list_time != float('inf'):
        print(f"  列表方式总耗时: {list_time:.2f}秒")
    else:
        print(f"  列表方式: 内存不足")
    
    total_gen_time = gen_creation_time + gen_usage_time
    print(f"  生成器方式总耗时: {total_gen_time:.4f}秒")
    
    if list_time != float('inf'):
        efficiency = list_time / total_gen_time
        print(f"  生成器效率提升: {efficiency:.1f}倍")

big_data_processing()
```

## 流式数据处理

### 数据流水线

```python
def streaming_data_pipeline():
    """流式数据处理管道演示"""
    print("\n=== 流式数据处理管道 ===")
    
    def data_source(count):
        """数据源生成器"""
        print(f"  数据源：准备生成 {count} 条数据")
        
        for i in range(count):
            # 模拟从外部源读取数据
            data = {
                'id': i,
                'value': i * 2 + 1,
                'category': 'A' if i % 3 == 0 else 'B' if i % 3 == 1 else 'C'
            }
            print(f"    生成数据: {data}")
            yield data
    
    def data_filter(data_stream, condition):
        """数据过滤器"""
        print("  过滤器：开始过滤数据")
        
        for data in data_stream:
            if condition(data):
                print(f"    过滤通过: {data}")
                yield data
            else:
                print(f"    过滤拒绝: {data}")
    
    def data_transformer(data_stream, transform_func):
        """数据转换器"""
        print("  转换器：开始转换数据")
        
        for data in data_stream:
            transformed = transform_func(data)
            print(f"    转换: {data} -> {transformed}")
            yield transformed
    
    def data_aggregator(data_stream, batch_size):
        """数据聚合器"""
        print(f"  聚合器：按 {batch_size} 个一批聚合数据")
        
        batch = []
        for data in data_stream:
            batch.append(data)
            
            if len(batch) >= batch_size:
                # 计算批次统计
                batch_stats = {
                    'count': len(batch),
                    'sum': sum(item['transformed_value'] for item in batch),
                    'avg': sum(item['transformed_value'] for item in batch) / len(batch),
                    'items': batch.copy()
                }
                print(f"    聚合批次: {batch_stats['count']} 项，平均值: {batch_stats['avg']:.2f}")
                yield batch_stats
                batch = []
        
        # 处理剩余数据
        if batch:
            batch_stats = {
                'count': len(batch),
                'sum': sum(item['transformed_value'] for item in batch),
                'avg': sum(item['transformed_value'] for item in batch) / len(batch),
                'items': batch.copy()
            }
            print(f"    聚合最后批次: {batch_stats['count']} 项，平均值: {batch_stats['avg']:.2f}")
            yield batch_stats
    
    # 构建处理管道
    print("\n构建流式处理管道:")
    
    # 1. 数据源
    source = data_source(10)
    
    # 2. 过滤器 - 只保留category为A或B的数据
    filtered = data_filter(source, lambda x: x['category'] in ['A', 'B'])
    
    # 3. 转换器 - 计算转换值
    def transform_data(data):
        return {
            'id': data['id'],
            'original_value': data['value'],
            'transformed_value': data['value'] ** 2,
            'category': data['category']
        }
    
    transformed = data_transformer(filtered, transform_data)
    
    # 4. 聚合器 - 每3个数据聚合一次
    aggregated = data_aggregator(transformed, 3)
    
    # 5. 处理结果
    print("\n开始流式处理:")
    results = []
    for batch_result in aggregated:
        results.append(batch_result)
        print(f"  收到聚合结果: 批次大小={batch_result['count']}, 平均值={batch_result['avg']:.2f}")
    
    print(f"\n处理完成，共产生 {len(results)} 个批次结果")
    
    # 展示内存效率
    print("\n内存效率分析:")
    print("  - 数据源：按需生成，不占用额外内存")
    print("  - 过滤器：流式处理，只保留当前数据")
    print("  - 转换器：即时转换，不存储中间结果")
    print("  - 聚合器：只保留当前批次，处理完即释放")
    print("  - 总体：内存使用量恒定，与数据量无关")

streaming_data_pipeline()
```

### 文件处理优化

```python
def file_processing_optimization():
    """文件处理优化演示"""
    print("\n=== 文件处理优化 ===")
    
    import tempfile
    import os
    
    # 创建测试文件
    def create_test_file(filename, lines):
        """创建测试文件"""
        with open(filename, 'w', encoding='utf-8') as f:
            for i in range(lines):
                f.write(f"line {i}: data value {i * 2}, category {i % 3}\n")
        print(f"  创建测试文件: {filename} ({lines} 行)")
    
    def process_file_traditional(filename):
        """传统方式处理文件"""
        print("  传统方式：一次性读取所有行")
        
        # 读取所有行
        with open(filename, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
        
        print(f"    读取了 {len(all_lines)} 行到内存")
        
        # 处理数据
        processed_lines = []
        for line in all_lines:
            if 'category 1' in line:  # 只处理category 1的行
                processed = line.strip().upper()
                processed_lines.append(processed)
        
        print(f"    处理完成，结果: {len(processed_lines)} 行")
        return processed_lines
    
    def process_file_generator(filename):
        """生成器方式处理文件"""
        print("  生成器方式：逐行读取和处理")
        
        def line_reader(filename):
            """行读取生成器"""
            with open(filename, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    print(f"    读取第 {line_num} 行")
                    yield line.strip()
        
        def line_processor(lines):
            """行处理生成器"""
            for line in lines:
                if 'category 1' in line:  # 只处理category 1的行
                    processed = line.upper()
                    print(f"    处理行: {processed[:50]}...")
                    yield processed
        
        # 创建处理管道
        lines = line_reader(filename)
        processed = line_processor(lines)
        
        # 收集结果（在实际应用中，可能会流式写入另一个文件）
        results = list(processed)
        print(f"    处理完成，结果: {len(results)} 行")
        return results
    
    def process_file_chunked(filename, chunk_size=1000):
        """分块处理文件"""
        print(f"  分块方式：每次处理 {chunk_size} 行")
        
        def chunk_reader(filename, chunk_size):
            """分块读取生成器"""
            with open(filename, 'r', encoding='utf-8') as f:
                chunk = []
                for line_num, line in enumerate(f, 1):
                    chunk.append(line.strip())
                    
                    if len(chunk) >= chunk_size:
                        print(f"    读取块: 行 {line_num - chunk_size + 1} - {line_num}")
                        yield chunk
                        chunk = []
                
                # 处理最后一块
                if chunk:
                    print(f"    读取最后块: {len(chunk)} 行")
                    yield chunk
        
        def chunk_processor(chunks):
            """分块处理生成器"""
            for chunk in chunks:
                processed_chunk = []
                for line in chunk:
                    if 'category 1' in line:  # 只处理category 1的行
                        processed = line.upper()
                        processed_chunk.append(processed)
                
                if processed_chunk:
                    print(f"    处理块: {len(processed_chunk)} 行符合条件")
                    yield processed_chunk
        
        # 创建处理管道
        chunks = chunk_reader(filename, chunk_size)
        processed_chunks = chunk_processor(chunks)
        
        # 收集结果
        all_results = []
        for chunk_results in processed_chunks:
            all_results.extend(chunk_results)
        
        print(f"    处理完成，总结果: {len(all_results)} 行")
        return all_results
    
    # 创建临时测试文件
    temp_dir = tempfile.mkdtemp()
    test_file = os.path.join(temp_dir, 'test_data.txt')
    
    try:
        # 创建测试文件
        create_test_file(test_file, 10000)
        
        print(f"\n文件大小: {os.path.getsize(test_file)} 字节")
        
        # 测试不同处理方式
        import time
        
        print("\n1. 传统方式处理:")
        start_time = time.time()
        traditional_results = process_file_traditional(test_file)
        traditional_time = time.time() - start_time
        print(f"  传统方式耗时: {traditional_time:.3f}秒")
        print(f"  结果数量: {len(traditional_results)}")
        
        print("\n2. 生成器方式处理:")
        start_time = time.time()
        generator_results = process_file_generator(test_file)
        generator_time = time.time() - start_time
        print(f"  生成器方式耗时: {generator_time:.3f}秒")
        print(f"  结果数量: {len(generator_results)}")
        
        print("\n3. 分块方式处理:")
        start_time = time.time()
        chunked_results = process_file_chunked(test_file, 1000)
        chunked_time = time.time() - start_time
        print(f"  分块方式耗时: {chunked_time:.3f}秒")
        print(f"  结果数量: {len(chunked_results)}")
        
        # 验证结果一致性
        print("\n结果验证:")
        print(f"  传统方式结果数: {len(traditional_results)}")
        print(f"  生成器方式结果数: {len(generator_results)}")
        print(f"  分块方式结果数: {len(chunked_results)}")
        
        if len(traditional_results) == len(generator_results) == len(chunked_results):
            print("  ✓ 所有方式结果数量一致")
        else:
            print("  ✗ 结果数量不一致")
        
        # 性能对比
        print("\n性能对比:")
        print(f"  传统方式: {traditional_time:.3f}秒")
        print(f"  生成器方式: {generator_time:.3f}秒")
        print(f"  分块方式: {chunked_time:.3f}秒")
        
        if generator_time > 0:
            print(f"  生成器 vs 传统: {traditional_time/generator_time:.2f}倍")
        if chunked_time > 0:
            print(f"  分块 vs 传统: {traditional_time/chunked_time:.2f}倍")
    
    finally:
        # 清理临时文件
        if os.path.exists(test_file):
            os.remove(test_file)
        os.rmdir(temp_dir)
        print(f"\n清理临时文件: {test_file}")

file_processing_optimization()
```

## 性能基准测试

### 内存和时间性能测试

```python
def performance_benchmarks():
    """性能基准测试"""
    print("\n=== 性能基准测试 ===")
    
    import time
    import gc
    
    def benchmark_memory_usage(func, *args, **kwargs):
        """基准测试内存使用"""
        # 执行垃圾回收
        gc.collect()
        
        # 记录执行前的对象数量
        before_objects = len(gc.get_objects())
        
        # 执行函数
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        # 记录执行后的对象数量
        after_objects = len(gc.get_objects())
        
        return {
            'result': result,
            'execution_time': end_time - start_time,
            'objects_created': after_objects - before_objects,
            'memory_impact': (after_objects - before_objects) * 64  # 估算字节
        }
    
    def list_comprehension_test(size):
        """列表推导式测试"""
        return [x ** 2 for x in range(size)]
    
    def generator_expression_test(size):
        """生成器表达式测试"""
        return (x ** 2 for x in range(size))
    
    def generator_function_test(size):
        """生成器函数测试"""
        def squares():
            for x in range(size):
                yield x ** 2
        return squares()
    
    def consume_first_n(iterable, n):
        """消费前n个元素"""
        result = []
        for i, item in enumerate(iterable):
            if i >= n:
                break
            result.append(item)
        return result
    
    # 测试不同大小的数据
    test_sizes = [1000, 10000, 100000]
    consume_count = 100  # 只消费前100个元素
    
    for size in test_sizes:
        print(f"\n--- 测试大小: {size:,} 元素，消费前 {consume_count} 个 ---")
        
        # 测试列表推导式
        print("\n1. 列表推导式:")
        list_benchmark = benchmark_memory_usage(list_comprehension_test, size)
        list_result = consume_first_n(list_benchmark['result'], consume_count)
        
        print(f"  创建时间: {list_benchmark['execution_time']:.4f}秒")
        print(f"  内存影响: {list_benchmark['objects_created']} 对象")
        print(f"  估算内存: {list_benchmark['memory_impact']/1024:.1f} KB")
        print(f"  消费结果: {len(list_result)} 个元素")
        
        # 清理
        del list_benchmark['result']
        del list_result
        gc.collect()
        
        # 测试生成器表达式
        print("\n2. 生成器表达式:")
        gen_expr_benchmark = benchmark_memory_usage(generator_expression_test, size)
        
        # 消费生成器
        start_time = time.time()
        gen_expr_result = consume_first_n(gen_expr_benchmark['result'], consume_count)
        consume_time = time.time() - start_time
        
        print(f"  创建时间: {gen_expr_benchmark['execution_time']:.4f}秒")
        print(f"  消费时间: {consume_time:.4f}秒")
        print(f"  总时间: {gen_expr_benchmark['execution_time'] + consume_time:.4f}秒")
        print(f"  内存影响: {gen_expr_benchmark['objects_created']} 对象")
        print(f"  估算内存: {gen_expr_benchmark['memory_impact']/1024:.1f} KB")
        print(f"  消费结果: {len(gen_expr_result)} 个元素")
        
        # 清理
        del gen_expr_benchmark['result']
        del gen_expr_result
        gc.collect()
        
        # 测试生成器函数
        print("\n3. 生成器函数:")
        gen_func_benchmark = benchmark_memory_usage(generator_function_test, size)
        
        # 消费生成器
        start_time = time.time()
        gen_func_result = consume_first_n(gen_func_benchmark['result'], consume_count)
        consume_time = time.time() - start_time
        
        print(f"  创建时间: {gen_func_benchmark['execution_time']:.4f}秒")
        print(f"  消费时间: {consume_time:.4f}秒")
        print(f"  总时间: {gen_func_benchmark['execution_time'] + consume_time:.4f}秒")
        print(f"  内存影响: {gen_func_benchmark['objects_created']} 对象")
        print(f"  估算内存: {gen_func_benchmark['memory_impact']/1024:.1f} KB")
        print(f"  消费结果: {len(gen_func_result)} 个元素")
        
        # 性能对比
        print("\n性能对比:")
        list_total_time = list_benchmark['execution_time']
        gen_expr_total_time = gen_expr_benchmark['execution_time'] + consume_time
        gen_func_total_time = gen_func_benchmark['execution_time'] + consume_time
        
        print(f"  列表推导式: {list_total_time:.4f}秒, {list_benchmark['memory_impact']/1024:.1f} KB")
        print(f"  生成器表达式: {gen_expr_total_time:.4f}秒, {gen_expr_benchmark['memory_impact']/1024:.1f} KB")
        print(f"  生成器函数: {gen_func_total_time:.4f}秒, {gen_func_benchmark['memory_impact']/1024:.1f} KB")
        
        # 效率计算
        if gen_expr_total_time > 0:
            time_efficiency = list_total_time / gen_expr_total_time
            memory_efficiency = list_benchmark['memory_impact'] / max(gen_expr_benchmark['memory_impact'], 1)
            print(f"  生成器表达式时间效率: {time_efficiency:.2f}倍")
            print(f"  生成器表达式内存效率: {memory_efficiency:.2f}倍")
        
        # 清理
        del gen_func_benchmark['result']
        del gen_func_result
        gc.collect()
        
        print("-" * 60)

performance_benchmarks()
```

## 实际应用场景

### 日志分析系统

```python
def log_analysis_system():
    """日志分析系统演示"""
    print("\n=== 日志分析系统 ===")
    
    import re
    import tempfile
    import os
    from datetime import datetime, timedelta
    
    def generate_sample_logs(filename, days=7, entries_per_day=1000):
        """生成示例日志文件"""
        print(f"  生成示例日志: {days} 天，每天 {entries_per_day} 条")
        
        log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']
        log_sources = ['web_server', 'database', 'cache', 'auth_service']
        
        with open(filename, 'w', encoding='utf-8') as f:
            base_date = datetime.now() - timedelta(days=days)
            
            for day in range(days):
                current_date = base_date + timedelta(days=day)
                
                for entry in range(entries_per_day):
                    timestamp = current_date + timedelta(
                        hours=entry // 42,  # 分布在24小时内
                        minutes=(entry * 17) % 60,
                        seconds=(entry * 7) % 60
                    )
                    
                    level = log_levels[entry % len(log_levels)]
                    source = log_sources[entry % len(log_sources)]
                    
                    # 模拟不同类型的日志消息
                    if level == 'ERROR':
                        messages = [
                            f"Connection failed to {source}",
                            f"Timeout in {source} operation",
                            f"Invalid request to {source}"
                        ]
                    elif level == 'WARNING':
                        messages = [
                            f"High memory usage in {source}",
                            f"Slow response from {source}",
                            f"Retry attempt for {source}"
                        ]
                    else:
                        messages = [
                            f"Request processed by {source}",
                            f"Operation completed in {source}",
                            f"Status check for {source}"
                        ]
                    
                    message = messages[entry % len(messages)]
                    
                    log_line = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} [{level}] {source}: {message}\n"
                    f.write(log_line)
        
        print(f"  日志文件生成完成: {filename}")
    
    def traditional_log_analysis(filename):
        """传统日志分析方式"""
        print("  传统方式：一次性加载所有日志")
        
        # 读取所有日志
        with open(filename, 'r', encoding='utf-8') as f:
            all_logs = f.readlines()
        
        print(f"    加载了 {len(all_logs)} 条日志到内存")
        
        # 分析日志
        error_logs = []
        warning_logs = []
        source_stats = {}
        
        for log_line in all_logs:
            if '[ERROR]' in log_line:
                error_logs.append(log_line.strip())
            elif '[WARNING]' in log_line:
                warning_logs.append(log_line.strip())
            
            # 统计来源
            for source in ['web_server', 'database', 'cache', 'auth_service']:
                if source in log_line:
                    source_stats[source] = source_stats.get(source, 0) + 1
        
        return {
            'total_logs': len(all_logs),
            'error_count': len(error_logs),
            'warning_count': len(warning_logs),
            'source_stats': source_stats,
            'sample_errors': error_logs[:5]
        }
    
    def streaming_log_analysis(filename):
        """流式日志分析"""
        print("  流式方式：逐行处理日志")
        
        def log_reader(filename):
            """日志读取生成器"""
            with open(filename, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    if line_num % 1000 == 0:
                        print(f"    处理到第 {line_num} 行")
                    yield line.strip()
        
        def log_analyzer(log_stream):
            """日志分析生成器"""
            stats = {
                'total_logs': 0,
                'error_count': 0,
                'warning_count': 0,
                'source_stats': {},
                'sample_errors': []
            }
            
            for log_line in log_stream:
                stats['total_logs'] += 1
                
                if '[ERROR]' in log_line:
                    stats['error_count'] += 1
                    if len(stats['sample_errors']) < 5:
                        stats['sample_errors'].append(log_line)
                elif '[WARNING]' in log_line:
                    stats['warning_count'] += 1
                
                # 统计来源
                for source in ['web_server', 'database', 'cache', 'auth_service']:
                    if source in log_line:
                        stats['source_stats'][source] = stats['source_stats'].get(source, 0) + 1
                
                # 定期产出中间结果
                if stats['total_logs'] % 1000 == 0:
                    yield stats.copy()
            
            # 最终结果
            yield stats
        
        # 创建分析管道
        logs = log_reader(filename)
        analysis_results = log_analyzer(logs)
        
        # 获取最终结果
        final_result = None
        for result in analysis_results:
            final_result = result
        
        return final_result
    
    def chunked_log_analysis(filename, chunk_size=1000):
        """分块日志分析"""
        print(f"  分块方式：每次处理 {chunk_size} 行")
        
        def chunk_reader(filename, chunk_size):
            """分块读取生成器"""
            with open(filename, 'r', encoding='utf-8') as f:
                chunk = []
                for line in f:
                    chunk.append(line.strip())
                    
                    if len(chunk) >= chunk_size:
                        yield chunk
                        chunk = []
                
                if chunk:
                    yield chunk
        
        def chunk_analyzer(chunks):
            """分块分析生成器"""
            total_stats = {
                'total_logs': 0,
                'error_count': 0,
                'warning_count': 0,
                'source_stats': {},
                'sample_errors': []
            }
            
            for chunk_num, chunk in enumerate(chunks, 1):
                print(f"    处理第 {chunk_num} 块，{len(chunk)} 行")
                
                chunk_stats = {
                    'error_count': 0,
                    'warning_count': 0,
                    'source_stats': {}
                }
                
                for log_line in chunk:
                    total_stats['total_logs'] += 1
                    
                    if '[ERROR]' in log_line:
                        total_stats['error_count'] += 1
                        chunk_stats['error_count'] += 1
                        if len(total_stats['sample_errors']) < 5:
                            total_stats['sample_errors'].append(log_line)
                    elif '[WARNING]' in log_line:
                        total_stats['warning_count'] += 1
                        chunk_stats['warning_count'] += 1
                    
                    # 统计来源
                    for source in ['web_server', 'database', 'cache', 'auth_service']:
                        if source in log_line:
                            total_stats['source_stats'][source] = total_stats['source_stats'].get(source, 0) + 1
                            chunk_stats['source_stats'][source] = chunk_stats['source_stats'].get(source, 0) + 1
                
                yield {
                    'chunk_num': chunk_num,
                    'chunk_stats': chunk_stats,
                    'total_stats': total_stats.copy()
                }
        
        # 创建分析管道
        chunks = chunk_reader(filename, chunk_size)
        analysis_results = chunk_analyzer(chunks)
        
        # 获取最终结果
        final_result = None
        for result in analysis_results:
            final_result = result['total_stats']
        
        return final_result
    
    # 创建测试日志文件
    temp_dir = tempfile.mkdtemp()
    log_file = os.path.join(temp_dir, 'application.log')
    
    try:
        # 生成日志文件
        generate_sample_logs(log_file, days=3, entries_per_day=2000)
        
        file_size = os.path.getsize(log_file)
        print(f"\n日志文件大小: {file_size / 1024:.1f} KB")
        
        # 测试不同分析方式
        import time
        
        print("\n1. 传统方式分析:")
        start_time = time.time()
        traditional_result = traditional_log_analysis(log_file)
        traditional_time = time.time() - start_time
        
        print(f"  分析耗时: {traditional_time:.3f}秒")
        print(f"  结果: {traditional_result}")
        
        print("\n2. 流式方式分析:")
        start_time = time.time()
        streaming_result = streaming_log_analysis(log_file)
        streaming_time = time.time() - start_time
        
        print(f"  分析耗时: {streaming_time:.3f}秒")
        print(f"  结果: {streaming_result}")
        
        print("\n3. 分块方式分析:")
        start_time = time.time()
        chunked_result = chunked_log_analysis(log_file, 500)
        chunked_time = time.time() - start_time
        
        print(f"  分析耗时: {chunked_time:.3f}秒")
        print(f"  结果: {chunked_result}")
        
        # 性能对比
        print("\n性能对比:")
        print(f"  传统方式: {traditional_time:.3f}秒")
        print(f"  流式方式: {streaming_time:.3f}秒")
        print(f"  分块方式: {chunked_time:.3f}秒")
        
        if streaming_time > 0:
            print(f"  流式 vs 传统: {traditional_time/streaming_time:.2f}倍")
        if chunked_time > 0:
            print(f"  分块 vs 传统: {traditional_time/chunked_time:.2f}倍")
    
    finally:
        # 清理
        if os.path.exists(log_file):
            os.remove(log_file)
        os.rmdir(temp_dir)
        print(f"\n清理临时文件: {log_file}")

log_analysis_system()
```

## 注意事项和最佳实践

### 常见陷阱

```python
def common_pitfalls():
    """常见陷阱演示"""
    print("\n=== 常见陷阱和注意事项 ===")
    
    print("\n1. 生成器只能迭代一次:")
    
    def number_generator():
        for i in range(5):
            print(f"  生成: {i}")
            yield i
    
    gen = number_generator()
    
    print("  第一次迭代:")
    first_iteration = list(gen)
    print(f"  结果: {first_iteration}")
    
    print("  第二次迭代:")
    second_iteration = list(gen)
    print(f"  结果: {second_iteration} (空！)")
    
    print("  解决方案：重新创建生成器")
    gen = number_generator()
    third_iteration = list(gen)
    print(f"  结果: {third_iteration}")
    
    print("\n2. 生成器中的变量绑定:")
    
    # 错误的做法
    generators = []
    for i in range(3):
        generators.append((x + i for x in range(3)))
    
    print("  错误的变量绑定:")
    for j, gen in enumerate(generators):
        result = list(gen)
        print(f"  生成器 {j}: {result} (都使用了最后的i值)")
    
    # 正确的做法
    def create_generator(offset):
        return (x + offset for x in range(3))
    
    generators = [create_generator(i) for i in range(3)]
    
    print("  正确的变量绑定:")
    for j, gen in enumerate(generators):
        result = list(gen)
        print(f"  生成器 {j}: {result}")
    
    print("\n3. 生成器中的异常处理:")
    
    def risky_generator():
        for i in range(5):
            if i == 3:
                raise ValueError(f"出错了：{i}")
            yield i
    
    print("  没有异常处理:")
    gen = risky_generator()
    try:
        for value in gen:
            print(f"  获得值: {value}")
    except ValueError as e:
        print(f"  捕获异常: {e}")
        print(f"  生成器状态: 已终止")
    
    print("  带异常处理的生成器:")
    def safe_generator():
        for i in range(5):
            try:
                if i == 3:
                    raise ValueError(f"模拟错误：{i}")
                yield i
            except ValueError as e:
                print(f"    生成器内部处理异常: {e}")
                yield -1  # 返回错误标记
    
    gen = safe_generator()
    for value in gen:
        print(f"  获得值: {value}")
    
    print("\n4. 内存泄漏风险:")
    
    def memory_leak_example():
        """可能导致内存泄漏的例子"""
        large_data = list(range(10000))  # 大数据
        
        def leaky_generator():
            # 错误：持有大数据的引用
            for item in large_data:
                yield item * 2
        
        return leaky_generator()
    
    def memory_efficient_example():
        """内存高效的例子"""
        def efficient_generator():
            # 正确：不持有大数据的引用
            for i in range(10000):
                yield i * 2
        
        return efficient_generator()
    
    print("  内存泄漏示例（持有大数据引用）:")
    leaky_gen = memory_leak_example()
    print(f"  生成器创建完成: {type(leaky_gen)}")
    
    print("  内存高效示例（不持有大数据引用）:")
    efficient_gen = memory_efficient_example()
    print(f"  生成器创建完成: {type(efficient_gen)}")
    
    # 测试前几个值
    print("  测试前5个值:")
    for i, (leak_val, eff_val) in enumerate(zip(leaky_gen, efficient_gen)):
        if i >= 5:
            break
        print(f"    泄漏版本: {leak_val}, 高效版本: {eff_val}")

common_pitfalls()
```

### 最佳实践

```python
def best_practices():
    """最佳实践演示"""
    print("\n=== 最佳实践 ===")
    
    print("\n1. 使用生成器工厂函数:")
    
    def create_fibonacci_generator(max_count=None):
        """斐波那契生成器工厂"""
        def fibonacci_gen():
            a, b = 0, 1
            count = 0
            while max_count is None or count < max_count:
                yield a
                a, b = b, a + b
                count += 1
        
        return fibonacci_gen()
    
    # 可以创建多个独立的生成器
    fib1 = create_fibonacci_generator(5)
    fib2 = create_fibonacci_generator(3)
    
    print(f"  斐波那契1 (5个): {list(fib1)}")
    print(f"  斐波那契2 (3个): {list(fib2)}")
    
    print("\n2. 组合生成器:")
    
    def chain_generators(*generators):
        """链接多个生成器"""
        for gen in generators:
            for item in gen:
                yield item
    
    def filter_generator(gen, condition):
        """过滤生成器"""
        for item in gen:
            if condition(item):
                yield item
    
    def map_generator(gen, func):
        """映射生成器"""
        for item in gen:
            yield func(item)
    
    # 创建基础生成器
    numbers1 = (x for x in range(5))
    numbers2 = (x for x in range(5, 10))
    
    # 组合生成器
    chained = chain_generators(numbers1, numbers2)
    filtered = filter_generator(chained, lambda x: x % 2 == 0)
    mapped = map_generator(filtered, lambda x: x ** 2)
    
    print(f"  组合结果: {list(mapped)}")
    
    print("\n3. 生成器上下文管理:")
    
    class GeneratorManager:
        """生成器管理器"""
        def __init__(self, generator_func, *args, **kwargs):
            self.generator_func = generator_func
            self.args = args
            self.kwargs = kwargs
            self.generator = None
        
        def __enter__(self):
            self.generator = self.generator_func(*self.args, **self.kwargs)
            return self.generator
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.generator:
                try:
                    self.generator.close()
                except GeneratorExit:
                    pass
                print("  生成器已安全关闭")
    
    def resource_generator(resource_name):
        """需要资源管理的生成器"""
        print(f"  打开资源: {resource_name}")
        try:
            for i in range(5):
                yield f"{resource_name}-{i}"
        finally:
            print(f"  清理资源: {resource_name}")
    
    print("  使用上下文管理器:")
    with GeneratorManager(resource_generator, "database") as gen:
        for item in gen:
            print(f"    处理: {item}")
            if "database-2" in item:
                break  # 提前退出
    
    print("\n4. 错误处理和恢复:")
    
    def robust_generator(data):
        """健壮的生成器"""
        for i, item in enumerate(data):
            try:
                # 模拟可能出错的处理
                if item < 0:
                    raise ValueError(f"负数不支持: {item}")
                
                result = item ** 0.5  # 平方根
                yield result
                
            except ValueError as e:
                print(f"    错误处理: {e}")
                # 可以选择跳过、返回默认值或重新抛出
                yield 0  # 返回默认值
            
            except Exception as e:
                print(f"    未预期错误: {e}")
                # 记录错误但继续处理
                continue
    
    test_data = [4, 9, -1, 16, "invalid", 25]
    print("  健壮生成器处理:")
    
    for result in robust_generator(test_data):
        print(f"    结果: {result}")
    
    print("\n5. 性能优化技巧:")
    
    def optimized_generator(data):
        """优化的生成器"""
        # 预计算常量
        threshold = len(data) // 2
        
        # 使用局部变量减少属性查找
        data_len = len(data)
        
        for i in range(data_len):
            item = data[i]
            
            # 避免重复计算
            if i < threshold:
                # 简单处理
                yield item * 2
            else:
                # 复杂处理
                yield item ** 2 + item
    
    test_