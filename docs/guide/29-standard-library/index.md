# 29 标准库

## 学习目标
- 熟悉Python标准库中的常用模块和功能
- 掌握系统操作、文件处理、数据序列化等核心技能
- 学会使用正则表达式、日期时间、数学运算等实用模块
- 了解网络编程和数据结构的标准库实现
- 培养查阅和使用标准库文档的能力

## 主要内容

### 1. 系统和环境模块
- **os模块**：操作系统接口，文件和目录操作
- **sys模块**：系统特定的参数和函数
- **pathlib模块**：面向对象的路径操作
- **shutil模块**：高级文件操作

### 2. 数据处理模块
- **json模块**：JSON数据的编码和解码
- **csv模块**：CSV文件的读写操作
- **pickle模块**：Python对象的序列化

### 3. 时间和随机模块
- **datetime模块**：日期和时间的处理
- **random模块**：随机数生成和随机选择

### 4. 文本处理模块
- **re模块**：正则表达式的模式匹配

### 5. 数学和统计模块
- **math模块**：数学函数和常数
- **statistics模块**：统计函数

### 6. 网络编程模块
- **urllib模块**：URL处理和HTTP客户端
- **http模块**：HTTP协议相关功能

### 7. 数据结构模块
- **collections模块**：专门的容器数据类型

## 代码文件说明

### [01_os_sys_modules.py](./01_os_sys_modules.md)
**学习内容**：os和sys模块的基本使用
- 环境变量的获取和设置
- 文件和目录的基本操作
- 系统信息的获取
- 命令行参数的处理

**重点知识点**：
- `os.environ`环境变量字典
- `os.path`路径操作函数
- `sys.argv`命令行参数
- `sys.path`模块搜索路径

### [02_datetime_module.py](./02_datetime_module.md)
**学习内容**：日期时间的创建、格式化和计算
- datetime对象的创建和操作
- 日期时间的格式化输出
- 时间差的计算
- 时区的处理

**重点知识点**：
- `datetime.datetime`类的使用
- `strftime()`和`strptime()`方法
- `timedelta`时间差计算
- 时区感知的日期时间处理

### [03_random_module.py](./03_random_module.md)
**学习内容**：随机数生成和随机选择
- 各种类型随机数的生成
- 随机选择和随机排列
- 随机种子的设置
- 概率分布的模拟

**重点知识点**：
- `random.random()`基础随机数
- `random.choice()`和`random.sample()`
- `random.shuffle()`随机打乱
- `random.seed()`种子设置

### [04_pathlib_shutil.py](./04_pathlib_shutil.md)
**学习内容**：现代化的文件和目录操作
- pathlib的面向对象路径操作
- shutil的高级文件操作
- 文件复制、移动和删除
- 目录树的操作

**重点知识点**：
- `pathlib.Path`类的使用
- 路径的拼接和解析
- `shutil.copy()`和`shutil.move()`
- `shutil.rmtree()`递归删除

### [05_json_csv_pickle.py](./05_json_csv_pickle.md)
**学习内容**：数据序列化和文件格式处理
- JSON数据的读写
- CSV文件的处理
- Python对象的pickle序列化
- 不同格式间的数据转换

**重点知识点**：
- `json.dumps()`和`json.loads()`
- `csv.reader()`和`csv.writer()`
- `pickle.dump()`和`pickle.load()`
- 数据格式的选择和转换

### [06_urllib_http.py](./06_urllib_http.md)
**学习内容**：网络编程基础
- HTTP请求的发送
- URL的解析和构建
- 网页内容的获取
- 简单的网络爬虫实现

**重点知识点**：
- `urllib.request.urlopen()`
- `urllib.parse`URL解析
- HTTP状态码处理
- 异常处理和重试机制

### [07_re_module.py](./07_re_module.md)
**学习内容**：正则表达式的模式匹配
- 正则表达式的基本语法
- 文本的搜索和替换
- 分组和捕获
- 实际应用场景

**重点知识点**：
- `re.search()`、`re.match()`、`re.findall()`
- 正则表达式的元字符
- 分组`()`和命名分组`(?P<name>)`
- `re.sub()`替换操作

### [08_math_statistics.py](./08_math_statistics.md)
**学习内容**：数学运算和统计分析
- 基本数学函数的使用
- 统计量的计算
- 数学常数和特殊函数
- 数据分析的基础操作

**重点知识点**：
- `math.sqrt()`、`math.log()`等函数
- `statistics.mean()`、`statistics.median()`
- 数学常数`math.pi`、`math.e`
- 统计分布的计算

### [09_collections_module.py](./09_collections_module.md)
**学习内容**：专门的容器数据类型
- Counter计数器的使用
- defaultdict默认字典
- namedtuple命名元组
- deque双端队列

**重点知识点**：
- `collections.Counter`计数统计
- `collections.defaultdict`默认值字典
- `collections.namedtuple`结构化数据
- `collections.deque`高效的队列操作

### [10_exercises.py](./10_exercises.md)
**学习内容**：标准库综合应用练习
- 多个模块的组合使用
- 实际问题的解决方案
- 代码的优化和重构
- 最佳实践的应用

**重点知识点**：
- 模块间的协作使用
- 错误处理和异常管理
- 代码的可读性和维护性
- 性能优化技巧

## 学习建议

### 学习顺序
1. **基础模块**：先学习01-04文件，掌握系统操作和文件处理
2. **数据处理**：学习05文件，了解数据序列化
3. **专项技能**：学习06-09文件，掌握网络、正则、数学、数据结构
4. **综合应用**：完成10文件的练习，巩固所学知识

### 使用方法
1. **逐个运行**：按顺序运行每个Python文件，观察输出结果
2. **修改实验**：尝试修改代码参数，观察不同的运行效果
3. **查阅文档**：使用`help()`函数查看模块和函数的详细文档
4. **实际应用**：将学到的知识应用到实际项目中

### 练习要点
1. **熟悉API**：记住常用函数的名称和参数
2. **理解原理**：了解每个模块解决的问题和适用场景
3. **组合使用**：学会将多个模块组合解决复杂问题
4. **异常处理**：掌握各种异常情况的处理方法
5. **性能考虑**：了解不同方法的性能特点

### 扩展学习
- 阅读Python官方文档中的标准库部分
- 学习第三方库如requests、pandas等
- 了解标准库的源码实现
- 关注Python版本更新中的标准库变化

## 注意事项
- 某些网络相关的示例需要网络连接
- 文件操作示例会在当前目录创建临时文件
- 建议在虚拟环境中运行代码
- 注意Python版本的兼容性问题