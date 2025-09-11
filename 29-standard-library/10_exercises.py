#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python标准库综合练习

本文件包含多个综合练习，整合前面学习的所有标准库模块：
- 文件系统操作 (os, sys, pathlib, shutil)
- 时间处理 (datetime)
- 随机数生成 (random)
- 数据处理 (json, csv, pickle)
- 网络编程 (urllib)
- 正则表达式 (re)
- 数学运算 (math, statistics)
- 集合数据结构 (collections, heapq, bisect, array, queue, enum)

练习目标：
1. 综合运用多个标准库模块
2. 解决实际问题
3. 提高编程技能和代码质量
4. 学会模块间的协作使用
"""

import os
import sys
import json
import csv
import pickle
import re
import math
import statistics
import random
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from pathlib import Path
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple
import heapq
import bisect
import array
from enum import Enum, IntEnum


class LogLevel(IntEnum):
    """日志级别枚举"""
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5


class FileType(Enum):
    """文件类型枚举"""
    TEXT = "text"
    JSON = "json"
    CSV = "csv"
    PICKLE = "pickle"


def exercise_1_log_analyzer():
    """
    练习1: 日志分析器
    
    功能：
    1. 解析日志文件
    2. 统计各种信息
    3. 生成分析报告
    4. 保存结果到不同格式的文件
    """
    print("=" * 60)
    print("练习1: 日志分析器")
    print("=" * 60)
    
    # 生成模拟日志数据
    def generate_sample_logs():
        """生成示例日志数据"""
        log_entries = []
        start_time = datetime.now() - timedelta(hours=24)
        
        # 模拟不同类型的日志
        log_templates = [
            (LogLevel.INFO, "User {user} logged in from {ip}"),
            (LogLevel.INFO, "User {user} logged out"),
            (LogLevel.WARNING, "High memory usage: {memory}%"),
            (LogLevel.ERROR, "Database connection failed: {error}"),
            (LogLevel.ERROR, "File not found: {file}"),
            (LogLevel.CRITICAL, "System crash: {reason}"),
            (LogLevel.DEBUG, "Processing request {request_id}")
        ]
        
        users = ['alice', 'bob', 'charlie', 'david', 'eve']
        ips = ['192.168.1.10', '192.168.1.20', '10.0.0.5', '172.16.0.1']
        
        for i in range(100):
            # 随机时间
            log_time = start_time + timedelta(minutes=random.randint(0, 1440))
            
            # 随机选择日志模板
            level, template = random.choice(log_templates)
            
            # 填充模板
            if '{user}' in template:
                message = template.format(
                    user=random.choice(users),
                    ip=random.choice(ips)
                )
            elif '{memory}' in template:
                message = template.format(memory=random.randint(70, 95))
            elif '{error}' in template:
                message = template.format(error=f"Connection timeout after {random.randint(5, 30)}s")
            elif '{file}' in template:
                message = template.format(file=f"/path/to/file_{random.randint(1, 100)}.txt")
            elif '{reason}' in template:
                message = template.format(reason="Out of memory")
            elif '{request_id}' in template:
                message = template.format(request_id=f"REQ_{random.randint(1000, 9999)}")
            else:
                message = template
            
            log_entry = f"{log_time.strftime('%Y-%m-%d %H:%M:%S')} {level.name} {message}"
            log_entries.append(log_entry)
        
        return sorted(log_entries)
    
    # 日志分析器类
    class LogAnalyzer:
        def __init__(self):
            self.logs = []
            self.parsed_logs = []
            self.stats = defaultdict(int)
            self.user_activities = defaultdict(list)
            self.error_patterns = Counter()
            self.hourly_stats = defaultdict(lambda: defaultdict(int))
        
        def load_logs(self, log_entries):
            """加载日志数据"""
            self.logs = log_entries
            self._parse_logs()
        
        def _parse_logs(self):
            """解析日志"""
            log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
            
            for log_entry in self.logs:
                match = re.match(log_pattern, log_entry)
                if match:
                    timestamp_str, level, message = match.groups()
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                    
                    parsed_log = {
                        'timestamp': timestamp,
                        'level': level,
                        'message': message
                    }
                    
                    self.parsed_logs.append(parsed_log)
                    
                    # 统计信息
                    self.stats[level] += 1
                    self.hourly_stats[timestamp.hour][level] += 1
                    
                    # 用户活动分析
                    user_match = re.search(r'User (\w+)', message)
                    if user_match:
                        user = user_match.group(1)
                        action = 'login' if 'logged in' in message else 'logout'
                        self.user_activities[user].append((timestamp, action))
                    
                    # 错误模式分析
                    if level in ['ERROR', 'CRITICAL']:
                        # 提取错误类型
                        if 'Database' in message:
                            self.error_patterns['Database Error'] += 1
                        elif 'File not found' in message:
                            self.error_patterns['File Not Found'] += 1
                        elif 'System crash' in message:
                            self.error_patterns['System Crash'] += 1
                        else:
                            self.error_patterns['Other Error'] += 1
        
        def generate_report(self):
            """生成分析报告"""
            report = {
                'summary': {
                    'total_logs': len(self.parsed_logs),
                    'time_range': {
                        'start': min(log['timestamp'] for log in self.parsed_logs).isoformat(),
                        'end': max(log['timestamp'] for log in self.parsed_logs).isoformat()
                    },
                    'log_levels': dict(self.stats)
                },
                'hourly_distribution': dict(self.hourly_stats),
                'user_activities': {user: len(activities) for user, activities in self.user_activities.items()},
                'error_patterns': dict(self.error_patterns.most_common()),
                'top_active_hours': self._get_top_active_hours()
            }
            
            return report
        
        def _get_top_active_hours(self):
            """获取最活跃的小时"""
            hour_totals = {}
            for hour, levels in self.hourly_stats.items():
                hour_totals[hour] = sum(levels.values())
            
            return sorted(hour_totals.items(), key=lambda x: x[1], reverse=True)[:5]
        
        def save_report(self, report, base_filename):
            """保存报告到不同格式"""
            # 保存为JSON
            json_file = f"{base_filename}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            # 保存为CSV（简化版）
            csv_file = f"{base_filename}.csv"
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Metric', 'Value'])
                writer.writerow(['Total Logs', report['summary']['total_logs']])
                
                for level, count in report['summary']['log_levels'].items():
                    writer.writerow([f'{level} Logs', count])
            
            # 保存为Pickle
            pickle_file = f"{base_filename}.pkl"
            with open(pickle_file, 'wb') as f:
                pickle.dump(report, f)
            
            return json_file, csv_file, pickle_file
    
    # 执行分析
    print("1. 生成模拟日志数据...")
    sample_logs = generate_sample_logs()
    print(f"   生成了 {len(sample_logs)} 条日志")
    
    print("\n2. 分析日志...")
    analyzer = LogAnalyzer()
    analyzer.load_logs(sample_logs)
    
    print("\n3. 生成报告...")
    report = analyzer.generate_report()
    
    # 显示报告摘要
    print("\n4. 报告摘要:")
    print(f"   总日志数: {report['summary']['total_logs']}")
    print("   日志级别分布:")
    for level, count in report['summary']['log_levels'].items():
        print(f"     {level}: {count}")
    
    print("\n   用户活动统计:")
    for user, count in report['user_activities'].items():
        print(f"     {user}: {count} 次活动")
    
    print("\n   错误模式:")
    for pattern, count in report['error_patterns'].items():
        print(f"     {pattern}: {count} 次")
    
    print("\n   最活跃时段:")
    for hour, count in report['top_active_hours']:
        print(f"     {hour:02d}:00 - {count} 条日志")
    
    # 保存报告
    print("\n5. 保存报告...")
    base_filename = "log_analysis_report"
    json_file, csv_file, pickle_file = analyzer.save_report(report, base_filename)
    print(f"   JSON报告: {json_file}")
    print(f"   CSV报告: {csv_file}")
    print(f"   Pickle报告: {pickle_file}")


def exercise_2_file_organizer():
    """
    练习2: 智能文件整理器
    
    功能：
    1. 扫描目录中的文件
    2. 按类型、大小、日期分类
    3. 生成整理建议
    4. 统计文件信息
    """
    print("\n" + "=" * 60)
    print("练习2: 智能文件整理器")
    print("=" * 60)
    
    class FileOrganizer:
        def __init__(self, target_dir="."):
            self.target_dir = Path(target_dir)
            self.file_info = []
            self.stats = {
                'total_files': 0,
                'total_size': 0,
                'by_extension': Counter(),
                'by_size_range': Counter(),
                'by_date_range': Counter()
            }
        
        def scan_directory(self):
            """扫描目录"""
            print(f"扫描目录: {self.target_dir.absolute()}")
            
            for file_path in self.target_dir.rglob('*'):
                if file_path.is_file():
                    try:
                        stat = file_path.stat()
                        file_info = {
                            'path': file_path,
                            'name': file_path.name,
                            'extension': file_path.suffix.lower(),
                            'size': stat.st_size,
                            'modified': datetime.fromtimestamp(stat.st_mtime),
                            'created': datetime.fromtimestamp(stat.st_ctime)
                        }
                        
                        self.file_info.append(file_info)
                        self._update_stats(file_info)
                        
                    except (OSError, PermissionError):
                        continue
        
        def _update_stats(self, file_info):
            """更新统计信息"""
            self.stats['total_files'] += 1
            self.stats['total_size'] += file_info['size']
            
            # 按扩展名统计
            ext = file_info['extension'] or 'no_extension'
            self.stats['by_extension'][ext] += 1
            
            # 按大小范围统计
            size = file_info['size']
            if size < 1024:  # < 1KB
                size_range = 'tiny'
            elif size < 1024 * 1024:  # < 1MB
                size_range = 'small'
            elif size < 10 * 1024 * 1024:  # < 10MB
                size_range = 'medium'
            elif size < 100 * 1024 * 1024:  # < 100MB
                size_range = 'large'
            else:
                size_range = 'huge'
            
            self.stats['by_size_range'][size_range] += 1
            
            # 按日期范围统计
            now = datetime.now()
            days_old = (now - file_info['modified']).days
            
            if days_old < 7:
                date_range = 'this_week'
            elif days_old < 30:
                date_range = 'this_month'
            elif days_old < 365:
                date_range = 'this_year'
            else:
                date_range = 'older'
            
            self.stats['by_date_range'][date_range] += 1
        
        def generate_organization_suggestions(self):
            """生成整理建议"""
            suggestions = []
            
            # 按扩展名分类建议
            ext_groups = defaultdict(list)
            for file_info in self.file_info:
                ext = file_info['extension'] or 'no_extension'
                ext_groups[ext].append(file_info)
            
            for ext, files in ext_groups.items():
                if len(files) > 5:  # 超过5个同类型文件
                    suggestions.append({
                        'type': 'group_by_extension',
                        'extension': ext,
                        'count': len(files),
                        'suggested_folder': f"files_{ext.replace('.', '')}" if ext != 'no_extension' else 'files_no_extension'
                    })
            
            # 大文件建议
            large_files = [f for f in self.file_info if f['size'] > 50 * 1024 * 1024]  # > 50MB
            if large_files:
                suggestions.append({
                    'type': 'large_files',
                    'count': len(large_files),
                    'total_size': sum(f['size'] for f in large_files),
                    'suggested_action': 'review_and_archive'
                })
            
            # 旧文件建议
            old_files = [f for f in self.file_info if (datetime.now() - f['modified']).days > 365]
            if old_files:
                suggestions.append({
                    'type': 'old_files',
                    'count': len(old_files),
                    'suggested_action': 'archive_or_delete'
                })
            
            return suggestions
        
        def format_size(self, size_bytes):
            """格式化文件大小"""
            for unit in ['B', 'KB', 'MB', 'GB']:
                if size_bytes < 1024:
                    return f"{size_bytes:.1f} {unit}"
                size_bytes /= 1024
            return f"{size_bytes:.1f} TB"
        
        def print_report(self):
            """打印报告"""
            print("\n文件统计报告:")
            print(f"  总文件数: {self.stats['total_files']}")
            print(f"  总大小: {self.format_size(self.stats['total_size'])}")
            
            print("\n按扩展名分布:")
            for ext, count in self.stats['by_extension'].most_common(10):
                print(f"  {ext}: {count} 个文件")
            
            print("\n按大小分布:")
            size_labels = {
                'tiny': '< 1KB',
                'small': '1KB - 1MB',
                'medium': '1MB - 10MB',
                'large': '10MB - 100MB',
                'huge': '> 100MB'
            }
            for size_range, count in self.stats['by_size_range'].items():
                print(f"  {size_labels[size_range]}: {count} 个文件")
            
            print("\n按修改时间分布:")
            date_labels = {
                'this_week': '本周',
                'this_month': '本月',
                'this_year': '今年',
                'older': '更早'
            }
            for date_range, count in self.stats['by_date_range'].items():
                print(f"  {date_labels[date_range]}: {count} 个文件")
            
            # 整理建议
            suggestions = self.generate_organization_suggestions()
            if suggestions:
                print("\n整理建议:")
                for i, suggestion in enumerate(suggestions, 1):
                    if suggestion['type'] == 'group_by_extension':
                        print(f"  {i}. 将 {suggestion['count']} 个 {suggestion['extension']} 文件移动到 '{suggestion['suggested_folder']}' 文件夹")
                    elif suggestion['type'] == 'large_files':
                        print(f"  {i}. 检查 {suggestion['count']} 个大文件 (总计 {self.format_size(suggestion['total_size'])})")
                    elif suggestion['type'] == 'old_files':
                        print(f"  {i}. 处理 {suggestion['count']} 个超过一年的旧文件")
    
    # 执行文件整理分析
    organizer = FileOrganizer()
    organizer.scan_directory()
    organizer.print_report()


def exercise_3_data_processor():
    """
    练习3: 数据处理管道
    
    功能：
    1. 从多种数据源读取数据
    2. 数据清洗和转换
    3. 统计分析
    4. 结果可视化（文本形式）
    """
    print("\n" + "=" * 60)
    print("练习3: 数据处理管道")
    print("=" * 60)
    
    # 学生成绩数据结构
    Student = namedtuple('Student', 'id name age grade math english science')
    
    class DataProcessor:
        def __init__(self):
            self.raw_data = []
            self.cleaned_data = []
            self.stats = {}
        
        def generate_sample_data(self, count=50):
            """生成示例学生数据"""
            names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']
            grades = ['A', 'B', 'C']
            
            for i in range(count):
                student = Student(
                    id=i + 1,
                    name=random.choice(names) + str(random.randint(1, 99)),
                    age=random.randint(16, 20),
                    grade=random.choice(grades),
                    math=random.randint(60, 100),
                    english=random.randint(60, 100),
                    science=random.randint(60, 100)
                )
                self.raw_data.append(student)
        
        def clean_data(self):
            """数据清洗"""
            print("执行数据清洗...")
            
            for student in self.raw_data:
                # 检查数据有效性
                if (student.math >= 0 and student.english >= 0 and student.science >= 0 and
                    student.age >= 16 and student.age <= 25):
                    self.cleaned_data.append(student)
            
            print(f"原始数据: {len(self.raw_data)} 条")
            print(f"清洗后数据: {len(self.cleaned_data)} 条")
            print(f"清洗掉: {len(self.raw_data) - len(self.cleaned_data)} 条")
        
        def calculate_statistics(self):
            """计算统计信息"""
            print("\n计算统计信息...")
            
            if not self.cleaned_data:
                return
            
            # 基本统计
            math_scores = [s.math for s in self.cleaned_data]
            english_scores = [s.english for s in self.cleaned_data]
            science_scores = [s.science for s in self.cleaned_data]
            ages = [s.age for s in self.cleaned_data]
            
            self.stats = {
                'total_students': len(self.cleaned_data),
                'math': {
                    'mean': statistics.mean(math_scores),
                    'median': statistics.median(math_scores),
                    'stdev': statistics.stdev(math_scores) if len(math_scores) > 1 else 0,
                    'min': min(math_scores),
                    'max': max(math_scores)
                },
                'english': {
                    'mean': statistics.mean(english_scores),
                    'median': statistics.median(english_scores),
                    'stdev': statistics.stdev(english_scores) if len(english_scores) > 1 else 0,
                    'min': min(english_scores),
                    'max': max(english_scores)
                },
                'science': {
                    'mean': statistics.mean(science_scores),
                    'median': statistics.median(science_scores),
                    'stdev': statistics.stdev(science_scores) if len(science_scores) > 1 else 0,
                    'min': min(science_scores),
                    'max': max(science_scores)
                },
                'age_distribution': Counter(ages),
                'grade_distribution': Counter(s.grade for s in self.cleaned_data)
            }
            
            # 计算总分和排名
            students_with_total = []
            for student in self.cleaned_data:
                total_score = student.math + student.english + student.science
                students_with_total.append((student, total_score))
            
            # 按总分排序
            students_with_total.sort(key=lambda x: x[1], reverse=True)
            self.stats['top_students'] = students_with_total[:5]
            self.stats['bottom_students'] = students_with_total[-5:]
            
            # 按年级分组统计
            grade_stats = defaultdict(list)
            for student in self.cleaned_data:
                total = student.math + student.english + student.science
                grade_stats[student.grade].append(total)
            
            self.stats['grade_performance'] = {}
            for grade, scores in grade_stats.items():
                self.stats['grade_performance'][grade] = {
                    'count': len(scores),
                    'average': statistics.mean(scores),
                    'median': statistics.median(scores)
                }
        
        def generate_report(self):
            """生成分析报告"""
            print("\n" + "=" * 40)
            print("数据分析报告")
            print("=" * 40)
            
            print(f"\n总学生数: {self.stats['total_students']}")
            
            # 各科成绩统计
            subjects = ['math', 'english', 'science']
            subject_names = {'math': '数学', 'english': '英语', 'science': '科学'}
            
            for subject in subjects:
                stats = self.stats[subject]
                print(f"\n{subject_names[subject]}成绩统计:")
                print(f"  平均分: {stats['mean']:.2f}")
                print(f"  中位数: {stats['median']:.2f}")
                print(f"  标准差: {stats['stdev']:.2f}")
                print(f"  最高分: {stats['max']}")
                print(f"  最低分: {stats['min']}")
            
            # 年龄分布
            print("\n年龄分布:")
            for age, count in sorted(self.stats['age_distribution'].items()):
                print(f"  {age}岁: {count}人")
            
            # 年级分布
            print("\n年级分布:")
            for grade, count in self.stats['grade_distribution'].items():
                print(f"  {grade}年级: {count}人")
            
            # 年级表现
            print("\n年级平均表现:")
            for grade, perf in self.stats['grade_performance'].items():
                print(f"  {grade}年级: 平均总分 {perf['average']:.2f} ({perf['count']}人)")
            
            # 优秀学生
            print("\n前5名学生:")
            for i, (student, total) in enumerate(self.stats['top_students'], 1):
                print(f"  {i}. {student.name} (总分: {total})")
        
        def save_results(self):
            """保存结果"""
            # 保存清洗后的数据为CSV
            with open('cleaned_student_data.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['ID', 'Name', 'Age', 'Grade', 'Math', 'English', 'Science', 'Total'])
                
                for student in self.cleaned_data:
                    total = student.math + student.english + student.science
                    writer.writerow([student.id, student.name, student.age, student.grade,
                                   student.math, student.english, student.science, total])
            
            # 保存统计结果为JSON
            # 需要处理不能序列化的对象
            serializable_stats = {}
            for key, value in self.stats.items():
                if key in ['top_students', 'bottom_students']:
                    # 转换为可序列化的格式
                    serializable_stats[key] = [
                        {
                            'name': student.name,
                            'grade': student.grade,
                            'total_score': total
                        }
                        for student, total in value
                    ]
                else:
                    serializable_stats[key] = value
            
            with open('student_statistics.json', 'w', encoding='utf-8') as f:
                json.dump(serializable_stats, f, indent=2, ensure_ascii=False)
            
            print("\n结果已保存:")
            print("  - cleaned_student_data.csv")
            print("  - student_statistics.json")
    
    # 执行数据处理
    processor = DataProcessor()
    processor.generate_sample_data()
    processor.clean_data()
    processor.calculate_statistics()
    processor.generate_report()
    processor.save_results()


def exercise_4_task_scheduler():
    """
    练习4: 任务调度系统
    
    功能：
    1. 任务优先级管理
    2. 任务执行调度
    3. 性能监控
    4. 结果统计
    """
    print("\n" + "=" * 60)
    print("练习4: 任务调度系统")
    print("=" * 60)
    
    class TaskPriority(IntEnum):
        LOW = 1
        NORMAL = 2
        HIGH = 3
        URGENT = 4
        CRITICAL = 5
    
    class TaskStatus(Enum):
        PENDING = "pending"
        RUNNING = "running"
        COMPLETED = "completed"
        FAILED = "failed"
    
    class Task:
        def __init__(self, task_id, name, priority, estimated_duration, func=None):
            self.task_id = task_id
            self.name = name
            self.priority = priority
            self.estimated_duration = estimated_duration
            self.func = func or self._default_task
            self.status = TaskStatus.PENDING
            self.created_time = datetime.now()
            self.start_time = None
            self.end_time = None
            self.actual_duration = None
            self.result = None
            self.error = None
        
        def _default_task(self):
            """默认任务函数"""
            import time
            # 模拟任务执行
            duration = random.uniform(0.1, self.estimated_duration)
            time.sleep(duration)
            return f"Task {self.name} completed in {duration:.2f}s"
        
        def execute(self):
            """执行任务"""
            self.status = TaskStatus.RUNNING
            self.start_time = datetime.now()
            
            try:
                self.result = self.func()
                self.status = TaskStatus.COMPLETED
            except Exception as e:
                self.error = str(e)
                self.status = TaskStatus.FAILED
            finally:
                self.end_time = datetime.now()
                self.actual_duration = (self.end_time - self.start_time).total_seconds()
        
        def __lt__(self, other):
            # 优先级高的任务排在前面（堆是最小堆，所以用负数）
            if self.priority != other.priority:
                return self.priority > other.priority
            # 相同优先级按创建时间排序
            return self.created_time < other.created_time
        
        def __repr__(self):
            return f"Task({self.task_id}, {self.name}, {self.priority.name})"
    
    class TaskScheduler:
        def __init__(self):
            self.task_queue = []  # 使用堆队列
            self.completed_tasks = []
            self.failed_tasks = []
            self.stats = {
                'total_tasks': 0,
                'completed_tasks': 0,
                'failed_tasks': 0,
                'total_execution_time': 0,
                'by_priority': Counter(),
                'by_status': Counter()
            }
        
        def add_task(self, task):
            """添加任务"""
            heapq.heappush(self.task_queue, task)
            self.stats['total_tasks'] += 1
            self.stats['by_priority'][task.priority.name] += 1
            print(f"添加任务: {task}")
        
        def execute_next_task(self):
            """执行下一个任务"""
            if not self.task_queue:
                return None
            
            task = heapq.heappop(self.task_queue)
            print(f"执行任务: {task.name} (优先级: {task.priority.name})")
            
            task.execute()
            
            if task.status == TaskStatus.COMPLETED:
                self.completed_tasks.append(task)
                self.stats['completed_tasks'] += 1
                print(f"  ✓ 完成: {task.result}")
            else:
                self.failed_tasks.append(task)
                self.stats['failed_tasks'] += 1
                print(f"  ✗ 失败: {task.error}")
            
            self.stats['total_execution_time'] += task.actual_duration
            self.stats['by_status'][task.status.value] += 1
            
            return task
        
        def execute_all_tasks(self):
            """执行所有任务"""
            print("\n开始执行所有任务...")
            
            while self.task_queue:
                self.execute_next_task()
            
            print("\n所有任务执行完成!")
        
        def generate_performance_report(self):
            """生成性能报告"""
            print("\n" + "=" * 40)
            print("任务执行性能报告")
            print("=" * 40)
            
            print(f"\n总任务数: {self.stats['total_tasks']}")
            print(f"完成任务: {self.stats['completed_tasks']}")
            print(f"失败任务: {self.stats['failed_tasks']}")
            print(f"成功率: {self.stats['completed_tasks']/self.stats['total_tasks']*100:.1f}%")
            print(f"总执行时间: {self.stats['total_execution_time']:.2f}秒")
            
            if self.completed_tasks:
                durations = [t.actual_duration for t in self.completed_tasks]
                print(f"平均执行时间: {statistics.mean(durations):.2f}秒")
                print(f"最快任务: {min(durations):.2f}秒")
                print(f"最慢任务: {max(durations):.2f}秒")
            
            print("\n按优先级分布:")
            for priority, count in self.stats['by_priority'].items():
                print(f"  {priority}: {count} 个任务")
            
            # 优先级vs执行时间分析
            if self.completed_tasks:
                priority_performance = defaultdict(list)
                for task in self.completed_tasks:
                    priority_performance[task.priority.name].append(task.actual_duration)
                
                print("\n优先级执行效率:")
                for priority, durations in priority_performance.items():
                    avg_duration = statistics.mean(durations)
                    print(f"  {priority}: 平均 {avg_duration:.2f}秒 ({len(durations)} 个任务)")
            
            # 时间估算准确性
            if self.completed_tasks:
                estimation_errors = []
                for task in self.completed_tasks:
                    error = abs(task.actual_duration - task.estimated_duration)
                    estimation_errors.append(error)
                
                avg_error = statistics.mean(estimation_errors)
                print(f"\n时间估算平均误差: {avg_error:.2f}秒")
    
    # 创建任务调度器
    scheduler = TaskScheduler()
    
    # 添加各种优先级的任务
    tasks_data = [
        (1, "数据备份", TaskPriority.LOW, 2.0),
        (2, "发送邮件", TaskPriority.NORMAL, 0.5),
        (3, "系统更新", TaskPriority.HIGH, 3.0),
        (4, "安全扫描", TaskPriority.URGENT, 1.5),
        (5, "紧急修复", TaskPriority.CRITICAL, 1.0),
        (6, "日志清理", TaskPriority.LOW, 1.0),
        (7, "用户通知", TaskPriority.NORMAL, 0.3),
        (8, "数据同步", TaskPriority.HIGH, 2.5),
        (9, "监控检查", TaskPriority.URGENT, 0.8),
        (10, "故障恢复", TaskPriority.CRITICAL, 1.2)
    ]
    
    # 随机顺序添加任务（测试优先级排序）
    random.shuffle(tasks_data)
    
    for task_id, name, priority, duration in tasks_data:
        task = Task(task_id, name, priority, duration)
        scheduler.add_task(task)
    
    # 执行所有任务
    scheduler.execute_all_tasks()
    
    # 生成性能报告
    scheduler.generate_performance_report()


def exercise_5_web_crawler():
    """
    练习5: 简单网页爬虫
    
    功能：
    1. 网页内容获取
    2. 链接提取
    3. 数据解析
    4. 结果存储
    
    注意：这是一个简化的示例，实际使用时需要考虑robots.txt、请求频率等
    """
    print("\n" + "=" * 60)
    print("练习5: 简单网页爬虫")
    print("=" * 60)
    
    class WebCrawler:
        def __init__(self):
            self.visited_urls = set()
            self.url_queue = deque()
            self.crawl_data = []
            self.stats = {
                'total_requests': 0,
                'successful_requests': 0,
                'failed_requests': 0,
                'total_links_found': 0
            }
        
        def add_url(self, url):
            """添加URL到爬取队列"""
            if url not in self.visited_urls:
                self.url_queue.append(url)
        
        def fetch_page(self, url, timeout=10):
            """获取网页内容"""
            try:
                self.stats['total_requests'] += 1
                
                # 创建请求
                req = urllib.request.Request(
                    url,
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Python Web Crawler Exercise)'
                    }
                )
                
                with urllib.request.urlopen(req, timeout=timeout) as response:
                    content = response.read().decode('utf-8', errors='ignore')
                    self.stats['successful_requests'] += 1
                    return content
                    
            except Exception as e:
                self.stats['failed_requests'] += 1
                print(f"  获取失败 {url}: {e}")
                return None
        
        def extract_links(self, content, base_url):
            """提取页面中的链接"""
            if not content:
                return []
            
            # 简单的链接提取（使用正则表达式）
            link_pattern = r'href=["\']([^"\'>]+)["\']'
            links = re.findall(link_pattern, content, re.IGNORECASE)
            
            # 处理相对链接
            absolute_links = []
            for link in links:
                if link.startswith('http'):
                    absolute_links.append(link)
                elif link.startswith('/'):
                    # 相对于根目录的链接
                    parsed_base = urllib.parse.urlparse(base_url)
                    absolute_link = f"{parsed_base.scheme}://{parsed_base.netloc}{link}"
                    absolute_links.append(absolute_link)
            
            self.stats['total_links_found'] += len(absolute_links)
            return absolute_links
        
        def extract_text_content(self, content):
            """提取文本内容"""
            if not content:
                return ""
            
            # 移除HTML标签（简单方法）
            text = re.sub(r'<[^>]+>', ' ', content)
            # 清理多余空白
            text = re.sub(r'\s+', ' ', text).strip()
            return text
        
        def crawl(self, start_urls, max_pages=5):
            """开始爬取"""
            print(f"开始爬取，最大页面数: {max_pages}")
            
            # 添加起始URL
            for url in start_urls:
                self.add_url(url)
            
            pages_crawled = 0
            
            while self.url_queue and pages_crawled < max_pages:
                url = self.url_queue.popleft()
                
                if url in self.visited_urls:
                    continue
                
                print(f"\n正在爬取: {url}")
                self.visited_urls.add(url)
                
                # 获取页面内容
                content = self.fetch_page(url)
                
                if content:
                    # 提取链接
                    links = self.extract_links(content, url)
                    print(f"  找到 {len(links)} 个链接")
                    
                    # 提取文本内容
                    text_content = self.extract_text_content(content)
                    
                    # 存储爬取数据
                    page_data = {
                        'url': url,
                        'title': self._extract_title(content),
                        'content_length': len(content),
                        'text_length': len(text_content),
                        'links_count': len(links),
                        'links': links[:10],  # 只保存前10个链接
                        'crawl_time': datetime.now().isoformat(),
                        'word_count': len(text_content.split())
                    }
                    
                    self.crawl_data.append(page_data)
                    
                    # 添加新发现的链接到队列（限制数量）
                    for link in links[:5]:  # 只添加前5个链接
                        self.add_url(link)
                    
                    pages_crawled += 1
                    print(f"  页面大小: {len(content)} 字符")
                    print(f"  文本长度: {len(text_content)} 字符")
                    print(f"  单词数: {len(text_content.split())}")
                
                # 添加延迟，避免过于频繁的请求
                import time
                time.sleep(1)
            
            print(f"\n爬取完成，共处理 {pages_crawled} 个页面")
        
        def _extract_title(self, content):
            """提取页面标题"""
            title_match = re.search(r'<title[^>]*>([^<]+)</title>', content, re.IGNORECASE)
            return title_match.group(1).strip() if title_match else "无标题"
        
        def generate_report(self):
            """生成爬取报告"""
            print("\n" + "=" * 40)
            print("爬取报告")
            print("=" * 40)
            
            print(f"\n请求统计:")
            print(f"  总请求数: {self.stats['total_requests']}")
            print(f"  成功请求: {self.stats['successful_requests']}")
            print(f"  失败请求: {self.stats['failed_requests']}")
            print(f"  成功率: {self.stats['successful_requests']/self.stats['total_requests']*100:.1f}%")
            print(f"  发现链接总数: {self.stats['total_links_found']}")
            
            if self.crawl_data:
                # 内容统计
                content_lengths = [page['content_length'] for page in self.crawl_data]
                word_counts = [page['word_count'] for page in self.crawl_data]
                
                print(f"\n内容统计:")
                print(f"  平均页面大小: {statistics.mean(content_lengths):.0f} 字符")
                print(f"  平均单词数: {statistics.mean(word_counts):.0f} 个")
                print(f"  最大页面: {max(content_lengths)} 字符")
                print(f"  最小页面: {min(content_lengths)} 字符")
                
                # 页面信息
                print(f"\n爬取的页面:")
                for i, page in enumerate(self.crawl_data, 1):
                    print(f"  {i}. {page['title'][:50]}...")
                    print(f"     URL: {page['url']}")
                    print(f"     大小: {page['content_length']} 字符, {page['word_count']} 单词")
        
        def save_results(self):
            """保存爬取结果"""
            # 保存为JSON
            with open('crawl_results.json', 'w', encoding='utf-8') as f:
                json.dump({
                    'stats': self.stats,
                    'pages': self.crawl_data
                }, f, indent=2, ensure_ascii=False)
            
            # 保存为CSV
            with open('crawl_summary.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['URL', 'Title', 'Content Length', 'Word Count', 'Links Count', 'Crawl Time'])
                
                for page in self.crawl_data:
                    writer.writerow([
                        page['url'],
                        page['title'],
                        page['content_length'],
                        page['word_count'],
                        page['links_count'],
                        page['crawl_time']
                    ])
            
            print("\n结果已保存:")
            print("  - crawl_results.json")
            print("  - crawl_summary.csv")
    
    # 注意：这里使用一些公开的、允许爬取的网站作为示例
    # 实际使用时请确保遵守网站的robots.txt和使用条款
    
    print("注意: 这是一个教学示例，实际使用时请遵守网站的robots.txt和使用条款")
    print("由于网络连接和网站可用性的限制，这里只演示爬虫的基本结构")
    
    crawler = WebCrawler()
    
    # 模拟爬取结果（避免实际网络请求）
    print("\n模拟爬取过程...")
    
    # 生成模拟数据
    sample_pages = [
        {
            'url': 'https://example.com/page1',
            'title': 'Python编程教程',
            'content_length': 5420,
            'text_length': 3200,
            'links_count': 15,
            'links': ['https://example.com/tutorial1', 'https://example.com/tutorial2'],
            'crawl_time': datetime.now().isoformat(),
            'word_count': 580
        },
        {
            'url': 'https://example.com/page2',
            'title': '数据结构与算法',
            'content_length': 7830,
            'text_length': 4500,
            'links_count': 22,
            'links': ['https://example.com/algorithm1', 'https://example.com/datastructure1'],
            'crawl_time': datetime.now().isoformat(),
            'word_count': 720
        },
        {
            'url': 'https://example.com/page3',
            'title': 'Web开发实践',
            'content_length': 6200,
            'text_length': 3800,
            'links_count': 18,
            'links': ['https://example.com/web1', 'https://example.com/web2'],
            'crawl_time': datetime.now().isoformat(),
            'word_count': 650
        }
    ]
    
    crawler.crawl_data = sample_pages
    crawler.stats = {
        'total_requests': 3,
        'successful_requests': 3,
        'failed_requests': 0,
        'total_links_found': 55
    }
    
    crawler.generate_report()
    crawler.save_results()


def main():
    """主函数 - 运行所有练习"""
    print("Python标准库综合练习")
    print("=" * 80)
    print("本练习整合了前面学习的所有标准库模块")
    print("包括：文件操作、时间处理、数据处理、网络编程、正则表达式、")
    print("      数学运算、集合数据结构等")
    print("=" * 80)
    
    try:
        # 练习1：日志分析器
        exercise_1_log_analyzer()
        
        # 练习2：文件整理器
        exercise_2_file_organizer()
        
        # 练习3：数据处理管道
        exercise_3_data_processor()
        
        # 练习4：任务调度系统
        exercise_4_task_scheduler()
        
        # 练习5：网页爬虫
        exercise_5_web_crawler()
        
    except KeyboardInterrupt:
        print("\n练习被用户中断")
    except Exception as e:
        print(f"\n练习执行出错: {e}")
    
    print("\n" + "=" * 60)
    print("综合练习总结")
    print("=" * 60)
    print("通过这些练习，你应该掌握了：")
    print("1. 多个标准库模块的协同使用")
    print("2. 实际问题的分析和解决")
    print("3. 数据处理和分析的基本流程")
    print("4. 文件操作和数据持久化")
    print("5. 网络编程和数据获取")
    print("6. 任务调度和优先级管理")
    print("7. 正则表达式在文本处理中的应用")
    print("8. 统计分析和报告生成")
    print("9. 错误处理和异常管理")
    print("10. 代码组织和模块化设计")
    print("\n继续学习更高级的Python特性和第三方库！")


if __name__ == "__main__":
    main()