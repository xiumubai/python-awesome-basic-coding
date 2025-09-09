# 文件基础操作

## 学习目标
- 掌握文件的基本打开和关闭操作
- 理解open()函数的基本用法
- 了解文件对象的基本属性和方法
- 学会正确管理文件资源

## 核心概念

### 文件对象
在Python中，文件是通过文件对象来操作的。文件对象提供了读写文件的方法和属性。

### open()函数
`open()`函数是Python中打开文件的标准方法，返回一个文件对象。

```python
file_obj = open(filename, mode, encoding='utf-8')
```

## 代码示例

### 基本文件打开和关闭

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def demonstrate_file_opening():
    """演示文件打开的基本方法"""
    print("=== 文件打开演示 ===")
    
    # 创建一个测试文件
    test_file = "test_file.txt"
    
    # 先创建文件并写入一些内容
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("这是一个测试文件\n")
        f.write("用于演示文件操作基础\n")
        f.write("Python文件操作很简单！\n")
    
    print(f"已创建测试文件: {test_file}")
    
    # 方法1：基本的文件打开
    print("\n1. 基本文件打开方式：")
    file_obj = open(test_file, 'r', encoding='utf-8')
    print(f"文件对象: {file_obj}")
    print(f"文件名: {file_obj.name}")
    print(f"文件模式: {file_obj.mode}")
    print(f"文件编码: {file_obj.encoding}")
    print(f"文件是否关闭: {file_obj.closed}")
    
    # 读取文件内容
    content = file_obj.read()
    print(f"文件内容:\n{content}")
    
    # 关闭文件
    file_obj.close()
    print(f"关闭后文件状态: {file_obj.closed}")
    
    # 清理测试文件
    os.remove(test_file)
    print(f"\n已删除测试文件: {test_file}")
```

### 文件对象属性

```python
def demonstrate_file_attributes():
    """演示文件对象的属性"""
    print("\n=== 文件对象属性演示 ===")
    
    test_file = "attributes_test.txt"
    
    # 创建测试文件
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("测试文件属性\n")
    
    # 打开文件并查看属性
    file_obj = open(test_file, 'r', encoding='utf-8')
    
    print("文件对象的重要属性：")
    print(f"name (文件名): {file_obj.name}")
    print(f"mode (打开模式): {file_obj.mode}")
    print(f"encoding (编码): {file_obj.encoding}")
    print(f"closed (是否关闭): {file_obj.closed}")
    print(f"readable() (是否可读): {file_obj.readable()}")
    print(f"writable() (是否可写): {file_obj.writable()}")
    print(f"seekable() (是否可定位): {file_obj.seekable()}")
    
    file_obj.close()
    os.remove(test_file)
```

### 文件操作生命周期

```python
def demonstrate_file_lifecycle():
    """演示文件操作的完整生命周期"""
    print("\n=== 文件操作生命周期演示 ===")
    
    test_file = "lifecycle_test.txt"
    
    print("1. 文件操作的标准流程：")
    print("   步骤1: 打开文件")
    file_obj = open(test_file, 'w', encoding='utf-8')
    print(f"   文件已打开: {file_obj.name}")
    
    print("   步骤2: 操作文件")
    file_obj.write("Hello, File Operations!\n")
    file_obj.write("这是文件操作的演示\n")
    print("   文件内容已写入")
    
    print("   步骤3: 关闭文件")
    file_obj.close()
    print("   文件已关闭")
    
    print("\n2. 验证文件内容：")
    # 重新打开文件读取内容
    file_obj = open(test_file, 'r', encoding='utf-8')
    content = file_obj.read()
    print(f"文件内容:\n{content}")
    file_obj.close()
    
    # 清理
    os.remove(test_file)
    print("测试文件已删除")
```

### 多文件操作

```python
def demonstrate_multiple_files():
    """演示同时操作多个文件"""
    print("\n=== 多文件操作演示 ===")
    
    file1 = "file1.txt"
    file2 = "file2.txt"
    
    # 创建两个文件
    f1 = open(file1, 'w', encoding='utf-8')
    f2 = open(file2, 'w', encoding='utf-8')
    
    print("同时打开两个文件进行写入：")
    f1.write("这是第一个文件\n")
    f2.write("这是第二个文件\n")
    
    print(f"文件1状态: {f1.name} - 关闭状态: {f1.closed}")
    print(f"文件2状态: {f2.name} - 关闭状态: {f2.closed}")
    
    # 关闭文件
    f1.close()
    f2.close()
    
    print("\n文件关闭后状态：")
    print(f"文件1关闭状态: {f1.closed}")
    print(f"文件2关闭状态: {f2.closed}")
    
    # 清理文件
    os.remove(file1)
    os.remove(file2)
    print("测试文件已清理")
```

### 错误处理

```python
def demonstrate_file_errors():
    """演示文件操作中的常见错误"""
    print("\n=== 文件操作错误演示 ===")
    
    print("1. 尝试打开不存在的文件：")
    try:
        file_obj = open("nonexistent_file.txt", 'r')
    except FileNotFoundError as e:
        print(f"   错误: {e}")
    
    print("\n2. 尝试对已关闭的文件进行操作：")
    test_file = "error_test.txt"
    
    # 创建并关闭文件
    file_obj = open(test_file, 'w', encoding='utf-8')
    file_obj.write("测试内容")
    file_obj.close()
    
    # 尝试对已关闭的文件进行操作
    try:
        file_obj.write("尝试写入已关闭的文件")
    except ValueError as e:
        print(f"   错误: {e}")
    
    # 清理
    os.remove(test_file)
```

## 重要知识点

### 1. 文件对象属性
- `name`: 文件名
- `mode`: 打开模式
- `encoding`: 文件编码
- `closed`: 文件是否已关闭
- `readable()`: 是否可读
- `writable()`: 是否可写
- `seekable()`: 是否支持随机访问

### 2. 文件操作流程
1. **打开文件**: 使用`open()`函数
2. **操作文件**: 读取或写入数据
3. **关闭文件**: 调用`close()`方法

### 3. 资源管理的重要性
- 文件操作后必须关闭文件
- 未关闭的文件会占用系统资源
- 可能导致数据丢失或文件锁定

## 最佳实践

1. **总是关闭文件**: 使用完文件后立即关闭
2. **使用异常处理**: 处理文件不存在等错误
3. **指定编码**: 明确指定文件编码，避免乱码
4. **使用with语句**: 推荐使用with语句自动管理资源

## 注意事项

1. **文件路径**: 注意相对路径和绝对路径的区别
2. **权限问题**: 确保有足够的文件读写权限
3. **编码问题**: 处理中文时要注意编码设置
4. **资源泄露**: 忘记关闭文件会导致资源泄露

## 练习建议

1. 尝试打开不同类型的文件
2. 观察文件对象的各种属性
3. 练习处理文件操作异常
4. 比较手动关闭和with语句的区别

## 下一步学习

学习完文件基础操作后，建议继续学习：
- [文件读取方法](./02_file_reading.md)
- [文件写入方法](./03_file_writing.md)
- [with语句使用](./05_with_statement.md)