# 局部和全局作用域详解

本节详细介绍Python函数中的作用域概念，包括局部作用域、全局作用域、变量遮蔽、global和nonlocal关键字的使用。

## 学习目标

- 理解局部作用域和全局作用域的概念
- 掌握变量遮蔽的机制
- 学会使用global和nonlocal关键字
- 理解LEGB作用域查找规则
- 掌握作用域的最佳实践
- 避免常见的作用域陷阱

## 1. 全局变量和局部变量

作用域决定了变量在程序中的可见性和生命周期：

```python
# 全局变量
global_var = "我是全局变量"
counter = 0

def demo_scope():
    """演示作用域基本概念"""
    # 局部变量
    local_var = "我是局部变量"
    
    print(f"函数内部访问全局变量：{global_var}")
    print(f"函数内部访问局部变量：{local_var}")
    
    # 可以读取全局变量，但不能直接修改
    print(f"函数内部读取全局counter：{counter}")

# 调用函数
demo_scope()
print(f"函数外部访问全局变量：{global_var}")
# print(local_var)  # 错误：局部变量在函数外部不可访问
```

**重要概念：**
- **全局变量**：在函数外部定义，整个程序中都可访问
- **局部变量**：在函数内部定义，只在函数内部可访问
- **生命周期**：局部变量在函数执行完毕后被销毁

## 2. 局部变量遮蔽全局变量

当局部变量与全局变量同名时，局部变量会遮蔽全局变量：

```python
name = "全局的张三"

def show_name():
    """局部变量遮蔽全局变量"""
    name = "局部的李四"  # 局部变量遮蔽全局变量
    print(f"函数内部的name：{name}")

def show_global_name():
    """访问全局变量"""
    print(f"函数内部访问全局name：{name}")

# 演示变量遮蔽
print(f"全局name：{name}")           # 输出：全局的张三
show_name()                        # 输出：局部的李四
show_global_name()                 # 输出：全局的张三
print(f"函数调用后全局name：{name}") # 输出：全局的张三
```

**遮蔽规则：**
- 局部变量优先级高于全局变量
- 函数内部的赋值创建局部变量
- 全局变量不会被局部变量修改

## 3. 使用global关键字

使用`global`关键字可以在函数内部修改全局变量：

```python
total = 0

def add_to_total(value):
    """使用global关键字修改全局变量"""
    global total
    total += value
    print(f"函数内部：total = {total}")

def reset_total():
    """重置全局变量"""
    global total
    total = 0
    print("total已重置为0")

# 使用global关键字
print(f"初始total：{total}")      # 输出：0
add_to_total(10)                 # 输出：函数内部：total = 10
print(f"函数调用后total：{total}") # 输出：10
add_to_total(20)                 # 输出：函数内部：total = 30
reset_total()                    # 输出：total已重置为0
```

**global关键字的作用：**
- 声明要修改的全局变量
- 必须在使用变量之前声明
- 可以同时声明多个变量：`global var1, var2`

## 4. 嵌套函数和nonlocal关键字

在嵌套函数中，内层函数可以访问外层函数的变量：

```python
def outer_function():
    """外层函数"""
    outer_var = "外层变量"
    
    def inner_function():
        """内层函数"""
        inner_var = "内层变量"
        print(f"内层函数访问外层变量：{outer_var}")
        print(f"内层函数访问内层变量：{inner_var}")
    
    print(f"外层函数的变量：{outer_var}")
    inner_function()
    # print(inner_var)  # 错误：外层函数不能访问内层变量

def counter_function():
    """使用nonlocal的计数器函数"""
    count = 0
    
    def increment():
        nonlocal count  # 声明要修改外层函数的变量
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def get_count():
        return count
    
    return increment, decrement, get_count

# 使用嵌套函数
outer_function()

# 使用nonlocal关键字
inc, dec, get = counter_function()
print(f"初始计数：{get()}")    # 输出：0
print(f"递增后：{inc()}")      # 输出：1
print(f"再次递增：{inc()}")    # 输出：2
print(f"递减后：{dec()}")      # 输出：1
```

**nonlocal关键字的作用：**
- 修改外层函数（非全局）的变量
- 用于闭包中修改外层变量
- 创建有状态的函数

## 5. LEGB规则详解

Python使用LEGB规则查找变量：**L**ocal → **E**nclosing → **G**lobal → **B**uilt-in

```python
# Built-in scope（内置作用域）
# len, print, str等都是内置函数

# Global scope（全局作用域）
x = "全局x"

def legb_demo():
    """演示LEGB查找规则"""
    # Enclosing scope（外层作用域）
    x = "外层x"
    
    def inner():
        # Local scope（局部作用域）
        x = "局部x"
        print(f"内层函数中的x：{x}")  # 找到局部x
        
        # 访问不同作用域的变量
        print(f"使用len函数（内置）：{len('hello')}")
    
    def inner_no_local():
        print(f"内层函数（无局部x）：{x}")  # 找到外层x
    
    print(f"外层函数中的x：{x}")
    inner()
    inner_no_local()

# 演示LEGB规则
print(f"全局作用域的x：{x}")  # 输出：全局x
legb_demo()
# 输出：
# 外层函数中的x：外层x
# 内层函数中的x：局部x
# 使用len函数（内置）：5
# 内层函数（无局部x）：外层x
```

**LEGB查找顺序：**
1. **Local**：当前函数的局部作用域
2. **Enclosing**：外层函数的作用域
3. **Global**：全局作用域
4. **Built-in**：内置作用域

## 6. 作用域陷阱和注意事项

了解常见的作用域陷阱可以避免编程错误：

```python
def scope_trap_demo():
    """演示常见的作用域陷阱"""
    
    # 陷阱1：在赋值前访问全局变量
    global_num = 100
    
    def trap1():
        print(f"访问全局变量：{global_num}")
        # global_num = 200  # 如果取消注释，上面的print会报错
        # UnboundLocalError: local variable referenced before assignment
    
    trap1()
    
    # 陷阱2：循环中的闭包
    functions = []
    for i in range(3):
        # 错误的方式：所有函数都会返回2（循环结束时i的值）
        # functions.append(lambda: i)
        
        # 正确的方式：使用默认参数捕获当前值
        functions.append(lambda x=i: x)
    
    print("闭包陷阱演示：")
    for j, func in enumerate(functions):
        print(f"函数{j}返回：{func()}")
        # 输出：函数0返回：0, 函数1返回：1, 函数2返回：2

scope_trap_demo()
```

**常见陷阱：**
- 在函数中先使用后赋值同名全局变量
- 循环中创建闭包时变量绑定问题
- 误解变量的作用域范围

## 7. 实际应用示例

以下是作用域在实际编程中的应用：

```python
# 配置管理示例
config = {
    "debug": False,
    "max_connections": 100,
    "timeout": 30
}

def get_config(key):
    """获取配置值"""
    return config.get(key)

def set_config(key, value):
    """设置配置值"""
    global config
    config[key] = value
    print(f"配置已更新：{key} = {value}")

def create_logger(name):
    """创建日志记录器（闭包示例）"""
    log_level = "INFO"
    
    def log(message, level="INFO"):
        nonlocal log_level
        if level == "DEBUG" and not config.get("debug", False):
            return
        print(f"[{level}] {name}: {message}")
    
    def set_level(level):
        nonlocal log_level
        log_level = level
        print(f"日志级别设置为：{level}")
    
    return log, set_level

# 使用示例
set_config("debug", True)
log, set_level = create_logger("MyApp")
log("应用程序启动")
log("调试信息", "DEBUG")
set_level("ERROR")
log("这是一个错误", "ERROR")
```

## 8. 最佳实践

以下是作用域使用的最佳实践：

```python
# 好的实践：使用类来管理状态，而不是全局变量
class AppState:
    """使用类来管理状态，而不是全局变量"""
    def __init__(self):
        self.user_count = 0
        self.is_running = False
    
    def start(self):
        self.is_running = True
        print("应用程序已启动")
    
    def add_user(self):
        self.user_count += 1
        print(f"用户数量：{self.user_count}")

def create_calculator():
    """使用闭包创建计算器"""
    history = []
    
    def calculate(operation, a, b):
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            result = a / b if b != 0 else "错误：除零"
        else:
            result = "未知操作"
        
        history.append(f"{operation}({a}, {b}) = {result}")
        return result
    
    def get_history():
        return history.copy()
    
    def clear_history():
        history.clear()
        print("历史记录已清空")
    
    return calculate, get_history, clear_history

# 使用类管理状态
app = AppState()
app.start()
app.add_user()

# 使用闭包创建功能
calc, get_hist, clear_hist = create_calculator()
print(f"计算结果：{calc('add', 5, 3)}")
print(f"计算结果：{calc('multiply', 4, 7)}")
print(f"历史记录：{get_hist()}")
clear_hist()
```

## 运行示例

你可以运行以下代码来测试作用域：

```bash
python3 04_local_global_scope.py
```

## 关键知识点总结

1. **局部作用域**：函数内部定义的变量只在函数内可见
2. **全局作用域**：函数外部定义的变量在整个程序中可见
3. **变量遮蔽**：局部变量会遮蔽同名的全局变量
4. **global关键字**：在函数内修改全局变量
5. **nonlocal关键字**：在嵌套函数中修改外层函数的变量
6. **LEGB规则**：Local → Enclosing → Global → Built-in
7. **闭包**：内层函数可以访问外层函数的变量
8. **作用域陷阱**：注意变量绑定和赋值时机

## 最佳实践建议

1. **最小化全局变量**：尽量减少全局变量的使用
2. **使用类管理状态**：用类代替全局变量来管理复杂状态
3. **明确作用域**：清楚地知道变量的作用域范围
4. **避免变量遮蔽**：避免在函数内使用与全局变量同名的局部变量
5. **合理使用闭包**：利用闭包创建有状态的函数
6. **文档说明**：在文档中说明函数对外部变量的依赖

## 练习建议

1. 编写一个使用全局变量的计数器程序
2. 创建嵌套函数，练习nonlocal关键字的使用
3. 实现一个配置管理系统，合理使用作用域
4. 分析和修复作用域相关的bug
5. 使用闭包实现一个简单的状态机

理解作用域是掌握Python函数的关键，它直接影响变量的可见性、生命周期和程序的结构设计。