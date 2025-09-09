#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lambda表达式与reduce函数

本文件介绍Lambda表达式与reduce函数的结合使用，
学习如何使用reduce函数对序列进行累积计算。

学习目标：
1. 理解reduce函数的工作原理
2. 掌握Lambda表达式与reduce函数的结合使用
3. 学会使用reduce进行累积计算
4. 了解reduce函数的应用场景
"""

from functools import reduce
import operator
import time

# 1. reduce函数基础
print("=== 1. reduce函数基础 ===")
print("reduce函数语法：reduce(function, iterable[, initializer])")
print("作用：对序列中的元素进行累积计算")
print("工作原理：将二元函数累积地应用到序列的元素上")
print("注意：reduce函数在Python 3中需要从functools模块导入")
print()

# 基本使用示例
numbers = [1, 2, 3, 4, 5]

# 计算累积和
sum_result = reduce(lambda x, y: x + y, numbers)
print(f"数字列表: {numbers}")
print(f"累积和: {sum_result}")
print("计算过程: ((((1+2)+3)+4)+5) = 15")

# 计算累积乘积
product_result = reduce(lambda x, y: x * y, numbers)
print(f"累积乘积: {product_result}")
print("计算过程: ((((1*2)*3)*4)*5) = 120")
print()

# 2. reduce的工作原理详解
print("=== 2. reduce的工作原理详解 ===")

# 手动模拟reduce的工作过程
def manual_reduce(func, iterable, initializer=None):
    """手动实现reduce函数的逻辑"""
    it = iter(iterable)
    if initializer is None:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    else:
        value = initializer
    
    for element in it:
        print(f"当前累积值: {value}, 当前元素: {element}")
        value = func(value, element)
        print(f"计算结果: {value}")
    
    return value

print("手动模拟reduce计算过程：")
test_numbers = [10, 20, 30]
result = manual_reduce(lambda x, y: x + y, test_numbers)
print(f"最终结果: {result}")
print()

# 3. 使用初始值的reduce
print("=== 3. 使用初始值的reduce ===")

numbers = [1, 2, 3, 4, 5]

# 不使用初始值
sum_no_init = reduce(lambda x, y: x + y, numbers)
print(f"不使用初始值的和: {sum_no_init}")

# 使用初始值
sum_with_init = reduce(lambda x, y: x + y, numbers, 100)
print(f"使用初始值100的和: {sum_with_init}")

# 空列表使用初始值
empty_list = []
sum_empty = reduce(lambda x, y: x + y, empty_list, 0)
print(f"空列表使用初始值0: {sum_empty}")

# 字符串连接
words = ['Hello', 'World', 'Python']
sentence = reduce(lambda x, y: x + ' ' + y, words)
print(f"单词列表: {words}")
print(f"连接结果: {sentence}")

# 使用初始值的字符串连接
sentence_with_init = reduce(lambda x, y: x + ' ' + y, words, 'Welcome:')
print(f"带初始值的连接: {sentence_with_init}")
print()

# 4. 数学运算应用
print("=== 4. 数学运算应用 ===")

# 计算阶乘
def factorial(n):
    """使用reduce计算阶乘"""
    if n <= 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

print("阶乘计算：")
for i in range(1, 8):
    print(f"{i}! = {factorial(i)}")

# 计算最大公约数
def gcd_two(a, b):
    """计算两个数的最大公约数"""
    while b:
        a, b = b, a % b
    return a

def gcd_multiple(numbers):
    """计算多个数的最大公约数"""
    return reduce(gcd_two, numbers)

numbers_gcd = [48, 18, 24, 12]
print(f"\n数字列表: {numbers_gcd}")
print(f"最大公约数: {gcd_multiple(numbers_gcd)}")

# 计算最小公倍数
def lcm_two(a, b):
    """计算两个数的最小公倍数"""
    return abs(a * b) // gcd_two(a, b)

def lcm_multiple(numbers):
    """计算多个数的最小公倍数"""
    return reduce(lcm_two, numbers)

print(f"最小公倍数: {lcm_multiple(numbers_gcd)}")
print()

# 5. 查找最值
print("=== 5. 查找最值 ===")

numbers = [45, 23, 78, 12, 67, 89, 34, 56]

# 查找最大值
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(f"数字列表: {numbers}")
print(f"最大值: {max_value}")

# 查找最小值
min_value = reduce(lambda x, y: x if x < y else y, numbers)
print(f"最小值: {min_value}")

# 比较内置函数
print(f"内置max函数: {max(numbers)}")
print(f"内置min函数: {min(numbers)}")

# 查找最长字符串
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(f"\n单词列表: {words}")
print(f"最长单词: {longest}")
print()

# 6. 复杂数据结构处理
print("=== 6. 复杂数据结构处理 ===")

# 学生成绩统计
students = [
    {'name': '张三', 'scores': [85, 92, 78]},
    {'name': '李四', 'scores': [90, 88, 95]},
    {'name': '王五', 'scores': [76, 82, 89]},
    {'name': '赵六', 'scores': [88, 91, 87]}
]

# 计算所有学生的总分
total_all_scores = reduce(
    lambda acc, student: acc + sum(student['scores']), 
    students, 
    0
)
print(f"所有学生总分: {total_all_scores}")

# 找出平均分最高的学生
best_student = reduce(
    lambda x, y: x if sum(x['scores'])/len(x['scores']) > sum(y['scores'])/len(y['scores']) else y,
    students
)
print(f"平均分最高的学生: {best_student['name']} - 平均分: {sum(best_student['scores'])/len(best_student['scores']):.1f}")

# 合并所有分数到一个列表
all_scores = reduce(
    lambda acc, student: acc + student['scores'],
    students,
    []
)
print(f"所有分数: {all_scores}")
print()

# 7. 字符串和列表操作
print("=== 7. 字符串和列表操作 ===")

# 字符串反转
text = "Hello World"
reversed_text = reduce(lambda x, y: y + x, text)
print(f"原始字符串: {text}")
print(f"反转字符串: {reversed_text}")

# 列表扁平化
nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
flattened = reduce(lambda x, y: x + y, nested_lists)
print(f"\n嵌套列表: {nested_lists}")
print(f"扁平化结果: {flattened}")

# 字典合并
dicts = [
    {'a': 1, 'b': 2},
    {'c': 3, 'd': 4},
    {'e': 5, 'f': 6}
]
merged_dict = reduce(lambda x, y: {**x, **y}, dicts)
print(f"\n字典列表: {dicts}")
print(f"合并字典: {merged_dict}")

# 统计字符出现次数
text = "hello world"
char_count = reduce(
    lambda acc, char: {**acc, char: acc.get(char, 0) + 1},
    text,
    {}
)
print(f"\n文本: {text}")
print(f"字符统计: {char_count}")
print()

# 8. 函数组合
print("=== 8. 函数组合 ===")

# 定义一些简单函数
def add_one(x):
    return x + 1

def multiply_two(x):
    return x * 2

def square(x):
    return x ** 2

# 使用reduce组合函数
functions = [add_one, multiply_two, square]
result = reduce(lambda f, g: lambda x: g(f(x)), functions)

print("函数组合示例：")
print(f"函数序列: add_one -> multiply_two -> square")
test_value = 3
print(f"输入值: {test_value}")
print(f"组合函数结果: {result(test_value)}")
print(f"手动计算: square(multiply_two(add_one(3))) = square(multiply_two(4)) = square(8) = 64")

# 管道操作
def pipe(*functions):
    """创建函数管道"""
    return reduce(lambda f, g: lambda x: g(f(x)), functions)

pipeline = pipe(
    lambda x: x + 10,
    lambda x: x * 3,
    lambda x: x - 5
)

print(f"\n管道操作结果: {pipeline(5)}")
print("计算过程: ((5+10)*3)-5 = (15*3)-5 = 45-5 = 40")
print()

# 9. 性能比较
print("=== 9. 性能比较 ===")

# 准备测试数据
large_numbers = list(range(10000))

def performance_test():
    # 方法1：使用reduce
    start_time = time.time()
    result1 = reduce(lambda x, y: x + y, large_numbers)
    reduce_time = time.time() - start_time
    
    # 方法2：使用内置sum函数
    start_time = time.time()
    result2 = sum(large_numbers)
    sum_time = time.time() - start_time
    
    # 方法3：使用循环
    start_time = time.time()
    result3 = 0
    for num in large_numbers:
        result3 += num
    loop_time = time.time() - start_time
    
    return reduce_time, sum_time, loop_time, result1, result2, result3

reduce_time, sum_time, loop_time, r1, r2, r3 = performance_test()
print(f"reduce方法时间: {reduce_time:.6f} 秒, 结果: {r1}")
print(f"sum函数时间: {sum_time:.6f} 秒, 结果: {r2}")
print(f"循环方法时间: {loop_time:.6f} 秒, 结果: {r3}")
print("结论：内置函数通常比reduce更快")
print()

# 10. 实际应用案例
print("=== 10. 实际应用案例 ===")

# 案例1：计算复合利息
def compound_interest_reduce(principal, rates):
    """使用reduce计算复合利息"""
    return reduce(lambda amount, rate: amount * (1 + rate), rates, principal)

rates = [0.05, 0.04, 0.06, 0.03, 0.05]  # 5年的年利率
principal = 10000
final_amount = compound_interest_reduce(principal, rates)
print(f"本金: ¥{principal}")
print(f"年利率: {[f'{r*100}%' for r in rates]}")
print(f"5年后金额: ¥{final_amount:.2f}")

# 案例2：路径拼接
path_parts = ['home', 'user', 'documents', 'projects', 'python']
full_path = reduce(lambda path, part: path + '/' + part, path_parts)
print(f"\n路径部分: {path_parts}")
print(f"完整路径: {full_path}")

# 案例3：数据验证链
validators = [
    lambda x: x.strip() if isinstance(x, str) else x,  # 去除空白
    lambda x: x.lower() if isinstance(x, str) else x,  # 转小写
    lambda x: x if len(x) >= 3 else None,  # 长度检查
    lambda x: x if x and '@' in x else None  # 邮箱格式检查
]

email_inputs = ['  JOHN@EXAMPLE.COM  ', 'ab', 'invalid-email', 'user@domain.com']

print("\n邮箱验证链：")
for email in email_inputs:
    try:
        validated = reduce(lambda data, validator: validator(data) if data is not None else None, validators, email)
        print(f"输入: '{email}' -> 验证结果: {validated}")
    except:
        print(f"输入: '{email}' -> 验证失败")

# 案例4：配置合并
configs = [
    {'host': 'localhost', 'port': 8080, 'debug': True},
    {'port': 3000, 'ssl': True},
    {'host': 'production.com', 'debug': False, 'timeout': 30}
]

final_config = reduce(
    lambda base, override: {**base, **override},
    configs,
    {}
)
print(f"\n配置合并：")
for i, config in enumerate(configs):
    print(f"配置{i+1}: {config}")
print(f"最终配置: {final_config}")
print()

# 11. reduce与其他函数的组合
print("=== 11. reduce与其他函数的组合 ===")

# map + reduce 组合
numbers = [1, 2, 3, 4, 5]

# 先平方再求和
square_sum = reduce(lambda x, y: x + y, map(lambda x: x**2, numbers))
print(f"数字: {numbers}")
print(f"平方和: {square_sum}")

# filter + reduce 组合
# 筛选偶数再求积
even_product = reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 0, numbers), 1)
print(f"偶数乘积: {even_product}")

# map + filter + reduce 组合
# 筛选大于2的数，平方后求和
complex_result = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2, filter(lambda x: x > 2, numbers))
)
print(f"大于2的数平方和: {complex_result}")
print()

# 12. 最佳实践和注意事项
print("=== 12. 最佳实践和注意事项 ===")
print("reduce函数的优点：")
print("✓ 函数式编程风格")
print("✓ 代码简洁，逻辑清晰")
print("✓ 适合累积计算")
print("✓ 可以处理复杂的聚合操作")
print()
print("使用注意事项：")
print("⚠ 需要从functools模块导入")
print("⚠ 空序列必须提供初始值")
print("⚠ 内置函数通常性能更好")
print("⚠ 复杂逻辑可能影响可读性")
print()
print("适用场景：")
print("• 累积计算（求和、求积等）")
print("• 查找最值")
print("• 数据聚合和合并")
print("• 函数组合")
print("• 复杂的折叠操作")
print()
print("选择建议：")
print("• 简单求和：使用内置sum()")
print("• 简单最值：使用内置max()/min()")
print("• 复杂聚合：考虑使用reduce")
print("• 函数组合：reduce是好选择")
print("• 性能敏感：测试比较不同方法")

if __name__ == "__main__":
    print("\n=== Lambda表达式与reduce函数学习完成 ===")
    print("reduce函数是累积计算的强大工具")
    print("与Lambda表达式结合可以实现复杂的聚合操作")
    print("下一步：学习Lambda表达式与排序函数的结合使用")