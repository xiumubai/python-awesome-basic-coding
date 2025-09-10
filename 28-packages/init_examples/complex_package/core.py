
# 核心模块
class CoreClass:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello from {self.name}"
    
    def __str__(self):
        return f"CoreClass({self.name})"
