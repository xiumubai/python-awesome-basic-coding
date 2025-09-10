
# 数据结构模块
class Stack:
    """栈数据结构"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """入栈"""
        self.items.append(item)
    
    def pop(self):
        """出栈"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self.items.pop()
    
    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self.items[-1]
    
    def is_empty(self):
        """检查栈是否为空"""
        return len(self.items) == 0
    
    def size(self):
        """获取栈大小"""
        return len(self.items)

class Queue:
    """队列数据结构"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """入队"""
        self.items.insert(0, item)
    
    def dequeue(self):
        """出队"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self.items.pop()
    
    def is_empty(self):
        """检查队列是否为空"""
        return len(self.items) == 0
    
    def size(self):
        """获取队列大小"""
        return len(self.items)
