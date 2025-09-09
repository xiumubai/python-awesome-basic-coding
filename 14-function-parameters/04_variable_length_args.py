#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
可变长度参数 *args (Variable Length Arguments)

*args允许函数接受任意数量的位置参数，这些参数会被收集到一个元组中。
这使得函数可以处理不确定数量的输入参数，提供了极大的灵活性。

学习目标：
1. 理解*args的概念和作用
2. 掌握*args的定义和使用方法
3. 学会*args与其他参数类型的组合使用
4. 了解*args的实际应用场景
"""

# 1. 基本的*args使用
def sum_numbers(*args):
    """
    计算任意数量数字的和
    
    参数:
        *args: 任意数量的数字
    
    返回:
        float: 所有数字的和
    """
    print(f"接收到的参数: {args}")
    print(f"参数类型: {type(args)}")
    print(f"参数数量: {len(args)}")
    
    if not args:
        print("没有提供参数，返回0")
        return 0
    
    total = sum(args)
    print(f"计算结果: {' + '.join(map(str, args))} = {total}")
    print("-" * 30)
    return total

# 2. *args与普通参数组合
def create_message(prefix, *args, suffix=""):
    """
    创建消息字符串
    
    参数:
        prefix (str): 消息前缀
        *args: 消息内容部分
        suffix (str): 消息后缀
    
    返回:
        str: 完整的消息字符串
    """
    print(f"前缀: {prefix}")
    print(f"内容部分: {args}")
    print(f"后缀: {suffix}")
    
    # 将所有内容部分连接起来
    content = " ".join(str(arg) for arg in args)
    message = f"{prefix} {content} {suffix}".strip()
    
    print(f"完整消息: '{message}'")
    print("-" * 30)
    return message

# 3. 数学运算函数
def calculate_statistics(*numbers):
    """
    计算数字的统计信息
    
    参数:
        *numbers: 任意数量的数字
    
    返回:
        dict: 包含各种统计信息的字典
    """
    if not numbers:
        print("没有提供数字")
        return {}
    
    print(f"输入数字: {numbers}")
    
    stats = {
        'count': len(numbers),
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers),
        'range': max(numbers) - min(numbers)
    }
    
    print(f"统计结果:")
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.2f}")
        else:
            print(f"  {key}: {value}")
    
    print("-" * 30)
    return stats

# 4. 字符串处理函数
def join_strings(separator=" ", *strings):
    """
    使用指定分隔符连接字符串
    
    参数:
        separator (str): 分隔符，默认为空格
        *strings: 要连接的字符串
    
    返回:
        str: 连接后的字符串
    """
    print(f"分隔符: '{separator}'")
    print(f"字符串列表: {strings}")
    
    if not strings:
        result = ""
    else:
        result = separator.join(str(s) for s in strings)
    
    print(f"连接结果: '{result}'")
    print("-" * 30)
    return result

# 5. 列表操作函数
def find_common_elements(*lists):
    """
    找出多个列表的公共元素
    
    参数:
        *lists: 任意数量的列表
    
    返回:
        set: 公共元素集合
    """
    if not lists:
        print("没有提供列表")
        return set()
    
    print(f"输入列表数量: {len(lists)}")
    for i, lst in enumerate(lists, 1):
        print(f"  列表{i}: {lst}")
    
    # 找出公共元素
    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
    
    print(f"公共元素: {sorted(common) if common else '无'}")
    print("-" * 30)
    return common

# 6. 函数调用链
def apply_functions(value, *functions):
    """
    对值依次应用多个函数
    
    参数:
        value: 初始值
        *functions: 要应用的函数列表
    
    返回:
        最终处理结果
    """
    print(f"初始值: {value}")
    print(f"要应用的函数数量: {len(functions)}")
    
    result = value
    for i, func in enumerate(functions, 1):
        old_result = result
        result = func(result)
        print(f"  步骤{i}: {func.__name__}({old_result}) = {result}")
    
    print(f"最终结果: {result}")
    print("-" * 30)
    return result

# 7. 日志记录函数
def log_message(level, *message_parts, timestamp=True):
    """
    记录日志消息
    
    参数:
        level (str): 日志级别
        *message_parts: 消息的各个部分
        timestamp (bool): 是否包含时间戳
    """
    from datetime import datetime
    
    # 组合消息
    message = " ".join(str(part) for part in message_parts)
    
    # 添加时间戳
    if timestamp:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{current_time}] [{level}] {message}"
    else:
        log_entry = f"[{level}] {message}"
    
    print(f"日志条目: {log_entry}")
    print("-" * 40)

# 8. 数据验证函数
def validate_all(*validators, data):
    """
    使用多个验证器验证数据
    
    参数:
        *validators: 验证函数列表
        data: 要验证的数据
    
    返回:
        tuple: (是否全部通过, 错误列表)
    """
    print(f"验证数据: {data}")
    print(f"验证器数量: {len(validators)}")
    
    errors = []
    
    for i, validator in enumerate(validators, 1):
        try:
            is_valid = validator(data)
            print(f"  验证器{i} ({validator.__name__}): {'通过' if is_valid else '失败'}")
            if not is_valid:
                errors.append(f"验证器{i}失败")
        except Exception as e:
            print(f"  验证器{i} ({validator.__name__}): 错误 - {e}")
            errors.append(f"验证器{i}出错: {e}")
    
    all_passed = len(errors) == 0
    print(f"验证结果: {'全部通过' if all_passed else '有失败项'}")
    
    if errors:
        print(f"错误列表: {errors}")
    
    print("-" * 40)
    return all_passed, errors

# 9. 装饰器相关的*args使用
def timing_decorator(func):
    """
    计时装饰器，演示*args在装饰器中的使用
    """
    import time
    
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"位置参数: {args}")
        print(f"关键字参数: {kwargs}")
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        print(f"执行时间: {end_time - start_time:.4f}秒")
        print("-" * 30)
        return result
    
    return wrapper

@timing_decorator
def slow_calculation(*numbers):
    """
    模拟耗时计算
    """
    import time
    time.sleep(0.1)  # 模拟耗时操作
    return sum(x ** 2 for x in numbers)

# 辅助函数用于演示
def is_positive(x):
    """检查是否为正数"""
    return x > 0

def is_even(x):
    """检查是否为偶数"""
    return x % 2 == 0

def is_in_range(x):
    """检查是否在1-100范围内"""
    return 1 <= x <= 100

def main():
    """
    主函数：演示*args的各种用法
    """
    print("=" * 50)
    print("可变长度参数 *args 演示")
    print("=" * 50)
    
    # 1. 基本*args使用
    print("\n1. 基本*args使用：")
    sum_numbers()  # 无参数
    sum_numbers(5)  # 一个参数
    sum_numbers(1, 2, 3, 4, 5)  # 多个参数
    sum_numbers(10, 20, 30, 40, 50, 60)  # 更多参数
    
    # 2. *args与普通参数组合
    print("\n2. *args与普通参数组合：")
    create_message("通知:")
    create_message("警告:", "系统", "即将", "重启")
    create_message("错误:", "文件", "不存在", suffix="请检查路径")
    
    # 3. 统计计算
    print("\n3. 数学统计函数：")
    calculate_statistics()
    calculate_statistics(42)
    calculate_statistics(10, 20, 30, 40, 50)
    calculate_statistics(1.5, 2.7, 3.2, 4.8, 5.1, 6.9)
    
    # 4. 字符串连接
    print("\n4. 字符串连接：")
    join_strings("-", "Python", "is", "awesome")
    join_strings(", ", "苹果", "香蕉", "橙子")
    join_strings(" | ", "姓名", "年龄", "城市")
    join_strings()  # 无字符串
    
    # 5. 找公共元素
    print("\n5. 找公共元素：")
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [4, 5, 6, 7, 8]
    find_common_elements(list1, list2, list3)
    
    list4 = ['a', 'b', 'c']
    list5 = ['b', 'c', 'd']
    find_common_elements(list4, list5)
    
    # 6. 函数调用链
    print("\n6. 函数调用链：")
    # 定义一些简单的函数
    def double(x):
        return x * 2
    
    def add_ten(x):
        return x + 10
    
    def square(x):
        return x ** 2
    
    apply_functions(5, double, add_ten, square)
    apply_functions(3, square, double)
    
    # 7. 日志记录
    print("\n7. 日志记录：")
    log_message("INFO", "用户", "登录", "成功")
    log_message("ERROR", "数据库", "连接", "失败", timestamp=False)
    log_message("DEBUG", "处理请求:", "/api/users", "参数:", "page=1")
    
    # 8. 数据验证
    print("\n8. 数据验证：")
    validate_all(is_positive, is_even, is_in_range, data=50)
    validate_all(is_positive, is_even, data=-10)
    validate_all(is_positive, is_in_range, data=150)
    
    # 9. 装饰器中的*args
    print("\n9. 装饰器中的*args：")
    result1 = slow_calculation(1, 2, 3, 4, 5)
    print(f"计算结果: {result1}")
    
    result2 = slow_calculation(10, 20)
    print(f"计算结果: {result2}")
    
    # 10. 实际应用：批量处理
    print("\n10. 实际应用示例：")
    
    def batch_process(*items, processor=str.upper):
        """
        批量处理项目
        """
        print(f"批量处理 {len(items)} 个项目")
        results = []
        for i, item in enumerate(items, 1):
            processed = processor(item)
            print(f"  项目{i}: {item} -> {processed}")
            results.append(processed)
        print(f"处理完成，结果: {results}")
        print("-" * 30)
        return results
    
    # 批量转换为大写
    batch_process("hello", "world", "python")
    
    # 批量计算平方
    batch_process(2, 3, 4, 5, processor=lambda x: x**2)
    
    print("\n=" * 50)
    print("*args 要点总结：")
    print("1. *args收集任意数量的位置参数到元组中")
    print("2. *args必须在普通位置参数之后")
    print("3. *args可以与关键字参数组合使用")
    print("4. 函数内部*args是一个元组，可以进行元组操作")
    print("5. *args提供了函数参数的极大灵活性")
    print("6. 常用于装饰器、批量处理、数学计算等场景")
    print("=" * 50)

if __name__ == "__main__":
    main()