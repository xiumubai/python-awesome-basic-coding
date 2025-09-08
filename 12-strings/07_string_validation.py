#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字符串验证方法

本文件演示Python中字符串验证的各种方法：
1. 内置验证方法（isalpha、isdigit、isalnum等）
2. 字符类型检查
3. 格式验证（邮箱、电话、URL等）
4. 自定义验证函数
5. 正则表达式验证
6. 数据清洗和验证

作者：Python学习教程
日期：2024年
"""

import re
import string
from urllib.parse import urlparse

def demonstrate_builtin_validation():
    """演示内置的字符串验证方法"""
    print("=== 内置字符串验证方法 ===")
    
    # 测试字符串列表
    test_strings = [
        "Hello",           # 纯字母
        "123",             # 纯数字
        "Hello123",        # 字母数字混合
        "Hello World",     # 包含空格
        "hello",           # 小写字母
        "HELLO",           # 大写字母
        "Hello!",          # 包含标点
        "   ",             # 空白字符
        "",                # 空字符串
        "\t\n",            # 制表符和换行符
        "①②③",            # 特殊数字字符
        "αβγ",             # 希腊字母
    ]
    
    print("字符串验证结果:")
    print(f"{'字符串':<15} {'isalpha':<8} {'isdigit':<8} {'isalnum':<8} {'isspace':<8} {'islower':<8} {'isupper':<8}")
    print("-" * 80)
    
    for s in test_strings:
        display_s = repr(s) if len(s) <= 10 else repr(s[:10] + "...")
        print(f"{display_s:<15} {str(s.isalpha()):<8} {str(s.isdigit()):<8} {str(s.isalnum()):<8} {str(s.isspace()):<8} {str(s.islower()):<8} {str(s.isupper()):<8}")
    
    # 详细说明每个方法
    print("\n方法详解:")
    
    # isalpha() - 检查是否只包含字母
    print("\n1. isalpha() - 检查是否只包含字母:")
    alpha_tests = ["Hello", "Hello123", "Hello!", "αβγ", ""]
    for test in alpha_tests:
        result = test.isalpha()
        print(f"  '{test}'.isalpha() = {result}")
    
    # isdigit() - 检查是否只包含数字
    print("\n2. isdigit() - 检查是否只包含数字:")
    digit_tests = ["123", "123.45", "123a", "①②③", ""]
    for test in digit_tests:
        result = test.isdigit()
        print(f"  '{test}'.isdigit() = {result}")
    
    # isalnum() - 检查是否只包含字母和数字
    print("\n3. isalnum() - 检查是否只包含字母和数字:")
    alnum_tests = ["Hello123", "Hello!", "123", "Hello", "Hello 123"]
    for test in alnum_tests:
        result = test.isalnum()
        print(f"  '{test}'.isalnum() = {result}")
    
    # isspace() - 检查是否只包含空白字符
    print("\n4. isspace() - 检查是否只包含空白字符:")
    space_tests = ["   ", "\t\n", " a ", "", "\r\n"]
    for test in space_tests:
        result = test.isspace()
        print(f"  {repr(test)}.isspace() = {result}")
    
    # islower() 和 isupper() - 检查大小写
    print("\n5. 大小写检查:")
    case_tests = ["hello", "HELLO", "Hello", "hello123", "HELLO!", "123"]
    for test in case_tests:
        lower = test.islower()
        upper = test.isupper()
        print(f"  '{test}': islower()={lower}, isupper()={upper}")

def demonstrate_advanced_validation():
    """演示高级字符串验证方法"""
    print("\n=== 高级字符串验证方法 ===")
    
    # isdecimal(), isnumeric(), isdigit() 的区别
    print("1. 数字验证方法的区别:")
    
    number_tests = [
        "123",      # 普通数字
        "123.45",   # 小数
        "-123",     # 负数
        "①②③",      # 中文数字字符
        "½",        # 分数字符
        "²",        # 上标数字
        "Ⅰ",        # 罗马数字
        "1e10",     # 科学计数法
    ]
    
    print(f"{'字符串':<10} {'isdigit':<8} {'isdecimal':<10} {'isnumeric':<10}")
    print("-" * 40)
    
    for test in number_tests:
        digit = test.isdigit()
        decimal = test.isdecimal()
        numeric = test.isnumeric()
        print(f"{test:<10} {str(digit):<8} {str(decimal):<10} {str(numeric):<10}")
    
    print("\n说明:")
    print("- isdigit(): 检查是否为数字字符（包括上标等）")
    print("- isdecimal(): 检查是否为十进制数字字符（0-9）")
    print("- isnumeric(): 检查是否为数值字符（包括中文数字、分数等）")
    
    # istitle() - 检查标题格式
    print("\n2. istitle() - 检查标题格式:")
    title_tests = [
        "Hello World",
        "Hello world",
        "HELLO WORLD",
        "hello world",
        "Hello World!",
        "123 Test",
        "Test123"
    ]
    
    for test in title_tests:
        result = test.istitle()
        print(f"  '{test}'.istitle() = {result}")
    
    # isidentifier() - 检查是否为有效的Python标识符
    print("\n3. isidentifier() - 检查Python标识符:")
    identifier_tests = [
        "variable",
        "_private",
        "Class1",
        "123invalid",
        "my-var",
        "my_var",
        "class",      # Python关键字
        "__init__",
        "π",          # Unicode字符
    ]
    
    import keyword
    
    for test in identifier_tests:
        is_id = test.isidentifier()
        is_keyword = keyword.iskeyword(test)
        valid = is_id and not is_keyword
        print(f"  '{test}': isidentifier()={is_id}, iskeyword()={is_keyword}, valid={valid}")
    
    # isprintable() - 检查是否为可打印字符
    print("\n4. isprintable() - 检查可打印字符:")
    printable_tests = [
        "Hello World",
        "Hello\nWorld",
        "Hello\tWorld",
        "Hello\x00World",
        "Hello\u200bWorld",  # 零宽空格
        "🐍",               # Emoji
    ]
    
    for test in printable_tests:
        result = test.isprintable()
        display = repr(test)
        print(f"  {display}.isprintable() = {result}")

def demonstrate_format_validation():
    """演示常见格式的验证"""
    print("\n=== 常见格式验证 ===")
    
    # 1. 邮箱验证
    print("1. 邮箱地址验证:")
    
    def validate_email_simple(email):
        """简单的邮箱验证"""
        if not email or '@' not in email:
            return False
        
        parts = email.split('@')
        if len(parts) != 2:
            return False
        
        local, domain = parts
        if not local or not domain:
            return False
        
        if '.' not in domain:
            return False
        
        return True
    
    def validate_email_regex(email):
        """使用正则表达式验证邮箱"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    email_tests = [
        "user@example.com",
        "test.email@domain.co.uk",
        "invalid.email",
        "@domain.com",
        "user@",
        "user@domain",
        "user name@domain.com",
        "user+tag@domain.com",
    ]
    
    print(f"{'邮箱地址':<25} {'简单验证':<10} {'正则验证':<10}")
    print("-" * 50)
    
    for email in email_tests:
        simple = validate_email_simple(email)
        regex = validate_email_regex(email)
        print(f"{email:<25} {str(simple):<10} {str(regex):<10}")
    
    # 2. 电话号码验证
    print("\n2. 电话号码验证:")
    
    def validate_phone(phone):
        """验证电话号码格式"""
        # 移除所有非数字字符
        digits = re.sub(r'\D', '', phone)
        
        # 检查长度（美国电话号码）
        if len(digits) == 10:
            return True
        elif len(digits) == 11 and digits[0] == '1':
            return True
        else:
            return False
    
    def validate_phone_format(phone):
        """验证特定格式的电话号码"""
        patterns = [
            r'^\d{3}-\d{3}-\d{4}$',           # 123-456-7890
            r'^\(\d{3}\)\s\d{3}-\d{4}$',      # (123) 456-7890
            r'^\d{10}$',                      # 1234567890
            r'^1-\d{3}-\d{3}-\d{4}$',         # 1-123-456-7890
        ]
        
        return any(re.match(pattern, phone) for pattern in patterns)
    
    phone_tests = [
        "123-456-7890",
        "(123) 456-7890",
        "1234567890",
        "1-123-456-7890",
        "123.456.7890",
        "123 456 7890",
        "12345",
        "+1-123-456-7890",
    ]
    
    print(f"{'电话号码':<20} {'数字验证':<10} {'格式验证':<10}")
    print("-" * 45)
    
    for phone in phone_tests:
        digit_valid = validate_phone(phone)
        format_valid = validate_phone_format(phone)
        print(f"{phone:<20} {str(digit_valid):<10} {str(format_valid):<10}")
    
    # 3. URL验证
    print("\n3. URL验证:")
    
    def validate_url_simple(url):
        """简单的URL验证"""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
    
    def validate_url_regex(url):
        """使用正则表达式验证URL"""
        pattern = r'^https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?$'
        return re.match(pattern, url) is not None
    
    url_tests = [
        "https://www.example.com",
        "http://example.com/path",
        "https://example.com:8080/path?query=value",
        "ftp://files.example.com",
        "www.example.com",
        "https://",
        "invalid-url",
        "https://example.com/path#anchor",
    ]
    
    print(f"{'URL':<40} {'简单验证':<10} {'正则验证':<10}")
    print("-" * 65)
    
    for url in url_tests:
        simple = validate_url_simple(url)
        regex = validate_url_regex(url)
        print(f"{url:<40} {str(simple):<10} {str(regex):<10}")

def demonstrate_custom_validation():
    """演示自定义验证函数"""
    print("\n=== 自定义验证函数 ===")
    
    # 1. 密码强度验证
    print("1. 密码强度验证:")
    
    def validate_password_strength(password):
        """验证密码强度"""
        if len(password) < 8:
            return False, "密码长度至少8位"
        
        checks = {
            '小写字母': any(c.islower() for c in password),
            '大写字母': any(c.isupper() for c in password),
            '数字': any(c.isdigit() for c in password),
            '特殊字符': any(c in string.punctuation for c in password)
        }
        
        failed_checks = [name for name, passed in checks.items() if not passed]
        
        if failed_checks:
            return False, f"缺少: {', '.join(failed_checks)}"
        
        return True, "密码强度良好"
    
    password_tests = [
        "password",
        "Password",
        "Password123",
        "Password123!",
        "Pass123!",
        "VeryStrongPassword123!",
        "12345678",
        "UPPERCASE123!",
    ]
    
    print(f"{'密码':<25} {'验证结果':<10} {'说明':<30}")
    print("-" * 70)
    
    for pwd in password_tests:
        valid, message = validate_password_strength(pwd)
        result = "通过" if valid else "失败"
        print(f"{pwd:<25} {result:<10} {message:<30}")
    
    # 2. 身份证号验证（简化版）
    print("\n2. 身份证号验证:")
    
    def validate_id_card(id_card):
        """验证身份证号格式（简化版）"""
        if not id_card:
            return False, "身份证号不能为空"
        
        # 移除空格
        id_card = id_card.replace(' ', '')
        
        # 检查长度
        if len(id_card) not in [15, 18]:
            return False, "身份证号长度应为15位或18位"
        
        # 检查前17位是否为数字（18位身份证）
        if len(id_card) == 18:
            if not id_card[:17].isdigit():
                return False, "前17位应为数字"
            
            # 检查最后一位（可以是数字或X）
            if not (id_card[17].isdigit() or id_card[17].upper() == 'X'):
                return False, "最后一位应为数字或X"
        
        # 检查15位身份证
        elif len(id_card) == 15:
            if not id_card.isdigit():
                return False, "15位身份证应全为数字"
        
        return True, "格式正确"
    
    id_tests = [
        "110101199001011234",
        "11010119900101123X",
        "110101900101123",
        "1101011990010112345",  # 长度错误
        "11010119900101123a",   # 包含字母
        "110101 199001 011234", # 包含空格
        "",                      # 空字符串
    ]
    
    print(f"{'身份证号':<20} {'验证结果':<10} {'说明':<20}")
    print("-" * 55)
    
    for id_card in id_tests:
        valid, message = validate_id_card(id_card)
        result = "通过" if valid else "失败"
        display_id = id_card if id_card else "(空)"
        print(f"{display_id:<20} {result:<10} {message:<20}")
    
    # 3. 信用卡号验证（Luhn算法）
    print("\n3. 信用卡号验证:")
    
    def validate_credit_card(card_number):
        """使用Luhn算法验证信用卡号"""
        # 移除空格和连字符
        card_number = re.sub(r'[\s-]', '', card_number)
        
        # 检查是否全为数字
        if not card_number.isdigit():
            return False, "信用卡号应只包含数字"
        
        # 检查长度
        if len(card_number) < 13 or len(card_number) > 19:
            return False, "信用卡号长度应在13-19位之间"
        
        # Luhn算法验证
        def luhn_check(card_num):
            digits = [int(d) for d in card_num]
            for i in range(len(digits) - 2, -1, -2):
                digits[i] *= 2
                if digits[i] > 9:
                    digits[i] -= 9
            return sum(digits) % 10 == 0
        
        if luhn_check(card_number):
            return True, "信用卡号有效"
        else:
            return False, "信用卡号校验失败"
    
    card_tests = [
        "4532015112830366",      # 有效的Visa卡号
        "4532-0151-1283-0366",   # 带连字符的格式
        "4532 0151 1283 0366",   # 带空格的格式
        "4532015112830367",      # 无效的卡号
        "123456789",             # 长度不够
        "4532015112830366abc",   # 包含字母
    ]
    
    print(f"{'信用卡号':<25} {'验证结果':<10} {'说明':<20}")
    print("-" * 60)
    
    for card in card_tests:
        valid, message = validate_credit_card(card)
        result = "通过" if valid else "失败"
        print(f"{card:<25} {result:<10} {message:<20}")

def demonstrate_data_cleaning_validation():
    """演示数据清洗和验证"""
    print("\n=== 数据清洗和验证 ===")
    
    # 1. 用户输入清洗
    print("1. 用户输入清洗:")
    
    def clean_user_input(text):
        """清洗用户输入"""
        if not text:
            return ""
        
        # 去除首尾空白
        cleaned = text.strip()
        
        # 移除多余的空白字符
        cleaned = re.sub(r'\s+', ' ', cleaned)
        
        # 移除控制字符
        cleaned = ''.join(char for char in cleaned if ord(char) >= 32 or char in '\t\n')
        
        return cleaned
    
    def validate_user_name(name):
        """验证用户名"""
        cleaned_name = clean_user_input(name)
        
        if not cleaned_name:
            return False, "用户名不能为空"
        
        if len(cleaned_name) < 2:
            return False, "用户名至少2个字符"
        
        if len(cleaned_name) > 50:
            return False, "用户名不能超过50个字符"
        
        # 检查是否包含有效字符（字母、数字、下划线、连字符）
        if not re.match(r'^[a-zA-Z0-9_\u4e00-\u9fff-]+$', cleaned_name):
            return False, "用户名只能包含字母、数字、下划线、连字符和中文"
        
        return True, cleaned_name
    
    name_tests = [
        "  Alice  ",
        "Bob123",
        "张三",
        "user_name",
        "user-name",
        "a",                    # 太短
        "a" * 60,              # 太长
        "user@name",           # 包含特殊字符
        "   \t\n   ",          # 只有空白
        "user\x00name",        # 包含控制字符
    ]
    
    print(f"{'原始输入':<20} {'验证结果':<10} {'清洗后/错误信息':<30}")
    print("-" * 65)
    
    for name in name_tests:
        valid, result = validate_user_name(name)
        status = "通过" if valid else "失败"
        display_input = repr(name) if len(name) <= 15 else repr(name[:15] + "...")
        print(f"{display_input:<20} {status:<10} {result:<30}")
    
    # 2. 数据类型验证和转换
    print("\n2. 数据类型验证和转换:")
    
    def safe_int_convert(value, default=None):
        """安全的整数转换"""
        if isinstance(value, int):
            return True, value
        
        if isinstance(value, str):
            value = value.strip()
            if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
                try:
                    return True, int(value)
                except ValueError:
                    pass
        
        return False, default
    
    def safe_float_convert(value, default=None):
        """安全的浮点数转换"""
        if isinstance(value, (int, float)):
            return True, float(value)
        
        if isinstance(value, str):
            value = value.strip()
            try:
                return True, float(value)
            except ValueError:
                pass
        
        return False, default
    
    conversion_tests = [
        ("123", "整数"),
        ("-456", "负整数"),
        ("123.45", "浮点数"),
        ("  789  ", "带空格的数字"),
        ("abc", "非数字字符串"),
        ("", "空字符串"),
        ("123abc", "混合字符串"),
        ("1.23e10", "科学计数法"),
    ]
    
    print(f"{'输入值':<15} {'类型':<10} {'整数转换':<15} {'浮点转换':<15}")
    print("-" * 60)
    
    for value, desc in conversion_tests:
        int_valid, int_result = safe_int_convert(value)
        float_valid, float_result = safe_float_convert(value)
        
        int_display = str(int_result) if int_valid else "失败"
        float_display = str(float_result) if float_valid else "失败"
        
        print(f"{repr(value):<15} {desc:<10} {int_display:<15} {float_display:<15}")
    
    # 3. 批量数据验证
    print("\n3. 批量数据验证:")
    
    def validate_data_batch(data_list, validators):
        """批量验证数据"""
        results = []
        
        for i, data in enumerate(data_list):
            row_errors = []
            
            for field_name, validator in validators.items():
                if field_name in data:
                    valid, message = validator(data[field_name])
                    if not valid:
                        row_errors.append(f"{field_name}: {message}")
                else:
                    row_errors.append(f"{field_name}: 缺少字段")
            
            results.append({
                'index': i,
                'valid': len(row_errors) == 0,
                'errors': row_errors,
                'data': data
            })
        
        return results
    
    # 示例数据
    sample_data = [
        {'name': 'Alice', 'email': 'alice@example.com', 'age': '25'},
        {'name': 'Bob', 'email': 'invalid-email', 'age': 'thirty'},
        {'name': '', 'email': 'charlie@test.com', 'age': '35'},
        {'name': 'Diana', 'email': 'diana@example.com'},  # 缺少age字段
    ]
    
    # 验证器
    validators = {
        'name': lambda x: validate_user_name(x),
        'email': lambda x: (validate_email_regex(x), "邮箱格式无效") if validate_email_regex(x) else (False, "邮箱格式无效"),
        'age': lambda x: safe_int_convert(x, 0)
    }
    
    validation_results = validate_data_batch(sample_data, validators)
    
    print("批量验证结果:")
    for result in validation_results:
        status = "✓" if result['valid'] else "✗"
        print(f"行 {result['index']}: {status} {result['data']}")
        if result['errors']:
            for error in result['errors']:
                print(f"    错误: {error}")

def demonstrate_regex_validation():
    """演示正则表达式验证"""
    print("\n=== 正则表达式验证 ===")
    
    # 常用正则表达式模式
    patterns = {
        '中文姓名': r'^[\u4e00-\u9fff]{2,4}$',
        '英文姓名': r'^[A-Za-z\s]{2,50}$',
        '手机号码': r'^1[3-9]\d{9}$',
        'QQ号码': r'^[1-9]\d{4,10}$',
        '邮政编码': r'^\d{6}$',
        'IP地址': r'^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$',
        '日期格式': r'^\d{4}-\d{2}-\d{2}$',
        '时间格式': r'^\d{2}:\d{2}:\d{2}$',
    }
    
    # 测试数据
    test_data = {
        '中文姓名': ['张三', '李四', '王五六', 'Alice', '张', '张三四五六'],
        '英文姓名': ['Alice Smith', 'Bob', 'Charlie Brown Jr', '张三', 'A', 'A' * 60],
        '手机号码': ['13812345678', '15987654321', '12345678901', '1381234567', '138123456789'],
        'QQ号码': ['12345', '123456789', '1234567890123', '1234', '0123456'],
        '邮政编码': ['100000', '200000', '12345', '1234567', 'abc123'],
        'IP地址': ['192.168.1.1', '255.255.255.255', '192.168.1.256', '192.168.1', '192.168.1.1.1'],
        '日期格式': ['2024-01-15', '2024-1-15', '24-01-15', '2024/01/15', '2024-13-01'],
        '时间格式': ['14:30:45', '9:30:45', '14:30', '25:30:45', '14:60:45'],
    }
    
    print("正则表达式验证结果:")
    
    for pattern_name, pattern in patterns.items():
        print(f"\n{pattern_name} (模式: {pattern}):")
        
        if pattern_name in test_data:
            for test_value in test_data[pattern_name]:
                match = re.match(pattern, test_value)
                result = "✓" if match else "✗"
                print(f"  {result} '{test_value}'")
    
    # 自定义复杂验证
    print("\n复杂验证示例:")
    
    def validate_chinese_id_card(id_card):
        """验证中国身份证号（包含校验位）"""
        if not re.match(r'^\d{17}[\dXx]$', id_card):
            return False, "格式不正确"
        
        # 校验码计算
        weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        
        sum_val = sum(int(id_card[i]) * weights[i] for i in range(17))
        check_code = check_codes[sum_val % 11]
        
        if id_card[17].upper() == check_code:
            return True, "身份证号有效"
        else:
            return False, "校验位错误"
    
    id_card_tests = [
        "11010119900307001X",  # 有效身份证
        "110101199003070010",  # 校验位错误
        "11010119900307001",   # 长度不够
        "11010119900307001Y",  # 无效字符
    ]
    
    print("\n身份证号验证:")
    for id_card in id_card_tests:
        valid, message = validate_chinese_id_card(id_card)
        result = "✓" if valid else "✗"
        print(f"  {result} {id_card}: {message}")

def main():
    """主函数，演示所有字符串验证方法"""
    print("Python字符串验证方法")
    print("=" * 50)
    
    demonstrate_builtin_validation()
    demonstrate_advanced_validation()
    demonstrate_format_validation()
    demonstrate_custom_validation()
    demonstrate_data_cleaning_validation()
    demonstrate_regex_validation()
    
    print("\n=== 总结 ===")
    print("1. 内置验证：isalpha()、isdigit()、isalnum()等")
    print("2. 高级验证：isdecimal()、isnumeric()、isidentifier()等")
    print("3. 格式验证：邮箱、电话、URL等常见格式")
    print("4. 自定义验证：密码强度、身份证、信用卡等")
    print("5. 数据清洗：用户输入清洗和类型转换")
    print("6. 正则验证：复杂模式匹配和验证")
    print("7. 最佳实践：组合使用多种验证方法")

if __name__ == "__main__":
    main()