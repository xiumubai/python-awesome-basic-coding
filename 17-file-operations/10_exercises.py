#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python文件操作 - 综合练习

本模块包含文件操作的综合练习题，涵盖：
1. 文本文件处理练习
2. 二进制文件操作练习
3. 文件系统操作练习
4. 异常处理练习
5. 实际应用场景练习
6. 性能优化练习
7. 高级文件操作练习

作者：Python学习助手
日期：2024年
"""

import os
import sys
import json
import csv
import shutil
import hashlib
import logging
import tempfile
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
from collections import defaultdict, Counter
import time
import random


# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FileExercises:
    """文件操作练习类"""
    
    def __init__(self):
        self.exercise_dir = Path('exercises_temp')
        self.exercise_dir.mkdir(exist_ok=True)
        self.results = {}
    
    def cleanup(self):
        """清理练习文件"""
        if self.exercise_dir.exists():
            shutil.rmtree(self.exercise_dir)
    
    def exercise_1_text_processing(self):
        """
        练习1：文本文件处理
        任务：处理一个包含学生成绩的文本文件
        """
        print("\n=== 练习1：文本文件处理 ===")
        print("任务：处理学生成绩文件，计算统计信息")
        
        # 创建测试数据
        grades_data = """
张三,数学,85
张三,语文,92
张三,英语,78
李四,数学,90
李四,语文,88
李四,英语,95
王五,数学,76
王五,语文,82
王五,英语,89
赵六,数学,94
赵六,语文,87
赵六,英语,91
"""
        
        grades_file = self.exercise_dir / 'grades.txt'
        grades_file.write_text(grades_data.strip(), encoding='utf-8')
        
        try:
            # 解决方案
            student_grades = defaultdict(dict)
            subject_scores = defaultdict(list)
            
            # 读取并解析数据
            with open(grades_file, 'r', encoding='utf-8') as f:
                for line in f:
                    name, subject, score = line.strip().split(',')
                    score = int(score)
                    student_grades[name][subject] = score
                    subject_scores[subject].append(score)
            
            # 计算每个学生的平均分
            print("\n学生平均分：")
            for name, grades in student_grades.items():
                avg_score = sum(grades.values()) / len(grades)
                print(f"{name}: {avg_score:.2f}")
            
            # 计算每科的平均分
            print("\n科目平均分：")
            for subject, scores in subject_scores.items():
                avg_score = sum(scores) / len(scores)
                print(f"{subject}: {avg_score:.2f}")
            
            # 找出最高分和最低分
            all_scores = []
            for grades in student_grades.values():
                all_scores.extend(grades.values())
            
            print(f"\n最高分: {max(all_scores)}")
            print(f"最低分: {min(all_scores)}")
            
            # 生成成绩报告
            report_file = self.exercise_dir / 'grade_report.txt'
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write("学生成绩报告\n")
                f.write("=" * 30 + "\n\n")
                
                for name, grades in student_grades.items():
                    f.write(f"学生：{name}\n")
                    for subject, score in grades.items():
                        f.write(f"  {subject}: {score}\n")
                    avg = sum(grades.values()) / len(grades)
                    f.write(f"  平均分: {avg:.2f}\n\n")
            
            print(f"成绩报告已生成：{report_file}")
            self.results['exercise_1'] = '完成'
            
        except Exception as e:
            print(f"练习1失败：{e}")
            self.results['exercise_1'] = f'失败: {e}'
    
    def exercise_2_csv_processing(self):
        """
        练习2：CSV文件处理
        任务：处理销售数据CSV文件
        """
        print("\n=== 练习2：CSV文件处理 ===")
        print("任务：分析销售数据，生成统计报告")
        
        # 创建测试CSV数据
        sales_data = [
            ['日期', '产品', '销售员', '数量', '单价'],
            ['2024-01-01', '笔记本电脑', '张三', '2', '5000'],
            ['2024-01-01', '鼠标', '张三', '5', '50'],
            ['2024-01-02', '键盘', '李四', '3', '200'],
            ['2024-01-02', '笔记本电脑', '李四', '1', '5000'],
            ['2024-01-03', '显示器', '王五', '2', '1500'],
            ['2024-01-03', '鼠标', '王五', '10', '50'],
            ['2024-01-04', '笔记本电脑', '张三', '3', '5000'],
            ['2024-01-04', '键盘', '赵六', '5', '200'],
        ]
        
        sales_file = self.exercise_dir / 'sales.csv'
        
        try:
            # 写入CSV文件
            with open(sales_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(sales_data)
            
            # 读取并分析CSV数据
            sales_records = []
            with open(sales_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row['数量'] = int(row['数量'])
                    row['单价'] = float(row['单价'])
                    row['总额'] = row['数量'] * row['单价']
                    sales_records.append(row)
            
            # 统计分析
            total_sales = sum(record['总额'] for record in sales_records)
            print(f"总销售额：{total_sales:,.2f}元")
            
            # 按产品统计
            product_sales = defaultdict(float)
            for record in sales_records:
                product_sales[record['产品']] += record['总额']
            
            print("\n产品销售额排行：")
            for product, amount in sorted(product_sales.items(), key=lambda x: x[1], reverse=True):
                print(f"{product}: {amount:,.2f}元")
            
            # 按销售员统计
            salesperson_sales = defaultdict(float)
            for record in sales_records:
                salesperson_sales[record['销售员']] += record['总额']
            
            print("\n销售员业绩排行：")
            for person, amount in sorted(salesperson_sales.items(), key=lambda x: x[1], reverse=True):
                print(f"{person}: {amount:,.2f}元")
            
            # 生成详细报告CSV
            report_file = self.exercise_dir / 'sales_report.csv'
            with open(report_file, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['日期', '产品', '销售员', '数量', '单价', '总额']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(sales_records)
            
            print(f"详细报告已生成：{report_file}")
            self.results['exercise_2'] = '完成'
            
        except Exception as e:
            print(f"练习2失败：{e}")
            self.results['exercise_2'] = f'失败: {e}'
    
    def exercise_3_json_config(self):
        """
        练习3：JSON配置文件处理
        任务：创建和管理应用程序配置
        """
        print("\n=== 练习3：JSON配置文件处理 ===")
        print("任务：管理应用程序配置文件")
        
        try:
            # 默认配置
            default_config = {
                'app': {
                    'name': 'MyApp',
                    'version': '1.0.0',
                    'debug': False
                },
                'database': {
                    'host': 'localhost',
                    'port': 5432,
                    'name': 'myapp_db',
                    'user': 'admin'
                },
                'logging': {
                    'level': 'INFO',
                    'file': 'app.log',
                    'max_size': '10MB'
                },
                'features': {
                    'email_notifications': True,
                    'auto_backup': True,
                    'analytics': False
                }
            }
            
            config_file = self.exercise_dir / 'config.json'
            
            # 保存默认配置
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(default_config, f, indent=2, ensure_ascii=False)
            
            print(f"默认配置已创建：{config_file}")
            
            # 读取配置
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            print("\n当前配置：")
            print(json.dumps(config, indent=2, ensure_ascii=False))
            
            # 修改配置
            config['app']['debug'] = True
            config['database']['port'] = 3306
            config['features']['analytics'] = True
            
            # 添加新的配置项
            config['cache'] = {
                'type': 'redis',
                'host': 'localhost',
                'port': 6379,
                'ttl': 3600
            }
            
            # 保存修改后的配置
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            print("\n配置已更新")
            
            # 创建配置备份
            backup_file = self.exercise_dir / f'config_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
            shutil.copy2(config_file, backup_file)
            print(f"配置备份已创建：{backup_file}")
            
            # 验证配置
            def validate_config(cfg):
                """验证配置文件"""
                required_keys = ['app', 'database', 'logging']
                for key in required_keys:
                    if key not in cfg:
                        raise ValueError(f"缺少必需的配置项：{key}")
                
                if not isinstance(cfg['database']['port'], int):
                    raise ValueError("数据库端口必须是整数")
                
                if cfg['database']['port'] < 1 or cfg['database']['port'] > 65535:
                    raise ValueError("数据库端口必须在1-65535范围内")
                
                return True
            
            validate_config(config)
            print("配置验证通过")
            
            self.results['exercise_3'] = '完成'
            
        except Exception as e:
            print(f"练习3失败：{e}")
            self.results['exercise_3'] = f'失败: {e}'
    
    def exercise_4_binary_file_analysis(self):
        """
        练习4：二进制文件分析
        任务：分析文件类型和计算文件哈希
        """
        print("\n=== 练习4：二进制文件分析 ===")
        print("任务：分析文件类型，计算哈希值")
        
        try:
            # 创建不同类型的测试文件
            test_files = {
                'text.txt': b'Hello, World! This is a text file.',
                'image.png': b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde',
                'pdf.pdf': b'%PDF-1.4\n1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj',
                'zip.zip': b'PK\x03\x04\x14\x00\x00\x00\x08\x00',
                'exe.exe': b'MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00'
            }
            
            # 文件类型签名
            file_signatures = {
                b'\x89PNG': 'PNG图像',
                b'%PDF': 'PDF文档',
                b'PK\x03\x04': 'ZIP压缩文件',
                b'MZ': 'Windows可执行文件',
                b'\xff\xd8\xff': 'JPEG图像',
                b'GIF8': 'GIF图像'
            }
            
            # 创建测试文件
            for filename, content in test_files.items():
                file_path = self.exercise_dir / filename
                file_path.write_bytes(content)
            
            print("\n文件分析结果：")
            print("-" * 60)
            
            for filename in test_files.keys():
                file_path = self.exercise_dir / filename
                
                # 读取文件头
                with open(file_path, 'rb') as f:
                    header = f.read(16)
                
                # 识别文件类型
                file_type = '未知类型'
                for signature, type_name in file_signatures.items():
                    if header.startswith(signature):
                        file_type = type_name
                        break
                
                # 计算文件大小
                file_size = file_path.stat().st_size
                
                # 计算MD5哈希
                md5_hash = hashlib.md5()
                with open(file_path, 'rb') as f:
                    for chunk in iter(lambda: f.read(4096), b''):
                        md5_hash.update(chunk)
                
                # 计算SHA256哈希
                sha256_hash = hashlib.sha256()
                with open(file_path, 'rb') as f:
                    for chunk in iter(lambda: f.read(4096), b''):
                        sha256_hash.update(chunk)
                
                print(f"文件名: {filename}")
                print(f"类型: {file_type}")
                print(f"大小: {file_size} 字节")
                print(f"MD5: {md5_hash.hexdigest()}")
                print(f"SHA256: {sha256_hash.hexdigest()}")
                print(f"文件头: {header.hex()[:32]}...")
                print("-" * 60)
            
            # 生成分析报告
            report_file = self.exercise_dir / 'file_analysis_report.txt'
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write("文件分析报告\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"分析时间: {datetime.now()}\n")
                f.write(f"分析文件数量: {len(test_files)}\n\n")
                
                for filename in test_files.keys():
                    file_path = self.exercise_dir / filename
                    file_size = file_path.stat().st_size
                    
                    with open(file_path, 'rb') as file:
                        header = file.read(16)
                    
                    file_type = '未知类型'
                    for signature, type_name in file_signatures.items():
                        if header.startswith(signature):
                            file_type = type_name
                            break
                    
                    f.write(f"文件: {filename}\n")
                    f.write(f"类型: {file_type}\n")
                    f.write(f"大小: {file_size} 字节\n")
                    f.write(f"修改时间: {datetime.fromtimestamp(file_path.stat().st_mtime)}\n\n")
            
            print(f"分析报告已生成：{report_file}")
            self.results['exercise_4'] = '完成'
            
        except Exception as e:
            print(f"练习4失败：{e}")
            self.results['exercise_4'] = f'失败: {e}'
    
    def exercise_5_log_analysis(self):
        """
        练习5：日志文件分析
        任务：分析Web服务器日志
        """
        print("\n=== 练习5：日志文件分析 ===")
        print("任务：分析Web服务器访问日志")
        
        try:
            # 生成模拟日志数据
            log_entries = []
            ips = ['192.168.1.100', '10.0.0.50', '172.16.0.25', '203.0.113.10', '198.51.100.5']
            paths = ['/', '/index.html', '/about.html', '/contact.html', '/api/users', '/api/products', '/login', '/admin']
            status_codes = [200, 200, 200, 200, 404, 500, 301, 403]
            user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            ]
            
            # 生成100条日志记录
            for i in range(100):
                timestamp = datetime.now().strftime('%d/%b/%Y:%H:%M:%S +0000')
                ip = random.choice(ips)
                path = random.choice(paths)
                status = random.choice(status_codes)
                size = random.randint(100, 10000)
                user_agent = random.choice(user_agents)
                
                log_entry = f'{ip} - - [{timestamp}] "GET {path} HTTP/1.1" {status} {size} "-" "{user_agent}"'
                log_entries.append(log_entry)
            
            # 写入日志文件
            log_file = self.exercise_dir / 'access.log'
            with open(log_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(log_entries))
            
            print(f"模拟日志文件已创建：{log_file}")
            
            # 分析日志
            ip_counter = Counter()
            path_counter = Counter()
            status_counter = Counter()
            total_bytes = 0
            error_logs = []
            
            with open(log_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    try:
                        # 简单的日志解析（实际应用中可能需要更复杂的正则表达式）
                        parts = line.strip().split()
                        if len(parts) >= 10:
                            ip = parts[0]
                            path = parts[6]
                            status = parts[8]
                            size = int(parts[9]) if parts[9].isdigit() else 0
                            
                            ip_counter[ip] += 1
                            path_counter[path] += 1
                            status_counter[status] += 1
                            total_bytes += size
                            
                            # 记录错误日志
                            if status.startswith('4') or status.startswith('5'):
                                error_logs.append((line_num, line.strip()))
                    
                    except (ValueError, IndexError) as e:
                        print(f"解析第{line_num}行时出错：{e}")
            
            # 生成分析报告
            print("\n=== 日志分析结果 ===")
            
            print(f"\n总请求数：{sum(ip_counter.values())}")
            print(f"总流量：{total_bytes:,} 字节 ({total_bytes/1024/1024:.2f} MB)")
            print(f"错误请求数：{len(error_logs)}")
            
            print("\n访问最多的IP地址：")
            for ip, count in ip_counter.most_common(5):
                print(f"{ip}: {count} 次")
            
            print("\n访问最多的页面：")
            for path, count in path_counter.most_common(5):
                print(f"{path}: {count} 次")
            
            print("\n状态码分布：")
            for status, count in status_counter.most_common():
                print(f"{status}: {count} 次")
            
            # 生成详细报告文件
            report_file = self.exercise_dir / 'log_analysis_report.txt'
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write("Web服务器日志分析报告\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"分析时间: {datetime.now()}\n")
                f.write(f"日志文件: {log_file}\n")
                f.write(f"总请求数: {sum(ip_counter.values())}\n")
                f.write(f"总流量: {total_bytes:,} 字节\n")
                f.write(f"错误请求数: {len(error_logs)}\n\n")
                
                f.write("访问最多的IP地址:\n")
                for ip, count in ip_counter.most_common(10):
                    f.write(f"{ip}: {count} 次\n")
                
                f.write("\n访问最多的页面:\n")
                for path, count in path_counter.most_common(10):
                    f.write(f"{path}: {count} 次\n")
                
                f.write("\n状态码分布:\n")
                for status, count in status_counter.most_common():
                    f.write(f"{status}: {count} 次\n")
                
                if error_logs:
                    f.write("\n错误日志记录:\n")
                    for line_num, log_line in error_logs[:20]:  # 只显示前20条错误
                        f.write(f"第{line_num}行: {log_line}\n")
            
            print(f"详细报告已生成：{report_file}")
            self.results['exercise_5'] = '完成'
            
        except Exception as e:
            print(f"练习5失败：{e}")
            self.results['exercise_5'] = f'失败: {e}'
    
    def exercise_6_file_backup_system(self):
        """
        练习6：文件备份系统
        任务：实现一个简单的文件备份系统
        """
        print("\n=== 练习6：文件备份系统 ===")
        print("任务：实现文件备份和恢复功能")
        
        try:
            # 创建源文件目录和文件
            source_dir = self.exercise_dir / 'source'
            backup_dir = self.exercise_dir / 'backup'
            source_dir.mkdir(exist_ok=True)
            backup_dir.mkdir(exist_ok=True)
            
            # 创建一些测试文件
            test_files = {
                'document1.txt': '这是第一个文档的内容',
                'document2.txt': '这是第二个文档的内容',
                'config.json': json.dumps({'setting1': 'value1', 'setting2': 'value2'}, indent=2),
                'data.csv': 'name,age,city\nAlice,25,New York\nBob,30,London'
            }
            
            for filename, content in test_files.items():
                (source_dir / filename).write_text(content, encoding='utf-8')
            
            print(f"源文件已创建在：{source_dir}")
            
            def create_backup(src_dir: Path, backup_dir: Path, backup_name: str = None):
                """创建备份"""
                if not backup_name:
                    backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                
                backup_path = backup_dir / backup_name
                backup_path.mkdir(exist_ok=True)
                
                backup_info = {
                    'timestamp': datetime.now().isoformat(),
                    'source_dir': str(src_dir),
                    'files': []
                }
                
                # 复制文件并记录信息
                for file_path in src_dir.rglob('*'):
                    if file_path.is_file():
                        relative_path = file_path.relative_to(src_dir)
                        dest_path = backup_path / relative_path
                        dest_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        shutil.copy2(file_path, dest_path)
                        
                        # 计算文件哈希
                        with open(file_path, 'rb') as f:
                            file_hash = hashlib.md5(f.read()).hexdigest()
                        
                        backup_info['files'].append({
                            'path': str(relative_path),
                            'size': file_path.stat().st_size,
                            'modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                            'hash': file_hash
                        })
                
                # 保存备份信息
                info_file = backup_path / 'backup_info.json'
                with open(info_file, 'w', encoding='utf-8') as f:
                    json.dump(backup_info, f, indent=2, ensure_ascii=False)
                
                return backup_path, backup_info
            
            def list_backups(backup_dir: Path):
                """列出所有备份"""
                backups = []
                for backup_path in backup_dir.iterdir():
                    if backup_path.is_dir():
                        info_file = backup_path / 'backup_info.json'
                        if info_file.exists():
                            with open(info_file, 'r', encoding='utf-8') as f:
                                backup_info = json.load(f)
                            backups.append((backup_path.name, backup_info))
                return sorted(backups, key=lambda x: x[1]['timestamp'], reverse=True)
            
            def restore_backup(backup_dir: Path, backup_name: str, restore_dir: Path):
                """恢复备份"""
                backup_path = backup_dir / backup_name
                info_file = backup_path / 'backup_info.json'
                
                if not info_file.exists():
                    raise FileNotFoundError(f"备份信息文件不存在：{info_file}")
                
                with open(info_file, 'r', encoding='utf-8') as f:
                    backup_info = json.load(f)
                
                restore_dir.mkdir(parents=True, exist_ok=True)
                
                restored_files = []
                for file_info in backup_info['files']:
                    src_file = backup_path / file_info['path']
                    dest_file = restore_dir / file_info['path']
                    dest_file.parent.mkdir(parents=True, exist_ok=True)
                    
                    shutil.copy2(src_file, dest_file)
                    restored_files.append(file_info['path'])
                
                return restored_files
            
            # 执行备份操作
            print("\n创建备份...")
            backup_path, backup_info = create_backup(source_dir, backup_dir)
            print(f"备份已创建：{backup_path}")
            print(f"备份了 {len(backup_info['files'])} 个文件")
            
            # 修改源文件
            print("\n修改源文件...")
            (source_dir / 'document1.txt').write_text('修改后的文档内容', encoding='utf-8')
            (source_dir / 'new_file.txt').write_text('这是新添加的文件', encoding='utf-8')
            
            # 创建第二个备份
            time.sleep(1)  # 确保时间戳不同
            backup_path2, backup_info2 = create_backup(source_dir, backup_dir)
            print(f"第二个备份已创建：{backup_path2}")
            
            # 列出所有备份
            print("\n可用的备份：")
            backups = list_backups(backup_dir)
            for i, (backup_name, info) in enumerate(backups, 1):
                print(f"{i}. {backup_name} - {info['timestamp']} ({len(info['files'])} 个文件)")
            
            # 恢复第一个备份
            print("\n恢复第一个备份...")
            restore_dir = self.exercise_dir / 'restored'
            if backups:
                first_backup_name = backups[-1][0]  # 最早的备份
                restored_files = restore_backup(backup_dir, first_backup_name, restore_dir)
                print(f"已恢复 {len(restored_files)} 个文件到：{restore_dir}")
                
                # 验证恢复的文件
                print("\n恢复的文件内容：")
                for filename in ['document1.txt', 'document2.txt']:
                    restored_file = restore_dir / filename
                    if restored_file.exists():
                        content = restored_file.read_text(encoding='utf-8')
                        print(f"{filename}: {content[:50]}...")
            
            self.results['exercise_6'] = '完成'
            
        except Exception as e:
            print(f"练习6失败：{e}")
            self.results['exercise_6'] = f'失败: {e}'
    
    def exercise_7_performance_optimization(self):
        """
        练习7：文件操作性能优化
        任务：比较不同文件操作方法的性能
        """
        print("\n=== 练习7：文件操作性能优化 ===")
        print("任务：测试和优化文件操作性能")
        
        try:
            # 创建大文件用于测试
            test_file = self.exercise_dir / 'large_test_file.txt'
            
            print("创建测试文件...")
            with open(test_file, 'w', encoding='utf-8') as f:
                for i in range(10000):
                    f.write(f"这是第{i+1}行的测试数据，包含一些随机内容用于测试文件操作性能。\n")
            
            file_size = test_file.stat().st_size
            print(f"测试文件大小：{file_size:,} 字节 ({file_size/1024/1024:.2f} MB)")
            
            def time_operation(operation_name: str, operation_func):
                """测量操作时间"""
                start_time = time.time()
                result = operation_func()
                end_time = time.time()
                duration = end_time - start_time
                print(f"{operation_name}: {duration:.4f}秒")
                return result, duration
            
            # 测试1：不同的读取方法
            print("\n=== 读取性能测试 ===")
            
            def read_all_at_once():
                with open(test_file, 'r', encoding='utf-8') as f:
                    return len(f.read())
            
            def read_line_by_line():
                count = 0
                with open(test_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        count += len(line)
                return count
            
            def read_with_buffer():
                count = 0
                with open(test_file, 'r', encoding='utf-8', buffering=8192) as f:
                    while True:
                        chunk = f.read(1024)
                        if not chunk:
                            break
                        count += len(chunk)
                return count
            
            def read_with_readlines():
                with open(test_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                return sum(len(line) for line in lines)
            
            # 执行读取测试
            read_results = {}
            read_results['read_all'], read_results['read_all_time'] = time_operation("一次性读取全部", read_all_at_once)
            read_results['read_lines'], read_results['read_lines_time'] = time_operation("逐行读取", read_line_by_line)
            read_results['read_buffer'], read_results['read_buffer_time'] = time_operation("缓冲读取", read_with_buffer)
            read_results['read_readlines'], read_results['read_readlines_time'] = time_operation("readlines读取", read_with_readlines)
            
            # 测试2：不同的写入方法
            print("\n=== 写入性能测试 ===")
            
            test_data = [f"测试行{i}\n" for i in range(5000)]
            
            def write_all_at_once():
                output_file = self.exercise_dir / 'write_test_1.txt'
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(''.join(test_data))
                return output_file.stat().st_size
            
            def write_line_by_line():
                output_file = self.exercise_dir / 'write_test_2.txt'
                with open(output_file, 'w', encoding='utf-8') as f:
                    for line in test_data:
                        f.write(line)
                return output_file.stat().st_size
            
            def write_with_writelines():
                output_file = self.exercise_dir / 'write_test_3.txt'
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.writelines(test_data)
                return output_file.stat().st_size
            
            def write_with_buffer():
                output_file = self.exercise_dir / 'write_test_4.txt'
                with open(output_file, 'w', encoding='utf-8', buffering=8192) as f:
                    for line in test_data:
                        f.write(line)
                return output_file.stat().st_size
            
            # 执行写入测试
            write_results = {}
            write_results['write_all'], write_results['write_all_time'] = time_operation("一次性写入全部", write_all_at_once)
            write_results['write_lines'], write_results['write_lines_time'] = time_operation("逐行写入", write_line_by_line)
            write_results['write_writelines'], write_results['write_writelines_time'] = time_operation("writelines写入", write_with_writelines)
            write_results['write_buffer'], write_results['write_buffer_time'] = time_operation("缓冲写入", write_with_buffer)
            
            # 测试3：文件复制性能
            print("\n=== 文件复制性能测试 ===")
            
            def copy_with_shutil():
                dest_file = self.exercise_dir / 'copy_shutil.txt'
                shutil.copy2(test_file, dest_file)
                return dest_file.stat().st_size
            
            def copy_with_read_write():
                dest_file = self.exercise_dir / 'copy_manual.txt'
                with open(test_file, 'rb') as src, open(dest_file, 'wb') as dst:
                    dst.write(src.read())
                return dest_file.stat().st_size
            
            def copy_with_chunks():
                dest_file = self.exercise_dir / 'copy_chunks.txt'
                with open(test_file, 'rb') as src, open(dest_file, 'wb') as dst:
                    while True:
                        chunk = src.read(8192)
                        if not chunk:
                            break
                        dst.write(chunk)
                return dest_file.stat().st_size
            
            # 执行复制测试
            copy_results = {}
            copy_results['shutil'], copy_results['shutil_time'] = time_operation("shutil.copy2", copy_with_shutil)
            copy_results['manual'], copy_results['manual_time'] = time_operation("手动读写", copy_with_read_write)
            copy_results['chunks'], copy_results['chunks_time'] = time_operation("分块复制", copy_with_chunks)
            
            # 生成性能报告
            print("\n=== 性能测试总结 ===")
            print("\n读取性能排名（从快到慢）：")
            read_times = [
                ('一次性读取', read_results['read_all_time']),
                ('缓冲读取', read_results['read_buffer_time']),
                ('逐行读取', read_results['read_lines_time']),
                ('readlines读取', read_results['read_readlines_time'])
            ]
            for i, (method, time_taken) in enumerate(sorted(read_times, key=lambda x: x[1]), 1):
                print(f"{i}. {method}: {time_taken:.4f}秒")
            
            print("\n写入性能排名（从快到慢）：")
            write_times = [
                ('一次性写入', write_results['write_all_time']),
                ('writelines写入', write_results['write_writelines_time']),
                ('缓冲写入', write_results['write_buffer_time']),
                ('逐行写入', write_results['write_lines_time'])
            ]
            for i, (method, time_taken) in enumerate(sorted(write_times, key=lambda x: x[1]), 1):
                print(f"{i}. {method}: {time_taken:.4f}秒")
            
            print("\n复制性能排名（从快到慢）：")
            copy_times = [
                ('shutil.copy2', copy_results['shutil_time']),
                ('分块复制', copy_results['chunks_time']),
                ('手动读写', copy_results['manual_time'])
            ]
            for i, (method, time_taken) in enumerate(sorted(copy_times, key=lambda x: x[1]), 1):
                print(f"{i}. {method}: {time_taken:.4f}秒")
            
            # 保存性能报告
            report_file = self.exercise_dir / 'performance_report.json'
            performance_data = {
                'test_file_size': file_size,
                'test_timestamp': datetime.now().isoformat(),
                'read_performance': {
                    'read_all': read_results['read_all_time'],
                    'read_lines': read_results['read_lines_time'],
                    'read_buffer': read_results['read_buffer_time'],
                    'read_readlines': read_results['read_readlines_time']
                },
                'write_performance': {
                    'write_all': write_results['write_all_time'],
                    'write_lines': write_results['write_lines_time'],
                    'write_writelines': write_results['write_writelines_time'],
                    'write_buffer': write_results['write_buffer_time']
                },
                'copy_performance': {
                    'shutil': copy_results['shutil_time'],
                    'manual': copy_results['manual_time'],
                    'chunks': copy_results['chunks_time']
                }
            }
            
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(performance_data, f, indent=2)
            
            print(f"\n性能报告已保存：{report_file}")
            self.results['exercise_7'] = '完成'
            
        except Exception as e:
            print(f"练习7失败：{e}")
            self.results['exercise_7'] = f'失败: {e}'
    
    def run_all_exercises(self):
        """运行所有练习"""
        print("开始执行文件操作综合练习")
        print("=" * 60)
        
        exercises = [
            self.exercise_1_text_processing,
            self.exercise_2_csv_processing,
            self.exercise_3_json_config,
            self.exercise_4_binary_file_analysis,
            self.exercise_5_log_analysis,
            self.exercise_6_file_backup_system,
            self.exercise_7_performance_optimization
        ]
        
        start_time = time.time()
        
        for i, exercise in enumerate(exercises, 1):
            try:
                print(f"\n{'='*20} 练习 {i} {'='*20}")
                exercise()
            except Exception as e:
                print(f"练习{i}执行失败：{e}")
                self.results[f'exercise_{i}'] = f'异常: {e}'
        
        end_time = time.time()
        total_time = end_time - start_time
        
        # 生成总结报告
        print("\n" + "=" * 60)
        print("=== 练习完成总结 ===")
        print(f"总执行时间：{total_time:.2f}秒")
        print(f"练习目录：{self.exercise_dir}")
        
        print("\n各练习完成情况：")
        for i in range(1, 8):
            exercise_key = f'exercise_{i}'
            status = self.results.get(exercise_key, '未执行')
            print(f"练习{i}：{status}")
        
        # 保存总结报告
        summary_file = self.exercise_dir / 'exercise_summary.json'
        summary_data = {
            'completion_time': datetime.now().isoformat(),
            'total_duration': total_time,
            'exercise_results': self.results,
            'exercise_directory': str(self.exercise_dir)
        }
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n总结报告已保存：{summary_file}")
        
        return self.results


def main():
    """主函数"""
    print("Python文件操作 - 综合练习")
    print("=" * 50)
    
    # 创建练习实例
    exercises = FileExercises()
    
    try:
        # 运行所有练习
        results = exercises.run_all_exercises()
        
        # 显示最终结果
        print("\n" + "=" * 50)
        print("=== 最终结果 ===")
        
        completed = sum(1 for status in results.values() if status == '完成')
        total = len(results)
        
        print(f"完成练习：{completed}/{total}")
        print(f"成功率：{completed/total*100:.1f}%")
        
        if completed == total:
            print("\n🎉 恭喜！所有练习都已完成！")
        else:
            print("\n💡 部分练习需要重新检查，请查看具体错误信息。")
    
    except KeyboardInterrupt:
        print("\n练习被用户中断")
    except Exception as e:
        print(f"\n练习执行过程中出现错误：{e}")
        logger.error(f"主程序异常：{e}", exc_info=True)
    finally:
        # 询问是否清理临时文件
        try:
            response = input("\n是否删除练习临时文件？(y/N): ").strip().lower()
            if response in ['y', 'yes']:
                exercises.cleanup()
                print("临时文件已清理")
            else:
                print(f"练习文件保留在：{exercises.exercise_dir}")
        except (EOFError, KeyboardInterrupt):
            print(f"\n练习文件保留在：{exercises.exercise_dir}")
    
    # 学习总结
    print("\n" + "=" * 50)
    print("=== 学习总结 ===")
    print("""
文件操作综合练习涵盖的知识点：

1. 文本文件处理：
   - 读取和解析结构化文本数据
   - 数据统计和分析
   - 生成格式化报告

2. CSV文件操作：
   - 使用csv模块读写CSV文件
   - 数据聚合和排序
   - 字典格式的数据处理

3. JSON配置管理：
   - JSON数据的序列化和反序列化
   - 配置文件的读取、修改和验证
   - 配置备份和版本管理

4. 二进制文件分析：
   - 文件类型识别
   - 哈希值计算
   - 文件头分析

5. 日志文件分析：
   - 大文件的逐行处理
   - 正则表达式和字符串解析
   - 数据统计和可视化

6. 文件备份系统：
   - 目录遍历和文件复制
   - 元数据管理
   - 版本控制和恢复

7. 性能优化：
   - 不同I/O方法的性能比较
   - 缓冲区大小的影响
   - 内存使用优化

实际应用场景：
- 数据处理和分析
- 系统监控和日志分析
- 配置管理
- 备份和恢复系统
- 文件格式转换
- 批量文件操作

最佳实践总结：
1. 始终使用with语句管理文件资源
2. 选择合适的读写方法以优化性能
3. 处理大文件时使用流式处理
4. 实现适当的错误处理和日志记录
5. 考虑跨平台兼容性
6. 使用标准库模块（csv、json等）处理特定格式
7. 实现数据验证和完整性检查
8. 定期备份重要数据

关键要点：
- 文件操作是系统编程的基础
- 性能和可靠性同样重要
- 错误处理不可忽视
- 选择合适的工具和方法
- 考虑数据的完整性和安全性
""")


if __name__ == "__main__":
    main()