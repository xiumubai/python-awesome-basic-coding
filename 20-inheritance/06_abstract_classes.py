#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抽象基类（Abstract Base Classes - ABC）

抽象基类是一种特殊的类，它不能被直接实例化，只能被继承。
抽象基类定义了子类必须实现的接口，确保了代码的一致性和可维护性。

学习要点：
1. 抽象基类的基本概念
2. 使用abc模块创建抽象基类
3. 抽象方法和抽象属性
4. 抽象基类的实际应用
5. 抽象基类vs接口
6. 内置抽象基类的使用
7. 自定义抽象基类的最佳实践
"""

from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod, abstractstaticmethod
from typing import Any, List, Dict
import math

# 1. 抽象基类的基本概念
print("=== 1. 抽象基类的基本概念 ===")

class Shape(ABC):
    """抽象基类：形状"""
    
    @abstractmethod
    def area(self) -> float:
        """计算面积的抽象方法"""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """计算周长的抽象方法"""
        pass
    
    def describe(self) -> str:
        """具体方法：描述形状"""
        return f"这是一个{self.__class__.__name__}，面积为{self.area():.2f}，周长为{self.perimeter():.2f}"

# 尝试实例化抽象基类（会失败）
print("尝试实例化抽象基类:")
try:
    shape = Shape()
except TypeError as e:
    print(f"错误: {e}")

# 实现抽象基类
class Rectangle(Shape):
    """矩形类 - 实现Shape抽象基类"""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """实现抽象方法：计算矩形面积"""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """实现抽象方法：计算矩形周长"""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """圆形类 - 实现Shape抽象基类"""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        """实现抽象方法：计算圆形面积"""
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """实现抽象方法：计算圆形周长"""
        return 2 * math.pi * self.radius

# 测试具体实现
print("\n创建具体形状实例:")
rectangle = Rectangle(5, 3)
circle = Circle(4)

print(rectangle.describe())
print(circle.describe())

# 尝试创建不完整的实现（会失败）
print("\n尝试创建不完整的实现:")
try:
    class IncompleteShape(Shape):
        def area(self):
            return 0
        # 缺少perimeter方法的实现
    
    incomplete = IncompleteShape()
except TypeError as e:
    print(f"错误: {e}")

print("\n=== 2. 抽象属性和类方法 ===")

# 2. 抽象属性和类方法
class Vehicle(ABC):
    """抽象基类：交通工具"""
    
    @property
    @abstractmethod
    def max_speed(self) -> float:
        """抽象属性：最大速度"""
        pass
    
    @property
    @abstractmethod
    def fuel_type(self) -> str:
        """抽象属性：燃料类型"""
        pass
    
    @abstractclassmethod
    def get_category(cls) -> str:
        """抽象类方法：获取类别"""
        pass
    
    @abstractstaticmethod
    def is_eco_friendly(fuel_type: str) -> bool:
        """抽象静态方法：判断是否环保"""
        pass
    
    @abstractmethod
    def start_engine(self) -> None:
        """抽象方法：启动引擎"""
        pass
    
    def get_info(self) -> str:
        """具体方法：获取信息"""
        return f"{self.__class__.__name__}: 最大速度{self.max_speed}km/h, 燃料类型: {self.fuel_type}"

class Car(Vehicle):
    """汽车类 - 实现Vehicle抽象基类"""
    
    def __init__(self, brand: str, model: str, max_speed: float):
        self.brand = brand
        self.model = model
        self._max_speed = max_speed
        self._fuel_type = "汽油"
    
    @property
    def max_speed(self) -> float:
        return self._max_speed
    
    @property
    def fuel_type(self) -> str:
        return self._fuel_type
    
    @classmethod
    def get_category(cls) -> str:
        return "陆地交通工具"
    
    @staticmethod
    def is_eco_friendly(fuel_type: str) -> bool:
        return fuel_type.lower() in ["电力", "氢气", "太阳能"]
    
    def start_engine(self) -> None:
        print(f"{self.brand} {self.model} 引擎启动!")

class ElectricCar(Vehicle):
    """电动汽车类"""
    
    def __init__(self, brand: str, model: str, max_speed: float, battery_capacity: float):
        self.brand = brand
        self.model = model
        self._max_speed = max_speed
        self.battery_capacity = battery_capacity
        self._fuel_type = "电力"
    
    @property
    def max_speed(self) -> float:
        return self._max_speed
    
    @property
    def fuel_type(self) -> str:
        return self._fuel_type
    
    @classmethod
    def get_category(cls) -> str:
        return "环保陆地交通工具"
    
    @staticmethod
    def is_eco_friendly(fuel_type: str) -> bool:
        return fuel_type.lower() in ["电力", "氢气", "太阳能"]
    
    def start_engine(self) -> None:
        print(f"{self.brand} {self.model} 电机启动! 电池容量: {self.battery_capacity}kWh")

# 测试抽象属性和方法
print("测试抽象属性和方法:")
car = Car("丰田", "卡罗拉", 180)
electric_car = ElectricCar("特斯拉", "Model 3", 250, 75)

for vehicle in [car, electric_car]:
    print(vehicle.get_info())
    vehicle.start_engine()
    print(f"类别: {vehicle.get_category()}")
    print(f"是否环保: {vehicle.is_eco_friendly(vehicle.fuel_type)}")
    print()

print("=== 3. 实际应用：数据处理器抽象基类 ===")

# 3. 实际应用场景
class DataProcessor(ABC):
    """数据处理器抽象基类"""
    
    @abstractmethod
    def load_data(self, source: str) -> Any:
        """加载数据的抽象方法"""
        pass
    
    @abstractmethod
    def process_data(self, data: Any) -> Any:
        """处理数据的抽象方法"""
        pass
    
    @abstractmethod
    def save_data(self, data: Any, destination: str) -> None:
        """保存数据的抽象方法"""
        pass
    
    @property
    @abstractmethod
    def supported_formats(self) -> List[str]:
        """支持的格式列表"""
        pass
    
    def execute_pipeline(self, source: str, destination: str) -> None:
        """执行完整的数据处理流水线"""
        print(f"开始处理数据流水线: {source} -> {destination}")
        
        # 加载数据
        print("1. 加载数据...")
        data = self.load_data(source)
        
        # 处理数据
        print("2. 处理数据...")
        processed_data = self.process_data(data)
        
        # 保存数据
        print("3. 保存数据...")
        self.save_data(processed_data, destination)
        
        print("数据处理流水线完成!")
    
    def validate_format(self, format_type: str) -> bool:
        """验证格式是否支持"""
        return format_type.lower() in [fmt.lower() for fmt in self.supported_formats]

class CSVProcessor(DataProcessor):
    """CSV数据处理器"""
    
    def load_data(self, source: str) -> List[Dict[str, str]]:
        """加载CSV数据（模拟）"""
        print(f"从 {source} 加载CSV数据")
        # 模拟CSV数据
        return [
            {"name": "张三", "age": "25", "city": "北京"},
            {"name": "李四", "age": "30", "city": "上海"},
            {"name": "王五", "age": "28", "city": "广州"}
        ]
    
    def process_data(self, data: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        """处理CSV数据"""
        print("处理CSV数据: 转换年龄为整数，添加年龄组")
        processed = []
        for row in data:
            processed_row = row.copy()
            processed_row["age"] = int(row["age"])
            processed_row["age_group"] = "青年" if int(row["age"]) < 30 else "中年"
            processed.append(processed_row)
        return processed
    
    def save_data(self, data: List[Dict[str, Any]], destination: str) -> None:
        """保存CSV数据（模拟）"""
        print(f"保存处理后的数据到 {destination}")
        for row in data:
            print(f"  {row}")
    
    @property
    def supported_formats(self) -> List[str]:
        return ["CSV", "TSV"]

class JSONProcessor(DataProcessor):
    """JSON数据处理器"""
    
    def load_data(self, source: str) -> Dict[str, Any]:
        """加载JSON数据（模拟）"""
        print(f"从 {source} 加载JSON数据")
        # 模拟JSON数据
        return {
            "users": [
                {"id": 1, "name": "张三", "score": 85},
                {"id": 2, "name": "李四", "score": 92},
                {"id": 3, "name": "王五", "score": 78}
            ]
        }
    
    def process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """处理JSON数据"""
        print("处理JSON数据: 计算平均分，添加等级")
        users = data["users"]
        total_score = sum(user["score"] for user in users)
        avg_score = total_score / len(users)
        
        for user in users:
            if user["score"] >= 90:
                user["grade"] = "A"
            elif user["score"] >= 80:
                user["grade"] = "B"
            else:
                user["grade"] = "C"
        
        return {
            "users": users,
            "statistics": {
                "total_users": len(users),
                "average_score": avg_score
            }
        }
    
    def save_data(self, data: Dict[str, Any], destination: str) -> None:
        """保存JSON数据（模拟）"""
        print(f"保存处理后的数据到 {destination}")
        print(f"  统计信息: {data['statistics']}")
        for user in data["users"]:
            print(f"  用户: {user}")
    
    @property
    def supported_formats(self) -> List[str]:
        return ["JSON", "JSONL"]

# 测试数据处理器
print("测试数据处理器:")
processors = [
    CSVProcessor(),
    JSONProcessor()
]

for processor in processors:
    print(f"\n{processor.__class__.__name__} 支持的格式: {processor.supported_formats}")
    processor.execute_pipeline("input.csv", "output.csv")
    print()

print("=== 4. 内置抽象基类的使用 ===")

# 4. 使用内置抽象基类
from collections.abc import Iterable, Iterator, Mapping, MutableMapping

class CustomIterable(Iterable):
    """自定义可迭代对象"""
    
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        return iter(self.data)

class CustomMapping(Mapping):
    """自定义映射对象"""
    
    def __init__(self, data):
        self._data = data
    
    def __getitem__(self, key):
        return self._data[key]
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)

class CustomMutableMapping(MutableMapping):
    """自定义可变映射对象"""
    
    def __init__(self):
        self._data = {}
    
    def __getitem__(self, key):
        return self._data[key]
    
    def __setitem__(self, key, value):
        self._data[key] = value
    
    def __delitem__(self, key):
        del self._data[key]
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)

# 测试内置抽象基类
print("测试内置抽象基类:")

# 测试可迭代对象
custom_iter = CustomIterable([1, 2, 3, 4, 5])
print(f"CustomIterable: {list(custom_iter)}")
print(f"是否为Iterable: {isinstance(custom_iter, Iterable)}")

# 测试映射对象
custom_map = CustomMapping({"a": 1, "b": 2, "c": 3})
print(f"CustomMapping: {dict(custom_map)}")
print(f"是否为Mapping: {isinstance(custom_map, Mapping)}")
print(f"获取键'a': {custom_map['a']}")

# 测试可变映射对象
custom_mut_map = CustomMutableMapping()
custom_mut_map["x"] = 10
custom_mut_map["y"] = 20
print(f"CustomMutableMapping: {dict(custom_mut_map)}")
print(f"是否为MutableMapping: {isinstance(custom_mut_map, MutableMapping)}")

print("\n=== 5. 抽象基类的高级应用 ===")

# 5. 抽象基类的高级应用
class Plugin(ABC):
    """插件系统的抽象基类"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """插件名称"""
        pass
    
    @property
    @abstractmethod
    def version(self) -> str:
        """插件版本"""
        pass
    
    @abstractmethod
    def initialize(self) -> None:
        """初始化插件"""
        pass
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """执行插件功能"""
        pass
    
    @abstractmethod
    def cleanup(self) -> None:
        """清理插件资源"""
        pass
    
    def get_info(self) -> Dict[str, str]:
        """获取插件信息"""
        return {
            "name": self.name,
            "version": self.version,
            "class": self.__class__.__name__
        }

class LoggingPlugin(Plugin):
    """日志插件"""
    
    @property
    def name(self) -> str:
        return "日志记录器"
    
    @property
    def version(self) -> str:
        return "1.0.0"
    
    def initialize(self) -> None:
        print(f"初始化 {self.name} v{self.version}")
        self.log_entries = []
    
    def execute(self, message: str, level: str = "INFO") -> None:
        log_entry = f"[{level}] {message}"
        self.log_entries.append(log_entry)
        print(f"记录日志: {log_entry}")
    
    def cleanup(self) -> None:
        print(f"清理 {self.name}，共记录 {len(self.log_entries)} 条日志")
        self.log_entries.clear()

class CachePlugin(Plugin):
    """缓存插件"""
    
    @property
    def name(self) -> str:
        return "缓存管理器"
    
    @property
    def version(self) -> str:
        return "2.1.0"
    
    def initialize(self) -> None:
        print(f"初始化 {self.name} v{self.version}")
        self.cache = {}
    
    def execute(self, action: str, key: str = None, value: Any = None) -> Any:
        if action == "set" and key and value is not None:
            self.cache[key] = value
            print(f"缓存设置: {key} = {value}")
        elif action == "get" and key:
            result = self.cache.get(key)
            print(f"缓存获取: {key} = {result}")
            return result
        elif action == "clear":
            self.cache.clear()
            print("缓存已清空")
    
    def cleanup(self) -> None:
        print(f"清理 {self.name}，缓存项数: {len(self.cache)}")
        self.cache.clear()

class PluginManager:
    """插件管理器"""
    
    def __init__(self):
        self.plugins: List[Plugin] = []
    
    def register_plugin(self, plugin: Plugin) -> None:
        """注册插件"""
        if not isinstance(plugin, Plugin):
            raise TypeError("插件必须继承自Plugin抽象基类")
        
        self.plugins.append(plugin)
        plugin.initialize()
        print(f"插件已注册: {plugin.get_info()}")
    
    def execute_all(self, method_name: str, *args, **kwargs) -> None:
        """执行所有插件的指定方法"""
        for plugin in self.plugins:
            if hasattr(plugin, method_name):
                getattr(plugin, method_name)(*args, **kwargs)
    
    def cleanup_all(self) -> None:
        """清理所有插件"""
        for plugin in self.plugins:
            plugin.cleanup()
        self.plugins.clear()

# 测试插件系统
print("测试插件系统:")
manager = PluginManager()

# 注册插件
logging_plugin = LoggingPlugin()
cache_plugin = CachePlugin()

manager.register_plugin(logging_plugin)
manager.register_plugin(cache_plugin)

# 使用插件
print("\n使用插件:")
logging_plugin.execute("应用程序启动", "INFO")
cache_plugin.execute("set", "user_id", 12345)
cache_plugin.execute("get", "user_id")
logging_plugin.execute("缓存操作完成", "DEBUG")

# 清理插件
print("\n清理插件:")
manager.cleanup_all()

print("\n=== 抽象基类最佳实践 ===")
print("""
抽象基类最佳实践：

1. 何时使用抽象基类
   - 定义通用接口和规范
   - 确保子类实现必要方法
   - 提供部分通用实现
   - 建立类型层次结构

2. 设计原则
   - 抽象方法应该是必需的
   - 提供有意义的默认实现
   - 保持接口简洁明确
   - 考虑向后兼容性

3. 实现技巧
   - 使用@abstractmethod装饰器
   - 合理使用抽象属性
   - 提供具体的辅助方法
   - 编写清晰的文档字符串

4. 常见模式
   - 模板方法模式
   - 策略模式
   - 工厂模式
   - 插件系统

5. 注意事项
   - 不要过度抽象
   - 考虑多重继承的影响
   - 测试所有抽象方法的实现
   - 保持抽象层次的一致性
""")

if __name__ == "__main__":
    print("\n抽象基类演示完成!")
    print("抽象基类是面向对象设计中的重要工具，")
    print("它帮助我们定义清晰的接口和确保实现的一致性。")