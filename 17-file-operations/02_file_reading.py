#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件读取方法详解

本模块演示Python中各种文件读取方法：
1. read() - 读取整个文件或指定字符数
2. readline() - 逐行读取文件
3. readlines() - 读取所有行到列表
4. 文件迭代器 - 逐行遍历文件
5. 不同读取方式的性能对比

学习要点：
- 掌握不同读取方法的使用场景
- 理解各种读取方式的优缺点
- 学会根据文件大小选择合适的读取方法
- 了解文件指针在读取过程中的变化
"""

import os
import time

def create_sample_file():
    """创建用于演示的示例文件"""
    filename = "sample_text.txt"
    content = """第一行：Python文件操作教程
第二行：学习文件读取方法
第三行：read()方法可以读取整个文件
第四行：readline()方法逐行读取
第五行：readlines()方法读取所有行
第六行：文件迭代器是最节省内存的方式
第七行：选择合适的读取方法很重要
第八行：大文件处理需要特别注意内存使用
第九行：文件操作完成后要记得关闭文件
第十行：这是示例文件的最后一行"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filename

def demonstrate_read_method():
    """演示read()方法的使用"""
    print("=== read()方法演示 ===")
    
    filename = create_sample_file()
    
    # 1. 读取整个文件
    print("1. 读取整个文件：")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"文件内容（共{len(content)}个字符）：")
        print(content[:100] + "..." if len(content) > 100 else content)
    
    # 2. 读取指定字符数
    print("\n2. 读取前50个字符：")
    with open(filename, 'r', encoding='utf-8') as f:
        partial_content = f.read(50)
        print(f"前50个字符: '{partial_content}'")
        
        # 继续读取剩余内容
        remaining = f.read(50)
        print(f"接下来50个字符: '{remaining}'")
    
    # 3. 多次调用read()
    print("\n3. 多次调用read()演示文件指针移动：")
    with open(filename, 'r', encoding='utf-8') as f:
        chunk1 = f.read(20)
        print(f"第一次读取: '{chunk1}'")
        
        chunk2 = f.read(20)
        print(f"第二次读取: '{chunk2}'")
        
        # 读取剩余所有内容
        rest = f.read()
        print(f"剩余内容长度: {len(rest)} 字符")
    
    os.remove(filename)

def demonstrate_readline_method():
    """演示readline()方法的使用"""
    print("\n=== readline()方法演示 ===")
    
    filename = create_sample_file()
    
    # 1. 逐行读取文件
    print("1. 使用readline()逐行读取：")
    with open(filename, 'r', encoding='utf-8') as f:
        line_number = 1
        while True:
            line = f.readline()
            if not line:  # 文件结束
                break
            print(f"第{line_number}行: {line.strip()}")
            line_number += 1
            
            # 只显示前5行作为演示
            if line_number > 5:
                print("... (省略剩余行)")
                break
    
    # 2. 读取指定长度的行内容
    print("\n2. readline()读取指定字符数：")
    with open(filename, 'r', encoding='utf-8') as f:
        partial_line = f.readline(15)  # 只读取15个字符
        print(f"部分行内容: '{partial_line}'")
        
        # 继续读取该行剩余内容
        rest_of_line = f.readline()
        print(f"该行剩余内容: '{rest_of_line.strip()}'")
    
    os.remove(filename)

def demonstrate_readlines_method():
    """演示readlines()方法的使用"""
    print("\n=== readlines()方法演示 ===")
    
    filename = create_sample_file()
    
    # 1. 读取所有行到列表
    print("1. readlines()读取所有行：")
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"总共读取了 {len(lines)} 行")
        
        # 显示前几行
        for i, line in enumerate(lines[:5], 1):
            print(f"第{i}行: {line.strip()}")
        
        if len(lines) > 5:
            print("... (省略剩余行)")
    
    # 2. 处理行列表
    print("\n2. 处理readlines()返回的列表：")
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        # 统计信息
        total_chars = sum(len(line) for line in lines)
        longest_line = max(lines, key=len)
        shortest_line = min(lines, key=len)
        
        print(f"总字符数: {total_chars}")
        print(f"最长行: {longest_line.strip()} (长度: {len(longest_line)})")
        print(f"最短行: {shortest_line.strip()} (长度: {len(shortest_line)})")
    
    os.remove(filename)

def demonstrate_file_iterator():
    """演示文件迭代器的使用"""
    print("\n=== 文件迭代器演示 ===")
    
    filename = create_sample_file()
    
    # 1. 直接迭代文件对象
    print("1. 使用for循环迭代文件：")
    with open(filename, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, 1):
            print(f"第{line_number}行: {line.strip()}")
            
            # 只显示前5行
            if line_number >= 5:
                print("... (省略剩余行)")
                break
    
    # 2. 文件迭代器的优势演示
    print("\n2. 文件迭代器处理大文件的优势：")
    print("   - 逐行读取，内存占用小")
    print("   - 适合处理大文件")
    print("   - 代码简洁易读")
    
    os.remove(filename)

def demonstrate_reading_performance():
    """演示不同读取方法的性能对比"""
    print("\n=== 读取方法性能对比 ===")
    
    # 创建一个较大的测试文件
    large_filename = "large_test.txt"
    print("创建大文件用于性能测试...")
    
    with open(large_filename, 'w', encoding='utf-8') as f:
        for i in range(1000):
            f.write(f"这是第{i+1}行，用于测试文件读取性能。包含一些中文字符和数字123456。\n")
    
    # 测试read()方法
    start_time = time.time()
    with open(large_filename, 'r', encoding='utf-8') as f:
        content = f.read()
    read_time = time.time() - start_time
    
    # 测试readlines()方法
    start_time = time.time()
    with open(large_filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    readlines_time = time.time() - start_time
    
    # 测试文件迭代器
    start_time = time.time()
    line_count = 0
    with open(large_filename, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
    iterator_time = time.time() - start_time
    
    # 测试readline()循环
    start_time = time.time()
    with open(large_filename, 'r', encoding='utf-8') as f:
        while f.readline():
            pass
    readline_time = time.time() - start_time
    
    print(f"文件大小: {os.path.getsize(large_filename)} 字节")
    print(f"read()方法耗时: {read_time:.4f}秒")
    print(f"readlines()方法耗时: {readlines_time:.4f}秒")
    print(f"文件迭代器耗时: {iterator_time:.4f}秒")
    print(f"readline()循环耗时: {readline_time:.4f}秒")
    
    print("\n性能建议：")
    print("- 小文件：使用read()或readlines()")
    print("- 大文件：使用文件迭代器")
    print("- 逐行处理：使用文件迭代器或readline()")
    
    os.remove(large_filename)

def demonstrate_reading_with_seek():
    """演示结合文件指针的读取操作"""
    print("\n=== 结合文件指针的读取操作 ===")
    
    # 创建一个纯英文文件避免UTF-8编码问题
    filename = "seek_test.txt"
    content = """Line 1: This is the first line of the file.
Line 2: This is the second line for testing.
Line 3: File pointer operations are important.
Line 4: Seek allows random access to file content.
Line 5: This is the last line of our test file."""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    with open(filename, 'r', encoding='utf-8') as f:
        # 读取前20个字符
        print("1. 读取前20个字符：")
        content1 = f.read(20)
        print(f"内容: '{content1}'")
        print(f"当前文件指针位置: {f.tell()}")
        
        # 移动文件指针到开头
        print("\n2. 重置文件指针到开头：")
        f.seek(0)
        print(f"重置后文件指针位置: {f.tell()}")
        
        # 重新读取
        content2 = f.read(20)
        print(f"重新读取的内容: '{content2}'")
        
        # 移动到安全的位置（行的开始）
        print("\n3. 移动到第二行开始：")
        f.seek(0)
        f.readline()  # 跳过第一行
        pos = f.tell()  # 获取第二行开始位置
        print(f"第二行开始位置: {pos}")
        
        content3 = f.read(30)
        print(f"第二行开始的30个字符: '{content3}'")
        
        # 演示文件结尾
        print("\n4. 移动到文件结尾：")
        f.seek(0, 2)  # 移动到文件结尾
        print(f"文件结尾位置: {f.tell()}")
        
        # 尝试读取（应该返回空字符串）
        end_content = f.read()
        print(f"文件结尾读取内容: '{end_content}' (长度: {len(end_content)})")
    
    os.remove(filename)

def main():
    """主函数 - 运行所有演示"""
    print("Python文件读取方法详解")
    print("=" * 50)
    
    # 运行各个演示函数
    demonstrate_read_method()
    demonstrate_readline_method()
    demonstrate_readlines_method()
    demonstrate_file_iterator()
    demonstrate_reading_performance()
    demonstrate_reading_with_seek()
    
    print("\n=== 学习总结 ===")
    print("1. read() - 适合小文件，一次性读取全部内容")
    print("2. readline() - 逐行读取，适合需要控制读取过程的场景")
    print("3. readlines() - 读取所有行到列表，适合需要随机访问行的场景")
    print("4. 文件迭代器 - 最推荐的方式，内存效率高，代码简洁")
    print("5. 选择读取方法要考虑文件大小和处理需求")
    print("\n最佳实践：")
    print("- 大文件使用文件迭代器")
    print("- 小文件可以使用read()或readlines()")
    print("- 需要逐行处理时使用文件迭代器")
    print("- 结合seek()可以实现随机访问")

if __name__ == "__main__":
    main()