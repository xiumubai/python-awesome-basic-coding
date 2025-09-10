"""引擎模块"""
import time
print(f"[{time.strftime('%H:%M:%S')}] 正在初始化 engine 模块")

# 模块级别变量
_module_init_time = time.time()

class Engine:
    """引擎类"""
    
    def __init__(self, name="默认引擎"):
        self.name = name
        self.running = False
        self.start_time = None
        print(f"  创建引擎实例: {name}")
    
    def start(self):
        """启动引擎"""
        if not self.running:
            self.running = True
            self.start_time = time.time()
            print(f"  引擎 {self.name} 已启动")
        else:
            print(f"  引擎 {self.name} 已经在运行中")
    
    def stop(self):
        """停止引擎"""
        if self.running:
            self.running = False
            run_time = time.time() - self.start_time if self.start_time else 0
            print(f"  引擎 {self.name} 已停止，运行时间: {run_time:.2f}秒")
        else:
            print(f"  引擎 {self.name} 未在运行")
    
    def get_status(self):
        """获取引擎状态"""
        return {
            "name": self.name,
            "running": self.running,
            "start_time": self.start_time,
            "module_init_time": _module_init_time
        }

print(f"[{time.strftime('%H:%M:%S')}] engine 模块初始化完成")
