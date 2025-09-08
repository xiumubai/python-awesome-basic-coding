#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
可变参数详解（*args和**kwargs）

本文件演示Python函数的可变参数，包括：
1. *args（可变位置参数）
2. **kwargs（可变关键字参数）
3. 参数顺序规则
4. 参数解包
5. 实际应用示例
6. 最佳实践

作者：Python学习教程
日期：2024年
"""

print("=" * 50)
print("Python 可变参数详解（*args和**kwargs）")
print("=" * 50)

# 1. *args - 可变位置参数
print("\n1. *args - 可变位置参数")
print("-" * 30)

def sum_all(*args):
    """计算所有参数的和"""
    print(f"接收到的参数：{args}")
    print(f"参数类型：{type(args)}")
    return sum(args)

def print_info(name, *subjects):
    """打印学生信息和科目"""
    print(f"学生姓名：{name}")
    print(f"学习科目：{subjects}")
    if subjects:
        print(f"科目数量：{len(subjects)}")
        for i, subject in enumerate(subjects, 1):
            print(f"  {i}. {subject}")
    else:
        print("没有学习科目")

def find_max(*numbers):
    """找出最大值"""
    if not numbers:
        return None
    return max(numbers)

print("*args基本用法：")
result1 = sum_all(1, 2, 3, 4, 5)
print(f"求和结果：{result1}")

result2 = sum_all(10, 20)
print(f"求和结果：{result2}")

result3 = sum_all()  # 没有参数
print(f"无参数求和：{result3}")

print("\n学生信息示例：")
print_info("张三")
print_info("李四", "数学", "物理", "化学")
print_info("王五", "语文")

print(f"\n最大值示例：")
print(f"最大值：{find_max(3, 7, 2, 9, 1)}")
print(f"空参数最大值：{find_max()}")
print()

# 2. **kwargs - 可变关键字参数
print("\n2. **kwargs - 可变关键字参数")
print("-" * 30)

def create_profile(name, age, **kwargs):
    """创建用户档案"""
    profile = {
        "name": name,
        "age": age
    }
    
    print(f"额外信息：{kwargs}")
    print(f"kwargs类型：{type(kwargs)}")
    
    # 将额外信息添加到档案中
    profile.update(kwargs)
    return profile

def configure_database(**config):
    """配置数据库连接"""
    default_config = {
        "host": "localhost",
        "port": 5432,
        "database": "mydb",
        "timeout": 30
    }
    
    print("默认配置：")
    for key, value in default_config.items():
        print(f"  {key}: {value}")
    
    print("\n用户配置：")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    # 合并配置
    final_config = {**default_config, **config}
    return final_config

def print_kwargs(**kwargs):
    """打印所有关键字参数"""
    if not kwargs:
        print("没有接收到关键字参数")
        return
    
    print("接收到的关键字参数：")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

print("**kwargs基本用法：")
profile1 = create_profile("张三", 25)
print(f"档案1：{profile1}")

profile2 = create_profile("李四", 30, city="北京", job="工程师", hobby="编程")
print(f"档案2：{profile2}")

print("\n数据库配置示例：")
db_config = configure_database(host="192.168.1.100", database="production")
print("\n最终配置：")
for key, value in db_config.items():
    print(f"  {key}: {value}")

print("\nkwargs演示：")
print_kwargs()
print_kwargs(a=1, b=2, c="hello")
print()

# 3. 同时使用*args和**kwargs
print("\n3. 同时使用*args和**kwargs")
print("-" * 30)

def flexible_function(required_param, *args, **kwargs):
    """灵活的函数，接受任意参数"""
    print(f"必需参数：{required_param}")
    print(f"位置参数：{args}")
    print(f"关键字参数：{kwargs}")
    
    result = {
        "required": required_param,
        "args_count": len(args),
        "kwargs_count": len(kwargs),
        "all_args": args,
        "all_kwargs": kwargs
    }
    return result

def complete_function(a, b=10, *args, **kwargs):
    """完整的参数示例"""
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")
    
    total = a + b + sum(args)
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            total += value
    
    return total

def logger(level, message, *details, **metadata):
    """日志记录函数"""
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"[{timestamp}] [{level}] {message}")
    
    if details:
        print("详细信息：")
        for i, detail in enumerate(details, 1):
            print(f"  {i}. {detail}")
    
    if metadata:
        print("元数据：")
        for key, value in metadata.items():
            print(f"  {key}: {value}")

print("灵活函数演示：")
result1 = flexible_function("必需值")
print(f"结果1：{result1}")

result2 = flexible_function("必需值", 1, 2, 3, name="张三", age=25)
print(f"结果2：{result2}")

print("\n完整函数演示：")
total1 = complete_function(5)
print(f"总计1：{total1}")

total2 = complete_function(5, 15, 10, 20, bonus=100, extra=50)
print(f"总计2：{total2}")

print("\n日志记录演示：")
logger("INFO", "应用程序启动")
logger("ERROR", "数据库连接失败", "连接超时", "重试3次后失败", 
       host="localhost", port=5432, user="admin")
print()

# 4. 参数顺序规则
print("\n4. 参数顺序规则")
print("-" * 30)

# 正确的参数顺序：位置参数 -> 默认参数 -> *args -> **kwargs
def correct_order(pos_arg, default_arg="default", *args, **kwargs):
    """正确的参数顺序"""
    return {
        "pos_arg": pos_arg,
        "default_arg": default_arg,
        "args": args,
        "kwargs": kwargs
    }

# 带有keyword-only参数的函数
def with_keyword_only(pos_arg, *args, keyword_only, **kwargs):
    """包含仅关键字参数的函数"""
    return {
        "pos_arg": pos_arg,
        "args": args,
        "keyword_only": keyword_only,
        "kwargs": kwargs
    }

print("参数顺序演示：")
result = correct_order("位置参数", "自定义默认值", 1, 2, 3, key1="value1", key2="value2")
print(f"正确顺序结果：{result}")

# keyword-only参数必须使用关键字传递
result2 = with_keyword_only("位置参数", 1, 2, 3, keyword_only="仅关键字", extra="额外")
print(f"仅关键字参数结果：{result2}")
print()

# 5. 参数解包
print("\n5. 参数解包")
print("-" * 30)

def multiply(a, b, c):
    """三个数相乘"""
    return a * b * c

def create_person(name, age, city, job):
    """创建人员信息"""
    return {
        "name": name,
        "age": age,
        "city": city,
        "job": job
    }

def process_data(*args, **kwargs):
    """处理数据并转发给其他函数"""
    print(f"处理数据：args={args}, kwargs={kwargs}")
    # 可以将参数转发给其他函数
    return {"processed_args": args, "processed_kwargs": kwargs}

print("参数解包演示：")
# 解包列表/元组作为位置参数
numbers = [2, 3, 4]
result = multiply(*numbers)
print(f"解包列表：{numbers} -> 结果：{result}")

# 解包字典作为关键字参数
person_data = {
    "name": "张三",
    "age": 30,
    "city": "北京",
    "job": "工程师"
}
person = create_person(**person_data)
print(f"解包字典：{person}")

# 同时解包
args_data = [1, 2, 3]
kwargs_data = {"option1": "value1", "option2": "value2"}
result = process_data(*args_data, **kwargs_data)
print(f"同时解包结果：{result}")
print()

# 6. 实际应用示例
print("\n6. 实际应用示例")
print("-" * 30)

def api_request(url, method="GET", *args, **kwargs):
    """模拟API请求"""
    print(f"API请求：{method} {url}")
    
    # 处理额外的位置参数（可能是路径参数）
    if args:
        full_url = url + "/" + "/".join(str(arg) for arg in args)
        print(f"完整URL：{full_url}")
    
    # 处理关键字参数（请求参数、头部等）
    headers = kwargs.pop("headers", {})
    params = kwargs.pop("params", {})
    data = kwargs.pop("data", None)
    
    if headers:
        print(f"请求头：{headers}")
    if params:
        print(f"查询参数：{params}")
    if data:
        print(f"请求数据：{data}")
    
    # 其他配置选项
    if kwargs:
        print(f"其他选项：{kwargs}")
    
    return {"status": "success", "url": url, "method": method}

def create_html_element(tag, content="", *children, **attributes):
    """创建HTML元素"""
    # 构建属性字符串
    attr_str = ""
    if attributes:
        attr_parts = []
        for key, value in attributes.items():
            # 处理特殊属性名（如class_变为class）
            if key.endswith("_"):
                key = key[:-1]
            attr_parts.append(f'{key}="{value}"')
        attr_str = " " + " ".join(attr_parts)
    
    # 构建开始标签
    start_tag = f"<{tag}{attr_str}>"
    end_tag = f"</{tag}>"
    
    # 构建内容
    full_content = content
    if children:
        full_content += "".join(str(child) for child in children)
    
    return f"{start_tag}{full_content}{end_tag}"

def calculate_statistics(*numbers, **options):
    """计算统计信息"""
    if not numbers:
        return {"error": "没有提供数字"}
    
    # 基本统计
    stats = {
        "count": len(numbers),
        "sum": sum(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "average": sum(numbers) / len(numbers)
    }
    
    # 可选的统计计算
    if options.get("include_median", False):
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        if n % 2 == 0:
            stats["median"] = (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
        else:
            stats["median"] = sorted_nums[n//2]
    
    if options.get("include_variance", False):
        mean = stats["average"]
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        stats["variance"] = variance
        stats["std_dev"] = variance ** 0.5
    
    return stats

print("实际应用示例：")
print("API请求示例：")
api_request("https://api.example.com/users", "GET", 
           headers={"Authorization": "Bearer token"},
           params={"page": 1, "limit": 10})

print("\nAPI请求（带路径参数）：")
api_request("https://api.example.com/users", "POST", "123", "profile",
           data={"name": "张三", "age": 30},
           timeout=30, verify=True)

print("\nHTML元素创建：")
div = create_html_element("div", "Hello World", 
                         class_="container", id="main", 
                         style="color: blue;")
print(f"DIV元素：{div}")

link = create_html_element("a", "点击这里", 
                          href="https://example.com", 
                          target="_blank")
print(f"链接元素：{link}")

print("\n统计计算示例：")
stats1 = calculate_statistics(1, 2, 3, 4, 5)
print(f"基本统计：{stats1}")

stats2 = calculate_statistics(10, 20, 30, 40, 50, 
                            include_median=True, 
                            include_variance=True)
print(f"完整统计：{stats2}")
print()

# 7. 装饰器中的应用
print("\n7. 装饰器中的应用")
print("-" * 30)

def timing_decorator(func):
    """计时装饰器"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间：{end_time - start_time:.4f}秒")
        return result
    
    return wrapper

def log_decorator(func):
    """日志装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用函数：{func.__name__}")
        print(f"位置参数：{args}")
        print(f"关键字参数：{kwargs}")
        result = func(*args, **kwargs)
        print(f"返回结果：{result}")
        return result
    
    return wrapper

@timing_decorator
@log_decorator
def complex_calculation(*numbers, **options):
    """复杂计算函数"""
    import time
    time.sleep(0.1)  # 模拟计算时间
    
    result = sum(numbers)
    if options.get("square", False):
        result = result ** 2
    if options.get("multiply", 1) != 1:
        result *= options["multiply"]
    
    return result

print("装饰器应用示例：")
result = complex_calculation(1, 2, 3, 4, 5, square=True, multiply=2)
print(f"最终结果：{result}")
print()

# 8. 最佳实践
print("\n8. 可变参数最佳实践")
print("-" * 30)

def good_practice_function(required, optional="default", *args, 
                          keyword_only=None, **kwargs):
    """最佳实践示例"""
    # 1. 验证必需参数
    if not required:
        raise ValueError("required参数不能为空")
    
    # 2. 处理可选参数
    if keyword_only is None:
        keyword_only = "默认值"
    
    # 3. 限制args的数量（如果需要）
    if len(args) > 10:
        raise ValueError("位置参数过多")
    
    # 4. 验证kwargs中的键
    allowed_kwargs = {"option1", "option2", "option3"}
    invalid_kwargs = set(kwargs.keys()) - allowed_kwargs
    if invalid_kwargs:
        raise ValueError(f"不支持的关键字参数：{invalid_kwargs}")
    
    # 5. 提供清晰的返回值
    return {
        "required": required,
        "optional": optional,
        "args_count": len(args),
        "keyword_only": keyword_only,
        "valid_kwargs": {k: v for k, v in kwargs.items() if k in allowed_kwargs}
    }

def flexible_constructor(cls_name, *bases, **methods):
    """灵活的类构造器示例"""
    # 动态创建类
    class_dict = {}
    
    # 添加方法
    for method_name, method_func in methods.items():
        class_dict[method_name] = method_func
    
    # 添加默认的__init__方法
    if '__init__' not in class_dict:
        def default_init(self, *args, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)
        class_dict['__init__'] = default_init
    
    # 创建类
    return type(cls_name, bases, class_dict)

print("最佳实践示例：")
try:
    result = good_practice_function("必需值", "可选值", 1, 2, 3,
                                  keyword_only="仅关键字",
                                  option1="值1", option2="值2")
    print(f"成功结果：{result}")
except ValueError as e:
    print(f"错误：{e}")

print("\n动态类创建示例：")
# 创建一个简单的类
def say_hello(self):
    return f"Hello, I'm {getattr(self, 'name', 'Unknown')}"

def get_age(self):
    return getattr(self, 'age', 0)

Person = flexible_constructor("Person", 
                            say_hello=say_hello,
                            get_age=get_age)

person = Person(name="张三", age=30, city="北京")
print(f"问候：{person.say_hello()}")
print(f"年龄：{person.get_age()}")
print(f"城市：{person.city}")

print("\n=" * 50)
print("可变参数学习完成！")
print("=" * 50)
print("\n总结：")
print("1. *args收集额外的位置参数为元组")
print("2. **kwargs收集额外的关键字参数为字典")
print("3. 参数顺序：位置参数 -> 默认参数 -> *args -> **kwargs")
print("4. 使用*和**可以解包参数")
print("5. 可变参数使函数更加灵活")
print("6. 在装饰器中经常使用可变参数")
print("7. 注意验证参数的有效性")
print("8. 合理使用可变参数可以创建强大的API")