"""缓存插件 - 来自path3"""
import time

class CachePlugin:
    """缓存插件类"""
    
    def __init__(self, max_size=100):
        self.name = "CachePlugin"
        self.version = "1.0.0"
        self.source = "path3"
        self.max_size = max_size
        self.cache = {}
        self.access_times = {}
        print(f"加载缓存插件 (来自 {self.source}, 最大容量: {max_size})")
    
    def set(self, key, value, ttl=None):
        """设置缓存"""
        if len(self.cache) >= self.max_size:
            # 简单的LRU清理
            oldest_key = min(self.access_times.keys(), key=lambda k: self.access_times[k])
            del self.cache[oldest_key]
            del self.access_times[oldest_key]
            print(f"缓存已满，清理最旧的键: {oldest_key}")
        
        self.cache[key] = {
            "value": value,
            "created_time": time.time(),
            "ttl": ttl
        }
        self.access_times[key] = time.time()
        print(f"设置缓存: {key} = {value}")
    
    def get(self, key):
        """获取缓存"""
        if key in self.cache:
            item = self.cache[key]
            
            # 检查TTL
            if item["ttl"] and (time.time() - item["created_time"]) > item["ttl"]:
                del self.cache[key]
                del self.access_times[key]
                print(f"缓存已过期: {key}")
                return None
            
            # 更新访问时间
            self.access_times[key] = time.time()
            print(f"获取缓存: {key} = {item['value']}")
            return item["value"]
        else:
            print(f"缓存未找到: {key}")
            return None
    
    def clear(self):
        """清空缓存"""
        count = len(self.cache)
        self.cache.clear()
        self.access_times.clear()
        print(f"清空缓存，共清理 {count} 个项目")
    
    def get_stats(self):
        """获取缓存统计"""
        return {
            "name": self.name,
            "version": self.version,
            "source": self.source,
            "size": len(self.cache),
            "max_size": self.max_size
        }

print(f"缓存插件已加载 (来自 path3)")
