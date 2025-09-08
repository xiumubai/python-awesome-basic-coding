# if-else语句

## 概述

if-else语句是条件控制结构的扩展，它不仅能在条件为真时执行代码，还能在条件为假时执行另一段代码。这种二选一的逻辑结构在编程中非常常见，能够处理更复杂的条件判断场景。

## 基本语法

```python
if condition:
    # 当条件为True时执行的代码
    statement1
else:
    # 当条件为False时执行的代码
    statement2
```

### 语法要点

1. **if部分**：条件为True时执行的代码块
2. **else关键字**：必须与if对应，后面跟冒号
3. **else部分**：条件为False时执行的代码块
4. **缩进一致**：if和else块内的代码必须保持相同的缩进级别
5. **互斥执行**：if和else块中的代码永远不会同时执行

## 基础示例

### 1. 简单的二选一判断

```python
# 年龄判断
age = 16
if age >= 18:
    print("你已经成年了！")
    print("可以投票和独立做决定")
else:
    print("你还未成年")
    print("需要监护人同意")

# 考试结果
score = 55
if score >= 60:
    print("恭喜！你通过了考试")
    print(f"你的分数是：{score}")
else:
    print("很遗憾，你没有通过考试")
    print(f"你的分数是：{score}，还需要努力")

# 天气判断
temperature = 15
if temperature > 20:
    print("天气暖和，适合外出")
    print("可以穿轻薄的衣服")
else:
    print("天气较冷，注意保暖")
    print("建议穿厚一点的衣服")
```

### 2. 用户认证系统

```python
# 用户登录验证
username = "admin"
password = "123456"

input_username = "admin"
input_password = "123456"

if input_username == username and input_password == password:
    print("登录成功！")
    print("欢迎进入系统")
    print("正在加载用户数据...")
else:
    print("登录失败！")
    print("用户名或密码错误")
    print("请重新输入")

# 权限检查
user_role = "guest"
if user_role == "admin":
    print("管理员权限")
    print("可以访问所有功能")
else:
    print("普通用户权限")
    print("只能访问基本功能")
```

### 3. 数值处理

```python
# 正负数判断
number = -5
if number >= 0:
    print(f"{number} 是非负数")
    if number > 0:
        print("这是一个正数")
    else:
        print("这是零")
else:
    print(f"{number} 是负数")
    print(f"它的绝对值是 {abs(number)}")

# 奇偶数判断
num = 7
if num % 2 == 0:
    print(f"{num} 是偶数")
    print("可以被2整除")
else:
    print(f"{num} 是奇数")
    print("不能被2整除")
```

## 嵌套if-else语句

### 1. 多层条件判断

```python
# 学生成绩评定系统
score = 85
attendance = 90  # 出勤率

if score >= 60:
    print("考试及格")
    if attendance >= 80:
        print("出勤率良好")
        if score >= 90:
            print("综合评定：优秀")
        else:
            print("综合评定：良好")
    else:
        print("出勤率不足")
        print("综合评定：需要改进")
else:
    print("考试不及格")
    if attendance >= 80:
        print("虽然出勤率良好，但需要补考")
    else:
        print("出勤率和成绩都需要改进")
```

### 2. 复杂业务逻辑

```python
# 购物折扣系统
total_amount = 150
is_member = True
member_level = "gold"

if total_amount >= 100:
    print("购买金额满100元")
    if is_member:
        print("会员用户，享受折扣")
        if member_level == "gold":
            discount = 0.8  # 8折
            print("金牌会员，8折优惠")
        else:
            discount = 0.9  # 9折
            print("普通会员，9折优惠")
        final_amount = total_amount * discount
        print(f"最终金额：{final_amount}元")
    else:
        print("非会员用户，无折扣")
        print(f"最终金额：{total_amount}元")
else:
    print("购买金额不足100元，无折扣")
    print(f"最终金额：{total_amount}元")
```

## 与布尔值的配合使用

### 1. 直接使用布尔变量

```python
# 系统状态检查
is_online = True
is_authenticated = False
has_permission = True

if is_online:
    print("系统在线")
    if is_authenticated:
        print("用户已认证")
        if has_permission:
            print("权限验证通过，可以访问")
        else:
            print("权限不足，拒绝访问")
    else:
        print("用户未认证，请先登录")
else:
    print("系统离线，无法访问")

# 功能开关
feature_enabled = False
if feature_enabled:
    print("新功能已启用")
    print("正在加载新功能模块...")
else:
    print("新功能未启用")
    print("使用默认功能")
```

### 2. 函数返回值判断

```python
# 文件操作
def file_exists(filename):
    import os
    return os.path.exists(filename)

filename = "data.txt"
if file_exists(filename):
    print(f"文件 {filename} 存在")
    print("开始读取文件内容...")
    # 这里可以添加文件读取代码
else:
    print(f"文件 {filename} 不存在")
    print("创建新文件...")
    # 这里可以添加文件创建代码

# 网络连接检查
def is_connected():
    # 模拟网络连接检查
    import random
    return random.choice([True, False])

if is_connected():
    print("网络连接正常")
    print("可以进行在线操作")
else:
    print("网络连接失败")
    print("切换到离线模式")
```

## 字符串和列表的判断

### 1. 字符串处理

```python
# 字符串内容判断
user_input = "hello world"
if user_input:
    print("用户输入了内容")
    print(f"输入内容：{user_input}")
    if len(user_input) > 10:
        print("输入内容较长")
    else:
        print("输入内容较短")
else:
    print("用户没有输入任何内容")
    print("请输入有效内容")

# 字符串格式验证
email = "user@example.com"
if "@" in email and "." in email:
    print("邮箱格式基本正确")
    if email.count("@") == 1:
        print("邮箱格式验证通过")
    else:
        print("邮箱格式有误：@符号数量不正确")
else:
    print("邮箱格式错误：缺少@或.符号")
```

### 2. 列表和容器判断

```python
# 列表内容检查
shopping_cart = ["apple", "banana", "orange"]
if shopping_cart:
    print("购物车有商品")
    print(f"商品数量：{len(shopping_cart)}")
    print(f"商品列表：{', '.join(shopping_cart)}")
    if len(shopping_cart) >= 5:
        print("商品较多，可以享受批量折扣")
    else:
        print("继续购物可享受更多优惠")
else:
    print("购物车为空")
    print("请添加商品到购物车")

# 字典数据检查
user_profile = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}

if "email" in user_profile:
    print("用户已设置邮箱")
    print(f"邮箱地址：{user_profile['email']}")
else:
    print("用户未设置邮箱")
    print("建议添加邮箱以便接收通知")
```

## 实际应用场景

### 1. 用户界面逻辑

```python
# 按钮状态控制
user_logged_in = True
has_unsaved_changes = False

if user_logged_in:
    print("显示用户菜单")
    print("- 个人资料")
    print("- 设置")
    print("- 退出登录")
    
    if has_unsaved_changes:
        print("警告：有未保存的更改")
        print("显示保存提示")
    else:
        print("所有更改已保存")
else:
    print("显示登录界面")
    print("- 用户名输入框")
    print("- 密码输入框")
    print("- 登录按钮")
```

### 2. 数据处理流程

```python
# 数据验证和处理
def process_user_data(data):
    if data:
        print("开始处理用户数据")
        
        # 检查必要字段
        if "name" in data and "age" in data:
            print("数据格式正确")
            
            # 年龄验证
            if isinstance(data["age"], int) and data["age"] > 0:
                print(f"处理用户：{data['name']}，年龄：{data['age']}")
                return True
            else:
                print("年龄数据无效")
                return False
        else:
            print("缺少必要的数据字段")
            return False
    else:
        print("没有提供数据")
        return False

# 测试数据处理
test_data = {"name": "Bob", "age": 30}
if process_user_data(test_data):
    print("数据处理成功")
else:
    print("数据处理失败")
```

### 3. 游戏逻辑

```python
# 简单的猜数字游戏
import random

secret_number = random.randint(1, 10)
user_guess = 7

print(f"神秘数字是1-10之间的整数")
print(f"你猜测的数字是：{user_guess}")

if user_guess == secret_number:
    print("🎉 恭喜你！猜对了！")
    print(f"神秘数字确实是 {secret_number}")
    print("你赢得了游戏！")
else:
    print("😔 很遗憾，猜错了")
    print(f"神秘数字是 {secret_number}")
    if abs(user_guess - secret_number) <= 2:
        print("不过你很接近了！")
    else:
        print("差距还比较大，继续努力！")
```

## 常见模式和最佳实践

### 1. 早期返回模式

```python
# 函数中的早期返回
def validate_password(password):
    if not password:
        print("密码不能为空")
        return False
    
    if len(password) < 8:
        print("密码长度至少8位")
        return False
    
    if password.isdigit():
        print("密码不能全是数字")
        return False
    
    print("密码验证通过")
    return True

# 测试密码验证
test_passwords = ["", "123", "12345678", "password123"]
for pwd in test_passwords:
    print(f"\n测试密码：'{pwd}'")
    if validate_password(pwd):
        print("✅ 密码有效")
    else:
        print("❌ 密码无效")
```

### 2. 状态机模式

```python
# 简单的状态机
class TrafficLight:
    def __init__(self):
        self.state = "red"
    
    def next_state(self):
        if self.state == "red":
            self.state = "green"
            print("🟢 绿灯：可以通行")
        else:
            self.state = "red"
            print("🔴 红灯：停止通行")
    
    def get_action(self):
        if self.state == "red":
            return "停车等待"
        else:
            return "安全通过"

# 使用状态机
traffic_light = TrafficLight()
print(f"当前状态：{traffic_light.state}")
print(f"行动指示：{traffic_light.get_action()}")

traffic_light.next_state()
print(f"当前状态：{traffic_light.state}")
print(f"行动指示：{traffic_light.get_action()}")
```

## 性能优化技巧

### 1. 条件短路

```python
# 利用短路特性优化性能
def expensive_operation():
    print("执行耗时操作...")
    return True

def cheap_check():
    print("执行快速检查...")
    return False

# 将快速检查放在前面
if cheap_check() and expensive_operation():
    print("两个条件都满足")
else:
    print("至少有一个条件不满足")
```

### 2. 避免重复计算

```python
# 低效的写法
data = [1, 2, 3, 4, 5]
if len(data) > 0:
    print("数据不为空")
    if len(data) > 3:
        print("数据量充足")

# 高效的写法
data = [1, 2, 3, 4, 5]
data_length = len(data)
if data_length > 0:
    print("数据不为空")
    if data_length > 3:
        print("数据量充足")
```

## 常见错误和调试

### 1. 缩进错误

```python
# 错误示例
age = 20
if age >= 18:
    print("成年了")
else:
print("未成年")  # 缺少缩进

# 正确示例
age = 20
if age >= 18:
    print("成年了")
else:
    print("未成年")  # 正确的缩进
```

### 2. 逻辑错误

```python
# 可能的逻辑错误
score = 75
if score > 80:
    print("优秀")
else:
    print("不优秀")  # 这样分类太粗糙

# 更好的逻辑
score = 75
if score >= 90:
    print("优秀")
else:
    if score >= 80:
        print("良好")
    else:
        if score >= 70:
            print("中等")
        else:
            print("需要努力")
```

## 练习题

### 基础练习

1. **温度转换器**：
   - 输入摄氏度，如果大于等于0，转换为华氏度
   - 否则提示温度过低

2. **简单计算器**：
   - 输入两个数字和运算符
   - 如果是除法，检查除数是否为0
   - 否则正常计算

3. **用户年龄验证**：
   - 如果年龄在18-65之间，显示"工作年龄"
   - 否则显示相应的年龄段信息

### 进阶练习

1. **银行ATM模拟**：
   - 检查账户余额
   - 如果余额足够，允许取款
   - 否则显示余额不足

2. **学生成绩管理**：
   - 输入多科成绩
   - 如果平均分及格，计算等级
   - 否则显示需要补考的科目

3. **简单的聊天机器人**：
   - 根据用户输入的关键词
   - 给出不同的回复

## 学习要点

1. **二选一逻辑**：理解if-else的互斥执行特性
2. **嵌套结构**：掌握多层条件判断的写法
3. **代码组织**：学会合理组织条件判断代码
4. **性能考虑**：了解条件判断的性能优化方法
5. **错误处理**：学会在条件判断中处理异常情况

通过掌握if-else语句，你可以处理更复杂的条件逻辑。接下来学习elif语句，可以处理多分支的条件判断。