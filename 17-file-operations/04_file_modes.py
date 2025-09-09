#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件模式详解

本模块详细演示Python中各种文件打开模式的使用：
1. 文本模式：'r', 'w', 'a', 'x'
2. 二进制模式：'rb', 'wb', 'ab'
3. 读写模式：'r+', 'w+', 'a+'
4. 模式组合和参数
5. 实际应用场景
6. 模式选择指南

学习要点：
- 理解各种文件模式的区别
- 掌握模式的组合使用
- 学会根据需求选择合适的模式
- 了解模式对文件指针的影响
"""

import os
import tempfile
from datetime import datetime


def demonstrate_basic_text_modes():
    """演示基本文本模式"""
    print("=== 基本文本模式演示 ===")
    
    filename = "modes_demo.txt"
    
    # 创建测试文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("原始内容：第一行\n原始内容：第二行\n原始内容：第三行\n")
    
    print("1. 'r' 模式 - 只读模式（默认）：")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"读取内容：\n{content}")
            print(f"文件指针位置：{f.tell()}")
            
            # 尝试写入（会失败）
            try:
                f.write("尝试写入")
            except io.UnsupportedOperation:
                print("'r'模式不支持写入操作")
    except FileNotFoundError:
        print("文件不存在，'r'模式无法创建文件")
    
    print("\n2. 'w' 模式 - 写入模式（覆盖）：")
    with open(filename, 'w', encoding='utf-8') as f:
        print(f"打开时文件指针位置：{f.tell()}")
        f.write("新内容：覆盖原有内容\n")
        f.write("新内容：第二行\n")
        print(f"写入后文件指针位置：{f.tell()}")
        
        # 尝试读取（会失败）
        try:
            f.seek(0)
            content = f.read()
        except io.UnsupportedOperation:
            print("'w'模式不支持读取操作")
    
    # 查看覆盖后的内容
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"覆盖后的文件内容：\n{content}")
    
    print("\n3. 'a' 模式 - 追加模式：")
    with open(filename, 'a', encoding='utf-8') as f:
        print(f"打开时文件指针位置：{f.tell()}")
        f.write("追加内容：第三行\n")
        f.write("追加内容：第四行\n")
        print(f"追加后文件指针位置：{f.tell()}")
    
    # 查看追加后的内容
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"追加后的文件内容：\n{content}")
    
    print("\n4. 'x' 模式 - 独占创建模式：")
    new_filename = "exclusive_test.txt"
    
    # 首次创建（成功）
    try:
        with open(new_filename, 'x', encoding='utf-8') as f:
            f.write("独占创建的文件内容\n")
        print("成功创建新文件")
        
        # 再次创建同名文件（失败）
        try:
            with open(new_filename, 'x', encoding='utf-8') as f:
                f.write("这不会被写入")
        except FileExistsError:
            print("文件已存在，'x'模式创建失败（这是预期的行为）")
        
        os.remove(new_filename)
    except Exception as e:
        print(f"创建文件时出错：{e}")
    
    os.remove(filename)


def demonstrate_binary_modes():
    """演示二进制模式"""
    print("\n=== 二进制模式演示 ===")
    
    filename = "binary_demo.bin"
    
    print("1. 'wb' 模式 - 二进制写入：")
    # 写入二进制数据
    binary_data = b"\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64"  # "Hello World"
    numbers = bytes([1, 2, 3, 4, 5, 255, 254, 253])
    
    with open(filename, 'wb') as f:
        f.write(binary_data)
        f.write(b"\n")
        f.write(numbers)
        print(f"写入了 {len(binary_data) + 1 + len(numbers)} 字节")
    
    print("\n2. 'rb' 模式 - 二进制读取：")
    with open(filename, 'rb') as f:
        # 读取所有数据
        all_data = f.read()
        print(f"读取的二进制数据：{all_data}")
        print(f"数据长度：{len(all_data)} 字节")
        
        # 重置并分段读取
        f.seek(0)
        text_part = f.read(11)  # "Hello World"
        newline = f.read(1)     # 换行符
        number_part = f.read()  # 剩余的数字
        
        print(f"文本部分：{text_part} -> '{text_part.decode('utf-8')}'")
        print(f"换行符：{newline}")
        print(f"数字部分：{list(number_part)}")
    
    print("\n3. 'ab' 模式 - 二进制追加：")
    additional_data = b"\nAppended binary data"
    with open(filename, 'ab') as f:
        f.write(additional_data)
        print(f"追加了 {len(additional_data)} 字节")
    
    # 读取追加后的内容
    with open(filename, 'rb') as f:
        final_data = f.read()
        print(f"最终文件大小：{len(final_data)} 字节")
        print(f"最终内容：{final_data}")
    
    os.remove(filename)


def demonstrate_read_write_modes():
    """演示读写模式"""
    print("\n=== 读写模式演示 ===")
    
    filename = "readwrite_demo.txt"
    
    # 创建初始文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("初始行1\n初始行2\n初始行3\n")
    
    print("1. 'r+' 模式 - 读写模式（文件必须存在）：")
    with open(filename, 'r+', encoding='utf-8') as f:
        print(f"打开时文件指针位置：{f.tell()}")
        
        # 先读取
        content = f.read()
        print(f"读取的内容：\n{content}")
        print(f"读取后文件指针位置：{f.tell()}")
        
        # 在文件末尾写入
        f.write("r+模式追加的内容\n")
        print(f"写入后文件指针位置：{f.tell()}")
        
        # 移动到开头并覆盖部分内容
        f.seek(0)
        f.write("修改")
        print("已修改文件开头的内容")
    
    # 查看修改后的内容
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"r+模式修改后的内容：\n{content}")
    
    print("\n2. 'w+' 模式 - 读写模式（清空文件）：")
    with open(filename, 'w+', encoding='utf-8') as f:
        print(f"打开时文件指针位置：{f.tell()}")
        
        # 写入新内容
        f.write("w+模式的新内容\n第二行\n第三行\n")
        print(f"写入后文件指针位置：{f.tell()}")
        
        # 移动到开头并读取
        f.seek(0)
        content = f.read()
        print(f"读取的内容：\n{content}")
        
        # 在中间位置插入内容
        f.seek(0)
        f.readline()  # 跳过第一行
        pos = f.tell()
        print(f"第二行开始位置：{pos}")
        
        # 读取剩余内容
        remaining = f.read()
        
        # 回到第二行开始位置，插入新内容
        f.seek(pos)
        f.write("插入的新行\n")
        f.write(remaining)
    
    # 查看最终内容
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"w+模式最终内容：\n{content}")
    
    print("\n3. 'a+' 模式 - 追加读写模式：")
    with open(filename, 'a+', encoding='utf-8') as f:
        print(f"打开时文件指针位置：{f.tell()}")
        
        # 写入内容（总是在末尾）
        f.write("a+模式追加的内容\n")
        print(f"写入后文件指针位置：{f.tell()}")
        
        # 移动到开头读取
        f.seek(0)
        content = f.read()
        print(f"读取的完整内容：\n{content}")
        
        # 再次写入（仍然在末尾）
        f.write("再次追加的内容\n")
    
    # 查看最终内容
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"a+模式最终内容：\n{content}")
    
    os.remove(filename)


def demonstrate_mode_combinations():
    """演示模式组合和参数"""
    print("\n=== 模式组合和参数演示 ===")
    
    filename = "combination_demo.txt"
    
    print("1. 文本和二进制模式组合：")
    
    # 'rt' - 明确指定文本读取模式
    with open(filename, 'wt', encoding='utf-8') as f:
        f.write("文本模式写入的内容\n包含中文字符\n")
    
    with open(filename, 'rt', encoding='utf-8') as f:
        content = f.read()
        print(f"文本模式读取：\n{content}")
    
    # 'rb' - 二进制模式读取同一文件
    with open(filename, 'rb') as f:
        binary_content = f.read()
        print(f"二进制模式读取：{binary_content}")
        print(f"解码为文本：{binary_content.decode('utf-8')}")
    
    print("\n2. 缓冲区参数演示：")
    
    # 无缓冲（仅二进制模式支持）
    binary_file = "unbuffered_demo.bin"
    with open(binary_file, 'wb', buffering=0) as f:
        f.write(b"Unbuffered write")
        print("无缓冲写入完成")
    
    # 行缓冲（文本模式）
    text_file = "line_buffered_demo.txt"
    with open(text_file, 'w', buffering=1, encoding='utf-8') as f:
        f.write("Line 1\n")
        f.write("Line 2 without newline")
        print("行缓冲写入完成")
    
    # 全缓冲
    with open(text_file, 'w', buffering=8192, encoding='utf-8') as f:
        f.write("Full buffered write\n")
        print("全缓冲写入完成")
    
    print("\n3. 编码参数演示：")
    
    # UTF-8 编码
    utf8_file = "utf8_demo.txt"
    with open(utf8_file, 'w', encoding='utf-8') as f:
        f.write("UTF-8编码：你好世界！\n")
    
    # GBK 编码
    gbk_file = "gbk_demo.txt"
    try:
        with open(gbk_file, 'w', encoding='gbk') as f:
            f.write("GBK编码：你好世界！\n")
        
        # 用不同编码读取
        with open(gbk_file, 'r', encoding='gbk') as f:
            content = f.read()
            print(f"GBK编码读取：{content.strip()}")
        
        # 错误的编码读取
        try:
            with open(gbk_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError as e:
            print(f"编码错误：{e}")
    
    except UnicodeEncodeError as e:
        print(f"GBK编码不支持某些字符：{e}")
    
    # 清理文件
    for f in [filename, binary_file, text_file, utf8_file, gbk_file]:
        if os.path.exists(f):
            os.remove(f)


def demonstrate_practical_scenarios():
    """演示实际应用场景"""
    print("\n=== 实际应用场景演示 ===")
    
    print("1. 日志文件追加：")
    log_file = "application.log"
    
    # 模拟应用程序日志
    def write_log(message, level="INFO"):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {level}: {message}\n")
    
    write_log("应用程序启动")
    write_log("用户登录成功", "INFO")
    write_log("数据库连接失败", "ERROR")
    write_log("应用程序关闭")
    
    with open(log_file, 'r', encoding='utf-8') as f:
        logs = f.read()
        print(f"日志内容：\n{logs}")
    
    print("\n2. 配置文件读写：")
    config_file = "config.txt"
    
    # 写入配置
    config = {
        'database_host': 'localhost',
        'database_port': '5432',
        'debug_mode': 'True',
        'max_connections': '100'
    }
    
    with open(config_file, 'w', encoding='utf-8') as f:
        for key, value in config.items():
            f.write(f"{key}={value}\n")
    
    # 读取配置
    loaded_config = {}
    with open(config_file, 'r', encoding='utf-8') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                loaded_config[key] = value
    
    print(f"加载的配置：{loaded_config}")
    
    print("\n3. 数据文件处理：")
    data_file = "data.csv"
    
    # 写入CSV数据
    with open(data_file, 'w', encoding='utf-8') as f:
        f.write("姓名,年龄,城市\n")
        f.write("张三,25,北京\n")
        f.write("李四,30,上海\n")
        f.write("王五,28,广州\n")
    
    # 读取并处理数据
    with open(data_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        headers = lines[0].strip().split(',')
        print(f"表头：{headers}")
        
        for i, line in enumerate(lines[1:], 1):
            values = line.strip().split(',')
            record = dict(zip(headers, values))
            print(f"记录{i}：{record}")
    
    print("\n4. 临时文件处理：")
    
    # 使用临时文件
    with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8', delete=False) as temp_f:
        temp_filename = temp_f.name
        temp_f.write("临时文件内容\n")
        temp_f.write("用于临时存储数据\n")
        
        # 重置到开头读取
        temp_f.seek(0)
        content = temp_f.read()
        print(f"临时文件内容：\n{content}")
    
    print(f"临时文件路径：{temp_filename}")
    
    # 清理文件
    for f in [log_file, config_file, data_file, temp_filename]:
        if os.path.exists(f):
            os.remove(f)


def demonstrate_mode_selection_guide():
    """演示模式选择指南"""
    print("\n=== 模式选择指南 ===")
    
    scenarios = [
        {
            'scenario': '读取现有文件',
            'mode': 'r',
            'description': '文件必须存在，只能读取'
        },
        {
            'scenario': '创建新文件或覆盖现有文件',
            'mode': 'w',
            'description': '清空文件内容，只能写入'
        },
        {
            'scenario': '向文件末尾添加内容',
            'mode': 'a',
            'description': '保留原内容，在末尾追加'
        },
        {
            'scenario': '创建新文件（确保不存在）',
            'mode': 'x',
            'description': '文件存在时会失败，安全创建'
        },
        {
            'scenario': '读写现有文件',
            'mode': 'r+',
            'description': '文件必须存在，可读可写'
        },
        {
            'scenario': '创建文件并读写',
            'mode': 'w+',
            'description': '清空文件，可读可写'
        },
        {
            'scenario': '追加并读取文件',
            'mode': 'a+',
            'description': '保留内容，末尾追加，可读'
        },
        {
            'scenario': '处理二进制数据',
            'mode': 'rb/wb/ab',
            'description': '添加b后缀处理字节数据'
        },
        {
            'scenario': '处理大文件',
            'mode': 'r + 迭代器',
            'description': '逐行读取，节省内存'
        },
        {
            'scenario': '日志记录',
            'mode': 'a',
            'description': '追加模式，保留历史日志'
        }
    ]
    
    print("常见场景的模式选择：")
    print("-" * 60)
    for scenario in scenarios:
        print(f"场景：{scenario['scenario']:<20} 模式：{scenario['mode']:<10} 说明：{scenario['description']}")
    
    print("\n模式选择决策树：")
    print("1. 需要读取吗？")
    print("   ├─ 是 → 需要写入吗？")
    print("   │        ├─ 是 → 保留原内容吗？")
    print("   │        │        ├─ 是 → r+ 或 a+")
    print("   │        │        └─ 否 → w+")
    print("   │        └─ 否 → r")
    print("   └─ 否 → 需要保留原内容吗？")
    print("            ├─ 是 → a")
    print("            ├─ 否 → w")
    print("            └─ 安全创建 → x")
    
    print("\n最佳实践：")
    print("- 优先使用with语句确保文件正确关闭")
    print("- 明确指定encoding参数避免编码问题")
    print("- 处理二进制数据时使用'b'模式")
    print("- 大文件使用迭代器而不是read()")
    print("- 日志文件使用'a'模式追加")
    print("- 配置文件使用'r+'模式读写")


def main():
    """主函数：运行所有演示"""
    print("Python文件模式完整教程")
    print("=" * 50)
    
    # 导入io模块用于异常处理
    import io
    globals()['io'] = io
    
    # 运行所有演示
    demonstrate_basic_text_modes()
    demonstrate_binary_modes()
    demonstrate_read_write_modes()
    demonstrate_mode_combinations()
    demonstrate_practical_scenarios()
    demonstrate_mode_selection_guide()
    
    # 学习总结
    print("\n=== 学习总结 ===")
    print("1. 基本模式：r(读), w(写), a(追加), x(创建)")
    print("2. 读写模式：r+(读写), w+(清空读写), a+(追加读写)")
    print("3. 二进制模式：添加'b'后缀处理字节数据")
    print("4. 文本模式：添加't'后缀或默认处理文本")
    print("5. 参数：encoding(编码), buffering(缓冲)")
    
    print("\n关键要点：")
    print("- 选择合适的模式避免数据丢失")
    print("- 'w'模式会清空文件，使用需谨慎")
    print("- 'a'模式写入总是在文件末尾")
    print("- 'x'模式提供安全的文件创建")
    print("- 二进制模式处理非文本数据")


if __name__ == "__main__":
    main()