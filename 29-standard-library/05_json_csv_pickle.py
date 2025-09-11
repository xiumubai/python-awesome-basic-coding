#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
05_json_csv_pickle.py - 数据序列化和处理模块学习

本文件演示Python数据序列化和处理的各种功能：
1. JSON数据处理
2. CSV文件读写
3. Pickle对象序列化
4. XML数据处理
5. 配置文件处理
6. 实际应用示例

学习目标：
- 掌握JSON数据的读写和处理
- 学会CSV文件的操作方法
- 了解Pickle序列化机制
- 掌握不同数据格式的转换
- 学会处理配置文件
"""

import json
import csv
import pickle
import xml.etree.ElementTree as ET
import configparser
import tempfile
from pathlib import Path
from datetime import datetime, date
from decimal import Decimal
import io

def json_operations_demo():
    """JSON操作演示"""
    print("=" * 50)
    print("JSON操作演示")
    print("=" * 50)
    
    # 基本数据类型
    data = {
        "name": "张三",
        "age": 30,
        "is_student": False,
        "scores": [85, 92, 78, 96],
        "address": {
            "city": "北京",
            "district": "朝阳区",
            "zipcode": "100000"
        },
        "hobbies": ["读书", "游泳", "编程"],
        "graduation_date": None
    }
    
    print("原始数据:")
    print(json.dumps(data, ensure_ascii=False, indent=2))
    
    # 序列化为JSON字符串
    json_string = json.dumps(data, ensure_ascii=False, indent=2)
    print(f"\nJSON字符串长度: {len(json_string)} 字符")
    
    # 从JSON字符串反序列化
    parsed_data = json.loads(json_string)
    print(f"\n反序列化成功: {parsed_data['name']}")
    print(f"平均分: {sum(parsed_data['scores']) / len(parsed_data['scores']):.1f}")
    
    # 处理特殊数据类型
    class DateTimeEncoder(json.JSONEncoder):
        """自定义JSON编码器，处理日期时间"""
        def default(self, obj):
            if isinstance(obj, (datetime, date)):
                return obj.isoformat()
            elif isinstance(obj, Decimal):
                return float(obj)
            return super().default(obj)
    
    complex_data = {
        "timestamp": datetime.now(),
        "birth_date": date(1990, 5, 15),
        "price": Decimal('99.99'),
        "metadata": {
            "version": "1.0",
            "created_at": datetime.now()
        }
    }
    
    # 使用自定义编码器
    complex_json = json.dumps(complex_data, cls=DateTimeEncoder, ensure_ascii=False, indent=2)
    print("\n复杂数据JSON:")
    print(complex_json)
    
    # JSON文件操作
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        json_file_path = f.name
    
    # 读取JSON文件
    with open(json_file_path, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    
    print(f"\n从文件加载的数据: {loaded_data['name']}")
    
    # 清理临时文件
    Path(json_file_path).unlink()
    
    print()

def csv_operations_demo():
    """CSV操作演示"""
    print("=" * 50)
    print("CSV操作演示")
    print("=" * 50)
    
    # 准备示例数据
    students_data = [
        ['姓名', '年龄', '专业', '成绩', '城市'],
        ['张三', 20, '计算机科学', 85.5, '北京'],
        ['李四', 21, '数学', 92.0, '上海'],
        ['王五', 19, '物理', 78.5, '广州'],
        ['赵六', 22, '化学', 88.0, '深圳'],
        ['钱七', 20, '生物', 91.5, '杭州']
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8', newline='') as f:
        csv_file_path = f.name
        
        # 写入CSV文件
        writer = csv.writer(f)
        writer.writerows(students_data)
    
    print(f"创建CSV文件: {Path(csv_file_path).name}")
    
    # 读取CSV文件
    print("\n读取CSV文件:")
    with open(csv_file_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                print(f"  表头: {row}")
            else:
                print(f"  数据: {row}")
    
    # 使用DictReader读取
    print("\n使用DictReader读取:")
    with open(csv_file_path, 'r', encoding='utf-8', newline='') as f:
        dict_reader = csv.DictReader(f)
        for row in dict_reader:
            print(f"  {row['姓名']}: {row['专业']}, 成绩 {row['成绩']}")
    
    # 写入字典数据
    dict_data = [
        {'产品': 'iPhone', '价格': 6999, '库存': 50, '分类': '电子产品'},
        {'产品': 'MacBook', '价格': 12999, '库存': 30, '分类': '电子产品'},
        {'产品': '咖啡杯', '价格': 29, '库存': 200, '分类': '生活用品'},
        {'产品': '笔记本', '价格': 15, '库存': 500, '分类': '文具'}
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8', newline='') as f:
        dict_csv_path = f.name
        
        fieldnames = ['产品', '价格', '库存', '分类']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()  # 写入表头
        writer.writerows(dict_data)
    
    print(f"\n创建产品CSV文件: {Path(dict_csv_path).name}")
    
    # 读取并处理数据
    print("\n产品数据分析:")
    with open(dict_csv_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        total_value = 0
        categories = {}
        
        for row in reader:
            price = float(row['价格'])
            stock = int(row['库存'])
            category = row['分类']
            value = price * stock
            total_value += value
            
            if category not in categories:
                categories[category] = {'count': 0, 'value': 0}
            categories[category]['count'] += 1
            categories[category]['value'] += value
    
    print(f"  总库存价值: ¥{total_value:,.2f}")
    print("  分类统计:")
    for category, stats in categories.items():
        print(f"    {category}: {stats['count']}种产品, 价值¥{stats['value']:,.2f}")
    
    # 处理特殊字符和格式
    special_data = [
        ['描述', '备注'],
        ['包含逗号,的文本', '正常文本'],
        ['包含"引号"的文本', '换行\n文本'],
        ['包含;分号;的文本', '制表符\t文本']
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8', newline='') as f:
        special_csv_path = f.name
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)  # 所有字段都加引号
        writer.writerows(special_data)
    
    print("\n特殊字符CSV内容:")
    with open(special_csv_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
    
    # 清理临时文件
    for path in [csv_file_path, dict_csv_path, special_csv_path]:
        Path(path).unlink()
    
    print()

# 定义一个复杂的类（模块级别，可以被pickle序列化）
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
    
    def __repr__(self):
        return self.__str__()

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
        },
        "settings": {
            "max_score": 100,
            "pass_score": 60,
            "grade_weights": [0.3, 0.3, 0.4]
        }
    }
    
    print("原始数据:")
    for student in students:
        print(f"  {student}")
    
    # 序列化到字节串
    pickled_data = pickle.dumps(complex_data)
    print(f"\n序列化后大小: {len(pickled_data)} 字节")
    
    # 反序列化
    unpickled_data = pickle.loads(pickled_data)
    print("\n反序列化后的数据:")
    for student in unpickled_data["students"]:
        print(f"  {student}")
    
    print(f"元数据: {unpickled_data['metadata']}")
    
    # 文件序列化
    with tempfile.NamedTemporaryFile(suffix='.pkl', delete=False) as f:
        pickle_file_path = f.name
        pickle.dump(complex_data, f)
    
    print(f"\n保存到文件: {Path(pickle_file_path).name}")
    
    # 从文件加载
    with open(pickle_file_path, 'rb') as f:
        loaded_data = pickle.load(f)
    
    print("从文件加载的数据:")
    print(f"  学生数量: {len(loaded_data['students'])}")
    print(f"  创建时间: {loaded_data['metadata']['created_at']}")
    
    # 不同协议版本的比较
    print("\n不同Pickle协议的大小比较:")
    for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
        data_bytes = pickle.dumps(complex_data, protocol=protocol)
        print(f"  协议 {protocol}: {len(data_bytes)} 字节")
    
    # 安全性注意事项
    print("\n安全性演示:")
    safe_data = {"message": "这是安全的数据", "numbers": [1, 2, 3, 4, 5]}
    safe_pickle = pickle.dumps(safe_data)
    
    # 只反序列化已知安全的数据
    try:
        safe_result = pickle.loads(safe_pickle)
        print(f"  安全数据加载成功: {safe_result['message']}")
    except Exception as e:
        print(f"  加载失败: {e}")
    
    # 清理临时文件
    Path(pickle_file_path).unlink()
    
    print()

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
        <description>一本优秀的Python入门书籍</description>
    </book>
    <book id="2" category="technical">
        <title>数据结构与算法</title>
        <author>李四</author>
        <year>2022</year>
        <price currency="CNY">89.00</price>
        <description>深入浅出的算法教程</description>
    </book>
    <book id="3" category="fiction">
        <title>机器学习实战</title>
        <author>王五</author>
        <year>2024</year>
        <price currency="CNY">128.00</price>
        <description>实用的机器学习指南</description>
    </book>
</library>'''
    
    # 解析XML
    root = ET.fromstring(xml_content)
    print(f"根元素: {root.tag}")
    
    # 遍历所有书籍
    print("\n书籍列表:")
    for book in root.findall('book'):
        book_id = book.get('id')
        category = book.get('category')
        title = book.find('title').text
        author = book.find('author').text
        year = book.find('year').text
        price = book.find('price').text
        currency = book.find('price').get('currency')
        
        print(f"  [{book_id}] {title}")
        print(f"      作者: {author} ({year})")
        print(f"      价格: {price} {currency}")
        print(f"      分类: {category}")
    
    # 查找特定元素
    fiction_books = root.findall(".//book[@category='fiction']")
    print(f"\n小说类书籍数量: {len(fiction_books)}")
    
    # 计算总价值
    total_value = 0
    for book in root.findall('book'):
        price = float(book.find('price').text)
        total_value += price
    
    print(f"图书总价值: ¥{total_value:.2f}")
    
    # 创建新的XML文档
    new_root = ET.Element("students")
    
    students_info = [
        {"id": "1", "name": "张三", "age": "20", "major": "计算机科学"},
        {"id": "2", "name": "李四", "age": "21", "major": "数学"},
        {"id": "3", "name": "王五", "age": "19", "major": "物理"}
    ]
    
    for student_info in students_info:
        student = ET.SubElement(new_root, "student")
        student.set("id", student_info["id"])
        
        name = ET.SubElement(student, "name")
        name.text = student_info["name"]
        
        age = ET.SubElement(student, "age")
        age.text = student_info["age"]
        
        major = ET.SubElement(student, "major")
        major.text = student_info["major"]
    
    # 格式化输出
    ET.indent(new_root, space="  ", level=0)
    new_xml = ET.tostring(new_root, encoding='unicode')
    
    print("\n创建的XML:")
    print(new_xml)
    
    print()

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
        'user': 'admin',
        'password': 'secret123'
    }
    
    config['web'] = {
        'host': '0.0.0.0',
        'port': '8080',
        'debug': 'true',  # 覆盖DEFAULT中的debug
        'static_path': '/static'
    }
    
    config['email'] = {
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': '587',
        'username': 'user@example.com',
        'use_tls': 'true'
    }
    
    # 保存配置文件
    with tempfile.NamedTemporaryFile(mode='w', suffix='.ini', delete=False, encoding='utf-8') as f:
        config_file_path = f.name
        config.write(f)
    
    print(f"创建配置文件: {Path(config_file_path).name}")
    
    # 读取配置文件
    new_config = configparser.ConfigParser()
    new_config.read(config_file_path, encoding='utf-8')
    
    print("\n配置文件内容:")
    for section_name in new_config.sections():
        print(f"  [{section_name}]")
        for key, value in new_config[section_name].items():
            print(f"    {key} = {value}")
    
    # 读取特定配置
    print("\n读取特定配置:")
    db_host = new_config.get('database', 'host')
    db_port = new_config.getint('database', 'port')
    web_debug = new_config.getboolean('web', 'debug')
    timeout = new_config.getint('DEFAULT', 'timeout')
    
    print(f"  数据库: {db_host}:{db_port}")
    print(f"  Web调试模式: {web_debug}")
    print(f"  超时时间: {timeout}秒")
    
    # 修改配置
    new_config.set('database', 'host', '192.168.1.100')
    new_config.set('web', 'port', '9000')
    
    # 添加新节
    new_config.add_section('cache')
    new_config.set('cache', 'type', 'redis')
    new_config.set('cache', 'host', 'localhost')
    new_config.set('cache', 'port', '6379')
    
    print("\n修改后的配置:")
    print(f"  数据库主机: {new_config.get('database', 'host')}")
    print(f"  Web端口: {new_config.get('web', 'port')}")
    print(f"  缓存类型: {new_config.get('cache', 'type')}")
    
    # 清理临时文件
    Path(config_file_path).unlink()
    
    print()

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
    
    print("原始数据:")
    for item in data:
        print(f"  {item}")
    
    # 转换为JSON
    json_data = json.dumps(data, ensure_ascii=False, indent=2)
    print("\nJSON格式:")
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
    
    # 转换为XML
    root = ET.Element("employees")
    for item in data:
        employee = ET.SubElement(root, "employee")
        for key, value in item.items():
            elem = ET.SubElement(employee, key)
            elem.text = str(value)
    
    ET.indent(root, space="  ", level=0)
    xml_data = ET.tostring(root, encoding='unicode')
    
    print("\nXML格式:")
    print(xml_data)
    
    # 从CSV转回字典
    csv_input = io.StringIO(csv_data)
    reader = csv.DictReader(csv_input)
    converted_data = list(reader)
    
    print("\n从CSV转换回的数据:")
    for item in converted_data:
        # 注意：CSV中的数字会变成字符串，需要转换
        item['age'] = int(item['age'])
        item['salary'] = int(item['salary'])
        print(f"  {item}")
    
    print()

def practical_applications():
    """实际应用示例"""
    print("=" * 50)
    print("实际应用示例")
    print("=" * 50)
    
    # 1. 数据备份和恢复
    def backup_restore_demo():
        """数据备份和恢复演示"""
        print("1. 数据备份和恢复:")
        
        # 模拟应用数据
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
        print(f"  JSON备份大小: {len(backup_json)} 字符")
        
        # 备份到Pickle（更紧凑，但不可读）
        backup_pickle = pickle.dumps(app_data)
        print(f"  Pickle备份大小: {len(backup_pickle)} 字节")
        
        # 恢复数据
        restored_data = json.loads(backup_json)
        print(f"  恢复用户数: {len(restored_data['users'])}")
    
    # 2. 配置管理
    def config_management_demo():
        """配置管理演示"""
        print("\n2. 配置管理:")
        
        # 多环境配置
        configs = {
            "development": {
                "database_url": "sqlite:///dev.db",
                "debug": True,
                "log_level": "DEBUG"
            },
            "production": {
                "database_url": "postgresql://prod_server/db",
                "debug": False,
                "log_level": "ERROR"
            }
        }
        
        # 保存配置
        for env, config in configs.items():
            config_json = json.dumps(config, indent=2)
            print(f"  {env}环境配置: {len(config_json)} 字符")
    
    # 3. 数据导入导出
    def import_export_demo():
        """数据导入导出演示"""
        print("\n3. 数据导入导出:")
        
        # 模拟从不同源导入数据
        csv_data = "name,score\n张三,85\n李四,92\n王五,78"
        json_data = '[{"name":"赵六","score":88},{"name":"钱七","score":95}]'
        
        # 解析CSV
        csv_reader = csv.DictReader(io.StringIO(csv_data))
        csv_records = [dict(row) for row in csv_reader]
        
        # 解析JSON
        json_records = json.loads(json_data)
        
        # 合并数据
        all_records = csv_records + json_records
        
        # 统计
        total_score = sum(int(record['score']) for record in all_records)
        avg_score = total_score / len(all_records)
        
        print(f"  导入记录数: {len(all_records)}")
        print(f"  平均分: {avg_score:.1f}")
        
        # 导出为不同格式
        export_json = json.dumps(all_records, ensure_ascii=False)
        print(f"  导出JSON大小: {len(export_json)} 字符")
    
    backup_restore_demo()
    config_management_demo()
    import_export_demo()
    
    print()

def main():
    """主函数"""
    print("Python数据序列化和处理模块学习演示")
    print("=" * 60)
    
    json_operations_demo()
    csv_operations_demo()
    pickle_operations_demo()
    xml_operations_demo()
    config_file_demo()
    data_conversion_demo()
    practical_applications()
    
    print("=" * 50)
    print("学习要点总结:")
    print("=" * 50)
    print("1. JSON适合跨语言数据交换，人类可读")
    print("2. CSV适合表格数据，Excel兼容")
    print("3. Pickle适合Python对象序列化，但不安全")
    print("4. XML适合结构化文档和配置")
    print("5. ConfigParser适合INI格式配置文件")
    print("6. 不同格式有各自的优缺点和适用场景")
    print("7. 数据转换时要注意类型和编码问题")
    print("8. 实际应用中常需要多种格式互相转换")

if __name__ == "__main__":
    main()