# 字典综合练习

## 学习目标

通过本节的综合练习，你将能够：

1. **综合运用字典的各种操作方法**
2. **解决实际的编程问题和业务场景**
3. **掌握字典在数据处理中的应用技巧**
4. **提高代码的组织和设计能力**
5. **学会性能优化和错误处理**
6. **培养解决复杂问题的思维方式**

## 练习1：学生成绩管理系统

### 题目描述

设计一个学生成绩管理系统，能够处理多个学生的多门课程成绩，并提供各种统计和查询功能。

### 功能要求

1. 添加学生和成绩
2. 计算各种统计信息（平均分、最高分、最低分等）
3. 成绩排名和分析
4. 课程统计
5. 数据导入导出

### 解决方案

```python
print("=== 练习1：学生成绩管理系统 ===")

class StudentGradeManager:
    def __init__(self):
        # 主数据结构：{student_id: {subject: grade, ...}, ...}
        self.grades = {}
        # 学生信息：{student_id: {name, class, ...}, ...}
        self.students = {}
        # 课程信息：{subject: {name, credit, ...}, ...}
        self.subjects = {}
    
    def add_student(self, student_id, name, class_name):
        """添加学生"""
        self.students[student_id] = {
            'name': name,
            'class': class_name,
            'created_at': '2024-01-01'  # 简化时间处理
        }
        if student_id not in self.grades:
            self.grades[student_id] = {}
        print(f"学生 {name} (ID: {student_id}) 已添加")
    
    def add_subject(self, subject_code, subject_name, credit=3):
        """添加课程"""
        self.subjects[subject_code] = {
            'name': subject_name,
            'credit': credit
        }
        print(f"课程 {subject_name} (代码: {subject_code}) 已添加")
    
    def add_grade(self, student_id, subject_code, grade):
        """添加成绩"""
        if student_id not in self.students:
            print(f"错误：学生ID {student_id} 不存在")
            return False
        
        if subject_code not in self.subjects:
            print(f"错误：课程代码 {subject_code} 不存在")
            return False
        
        if not (0 <= grade <= 100):
            print(f"错误：成绩 {grade} 不在有效范围内 (0-100)")
            return False
        
        self.grades[student_id][subject_code] = grade
        student_name = self.students[student_id]['name']
        subject_name = self.subjects[subject_code]['name']
        print(f"已为学生 {student_name} 添加 {subject_name} 成绩: {grade}")
        return True
    
    def get_student_average(self, student_id):
        """计算学生平均分"""
        if student_id not in self.grades or not self.grades[student_id]:
            return 0
        
        grades = list(self.grades[student_id].values())
        return sum(grades) / len(grades)
    
    def get_subject_statistics(self, subject_code):
        """获取课程统计信息"""
        subject_grades = [
            grade for student_grades in self.grades.values()
            for subject, grade in student_grades.items()
            if subject == subject_code
        ]
        
        if not subject_grades:
            return None
        
        return {
            'count': len(subject_grades),
            'average': sum(subject_grades) / len(subject_grades),
            'max': max(subject_grades),
            'min': min(subject_grades),
            'pass_rate': len([g for g in subject_grades if g >= 60]) / len(subject_grades) * 100
        }
    
    def get_class_ranking(self, class_name=None):
        """获取班级排名"""
        # 筛选指定班级的学生
        target_students = {
            sid: info for sid, info in self.students.items()
            if class_name is None or info['class'] == class_name
        }
        
        # 计算每个学生的平均分
        student_averages = {
            sid: {
                'name': self.students[sid]['name'],
                'class': self.students[sid]['class'],
                'average': self.get_student_average(sid),
                'subject_count': len(self.grades.get(sid, {}))
            }
            for sid in target_students.keys()
        }
        
        # 按平均分排序
        ranking = sorted(
            student_averages.items(),
            key=lambda x: x[1]['average'],
            reverse=True
        )
        
        return ranking
    
    def get_grade_distribution(self, subject_code=None):
        """获取成绩分布"""
        if subject_code:
            # 特定课程的成绩分布
            grades = [
                grade for student_grades in self.grades.values()
                for subject, grade in student_grades.items()
                if subject == subject_code
            ]
        else:
            # 所有成绩的分布
            grades = [
                grade for student_grades in self.grades.values()
                for grade in student_grades.values()
            ]
        
        if not grades:
            return {}
        
        # 按分数段统计
        distribution = {
            'A (90-100)': len([g for g in grades if 90 <= g <= 100]),
            'B (80-89)': len([g for g in grades if 80 <= g < 90]),
            'C (70-79)': len([g for g in grades if 70 <= g < 80]),
            'D (60-69)': len([g for g in grades if 60 <= g < 70]),
            'F (0-59)': len([g for g in grades if 0 <= g < 60])
        }
        
        return distribution
    
    def find_students_by_criteria(self, **criteria):
        """根据条件查找学生"""
        results = []
        
        for student_id, student_info in self.students.items():
            match = True
            student_avg = self.get_student_average(student_id)
            
            # 检查各种条件
            if 'min_average' in criteria and student_avg < criteria['min_average']:
                match = False
            if 'max_average' in criteria and student_avg > criteria['max_average']:
                match = False
            if 'class_name' in criteria and student_info['class'] != criteria['class_name']:
                match = False
            if 'subject_grade' in criteria:
                subject, min_grade = criteria['subject_grade']
                if (student_id not in self.grades or 
                    subject not in self.grades[student_id] or 
                    self.grades[student_id][subject] < min_grade):
                    match = False
            
            if match:
                results.append({
                    'id': student_id,
                    'name': student_info['name'],
                    'class': student_info['class'],
                    'average': student_avg,
                    'grades': self.grades.get(student_id, {})
                })
        
        return results
    
    def export_report(self):
        """导出完整报告"""
        report = {
            'summary': {
                'total_students': len(self.students),
                'total_subjects': len(self.subjects),
                'total_grades': sum(len(grades) for grades in self.grades.values())
            },
            'students': {},
            'subjects': {},
            'class_statistics': {}
        }
        
        # 学生报告
        for student_id, student_info in self.students.items():
            report['students'][student_id] = {
                **student_info,
                'average': self.get_student_average(student_id),
                'grades': self.grades.get(student_id, {}),
                'grade_count': len(self.grades.get(student_id, {}))
            }
        
        # 课程报告
        for subject_code, subject_info in self.subjects.items():
            stats = self.get_subject_statistics(subject_code)
            report['subjects'][subject_code] = {
                **subject_info,
                'statistics': stats
            }
        
        # 班级统计
        classes = set(info['class'] for info in self.students.values())
        for class_name in classes:
            class_students = [sid for sid, info in self.students.items() if info['class'] == class_name]
            class_averages = [self.get_student_average(sid) for sid in class_students]
            
            if class_averages:
                report['class_statistics'][class_name] = {
                    'student_count': len(class_students),
                    'average': sum(class_averages) / len(class_averages),
                    'max': max(class_averages),
                    'min': min(class_averages)
                }
        
        return report

# 测试学生成绩管理系统
manager = StudentGradeManager()

# 添加课程
manager.add_subject('MATH101', '高等数学', 4)
manager.add_subject('ENG101', '大学英语', 3)
manager.add_subject('CS101', '计算机基础', 3)
manager.add_subject('PHY101', '大学物理', 4)

# 添加学生
manager.add_student('S001', '张三', '计算机1班')
manager.add_student('S002', '李四', '计算机1班')
manager.add_student('S003', '王五', '计算机2班')
manager.add_student('S004', '赵六', '计算机2班')

# 添加成绩
grade_data = [
    ('S001', 'MATH101', 85), ('S001', 'ENG101', 78), ('S001', 'CS101', 92), ('S001', 'PHY101', 88),
    ('S002', 'MATH101', 76), ('S002', 'ENG101', 82), ('S002', 'CS101', 79), ('S002', 'PHY101', 74),
    ('S003', 'MATH101', 94), ('S003', 'ENG101', 89), ('S003', 'CS101', 96), ('S003', 'PHY101', 91),
    ('S004', 'MATH101', 68), ('S004', 'ENG101', 72), ('S004', 'CS101', 75), ('S004', 'PHY101', 70)
]

for student_id, subject_code, grade in grade_data:
    manager.add_grade(student_id, subject_code, grade)

# 查询和统计
print("\n=== 统计结果 ===")

# 班级排名
print("\n计算机1班排名:")
ranking = manager.get_class_ranking('计算机1班')
for i, (student_id, info) in enumerate(ranking, 1):
    print(f"  {i}. {info['name']} - 平均分: {info['average']:.2f}")

# 课程统计
print("\n课程统计:")
for subject_code in manager.subjects.keys():
    stats = manager.get_subject_statistics(subject_code)
    subject_name = manager.subjects[subject_code]['name']
    if stats:
        print(f"  {subject_name}: 平均分 {stats['average']:.2f}, 及格率 {stats['pass_rate']:.1f}%")

# 成绩分布
print("\n整体成绩分布:")
distribution = manager.get_grade_distribution()
for grade_range, count in distribution.items():
    print(f"  {grade_range}: {count} 人")

# 条件查询
print("\n优秀学生 (平均分 >= 85):")
excellent_students = manager.find_students_by_criteria(min_average=85)
for student in excellent_students:
    print(f"  {student['name']} ({student['class']}) - 平均分: {student['average']:.2f}")
```

## 练习2：商品库存管理系统

### 题目描述

设计一个商品库存管理系统，支持商品的增删改查、库存管理、销售统计等功能。

### 解决方案

```python
print("\n=== 练习2：商品库存管理系统 ===")

import json
from datetime import datetime
from collections import defaultdict

class InventoryManager:
    def __init__(self):
        # 商品信息：{product_id: {name, category, price, cost, ...}}
        self.products = {}
        # 库存信息：{product_id: {quantity, min_stock, max_stock, ...}}
        self.inventory = {}
        # 交易记录：[{type, product_id, quantity, price, timestamp}, ...]
        self.transactions = []
        # 供应商信息：{supplier_id: {name, contact, products}}
        self.suppliers = {}
    
    def add_product(self, product_id, name, category, price, cost, supplier_id=None):
        """添加商品"""
        self.products[product_id] = {
            'name': name,
            'category': category,
            'price': price,
            'cost': cost,
            'supplier_id': supplier_id,
            'created_at': datetime.now().isoformat()
        }
        
        # 初始化库存
        self.inventory[product_id] = {
            'quantity': 0,
            'min_stock': 10,  # 默认最小库存
            'max_stock': 1000,  # 默认最大库存
            'reserved': 0  # 预留库存
        }
        
        print(f"商品 {name} (ID: {product_id}) 已添加")
    
    def update_stock(self, product_id, quantity, transaction_type='adjustment', price=None):
        """更新库存"""
        if product_id not in self.products:
            print(f"错误：商品ID {product_id} 不存在")
            return False
        
        old_quantity = self.inventory[product_id]['quantity']
        
        if transaction_type == 'sale' and old_quantity < quantity:
            print(f"错误：库存不足，当前库存: {old_quantity}，需要: {quantity}")
            return False
        
        # 更新库存
        if transaction_type == 'sale':
            self.inventory[product_id]['quantity'] -= quantity
        else:
            self.inventory[product_id]['quantity'] += quantity
        
        # 记录交易
        transaction_price = price or self.products[product_id]['price']
        self.transactions.append({
            'type': transaction_type,
            'product_id': product_id,
            'quantity': quantity,
            'price': transaction_price,
            'timestamp': datetime.now().isoformat(),
            'old_stock': old_quantity,
            'new_stock': self.inventory[product_id]['quantity']
        })
        
        product_name = self.products[product_id]['name']
        new_quantity = self.inventory[product_id]['quantity']
        print(f"{product_name} 库存更新: {old_quantity} -> {new_quantity}")
        
        # 检查库存警告
        self._check_stock_alerts(product_id)
        
        return True
    
    def _check_stock_alerts(self, product_id):
        """检查库存警告"""
        current_stock = self.inventory[product_id]['quantity']
        min_stock = self.inventory[product_id]['min_stock']
        max_stock = self.inventory[product_id]['max_stock']
        product_name = self.products[product_id]['name']
        
        if current_stock <= min_stock:
            print(f"⚠️  警告：{product_name} 库存不足 (当前: {current_stock}, 最小: {min_stock})")
        elif current_stock >= max_stock:
            print(f"⚠️  警告：{product_name} 库存过多 (当前: {current_stock}, 最大: {max_stock})")
    
    def get_low_stock_products(self):
        """获取低库存商品"""
        low_stock = {}
        for product_id, stock_info in self.inventory.items():
            if stock_info['quantity'] <= stock_info['min_stock']:
                low_stock[product_id] = {
                    'name': self.products[product_id]['name'],
                    'current_stock': stock_info['quantity'],
                    'min_stock': stock_info['min_stock'],
                    'shortage': stock_info['min_stock'] - stock_info['quantity']
                }
        return low_stock
    
    def get_sales_report(self, start_date=None, end_date=None):
        """获取销售报告"""
        sales_transactions = [
            t for t in self.transactions 
            if t['type'] == 'sale'
        ]
        
        if not sales_transactions:
            return {'total_revenue': 0, 'total_quantity': 0, 'products': {}}
        
        # 按商品统计销售
        product_sales = defaultdict(lambda: {'quantity': 0, 'revenue': 0})
        total_revenue = 0
        total_quantity = 0
        
        for transaction in sales_transactions:
            product_id = transaction['product_id']
            quantity = transaction['quantity']
            revenue = quantity * transaction['price']
            
            product_sales[product_id]['quantity'] += quantity
            product_sales[product_id]['revenue'] += revenue
            total_revenue += revenue
            total_quantity += quantity
        
        # 添加商品名称和利润信息
        detailed_sales = {}
        for product_id, sales_data in product_sales.items():
            product_info = self.products[product_id]
            cost = product_info['cost']
            profit = sales_data['revenue'] - (sales_data['quantity'] * cost)
            
            detailed_sales[product_id] = {
                'name': product_info['name'],
                'category': product_info['category'],
                'quantity_sold': sales_data['quantity'],
                'revenue': sales_data['revenue'],
                'profit': profit,
                'profit_margin': (profit / sales_data['revenue'] * 100) if sales_data['revenue'] > 0 else 0
            }
        
        return {
            'total_revenue': total_revenue,
            'total_quantity': total_quantity,
            'total_profit': sum(p['profit'] for p in detailed_sales.values()),
            'products': detailed_sales
        }
    
    def get_category_analysis(self):
        """获取分类分析"""
        category_data = defaultdict(lambda: {
            'product_count': 0,
            'total_stock': 0,
            'total_value': 0,
            'products': []
        })
        
        for product_id, product_info in self.products.items():
            category = product_info['category']
            stock_quantity = self.inventory[product_id]['quantity']
            stock_value = stock_quantity * product_info['cost']
            
            category_data[category]['product_count'] += 1
            category_data[category]['total_stock'] += stock_quantity
            category_data[category]['total_value'] += stock_value
            category_data[category]['products'].append({
                'id': product_id,
                'name': product_info['name'],
                'stock': stock_quantity,
                'value': stock_value
            })
        
        return dict(category_data)
    
    def search_products(self, **criteria):
        """搜索商品"""
        results = []
        
        for product_id, product_info in self.products.items():
            match = True
            
            # 检查各种搜索条件
            if 'name' in criteria and criteria['name'].lower() not in product_info['name'].lower():
                match = False
            if 'category' in criteria and product_info['category'] != criteria['category']:
                match = False
            if 'min_price' in criteria and product_info['price'] < criteria['min_price']:
                match = False
            if 'max_price' in criteria and product_info['price'] > criteria['max_price']:
                match = False
            if 'low_stock' in criteria and criteria['low_stock']:
                if self.inventory[product_id]['quantity'] > self.inventory[product_id]['min_stock']:
                    match = False
            
            if match:
                results.append({
                    'id': product_id,
                    **product_info,
                    'stock': self.inventory[product_id]['quantity'],
                    'stock_value': self.inventory[product_id]['quantity'] * product_info['cost']
                })
        
        return results
    
    def generate_reorder_suggestions(self):
        """生成补货建议"""
        suggestions = []
        
        for product_id, stock_info in self.inventory.items():
            current_stock = stock_info['quantity']
            min_stock = stock_info['min_stock']
            max_stock = stock_info['max_stock']
            
            if current_stock <= min_stock:
                # 计算建议补货量
                suggested_order = max_stock - current_stock
                product_info = self.products[product_id]
                
                suggestions.append({
                    'product_id': product_id,
                    'name': product_info['name'],
                    'current_stock': current_stock,
                    'min_stock': min_stock,
                    'suggested_order': suggested_order,
                    'estimated_cost': suggested_order * product_info['cost'],
                    'supplier_id': product_info.get('supplier_id'),
                    'priority': 'high' if current_stock == 0 else 'medium'
                })
        
        # 按优先级和缺货程度排序
        suggestions.sort(key=lambda x: (x['priority'] == 'high', x['current_stock']))
        return suggestions

# 测试库存管理系统
inventory = InventoryManager()

# 添加商品
products_data = [
    ('P001', '笔记本电脑', '电子产品', 5999, 4500),
    ('P002', '无线鼠标', '电子产品', 199, 120),
    ('P003', '机械键盘', '电子产品', 599, 350),
    ('P004', '办公椅', '办公用品', 899, 600),
    ('P005', '台灯', '办公用品', 299, 180)
]

for product_data in products_data:
    inventory.add_product(*product_data)

# 进货
print("\n=== 进货操作 ===")
stock_updates = [
    ('P001', 50, 'purchase'),
    ('P002', 100, 'purchase'),
    ('P003', 30, 'purchase'),
    ('P004', 20, 'purchase'),
    ('P005', 40, 'purchase')
]

for product_id, quantity, trans_type in stock_updates:
    inventory.update_stock(product_id, quantity, trans_type)

# 销售
print("\n=== 销售操作 ===")
sales_data = [
    ('P001', 5, 'sale'),
    ('P002', 15, 'sale'),
    ('P003', 8, 'sale'),
    ('P004', 3, 'sale'),
    ('P005', 12, 'sale')
]

for product_id, quantity, trans_type in sales_data:
    inventory.update_stock(product_id, quantity, trans_type)

# 查询和分析
print("\n=== 库存分析 ===")

# 低库存商品
low_stock = inventory.get_low_stock_products()
if low_stock:
    print("\n低库存商品:")
    for product_id, info in low_stock.items():
        print(f"  {info['name']}: 当前 {info['current_stock']}, 需要 {info['shortage']} 件")

# 销售报告
sales_report = inventory.get_sales_report()
print(f"\n销售报告:")
print(f"  总收入: ¥{sales_report['total_revenue']:,.2f}")
print(f"  总利润: ¥{sales_report['total_profit']:,.2f}")
print(f"  销售数量: {sales_report['total_quantity']} 件")

# 分类分析
category_analysis = inventory.get_category_analysis()
print("\n分类分析:")
for category, data in category_analysis.items():
    print(f"  {category}: {data['product_count']} 种商品, 库存价值 ¥{data['total_value']:,.2f}")

# 补货建议
reorder_suggestions = inventory.generate_reorder_suggestions()
if reorder_suggestions:
    print("\n补货建议:")
    for suggestion in reorder_suggestions[:3]:  # 显示前3个建议
        print(f"  {suggestion['name']}: 建议补货 {suggestion['suggested_order']} 件 (成本: ¥{suggestion['estimated_cost']:,.2f})")
```

## 练习3：文本分析工具

### 题目描述

开发一个文本分析工具，能够分析文本的各种特征，包括词频统计、情感分析、关键词提取等。

### 解决方案

```python
print("\n=== 练习3：文本分析工具 ===")

import re
from collections import Counter, defaultdict
import math

class TextAnalyzer:
    def __init__(self):
        # 停用词列表
        self.stop_words = {
            '的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个', '上', '也', '很', '到', '说', '要', '去', '你', '会', '着', '没有', '看', '好', '自己', '这'
        }
        
        # 情感词典（简化版）
        self.sentiment_words = {
            'positive': {'好', '棒', '优秀', '喜欢', '满意', '开心', '快乐', '成功', '完美', '赞'},
            'negative': {'坏', '差', '糟糕', '讨厌', '失望', '难过', '失败', '问题', '错误', '烦'}
        }
    
    def preprocess_text(self, text):
        """文本预处理"""
        # 转换为小写
        text = text.lower()
        
        # 移除标点符号和特殊字符
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # 分词（简化处理，实际应用中可能需要更复杂的分词算法）
        words = text.split()
        
        # 移除停用词
        words = [word for word in words if word not in self.stop_words and len(word) > 1]
        
        return words
    
    def word_frequency_analysis(self, text):
        """词频分析"""
        words = self.preprocess_text(text)
        
        # 基本统计
        word_count = Counter(words)
        total_words = len(words)
        unique_words = len(word_count)
        
        # 计算词频
        word_freq = {word: count/total_words for word, count in word_count.items()}
        
        # 获取高频词
        top_words = word_count.most_common(10)
        
        return {
            'total_words': total_words,
            'unique_words': unique_words,
            'vocabulary_richness': unique_words / total_words if total_words > 0 else 0,
            'word_frequencies': word_freq,
            'top_words': top_words,
            'word_count': dict(word_count)
        }
    
    def sentiment_analysis(self, text):
        """情感分析"""
        words = self.preprocess_text(text)
        
        sentiment_scores = {
            'positive': 0,
            'negative': 0,
            'neutral': 0
        }
        
        sentiment_words_found = {
            'positive': [],
            'negative': []
        }
        
        for word in words:
            if word in self.sentiment_words['positive']:
                sentiment_scores['positive'] += 1
                sentiment_words_found['positive'].append(word)
            elif word in self.sentiment_words['negative']:
                sentiment_scores['negative'] += 1
                sentiment_words_found['negative'].append(word)
            else:
                sentiment_scores['neutral'] += 1
        
        # 计算总体情感倾向
        total_sentiment_words = sentiment_scores['positive'] + sentiment_scores['negative']
        
        if total_sentiment_words == 0:
            overall_sentiment = 'neutral'
            confidence = 0
        else:
            pos_ratio = sentiment_scores['positive'] / total_sentiment_words
            if pos_ratio > 0.6:
                overall_sentiment = 'positive'
                confidence = pos_ratio
            elif pos_ratio < 0.4:
                overall_sentiment = 'negative'
                confidence = 1 - pos_ratio
            else:
                overall_sentiment = 'neutral'
                confidence = 0.5
        
        return {
            'sentiment_scores': sentiment_scores,
            'sentiment_words_found': sentiment_words_found,
            'overall_sentiment': overall_sentiment,
            'confidence': confidence,
            'sentiment_ratio': {
                'positive': sentiment_scores['positive'] / len(words) if words else 0,
                'negative': sentiment_scores['negative'] / len(words) if words else 0,
                'neutral': sentiment_scores['neutral'] / len(words) if words else 0
            }
        }
    
    def extract_keywords(self, text, top_n=5):
        """关键词提取（基于TF-IDF的简化版本）"""
        words = self.preprocess_text(text)
        
        if not words:
            return []
        
        # 计算词频（TF）
        word_count = Counter(words)
        total_words = len(words)
        tf_scores = {word: count/total_words for word, count in word_count.items()}
        
        # 简化的IDF计算（假设文档集合）
        # 在实际应用中，这里应该使用真实的文档集合
        doc_freq = defaultdict(int)
        sentences = text.split('。')
        total_docs = len(sentences)
        
        for sentence in sentences:
            sentence_words = set(self.preprocess_text(sentence))
            for word in sentence_words:
                doc_freq[word] += 1
        
        # 计算TF-IDF分数
        tfidf_scores = {}
        for word in tf_scores:
            tf = tf_scores[word]
            idf = math.log(total_docs / (doc_freq[word] + 1))
            tfidf_scores[word] = tf * idf
        
        # 获取top关键词
        keywords = sorted(tfidf_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
        
        return keywords
    
    def text_statistics(self, text):
        """文本统计信息"""
        # 基本统计
        char_count = len(text)
        char_count_no_spaces = len(text.replace(' ', ''))
        word_count = len(text.split())
        sentence_count = len([s for s in text.split('。') if s.strip()])
        paragraph_count = len([p for p in text.split('\n\n') if p.strip()])
        
        # 字符分析
        char_analysis = {
            'letters': sum(1 for c in text if c.isalpha()),
            'digits': sum(1 for c in text if c.isdigit()),
            'spaces': sum(1 for c in text if c.isspace()),
            'punctuation': sum(1 for c in text if not c.isalnum() and not c.isspace())
        }
        
        # 平均值计算
        avg_word_length = sum(len(word) for word in text.split()) / word_count if word_count > 0 else 0
        avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0
        
        return {
            'character_count': char_count,
            'character_count_no_spaces': char_count_no_spaces,
            'word_count': word_count,
            'sentence_count': sentence_count,
            'paragraph_count': paragraph_count,
            'character_analysis': char_analysis,
            'average_word_length': avg_word_length,
            'average_sentence_length': avg_sentence_length,
            'reading_time_minutes': word_count / 200  # 假设每分钟阅读200字
        }
    
    def analyze_text_complexity(self, text):
        """分析文本复杂度"""
        words = text.split()
        sentences = [s for s in text.split('。') if s.strip()]
        
        if not words or not sentences:
            return {'complexity_score': 0, 'level': 'unknown'}
        
        # 计算各种复杂度指标
        avg_word_length = sum(len(word) for word in words) / len(words)
        avg_sentence_length = len(words) / len(sentences)
        
        # 词汇多样性
        unique_words = len(set(words))
        vocabulary_diversity = unique_words / len(words)
        
        # 长词比例
        long_words = sum(1 for word in words if len(word) > 6)
        long_word_ratio = long_words / len(words)
        
        # 复杂度评分（简化算法）
        complexity_score = (
            (avg_word_length - 3) * 0.3 +
            (avg_sentence_length - 10) * 0.1 +
            vocabulary_diversity * 0.4 +
            long_word_ratio * 0.2
        )
        
        # 确定复杂度等级
        if complexity_score < 0.3:
            level = '简单'
        elif complexity_score < 0.6:
            level = '中等'
        else:
            level = '复杂'
        
        return {
            'complexity_score': complexity_score,
            'level': level,
            'metrics': {
                'avg_word_length': avg_word_length,
                'avg_sentence_length': avg_sentence_length,
                'vocabulary_diversity': vocabulary_diversity,
                'long_word_ratio': long_word_ratio
            }
        }
    
    def comprehensive_analysis(self, text):
        """综合分析"""
        return {
            'basic_statistics': self.text_statistics(text),
            'word_frequency': self.word_frequency_analysis(text),
            'sentiment_analysis': self.sentiment_analysis(text),
            'keywords': self.extract_keywords(text),
            'complexity': self.analyze_text_complexity(text)
        }

# 测试文本分析工具
analyzer = TextAnalyzer()

# 示例文本
sample_text = """
Python是一种非常优秀的编程语言。它具有简洁明了的语法，强大的功能库，
以及活跃的社区支持。许多开发者都喜欢使用Python来开发各种应用程序。
Python在数据科学、人工智能、Web开发等领域都有广泛的应用。
学习Python是一个很好的选择，它可以帮助你快速入门编程世界。
虽然学习过程中可能会遇到一些困难，但是坚持下去就会看到成果。
"""

print("文本分析结果:")

# 基本统计
stats = analyzer.text_statistics(sample_text)
print(f"\n基本统计:")
print(f"  字符数: {stats['character_count']}")
print(f"  词数: {stats['word_count']}")
print(f"  句数: {stats['sentence_count']}")
print(f"  平均词长: {stats['average_word_length']:.2f}")
print(f"  预计阅读时间: {stats['reading_time_minutes']:.1f} 分钟")

# 词频分析
word_freq = analyzer.word_frequency_analysis(sample_text)
print(f"\n词频分析:")
print(f"  总词数: {word_freq['total_words']}")
print(f"  唯一词数: {word_freq['unique_words']}")
print(f"  词汇丰富度: {word_freq['vocabulary_richness']:.3f}")
print(f"  高频词: {word_freq['top_words'][:5]}")

# 情感分析
sentiment = analyzer.sentiment_analysis(sample_text)
print(f"\n情感分析:")
print(f"  总体情感: {sentiment['overall_sentiment']}")
print(f"  置信度: {sentiment['confidence']:.3f}")
print(f"  情感词分布: 积极 {sentiment['sentiment_scores']['positive']}, 消极 {sentiment['sentiment_scores']['negative']}")

# 关键词提取
keywords = analyzer.extract_keywords(sample_text)
print(f"\n关键词:")
for word, score in keywords:
    print(f"  {word}: {score:.3f}")

# 复杂度分析
complexity = analyzer.analyze_text_complexity(sample_text)
print(f"\n复杂度分析:")
print(f"  复杂度等级: {complexity['level']}")
print(f"  复杂度评分: {complexity['complexity_score']:.3f}")
print(f"  词汇多样性: {complexity['metrics']['vocabulary_diversity']:.3f}")
```

## 练习4：销售数据分析系统

### 题目描述

开发一个销售数据分析系统，能够处理销售数据，生成各种报表和分析结果。

### 解决方案

```python
print("\n=== 练习4：销售数据分析系统 ===")

from datetime import datetime, timedelta
import random
from collections import defaultdict

class SalesAnalyzer:
    def __init__(self):
        # 销售数据：[{date, product, category, quantity, price, customer, region}, ...]
        self.sales_data = []
        # 产品信息：{product_id: {name, category, cost, ...}}
        self.products = {}
        # 客户信息：{customer_id: {name, region, type, ...}}
        self.customers = {}
    
    def add_product(self, product_id, name, category, cost):
        """添加产品信息"""
        self.products[product_id] = {
            'name': name,
            'category': category,
            'cost': cost
        }
    
    def add_customer(self, customer_id, name, region, customer_type='regular'):
        """添加客户信息"""
        self.customers[customer_id] = {
            'name': name,
            'region': region,
            'type': customer_type
        }
    
    def add_sale(self, date, product_id, quantity, price, customer_id):
        """添加销售记录"""
        if product_id not in self.products:
            print(f"警告：产品 {product_id} 不存在")
            return False
        
        if customer_id not in self.customers:
            print(f"警告：客户 {customer_id} 不存在")
            return False
        
        sale_record = {
            'date': date,
            'product_id': product_id,
            'product_name': self.products[product_id]['name'],
            'category': self.products[product_id]['category'],
            'quantity': quantity,
            'price': price,
            'revenue': quantity * price,
            'cost': quantity * self.products[product_id]['cost'],
            'profit': quantity * (price - self.products[product_id]['cost']),
            'customer_id': customer_id,
            'customer_name': self.customers[customer_id]['name'],
            'region': self.customers[customer_id]['region']
        }
        
        self.sales_data.append(sale_record)
        return True
    
    def get_sales_summary(self, start_date=None, end_date=None):
        """获取销售汇总"""
        filtered_data = self._filter_by_date(self.sales_data, start_date, end_date)
        
        if not filtered_data:
            return {'total_revenue': 0, 'total_profit': 0, 'total_quantity': 0, 'order_count': 0}
        
        total_revenue = sum(sale['revenue'] for sale in filtered_data)
        total_profit = sum(sale['profit'] for sale in filtered_data)
        total_quantity = sum(sale['quantity'] for sale in filtered_data)
        order_count = len(filtered_data)
        
        return {
            'total_revenue': total_revenue,
            'total_profit': total_profit,
            'total_quantity': total_quantity,
            'order_count': order_count,
            'average_order_value': total_revenue / order_count if order_count > 0 else 0,
            'profit_margin': (total_profit / total_revenue * 100) if total_revenue > 0 else 0
        }
    
    def get_product_analysis(self):
        """产品分析"""
        product_stats = defaultdict(lambda: {
            'quantity_sold': 0,
            'revenue': 0,
            'profit': 0,
            'order_count': 0
        })
        
        for sale in self.sales_data:
            product_id = sale['product_id']
            product_stats[product_id]['quantity_sold'] += sale['quantity']
            product_stats[product_id]['revenue'] += sale['revenue']
            product_stats[product_id]['profit'] += sale['profit']
            product_stats[product_id]['order_count'] += 1
        
        # 添加产品信息和计算指标
        detailed_stats = {}
        for product_id, stats in product_stats.items():
            product_info = self.products[product_id]
            detailed_stats[product_id] = {
                'name': product_info['name'],
                'category': product_info['category'],
                **stats,
                'average_price': stats['revenue'] / stats['quantity_sold'] if stats['quantity_sold'] > 0 else 0,
                'profit_margin': (stats['profit'] / stats['revenue'] * 100) if stats['revenue'] > 0 else 0
            }
        
        return detailed_stats
    
    def get_customer_analysis(self):
        """客户分析"""
        customer_stats = defaultdict(lambda: {
            'total_spent': 0,
            'total_orders': 0,
            'total_quantity': 0,
            'first_purchase': None,
            'last_purchase': None
        })
        
        for sale in self.sales_data:
            customer_id = sale['customer_id']
            customer_stats[customer_id]['total_spent'] += sale['revenue']
            customer_stats[customer_id]['total_orders'] += 1
            customer_stats[customer_id]['total_quantity'] += sale['quantity']
            
            # 更新首次和最后购买日期
            sale_date = sale['date']
            if (customer_stats[customer_id]['first_purchase'] is None or 
                sale_date < customer_stats[customer_id]['first_purchase']):
                customer_stats[customer_id]['first_purchase'] = sale_date
            
            if (customer_stats[customer_id]['last_purchase'] is None or 
                sale_date > customer_stats[customer_id]['last_purchase']):
                customer_stats[customer_id]['last_purchase'] = sale_date
        
        # 添加客户信息和计算指标
        detailed_stats = {}
        for customer_id, stats in customer_stats.items():
            customer_info = self.customers[customer_id]
            
            # 计算客户价值等级
            if stats['total_spent'] > 10000:
                value_tier = 'VIP'
            elif stats['total_spent'] > 5000:
                value_tier = 'Gold'
            elif stats['total_spent'] > 1000:
                value_tier = 'Silver'
            else:
                value_tier = 'Bronze'
            
            detailed_stats[customer_id] = {
                'name': customer_info['name'],
                'region': customer_info['region'],
                'type': customer_info['type'],
                **stats,
                'average_order_value': stats['total_spent'] / stats['total_orders'] if stats['total_orders'] > 0 else 0,
                'value_tier': value_tier
            }
        
        return detailed_stats
    
    def get_regional_analysis(self):
        """区域分析"""
        regional_stats = defaultdict(lambda: {
            'revenue': 0,
            'profit': 0,
            'orders': 0,
            'customers': set()
        })
        
        for sale in self.sales_data:
            region = sale['region']
            regional_stats[region]['revenue'] += sale['revenue']
            regional_stats[region]['profit'] += sale['profit']
            regional_stats[region]['orders'] += 1
            regional_stats[region]['customers'].add(sale['customer_id'])
        
        # 转换为最终格式
        result = {}
        for region, stats in regional_stats.items():
            result[region] = {
                'revenue': stats['revenue'],
                'profit': stats['profit'],
                'orders': stats['orders'],
                'customer_count': len(stats['customers']),
                'average_order_value': stats['revenue'] / stats['orders'] if stats['orders'] > 0 else 0,
                'profit_margin': (stats['profit'] / stats['revenue'] * 100) if stats['revenue'] > 0 else 0
            }
        
        return result
    
    def get_time_series_analysis(self, period='month'):
        """时间序列分析"""
        time_stats = defaultdict(lambda: {
            'revenue': 0,
            'profit': 0,
            'orders': 0,
            'quantity': 0
        })
        
        for sale in self.sales_data:
            # 根据周期分组
            if period == 'day':
                time_key = sale['date']
            elif period == 'month':
                time_key = sale['date'][:7]  # YYYY-MM
            elif period == 'year':
                time_key = sale['date'][:4]  # YYYY
            else:
                time_key = sale['date']
            
            time_stats[time_key]['revenue'] += sale['revenue']
            time_stats[time_key]['profit'] += sale['profit']
            time_stats[time_key]['orders'] += 1
            time_stats[time_key]['quantity'] += sale['quantity']
        
        # 排序并计算趋势
        sorted_periods = sorted(time_stats.keys())
        result = {}
        
        for i, period_key in enumerate(sorted_periods):
            stats = time_stats[period_key]
            
            # 计算环比增长（如果有前一期数据）
            growth_rate = 0
            if i > 0:
                prev_revenue = time_stats[sorted_periods[i-1]]['revenue']
                if prev_revenue > 0:
                    growth_rate = ((stats['revenue'] - prev_revenue) / prev_revenue) * 100
            
            result[period_key] = {
                **stats,
                'average_order_value': stats['revenue'] / stats['orders'] if stats['orders'] > 0 else 0,
                'growth_rate': growth_rate
            }
        
        return result
    
    def get_top_performers(self, metric='revenue', top_n=5):
        """获取表现最佳的项目"""
        results = {
            'products': [],
            'customers': [],
            'regions': []
        }
        
        # 产品排行
        product_analysis = self.get_product_analysis()
        top_products = sorted(
            product_analysis.items(),
            key=lambda x: x[1][metric],
            reverse=True
        )[:top_n]
        results['products'] = [(pid, data['name'], data[metric]) for pid, data in top_products]
        
        # 客户排行
        customer_analysis = self.get_customer_analysis()
        customer_metric = 'total_spent' if metric == 'revenue' else metric
        top_customers = sorted(
            customer_analysis.items(),
            key=lambda x: x[1].get(customer_metric, 0),
            reverse=True
        )[:top_n]
        results['customers'] = [(cid, data['name'], data.get(customer_metric, 0)) for cid, data in top_customers]
        
        # 区域排行
        regional_analysis = self.get_regional_analysis()
        top_regions = sorted(
            regional_analysis.items(),
            key=lambda x: x[1][metric],
            reverse=True
        )[:top_n]
        results['regions'] = [(region, data[metric]) for region, data in top_regions]
        
        return results
    
    def _filter_by_date(self, data, start_date=None, end_date=None):
        """按日期过滤数据"""
        if not start_date and not end_date:
            return data
        
        filtered = []
        for item in data:
            item_date = item['date']
            if start_date and item_date < start_date:
                continue
            if end_date and item_date > end_date:
                continue
            filtered.append(item)
        
        return filtered
    
    def generate_comprehensive_report(self):
        """生成综合报告"""
        return {
            'summary': self.get_sales_summary(),
            'product_analysis': self.get_product_analysis(),
            'customer_analysis': self.get_customer_analysis(),
            'regional_analysis': self.get_regional_analysis(),
            'time_series': self.get_time_series_analysis('month'),
            'top_performers': self.get_top_performers()
        }

# 测试销售分析系统
sales_analyzer = SalesAnalyzer()

# 添加产品
products = [
    ('P001', '笔记本电脑', '电子产品', 4000),
    ('P002', '智能手机', '电子产品', 2000),
    ('P003', '平板电脑', '电子产品', 1500),
    ('P004', '耳机', '配件', 200),
    ('P005', '键盘', '配件', 300)
]

for product in products:
    sales_analyzer.add_product(*product)

# 添加客户
customers = [
    ('C001', '张三', '北京', 'VIP'),
    ('C002', '李四', '上海', 'regular'),
    ('C003', '王五', '广州', 'regular'),
    ('C004', '赵六', '深圳', 'Gold'),
    ('C005', '钱七', '杭州', 'regular')
]

for customer in customers:
    sales_analyzer.add_customer(*customer)

# 生成模拟销售数据
print("生成销售数据...")
for i in range(100):
    # 随机生成销售记录
    date = f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    product_id = random.choice(['P001', 'P002', 'P003', 'P004', 'P005'])
    quantity = random.randint(1, 5)
    
    # 根据产品设置价格范围
    base_prices = {'P001': 6000, 'P002': 3000, 'P003': 2500, 'P004': 500, 'P005': 600}
    price = base_prices[product_id] + random.randint(-500, 500)
    
    customer_id = random.choice(['C001', 'C002', 'C003', 'C004', 'C005'])
    
    sales_analyzer.add_sale(date, product_id, quantity, price, customer_id)

# 分析结果
print("\n=== 销售分析结果 ===")

# 销售汇总
summary = sales_analyzer.get_sales_summary()
print(f"\n销售汇总:")
print(f"  总收入: ¥{summary['total_revenue']:,.2f}")
print(f"  总利润: ¥{summary['total_profit']:,.2f}")
print(f"  利润率: {summary['profit_margin']:.1f}%")
print(f"  订单数: {summary['order_count']}")
print(f"  平均订单价值: ¥{summary['average_order_value']:,.2f}")

# 产品表现
top_performers = sales_analyzer.get_top_performers()
print(f"\n产品销售排行:")
for i, (pid, name, revenue) in enumerate(top_performers['products'], 1):
    print(f"  {i}. {name}: ¥{revenue:,.2f}")

# 客户价值排行
print(f"\n客户价值排行:")
for i, (cid, name, spent) in enumerate(top_performers['customers'], 1):
    print(f"  {i}. {name}: ¥{spent:,.2f}")

# 区域表现
regional_analysis = sales_analyzer.get_regional_analysis()
print(f"\n区域表现:")
for region, data in sorted(regional_analysis.items(), key=lambda x: x[1]['revenue'], reverse=True):
    print(f"  {region}: ¥{data['revenue']:,.2f} (订单: {data['orders']}, 客户: {data['customer_count']})")

# 月度趋势
time_series = sales_analyzer.get_time_series_analysis('month')
print(f"\n月度销售趋势 (最近3个月):")
for period in sorted(time_series.keys())[-3:]:
    data = time_series[period]
    print(f"  {period}: ¥{data['revenue']:,.2f} (增长率: {data['growth_rate']:+.1f}%)")
```

## 练习5：配置文件管理器

### 题目描述

开发一个配置文件管理器，能够读取、写入、验证和管理各种格式的配置文件。

### 解决方案

```python
print("\n=== 练习5：配置文件管理器 ===")

import json
import re
from copy import deepcopy

class ConfigManager:
    def __init__(self):
        # 配置数据
        self.config = {}
        # 配置模式定义
        self.schema = {}
        # 默认值
        self.defaults = {}
        # 验证规则
        self.validators = {}
    
    def define_schema(self, schema_dict):
        """定义配置模式"""
        self.schema = deepcopy(schema_dict)
        print("配置模式已定义")
    
    def set_defaults(self, defaults_dict):
        """设置默认值"""
        self.defaults = deepcopy(defaults_dict)
        # 应用默认值到当前配置
        self._apply_defaults()
        print("默认值已设置")
    
    def _apply_defaults(self):
        """应用默认值"""
        def apply_nested_defaults(config_dict, defaults_dict):
            for key, default_value in defaults_dict.items():
                if key not in config_dict:
                    config_dict[key] = deepcopy(default_value)
                elif isinstance(default_value, dict) and isinstance(config_dict[key], dict):
                    apply_nested_defaults(config_dict[key], default_value)
        
        apply_nested_defaults(self.config, self.defaults)
    
    def add_validator(self, path, validator_func, error_message="Validation failed"):
        """添加验证器"""
        self.validators[path] = {
            'func': validator_func,
            'message': error_message
        }
    
    def set_config(self, path, value):
        """设置配置值"""
        keys = path.split('.')
        current = self.config
        
        # 创建嵌套结构
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        
        # 设置值
        current[keys[-1]] = value
        
        # 验证配置
        if not self.validate_config():
            # 如果验证失败，回滚更改
            print(f"警告：配置 {path} 验证失败，已回滚")
            return False
        
        print(f"配置 {path} 已设置为: {value}")
        return True
    
    def get_config(self, path=None, default=None):
        """获取配置值"""
        if path is None:
            return deepcopy(self.config)
        
        keys = path.split('.')
        current = self.config
        
        try:
            for key in keys:
                current = current[key]
            return current
        except (KeyError, TypeError):
            return default
    
    def validate_config(self):
        """验证配置"""
        errors = []
        
        # 检查必需字段
        def check_required_fields(config_dict, schema_dict, path=""):
            for key, schema_value in schema_dict.items():
                current_path = f"{path}.{key}" if path else key
                
                if isinstance(schema_value, dict):
                    if 'required' in schema_value and schema_value['required']:
                        if key not in config_dict:
                            errors.append(f"必需字段缺失: {current_path}")
                            continue
                    
                    if key in config_dict and isinstance(config_dict[key], dict):
                        # 递归检查嵌套对象
                        nested_schema = {k: v for k, v in schema_value.items() if k != 'required'}
                        if nested_schema:
                            check_required_fields(config_dict[key], nested_schema, current_path)
        
        if self.schema:
            check_required_fields(self.config, self.schema)
        
        # 运行自定义验证器
        for path, validator_info in self.validators.items():
            value = self.get_config(path)
            if value is not None:
                try:
                    if not validator_info['func'](value):
                        errors.append(f"{path}: {validator_info['message']}")
                except Exception as e:
                    errors.append(f"{path}: 验证器错误 - {str(e)}")
        
        if errors:
            print("配置验证失败:")
            for error in errors:
                print(f"  - {error}")
            return False
        
        return True
    
    def load_from_dict(self, config_dict):
        """从字典加载配置"""
        self.config = deepcopy(config_dict)
        self._apply_defaults()
        
        if self.validate_config():
            print("配置已成功加载")
            return True
        else:
            print("配置加载失败：验证不通过")
            self.config = {}
            self._apply_defaults()
            return False
    
    def export_config(self, include_defaults=True):
        """导出配置"""
        if include_defaults:
            return deepcopy(self.config)
        else:
            # 只导出非默认值
            exported = {}
            
            def export_non_defaults(config_dict, defaults_dict, result_dict):
                for key, value in config_dict.items():
                    if key not in defaults_dict:
                        result_dict[key] = deepcopy(value)
                    elif isinstance(value, dict) and isinstance(defaults_dict[key], dict):
                        nested_result = {}
                        export_non_defaults(value, defaults_dict[key], nested_result)
                        if nested_result:
                            result_dict[key] = nested_result
                    elif value != defaults_dict[key]:
                        result_dict[key] = deepcopy(value)
            
            export_non_defaults(self.config, self.defaults, exported)
            return exported
    
    def reset_to_defaults(self):
        """重置为默认值"""
        self.config = {}
        self._apply_defaults()
        print("配置已重置为默认值")
    
    def merge_config(self, other_config):
        """合并配置"""
        def deep_merge(dict1, dict2):
            result = deepcopy(dict1)
            for key, value in dict2.items():
                if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                    result[key] = deep_merge(result[key], value)
                else:
                    result[key] = deepcopy(value)
            return result
        
        old_config = deepcopy(self.config)
        self.config = deep_merge(self.config, other_config)
        
        if self.validate_config():
            print("配置合并成功")
            return True
        else:
            print("配置合并失败：验证不通过，已回滚")
            self.config = old_config
            return False
    
    def get_config_diff(self, other_config):
        """获取配置差异"""
        differences = {
            'added': {},
            'removed': {},
            'modified': {}
        }
        
        def find_differences(dict1, dict2, path=""):
            # 检查dict1中的键
            for key, value in dict1.items():
                current_path = f"{path}.{key}" if path else key
                
                if key not in dict2:
                    differences['removed'][current_path] = value
                elif isinstance(value, dict) and isinstance(dict2[key], dict):
                    find_differences(value, dict2[key], current_path)
                elif value != dict2[key]:
                    differences['modified'][current_path] = {
                        'old': value,
                        'new': dict2[key]
                    }
            
            # 检查dict2中新增的键
            for key, value in dict2.items():
                current_path = f"{path}.{key}" if path else key
                if key not in dict1:
                    differences['added'][current_path] = value
        
        find_differences(self.config, other_config)
        return differences
    
    def search_config(self, pattern, search_keys=True, search_values=True):
        """搜索配置"""
        results = []
        regex = re.compile(pattern, re.IGNORECASE)
        
        def search_recursive(config_dict, path=""):
            for key, value in config_dict.items():
                current_path = f"{path}.{key}" if path else key
                
                # 搜索键名
                if search_keys and regex.search(key):
                    results.append({
                        'path': current_path,
                        'type': 'key',
                        'match': key,
                        'value': value
                    })
                
                # 搜索值
                if search_values and isinstance(value, str) and regex.search(value):
                    results.append({
                        'path': current_path,
                        'type': 'value',
                        'match': value,
                        'key': key
                    })
                
                # 递归搜索嵌套字典
                if isinstance(value, dict):
                    search_recursive(value, current_path)
        
        search_recursive(self.config)
        return results
    
    def get_config_summary(self):
        """获取配置摘要"""
        def count_items(config_dict):
            count = 0
            for value in config_dict.values():
                count += 1
                if isinstance(value, dict):
                    count += count_items(value)
            return count
        
        def get_max_depth(config_dict, current_depth=0):
            if not isinstance(config_dict, dict):
                return current_depth
            
            max_depth = current_depth
            for value in config_dict.values():
                if isinstance(value, dict):
                    depth = get_max_depth(value, current_depth + 1)
                    max_depth = max(max_depth, depth)
            
            return max_depth
        
        return {
            'total_items': count_items(self.config),
            'top_level_keys': len(self.config),
            'max_depth': get_max_depth(self.config),
            'has_schema': bool(self.schema),
            'has_defaults': bool(self.defaults),
            'validator_count': len(self.validators)
        }

# 测试配置管理器
config_manager = ConfigManager()

# 定义配置模式
schema = {
    'database': {
        'host': {'required': True},
        'port': {'required': True},
        'username': {'required': True},
        'password': {'required': True}
    },
    'server': {
        'port': {'required': True},
        'debug': {'required': False}
    },
    'logging': {
        'level': {'required': True},
        'file': {'required': False}
    }
}

config_manager.define_schema(schema)

# 设置默认值
defaults = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'timeout': 30
    },
    'server': {
        'port': 8000,
        'debug': False,
        'workers': 4
    },
    'logging': {
        'level': 'INFO',
        'format': '%(asctime)s - %(levelname)s - %(message)s'
    }
}

config_manager.set_defaults(defaults)

# 添加验证器
config_manager.add_validator(
    'database.port',
    lambda x: isinstance(x, int) and 1 <= x <= 65535,
    "端口必须是1-65535之间的整数"
)

config_manager.add_validator(
    'server.port',
    lambda x: isinstance(x, int) and 1 <= x <= 65535,
    "端口必须是1-65535之间的整数"
)

config_manager.add_validator(
    'logging.level',
    lambda x: x in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
    "日志级别必须是有效的级别"
)

# 设置配置
print("\n设置配置:")
config_manager.set_config('database.username', 'admin')
config_manager.set_config('database.password', 'secret123')
config_manager.set_config('server.debug', True)
config_manager.set_config('logging.level', 'DEBUG')

# 获取配置
print(f"\n数据库配置: {config_manager.get_config('database')}")
print(f"服务器端口: {config_manager.get_config('server.port')}")
print(f"调试模式: {config_manager.get_config('server.debug')}")

# 配置摘要
summary = config_manager.get_config_summary()
print(f"\n配置摘要:")
print(f"  总配置项: {summary['total_items']}")
print(f"  顶级键数: {summary['top_level_keys']}")
print(f"  最大深度: {summary['max_depth']}")
print(f"  验证器数: {summary['validator_count']}")

# 搜索配置
print(f"\n搜索包含'port'的配置:")
search_results = config_manager.search_config('port')
for result in search_results:
    print(f"  {result['path']}: {result['match']} ({result['type']})")

# 导出配置
full_config = config_manager.export_config(include_defaults=True)
print(f"\n完整配置已导出 (包含 {len(str(full_config))} 字符)")

custom_config = config_manager.export_config(include_defaults=False)
print(f"自定义配置已导出 (包含 {len(str(custom_config))} 字符)")
```

## 练习6：数据去重和合并工具

### 题目描述

开发一个数据去重和合并工具，能够处理复杂的数据结构，识别重复项，并提供多种合并策略。

### 解决方案

```python
print("\n=== 练习6：数据去重和合并工具 ===")

from collections import defaultdict
import hashlib
import json

class DataDeduplicator:
    def __init__(self):
        # 去重策略
        self.strategies = {
            'first': self._keep_first,
            'last': self._keep_last,
            'merge': self._merge_records,
            'custom': None
        }
        
        # 相似度阈值
        self.similarity_threshold = 0.8
    
    def _keep_first(self, records):
        """保留第一个记录"""
        return records[0]
    
    def _keep_last(self, records):
        """保留最后一个记录"""
        return records[-1]
    
    def _merge_records(self, records):
        """合并记录"""
        if not records:
            return None
        
        merged = {}
        
        # 收集所有键
        all_keys = set()
        for record in records:
            if isinstance(record, dict):
                all_keys.update(record.keys())
        
        # 合并值
        for key in all_keys:
            values = []
            for record in records:
                if isinstance(record, dict) and key in record:
                    value = record[key]
                    if value is not None and value != '':
                        values.append(value)
            
            if values:
                # 根据值类型选择合并策略
                if all(isinstance(v, (int, float)) for v in values):
                    # 数值类型：取平均值
                    merged[key] = sum(values) / len(values)
                elif all(isinstance(v, str) for v in values):
                    # 字符串类型：取最长的或合并唯一值
                    unique_values = list(set(values))
                    if len(unique_values) == 1:
                        merged[key] = unique_values[0]
                    else:
                        merged[key] = ' | '.join(unique_values)
                elif all(isinstance(v, list) for v in values):
                    # 列表类型：合并并去重
                    combined = []
                    for v in values:
                        combined.extend(v)
                    merged[key] = list(set(combined))
                else:
                    # 其他类型：取第一个非空值
                    merged[key] = values[0]
        
        return merged
    
    def calculate_similarity(self, record1, record2, key_weights=None):
        """计算两个记录的相似度"""
        if not isinstance(record1, dict) or not isinstance(record2, dict):
            return 0.0
        
        all_keys = set(record1.keys()) | set(record2.keys())
        if not all_keys:
            return 1.0
        
        similarity_sum = 0.0
        total_weight = 0.0
        
        for key in all_keys:
            weight = key_weights.get(key, 1.0) if key_weights else 1.0
            total_weight += weight
            
            val1 = record1.get(key)
            val2 = record2.get(key)
            
            # 计算字段相似度
            field_similarity = self._calculate_field_similarity(val1, val2)
            similarity_sum += field_similarity * weight
        
        return similarity_sum / total_weight if total_weight > 0 else 0.0
    
    def _calculate_field_similarity(self, val1, val2):
        """计算字段相似度"""
        if val1 is None and val2 is None:
            return 1.0
        if val1 is None or val2 is None:
            return 0.0
        if val1 == val2:
            return 1.0
        
        # 字符串相似度（简化的编辑距离）
        if isinstance(val1, str) and isinstance(val2, str):
            return self._string_similarity(val1.lower(), val2.lower())
        
        # 数值相似度
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            max_val = max(abs(val1), abs(val2))
            if max_val == 0:
                return 1.0
            return 1.0 - abs(val1 - val2) / max_val
        
        # 列表相似度
        if isinstance(val1, list) and isinstance(val2, list):
            set1, set2 = set(val1), set(val2)
            intersection = len(set1 & set2)
            union = len(set1 | set2)
            return intersection / union if union > 0 else 0.0
        
        return 0.0
    
    def _string_similarity(self, s1, s2):
        """计算字符串相似度（Jaccard相似度）"""
        if not s1 and not s2:
            return 1.0
        if not s1 or not s2:
            return 0.0
        
        # 使用字符级别的Jaccard相似度
        set1 = set(s1)
        set2 = set(s2)
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        
        return intersection / union if union > 0 else 0.0
    
    def find_duplicates_exact(self, records, key_fields=None):
        """查找完全重复的记录"""
        if key_fields:
            # 基于指定字段的重复检测
            groups = defaultdict(list)
            
            for i, record in enumerate(records):
                if isinstance(record, dict):
                    key_values = tuple(record.get(field) for field in key_fields)
                    groups[key_values].append((i, record))
                else:
                    # 非字典类型，直接使用值作为键
                    groups[record].append((i, record))
            
            duplicates = {key: items for key, items in groups.items() if len(items) > 1}
        else:
            # 基于完整记录的重复检测
            groups = defaultdict(list)
            
            for i, record in enumerate(records):
                # 创建记录的哈希值
                record_hash = self._get_record_hash(record)
                groups[record_hash].append((i, record))
            
            duplicates = {key: items for key, items in groups.items() if len(items) > 1}
        
        return duplicates
    
    def find_duplicates_fuzzy(self, records, key_weights=None):
        """查找模糊重复的记录"""
        duplicate_groups = []
        processed = set()
        
        for i, record1 in enumerate(records):
            if i in processed:
                continue
            
            current_group = [(i, record1)]
            processed.add(i)
            
            for j, record2 in enumerate(records[i+1:], i+1):
                if j in processed:
                    continue
                
                similarity = self.calculate_similarity(record1, record2, key_weights)
                
                if similarity >= self.similarity_threshold:
                    current_group.append((j, record2))
                    processed.add(j)
            
            if len(current_group) > 1:
                duplicate_groups.append(current_group)
        
        return duplicate_groups
    
    def _get_record_hash(self, record):
        """获取记录的哈希值"""
        if isinstance(record, dict):
            # 对字典进行排序后序列化
            sorted_items = sorted(record.items())
            record_str = json.dumps(sorted_items, sort_keys=True, default=str)
        else:
            record_str = str(record)
        
        return hashlib.md5(record_str.encode()).hexdigest()
    
    def deduplicate(self, records, strategy='first', key_fields=None, key_weights=None, fuzzy=False):
        """去重处理"""
        if not records:
            return []
        
        # 查找重复项
        if fuzzy:
            duplicate_groups = self.find_duplicates_fuzzy(records, key_weights)
            # 转换格式以匹配exact方法的输出
            duplicates = {}
            for i, group in enumerate(duplicate_groups):
                duplicates[f"group_{i}"] = group
        else:
            duplicates = self.find_duplicates_exact(records, key_fields)
        
        # 应用去重策略
        strategy_func = self.strategies.get(strategy, self._keep_first)
        
        # 记录要保留的索引
        keep_indices = set(range(len(records)))
        deduplicated_records = []
        
        for group_key, duplicate_items in duplicates.items():
            indices = [item[0] for item in duplicate_items]
            duplicate_records = [item[1] for item in duplicate_items]
            
            # 应用策略选择保留的记录
            if strategy == 'custom' and hasattr(self, 'custom_strategy'):
                kept_record = self.custom_strategy(duplicate_records)
            else:
                kept_record = strategy_func(duplicate_records)
            
            # 移除重复项的索引，保留第一个
            for idx in indices[1:]:
                keep_indices.discard(idx)
            
            # 更新第一个记录
            if indices:
                records[indices[0]] = kept_record
        
        # 构建去重后的结果
        for i, record in enumerate(records):
            if i in keep_indices:
                deduplicated_records.append(record)
        
        return deduplicated_records
    
    def get_deduplication_report(self, original_records, deduplicated_records, duplicates=None):
        """生成去重报告"""
        original_count = len(original_records)
        deduplicated_count = len(deduplicated_records)
        removed_count = original_count - deduplicated_count
        
        report = {
            'original_count': original_count,
            'deduplicated_count': deduplicated_count,
            'removed_count': removed_count,
            'removal_rate': (removed_count / original_count * 100) if original_count > 0 else 0,
            'duplicate_groups': len(duplicates) if duplicates else 0
        }
        
        if duplicates:
            report['duplicate_details'] = []
            for group_key, items in duplicates.items():
                report['duplicate_details'].append({
                    'group': group_key,
                    'count': len(items),
                    'indices': [item[0] for item in items]
                })
        
        return report
    
    def merge_datasets(self, *datasets, merge_strategy='union'):
        """合并多个数据集"""
        if not datasets:
            return []
        
        if merge_strategy == 'union':
            # 简单合并所有记录
            merged = []
            for dataset in datasets:
                merged.extend(dataset)
            return merged
        
        elif merge_strategy == 'intersection':
            # 只保留在所有数据集中都存在的记录
            if len(datasets) < 2:
                return list(datasets[0]) if datasets else []
            
            common_records = []
            first_dataset = datasets[0]
            
            for record in first_dataset:
                found_in_all = True
                for other_dataset in datasets[1:]:
                    if not any(self.calculate_similarity(record, other_record) >= self.similarity_threshold 
                             for other_record in other_dataset):
                        found_in_all = False
                        break
                
                if found_in_all:
                    common_records.append(record)
            
            return common_records
        
        elif merge_strategy == 'smart_merge':
            # 智能合并：合并相似记录，保留唯一记录
            all_records = []
            for dataset in datasets:
                all_records.extend(dataset)
            
            return self.deduplicate(all_records, strategy='merge', fuzzy=True)
        
        else:
            raise ValueError(f"未知的合并策略: {merge_strategy}")

# 测试数据去重和合并工具
deduplicator = DataDeduplicator()

# 创建测试数据
test_records = [
    {'id': 1, 'name': '张三', 'email': 'zhangsan@email.com', 'age': 25, 'city': '北京'},
    {'id': 2, 'name': '李四', 'email': 'lisi@email.com', 'age': 30, 'city': '上海'},
    {'id': 3, 'name': '张三', 'email': 'zhangsan@email.com', 'age': 25, 'city': '北京'},  # 完全重复
    {'id': 4, 'name': '张三', 'email': 'zhangsan@gmail.com', 'age': 26, 'city': '北京'},  # 相似记录
    {'id': 5, 'name': '王五', 'email': 'wangwu@email.com', 'age': 28, 'city': '广州'},
    {'id': 6, 'name': '李四', 'email': 'lisi@email.com', 'age': 30, 'city': '上海'},  # 完全重复
    {'id': 7, 'name': '赵六', 'email': 'zhaoliu@email.com', 'age': 35, 'city': '深圳'}
]

print(f"原始记录数: {len(test_records)}")

# 完全匹配去重
print("\n=== 完全匹配去重 ===")
exact_duplicates = deduplicator.find_duplicates_exact(test_records, key_fields=['name', 'email'])
print(f"发现 {len(exact_duplicates)} 组完全重复:")
for key, items in exact_duplicates.items():
    print(f"  组 {key}: {len(items)} 条记录")
    for idx, record in items:
        print(f"    索引 {idx}: {record['name']} - {record['email']}")

# 应用去重
deduplicated_exact = deduplicator.deduplicate(test_records.copy(), strategy='first', key_fields=['name', 'email'])
print(f"\n完全匹配去重后记录数: {len(deduplicated_exact)}")

# 模糊匹配去重
print("\n=== 模糊匹配去重 ===")
deduplicator.similarity_threshold = 0.7
fuzzy_groups = deduplicator.find_duplicates_fuzzy(test_records)
print(f"发现 {len(fuzzy_groups)} 组相似记录:")
for i, group in enumerate(fuzzy_groups):
    print(f"  组 {i+1}: {len(group)} 条记录")
    for idx, record in group:
        print(f"    索引 {idx}: {record['name']} - {record['email']} - 年龄{record['age']}")

# 应用模糊去重
deduplicated_fuzzy = deduplicator.deduplicate(test_records.copy(), strategy='merge', fuzzy=True)
print(f"\n模糊匹配去重后记录数: {len(deduplicated_fuzzy)}")

# 生成去重报告
report = deduplicator.get_deduplication_report(test_records, deduplicated_fuzzy, 
                                              {f"group_{i}": group for i, group in enumerate(fuzzy_groups)})
print(f"\n去重报告:")
print(f"  原始记录: {report['original_count']}")
print(f"  去重后记录: {report['deduplicated_count']}")
print(f"  移除记录: {report['removed_count']}")
print(f"  去重率: {report['removal_rate']:.1f}%")
print(f"  重复组数: {report['duplicate_groups']}")

# 数据集合并测试
print("\n=== 数据集合并测试 ===")
dataset1 = test_records[:3]
dataset2 = test_records[2:5]
dataset3 = test_records[4:]

print(f"数据集1: {len(dataset1)} 条记录")
print(f"数据集2: {len(dataset2)} 条记录")
print(f"数据集3: {len(dataset3)} 条记录")

# 联合合并
union_result = deduplicator.merge_datasets(dataset1, dataset2, dataset3, merge_strategy='union')
print(f"\n联合合并结果: {len(union_result)} 条记录")

# 智能合并
smart_result = deduplicator.merge_datasets(dataset1, dataset2, dataset3, merge_strategy='smart_merge')
print(f"智能合并结果: {len(smart_result)} 条记录")

print("\n智能合并后的记录:")
for i, record in enumerate(smart_result):
    print(f"  {i+1}. {record['name']} - {record['email']} - 年龄{record.get('age', 'N/A')}")
```

## 学习要点

### 核心概念

1. **字典的综合应用**
   - 复杂数据结构的设计和管理
   - 嵌套字典的操作和遍历
   - 字典作为数据容器的高级用法

2. **数据处理技巧**
   - 数据验证和清洗
   - 统计分析和报表生成
   - 数据转换和格式化

3. **算法设计思维**
   - 问题分解和模块化设计
   - 数据结构的选择和优化
   - 异常处理和错误管理

### 实用技巧

1. **性能优化**
   - 使用`defaultdict`简化代码
   - 合理使用字典推导式
   - 避免不必要的深拷贝操作

2. **代码组织**
   - 类的设计和方法分离
   - 配置和数据的分离
   - 可扩展的架构设计

3. **错误处理**
   - 输入验证和边界检查
   - 优雅的错误恢复机制
   - 详细的日志和调试信息

### 最佳实践

1. **数据安全**
   - 使用深拷贝避免意外修改
   - 输入验证和类型检查
   - 敏感数据的保护

2. **可维护性**
   - 清晰的命名和注释
   - 模块化的功能设计
   - 完善的测试覆盖

3. **扩展性**
   - 插件化的架构设计
   - 配置驱动的功能实现
   - 标准化的接口定义

## 练习题

### 基础练习

1. **图书管理系统**
   - 实现图书的增删改查
   - 支持按多种条件搜索
   - 生成借阅统计报告

2. **员工信息管理**
   - 管理员工基本信息和部门关系
   - 计算薪资统计和绩效分析
   - 支持组织架构的动态调整

### 进阶练习

3. **网站访问日志分析**
   - 解析和分析Web服务器日志
   - 统计访问量、用户行为等指标
   - 生成可视化报表数据

4. **社交网络分析**
   - 构建用户关系图
   - 分析影响力和社区结构
   - 推荐算法的实现

### 实战练习

5. **电商数据分析平台**
   - 整合多源数据（订单、用户、商品）
   - 实现复杂的业务指标计算
   - 支持实时数据更新和查询

6. **智能配置管理系统**
   - 支持多环境配置管理
   - 实现配置的版本控制和回滚
   - 提供配置变更的影响分析

## 下一步学习

完成这些练习后，建议继续学习：

1. **数据库操作** - 学习如何将字典数据持久化到数据库
2. **Web开发** - 使用字典处理HTTP请求和响应数据
3. **数据科学** - 结合pandas等库进行更复杂的数据分析
4. **API开发** - 使用字典构建RESTful API的数据格式
5. **缓存系统** - 学习Redis等键值存储系统的使用

通过这些综合练习，你将能够熟练运用字典解决各种实际问题，为后续的高级编程学习打下坚实基础。