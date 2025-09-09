#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件写入方法演示

本模块演示Python中各种文件写入方法的使用：
1. write() - 写入字符串
2. writelines() - 写入字符串列表
3. 不同写入模式的区别
4. 格式化写入
5. 缓冲区和刷新
6. 写入性能对比

学习要点：
- 掌握write()和writelines()的使用
- 理解不同写入模式的区别
- 学会处理写入缓冲区
- 了解写入性能优化
"""

import os
import time
from datetime import datetime


def demonstrate_write_method():
    """演示write()方法的使用"""
    print("=== write()方法演示 ===")
    
    filename = "write_demo.txt"
    
    # 1. 基本写入
    print("1. 基本写入操作：")
    with open(filename, 'w', encoding='utf-8') as f:
        # write()返回写入的字符数
        chars_written = f.write("Hello, Python文件操作！\n")
        print(f"写入了 {chars_written} 个字符")
        
        # 继续写入
        f.write("这是第二行内容\n")
        f.write("这是第三行内容")
    
    # 读取并显示写入的内容
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"写入的内容：\n{content}")
    
    # 2. 追加写入
    print("\n2. 追加写入操作：")
    with open(filename, 'a', encoding='utf-8') as f:
        f.write("\n这是追加的第四行")
        f.write("\n这是追加的第五行")
    
    # 读取并显示追加后的内容
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"追加后的内容：\n{content}")
    
    os.remove(filename)


def demonstrate_writelines_method():
    """演示writelines()方法的使用"""
    print("\n=== writelines()方法演示 ===")
    
    filename = "writelines_demo.txt"
    
    # 1. 写入字符串列表
    print("1. 写入字符串列表：")
    lines = [
        "第一行：Python文件写入\n",
        "第二行：writelines()方法\n",
        "第三行：处理多行数据\n",
        "第四行：非常方便\n"
    ]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
        print(f"写入了 {len(lines)} 行数据")
    
    # 读取并显示
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"写入的内容：\n{content}")
    
    # 2. 注意：writelines()不会自动添加换行符
    print("\n2. writelines()不自动添加换行符的演示：")
    lines_no_newline = ["行1", "行2", "行3", "行4"]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines_no_newline)
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"没有换行符的结果：'{content}'")
    
    # 3. 正确的方式：手动添加换行符
    print("\n3. 正确添加换行符：")
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines([line + '\n' for line in lines_no_newline])
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"正确格式的结果：\n{content}")
    
    os.remove(filename)


def demonstrate_write_modes():
    """演示不同写入模式的区别"""
    print("\n=== 不同写入模式演示 ===")
    
    filename = "modes_demo.txt"
    
    # 创建初始文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("初始内容：第一行\n初始内容：第二行\n")
    
    print("1. 初始文件内容：")
    with open(filename, 'r', encoding='utf-8') as f:
        print(f"'{f.read()}'")
    
    # 'w' 模式：覆盖写入
    print("\n2. 'w'模式 - 覆盖写入：")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("覆盖后的新内容\n")
    
    with open(filename, 'r', encoding='utf-8') as f:
        print(f"'{f.read()}'")
    
    # 'a' 模式：追加写入
    print("\n3. 'a'模式 - 追加写入：")
    with open(filename, 'a', encoding='utf-8') as f:
        f.write("追加的内容\n")
    
    with open(filename, 'r', encoding='utf-8') as f:
        print(f"'{f.read()}'")
    
    # 'x' 模式：独占创建（文件不存在时创建）
    print("\n4. 'x'模式 - 独占创建：")
    new_filename = "exclusive_demo.txt"
    try:
        with open(new_filename, 'x', encoding='utf-8') as f:
            f.write("独占创建的文件内容\n")
        print("成功创建新文件")
        
        # 再次尝试创建同名文件（会失败）
        try:
            with open(new_filename, 'x', encoding='utf-8') as f:
                f.write("这不会被写入")
        except FileExistsError:
            print("文件已存在，'x'模式创建失败（这是正常的）")
        
        os.remove(new_filename)
    except Exception as e:
        print(f"创建文件时出错：{e}")
    
    os.remove(filename)


def demonstrate_formatted_writing():
    """演示格式化写入"""
    print("\n=== 格式化写入演示 ===")
    
    filename = "formatted_demo.txt"
    
    # 1. 使用字符串格式化
    print("1. 字符串格式化写入：")
    data = {
        'name': '张三',
        'age': 25,
        'score': 95.5,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        # 使用format()方法
        f.write("学生信息报告\n")
        f.write("=" * 20 + "\n")
        f.write("姓名：{}\n".format(data['name']))
        f.write("年龄：{}岁\n".format(data['age']))
        f.write("成绩：{:.1f}分\n".format(data['score']))
        f.write("记录时间：{}\n".format(data['date']))
        
        # 使用f-string（推荐）
        f.write("\n--- 使用f-string格式化 ---\n")
        f.write(f"学生{data['name']}今年{data['age']}岁，")
        f.write(f"考试成绩为{data['score']:.1f}分\n")
    
    # 读取并显示
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"格式化写入的内容：\n{content}")
    
    # 2. 写入表格数据
    print("\n2. 表格数据写入：")
    students = [
        {'name': '张三', 'math': 95, 'english': 87, 'science': 92},
        {'name': '李四', 'math': 88, 'english': 94, 'science': 89},
        {'name': '王五', 'math': 92, 'english': 91, 'science': 95}
    ]
    
    with open(filename, 'w', encoding='utf-8') as f:
        # 写入表头
        f.write(f"{'姓名':<8} {'数学':<6} {'英语':<6} {'科学':<6} {'平均分':<8}\n")
        f.write("-" * 40 + "\n")
        
        # 写入数据行
        for student in students:
            avg = (student['math'] + student['english'] + student['science']) / 3
            f.write(f"{student['name']:<8} {student['math']:<6} {student['english']:<6} {student['science']:<6} {avg:<8.1f}\n")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"表格数据：\n{content}")
    
    os.remove(filename)


def demonstrate_buffer_and_flush():
    """演示缓冲区和刷新操作"""
    print("\n=== 缓冲区和刷新演示 ===")
    
    filename = "buffer_demo.txt"
    
    print("1. 缓冲区写入演示：")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("第一行数据\n")
        print("已写入第一行，但可能还在缓冲区中")
        
        # 手动刷新缓冲区
        f.flush()
        print("已刷新缓冲区，数据确保写入磁盘")
        
        f.write("第二行数据\n")
        print("写入第二行，等待3秒...")
        time.sleep(3)
        
        f.write("第三行数据\n")
        print("写入第三行，文件关闭时会自动刷新")
    
    # 读取并显示最终内容
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"最终文件内容：\n{content}")
    
    # 2. 实时写入演示
    print("\n2. 实时写入日志演示：")
    log_filename = "realtime_log.txt"
    
    with open(log_filename, 'w', encoding='utf-8') as f:
        for i in range(5):
            timestamp = datetime.now().strftime('%H:%M:%S')
            log_entry = f"[{timestamp}] 处理任务 {i+1}\n"
            f.write(log_entry)
            f.flush()  # 立即刷新，确保实时写入
            print(f"写入日志：{log_entry.strip()}")
            time.sleep(1)
    
    with open(log_filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"\n日志文件内容：\n{content}")
    
    os.remove(filename)
    os.remove(log_filename)


def demonstrate_write_performance():
    """演示写入性能对比"""
    print("\n=== 写入性能对比 ===")
    
    # 准备测试数据
    lines = [f"这是第{i+1}行测试数据\n" for i in range(10000)]
    
    # 方法1：逐行写入
    print("1. 逐行写入性能测试：")
    filename1 = "performance_test1.txt"
    start_time = time.time()
    
    with open(filename1, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
    
    time1 = time.time() - start_time
    print(f"逐行写入耗时: {time1:.4f}秒")
    
    # 方法2：批量写入（writelines）
    print("\n2. 批量写入性能测试：")
    filename2 = "performance_test2.txt"
    start_time = time.time()
    
    with open(filename2, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    time2 = time.time() - start_time
    print(f"批量写入耗时: {time2:.4f}秒")
    
    # 方法3：拼接后一次写入
    print("\n3. 拼接后一次写入性能测试：")
    filename3 = "performance_test3.txt"
    start_time = time.time()
    
    content = ''.join(lines)
    with open(filename3, 'w', encoding='utf-8') as f:
        f.write(content)
    
    time3 = time.time() - start_time
    print(f"拼接写入耗时: {time3:.4f}秒")
    
    # 性能对比
    print("\n性能对比结果：")
    fastest = min(time1, time2, time3)
    print(f"逐行写入: {time1:.4f}秒 (慢 {time1/fastest:.1f}倍)")
    print(f"批量写入: {time2:.4f}秒 (慢 {time2/fastest:.1f}倍)")
    print(f"拼接写入: {time3:.4f}秒 (慢 {time3/fastest:.1f}倍)")
    
    # 验证文件大小一致
    size1 = os.path.getsize(filename1)
    size2 = os.path.getsize(filename2)
    size3 = os.path.getsize(filename3)
    print(f"\n文件大小验证: {size1} = {size2} = {size3} 字节")
    
    # 清理文件
    os.remove(filename1)
    os.remove(filename2)
    os.remove(filename3)


def main():
    """主函数：运行所有演示"""
    print("Python文件写入方法完整教程")
    print("=" * 50)
    
    # 运行所有演示
    demonstrate_write_method()
    demonstrate_writelines_method()
    demonstrate_write_modes()
    demonstrate_formatted_writing()
    demonstrate_buffer_and_flush()
    demonstrate_write_performance()
    
    # 学习总结
    print("\n=== 学习总结 ===")
    print("1. write() - 写入单个字符串，返回写入字符数")
    print("2. writelines() - 写入字符串列表，不自动添加换行符")
    print("3. 写入模式：'w'覆盖，'a'追加，'x'独占创建")
    print("4. 使用f-string进行格式化写入")
    print("5. flush()可以强制刷新缓冲区")
    print("6. 批量写入比逐行写入性能更好")
    
    print("\n最佳实践：")
    print("- 大量数据使用writelines()或拼接后write()")
    print("- 实时日志需要及时flush()")
    print("- 使用with语句确保文件正确关闭")
    print("- 选择合适的写入模式避免数据丢失")


if __name__ == "__main__":
    main()