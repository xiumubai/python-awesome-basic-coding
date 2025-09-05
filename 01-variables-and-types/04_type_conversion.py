#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第四课：类型转换

学习目标：
1. 理解什么是类型转换
2. 掌握显式类型转换的方法
3. 了解隐式类型转换
4. 学会处理类型转换中的异常
5. 掌握常见的类型转换场景
6. 了解类型转换的最佳实践

作者：Python基础教程
日期：2024年
"""

print("=" * 50)
print("第四课：类型转换")
print("=" * 50)

# 1. 什么是类型转换？
print("\n1. 什么是类型转换？")
print("-" * 30)
print("类型转换是将一种数据类型的值转换为另一种数据类型的过程")
print("Python提供了多种内置函数来进行类型转换")
print("类型转换分为显式转换和隐式转换")

# 2. 显式类型转换 - 转换为整数
print("\n2. 转换为整数 (int)")
print("-" * 30)

# 从浮点数转换为整数
float_num = 3.14
int_from_float = int(float_num)
print(f"浮点数 {float_num} 转换为整数：{int_from_float}")
print(f"注意：小数部分被截断，不是四舍五入")

# 从字符串转换为整数
str_num = "123"
int_from_str = int(str_num)
print(f"字符串 '{str_num}' 转换为整数：{int_from_str}")

# 从布尔值转换为整数
bool_true = True
bool_false = False
int_from_bool_true = int(bool_true)
int_from_bool_false = int(bool_false)
print(f"布尔值 {bool_true} 转换为整数：{int_from_bool_true}")
print(f"布尔值 {bool_false} 转换为整数：{int_from_bool_false}")

# 不同进制的字符串转换为整数
print("\n不同进制字符串转换为整数：")
binary_str = "1010"
octal_str = "12"
hex_str = "A"
print(f"二进制 '{binary_str}' 转换为整数：{int(binary_str, 2)}")
print(f"八进制 '{octal_str}' 转换为整数：{int(octal_str, 8)}")
print(f"十六进制 '{hex_str}' 转换为整数：{int(hex_str, 16)}")

# 3. 显式类型转换 - 转换为浮点数
print("\n3. 转换为浮点数 (float)")
print("-" * 30)

# 从整数转换为浮点数
int_num = 42
float_from_int = float(int_num)
print(f"整数 {int_num} 转换为浮点数：{float_from_int}")

# 从字符串转换为浮点数
str_float = "3.14159"
float_from_str = float(str_float)
print(f"字符串 '{str_float}' 转换为浮点数：{float_from_str}")

# 科学计数法字符串转换
scientific_str = "1.5e3"
float_from_scientific = float(scientific_str)
print(f"科学计数法 '{scientific_str}' 转换为浮点数：{float_from_scientific}")

# 从布尔值转换为浮点数
float_from_bool = float(True)
print(f"布尔值 True 转换为浮点数：{float_from_bool}")

# 4. 显式类型转换 - 转换为字符串
print("\n4. 转换为字符串 (str)")
print("-" * 30)

# 从整数转换为字符串
num = 123
str_from_int = str(num)
print(f"整数 {num} 转换为字符串：'{str_from_int}'")

# 从浮点数转换为字符串
float_val = 3.14159
str_from_float = str(float_val)
print(f"浮点数 {float_val} 转换为字符串：'{str_from_float}'")

# 从布尔值转换为字符串
str_from_bool = str(True)
print(f"布尔值 True 转换为字符串：'{str_from_bool}'")

# 从列表转换为字符串
list_val = [1, 2, 3]
str_from_list = str(list_val)
print(f"列表 {list_val} 转换为字符串：'{str_from_list}'")

# 5. 显式类型转换 - 转换为布尔值
print("\n5. 转换为布尔值 (bool)")
print("-" * 30)
print("Python中的真值测试规则：")
print("False值：False, None, 0, 0.0, '', [], {}, set()")
print("True值：其他所有值")

# 测试不同值的布尔转换
test_values = [0, 1, -1, 0.0, 3.14, "", "hello", [], [1, 2], {}, {"key": "value"}, None]

print("\n各种值的布尔转换结果：")
for value in test_values:
    bool_result = bool(value)
    print(f"bool({repr(value)}) = {bool_result}")

# 6. 隐式类型转换
print("\n6. 隐式类型转换")
print("-" * 30)
print("Python在某些操作中会自动进行类型转换")

# 数学运算中的隐式转换
print("\n数学运算中的隐式转换：")
int_val = 5
float_val = 2.5
result = int_val + float_val  # int自动转换为float
print(f"{int_val} + {float_val} = {result} (类型：{type(result)})")

# 布尔值在数学运算中的转换
bool_val = True
result2 = bool_val + int_val  # bool自动转换为int
print(f"{bool_val} + {int_val} = {result2} (类型：{type(result2)})")

# 字符串格式化中的隐式转换
print("\n字符串格式化中的隐式转换：")
age = 25
message = f"我今年{age}岁"  # int自动转换为str
print(f"格式化结果：{message}")

# 7. 类型转换中的异常处理
print("\n7. 类型转换中的异常处理")
print("-" * 30)
print("不是所有的类型转换都能成功，需要处理可能的异常")

# 无效的字符串转整数
print("\n处理无效的类型转换：")
invalid_strings = ["abc", "12.5", "12a", "", "  "]

for s in invalid_strings:
    try:
        result = int(s)
        print(f"'{s}' 转换为整数成功：{result}")
    except ValueError as e:
        print(f"'{s}' 转换为整数失败：{e}")

# 安全的类型转换函数
def safe_int_conversion(value, default=0):
    """安全的整数转换函数"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print("\n使用安全转换函数：")
test_values = ["123", "abc", 45.6, None, ""]
for val in test_values:
    result = safe_int_conversion(val, -1)
    print(f"safe_int_conversion({repr(val)}) = {result}")

# 8. 常见的类型转换场景
print("\n8. 常见的类型转换场景")
print("-" * 30)

# 场景1：用户输入处理
print("场景1：用户输入处理")
def process_user_input():
    """模拟处理用户输入"""
    # 模拟用户输入（实际中使用input()函数）
    user_inputs = ["25", "3.14", "hello", "true"]
    
    for user_input in user_inputs:
        print(f"\n用户输入：'{user_input}'")
        
        # 尝试转换为数字
        try:
            # 先尝试整数
            num = int(user_input)
            print(f"  识别为整数：{num}")
        except ValueError:
            try:
                # 再尝试浮点数
                num = float(user_input)
                print(f"  识别为浮点数：{num}")
            except ValueError:
                # 保持为字符串
                print(f"  保持为字符串：'{user_input}'")

process_user_input()

# 场景2：数据清洗
print("\n场景2：数据清洗")
raw_data = ["123", "45.6", "abc", "78", "", "90.1"]
print(f"原始数据：{raw_data}")

# 清洗数据，只保留能转换为数字的
cleaned_numbers = []
for item in raw_data:
    try:
        # 尝试转换为浮点数
        num = float(item)
        cleaned_numbers.append(num)
    except ValueError:
        print(f"跳过无效数据：'{item}'")

print(f"清洗后的数字：{cleaned_numbers}")

# 场景3：配置文件处理
print("\n场景3：配置文件处理")
config_strings = {
    "port": "8080",
    "debug": "true",
    "timeout": "30.5",
    "name": "MyApp"
}

print("配置字符串转换：")
config_values = {}
for key, value in config_strings.items():
    # 尝试转换为合适的类型
    if value.lower() in ['true', 'false']:
        config_values[key] = value.lower() == 'true'
    elif value.isdigit():
        config_values[key] = int(value)
    elif value.replace('.', '').replace('-', '').isdigit():
        config_values[key] = float(value)
    else:
        config_values[key] = value
    
    print(f"  {key}: '{value}' -> {config_values[key]} ({type(config_values[key]).__name__})")

# 9. 类型转换的最佳实践
print("\n9. 类型转换的最佳实践")
print("-" * 30)
print("1. 总是处理可能的异常")
print("2. 使用合适的默认值")
print("3. 验证转换后的值是否合理")
print("4. 在函数中明确参数类型要求")
print("5. 使用类型注解提高代码可读性")

# 最佳实践示例
def convert_to_positive_int(value, default=1):
    """转换为正整数的最佳实践示例"""
    try:
        # 转换为整数
        result = int(value)
        
        # 验证是否为正数
        if result <= 0:
            print(f"警告：{result} 不是正数，使用默认值 {default}")
            return default
        
        return result
    except (ValueError, TypeError) as e:
        print(f"转换失败：{e}，使用默认值 {default}")
        return default

print("\n最佳实践示例：")
test_cases = ["10", "-5", "abc", "0", 15.7, None]
for case in test_cases:
    result = convert_to_positive_int(case)
    print(f"convert_to_positive_int({repr(case)}) = {result}")

# 10. 实践练习
print("\n10. 实践练习")
print("-" * 30)
print("练习1：编写函数将字符串列表转换为数字列表")
print("练习2：编写函数安全地将用户输入转换为指定类型")
print("练习3：处理混合类型数据的求和")

# 练习1示例
def string_list_to_numbers(string_list):
    """将字符串列表转换为数字列表"""
    numbers = []
    for s in string_list:
        try:
            # 尝试转换为整数
            if '.' not in s:
                numbers.append(int(s))
            else:
                numbers.append(float(s))
        except ValueError:
            print(f"跳过无效字符串：'{s}'")
    return numbers

print("\n练习1示例：")
string_nums = ["1", "2.5", "3", "abc", "4.7"]
result = string_list_to_numbers(string_nums)
print(f"输入：{string_nums}")
print(f"输出：{result}")

# 练习3示例
def safe_sum(mixed_list):
    """安全地对混合类型列表求和"""
    total = 0
    count = 0
    
    for item in mixed_list:
        try:
            # 尝试转换为数字并累加
            if isinstance(item, (int, float)):
                total += item
                count += 1
            elif isinstance(item, str):
                num = float(item)
                total += num
                count += 1
            elif isinstance(item, bool):
                total += int(item)
                count += 1
        except (ValueError, TypeError):
            print(f"跳过无法转换的项：{repr(item)}")
    
    return total, count

print("\n练习3示例：")
mixed_data = [1, "2.5", 3, "abc", True, 4.5, None, "6"]
total, count = safe_sum(mixed_data)
print(f"输入：{mixed_data}")
print(f"有效数字总和：{total}，有效数字个数：{count}")

print("\n=" * 50)
print("第四课学习完成！")
print("下一课将学习变量命名规范")
print("=" * 50)

# 运行这个文件的方法：
# 在终端中输入：python 04_type_conversion.py
# 或者在IDE中直接运行