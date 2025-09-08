# 输入验证和类型转换

## 概述

本节学习如何对用户输入进行验证和类型转换，这是编程中非常重要的技能。通过合适的输入验证，我们可以确保程序的健壮性和安全性。

## 学习目标

- 掌握基本的类型转换方法
- 学会使用异常处理机制处理转换错误
- 了解输入验证的重要性和常用策略
- 实现安全的输入转换函数
- 掌握数值范围验证和字符串格式验证
- 学会设计循环输入直到有效的机制

## 完整代码

```python
"""
输入验证和类型转换
学习目标：
1. 掌握基本的类型转换
2. 学会处理转换异常
3. 实现输入验证
4. 了解安全编程实践
"""

# ============================================================================
# 1. 基本类型转换
# ============================================================================

print("=" * 50)
print("1. 基本类型转换")
print("=" * 50)

# 模拟用户输入
user_input = "25"
print(f"用户输入：{user_input}")
print(f"输入类型：{type(user_input)}")

# 转换为整数
age = int(user_input)
print(f"转换为整数：{age}")
print(f"转换后类型：{type(age)}")

# 转换为浮点数
user_input_float = "3.14"
print(f"\n用户输入：{user_input_float}")
pi = float(user_input_float)
print(f"转换为浮点数：{pi}")
print(f"转换后类型：{type(pi)}")

# 转换为布尔值（注意：非空字符串都是True）
user_input_bool = "True"
print(f"\n用户输入：{user_input_bool}")
# 字符串转布尔需要特殊处理
if user_input_bool.lower() in ['true', '1', 'yes', 'y']:
    result = True
elif user_input_bool.lower() in ['false', '0', 'no', 'n']:
    result = False
else:
    result = None
print(f"转换为布尔值：{result}")

# ============================================================================
# 2. 类型转换异常处理
# ============================================================================

print("\n" + "=" * 50)
print("2. 类型转换异常处理")
print("=" * 50)

# 处理无效的整数转换
invalid_inputs = ["abc", "12.5", "", "  ", "123abc"]

for invalid_input in invalid_inputs:
    print(f"\n尝试转换：'{invalid_input}'")
    try:
        result = int(invalid_input)
        print(f"转换成功：{result}")
    except ValueError as e:
        print(f"转换失败：{e}")

# 处理浮点数转换异常
print("\n--- 浮点数转换异常 ---")
float_inputs = ["3.14", "abc", "1.2.3", "inf", "nan"]

for float_input in float_inputs:
    print(f"\n尝试转换：'{float_input}'")
    try:
        result = float(float_input)
        print(f"转换成功：{result}")
        # 检查特殊值
        if result != result:  # NaN检查
            print("警告：结果是NaN")
        elif result == float('inf') or result == float('-inf'):
            print("警告：结果是无穷大")
    except ValueError as e:
        print(f"转换失败：{e}")

# ============================================================================
# 3. 安全的输入转换函数
# ============================================================================

print("\n" + "=" * 50)
print("3. 安全的输入转换函数")
print("=" * 50)

def safe_int_input(prompt, default=None):
    """
    安全的整数输入函数
    
    Args:
        prompt: 提示信息
        default: 默认值
    
    Returns:
        int or None: 转换后的整数或默认值
    """
    # 模拟用户输入
    user_input = "25"  # 这里用固定值模拟
    print(f"{prompt}{user_input}")
    
    try:
        return int(user_input.strip())
    except ValueError:
        print(f"输入'{user_input}'不是有效的整数")
        if default is not None:
            print(f"使用默认值：{default}")
            return default
        return None

def safe_float_input(prompt, default=None):
    """
    安全的浮点数输入函数
    
    Args:
        prompt: 提示信息
        default: 默认值
    
    Returns:
        float or None: 转换后的浮点数或默认值
    """
    # 模拟用户输入
    user_input = "3.14"  # 这里用固定值模拟
    print(f"{prompt}{user_input}")
    
    try:
        result = float(user_input.strip())
        # 检查特殊值
        if result != result:  # NaN
            print("警告：输入是NaN，使用默认值")
            return default
        if result == float('inf') or result == float('-inf'):
            print("警告：输入是无穷大，使用默认值")
            return default
        return result
    except ValueError:
        print(f"输入'{user_input}'不是有效的浮点数")
        if default is not None:
            print(f"使用默认值：{default}")
            return default
        return None

# 测试安全输入函数
print("\n--- 测试安全输入函数 ---")
age = safe_int_input("请输入年龄：", 18)
print(f"获取的年龄：{age}")

score = safe_float_input("请输入分数：", 0.0)
print(f"获取的分数：{score}")

# ============================================================================
# 4. 输入范围验证
# ============================================================================

print("\n" + "=" * 50)
print("4. 输入范围验证")
print("=" * 50)

def get_age_input():
    """
    获取有效的年龄输入（0-150岁）
    
    Returns:
        int or None: 有效的年龄或None
    """
    # 模拟用户输入
    user_input = "25"
    print(f"请输入年龄（0-150岁）：{user_input}")
    
    try:
        age = int(user_input.strip())
        
        # 验证范围
        if age < 0:
            print("年龄不能为负数")
            return None
        elif age > 150:
            print("年龄不能超过150岁")
            return None
        else:
            print(f"年龄输入有效：{age}岁")
            return age
            
    except ValueError:
        print(f"'{user_input}'不是有效的数字")
        return None

def get_score_input():
    """
    获取有效的分数输入（0-100分）
    
    Returns:
        float or None: 有效的分数或None
    """
    # 模拟用户输入
    user_input = "85.5"
    print(f"请输入分数（0-100分）：{user_input}")
    
    try:
        score = float(user_input.strip())
        
        # 验证范围
        if score < 0:
            print("分数不能为负数")
            return None
        elif score > 100:
            print("分数不能超过100分")
            return None
        else:
            print(f"分数输入有效：{score}分")
            return score
            
    except ValueError:
        print(f"'{user_input}'不是有效的数字")
        return None

def get_percentage_input():
    """
    获取百分比输入（0%-100%）
    
    Returns:
        float or None: 有效的百分比（小数形式）或None
    """
    # 模拟用户输入
    user_input = "75%"
    print(f"请输入百分比（如：75%）：{user_input}")
    
    try:
        # 处理百分号
        if user_input.strip().endswith('%'):
            number_str = user_input.strip()[:-1]
            percentage = float(number_str)
        else:
            percentage = float(user_input.strip())
        
        # 验证范围
        if percentage < 0:
            print("百分比不能为负数")
            return None
        elif percentage > 100:
            print("百分比不能超过100%")
            return None
        else:
            decimal_value = percentage / 100
            print(f"百分比输入有效：{percentage}%（小数：{decimal_value}）")
            return decimal_value
            
    except ValueError:
        print(f"'{user_input}'不是有效的百分比")
        return None

# 测试范围验证
print("\n--- 测试范围验证 ---")
age = get_age_input()
score = get_score_input()
percentage = get_percentage_input()

print(f"\n验证结果：")
print(f"年龄：{age}")
print(f"分数：{score}")
print(f"百分比：{percentage}")

# ============================================================================
# 5. 字符串输入验证
# ============================================================================

print("\n" + "=" * 50)
print("5. 字符串输入验证")
print("=" * 50)

def validate_name(name):
    """
    验证姓名输入
    
    Args:
        name: 输入的姓名
    
    Returns:
        bool: 是否有效
    """
    name = name.strip()
    
    # 检查是否为空
    if not name:
        print("姓名不能为空")
        return False
    
    # 检查长度
    if len(name) < 2 or len(name) > 20:
        print("姓名长度应在2-20个字符之间")
        return False
    
    # 检查是否包含数字
    if any(char.isdigit() for char in name):
        print("姓名不应包含数字")
        return False
    
    return True

def validate_email(email):
    """
    简单的邮箱验证
    
    Args:
        email: 输入的邮箱
    
    Returns:
        bool: 是否有效
    """
    email = email.strip()
    
    # 基本格式检查
    if '@' not in email:
        print("邮箱格式错误：缺少@符号")
        return False
    
    if email.count('@') != 1:
        print("邮箱格式错误：@符号数量不正确")
        return False
    
    local, domain = email.split('@')
    
    if not local or not domain:
        print("邮箱格式错误：@前后不能为空")
        return False
    
    if '.' not in domain:
        print("邮箱格式错误：域名格式不正确")
        return False
    
    return True

# 测试字符串验证
print("\n--- 测试姓名验证 ---")
test_names = ["张三", "李四", "", "a", "这是一个非常长的姓名超过了限制", "张3"]

for name in test_names:
    print(f"验证姓名'{name}'：{validate_name(name)}")

print("\n--- 测试邮箱验证 ---")
test_emails = [
    "user@example.com",
    "invalid-email",
    "user@@example.com",
    "@example.com",
    "user@",
    "user@example"
]

for email in test_emails:
    print(f"验证邮箱'{email}'：{validate_email(email)}")

# ============================================================================
# 6. 循环输入直到有效
# ============================================================================

print("\n" + "=" * 50)
print("6. 循环输入直到有效")
print("=" * 50)

def get_valid_integer(prompt, min_val=None, max_val=None, max_attempts=3):
    """
    循环获取有效整数输入
    
    Args:
        prompt: 提示信息
        min_val: 最小值
        max_val: 最大值
        max_attempts: 最大尝试次数
    
    Returns:
        int or None: 有效整数或None（超过最大尝试次数）
    """
    # 模拟用户输入序列
    mock_inputs = ["abc", "200", "25"]  # 第一次无效，第二次超范围，第三次有效
    attempt = 0
    
    for attempt in range(max_attempts):
        try:
            # 模拟用户输入
            user_input = mock_inputs[attempt] if attempt < len(mock_inputs) else "25"
            print(f"\n尝试 {attempt + 1}/{max_attempts}")
            print(f"{prompt}{user_input}")
            
            value = int(user_input.strip())
            
            # 检查范围
            if min_val is not None and value < min_val:
                print(f"输入值{value}小于最小值{min_val}")
                continue
            
            if max_val is not None and value > max_val:
                print(f"输入值{value}大于最大值{max_val}")
                continue
            
            print(f"输入有效：{value}")
            return value
            
        except ValueError:
            print(f"'{user_input}'不是有效的整数")
    
    print(f"\n超过最大尝试次数({max_attempts})，输入失败")
    return None

# 测试循环输入
print("\n--- 测试循环输入验证 ---")
result = get_valid_integer("请输入年龄（18-65）：", 18, 65, 3)
print(f"\n最终结果：{result}")

# ============================================================================
# 7. 综合应用示例
# ============================================================================

print("\n" + "=" * 50)
print("7. 综合应用示例")
print("=" * 50)

def collect_user_info():
    """
    收集用户信息的综合示例
    """
    print("\n=== 用户信息收集系统 ===")
    
    # 模拟用户输入
    user_data = {
        'name': '张三',
        'age': '25',
        'email': 'zhangsan@example.com',
        'score': '85.5'
    }
    
    # 收集姓名
    print(f"\n请输入姓名：{user_data['name']}")
    name = user_data['name']
    if not validate_name(name):
        print("姓名验证失败")
        return None
    
    # 收集年龄
    print(f"请输入年龄：{user_data['age']}")
    try:
        age = int(user_data['age'])
        if not (0 <= age <= 150):
            print("年龄超出有效范围")
            return None
    except ValueError:
        print("年龄格式错误")
        return None
    
    # 收集邮箱
    print(f"请输入邮箱：{user_data['email']}")
    email = user_data['email']
    if not validate_email(email):
        print("邮箱验证失败")
        return None
    
    # 收集分数
    print(f"请输入分数：{user_data['score']}")
    try:
        score = float(user_data['score'])
        if not (0 <= score <= 100):
            print("分数超出有效范围")
            return None
    except ValueError:
        print("分数格式错误")
        return None
    
    # 返回收集的信息
    return {
        'name': name,
        'age': age,
        'email': email,
        'score': score
    }

# 运行综合示例
user_info = collect_user_info()
if user_info:
    print("\n=== 信息收集成功 ===")
    print(f"姓名：{user_info['name']}")
    print(f"年龄：{user_info['age']}岁")
    print(f"邮箱：{user_info['email']}")
    print(f"分数：{user_info['score']}分")
else:
    print("\n信息收集失败")

# ============================================================================
# 8. 练习题
# ============================================================================

print("\n" + "=" * 50)
print("8. 练习题")
print("=" * 50)

print("""
练习题：

1. 基础练习：
   - 编写函数验证手机号码格式（11位数字）
   - 编写函数获取有效的百分比输入（0-100%）
   - 实现一个安全的除法计算器（处理除零错误）

2. 进阶练习：
   - 编写一个学生成绩管理系统的输入验证模块
   - 实现一个带重试机制的用户注册系统
   - 编写函数验证身份证号码格式

3. 思考题：
   - 为什么需要对用户输入进行验证？
   - 如何平衡用户体验和输入验证的严格性？
   - 在什么情况下应该使用异常处理？

4. 挑战练习：
   - 实现一个通用的输入验证框架
   - 编写一个支持多种数据类型的配置文件读取器
   - 实现一个智能的输入建议系统
""")

# ============================================================================
# 9. 知识点总结
# ============================================================================

print("\n" + "=" * 50)
print("9. 知识点总结")
print("=" * 50)

print("""
知识点总结：

1. 类型转换：
   - int(): 转换为整数
   - float(): 转换为浮点数
   - str(): 转换为字符串
   - 转换可能抛出ValueError异常

2. 异常处理：
   - 使用try-except处理转换错误
   - ValueError: 类型转换失败
   - 提供默认值或重新输入机制

3. 输入验证策略：
   - 类型验证：确保数据类型正确
   - 范围验证：确保数值在有效范围内
   - 格式验证：确保字符串格式正确
   - 逻辑验证：确保数据符合业务逻辑

4. 最佳实践：
   - 提供清晰的错误信息
   - 实现重试机制
   - 设置合理的默认值
   - 考虑用户体验

5. 常用验证模式：
   - 立即验证：输入后立即检查
   - 批量验证：收集所有输入后统一验证
   - 渐进验证：逐步引导用户输入正确数据
""")

print("\n程序运行完成！")
print("建议：尝试修改模拟输入，测试不同的验证场景。")
```

## 代码详解

### 1. 基本类型转换

- **int()函数**：将字符串转换为整数
- **float()函数**：将字符串转换为浮点数
- **类型检查**：使用type()函数检查数据类型

### 2. 异常处理机制

- **try-except语句**：捕获转换过程中的异常
- **ValueError异常**：当转换失败时抛出
- **错误信息处理**：提供友好的错误提示

### 3. 输入验证策略

- **类型验证**：确保输入可以转换为目标类型
- **范围验证**：检查数值是否在有效范围内
- **格式验证**：验证字符串是否符合特定格式
- **逻辑验证**：确保数据符合业务规则

### 4. 安全编程实践

- **防御性编程**：假设所有输入都可能有问题
- **默认值机制**：为无效输入提供合理的默认值
- **重试机制**：允许用户重新输入
- **清晰的错误信息**：帮助用户理解问题所在

## 学习要点

1. **理解类型转换的重要性**：用户输入默认是字符串类型
2. **掌握异常处理**：使用try-except处理转换错误
3. **实现输入验证**：确保数据的有效性和安全性
4. **设计用户友好的界面**：提供清晰的提示和错误信息
5. **考虑边界情况**：处理空输入、特殊字符等情况

## 实践练习

1. **基础练习**：
   - 编写手机号码验证函数
   - 实现安全的数学计算器
   - 创建用户注册验证系统

2. **进阶练习**：
   - 设计通用的输入验证框架
   - 实现配置文件解析器
   - 创建智能输入建议系统

## 运行示例

```bash
# 运行完整程序
python 02_input_validation.py

# 预期输出：展示各种输入验证场景
# 包括成功和失败的验证示例
```

## 扩展思考

1. **为什么需要输入验证？**
   - 防止程序崩溃
   - 确保数据质量
   - 提高用户体验
   - 增强程序安全性

2. **如何平衡严格性和用户体验？**
   - 提供清晰的错误信息
   - 允许合理的重试次数
   - 提供输入建议和示例
   - 考虑用户的使用习惯

3. **什么时候使用异常处理？**
   - 类型转换可能失败时
   - 文件操作可能出错时
   - 网络请求可能超时时
   - 任何可能出现错误的操作

---

## 模块导航

- [返回目录](./index.md)
- [上一节：基础输入](./basic-input.md)
- [下一节：基础输出](./basic-output.md)
- [返回首页](../../index.md)