#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
输入输出综合练习题

学习目标：
1. 综合运用输入输出的各种技巧
2. 解决实际问题中的IO需求
3. 提高代码的健壮性和用户体验
4. 掌握错误处理和数据验证
5. 学会设计用户友好的交互界面

作者：Python基础教程
日期：2024年
"""

import os
import json
import csv
import time
import datetime
import random
from pathlib import Path

# ============================================================================
# 练习1：学生成绩管理系统
# ============================================================================

print("=" * 60)
print("练习1：学生成绩管理系统")
print("=" * 60)

class StudentManager:
    """
    学生成绩管理系统
    功能：添加学生、录入成绩、查询统计、导出数据
    """
    
    def __init__(self):
        self.students = []
        self.data_file = "students_data.json"
        self.load_data()
    
    def load_data(self):
        """从文件加载数据"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.students = json.load(f)
                print(f"已加载 {len(self.students)} 名学生的数据")
            else:
                print("数据文件不存在，将创建新的数据文件")
        except Exception as e:
            print(f"加载数据失败：{e}")
            self.students = []
    
    def save_data(self):
        """保存数据到文件"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.students, f, ensure_ascii=False, indent=2)
            print("数据保存成功")
        except Exception as e:
            print(f"保存数据失败：{e}")
    
    def add_student(self):
        """添加学生"""
        print("\n--- 添加学生 ---")
        
        while True:
            name = input("请输入学生姓名（输入'q'退出）：").strip()
            if name.lower() == 'q':
                return
            if name:
                break
            print("姓名不能为空，请重新输入")
        
        # 检查是否已存在
        for student in self.students:
            if student['name'] == name:
                print(f"学生 '{name}' 已存在")
                return
        
        # 输入年龄
        while True:
            try:
                age = int(input("请输入年龄："))
                if 1 <= age <= 150:
                    break
                else:
                    print("年龄应在1-150之间")
            except ValueError:
                print("请输入有效的数字")
        
        # 输入班级
        class_name = input("请输入班级：").strip() or "未分班"
        
        # 创建学生记录
        student = {
            'name': name,
            'age': age,
            'class': class_name,
            'scores': {},
            'created_time': datetime.datetime.now().isoformat()
        }
        
        self.students.append(student)
        print(f"学生 '{name}' 添加成功")
        self.save_data()
    
    def add_score(self):
        """录入成绩"""
        print("\n--- 录入成绩 ---")
        
        if not self.students:
            print("暂无学生数据，请先添加学生")
            return
        
        # 显示学生列表
        print("学生列表：")
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student['name']} ({student['class']})")
        
        # 选择学生
        while True:
            try:
                choice = int(input("请选择学生编号：")) - 1
                if 0 <= choice < len(self.students):
                    selected_student = self.students[choice]
                    break
                else:
                    print(f"请输入1-{len(self.students)}之间的数字")
            except ValueError:
                print("请输入有效的数字")
        
        print(f"为学生 '{selected_student['name']}' 录入成绩")
        
        # 输入科目
        subject = input("请输入科目名称：").strip()
        if not subject:
            print("科目名称不能为空")
            return
        
        # 输入成绩
        while True:
            try:
                score = float(input(f"请输入{subject}成绩（0-100）："))
                if 0 <= score <= 100:
                    break
                else:
                    print("成绩应在0-100之间")
            except ValueError:
                print("请输入有效的数字")
        
        # 保存成绩
        selected_student['scores'][subject] = score
        print(f"成绩录入成功：{selected_student['name']} - {subject}: {score}")
        self.save_data()
    
    def query_student(self):
        """查询学生信息"""
        print("\n--- 查询学生 ---")
        
        if not self.students:
            print("暂无学生数据")
            return
        
        name = input("请输入要查询的学生姓名：").strip()
        
        found_students = [s for s in self.students if name.lower() in s['name'].lower()]
        
        if not found_students:
            print(f"未找到包含 '{name}' 的学生")
            return
        
        for student in found_students:
            print(f"\n学生信息：")
            print(f"  姓名：{student['name']}")
            print(f"  年龄：{student['age']}")
            print(f"  班级：{student['class']}")
            print(f"  成绩：")
            
            if student['scores']:
                total_score = 0
                for subject, score in student['scores'].items():
                    print(f"    {subject}: {score}")
                    total_score += score
                
                avg_score = total_score / len(student['scores'])
                print(f"  平均分：{avg_score:.1f}")
            else:
                print("    暂无成绩记录")
    
    def statistics(self):
        """统计信息"""
        print("\n--- 统计信息 ---")
        
        if not self.students:
            print("暂无学生数据")
            return
        
        print(f"学生总数：{len(self.students)}")
        
        # 按班级统计
        class_count = {}
        for student in self.students:
            class_name = student['class']
            class_count[class_name] = class_count.get(class_name, 0) + 1
        
        print("\n班级分布：")
        for class_name, count in class_count.items():
            print(f"  {class_name}: {count}人")
        
        # 成绩统计
        all_scores = {}
        for student in self.students:
            for subject, score in student['scores'].items():
                if subject not in all_scores:
                    all_scores[subject] = []
                all_scores[subject].append(score)
        
        if all_scores:
            print("\n各科成绩统计：")
            for subject, scores in all_scores.items():
                avg_score = sum(scores) / len(scores)
                max_score = max(scores)
                min_score = min(scores)
                print(f"  {subject}: 平均{avg_score:.1f}, 最高{max_score}, 最低{min_score} ({len(scores)}人)")
    
    def export_data(self):
        """导出数据"""
        print("\n--- 导出数据 ---")
        
        if not self.students:
            print("暂无数据可导出")
            return
        
        print("选择导出格式：")
        print("1. CSV格式")
        print("2. 文本报告")
        print("3. JSON格式")
        
        while True:
            try:
                choice = int(input("请选择（1-3）："))
                if choice in [1, 2, 3]:
                    break
                else:
                    print("请输入1-3之间的数字")
            except ValueError:
                print("请输入有效的数字")
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if choice == 1:
            # CSV导出
            filename = f"students_export_{timestamp}.csv"
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # 获取所有科目
                all_subjects = set()
                for student in self.students:
                    all_subjects.update(student['scores'].keys())
                all_subjects = sorted(all_subjects)
                
                # 写入表头
                header = ['姓名', '年龄', '班级'] + all_subjects + ['平均分']
                writer.writerow(header)
                
                # 写入数据
                for student in self.students:
                    row = [student['name'], student['age'], student['class']]
                    
                    scores = []
                    for subject in all_subjects:
                        score = student['scores'].get(subject, '')
                        row.append(score)
                        if score:
                            scores.append(score)
                    
                    # 计算平均分
                    avg_score = sum(scores) / len(scores) if scores else ''
                    if avg_score:
                        avg_score = f"{avg_score:.1f}"
                    row.append(avg_score)
                    
                    writer.writerow(row)
            
            print(f"CSV文件导出成功：{filename}")
        
        elif choice == 2:
            # 文本报告
            filename = f"students_report_{timestamp}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("学生成绩报告\n")
                f.write("=" * 40 + "\n")
                f.write(f"生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"学生总数：{len(self.students)}\n\n")
                
                for i, student in enumerate(self.students, 1):
                    f.write(f"{i}. {student['name']}\n")
                    f.write(f"   年龄：{student['age']}\n")
                    f.write(f"   班级：{student['class']}\n")
                    f.write(f"   成绩：")
                    
                    if student['scores']:
                        f.write("\n")
                        total_score = 0
                        for subject, score in student['scores'].items():
                            f.write(f"     {subject}: {score}\n")
                            total_score += score
                        
                        avg_score = total_score / len(student['scores'])
                        f.write(f"   平均分：{avg_score:.1f}\n")
                    else:
                        f.write(" 暂无\n")
                    
                    f.write("\n")
            
            print(f"文本报告导出成功：{filename}")
        
        elif choice == 3:
            # JSON导出
            filename = f"students_backup_{timestamp}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                export_data = {
                    'export_time': datetime.datetime.now().isoformat(),
                    'total_students': len(self.students),
                    'students': self.students
                }
                json.dump(export_data, f, ensure_ascii=False, indent=2)
            
            print(f"JSON文件导出成功：{filename}")
    
    def run(self):
        """运行主程序"""
        print("欢迎使用学生成绩管理系统")
        
        while True:
            print("\n" + "=" * 30)
            print("1. 添加学生")
            print("2. 录入成绩")
            print("3. 查询学生")
            print("4. 统计信息")
            print("5. 导出数据")
            print("0. 退出系统")
            print("=" * 30)
            
            try:
                choice = input("请选择操作（0-5）：").strip()
                
                if choice == '1':
                    self.add_student()
                elif choice == '2':
                    self.add_score()
                elif choice == '3':
                    self.query_student()
                elif choice == '4':
                    self.statistics()
                elif choice == '5':
                    self.export_data()
                elif choice == '0':
                    print("感谢使用，再见！")
                    break
                else:
                    print("无效选择，请重新输入")
            
            except KeyboardInterrupt:
                print("\n\n程序被用户中断")
                break
            except Exception as e:
                print(f"发生错误：{e}")

# 演示学生管理系统
print("\n--- 学生管理系统演示 ---")
print("提示：这是一个完整的学生成绩管理系统")
print("功能包括：添加学生、录入成绩、查询统计、数据导出")
print("在实际使用中，可以运行 manager.run() 来启动交互界面")

# 创建示例数据
manager = StudentManager()

# 添加示例学生（如果没有数据的话）
if not manager.students:
    sample_students = [
        {'name': '张三', 'age': 18, 'class': '高三1班', 'scores': {'数学': 85, '英语': 92, '物理': 78}, 'created_time': datetime.datetime.now().isoformat()},
        {'name': '李四', 'age': 17, 'class': '高三1班', 'scores': {'数学': 92, '英语': 88, '物理': 95}, 'created_time': datetime.datetime.now().isoformat()},
        {'name': '王五', 'age': 18, 'class': '高三2班', 'scores': {'数学': 78, '英语': 85, '物理': 82}, 'created_time': datetime.datetime.now().isoformat()}
    ]
    
    manager.students = sample_students
    manager.save_data()
    print("已创建示例数据")

# 显示统计信息
manager.statistics()

# ============================================================================
# 练习2：文件批处理工具
# ============================================================================

print("\n" + "=" * 60)
print("练习2：文件批处理工具")
print("=" * 60)

class FileBatchProcessor:
    """
    文件批处理工具
    功能：批量重命名、格式转换、内容处理
    """
    
    def __init__(self):
        self.processed_files = []
        self.log_file = "batch_process.log"
    
    def log_operation(self, message):
        """记录操作日志"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"写入日志失败：{e}")
        
        print(message)
    
    def create_test_files(self, count=5):
        """创建测试文件"""
        print("\n--- 创建测试文件 ---")
        
        test_dir = "test_files"
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)
        
        for i in range(count):
            filename = f"{test_dir}/test_file_{i+1:02d}.txt"
            content = f"这是测试文件 {i+1}\n" + \
                     f"创建时间：{datetime.datetime.now()}\n" + \
                     f"文件编号：{i+1:03d}\n" + \
                     f"随机数：{random.randint(1000, 9999)}\n"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        
        self.log_operation(f"创建了 {count} 个测试文件")
        return test_dir
    
    def batch_rename(self, directory, pattern, replacement):
        """批量重命名文件"""
        print(f"\n--- 批量重命名：{pattern} -> {replacement} ---")
        
        if not os.path.exists(directory):
            self.log_operation(f"目录不存在：{directory}")
            return
        
        renamed_count = 0
        
        for filename in os.listdir(directory):
            if pattern in filename:
                old_path = os.path.join(directory, filename)
                new_filename = filename.replace(pattern, replacement)
                new_path = os.path.join(directory, new_filename)
                
                try:
                    os.rename(old_path, new_path)
                    self.log_operation(f"重命名：{filename} -> {new_filename}")
                    renamed_count += 1
                except Exception as e:
                    self.log_operation(f"重命名失败 {filename}：{e}")
        
        self.log_operation(f"批量重命名完成，共处理 {renamed_count} 个文件")
    
    def batch_convert_encoding(self, directory, from_encoding='gbk', to_encoding='utf-8'):
        """批量转换文件编码"""
        print(f"\n--- 批量转换编码：{from_encoding} -> {to_encoding} ---")
        
        if not os.path.exists(directory):
            self.log_operation(f"目录不存在：{directory}")
            return
        
        converted_count = 0
        
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory, filename)
                
                try:
                    # 读取原文件
                    with open(file_path, 'r', encoding=from_encoding) as f:
                        content = f.read()
                    
                    # 写入新编码
                    with open(file_path, 'w', encoding=to_encoding) as f:
                        f.write(content)
                    
                    self.log_operation(f"转换编码：{filename}")
                    converted_count += 1
                    
                except UnicodeDecodeError:
                    # 如果不是指定编码，尝试其他编码
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        self.log_operation(f"文件 {filename} 已是UTF-8编码")
                    except Exception as e:
                        self.log_operation(f"编码转换失败 {filename}：{e}")
                
                except Exception as e:
                    self.log_operation(f"处理文件失败 {filename}：{e}")
        
        self.log_operation(f"编码转换完成，共处理 {converted_count} 个文件")
    
    def batch_add_header(self, directory, header_text):
        """批量添加文件头"""
        print(f"\n--- 批量添加文件头 ---")
        
        if not os.path.exists(directory):
            self.log_operation(f"目录不存在：{directory}")
            return
        
        processed_count = 0
        
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory, filename)
                
                try:
                    # 读取原内容
                    with open(file_path, 'r', encoding='utf-8') as f:
                        original_content = f.read()
                    
                    # 检查是否已有头部
                    if not original_content.startswith(header_text):
                        # 添加头部
                        new_content = header_text + "\n" + "=" * 40 + "\n" + original_content
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        self.log_operation(f"添加文件头：{filename}")
                        processed_count += 1
                    else:
                        self.log_operation(f"文件头已存在：{filename}")
                
                except Exception as e:
                    self.log_operation(f"处理文件失败 {filename}：{e}")
        
        self.log_operation(f"添加文件头完成，共处理 {processed_count} 个文件")
    
    def generate_file_report(self, directory):
        """生成文件报告"""
        print(f"\n--- 生成文件报告 ---")
        
        if not os.path.exists(directory):
            self.log_operation(f"目录不存在：{directory}")
            return
        
        report_file = f"file_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("文件处理报告\n")
            f.write("=" * 50 + "\n")
            f.write(f"生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"目标目录：{directory}\n\n")
            
            files = os.listdir(directory)
            f.write(f"文件总数：{len(files)}\n\n")
            
            f.write("文件详情：\n")
            f.write("-" * 50 + "\n")
            
            total_size = 0
            for filename in sorted(files):
                file_path = os.path.join(directory, filename)
                if os.path.isfile(file_path):
                    size = os.path.getsize(file_path)
                    total_size += size
                    
                    # 获取修改时间
                    mtime = os.path.getmtime(file_path)
                    mtime_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
                    
                    f.write(f"{filename:<30} {size:>8} 字节  {mtime_str}\n")
            
            f.write("-" * 50 + "\n")
            f.write(f"总大小：{total_size:,} 字节\n")
        
        self.log_operation(f"文件报告生成完成：{report_file}")
        return report_file

# 演示文件批处理工具
print("\n--- 文件批处理工具演示 ---")
processor = FileBatchProcessor()

# 创建测试文件
test_dir = processor.create_test_files(3)

# 批量重命名
processor.batch_rename(test_dir, "test_file", "processed_file")

# 添加文件头
header = "# 处理后的文件\n# 批处理工具生成"
processor.batch_add_header(test_dir, header)

# 生成报告
report_file = processor.generate_file_report(test_dir)

# 显示报告内容
if os.path.exists(report_file):
    print(f"\n--- 报告内容 ---")
    with open(report_file, 'r', encoding='utf-8') as f:
        print(f.read())

# ============================================================================
# 练习3：日志分析器
# ============================================================================

print("\n" + "=" * 60)
print("练习3：日志分析器")
print("=" * 60)

class LogAnalyzer:
    """
    日志分析器
    功能：解析日志文件、统计分析、生成报告
    """
    
    def __init__(self):
        self.log_entries = []
        self.stats = {
            'total_lines': 0,
            'error_count': 0,
            'warning_count': 0,
            'info_count': 0,
            'debug_count': 0,
            'ip_addresses': {},
            'status_codes': {},
            'hourly_stats': {}
        }
    
    def create_sample_log(self, filename="sample.log", lines=100):
        """创建示例日志文件"""
        print(f"\n--- 创建示例日志文件 ---")
        
        log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']
        ip_addresses = ['192.168.1.100', '192.168.1.101', '10.0.0.50', '172.16.0.10']
        status_codes = [200, 404, 500, 301, 403]
        
        with open(filename, 'w', encoding='utf-8') as f:
            for i in range(lines):
                # 生成时间戳
                timestamp = datetime.datetime.now() - datetime.timedelta(
                    hours=random.randint(0, 24),
                    minutes=random.randint(0, 59),
                    seconds=random.randint(0, 59)
                )
                
                # 随机选择日志级别
                level = random.choice(log_levels)
                
                # 随机选择IP地址
                ip = random.choice(ip_addresses)
                
                # 随机选择状态码
                status = random.choice(status_codes)
                
                # 生成日志消息
                messages = {
                    'INFO': [
                        f"用户登录成功 - IP: {ip}",
                        f"页面访问 - 状态码: {status}",
                        "系统启动完成",
                        "定时任务执行成功"
                    ],
                    'WARNING': [
                        f"登录尝试失败 - IP: {ip}",
                        "内存使用率较高",
                        "磁盘空间不足",
                        "网络连接不稳定"
                    ],
                    'ERROR': [
                        f"数据库连接失败 - IP: {ip}",
                        f"HTTP错误 {status}",
                        "文件读取失败",
                        "服务器内部错误"
                    ],
                    'DEBUG': [
                        f"调试信息 - 处理请求 {ip}",
                        "变量值检查",
                        "函数调用跟踪",
                        "性能监控数据"
                    ]
                }
                
                message = random.choice(messages[level])
                
                # 写入日志行
                log_line = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} [{level}] {message}\n"
                f.write(log_line)
        
        print(f"示例日志文件创建完成：{filename} ({lines} 行)")
        return filename
    
    def parse_log_file(self, filename):
        """解析日志文件"""
        print(f"\n--- 解析日志文件：{filename} ---")
        
        if not os.path.exists(filename):
            print(f"文件不存在：{filename}")
            return
        
        self.log_entries = []
        self.stats = {
            'total_lines': 0,
            'error_count': 0,
            'warning_count': 0,
            'info_count': 0,
            'debug_count': 0,
            'ip_addresses': {},
            'status_codes': {},
            'hourly_stats': {}
        }
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    
                    self.stats['total_lines'] += 1
                    
                    # 解析日志级别
                    if '[ERROR]' in line:
                        self.stats['error_count'] += 1
                    elif '[WARNING]' in line:
                        self.stats['warning_count'] += 1
                    elif '[INFO]' in line:
                        self.stats['info_count'] += 1
                    elif '[DEBUG]' in line:
                        self.stats['debug_count'] += 1
                    
                    # 提取IP地址
                    import re
                    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
                    ip_matches = re.findall(ip_pattern, line)
                    for ip in ip_matches:
                        self.stats['ip_addresses'][ip] = self.stats['ip_addresses'].get(ip, 0) + 1
                    
                    # 提取状态码
                    status_pattern = r'状态码: (\d{3})'
                    status_matches = re.findall(status_pattern, line)
                    for status in status_matches:
                        self.stats['status_codes'][status] = self.stats['status_codes'].get(status, 0) + 1
                    
                    # 提取时间信息（按小时统计）
                    time_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}):\d{2}:\d{2}'
                    time_matches = re.findall(time_pattern, line)
                    for time_hour in time_matches:
                        self.stats['hourly_stats'][time_hour] = self.stats['hourly_stats'].get(time_hour, 0) + 1
                    
                    # 保存日志条目
                    self.log_entries.append({
                        'line_number': line_num,
                        'content': line
                    })
        
        except Exception as e:
            print(f"解析日志文件失败：{e}")
            return
        
        print(f"日志解析完成，共处理 {self.stats['total_lines']} 行")
    
    def generate_analysis_report(self, output_file="log_analysis_report.txt"):
        """生成分析报告"""
        print(f"\n--- 生成分析报告 ---")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("日志分析报告\n")
            f.write("=" * 50 + "\n")
            f.write(f"生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"分析的日志行数：{self.stats['total_lines']:,}\n\n")
            
            # 日志级别统计
            f.write("日志级别统计：\n")
            f.write("-" * 20 + "\n")
            f.write(f"ERROR:   {self.stats['error_count']:>6} ({self.stats['error_count']/self.stats['total_lines']*100:.1f}%)\n")
            f.write(f"WARNING: {self.stats['warning_count']:>6} ({self.stats['warning_count']/self.stats['total_lines']*100:.1f}%)\n")
            f.write(f"INFO:    {self.stats['info_count']:>6} ({self.stats['info_count']/self.stats['total_lines']*100:.1f}%)\n")
            f.write(f"DEBUG:   {self.stats['debug_count']:>6} ({self.stats['debug_count']/self.stats['total_lines']*100:.1f}%)\n\n")
            
            # IP地址统计
            if self.stats['ip_addresses']:
                f.write("IP地址访问统计（前10）：\n")
                f.write("-" * 30 + "\n")
                sorted_ips = sorted(self.stats['ip_addresses'].items(), key=lambda x: x[1], reverse=True)
                for ip, count in sorted_ips[:10]:
                    f.write(f"{ip:<15} {count:>6} 次\n")
                f.write("\n")
            
            # 状态码统计
            if self.stats['status_codes']:
                f.write("HTTP状态码统计：\n")
                f.write("-" * 20 + "\n")
                sorted_codes = sorted(self.stats['status_codes'].items(), key=lambda x: x[1], reverse=True)
                for code, count in sorted_codes:
                    f.write(f"{code:<6} {count:>6} 次\n")
                f.write("\n")
            
            # 按小时统计
            if self.stats['hourly_stats']:
                f.write("按小时活动统计（前10）：\n")
                f.write("-" * 30 + "\n")
                sorted_hours = sorted(self.stats['hourly_stats'].items(), key=lambda x: x[1], reverse=True)
                for hour, count in sorted_hours[:10]:
                    f.write(f"{hour:<13} {count:>6} 条\n")
                f.write("\n")
            
            # 错误日志详情
            f.write("错误日志详情（最近10条）：\n")
            f.write("-" * 40 + "\n")
            error_logs = [entry for entry in self.log_entries if '[ERROR]' in entry['content']]
            for entry in error_logs[-10:]:
                f.write(f"行 {entry['line_number']:>4}: {entry['content']}\n")
        
        print(f"分析报告生成完成：{output_file}")
        return output_file
    
    def search_logs(self, keyword, case_sensitive=False):
        """搜索日志"""
        print(f"\n--- 搜索关键词：{keyword} ---")
        
        if not case_sensitive:
            keyword = keyword.lower()
        
        matches = []
        for entry in self.log_entries:
            content = entry['content'] if case_sensitive else entry['content'].lower()
            if keyword in content:
                matches.append(entry)
        
        print(f"找到 {len(matches)} 条匹配记录")
        
        # 显示前5条匹配结果
        for i, match in enumerate(matches[:5]):
            print(f"{i+1}. 行{match['line_number']}: {match['content']}")
        
        if len(matches) > 5:
            print(f"... 还有 {len(matches) - 5} 条记录")
        
        return matches

# 演示日志分析器
print("\n--- 日志分析器演示 ---")
analyzer = LogAnalyzer()

# 创建示例日志
log_file = analyzer.create_sample_log("demo.log", 50)

# 解析日志
analyzer.parse_log_file(log_file)

# 生成报告
report_file = analyzer.generate_analysis_report()

# 显示报告内容
if os.path.exists(report_file):
    print(f"\n--- 分析报告内容 ---")
    with open(report_file, 'r', encoding='utf-8') as f:
        print(f.read())

# 搜索示例
analyzer.search_logs("ERROR")

# ============================================================================
# 练习4：配置文件管理器
# ============================================================================

print("\n" + "=" * 60)
print("练习4：配置文件管理器")
print("=" * 60)

class ConfigManager:
    """
    配置文件管理器
    功能：读取、写入、验证各种格式的配置文件
    """
    
    def __init__(self):
        self.config_data = {}
        self.config_file = None
    
    def create_sample_config(self):
        """创建示例配置文件"""
        print("\n--- 创建示例配置文件 ---")
        
        # JSON配置
        json_config = {
            "application": {
                "name": "示例应用",
                "version": "1.0.0",
                "debug": True
            },
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "myapp",
                "username": "admin",
                "password": "secret123"
            },
            "logging": {
                "level": "INFO",
                "file": "app.log",
                "max_size": "10MB"
            },
            "features": {
                "enable_cache": True,
                "enable_ssl": False,
                "max_connections": 100
            }
        }
        
        with open("config.json", 'w', encoding='utf-8') as f:
            json.dump(json_config, f, ensure_ascii=False, indent=2)
        
        print("JSON配置文件创建完成：config.json")
        
        # INI风格配置
        ini_content = """
[application]
name = 示例应用
version = 1.0.0
debug = true

[database]
host = localhost
port = 5432
name = myapp
username = admin
password = secret123

[logging]
level = INFO
file = app.log
max_size = 10MB

[features]
enable_cache = true
enable_ssl = false
max_connections = 100
"""
        
        with open("config.ini", 'w', encoding='utf-8') as f:
            f.write(ini_content.strip())
        
        print("INI配置文件创建完成：config.ini")
        
        return "config.json", "config.ini"
    
    def load_json_config(self, filename):
        """加载JSON配置文件"""
        print(f"\n--- 加载JSON配置：{filename} ---")
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.config_data = json.load(f)
            
            self.config_file = filename
            print(f"配置加载成功，包含 {len(self.config_data)} 个主要配置项")
            return True
            
        except FileNotFoundError:
            print(f"配置文件不存在：{filename}")
            return False
        except json.JSONDecodeError as e:
            print(f"JSON格式错误：{e}")
            return False
        except Exception as e:
            print(f"加载配置失败：{e}")
            return False
    
    def load_ini_config(self, filename):
        """加载INI配置文件"""
        print(f"\n--- 加载INI配置：{filename} ---")
        
        try:
            config_data = {}
            current_section = None
            
            with open(filename, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    
                    # 跳过空行和注释
                    if not line or line.startswith('#') or line.startswith(';'):
                        continue
                    
                    # 处理节（section）
                    if line.startswith('[') and line.endswith(']'):
                        current_section = line[1:-1]
                        config_data[current_section] = {}
                        continue
                    
                    # 处理键值对
                    if '=' in line and current_section:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        
                        # 类型转换
                        if value.lower() in ['true', 'false']:
                            value = value.lower() == 'true'
                        elif value.isdigit():
                            value = int(value)
                        elif value.replace('.', '').isdigit():
                            value = float(value)
                        
                        config_data[current_section][key] = value
            
            self.config_data = config_data
            self.config_file = filename
            print(f"INI配置加载成功，包含 {len(self.config_data)} 个配置节")
            return True
            
        except Exception as e:
            print(f"加载INI配置失败：{e}")
            return False
    
    def get_config(self, path, default=None):
        """获取配置值（支持点号路径）"""
        keys = path.split('.')
        value = self.config_data
        
        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default
    
    def set_config(self, path, value):
        """设置配置值（支持点号路径）"""
        keys = path.split('.')
        config = self.config_data
        
        # 创建嵌套字典结构
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        
        # 设置最终值
        config[keys[-1]] = value
        print(f"配置已更新：{path} = {value}")
    
    def validate_config(self, rules):
        """验证配置"""
        print("\n--- 配置验证 ---")
        
        errors = []
        warnings = []
        
        for rule in rules:
            path = rule['path']
            value = self.get_config(path)
            
            # 检查必需项
            if rule.get('required', False) and value is None:
                errors.append(f"缺少必需配置项：{path}")
                continue
            
            if value is not None:
                # 类型检查
                if 'type' in rule:
                    expected_type = rule['type']
                    if not isinstance(value, expected_type):
                        errors.append(f"配置项 {path} 类型错误，期望 {expected_type.__name__}，实际 {type(value).__name__}")
                
                # 范围检查
                if 'min' in rule and isinstance(value, (int, float)):
                    if value < rule['min']:
                        errors.append(f"配置项 {path} 值 {value} 小于最小值 {rule['min']}")
                
                if 'max' in rule and isinstance(value, (int, float)):
                    if value > rule['max']:
                        errors.append(f"配置项 {path} 值 {value} 大于最大值 {rule['max']}")
                
                # 选项检查
                if 'choices' in rule:
                    if value not in rule['choices']:
                        errors.append(f"配置项 {path} 值 {value} 不在允许的选项中：{rule['choices']}")
                
                # 警告检查
                if 'warn_if' in rule:
                    warn_condition = rule['warn_if']
                    if callable(warn_condition) and warn_condition(value):
                        warnings.append(f"配置项 {path} 值 {value} 可能存在问题")
        
        # 输出验证结果
        if errors:
            print(f"发现 {len(errors)} 个错误：")
            for error in errors:
                print(f"  ❌ {error}")
        
        if warnings:
            print(f"发现 {len(warnings)} 个警告：")
            for warning in warnings:
                print(f"  ⚠️  {warning}")
        
        if not errors and not warnings:
            print("✅ 配置验证通过")
        
        return len(errors) == 0
    
    def save_config(self, filename=None):
        """保存配置"""
        if filename is None:
            filename = self.config_file
        
        if filename is None:
            print("没有指定保存文件")
            return False
        
        try:
            if filename.endswith('.json'):
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.config_data, f, ensure_ascii=False, indent=2)
            else:
                # 简单的INI格式保存
                with open(filename, 'w', encoding='utf-8') as f:
                    for section, items in self.config_data.items():
                        f.write(f"[{section}]\n")
                        for key, value in items.items():
                            f.write(f"{key} = {value}\n")
                        f.write("\n")
            
            print(f"配置已保存到：{filename}")
            return True
            
        except Exception as e:
            print(f"保存配置失败：{e}")
            return False
    
    def print_config(self):
        """打印配置"""
        print("\n--- 当前配置 ---")
        self._print_dict(self.config_data)
    
    def _print_dict(self, d, indent=0):
        """递归打印字典"""
        for key, value in d.items():
            if isinstance(value, dict):
                print("  " * indent + f"{key}:")
                self._print_dict(value, indent + 1)
            else:
                print("  " * indent + f"{key}: {value}")

# 演示配置管理器
print("\n--- 配置管理器演示 ---")
config_manager = ConfigManager()

# 创建示例配置
json_file, ini_file = config_manager.create_sample_config()

# 加载JSON配置
config_manager.load_json_config(json_file)
config_manager.print_config()

# 获取配置值
app_name = config_manager.get_config('application.name')
db_port = config_manager.get_config('database.port')
print(f"\n应用名称：{app_name}")
print(f"数据库端口：{db_port}")

# 修改配置
config_manager.set_config('application.debug', False)
config_manager.set_config('database.port', 3306)

# 配置验证规则
validation_rules = [
    {'path': 'application.name', 'required': True, 'type': str},
    {'path': 'application.version', 'required': True, 'type': str},
    {'path': 'database.port', 'required': True, 'type': int, 'min': 1, 'max': 65535},
    {'path': 'logging.level', 'required': True, 'choices': ['DEBUG', 'INFO', 'WARNING', 'ERROR']},
    {'path': 'features.max_connections', 'type': int, 'min': 1, 'max': 1000}
]

# 验证配置
config_manager.validate_config(validation_rules)

# 保存配置
config_manager.save_config("updated_config.json")

# ============================================================================
# 综合练习总结
# ============================================================================

print("\n" + "=" * 60)
print("综合练习总结")
print("=" * 60)

print("""
🎉 恭喜完成输入输出综合练习！

本次练习涵盖了以下内容：

1. 学生成绩管理系统 📚
   - 数据输入验证
   - JSON文件操作
   - 用户交互界面
   - 数据统计和导出

2. 文件批处理工具 🔧
   - 批量文件操作
   - 日志记录
   - 错误处理
   - 文件报告生成

3. 日志分析器 📊
   - 正则表达式应用
   - 大文件处理
   - 数据统计分析
   - 报告生成

4. 配置文件管理器 ⚙️
   - 多格式配置文件
   - 配置验证
   - 动态配置修改
   - 类型转换

💡 学习要点：
- 输入验证的重要性
- 异常处理的最佳实践
- 用户体验的考虑
- 代码的模块化设计
- 数据持久化策略

🚀 进阶建议：
1. 为这些工具添加图形界面
2. 实现网络功能和API接口
3. 添加数据库支持
4. 实现插件系统
5. 添加单元测试

继续加油，Python学习之路越来越精彩！ 🐍✨
""")

# 清理演示文件提示
print("\n" + "=" * 60)
print("文件清理提示")
print("=" * 60)

print("""
本次练习创建了以下文件和目录：
- students_data.json (学生数据)
- test_files/ (测试文件目录)
- batch_process.log (批处理日志)
- demo.log (示例日志)
- log_analysis_report.txt (日志分析报告)
- config.json, config.ini (配置文件)
- 各种导出和报告文件

这些文件用于演示各种IO操作，可以：
1. 保留文件以便进一步学习和实验
2. 手动删除不需要的文件
3. 修改代码以自动清理临时文件

建议查看这些文件的内容，了解不同IO操作的实际效果。
""")

print("\n程序运行完成！感谢使用Python输入输出综合练习系统！")