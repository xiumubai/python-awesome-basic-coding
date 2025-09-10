"""辅助工具 - 来自path3"""

class Helper:
    """辅助工具类"""
    
    def __init__(self):
        self.source = "path3"
        self.operations_count = 0
        print(f"创建辅助工具 (来自 {self.source})")
    
    def format_text(self, text, style="normal"):
        """格式化文本"""
        self.operations_count += 1
        
        styles = {
            "upper": text.upper(),
            "lower": text.lower(),
            "title": text.title(),
            "reverse": text[::-1],
            "normal": text
        }
        
        result = styles.get(style, text)
        print(f"格式化文本: '{text}' -> '{result}' (操作#{self.operations_count})")
        return result
    
    def calculate_hash(self, text):
        """计算简单哈希"""
        self.operations_count += 1
        hash_value = hash(text) % 1000000
        print(f"计算哈希: '{text}' -> {hash_value} (操作#{self.operations_count})")
        return hash_value
    
    def get_stats(self):
        """获取统计信息"""
        return {
            "source": self.source,
            "operations_count": self.operations_count
        }

print(f"辅助工具已加载 (来自 path3)")
