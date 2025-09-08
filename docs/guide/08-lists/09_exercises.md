# Python列表综合练习

本章包含了Python列表的综合练习和实战项目，通过大量的实践来巩固和提升列表操作技能。

## 学习目标

- 综合运用列表的各种操作方法
- 掌握常见算法的列表实现
- 学会使用列表解决实际问题
- 提升代码设计和优化能力
- 培养算法思维和问题解决能力

## 基础练习

### 1. 列表基本操作

```python
def basic_list_operations():
    """基础列表操作练习"""
    # 创建和初始化
    numbers = [1, 2, 3, 4, 5]
    print(f"原始列表: {numbers}")
    
    # 添加元素
    numbers.append(6)
    numbers.insert(0, 0)
    numbers.extend([7, 8, 9])
    print(f"添加元素后: {numbers}")
    
    # 删除元素
    numbers.remove(0)  # 删除值为0的元素
    popped = numbers.pop()  # 删除并返回最后一个元素
    del numbers[0]  # 删除索引为0的元素
    print(f"删除元素后: {numbers}, 弹出的元素: {popped}")
    
    # 修改元素
    numbers[0] = 10
    numbers[1:3] = [20, 30]
    print(f"修改元素后: {numbers}")
```

### 2. 列表切片操作

```python
def slicing_exercises():
    """切片操作练习"""
    data = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"原始数据: {data}")
    
    # 基本切片
    print(f"前5个元素: {data[:5]}")
    print(f"后5个元素: {data[-5:]}")
    print(f"中间元素: {data[2:8]}")
    
    # 步长切片
    print(f"偶数索引元素: {data[::2]}")
    print(f"奇数索引元素: {data[1::2]}")
    print(f"反向: {data[::-1]}")
    
    # 复杂切片
    print(f"每隔2个取1个，从索引1开始: {data[1::3]}")
    print(f"反向每隔2个: {data[::-2]}")
```

### 3. 列表方法应用

```python
def method_applications():
    """列表方法应用练习"""
    fruits = ['apple', 'banana', 'orange', 'apple', 'grape']
    print(f"水果列表: {fruits}")
    
    # 查找和计数
    print(f"apple的索引: {fruits.index('apple')}")
    print(f"apple出现次数: {fruits.count('apple')}")
    
    # 排序
    fruits_copy = fruits.copy()
    fruits_copy.sort()
    print(f"排序后: {fruits_copy}")
    
    # 反转
    fruits.reverse()
    print(f"反转后: {fruits}")
```

### 4. 列表推导式练习

```python
def comprehension_exercises():
    """列表推导式练习"""
    # 基本推导式
    squares = [x**2 for x in range(10)]
    print(f"平方数: {squares}")
    
    # 带条件的推导式
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"偶数的平方: {even_squares}")
    
    # 字符串处理
    words = ['hello', 'world', 'python', 'programming']
    lengths = [len(word) for word in words]
    print(f"单词长度: {lengths}")
    
    # 嵌套推导式
    matrix = [[i*j for j in range(3)] for i in range(3)]
    print(f"乘法表矩阵: {matrix}")
```

## 进阶练习

### 1. 查找重复元素

```python
def find_duplicates(lst):
    """查找列表中的重复元素"""
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

# 测试
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1]
duplicates = find_duplicates(numbers)
print(f"重复元素: {duplicates}")
```

### 2. 去重并保持顺序

```python
def remove_duplicates_keep_order(lst):
    """去重并保持原有顺序"""
    seen = set()
    result = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# 测试
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1]
unique_numbers = remove_duplicates_keep_order(numbers)
print(f"去重后: {unique_numbers}")
```

### 3. 列表分组

```python
def group_by_length(words):
    """按长度分组单词"""
    groups = {}
    
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    
    return groups

# 测试
words = ['cat', 'dog', 'elephant', 'bird', 'fish', 'butterfly']
groups = group_by_length(words)
for length, word_list in groups.items():
    print(f"长度{length}: {word_list}")
```

### 4. 列表旋转

```python
def rotate_list(lst, k):
    """将列表向右旋转k位"""
    if not lst or k == 0:
        return lst
    
    n = len(lst)
    k = k % n  # 处理k大于列表长度的情况
    
    return lst[-k:] + lst[:-k]

# 测试
numbers = [1, 2, 3, 4, 5, 6, 7]
rotated = rotate_list(numbers, 3)
print(f"原列表: {numbers}")
print(f"右旋转3位: {rotated}")
```

### 5. 合并有序列表

```python
def merge_sorted_lists(list1, list2):
    """合并两个有序列表"""
    result = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # 添加剩余元素
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result

# 测试
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(f"合并结果: {merged}")
```

## 实战项目

### 1. 学生成绩管理系统

```python
class GradeManager:
    """学生成绩管理系统"""
    
    def __init__(self):
        self.students = []  # 存储学生信息的列表
    
    def add_student(self, name, grades):
        """添加学生"""
        student = {
            'name': name,
            'grades': grades,
            'average': sum(grades) / len(grades) if grades else 0
        }
        self.students.append(student)
        print(f"已添加学生: {name}")
    
    def get_class_average(self):
        """获取班级平均分"""
        if not self.students:
            return 0
        
        total_average = sum(student['average'] for student in self.students)
        return total_average / len(self.students)
    
    def get_top_students(self, n=3):
        """获取前N名学生"""
        sorted_students = sorted(self.students, 
                               key=lambda x: x['average'], 
                               reverse=True)
        return sorted_students[:n]
    
    def display_report(self):
        """显示成绩报告"""
        print("\n=== 成绩报告 ===")
        print(f"班级人数: {len(self.students)}")
        print(f"班级平均分: {self.get_class_average():.2f}")
        
        print("\n学生成绩:")
        for student in self.students:
            print(f"  {student['name']}: {student['grades']} (平均: {student['average']:.2f})")
        
        print("\n前三名:")
        top_students = self.get_top_students(3)
        for i, student in enumerate(top_students, 1):
            print(f"  {i}. {student['name']}: {student['average']:.2f}")

# 使用示例
grade_manager = GradeManager()
grade_manager.add_student("Alice", [85, 92, 78, 96, 88])
grade_manager.add_student("Bob", [76, 85, 90, 82, 79])
grade_manager.add_student("Charlie", [95, 87, 92, 89, 94])
grade_manager.display_report()
```

### 2. 购物清单管理器

```python
class ShoppingList:
    """购物清单管理器"""
    
    def __init__(self):
        self.items = []  # 存储购物项目
    
    def add_item(self, name, price, quantity=1):
        """添加商品"""
        item = {
            'name': name,
            'price': price,
            'quantity': quantity,
            'total': price * quantity
        }
        self.items.append(item)
        print(f"已添加: {name} x{quantity}")
    
    def remove_item(self, name):
        """删除商品"""
        for i, item in enumerate(self.items):
            if item['name'] == name:
                removed = self.items.pop(i)
                print(f"已删除: {removed['name']}")
                return
        print(f"未找到商品: {name}")
    
    def update_quantity(self, name, new_quantity):
        """更新商品数量"""
        for item in self.items:
            if item['name'] == name:
                item['quantity'] = new_quantity
                item['total'] = item['price'] * new_quantity
                print(f"已更新 {name} 数量为 {new_quantity}")
                return
        print(f"未找到商品: {name}")
    
    def get_total_cost(self):
        """计算总价"""
        return sum(item['total'] for item in self.items)
    
    def display_list(self):
        """显示购物清单"""
        print("\n=== 购物清单 ===")
        if not self.items:
            print("清单为空")
            return
        
        for item in self.items:
            print(f"{item['name']}: ${item['price']:.2f} x{item['quantity']} = ${item['total']:.2f}")
        
        print(f"\n总计: ${self.get_total_cost():.2f}")
    
    def sort_by_price(self, reverse=False):
        """按价格排序"""
        self.items.sort(key=lambda x: x['price'], reverse=reverse)
        print(f"已按价格{'降序' if reverse else '升序'}排序")
    
    def get_expensive_items(self, threshold):
        """获取高价商品"""
        expensive = [item for item in self.items if item['price'] > threshold]
        return expensive

# 使用示例
shopping_list = ShoppingList()
shopping_list.add_item("苹果", 3.50, 2)
shopping_list.add_item("牛奶", 4.20, 1)
shopping_list.add_item("面包", 2.80, 3)
shopping_list.display_list()
```

### 3. 任务管理器

```python
class TaskManager:
    """简单的任务管理器"""
    
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, description, priority='medium'):
        """添加任务"""
        task = {
            'id': self.next_id,
            'description': description,
            'priority': priority,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        print(f"已添加任务: {description}")
    
    def complete_task(self, task_id):
        """完成任务"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"任务 {task_id} 已完成")
                return
        print(f"未找到任务 ID: {task_id}")
    
    def get_pending_tasks(self):
        """获取待办任务"""
        return [task for task in self.tasks if not task['completed']]
    
    def get_completed_tasks(self):
        """获取已完成任务"""
        return [task for task in self.tasks if task['completed']]
    
    def get_tasks_by_priority(self, priority):
        """按优先级获取任务"""
        return [task for task in self.tasks if task['priority'] == priority]
    
    def display_tasks(self):
        """显示所有任务"""
        print("\n=== 任务列表 ===")
        if not self.tasks:
            print("暂无任务")
            return
        
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"{status} [{task['id']}] {task['description']} ({task['priority']})")
        
        pending = len(self.get_pending_tasks())
        completed = len(self.get_completed_tasks())
        print(f"\n待办: {pending}, 已完成: {completed}")

# 使用示例
task_manager = TaskManager()
task_manager.add_task("完成Python作业", "high")
task_manager.add_task("买菜", "medium")
task_manager.add_task("看电影", "low")
task_manager.complete_task(1)
task_manager.display_tasks()
```

## 算法练习

### 1. 冒泡排序

```python
def bubble_sort(arr):
    """冒泡排序算法"""
    n = len(arr)
    arr = arr.copy()  # 不修改原数组
    
    for i in range(n):
        # 标记是否发生交换
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果没有交换，说明已经有序
        if not swapped:
            break
    
    return arr

# 测试
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(f"原数组: {numbers}")
print(f"排序后: {sorted_numbers}")
```

### 2. 二分查找

```python
def binary_search(arr, target):
    """二分查找算法"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # 未找到

# 测试
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
index = binary_search(sorted_array, target)
print(f"在数组 {sorted_array} 中查找 {target}")
print(f"找到位置: {index}" if index != -1 else "未找到")
```

### 3. 最大子数组和（Kadane算法）

```python
def max_subarray_sum(arr):
    """找到最大子数组和"""
    if not arr:
        return 0
    
    max_sum = current_sum = arr[0]
    start = end = temp_start = 0
    
    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, arr[start:end+1]

# 测试
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = max_subarray_sum(array)
print(f"数组: {array}")
print(f"最大子数组和: {max_sum}")
print(f"最大子数组: {subarray}")
```

### 4. 两数之和

```python
def two_sum(nums, target):
    """找到两个数的和等于目标值"""
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []  # 未找到

# 测试
numbers = [2, 7, 11, 15]
target = 9
result = two_sum(numbers, target)
print(f"数组: {numbers}, 目标: {target}")
print(f"结果索引: {result}")
if result:
    print(f"两个数: {numbers[result[0]]}, {numbers[result[1]]}")
```

### 5. 移动零

```python
def move_zeros(nums):
    """将所有0移动到数组末尾"""
    # 双指针方法
    left = 0  # 指向下一个非零元素应该放置的位置
    
    # 将所有非零元素移到前面
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    
    return nums

# 测试
array = [0, 1, 0, 3, 12]
print(f"原数组: {array}")
move_zeros(array)
print(f"移动后: {array}")
```

## 数据处理练习

### 1. 统计词频

```python
def word_frequency(text):
    """统计文本中单词的频率"""
    # 清理文本并分割单词
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    
    # 统计频率
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    # 按频率排序
    sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq

# 测试
text = "Python is great. Python is powerful. Python is easy to learn."
freq = word_frequency(text)
print(f"文本: {text}")
print("词频统计:")
for word, count in freq:
    print(f"  {word}: {count}")
```

### 2. 数据分组和聚合

```python
def group_and_aggregate(data, group_by, aggregate_field):
    """按指定字段分组并聚合"""
    groups = {}
    for item in data:
        key = item[group_by]
        if key not in groups:
            groups[key] = []
        groups[key].append(item[aggregate_field])
    
    # 计算每组的统计信息
    result = {}
    for key, values in groups.items():
        result[key] = {
            'count': len(values),
            'sum': sum(values),
            'avg': sum(values) / len(values),
            'min': min(values),
            'max': max(values)
        }
    return result

# 测试数据
sales_data = [
    {'product': 'A', 'region': 'North', 'sales': 100},
    {'product': 'B', 'region': 'North', 'sales': 150},
    {'product': 'A', 'region': 'South', 'sales': 200},
    {'product': 'B', 'region': 'South', 'sales': 120},
    {'product': 'A', 'region': 'North', 'sales': 80},
]

# 按产品分组
product_stats = group_and_aggregate(sales_data, 'product', 'sales')
print("按产品分组的销售统计:")
for product, stats in product_stats.items():
    print(f"  产品{product}: 总销售={stats['sum']}, 平均={stats['avg']:.1f}")
```

### 3. 数据清洗

```python
def clean_data(data):
    """清洗数据"""
    cleaned = []
    
    for record in data:
        # 清洗姓名
        name = record['name'].strip()
        if not name:
            continue  # 跳过空姓名
        
        # 清洗年龄
        try:
            age = int(record['age']) if record['age'] else None
            if age and (age < 0 or age > 150):
                age = None
        except ValueError:
            age = None
        
        # 清洗邮箱
        email = record['email']
        if '@' not in email or '.' not in email:
            email = None
        
        cleaned_record = {
            'name': name,
            'age': age,
            'email': email
        }
        cleaned.append(cleaned_record)
    
    return cleaned

# 测试数据
raw_data = [
    {'name': '  Alice  ', 'age': '25', 'email': 'alice@email.com'},
    {'name': 'Bob', 'age': '', 'email': 'invalid-email'},
    {'name': '', 'age': '30', 'email': 'charlie@email.com'},
    {'name': 'Diana', 'age': 'invalid', 'email': 'diana@email.com'},
    {'name': 'Eve', 'age': '28', 'email': 'eve@email.com'}
]

cleaned_data = clean_data(raw_data)
print("清洗后数据:")
for record in cleaned_data:
    print(f"  {record}")
```

## 挑战题目

### 1. LRU缓存实现

```python
class LRUCache:
    """LRU（最近最少使用）缓存实现"""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []  # 使用列表模拟，实际应用中使用双向链表+哈希表更高效
        self.data = {}
    
    def get(self, key):
        if key in self.data:
            # 移动到最前面（最近使用）
            self.cache.remove(key)
            self.cache.append(key)
            return self.data[key]
        return -1
    
    def put(self, key, value):
        if key in self.data:
            # 更新现有键
            self.cache.remove(key)
            self.cache.append(key)
            self.data[key] = value
        else:
            # 添加新键
            if len(self.cache) >= self.capacity:
                # 移除最久未使用的
                oldest = self.cache.pop(0)
                del self.data[oldest]
            
            self.cache.append(key)
            self.data[key] = value
    
    def display(self):
        print(f"缓存状态: {[(k, self.data[k]) for k in self.cache]}")

# 测试LRU缓存
lru = LRUCache(3)
lru.put(1, 'A')
lru.put(2, 'B')
lru.put(3, 'C')
lru.display()

print(f"获取键1: {lru.get(1)}")
lru.display()

lru.put(4, 'D')  # 应该移除键2
lru.display()
```

### 2. 表达式求值

```python
def evaluate_expression(expression):
    """计算简单的数学表达式"""
    # 移除空格
    expression = expression.replace(' ', '')
    
    # 使用两个栈：数字栈和操作符栈
    numbers = []
    operators = []
    i = 0
    
    def precedence(op):
        if op in ['+', '-']:
            return 1
        if op in ['*', '/']:
            return 2
        return 0
    
    def apply_operator():
        if len(numbers) < 2 or not operators:
            return
        
        b = numbers.pop()
        a = numbers.pop()
        op = operators.pop()
        
        if op == '+':
            numbers.append(a + b)
        elif op == '-':
            numbers.append(a - b)
        elif op == '*':
            numbers.append(a * b)
        elif op == '/':
            numbers.append(a / b)
    
    while i < len(expression):
        char = expression[i]
        
        if char.isdigit():
            # 读取完整的数字
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            numbers.append(num)
            i -= 1
        
        elif char in ['+', '-', '*', '/']:
            # 处理操作符优先级
            while (operators and 
                   precedence(operators[-1]) >= precedence(char)):
                apply_operator()
            operators.append(char)
        
        elif char == '(':
            operators.append(char)
        
        elif char == ')':
            while operators and operators[-1] != '(':
                apply_operator()
            if operators:
                operators.pop()  # 移除 '('
        
        i += 1
    
    # 处理剩余的操作符
    while operators:
        apply_operator()
    
    return numbers[0] if numbers else 0

# 测试表达式求值
expressions = [
    "2 + 3 * 4",
    "(2 + 3) * 4",
    "10 - 2 * 3",
    "(10 - 2) * 3"
]

for expr in expressions:
    result = evaluate_expression(expr)
    print(f"{expr} = {result}")
```

### 3. 数独验证器

```python
def is_valid_sudoku(board):
    """验证9x9数独是否有效"""
    def is_valid_unit(unit):
        # 过滤掉空格，检查是否有重复数字
        unit = [i for i in unit if i != '.']
        return len(unit) == len(set(unit))
    
    # 检查行
    for row in board:
        if not is_valid_unit(row):
            return False
    
    # 检查列
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_unit(column):
            return False
    
    # 检查3x3方格
    for box_row in range(3):
        for box_col in range(3):
            box = []
            for row in range(box_row * 3, (box_row + 1) * 3):
                for col in range(box_col * 3, (box_col + 1) * 3):
                    box.append(board[row][col])
            if not is_valid_unit(box):
                return False
    
    return True

# 测试数独
valid_sudoku = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

result = is_valid_sudoku(valid_sudoku)
print(f"数独验证结果: {'有效' if result else '无效'}")
```

## 学习要点

### 关键概念

1. **列表操作的时间复杂度**
   - 访问元素：O(1)
   - 搜索元素：O(n)
   - 插入/删除（末尾）：O(1)
   - 插入/删除（中间）：O(n)

2. **算法设计思想**
   - 分治法：归并排序、快速排序
   - 动态规划：最大子数组和
   - 双指针：两数之和、移动零
   - 贪心算法：区间调度

3. **数据结构选择**
   - 列表：适合频繁访问和修改
   - 集合：适合去重和成员检查
   - 字典：适合键值对映射

### 最佳实践

1. **性能优化**
   - 使用列表推导式而不是循环
   - 避免在循环中频繁修改列表大小
   - 选择合适的数据结构

2. **代码质量**
   - 编写清晰的函数文档
   - 使用有意义的变量名
   - 添加适当的错误处理

3. **测试和调试**
   - 编写测试用例
   - 使用断言验证结果
   - 逐步调试复杂算法

### 常见陷阱

1. **列表修改陷阱**
   - 在遍历时修改列表
   - 浅拷贝vs深拷贝
   - 列表作为默认参数

2. **性能陷阱**
   - 嵌套循环的时间复杂度
   - 不必要的列表复制
   - 频繁的字符串连接

3. **逻辑陷阱**
   - 边界条件处理
   - 空列表的特殊情况
   - 索引越界错误

## 练习建议

### 基础练习
1. 完成所有基础操作练习
2. 熟练掌握列表推导式
3. 练习嵌套列表操作

### 进阶练习
1. 实现常见排序算法
2. 解决经典算法问题
3. 设计数据结构

### 项目实践
1. 开发完整的管理系统
2. 处理真实数据集
3. 优化算法性能

### 挑战目标
1. 参加编程竞赛
2. 贡献开源项目
3. 学习高级数据结构

通过这些综合练习，你将全面掌握Python列表的使用，并培养出色的编程思维和问题解决能力。记住，编程是一门实践性很强的技能，多练习、多思考、多总结是提高的关键！