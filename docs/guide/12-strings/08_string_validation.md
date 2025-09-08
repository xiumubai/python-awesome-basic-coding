# 字符串验证方法

## 学习目标

通过本节学习，你将掌握：
- Python内置字符串验证方法的使用
- 高级字符串验证技巧
- 常见格式的验证方法（邮箱、电话、URL等）
- 自定义验证函数的编写
- 数据清洗和验证的最佳实践
- 正则表达式在字符串验证中的应用

## 内置验证方法

### 基本字符验证

```python
def demonstrate_builtin_validation():
    """演示Python内置的字符串验证方法"""
    print("=== Python内置字符串验证方法 ===")
    
    test_strings = [
        "Hello",      # 纯字母
        "123",        # 纯数字
        "Hello123",   # 字母数字混合
        "Hello World", # 包含空格
        "hello",      # 小写字母
        "HELLO",      # 大写字母
        "Hello World!", # 包含标点
        "",           # 空字符串
        "   ",        # 空白字符
        "\t\n",       # 制表符和换行符
    ]
    
    # 验证方法列表
    methods = [
        ('isalpha', '是否为字母'),
        ('isdigit', '是否为数字'),
        ('isalnum', '是否为字母或数字'),
        ('isspace', '是否为空白字符'),
        ('islower', '是否为小写'),
        ('isupper', '是否为大写'),
        ('istitle', '是否为标题格式'),
        ('isprintable', '是否为可打印字符')
    ]
    
    # 打印表头
    print(f"{'字符串':<15}", end="")
    for method, desc in methods:
        print(f"{method:<10}", end="")
    print()
    print("-" * (15 + 10 * len(methods)))
    
    # 测试每个字符串
    for s in test_strings:
        display_s = repr(s) if len(s) <= 10 else repr(s[:10] + "...")
        print(f"{display_s:<15}", end="")
        
        for method, desc in methods:
            result = getattr(s, method)()
            print(f"{str(result):<10}", end="")
        print()
```

### 高级验证方法

```python
def demonstrate_advanced_validation():
    """演示高级字符串验证方法"""
    print("\n=== 高级字符串验证方法 ===")
    
    # 1. 数字验证的区别
    print("1. 数字验证方法的区别:")
    
    number_tests = [
        "123",        # 普通数字
        "123.45",     # 小数
        "½",          # 分数字符
        "²",          # 上标数字
        "Ⅴ",          # 罗马数字
        "一二三",      # 中文数字
        "-123",       # 负数
        "+123",       # 正数符号
    ]
    
    print(f"{'字符串':<10} {'isdigit':<8} {'isdecimal':<10} {'isnumeric':<10} {'说明':<20}")
    print("-" * 60)
    
    for s in number_tests:
        digit = s.isdigit()
        decimal = s.isdecimal()
        numeric = s.isnumeric()
        
        # 说明
        if s == "123":
            desc = "基本数字"
        elif s == "123.45":
            desc = "包含小数点"
        elif s == "½":
            desc = "Unicode分数"
        elif s == "²":
            desc = "Unicode上标"
        elif s == "Ⅴ":
            desc = "罗马数字"
        elif s == "一二三":
            desc = "中文数字"
        elif s == "-123":
            desc = "负数"
        elif s == "+123":
            desc = "带正号"
        else:
            desc = "其他"
        
        print(f"{s:<10} {digit!s:<8} {decimal!s:<10} {numeric!s:<10} {desc:<20}")
    
    # 2. 其他高级验证
    print("\n2. 其他高级验证方法:")
    
    advanced_tests = [
        ("Hello World", "istitle", "标题格式检查"),
        ("hello world", "istitle", "标题格式检查"),
        ("Hello world", "istitle", "标题格式检查"),
        ("variable_name", "isidentifier", "标识符检查"),
        ("123variable", "isidentifier", "标识符检查"),
        ("_private", "isidentifier", "标识符检查"),
        ("class", "isidentifier", "标识符检查"),
        ("Hello\nWorld", "isprintable", "可打印字符检查"),
        ("Hello World", "isprintable", "可打印字符检查"),
    ]
    
    print(f"{'字符串':<15} {'方法':<15} {'结果':<8} {'说明':<15}")
    print("-" * 60)
    
    for s, method, desc in advanced_tests:
        result = getattr(s, method)()
        display_s = repr(s) if '\n' in s else s
        print(f"{display_s:<15} {method:<15} {result!s:<8} {desc:<15}")
```

## 格式验证

### 邮箱和电话验证

```python
import re

def demonstrate_format_validation():
    """演示常见格式的验证方法"""
    print("\n=== 常见格式验证 ===")
    
    # 1. 邮箱验证
    print("1. 邮箱格式验证:")
    
    def validate_email_simple(email):
        """简单的邮箱验证"""
        return '@' in email and '.' in email.split('@')[-1]
    
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
        "user@domain..com",
    ]
    
    print(f"{'邮箱地址':<25} {'简单验证':<10} {'正则验证':<10}")
    print("-" * 50)
    
    for email in email_tests:
        simple_result = validate_email_simple(email)
        regex_result = validate_email_regex(email)
        print(f"{email:<25} {simple_result!s:<10} {regex_result!s:<10}")
    
    # 2. 电话号码验证
    print("\n2. 电话号码验证:")
    
    def validate_phone_simple(phone):
        """简单的电话号码验证"""
        # 移除所有非数字字符
        digits = ''.join(c for c in phone if c.isdigit())
        # 检查长度（中国手机号11位）
        return len(digits) == 11 and digits.startswith('1')
    
    def validate_phone_regex(phone):
        """使用正则表达式验证电话号码"""
        # 支持多种格式：138-1234-5678, 138 1234 5678, 13812345678
        pattern = r'^1[3-9]\d[\s-]?\d{4}[\s-]?\d{4}$'
        return re.match(pattern, phone) is not None
    
    phone_tests = [
        "13812345678",
        "138-1234-5678",
        "138 1234 5678",
        "021-12345678",
        "12345678901",
        "1381234567",
        "138123456789",
        "+86 138 1234 5678",
    ]
    
    print(f"{'电话号码':<20} {'简单验证':<10} {'正则验证':<10}")
    print("-" * 45)
    
    for phone in phone_tests:
        simple_result = validate_phone_simple(phone)
        regex_result = validate_phone_regex(phone)
        print(f"{phone:<20} {simple_result!s:<10} {regex_result!s:<10}")
```

### URL验证

```python
def validate_url_simple(url):
    """简单的URL验证"""
    return url.startswith(('http://', 'https://')) and '.' in url

def validate_url_regex(url):
    """使用正则表达式验证URL"""
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return re.match(pattern, url) is not None

url_tests = [
    "https://www.example.com",
    "http://example.com/path",
    "https://sub.domain.com/path?query=1",
    "ftp://example.com",
    "www.example.com",
    "https://",
    "https://example",
]

print("\n3. URL验证:")
print(f"{'URL':<35} {'简单验证':<10} {'正则验证':<10}")
print("-" * 60)

for url in url_tests:
    simple_result = validate_url_simple(url)
    regex_result = validate_url_regex(url)
    print(f"{url:<35} {simple_result!s:<10} {regex_result!s:<10}")
```

## 自定义验证函数

### 密码强度验证

```python
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
            '特殊字符': any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)
        }
        
        missing = [name for name, present in checks.items() if not present]
        
        if len(missing) == 0:
            return True, "强密码"
        elif len(missing) <= 1:
            return True, f"中等强度，建议添加{missing[0]}"
        else:
            return False, f"弱密码，缺少：{', '.join(missing)}"
    
    password_tests = [
        "123456",
        "password",
        "Password",
        "Password123",
        "Password123!",
        "P@ssw0rd",
        "MySecureP@ssw0rd2024",
    ]
    
    print(f"{'密码':<20} {'验证结果':<10} {'说明':<30}")
    print("-" * 65)
    
    for pwd in password_tests:
        valid, message = validate_password_strength(pwd)
        status = "通过" if valid else "失败"
        print(f"{pwd:<20} {status:<10} {message:<30}")
```

### 身份证和信用卡验证

```python
def validate_chinese_id(id_number):
    """验证中国身份证号码（简化版）"""
    if len(id_number) != 18:
        return False, "身份证号码应为18位"
    
    if not id_number[:17].isdigit():
        return False, "前17位应为数字"
    
    if id_number[17] not in '0123456789Xx':
        return False, "最后一位应为数字或X"
    
    # 简单的出生日期检查
    birth_year = int(id_number[6:10])
    birth_month = int(id_number[10:12])
    birth_day = int(id_number[12:14])
    
    if not (1900 <= birth_year <= 2024):
        return False, "出生年份不合理"
    
    if not (1 <= birth_month <= 12):
        return False, "出生月份不合理"
    
    if not (1 <= birth_day <= 31):
        return False, "出生日期不合理"
    
    return True, "身份证号码格式正确"

def validate_credit_card_luhn(card_number):
    """使用Luhn算法验证信用卡号"""
    # 移除空格和连字符
    card_number = card_number.replace(' ', '').replace('-', '')
    
    if not card_number.isdigit():
        return False, "信用卡号应只包含数字"
    
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
        return True, "信用卡号验证通过"
    else:
        return False, "信用卡号校验失败"

print("\n2. 身份证号验证:")
id_tests = [
    "11010119900101001X",
    "110101199001010010",
    "1101011990010100",
    "11010119900101001Y",
]

for id_num in id_tests:
    valid, message = validate_chinese_id(id_num)
    status = "✓" if valid else "✗"
    print(f"{status} {id_num}: {message}")

print("\n3. 信用卡号验证:")
card_tests = [
    "4532015112830366",  # 有效的Visa卡号
    "4532-0151-1283-0366",  # 带连字符
    "4532 0151 1283 0366",  # 带空格
    "1234567890123456",  # 无效卡号
]

for card in card_tests:
    valid, message = validate_credit_card_luhn(card)
    status = "✓" if valid else "✗"
    print(f"{status} {card}: {message}")
```

## 数据清洗和验证

### 用户输入清洗

```python
def demonstrate_data_cleaning_validation():
    """演示数据清洗和验证"""
    print("\n=== 数据清洗和验证 ===")
    
    # 1. 用户输入清洗
    print("1. 用户输入清洗:")
    
    def clean_user_input(text):
        """清洗用户输入"""
        if not isinstance(text, str):
            return ""
        
        # 移除首尾空白
        text = text.strip()
        
        # 移除多余的空白字符
        text = ' '.join(text.split())
        
        # 移除控制字符
        text = ''.join(char for char in text if char.isprintable())
        
        return text
    
    def validate_user_name(name):
        """验证用户名"""
        # 先清洗输入
        clean_name = clean_user_input(name)
        
        if not clean_name:
            return False, "用户名不能为空"
        
        if len(clean_name) < 2:
            return False, "用户名至少2个字符"
        
        if len(clean_name) > 20:
            return False, "用户名不能超过20个字符"
        
        # 只允许字母、数字、下划线和中文
        if not re.match(r'^[a-zA-Z0-9_\u4e00-\u9fff]+$', clean_name):
            return False, "用户名只能包含字母、数字、下划线和中文"
        
        return True, clean_name
    
    name_tests = [
        "  Alice  ",
        "Bob123",
        "用户名",
        "user_name",
        "a",
        "a" * 25,
        "user@name",
        "\t\nAlice\t\n",
        "",
        "   ",
    ]
    
    print(f"{'原始输入':<20} {'验证结果':<10} {'清洗后/错误信息':<30}")
    print("-" * 65)
    
    for name in name_tests:
        valid, result = validate_user_name(name)
        status = "通过" if valid else "失败"
        display_input = repr(name) if len(name) <= 15 else repr(name[:15] + "...")
        print(f"{display_input:<20} {status:<10} {result:<30}")
```

### 数据类型验证和转换

```python
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

print("\n2. 数据类型验证和转换:")
print(f"{'输入值':<15} {'类型':<10} {'整数转换':<15} {'浮点转换':<15}")
print("-" * 60)

for value, desc in conversion_tests:
    int_valid, int_result = safe_int_convert(value)
    float_valid, float_result = safe_float_convert(value)
    
    int_display = str(int_result) if int_valid else "失败"
    float_display = str(float_result) if float_valid else "失败"
    
    print(f"{repr(value):<15} {desc:<10} {int_display:<15} {float_display:<15}")
```

## 正则表达式验证

### 常用正则模式

```python
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
```

### 复杂验证示例

```python
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
```

## 完整示例代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字符串验证方法

本模块演示了Python中各种字符串验证方法的使用，包括：
1. 内置验证方法（isalpha, isdigit等）
2. 高级验证方法（isdecimal, isnumeric等）
3. 格式验证（邮箱、电话、URL等）
4. 自定义验证函数
5. 数据清洗和验证
6. 正则表达式验证

作者：Python学习助手
日期：2024年1月
"""

import re

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
```

## 运行示例

```bash
# 运行字符串验证演示
python3 07_string_validation.py
```

## 学习要点

### 1. 内置验证方法
- `isalpha()`: 检查是否只包含字母
- `isdigit()`: 检查是否只包含数字
- `isalnum()`: 检查是否只包含字母和数字
- `isspace()`: 检查是否只包含空白字符
- `islower()`/`isupper()`: 检查大小写
- `istitle()`: 检查标题格式
- `isprintable()`: 检查是否为可打印字符

### 2. 数字验证区别
- `isdigit()`: 只识别0-9数字字符
- `isdecimal()`: 识别十进制数字字符
- `isnumeric()`: 识别所有数字字符（包括分数、上标等）

### 3. 格式验证技巧
- 简单验证：快速但不够严格
- 正则验证：严格但复杂
- 组合验证：平衡准确性和性能

### 4. 自定义验证原则
- 明确验证规则
- 提供清晰的错误信息
- 考虑边界情况
- 支持数据清洗

## 实际应用场景

1. **用户注册验证**：用户名、密码、邮箱格式检查
2. **数据导入验证**：CSV文件数据格式验证
3. **API参数验证**：请求参数的格式和类型检查
4. **表单验证**：Web表单输入的客户端和服务端验证
5. **数据清洗**：清理和标准化用户输入数据

## 注意事项

1. **性能考虑**：复杂正则表达式可能影响性能
2. **国际化支持**：考虑不同语言和地区的格式差异
3. **安全性**：验证用户输入防止注入攻击
4. **用户体验**：提供友好的错误提示信息
5. **维护性**：将验证规则集中管理，便于修改

## 下一步学习

学习完字符串验证后，建议继续学习：
- 字符串编码和解码（08_string_encoding.py）
- 正则表达式进阶（09_regular_expressions.py）
- 字符串处理综合练习（10_exercises.py）
- 数据验证框架的使用
- Web表单验证的实现