#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
集合推导式 (Set Comprehensions)

学习目标：
1. 理解集合推导式的基本语法
2. 掌握集合的去重特性在推导式中的应用
3. 学会使用集合推导式进行数据去重和筛选
4. 了解集合推导式在数据处理中的优势

作者：Python学习教程
日期：2024年
"""

def basic_set_comprehensions():
    """基本集合推导式语法"""
    print("=== 基本集合推导式 ===")
    
    # 基本语法：{expression for item in iterable}
    # 创建数字平方的集合
    squares_set = {x**2 for x in range(1, 6)}
    print(f"数字平方集合: {squares_set}")
    
    # 传统方法对比
    squares_traditional = set()
    for x in range(1, 6):
        squares_traditional.add(x**2)
    print(f"传统方法结果: {squares_traditional}")
    
    # 字符串长度集合
    words = ['apple', 'banana', 'cherry', 'date', 'apple']  # 注意有重复
    word_lengths = {len(word) for word in words}
    print(f"单词长度集合: {word_lengths}")
    
    # 字符集合
    text = "hello world"
    unique_chars = {char for char in text if char != ' '}
    print(f"唯一字符集合: {unique_chars}")
    
    print()

def deduplication_examples():
    """去重应用示例"""
    print("=== 去重应用示例 ===")
    
    # 列表去重
    numbers_with_duplicates = [1, 2, 3, 2, 4, 1, 5, 3, 6, 4]
    unique_numbers = {x for x in numbers_with_duplicates}
    print(f"原列表: {numbers_with_duplicates}")
    print(f"去重后: {sorted(unique_numbers)}")
    
    # 字符串去重
    words_with_duplicates = ['apple', 'banana', 'apple', 'cherry', 'banana', 'date']
    unique_words = {word for word in words_with_duplicates}
    print(f"原单词列表: {words_with_duplicates}")
    print(f"去重后: {sorted(unique_words)}")
    
    # 提取唯一的首字母
    names = ['Alice', 'Bob', 'Charlie', 'Anna', 'David', 'Amy']
    first_letters = {name[0] for name in names}
    print(f"姓名: {names}")
    print(f"唯一首字母: {sorted(first_letters)}")
    
    # 提取文件扩展名
    filenames = ['doc1.txt', 'image.jpg', 'script.py', 'data.csv', 'doc2.txt', 'photo.jpg']
    extensions = {filename.split('.')[-1] for filename in filenames}
    print(f"文件名: {filenames}")
    print(f"唯一扩展名: {sorted(extensions)}")
    
    print()

def conditional_set_comprehensions():
    """带条件的集合推导式"""
    print("=== 带条件的集合推导式 ===")
    
    # 语法：{expression for item in iterable if condition}
    # 筛选偶数
    numbers = range(1, 21)
    even_numbers = {x for x in numbers if x % 2 == 0}
    print(f"1-20中的偶数: {sorted(even_numbers)}")
    
    # 筛选长单词
    words = ['cat', 'elephant', 'dog', 'hippopotamus', 'ant', 'butterfly', 'cat']
    long_words = {word for word in words if len(word) > 5}
    print(f"长度大于5的单词: {sorted(long_words)}")
    
    # 筛选质数
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = {x for x in range(2, 50) if is_prime(x)}
    print(f"2-50之间的质数: {sorted(primes)}")
    
    # 多条件筛选
    numbers = range(1, 101)
    special_numbers = {x for x in numbers if x % 3 == 0 and x % 5 != 0}
    print(f"能被3整除但不能被5整除的数(前10个): {sorted(list(special_numbers))[:10]}")
    
    print()

def string_set_comprehensions():
    """字符串相关的集合推导式"""
    print("=== 字符串处理 ===")
    
    # 提取唯一字符
    text = "programming"
    unique_chars = {char for char in text}
    print(f"'{text}'中的唯一字符: {sorted(unique_chars)}")
    
    # 提取元音字母
    sentence = "The quick brown fox jumps over the lazy dog"
    vowels = {char.lower() for char in sentence if char.lower() in 'aeiou'}
    print(f"句子中的唯一元音: {sorted(vowels)}")
    
    # 提取数字字符
    mixed_text = "abc123def456ghi789xyz"
    digits = {char for char in mixed_text if char.isdigit()}
    print(f"混合文本中的数字: {sorted(digits)}")
    
    # 单词长度集合
    paragraph = "Python is a powerful programming language that is easy to learn"
    word_lengths = {len(word.strip('.,!?')) for word in paragraph.split()}
    print(f"段落中单词的长度集合: {sorted(word_lengths)}")
    
    # 域名提取
    emails = ['alice@gmail.com', 'bob@yahoo.com', 'charlie@gmail.com', 'diana@hotmail.com']
    domains = {email.split('@')[1] for email in emails}
    print(f"邮箱域名: {sorted(domains)}")
    
    print()

def mathematical_set_operations():
    """数学集合操作"""
    print("=== 数学集合操作 ===")
    
    # 创建两个集合
    set_a = {x for x in range(1, 11) if x % 2 == 0}  # 偶数
    set_b = {x for x in range(1, 11) if x % 3 == 0}  # 3的倍数
    
    print(f"集合A (偶数): {sorted(set_a)}")
    print(f"集合B (3的倍数): {sorted(set_b)}")
    
    # 集合运算
    print(f"并集 A ∪ B: {sorted(set_a | set_b)}")
    print(f"交集 A ∩ B: {sorted(set_a & set_b)}")
    print(f"差集 A - B: {sorted(set_a - set_b)}")
    print(f"对称差集 A ⊕ B: {sorted(set_a ^ set_b)}")
    
    # 使用推导式创建复杂集合
    # 完全平方数
    perfect_squares = {x**2 for x in range(1, 11)}
    print(f"\n完全平方数: {sorted(perfect_squares)}")
    
    # 立方数
    perfect_cubes = {x**3 for x in range(1, 6)}
    print(f"立方数: {sorted(perfect_cubes)}")
    
    # 既是平方数又是立方数的数
    sixth_powers = perfect_squares & perfect_cubes
    print(f"既是平方数又是立方数: {sorted(sixth_powers)}")
    
    print()

def nested_set_comprehensions():
    """嵌套集合推导式"""
    print("=== 嵌套集合推导式 ===")
    
    # 从二维列表中提取唯一元素
    matrix = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [1, 2, 3]]
    unique_elements = {item for row in matrix for item in row}
    print(f"矩阵: {matrix}")
    print(f"唯一元素: {sorted(unique_elements)}")
    
    # 从字符串列表中提取唯一字符
    words = ['hello', 'world', 'python', 'programming']
    unique_chars = {char for word in words for char in word}
    print(f"单词列表: {words}")
    print(f"唯一字符: {sorted(unique_chars)}")
    
    # 笛卡尔积的子集
    colors = ['red', 'blue', 'green']
    sizes = ['S', 'M', 'L']
    # 只选择特定组合
    combinations = {(color, size) for color in colors for size in sizes if color != 'red' or size != 'S'}
    print(f"颜色: {colors}")
    print(f"尺寸: {sizes}")
    print(f"过滤后的组合: {sorted(combinations)}")
    
    print()

def advanced_set_comprehensions():
    """高级集合推导式用法"""
    print("=== 高级用法 ===")
    
    # 使用函数处理
    def get_factors(n):
        return {i for i in range(1, n + 1) if n % i == 0}
    
    number = 24
    factors = get_factors(number)
    print(f"{number}的因数: {sorted(factors)}")
    
    # 多个数字的公共因数
    numbers = [12, 18, 24]
    common_factors = set.intersection(*[get_factors(n) for n in numbers])
    print(f"{numbers}的公共因数: {sorted(common_factors)}")
    
    # 处理复杂数据结构
    students = [
        {'name': 'Alice', 'subjects': ['Math', 'Science']},
        {'name': 'Bob', 'subjects': ['Math', 'English']},
        {'name': 'Charlie', 'subjects': ['Science', 'History']},
        {'name': 'Diana', 'subjects': ['Math', 'History']}
    ]
    
    # 提取所有科目
    all_subjects = {subject for student in students for subject in student['subjects']}
    print(f"所有科目: {sorted(all_subjects)}")
    
    # 提取学习数学的学生
    math_students = {student['name'] for student in students if 'Math' in student['subjects']}
    print(f"学习数学的学生: {sorted(math_students)}")
    
    # 文件路径处理
    file_paths = [
        '/home/user/documents/file1.txt',
        '/home/user/images/photo.jpg',
        '/home/user/documents/file2.pdf',
        '/var/log/system.log'
    ]
    
    # 提取唯一目录
    directories = {'/'.join(path.split('/')[:-1]) for path in file_paths}
    print(f"唯一目录: {sorted(directories)}")
    
    print()

def performance_comparison():
    """性能对比"""
    print("=== 性能对比 ===")
    
    import time
    
    # 大数据量测试
    data = list(range(50000)) * 2  # 创建有重复的大列表
    
    # 集合推导式去重
    start_time = time.time()
    unique_set_comp = {x for x in data}
    comp_time = time.time() - start_time
    
    # 传统方法去重
    start_time = time.time()
    unique_set_loop = set()
    for x in data:
        unique_set_loop.add(x)
    loop_time = time.time() - start_time
    
    # set()构造函数
    start_time = time.time()
    unique_set_constructor = set(data)
    constructor_time = time.time() - start_time
    
    print(f"处理{len(data)}个元素的去重:")
    print(f"集合推导式: {comp_time:.4f}秒")
    print(f"传统循环: {loop_time:.4f}秒")
    print(f"set构造函数: {constructor_time:.4f}秒")
    
    # 验证结果一致性
    print(f"结果一致性: {unique_set_comp == unique_set_loop == unique_set_constructor}")
    print(f"去重后元素数量: {len(unique_set_comp)}")
    
    print()

def practical_applications():
    """实际应用场景"""
    print("=== 实际应用场景 ===")
    
    # 数据清洗：去除重复的用户ID
    user_logs = [
        {'user_id': 1001, 'action': 'login'},
        {'user_id': 1002, 'action': 'view'},
        {'user_id': 1001, 'action': 'logout'},
        {'user_id': 1003, 'action': 'login'},
        {'user_id': 1002, 'action': 'purchase'}
    ]
    
    unique_users = {log['user_id'] for log in user_logs}
    print(f"活跃用户ID: {sorted(unique_users)}")
    
    # 标签去重
    articles = [
        {'title': 'Python Basics', 'tags': ['python', 'programming', 'beginner']},
        {'title': 'Advanced Python', 'tags': ['python', 'advanced', 'programming']},
        {'title': 'Web Development', 'tags': ['web', 'html', 'css', 'programming']}
    ]
    
    all_tags = {tag for article in articles for tag in article['tags']}
    print(f"所有标签: {sorted(all_tags)}")
    
    # IP地址去重
    access_logs = [
        '192.168.1.1 - GET /index.html',
        '192.168.1.2 - POST /login',
        '192.168.1.1 - GET /about.html',
        '10.0.0.1 - GET /index.html',
        '192.168.1.2 - GET /logout'
    ]
    
    unique_ips = {log.split()[0] for log in access_logs}
    print(f"唯一IP地址: {sorted(unique_ips)}")
    
    # 依赖关系分析
    packages = [
        {'name': 'requests', 'dependencies': ['urllib3', 'certifi']},
        {'name': 'flask', 'dependencies': ['werkzeug', 'jinja2']},
        {'name': 'django', 'dependencies': ['sqlparse', 'pytz']},
        {'name': 'fastapi', 'dependencies': ['starlette', 'pydantic']}
    ]
    
    all_dependencies = {dep for pkg in packages for dep in pkg['dependencies']}
    print(f"所有依赖包: {sorted(all_dependencies)}")
    
    print()

def common_mistakes():
    """常见错误和注意事项"""
    print("=== 常见错误和注意事项 ===")
    
    # 错误1：忘记集合的无序性
    print("❌ 注意集合是无序的")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    number_set = {x for x in numbers}
    print(f"原列表: {numbers}")
    print(f"集合（无序）: {number_set}")
    print(f"排序后: {sorted(number_set)}")
    
    # 错误2：期望保持插入顺序（Python 3.7+字典有序，但集合仍无序）
    print("\n❌ 集合不保证顺序")
    words = ['first', 'second', 'third', 'first']
    word_set = {word for word in words}
    print(f"原列表: {words}")
    print(f"集合: {word_set}")
    
    # 正确做法：需要顺序时使用其他数据结构
    from collections import OrderedDict
    ordered_unique = list(OrderedDict.fromkeys(words))
    print(f"保持顺序的去重: {ordered_unique}")
    
    # 错误3：尝试存储可变对象
    print("\n❌ 集合只能存储不可变对象")
    try:
        # 这会报错，因为列表是可变的
        # bad_set = {[1, 2], [3, 4]}
        pass
    except TypeError as e:
        print(f"错误: {e}")
    
    # 正确做法：使用元组
    good_set = {(1, 2), (3, 4), (1, 2)}  # 注意重复的(1,2)会被去除
    print(f"正确的集合: {good_set}")
    
    # 注意4：空集合的创建
    print("\n⚠️ 空集合的正确创建方式")
    empty_set = set()  # 正确
    not_empty_set = {}  # 这是空字典，不是空集合！
    print(f"空集合: {empty_set}, 类型: {type(empty_set)}")
    print(f"空字典: {not_empty_set}, 类型: {type(not_empty_set)}")
    
    print()

def main():
    """主函数"""
    print("Python 集合推导式学习教程")
    print("=" * 50)
    
    basic_set_comprehensions()
    deduplication_examples()
    conditional_set_comprehensions()
    string_set_comprehensions()
    mathematical_set_operations()
    nested_set_comprehensions()
    advanced_set_comprehensions()
    performance_comparison()
    practical_applications()
    common_mistakes()
    
    print("学习要点总结:")
    print("1. 集合推导式语法：{expression for item in iterable}")
    print("2. 自动去重，适合处理唯一性需求")
    print("3. 集合是无序的，不保证元素顺序")
    print("4. 只能存储不可变对象（数字、字符串、元组等）")
    print("5. 支持数学集合运算（并集、交集、差集等）")
    print("6. 性能优秀，特别适合大数据去重")
    print("7. 空集合使用set()创建，不是{}")

if __name__ == "__main__":
    main()