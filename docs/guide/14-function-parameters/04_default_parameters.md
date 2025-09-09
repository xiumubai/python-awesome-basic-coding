# 默认参数 (Default Parameters)

默认参数是Python函数中一个非常实用的特性，它允许你为函数参数设置默认值。当调用函数时，如果没有提供该参数的值，就会使用默认值。这大大简化了函数的调用，提高了代码的灵活性。

## 核心概念

### 什么是默认参数？
默认参数是在函数定义时就指定了默认值的参数。调用函数时，这些参数是可选的，如果不提供值，就使用默认值。

### 特点
- **可选性**：调用时可以省略有默认值的参数
- **向后兼容**：添加新参数时不会破坏现有代码
- **简化调用**：常用配置可以设为默认值
- **灵活性**：可以根据需要覆盖默认值

## 基础用法

### 简单默认参数

```python
def greet_user(name, greeting="你好"):
    """
    问候用户
    
    Args:
        name: 用户名（必需）
        greeting: 问候语（可选，默认为"你好"）
    """
    message = f"{greeting}，{name}！"
    print(message)
    return message

# 使用默认值
greet_user("小明")  # 输出: 你好，小明！

# 覆盖默认值
greet_user("小红", "早上好")  # 输出: 早上好，小红！
greet_user("小李", greeting="晚上好")  # 输出: 晚上好，小李！
```

### 多个默认参数

```python
def create_user_account(username, email, role="user", active=True, notifications=True):
    """
    创建用户账户
    
    Args:
        username: 用户名（必需）
        email: 邮箱（必需）
        role: 用户角色（默认为"user"）
        active: 账户是否激活（默认为True）
        notifications: 是否接收通知（默认为True）
    """
    account = {
        "username": username,
        "email": email,
        "role": role,
        "active": active,
        "notifications": notifications
    }
    
    print(f"创建账户: {username}")
    print(f"邮箱: {email}")
    print(f"角色: {role}")
    print(f"状态: {'激活' if active else '未激活'}")
    print(f"通知: {'开启' if notifications else '关闭'}")
    print("-" * 30)
    
    return account

# 只使用必需参数
create_user_account("john_doe", "john@example.com")

# 部分覆盖默认值
create_user_account("admin_user", "admin@example.com", role="admin")

# 覆盖多个默认值
create_user_account("test_user", "test@example.com", 
                   role="tester", active=False, notifications=False)
```

## 实际应用示例

### 数值计算函数

```python
def calculate_compound_interest(principal, rate, time, compound_frequency=1):
    """
    计算复利
    
    Args:
        principal: 本金
        rate: 年利率（小数形式，如0.05表示5%）
        time: 时间（年）
        compound_frequency: 复利频率（每年复利次数，默认为1）
    """
    amount = principal * (1 + rate/compound_frequency) ** (compound_frequency * time)
    interest = amount - principal
    
    print(f"本金: ¥{principal:,.2f}")
    print(f"年利率: {rate*100:.2f}%")
    print(f"时间: {time}年")
    print(f"复利频率: 每年{compound_frequency}次")
    print(f"最终金额: ¥{amount:,.2f}")
    print(f"利息收入: ¥{interest:,.2f}")
    print("-" * 40)
    
    return amount, interest

# 使用默认复利频率（年复利）
calculate_compound_interest(10000, 0.05, 5)

# 月复利
calculate_compound_interest(10000, 0.05, 5, compound_frequency=12)

# 日复利
calculate_compound_interest(10000, 0.05, 5, compound_frequency=365)
```

### 字符串处理函数

```python
def format_text(text, uppercase=False, remove_spaces=False, 
                add_prefix="", add_suffix="", max_length=None):
    """
    格式化文本
    
    Args:
        text: 原始文本
        uppercase: 是否转为大写（默认False）
        remove_spaces: 是否移除空格（默认False）
        add_prefix: 添加前缀（默认为空）
        add_suffix: 添加后缀（默认为空）
        max_length: 最大长度限制（默认无限制）
    """
    result = text
    
    print(f"原始文本: '{text}'")
    
    # 转换大小写
    if uppercase:
        result = result.upper()
        print(f"转为大写: '{result}'")
    
    # 移除空格
    if remove_spaces:
        result = result.replace(" ", "")
        print(f"移除空格: '{result}'")
    
    # 添加前缀和后缀
    if add_prefix:
        result = add_prefix + result
        print(f"添加前缀: '{result}'")
    
    if add_suffix:
        result = result + add_suffix
        print(f"添加后缀: '{result}'")
    
    # 长度限制
    if max_length and len(result) > max_length:
        result = result[:max_length] + "..."
        print(f"长度限制: '{result}'")
    
    print(f"最终结果: '{result}'")
    print("-" * 40)
    
    return result

# 基本使用
format_text("Hello World")

# 多种格式化选项
format_text("hello world", uppercase=True, add_prefix=">>> ", add_suffix=" <<<")

# 复杂格式化
format_text("This is a very long text that needs to be processed", 
           remove_spaces=True, add_prefix="[LOG] ", max_length=20)
```

### 文件操作函数

```python
def read_file_content(filename, encoding='utf-8', strip_whitespace=True, 
                     split_lines=False, ignore_empty_lines=False):
    """
    读取文件内容
    
    Args:
        filename: 文件名
        encoding: 文件编码（默认utf-8）
        strip_whitespace: 是否去除首尾空白（默认True）
        split_lines: 是否按行分割（默认False）
        ignore_empty_lines: 是否忽略空行（默认False）
    """
    try:
        print(f"读取文件: {filename}")
        print(f"编码: {encoding}")
        
        # 模拟文件内容（实际应用中会真正读取文件）
        sample_content = """  第一行内容  
        
第二行内容
   第三行内容   

最后一行
  """
        
        content = sample_content
        
        if strip_whitespace:
            if split_lines:
                lines = content.split('\n')
                content = [line.strip() for line in lines]
                print("已去除每行首尾空白")
            else:
                content = content.strip()
                print("已去除整体首尾空白")
        
        if split_lines and isinstance(content, str):
            content = content.split('\n')
            print("已按行分割")
        
        if ignore_empty_lines and isinstance(content, list):
            content = [line for line in content if line.strip()]
            print("已忽略空行")
        
        print(f"处理结果类型: {type(content).__name__}")
        if isinstance(content, list):
            print(f"行数: {len(content)}")
            for i, line in enumerate(content, 1):
                print(f"  第{i}行: '{line}'")
        else:
            print(f"内容长度: {len(content)}")
            print(f"内容预览: '{content[:50]}{'...' if len(content) > 50 else ''}'")
        
        print("-" * 40)
        return content
        
    except Exception as e:
        print(f"读取文件出错: {e}")
        return None

# 基本读取
read_file_content("example.txt")

# 按行读取，忽略空行
read_file_content("example.txt", split_lines=True, ignore_empty_lines=True)

# 保留原始格式
read_file_content("example.txt", strip_whitespace=False, split_lines=True)
```

### 数据处理函数

```python
def process_data_list(data, sort_data=False, reverse_sort=False, 
                     remove_duplicates=False, filter_function=None, 
                     transform_function=None):
    """
    处理数据列表
    
    Args:
        data: 数据列表
        sort_data: 是否排序（默认False）
        reverse_sort: 是否逆序排序（默认False）
        remove_duplicates: 是否去重（默认False）
        filter_function: 过滤函数（默认None）
        transform_function: 转换函数（默认None）
    """
    result = data.copy()  # 避免修改原始数据
    
    print(f"原始数据: {data}")
    print(f"数据长度: {len(data)}")
    
    # 去重
    if remove_duplicates:
        result = list(set(result))
        print(f"去重后: {result}")
    
    # 过滤
    if filter_function:
        result = [item for item in result if filter_function(item)]
        print(f"过滤后: {result}")
    
    # 转换
    if transform_function:
        result = [transform_function(item) for item in result]
        print(f"转换后: {result}")
    
    # 排序
    if sort_data:
        try:
            result.sort(reverse=reverse_sort)
            sort_order = "降序" if reverse_sort else "升序"
            print(f"排序后({sort_order}): {result}")
        except TypeError as e:
            print(f"排序失败: {e}")
    
    print(f"最终结果: {result}")
    print(f"处理后长度: {len(result)}")
    print("-" * 40)
    
    return result

# 基本处理
data1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
process_data_list(data1)

# 排序和去重
process_data_list(data1, sort_data=True, remove_duplicates=True)

# 复杂处理：过滤偶数，平方，降序排列
process_data_list(
    data1,
    filter_function=lambda x: x % 2 == 0,  # 只保留偶数
    transform_function=lambda x: x ** 2,   # 平方
    sort_data=True,
    reverse_sort=True
)

# 字符串处理
data2 = ["apple", "banana", "cherry", "apple", "date"]
process_data_list(
    data2,
    remove_duplicates=True,
    transform_function=str.upper,
    sort_data=True
)
```

## 默认参数的陷阱和最佳实践

### 1. 可变对象陷阱

```python
# 错误的做法：使用可变对象作为默认值
def bad_append_to_list(item, target_list=[]):
    """危险！默认参数是可变对象"""
    target_list.append(item)
    return target_list

# 这会导致问题
print("第一次调用:", bad_append_to_list(1))  # [1]
print("第二次调用:", bad_append_to_list(2))  # [1, 2] - 不是期望的[2]！
print("第三次调用:", bad_append_to_list(3))  # [1, 2, 3] - 问题更严重！

print("-" * 40)

# 正确的做法：使用None作为默认值
def good_append_to_list(item, target_list=None):
    """正确的方式"""
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

# 这样就正常了
print("第一次调用:", good_append_to_list(1))  # [1]
print("第二次调用:", good_append_to_list(2))  # [2]
print("第三次调用:", good_append_to_list(3))  # [3]
```

### 2. 默认参数的最佳实践

```python
def create_config(app_name, debug=False, log_level="INFO", 
                 database_url=None, cache_settings=None, 
                 feature_flags=None):
    """
    创建应用配置
    
    最佳实践：
    1. 不可变对象可以直接作为默认值
    2. 可变对象使用None，在函数内部创建
    3. 布尔值和字符串可以安全使用
    """
    # 处理可变默认参数
    if cache_settings is None:
        cache_settings = {"enabled": True, "timeout": 300}
    
    if feature_flags is None:
        feature_flags = []
    
    config = {
        "app_name": app_name,
        "debug": debug,
        "log_level": log_level,
        "database_url": database_url or "sqlite:///default.db",
        "cache_settings": cache_settings,
        "feature_flags": feature_flags
    }
    
    print(f"应用配置: {app_name}")
    for key, value in config.items():
        print(f"  {key}: {value}")
    print("-" * 40)
    
    return config

# 使用默认配置
create_config("MyApp")

# 自定义配置
create_config(
    "ProductionApp",
    debug=False,
    log_level="ERROR",
    database_url="postgresql://user:pass@localhost/prod",
    cache_settings={"enabled": True, "timeout": 600},
    feature_flags=["feature_a", "feature_b"]
)
```

### 3. 参数顺序和设计原则

```python
def design_good_function(required_param1, required_param2,
                        common_optional="default_value",
                        less_common_optional=None,
                        advanced_option=False):
    """
    良好的函数设计原则：
    1. 必需参数在前
    2. 常用的可选参数在中间
    3. 高级或不常用的参数在后
    4. 布尔开关通常默认为False
    """
    print(f"必需参数1: {required_param1}")
    print(f"必需参数2: {required_param2}")
    print(f"常用可选参数: {common_optional}")
    print(f"不常用可选参数: {less_common_optional}")
    print(f"高级选项: {advanced_option}")
    print("-" * 40)

# 易于使用的调用方式
design_good_function("value1", "value2")
design_good_function("value1", "value2", "custom_value")
design_good_function("value1", "value2", advanced_option=True)
```

## 运行示例

要运行这些示例，请使用以下命令：

```bash
python3 03_default_parameters.py
```

## 学习要点

1. **简化调用**：默认参数让函数更易用
2. **向后兼容**：添加新参数不会破坏现有代码
3. **避免陷阱**：不要使用可变对象作为默认值
4. **合理设计**：常用配置设为默认值
5. **参数顺序**：必需参数在前，可选参数在后
6. **使用None模式**：对于可变默认参数使用None

## 下一步

掌握了默认参数后，接下来学习[可变长度参数(*args)](05_variable_length_args.md)，了解如何处理不定数量的参数。