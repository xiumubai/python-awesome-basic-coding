# 输入输出综合练习

## 概述

本章提供了四个综合性的练习项目，帮助你将前面学到的输入输出知识应用到实际场景中。这些练习涵盖了数据管理、文件处理、日志分析和配置管理等常见的编程任务。

## 学习目标

- 掌握复杂数据结构的输入输出操作
- 学会设计用户友好的交互界面
- 理解文件批处理的实现方法
- 掌握日志分析和数据统计技巧
- 学会配置文件的管理和验证
- 培养异常处理和错误恢复的能力

## 完整代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
输入输出综合练习

本文件包含四个综合练习项目：
1. 学生成绩管理系统
2. 文件批处理工具
3. 日志分析器
4. 配置文件管理器

作者：Python学习者
日期：2024年
"""

import os
import json
import csv
import datetime
import random
import shutil
import re
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
    
    def __init__(self, data_file="students_data.json"):
        self.data_file = data_file
        self.students = {}
        self.load_data()
    
    def load_data(self):
        """从文件加载学生数据"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.students = json.load(f)
                print(f"已加载 {len(self.students)} 名学生的数据")
            else:
                print("数据文件不存在，将创建新的数据文件")
        except Exception as e:
            print(f"加载数据失败：{e}")
            self.students = {}
    
    def save_data(self):
        """保存学生数据到文件"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.students, f, ensure_ascii=False, indent=2)
            print("数据保存成功")
        except Exception as e:
            print(f"保存数据失败：{e}")
    
    def add_student(self, student_id, name, class_name):
        """添加学生"""
        if student_id in self.students:
            print(f"学生 {student_id} 已存在")
            return False
        
        self.students[student_id] = {
            'name': name,
            'class': class_name,
            'scores': {},
            'created_time': datetime.datetime.now().isoformat()
        }
        
        print(f"学生 {name}（{student_id}）添加成功")
        return True
    
    def add_score(self, student_id, subject, score):
        """录入成绩"""
        if student_id not in self.students:
            print(f"学生 {student_id} 不存在")
            return False
        
        if not (0 <= score <= 100):
            print("成绩必须在0-100之间")
            return False
        
        if 'scores' not in self.students[student_id]:
            self.students[student_id]['scores'] = {}
        
        self.students[student_id]['scores'][subject] = score
        print(f"学生 {student_id} 的 {subject} 成绩录入成功：{score}分")
        return True
    
    def get_student_info(self, student_id):
        """查询学生信息"""
        if student_id not in self.students:
            print(f"学生 {student_id} 不存在")
            return None
        
        student = self.students[student_id]
        print(f"\n学生信息：")
        print(f"学号：{student_id}")
        print(f"姓名：{student['name']}")
        print(f"班级：{student['class']}")
        print(f"成绩：")
        
        if student['scores']:
            total_score = 0
            subject_count = 0
            for subject, score in student['scores'].items():
                print(f"  {subject}: {score}分")
                total_score += score
                subject_count += 1
            
            if subject_count > 0:
                average = total_score / subject_count
                print(f"平均分：{average:.2f}分")
        else:
            print("  暂无成绩记录")
        
        return student
    
    def get_statistics(self):
        """获取统计信息"""
        if not self.students:
            print("暂无学生数据")
            return
        
        print(f"\n=== 统计信息 ===")
        print(f"学生总数：{len(self.students)}")
        
        # 班级分布
        class_count = {}
        for student in self.students.values():
            class_name = student['class']
            class_count[class_name] = class_count.get(class_name, 0) + 1
        
        print(f"班级分布：")
        for class_name, count in class_count.items():
            print(f"  {class_name}: {count}人")
        
        # 各科成绩统计
        subject_scores = {}
        for student in self.students.values():
            for subject, score in student.get('scores', {}).items():
                if subject not in subject_scores:
                    subject_scores[subject] = []
                subject_scores[subject].append(score)
        
        if subject_scores:
            print(f"各科成绩统计：")
            for subject, scores in subject_scores.items():
                avg_score = sum(scores) / len(scores)
                max_score = max(scores)
                min_score = min(scores)
                print(f"  {subject}: 平均{avg_score:.2f}分, 最高{max_score}分, 最低{min_score}分 ({len(scores)}人)")
    
    def export_to_csv(self, filename="students_export.csv"):
        """导出数据到CSV文件"""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # 写入表头
                headers = ['学号', '姓名', '班级']
                
                # 收集所有科目
                all_subjects = set()
                for student in self.students.values():
                    all_subjects.update(student.get('scores', {}).keys())
                
                headers.extend(sorted(all_subjects))
                headers.append('平均分')
                writer.writerow(headers)
                
                # 写入数据
                for student_id, student in self.students.items():
                    row = [student_id, student['name'], student['class']]
                    
                    scores = student.get('scores', {})
                    total_score = 0
                    subject_count = 0
                    
                    for subject in sorted(all_subjects):
                        score = scores.get(subject, '')
                        row.append(score)
                        if score:
                            total_score += score
                            subject_count += 1
                    
                    # 计算平均分
                    average = total_score / subject_count if subject_count > 0 else ''
                    if average:
                        row.append(f"{average:.2f}")
                    else:
                        row.append('')
                    
                    writer.writerow(row)
            
            print(f"数据已导出到：{filename}")
            return True
            
        except Exception as e:
            print(f"导出CSV失败：{e}")
            return False
    
    def export_to_txt(self, filename="students_report.txt"):
        """导出文本报告"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("学生成绩报告\n")
                f.write("=" * 50 + "\n")
                f.write(f"生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"学生总数：{len(self.students)}\n\n")
                
                for student_id, student in self.students.items():
                    f.write(f"学号：{student_id}\n")
                    f.write(f"姓名：{student['name']}\n")
                    f.write(f"班级：{student['class']}\n")
                    
                    scores = student.get('scores', {})
                    if scores:
                        f.write("成绩：\n")
                        total_score = 0
                        for subject, score in scores.items():
                            f.write(f"  {subject}: {score}分\n")
                            total_score += score
                        
                        average = total_score / len(scores)
                        f.write(f"平均分：{average:.2f}分\n")
                    else:
                        f.write("成绩：暂无记录\n")
                    
                    f.write("-" * 30 + "\n")
            
            print(f"报告已导出到：{filename}")
            return True
            
        except Exception as e:
            print(f"导出报告失败：{e}")
            return False
    
    def export_to_json(self, filename="students_backup.json"):
        """导出JSON备份"""
        try:
            backup_data = {
                'export_time': datetime.datetime.now().isoformat(),
                'student_count': len(self.students),
                'students': self.students
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, ensure_ascii=False, indent=2)
            
            print(f"JSON备份已导出到：{filename}")
            return True
            
        except Exception as e:
            print(f"导出JSON失败：{e}")
            return False
    
    def run_interactive(self):
        """运行交互式主程序"""
        print("\n欢迎使用学生成绩管理系统！")
        
        while True:
            print("\n" + "-" * 40)
            print("请选择操作：")
            print("1. 添加学生")
            print("2. 录入成绩")
            print("3. 查询学生")
            print("4. 统计信息")
            print("5. 导出数据")
            print("6. 保存并退出")
            print("0. 直接退出")
            
            try:
                choice = input("请输入选项（0-6）：").strip()
                
                if choice == '1':
                    student_id = input("请输入学号：").strip()
                    name = input("请输入姓名：").strip()
                    class_name = input("请输入班级：").strip()
                    
                    if student_id and name and class_name:
                        self.add_student(student_id, name, class_name)
                    else:
                        print("输入信息不完整")
                
                elif choice == '2':
                    student_id = input("请输入学号：").strip()
                    subject = input("请输入科目：").strip()
                    
                    try:
                        score = float(input("请输入成绩：").strip())
                        self.add_score(student_id, subject, score)
                    except ValueError:
                        print("成绩必须是数字")
                
                elif choice == '3':
                    student_id = input("请输入学号：").strip()
                    self.get_student_info(student_id)
                
                elif choice == '4':
                    self.get_statistics()
                
                elif choice == '5':
                    print("导出格式：")
                    print("1. CSV格式")
                    print("2. 文本报告")
                    print("3. JSON备份")
                    
                    export_choice = input("请选择导出格式（1-3）：").strip()
                    
                    if export_choice == '1':
                        self.export_to_csv()
                    elif export_choice == '2':
                        self.export_to_txt()
                    elif export_choice == '3':
                        self.export_to_json()
                    else:
                        print("无效选择")
                
                elif choice == '6':
                    self.save_data()
                    print("数据已保存，程序退出")
                    break
                
                elif choice == '0':
                    print("程序退出（数据未保存）")
                    break
                
                else:
                    print("无效选择，请重新输入")
                    
            except KeyboardInterrupt:
                print("\n程序被中断")
                break
            except Exception as e:
                print(f"操作失败：{e}")

# 演示学生管理系统
print("\n--- 学生管理系统演示 ---")
manager = StudentManager()

# 添加示例学生
manager.add_student("2024001", "张三", "计算机1班")
manager.add_student("2024002", "李四", "计算机1班")
manager.add_student("2024003", "王五", "计算机2班")

# 录入成绩
manager.add_score("2024001", "数学", 85)
manager.add_score("2024001", "英语", 92)
manager.add_score("2024001", "编程", 88)

manager.add_score("2024002", "数学", 78)
manager.add_score("2024002", "英语", 85)
manager.add_score("2024002", "编程", 95)

manager.add_score("2024003", "数学", 92)
manager.add_score("2024003", "英语", 88)

# 查询学生信息
manager.get_student_info("2024001")

# 显示统计信息
manager.get_statistics()

# 导出数据
manager.export_to_csv()
manager.export_to_txt()

# 保存数据
manager.save_data()

# ============================================================================
# 练习2：文件批处理工具
# ============================================================================

print("\n" + "=" * 60)
print("练习2：文件批处理工具")
print("=" * 60)

class FileBatchProcessor:
    """
    文件批处理工具
    功能：批量重命名、编码转换、添加文件头、生成报告
    """
    
    def __init__(self, log_file="batch_process.log"):
        self.log_file = log_file
        self.setup_logging()
    
    def setup_logging(self):
        """设置日志记录"""
        self.log_entries = []
    
    def log(self, message, level="INFO"):
        """记录日志"""
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{level}] {message}"
        self.log_entries.append(log_entry)
        print(log_entry)
        
        # 写入日志文件
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry + "\n")
        except Exception as e:
            print(f"写入日志失败：{e}")
    
    def create_test_files(self, directory="test_files", count=5):
        """创建测试文件"""
        self.log(f"开始创建测试文件，目录：{directory}，数量：{count}")
        
        try:
            # 创建目录
            os.makedirs(directory, exist_ok=True)
            
            for i in range(1, count + 1):
                filename = f"test_file_{i:02d}.txt"
                filepath = os.path.join(directory, filename)
                
                content = f"""这是测试文件 {i}
创建时间：{datetime.datetime.now()}
文件编号：{i:02d}
内容：这是一个用于批处理测试的文件。
包含中文字符以测试编码转换功能。

随机数据：{random.randint(1000, 9999)}
"""
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.log(f"创建文件：{filepath}")
            
            self.log(f"测试文件创建完成，共 {count} 个文件")
            return directory
            
        except Exception as e:
            self.log(f"创建测试文件失败：{e}", "ERROR")
            return None
    
    def batch_rename(self, directory, old_pattern, new_pattern):
        """批量重命名文件"""
        self.log(f"开始批量重命名，目录：{directory}")
        self.log(f"替换模式：{old_pattern} -> {new_pattern}")
        
        if not os.path.exists(directory):
            self.log(f"目录不存在：{directory}", "ERROR")
            return 0
        
        renamed_count = 0
        
        try:
            for filename in os.listdir(directory):
                if old_pattern in filename:
                    old_path = os.path.join(directory, filename)
                    new_filename = filename.replace(old_pattern, new_pattern)
                    new_path = os.path.join(directory, new_filename)
                    
                    if os.path.exists(new_path):
                        self.log(f"目标文件已存在，跳过：{new_filename}", "WARNING")
                        continue
                    
                    os.rename(old_path, new_path)
                    self.log(f"重命名：{filename} -> {new_filename}")
                    renamed_count += 1
            
            self.log(f"批量重命名完成，共处理 {renamed_count} 个文件")
            return renamed_count
            
        except Exception as e:
            self.log(f"批量重命名失败：{e}", "ERROR")
            return 0
    
    def batch_convert_encoding(self, directory, from_encoding="utf-8", to_encoding="gbk"):
        """批量转换文件编码"""
        self.log(f"开始批量转换编码：{from_encoding} -> {to_encoding}")
        
        if not os.path.exists(directory):
            self.log(f"目录不存在：{directory}", "ERROR")
            return 0
        
        converted_count = 0
        
        try:
            for filename in os.listdir(directory):
                if filename.endswith('.txt'):
                    filepath = os.path.join(directory, filename)
                    
                    try:
                        # 读取原文件
                        with open(filepath, 'r', encoding=from_encoding) as f:
                            content = f.read()
                        
                        # 写入新编码
                        with open(filepath, 'w', encoding=to_encoding) as f:
                            f.write(content)
                        
                        self.log(f"转换编码：{filename}")
                        converted_count += 1
                        
                    except UnicodeDecodeError:
                        self.log(f"编码转换失败（解码错误）：{filename}", "WARNING")
                    except UnicodeEncodeError:
                        self.log(f"编码转换失败（编码错误）：{filename}", "WARNING")
            
            self.log(f"批量编码转换完成，共处理 {converted_count} 个文件")
            return converted_count
            
        except Exception as e:
            self.log(f"批量编码转换失败：{e}", "ERROR")
            return 0
    
    def batch_add_header(self, directory, header_text):
        """批量添加文件头"""
        self.log(f"开始批量添加文件头")
        
        if not os.path.exists(directory):
            self.log(f"目录不存在：{directory}", "ERROR")
            return 0
        
        processed_count = 0
        
        try:
            for filename in os.listdir(directory):
                if filename.endswith('.txt'):
                    filepath = os.path.join(directory, filename)
                    
                    try:
                        # 读取原文件内容
                        with open(filepath, 'r', encoding='utf-8') as f:
                            original_content = f.read()
                        
                        # 检查是否已有文件头
                        if header_text.strip() in original_content:
                            self.log(f"文件头已存在，跳过：{filename}", "INFO")
                            continue
                        
                        # 添加文件头
                        new_content = header_text + "\n\n" + original_content
                        
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        self.log(f"添加文件头：{filename}")
                        processed_count += 1
                        
                    except Exception as e:
                        self.log(f"处理文件失败：{filename} - {e}", "ERROR")
            
            self.log(f"批量添加文件头完成，共处理 {processed_count} 个文件")
            return processed_count
            
        except Exception as e:
            self.log(f"批量添加文件头失败：{e}", "ERROR")
            return 0
    
    def generate_file_report(self, directory, report_file="file_report.txt"):
        """生成文件报告"""
        self.log(f"开始生成文件报告：{directory}")
        
        if not os.path.exists(directory):
            self.log(f"目录不存在：{directory}", "ERROR")
            return None
        
        try:
            report_data = {
                'directory': directory,
                'scan_time': datetime.datetime.now().isoformat(),
                'files': [],
                'summary': {
                    'total_files': 0,
                    'total_size': 0,
                    'file_types': {}
                }
            }
            
            # 扫描文件
            for filename in os.listdir(directory):
                filepath = os.path.join(directory, filename)
                
                if os.path.isfile(filepath):
                    file_stat = os.stat(filepath)
                    file_info = {
                        'name': filename,
                        'size': file_stat.st_size,
                        'modified_time': datetime.datetime.fromtimestamp(file_stat.st_mtime).isoformat(),
                        'extension': os.path.splitext(filename)[1].lower()
                    }
                    
                    report_data['files'].append(file_info)
                    report_data['summary']['total_files'] += 1
                    report_data['summary']['total_size'] += file_stat.st_size
                    
                    # 统计文件类型
                    ext = file_info['extension']
                    report_data['summary']['file_types'][ext] = report_data['summary']['file_types'].get(ext, 0) + 1
            
            # 生成报告文件
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write("文件处理报告\n")
                f.write("=" * 50 + "\n")
                f.write(f"扫描目录：{directory}\n")
                f.write(f"扫描时间：{report_data['scan_time']}\n")
                f.write(f"文件总数：{report_data['summary']['total_files']}\n")
                f.write(f"总大小：{report_data['summary']['total_size']:,} 字节\n\n")
                
                # 文件类型统计
                f.write("文件类型统计：\n")
                f.write("-" * 20 + "\n")
                for ext, count in report_data['summary']['file_types'].items():
                    ext_name = ext if ext else "无扩展名"
                    f.write(f"{ext_name:<10} {count:>6} 个\n")
                f.write("\n")
                
                # 文件详情
                f.write("文件详情：\n")
                f.write("-" * 20 + "\n")
                f.write(f"{'文件名':<30} {'大小':<10} {'修改时间'}\n")
                f.write("-" * 70 + "\n")
                
                for file_info in sorted(report_data['files'], key=lambda x: x['name']):
                    f.write(f"{file_info['name']:<30} {file_info['size']:<10} {file_info['modified_time']}\n")
            
            self.log(f"文件报告生成完成：{report_file}")
            return report_file
            
        except Exception as e:
            self.log(f"生成文件报告失败：{e}", "ERROR")
            return None

# 演示文件批处理工具
print("\n--- 文件批处理工具演示 ---")
processor = FileBatchProcessor()

# 创建测试文件
test_dir = processor.create_test_files("test_files", 3)

if test_dir:
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
```

## 代码详解

### 1. 学生成绩管理系统

这是一个完整的数据管理系统，展示了以下技术：

- **数据持久化**：使用JSON格式保存学生数据
- **输入验证**：检查学号重复、成绩范围等
- **用户交互**：提供友好的命令行界面
- **数据导出**：支持CSV、文本、JSON多种格式
- **统计分析**：自动计算平均分、班级分布等

### 2. 文件批处理工具

展示了批量文件操作的实现：

- **批量重命名**：使用字符串替换实现文件重命名
- **编码转换**：处理不同字符编码的文件
- **文件头添加**：批量为文件添加统一的头部信息
- **日志记录**：记录所有操作过程和结果
- **报告生成**：统计文件信息并生成详细报告

### 3. 日志分析器

实现了日志文件的智能分析：

- **正则表达式**：提取IP地址、状态码、时间等信息
- **统计分析**：按级别、时间、来源等维度统计
- **搜索功能**：支持关键词搜索和过滤
- **报告生成**：自动生成分析报告

### 4. 配置文件管理器

展示了配置文件的完整管理方案：

- **多格式支持**：JSON和INI格式的读写
- **配置验证**：类型检查、范围验证、必需项检查
- **动态修改**：支持运行时修改配置
- **路径访问**：使用点号路径访问嵌套配置

## 学习要点

### 1. 数据验证

```python
# 输入验证示例
def validate_score(score):
    if not isinstance(score, (int, float)):
        return False, "成绩必须是数字"
    if not (0 <= score <= 100):
        return False, "成绩必须在0-100之间"
    return True, "验证通过"
```

### 2. 异常处理

```python
# 文件操作异常处理
try:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"文件不存在：{filename}")
except json.JSONDecodeError:
    print("JSON格式错误")
except Exception as e:
    print(f"未知错误：{e}")
```

### 3. 用户交互设计

```python
# 友好的用户界面
while True:
    print("\n请选择操作：")
    print("1. 添加数据")
    print("2. 查询数据")
    print("0. 退出")
    
    choice = input("请输入选项：").strip()
    # 处理用户选择...
```

## 实践练习

### 基础练习

1. **扩展学生管理系统**
   - 添加课程管理功能
   - 实现成绩趋势分析
   - 添加数据备份和恢复

2. **改进文件处理工具**
   - 支持更多文件格式
   - 添加文件内容搜索替换
   - 实现文件同步功能

### 进阶练习

3. **增强日志分析器**
   - 实现实时日志监控
   - 添加异常检测算法
   - 支持多种日志格式

4. **完善配置管理器**
   - 添加配置模板功能
   - 实现配置继承机制
   - 支持环境变量替换

### 挑战练习

5. **系统集成**
   - 将四个工具整合为统一系统
   - 添加Web界面
   - 实现用户权限管理

6. **性能优化**
   - 优化大文件处理性能
   - 实现并发处理
   - 添加缓存机制

## 运行示例

### 学生管理系统运行

```bash
# 运行学生管理系统
python 08_exercises.py

# 输出示例：
学生 张三（2024001）添加成功
学生 2024001 的 数学 成绩录入成功：85分

学生信息：
学号：2024001
姓名：张三
班级：计算机1班
成绩：
  数学: 85分
  英语: 92分
  编程: 88分
平均分：88.33分
```

### 文件批处理运行

```bash
# 批处理操作示例
[2024-01-15 10:30:15] [INFO] 开始创建测试文件
[2024-01-15 10:30:15] [INFO] 创建文件：test_files/test_file_01.txt
[2024-01-15 10:30:15] [INFO] 重命名：test_file_01.txt -> processed_file_01.txt
[2024-01-15 10:30:15] [INFO] 批量重命名完成，共处理 3 个文件
```

### 日志分析运行

```bash
# 日志分析结果示例
日志解析完成，共处理 50 行

日志级别统计：
ERROR:     8 (16.0%)
WARNING:  12 (24.0%)
INFO:     20 (40.0%)
DEBUG:    10 (20.0%)

IP地址访问统计（前5）：
192.168.1.100    15 次
192.168.1.101    12 次
```

## 扩展思考

### 1. 架构设计

- 如何设计可扩展的插件系统？
- 如何实现配置的热更新？
- 如何处理大规模数据的性能问题？

### 2. 安全考虑

- 如何防止配置文件中的敏感信息泄露？
- 如何验证用户输入的安全性？
- 如何实现访问控制和权限管理？

### 3. 用户体验

- 如何设计更直观的用户界面？
- 如何提供更好的错误提示和帮助信息？
- 如何实现操作的撤销和重做？

### 4. 数据处理

- 如何处理不同格式的数据转换？
- 如何实现数据的增量更新？
- 如何保证数据的一致性和完整性？

## 模块导航

### 相关模块

- [基础输入](./basic-input.md) - 学习基本输入操作
- [输入验证](./input-validation.md) - 掌握输入验证技巧
- [文件输入](./file-input.md) - 了解文件读取方法
- [文件输出](./file-output.md) - 学习文件写入操作
- [高级IO](./advanced-io.md) - 探索高级输入输出技术

### 学习路径

1. **基础阶段**：掌握基本的输入输出操作
2. **进阶阶段**：学习文件操作和数据处理
3. **应用阶段**：完成综合练习项目
4. **优化阶段**：改进性能和用户体验

### 下一步学习

- [04-控制结构](../../04-control-structures/) - 学习程序控制流
- [05-函数](../../05-functions/) - 掌握函数设计
- [06-面向对象](../../06-object-oriented/) - 学习面向对象编程

---

**提示**：这些练习项目展示了Python输入输出的实际应用，建议逐个运行和分析，理解每个功能的实现原理。通过修改和扩展这些代码，可以加深对输入输出操作的理解。