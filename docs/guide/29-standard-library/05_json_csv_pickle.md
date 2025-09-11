# JSON、CSV、Pickle数据处理

## 学习目标

通过本节学习，你将掌握：
- JSON数据的读写和处理
- CSV文件的操作和数据处理
- Pickle序列化的使用和注意事项
- XML数据的解析和生成
- 配置文件的处理
- 不同数据格式之间的转换
- 实际应用场景和最佳实践

## 核心概念

### 数据序列化格式
- **JSON**: 轻量级数据交换格式，人类可读
- **CSV**: 逗号分隔值，适合表格数据
- **Pickle**: Python特有的二进制序列化格式
- **XML**: 可扩展标记语言，结构化数据
- **INI**: 配置文件格式

## 代码示例

### 1. JSON操作演示

```python
import json
import tempfile
from pathlib import Path
from datetime import datetime

def json_operations_demo():
    """JSON操作演示"""
    print("=" * 50)
    print("JSON操作演示")
    print("=" * 50)
    
    # 基本数据类型
    basic_data = {
        "name": "张三",
        "age": 25,
        "is_student": True,
        "scores": [85, 92, 78, 90],
        "address": {
            "city": "北京",
            "district": "朝阳区",
            "zipcode": "100000"
        },
        "hobbies": ["编程", "阅读", "游泳"]
    }
    
    print("原始数据:")
    for key, value in basic_data.items():
        print(f"  {key}: {value}")
    
    # 序列化为JSON字符串
    json_str = json.dumps(basic_data, ensure_ascii=False, indent=2)
    print(f"\nJSON字符串 ({len(json_str)} 字符):")
    print(json_str)
    
    # 反序列化
    parsed_data = json.loads(json_str)
    print(f"\n反序列化后的姓名: {parsed_data['name']}")
    print(f"平均分: {sum(parsed_data['scores']) / len(parsed_data['scores']):.1f}")
```

### 2. CSV操作演示

```python
import csv
import io

def csv_operations_demo():
    """CSV操作演示"""
    print("=" * 50)
    print("CSV操作演示")
    print("=" * 50)
    
    # 列表数据写入CSV
    data = [
        ["姓名", "年龄", "城市", "薪资"],
        ["张三", 25, "北京", 8000],
        ["李四", 30, "上海", 12000],
        ["王五", 28, "广州", 9500]
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, 
                                   encoding='utf-8', newline='') as f:
        csv_file_path = f.name
        writer = csv.writer(f)
        writer.writerows(data)
    
    print(f"创建CSV文件: {Path(csv_file_path).name}")
    
    # 读取CSV文件
    print("\nCSV内容:")
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                print(f"  表头: {row}")
            else:
                print(f"  数据: {row}")
```

### 3. Pickle序列化演示

```python
import pickle
from datetime import datetime

class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores
        self.created_at = datetime.now()
    
    def average_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0
    
    def __str__(self):
        return f"Student({self.name}, {self.age}, avg={self.average_score():.1f})"

def pickle_operations_demo():
    """Pickle序列化演示"""
    print("=" * 50)
    print("Pickle序列化演示")
    print("=" * 50)
    
    # 创建复杂数据结构
    students = [
        Student("张三", 20, [85, 92, 78]),
        Student("李四", 21, [90, 88, 95]),
        Student("王五", 19, [82, 85, 89])
    ]
    
    complex_data = {
        "students": students,
        "metadata": {
            "created_at": datetime.now(),
            "version": "1.0",
            "total_students": len(students)
        }
    }
    
    # 序列化到字节串
    pickled_data = pickle.dumps(complex_data)
    print(f"序列化后大小: {len(pickled_data)} 字节")
    
    # 反序列化
    unpickled_data = pickle.loads(pickled_data)
    print("\n反序列化后的数据:")
    for student in unpickled_data["students"]:
        print(f"  {student}")
```

### 4. XML操作演示

```python
import xml.etree.ElementTree as ET

def xml_operations_demo():
    """XML操作演示"""
    print("=" * 50)
    print("XML操作演示")
    print("=" * 50)
    
    # 创建XML数据
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<library>
    <book id="1" category="fiction">
        <title>Python编程入门</title>
        <author>张三</author>
        <year>2023</year>
        <price currency="CNY">59.90</price>
    </book>
    <book id="2" category="technical">
        <title>数据结构与算法</title>
        <author>李四</author>
        <year>2022</year>
        <price currency="CNY">89.00</price>
    </book>
</library>'''
    
    # 解析XML
    root = ET.fromstring(xml_content)
    print(f"根元素: {root.tag}")
    
    # 遍历所有书籍
    print("\n书籍列表:")
    for book in root.findall('book'):
        book_id = book.get('id')
        title = book.find('title').text
        author = book.find('author').text
        price = book.find('price').text
        
        print(f"  [{book_id}] {title} - {author} (¥{price})")
```

### 5. 配置文件处理

```python
import configparser

def config_file_demo():
    """配置文件处理演示"""
    print("=" * 50)
    print("配置文件处理演示")
    print("=" * 50)
    
    # 创建配置解析器
    config = configparser.ConfigParser()
    
    # 添加配置节和选项
    config['DEFAULT'] = {
        'debug': 'false',
        'log_level': 'INFO',
        'timeout': '30'
    }
    
    config['database'] = {
        'host': 'localhost',
        'port': '5432',
        'name': 'myapp',
        'user': 'admin'
    }
    
    config['web'] = {
        'host': '0.0.0.0',
        'port': '8080',
        'debug': 'true'
    }
    
    # 读取特定配置
    db_host = config.get('database', 'host')
    db_port = config.getint('database', 'port')
    web_debug = config.getboolean('web', 'debug')
    
    print(f"数据库: {db_host}:{db_port}")
    print(f"Web调试模式: {web_debug}")
```

### 6. 数据格式转换

```python
def data_conversion_demo():
    """数据格式转换演示"""
    print("=" * 50)
    print("数据格式转换演示")
    print("=" * 50)
    
    # 原始数据
    data = [
        {"name": "张三", "age": 25, "city": "北京", "salary": 8000},
        {"name": "李四", "age": 30, "city": "上海", "salary": 12000},
        {"name": "王五", "age": 28, "city": "广州", "salary": 9500}
    ]
    
    # 转换为JSON
    json_data = json.dumps(data, ensure_ascii=False, indent=2)
    print("JSON格式:")
    print(json_data)
    
    # 转换为CSV
    csv_output = io.StringIO()
    fieldnames = ['name', 'age', 'city', 'salary']
    writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
    csv_data = csv_output.getvalue()
    
    print("\nCSV格式:")
    print(csv_data)
```

### 7. 实际应用示例

```python
def practical_applications():
    """实际应用示例"""
    print("=" * 50)
    print("实际应用示例")
    print("=" * 50)
    
    # 数据备份和恢复
    app_data = {
        "users": [
            {"id": 1, "username": "admin", "email": "admin@example.com"},
            {"id": 2, "username": "user1", "email": "user1@example.com"}
        ],
        "settings": {
            "theme": "dark",
            "language": "zh-CN",
            "notifications": True
        },
        "backup_time": datetime.now().isoformat()
    }
    
    # 备份到JSON
    backup_json = json.dumps(app_data, ensure_ascii=False, indent=2)
    print(f"JSON备份大小: {len(backup_json)} 字符")
    
    # 备份到Pickle
    backup_pickle = pickle.dumps(app_data)
    print(f"Pickle备份大小: {len(backup_pickle)} 字节")
    
    # 恢复数据
    restored_data = json.loads(backup_json)
    print(f"恢复用户数: {len(restored_data['users'])}")
```

## 重要知识点

### 1. 格式特点对比
- **JSON**: 跨语言、人类可读、不支持注释
- **CSV**: 简单、Excel兼容、适合表格数据
- **Pickle**: Python专用、支持复杂对象、不安全
- **XML**: 结构化、支持属性、冗余较多

### 2. 使用场景
- **JSON**: API数据交换、配置文件、Web应用
- **CSV**: 数据导入导出、报表、数据分析
- **Pickle**: 对象持久化、缓存、进程间通信
- **XML**: 配置文件、文档格式、SOAP协议

### 3. 安全注意事项
- Pickle不安全，不要反序列化不信任的数据
- JSON相对安全，但要验证数据结构
- CSV注意注入攻击和编码问题
- XML注意XXE攻击和实体展开

### 4. 性能考虑
- JSON解析速度快，文件较小
- CSV处理简单，内存占用少
- Pickle序列化快，但文件较大
- XML解析较慢，文件冗余多

## 运行方式

```bash
# 运行完整示例
python3 05_json_csv_pickle.py

# 或者在Python解释器中
python3
>>> exec(open('05_json_csv_pickle.py').read())
```

## 练习建议

1. **基础练习**：
   - 创建包含不同数据类型的JSON文件
   - 读写CSV文件，处理中文和特殊字符
   - 使用Pickle保存和加载自定义类对象

2. **进阶练习**：
   - 实现不同格式之间的数据转换工具
   - 创建配置文件管理系统
   - 处理大型CSV文件的内存优化

3. **实战项目**：
   - 开发数据备份和恢复工具
   - 创建多格式数据导入导出系统
   - 实现配置文件热重载功能

## 注意事项

1. **编码问题**：始终指定正确的编码格式
2. **数据验证**：反序列化前验证数据格式和内容
3. **错误处理**：妥善处理文件不存在、格式错误等异常
4. **内存管理**：处理大文件时考虑内存占用
5. **安全性**：不要反序列化不信任的Pickle数据
6. **兼容性**：考虑不同Python版本的兼容性问题