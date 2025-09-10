# 多态练习题

本文档包含多个多态相关的练习题和实战项目，帮助你深入理解和应用多态的概念。

## 练习1：图形计算系统

设计一个图形计算系统，支持多种几何图形的面积和周长计算。

### 需求分析

- 支持圆形、矩形、三角形等基本图形
- 每种图形都能计算面积和周长
- 支持图形的缩放操作
- 能够批量处理多个图形

### 实现代码

```python
from abc import ABC, abstractmethod
from typing import List
import math

# 抽象图形基类
class Shape(ABC):
    """图形抽象基类"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def area(self) -> float:
        """计算面积"""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """计算周长"""
        pass
    
    @abstractmethod
    def scale(self, factor: float) -> 'Shape':
        """缩放图形"""
        pass
    
    def get_info(self) -> str:
        """获取图形信息"""
        return f"{self.name}: 面积={self.area():.2f}, 周长={self.perimeter():.2f}"
    
    def __str__(self) -> str:
        return self.get_info()

# 具体图形类
class Circle(Shape):
    """圆形类"""
    
    def __init__(self, radius: float):
        super().__init__("圆形")
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def scale(self, factor: float) -> 'Circle':
        return Circle(self.radius * factor)
    
    def get_info(self) -> str:
        return f"{self.name}(半径={self.radius:.2f}): 面积={self.area():.2f}, 周长={self.perimeter():.2f}"

class Rectangle(Shape):
    """矩形类"""
    
    def __init__(self, width: float, height: float):
        super().__init__("矩形")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def scale(self, factor: float) -> 'Rectangle':
        return Rectangle(self.width * factor, self.height * factor)
    
    def get_info(self) -> str:
        return f"{self.name}({self.width:.2f}x{self.height:.2f}): 面积={self.area():.2f}, 周长={self.perimeter():.2f}"

class Triangle(Shape):
    """三角形类"""
    
    def __init__(self, a: float, b: float, c: float):
        super().__init__("三角形")
        self.a = a
        self.b = b
        self.c = c
        
        # 验证三角形的有效性
        if not self._is_valid_triangle():
            raise ValueError("无效的三角形边长")
    
    def _is_valid_triangle(self) -> bool:
        """验证三角形是否有效"""
        return (self.a + self.b > self.c and 
                self.a + self.c > self.b and 
                self.b + self.c > self.a)
    
    def area(self) -> float:
        # 使用海伦公式计算面积
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c
    
    def scale(self, factor: float) -> 'Triangle':
        return Triangle(self.a * factor, self.b * factor, self.c * factor)
    
    def get_info(self) -> str:
        return f"{self.name}({self.a:.2f},{self.b:.2f},{self.c:.2f}): 面积={self.area():.2f}, 周长={self.perimeter():.2f}"

class Square(Rectangle):
    """正方形类（继承自矩形）"""
    
    def __init__(self, side: float):
        super().__init__(side, side)
        self.name = "正方形"
        self.side = side
    
    def scale(self, factor: float) -> 'Square':
        return Square(self.side * factor)
    
    def get_info(self) -> str:
        return f"{self.name}(边长={self.side:.2f}): 面积={self.area():.2f}, 周长={self.perimeter():.2f}"

# 图形计算器
class ShapeCalculator:
    """图形计算器"""
    
    def __init__(self):
        self.shapes: List[Shape] = []
    
    def add_shape(self, shape: Shape):
        """添加图形"""
        self.shapes.append(shape)
    
    def add_shapes(self, shapes: List[Shape]):
        """批量添加图形"""
        self.shapes.extend(shapes)
    
    def calculate_total_area(self) -> float:
        """计算总面积"""
        return sum(shape.area() for shape in self.shapes)
    
    def calculate_total_perimeter(self) -> float:
        """计算总周长"""
        return sum(shape.perimeter() for shape in self.shapes)
    
    def find_largest_area(self) -> Shape:
        """找到面积最大的图形"""
        if not self.shapes:
            return None
        return max(self.shapes, key=lambda shape: shape.area())
    
    def find_smallest_area(self) -> Shape:
        """找到面积最小的图形"""
        if not self.shapes:
            return None
        return min(self.shapes, key=lambda shape: shape.area())
    
    def scale_all_shapes(self, factor: float) -> List[Shape]:
        """缩放所有图形"""
        return [shape.scale(factor) for shape in self.shapes]
    
    def get_shapes_by_type(self, shape_type: type) -> List[Shape]:
        """按类型获取图形"""
        return [shape for shape in self.shapes if isinstance(shape, shape_type)]
    
    def get_statistics(self) -> dict:
        """获取统计信息"""
        if not self.shapes:
            return {"count": 0}
        
        areas = [shape.area() for shape in self.shapes]
        perimeters = [shape.perimeter() for shape in self.shapes]
        
        return {
            "count": len(self.shapes),
            "total_area": sum(areas),
            "total_perimeter": sum(perimeters),
            "average_area": sum(areas) / len(areas),
            "average_perimeter": sum(perimeters) / len(perimeters),
            "largest_area": max(areas),
            "smallest_area": min(areas)
        }
    
    def display_all_shapes(self):
        """显示所有图形信息"""
        if not self.shapes:
            print("没有图形")
            return
        
        print(f"共有 {len(self.shapes)} 个图形:")
        for i, shape in enumerate(self.shapes, 1):
            print(f"  {i}. {shape.get_info()}")

# 演示图形计算系统
def demonstrate_shape_calculator():
    """演示图形计算系统"""
    print("=== 图形计算系统练习 ===")
    
    # 创建图形计算器
    calculator = ShapeCalculator()
    
    # 创建各种图形
    shapes = [
        Circle(5.0),
        Rectangle(4.0, 6.0),
        Triangle(3.0, 4.0, 5.0),
        Square(4.0),
        Circle(3.0),
        Rectangle(2.0, 8.0)
    ]
    
    # 添加图形到计算器
    calculator.add_shapes(shapes)
    
    print("1. 所有图形信息:")
    calculator.display_all_shapes()
    
    # 计算统计信息
    stats = calculator.get_statistics()
    print(f"\n2. 统计信息:")
    print(f"   图形总数: {stats['count']}")
    print(f"   总面积: {stats['total_area']:.2f}")
    print(f"   总周长: {stats['total_perimeter']:.2f}")
    print(f"   平均面积: {stats['average_area']:.2f}")
    print(f"   平均周长: {stats['average_perimeter']:.2f}")
    
    # 找到最大和最小面积的图形
    largest = calculator.find_largest_area()
    smallest = calculator.find_smallest_area()
    print(f"\n3. 面积比较:")
    print(f"   最大面积: {largest.get_info()}")
    print(f"   最小面积: {smallest.get_info()}")
    
    # 按类型分组
    print(f"\n4. 按类型分组:")
    circles = calculator.get_shapes_by_type(Circle)
    rectangles = calculator.get_shapes_by_type(Rectangle)
    triangles = calculator.get_shapes_by_type(Triangle)
    
    print(f"   圆形数量: {len(circles)}")
    print(f"   矩形数量: {len(rectangles)}")
    print(f"   三角形数量: {len(triangles)}")
    
    # 缩放所有图形
    print(f"\n5. 缩放后的图形 (放大2倍):")
    scaled_shapes = calculator.scale_all_shapes(2.0)
    for i, shape in enumerate(scaled_shapes, 1):
        print(f"   {i}. {shape.get_info()}")
    
    print("\n=== 图形计算系统练习完成 ===\n")

demonstrate_shape_calculator()
```

## 练习2：排序算法比较系统

实现一个排序算法比较系统，支持多种排序算法的性能测试和比较。

### 实现代码

```python
from abc import ABC, abstractmethod
from typing import List, Tuple
import time
import random
import copy

# 排序算法抽象基类
class SortAlgorithm(ABC):
    """排序算法抽象基类"""
    
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        """排序方法"""
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """算法名称"""
        pass
    
    @property
    @abstractmethod
    def time_complexity(self) -> str:
        """时间复杂度"""
        pass
    
    @property
    @abstractmethod
    def space_complexity(self) -> str:
        """空间复杂度"""
        pass
    
    def get_info(self) -> str:
        """获取算法信息"""
        return f"{self.name} - 时间复杂度: {self.time_complexity}, 空间复杂度: {self.space_complexity}"

# 具体排序算法实现
class BubbleSort(SortAlgorithm):
    """冒泡排序"""
    
    @property
    def name(self) -> str:
        return "冒泡排序"
    
    @property
    def time_complexity(self) -> str:
        return "O(n²)"
    
    @property
    def space_complexity(self) -> str:
        return "O(1)"
    
    def sort(self, data: List[int]) -> List[int]:
        result = data.copy()
        n = len(result)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
            
            # 如果没有交换，说明已经有序
            if not swapped:
                break
        
        return result

class SelectionSort(SortAlgorithm):
    """选择排序"""
    
    @property
    def name(self) -> str:
        return "选择排序"
    
    @property
    def time_complexity(self) -> str:
        return "O(n²)"
    
    @property
    def space_complexity(self) -> str:
        return "O(1)"
    
    def sort(self, data: List[int]) -> List[int]:
        result = data.copy()
        n = len(result)
        
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if result[j] < result[min_idx]:
                    min_idx = j
            
            result[i], result[min_idx] = result[min_idx], result[i]
        
        return result

class InsertionSort(SortAlgorithm):
    """插入排序"""
    
    @property
    def name(self) -> str:
        return "插入排序"
    
    @property
    def time_complexity(self) -> str:
        return "O(n²)"
    
    @property
    def space_complexity(self) -> str:
        return "O(1)"
    
    def sort(self, data: List[int]) -> List[int]:
        result = data.copy()
        
        for i in range(1, len(result)):
            key = result[i]
            j = i - 1
            
            while j >= 0 and result[j] > key:
                result[j + 1] = result[j]
                j -= 1
            
            result[j + 1] = key
        
        return result

class QuickSort(SortAlgorithm):
    """快速排序"""
    
    @property
    def name(self) -> str:
        return "快速排序"
    
    @property
    def time_complexity(self) -> str:
        return "O(n log n)"
    
    @property
    def space_complexity(self) -> str:
        return "O(log n)"
    
    def sort(self, data: List[int]) -> List[int]:
        result = data.copy()
        self._quick_sort(result, 0, len(result) - 1)
        return result
    
    def _quick_sort(self, arr: List[int], low: int, high: int):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)
    
    def _partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

class MergeSort(SortAlgorithm):
    """归并排序"""
    
    @property
    def name(self) -> str:
        return "归并排序"
    
    @property
    def time_complexity(self) -> str:
        return "O(n log n)"
    
    @property
    def space_complexity(self) -> str:
        return "O(n)"
    
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data.copy()
        
        result = data.copy()
        self._merge_sort(result)
        return result
    
    def _merge_sort(self, arr: List[int]):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            
            self._merge_sort(left)
            self._merge_sort(right)
            
            i = j = k = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

class HeapSort(SortAlgorithm):
    """堆排序"""
    
    @property
    def name(self) -> str:
        return "堆排序"
    
    @property
    def time_complexity(self) -> str:
        return "O(n log n)"
    
    @property
    def space_complexity(self) -> str:
        return "O(1)"
    
    def sort(self, data: List[int]) -> List[int]:
        result = data.copy()
        n = len(result)
        
        # 构建最大堆
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(result, n, i)
        
        # 逐个提取元素
        for i in range(n - 1, 0, -1):
            result[0], result[i] = result[i], result[0]
            self._heapify(result, i, 0)
        
        return result
    
    def _heapify(self, arr: List[int], n: int, i: int):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)

# 排序性能测试器
class SortPerformanceTester:
    """排序性能测试器"""
    
    def __init__(self):
        self.algorithms: List[SortAlgorithm] = []
        self.test_results = []
    
    def add_algorithm(self, algorithm: SortAlgorithm):
        """添加排序算法"""
        self.algorithms.append(algorithm)
    
    def add_algorithms(self, algorithms: List[SortAlgorithm]):
        """批量添加排序算法"""
        self.algorithms.extend(algorithms)
    
    def generate_test_data(self, size: int, data_type: str = "random") -> List[int]:
        """生成测试数据"""
        if data_type == "random":
            return [random.randint(1, 1000) for _ in range(size)]
        elif data_type == "sorted":
            return list(range(1, size + 1))
        elif data_type == "reverse":
            return list(range(size, 0, -1))
        elif data_type == "nearly_sorted":
            data = list(range(1, size + 1))
            # 随机交换一些元素
            for _ in range(size // 10):
                i, j = random.randint(0, size - 1), random.randint(0, size - 1)
                data[i], data[j] = data[j], data[i]
            return data
        else:
            raise ValueError(f"不支持的数据类型: {data_type}")
    
    def test_algorithm(self, algorithm: SortAlgorithm, data: List[int]) -> Tuple[float, bool]:
        """测试单个算法"""
        start_time = time.time()
        sorted_data = algorithm.sort(data)
        end_time = time.time()
        
        # 验证排序结果是否正确
        is_correct = sorted_data == sorted(data)
        
        return end_time - start_time, is_correct
    
    def run_performance_test(self, data_sizes: List[int], data_types: List[str] = None):
        """运行性能测试"""
        if data_types is None:
            data_types = ["random"]
        
        self.test_results = []
        
        for data_type in data_types:
            for size in data_sizes:
                print(f"\n测试数据类型: {data_type}, 大小: {size}")
                print("-" * 50)
                
                # 生成测试数据
                test_data = self.generate_test_data(size, data_type)
                
                type_results = []
                
                for algorithm in self.algorithms:
                    try:
                        execution_time, is_correct = self.test_algorithm(algorithm, test_data)
                        
                        result = {
                            "algorithm": algorithm.name,
                            "data_type": data_type,
                            "data_size": size,
                            "execution_time": execution_time,
                            "is_correct": is_correct,
                            "time_complexity": algorithm.time_complexity,
                            "space_complexity": algorithm.space_complexity
                        }
                        
                        type_results.append(result)
                        self.test_results.append(result)
                        
                        status = "✓" if is_correct else "✗"
                        print(f"{status} {algorithm.name:12} - {execution_time:.6f}秒 ({algorithm.time_complexity})")
                        
                    except Exception as e:
                        print(f"✗ {algorithm.name:12} - 错误: {str(e)}")
                
                # 显示本轮最快的算法
                if type_results:
                    fastest = min(type_results, key=lambda x: x["execution_time"])
                    print(f"\n最快算法: {fastest['algorithm']} ({fastest['execution_time']:.6f}秒)")
    
    def get_performance_summary(self) -> dict:
        """获取性能总结"""
        if not self.test_results:
            return {}
        
        summary = {}
        
        # 按算法分组
        for result in self.test_results:
            algo_name = result["algorithm"]
            if algo_name not in summary:
                summary[algo_name] = {
                    "total_time": 0,
                    "test_count": 0,
                    "success_count": 0,
                    "time_complexity": result["time_complexity"],
                    "space_complexity": result["space_complexity"]
                }
            
            summary[algo_name]["total_time"] += result["execution_time"]
            summary[algo_name]["test_count"] += 1
            if result["is_correct"]:
                summary[algo_name]["success_count"] += 1
        
        # 计算平均时间和成功率
        for algo_name in summary:
            algo_summary = summary[algo_name]
            algo_summary["average_time"] = algo_summary["total_time"] / algo_summary["test_count"]
            algo_summary["success_rate"] = algo_summary["success_count"] / algo_summary["test_count"]
        
        return summary
    
    def display_performance_summary(self):
        """显示性能总结"""
        summary = self.get_performance_summary()
        
        if not summary:
            print("没有测试结果")
            return
        
        print("\n=== 性能总结 ===")
        print(f"{'算法名称':12} {'平均时间':>10} {'成功率':>8} {'时间复杂度':>12} {'空间复杂度':>12}")
        print("-" * 70)
        
        # 按平均时间排序
        sorted_algos = sorted(summary.items(), key=lambda x: x[1]["average_time"])
        
        for algo_name, algo_data in sorted_algos:
            avg_time = algo_data["average_time"]
            success_rate = algo_data["success_rate"] * 100
            time_complexity = algo_data["time_complexity"]
            space_complexity = algo_data["space_complexity"]
            
            print(f"{algo_name:12} {avg_time:>10.6f}s {success_rate:>7.1f}% {time_complexity:>12} {space_complexity:>12}")

# 演示排序算法比较系统
def demonstrate_sort_comparison():
    """演示排序算法比较系统"""
    print("=== 排序算法比较系统练习 ===")
    
    # 创建性能测试器
    tester = SortPerformanceTester()
    
    # 添加各种排序算法
    algorithms = [
        BubbleSort(),
        SelectionSort(),
        InsertionSort(),
        QuickSort(),
        MergeSort(),
        HeapSort()
    ]
    
    tester.add_algorithms(algorithms)
    
    print("1. 算法信息:")
    for algorithm in algorithms:
        print(f"   {algorithm.get_info()}")
    
    # 运行性能测试
    print("\n2. 性能测试:")
    data_sizes = [100, 500, 1000]
    data_types = ["random", "sorted", "reverse"]
    
    tester.run_performance_test(data_sizes, data_types)
    
    # 显示性能总结
    tester.display_performance_summary()
    
    print("\n=== 排序算法比较系统练习完成 ===\n")

demonstrate_sort_comparison()
```

## 练习3：数据库连接器系统

设计一个数据库连接器系统，支持多种数据库类型的统一操作接口。

### 实现代码

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import json
import random
from datetime import datetime

# 数据库连接器抽象基类
class DatabaseConnector(ABC):
    """数据库连接器抽象基类"""
    
    def __init__(self, host: str, port: int, database: str, username: str, password: str):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.is_connected = False
    
    @abstractmethod
    def connect(self) -> bool:
        """连接数据库"""
        pass
    
    @abstractmethod
    def disconnect(self) -> bool:
        """断开连接"""
        pass
    
    @abstractmethod
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """执行查询"""
        pass
    
    @abstractmethod
    def execute_update(self, query: str) -> int:
        """执行更新操作"""
        pass
    
    @abstractmethod
    def create_table(self, table_name: str, columns: Dict[str, str]) -> bool:
        """创建表"""
        pass
    
    @abstractmethod
    def insert_data(self, table_name: str, data: Dict[str, Any]) -> bool:
        """插入数据"""
        pass
    
    @abstractmethod
    def update_data(self, table_name: str, data: Dict[str, Any], condition: str) -> int:
        """更新数据"""
        pass
    
    @abstractmethod
    def delete_data(self, table_name: str, condition: str) -> int:
        """删除数据"""
        pass
    
    @property
    @abstractmethod
    def db_type(self) -> str:
        """数据库类型"""
        pass
    
    def get_connection_info(self) -> str:
        """获取连接信息"""
        return f"{self.db_type} - {self.host}:{self.port}/{self.database}"
    
    def is_connection_active(self) -> bool:
        """检查连接是否活跃"""
        return self.is_connected

# MySQL连接器
class MySQLConnector(DatabaseConnector):
    """MySQL数据库连接器"""
    
    def __init__(self, host: str, port: int, database: str, username: str, password: str):
        super().__init__(host, port, database, username, password)
        self.tables = {}  # 模拟表数据
    
    @property
    def db_type(self) -> str:
        return "MySQL"
    
    def connect(self) -> bool:
        """连接MySQL数据库"""
        print(f"连接到MySQL数据库: {self.host}:{self.port}/{self.database}")
        # 模拟连接过程
        self.is_connected = True
        return True
    
    def disconnect(self) -> bool:
        """断开MySQL连接"""
        print(f"断开MySQL连接: {self.database}")
        self.is_connected = False
        return True
    
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """执行MySQL查询"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        print(f"执行MySQL查询: {query}")
        
        # 模拟查询结果
        if "SELECT" in query.upper():
            return [
                {"id": i, "name": f"用户{i}", "email": f"user{i}@mysql.com"}
                for i in range(1, random.randint(3, 6))
            ]
        return []
    
    def execute_update(self, query: str) -> int:
        """执行MySQL更新操作"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        print(f"执行MySQL更新: {query}")
        return random.randint(1, 5)  # 模拟影响的行数
    
    def create_table(self, table_name: str, columns: Dict[str, str]) -> bool:
        """创建MySQL表"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        column_defs = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
        query = f"CREATE TABLE {table_name} ({column_defs})"
        print(f"创建MySQL表: {query}")
        
        self.tables[table_name] = []
        return True
    
    def insert_data(self, table_name: str, data: Dict[str, Any]) -> bool:
        """插入数据到MySQL表"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        columns = ", ".join(data.keys())
        values = ", ".join([f"'{v}'" if isinstance(v, str) else str(v) for v in data.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        print(f"插入MySQL数据: {query}")
        
        if table_name not in self.tables:
            self.tables[table_name] = []
        self.tables[table_name].append(data)
        return True
    
    def update_data(self, table_name: str, data: Dict[str, Any], condition: str) -> int:
        """更新MySQL数据"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        set_clause = ", ".join([f"{k}='{v}'" if isinstance(v, str) else f"{k}={v}" for k, v in data.items()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        print(f"更新MySQL数据: {query}")
        return random.randint(0, 3)
    
    def delete_data(self, table_name: str, condition: str) -> int:
        """删除MySQL数据"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        query = f"DELETE FROM {table_name} WHERE {condition}"
        print(f"删除MySQL数据: {query}")
        return random.randint(0, 2)

# PostgreSQL连接器
class PostgreSQLConnector(DatabaseConnector):
    """PostgreSQL数据库连接器"""
    
    def __init__(self, host: str, port: int, database: str, username: str, password: str):
        super().__init__(host, port, database, username, password)
        self.schemas = {"public": {}}  # 模拟模式和表
    
    @property
    def db_type(self) -> str:
        return "PostgreSQL"
    
    def connect(self) -> bool:
        """连接PostgreSQL数据库"""
        print(f"连接到PostgreSQL数据库: {self.host}:{self.port}/{self.database}")
        self.is_connected = True
        return True
    
    def disconnect(self) -> bool:
        """断开PostgreSQL连接"""
        print(f"断开PostgreSQL连接: {self.database}")
        self.is_connected = False
        return True
    
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """执行PostgreSQL查询"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        print(f"执行PostgreSQL查询: {query}")
        
        if "SELECT" in query.upper():
            return [
                {"id": i, "name": f"用户{i}", "email": f"user{i}@postgresql.com", "created_at": datetime.now()}
                for i in range(1, random.randint(3, 6))
            ]
        return []
    
    def execute_update(self, query: str) -> int:
        """执行PostgreSQL更新操作"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        print(f"执行PostgreSQL更新: {query}")
        return random.randint(1, 5)
    
    def create_table(self, table_name: str, columns: Dict[str, str]) -> bool:
        """创建PostgreSQL表"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        column_defs = ", \n    ".join([f"{col} {dtype}" for col, dtype in columns.items()])
        query = f"CREATE TABLE {table_name} (\n    {column_defs}\n)"
        print(f"创建PostgreSQL表: {query}")
        
        self.schemas["public"][table_name] = []
        return True
    
    def insert_data(self, table_name: str, data: Dict[str, Any]) -> bool:
        """插入数据到PostgreSQL表"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        columns = ", ".join(data.keys())
        values = ", ".join([f"'{v}'" if isinstance(v, str) else str(v) for v in data.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        print(f"插入PostgreSQL数据: {query}")
        
        if table_name not in self.schemas["public"]:
            self.schemas["public"][table_name] = []
        self.schemas["public"][table_name].append(data)
        return True
    
    def update_data(self, table_name: str, data: Dict[str, Any], condition: str) -> int:
        """更新PostgreSQL数据"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        set_clause = ", ".join([f"{k}='{v}'" if isinstance(v, str) else f"{k}={v}" for k, v in data.items()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        print(f"更新PostgreSQL数据: {query}")
        return random.randint(0, 3)
    
    def delete_data(self, table_name: str, condition: str) -> int:
        """删除PostgreSQL数据"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        query = f"DELETE FROM {table_name} WHERE {condition}"
        print(f"删除PostgreSQL数据: {query}")
        return random.randint(0, 2)

# SQLite连接器
class SQLiteConnector(DatabaseConnector):
    """SQLite数据库连接器"""
    
    def __init__(self, database_file: str):
        super().__init__("localhost", 0, database_file, "", "")
        self.database_file = database_file
        self.tables = {}  # 模拟表数据
    
    @property
    def db_type(self) -> str:
        return "SQLite"
    
    def connect(self) -> bool:
        """连接SQLite数据库"""
        print(f"连接到SQLite数据库: {self.database_file}")
        self.is_connected = True
        return True
    
    def disconnect(self) -> bool:
        """断开SQLite连接"""
        print(f"断开SQLite连接: {self.database_file}")
        self.is_connected = False
        return True
    
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """执行SQLite查询"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        print(f"执行SQLite查询: {query}")
        
        if "SELECT" in query.upper():
            return [
                {"id": i, "name": f"用户{i}", "email": f"user{i}@sqlite.com"}
                for i in range(1, random.randint(2, 5))
            ]
        return []
    
    def execute_update(self, query: str) -> int:
        """执行SQLite更新操作"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        print(f"执行SQLite更新: {query}")
        return random.randint(1, 3)
    
    def create_table(self, table_name: str, columns: Dict[str, str]) -> bool:
        """创建SQLite表"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        column_defs = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
        query = f"CREATE TABLE {table_name} ({column_defs})"
        print(f"创建SQLite表: {query}")
        
        self.tables[table_name] = []
        return True
    
    def insert_data(self, table_name: str, data: Dict[str, Any]) -> bool:
        """插入数据到SQLite表"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        print(f"插入SQLite数据: {query} with values {list(data.values())}")
        
        if table_name not in self.tables:
            self.tables[table_name] = []
        self.tables[table_name].append(data)
        return True
    
    def update_data(self, table_name: str, data: Dict[str, Any], condition: str) -> int:
        """更新SQLite数据"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        set_clause = ", ".join([f"{k}=?" for k in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        print(f"更新SQLite数据: {query} with values {list(data.values())}")
        return random.randint(0, 2)
    
    def delete_data(self, table_name: str, condition: str) -> int:
        """删除SQLite数据"""
        if not self.is_connected:
            raise Exception("数据库未连接")
        
        query = f"DELETE FROM {table_name} WHERE {condition}"
        print(f"删除SQLite数据: {query}")
        return random.randint(0, 2)

# 数据库管理器
class DatabaseManager:
    """数据库管理器"""
    
    def __init__(self):
        self.connectors: Dict[str, DatabaseConnector] = {}
        self.active_connector: Optional[DatabaseConnector] = None
    
    def add_connector(self, name: str, connector: DatabaseConnector):
        """添加数据库连接器"""
        self.connectors[name] = connector
    
    def connect_to_database(self, name: str) -> bool:
        """连接到指定数据库"""
        if name not in self.connectors:
            print(f"未找到数据库连接器: {name}")
            return False
        
        connector = self.connectors[name]
        if connector.connect():
            self.active_connector = connector
            print(f"成功连接到: {connector.get_connection_info()}")
            return True
        return False
    
    def disconnect_current(self) -> bool:
        """断开当前连接"""
        if self.active_connector:
            result = self.active_connector.disconnect()
            self.active_connector = None
            return result
        return True
    
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """在当前连接上执行查询"""
        if not self.active_connector:
            raise Exception("没有活跃的数据库连接")
        return self.active_connector.execute_query(query)
    
    def create_user_table(self) -> bool:
        """创建用户表（演示用）"""
        if not self.active_connector:
            raise Exception("没有活跃的数据库连接")
        
        columns = {
            "id": "INTEGER PRIMARY KEY",
            "name": "VARCHAR(100)",
            "email": "VARCHAR(255)",
            "created_at": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
        }
        
        return self.active_connector.create_table("users", columns)
    
    def insert_sample_users(self) -> bool:
        """插入示例用户数据"""
        if not self.active_connector:
            raise Exception("没有活跃的数据库连接")
        
        sample_users = [
            {"name": "张三", "email": "zhangsan@example.com"},
            {"name": "李四", "email": "lisi@example.com"},
            {"name": "王五", "email": "wangwu@example.com"}
        ]
        
        for user in sample_users:
            self.active_connector.insert_data("users", user)
        
        return True
    
    def get_current_connection_info(self) -> str:
        """获取当前连接信息"""
        if self.active_connector:
            return self.active_connector.get_connection_info()
        return "无活跃连接"
    
    def list_connectors(self) -> List[str]:
        """列出所有连接器"""
        return list(self.connectors.keys())
    
    def test_all_connectors(self):
        """测试所有连接器"""
        print("\n=== 测试所有数据库连接器 ===")
        
        for name, connector in self.connectors.items():
            print(f"\n测试 {name} ({connector.db_type}):")
            print("-" * 40)
            
            try:
                # 连接
                if self.connect_to_database(name):
                    # 创建表
                    self.create_user_table()
                    
                    # 插入数据
                    self.insert_sample_users()
                    
                    # 查询数据
                    results = self.execute_query("SELECT * FROM users")
                    print(f"查询结果: {len(results)} 条记录")
                    
                    # 更新数据
                    updated = self.active_connector.update_data(
                        "users", 
                        {"email": "newemail@example.com"}, 
                        "name='张三'"
                    )
                    print(f"更新了 {updated} 条记录")
                    
                    # 删除数据
                    deleted = self.active_connector.delete_data("users", "name='李四'")
                    print(f"删除了 {deleted} 条记录")
                    
                    # 断开连接
                    self.disconnect_current()
                    print("测试完成")
                
            except Exception as e:
                print(f"测试失败: {str(e)}")
                if self.active_connector:
                    self.disconnect_current()

# 演示数据库连接器系统
def demonstrate_database_connectors():
    """演示数据库连接器系统"""
    print("=== 数据库连接器系统练习 ===")
    
    # 创建数据库管理器
    db_manager = DatabaseManager()
    
    # 创建不同类型的数据库连接器
    mysql_connector = MySQLConnector("localhost", 3306, "testdb", "root", "password")
    postgresql_connector = PostgreSQLConnector("localhost", 5432, "testdb", "postgres", "password")
    sqlite_connector = SQLiteConnector("test.db")
    
    # 添加连接器到管理器
    db_manager.add_connector("mysql", mysql_connector)
    db_manager.add_connector("postgresql", postgresql_connector)
    db_manager.add_connector("sqlite", sqlite_connector)
    
    print("1. 可用的数据库连接器:")
    for name in db_manager.list_connectors():
        connector = db_manager.connectors[name]
        print(f"   {name}: {connector.get_connection_info()}")
    
    # 测试所有连接器
    db_manager.test_all_connectors()
    
    print("\n=== 数据库连接器系统练习完成 ===\n")

demonstrate_database_connectors()
```

## 练习4：股票价格监控系统

实现一个股票价格监控系统，支持多种数据源和通知方式。

### 实现代码

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Callable
import random
import time
from datetime import datetime, timedelta
from enum import Enum

# 股票数据源抽象基类
class StockDataSource(ABC):
    """股票数据源抽象基类"""
    
    @abstractmethod
    def get_stock_price(self, symbol: str) -> float:
        """获取股票价格"""
        pass
    
    @abstractmethod
    def get_stock_info(self, symbol: str) -> Dict[str, Any]:
        """获取股票信息"""
        pass
    
    @property
    @abstractmethod
    def source_name(self) -> str:
        """数据源名称"""
        pass

# 具体数据源实现
class YahooFinanceSource(StockDataSource):
    """Yahoo Finance数据源"""
    
    def __init__(self):
        self.base_prices = {
            "AAPL": 150.0,
            "GOOGL": 2800.0,
            "MSFT": 300.0,
            "TSLA": 800.0,
            "AMZN": 3200.0
        }
    
    @property
    def source_name(self) -> str:
        return "Yahoo Finance"
    
    def get_stock_price(self, symbol: str) -> float:
        """获取股票价格"""
        if symbol not in self.base_prices:
            raise ValueError(f"不支持的股票代码: {symbol}")
        
        base_price = self.base_prices[symbol]
        # 模拟价格波动 ±5%
        fluctuation = random.uniform(-0.05, 0.05)
        return round(base_price * (1 + fluctuation), 2)
    
    def get_stock_info(self, symbol: str) -> Dict[str, Any]:
        """获取股票信息"""
        price = self.get_stock_price(symbol)
        return {
            "symbol": symbol,
            "price": price,
            "source": self.source_name,
            "timestamp": datetime.now(),
            "volume": random.randint(1000000, 10000000),
            "market_cap": price * random.randint(1000000000, 5000000000)
        }

class BloombergSource(StockDataSource):
    """Bloomberg数据源"""
    
    def __init__(self):
        self.base_prices = {
            "AAPL": 151.0,
            "GOOGL": 2805.0,
            "MSFT": 301.0,
            "TSLA": 805.0,
            "AMZN": 3205.0
        }
    
    @property
    def source_name(self) -> str:
        return "Bloomberg"
    
    def get_stock_price(self, symbol: str) -> float:
        """获取股票价格"""
        if symbol not in self.base_prices:
            raise ValueError(f"不支持的股票代码: {symbol}")
        
        base_price = self.base_prices[symbol]
        # 模拟价格波动 ±3%
        fluctuation = random.uniform(-0.03, 0.03)
        return round(base_price * (1 + fluctuation), 2)
    
    def get_stock_info(self, symbol: str) -> Dict[str, Any]:
        """获取股票信息"""
        price = self.get_stock_price(symbol)
        return {
            "symbol": symbol,
            "price": price,
            "source": self.source_name,
            "timestamp": datetime.now(),
            "volume": random.randint(800000, 8000000),
            "bid": price - 0.01,
            "ask": price + 0.01
        }

class AlphaVantageSource(StockDataSource):
    """Alpha Vantage数据源"""
    
    def __init__(self):
        self.base_prices = {
            "AAPL": 149.5,
            "GOOGL": 2795.0,
            "MSFT": 299.5,
            "TSLA": 795.0,
            "AMZN": 3195.0
        }
    
    @property
    def source_name(self) -> str:
        return "Alpha Vantage"
    
    def get_stock_price(self, symbol: str) -> float:
        """获取股票价格"""
        if symbol not in self.base_prices:
            raise ValueError(f"不支持的股票代码: {symbol}")
        
        base_price = self.base_prices[symbol]
        # 模拟价格波动 ±4%
        fluctuation = random.uniform(-0.04, 0.04)
        return round(base_price * (1 + fluctuation), 2)
    
    def get_stock_info(self, symbol: str) -> Dict[str, Any]:
        """获取股票信息"""
        price = self.get_stock_price(symbol)
        return {
            "symbol": symbol,
            "price": price,
            "source": self.source_name,
            "timestamp": datetime.now(),
            "volume": random.randint(500000, 5000000),
            "change": round(random.uniform(-10, 10), 2),
            "change_percent": round(random.uniform(-5, 5), 2)
        }

# 通知方式抽象基类
class NotificationMethod(ABC):
    """通知方式抽象基类"""
    
    @abstractmethod
    def send_notification(self, message: str, data: Dict[str, Any] = None):
        """发送通知"""
        pass
    
    @property
    @abstractmethod
    def method_name(self) -> str:
        """通知方式名称"""
        pass

# 具体通知方式实现
class EmailNotification(NotificationMethod):
    """邮件通知"""
    
    def __init__(self, email_address: str):
        self.email_address = email_address
    
    @property
    def method_name(self) -> str:
        return "邮件通知"
    
    def send_notification(self, message: str, data: Dict[str, Any] = None):
        """发送邮件通知"""
        print(f"📧 发送邮件到 {self.email_address}:")
        print(f"   主题: 股票价格提醒")
        print(f"   内容: {message}")
        if data:
            print(f"   详细信息: {data}")

class SMSNotification(NotificationMethod):
    """短信通知"""
    
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
    
    @property
    def method_name(self) -> str:
        return "短信通知"
    
    def send_notification(self, message: str, data: Dict[str, Any] = None):
        """发送短信通知"""
        print(f"📱 发送短信到 {self.phone_number}:")
        print(f"   {message}")

class PushNotification(NotificationMethod):
    """推送通知"""
    
    def __init__(self, device_id: str):
        self.device_id = device_id
    
    @property
    def method_name(self) -> str:
        return "推送通知"
    
    def send_notification(self, message: str, data: Dict[str, Any] = None):
        """发送推送通知"""
        print(f"🔔 推送通知到设备 {self.device_id}:")
        print(f"   {message}")
        if data:
            print(f"   点击查看详情: {data.get('symbol', 'N/A')}")

# 价格监控器
class StockPriceMonitor:
    """股票价格监控器"""
    
    def __init__(self):
        self.data_sources: List[StockDataSource] = []
        self.notification_methods: List[NotificationMethod] = []
        self.price_alerts: Dict[str, Dict[str, float]] = {}  # {symbol: {"high": price, "low": price}}
        self.monitoring = False
    
    def add_data_source(self, source: StockDataSource):
        """添加数据源"""
        self.data_sources.append(source)
    
    def add_notification_method(self, method: NotificationMethod):
        """添加通知方式"""
        self.notification_methods.append(method)
    
    def set_price_alert(self, symbol: str, high_threshold: float = None, low_threshold: float = None):
        """设置价格提醒"""
        if symbol not in self.price_alerts:
            self.price_alerts[symbol] = {}
        
        if high_threshold is not None:
            self.price_alerts[symbol]["high"] = high_threshold
        if low_threshold is not None:
            self.price_alerts[symbol]["low"] = low_threshold
    
    def get_aggregated_price(self, symbol: str) -> Dict[str, Any]:
        """获取聚合价格信息"""
        prices = []
        source_data = []
        
        for source in self.data_sources:
            try:
                info = source.get_stock_info(symbol)
                prices.append(info["price"])
                source_data.append(info)
            except Exception as e:
                print(f"从 {source.source_name} 获取 {symbol} 数据失败: {str(e)}")
        
        if not prices:
            raise Exception(f"无法获取 {symbol} 的价格数据")
        
        avg_price = sum(prices) / len(prices)
        
        return {
            "symbol": symbol,
            "average_price": round(avg_price, 2),
            "price_range": {"min": min(prices), "max": max(prices)},
            "source_count": len(prices),
            "source_data": source_data,
            "timestamp": datetime.now()
        }
    
    def check_price_alerts(self, symbol: str, current_price: float):
        """检查价格提醒"""
        if symbol not in self.price_alerts:
            return
        
        alerts = self.price_alerts[symbol]
        
        # 检查高价提醒
        if "high" in alerts and current_price >= alerts["high"]:
            message = f"{symbol} 价格达到高位提醒: ${current_price} (>= ${alerts['high']})"
            self.send_notifications(message, {"symbol": symbol, "price": current_price, "type": "high_alert"})
        
        # 检查低价提醒
        if "low" in alerts and current_price <= alerts["low"]:
            message = f"{symbol} 价格达到低位提醒: ${current_price} (<= ${alerts['low']})"
            self.send_notifications(message, {"symbol": symbol, "price": current_price, "type": "low_alert"})
    
    def send_notifications(self, message: str, data: Dict[str, Any] = None):
        """发送通知"""
        for method in self.notification_methods:
            try:
                method.send_notification(message, data)
            except Exception as e:
                print(f"通过 {method.method_name} 发送通知失败: {str(e)}")
    
    def monitor_stocks(self, symbols: List[str], duration: int = 10, interval: int = 2):
        """监控股票价格"""
        print(f"开始监控股票: {', '.join(symbols)}")
        print(f"监控时长: {duration}秒, 检查间隔: {interval}秒")
        print("-" * 60)
        
        self.monitoring = True
        start_time = time.time()
        
        while self.monitoring and (time.time() - start_time) < duration:
            for symbol in symbols:
                try:
                    # 获取聚合价格信息
                    price_info = self.get_aggregated_price(symbol)
                    current_price = price_info["average_price"]
                    
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] {symbol}: ${current_price} (来源: {price_info['source_count']}个)")
                    
                    # 检查价格提醒
                    self.check_price_alerts(symbol, current_price)
                    
                except Exception as e:
                    print(f"监控 {symbol} 时出错: {str(e)}")
            
            print()
            time.sleep(interval)
        
        print("股票监控结束")
        self.monitoring = False
    
    def stop_monitoring(self):
        """停止监控"""
        self.monitoring = False
    
    def get_monitoring_summary(self) -> Dict[str, Any]:
        """获取监控摘要"""
        return {
            "data_sources": [source.source_name for source in self.data_sources],
            "notification_methods": [method.method_name for method in self.notification_methods],
            "price_alerts": self.price_alerts,
            "monitoring_status": self.monitoring
        }

# 演示股票价格监控系统
def demonstrate_stock_monitor():
    """演示股票价格监控系统"""
    print("=== 股票价格监控系统练习 ===")
    
    # 创建监控器
    monitor = StockPriceMonitor()
    
    # 添加数据源
    monitor.add_data_source(YahooFinanceSource())
    monitor.add_data_source(BloombergSource())
    monitor.add_data_source(AlphaVantageSource())
    
    # 添加通知方式
    monitor.add_notification_method(EmailNotification("trader@example.com"))
    monitor.add_notification_method(SMSNotification("+1234567890"))
    monitor.add_notification_method(PushNotification("device_123"))
    
    # 设置价格提醒
    monitor.set_price_alert("AAPL", high_threshold=155.0, low_threshold=145.0)
    monitor.set_price_alert("TSLA", high_threshold=820.0, low_threshold=780.0)
    
    print("1. 监控系统配置:")
    summary = monitor.get_monitoring_summary()
    print(f"   数据源: {', '.join(summary['data_sources'])}")
    print(f"   通知方式: {', '.join(summary['notification_methods'])}")
    print(f"   价格提醒: {summary['price_alerts']}")
    
    print("\n2. 获取实时价格信息:")
    symbols = ["AAPL", "TSLA", "GOOGL"]
    for symbol in symbols:
        try:
            price_info = monitor.get_aggregated_price(symbol)
            print(f"   {symbol}: 平均价格 ${price_info['average_price']}, 价格范围 ${price_info['price_range']['min']}-${price_info['price_range']['max']}")
        except Exception as e:
            print(f"   {symbol}: 获取失败 - {str(e)}")
    
    print("\n3. 开始价格监控 (模拟5秒):")
    monitor.monitor_stocks(["AAPL", "TSLA"], duration=5, interval=1)
    
    print("\n=== 股票价格监控系统练习完成 ===\n")

demonstrate_stock_monitor()
```

## 练习5：游戏角色系统

设计一个游戏角色系统，支持多种角色类型和技能系统。

### 实现代码

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from enum import Enum
import random
import math

# 角色类型枚举
class CharacterType(Enum):
    WARRIOR = "战士"
    MAGE = "法师"
    ARCHER = "弓箭手"
    ROGUE = "盗贼"
    HEALER = "治疗师"

# 技能类型枚举
class SkillType(Enum):
    ATTACK = "攻击"
    DEFENSE = "防御"
    HEAL = "治疗"
    BUFF = "增益"
    DEBUFF = "减益"

# 游戏角色抽象基类
class GameCharacter(ABC):
    """游戏角色抽象基类"""
    
    def __init__(self, name: str, level: int = 1):
        self.name = name
        self.level = level
        self.max_hp = self.calculate_max_hp()
        self.current_hp = self.max_hp
        self.max_mp = self.calculate_max_mp()
        self.current_mp = self.max_mp
        self.experience = 0
        self.skills: List['Skill'] = []
        self.status_effects: Dict[str, int] = {}  # {effect_name: remaining_turns}
    
    @property
    @abstractmethod
    def character_type(self) -> CharacterType:
        """角色类型"""
        pass
    
    @property
    @abstractmethod
    def base_attack(self) -> int:
        """基础攻击力"""
        pass
    
    @property
    @abstractmethod
    def base_defense(self) -> int:
        """基础防御力"""
        pass
    
    @property
    @abstractmethod
    def base_speed(self) -> int:
        """基础速度"""
        pass
    
    @abstractmethod
    def calculate_max_hp(self) -> int:
        """计算最大生命值"""
        pass
    
    @abstractmethod
    def calculate_max_mp(self) -> int:
        """计算最大魔法值"""
        pass
    
    @abstractmethod
    def get_special_ability(self) -> str:
        """获取特殊能力描述"""
        pass
    
    def attack(self, target: 'GameCharacter') -> Dict[str, Any]:
        """攻击目标"""
        damage = self.calculate_damage(target)
        actual_damage = target.take_damage(damage)
        
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": actual_damage,
            "target_hp": target.current_hp
        }
    
    def calculate_damage(self, target: 'GameCharacter') -> int:
        """计算伤害"""
        base_damage = self.base_attack + (self.level * 2)
        defense_reduction = target.base_defense + (target.level * 1.5)
        
        # 应用状态效果
        if "攻击增强" in self.status_effects:
            base_damage = int(base_damage * 1.3)
        if "防御增强" in target.status_effects:
            defense_reduction = int(defense_reduction * 1.3)
        
        damage = max(1, int(base_damage - defense_reduction * 0.5))
        
        # 添加随机因素
        damage = int(damage * random.uniform(0.8, 1.2))
        
        return max(1, damage)
    
    def take_damage(self, damage: int) -> int:
        """承受伤害"""
        actual_damage = min(damage, self.current_hp)
        self.current_hp -= actual_damage
        return actual_damage
    
    def heal(self, amount: int) -> int:
        """治疗"""
        actual_heal = min(amount, self.max_hp - self.current_hp)
        self.current_hp += actual_heal
        return actual_heal
    
    def use_mp(self, amount: int) -> bool:
        """使用魔法值"""
        if self.current_mp >= amount:
            self.current_mp -= amount
            return True
        return False
    
    def restore_mp(self, amount: int) -> int:
        """恢复魔法值"""
        actual_restore = min(amount, self.max_mp - self.current_mp)
        self.current_mp += actual_restore
        return actual_restore
    
    def add_status_effect(self, effect_name: str, duration: int):
        """添加状态效果"""
        self.status_effects[effect_name] = duration
    
    def update_status_effects(self):
        """更新状态效果"""
        expired_effects = []
        for effect, duration in self.status_effects.items():
            self.status_effects[effect] = duration - 1
            if self.status_effects[effect] <= 0:
                expired_effects.append(effect)
        
        for effect in expired_effects:
            del self.status_effects[effect]
    
    def is_alive(self) -> bool:
        """检查是否存活"""
        return self.current_hp > 0
    
    def get_status(self) -> Dict[str, Any]:
        """获取角色状态"""
        return {
            "name": self.name,
            "type": self.character_type.value,
            "level": self.level,
            "hp": f"{self.current_hp}/{self.max_hp}",
            "mp": f"{self.current_mp}/{self.max_mp}",
            "attack": self.base_attack,
            "defense": self.base_defense,
            "speed": self.base_speed,
            "status_effects": list(self.status_effects.keys()),
            "alive": self.is_alive()
        }
    
    def __str__(self) -> str:
        status = "存活" if self.is_alive() else "死亡"
        return f"{self.name}({self.character_type.value}, Lv.{self.level}) - HP:{self.current_hp}/{self.max_hp}, MP:{self.current_mp}/{self.max_mp} [{status}]"

# 具体角色类实现
class Warrior(GameCharacter):
    """战士"""
    
    @property
    def character_type(self) -> CharacterType:
        return CharacterType.WARRIOR
    
    @property
    def base_attack(self) -> int:
        return 15 + self.level * 3
    
    @property
    def base_defense(self) -> int:
        return 12 + self.level * 2
    
    @property
    def base_speed(self) -> int:
        return 8 + self.level
    
    def calculate_max_hp(self) -> int:
        return 120 + self.level * 15
    
    def calculate_max_mp(self) -> int:
        return 30 + self.level * 3
    
    def get_special_ability(self) -> str:
        return "重击：造成150%伤害，消耗10MP"
    
    def heavy_strike(self, target: 'GameCharacter') -> Dict[str, Any]:
        """重击技能"""
        if not self.use_mp(10):
            return {"error": "魔法值不足"}
        
        damage = int(self.calculate_damage(target) * 1.5)
        actual_damage = target.take_damage(damage)
        
        return {
            "skill": "重击",
            "attacker": self.name,
            "target": target.name,
            "damage": actual_damage,
            "target_hp": target.current_hp
        }

class Mage(GameCharacter):
    """法师"""
    
    @property
    def character_type(self) -> CharacterType:
        return CharacterType.MAGE
    
    @property
    def base_attack(self) -> int:
        return 8 + self.level * 2
    
    @property
    def base_defense(self) -> int:
        return 6 + self.level
    
    @property
    def base_speed(self) -> int:
        return 10 + self.level
    
    def calculate_max_hp(self) -> int:
        return 80 + self.level * 8
    
    def calculate_max_mp(self) -> int:
        return 100 + self.level * 12
    
    def get_special_ability(self) -> str:
        return "火球术：造成魔法伤害，消耗15MP"
    
    def fireball(self, target: 'GameCharacter') -> Dict[str, Any]:
        """火球术"""
        if not self.use_mp(15):
            return {"error": "魔法值不足"}
        
        # 魔法伤害基于智力而非攻击力
        magic_damage = (self.level * 5 + 20) * random.uniform(0.9, 1.3)
        actual_damage = target.take_damage(int(magic_damage))
        
        return {
            "skill": "火球术",
            "attacker": self.name,
            "target": target.name,
            "damage": actual_damage,
            "target_hp": target.current_hp
        }

class Archer(GameCharacter):
    """弓箭手"""
    
    @property
    def character_type(self) -> CharacterType:
        return CharacterType.ARCHER
    
    @property
    def base_attack(self) -> int:
        return 12 + self.level * 2
    
    @property
    def base_defense(self) -> int:
        return 8 + self.level
    
    @property
    def base_speed(self) -> int:
        return 15 + self.level * 2
    
    def calculate_max_hp(self) -> int:
        return 90 + self.level * 10
    
    def calculate_max_mp(self) -> int:
        return 50 + self.level * 5
    
    def get_special_ability(self) -> str:
        return "精准射击：必定命中，造成120%伤害，消耗8MP"
    
    def precise_shot(self, target: 'GameCharacter') -> Dict[str, Any]:
        """精准射击"""
        if not self.use_mp(8):
            return {"error": "魔法值不足"}
        
        damage = int(self.calculate_damage(target) * 1.2)
        actual_damage = target.take_damage(damage)
        
        return {
            "skill": "精准射击",
            "attacker": self.name,
            "target": target.name,
            "damage": actual_damage,
            "target_hp": target.current_hp,
            "critical": True
        }

class Rogue(GameCharacter):
    """盗贼"""
    
    @property
    def character_type(self) -> CharacterType:
        return CharacterType.ROGUE
    
    @property
    def base_attack(self) -> int:
        return 10 + self.level * 2
    
    @property
    def base_defense(self) -> int:
        return 7 + self.level
    
    @property
    def base_speed(self) -> int:
        return 18 + self.level * 2
    
    def calculate_max_hp(self) -> int:
        return 85 + self.level * 9
    
    def calculate_max_mp(self) -> int:
        return 40 + self.level * 4
    
    def get_special_ability(self) -> str:
        return "背刺：从背后攻击造成200%伤害，消耗12MP"
    
    def backstab(self, target: 'GameCharacter') -> Dict[str, Any]:
        """背刺"""
        if not self.use_mp(12):
            return {"error": "魔法值不足"}
        
        damage = int(self.calculate_damage(target) * 2.0)
        actual_damage = target.take_damage(damage)
        
        return {
            "skill": "背刺",
            "attacker": self.name,
            "target": target.name,
            "damage": actual_damage,
            "target_hp": target.current_hp,
            "critical": True
        }

class Healer(GameCharacter):
    """治疗师"""
    
    @property
    def character_type(self) -> CharacterType:
        return CharacterType.HEALER
    
    @property
    def base_attack(self) -> int:
        return 6 + self.level
    
    @property
    def base_defense(self) -> int:
        return 9 + self.level
    
    @property
    def base_speed(self) -> int:
        return 12 + self.level
    
    def calculate_max_hp(self) -> int:
        return 95 + self.level * 11
    
    def calculate_max_mp(self) -> int:
        return 120 + self.level * 15
    
    def get_special_ability(self) -> str:
        return "治疗术：恢复目标生命值，消耗20MP"
    
    def heal_spell(self, target: 'GameCharacter') -> Dict[str, Any]:
        """治疗术"""
        if not self.use_mp(20):
            return {"error": "魔法值不足"}
        
        heal_amount = (self.level * 8 + 30) * random.uniform(0.8, 1.2)
        actual_heal = target.heal(int(heal_amount))
        
        return {
            "skill": "治疗术",
            "caster": self.name,
            "target": target.name,
            "heal": actual_heal,
            "target_hp": target.current_hp
        }
    
    def blessing(self, target: 'GameCharacter') -> Dict[str, Any]:
        """祝福术"""
        if not self.use_mp(15):
            return {"error": "魔法值不足"}
        
        target.add_status_effect("攻击增强", 3)
        target.add_status_effect("防御增强", 3)
        
        return {
            "skill": "祝福术",
            "caster": self.name,
            "target": target.name,
            "effect": "攻击和防御增强3回合"
        }

# 战斗系统
class BattleSystem:
    """战斗系统"""
    
    def __init__(self):
        self.participants: List[GameCharacter] = []
        self.turn_order: List[GameCharacter] = []
        self.current_turn = 0
        self.battle_log: List[str] = []
    
    def add_participant(self, character: GameCharacter):
        """添加战斗参与者"""
        self.participants.append(character)
    
    def start_battle(self):
        """开始战斗"""
        # 按速度排序决定行动顺序
        self.turn_order = sorted(self.participants, key=lambda x: x.base_speed, reverse=True)
        self.current_turn = 0
        self.battle_log = []
        
        print("=== 战斗开始 ===")
        print("行动顺序:")
        for i, char in enumerate(self.turn_order, 1):
            print(f"  {i}. {char.name}({char.character_type.value}) - 速度: {char.base_speed}")
        print()
    
    def execute_turn(self) -> bool:
        """执行一个回合"""
        if self.is_battle_over():
            return False
        
        current_char = self.turn_order[self.current_turn % len(self.turn_order)]
        
        if not current_char.is_alive():
            self.current_turn += 1
            return True
        
        print(f"--- {current_char.name} 的回合 ---")
        
        # 更新状态效果
        current_char.update_status_effects()
        
        # AI行动逻辑（简单实现）
        self.ai_action(current_char)
        
        self.current_turn += 1
        return True
    
    def ai_action(self, character: GameCharacter):
        """AI行动逻辑"""
        # 获取存活的敌人
        enemies = [char for char in self.participants if char != character and char.is_alive()]
        
        if not enemies:
            return
        
        # 简单AI：随机选择目标和行动
        target = random.choice(enemies)
        
        # 根据角色类型选择行动
        if isinstance(character, Healer):
            # 治疗师优先治疗血量低的队友
            allies = [char for char in self.participants if char != character and char.is_alive()]
            low_hp_allies = [ally for ally in allies if ally.current_hp < ally.max_hp * 0.5]
            
            if low_hp_allies and character.current_mp >= 20:
                heal_target = min(low_hp_allies, key=lambda x: x.current_hp)
                result = character.heal_spell(heal_target)
                print(f"  {character.name} 对 {heal_target.name} 使用治疗术，恢复 {result.get('heal', 0)} HP")
            elif character.current_mp >= 15 and random.random() < 0.3:
                buff_target = random.choice(allies) if allies else character
                result = character.blessing(buff_target)
                print(f"  {character.name} 对 {buff_target.name} 使用祝福术")
            else:
                result = character.attack(target)
                print(f"  {character.name} 攻击 {target.name}，造成 {result['damage']} 伤害")
        
        elif isinstance(character, Warrior) and character.current_mp >= 10 and random.random() < 0.4:
            result = character.heavy_strike(target)
            if "error" not in result:
                print(f"  {character.name} 对 {target.name} 使用重击，造成 {result['damage']} 伤害")
            else:
                result = character.attack(target)
                print(f"  {character.name} 攻击 {target.name}，造成 {result['damage']} 伤害")
        
        elif isinstance(character, Mage) and character.current_mp >= 15 and random.random() < 0.5:
            result = character.fireball(target)
            if "error" not in result:
                print(f"  {character.name} 对 {target.name} 使用火球术，造成 {result['damage']} 魔法伤害")
            else:
                result = character.attack(target)
                print(f"  {character.name} 攻击 {target.name}，造成 {result['damage']} 伤害")
        
        elif isinstance(character, Archer) and character.current_mp >= 8 and random.random() < 0.4:
            result = character.precise_shot(target)
            if "error" not in result:
                print(f"  {character.name} 对 {target.name} 使用精准射击，造成 {result['damage']} 伤害")
            else:
                result = character.attack(target)
                print(f"  {character.name} 攻击 {target.name}，造成 {result['damage']} 伤害")
        
        elif isinstance(character, Rogue) and character.current_mp >= 12 and random.random() < 0.3:
            result = character.backstab(target)
            if "error" not in result:
                print(f"  {character.name} 对 {target.name} 使用背刺，造成 {result['damage']} 暴击伤害")
            else:
                result = character.attack(target)
                print(f"  {character.name} 攻击 {target.name}，造成 {result['damage']} 伤害")
        
        else:
            result = character.attack(target)
            print(f"  {character.name} 攻击 {target.name}，造成 {result['damage']} 伤害")
        
        # 显示目标状态
        if target.is_alive():
            print(f"    {target.name} 剩余HP: {target.current_hp}/{target.max_hp}")
        else:
            print(f"    {target.name} 被击败！")
    
    def is_battle_over(self) -> bool:
        """检查战斗是否结束"""
        alive_chars = [char for char in self.participants if char.is_alive()]
        return len(alive_chars) <= 1
    
    def get_winner(self) -> Optional[GameCharacter]:
        """获取胜利者"""
        alive_chars = [char for char in self.participants if char.is_alive()]
        return alive_chars[0] if len(alive_chars) == 1 else None
    
    def run_battle(self, max_turns: int = 50):
        """运行完整战斗"""
        self.start_battle()
        
        turn_count = 0
        while turn_count < max_turns and self.execute_turn():
            turn_count += 1
            
            # 每5回合显示一次状态
            if turn_count % 5 == 0:
                print("\n当前状态:")
                for char in self.participants:
                    if char.is_alive():
                        print(f"  {char}")
                print()
        
        print("=== 战斗结束 ===")
        winner = self.get_winner()
        if winner:
            print(f"胜利者: {winner.name}({winner.character_type.value})")
        else:
            print("战斗平局或超时")
        
        print("\n最终状态:")
        for char in self.participants:
            print(f"  {char}")

# 演示游戏角色系统
def demonstrate_game_characters():
    """演示游戏角色系统"""
    print("=== 游戏角色系统练习 ===")
    
    # 创建不同类型的角色
    characters = [
        Warrior("亚瑟王", level=5),
        Mage("梅林", level=5),
        Archer("罗宾汉", level=5),
        Rogue("影刃", level=5),
        Healer("圣女贞德", level=5)
    ]
    
    print("1. 角色信息:")
    for char in characters:
        print(f"   {char}")
        print(f"      特殊能力: {char.get_special_ability()}")
    
    print("\n2. 角色详细属性:")
    for char in characters:
        status = char.get_status()
        print(f"   {status['name']}({status['type']})")
        print(f"      等级: {status['level']}, 攻击: {status['attack']}, 防御: {status['defense']}, 速度: {status['speed']}")
    
    print("\n3. 战斗模拟:")
    # 创建战斗系统
    battle = BattleSystem()
    
    # 选择3个角色进行战斗
    battle_chars = [characters[0], characters[1], characters[4]]  # 战士 vs 法师 vs 治疗师
    for char in battle_chars:
        battle.add_participant(char)
    
    # 运行战斗
    battle.run_battle(max_turns=20)
    
    print("\n=== 游戏角色系统练习完成 ===\n")

demonstrate_game_characters()
```

## 练习总结

这些练习涵盖了多态的各个方面：

### 学习要点

1. **抽象基类设计**：每个练习都使用了抽象基类来定义接口
2. **多态实现**：不同的具体类实现相同的接口，表现出不同的行为
3. **鸭子类型**：某些练习中使用了鸭子类型的概念
4. **设计模式**：应用了策略模式、工厂模式等设计模式
5. **实际应用**：展示了多态在实际项目中的应用场景

### 扩展建议

1. **添加更多功能**：为每个系统添加更多特性和功能
2. **优化性能**：考虑性能优化和内存管理
3. **错误处理**：添加更完善的错误处理机制
4. **单元测试**：为每个类和方法编写单元测试
5. **文档完善**：添加更详细的文档和使用说明

### 学习建议

1. **逐个练习**：按顺序完成每个练习，理解其设计思路
2. **修改扩展**：尝试修改和扩展现有代码
3. **自主设计**：基于学到的概念设计自己的多态系统
4. **代码重构**：练习重构代码以提高可维护性
5. **性能分析**：分析不同实现方式的性能差异

通过这些练习，你将深入理解多态的概念和应用，掌握面向对象编程的核心技能。