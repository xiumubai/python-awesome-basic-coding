# continue语句的使用

continue语句用于跳过当前循环迭代中剩余的代码，直接进入下一次循环迭代。与break不同，continue不会退出循环，而是继续执行循环。

## 基本语法和作用

continue语句的语法：

```python
continue
```

### 基本示例

```python
# 在for循环中使用continue
for i in range(10):
    if i % 2 == 0:  # 跳过偶数
        continue
    print(f"奇数: {i}")

# 输出：
# 奇数: 1
# 奇数: 3
# 奇数: 5
# 奇数: 7
# 奇数: 9
```

```python
# 在while循环中使用continue
count = 0
while count < 10:
    count += 1
    if count % 3 == 0:  # 跳过3的倍数
        continue
    print(f"数字: {count}")

# 输出：
# 数字: 1
# 数字: 2
# 数字: 4
# 数字: 5
# 数字: 7
# 数字: 8
# 数字: 10
```

## continue与break的区别

```python
# 对比continue和break的行为
print("使用continue:")
for i in range(5):
    if i == 2:
        continue  # 跳过i=2，继续下一次迭代
    print(f"continue示例: {i}")

print("\n使用break:")
for i in range(5):
    if i == 2:
        break  # 在i=2时退出整个循环
    print(f"break示例: {i}")

# 输出：
# 使用continue:
# continue示例: 0
# continue示例: 1
# continue示例: 3
# continue示例: 4
# 
# 使用break:
# break示例: 0
# break示例: 1
```

## 实际应用场景

### 1. 数据过滤

```python
# 处理学生成绩，跳过无效数据
scores = [85, -1, 92, 78, 150, 88, 0, 95]
valid_scores = []
total = 0
count = 0

for score in scores:
    # 跳过无效成绩（负数或超过100分）
    if score < 0 or score > 100:
        print(f"跳过无效成绩: {score}")
        continue
    
    # 跳过0分（可能是缺考）
    if score == 0:
        print("跳过缺考学生")
        continue
    
    valid_scores.append(score)
    total += score
    count += 1

if count > 0:
    average = total / count
    print(f"有效成绩: {valid_scores}")
    print(f"平均分: {average:.2f}")
```

### 2. 字符串处理

```python
# 处理文本，跳过空行和注释行
text_lines = [
    "# 这是注释",
    "print('Hello')",
    "",
    "x = 10",
    "# 另一个注释",
    "print(x)",
    "   ",  # 只有空格的行
    "y = 20"
]

print("处理后的代码行:")
for line in text_lines:
    # 跳过空行
    if not line.strip():
        continue
    
    # 跳过注释行
    if line.strip().startswith('#'):
        continue
    
    print(f"代码: {line}")

# 输出：
# 处理后的代码行:
# 代码: print('Hello')
# 代码: x = 10
# 代码: print(x)
# 代码: y = 20
```

### 3. 用户输入处理

```python
# 收集有效的用户输入
valid_numbers = []
max_attempts = 5

print("请输入5个正整数:")
for attempt in range(max_attempts):
    try:
        user_input = input(f"输入第{attempt + 1}个数字: ")
        
        # 跳过空输入
        if not user_input.strip():
            print("输入为空，请重新输入")
            continue
        
        number = int(user_input)
        
        # 跳过非正数
        if number <= 0:
            print("请输入正整数")
            continue
        
        valid_numbers.append(number)
        print(f"已接受: {number}")
        
    except ValueError:
        print("输入无效，请输入数字")
        continue

print(f"收集到的有效数字: {valid_numbers}")
```

### 4. 文件处理

```python
# 处理多个文件，跳过无法访问的文件
import os

filenames = ['file1.txt', 'file2.txt', 'nonexistent.txt', 'file3.txt']
processed_files = []

for filename in filenames:
    # 跳过不存在的文件
    if not os.path.exists(filename):
        print(f"文件 {filename} 不存在，跳过")
        continue
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            
            # 跳过空文件
            if not content.strip():
                print(f"文件 {filename} 为空，跳过")
                continue
            
            # 处理文件内容
            processed_files.append(filename)
            print(f"成功处理文件: {filename}")
            
    except PermissionError:
        print(f"没有权限访问文件 {filename}，跳过")
        continue
    except Exception as e:
        print(f"处理文件 {filename} 时出错: {e}，跳过")
        continue

print(f"成功处理的文件: {processed_files}")
```

## 嵌套循环中的continue

continue只影响最内层的循环：

```python
# continue在嵌套循环中的行为
for i in range(3):
    print(f"外层循环: {i}")
    for j in range(5):
        if j == 2:
            print(f"  内层循环跳过 j={j}")
            continue  # 只跳过内层循环的当前迭代
        print(f"  内层循环: {j}")
    print(f"外层循环 {i} 完成")

# 输出：
# 外层循环: 0
#   内层循环: 0
#   内层循环: 1
#   内层循环跳过 j=2
#   内层循环: 3
#   内层循环: 4
# 外层循环 0 完成
# ...
```

## continue与else子句的关系

continue不会影响循环的else子句执行：

```python
# continue不影响else子句
for i in range(5):
    if i == 2:
        print(f"跳过 {i}")
        continue
    print(f"处理 {i}")
else:
    print("循环正常结束")  # 这行会执行

# 输出：
# 处理 0
# 处理 1
# 跳过 2
# 处理 3
# 处理 4
# 循环正常结束
```

## 代码优化：避免深层嵌套

### 不推荐的写法（深层if-else嵌套）

```python
# 深层嵌套的代码
for item in items:
    if condition1(item):
        if condition2(item):
            if condition3(item):
                # 实际处理逻辑
                process_item(item)
            else:
                print("条件3不满足")
        else:
            print("条件2不满足")
    else:
        print("条件1不满足")
```

### 推荐的写法（使用continue）

```python
# 使用continue减少嵌套
for item in items:
    if not condition1(item):
        print("条件1不满足")
        continue
    
    if not condition2(item):
        print("条件2不满足")
        continue
    
    if not condition3(item):
        print("条件3不满足")
        continue
    
    # 实际处理逻辑
    process_item(item)
```

## 实际应用：数据清洗

```python
# 清洗用户数据
raw_data = [
    {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'},
    {'name': '', 'age': 30, 'email': 'bob@example.com'},  # 姓名为空
    {'name': 'Charlie', 'age': -5, 'email': 'charlie@example.com'},  # 年龄无效
    {'name': 'David', 'age': 35, 'email': 'invalid-email'},  # 邮箱无效
    {'name': 'Eve', 'age': 28, 'email': 'eve@example.com'},
]

clean_data = []

for record in raw_data:
    # 跳过姓名为空的记录
    if not record['name'].strip():
        print(f"跳过姓名为空的记录: {record}")
        continue
    
    # 跳过年龄无效的记录
    if record['age'] <= 0 or record['age'] > 150:
        print(f"跳过年龄无效的记录: {record}")
        continue
    
    # 跳过邮箱格式无效的记录
    if '@' not in record['email'] or '.' not in record['email']:
        print(f"跳过邮箱无效的记录: {record}")
        continue
    
    # 记录有效，添加到清洗后的数据中
    clean_data.append(record)
    print(f"有效记录: {record['name']}")

print(f"\n原始数据: {len(raw_data)} 条")
print(f"清洗后数据: {len(clean_data)} 条")
print(f"清洗后的数据: {clean_data}")
```

## 性能考虑

```python
# 使用continue可以避免不必要的计算
import time

numbers = list(range(1000000))

# 方法1：使用continue（推荐）
start_time = time.time()
result1 = []
for num in numbers:
    if num % 2 == 0:  # 只处理偶数
        continue
    if num % 3 == 0:  # 跳过3的倍数
        continue
    # 复杂的计算只对满足条件的数字执行
    result1.append(num ** 2)
time1 = time.time() - start_time

# 方法2：使用嵌套if（不推荐）
start_time = time.time()
result2 = []
for num in numbers:
    if num % 2 != 0:  # 只处理奇数
        if num % 3 != 0:  # 不是3的倍数
            # 复杂的计算
            result2.append(num ** 2)
time2 = time.time() - start_time

print(f"使用continue的时间: {time1:.4f}秒")
print(f"使用嵌套if的时间: {time2:.4f}秒")
print(f"结果相同: {result1 == result2}")
```

## 最佳实践

### 1. 早期过滤

```python
# 在循环开始就过滤掉不需要的项
for item in items:
    # 早期过滤
    if not is_valid(item):
        continue
    
    # 主要处理逻辑
    process_item(item)
```

### 2. 清晰的条件判断

```python
# 使用有意义的函数名
def should_skip_item(item):
    return item is None or item == '' or not item.isdigit()

for item in items:
    if should_skip_item(item):
        continue
    
    process_item(item)
```

### 3. 记录跳过的原因

```python
# 记录跳过的原因，便于调试
skipped_count = 0
processed_count = 0

for item in items:
    if not item:
        print(f"跳过空项: {item}")
        skipped_count += 1
        continue
    
    if not is_valid_format(item):
        print(f"跳过格式无效的项: {item}")
        skipped_count += 1
        continue
    
    process_item(item)
    processed_count += 1

print(f"处理了 {processed_count} 项，跳过了 {skipped_count} 项")
```

## 学习要点

1. **continue跳过当前迭代**：不是退出循环，而是跳到下一次迭代
2. **只影响最内层循环**：在嵌套循环中要注意作用范围
3. **不影响else子句**：循环仍然可以正常结束并执行else子句
4. **提高代码可读性**：避免深层的if-else嵌套
5. **性能优化**：早期过滤可以避免不必要的计算

## 练习建议

1. 编写一个程序，打印1到100中所有不能被3和5整除的数字
2. 处理一个包含各种数据类型的列表，只处理字符串类型的元素
3. 实现一个简单的日志分析器，跳过空行和注释行
4. 编写一个数据验证程序，跳过不符合格式要求的记录

continue语句是处理数据过滤和条件跳过的强大工具，合理使用可以让代码更加清晰和高效。