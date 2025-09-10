
# 文本处理模块
import re
from collections import Counter

def process_text(text):
    """处理文本：清理、标准化"""
    # 移除多余空格
    text = re.sub(r'\s+', ' ', text.strip())
    return text

def reverse_text(text):
    """反转文本"""
    return text[::-1]

def count_words(text):
    """统计单词数量"""
    words = text.lower().split()
    return Counter(words)

def capitalize_sentences(text):
    """句子首字母大写"""
    sentences = text.split('. ')
    capitalized = [s.capitalize() for s in sentences]
    return '. '.join(capitalized)

class TextAnalyzer:
    """文本分析器"""
    
    def __init__(self, text):
        self.text = text
        self.words = text.lower().split()
    
    def word_count(self):
        """单词总数"""
        return len(self.words)
    
    def unique_words(self):
        """唯一单词数"""
        return len(set(self.words))
    
    def most_common_words(self, n=5):
        """最常见的n个单词"""
        counter = Counter(self.words)
        return counter.most_common(n)
    
    def average_word_length(self):
        """平均单词长度"""
        if not self.words:
            return 0
        total_length = sum(len(word) for word in self.words)
        return total_length / len(self.words)
