"""缓存插件 - 来自path2"""

class CachePlugin:
    """缓存插件类"""
    
    def __init__(self, max_size=100):
        self.name = "CachePlugin"
        self.version = "1.0.0"
        self.source = "path2"
        self.max_size = max_size
        self.cache = {}
        print(f"加载缓存插件 (来自 {self.source}, 最大容量: {max_size})")
    
    def set(self, key, value):
        """设置缓存"""
        if len(self.cache) >= self.max_size:
            # 简单的清理策略
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
            print(f"缓存已满，清理最旧的键: {oldest_key}")
        
        self.cache[key] = value
        print(f"设置缓存: {key} = {value}")
    
    def get(self, key):
        """获取缓存"""
        value = self.cache.get(key)
        print(f"获取缓存: {key} = {value}")
        return value
    
    def clear(self):
        """清空缓存"""
        count = len(self.cache)
        self.cache.clear()
        print(f"清空缓存，共清理 {count} 个项目")
    
    def get_info(self):
        """获取插件信息"""
        return {
            "name": self.name,
            "version": self.version,
            "source": self.source,
            "size": len(self.cache),
            "max_size": self.max_size
        }

print(f"缓存插件已加载 (来自 path2)")
