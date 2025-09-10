# 自定义迭代器实现

本节展示如何创建自定义迭代器类，实现复杂的迭代逻辑。通过实际例子学习迭代器的设计模式和最佳实践。

## 学习目标

1. 掌握自定义迭代器的实现方法
2. 理解迭代器的状态管理
3. 学会设计可重用的迭代器
4. 了解迭代器的性能优化

## 1. 基础自定义迭代器

创建一个简单的倒计时迭代器：

```python
class CountDown:
    """倒计时迭代器"""
    
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# 使用倒计时迭代器
print("倒计时迭代器演示:")
countdown = CountDown(5)
for num in countdown:
    print(f"倒计时: {num}")
```

## 2. 可重用的迭代器设计

设计可以多次使用的迭代器：

```python
class ReusableRange:
    """可重用的范围迭代器"""
    
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        # 返回一个新的迭代器实例，而不是self
        return RangeIterator(self.start, self.end, self.step)

class RangeIterator:
    """范围迭代器的实际实现"""
    
    def __init__(self, start, end, step):
        self.current = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current >= self.end) or \
           (self.step < 0 and self.current <= self.end):
            raise StopIteration
        result = self.current
        self.current += self.step
        return result

# 测试可重用迭代器
my_range = ReusableRange(1, 6, 2)

print("第一次遍历:")
for num in my_range:
    print(f"数字: {num}")

print("第二次遍历:")
for num in my_range:
    print(f"数字: {num}")
```

## 3. 斐波那契数列迭代器

实现无限或有限的斐波那契数列：

```python
class Fibonacci:
    """斐波那契数列迭代器"""
    
    def __init__(self, max_count=None):
        self.max_count = max_count
        self.count = 0
        self.current = 0
        self.next_val = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.max_count is not None and self.count >= self.max_count:
            raise StopIteration
        
        result = self.current
        self.current, self.next_val = self.next_val, self.current + self.next_val
        self.count += 1
        return result

# 使用斐波那契迭代器
print("斐波那契数列前10项:")
fib = Fibonacci(10)
for num in fib:
    print(f"斐波那契数: {num}")
```

## 4. 文件行迭代器

逐行读取文件的迭代器：

```python
class FileLineIterator:
    """文件行迭代器，逐行读取文件"""
    
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.file is None:
            try:
                self.file = open(self.filename, 'r', encoding='utf-8')
            except FileNotFoundError:
                raise StopIteration(f"文件 {self.filename} 不存在")
        
        line = self.file.readline()
        if not line:
            self.file.close()
            self.file = None
            raise StopIteration
        
        return line.rstrip('\n')
    
    def __del__(self):
        if self.file:
            self.file.close()

# 使用文件行迭代器
file_iter = FileLineIterator('example.txt')
for line_num, line in enumerate(file_iter, 1):
    print(f"第{line_num}行: {line}")
```

## 5. 树形结构迭代器

实现树的深度优先遍历：

```python
class TreeNode:
    """树节点"""
    
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def __iter__(self):
        return TreeIterator(self)

class TreeIterator:
    """树的深度优先遍历迭代器"""
    
    def __init__(self, root):
        self.stack = [root] if root else []
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.stack:
            raise StopIteration
        
        node = self.stack.pop()
        # 将子节点逆序添加到栈中，确保左子树先遍历
        for child in reversed(node.children):
            self.stack.append(child)
        
        return node.value

# 创建和遍历树结构
root = TreeNode("根节点")
child1 = TreeNode("子节点1")
child2 = TreeNode("子节点2")
root.add_child(child1)
root.add_child(child2)

for value in root:
    print(f"节点: {value}")
```

## 6. 批量处理迭代器

将数据分批返回的迭代器：

```python
class BatchIterator:
    """批量处理迭代器，将数据分批返回"""
    
    def __init__(self, iterable, batch_size):
        self.iterator = iter(iterable)
        self.batch_size = batch_size
    
    def __iter__(self):
        return self
    
    def __next__(self):
        batch = []
        try:
            for _ in range(self.batch_size):
                batch.append(next(self.iterator))
        except StopIteration:
            if batch:
                return batch
            raise
        return batch

# 使用批量处理迭代器
data = list(range(1, 12))  # [1, 2, 3, ..., 11]
batch_iter = BatchIterator(data, 3)
for batch_num, batch in enumerate(batch_iter, 1):
    print(f"批次{batch_num}: {batch}")
```

## 7. 循环迭代器

无限循环遍历序列的迭代器：

```python
class CycleIterator:
    """循环迭代器，无限循环遍历序列"""
    
    def __init__(self, iterable, max_cycles=None):
        self.iterable = list(iterable)
        self.max_cycles = max_cycles
        self.current_cycle = 0
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.iterable:
            raise StopIteration
        
        if self.max_cycles is not None and self.current_cycle >= self.max_cycles:
            raise StopIteration
        
        if self.index >= len(self.iterable):
            self.index = 0
            self.current_cycle += 1
            if self.max_cycles is not None and self.current_cycle >= self.max_cycles:
                raise StopIteration
        
        result = self.iterable[self.index]
        self.index += 1
        return result

# 使用循环迭代器
colors = ['红', '绿', '蓝']
cycle_iter = CycleIterator(colors, 3)
for i, color in enumerate(cycle_iter):
    if i >= 9:  # 限制输出数量
        break
    print(f"颜色{i+1}: {color}")
```

## 8. 过滤迭代器

根据条件过滤元素的迭代器：

```python
class FilterIterator:
    """过滤迭代器，根据条件过滤元素"""
    
    def __init__(self, iterable, predicate):
        self.iterator = iter(iterable)
        self.predicate = predicate
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            try:
                item = next(self.iterator)
                if self.predicate(item):
                    return item
            except StopIteration:
                raise

# 使用过滤迭代器
numbers = range(1, 11)
even_filter = FilterIterator(numbers, lambda x: x % 2 == 0)
for num in even_filter:
    print(f"偶数: {num}")
```

## 设计原则

### 1. 可重用性
- 在`__iter__()`方法中返回新的迭代器实例
- 避免修改原始数据结构的状态

### 2. 状态管理
- 合理管理迭代器的内部状态
- 确保状态变化的一致性

### 3. 异常处理
- 适当处理边界条件
- 正确抛出`StopIteration`异常

### 4. 资源管理
- 及时释放文件句柄等资源
- 实现`__del__`方法进行清理

## 学习要点

1. **迭代器协议**：必须实现`__iter__()`和`__next__()`方法
2. **状态维护**：合理管理迭代过程中的状态变化
3. **可重用设计**：通过返回新实例实现多次遍历
4. **异常处理**：正确使用`StopIteration`标识迭代结束
5. **资源管理**：及时清理占用的系统资源

## 注意事项

- 自定义迭代器应该是一次性的（除非特别设计为可重用）
- `__iter__()`方法通常返回`self`，但可重用迭代器应返回新实例
- 合理处理边界条件和异常情况
- 考虑内存效率，避免一次性加载大量数据
- 保持迭代器接口的简洁和一致性

通过这些例子，你可以学会如何设计和实现各种类型的自定义迭代器，满足不同的业务需求。