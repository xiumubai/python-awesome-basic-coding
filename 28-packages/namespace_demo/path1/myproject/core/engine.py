"""核心引擎模块 - 来自path1"""

class Engine:
    """核心引擎类"""
    
    def __init__(self, name="Engine"):
        self.name = name
        self.version = "1.0.0"
        self.source = "path1"
        print(f"创建引擎: {name} (来自 {self.source})")
    
    def start(self):
        """启动引擎"""
        print(f"引擎 {self.name} 已启动 (版本: {self.version})")
    
    def get_info(self):
        """获取引擎信息"""
        return {
            "name": self.name,
            "version": self.version,
            "source": self.source,
            "type": "core_engine"
        }

# 模块级别函数
def create_engine(name="默认引擎"):
    """创建引擎实例"""
    return Engine(name)

print(f"核心引擎模块已加载 (来自 path1)")
