# Python标准库综合练习

## 学习目标

通过综合练习，掌握多个标准库模块的协同使用，培养解决实际问题的能力。

### 主要内容
- 日志分析系统
- 文件整理工具
- 数据处理管道
- 任务调度系统
- 网页爬虫基础

## 核心概念

### 1. 系统集成
- 多模块协作
- 数据流处理
- 错误处理策略
- 性能优化

### 2. 实际应用
- 日志分析
- 文件管理
- 数据统计
- 任务调度
- 网络爬虫

## 代码示例

### 练习1：日志分析器

```python
def exercise_1_log_analyzer():
    """
    练习1: 日志分析器
    
    功能：
    1. 解析各种格式的日志文件
    2. 统计访问量、错误率等指标
    3. 生成分析报告
    4. 支持多种输出格式
    """
    
    class LogAnalyzer:
        def __init__(self):
            self.logs = []
            self.stats = {
                'total_requests': 0,
                'error_count': 0,
                'by_ip': defaultdict(int),
                'by_status': defaultdict(int),
                'by_hour': defaultdict(int),
                'by_method': defaultdict(int)
            }
        
        def load_logs(self, log_data):
            """加载日志数据"""
            self.logs = self._parse_logs(log_data)
            self._calculate_stats()
        
        def _parse_logs(self, log_data):
            """解析日志数据"""
            parsed_logs = []
            
            # Apache/Nginx日志格式解析
            log_pattern = r'(\S+) - - \[(.*?)\] "(\S+) (\S+) (\S+)" (\d+) (\d+)'
            
            for line in log_data:
                match = re.match(log_pattern, line.strip())
                if match:
                    ip, timestamp, method, path, protocol, status, size = match.groups()
                    
                    # 解析时间戳
                    try:
                        dt = datetime.strptime(timestamp, '%d/%b/%Y:%H:%M:%S %z')
                    except ValueError:
                        dt = datetime.now()
                    
                    log_entry = {
                        'ip': ip,
                        'timestamp': dt,
                        'method': method,
                        'path': path,
                        'status': int(status),
                        'size': int(size) if size != '-' else 0,
                        'hour': dt.hour
                    }
                    
                    parsed_logs.append(log_entry)
            
            return parsed_logs
```

### 练习2：文件整理器

```python
def exercise_2_file_organizer():
    """
    练习2: 智能文件整理器
    
    功能：
    1. 扫描指定目录
    2. 按文件类型分类
    3. 生成整理建议
    4. 执行文件移动操作
    """
    
    class FileOrganizer:
        def __init__(self, base_path):
            self.base_path = Path(base_path)
            self.file_types = {
                FileType.IMAGE: ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
                FileType.DOCUMENT: ['.pdf', '.doc', '.docx', '.txt', '.rtf'],
                FileType.SPREADSHEET: ['.xls', '.xlsx', '.csv'],
                FileType.PRESENTATION: ['.ppt', '.pptx'],
                FileType.ARCHIVE: ['.zip', '.rar', '.7z', '.tar', '.gz'],
                FileType.VIDEO: ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
                FileType.AUDIO: ['.mp3', '.wav', '.flac', '.aac'],
                FileType.CODE: ['.py', '.js', '.html', '.css', '.java', '.cpp']
            }
            self.scan_results = []
        
        def scan_directory(self, max_depth=3):
            """扫描目录结构"""
            print(f"扫描目录: {self.base_path}")
            
            for file_path in self.base_path.rglob('*'):
                if file_path.is_file():
                    file_info = self._analyze_file(file_path)
                    self.scan_results.append(file_info)
            
            print(f"扫描完成，找到 {len(self.scan_results)} 个文件")
```

### 练习3：数据处理管道

```python
def exercise_3_data_processor():
    """
    练习3: 学生成绩数据处理管道
    
    功能：
    1. 生成模拟学生数据
    2. 数据清洗和验证
    3. 统计分析
    4. 生成报告
    """
    
    class StudentDataProcessor:
        def __init__(self):
            self.raw_data = []
            self.clean_data = []
            self.stats = {}
        
        def generate_sample_data(self, num_students=100):
            """生成模拟学生数据"""
            subjects = ['数学', '语文', '英语', '物理', '化学', '生物']
            
            for i in range(num_students):
                student = {
                    'id': f'S{i+1:04d}',
                    'name': f'学生{i+1}',
                    'age': random.randint(16, 19),
                    'gender': random.choice(['男', '女']),
                    'class': f'{random.randint(1, 6)}班',
                    'scores': {}
                }
                
                # 生成成绩（包含一些异常数据）
                for subject in subjects:
                    if random.random() < 0.95:  # 95%的概率有成绩
                        base_score = random.normalvariate(75, 15)
                        score = max(0, min(100, base_score))
                        student['scores'][subject] = round(score, 1)
                    else:
                        student['scores'][subject] = None  # 缺考
                
                self.raw_data.append(student)
```

### 练习4：任务调度系统

```python
def exercise_4_task_scheduler():
    """
    练习4: 优先级任务调度系统
    
    功能：
    1. 任务优先级管理
    2. 任务队列调度
    3. 执行时间统计
    4. 性能分析报告
    """
    
    class TaskPriority(Enum):
        CRITICAL = (1, "紧急")
        URGENT = (2, "重要")
        HIGH = (3, "高")
        NORMAL = (4, "普通")
        LOW = (5, "低")
        
        def __init__(self, priority, description):
            self.priority = priority
            self.description = description
    
    @dataclass
    class Task:
        task_id: int
        name: str
        priority: TaskPriority
        estimated_duration: float
        created_at: datetime = field(default_factory=datetime.now)
        started_at: Optional[datetime] = None
        completed_at: Optional[datetime] = None
        actual_duration: Optional[float] = None
        
        def __lt__(self, other):
            return self.priority.priority < other.priority.priority
    
    class TaskScheduler:
        def __init__(self):
            self.task_queue = []
            self.completed_tasks = []
            self.stats = {
                'total_tasks': 0,
                'completed_tasks': 0,
                'total_execution_time': 0,
                'by_priority': defaultdict(int)
            }
        
        def add_task(self, task):
            """添加任务到队列"""
            heapq.heappush(self.task_queue, task)
            self.stats['total_tasks'] += 1
            self.stats['by_priority'][task.priority.name] += 1
```

### 练习5：网页爬虫基础

```python
def exercise_5_web_crawler():
    """
    练习5: 简单网页爬虫
    
    功能：
    1. 网页内容获取
    2. 链接提取
    3. 数据解析
    4. 结果存储
    """
    
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
        
        def fetch_page(self, url, timeout=10):
            """获取网页内容"""
            try:
                self.stats['total_requests'] += 1
                
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
                print(f"获取失败 {url}: {e}")
                return None
        
        def extract_links(self, content, base_url):
            """提取页面中的链接"""
            if not content:
                return []
            
            link_pattern = r'href=["\']([^"\'>]+)["\']'
            links = re.findall(link_pattern, content, re.IGNORECASE)
            
            absolute_links = []
            for link in links:
                if link.startswith('http'):
                    absolute_links.append(link)
                elif link.startswith('/'):
                    parsed_base = urllib.parse.urlparse(base_url)
                    absolute_link = f"{parsed_base.scheme}://{parsed_base.netloc}{link}"
                    absolute_links.append(absolute_link)
            
            self.stats['total_links_found'] += len(absolute_links)
            return absolute_links
```

## 重要知识点

### 1. 模块集成
- **多模块协作**：不同标准库模块的组合使用
- **数据流设计**：数据在不同处理阶段的传递
- **接口设计**：模块间的清晰接口定义

### 2. 错误处理
- **异常捕获**：针对不同类型错误的处理策略
- **数据验证**：输入数据的完整性检查
- **容错机制**：系统在异常情况下的恢复能力

### 3. 性能优化
- **算法选择**：根据数据规模选择合适算法
- **内存管理**：大数据处理时的内存使用优化
- **并发处理**：适当使用多线程或异步处理

### 4. 数据处理
- **数据清洗**：处理缺失值、异常值
- **统计分析**：使用statistics模块进行数据分析
- **结果可视化**：生成易读的报告和图表

### 5. 文件操作
- **路径处理**：使用pathlib进行跨平台路径操作
- **文件格式**：支持多种文件格式的读写
- **批量操作**：高效处理大量文件

## 运行方式

```bash
# 运行完整练习
python3 10_exercises.py

# 单独运行某个练习（修改main函数）
python3 -c "from 10_exercises import exercise_1_log_analyzer; exercise_1_log_analyzer()"
```

## 练习建议

### 基础练习
1. **理解代码结构**：分析每个练习的设计思路
2. **修改参数**：调整数据规模、处理逻辑等
3. **添加功能**：为现有练习添加新特性

### 进阶练习
1. **性能优化**：分析并优化代码性能
2. **错误处理**：完善异常处理机制
3. **功能扩展**：添加更多实用功能

### 实际应用
1. **真实数据**：使用实际的日志文件、数据文件
2. **生产环境**：考虑生产环境的需求和限制
3. **用户界面**：添加命令行界面或图形界面

## 注意事项

### 1. 网络爬虫
- **遵守robots.txt**：检查网站的爬虫协议
- **请求频率**：避免过于频繁的请求
- **用户代理**：设置合适的User-Agent
- **法律合规**：确保爬虫行为符合法律法规

### 2. 文件操作
- **权限检查**：确保有足够的文件操作权限
- **备份重要数据**：在批量操作前备份重要文件
- **路径安全**：防止路径遍历攻击

### 3. 数据处理
- **内存限制**：处理大文件时注意内存使用
- **数据隐私**：保护敏感数据的隐私
- **数据完整性**：确保处理过程中数据不丢失

### 4. 性能考虑
- **算法复杂度**：选择合适的算法和数据结构
- **I/O优化**：减少不必要的文件读写操作
- **并发安全**：多线程环境下的数据安全

这些综合练习展示了Python标准库在实际项目中的应用，通过完成这些练习，你将能够熟练运用多个标准库模块解决复杂的实际问题。