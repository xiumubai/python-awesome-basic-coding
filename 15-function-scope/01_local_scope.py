#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
局部作用域 (Local Scope)

局部作用域是指在函数内部定义的变量的作用范围。
这些变量只能在定义它们的函数内部访问，函数外部无法访问。

学习目标：
1. 理解局部作用域的概念
2. 掌握局部变量的定义和使用
3. 了解局部变量的生命周期
4. 理解函数参数也是局部变量
"""

# 1. 基本的局部作用域
def basic_local_scope():
    """演示基本的局部作用域"""
    print("=== 基本局部作用域 ===")
    
    # 在函数内部定义的变量是局部变量
    local_var = "我是局部变量"
    number = 42
    
    print(f"函数内部访问局部变量: {local_var}")
    print(f"函数内部访问数字: {number}")
    
    # 局部变量只在函数内部有效
    return local_var

# 2. 局部变量的生命周期
def variable_lifecycle():
    """演示局部变量的生命周期"""
    print("\n=== 局部变量的生命周期 ===")
    
    # 变量在函数开始时创建
    temp_var = "临时变量"
    print(f"变量创建: {temp_var}")
    
    # 在函数执行过程中可以修改
    temp_var = "修改后的变量"
    print(f"变量修改: {temp_var}")
    
    # 函数结束时变量被销毁
    print("函数即将结束，变量将被销毁")

# 3. 函数参数也是局部变量
def parameters_are_local(name, age, city="北京"):
    """演示函数参数也是局部变量"""
    print("\n=== 函数参数是局部变量 ===")
    
    # 参数在函数内部就是局部变量
    print(f"姓名参数: {name}")
    print(f"年龄参数: {age}")
    print(f"城市参数: {city}")
    
    # 可以修改参数值（不影响外部）
    name = name + "_modified"
    age = age + 1
    
    print(f"修改后的姓名: {name}")
    print(f"修改后的年龄: {age}")
    
    return name, age

# 4. 多个函数的独立局部作用域
def function_a():
    """函数A的局部作用域"""
    var = "函数A的变量"
    print(f"函数A中的变量: {var}")
    return var

def function_b():
    """函数B的局部作用域"""
    var = "函数B的变量"
    print(f"函数B中的变量: {var}")
    return var

def independent_scopes():
    """演示不同函数的独立局部作用域"""
    print("\n=== 独立的局部作用域 ===")
    
    result_a = function_a()
    result_b = function_b()
    
    print(f"函数A返回: {result_a}")
    print(f"函数B返回: {result_b}")

# 5. 嵌套函数的局部作用域
def outer_function():
    """外层函数"""
    outer_var = "外层变量"
    
    def inner_function():
        """内层函数"""
        inner_var = "内层变量"
        print(f"内层函数访问内层变量: {inner_var}")
        print(f"内层函数访问外层变量: {outer_var}")
        return inner_var
    
    print("\n=== 嵌套函数的局部作用域 ===")
    print(f"外层函数的变量: {outer_var}")
    
    result = inner_function()
    return result

# 6. 局部作用域的限制
def scope_limitations():
    """演示局部作用域的限制"""
    print("\n=== 局部作用域的限制 ===")
    
    # 函数内部定义的变量
    internal_var = "内部变量"
    print(f"函数内部: {internal_var}")
    
    # 尝试在函数外部访问会报错
    print("注意：函数外部无法访问internal_var")

# 7. 局部变量与同名全局变量
global_name = "全局变量"

def local_vs_global():
    """演示局部变量与全局变量的关系"""
    print("\n=== 局部变量与全局变量 ===")
    
    # 定义同名的局部变量
    global_name = "局部变量"
    
    print(f"函数内部的global_name: {global_name}")
    print("局部变量会遮蔽同名的全局变量")

# 8. 实际应用示例
def calculate_area(length, width):
    """计算矩形面积的实际应用"""
    # 所有变量都是局部的
    area = length * width
    unit = "平方米"
    
    print(f"长度: {length}米")
    print(f"宽度: {width}米")
    print(f"面积: {area}{unit}")
    
    return area

def process_student_info(student_id, name, scores):
    """处理学生信息的实际应用"""
    # 局部变量用于计算
    total_score = sum(scores)
    average_score = total_score / len(scores)
    grade = "优秀" if average_score >= 90 else "良好" if average_score >= 80 else "及格" if average_score >= 60 else "不及格"
    
    print(f"\n学生ID: {student_id}")
    print(f"姓名: {name}")
    print(f"总分: {total_score}")
    print(f"平均分: {average_score:.2f}")
    print(f"等级: {grade}")
    
    return {
        'id': student_id,
        'name': name,
        'total': total_score,
        'average': average_score,
        'grade': grade
    }

# 主程序
if __name__ == "__main__":
    print("Python函数作用域学习 - 局部作用域")
    print("=" * 50)
    
    # 1. 基本局部作用域
    result = basic_local_scope()
    print(f"函数返回值: {result}")
    
    # 尝试访问局部变量（会报错，所以注释掉）
    # print(local_var)  # NameError: name 'local_var' is not defined
    
    # 2. 变量生命周期
    variable_lifecycle()
    
    # 3. 函数参数
    original_name = "张三"
    original_age = 25
    print(f"\n调用前 - 姓名: {original_name}, 年龄: {original_age}")
    
    new_name, new_age = parameters_are_local(original_name, original_age, "上海")
    print(f"调用后 - 原始姓名: {original_name}, 原始年龄: {original_age}")
    print(f"返回值 - 姓名: {new_name}, 年龄: {new_age}")
    
    # 4. 独立作用域
    independent_scopes()
    
    # 5. 嵌套函数
    nested_result = outer_function()
    print(f"嵌套函数返回: {nested_result}")
    
    # 6. 作用域限制
    scope_limitations()
    
    # 7. 局部vs全局
    print(f"\n调用函数前的全局变量: {global_name}")
    local_vs_global()
    print(f"调用函数后的全局变量: {global_name}")
    
    # 8. 实际应用
    print("\n=== 实际应用示例 ===")
    
    # 计算面积
    area_result = calculate_area(5, 3)
    print(f"计算结果: {area_result}")
    
    # 处理学生信息
    student_result = process_student_info("S001", "李四", [85, 92, 78, 96, 88])
    print(f"处理结果: {student_result}")
    
    print("\n=== 学习总结 ===")
    print("1. 局部变量只在定义它们的函数内部有效")
    print("2. 函数参数也是局部变量")
    print("3. 每个函数都有自己独立的局部作用域")
    print("4. 局部变量在函数结束时被销毁")
    print("5. 局部变量会遮蔽同名的全局变量")