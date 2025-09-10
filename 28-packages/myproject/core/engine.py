
"""核心引擎模块"""

import time
import threading
from typing import Dict, Any, Optional

class EngineError(Exception):
    """引擎异常"""
    pass

class Engine:
    """核心引擎类"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.is_running = False
        self.start_time = None
        self.tasks = []
        self._lock = threading.Lock()
        
        print(f"引擎初始化完成，配置: {self.config}")
    
    def start(self):
        """启动引擎"""
        with self._lock:
            if self.is_running:
                raise EngineError("引擎已经在运行")
            
            self.is_running = True
            self.start_time = time.time()
            print("引擎启动成功")
    
    def stop(self):
        """停止引擎"""
        with self._lock:
            if not self.is_running:
                raise EngineError("引擎未运行")
            
            self.is_running = False
            self.start_time = None
            print("引擎已停止")
    
    def add_task(self, task_name: str, task_data: Any = None):
        """添加任务"""
        if not self.is_running:
            raise EngineError("引擎未运行，无法添加任务")
        
        task = {
            'name': task_name,
            'data': task_data,
            'created_at': time.time()
        }
        
        with self._lock:
            self.tasks.append(task)
        
        print(f"任务已添加: {task_name}")
        return len(self.tasks) - 1  # 返回任务ID
    
    def get_status(self):
        """获取引擎状态"""
        with self._lock:
            return {
                'running': self.is_running,
                'uptime': time.time() - self.start_time if self.start_time else 0,
                'task_count': len(self.tasks),
                'config': self.config.copy()
            }
    
    def process_tasks(self):
        """处理任务（模拟）"""
        if not self.is_running:
            raise EngineError("引擎未运行")
        
        with self._lock:
            processed = len(self.tasks)
            self.tasks.clear()
        
        print(f"处理了 {processed} 个任务")
        return processed
