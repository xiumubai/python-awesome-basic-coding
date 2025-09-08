#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字符串综合练习

本文件包含字符串相关的综合练习题目和解答：
1. 基础练习：字符串操作和方法
2. 中级练习：字符串处理和分析
3. 高级练习：复杂字符串算法
4. 实战练习：实际应用场景
5. 挑战练习：算法和数据结构
6. 项目练习：完整的字符串处理项目

作者：Python学习教程
日期：2024年
"""

import re
import string
import random
from collections import Counter, defaultdict
from typing import List, Dict, Tuple, Optional
import time

# ==================== 基础练习 ====================

def exercise_1_basic_operations():
    """练习1：基础字符串操作"""
    print("=== 练习1：基础字符串操作 ===")
    
    # 题目1：字符串反转
    def reverse_string(s: str) -> str:
        """反转字符串"""
        return s[::-1]
    
    # 题目2：统计字符频率
    def count_characters(s: str) -> Dict[str, int]:
        """统计字符串中每个字符的出现频率"""
        return dict(Counter(s.lower()))
    
    # 题目3：检查回文
    def is_palindrome(s: str) -> bool:
        """检查字符串是否为回文（忽略大小写和空格）"""
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        return cleaned == cleaned[::-1]
    
    # 题目4：首字母大写
    def capitalize_words(s: str) -> str:
        """将字符串中每个单词的首字母大写"""
        return ' '.join(word.capitalize() for word in s.split())
    
    # 题目5：移除重复字符
    def remove_duplicates(s: str) -> str:
        """移除字符串中的重复字符，保持原有顺序"""
        seen = set()
        result = []
        for char in s:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)
    
    # 测试用例
    test_cases = [
        "Hello World",
        "A man a plan a canal Panama",
        "programming",
        "  hello   world  ",
        "abcabcabc"
    ]
    
    print("基础操作测试结果：")
    print(f"{'原字符串':<25} {'反转':<25} {'回文?':<8} {'首字母大写':<25} {'去重':<15}")
    print("-" * 110)
    
    for test_str in test_cases:
        reversed_str = reverse_string(test_str)
        is_palin = is_palindrome(test_str)
        capitalized = capitalize_words(test_str)
        deduplicated = remove_duplicates(test_str)
        
        print(f"{test_str:<25} {reversed_str:<25} {'是' if is_palin else '否':<8} {capitalized:<25} {deduplicated:<15}")
    
    # 字符频率统计
    print("\n字符频率统计：")
    for test_str in test_cases[:2]:
        freq = count_characters(test_str)
        print(f"{test_str}: {dict(sorted(freq.items()))}")

def exercise_2_string_validation():
    """练习2：字符串验证"""
    print("\n=== 练习2：字符串验证 ===")
    
    # 题目1：密码强度检查
    def check_password_strength(password: str) -> Tuple[bool, List[str]]:
        """检查密码强度"""
        issues = []
        
        if len(password) < 8:
            issues.append("密码长度至少8位")
        if not re.search(r'[a-z]', password):
            issues.append("需要包含小写字母")
        if not re.search(r'[A-Z]', password):
            issues.append("需要包含大写字母")
        if not re.search(r'\d', password):
            issues.append("需要包含数字")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            issues.append("需要包含特殊字符")
        
        return len(issues) == 0, issues
    
    # 题目2：邮箱验证
    def validate_email(email: str) -> bool:
        """验证邮箱格式"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    # 题目3：手机号验证（中国）
    def validate_chinese_phone(phone: str) -> bool:
        """验证中国手机号格式"""
        pattern = r'^1[3-9]\d{9}$'
        return bool(re.match(pattern, phone))
    
    # 题目4：身份证验证（简化版）
    def validate_id_card(id_card: str) -> bool:
        """验证身份证号格式（简化版）"""
        if len(id_card) != 18:
            return False
        
        # 前17位必须是数字
        if not id_card[:17].isdigit():
            return False
        
        # 最后一位可以是数字或X
        if not (id_card[17].isdigit() or id_card[17].upper() == 'X'):
            return False
        
        return True
    
    # 题目5：URL验证
    def validate_url(url: str) -> bool:
        """验证URL格式"""
        pattern = r'^https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?$'
        return bool(re.match(pattern, url))
    
    # 测试数据
    test_data = {
        '密码': [
            'Password123!',
            'password',
            'PASSWORD',
            '12345678',
            'Pass123',
            'MySecureP@ssw0rd'
        ],
        '邮箱': [
            'user@example.com',
            'test.email@domain.co.uk',
            'invalid.email',
            '@domain.com',
            'user@',
            'user@domain'
        ],
        '手机号': [
            '13812345678',
            '15987654321',
            '12345678901',
            '1381234567',
            '138123456789',
            '11812345678'
        ],
        '身份证': [
            '110101199001011234',
            '11010119900101123X',
            '12345',
            '110101199001011',
            '110101199001011abc',
            '110101199001011235'
        ],
        'URL': [
            'https://www.example.com',
            'http://test.org/path?param=value',
            'https://domain.com:8080/path#section',
            'invalid-url',
            'ftp://example.com',
            'https://'
        ]
    }
    
    validators = {
        '密码': lambda x: check_password_strength(x)[0],
        '邮箱': validate_email,
        '手机号': validate_chinese_phone,
        '身份证': validate_id_card,
        'URL': validate_url
    }
    
    print("验证结果：")
    for data_type, test_values in test_data.items():
        print(f"\n{data_type}验证：")
        validator = validators[data_type]
        
        for value in test_values:
            if data_type == '密码':
                is_valid, issues = check_password_strength(value)
                status = "✓" if is_valid else "✗"
                issue_text = " (" + ", ".join(issues) + ")" if issues else ""
                print(f"  {status} {value:<20} {issue_text}")
            else:
                is_valid = validator(value)
                status = "✓" if is_valid else "✗"
                print(f"  {status} {value}")

def exercise_3_text_processing():
    """练习3：文本处理"""
    print("\n=== 练习3：文本处理 ===")
    
    # 题目1：单词统计
    def word_statistics(text: str) -> Dict[str, int]:
        """统计文本中单词出现频率"""
        # 转换为小写并移除标点符号
        words = re.findall(r'\b\w+\b', text.lower())
        return dict(Counter(words))
    
    # 题目2：文本摘要（简单版）
    def simple_summary(text: str, max_sentences: int = 3) -> str:
        """生成简单的文本摘要"""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        # 按句子长度排序，选择较长的句子作为摘要
        sentences.sort(key=len, reverse=True)
        summary_sentences = sentences[:max_sentences]
        
        return '. '.join(summary_sentences) + '.'
    
    # 题目3：敏感词过滤
    def filter_sensitive_words(text: str, sensitive_words: List[str]) -> str:
        """过滤敏感词"""
        filtered_text = text
        for word in sensitive_words:
            # 使用正则表达式进行不区分大小写的替换
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            filtered_text = pattern.sub('*' * len(word), filtered_text)
        return filtered_text
    
    # 题目4：文本格式化
    def format_paragraph(text: str, line_width: int = 50) -> str:
        """格式化段落，按指定宽度换行"""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + len(current_line) <= line_width:
                current_line.append(word)
                current_length += len(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return '\n'.join(lines)
    
    # 题目5：提取关键信息
    def extract_contact_info(text: str) -> Dict[str, List[str]]:
        """从文本中提取联系信息"""
        patterns = {
            'emails': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phones': r'\b(?:\+?1[-.]?)?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b',
            'urls': r'https?://[^\s]+',
            'dates': r'\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b'
        }
        
        result = {}
        for info_type, pattern in patterns.items():
            result[info_type] = re.findall(pattern, text)
        
        return result
    
    # 测试文本
    sample_text = """
    Python是一种高级编程语言，由Guido van Rossum在1989年发明。
    Python的设计哲学强调代码的可读性和简洁的语法。
    它支持多种编程范式，包括面向对象、命令式、函数式和过程式编程。
    Python拥有丰富的标准库，被广泛应用于Web开发、数据科学、人工智能等领域。
    如需了解更多信息，请访问https://www.python.org或发送邮件至info@python.org。
    联系电话：+1-555-123-4567，更新日期：2024-01-15。
    """
    
    print("文本处理示例：")
    print(f"原文本：{sample_text.strip()}")
    
    # 单词统计
    word_stats = word_statistics(sample_text)
    print(f"\n单词统计（前10个）：")
    for word, count in sorted(word_stats.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {word}: {count}")
    
    # 文本摘要
    summary = simple_summary(sample_text, 2)
    print(f"\n文本摘要：{summary}")
    
    # 敏感词过滤
    sensitive_words = ['Python', '人工智能', 'Web']
    filtered = filter_sensitive_words(sample_text, sensitive_words)
    print(f"\n敏感词过滤：{filtered[:100]}...")
    
    # 文本格式化
    formatted = format_paragraph(sample_text, 40)
    print(f"\n格式化文本（40字符宽度）：\n{formatted}")
    
    # 提取联系信息
    contact_info = extract_contact_info(sample_text)
    print(f"\n提取的联系信息：")
    for info_type, values in contact_info.items():
        if values:
            print(f"  {info_type}: {values}")

def exercise_4_string_algorithms():
    """练习4：字符串算法"""
    print("\n=== 练习4：字符串算法 ===")
    
    # 题目1：最长公共子序列
    def longest_common_subsequence(str1: str, str2: str) -> str:
        """找到两个字符串的最长公共子序列"""
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 填充DP表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # 重构LCS
        lcs = []
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                lcs.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        
        return ''.join(reversed(lcs))
    
    # 题目2：编辑距离
    def edit_distance(str1: str, str2: str) -> int:
        """计算两个字符串的编辑距离（Levenshtein距离）"""
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 初始化
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # 填充DP表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # 删除
                        dp[i][j-1],    # 插入
                        dp[i-1][j-1]   # 替换
                    )
        
        return dp[m][n]
    
    # 题目3：KMP字符串匹配
    def kmp_search(text: str, pattern: str) -> List[int]:
        """使用KMP算法搜索模式串在文本中的所有位置"""
        def compute_lps(pattern):
            """计算最长前缀后缀数组"""
            lps = [0] * len(pattern)
            length = 0
            i = 1
            
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        if not pattern:
            return []
        
        lps = compute_lps(pattern)
        matches = []
        i = j = 0
        
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            
            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return matches
    
    # 题目4：字符串压缩
    def compress_string(s: str) -> str:
        """压缩字符串（如aabcccccaaa -> a2b1c5a3）"""
        if not s:
            return s
        
        compressed = []
        current_char = s[0]
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                compressed.append(current_char + str(count))
                current_char = s[i]
                count = 1
        
        compressed.append(current_char + str(count))
        
        # 如果压缩后更长，返回原字符串
        compressed_str = ''.join(compressed)
        return compressed_str if len(compressed_str) < len(s) else s
    
    # 题目5：字符串解压缩
    def decompress_string(s: str) -> str:
        """解压缩字符串（如a2b1c5 -> aabccccc）"""
        result = []
        i = 0
        
        while i < len(s):
            char = s[i]
            i += 1
            
            # 读取数字
            num_str = ''
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            
            count = int(num_str) if num_str else 1
            result.append(char * count)
        
        return ''.join(result)
    
    # 测试算法
    print("字符串算法测试：")
    
    # 测试LCS
    str1, str2 = "ABCDGH", "AEDFHR"
    lcs = longest_common_subsequence(str1, str2)
    print(f"\n最长公共子序列：")
    print(f"  字符串1: {str1}")
    print(f"  字符串2: {str2}")
    print(f"  LCS: {lcs}")
    
    # 测试编辑距离
    edit_pairs = [
        ("kitten", "sitting"),
        ("hello", "world"),
        ("python", "java")
    ]
    
    print(f"\n编辑距离：")
    for s1, s2 in edit_pairs:
        distance = edit_distance(s1, s2)
        print(f"  '{s1}' -> '{s2}': {distance}")
    
    # 测试KMP搜索
    text = "ABABDABACDABABCABCABCABCABC"
    pattern = "ABABCAB"
    matches = kmp_search(text, pattern)
    print(f"\nKMP搜索：")
    print(f"  文本: {text}")
    print(f"  模式: {pattern}")
    print(f"  匹配位置: {matches}")
    
    # 测试字符串压缩
    test_strings = ["aabcccccaaa", "abcdef", "aabbcc", "aaaa"]
    print(f"\n字符串压缩：")
    for s in test_strings:
        compressed = compress_string(s)
        decompressed = decompress_string(compressed)
        print(f"  原始: {s} -> 压缩: {compressed} -> 解压: {decompressed}")

def exercise_5_practical_projects():
    """练习5：实际项目"""
    print("\n=== 练习5：实际项目 ===")
    
    # 项目1：简单的模板引擎
    class SimpleTemplateEngine:
        """简单的模板引擎"""
        
        def __init__(self):
            self.variables = {}
        
        def set_variable(self, name: str, value: str):
            """设置模板变量"""
            self.variables[name] = value
        
        def render(self, template: str) -> str:
            """渲染模板"""
            result = template
            
            # 替换变量 {{variable}}
            for var_name, var_value in self.variables.items():
                pattern = f'{{{{\s*{var_name}\s*}}}}'
                result = re.sub(pattern, str(var_value), result)
            
            # 处理条件语句 {% if condition %} ... {% endif %}
            result = self._process_conditions(result)
            
            # 处理循环 {% for item in items %} ... {% endfor %}
            result = self._process_loops(result)
            
            return result
        
        def _process_conditions(self, template: str) -> str:
            """处理条件语句"""
            pattern = r'{%\s*if\s+(\w+)\s*%}(.*?){%\s*endif\s*%}'
            
            def replace_condition(match):
                var_name = match.group(1)
                content = match.group(2)
                
                if var_name in self.variables and self.variables[var_name]:
                    return content
                return ''
            
            return re.sub(pattern, replace_condition, template, flags=re.DOTALL)
        
        def _process_loops(self, template: str) -> str:
            """处理循环语句"""
            pattern = r'{%\s*for\s+(\w+)\s+in\s+(\w+)\s*%}(.*?){%\s*endfor\s*%}'
            
            def replace_loop(match):
                item_name = match.group(1)
                list_name = match.group(2)
                content = match.group(3)
                
                if list_name in self.variables:
                    items = self.variables[list_name]
                    if isinstance(items, (list, tuple)):
                        result = []
                        for item in items:
                            item_content = content.replace(f'{{{{{item_name}}}}}', str(item))
                            result.append(item_content)
                        return ''.join(result)
                return ''
            
            return re.sub(pattern, replace_loop, template, flags=re.DOTALL)
    
    # 项目2：日志分析器
    class LogAnalyzer:
        """日志分析器"""
        
        def __init__(self):
            self.log_pattern = re.compile(
                r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
                r'\[(?P<level>\w+)\] '
                r'(?P<message>.+)'
            )
        
        def parse_log_file(self, log_content: str) -> List[Dict]:
            """解析日志文件"""
            logs = []
            for line in log_content.strip().split('\n'):
                match = self.log_pattern.match(line.strip())
                if match:
                    logs.append(match.groupdict())
            return logs
        
        def analyze_logs(self, logs: List[Dict]) -> Dict:
            """分析日志"""
            analysis = {
                'total_logs': len(logs),
                'level_counts': Counter(log['level'] for log in logs),
                'error_messages': [log['message'] for log in logs if log['level'] == 'ERROR'],
                'hourly_distribution': defaultdict(int)
            }
            
            # 按小时统计
            for log in logs:
                hour = log['timestamp'].split()[1].split(':')[0]
                analysis['hourly_distribution'][hour] += 1
            
            return analysis
        
        def generate_report(self, analysis: Dict) -> str:
            """生成分析报告"""
            report = []
            report.append("=== 日志分析报告 ===")
            report.append(f"总日志数: {analysis['total_logs']}")
            
            report.append("\n日志级别分布:")
            for level, count in analysis['level_counts'].items():
                percentage = (count / analysis['total_logs']) * 100
                report.append(f"  {level}: {count} ({percentage:.1f}%)")
            
            if analysis['error_messages']:
                report.append(f"\n错误消息 (前5条):")
                for i, msg in enumerate(analysis['error_messages'][:5], 1):
                    report.append(f"  {i}. {msg}")
            
            report.append("\n小时分布:")
            for hour in sorted(analysis['hourly_distribution'].keys()):
                count = analysis['hourly_distribution'][hour]
                report.append(f"  {hour}:00 - {count} 条日志")
            
            return '\n'.join(report)
    
    # 项目3：文本相似度计算器
    class TextSimilarity:
        """文本相似度计算器"""
        
        @staticmethod
        def jaccard_similarity(text1: str, text2: str) -> float:
            """计算Jaccard相似度"""
            words1 = set(re.findall(r'\b\w+\b', text1.lower()))
            words2 = set(re.findall(r'\b\w+\b', text2.lower()))
            
            intersection = words1.intersection(words2)
            union = words1.union(words2)
            
            return len(intersection) / len(union) if union else 0.0
        
        @staticmethod
        def cosine_similarity(text1: str, text2: str) -> float:
            """计算余弦相似度"""
            words1 = re.findall(r'\b\w+\b', text1.lower())
            words2 = re.findall(r'\b\w+\b', text2.lower())
            
            # 创建词频向量
            all_words = set(words1 + words2)
            vector1 = [words1.count(word) for word in all_words]
            vector2 = [words2.count(word) for word in all_words]
            
            # 计算余弦相似度
            dot_product = sum(a * b for a, b in zip(vector1, vector2))
            magnitude1 = sum(a * a for a in vector1) ** 0.5
            magnitude2 = sum(b * b for b in vector2) ** 0.5
            
            if magnitude1 == 0 or magnitude2 == 0:
                return 0.0
            
            return dot_product / (magnitude1 * magnitude2)
    
    # 测试项目
    print("实际项目测试：")
    
    # 测试模板引擎
    print("\n1. 模板引擎测试：")
    template_engine = SimpleTemplateEngine()
    template_engine.set_variable('name', 'Python')
    template_engine.set_variable('version', '3.12')
    template_engine.set_variable('show_features', True)
    template_engine.set_variable('features', ['简洁', '强大', '易学'])
    
    template = """
欢迎使用 {{name}} {{version}}！
{% if show_features %}
主要特性：
{% for feature in features %}
- {{feature}}
{% endfor %}
{% endif %}
    """.strip()
    
    rendered = template_engine.render(template)
    print(f"模板: {template}")
    print(f"渲染结果: {rendered}")
    
    # 测试日志分析器
    print("\n2. 日志分析器测试：")
    log_analyzer = LogAnalyzer()
    
    sample_logs = """
2024-01-15 10:30:45 [INFO] Application started
2024-01-15 10:31:02 [ERROR] Database connection failed
2024-01-15 10:31:15 [WARNING] High memory usage detected
2024-01-15 10:32:00 [INFO] User login successful
2024-01-15 11:30:30 [ERROR] File not found: config.txt
2024-01-15 11:31:45 [INFO] Backup completed
    """
    
    parsed_logs = log_analyzer.parse_log_file(sample_logs)
    analysis = log_analyzer.analyze_logs(parsed_logs)
    report = log_analyzer.generate_report(analysis)
    print(report)
    
    # 测试文本相似度
    print("\n3. 文本相似度测试：")
    text_pairs = [
        ("Python是一种编程语言", "Python是一门编程语言"),
        ("机器学习很有趣", "深度学习很复杂"),
        ("今天天气很好", "明天可能下雨")
    ]
    
    for text1, text2 in text_pairs:
        jaccard = TextSimilarity.jaccard_similarity(text1, text2)
        cosine = TextSimilarity.cosine_similarity(text1, text2)
        print(f"文本1: {text1}")
        print(f"文本2: {text2}")
        print(f"Jaccard相似度: {jaccard:.3f}")
        print(f"余弦相似度: {cosine:.3f}")
        print()

def exercise_6_performance_challenges():
    """练习6：性能挑战"""
    print("\n=== 练习6：性能挑战 ===")
    
    # 挑战1：大文本搜索优化
    def benchmark_search_methods(text: str, pattern: str, iterations: int = 1000):
        """比较不同搜索方法的性能"""
        methods = {
            'str.find()': lambda: text.find(pattern),
            'str.index()': lambda: text.index(pattern) if pattern in text else -1,
            're.search()': lambda: re.search(pattern, text),
            'in operator': lambda: pattern in text,
        }
        
        results = {}
        
        for method_name, method_func in methods.items():
            start_time = time.time()
            
            for _ in range(iterations):
                try:
                    method_func()
                except ValueError:
                    pass  # index() 方法可能抛出异常
            
            end_time = time.time()
            results[method_name] = end_time - start_time
        
        return results
    
    # 挑战2：字符串构建优化
    def benchmark_string_building(n: int = 10000):
        """比较不同字符串构建方法的性能"""
        methods = {
            '字符串连接': lambda: functools.reduce(lambda a, b: a + b, [str(i) for i in range(n)]),
            'join方法': lambda: ''.join(str(i) for i in range(n)),
            'StringIO': lambda: __import__('io').StringIO(''.join(str(i) for i in range(n))).getvalue(),
            '列表append': lambda: ''.join([str(i) for i in range(n)]),
        }
        
        results = {}
        
        for method_name, method_func in methods.items():
            start_time = time.time()
            method_func()
            end_time = time.time()
            results[method_name] = end_time - start_time
        
        return results
    
    # 挑战3：正则表达式优化
    def benchmark_regex_compilation():
        """比较编译和未编译正则表达式的性能"""
        text = "test@example.com, user@domain.org, admin@site.net" * 1000
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        compiled_pattern = re.compile(pattern)
        
        iterations = 1000
        
        # 未编译版本
        start_time = time.time()
        for _ in range(iterations):
            re.findall(pattern, text)
        uncompiled_time = time.time() - start_time
        
        # 编译版本
        start_time = time.time()
        for _ in range(iterations):
            compiled_pattern.findall(text)
        compiled_time = time.time() - start_time
        
        return {
            '未编译正则': uncompiled_time,
            '编译正则': compiled_time,
            '性能提升': uncompiled_time / compiled_time if compiled_time > 0 else 0
        }
    
    # 运行性能测试
    print("性能测试结果：")
    
    # 搜索方法性能测试
    large_text = "Python is a great programming language. " * 10000
    search_pattern = "programming"
    
    print(f"\n1. 搜索方法性能比较（文本长度: {len(large_text)}, 模式: '{search_pattern}'）:")
    search_results = benchmark_search_methods(large_text, search_pattern)
    
    fastest_method = min(search_results.items(), key=lambda x: x[1])
    
    for method, time_taken in sorted(search_results.items(), key=lambda x: x[1]):
        relative_speed = time_taken / fastest_method[1]
        print(f"  {method:<15}: {time_taken:.6f}秒 ({relative_speed:.2f}x)")
    
    # 字符串构建性能测试
    print(f"\n2. 字符串构建性能比较（构建{10000}个数字）:")
    import functools
    
    build_results = benchmark_string_building(1000)  # 减少数量以避免过长时间
    
    fastest_build = min(build_results.items(), key=lambda x: x[1])
    
    for method, time_taken in sorted(build_results.items(), key=lambda x: x[1]):
        relative_speed = time_taken / fastest_build[1]
        print(f"  {method:<15}: {time_taken:.6f}秒 ({relative_speed:.2f}x)")
    
    # 正则表达式编译性能测试
    print(f"\n3. 正则表达式编译性能比较:")
    regex_results = benchmark_regex_compilation()
    
    for method, time_taken in regex_results.items():
        if method == '性能提升':
            print(f"  {method}: {time_taken:.2f}倍")
        else:
            print(f"  {method}: {time_taken:.6f}秒")

def main():
    """主函数，运行所有练习"""
    print("Python字符串综合练习")
    print("=" * 50)
    
    # 运行所有练习
    exercise_1_basic_operations()
    exercise_2_string_validation()
    exercise_3_text_processing()
    exercise_4_string_algorithms()
    exercise_5_practical_projects()
    exercise_6_performance_challenges()
    
    print("\n=== 练习总结 ===")
    print("1. 基础操作：字符串反转、统计、回文检查等")
    print("2. 字符串验证：密码、邮箱、手机号等格式验证")
    print("3. 文本处理：单词统计、摘要生成、敏感词过滤")
    print("4. 字符串算法：LCS、编辑距离、KMP搜索")
    print("5. 实际项目：模板引擎、日志分析、相似度计算")
    print("6. 性能优化：搜索方法、字符串构建、正则编译")
    
    print("\n=== 学习建议 ===")
    print("1. 掌握字符串的基本操作和方法")
    print("2. 学会使用正则表达式处理复杂模式")
    print("3. 了解字符串算法的原理和应用")
    print("4. 注意性能优化，选择合适的方法")
    print("5. 多练习实际项目，提高解决问题的能力")
    
    print("\n=== 进阶方向 ===")
    print("1. 自然语言处理（NLP）")
    print("2. 文本挖掘和信息提取")
    print("3. 编译原理中的词法分析")
    print("4. 生物信息学中的序列分析")
    print("5. 网络安全中的模式匹配")

if __name__ == "__main__":
    main()