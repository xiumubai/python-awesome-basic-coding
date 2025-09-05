#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
注释最佳实践

本文件总结了Python注释的最佳实践、编写规范和常见误区。
通过正确和错误的示例对比，帮助开发者写出高质量的注释。

作者: Python学习教程
日期: 2024
"""

import datetime
import json
from typing import List, Dict, Optional

# ============================================================
# 1. 注释的基本原则
# ============================================================

print("=== 注释最佳实践指南 ===")

# 原则1: 注释应该解释"为什么"，而不是"是什么"

# ❌ 不好的注释 - 重复代码内容
# x = x + 1  # 将x加1

# ✅ 好的注释 - 解释目的
retry_count = retry_count + 1  # 增加重试次数，处理网络不稳定情况

# 原则2: 保持注释与代码同步

def calculate_discount(price, customer_type):
    """
    根据客户类型计算折扣。
    
    参数:
        price (float): 原价
        customer_type (str): 客户类型 ('vip', 'regular', 'new')
    
    返回:
        float: 折扣后的价格
    """
    # ✅ 注释与代码逻辑一致
    if customer_type == 'vip':      # VIP客户享受20%折扣
        return price * 0.8
    elif customer_type == 'new':    # 新客户享受10%折扣
        return price * 0.9
    else:                           # 普通客户无折扣
        return price

print(f"VIP客户100元商品价格: {calculate_discount(100, 'vip')}")

# ============================================================
# 2. 函数和类的注释最佳实践
# ============================================================

class BankAccount:
    """
    银行账户类，用于管理账户余额和交易记录。
    
    这个类提供了基本的银行账户功能，包括存款、取款、
    查询余额和交易历史记录。所有交易都会被记录。
    
    属性:
        account_number (str): 账户号码
        balance (float): 当前余额
        transactions (list): 交易记录列表
    
    示例:
        >>> account = BankAccount("123456", 1000)
        >>> account.deposit(500)
        >>> account.get_balance()
        1500.0
    """
    
    def __init__(self, account_number: str, initial_balance: float = 0):
        """
        初始化银行账户。
        
        参数:
            account_number: 账户号码，必须唯一
            initial_balance: 初始余额，默认为0
        
        异常:
            ValueError: 当初始余额为负数时抛出
        """
        if initial_balance < 0:
            raise ValueError("初始余额不能为负数")
        
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []  # 存储所有交易记录
        
        # 记录账户创建
        self._add_transaction("账户创建", initial_balance)
    
    def deposit(self, amount: float) -> None:
        """
        存款操作。
        
        参数:
            amount: 存款金额，必须为正数
        
        异常:
            ValueError: 当存款金额不是正数时抛出
        """
        if amount <= 0:
            raise ValueError("存款金额必须为正数")
        
        self.balance += amount
        self._add_transaction("存款", amount)
    
    def withdraw(self, amount: float) -> bool:
        """
        取款操作。
        
        参数:
            amount: 取款金额，必须为正数且不超过余额
        
        返回:
            bool: 取款是否成功
        
        异常:
            ValueError: 当取款金额不是正数时抛出
        """
        if amount <= 0:
            raise ValueError("取款金额必须为正数")
        
        if amount > self.balance:
            return False  # 余额不足，取款失败
        
        self.balance -= amount
        self._add_transaction("取款", -amount)
        return True
    
    def get_balance(self) -> float:
        """
        获取当前余额。
        
        返回:
            float: 当前账户余额
        """
        return self.balance
    
    def _add_transaction(self, transaction_type: str, amount: float) -> None:
        """
        添加交易记录（私有方法）。
        
        参数:
            transaction_type: 交易类型
            amount: 交易金额
        """
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'timestamp': datetime.datetime.now(),
            'balance_after': self.balance
        }
        self.transactions.append(transaction)

# 测试银行账户类
account = BankAccount("123456", 1000)
account.deposit(500)
account.withdraw(200)
print(f"账户余额: {account.get_balance()}")

# ============================================================
# 3. 复杂算法的注释最佳实践
# ============================================================

def quick_sort(arr: List[int]) -> List[int]:
    """
    快速排序算法实现。
    
    使用分治法对数组进行排序。选择一个基准元素，
    将数组分为小于基准和大于基准的两部分，
    然后递归地对两部分进行排序。
    
    时间复杂度: 平均O(n log n)，最坏O(n²)
    空间复杂度: O(log n)
    
    参数:
        arr: 待排序的整数列表
    
    返回:
        List[int]: 排序后的列表
    
    示例:
        >>> quick_sort([3, 6, 8, 10, 1, 2, 1])
        [1, 1, 2, 3, 6, 8, 10]
    """
    # 基础情况：空数组或单元素数组已经有序
    if len(arr) <= 1:
        return arr
    
    # 选择中间元素作为基准（避免最坏情况）
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    
    # 分区：将元素分为三部分
    left = []    # 小于基准的元素
    middle = []  # 等于基准的元素
    right = []   # 大于基准的元素
    
    for element in arr:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            middle.append(element)
        else:
            right.append(element)
    
    # 递归排序左右两部分，然后合并结果
    return quick_sort(left) + middle + quick_sort(right)

# 测试快速排序
test_array = [3, 6, 8, 10, 1, 2, 1]
print(f"排序前: {test_array}")
print(f"排序后: {quick_sort(test_array)}")

# ============================================================
# 4. 配置和常量的注释最佳实践
# ============================================================

# ✅ 好的常量注释 - 解释用途和来源
MAX_RETRY_ATTEMPTS = 3      # 网络请求最大重试次数，基于经验值
CONNECTION_TIMEOUT = 30     # 连接超时时间（秒），符合HTTP标准
DEFAULT_PAGE_SIZE = 20      # 分页默认大小，平衡性能和用户体验

# API配置
API_CONFIG = {
    'base_url': 'https://api.example.com',  # 生产环境API地址
    'version': 'v1',                        # API版本号
    'timeout': CONNECTION_TIMEOUT,          # 请求超时时间
    'max_retries': MAX_RETRY_ATTEMPTS       # 最大重试次数
}

# 数据库配置
DB_CONFIG = {
    'host': 'localhost',        # 数据库服务器地址
    'port': 5432,              # PostgreSQL默认端口
    'database': 'myapp',       # 数据库名称
    'pool_size': 10,           # 连接池大小，根据并发需求设定
    'pool_timeout': 30         # 连接池超时时间（秒）
}

print(f"API配置: {json.dumps(API_CONFIG, indent=2)}")

# ============================================================
# 5. 错误处理的注释最佳实践
# ============================================================

def safe_divide(a: float, b: float) -> Optional[float]:
    """
    安全的除法运算，处理除零错误。
    
    参数:
        a: 被除数
        b: 除数
    
    返回:
        Optional[float]: 除法结果，除零时返回None
    """
    try:
        return a / b
    except ZeroDivisionError:
        # 记录错误但不抛出异常，让调用者决定如何处理
        print(f"警告: 尝试除以零 ({a} / {b})")
        return None
    except TypeError as e:
        # 处理类型错误，提供有用的错误信息
        print(f"类型错误: {e}")
        return None

def process_user_data(data: Dict) -> Dict:
    """
    处理用户数据，包含完整的错误处理。
    
    参数:
        data: 用户数据字典
    
    返回:
        Dict: 处理结果，包含状态和数据
    """
    try:
        # 验证必需字段
        required_fields = ['name', 'email', 'age']
        for field in required_fields:
            if field not in data:
                return {
                    'success': False,
                    'error': f'缺少必需字段: {field}'
                }
        
        # 验证数据类型和范围
        if not isinstance(data['age'], int) or data['age'] < 0:
            return {
                'success': False,
                'error': '年龄必须是非负整数'
            }
        
        # 验证邮箱格式（简单验证）
        if '@' not in data['email']:
            return {
                'success': False,
                'error': '邮箱格式不正确'
            }
        
        # 数据处理成功
        return {
            'success': True,
            'data': {
                'name': data['name'].strip().title(),  # 标准化姓名格式
                'email': data['email'].lower(),        # 邮箱转小写
                'age': data['age']
            }
        }
    
    except Exception as e:
        # 捕获未预期的错误
        return {
            'success': False,
            'error': f'处理数据时发生错误: {str(e)}'
        }

# 测试错误处理
test_data = {'name': '  张三  ', 'email': 'ZHANG@EXAMPLE.COM', 'age': 25}
result = process_user_data(test_data)
print(f"处理结果: {result}")

# ============================================================
# 6. 注释的常见误区和改进建议
# ============================================================

print("\n=== 注释常见误区 ===")

# ❌ 误区1: 过度注释显而易见的代码
# i = 0           # 初始化i为0
# i = i + 1       # i自增1
# print(i)        # 打印i的值

# ✅ 改进: 只注释需要解释的部分
loop_counter = 0
while loop_counter < 3:  # 执行3次循环，确保数据同步
    # 执行同步操作
    loop_counter += 1

# ❌ 误区2: 注释与代码不一致
# def calculate_tax(price):
#     return price * 0.15  # 计算10%的税费（注释错误！）

# ✅ 改进: 保持注释与代码一致
def calculate_tax(price):
    """
    计算商品税费。
    
    当前税率为15%，根据最新税法规定。
    """
    TAX_RATE = 0.15  # 当前税率15%
    return price * TAX_RATE

# ❌ 误区3: 使用注释来"修复"糟糕的代码
# def func(x, y, z):  # x是价格，y是数量，z是折扣
#     return x * y * (1 - z)

# ✅ 改进: 使用有意义的变量名
def calculate_discounted_total(unit_price, quantity, discount_rate):
    """
    计算折扣后的总价。
    
    参数:
        unit_price: 单价
        quantity: 数量
        discount_rate: 折扣率（0-1之间）
    
    返回:
        float: 折扣后的总价
    """
    return unit_price * quantity * (1 - discount_rate)

# ============================================================
# 7. 团队协作中的注释规范
# ============================================================

# TODO标记的使用
def user_authentication(username, password):
    """
    用户认证功能。
    
    TODO: 添加双因素认证支持
    TODO: 实现密码强度检查
    FIXME: 修复密码哈希算法的安全问题
    NOTE: 需要与安全团队确认加密标准
    """
    # 当前实现（简化版）
    if username and password:
        return True  # 临时实现，待完善
    return False

# 版本控制相关注释
# Added in v2.1.0: 支持批量用户导入
# Modified in v2.2.0: 优化导入性能
# Deprecated in v3.0.0: 使用新的import_users_v2()方法
def import_users(user_list):
    """
    批量导入用户（已废弃）。
    
    警告: 此方法在v3.0.0中已废弃，请使用import_users_v2()。
    
    参数:
        user_list: 用户列表
    """
    print("警告: 使用了已废弃的方法")
    # 实现细节...

print("\n=== 注释最佳实践总结 ===")
print("1. 注释应该解释'为什么'，而不是'是什么'")
print("2. 保持注释与代码同步")
print("3. 使用有意义的变量名减少注释需求")
print("4. 为复杂算法和业务逻辑添加详细注释")
print("5. 使用标准的文档字符串格式")
print("6. 避免过度注释和显而易见的注释")
print("7. 在团队中统一注释风格和规范")

# 运行这个文件来学习注释最佳实践
# 在终端中执行: python 05_comment_best_practices.py