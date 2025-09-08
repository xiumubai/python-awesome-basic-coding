# 字符串综合练习

## 学习目标

通过本章的综合练习，你将能够：

- 掌握字符串的各种基础操作和高级技巧
- 学会字符串验证和格式检查的实现方法
- 理解文本处理和数据清洗的常用技术
- 掌握字符串算法的原理和实现
- 学会构建实际的字符串处理项目
- 了解字符串操作的性能优化技巧

## 练习1：基础操作

### 字符串反转

```python
def reverse_string(s: str) -> str:
    """反转字符串"""
    return s[::-1]

def reverse_string_recursive(s: str) -> str:
    """递归方式反转字符串"""
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string_recursive(s[:-1])

def reverse_string_iterative(s: str) -> str:
    """迭代方式反转字符串"""
    result = ""
    for char in s:
        result = char + result
    return result
```

### 字符频率统计

```python
def count_characters(s: str) -> dict:
    """统计字符频率"""
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def count_characters_counter(s: str) -> dict:
    """使用Counter统计字符频率"""
    from collections import Counter
    return dict(Counter(s))
```

### 回文检查

```python
def is_palindrome(s: str) -> bool:
    """检查是否为回文（忽略大小写和空格）"""
    # 清理字符串：只保留字母和数字，转换为小写
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def is_palindrome_two_pointers(s: str) -> bool:
    """使用双指针检查回文"""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True
```

## 练习2：字符串验证

### 密码强度检查

```python
import re

def check_password_strength(password: str) -> dict:
    """检查密码强度"""
    result = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    strength_score = sum(result.values())
    
    if strength_score >= 4:
        result['strength'] = 'Strong'
    elif strength_score >= 3:
        result['strength'] = 'Medium'
    else:
        result['strength'] = 'Weak'
    
    return result
```

### 邮箱验证

```python
def validate_email(email: str) -> bool:
    """验证邮箱格式"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_email_detailed(email: str) -> dict:
    """详细的邮箱验证"""
    result = {'valid': False, 'errors': []}
    
    if '@' not in email:
        result['errors'].append('缺少@符号')
        return result
    
    local, domain = email.rsplit('@', 1)
    
    # 检查本地部分
    if not local:
        result['errors'].append('本地部分不能为空')
    elif len(local) > 64:
        result['errors'].append('本地部分过长')
    
    # 检查域名部分
    if not domain:
        result['errors'].append('域名部分不能为空')
    elif '.' not in domain:
        result['errors'].append('域名缺少顶级域名')
    
    if not result['errors']:
        result['valid'] = validate_email(email)
        if not result['valid']:
            result['errors'].append('邮箱格式不正确')
    
    return result
```

## 练习3：文本处理

### 单词统计

```python
def count_words(text: str) -> dict:
    """统计单词频率"""
    # 清理文本，分割单词
    words = re.findall(r'\b\w+\b', text.lower())
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

def get_word_statistics(text: str) -> dict:
    """获取文本统计信息"""
    words = re.findall(r'\b\w+\b', text)
    sentences = re.split(r'[.!?]+', text)
    paragraphs = text.split('\n\n')
    
    return {
        'characters': len(text),
        'words': len(words),
        'sentences': len([s for s in sentences if s.strip()]),
        'paragraphs': len([p for p in paragraphs if p.strip()]),
        'avg_word_length': sum(len(word) for word in words) / len(words) if words else 0
    }
```

### 文本摘要生成

```python
def generate_summary(text: str, max_sentences: int = 3) -> str:
    """生成文本摘要（基于句子长度和关键词）"""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if len(sentences) <= max_sentences:
        return text
    
    # 简单的评分机制：句子长度和单词数量
    scored_sentences = []
    for sentence in sentences:
        words = len(sentence.split())
        score = words * len(sentence)  # 简单评分
        scored_sentences.append((score, sentence))
    
    # 选择得分最高的句子
    scored_sentences.sort(reverse=True)
    summary_sentences = [sent for _, sent in scored_sentences[:max_sentences]]
    
    return '. '.join(summary_sentences) + '.'
```

## 练习4：字符串算法

### 最长公共子序列

```python
def longest_common_subsequence(str1: str, str2: str) -> str:
    """找到两个字符串的最长公共子序列"""
    m, n = len(str1), len(str2)
    
    # 创建DP表
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
```

### 编辑距离

```python
def edit_distance(str1: str, str2: str) -> int:
    """计算两个字符串的编辑距离（Levenshtein距离）"""
    m, n = len(str1), len(str2)
    
    # 创建DP表
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 初始化边界条件
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
```

### KMP字符串匹配

```python
def kmp_search(text: str, pattern: str) -> list:
    """KMP算法进行字符串匹配"""
    def compute_lps(pattern):
        """计算最长前缀后缀数组"""
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        
        while i < m:
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
    
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    
    lps = compute_lps(pattern)
    matches = []
    
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches
```

## 练习5：实际项目

### 简单模板引擎

```python
class SimpleTemplateEngine:
    """简单的模板引擎"""
    
    def __init__(self):
        self.variables = {}
    
    def set_variable(self, name: str, value):
        """设置模板变量"""
        self.variables[name] = value
    
    def render(self, template: str) -> str:
        """渲染模板"""
        result = template
        
        # 处理变量替换 {{variable}}
        import re
        pattern = r'\{\{\s*(\w+)\s*\}\}'
        
        def replace_var(match):
            var_name = match.group(1)
            return str(self.variables.get(var_name, f'{{{{ {var_name} }}}}'))
        
        result = re.sub(pattern, replace_var, result)
        
        # 处理条件语句 {% if condition %}
        result = self._process_conditionals(result)
        
        # 处理循环语句 {% for item in items %}
        result = self._process_loops(result)
        
        return result
    
    def _process_conditionals(self, template: str) -> str:
        """处理条件语句"""
        import re
        
        pattern = r'\{%\s*if\s+(\w+)\s*%\}(.*?)\{%\s*endif\s*%\}'
        
        def replace_condition(match):
            condition = match.group(1)
            content = match.group(2)
            
            if condition in self.variables and self.variables[condition]:
                return content
            return ''
        
        return re.sub(pattern, replace_condition, template, flags=re.DOTALL)
    
    def _process_loops(self, template: str) -> str:
        """处理循环语句"""
        import re
        
        pattern = r'\{%\s*for\s+(\w+)\s+in\s+(\w+)\s*%\}(.*?)\{%\s*endfor\s*%\}'
        
        def replace_loop(match):
            item_var = match.group(1)
            list_var = match.group(2)
            content = match.group(3)
            
            if list_var not in self.variables:
                return ''
            
            result = []
            for item in self.variables[list_var]:
                # 临时设置循环变量
                old_value = self.variables.get(item_var)
                self.variables[item_var] = item
                
                # 渲染内容
                rendered_content = self.render(content)
                result.append(rendered_content)
                
                # 恢复原值
                if old_value is not None:
                    self.variables[item_var] = old_value
                else:
                    self.variables.pop(item_var, None)
            
            return ''.join(result)
        
        return re.sub(pattern, replace_loop, template, flags=re.DOTALL)
```

### 日志分析器

```python
import re
from datetime import datetime
from collections import defaultdict, Counter

class LogAnalyzer:
    """日志分析器"""
    
    def __init__(self):
        self.log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)'
    
    def parse_log_line(self, line: str) -> dict:
        """解析单行日志"""
        match = re.match(self.log_pattern, line.strip())
        if match:
            timestamp_str, level, message = match.groups()
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            
            return {
                'timestamp': timestamp,
                'level': level,
                'message': message,
                'raw': line.strip()
            }
        return None
    
    def parse_log_file(self, log_content: str) -> list:
        """解析日志文件内容"""
        logs = []
        for line in log_content.strip().split('\n'):
            if line.strip():
                parsed = self.parse_log_line(line)
                if parsed:
                    logs.append(parsed)
        return logs
    
    def analyze_logs(self, logs: list) -> dict:
        """分析日志数据"""
        if not logs:
            return {}
        
        # 统计各级别日志数量
        level_counts = Counter(log['level'] for log in logs)
        
        # 按小时统计日志数量
        hourly_counts = defaultdict(int)
        for log in logs:
            hour = log['timestamp'].strftime('%Y-%m-%d %H:00')
            hourly_counts[hour] += 1
        
        # 查找错误和警告
        errors = [log for log in logs if log['level'] == 'ERROR']
        warnings = [log for log in logs if log['level'] == 'WARNING']
        
        # 时间范围
        timestamps = [log['timestamp'] for log in logs]
        time_range = {
            'start': min(timestamps),
            'end': max(timestamps),
            'duration': max(timestamps) - min(timestamps)
        }
        
        return {
            'total_logs': len(logs),
            'level_counts': dict(level_counts),
            'hourly_counts': dict(hourly_counts),
            'errors': errors,
            'warnings': warnings,
            'time_range': time_range
        }
    
    def generate_report(self, analysis: dict) -> str:
        """生成分析报告"""
        if not analysis:
            return "没有可分析的日志数据"
        
        report = []
        report.append("=== 日志分析报告 ===")
        report.append(f"总日志条数: {analysis['total_logs']}")
        
        # 时间范围
        time_range = analysis['time_range']
        report.append(f"时间范围: {time_range['start']} 到 {time_range['end']}")
        report.append(f"持续时间: {time_range['duration']}")
        
        # 日志级别统计
        report.append("\n日志级别统计:")
        for level, count in analysis['level_counts'].items():
            percentage = (count / analysis['total_logs']) * 100
            report.append(f"  {level}: {count} ({percentage:.1f}%)")
        
        # 错误和警告
        if analysis['errors']:
            report.append(f"\n错误日志 ({len(analysis['errors'])} 条):")
            for error in analysis['errors'][:5]:  # 只显示前5条
                report.append(f"  {error['timestamp']}: {error['message']}")
            if len(analysis['errors']) > 5:
                report.append(f"  ... 还有 {len(analysis['errors']) - 5} 条错误")
        
        if analysis['warnings']:
            report.append(f"\n警告日志 ({len(analysis['warnings'])} 条):")
            for warning in analysis['warnings'][:3]:  # 只显示前3条
                report.append(f"  {warning['timestamp']}: {warning['message']}")
            if len(analysis['warnings']) > 3:
                report.append(f"  ... 还有 {len(analysis['warnings']) - 3} 条警告")
        
        return '\n'.join(report)
```

## 练习6：性能优化

### 搜索方法性能比较

```python
import time
import re

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
```

### 字符串构建性能比较

```python
import functools

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
```

## 完整示例代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python字符串综合练习

本文件包含了字符串处理的各种练习，从基础操作到高级算法，
涵盖了实际开发中常见的字符串处理需求。

练习内容：
1. 基础操作：反转、统计、回文检查等
2. 字符串验证：密码、邮箱、手机号等
3. 文本处理：单词统计、摘要生成、敏感词过滤
4. 字符串算法：LCS、编辑距离、KMP搜索
5. 实际项目：模板引擎、日志分析、相似度计算
6. 性能优化：搜索方法、字符串构建、正则编译
"""

import re
import time
import functools
from collections import Counter, defaultdict
from datetime import datetime
from typing import List, Dict, Tuple, Optional

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

if __name__ == "__main__":
    main()
```

## 运行示例

```bash
# 运行完整的练习程序
python3 10_exercises.py
```

输出示例：
```
Python字符串综合练习
==================================================

=== 练习1：基础操作 ===

1. 字符串反转测试：
原字符串: Hello, World!
切片反转: !dlroW ,olleH
递归反转: !dlroW ,olleH
迭代反转: !dlroW ,olleH

2. 字符频率统计：
字符串: programming
字符频率: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

3. 回文检查：
'A man a plan a canal Panama' 是回文: True
'race a car' 是回文: False

=== 练习2：字符串验证 ===

1. 密码强度检查：
Password123! 强度检查: {'length': True, 'uppercase': True, 'lowercase': True, 'digit': True, 'special': True, 'strength': 'Strong'}

2. 邮箱验证：
user@example.com 验证结果: True
invalid-email 验证结果: False

=== 练习总结 ===
1. 基础操作：字符串反转、统计、回文检查等
2. 字符串验证：密码、邮箱、手机号等格式验证
3. 文本处理：单词统计、摘要生成、敏感词过滤
4. 字符串算法：LCS、编辑距离、KMP搜索
5. 实际项目：模板引擎、日志分析、相似度计算
6. 性能优化：搜索方法、字符串构建、正则编译
```

## 学习要点

### 1. 基础操作掌握
- **字符串反转**：掌握切片、递归、迭代等多种方法
- **字符统计**：学会使用字典和Counter进行频率统计
- **回文检查**：理解字符串清理和双指针技术

### 2. 验证技术
- **正则表达式**：掌握复杂模式匹配
- **格式检查**：学会邮箱、电话、身份证等验证
- **密码强度**：理解多条件验证逻辑

### 3. 文本处理
- **单词统计**：掌握文本分析基础
- **摘要生成**：学会简单的文本提取算法
- **数据清洗**：理解文本预处理技术

### 4. 算法实现
- **动态规划**：LCS和编辑距离的经典应用
- **字符串匹配**：KMP算法的原理和实现
- **性能优化**：不同方法的时间复杂度分析

### 5. 实际应用
- **模板引擎**：理解模板解析和渲染
- **日志分析**：学会结构化数据处理
- **相似度计算**：掌握文本比较算法

## 实际应用场景

### 1. Web开发
- 用户输入验证和清理
- 模板渲染和内容生成
- URL路由和参数解析

### 2. 数据处理
- 日志文件分析和监控
- CSV/JSON数据清洗
- 文本挖掘和信息提取

### 3. 系统管理
- 配置文件解析
- 脚本参数处理
- 系统日志分析

### 4. 自然语言处理
- 文本预处理和清理
- 关键词提取和分析
- 文档相似度计算

## 注意事项

### 1. 性能考虑
- 大文本处理时选择合适的算法
- 正则表达式的编译和重用
- 字符串构建方法的选择

### 2. 内存管理
- 避免不必要的字符串复制
- 使用生成器处理大文件
- 及时释放临时变量

### 3. 编码处理
- 注意Unicode和字节的区别
- 处理不同编码格式的文本
- 避免编码错误和乱码

### 4. 错误处理
- 验证输入参数的有效性
- 处理边界情况和异常
- 提供友好的错误信息

## 下一步学习建议

### 1. 深入学习
- **正则表达式高级特性**：前瞻、后顾、条件匹配
- **字符串算法**：后缀数组、AC自动机
- **自然语言处理**：分词、词性标注、情感分析

### 2. 实践项目
- **文本编辑器**：实现查找替换、语法高亮
- **日志监控系统**：实时分析和告警
- **内容管理系统**：模板引擎和内容渲染

### 3. 性能优化
- **并行处理**：多线程文本处理
- **内存优化**：流式处理大文件
- **算法优化**：选择最适合的字符串算法

### 4. 相关技术
- **数据库操作**：文本字段的查询和索引
- **网络编程**：HTTP请求和响应处理
- **机器学习**：文本特征提取和分类

通过这些综合练习，你将全面掌握Python字符串处理的各种技术，为后续的高级应用打下坚实基础。