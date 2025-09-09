#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件操作基础 - 文件的打开和关闭

本模块演示Python中文件操作的基础知识：
1. 文件的打开方式
2. 文件对象的基本属性
3. 文件的关闭操作
4. 文件操作的基本流程

学习要点：
- 理解文件对象的概念
- 掌握open()函数的基本用法
- 了解文件操作的完整流程
- 学会正确关闭文件资源
"""

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

def main():
    """主函数 - 运行所有演示"""
    print("Python文件操作基础教程")
    print("=" * 50)
    
    # 运行各个演示函数
    demonstrate_file_opening()
    demonstrate_file_attributes()
    demonstrate_file_lifecycle()
    demonstrate_multiple_files()
    demonstrate_file_errors()
    
    print("\n=== 学习总结 ===")
    print("1. 使用open()函数打开文件")
    print("2. 文件对象有name、mode、encoding等重要属性")
    print("3. 文件操作后必须调用close()方法关闭文件")
    print("4. 可以同时操作多个文件")
    print("5. 要注意处理文件操作中的异常")
    print("\n建议：在实际开发中，推荐使用with语句来自动管理文件资源！")

if __name__ == "__main__":
    main()