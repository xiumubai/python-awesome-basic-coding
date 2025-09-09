#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件操作 - 文件指针操作

本模块演示文件指针操作，包括：
1. 文件指针的基本概念
2. seek()方法的使用
3. tell()方法获取当前位置
4. 不同模式下的指针行为
5. 文件指针与读写操作的关系
6. 实际应用场景

作者：Python学习助手
日期：2024年
"""

import os


def demonstrate_basic_pointer_operations():
    """演示文件指针的基本操作"""
    print("=== 文件指针基本操作 ===")
    
    # 创建测试文件
    content = "Hello World!\nThis is line 2\nThis is line 3\nEnd of file"
    with open('pointer_test.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n1. tell()方法 - 获取当前指针位置：")
    with open('pointer_test.txt', 'r', encoding='utf-8') as f:
        print(f"文件打开时指针位置: {f.tell()}")
        
        # 读取一些字符
        char = f.read(5)
        print(f"读取'{char}'后指针位置: {f.tell()}")
        
        # 读取一行
        line = f.readline()
        print(f"读取一行'{line.strip()}'后指针位置: {f.tell()}")
        
        # 读取剩余内容
        remaining = f.read()
        print(f"读取剩余内容后指针位置: {f.tell()}")
        print(f"文件大小: {len(content.encode('utf-8'))}字节")


def demonstrate_seek_operations():
    """演示seek()方法的使用"""
    print("\n=== seek()方法使用 ===")
    
    # 创建英文测试文件（避免编码问题）
    content = "ABCDEFGHIJKLMNOPQRSTUVWXYZ\n0123456789\nHello Python\nEnd"
    with open('seek_test.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n1. 文本模式下的基本seek操作：")
    with open('seek_test.txt', 'r', encoding='utf-8') as f:
        # 模式0: SEEK_SET - 从文件开头计算（文本模式主要支持这种）
        print("\n模式0 (SEEK_SET) - 从文件开头：")
        f.seek(0)  # 回到文件开头（默认whence=0）
        print(f"seek(0)后位置: {f.tell()}, 读取: '{f.read(5)}'")
        
        f.seek(10)  # 从开头偏移10个字节
        print(f"seek(10)后位置: {f.tell()}, 读取: '{f.read(5)}'")
        
        # 获取文件大小
        f.seek(0, 2)  # 移到文件末尾
        file_size = f.tell()
        print(f"\n文件大小: {file_size}字节")
        
        # 回到开头继续演示
        f.seek(0)
        print(f"回到开头: {f.tell()}, 读取前3个字符: '{f.read(3)}'")
    
    print("\n2. seek()在二进制模式下的完整功能：")
    # 在二进制模式下演示所有三种模式
    with open('seek_test.txt', 'rb') as f:
        # 模式0: SEEK_SET - 从文件开头计算
        print("\n二进制模式 - 模式0 (SEEK_SET)：")
        f.seek(0, 0)
        data = f.read(5)
        print(f"seek(0, 0)后位置: {f.tell()}, 读取: {data.decode('utf-8')}")
        
        # 模式1: SEEK_CUR - 从当前位置计算（二进制模式支持）
        print("\n二进制模式 - 模式1 (SEEK_CUR)：")
        current_pos = f.tell()
        f.seek(5, 1)  # 从当前位置向前5个字节
        data = f.read(3)
        print(f"从位置{current_pos}向前5字节到: {f.tell()}, 读取: {data.decode('utf-8')}")
        
        f.seek(-3, 1)  # 从当前位置向后3个字节
        data = f.read(3)
        print(f"向后3字节到: {f.tell()}, 读取: {data.decode('utf-8')}")
        
        # 模式2: SEEK_END - 从文件末尾计算
        print("\n二进制模式 - 模式2 (SEEK_END)：")
        f.seek(0, 2)
        print(f"seek(0, 2)文件末尾位置: {f.tell()}")
        
        f.seek(-10, 2)
        data = f.read()
        print(f"从末尾向前10字节: {f.tell()}, 读取: {data.decode('utf-8')}")
    
    print("\n注意：文本模式下只支持SEEK_SET和SEEK_END，不支持SEEK_CUR的非零偏移")


def demonstrate_pointer_with_different_modes():
    """演示不同文件模式下的指针行为"""
    print("\n=== 不同模式下的指针行为 ===")
    
    # 准备测试数据
    original_content = "Line 1\nLine 2\nLine 3\n"
    
    print("\n1. 读模式('r')的指针行为：")
    with open('mode_test.txt', 'w', encoding='utf-8') as f:
        f.write(original_content)
    
    with open('mode_test.txt', 'r', encoding='utf-8') as f:
        print(f"打开时指针位置: {f.tell()}")
        f.read(5)
        print(f"读取后指针位置: {f.tell()}")
        f.seek(0)
        print(f"seek(0)后指针位置: {f.tell()}")
    
    print("\n2. 写模式('w')的指针行为：")
    with open('mode_test.txt', 'w', encoding='utf-8') as f:
        print(f"写模式打开时指针位置: {f.tell()}")
        f.write("New content")
        print(f"写入后指针位置: {f.tell()}")
    
    print("\n3. 追加模式('a')的指针行为：")
    with open('mode_test.txt', 'a', encoding='utf-8') as f:
        print(f"追加模式打开时指针位置: {f.tell()}")
        f.write(" Appended")
        print(f"追加后指针位置: {f.tell()}")
        
        # 在追加模式下尝试移动指针
        f.seek(0)
        print(f"追加模式seek(0)后位置: {f.tell()}")
        f.write(" More")
        print(f"追加模式写入后位置: {f.tell()}")
    
    print("\n4. 读写模式('r+')的指针行为：")
    with open('mode_test.txt', 'r+', encoding='utf-8') as f:
        print(f"读写模式打开时指针位置: {f.tell()}")
        content = f.read(5)
        print(f"读取'{content}'后位置: {f.tell()}")
        
        f.seek(0)
        f.write("MODIFIED")
        print(f"写入后指针位置: {f.tell()}")
        
        # 读取修改后的内容
        f.seek(0)
        print(f"修改后的文件内容: '{f.read()}'")


def demonstrate_pointer_with_binary_mode():
    """演示二进制模式下的指针操作"""
    print("\n=== 二进制模式下的指针操作 ===")
    
    # 创建二进制数据
    binary_data = bytes(range(256))  # 0-255的字节数据
    
    with open('binary_test.bin', 'wb') as f:
        f.write(binary_data)
    
    print("\n1. 二进制文件的指针操作：")
    with open('binary_test.bin', 'rb') as f:
        print(f"文件大小: {len(binary_data)}字节")
        
        # 读取前10个字节
        data = f.read(10)
        print(f"前10字节: {list(data)}, 指针位置: {f.tell()}")
        
        # 跳到中间位置
        f.seek(100)
        data = f.read(5)
        print(f"位置100开始的5字节: {list(data)}, 指针位置: {f.tell()}")
        
        # 从末尾读取
        f.seek(-10, 2)
        data = f.read()
        print(f"最后10字节: {list(data)}, 指针位置: {f.tell()}")
    
    print("\n2. 二进制文件的随机访问：")
    with open('binary_test.bin', 'r+b') as f:
        # 修改特定位置的数据
        f.seek(50)
        original = f.read(1)[0]
        print(f"位置50的原始值: {original}")
        
        f.seek(50)
        f.write(bytes([255]))  # 写入255
        
        f.seek(50)
        modified = f.read(1)[0]
        print(f"位置50的修改值: {modified}")


def demonstrate_practical_applications():
    """演示文件指针的实际应用场景"""
    print("\n=== 实际应用场景 ===")
    
    print("\n1. 日志文件的尾部追踪：")
    
    # 模拟日志文件
    log_content = """2024-01-01 10:00:00 INFO: Application started
2024-01-01 10:01:00 DEBUG: Loading configuration
2024-01-01 10:02:00 INFO: Server listening on port 8080
2024-01-01 10:03:00 WARNING: High memory usage detected
2024-01-01 10:04:00 ERROR: Database connection failed
"""
    
    with open('app.log', 'w', encoding='utf-8') as f:
        f.write(log_content)
    
    # 模拟tail -f功能
    def tail_file(filename, lines=3):
        """读取文件的最后几行"""
        with open(filename, 'r', encoding='utf-8') as f:
            # 移到文件末尾
            f.seek(0, 2)
            file_size = f.tell()
            
            # 从末尾向前查找换行符
            lines_found = 0
            pos = file_size
            
            while pos > 0 and lines_found < lines:
                pos -= 1
                f.seek(pos)
                if f.read(1) == '\n':
                    lines_found += 1
            
            # 如果找到了足够的行，移动到正确位置
            if lines_found == lines:
                f.seek(pos + 1)
            else:
                f.seek(0)
            
            return f.read()
    
    print("最后3行日志：")
    print(tail_file('app.log', 3))
    
    print("\n2. 配置文件的部分更新：")
    
    # 创建配置文件
    config_content = """[database]
host=localhost
port=5432
user=admin
password=secret123

[server]
port=8080
debug=true
"""
    
    with open('config.ini', 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    def update_config_value(filename, section, key, new_value):
        """更新配置文件中的特定值"""
        with open(filename, 'r+', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            
            in_section = False
            for i, line in enumerate(lines):
                if line.strip() == f'[{section}]':
                    in_section = True
                elif line.startswith('[') and line.endswith(']'):
                    in_section = False
                elif in_section and line.startswith(f'{key}='):
                    lines[i] = f'{key}={new_value}'
                    break
            
            # 重写文件
            f.seek(0)
            f.write('\n'.join(lines))
            f.truncate()
    
    print("更新数据库端口为5433：")
    update_config_value('config.ini', 'database', 'port', '5433')
    
    with open('config.ini', 'r', encoding='utf-8') as f:
        print(f.read())
    
    print("\n3. 大文件的分块处理：")
    
    def process_large_file_in_chunks(filename, chunk_size=1024):
        """分块处理大文件"""
        with open(filename, 'rb') as f:
            chunk_count = 0
            while True:
                chunk_start = f.tell()
                chunk = f.read(chunk_size)
                
                if not chunk:
                    break
                
                chunk_count += 1
                print(f"处理块{chunk_count}: 位置{chunk_start}-{f.tell()-1}, 大小{len(chunk)}字节")
                
                # 这里可以处理chunk数据
                # process_chunk(chunk)
    
    # 创建一个较大的测试文件
    with open('large_file.dat', 'wb') as f:
        f.write(b'X' * 5000)  # 5KB的测试数据
    
    print("分块处理5KB文件（每块1KB）：")
    process_large_file_in_chunks('large_file.dat', 1024)


def demonstrate_pointer_pitfalls():
    """演示文件指针操作的常见陷阱"""
    print("\n=== 文件指针常见陷阱 ===")
    
    print("\n1. 文本模式下的字符编码问题：")
    
    # 创建包含中文的文件
    chinese_content = "你好世界\nHello World\n测试文本"
    with open('chinese_test.txt', 'w', encoding='utf-8') as f:
        f.write(chinese_content)
    
    with open('chinese_test.txt', 'r', encoding='utf-8') as f:
        print(f"文件内容: {repr(f.read())}")
        
        # 重置到开头
        f.seek(0)
        
        # 尝试移动到字符中间（可能导致问题）
        try:
            f.seek(2)  # 可能在多字节字符中间
            char = f.read(1)
            print(f"位置2的字符: {repr(char)}")
        except UnicodeDecodeError as e:
            print(f"编码错误: {e}")
    
    print("\n2. 追加模式下的指针行为：")
    
    with open('append_test.txt', 'w', encoding='utf-8') as f:
        f.write("Initial content\n")
    
    with open('append_test.txt', 'a', encoding='utf-8') as f:
        print(f"追加模式打开时位置: {f.tell()}")
        
        # 尝试移动到开头
        f.seek(0)
        print(f"seek(0)后位置: {f.tell()}")
        
        # 写入数据（总是在末尾）
        f.write("Appended at end\n")
        print(f"写入后位置: {f.tell()}")
    
    with open('append_test.txt', 'r', encoding='utf-8') as f:
        print(f"最终文件内容:\n{f.read()}")
    
    print("\n3. 读写模式下的指针同步：")
    
    with open('rw_test.txt', 'w', encoding='utf-8') as f:
        f.write("ABCDEFGHIJ")
    
    with open('rw_test.txt', 'r+', encoding='utf-8') as f:
        # 读取前5个字符
        data = f.read(5)
        print(f"读取: {data}, 当前位置: {f.tell()}")
        
        # 在当前位置写入
        f.write("XYZ")
        print(f"写入XYZ后位置: {f.tell()}")
        
        # 读取剩余内容
        remaining = f.read()
        print(f"剩余内容: {remaining}")
        
        # 查看最终文件内容
        f.seek(0)
        final_content = f.read()
        print(f"最终文件内容: {final_content}")


def cleanup_test_files():
    """清理测试文件"""
    test_files = [
        'pointer_test.txt', 'seek_test.txt', 'mode_test.txt',
        'binary_test.bin', 'app.log', 'config.ini', 'large_file.dat',
        'chinese_test.txt', 'append_test.txt', 'rw_test.txt'
    ]
    
    for filename in test_files:
        try:
            if os.path.exists(filename):
                os.remove(filename)
        except Exception:
            pass


def main():
    """主函数"""
    print("Python文件操作 - 文件指针操作")
    print("=" * 50)
    
    try:
        # 演示各种文件指针操作
        demonstrate_basic_pointer_operations()
        demonstrate_seek_operations()
        demonstrate_pointer_with_different_modes()
        demonstrate_pointer_with_binary_mode()
        demonstrate_practical_applications()
        demonstrate_pointer_pitfalls()
        
    finally:
        # 清理测试文件
        cleanup_test_files()
    
    print("\n" + "=" * 50)
    print("=== 学习总结 ===")
    print("\n文件指针核心概念：")
    print("1. 文件指针：标记当前读写位置的游标")
    print("2. tell()：获取当前指针位置（字节偏移）")
    print("3. seek()：移动指针到指定位置")
    print("4. 指针位置影响所有读写操作")
    
    print("\nseek()方法的三种模式：")
    print("- seek(offset, 0)：从文件开头计算偏移")
    print("- seek(offset, 1)：从当前位置计算偏移")
    print("- seek(offset, 2)：从文件末尾计算偏移")
    
    print("\n不同文件模式的指针行为：")
    print("- 'r'模式：指针从开头开始，只能读取")
    print("- 'w'模式：指针从开头开始，清空文件")
    print("- 'a'模式：指针在末尾，写入总是追加")
    print("- 'r+'模式：指针从开头开始，可读可写")
    print("- 'w+'模式：指针从开头开始，清空文件，可读可写")
    print("- 'a+'模式：指针在末尾，可读，写入总是追加")
    
    print("\n实际应用场景：")
    print("- 日志文件尾部追踪（tail功能）")
    print("- 配置文件部分更新")
    print("- 大文件分块处理")
    print("- 二进制文件随机访问")
    print("- 数据文件的索引操作")
    
    print("\n注意事项和最佳实践：")
    print("- 文本模式下注意多字节字符的边界")
    print("- 追加模式下seek()不影响写入位置")
    print("- 读写操作会自动移动指针")
    print("- 二进制模式下指针操作更精确")
    print("- 使用tell()确认当前位置")
    print("- 大文件操作时注意内存使用")


if __name__ == "__main__":
    main()