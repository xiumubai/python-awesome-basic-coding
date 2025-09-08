#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字符串索引和切片

本文件演示Python中字符串的索引和切片操作：
1. 字符串索引的基本概念
2. 正向索引和反向索引
3. 字符串切片操作
4. 切片的高级用法
5. 索引和切片的实际应用

作者：Python学习教程
日期：2024年
"""

def demonstrate_string_indexing():
    """演示字符串索引的基本概念"""
    print("=== 字符串索引 ===")
    
    sample_string = "Python"
    print(f"字符串: {sample_string}")
    print(f"长度: {len(sample_string)}")
    
    # 正向索引（从0开始）
    print("\n正向索引:")
    for i in range(len(sample_string)):
        print(f"索引 {i}: '{sample_string[i]}'")
    
    # 反向索引（从-1开始）
    print("\n反向索引:")
    for i in range(-1, -len(sample_string)-1, -1):
        print(f"索引 {i}: '{sample_string[i]}'")
    
    # 索引对应关系
    print("\n索引对应关系:")
    print("字符:  ", end="")
    for char in sample_string:
        print(f"{char:>3}", end="")
    print()
    
    print("正向:  ", end="")
    for i in range(len(sample_string)):
        print(f"{i:>3}", end="")
    print()
    
    print("反向:  ", end="")
    for i in range(-len(sample_string), 0):
        print(f"{i:>3}", end="")
    print()

def demonstrate_index_errors():
    """演示索引错误和边界情况"""
    print("\n=== 索引错误处理 ===")
    
    text = "Hello"
    print(f"字符串: {text}")
    print(f"有效索引范围: 0 到 {len(text)-1} 或 -{len(text)} 到 -1")
    
    # 有效索引
    print(f"\n有效索引示例:")
    print(f"text[0] = '{text[0]}'")
    print(f"text[4] = '{text[4]}'")
    print(f"text[-1] = '{text[-1]}'")
    print(f"text[-5] = '{text[-5]}'")
    
    # 无效索引会引发错误
    print("\n无效索引示例:")
    invalid_indices = [5, -6, 10]
    
    for index in invalid_indices:
        try:
            result = text[index]
            print(f"text[{index}] = '{result}'")
        except IndexError as e:
            print(f"text[{index}] -> 错误: {e}")

def demonstrate_basic_slicing():
    """演示基本的字符串切片"""
    print("\n=== 基本字符串切片 ===")
    
    text = "Programming"
    print(f"字符串: {text}")
    print(f"长度: {len(text)}")
    
    # 基本切片语法: string[start:end]
    print("\n基本切片 [start:end]:")
    print(f"text[0:4] = '{text[0:4]}'  # 从索引0到3")
    print(f"text[2:7] = '{text[2:7]}'  # 从索引2到6")
    print(f"text[4:11] = '{text[4:11]}'  # 从索引4到10")
    
    # 省略开始或结束索引
    print("\n省略索引:")
    print(f"text[:4] = '{text[:4]}'    # 从开始到索引3")
    print(f"text[4:] = '{text[4:]}'    # 从索引4到结束")
    print(f"text[:] = '{text[:]}'      # 完整字符串")
    
    # 使用负数索引
    print("\n负数索引切片:")
    print(f"text[-4:] = '{text[-4:]}'   # 最后4个字符")
    print(f"text[:-4] = '{text[:-4]}'   # 除了最后4个字符")
    print(f"text[-7:-2] = '{text[-7:-2]}' # 从倒数第7到倒数第3")

def demonstrate_advanced_slicing():
    """演示高级切片操作"""
    print("\n=== 高级切片操作 ===")
    
    text = "abcdefghijk"
    print(f"字符串: {text}")
    
    # 带步长的切片: string[start:end:step]
    print("\n带步长的切片 [start:end:step]:")
    print(f"text[::2] = '{text[::2]}'     # 每隔一个字符")
    print(f"text[1::2] = '{text[1::2]}'   # 从索引1开始，每隔一个")
    print(f"text[::3] = '{text[::3]}'     # 每隔两个字符")
    
    # 反向切片
    print("\n反向切片:")
    print(f"text[::-1] = '{text[::-1]}'   # 反转字符串")
    print(f"text[::-2] = '{text[::-2]}'   # 反向每隔一个")
    print(f"text[8:2:-1] = '{text[8:2:-1]}' # 从索引8到3反向")
    
    # 复杂切片示例
    print("\n复杂切片示例:")
    print(f"text[2:8:2] = '{text[2:8:2]}'  # 从索引2到7，步长2")
    print(f"text[7:1:-2] = '{text[7:1:-2]}' # 从索引7到2，反向步长2")

def demonstrate_slicing_edge_cases():
    """演示切片的边界情况"""
    print("\n=== 切片边界情况 ===")
    
    text = "Python"
    print(f"字符串: {text}")
    
    # 超出范围的切片不会报错
    print("\n超出范围的切片:")
    print(f"text[2:100] = '{text[2:100]}'  # 结束索引超出范围")
    print(f"text[-100:4] = '{text[-100:4]}' # 开始索引超出范围")
    print(f"text[100:200] = '{text[100:200]}' # 都超出范围")
    
    # 开始索引大于结束索引
    print("\n开始索引大于结束索引:")
    print(f"text[4:2] = '{text[4:2]}'      # 返回空字符串")
    print(f"text[5:1] = '{text[5:1]}'      # 返回空字符串")
    
    # 步长为0会报错
    print("\n步长为0的情况:")
    try:
        result = text[::0]
        print(f"text[::0] = '{result}'")
    except ValueError as e:
        print(f"text[::0] -> 错误: {e}")

def demonstrate_practical_applications():
    """演示索引和切片的实际应用"""
    print("\n=== 实际应用示例 ===")
    
    # 1. 获取文件扩展名
    filename = "document.pdf"
    extension = filename[filename.rfind('.'):]
    print(f"文件名: {filename}")
    print(f"扩展名: {extension}")
    
    # 2. 获取文件名（不含扩展名）
    name_only = filename[:filename.rfind('.')]
    print(f"文件名（无扩展名）: {name_only}")
    
    # 3. 提取域名
    email = "user@example.com"
    domain = email[email.find('@')+1:]
    username = email[:email.find('@')]
    print(f"\n邮箱: {email}")
    print(f"用户名: {username}")
    print(f"域名: {domain}")
    
    # 4. 字符串反转
    original = "Hello World"
    reversed_str = original[::-1]
    print(f"\n原字符串: {original}")
    print(f"反转后: {reversed_str}")
    
    # 5. 获取字符串的前几个和后几个字符
    text = "Programming is fun"
    first_5 = text[:5]
    last_5 = text[-5:]
    middle = text[5:-5]
    print(f"\n原字符串: {text}")
    print(f"前5个字符: '{first_5}'")
    print(f"后5个字符: '{last_5}'")
    print(f"中间部分: '{middle}'")
    
    # 6. 每隔n个字符提取
    data = "a1b2c3d4e5f6g7h8"
    letters = data[::2]  # 提取字母
    numbers = data[1::2]  # 提取数字
    print(f"\n原数据: {data}")
    print(f"字母: {letters}")
    print(f"数字: {numbers}")

def demonstrate_string_slicing_methods():
    """演示字符串切片的不同方法"""
    print("\n=== 字符串切片方法对比 ===")
    
    text = "Hello, World!"
    print(f"原字符串: {text}")
    
    # 方法1: 直接切片
    result1 = text[7:12]
    print(f"直接切片 text[7:12]: '{result1}'")
    
    # 方法2: 使用变量
    start = 7
    end = 12
    result2 = text[start:end]
    print(f"使用变量 text[{start}:{end}]: '{result2}'")
    
    # 方法3: 动态计算索引
    comma_pos = text.find(',')
    result3 = text[comma_pos+2:comma_pos+7]
    print(f"动态索引: '{result3}'")
    
    # 方法4: 结合字符串方法
    words = text.split()
    second_word = words[1]
    # 去掉标点符号
    clean_word = second_word[:-1] if second_word[-1] in '!.,;' else second_word
    print(f"结合split方法: '{clean_word}'")

def main():
    """主函数，演示所有字符串索引和切片概念"""
    print("Python字符串索引和切片")
    print("=" * 50)
    
    demonstrate_string_indexing()
    demonstrate_index_errors()
    demonstrate_basic_slicing()
    demonstrate_advanced_slicing()
    demonstrate_slicing_edge_cases()
    demonstrate_practical_applications()
    demonstrate_string_slicing_methods()
    
    print("\n=== 总结 ===")
    print("1. 字符串索引从0开始，支持负数索引")
    print("2. 切片语法: string[start:end:step]")
    print("3. 切片不会引发索引错误，会自动处理边界")
    print("4. 反向切片使用负数步长")
    print("5. 切片创建新的字符串对象")
    print("6. 索引和切片在字符串处理中应用广泛")

if __name__ == "__main__":
    main()