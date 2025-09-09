#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python文件操作 - 二进制文件处理

本模块演示二进制文件的各种操作：
1. 二进制文件的读写基础
2. 字节数据的处理
3. struct模块的使用
4. 图像文件的简单处理
5. 二进制文件的复制和比较
6. 数据序列化和反序列化
7. 二进制文件的性能优化

作者：Python学习助手
日期：2024年
"""

import os
import struct
import time
import pickle
from typing import List, Tuple, Any


def demonstrate_binary_basics():
    """演示二进制文件的基本读写操作"""
    print("\n=== 二进制文件基本操作 ===")
    
    # 1. 写入二进制数据
    print("\n1. 写入二进制数据：")
    binary_data = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'  # "Hello World"
    with open('binary_test.bin', 'wb') as f:
        f.write(binary_data)
        print(f"写入了 {len(binary_data)} 字节的二进制数据")
    
    # 2. 读取二进制数据
    print("\n2. 读取二进制数据：")
    with open('binary_test.bin', 'rb') as f:
        data = f.read()
        print(f"读取到 {len(data)} 字节：{data}")
        print(f"转换为字符串：{data.decode('utf-8')}")
    
    # 3. 字节和字符串的转换
    print("\n3. 字节和字符串的转换：")
    text = "Python二进制文件处理"
    # 字符串转字节
    bytes_data = text.encode('utf-8')
    print(f"字符串 '{text}' 转换为字节：{bytes_data}")
    print(f"字节长度：{len(bytes_data)}")
    
    # 字节转字符串
    decoded_text = bytes_data.decode('utf-8')
    print(f"字节转换回字符串：'{decoded_text}'")
    
    # 4. 逐字节处理
    print("\n4. 逐字节处理：")
    with open('binary_test.bin', 'rb') as f:
        byte_count = 0
        while True:
            byte = f.read(1)
            if not byte:
                break
            print(f"字节 {byte_count}: {byte} (0x{byte[0]:02x}) -> '{chr(byte[0])}'")
            byte_count += 1


def demonstrate_struct_usage():
    """演示struct模块的使用"""
    print("\n=== struct模块使用 ===")
    
    # 1. 基本数据类型的打包和解包
    print("\n1. 基本数据类型的打包：")
    
    # 打包不同类型的数据
    integer_val = 42
    float_val = 3.14159
    string_val = b"Hello"
    
    # 格式字符串：i=int, f=float, 5s=5字节字符串
    packed_data = struct.pack('if5s', integer_val, float_val, string_val)
    print(f"原始数据：整数={integer_val}, 浮点数={float_val}, 字符串={string_val}")
    print(f"打包后的字节数据：{packed_data}")
    print(f"打包后的长度：{len(packed_data)} 字节")
    
    # 解包数据
    unpacked_data = struct.unpack('if5s', packed_data)
    print(f"解包后的数据：{unpacked_data}")
    print(f"解包的整数：{unpacked_data[0]}")
    print(f"解包的浮点数：{unpacked_data[1]}")
    print(f"解包的字符串：{unpacked_data[2]}")
    
    # 2. 复杂数据结构的处理
    print("\n2. 复杂数据结构的处理：")
    
    # 模拟一个简单的文件头结构
    class FileHeader:
        def __init__(self, magic: bytes, version: int, size: int, checksum: int):
            self.magic = magic
            self.version = version
            self.size = size
            self.checksum = checksum
        
        def pack(self) -> bytes:
            """将文件头打包为二进制数据"""
            return struct.pack('4sIII', self.magic, self.version, self.size, self.checksum)
        
        @classmethod
        def unpack(cls, data: bytes):
            """从二进制数据解包文件头"""
            magic, version, size, checksum = struct.unpack('4sIII', data)
            return cls(magic, version, size, checksum)
        
        def __str__(self):
            return f"FileHeader(magic={self.magic}, version={self.version}, size={self.size}, checksum={self.checksum})"
    
    # 创建和保存文件头
    header = FileHeader(b'PYTH', 1, 1024, 0x12345678)
    print(f"原始文件头：{header}")
    
    with open('header_test.bin', 'wb') as f:
        f.write(header.pack())
    
    # 读取和解析文件头
    with open('header_test.bin', 'rb') as f:
        header_data = f.read(struct.calcsize('4sIII'))
        loaded_header = FileHeader.unpack(header_data)
        print(f"加载的文件头：{loaded_header}")
    
    # 3. 不同字节序的处理
    print("\n3. 字节序处理：")
    value = 0x12345678
    
    # 大端序（网络字节序）
    big_endian = struct.pack('>I', value)
    print(f"大端序：{big_endian.hex()}")
    
    # 小端序（本机字节序）
    little_endian = struct.pack('<I', value)
    print(f"小端序：{little_endian.hex()}")
    
    # 本机字节序
    native_endian = struct.pack('I', value)
    print(f"本机字节序：{native_endian.hex()}")


def demonstrate_image_processing():
    """演示简单的图像文件处理"""
    print("\n=== 简单图像文件处理 ===")
    
    # 创建一个简单的BMP文件头（简化版）
    def create_simple_bmp(width: int, height: int, filename: str):
        """创建一个简单的24位BMP图像"""
        # BMP文件头（14字节）
        file_header = struct.pack('<2sIHHI',
            b'BM',  # 文件类型
            54 + width * height * 3,  # 文件大小
            0,  # 保留字段
            0,  # 保留字段
            54  # 数据偏移
        )
        
        # BMP信息头（40字节）
        info_header = struct.pack('<IIIHHIIIIII',
            40,  # 信息头大小
            width,  # 图像宽度
            height,  # 图像高度
            1,  # 颜色平面数
            24,  # 每像素位数
            0,  # 压缩方式
            width * height * 3,  # 图像数据大小
            0,  # 水平分辨率
            0,  # 垂直分辨率
            0,  # 颜色数
            0   # 重要颜色数
        )
        
        # 创建简单的渐变图像数据（BGR格式）
        image_data = bytearray()
        for y in range(height):
            for x in range(width):
                # 创建简单的渐变效果
                blue = (x * 255) // width
                green = (y * 255) // height
                red = ((x + y) * 255) // (width + height)
                image_data.extend([blue, green, red])
        
        # 写入BMP文件
        with open(filename, 'wb') as f:
            f.write(file_header)
            f.write(info_header)
            f.write(image_data)
        
        print(f"创建了 {width}x{height} 的BMP图像：{filename}")
        return len(file_header) + len(info_header) + len(image_data)
    
    # 创建示例图像
    file_size = create_simple_bmp(100, 100, 'test_image.bmp')
    print(f"文件大小：{file_size} 字节")
    
    # 读取和分析BMP文件
    def analyze_bmp(filename: str):
        """分析BMP文件的基本信息"""
        with open(filename, 'rb') as f:
            # 读取文件头
            file_header = f.read(14)
            if len(file_header) < 14:
                print("文件头不完整")
                return
            
            file_type, file_size, _, _, data_offset = struct.unpack('<2sIHHI', file_header)
            print(f"\n文件类型：{file_type}")
            print(f"文件大小：{file_size} 字节")
            print(f"数据偏移：{data_offset} 字节")
            
            # 读取信息头
            info_header = f.read(40)
            if len(info_header) < 40:
                print("信息头不完整")
                return
            
            (header_size, width, height, planes, bits_per_pixel,
             compression, image_size, x_res, y_res, colors, important_colors) = struct.unpack('<IIIHHIIIIII', info_header)
            
            print(f"图像尺寸：{width} x {height}")
            print(f"每像素位数：{bits_per_pixel}")
            print(f"图像数据大小：{image_size} 字节")
    
    analyze_bmp('test_image.bmp')


def demonstrate_file_operations():
    """演示二进制文件的复制和比较"""
    print("\n=== 二进制文件操作 ===")
    
    # 1. 二进制文件复制
    print("\n1. 二进制文件复制：")
    
    def copy_binary_file(src: str, dst: str, buffer_size: int = 8192) -> int:
        """复制二进制文件"""
        bytes_copied = 0
        with open(src, 'rb') as src_file, open(dst, 'wb') as dst_file:
            while True:
                chunk = src_file.read(buffer_size)
                if not chunk:
                    break
                dst_file.write(chunk)
                bytes_copied += len(chunk)
        return bytes_copied
    
    # 复制之前创建的BMP文件
    if os.path.exists('test_image.bmp'):
        copied_bytes = copy_binary_file('test_image.bmp', 'test_image_copy.bmp')
        print(f"复制了 {copied_bytes} 字节")
    
    # 2. 二进制文件比较
    print("\n2. 二进制文件比较：")
    
    def compare_binary_files(file1: str, file2: str) -> Tuple[bool, int]:
        """比较两个二进制文件"""
        if not (os.path.exists(file1) and os.path.exists(file2)):
            return False, -1
        
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            pos = 0
            while True:
                chunk1 = f1.read(8192)
                chunk2 = f2.read(8192)
                
                if chunk1 != chunk2:
                    # 找到第一个不同的字节位置
                    for i, (b1, b2) in enumerate(zip(chunk1, chunk2)):
                        if b1 != b2:
                            return False, pos + i
                    # 如果长度不同
                    return False, pos + min(len(chunk1), len(chunk2))
                
                if not chunk1:  # 文件结束
                    break
                
                pos += len(chunk1)
        
        return True, -1
    
    if os.path.exists('test_image.bmp') and os.path.exists('test_image_copy.bmp'):
        is_same, diff_pos = compare_binary_files('test_image.bmp', 'test_image_copy.bmp')
        if is_same:
            print("文件完全相同")
        else:
            print(f"文件在位置 {diff_pos} 处不同")
    
    # 3. 文件校验和计算
    print("\n3. 文件校验和计算：")
    
    def calculate_checksum(filename: str) -> int:
        """计算文件的简单校验和"""
        checksum = 0
        with open(filename, 'rb') as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                checksum += sum(chunk)
        return checksum & 0xFFFFFFFF  # 32位校验和
    
    if os.path.exists('test_image.bmp'):
        checksum = calculate_checksum('test_image.bmp')
        print(f"文件校验和：0x{checksum:08x}")


def demonstrate_serialization():
    """演示数据序列化和反序列化"""
    print("\n=== 数据序列化 ===")
    
    # 1. 使用pickle进行对象序列化
    print("\n1. pickle序列化：")
    
    # 创建复杂的数据结构
    data = {
        'name': 'Python学习者',
        'scores': [85, 92, 78, 96],
        'info': {
            'age': 25,
            'city': '北京'
        },
        'timestamp': time.time()
    }
    
    print(f"原始数据：{data}")
    
    # 序列化到文件
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)
    
    # 从文件反序列化
    with open('data.pickle', 'rb') as f:
        loaded_data = pickle.load(f)
    
    print(f"加载的数据：{loaded_data}")
    print(f"数据是否相同：{data == loaded_data}")
    
    # 2. 自定义二进制格式
    print("\n2. 自定义二进制格式：")
    
    class Student:
        def __init__(self, name: str, age: int, scores: List[float]):
            self.name = name
            self.age = age
            self.scores = scores
        
        def to_binary(self) -> bytes:
            """转换为二进制格式"""
            # 格式：名字长度(1字节) + 名字 + 年龄(2字节) + 成绩数量(1字节) + 成绩列表
            name_bytes = self.name.encode('utf-8')
            data = struct.pack('B', len(name_bytes))  # 名字长度
            data += name_bytes  # 名字
            data += struct.pack('H', self.age)  # 年龄
            data += struct.pack('B', len(self.scores))  # 成绩数量
            for score in self.scores:
                data += struct.pack('f', score)  # 每个成绩
            return data
        
        @classmethod
        def from_binary(cls, data: bytes):
            """从二进制格式创建对象"""
            offset = 0
            
            # 读取名字长度
            name_len = struct.unpack_from('B', data, offset)[0]
            offset += 1
            
            # 读取名字
            name = data[offset:offset + name_len].decode('utf-8')
            offset += name_len
            
            # 读取年龄
            age = struct.unpack_from('H', data, offset)[0]
            offset += 2
            
            # 读取成绩数量
            score_count = struct.unpack_from('B', data, offset)[0]
            offset += 1
            
            # 读取成绩列表
            scores = []
            for _ in range(score_count):
                score = struct.unpack_from('f', data, offset)[0]
                scores.append(score)
                offset += 4
            
            return cls(name, age, scores)
        
        def __str__(self):
            return f"Student(name='{self.name}', age={self.age}, scores={self.scores})"
    
    # 创建学生对象
    student = Student("张三", 20, [85.5, 92.0, 78.5, 96.0])
    print(f"原始学生对象：{student}")
    
    # 序列化
    binary_data = student.to_binary()
    print(f"二进制数据长度：{len(binary_data)} 字节")
    print(f"二进制数据：{binary_data.hex()}")
    
    # 反序列化
    loaded_student = Student.from_binary(binary_data)
    print(f"加载的学生对象：{loaded_student}")


def demonstrate_performance():
    """演示二进制文件操作的性能优化"""
    print("\n=== 性能优化 ===")
    
    # 创建测试数据
    test_data = b'0123456789' * 10000  # 100KB数据
    
    print("\n1. 不同缓冲区大小的性能比较：")
    
    def write_with_buffer(data: bytes, filename: str, buffer_size: int) -> float:
        """使用指定缓冲区大小写入数据"""
        start_time = time.time()
        with open(filename, 'wb', buffering=buffer_size) as f:
            f.write(data)
        return time.time() - start_time
    
    buffer_sizes = [1024, 4096, 8192, 16384, 65536]
    for buffer_size in buffer_sizes:
        filename = f'test_{buffer_size}.bin'
        write_time = write_with_buffer(test_data, filename, buffer_size)
        print(f"缓冲区 {buffer_size:5d} 字节：写入时间 {write_time:.4f} 秒")
        
        # 清理测试文件
        if os.path.exists(filename):
            os.remove(filename)
    
    print("\n2. 分块读取vs一次性读取：")
    
    # 创建测试文件
    with open('large_test.bin', 'wb') as f:
        f.write(test_data)
    
    # 一次性读取
    start_time = time.time()
    with open('large_test.bin', 'rb') as f:
        data = f.read()
    read_all_time = time.time() - start_time
    print(f"一次性读取：{read_all_time:.4f} 秒，读取 {len(data)} 字节")
    
    # 分块读取
    start_time = time.time()
    total_bytes = 0
    with open('large_test.bin', 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            total_bytes += len(chunk)
    chunk_read_time = time.time() - start_time
    print(f"分块读取：{chunk_read_time:.4f} 秒，读取 {total_bytes} 字节")
    
    # 清理测试文件
    if os.path.exists('large_test.bin'):
        os.remove('large_test.bin')


def cleanup_files():
    """清理演示过程中创建的文件"""
    files_to_remove = [
        'binary_test.bin', 'header_test.bin', 'test_image.bmp', 
        'test_image_copy.bmp', 'data.pickle'
    ]
    
    for filename in files_to_remove:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"已删除文件：{filename}")


def main():
    """主函数"""
    print("Python文件操作 - 二进制文件处理")
    print("=" * 50)
    
    try:
        # 演示各种二进制文件操作
        demonstrate_binary_basics()
        demonstrate_struct_usage()
        demonstrate_image_processing()
        demonstrate_file_operations()
        demonstrate_serialization()
        demonstrate_performance()
        
    except Exception as e:
        print(f"\n演示过程中出现错误：{e}")
    
    finally:
        # 清理文件
        print("\n=== 清理演示文件 ===")
        cleanup_files()
    
    # 学习总结
    print("\n" + "=" * 50)
    print("=== 学习总结 ===")
    print("""
二进制文件处理核心概念：
1. 二进制模式：使用'rb'、'wb'、'ab'等模式
2. 字节对象：bytes和bytearray的使用
3. 编码转换：字符串和字节之间的转换
4. 逐字节处理：精确控制数据读写

struct模块的重要性：
- 数据打包：将Python对象转换为字节
- 数据解包：将字节转换为Python对象
- 格式字符串：定义数据结构
- 字节序控制：处理不同平台的差异

实际应用场景：
- 图像文件处理：BMP、PNG等格式
- 网络协议：数据包的构造和解析
- 文件格式：自定义二进制格式
- 数据序列化：对象的持久化存储
- 系统编程：与底层系统交互

性能优化技巧：
- 合适的缓冲区大小
- 分块处理大文件
- 避免频繁的小量读写
- 使用适当的数据结构
- 考虑内存使用效率

注意事项和最佳实践：
- 始终使用二进制模式处理二进制数据
- 注意字节序的影响
- 处理编码和解码错误
- 合理使用缓冲区
- 及时关闭文件句柄
- 考虑跨平台兼容性
""")


if __name__ == "__main__":
    main()