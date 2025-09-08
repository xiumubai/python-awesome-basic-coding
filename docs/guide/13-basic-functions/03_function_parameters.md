# 函数参数详解

本节详细介绍Python函数参数的各种用法，包括位置参数、关键字参数、参数传递方式和最佳实践。

## 学习目标

- 掌握位置参数和关键字参数的使用
- 理解参数传递的顺序规则
- 学会混合使用不同类型的参数
- 了解参数验证的重要性
- 掌握函数参数设计的最佳实践

## 1. 位置参数（Positional Arguments）

位置参数是最基本的参数类型，必须按照定义的顺序传递：

```python
def introduce_person(name, age, city):
    """使用位置参数的函数"""
    print(f"姓名：{name}，年龄：{age}，城市：{city}")

# 位置参数必须按顺序传递
introduce_person("张三", 25, "北京")  # 输出：姓名：张三，年龄：25，城市：北京
introduce_person("李四", 30, "上海")  # 输出：姓名：李四，年龄：30，城市：上海
```

**重要提示：** 位置参数的顺序非常重要，传递错误的顺序会导致逻辑错误：

```python
# 正确顺序
introduce_person("王五", 28, "广州")  # 输出：姓名：王五，年龄：28，城市：广州

# 错误顺序（会导致逻辑错误）
# introduce_person(28, "王五", "广州")  # 姓名：28，年龄：王五，城市：广州
```

## 2. 关键字参数（Keyword Arguments）

关键字参数允许通过参数名指定值，顺序可以任意：

```python
def create_profile(name, age, city, job):
    """创建个人档案"""
    print(f"个人档案：")
    print(f"  姓名：{name}")
    print(f"  年龄：{age}")
    print(f"  城市：{city}")
    print(f"  职业：{job}")

# 使用关键字参数，顺序可以任意
create_profile(name="赵六", age=32, city="深圳", job="工程师")
create_profile(job="设计师", city="杭州", name="孙七", age=27)
```

**关键字参数的优势：**
- 代码更清晰易读
- 参数顺序灵活
- 减少传参错误

## 3. 混合使用位置参数和关键字参数

可以同时使用位置参数和关键字参数，但必须遵循顺序规则：

```python
def book_info(title, author, year=2024, publisher="未知出版社"):
    """图书信息函数"""
    print(f"书名：{title}")
    print(f"作者：{author}")
    print(f"出版年份：{year}")
    print(f"出版社：{publisher}")

# 不同的调用方式
book_info("Python编程", "作者A")  # 使用默认值
book_info("数据结构", "作者B", year=2023)  # 部分使用关键字参数
book_info("算法导论", "作者C", publisher="清华出版社", year=2022)  # 关键字参数顺序任意
```

## 4. 参数传递的详细示例

以下是一个更复杂的参数传递示例：

```python
def calculate_rectangle(length, width, unit="米"):
    """计算矩形面积和周长"""
    area = length * width
    perimeter = 2 * (length + width)
    print(f"矩形尺寸：{length}{unit} × {width}{unit}")
    print(f"面积：{area} 平方{unit}")
    print(f"周长：{perimeter} {unit}")

# 不同的调用方式
calculate_rectangle(5, 3)  # 全部位置参数
calculate_rectangle(5, 3, "厘米")  # 全部位置参数
calculate_rectangle(length=4, width=6)  # 全部关键字参数
calculate_rectangle(4, width=6, unit="英尺")  # 混合参数
```

## 5. 参数顺序规则

在混合使用参数时，必须遵循以下顺序规则：

```python
def order_demo(pos1, pos2, key1="default1", key2="default2"):
    """演示参数顺序规则"""
    print(f"位置参数1：{pos1}")
    print(f"位置参数2：{pos2}")
    print(f"关键字参数1：{key1}")
    print(f"关键字参数2：{key2}")

# 正确的调用方式
order_demo("A", "B")  # 只传位置参数
order_demo("A", "B", "C")  # 位置参数 + 一个关键字参数
order_demo("A", "B", key2="D")  # 位置参数 + 指定关键字参数
order_demo("A", "B", key1="C", key2="D")  # 位置参数 + 所有关键字参数

# 错误的调用方式
# order_demo(pos1="A", "B")  # 错误：关键字参数后不能有位置参数
```

**重要规则：**
1. 位置参数必须在关键字参数之前
2. 同一个参数不能同时用位置和关键字方式传递
3. 关键字参数之间的顺序可以任意

## 6. 实际应用示例

以下是一个实际的邮件发送函数示例：

```python
def send_email(to, subject, body, cc=None, bcc=None, priority="normal"):
    """发送邮件函数"""
    print(f"发送邮件：")
    print(f"  收件人：{to}")
    print(f"  主题：{subject}")
    print(f"  正文：{body}")
    if cc:
        print(f"  抄送：{cc}")
    if bcc:
        print(f"  密送：{bcc}")
    print(f"  优先级：{priority}")

# 不同的使用场景
send_email("user@example.com", "会议通知", "明天下午2点开会")
send_email("user@example.com", "紧急通知", "系统维护", priority="high")
send_email(
    to="user@example.com",
    subject="项目更新",
    body="项目进度报告",
    cc="manager@example.com",
    priority="normal"
)
```

## 7. 参数验证

在函数中进行参数验证是一个好习惯：

```python
def create_user(username, email, age, active=True):
    """创建用户，包含参数验证"""
    # 参数验证
    if not username or len(username) < 3:
        print("错误：用户名至少需要3个字符")
        return
    
    if "@" not in email:
        print("错误：邮箱格式不正确")
        return
    
    if age < 0 or age > 150:
        print("错误：年龄必须在0-150之间")
        return
    
    # 创建用户
    print(f"用户创建成功：")
    print(f"  用户名：{username}")
    print(f"  邮箱：{email}")
    print(f"  年龄：{age}")
    print(f"  状态：{'激活' if active else '未激活'}")

# 测试用户创建
create_user("alice", "alice@example.com", 25)
create_user("bob", "bob@example.com", 30, active=False)
create_user("x", "invalid-email", -5)  # 这会触发验证错误
```

## 8. 函数参数的最佳实践

以下是设计函数参数的最佳实践：

```python
def good_function_example(required_param, optional_param="default", flag=False):
    """良好的函数参数设计示例"""
    result = f"必需参数：{required_param}"
    if optional_param != "default":
        result += f"，可选参数：{optional_param}"
    if flag:
        result += "，标志已启用"
    return result

# 使用示例
print(good_function_example("重要数据"))
print(good_function_example("重要数据", "额外信息"))
print(good_function_example("重要数据", flag=True))
print(good_function_example("重要数据", "额外信息", True))
```

## 运行示例

你可以运行以下代码来测试函数参数：

```bash
python3 02_function_parameters.py
```

## 关键知识点总结

1. **位置参数**：按顺序传递，顺序不能错
2. **关键字参数**：通过参数名传递，顺序灵活
3. **参数顺序**：位置参数必须在关键字参数之前
4. **默认值**：可以为参数设置默认值
5. **参数验证**：在函数内部验证参数的有效性
6. **清晰命名**：参数名应该清晰地表达其用途

## 最佳实践建议

1. **必需参数在前**：将必需的参数放在前面
2. **合理默认值**：为可选参数设置合理的默认值
3. **参数验证**：对重要参数进行验证
4. **清晰命名**：使用描述性的参数名
5. **文档说明**：在文档字符串中说明参数的用途
6. **避免过多参数**：如果参数太多，考虑使用字典或类

## 练习建议

1. 编写一个计算学生成绩的函数，包含必需和可选参数
2. 创建一个配置系统设置的函数，使用关键字参数
3. 实现一个数据处理函数，包含参数验证
4. 练习混合使用位置参数和关键字参数

掌握函数参数的使用是编写灵活、可维护代码的关键技能。