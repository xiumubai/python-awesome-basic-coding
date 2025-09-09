# 全局作用域

全局作用域是Python中最外层的作用域，理解全局作用域对于编写模块化和可维护的代码至关重要。

## 什么是全局作用域

全局作用域（Global Scope）是指在模块级别定义的作用域。在全局作用域中定义的变量可以在模块的任何地方被访问，这些变量被称为全局变量。

## 全局作用域的特点

1. **模块级别**：全局变量在整个模块中都可见
2. **持久性**：全局变量在模块加载后一直存在
3. **共享性**：所有函数都可以访问全局变量
4. **可修改性**：通过global关键字可以修改全局变量

## 代码示例

### 基本全局变量示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全局作用域演示

本文件演示Python中全局作用域的概念和使用方法。
全局作用域是模块级别的作用域，全局变量在整个模块中都可见。
"""

# 这些是全局变量
APP_NAME = "Python作用域学习系统"
VERSION = "1.0.0"
DEBUG_MODE = True
user_count = 0
configuration = {
    "language": "zh-CN",
    "theme": "light",
    "auto_save": True
}

def demonstrate_global_access():
    """
    演示如何访问全局变量
    """
    print("=== 访问全局变量 ===")
    
    # 函数内部可以直接读取全局变量
    print(f"应用名称: {APP_NAME}")
    print(f"版本号: {VERSION}")
    print(f"调试模式: {DEBUG_MODE}")
    print(f"当前用户数: {user_count}")
    
    # 访问全局字典
    print(f"语言设置: {configuration['language']}")
    print(f"主题设置: {configuration['theme']}")

def demonstrate_global_vs_local():
    """
    演示全局变量与局部变量的区别
    """
    print("\n=== 全局变量 vs 局部变量 ===")
    
    # 创建与全局变量同名的局部变量
    APP_NAME = "局部应用名称"  # 这是局部变量，不会影响全局变量
    local_var = "我是局部变量"
    
    print(f"函数内的APP_NAME: {APP_NAME}")
    print(f"局部变量: {local_var}")
    
    # 全局变量仍然可以通过globals()访问
    print(f"通过globals()访问全局APP_NAME: {globals()['APP_NAME']}")

def demonstrate_global_modification_error():
    """
    演示不使用global关键字修改全局变量的错误
    """
    print("\n=== 修改全局变量的错误示例 ===")
    
    def try_modify_without_global():
        try:
            # 尝试修改全局变量（错误做法）
            print(f"修改前的user_count: {user_count}")
            # user_count += 1  # 这会引发UnboundLocalError
        except UnboundLocalError as e:
            print(f"错误: {e}")
            print("不能在没有global声明的情况下修改全局变量")
    
    try_modify_without_global()

def demonstrate_reading_global():
    """
    演示读取全局变量的不同方式
    """
    print("\n=== 读取全局变量的方式 ===")
    
    # 方式1：直接访问（最常用）
    print(f"直接访问: {APP_NAME}")
    
    # 方式2：通过globals()函数
    print(f"通过globals(): {globals()['VERSION']}")
    
    # 方式3：使用getattr访问模块属性
    import sys
    current_module = sys.modules[__name__]
    print(f"通过模块属性: {getattr(current_module, 'DEBUG_MODE')}")
    
    # 显示所有全局变量
    print("\n当前模块的全局变量:")
    for name, value in globals().items():
        if not name.startswith('_') and not callable(value):
            print(f"  {name}: {value}")

def demonstrate_global_collections():
    """
    演示全局集合类型的操作
    """
    print("\n=== 全局集合类型操作 ===")
    
    # 可以修改全局集合的内容（不需要global关键字）
    print(f"修改前的配置: {configuration}")
    
    # 修改字典内容
    configuration["theme"] = "dark"
    configuration["font_size"] = 14
    
    print(f"修改后的配置: {configuration}")
    
    # 但是不能重新赋值整个字典（需要global关键字）
    print("注意：修改集合内容 ≠ 重新赋值集合变量")

def create_global_list():
    """
    演示全局列表的使用
    """
    print("\n=== 全局列表操作 ===")
    
    # 访问和修改全局列表
    print(f"当前日志: {log_messages}")
    
    # 添加新的日志消息
    log_messages.append(f"函数 {create_global_list.__name__} 被调用")
    log_messages.append("全局列表内容被修改")
    
    print(f"更新后的日志: {log_messages}")

def demonstrate_global_constants():
    """
    演示全局常量的使用
    """
    print("\n=== 全局常量使用 ===")
    
    # 使用全局常量进行计算
    if DEBUG_MODE:
        print("调试模式已启用")
        print(f"应用信息: {APP_NAME} v{VERSION}")
    
    # 全局常量用于配置
    max_users = MAX_USERS
    current_users = user_count
    
    print(f"最大用户数: {max_users}")
    print(f"当前用户数: {current_users}")
    print(f"剩余容量: {max_users - current_users}")

def demonstrate_module_level_code():
    """
    演示模块级别代码的执行
    """
    print("\n=== 模块级别代码 ===")
    
    print("这个函数演示模块级别代码的概念")
    print(f"模块初始化时间: {INIT_TIME}")
    print(f"模块名称: {__name__}")
    
    # 显示模块级别定义的所有内容
    module_items = [name for name in globals().keys() if not name.startswith('_')]
    print(f"模块级别定义的项目数量: {len(module_items)}")

def practical_example_config_manager():
    """
    实际应用示例：配置管理器
    """
    print("\n=== 实际应用：配置管理器 ===")
    
    def get_config(key, default=None):
        """获取配置值"""
        return configuration.get(key, default)
    
    def update_config(key, value):
        """更新配置值"""
        old_value = configuration.get(key)
        configuration[key] = value
        log_messages.append(f"配置更新: {key} 从 {old_value} 改为 {value}")
    
    def get_app_info():
        """获取应用信息"""
        return {
            "name": APP_NAME,
            "version": VERSION,
            "debug": DEBUG_MODE,
            "users": user_count
        }
    
    # 使用配置管理器
    print(f"当前主题: {get_config('theme')}")
    update_config('theme', 'blue')
    print(f"更新后主题: {get_config('theme')}")
    
    app_info = get_app_info()
    print(f"应用信息: {app_info}")

def demonstrate_global_scope_benefits():
    """
    演示全局作用域的优势
    """
    print("\n=== 全局作用域的优势 ===")
    
    # 1. 配置共享
    def feature_a():
        if configuration.get('auto_save', False):
            return "功能A：自动保存已启用"
        return "功能A：自动保存已禁用"
    
    def feature_b():
        theme = configuration.get('theme', 'light')
        return f"功能B：使用{theme}主题"
    
    # 2. 状态共享
    def increment_users():
        global user_count
        user_count += 1
        return f"用户数增加到: {user_count}"
    
    def get_user_status():
        if user_count >= MAX_USERS:
            return "用户已满"
        return f"还可以接受 {MAX_USERS - user_count} 个用户"
    
    # 测试功能
    print(feature_a())
    print(feature_b())
    print(increment_users())
    print(get_user_status())

def demonstrate_global_scope_pitfalls():
    """
    演示全局作用域的潜在问题
    """
    print("\n=== 全局作用域的潜在问题 ===")
    
    # 问题1：意外的变量覆盖
    def problematic_function():
        # 创建了与全局变量同名的局部变量
        DEBUG_MODE = False  # 这不会影响全局变量
        print(f"函数内DEBUG_MODE: {DEBUG_MODE}")
        print(f"全局DEBUG_MODE: {globals()['DEBUG_MODE']}")
    
    # 问题2：全局状态的意外修改
    def another_problematic_function():
        # 修改全局集合可能产生副作用
        configuration.clear()  # 危险操作！
        print("配置被清空了！")
    
    problematic_function()
    
    # 备份配置以防被清空
    config_backup = configuration.copy()
    another_problematic_function()
    
    # 恢复配置
    configuration.update(config_backup)
    print(f"配置已恢复: {configuration}")

def best_practices():
    """
    全局作用域的最佳实践
    """
    print("\n=== 全局作用域最佳实践 ===")
    
    # 1. 使用常量命名约定
    print(f"常量示例: {MAX_USERS}, {APP_NAME}")
    
    # 2. 最小化全局变量的使用
    def get_system_info():
        """返回系统信息而不是使用全局变量"""
        return {
            "app_name": APP_NAME,
            "version": VERSION,
            "debug_mode": DEBUG_MODE
        }
    
    # 3. 使用函数封装全局状态访问
    def safe_increment_users():
        """安全地增加用户数"""
        global user_count
        if user_count < MAX_USERS:
            user_count += 1
            return True, f"用户数: {user_count}"
        return False, "已达到最大用户数"
    
    # 4. 提供清晰的接口
    def reset_system():
        """重置系统状态"""
        global user_count
        user_count = 0
        configuration.update({
            "language": "zh-CN",
            "theme": "light",
            "auto_save": True
        })
        log_messages.clear()
        log_messages.append("系统已重置")
    
    # 测试最佳实践
    info = get_system_info()
    print(f"系统信息: {info}")
    
    success, message = safe_increment_users()
    print(f"增加用户: {success}, {message}")

# 更多全局变量定义
MAX_USERS = 100
log_messages = ["系统启动"]

# 模块初始化代码
import datetime
INIT_TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 模块级别的初始化
if DEBUG_MODE:
    log_messages.append(f"调试模式启用于 {INIT_TIME}")

def main():
    """
    主函数：演示所有全局作用域概念
    """
    print("Python 全局作用域详解")
    print("=" * 50)
    
    # 演示各种全局作用域概念
    demonstrate_global_access()
    demonstrate_global_vs_local()
    demonstrate_global_modification_error()
    demonstrate_reading_global()
    demonstrate_global_collections()
    create_global_list()
    demonstrate_global_constants()
    demonstrate_module_level_code()
    practical_example_config_manager()
    demonstrate_global_scope_benefits()
    demonstrate_global_scope_pitfalls()
    best_practices()
    
    print("\n=== 总结 ===")
    print("1. 全局变量在整个模块中都可见")
    print("2. 函数可以读取全局变量，但修改需要global关键字")
    print("3. 全局集合的内容可以直接修改")
    print("4. 合理使用全局变量可以实现配置和状态共享")
    print("5. 避免过度使用全局变量，保持代码的可维护性")
    
    # 显示最终的全局状态
    print("\n=== 最终全局状态 ===")
    print(f"用户数: {user_count}")
    print(f"配置: {configuration}")
    print(f"日志条数: {len(log_messages)}")

if __name__ == "__main__":
    main()
```

## 学习要点

### 核心概念
1. **全局变量定义**：在模块级别定义的变量
2. **作用域范围**：整个模块内都可访问
3. **生命周期**：从模块加载到程序结束
4. **访问方式**：函数内可直接读取，修改需要global关键字

### 重要特性
1. **可见性**：在模块的任何地方都可见
2. **持久性**：在程序运行期间一直存在
3. **共享性**：所有函数都可以访问
4. **修改限制**：需要global关键字才能修改

### 实际应用
1. **配置管理**：存储应用程序配置
2. **状态共享**：在函数间共享状态
3. **常量定义**：定义程序常量
4. **缓存数据**：存储计算结果或临时数据

### 最佳实践
1. **命名约定**：常量使用大写字母
2. **最小化使用**：避免过度依赖全局变量
3. **封装访问**：通过函数访问全局状态
4. **文档说明**：清楚说明全局变量的用途

## 运行示例

在15-function-scope目录下运行：

```bash
python3 02_global_scope.py
```

## 注意事项

1. **修改限制**：修改全局变量需要global关键字
2. **命名冲突**：避免局部变量与全局变量同名
3. **副作用**：修改全局状态可能产生意外副作用
4. **测试困难**：全局状态使单元测试变得复杂

## 下一步学习

掌握全局作用域后，建议继续学习：
- [global关键字](04_global_keyword.md)
- [nonlocal关键字](05_nonlocal_keyword.md)
- [作用域解析规则](08_scope_resolution.md)