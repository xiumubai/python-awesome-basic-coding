#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
循环控制 - else子句

Python中的for和while循环都可以有else子句。
else子句只在循环正常结束时执行，如果循环被break中断则不执行。

学习目标：
1. 理解循环else子句的执行条件
2. 掌握for-else和while-else的使用
3. 了解else子句与break的关系
4. 学会在实际场景中应用else子句
"""

# 1. 基本的else子句使用
print("=== 1. 基本的else子句使用 ===")

# for循环的else子句
print("for循环正常结束:")
for i in range(3):
    print(f"循环: {i}")
else:
    print("for循环正常结束，执行else子句")
print()

# while循环的else子句
print("while循环正常结束:")
count = 0
while count < 3:
    print(f"while循环: {count}")
    count += 1
else:
    print("while循环正常结束，执行else子句")
print()

# 2. break对else子句的影响
print("=== 2. break对else子句的影响 ===")

# 被break中断的for循环
print("被break中断的for循环:")
for i in range(5):
    if i == 2:
        print(f"在i={i}时break")
        break
    print(f"循环: {i}")
else:
    print("这行不会执行，因为循环被break中断")
print("for循环结束\n")

# 被break中断的while循环
print("被break中断的while循环:")
count = 0
while count < 5:
    if count == 2:
        print(f"在count={count}时break")
        break
    print(f"while循环: {count}")
    count += 1
else:
    print("这行不会执行，因为循环被break中断")
print("while循环结束\n")

# 3. continue对else子句的影响
print("=== 3. continue对else子句的影响 ===")

# continue不影响else子句的执行
print("包含continue的循环:")
for i in range(5):
    if i == 2:
        print(f"跳过i={i}")
        continue
    print(f"处理: {i}")
else:
    print("循环正常结束，else子句执行（continue不影响else）")
print()

# 4. 实际应用场景 - 查找元素
print("=== 4. 实际应用场景 - 查找元素 ===")

# 场景1: 查找特定元素
print("查找特定元素:")
numbers = [1, 3, 5, 7, 9]
target = 6

for num in numbers:
    if num == target:
        print(f"找到目标数字: {target}")
        break
    print(f"检查: {num}")
else:
    print(f"未找到目标数字: {target}")
print()

# 场景2: 查找存在的元素
print("查找存在的元素:")
numbers = [1, 3, 5, 7, 9]
target = 5

for num in numbers:
    if num == target:
        print(f"找到目标数字: {target}")
        break
    print(f"检查: {num}")
else:
    print(f"未找到目标数字: {target}")
print()

# 5. 验证和检查场景
print("=== 5. 验证和检查场景 ===")

# 检查所有元素是否满足条件
print("检查所有数字是否为正数:")
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num <= 0:
        print(f"发现非正数: {num}")
        break
    print(f"检查正数: {num}")
else:
    print("所有数字都是正数！")
print()

# 包含负数的情况
print("包含负数的情况:")
numbers = [1, 2, -3, 4, 5]

for num in numbers:
    if num <= 0:
        print(f"发现非正数: {num}")
        break
    print(f"检查正数: {num}")
else:
    print("所有数字都是正数！")
print()

# 6. 用户输入验证
print("=== 6. 用户输入验证 ===")

# 模拟用户输入验证
print("密码尝试验证:")
passwords = ['123', 'password', 'wrong']
correct_password = 'admin'
max_attempts = 3

for attempt in range(max_attempts):
    # 模拟用户输入
    if attempt < len(passwords):
        user_input = passwords[attempt]
    else:
        user_input = 'timeout'
    
    print(f"尝试 {attempt + 1}: {user_input}")
    
    if user_input == correct_password:
        print("密码正确，登录成功！")
        break
    else:
        print("密码错误")
else:
    print("达到最大尝试次数，账户被锁定")
print()

# 7. 数据处理和验证
print("=== 7. 数据处理和验证 ===")

# 处理配置文件
print("验证配置文件:")
config_lines = [
    "host=localhost",
    "port=8080",
    "debug=true",
    "timeout=30"
]

required_keys = ['host', 'port', 'debug']

for key in required_keys:
    found = False
    for line in config_lines:
        if line.startswith(f"{key}="):
            print(f"找到配置: {line}")
            found = True
            break
    
    if not found:
        print(f"缺少必需的配置: {key}")
        break
else:
    print("所有必需的配置都存在，配置文件有效！")
print()

# 8. 复杂的搜索场景
print("=== 8. 复杂的搜索场景 ===")

# 在嵌套结构中搜索
print("在学生成绩中查找不及格:")
students = [
    {'name': 'Alice', 'scores': [85, 92, 78]},
    {'name': 'Bob', 'scores': [76, 88, 95]},
    {'name': 'Charlie', 'scores': [90, 87, 93]}
]

for student in students:
    print(f"检查学生: {student['name']}")
    for score in student['scores']:
        if score < 60:
            print(f"  发现不及格分数: {score}")
            break
    else:
        print(f"  {student['name']} 所有成绩都及格")
        continue
    print(f"  {student['name']} 有不及格成绩")
print()

# 9. while-else的实际应用
print("=== 9. while-else的实际应用 ===")

# 等待条件满足
print("模拟等待网络连接:")
max_retries = 5
retry_count = 0
connection_success = False

# 模拟连接尝试
connection_attempts = [False, False, True]  # 第3次成功

while retry_count < max_retries:
    print(f"尝试连接... (第{retry_count + 1}次)")
    
    # 模拟连接结果
    if retry_count < len(connection_attempts):
        connection_success = connection_attempts[retry_count]
    else:
        connection_success = False
    
    if connection_success:
        print("连接成功！")
        break
    
    retry_count += 1
    print("连接失败，重试...")
else:
    print("达到最大重试次数，连接失败")
print()

# 10. else子句的最佳实践
print("=== 10. else子句的最佳实践 ===")

# 使用else子句简化代码逻辑
print("简化的素数检查:")
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} 不是素数，因为 {n} % {i} == 0")
            return False
    else:
        print(f"{n} 是素数")
        return True

# 测试素数检查
test_numbers = [7, 8, 17, 20]
for num in test_numbers:
    result = is_prime(num)
    print(f"{num}: {'是' if result else '不是'}素数\n")

# 使用else子句处理异常情况
print("处理文件查找:")
filenames = ['config.txt', 'data.csv', 'log.txt']
target_file = 'settings.ini'

for filename in filenames:
    print(f"检查文件: {filename}")
    if filename == target_file:
        print(f"找到目标文件: {target_file}")
        break
else:
    print(f"未找到目标文件: {target_file}，使用默认配置")

print("\n=== else子句学习总结 ===")
print("1. else子句只在循环正常结束时执行")
print("2. 被break中断的循环不会执行else子句")
print("3. continue不影响else子句的执行")
print("4. 常用于搜索、验证、异常处理场景")
print("5. 可以简化代码逻辑，避免额外的标志变量")
print("6. for-else和while-else的行为完全一致")