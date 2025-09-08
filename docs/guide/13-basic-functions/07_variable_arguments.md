# 可变参数详解 (*args 和 **kwargs)

## 学习目标

通过本节学习，你将掌握：
- 理解可变参数的概念和作用
- 掌握 *args 的使用方法
- 掌握 **kwargs 的使用方法
- 了解参数顺序规则
- 学会参数解包技术
- 掌握可变参数在实际项目中的应用
- 了解装饰器中可变参数的使用
- 掌握可变参数的最佳实践

## 1. *args - 可变位置参数

*args 允许函数接收任意数量的位置参数，这些参数会被收集到一个元组中。

```python
def sum_all(*args):
    """计算所有参数的和"""
    print(f"接收到的参数：{args}")
    print(f"参数类型：{type(args)}")
    return sum(args)

# 使用示例
result1 = sum_all(1, 2, 3)
result2 = sum_all(10, 20, 30, 40, 50)
result3 = sum_all()  # 没有参数
```

## 2. **kwargs - 可变关键字参数

**kwargs 允许函数接收任意数量的关键字参数，这些参数会被收集到一个字典中。

```python
def create_profile(**kwargs):
    """创建用户档案"""
    print(f"接收到的关键字参数：{kwargs}")
    print(f"参数类型：{type(kwargs)}")
    
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    
    return profile

# 使用示例
profile1 = create_profile(name="张三", age=30, city="北京")
profile2 = create_profile(name="李四", job="工程师", salary=8000, married=True)
```

## 3. 同时使用 *args 和 **kwargs

可以在同一个函数中同时使用 *args 和 **kwargs，提供最大的灵活性。

```python
def flexible_function(*args, **kwargs):
    """灵活的函数，可以接收任意参数"""
    print(f"位置参数：{args}")
    print(f"关键字参数：{kwargs}")
    
    # 处理位置参数
    if args:
        print(f"位置参数总和：{sum(args)}")
    
    # 处理关键字参数
    if kwargs:
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    
    return {"args": args, "kwargs": kwargs}

# 使用示例
result = flexible_function(1, 2, 3, name="张三", age=30, city="北京")
```

## 4. 参数顺序规则

在函数定义中，参数必须按照特定顺序排列：

```python
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

# 使用示例
result1 = correct_order("位置参数", "自定义默认值", 1, 2, 3, key1="value1", key2="value2")
result2 = with_keyword_only("位置参数", 1, 2, 3, keyword_only="仅关键字", extra="额外")
```

## 5. 参数解包

使用 * 和 ** 可以将序列和字典解包为函数参数。

```python
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
```

## 6. 实际应用示例

### API 请求函数

```python
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
    
    return {"status": "success", "url": url, "method": method}

# 使用示例
api_request("https://api.example.com/users", "GET", 
           headers={"Authorization": "Bearer token"},
           params={"page": 1, "limit": 10})
```

### HTML 元素创建器

```python
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

# 使用示例
div = create_html_element("div", "Hello World", 
                         class_="container", id="main", 
                         style="color: blue;")
print(f"DIV元素：{div}")
```

## 7. 装饰器中的应用

可变参数在装饰器中非常有用，可以让装饰器适用于任何函数。

```python
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

# 使用示例
result = complex_calculation(1, 2, 3, 4, 5, square=True, multiply=2)
```

## 8. 最佳实践

```python
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
```

## 运行示例

```bash
# 运行可变参数示例
python3 06_variable_arguments.py
```

## 关键知识点总结

1. **`*args` 收集位置参数**：将多余的位置参数收集到元组中
2. **`**kwargs` 收集关键字参数**：将多余的关键字参数收集到字典中
3. **参数顺序规则**：位置参数 → 默认参数 → *args → **kwargs
4. **参数解包**：使用 * 和 ** 将序列和字典解包为函数参数
5. **灵活性与验证**：可变参数提供灵活性，但需要适当的参数验证
6. **装饰器应用**：可变参数让装饰器能够适用于任何函数
7. **实际应用**：API函数、配置函数、工厂函数等场景

## 最佳实践建议

1. **明确文档**：清楚说明函数接受哪些参数
2. **参数验证**：验证可变参数的有效性
3. **合理限制**：避免接受过多或无效的参数
4. **类型提示**：使用类型提示提高代码可读性
5. **错误处理**：提供清晰的错误信息
6. **性能考虑**：避免不必要的参数处理开销

## 练习建议

1. 创建一个灵活的日志函数，支持不同级别和格式
2. 实现一个通用的数据验证函数
3. 编写一个配置管理器，支持多种配置源
4. 创建一个装饰器，记录函数调用信息
5. 实现一个简单的模板引擎，支持可变参数