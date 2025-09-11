# 正则表达式 - re模块

## 学习目标

通过本节学习，你将掌握：
- 正则表达式的基本语法和概念
- re模块的各种函数和方法
- 模式匹配和字符串操作技巧
- 分组和捕获的使用方法
- 正则表达式的编译和性能优化
- 实际项目中的应用场景

## 核心概念

### 正则表达式基础
- **元字符**: `.` `*` `+` `?` `^` `$` `[]` `{}` `()` `|` `\`
- **字符类**: `\d` `\w` `\s` `\D` `\W` `\S`
- **量词**: `*` `+` `?` `{n}` `{n,}` `{n,m}`
- **锚点**: `^` `$` `\b` `\B`

### re模块主要函数
- **re.match()**: 从字符串开头匹配
- **re.search()**: 搜索第一个匹配
- **re.findall()**: 查找所有匹配
- **re.sub()**: 替换匹配的内容
- **re.split()**: 按模式分割字符串

## 代码示例

### 1. 正则表达式基础

```python
import re
from datetime import datetime
import json

def regex_basics_demo():
    """正则表达式基础演示"""
    print("=" * 50)
    print("正则表达式基础演示")
    print("=" * 50)
    
    # 测试文本
    text = "Hello World! My phone is 138-1234-5678, email: user@example.com. Today is 2024-01-15."
    
    # 1. 基本匹配
    print("1. 基本匹配:")
    patterns = [
        (r"Hello", "匹配Hello"),
        (r"\d+", "匹配数字"),
        (r"\w+", "匹配单词"),
        (r"\S+@\S+", "匹配邮箱"),
        (r"\d{4}-\d{2}-\d{2}", "匹配日期")
    ]
    
    for pattern, description in patterns:
        match = re.search(pattern, text)
        if match:
            print(f"  {description}: '{match.group()}' (位置: {match.start()}-{match.end()})")
        else:
            print(f"  {description}: 未找到匹配")
    
    # 2. 查找所有匹配
    print("\n2. 查找所有匹配:")
    all_words = re.findall(r"\w+", text)
    print(f"  所有单词: {all_words}")
    
    all_numbers = re.findall(r"\d+", text)
    print(f"  所有数字: {all_numbers}")
    
    # 3. 匹配对象的详细信息
    print("\n3. 匹配对象详细信息:")
    phone_pattern = r"(\d{3})-(\d{4})-(\d{4})"
    phone_match = re.search(phone_pattern, text)
    
    if phone_match:
        print(f"  完整匹配: {phone_match.group(0)}")
        print(f"  第一组: {phone_match.group(1)}")
        print(f"  第二组: {phone_match.group(2)}")
        print(f"  第三组: {phone_match.group(3)}")
        print(f"  所有组: {phone_match.groups()}")
        print(f"  匹配位置: {phone_match.span()}")
```

### 2. 模式匹配验证

```python
def pattern_matching_demo():
    """模式匹配演示"""
    # 邮箱验证
    print("1. 邮箱验证:")
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    test_emails = [
        "user@example.com",
        "admin@company.org", 
        "invalid-email",
        "test@domain",
        "good.email@sub.domain.com"
    ]
    
    for email in test_emails:
        if re.match(email_pattern, email):
            print(f"  ✓ {email} - 有效邮箱")
        else:
            print(f"  ✗ {email} - 无效邮箱")
    
    # 手机号验证
    print("\n2. 手机号验证:")
    phone_numbers = [
        "13812345678",
        "138-1234-5678", 
        "138 1234 5678",
        "12345678901",
        "+86 138 1234 5678"
    ]
    
    phone_patterns = [
        (r"^1[3-9]\d{9}$", "标准手机号"),
        (r"^1[3-9]\d-\d{4}-\d{4}$", "带短横线"),
        (r"^1[3-9]\d \d{4} \d{4}$", "带空格"),
        (r"^\+86 1[3-9]\d \d{4} \d{4}$", "国际格式")
    ]
    
    for phone in phone_numbers:
        print(f"  测试: {phone}")
        matched = False
        for pattern, desc in phone_patterns:
            if re.match(pattern, phone):
                print(f"    ✓ 匹配 {desc}")
                matched = True
                break
        if not matched:
            print(f"    ✗ 无效格式")
```

### 3. 字符串操作

```python
def string_operations_demo():
    """字符串操作演示"""
    # 1. 字符串替换
    print("1. 字符串替换:")
    text = "今天是2024年1月15日，明天是2024年1月16日，后天是2024年1月17日。"
    print(f"  原文: {text}")
    
    # 简单替换
    result1 = re.sub(r"2024", "2025", text)
    print(f"  替换年份: {result1}")
    
    # 使用分组替换
    result2 = re.sub(r"(\d{4})年(\d{1,2})月(\d{1,2})日", r"\1-\2-\3", text)
    print(f"  格式化日期: {result2}")
    
    # 使用函数替换
    def date_replacer(match):
        year, month, day = match.groups()
        return f"{year}/{month.zfill(2)}/{day.zfill(2)}"
    
    result3 = re.sub(r"(\d{4})年(\d{1,2})月(\d{1,2})日", date_replacer, text)
    print(f"  自定义格式: {result3}")
    
    # 2. 字符串分割
    print("\n2. 字符串分割:")
    data = "apple,banana;orange:grape|watermelon"
    print(f"  原始数据: {data}")
    
    # 按多个分隔符分割
    fruits = re.split(r"[,;:|]", data)
    print(f"  分割结果: {fruits}")
    
    # 保留分隔符
    parts = re.split(r"([,;:|])", data)
    print(f"  保留分隔符: {parts}")
    
    # 3. 文本清理
    print("\n3. 文本清理:")
    messy_text = "  Hello   World!  \n\n  This   is    a   test.  \t\t  "
    print(f"  原始文本: '{messy_text}'")
    
    # 清理多余空白
    cleaned = re.sub(r"\s+", " ", messy_text.strip())
    print(f"  清理后: '{cleaned}'")
    
    # 4. HTML标签清理
    print("\n4. HTML标签清理:")
    html_text = "<p>这是一个<strong>重要</strong>的<em>消息</em>。</p><br><a href='#'>链接</a>"
    print(f"  HTML文本: {html_text}")
    
    # 移除HTML标签
    clean_text = re.sub(r"<[^>]+>", "", html_text)
    print(f"  纯文本: {clean_text}")
```

### 4. 分组和捕获

```python
def grouping_demo():
    """分组和捕获演示"""
    # 1. 基本分组
    print("1. 基本分组:")
    log_line = "2024-01-15 10:30:45 [INFO] User login successful: user123"
    
    log_pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[([A-Z]+)\] (.+)"
    match = re.match(log_pattern, log_line)
    
    if match:
        date, time, level, message = match.groups()
        print(f"  日期: {date}")
        print(f"  时间: {time}")
        print(f"  级别: {level}")
        print(f"  消息: {message}")
    
    # 2. 命名分组
    print("\n2. 命名分组:")
    named_pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) \[(?P<level>[A-Z]+)\] (?P<message>.+)"
    named_match = re.match(named_pattern, log_line)
    
    if named_match:
        print(f"  日期: {named_match.group('date')}")
        print(f"  时间: {named_match.group('time')}")
        print(f"  级别: {named_match.group('level')}")
        print(f"  消息: {named_match.group('message')}")
        print(f"  所有组: {named_match.groupdict()}")
    
    # 3. 非捕获分组
    print("\n3. 非捕获分组:")
    text = "color: red, colour: blue, color: green"
    
    # 使用非捕获分组匹配color或colour
    pattern = r"(?:color|colour): (\w+)"
    matches = re.findall(pattern, text)
    print(f"  颜色值: {matches}")
    
    # 4. 分组引用
    print("\n4. 分组引用:")
    html_tags = "<div>content</div> <span>text</span> <p>paragraph</p>"
    
    # 匹配成对的HTML标签
    tag_pattern = r"<(\w+)>.*?</\1>"
    tags = re.findall(r"<(\w+)>.*?</\1>", html_tags)
    print(f"  匹配的标签: {tags}")
    
    # 提取标签和内容
    content_pattern = r"<(\w+)>(.*?)</\1>"
    tag_contents = re.findall(content_pattern, html_tags)
    print(f"  标签和内容: {tag_contents}")
```

### 5. 编译模式和性能优化

```python
def compiled_patterns_demo():
    """编译模式演示"""
    # 1. 编译正则表达式
    print("1. 编译正则表达式:")
    
    # 编译常用模式
    email_regex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    phone_regex = re.compile(r"1[3-9]\d{9}")
    date_regex = re.compile(r"\d{4}-\d{2}-\d{2}")
    
    test_text = """
    联系方式：
    邮箱：admin@example.com, user@test.org
    电话：13812345678, 13987654321
    日期：2024-01-15, 2024-12-31
    """
    
    # 使用编译后的模式
    emails = email_regex.findall(test_text)
    phones = phone_regex.findall(test_text)
    dates = date_regex.findall(test_text)
    
    print(f"  邮箱: {emails}")
    print(f"  电话: {phones}")
    print(f"  日期: {dates}")
    
    # 2. 模式标志
    print("\n2. 模式标志:")
    
    text_with_case = "Hello WORLD hello world HELLO"
    
    # 忽略大小写
    case_insensitive = re.compile(r"hello", re.IGNORECASE)
    matches = case_insensitive.findall(text_with_case)
    print(f"  忽略大小写匹配: {matches}")
    
    # 多行模式
    multiline_text = """第一行
    第二行开始
    第三行结束"""
    
    # 匹配行首
    line_start = re.compile(r"^第", re.MULTILINE)
    line_matches = line_start.findall(multiline_text)
    print(f"  多行匹配: {len(line_matches)} 个匹配")
    
    # 点号匹配所有字符
    dotall_pattern = re.compile(r"第一行.*第三行", re.DOTALL)
    dotall_match = dotall_pattern.search(multiline_text)
    if dotall_match:
        print(f"  DOTALL匹配: '{dotall_match.group()}'")
```

### 6. 实际应用示例

```python
def practical_applications():
    """实际应用示例"""
    # 1. 日志分析器
    def log_analyzer():
        log_entries = [
            "2024-01-15 10:30:45 [INFO] User login: user123 from 192.168.1.100",
            "2024-01-15 10:31:12 [ERROR] Database connection failed",
            "2024-01-15 10:31:45 [WARNING] High memory usage: 85%",
            "2024-01-15 10:32:00 [INFO] User logout: user123",
            "2024-01-15 10:32:30 [ERROR] File not found: /path/to/file.txt"
        ]
        
        # 日志解析模式
        log_pattern = re.compile(
            r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
            r"\[(?P<level>\w+)\] "
            r"(?P<message>.*)"
        )
        
        # 统计信息
        level_counts = {}
        error_messages = []
        
        for entry in log_entries:
            match = log_pattern.match(entry)
            if match:
                level = match.group('level')
                message = match.group('message')
                
                # 统计日志级别
                level_counts[level] = level_counts.get(level, 0) + 1
                
                # 收集错误消息
                if level == 'ERROR':
                    error_messages.append(message)
        
        print(f"  日志级别统计: {level_counts}")
        print(f"  错误消息: {error_messages}")
    
    # 2. 数据验证器
    class DataValidator:
        def __init__(self):
            self.patterns = {
                'email': re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"),
                'phone': re.compile(r"^1[3-9]\d{9}$"),
                'id_card': re.compile(r"^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dX]$"),
                'password': re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
            }
        
        def validate(self, data_type, value):
            if data_type in self.patterns:
                return bool(self.patterns[data_type].match(value))
            return False
    
    # 3. 文本提取器
    def text_extractor():
        document = """
        联系我们：
        电话：400-123-4567 或 021-12345678
        邮箱：contact@company.com
        网站：https://www.company.com
        地址：上海市浦东新区张江高科技园区
        邮编：201203
        
        价格信息：
        产品A：￥299.99
        产品B：$199.00
        产品C：€159.50
        """
        
        extractors = {
            '电话号码': re.compile(r"\b(?:\d{3,4}-)?\d{7,8}\b|\b400-\d{3}-\d{4}\b"),
            '邮箱地址': re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"),
            '网址': re.compile(r"https?://[\w.-]+\.[a-zA-Z]{2,}(?:/[\w.-]*)*"),
            '价格': re.compile(r"[￥$€]\d+(?:\.\d{2})?"),
            '邮编': re.compile(r"\b\d{6}\b")
        }
        
        for name, pattern in extractors.items():
            matches = pattern.findall(document)
            if matches:
                print(f"  {name}: {matches}")
```

### 7. 高级特性

```python
def advanced_features_demo():
    """高级特性演示"""
    # 1. 前瞻和后顾断言
    print("1. 前瞻和后顾断言:")
    
    text = "password123 username456 email789"
    
    # 正向前瞻：匹配后面跟着数字的单词
    lookahead_pattern = r"\w+(?=\d+)"
    matches = re.findall(lookahead_pattern, text)
    print(f"  前瞻匹配: {matches}")
    
    # 负向前瞻：匹配后面不跟着数字的单词
    negative_lookahead = r"\w+(?!\d+)"
    matches = re.findall(negative_lookahead, text)
    print(f"  负向前瞻: {matches}")
    
    # 2. 贪婪与非贪婪匹配
    print("\n2. 贪婪与非贪婪匹配:")
    
    html = "<div>内容1</div><div>内容2</div>"
    
    # 贪婪匹配
    greedy = re.findall(r"<div>.*</div>", html)
    print(f"  贪婪匹配: {greedy}")
    
    # 非贪婪匹配
    non_greedy = re.findall(r"<div>.*?</div>", html)
    print(f"  非贪婪匹配: {non_greedy}")
    
    # 3. 条件匹配
    print("\n3. 条件匹配示例:")
    
    # 匹配引号内的内容（单引号或双引号）
    quoted_text = '"Hello World" and \'Python Programming\''
    
    # 使用条件匹配
    quote_pattern = r'(["\'])([^"\']*)\1'
    quotes = re.findall(quote_pattern, quoted_text)
    print(f"  引号内容: {[content for quote, content in quotes]}")
```

## 重要知识点

### 1. 正则表达式语法
- **基本字符**: 普通字符直接匹配
- **元字符**: 具有特殊含义的字符
- **字符类**: 匹配一组字符中的任意一个
- **量词**: 指定匹配次数
- **锚点**: 指定匹配位置

### 2. re模块函数特点
- **match()**: 只从字符串开头匹配
- **search()**: 搜索整个字符串的第一个匹配
- **findall()**: 返回所有匹配的列表
- **finditer()**: 返回匹配对象的迭代器
- **sub()**: 替换匹配的内容
- **split()**: 按模式分割字符串

### 3. 分组功能
- **普通分组**: 使用圆括号 `()`
- **命名分组**: 使用 `(?P<name>...)`
- **非捕获分组**: 使用 `(?:...)`
- **分组引用**: 使用 `\1` `\2` 等

### 4. 性能优化
- **编译模式**: 重复使用时提高性能
- **原始字符串**: 避免转义字符问题
- **非贪婪匹配**: 提高匹配效率
- **合理使用锚点**: 减少不必要的搜索

### 5. 常见应用场景
- **数据验证**: 邮箱、手机号、身份证等
- **文本提取**: 从文档中提取特定信息
- **日志分析**: 解析和统计日志文件
- **数据清理**: 清理和格式化文本数据
- **模板处理**: 简单的模板替换

## 运行方式

```bash
# 运行完整示例
python3 07_re_module.py

# 或者在Python解释器中
python3
>>> exec(open('07_re_module.py').read())
```

## 练习建议

1. **基础练习**：
   - 练习基本的正则表达式语法
   - 使用不同的re模块函数
   - 理解贪婪与非贪婪匹配的区别

2. **进阶练习**：
   - 编写复杂的数据验证器
   - 实现文本提取和清理工具
   - 使用前瞻后顾断言解决复杂匹配

3. **实战项目**：
   - 开发日志分析工具
   - 构建网页内容提取器
   - 创建配置文件解析器

## 注意事项

1. **性能考虑**：
   - 复杂正则表达式可能影响性能
   - 重复使用时应编译模式
   - 避免过度使用回溯

2. **可读性**：
   - 复杂模式应添加注释
   - 考虑使用re.VERBOSE标志
   - 将复杂模式分解为简单部分

3. **安全性**：
   - 验证用户输入时要小心
   - 避免正则表达式注入攻击
   - 设置合理的匹配限制

4. **替代方案**：
   - 简单字符串操作可能更高效
   - 复杂解析考虑使用专门的解析器
   - 某些场景下字符串方法更合适

5. **调试技巧**：
   - 使用在线正则表达式测试工具
   - 逐步构建复杂模式
   - 测试边界情况和异常输入