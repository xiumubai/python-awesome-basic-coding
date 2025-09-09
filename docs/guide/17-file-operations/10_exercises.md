# 文件操作综合练习

## 学习目标

通过本节的综合练习，你将能够：

- 掌握文本文件的处理和数据分析技巧
- 熟练使用CSV和JSON格式进行数据操作
- 理解二进制文件的分析方法
- 实现日志文件的解析和统计
- 构建文件备份和恢复系统
- 优化文件操作的性能
- 综合运用文件操作的各种技术

## 核心概念

### 文件操作综合应用

文件操作的综合练习涵盖了实际开发中常见的文件处理场景，包括数据分析、配置管理、系统监控、备份恢复等多个方面。

### 实际应用场景

- **数据处理**：文本数据的解析、统计和报告生成
- **配置管理**：JSON配置文件的读取、修改和验证
- **系统监控**：日志文件的分析和性能监控
- **文件管理**：备份系统和文件操作优化

## 代码示例

### 练习1：文本文件处理

```python
def exercise_1_text_processing(self):
    """
    练习1：文本文件处理
    任务：处理学生成绩数据，生成统计报告
    """
    print("\n=== 练习1：文本文件处理 ===")
    print("任务：处理学生成绩数据并生成统计报告")
    
    try:
        # 创建测试数据
        students_data = [
            "张三,数学,85,语文,92,英语,78",
            "李四,数学,92,语文,88,英语,95",
            "王五,数学,78,语文,85,英语,82",
            "赵六,数学,95,语文,90,英语,88",
            "钱七,数学,88,语文,94,英语,91"
        ]
        
        # 写入测试文件
        input_file = self.exercise_dir / 'students_scores.txt'
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write("# 学生成绩数据\n")
            f.write("# 格式：姓名,科目1,分数1,科目2,分数2,科目3,分数3\n")
            for line in students_data:
                f.write(line + "\n")
        
        print(f"测试数据已写入：{input_file}")
        
        # 解析数据
        students = {}
        subjects = set()
        
        with open(input_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                parts = line.split(',')
                if len(parts) < 7:  # 至少需要姓名+3个科目成绩
                    print(f"第{line_num}行数据格式错误：{line}")
                    continue
                
                name = parts[0]
                scores = {}
                
                # 解析科目和成绩
                for i in range(1, len(parts), 2):
                    if i + 1 < len(parts):
                        subject = parts[i]
                        try:
                            score = int(parts[i + 1])
                            scores[subject] = score
                            subjects.add(subject)
                        except ValueError:
                            print(f"第{line_num}行分数格式错误：{parts[i + 1]}")
                
                students[name] = scores
        
        print(f"\n成功解析 {len(students)} 名学生的成绩数据")
        print(f"涉及科目：{', '.join(sorted(subjects))}")
        
        # 统计分析
        subject_stats = {}
        for subject in subjects:
            scores = [student_scores.get(subject, 0) for student_scores in students.values() 
                     if subject in student_scores]
            if scores:
                subject_stats[subject] = {
                    'count': len(scores),
                    'total': sum(scores),
                    'average': sum(scores) / len(scores),
                    'max': max(scores),
                    'min': min(scores)
                }
        
        # 生成报告
        report_file = self.exercise_dir / 'score_report.txt'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("学生成绩统计报告\n")
            f.write("=" * 40 + "\n\n")
            
            f.write(f"总学生数：{len(students)}\n")
            f.write(f"统计科目：{len(subjects)}\n\n")
            
            # 各科目统计
            f.write("各科目成绩统计：\n")
            f.write("-" * 30 + "\n")
            for subject, stats in subject_stats.items():
                f.write(f"{subject}：\n")
                f.write(f"  平均分：{stats['average']:.2f}\n")
                f.write(f"  最高分：{stats['max']}\n")
                f.write(f"  最低分：{stats['min']}\n")
                f.write(f"  总分：{stats['total']}\n\n")
            
            # 学生排名
            f.write("学生总分排名：\n")
            f.write("-" * 30 + "\n")
            student_totals = []
            for name, scores in students.items():
                total = sum(scores.values())
                avg = total / len(scores) if scores else 0
                student_totals.append((name, total, avg, scores))
            
            # 按总分排序
            student_totals.sort(key=lambda x: x[1], reverse=True)
            
            for rank, (name, total, avg, scores) in enumerate(student_totals, 1):
                f.write(f"{rank}. {name} - 总分：{total}, 平均分：{avg:.2f}\n")
                score_details = ', '.join([f"{subj}:{score}" for subj, score in scores.items()])
                f.write(f"   详细：{score_details}\n\n")
        
        print(f"统计报告已生成：{report_file}")
        self.results['exercise_1'] = '完成'
        
    except Exception as e:
        print(f"练习1失败：{e}")
        self.results['exercise_1'] = f'失败: {e}'
```

### 练习2：CSV文件处理

```python
def exercise_2_csv_processing(self):
    """
    练习2：CSV文件处理
    任务：处理销售数据，生成月度报告
    """
    print("\n=== 练习2：CSV文件处理 ===")
    print("任务：处理销售数据并生成月度报告")
    
    try:
        # 创建销售数据
        sales_data = [
            ['日期', '产品', '销售员', '数量', '单价', '总额'],
            ['2024-01-15', '笔记本电脑', '张三', '2', '5000', '10000'],
            ['2024-01-16', '鼠标', '李四', '10', '50', '500'],
            ['2024-01-17', '键盘', '王五', '5', '200', '1000'],
            ['2024-01-18', '笔记本电脑', '张三', '1', '5000', '5000'],
            ['2024-01-19', '显示器', '赵六', '3', '1500', '4500']
        ]
        
        # 写入CSV文件
        csv_file = self.exercise_dir / 'sales_data.csv'
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(sales_data)
        
        print(f"销售数据已写入：{csv_file}")
        
        # 读取和处理CSV数据
        sales_records = []
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 数据类型转换
                record = {
                    '日期': datetime.strptime(row['日期'], '%Y-%m-%d').date(),
                    '产品': row['产品'],
                    '销售员': row['销售员'],
                    '数量': int(row['数量']),
                    '单价': float(row['单价']),
                    '总额': float(row['总额'])
                }
                sales_records.append(record)
        
        print(f"成功读取 {len(sales_records)} 条销售记录")
        
        # 数据分析
        # 按产品统计
        product_stats = {}
        for record in sales_records:
            product = record['产品']
            if product not in product_stats:
                product_stats[product] = {'数量': 0, '总额': 0, '次数': 0}
            
            product_stats[product]['数量'] += record['数量']
            product_stats[product]['总额'] += record['总额']
            product_stats[product]['次数'] += 1
        
        # 按销售员统计
        salesperson_stats = {}
        for record in sales_records:
            person = record['销售员']
            if person not in salesperson_stats:
                salesperson_stats[person] = {'数量': 0, '总额': 0, '次数': 0}
            
            salesperson_stats[person]['数量'] += record['数量']
            salesperson_stats[person]['总额'] += record['总额']
            salesperson_stats[person]['次数'] += 1
        
        # 生成汇总报告CSV
        summary_file = self.exercise_dir / 'sales_summary.csv'
        with open(summary_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # 产品销售汇总
            writer.writerow(['产品销售汇总'])
            writer.writerow(['产品', '销售数量', '销售总额', '销售次数', '平均单价'])
            
            for product, stats in sorted(product_stats.items(), key=lambda x: x[1]['总额'], reverse=True):
                avg_price = stats['总额'] / stats['数量'] if stats['数量'] > 0 else 0
                writer.writerow([product, stats['数量'], stats['总额'], stats['次数'], f"{avg_price:.2f}"])
            
            writer.writerow([])  # 空行
            
            # 销售员业绩汇总
            writer.writerow(['销售员业绩汇总'])
            writer.writerow(['销售员', '销售数量', '销售总额', '销售次数', '平均每单'])
            
            for person, stats in sorted(salesperson_stats.items(), key=lambda x: x[1]['总额'], reverse=True):
                avg_per_sale = stats['总额'] / stats['次数'] if stats['次数'] > 0 else 0
                writer.writerow([person, stats['数量'], stats['总额'], stats['次数'], f"{avg_per_sale:.2f}"])
        
        print(f"销售汇总报告已生成：{summary_file}")
        self.results['exercise_2'] = '完成'
        
    except Exception as e:
        print(f"练习2失败：{e}")
        self.results['exercise_2'] = f'失败: {e}'
```

### 练习3：JSON配置管理

```python
def exercise_3_json_config(self):
    """
    练习3：JSON配置文件管理
    任务：创建、读取、修改和验证JSON配置文件
    """
    print("\n=== 练习3：JSON配置文件管理 ===")
    print("任务：管理应用程序配置文件")
    
    try:
        # 创建初始配置
        initial_config = {
            "application": {
                "name": "文件处理系统",
                "version": "1.0.0",
                "debug": False
            },
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "filedb",
                "username": "admin",
                "password": "secret123"
            },
            "logging": {
                "level": "INFO",
                "file": "app.log",
                "max_size": "10MB",
                "backup_count": 5
            },
            "features": {
                "auto_backup": True,
                "compression": False,
                "encryption": True
            }
        }
        
        # 保存初始配置
        config_file = self.exercise_dir / 'app_config.json'
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(initial_config, f, indent=2, ensure_ascii=False)
        
        print(f"初始配置已创建：{config_file}")
        
        def load_config(file_path):
            """加载配置文件"""
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except FileNotFoundError:
                print(f"配置文件不存在：{file_path}")
                return None
            except json.JSONDecodeError as e:
                print(f"配置文件格式错误：{e}")
                return None
        
        def save_config(config, file_path):
            """保存配置文件"""
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(config, f, indent=2, ensure_ascii=False)
                return True
            except Exception as e:
                print(f"保存配置失败：{e}")
                return False
        
        def validate_config(config):
            """验证配置文件"""
            required_sections = ['application', 'database', 'logging', 'features']
            errors = []
            
            for section in required_sections:
                if section not in config:
                    errors.append(f"缺少必需的配置节：{section}")
            
            # 验证应用程序配置
            if 'application' in config:
                app_config = config['application']
                if 'name' not in app_config or not app_config['name']:
                    errors.append("应用程序名称不能为空")
                if 'version' not in app_config:
                    errors.append("缺少版本信息")
            
            # 验证数据库配置
            if 'database' in config:
                db_config = config['database']
                required_db_fields = ['host', 'port', 'name', 'username']
                for field in required_db_fields:
                    if field not in db_config:
                        errors.append(f"数据库配置缺少字段：{field}")
                
                if 'port' in db_config:
                    try:
                        port = int(db_config['port'])
                        if not (1 <= port <= 65535):
                            errors.append("数据库端口号无效")
                    except (ValueError, TypeError):
                        errors.append("数据库端口号必须是数字")
            
            return errors
        
        # 读取配置
        config = load_config(config_file)
        if config:
            print("配置文件读取成功")
            
            # 验证配置
            validation_errors = validate_config(config)
            if validation_errors:
                print("配置验证失败：")
                for error in validation_errors:
                    print(f"  - {error}")
            else:
                print("配置验证通过")
        
        # 修改配置
        print("\n修改配置...")
        config['application']['debug'] = True
        config['application']['version'] = '1.1.0'
        config['database']['port'] = 3306
        config['logging']['level'] = 'DEBUG'
        config['features']['compression'] = True
        
        # 添加新的配置项
        config['cache'] = {
            "enabled": True,
            "type": "redis",
            "host": "localhost",
            "port": 6379,
            "ttl": 3600
        }
        
        # 保存修改后的配置
        modified_config_file = self.exercise_dir / 'app_config_modified.json'
        if save_config(config, modified_config_file):
            print(f"修改后的配置已保存：{modified_config_file}")
        
        # 创建配置备份
        backup_file = self.exercise_dir / f'app_config_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        if save_config(initial_config, backup_file):
            print(f"配置备份已创建：{backup_file}")
        
        # 配置比较
        print("\n配置变更对比：")
        def compare_configs(old_config, new_config, path=""):
            """比较两个配置的差异"""
            changes = []
            
            # 检查修改和新增
            for key, value in new_config.items():
                current_path = f"{path}.{key}" if path else key
                
                if key not in old_config:
                    changes.append(f"新增：{current_path} = {value}")
                elif isinstance(value, dict) and isinstance(old_config[key], dict):
                    changes.extend(compare_configs(old_config[key], value, current_path))
                elif old_config[key] != value:
                    changes.append(f"修改：{current_path} = {old_config[key]} -> {value}")
            
            # 检查删除
            for key in old_config:
                if key not in new_config:
                    current_path = f"{path}.{key}" if path else key
                    changes.append(f"删除：{current_path}")
            
            return changes
        
        changes = compare_configs(initial_config, config)
        for change in changes:
            print(f"  {change}")
        
        # 生成配置文档
        doc_file = self.exercise_dir / 'config_documentation.md'
        with open(doc_file, 'w', encoding='utf-8') as f:
            f.write("# 应用程序配置文档\n\n")
            
            def document_config(config_dict, level=2):
                """生成配置文档"""
                doc_lines = []
                for key, value in config_dict.items():
                    doc_lines.append(f"{'#' * level} {key}\n")
                    
                    if isinstance(value, dict):
                        doc_lines.extend(document_config(value, level + 1))
                    else:
                        doc_lines.append(f"- **类型**: {type(value).__name__}\n")
                        doc_lines.append(f"- **默认值**: `{value}`\n")
                        doc_lines.append(f"- **说明**: {key}配置项\n\n")
                
                return doc_lines
            
            f.writelines(document_config(config))
        
        print(f"配置文档已生成：{doc_file}")
        self.results['exercise_3'] = '完成'
        
    except Exception as e:
        print(f"练习3失败：{e}")
        self.results['exercise_3'] = f'失败: {e}'
```

### 练习4：二进制文件分析

```python
def exercise_4_binary_file_analysis(self):
    """
    练习4：二进制文件分析
    任务：分析不同类型的二进制文件
    """
    print("\n=== 练习4：二进制文件分析 ===")
    print("任务：分析和识别二进制文件类型")
    
    try:
        # 创建不同类型的测试文件
        test_files = {}
        
        # 1. 创建文本文件（作为对比）
        text_file = self.exercise_dir / 'test.txt'
        with open(text_file, 'w', encoding='utf-8') as f:
            f.write("这是一个文本文件\n用于测试文件类型识别")
        test_files['text'] = text_file
        
        # 2. 创建二进制数据文件
        binary_file = self.exercise_dir / 'test.bin'
        with open(binary_file, 'wb') as f:
            # 写入一些二进制数据
            f.write(b'\x89PNG\r\n\x1a\n')  # PNG文件头
            f.write(b'\x00' * 100)  # 填充数据
        test_files['binary'] = binary_file
        
        # 3. 创建JSON文件
        json_file = self.exercise_dir / 'test.json'
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump({"test": "data", "number": 123}, f)
        test_files['json'] = json_file
        
        print(f"测试文件已创建：{len(test_files)} 个")
        
        def analyze_file(file_path):
            """分析文件"""
            analysis = {
                'path': str(file_path),
                'name': file_path.name,
                'size': 0,
                'type': 'unknown',
                'encoding': None,
                'hash_md5': None,
                'hash_sha256': None,
                'header': None,
                'is_text': False,
                'line_count': 0
            }
            
            if not file_path.exists():
                analysis['error'] = '文件不存在'
                return analysis
            
            # 获取文件大小
            analysis['size'] = file_path.stat().st_size
            
            # 读取文件头
            try:
                with open(file_path, 'rb') as f:
                    header = f.read(16)
                    analysis['header'] = header.hex() if header else None
            except Exception as e:
                analysis['error'] = f'读取文件头失败: {e}'
                return analysis
            
            # 计算哈希值
            try:
                with open(file_path, 'rb') as f:
                    content = f.read()
                    analysis['hash_md5'] = hashlib.md5(content).hexdigest()
                    analysis['hash_sha256'] = hashlib.sha256(content).hexdigest()
            except Exception as e:
                analysis['hash_error'] = str(e)
            
            # 文件类型识别
            if header:
                if header.startswith(b'\x89PNG'):
                    analysis['type'] = 'PNG图像'
                elif header.startswith(b'\xff\xd8\xff'):
                    analysis['type'] = 'JPEG图像'
                elif header.startswith(b'GIF8'):
                    analysis['type'] = 'GIF图像'
                elif header.startswith(b'PK\x03\x04'):
                    analysis['type'] = 'ZIP压缩文件'
                elif header.startswith(b'%PDF'):
                    analysis['type'] = 'PDF文档'
            
            # 尝试作为文本文件读取
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    analysis['is_text'] = True
                    analysis['encoding'] = 'utf-8'
                    analysis['line_count'] = len(content.splitlines())
                    
                    # 进一步判断文本文件类型
                    if file_path.suffix.lower() == '.json':
                        try:
                            json.loads(content)
                            analysis['type'] = 'JSON文件'
                        except json.JSONDecodeError:
                            analysis['type'] = '文本文件（JSON格式错误）'
                    elif file_path.suffix.lower() in ['.txt', '.log']:
                        analysis['type'] = '纯文本文件'
                    elif analysis['type'] == 'unknown':
                        analysis['type'] = '文本文件'
                        
            except UnicodeDecodeError:
                # 尝试其他编码
                for encoding in ['gbk', 'latin1']:
                    try:
                        with open(file_path, 'r', encoding=encoding) as f:
                            content = f.read()
                            analysis['is_text'] = True
                            analysis['encoding'] = encoding
                            analysis['line_count'] = len(content.splitlines())
                            if analysis['type'] == 'unknown':
                                analysis['type'] = f'文本文件（{encoding}编码）'
                            break
                    except UnicodeDecodeError:
                        continue
                
                if not analysis['is_text'] and analysis['type'] == 'unknown':
                    analysis['type'] = '二进制文件'
            
            except Exception as e:
                analysis['read_error'] = str(e)
            
            return analysis
        
        # 分析所有测试文件
        print("\n文件分析结果：")
        analysis_results = []
        
        for file_type, file_path in test_files.items():
            print(f"\n分析文件：{file_path.name}")
            result = analyze_file(file_path)
            analysis_results.append(result)
            
            print(f"  文件大小：{result['size']} 字节")
            print(f"  文件类型：{result['type']}")
            print(f"  是否文本：{result['is_text']}")
            if result['encoding']:
                print(f"  编码格式：{result['encoding']}")
            if result['line_count'] > 0:
                print(f"  行数：{result['line_count']}")
            if result['header']:
                print(f"  文件头：{result['header'][:32]}...")
            if result['hash_md5']:
                print(f"  MD5：{result['hash_md5']}")
        
        # 生成分析报告
        report_file = self.exercise_dir / 'file_analysis_report.json'
        report_data = {
            'analysis_time': datetime.now().isoformat(),
            'total_files': len(analysis_results),
            'files': analysis_results,
            'summary': {
                'text_files': sum(1 for r in analysis_results if r['is_text']),
                'binary_files': sum(1 for r in analysis_results if not r['is_text']),
                'total_size': sum(r['size'] for r in analysis_results)
            }
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n分析报告已保存：{report_file}")
        print(f"总计分析 {len(analysis_results)} 个文件")
        print(f"文本文件：{report_data['summary']['text_files']} 个")
        print(f"二进制文件：{report_data['summary']['binary_files']} 个")
        print(f"总大小：{report_data['summary']['total_size']} 字节")
        
        self.results['exercise_4'] = '完成'
        
    except Exception as e:
        print(f"练习4失败：{e}")
        self.results['exercise_4'] = f'失败: {e}'
```

### 练习5：日志文件分析

```python
def exercise_5_log_analysis(self):
    """
    练习5：日志文件分析
    任务：分析Web服务器访问日志
    """
    print("\n=== 练习5：日志文件分析 ===")
    print("任务：分析Web服务器访问日志")
    
    try:
        # 创建模拟的访问日志
        log_entries = [
            '192.168.1.100 - - [15/Jan/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234',
            '192.168.1.101 - - [15/Jan/2024:10:31:12 +0000] "GET /about.html HTTP/1.1" 200 2345',
            '192.168.1.102 - - [15/Jan/2024:10:32:33 +0000] "POST /login HTTP/1.1" 302 0',
            '192.168.1.100 - - [15/Jan/2024:10:33:21 +0000] "GET /dashboard HTTP/1.1" 200 5678',
            '192.168.1.103 - - [15/Jan/2024:10:34:56 +0000] "GET /nonexistent HTTP/1.1" 404 1024',
            '192.168.1.101 - - [15/Jan/2024:10:35:44 +0000] "GET /api/data HTTP/1.1" 500 512'
        ]
        
        # 写入日志文件
        log_file = self.exercise_dir / 'access.log'
        with open(log_file, 'w', encoding='utf-8') as f:
            for entry in log_entries:
                f.write(entry + '\n')
        
        print(f"模拟日志文件已创建：{log_file}")
        
        # 解析日志
        import re
        from collections import Counter, defaultdict
        
        # Apache访问日志的正则表达式
        log_pattern = re.compile(
            r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - '
            r'\[(?P<timestamp>[^\]]+)\] '
            r'"(?P<method>\w+) (?P<path>[^\s]+) HTTP/[^"]+" '
            r'(?P<status>\d+) (?P<bytes>\d+)'
        )
        
        parsed_logs = []
        error_logs = []
        
        with open(log_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                
                match = log_pattern.match(line)
                if match:
                    log_entry = match.groupdict()
                    log_entry['line_number'] = line_num
                    log_entry['status'] = int(log_entry['status'])
                    log_entry['bytes'] = int(log_entry['bytes'])
                    parsed_logs.append(log_entry)
                else:
                    error_logs.append((line_num, line))
        
        print(f"成功解析 {len(parsed_logs)} 条日志记录")
        if error_logs:
            print(f"发现 {len(error_logs)} 条格式错误的日志")
        
        # 统计分析
        ip_counter = Counter(log['ip'] for log in parsed_logs)
        path_counter = Counter(log['path'] for log in parsed_logs)
        status_counter = Counter(log['status'] for log in parsed_logs)
        method_counter = Counter(log['method'] for log in parsed_logs)
        
        # 计算总流量
        total_bytes = sum(log['bytes'] for log in parsed_logs)
        
        # 按小时统计访问量
        hourly_stats = defaultdict(int)
        for log in parsed_logs:
            # 简单提取小时信息（实际应用中需要更完整的时间解析）
            timestamp = log['timestamp']
            hour = timestamp.split(':')[1]  # 提取小时部分
            hourly_stats[hour] += 1
        
        # 错误分析
        error_4xx = [log for log in parsed_logs if 400 <= log['status'] < 500]
        error_5xx = [log for log in parsed_logs if 500 <= log['status'] < 600]
        
        print("\n=== 统计结果 ===")
        print(f"总请求数：{len(parsed_logs)}")
        print(f"总流量：{total_bytes:,} 字节 ({total_bytes/1024:.2f} KB)")
        print(f"4xx错误：{len(error_4xx)} 个")
        print(f"5xx错误：{len(error_5xx)} 个")
        
        print("\n访问最多的IP地址：")
        for ip, count in ip_counter.most_common(5):
            print(f"  {ip}: {count} 次")
        
        print("\n访问最多的页面：")
        for path, count in path_counter.most_common(5):
            print(f"  {path}: {count} 次")
        
        print("\n状态码分布：")
        for status, count in status_counter.most_common():
            print(f"  {status}: {count} 次")
        
        # 生成详细报告
        report_file = self.exercise_dir / 'log_analysis_report.txt'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("Web服务器访问日志分析报告\n")
            f.write("=" * 40 + "\n\n")
            
            f.write(f"分析时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"日志文件：{log_file}\n")
            f.write(f"总请求数：{sum(ip_counter.values())}\n")
            f.write(f"总流量：{total_bytes:,} 字节\n")
            f.write(f"错误请求数：{len(error_logs)}\n\n")
            
            f.write("访问最多的IP地址：\n")
            for ip, count in ip_counter.most_common(10):
                f.write(f"{ip}: {count} 次\n")
            
            f.write("\n访问最多的页面：\n")
            for path, count in path_counter.most_common(10):
                f.write(f"{path}: {count} 次\n")
            
            f.write("\n状态码分布：\n")
            for status, count in status_counter.most_common():
                f.write(f"{status}: {count} 次\n")
            
            if error_logs:
                f.write("\n错误日志记录：\n")
                for line_num, log_line in error_logs[:20]:  # 只显示前20条错误
                    f.write(f"第{line_num}行: {log_line}\n")
        
        print(f"详细报告已生成：{report_file}")
        self.results['exercise_5'] = '完成'
        
    except Exception as e:
        print(f"练习5失败：{e}")
        self.results['exercise_5'] = f'失败: {e}'
```

### 练习6：文件备份系统

```python
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
```

### 练习7：性能优化

```python
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
            }
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(performance_data, f, indent=2)
        
        print(f"\n性能报告已保存：{report_file}")
        self.results['exercise_7'] = '完成'
        
    except Exception as e:
        print(f"练习7失败：{e}")
        self.results['exercise_7'] = f'失败: {e}'
```

## 重要知识点

### 1. 综合应用技巧

- **数据处理流程**：读取 → 解析 → 分析 → 报告
- **错误处理策略**：预防性检查、异常捕获、错误恢复
- **性能优化方法**：选择合适的I/O方法、缓冲区优化
- **代码组织结构**：模块化设计、类的使用、方法封装

### 2. 实际应用场景

- **数据分析**：日志分析、统计报告、数据挖掘
- **系统管理**：配置管理、备份恢复、监控报警
- **文件处理**：格式转换、批量操作、内容分析
- **性能监控**：基准测试、性能对比、优化建议

### 3. 最佳实践总结

- **资源管理**：使用with语句确保文件正确关闭
- **异常处理**：针对不同类型的错误采用相应的处理策略
- **性能考虑**：根据文件大小和操作类型选择最优方法
- **代码质量**：保持代码清晰、注释完整、结构合理

## 最佳实践

### 1. 项目结构设计

```python
class FileExercises:
    def __init__(self):
        self.exercise_dir = Path('file_exercises')
        self.exercise_dir.mkdir(exist_ok=True)
        self.results = {}
    
    def cleanup(self):
        """清理临时文件"""
        if self.exercise_dir.exists():
            shutil.rmtree(self.exercise_dir)
```

### 2. 错误处理模式

```python
try:
    # 文件操作代码
    pass
except FileNotFoundError:
    print("文件不存在")
except PermissionError:
    print("权限不足")
except Exception as e:
    print(f"操作失败：{e}")
```

### 3. 性能测试框架

```python
def time_operation(operation_name: str, operation_func):
    """测量操作时间"""
    start_time = time.time()
    result = operation_func()
    end_time = time.time()
    duration = end_time - start_time
    print(f"{operation_name}: {duration:.4f}秒")
    return result, duration
```

## 注意事项

### 1. 文件操作安全

- 始终验证文件路径的合法性
- 检查文件权限和磁盘空间
- 处理并发访问问题
- 实现适当的备份机制

### 2. 性能优化

- 选择合适的缓冲区大小
- 避免不必要的文件重复读取
- 使用流式处理处理大文件
- 考虑内存使用限制

### 3. 数据完整性

- 实现数据验证机制
- 使用哈希值检查文件完整性
- 提供数据恢复功能
- 记录操作日志

### 4. 跨平台兼容性

- 使用pathlib处理路径
- 注意不同系统的编码差异
- 考虑文件系统的限制
- 测试不同操作系统的兼容性

## 练习建议

### 1. 基础练习

1. **修改练习参数**：调整数据量、文件大小等参数
2. **添加新功能**：为现有练习添加新的分析功能
3. **优化算法**：改进数据处理和分析算法
4. **扩展格式**：支持更多文件格式的处理

### 2. 进阶练习

1. **并发处理**：使用多线程或多进程处理大量文件
2. **网络集成**：添加远程文件下载和上传功能
3. **数据库集成**：将分析结果存储到数据库
4. **Web界面**：创建Web界面展示分析结果

### 3. 实际项目

1. **日志监控系统**：实时监控和分析系统日志
2. **文件同步工具**：实现文件夹同步功能
3. **数据迁移工具**：批量处理和转换数据文件
4. **备份管理系统**：完整的备份和恢复解决方案

## 下一步学习

### 1. 高级文件操作

- 文件锁定和并发控制
- 内存映射文件操作
- 异步文件I/O
- 文件系统监控

### 2. 数据处理进阶

- 大数据处理技术
- 流式数据处理
- 数据压缩和加密
- 分布式文件系统

### 3. 系统集成

- 操作系统API调用
- 网络文件系统
- 云存储集成
- 容器化部署

### 4. 性能优化深入

- 内存优化技术
- I/O性能调优
- 缓存策略设计
- 性能监控和分析

通过这些综合练习，你将掌握文件操作的各个方面，能够处理实际项目中的复杂文件操作需求，并具备优化和扩展的能力。