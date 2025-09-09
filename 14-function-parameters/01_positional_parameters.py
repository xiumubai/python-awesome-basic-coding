#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
位置参数 (Positional Parameters)

位置参数是函数中最基本的参数类型，参数的值根据位置顺序传递给函数。
调用函数时，参数必须按照定义时的顺序传递。

学习目标：
1. 理解位置参数的概念
2. 掌握位置参数的定义和使用
3. 了解位置参数的特点和限制
4. 学会处理位置参数的常见问题
"""

# 1. 基本的位置参数
def greet(name, age):
    """
    简单的问候函数
    
    参数:
        name (str): 姓名
        age (int): 年龄
    """
    print(f"你好，{name}！你今年{age}岁了。")

# 2. 多个位置参数
def calculate_rectangle_area(length, width):
    """
    计算矩形面积
    
    参数:
        length (float): 长度
        width (float): 宽度
    
    返回:
        float: 矩形面积
    """
    area = length * width
    print(f"矩形面积：{length} × {width} = {area}")
    return area

# 3. 位置参数的顺序很重要
def divide(dividend, divisor):
    """
    除法运算
    
    参数:
        dividend (float): 被除数
        divisor (float): 除数
    
    返回:
        float: 商
    """
    if divisor == 0:
        print("错误：除数不能为零！")
        return None
    
    result = dividend / divisor
    print(f"{dividend} ÷ {divisor} = {result}")
    return result

# 4. 位置参数与数据类型
def format_person_info(name, age, height, is_student):
    """
    格式化个人信息
    
    参数:
        name (str): 姓名
        age (int): 年龄
        height (float): 身高（米）
        is_student (bool): 是否为学生
    """
    status = "学生" if is_student else "非学生"
    print(f"姓名：{name}")
    print(f"年龄：{age}岁")
    print(f"身高：{height}米")
    print(f"身份：{status}")
    print("-" * 20)

# 5. 位置参数的数量检查
def add_three_numbers(a, b, c):
    """
    三个数相加
    
    参数:
        a (float): 第一个数
        b (float): 第二个数
        c (float): 第三个数
    
    返回:
        float: 三数之和
    """
    result = a + b + c
    print(f"{a} + {b} + {c} = {result}")
    return result

# 6. 位置参数与列表/元组
def process_coordinates(x, y, z):
    """
    处理三维坐标
    
    参数:
        x (float): X坐标
        y (float): Y坐标
        z (float): Z坐标
    """
    print(f"坐标点：({x}, {y}, {z})")
    distance = (x**2 + y**2 + z**2)**0.5
    print(f"到原点的距离：{distance:.2f}")
    return distance

# 7. 位置参数的实际应用示例
def create_user_profile(username, email, phone, city):
    """
    创建用户档案
    
    参数:
        username (str): 用户名
        email (str): 邮箱
        phone (str): 电话
        city (str): 城市
    
    返回:
        dict: 用户档案字典
    """
    profile = {
        'username': username,
        'email': email,
        'phone': phone,
        'city': city
    }
    
    print("用户档案创建成功：")
    for key, value in profile.items():
        print(f"  {key}: {value}")
    
    return profile

# 8. 位置参数的错误处理
def safe_divide(a, b):
    """
    安全的除法运算（带错误处理）
    
    参数:
        a (float): 被除数
        b (float): 除数
    
    返回:
        float or None: 运算结果或None（出错时）
    """
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            print("错误：参数必须是数字类型")
            return None
        
        if b == 0:
            print("错误：除数不能为零")
            return None
        
        result = a / b
        print(f"计算结果：{a} ÷ {b} = {result}")
        return result
    
    except Exception as e:
        print(f"计算出错：{e}")
        return None

def main():
    """
    主函数：演示位置参数的各种用法
    """
    print("=" * 50)
    print("位置参数演示")
    print("=" * 50)
    
    # 1. 基本位置参数使用
    print("\n1. 基本位置参数：")
    greet("小明", 25)
    greet("小红", 22)
    
    # 2. 计算矩形面积
    print("\n2. 多个位置参数：")
    area1 = calculate_rectangle_area(5.0, 3.0)
    area2 = calculate_rectangle_area(10.5, 7.2)
    
    # 3. 演示参数顺序的重要性
    print("\n3. 参数顺序的重要性：")
    print("正确顺序：")
    divide(10, 2)
    print("交换顺序：")
    divide(2, 10)
    
    # 4. 不同数据类型的位置参数
    print("\n4. 不同数据类型的参数：")
    format_person_info("张三", 28, 1.75, True)
    format_person_info("李四", 35, 1.68, False)
    
    # 5. 三个数相加
    print("\n5. 固定数量的参数：")
    sum_result = add_three_numbers(10, 20, 30)
    sum_result2 = add_three_numbers(1.5, 2.7, 3.8)
    
    # 6. 处理坐标
    print("\n6. 处理三维坐标：")
    distance1 = process_coordinates(3, 4, 5)
    distance2 = process_coordinates(1.0, 2.0, 2.0)
    
    # 7. 创建用户档案
    print("\n7. 实际应用示例：")
    user1 = create_user_profile("john_doe", "john@email.com", "13800138000", "北京")
    user2 = create_user_profile("jane_smith", "jane@email.com", "13900139000", "上海")
    
    # 8. 错误处理演示
    print("\n8. 错误处理：")
    safe_divide(10, 2)
    safe_divide(10, 0)  # 除零错误
    safe_divide("10", 2)  # 类型错误
    
    # 9. 常见错误演示
    print("\n9. 常见错误演示：")
    try:
        # 参数数量不匹配
        greet("小明")  # 缺少参数
    except TypeError as e:
        print(f"参数数量错误：{e}")
    
    try:
        # 参数过多
        greet("小明", 25, "额外参数")  # 参数过多
    except TypeError as e:
        print(f"参数数量错误：{e}")
    
    print("\n=" * 50)
    print("位置参数要点总结：")
    print("1. 位置参数必须按照定义时的顺序传递")
    print("2. 参数数量必须完全匹配")
    print("3. 参数的位置决定了它们的含义")
    print("4. 位置参数是最基本的参数传递方式")
    print("5. 调用时不能省略任何位置参数")
    print("=" * 50)

if __name__ == "__main__":
    main()