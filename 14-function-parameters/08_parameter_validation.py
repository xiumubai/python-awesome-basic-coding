#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
参数验证 (Parameter Validation)

参数验证是确保函数接收到正确类型和值的参数的重要技术。
良好的参数验证可以提高代码的健壮性，减少运行时错误，并提供清晰的错误信息。

学习目标：
1. 理解参数验证的重要性
2. 掌握基本的参数类型检查方法
3. 学会使用断言进行参数验证
4. 了解自定义验证函数的编写
5. 掌握使用装饰器进行参数验证
6. 学会处理验证错误和提供有用的错误信息
"""

import functools
import inspect
from typing import Any, Callable, Union, List, Dict, Optional
from numbers import Number

# 1. 基本的类型检查
def basic_type_validation(name: str, age: int, salary: float) -> dict:
    """
    基本类型验证示例
    
    参数:
        name (str): 姓名
        age (int): 年龄
        salary (float): 薪资
    
    返回:
        dict: 员工信息
    
    异常:
        TypeError: 参数类型不正确时抛出
        ValueError: 参数值不合理时抛出
    """
    # 类型检查
    if not isinstance(name, str):
        raise TypeError(f"name必须是字符串，得到的是 {type(name).__name__}")
    
    if not isinstance(age, int):
        raise TypeError(f"age必须是整数，得到的是 {type(age).__name__}")
    
    if not isinstance(salary, (int, float)):
        raise TypeError(f"salary必须是数字，得到的是 {type(salary).__name__}")
    
    # 值范围检查
    if not name.strip():
        raise ValueError("name不能为空")
    
    if age < 0 or age > 150:
        raise ValueError(f"age必须在0-150之间，得到的是 {age}")
    
    if salary < 0:
        raise ValueError(f"salary不能为负数，得到的是 {salary}")
    
    employee = {
        'name': name.strip(),
        'age': age,
        'salary': float(salary)
    }
    
    print(f"创建员工: {employee}")
    return employee

# 2. 使用断言进行验证
def assert_validation_example(numbers: list, operation: str = "sum") -> float:
    """
    使用断言进行参数验证
    
    参数:
        numbers (list): 数字列表
        operation (str): 操作类型
    
    返回:
        float: 计算结果
    """
    # 使用断言进行验证
    assert isinstance(numbers, list), f"numbers必须是列表，得到 {type(numbers).__name__}"
    assert len(numbers) > 0, "numbers不能为空列表"
    assert all(isinstance(n, (int, float)) for n in numbers), "numbers中必须都是数字"
    assert operation in ["sum", "avg", "max", "min"], f"不支持的操作: {operation}"
    
    print(f"验证通过: numbers={numbers}, operation={operation}")
    
    if operation == "sum":
        result = sum(numbers)
    elif operation == "avg":
        result = sum(numbers) / len(numbers)
    elif operation == "max":
        result = max(numbers)
    elif operation == "min":
        result = min(numbers)
    
    print(f"计算结果: {result}")
    return result

# 3. 自定义验证函数
def validate_email(email: str) -> bool:
    """
    验证邮箱格式
    
    参数:
        email (str): 邮箱地址
    
    返回:
        bool: 是否有效
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    """
    验证手机号格式（简单验证）
    
    参数:
        phone (str): 手机号
    
    返回:
        bool: 是否有效
    """
    import re
    # 简单的中国手机号验证
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, phone))

def validate_password(password: str) -> tuple:
    """
    验证密码强度
    
    参数:
        password (str): 密码
    
    返回:
        tuple: (是否有效, 错误信息列表)
    """
    errors = []
    
    if len(password) < 8:
        errors.append("密码长度至少8位")
    
    if not any(c.isupper() for c in password):
        errors.append("密码必须包含大写字母")
    
    if not any(c.islower() for c in password):
        errors.append("密码必须包含小写字母")
    
    if not any(c.isdigit() for c in password):
        errors.append("密码必须包含数字")
    
    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        errors.append("密码必须包含特殊字符")
    
    return len(errors) == 0, errors

def create_user_account(username: str, email: str, phone: str, password: str) -> dict:
    """
    创建用户账户，使用自定义验证函数
    
    参数:
        username (str): 用户名
        email (str): 邮箱
        phone (str): 手机号
        password (str): 密码
    
    返回:
        dict: 用户信息
    
    异常:
        ValueError: 验证失败时抛出
    """
    errors = []
    
    # 用户名验证
    if not isinstance(username, str) or not username.strip():
        errors.append("用户名不能为空")
    elif len(username.strip()) < 3:
        errors.append("用户名至少3个字符")
    elif len(username.strip()) > 20:
        errors.append("用户名不能超过20个字符")
    
    # 邮箱验证
    if not isinstance(email, str) or not validate_email(email):
        errors.append("邮箱格式不正确")
    
    # 手机号验证
    if not isinstance(phone, str) or not validate_phone(phone):
        errors.append("手机号格式不正确")
    
    # 密码验证
    if not isinstance(password, str):
        errors.append("密码必须是字符串")
    else:
        is_valid, password_errors = validate_password(password)
        if not is_valid:
            errors.extend(password_errors)
    
    # 如果有错误，抛出异常
    if errors:
        raise ValueError("用户信息验证失败:\n" + "\n".join(f"- {error}" for error in errors))
    
    # 创建用户
    user = {
        'username': username.strip(),
        'email': email.lower(),
        'phone': phone,
        'password_hash': f"hash_{password}"  # 实际应用中应该使用真正的哈希
    }
    
    print(f"用户创建成功: {user['username']} ({user['email']})")
    return user

# 4. 参数验证装饰器
def validate_types(**expected_types):
    """
    类型验证装饰器
    
    参数:
        **expected_types: 参数名和期望类型的映射
    
    返回:
        function: 装饰器函数
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 获取函数签名
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # 验证类型
            for param_name, expected_type in expected_types.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"参数 '{param_name}' 期望类型 {expected_type.__name__}, "
                            f"得到 {type(value).__name__}"
                        )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_range(**ranges):
    """
    数值范围验证装饰器
    
    参数:
        **ranges: 参数名和(最小值, 最大值)的映射
    
    返回:
        function: 装饰器函数
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 获取函数签名
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # 验证范围
            for param_name, (min_val, max_val) in ranges.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if isinstance(value, Number):
                        if value < min_val or value > max_val:
                            raise ValueError(
                                f"参数 '{param_name}' 必须在 [{min_val}, {max_val}] 范围内, "
                                f"得到 {value}"
                            )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(name=str, age=int, score=float)
@validate_range(age=(0, 150), score=(0.0, 100.0))
def create_student(name: str, age: int, score: float, grade: str = "A") -> dict:
    """
    创建学生信息，使用装饰器进行验证
    
    参数:
        name (str): 学生姓名
        age (int): 年龄
        score (float): 分数
        grade (str): 等级
    
    返回:
        dict: 学生信息
    """
    student = {
        'name': name,
        'age': age,
        'score': score,
        'grade': grade
    }
    
    print(f"学生信息: {student}")
    return student

# 5. 复合验证装饰器
class ValidationError(Exception):
    """
    自定义验证异常
    """
    pass

def comprehensive_validator(*validators):
    """
    综合验证装饰器，支持多个验证器
    
    参数:
        *validators: 验证器函数列表
    
    返回:
        function: 装饰器函数
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 获取函数签名
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # 应用所有验证器
            for validator in validators:
                try:
                    validator(bound_args.arguments)
                except Exception as e:
                    raise ValidationError(f"验证失败: {e}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 验证器函数
def validate_positive_numbers(args: dict):
    """
    验证所有数字参数都是正数
    """
    for name, value in args.items():
        if isinstance(value, Number) and value <= 0:
            raise ValueError(f"参数 '{name}' 必须是正数，得到 {value}")

def validate_non_empty_strings(args: dict):
    """
    验证所有字符串参数都不为空
    """
    for name, value in args.items():
        if isinstance(value, str) and not value.strip():
            raise ValueError(f"参数 '{name}' 不能为空字符串")

def validate_list_not_empty(args: dict):
    """
    验证所有列表参数都不为空
    """
    for name, value in args.items():
        if isinstance(value, list) and len(value) == 0:
            raise ValueError(f"参数 '{name}' 不能为空列表")

@comprehensive_validator(
    validate_positive_numbers,
    validate_non_empty_strings,
    validate_list_not_empty
)
def process_order(customer_name: str, items: list, total_amount: float, 
                 discount: float = 0.0) -> dict:
    """
    处理订单，使用综合验证装饰器
    
    参数:
        customer_name (str): 客户姓名
        items (list): 商品列表
        total_amount (float): 总金额
        discount (float): 折扣
    
    返回:
        dict: 订单信息
    """
    final_amount = total_amount - discount
    
    order = {
        'customer': customer_name,
        'items': items,
        'total_amount': total_amount,
        'discount': discount,
        'final_amount': final_amount
    }
    
    print(f"订单处理成功: {order}")
    return order

# 6. 条件验证
def conditional_validation(condition_func: Callable, 
                         validation_func: Callable, 
                         error_message: str = "条件验证失败"):
    """
    条件验证装饰器
    
    参数:
        condition_func: 条件函数
        validation_func: 验证函数
        error_message: 错误信息
    
    返回:
        function: 装饰器函数
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 获取函数签名
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # 检查条件
            if condition_func(bound_args.arguments):
                # 如果条件满足，执行验证
                if not validation_func(bound_args.arguments):
                    raise ValidationError(error_message)
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 条件和验证函数
def is_premium_user(args: dict) -> bool:
    """检查是否是高级用户"""
    return args.get('user_type') == 'premium'

def validate_premium_limits(args: dict) -> bool:
    """验证高级用户的限制"""
    amount = args.get('amount', 0)
    return amount <= 10000  # 高级用户单次限额10000

@conditional_validation(
    is_premium_user,
    validate_premium_limits,
    "高级用户单次交易金额不能超过10000"
)
def make_transaction(user_id: str, amount: float, user_type: str = "regular") -> dict:
    """
    执行交易，对高级用户有特殊验证
    
    参数:
        user_id (str): 用户ID
        amount (float): 交易金额
        user_type (str): 用户类型
    
    返回:
        dict: 交易信息
    """
    transaction = {
        'user_id': user_id,
        'amount': amount,
        'user_type': user_type,
        'transaction_id': f"TXN_{user_id}_{amount}"
    }
    
    print(f"交易成功: {transaction}")
    return transaction

# 7. 参数验证工具类
class ParameterValidator:
    """
    参数验证工具类
    """
    
    @staticmethod
    def validate_string(value: Any, name: str, min_length: int = 0, 
                       max_length: int = None, pattern: str = None) -> str:
        """
        验证字符串参数
        
        参数:
            value: 要验证的值
            name: 参数名
            min_length: 最小长度
            max_length: 最大长度
            pattern: 正则表达式模式
        
        返回:
            str: 验证后的字符串
        
        异常:
            TypeError: 类型错误
            ValueError: 值错误
        """
        if not isinstance(value, str):
            raise TypeError(f"参数 '{name}' 必须是字符串，得到 {type(value).__name__}")
        
        if len(value) < min_length:
            raise ValueError(f"参数 '{name}' 长度不能少于 {min_length} 个字符")
        
        if max_length is not None and len(value) > max_length:
            raise ValueError(f"参数 '{name}' 长度不能超过 {max_length} 个字符")
        
        if pattern is not None:
            import re
            if not re.match(pattern, value):
                raise ValueError(f"参数 '{name}' 格式不正确")
        
        return value
    
    @staticmethod
    def validate_number(value: Any, name: str, min_val: Number = None, 
                       max_val: Number = None, allow_zero: bool = True) -> Number:
        """
        验证数字参数
        
        参数:
            value: 要验证的值
            name: 参数名
            min_val: 最小值
            max_val: 最大值
            allow_zero: 是否允许零
        
        返回:
            Number: 验证后的数字
        
        异常:
            TypeError: 类型错误
            ValueError: 值错误
        """
        if not isinstance(value, Number):
            raise TypeError(f"参数 '{name}' 必须是数字，得到 {type(value).__name__}")
        
        if not allow_zero and value == 0:
            raise ValueError(f"参数 '{name}' 不能为零")
        
        if min_val is not None and value < min_val:
            raise ValueError(f"参数 '{name}' 不能小于 {min_val}")
        
        if max_val is not None and value > max_val:
            raise ValueError(f"参数 '{name}' 不能大于 {max_val}")
        
        return value
    
    @staticmethod
    def validate_list(value: Any, name: str, min_length: int = 0, 
                     max_length: int = None, item_type: type = None) -> list:
        """
        验证列表参数
        
        参数:
            value: 要验证的值
            name: 参数名
            min_length: 最小长度
            max_length: 最大长度
            item_type: 列表项类型
        
        返回:
            list: 验证后的列表
        
        异常:
            TypeError: 类型错误
            ValueError: 值错误
        """
        if not isinstance(value, list):
            raise TypeError(f"参数 '{name}' 必须是列表，得到 {type(value).__name__}")
        
        if len(value) < min_length:
            raise ValueError(f"参数 '{name}' 长度不能少于 {min_length}")
        
        if max_length is not None and len(value) > max_length:
            raise ValueError(f"参数 '{name}' 长度不能超过 {max_length}")
        
        if item_type is not None:
            for i, item in enumerate(value):
                if not isinstance(item, item_type):
                    raise TypeError(
                        f"参数 '{name}' 的第 {i} 项必须是 {item_type.__name__}, "
                        f"得到 {type(item).__name__}"
                    )
        
        return value

def create_product(name: str, price: float, categories: list, 
                  description: str = "") -> dict:
    """
    创建产品，使用验证工具类
    
    参数:
        name (str): 产品名称
        price (float): 价格
        categories (list): 分类列表
        description (str): 描述
    
    返回:
        dict: 产品信息
    """
    # 使用验证工具类进行验证
    validator = ParameterValidator()
    
    name = validator.validate_string(name, "name", min_length=1, max_length=100)
    price = validator.validate_number(price, "price", min_val=0, allow_zero=False)
    categories = validator.validate_list(categories, "categories", 
                                       min_length=1, item_type=str)
    description = validator.validate_string(description, "description", 
                                          max_length=500)
    
    product = {
        'name': name,
        'price': price,
        'categories': categories,
        'description': description
    }
    
    print(f"产品创建成功: {product}")
    return product

def main():
    """
    主函数：演示各种参数验证技术
    """
    print("=" * 50)
    print("参数验证演示")
    print("=" * 50)
    
    # 1. 基本类型验证
    print("\n1. 基本类型验证：")
    try:
        basic_type_validation("张三", 25, 5000.0)
        basic_type_validation("李四", 30, 6000)
    except (TypeError, ValueError) as e:
        print(f"验证错误: {e}")
    
    # 错误示例
    try:
        basic_type_validation(123, 25, 5000.0)  # 错误的类型
    except (TypeError, ValueError) as e:
        print(f"验证错误: {e}")
    
    try:
        basic_type_validation("王五", -5, 5000.0)  # 错误的值
    except (TypeError, ValueError) as e:
        print(f"验证错误: {e}")
    
    # 2. 断言验证
    print("\n2. 断言验证：")
    try:
        assert_validation_example([1, 2, 3, 4, 5], "sum")
        assert_validation_example([10, 20, 30], "avg")
    except AssertionError as e:
        print(f"断言错误: {e}")
    
    # 错误示例
    try:
        assert_validation_example([], "sum")  # 空列表
    except AssertionError as e:
        print(f"断言错误: {e}")
    
    # 3. 自定义验证函数
    print("\n3. 自定义验证函数：")
    try:
        create_user_account("john_doe", "john@example.com", 
                          "13800138000", "MyPassword123!")
    except ValueError as e:
        print(f"验证错误: {e}")
    
    # 错误示例
    try:
        create_user_account("jo", "invalid-email", 
                          "123", "weak")  # 多个验证错误
    except ValueError as e:
        print(f"验证错误: {e}")
    
    # 4. 装饰器验证
    print("\n4. 装饰器验证：")
    try:
        create_student("张三", 20, 85.5)
        create_student("李四", 22, 92.0, "A+")
    except (TypeError, ValueError) as e:
        print(f"验证错误: {e}")
    
    # 错误示例
    try:
        create_student("王五", "twenty", 85.5)  # 类型错误
    except (TypeError, ValueError) as e:
        print(f"验证错误: {e}")
    
    try:
        create_student("赵六", 200, 85.5)  # 范围错误
    except (TypeError, ValueError) as e:
        print(f"验证错误: {e}")
    
    # 5. 综合验证装饰器
    print("\n5. 综合验证装饰器：")
    try:
        process_order("张三", ["商品1", "商品2"], 100.0, 10.0)
    except ValidationError as e:
        print(f"验证错误: {e}")
    
    # 错误示例
    try:
        process_order("", [], -100.0, 10.0)  # 多个验证错误
    except ValidationError as e:
        print(f"验证错误: {e}")
    
    # 6. 条件验证
    print("\n6. 条件验证：")
    try:
        make_transaction("user123", 5000.0, "regular")
        make_transaction("vip456", 8000.0, "premium")
    except ValidationError as e:
        print(f"验证错误: {e}")
    
    # 错误示例
    try:
        make_transaction("vip789", 15000.0, "premium")  # 超过高级用户限额
    except ValidationError as e:
        print(f"验证错误: {e}")
    
    # 7. 验证工具类
    print("\n7. 验证工具类：")
    try:
        create_product("iPhone 15", 8999.0, ["电子产品", "手机"], 
                      "最新款iPhone")
    except (TypeError, ValueError) as e:
        print(f"验证错误: {e}")
    
    # 错误示例
    try:
        create_product("", -100.0, [], "x" * 600)  # 多个验证错误
    except (TypeError, ValueError) as e:
        print(f"验证错误: {e}")
    
    print("\n=" * 50)
    print("参数验证最佳实践：")
    print("1. 尽早验证参数，在函数开始时进行检查")
    print("2. 提供清晰、有用的错误信息")
    print("3. 使用适当的异常类型（TypeError, ValueError等）")
    print("4. 考虑使用装饰器来减少重复的验证代码")
    print("5. 为复杂验证逻辑创建专门的验证函数")
    print("6. 在文档中明确说明参数要求和可能的异常")
    print("7. 平衡验证的严格性和性能开销")
    print("8. 使用类型提示来帮助IDE和工具进行静态检查")
    print("=" * 50)

if __name__ == "__main__":
    main()