#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
列表综合练习 - 实战项目和练习题

本文件包含了Python列表的综合练习和实战项目：
1. 基础练习题
2. 进阶练习题
3. 实战项目
4. 算法练习
5. 数据处理练习
6. 挑战题目

作者：Python学习教程
日期：2024年
"""

def basic_exercises():
    """基础练习题"""
    print("=== 基础练习题 ===")
    
    # 练习1：创建和操作列表
    print("练习1：列表基本操作")
    numbers = [1, 2, 3, 4, 5]
    print(f"原列表: {numbers}")
    
    # 添加元素
    numbers.append(6)
    numbers.insert(0, 0)
    print(f"添加元素后: {numbers}")
    
    # 删除元素
    numbers.remove(3)
    popped = numbers.pop()
    print(f"删除元素后: {numbers}, 弹出的元素: {popped}")
    
    # 练习2：列表切片
    print("\n练习2：列表切片")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(f"原列表: {alphabet}")
    print(f"前3个元素: {alphabet[:3]}")
    print(f"后3个元素: {alphabet[-3:]}")
    print(f"每隔一个元素: {alphabet[::2]}")
    print(f"反转列表: {alphabet[::-1]}")
    
    # 练习3：列表方法
    print("\n练习3：列表方法应用")
    fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(f"水果列表: {fruits}")
    print(f"apple出现次数: {fruits.count('apple')}")
    print(f"banana第一次出现的索引: {fruits.index('banana')}")
    
    # 排序
    fruits_copy = fruits.copy()
    fruits_copy.sort()
    print(f"排序后: {fruits_copy}")
    
    # 练习4：列表推导式基础
    print("\n练习4：列表推导式")
    numbers = list(range(1, 11))
    squares = [x**2 for x in numbers]
    evens = [x for x in numbers if x % 2 == 0]
    print(f"数字: {numbers}")
    print(f"平方: {squares}")
    print(f"偶数: {evens}")

def intermediate_exercises():
    """进阶练习题"""
    print("\n=== 进阶练习题 ===")
    
    # 练习1：查找列表中的重复元素
    print("练习1：查找重复元素")
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
    
    test_list = [1, 2, 3, 2, 4, 5, 3, 6, 1]
    duplicates = find_duplicates(test_list)
    print(f"原列表: {test_list}")
    print(f"重复元素: {duplicates}")
    
    # 练习2：列表去重并保持顺序
    print("\n练习2：去重保持顺序")
    def remove_duplicates_keep_order(lst):
        """去重并保持原有顺序"""
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    original = [1, 2, 3, 2, 4, 1, 5, 3, 6]
    unique = remove_duplicates_keep_order(original)
    print(f"原列表: {original}")
    print(f"去重后: {unique}")
    
    # 练习3：列表分组
    print("\n练习3：列表分组")
    def group_by_length(words):
        """按长度分组单词"""
        groups = {}
        for word in words:
            length = len(word)
            if length not in groups:
                groups[length] = []
            groups[length].append(word)
        return groups
    
    words = ['cat', 'dog', 'elephant', 'bird', 'fish', 'butterfly']
    grouped = group_by_length(words)
    print(f"单词列表: {words}")
    print("按长度分组:")
    for length, word_list in sorted(grouped.items()):
        print(f"  长度{length}: {word_list}")
    
    # 练习4：列表旋转
    print("\n练习4：列表旋转")
    def rotate_list(lst, k):
        """向右旋转列表k个位置"""
        if not lst or k == 0:
            return lst
        k = k % len(lst)  # 处理k大于列表长度的情况
        return lst[-k:] + lst[:-k]
    
    original = [1, 2, 3, 4, 5, 6, 7]
    rotated = rotate_list(original, 3)
    print(f"原列表: {original}")
    print(f"右旋转3位: {rotated}")
    
    # 练习5：合并有序列表
    print("\n练习5：合并有序列表")
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
    
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 6, 8, 10, 11, 12]
    merged = merge_sorted_lists(list1, list2)
    print(f"列表1: {list1}")
    print(f"列表2: {list2}")
    print(f"合并后: {merged}")

def practical_projects():
    """实战项目"""
    print("\n=== 实战项目 ===")
    
    # 项目1：学生成绩管理系统
    print("项目1：学生成绩管理系统")
    
    class GradeManager:
        def __init__(self):
            self.students = []
        
        def add_student(self, name, grades):
            """添加学生"""
            self.students.append({'name': name, 'grades': grades})
        
        def calculate_average(self, name):
            """计算学生平均分"""
            for student in self.students:
                if student['name'] == name:
                    return sum(student['grades']) / len(student['grades'])
            return None
        
        def get_class_average(self):
            """计算班级平均分"""
            all_grades = []
            for student in self.students:
                all_grades.extend(student['grades'])
            return sum(all_grades) / len(all_grades) if all_grades else 0
        
        def get_top_students(self, n=3):
            """获取前n名学生"""
            student_averages = []
            for student in self.students:
                avg = sum(student['grades']) / len(student['grades'])
                student_averages.append((student['name'], avg))
            
            student_averages.sort(key=lambda x: x[1], reverse=True)
            return student_averages[:n]
        
        def display_report(self):
            """显示成绩报告"""
            print("  成绩报告:")
            for student in self.students:
                avg = sum(student['grades']) / len(student['grades'])
                print(f"    {student['name']}: {student['grades']} (平均分: {avg:.1f})")
            
            print(f"    班级平均分: {self.get_class_average():.1f}")
            
            top_students = self.get_top_students()
            print("    前三名:")
            for i, (name, avg) in enumerate(top_students, 1):
                print(f"      {i}. {name}: {avg:.1f}")
    
    # 使用成绩管理系统
    gm = GradeManager()
    gm.add_student('Alice', [85, 92, 78, 96])
    gm.add_student('Bob', [88, 85, 90, 87])
    gm.add_student('Charlie', [92, 89, 94, 91])
    gm.add_student('Diana', [76, 82, 79, 85])
    gm.display_report()
    
    # 项目2：购物清单管理器
    print("\n项目2：购物清单管理器")
    
    class ShoppingList:
        def __init__(self):
            self.items = []
        
        def add_item(self, item, quantity=1, price=0):
            """添加商品"""
            for existing_item in self.items:
                if existing_item['name'] == item:
                    existing_item['quantity'] += quantity
                    return
            self.items.append({'name': item, 'quantity': quantity, 'price': price})
        
        def remove_item(self, item):
            """删除商品"""
            self.items = [i for i in self.items if i['name'] != item]
        
        def update_quantity(self, item, quantity):
            """更新数量"""
            for existing_item in self.items:
                if existing_item['name'] == item:
                    existing_item['quantity'] = quantity
                    break
        
        def calculate_total(self):
            """计算总价"""
            return sum(item['price'] * item['quantity'] for item in self.items)
        
        def display_list(self):
            """显示购物清单"""
            print("  购物清单:")
            if not self.items:
                print("    清单为空")
                return
            
            for item in self.items:
                total_price = item['price'] * item['quantity']
                print(f"    {item['name']}: {item['quantity']}个 x ${item['price']} = ${total_price}")
            
            print(f"    总计: ${self.calculate_total()}")
        
        def sort_by_price(self):
            """按价格排序"""
            self.items.sort(key=lambda x: x['price'], reverse=True)
        
        def get_expensive_items(self, threshold):
            """获取价格超过阈值的商品"""
            return [item for item in self.items if item['price'] > threshold]
    
    # 使用购物清单管理器
    shopping = ShoppingList()
    shopping.add_item('苹果', 5, 2.5)
    shopping.add_item('牛奶', 2, 3.8)
    shopping.add_item('面包', 1, 4.2)
    shopping.add_item('鸡蛋', 12, 0.5)
    shopping.display_list()
    
    print("\n  按价格排序后:")
    shopping.sort_by_price()
    shopping.display_list()
    
    expensive_items = shopping.get_expensive_items(3.0)
    print(f"\n  价格超过$3的商品: {[item['name'] for item in expensive_items]}")
    
    # 项目3：简单的任务管理器
    print("\n项目3：任务管理器")
    
    class TaskManager:
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
            return task['id']
        
        def complete_task(self, task_id):
            """完成任务"""
            for task in self.tasks:
                if task['id'] == task_id:
                    task['completed'] = True
                    return True
            return False
        
        def get_pending_tasks(self):
            """获取待完成任务"""
            return [task for task in self.tasks if not task['completed']]
        
        def get_completed_tasks(self):
            """获取已完成任务"""
            return [task for task in self.tasks if task['completed']]
        
        def get_tasks_by_priority(self, priority):
            """按优先级获取任务"""
            return [task for task in self.tasks if task['priority'] == priority]
        
        def display_tasks(self):
            """显示所有任务"""
            print("  任务列表:")
            if not self.tasks:
                print("    没有任务")
                return
            
            pending = self.get_pending_tasks()
            completed = self.get_completed_tasks()
            
            print(f"    待完成任务 ({len(pending)}个):")
            for task in pending:
                status = "✓" if task['completed'] else "○"
                print(f"      {status} [{task['id']}] {task['description']} ({task['priority']})")
            
            print(f"    已完成任务 ({len(completed)}个):")
            for task in completed:
                status = "✓" if task['completed'] else "○"
                print(f"      {status} [{task['id']}] {task['description']} ({task['priority']})")
    
    # 使用任务管理器
    tm = TaskManager()
    tm.add_task('完成Python作业', 'high')
    tm.add_task('买菜', 'medium')
    tm.add_task('看电影', 'low')
    tm.add_task('健身', 'medium')
    
    tm.display_tasks()
    
    # 完成一些任务
    tm.complete_task(1)
    tm.complete_task(3)
    
    print("\n  完成部分任务后:")
    tm.display_tasks()
    
    high_priority = tm.get_tasks_by_priority('high')
    print(f"\n  高优先级任务: {[task['description'] for task in high_priority]}")

def algorithm_exercises():
    """算法练习"""
    print("\n=== 算法练习 ===")
    
    # 练习1：冒泡排序
    print("练习1：冒泡排序")
    def bubble_sort(arr):
        """冒泡排序实现"""
        n = len(arr)
        arr = arr.copy()  # 不修改原数组
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    unsorted = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(unsorted)
    print(f"  原数组: {unsorted}")
    print(f"  排序后: {sorted_arr}")
    
    # 练习2：二分查找
    print("\n练习2：二分查找")
    def binary_search(arr, target):
        """二分查找实现"""
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    index = binary_search(sorted_list, target)
    print(f"  有序数组: {sorted_list}")
    print(f"  查找{target}: 索引{index}")
    
    # 练习3：最大子数组和（Kadane算法）
    print("\n练习3：最大子数组和")
    def max_subarray_sum(arr):
        """找到最大子数组和"""
        max_sum = float('-inf')
        current_sum = 0
        start = end = temp_start = 0
        
        for i, num in enumerate(arr):
            current_sum += num
            
            if current_sum > max_sum:
                max_sum = current_sum
                start = temp_start
                end = i
            
            if current_sum < 0:
                current_sum = 0
                temp_start = i + 1
        
        return max_sum, arr[start:end + 1]
    
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, subarray = max_subarray_sum(array)
    print(f"  数组: {array}")
    print(f"  最大子数组: {subarray}")
    print(f"  最大和: {max_sum}")
    
    # 练习4：两数之和
    print("\n练习4：两数之和")
    def two_sum(nums, target):
        """找到两个数的索引，使其和等于目标值"""
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
    
    numbers = [2, 7, 11, 15]
    target_sum = 9
    indices = two_sum(numbers, target_sum)
    print(f"  数组: {numbers}")
    print(f"  目标和: {target_sum}")
    if indices:
        print(f"  索引: {indices}, 值: [{numbers[indices[0]]}, {numbers[indices[1]]}]")
    
    # 练习5：移动零
    print("\n练习5：移动零")
    def move_zeros(nums):
        """将所有0移动到数组末尾"""
        nums = nums.copy()
        write_index = 0
        
        # 将非零元素移到前面
        for read_index in range(len(nums)):
            if nums[read_index] != 0:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        # 填充剩余位置为0
        while write_index < len(nums):
            nums[write_index] = 0
            write_index += 1
        
        return nums
    
    original = [0, 1, 0, 3, 12]
    moved = move_zeros(original)
    print(f"  原数组: {original}")
    print(f"  移动后: {moved}")

def data_processing_exercises():
    """数据处理练习"""
    print("\n=== 数据处理练习 ===")
    
    # 练习1：统计词频
    print("练习1：统计词频")
    def word_frequency(text):
        """统计文本中单词的频率"""
        # 简单的文本处理
        words = text.lower().replace(',', '').replace('.', '').split()
        frequency = {}
        
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        
        # 按频率排序
        sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        return sorted_freq
    
    text = "Python is great. Python is powerful. Python is easy to learn."
    freq = word_frequency(text)
    print(f"  文本: {text}")
    print("  词频统计:")
    for word, count in freq:
        print(f"    {word}: {count}")
    
    # 练习2：数据分组和聚合
    print("\n练习2：数据分组和聚合")
    sales_data = [
        {'product': 'A', 'region': 'North', 'sales': 100},
        {'product': 'B', 'region': 'North', 'sales': 150},
        {'product': 'A', 'region': 'South', 'sales': 200},
        {'product': 'B', 'region': 'South', 'sales': 120},
        {'product': 'A', 'region': 'North', 'sales': 80},
    ]
    
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
    
    # 按产品分组
    product_stats = group_and_aggregate(sales_data, 'product', 'sales')
    print("  按产品分组的销售统计:")
    for product, stats in product_stats.items():
        print(f"    产品{product}: 总销售={stats['sum']}, 平均={stats['avg']:.1f}, 次数={stats['count']}")
    
    # 按地区分组
    region_stats = group_and_aggregate(sales_data, 'region', 'sales')
    print("  按地区分组的销售统计:")
    for region, stats in region_stats.items():
        print(f"    {region}: 总销售={stats['sum']}, 平均={stats['avg']:.1f}, 次数={stats['count']}")
    
    # 练习3：数据清洗
    print("\n练习3：数据清洗")
    raw_data = [
        {'name': '  Alice  ', 'age': '25', 'email': 'alice@email.com'},
        {'name': 'Bob', 'age': '', 'email': 'invalid-email'},
        {'name': '', 'age': '30', 'email': 'charlie@email.com'},
        {'name': 'Diana', 'age': 'invalid', 'email': 'diana@email.com'},
        {'name': 'Eve', 'age': '28', 'email': 'eve@email.com'}
    ]
    
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
    
    cleaned_data = clean_data(raw_data)
    print("  原始数据:")
    for record in raw_data:
        print(f"    {record}")
    
    print("  清洗后数据:")
    for record in cleaned_data:
        print(f"    {record}")
    
    # 练习4：数据透视
    print("\n练习4：数据透视")
    transaction_data = [
        {'date': '2024-01', 'category': 'Food', 'amount': 100},
        {'date': '2024-01', 'category': 'Transport', 'amount': 50},
        {'date': '2024-02', 'category': 'Food', 'amount': 120},
        {'date': '2024-02', 'category': 'Transport', 'amount': 60},
        {'date': '2024-01', 'category': 'Entertainment', 'amount': 80},
        {'date': '2024-02', 'category': 'Entertainment', 'amount': 90},
    ]
    
    def create_pivot_table(data, row_field, col_field, value_field):
        """创建数据透视表"""
        # 获取所有唯一的行和列值
        rows = sorted(set(record[row_field] for record in data))
        cols = sorted(set(record[col_field] for record in data))
        
        # 创建透视表
        pivot = {}
        for row in rows:
            pivot[row] = {col: 0 for col in cols}
        
        # 填充数据
        for record in data:
            row_val = record[row_field]
            col_val = record[col_field]
            value = record[value_field]
            pivot[row_val][col_val] += value
        
        return pivot, rows, cols
    
    pivot_table, dates, categories = create_pivot_table(
        transaction_data, 'date', 'category', 'amount'
    )
    
    print("  交易数据透视表:")
    print(f"    {'Date':<10}", end='')
    for category in categories:
        print(f"{category:>12}", end='')
    print(f"{'Total':>12}")
    
    for date in dates:
        print(f"    {date:<10}", end='')
        row_total = 0
        for category in categories:
            amount = pivot_table[date][category]
            print(f"{amount:>12}", end='')
            row_total += amount
        print(f"{row_total:>12}")
    
    # 计算列总计
    print(f"    {'Total':<10}", end='')
    grand_total = 0
    for category in categories:
        col_total = sum(pivot_table[date][category] for date in dates)
        print(f"{col_total:>12}", end='')
        grand_total += col_total
    print(f"{grand_total:>12}")

def challenge_problems():
    """挑战题目"""
    print("\n=== 挑战题目 ===")
    
    # 挑战1：实现LRU缓存
    print("挑战1：LRU缓存实现")
    class LRUCache:
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
            print(f"    缓存状态: {[(k, self.data[k]) for k in self.cache]}")
    
    # 测试LRU缓存
    lru = LRUCache(3)
    lru.put(1, 'A')
    lru.put(2, 'B')
    lru.put(3, 'C')
    lru.display()
    
    print(f"    获取键1: {lru.get(1)}")
    lru.display()
    
    lru.put(4, 'D')  # 应该移除键2
    lru.display()
    
    # 挑战2：表达式求值
    print("\n挑战2：表达式求值")
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
    
    expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "10 - 2 * 3",
        "(10 - 2) * 3"
    ]
    
    for expr in expressions:
        result = evaluate_expression(expr)
        print(f"    {expr} = {result}")
    
    # 挑战3：数独验证器
    print("\n挑战3：数独验证器")
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
    print(f"    数独验证结果: {'有效' if result else '无效'}")

def main():
    """主函数，运行所有练习"""
    print("Python列表综合练习")
    print("=" * 50)
    
    basic_exercises()
    intermediate_exercises()
    practical_projects()
    algorithm_exercises()
    data_processing_exercises()
    challenge_problems()
    
    print("\n=== 练习总结 ===")
    print("通过这些练习，你应该掌握了:")
    print("\n基础技能:")
    print("- 列表的创建、访问、修改和删除")
    print("- 列表方法的熟练使用")
    print("- 列表推导式的各种应用")
    print("- 嵌套列表的处理")
    print("\n进阶技能:")
    print("- 复杂数据结构的设计和操作")
    print("- 算法的实现和优化")
    print("- 数据处理和分析")
    print("- 实际项目的开发")
    print("\n实战能力:")
    print("- 学生成绩管理系统")
    print("- 购物清单管理器")
    print("- 任务管理系统")
    print("- 数据清洗和分析")
    print("\n算法思维:")
    print("- 排序和搜索算法")
    print("- 动态规划思想")
    print("- 数据结构设计")
    print("- 问题分解和解决")
    print("\n继续学习建议:")
    print("- 尝试更复杂的算法实现")
    print("- 学习NumPy进行数值计算")
    print("- 学习Pandas进行数据分析")
    print("- 参与开源项目实践")

if __name__ == "__main__":
    main()