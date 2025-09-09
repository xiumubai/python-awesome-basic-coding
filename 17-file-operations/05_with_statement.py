#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件操作 - with语句的使用

本模块演示with语句在文件操作中的使用，包括：
1. with语句的基本用法
2. 上下文管理器的工作原理
3. 多文件同时操作
4. 自定义上下文管理器
5. 异常处理与资源清理
6. 嵌套with语句

作者：Python学习助手
日期：2024年
"""

import os
import time
from contextlib import contextmanager


def demonstrate_basic_with():
    """演示with语句的基本用法"""
    print("=== with语句基本用法 ===")
    
    # 传统方式（不推荐）
    print("\n1. 传统方式（手动管理资源）：")
    try:
        file = open('traditional_way.txt', 'w', encoding='utf-8')
        file.write('传统方式写入文件\n')
        file.write('需要手动关闭文件\n')
    finally:
        file.close()  # 必须手动关闭
    print("传统方式：文件已写入并手动关闭")
    
    # with语句方式（推荐）
    print("\n2. with语句方式（自动管理资源）：")
    with open('with_statement_way.txt', 'w', encoding='utf-8') as file:
        file.write('使用with语句写入文件\n')
        file.write('文件会自动关闭\n')
    print("with语句：文件已写入并自动关闭")
    
    # 验证文件状态
    print("\n3. 验证文件关闭状态：")
    with open('with_statement_way.txt', 'r', encoding='utf-8') as file:
        print(f"文件是否关闭：{file.closed}")  # False，文件在with块内是打开的
    print(f"离开with块后文件是否关闭：{file.closed}")  # True，自动关闭


def demonstrate_context_manager_principle():
    """演示上下文管理器的工作原理"""
    print("\n=== 上下文管理器工作原理 ===")
    
    class FileManager:
        """自定义文件管理器，演示上下文管理器协议"""
        
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None
        
        def __enter__(self):
            """进入with块时调用"""
            print(f"__enter__: 打开文件 {self.filename}")
            self.file = open(self.filename, self.mode, encoding='utf-8')
            return self.file
        
        def __exit__(self, exc_type, exc_value, traceback):
            """离开with块时调用"""
            print(f"__exit__: 关闭文件 {self.filename}")
            if self.file:
                self.file.close()
            
            # 处理异常信息
            if exc_type:
                print(f"发生异常: {exc_type.__name__}: {exc_value}")
            return False  # 不抑制异常
    
    print("\n使用自定义上下文管理器：")
    with FileManager('custom_manager.txt', 'w') as file:
        print("在with块内写入数据")
        file.write('使用自定义上下文管理器\n')
        file.write('演示__enter__和__exit__方法\n')
    print("离开with块")


def demonstrate_multiple_files():
    """演示多文件同时操作"""
    print("\n=== 多文件同时操作 ===")
    
    # 方式1：嵌套with语句
    print("\n1. 嵌套with语句：")
    with open('source.txt', 'w', encoding='utf-8') as source:
        source.write('这是源文件内容\n')
        source.write('包含多行数据\n')
        source.write('需要复制到目标文件\n')
    
    with open('source.txt', 'r', encoding='utf-8') as source:
        with open('target1.txt', 'w', encoding='utf-8') as target:
            content = source.read()
            target.write(content)
            print("嵌套方式：文件复制完成")
    
    # 方式2：单个with语句管理多个文件
    print("\n2. 单个with语句管理多个文件：")
    with open('source.txt', 'r', encoding='utf-8') as source, \
         open('target2.txt', 'w', encoding='utf-8') as target:
        
        for line_num, line in enumerate(source, 1):
            target.write(f"第{line_num}行: {line}")
        print("单with方式：文件复制完成")
    
    # 方式3：使用contextlib.ExitStack
    print("\n3. 使用ExitStack管理多个文件：")
    from contextlib import ExitStack
    
    filenames = ['file1.txt', 'file2.txt', 'file3.txt']
    
    with ExitStack() as stack:
        files = [stack.enter_context(open(f, 'w', encoding='utf-8')) 
                for f in filenames]
        
        for i, file in enumerate(files):
            file.write(f'这是文件{i+1}的内容\n')
            file.write(f'使用ExitStack管理\n')
        
        print(f"ExitStack方式：同时创建了{len(files)}个文件")


@contextmanager
def file_with_backup(filename, mode='r'):
    """使用contextlib.contextmanager装饰器创建上下文管理器"""
    backup_name = f"{filename}.backup"
    
    # 如果是写模式且文件存在，先备份
    if 'w' in mode and os.path.exists(filename):
        print(f"备份原文件: {filename} -> {backup_name}")
        with open(filename, 'r', encoding='utf-8') as original:
            with open(backup_name, 'w', encoding='utf-8') as backup:
                backup.write(original.read())
    
    try:
        print(f"打开文件: {filename}")
        file = open(filename, mode, encoding='utf-8')
        yield file
    except Exception as e:
        print(f"操作失败，恢复备份: {e}")
        if os.path.exists(backup_name):
            os.rename(backup_name, filename)
        raise
    else:
        print(f"操作成功，删除备份")
        if os.path.exists(backup_name):
            os.remove(backup_name)
    finally:
        if 'file' in locals():
            file.close()
            print(f"关闭文件: {filename}")


def demonstrate_custom_context_manager():
    """演示自定义上下文管理器"""
    print("\n=== 自定义上下文管理器 ===")
    
    # 创建原始文件
    with open('important_data.txt', 'w', encoding='utf-8') as f:
        f.write('重要数据\n')
        f.write('不能丢失\n')
    
    print("\n使用带备份功能的上下文管理器：")
    try:
        with file_with_backup('important_data.txt', 'w') as f:
            f.write('修改后的数据\n')
            f.write('新的内容\n')
            # 模拟可能的错误
            # raise ValueError("模拟错误")
    except ValueError as e:
        print(f"捕获到错误: {e}")


def demonstrate_exception_handling():
    """演示with语句中的异常处理"""
    print("\n=== with语句异常处理 ===")
    
    class SafeFileManager:
        """安全的文件管理器，处理各种异常情况"""
        
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None
        
        def __enter__(self):
            try:
                print(f"尝试打开文件: {self.filename}")
                self.file = open(self.filename, self.mode, encoding='utf-8')
                return self.file
            except FileNotFoundError:
                print(f"文件不存在: {self.filename}")
                raise
            except PermissionError:
                print(f"权限不足: {self.filename}")
                raise
        
        def __exit__(self, exc_type, exc_value, traceback):
            if self.file and not self.file.closed:
                self.file.close()
                print(f"文件已安全关闭: {self.filename}")
            
            if exc_type:
                print(f"处理异常: {exc_type.__name__}: {exc_value}")
                # 返回True会抑制异常，False会传播异常
                return False
    
    # 测试正常情况
    print("\n1. 正常文件操作：")
    try:
        with SafeFileManager('safe_test.txt', 'w') as f:
            f.write('安全文件操作测试\n')
        print("操作成功完成")
    except Exception as e:
        print(f"操作失败: {e}")
    
    # 测试异常情况
    print("\n2. 异常情况处理：")
    try:
        with SafeFileManager('nonexistent_dir/file.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("已正确处理文件不存在的异常")


def demonstrate_nested_with():
    """演示嵌套with语句的使用"""
    print("\n=== 嵌套with语句 ===")
    
    # 创建测试数据
    test_data = [
        "第一行数据",
        "第二行数据", 
        "第三行数据"
    ]
    
    print("\n创建多个相关文件：")
    
    # 嵌套with处理多个相关操作
    with open('data_source.txt', 'w', encoding='utf-8') as source:
        # 写入源数据
        for line in test_data:
            source.write(f"{line}\n")
        
        # 在同一个with块中进行相关操作
        with open('data_processed.txt', 'w', encoding='utf-8') as processed:
            with open('data_log.txt', 'w', encoding='utf-8') as log:
                
                log.write(f"处理开始时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                
                # 重新读取源文件进行处理
                source.seek(0)  # 回到文件开头
                
                for i, line in enumerate(test_data):
                    processed_line = f"处理后-{line.upper()}"
                    processed.write(f"{processed_line}\n")
                    log.write(f"处理第{i+1}行: {line} -> {processed_line}\n")
                
                log.write(f"处理结束时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                log.write(f"总共处理了{len(test_data)}行数据\n")
    
    print("嵌套with操作完成：创建了源文件、处理文件和日志文件")


def demonstrate_performance_comparison():
    """演示with语句的性能和安全性优势"""
    print("\n=== 性能和安全性对比 ===")
    
    import time
    
    # 测试数据
    test_lines = [f"测试数据行 {i}\n" for i in range(1000)]
    
    # 方式1：手动管理（容易出错）
    print("\n1. 手动管理文件（不推荐）：")
    start_time = time.time()
    
    files = []
    try:
        for i in range(5):
            f = open(f'manual_{i}.txt', 'w', encoding='utf-8')
            files.append(f)
            f.writelines(test_lines)
    finally:
        # 手动关闭所有文件
        for f in files:
            if not f.closed:
                f.close()
    
    manual_time = time.time() - start_time
    print(f"手动管理耗时: {manual_time:.4f}秒")
    
    # 方式2：with语句管理（推荐）
    print("\n2. with语句管理（推荐）：")
    start_time = time.time()
    
    for i in range(5):
        with open(f'with_{i}.txt', 'w', encoding='utf-8') as f:
            f.writelines(test_lines)
    
    with_time = time.time() - start_time
    print(f"with语句耗时: {with_time:.4f}秒")
    
    print(f"\n性能对比：")
    print(f"- 手动管理: {manual_time:.4f}秒")
    print(f"- with语句: {with_time:.4f}秒")
    print(f"- 性能差异: {abs(manual_time - with_time):.4f}秒")
    
    print("\n安全性优势：")
    print("- with语句确保文件总是被正确关闭")
    print("- 即使发生异常也能正确清理资源")
    print("- 代码更简洁，减少出错可能")
    print("- 符合Python的'优雅胜于丑陋'原则")


def cleanup_test_files():
    """清理测试文件"""
    test_files = [
        'traditional_way.txt', 'with_statement_way.txt', 'custom_manager.txt',
        'source.txt', 'target1.txt', 'target2.txt', 'file1.txt', 'file2.txt', 'file3.txt',
        'important_data.txt', 'important_data.txt.backup', 'safe_test.txt',
        'data_source.txt', 'data_processed.txt', 'data_log.txt'
    ]
    
    # 添加批量生成的文件
    for i in range(5):
        test_files.extend([f'manual_{i}.txt', f'with_{i}.txt'])
    
    for filename in test_files:
        try:
            if os.path.exists(filename):
                os.remove(filename)
        except Exception:
            pass  # 忽略删除错误


def main():
    """主函数"""
    print("Python文件操作 - with语句的使用")
    print("=" * 50)
    
    try:
        # 演示各种with语句用法
        demonstrate_basic_with()
        demonstrate_context_manager_principle()
        demonstrate_multiple_files()
        demonstrate_custom_context_manager()
        demonstrate_exception_handling()
        demonstrate_nested_with()
        demonstrate_performance_comparison()
        
    finally:
        # 清理测试文件
        cleanup_test_files()
    
    print("\n" + "=" * 50)
    print("=== 学习总结 ===")
    print("\nwith语句的核心概念：")
    print("1. 上下文管理器协议：__enter__和__exit__方法")
    print("2. 自动资源管理：确保资源正确获取和释放")
    print("3. 异常安全：即使发生异常也能正确清理")
    print("4. 代码简洁：减少样板代码，提高可读性")
    
    print("\nwith语句的优势：")
    print("- 自动调用__enter__和__exit__方法")
    print("- 保证资源正确释放，避免资源泄露")
    print("- 异常安全，即使出错也能清理资源")
    print("- 代码更简洁，符合Python哲学")
    
    print("\n实际应用场景：")
    print("- 文件操作：自动关闭文件")
    print("- 数据库连接：自动关闭连接")
    print("- 网络连接：自动关闭socket")
    print("- 线程锁：自动释放锁")
    print("- 临时目录：自动清理临时文件")
    
    print("\n最佳实践：")
    print("- 优先使用with语句进行资源管理")
    print("- 自定义类时实现上下文管理器协议")
    print("- 使用contextlib简化上下文管理器创建")
    print("- 合理处理__exit__方法中的异常")
    print("- 多个资源可以在一个with语句中管理")


if __name__ == "__main__":
    main()