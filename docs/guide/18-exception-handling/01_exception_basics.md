# 01. 异常基础概念

## 学习目标

- 理解什么是异常以及异常在程序中的作用
- 掌握Python内置异常的层次结构
- 了解常见异常类型及其触发条件
- 学会基本的异常处理语法

## 什么是异常？

异常（Exception）是程序执行过程中发生的错误或异常情况。当Python解释器遇到无法处理的情况时，会抛出异常。如果异常没有被适当处理，程序就会终止执行。

### 异常 vs 语法错误

- **语法错误**：代码不符合Python语法规则，在解析阶段就被发现
- **异常**：语法正确但在运行时出现的错误

## Python异常层次结构

Python的异常都继承自`BaseException`类，形成了一个层次结构：

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      |    +-- OverflowError
      |    +-- FloatingPointError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- ValueError
      +-- TypeError
      +-- AttributeError
      +-- NameError
      +-- IOError
      +-- OSError
      +-- RuntimeError
      +-- ...
```

## 常见异常类型演示

### 1. 算术异常 (ArithmeticError)

```python
# ZeroDivisionError - 除零错误
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零！")

# OverflowError - 数值溢出（在某些情况下）
import math
try:
    result = math.exp(1000)  # 可能导致溢出
except OverflowError:
    print("数值溢出！")
```

### 2. 查找异常 (LookupError)

```python
# IndexError - 索引超出范围
my_list = [1, 2, 3]
try:
    value = my_list[10]
except IndexError:
    print("列表索引超出范围！")

# KeyError - 字典键不存在
my_dict = {'a': 1, 'b': 2}
try:
    value = my_dict['c']
except KeyError:
    print("字典中不存在该键！")
```

### 3. 类型和值异常

```python
# TypeError - 类型错误
try:
    result = "hello" + 5
except TypeError:
    print("不能将字符串和数字相加！")

# ValueError - 值错误
try:
    number = int("hello")
except ValueError:
    print("无法将字符串转换为整数！")
```

### 4. 属性和名称异常

```python
# AttributeError - 属性错误
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
try:
    age = person.age  # Person类没有age属性
except AttributeError:
    print("对象没有该属性！")

# NameError - 名称错误
try:
    print(undefined_variable)  # 变量未定义
except NameError:
    print("变量未定义！")
```

### 5. 文件和系统异常

```python
# FileNotFoundError - 文件未找到
try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在！")

# PermissionError - 权限错误
try:
    with open("/root/protected_file.txt", "w") as f:
        f.write("test")
except PermissionError:
    print("没有权限访问该文件！")
```

## 基本异常处理语法

### 1. 简单的try-except

```python
try:
    # 可能出现异常的代码
    risky_operation()
except ExceptionType:
    # 处理异常的代码
    handle_exception()
```

### 2. 捕获异常对象

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"捕获到异常: {e}")
    print(f"异常类型: {type(e).__name__}")
```

### 3. 捕获多种异常

```python
try:
    # 可能出现多种异常的代码
    user_input = input("请输入一个数字: ")
    number = int(user_input)
    result = 10 / number
except ValueError:
    print("输入的不是有效数字！")
except ZeroDivisionError:
    print("不能除以零！")
```

## 异常信息的获取

### 1. 异常消息

```python
try:
    int("abc")
except ValueError as e:
    print(f"异常消息: {str(e)}")
    print(f"异常表示: {repr(e)}")
```

### 2. 异常类型信息

```python
try:
    [][0]  # IndexError
except Exception as e:
    print(f"异常类型: {type(e).__name__}")
    print(f"异常模块: {type(e).__module__}")
    print(f"异常基类: {type(e).__bases__}")
```

### 3. 异常回溯信息

```python
import traceback

try:
    def func_a():
        func_b()
    
    def func_b():
        func_c()
    
    def func_c():
        raise ValueError("这是一个测试异常")
    
    func_a()
except ValueError as e:
    print("异常回溯信息:")
    traceback.print_exc()
```

## 异常处理的基本原则

### 1. 具体异常优于通用异常

```python
# 好的做法
try:
    value = my_dict[key]
except KeyError:
    print("键不存在")

# 不推荐的做法
try:
    value = my_dict[key]
except Exception:
    print("出现了某种错误")
```

### 2. 不要忽略异常

```python
# 不好的做法
try:
    risky_operation()
except Exception:
    pass  # 静默忽略所有异常

# 好的做法
try:
    risky_operation()
except SpecificException as e:
    logger.error(f"操作失败: {e}")
    # 进行适当的错误处理
```

### 3. 异常处理要有意义

```python
# 有意义的异常处理
try:
    user_age = int(input("请输入年龄: "))
except ValueError:
    print("请输入有效的数字")
    user_age = 0  # 提供默认值或重新获取输入
```

## 实际应用示例

### 安全的用户输入处理

```python
def get_positive_integer(prompt):
    """安全地获取正整数输入"""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("请输入正整数")
                continue
            return value
        except ValueError:
            print("请输入有效的数字")
        except KeyboardInterrupt:
            print("\n用户取消输入")
            return None

# 使用示例
age = get_positive_integer("请输入您的年龄: ")
if age:
    print(f"您的年龄是: {age}")
```

### 安全的文件操作

```python
def safe_read_file(filename):
    """安全地读取文件内容"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
        return None
    except PermissionError:
        print(f"没有权限读取文件 {filename}")
        return None
    except UnicodeDecodeError:
        print(f"文件 {filename} 编码格式不正确")
        return None
    except Exception as e:
        print(f"读取文件时发生未知错误: {e}")
        return None

# 使用示例
content = safe_read_file("example.txt")
if content:
    print("文件内容:", content[:100])  # 显示前100个字符
```

## 学习要点总结

### 核心概念
1. **异常是程序运行时的错误**，不同于语法错误
2. **Python异常有层次结构**，都继承自BaseException
3. **常见异常类型**包括算术、查找、类型、属性等错误
4. **异常对象包含丰富信息**，包括消息、类型、回溯等

### 最佳实践
1. **捕获具体异常**而不是通用Exception
2. **不要忽略异常**，要进行适当处理
3. **异常处理要有意义**，提供有用的错误信息
4. **使用异常信息**进行调试和问题定位

### 注意事项
- 异常处理有性能开销，不要滥用
- 异常应该用于异常情况，不是正常流程控制
- 在捕获异常时要考虑程序的健壮性
- 记录异常信息有助于后续调试

## 下一步学习

掌握了异常基础概念后，接下来将学习：
- [02. try-except语法](./02_try_except.md) - 深入学习异常捕获语法
- [03. 多异常处理](./03_multiple_except.md) - 处理多种异常的技巧
- [04. else和finally子句](./04_else_finally.md) - 完整的异常处理结构

通过理解异常的本质和基本处理方法，你已经为编写更健壮的Python程序打下了坚实基础。