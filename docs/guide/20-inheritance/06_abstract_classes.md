# 抽象基类

抽象基类（Abstract Base Classes, ABC）是Python中定义接口和强制子类实现特定方法的机制。通过使用abc模块，我们可以创建不能直接实例化的类，并确保子类实现必要的方法。

## 抽象基类的基本概念

抽象基类定义了一个接口，规定了子类必须实现的方法。这有助于确保代码的一致性和可维护性。

```python
from abc import ABC, abstractmethod

# 1. 基本抽象基类示例
class Animal(ABC):
    """动物抽象基类"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    @abstractmethod
    def make_sound(self):
        """抽象方法：发出声音"""
        pass
    
    @abstractmethod
    def move(self):
        """抽象方法：移动方式"""
        pass
    
    # 具体方法（非抽象）
    def introduce(self):
        """介绍自己"""
        return f"我是{self.name}，是一只{self.species}"
    
    def sleep(self):
        """睡觉（所有动物都会睡觉）"""
        return f"{self.name}正在睡觉"

print("=== 抽象基类基本概念 ===")

# 尝试直接实例化抽象基类（会报错）
try:
    animal = Animal("未知动物", "未知物种")
except TypeError as e:
    print(f"无法实例化抽象基类: {e}")
print()

# 正确的做法：创建具体的子类
class Dog(Animal):
    """狗类 - 实现所有抽象方法"""
    
    def __init__(self, name, breed):
        super().__init__(name, "犬科")
        self.breed = breed
    
    def make_sound(self):
        return f"{self.name}汪汪叫"
    
    def move(self):
        return f"{self.name}四腿奔跑"
    
    def fetch(self):
        """狗特有的方法"""
        return f"{self.name}去捡球"

class Bird(Animal):
    """鸟类 - 实现所有抽象方法"""
    
    def __init__(self, name, can_fly=True):
        super().__init__(name, "鸟类")
        self.can_fly = can_fly
    
    def make_sound(self):
        return f"{self.name}叽叽喳喳"
    
    def move(self):
        if self.can_fly:
            return f"{self.name}展翅飞翔"
        else:
            return f"{self.name}在地上跳跃"
    
    def build_nest(self):
        """鸟类特有的方法"""
        return f"{self.name}正在筑巢"

# 创建具体实例
dog = Dog("旺财", "金毛")
bird = Bird("小黄", True)

print("具体类实例测试:")
print(f"狗: {dog.introduce()}")
print(f"狗的声音: {dog.make_sound()}")
print(f"狗的移动: {dog.move()}")
print(f"狗的特殊行为: {dog.fetch()}")
print()

print(f"鸟: {bird.introduce()}")
print(f"鸟的声音: {bird.make_sound()}")
print(f"鸟的移动: {bird.move()}")
print(f"鸟的特殊行为: {bird.build_nest()}")
print()

# 测试不完整的实现（会报错）
class IncompleteAnimal(Animal):
    """不完整的动物类 - 只实现了部分抽象方法"""
    
    def make_sound(self):
        return "某种声音"
    
    # 注意：没有实现move()方法

try:
    incomplete = IncompleteAnimal("不完整", "未知")
except TypeError as e:
    print(f"不完整实现错误: {e}")
print()
```

## 抽象属性

除了抽象方法，Python还支持抽象属性，要求子类必须定义特定的属性。

```python
# 2. 抽象属性示例
from abc import ABC, abstractmethod, abstractproperty

class Shape(ABC):
    """形状抽象基类"""
    
    @property
    @abstractmethod
    def area(self):
        """抽象属性：面积"""
        pass
    
    @property
    @abstractmethod
    def perimeter(self):
        """抽象属性：周长"""
        pass
    
    @abstractmethod
    def describe(self):
        """抽象方法：描述形状"""
        pass
    
    # 具体方法
    def info(self):
        return f"{self.describe()}, 面积: {self.area:.2f}, 周长: {self.perimeter:.2f}"

class Rectangle(Shape):
    """矩形类"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def describe(self):
        return f"矩形(宽:{self.width}, 高:{self.height})"

class Circle(Shape):
    """圆形类"""
    
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    @property
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius
    
    def describe(self):
        return f"圆形(半径:{self.radius})"

print("=== 抽象属性示例 ===")

# 创建具体形状实例
rectangle = Rectangle(5, 3)
circle = Circle(4)

print("形状信息:")
print(rectangle.info())
print(circle.info())
print()

# 直接访问属性
print("直接访问属性:")
print(f"矩形面积: {rectangle.area}")
print(f"圆形周长: {circle.perimeter:.2f}")
print()
```

## 使用abc.register()注册虚拟子类

```python
# 3. 虚拟子类注册
from abc import ABC, abstractmethod

class Drawable(ABC):
    """可绘制对象抽象基类"""
    
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def get_bounds(self):
        """获取边界"""
        pass

# 传统方式：通过继承
class Square(Drawable):
    def __init__(self, size):
        self.size = size
    
    def draw(self):
        return f"绘制边长为{self.size}的正方形"
    
    def get_bounds(self):
        return (0, 0, self.size, self.size)

# 现有的类（不继承Drawable）
class ExistingImage:
    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.data = data
    
    def draw(self):
        return f"绘制{self.width}x{self.height}的图像"
    
    def get_bounds(self):
        return (0, 0, self.width, self.height)
    
    def save(self, filename):
        return f"保存图像到{filename}"

# 使用register()将现有类注册为虚拟子类
Drawable.register(ExistingImage)

print("=== 虚拟子类注册 ===")

# 测试类型检查
square = Square(10)
image = ExistingImage(800, 600, "image_data")

print("类型检查:")
print(f"Square是Drawable的实例: {isinstance(square, Drawable)}")
print(f"ExistingImage是Drawable的实例: {isinstance(image, Drawable)}")
print(f"Square是Drawable的子类: {issubclass(Square, Drawable)}")
print(f"ExistingImage是Drawable的子类: {issubclass(ExistingImage, Drawable)}")
print()

# 多态使用
def render_objects(drawables):
    """渲染可绘制对象列表"""
    for obj in drawables:
        if isinstance(obj, Drawable):
            print(f"渲染: {obj.draw()}")
            print(f"边界: {obj.get_bounds()}")
        else:
            print(f"无法渲染: {type(obj).__name__}")
        print()

print("多态渲染测试:")
render_objects([square, image, "不是可绘制对象"])
```

## 抽象基类的高级用法

```python
# 4. 抽象基类高级用法
from abc import ABC, abstractmethod
from typing import Any, List

class DataProcessor(ABC):
    """数据处理器抽象基类"""
    
    def __init__(self, name: str):
        self.name = name
        self._processed_count = 0
    
    @abstractmethod
    def validate_data(self, data: Any) -> bool:
        """验证数据"""
        pass
    
    @abstractmethod
    def process_item(self, item: Any) -> Any:
        """处理单个数据项"""
        pass
    
    @abstractmethod
    def get_supported_types(self) -> List[type]:
        """获取支持的数据类型"""
        pass
    
    # 模板方法模式
    def process_data(self, data: List[Any]) -> List[Any]:
        """处理数据的模板方法"""
        print(f"{self.name} 开始处理数据...")
        
        results = []
        for item in data:
            if self.validate_data(item):
                try:
                    result = self.process_item(item)
                    results.append(result)
                    self._processed_count += 1
                    print(f"处理成功: {item} -> {result}")
                except Exception as e:
                    print(f"处理失败: {item}, 错误: {e}")
            else:
                print(f"数据验证失败: {item}")
        
        print(f"{self.name} 处理完成，共处理 {len(results)} 项")
        return results
    
    def get_stats(self):
        """获取处理统计"""
        return {
            'name': self.name,
            'processed_count': self._processed_count,
            'supported_types': [t.__name__ for t in self.get_supported_types()]
        }

class NumberProcessor(DataProcessor):
    """数字处理器"""
    
    def __init__(self, operation='square'):
        super().__init__(f"数字处理器({operation})")
        self.operation = operation
    
    def validate_data(self, data: Any) -> bool:
        return isinstance(data, (int, float))
    
    def process_item(self, item: Any) -> Any:
        if self.operation == 'square':
            return item ** 2
        elif self.operation == 'double':
            return item * 2
        elif self.operation == 'abs':
            return abs(item)
        else:
            raise ValueError(f"不支持的操作: {self.operation}")
    
    def get_supported_types(self) -> List[type]:
        return [int, float]

class StringProcessor(DataProcessor):
    """字符串处理器"""
    
    def __init__(self, operation='upper'):
        super().__init__(f"字符串处理器({operation})")
        self.operation = operation
    
    def validate_data(self, data: Any) -> bool:
        return isinstance(data, str) and len(data) > 0
    
    def process_item(self, item: Any) -> Any:
        if self.operation == 'upper':
            return item.upper()
        elif self.operation == 'reverse':
            return item[::-1]
        elif self.operation == 'length':
            return len(item)
        else:
            raise ValueError(f"不支持的操作: {self.operation}")
    
    def get_supported_types(self) -> List[type]:
        return [str]

class ListProcessor(DataProcessor):
    """列表处理器"""
    
    def __init__(self, operation='sum'):
        super().__init__(f"列表处理器({operation})")
        self.operation = operation
    
    def validate_data(self, data: Any) -> bool:
        return isinstance(data, list) and len(data) > 0
    
    def process_item(self, item: Any) -> Any:
        if self.operation == 'sum':
            return sum(item) if all(isinstance(x, (int, float)) for x in item) else None
        elif self.operation == 'length':
            return len(item)
        elif self.operation == 'max':
            return max(item) if item else None
        else:
            raise ValueError(f"不支持的操作: {self.operation}")
    
    def get_supported_types(self) -> List[type]:
        return [list]

print("=== 抽象基类高级用法 ===")

# 创建不同的处理器
processors = [
    NumberProcessor('square'),
    StringProcessor('upper'),
    ListProcessor('sum')
]

# 测试数据
test_data = [
    [1, 2, 3, 4, 5],           # 数字列表
    ["hello", "world", "python"], # 字符串列表
    [[1, 2, 3], [4, 5], [6, 7, 8, 9]], # 嵌套列表
    [1.5, 2.5, 3.5],          # 浮点数列表
    ["invalid", 123, [1, 2]]   # 混合类型（部分无效）
]

# 使用每个处理器处理数据
for i, processor in enumerate(processors):
    print(f"\n--- 使用 {processor.name} ---")
    results = processor.process_data(test_data[i] if i < len(test_data) else test_data[0])
    print(f"处理结果: {results}")
    print(f"统计信息: {processor.get_stats()}")

# 处理器工厂
class ProcessorFactory:
    """处理器工厂"""
    
    _processors = {
        'number': NumberProcessor,
        'string': StringProcessor,
        'list': ListProcessor
    }
    
    @classmethod
    def create_processor(cls, processor_type: str, operation: str = None) -> DataProcessor:
        if processor_type not in cls._processors:
            raise ValueError(f"不支持的处理器类型: {processor_type}")
        
        processor_class = cls._processors[processor_type]
        if operation:
            return processor_class(operation)
        else:
            return processor_class()
    
    @classmethod
    def get_available_types(cls) -> List[str]:
        return list(cls._processors.keys())

print("\n=== 处理器工厂演示 ===")
print(f"可用处理器类型: {ProcessorFactory.get_available_types()}")

# 使用工厂创建处理器
factory_processor = ProcessorFactory.create_processor('string', 'reverse')
result = factory_processor.process_data(["hello", "world", "abc"])
print(f"工厂创建的处理器结果: {result}")
print()
```

## 内置抽象基类

Python标准库提供了许多有用的抽象基类，位于collections.abc模块中。

```python
# 5. 内置抽象基类使用
from collections.abc import Iterable, Container, Sized, Mapping, MutableMapping
from abc import ABC, abstractmethod

class CustomContainer(Container, Sized, Iterable):
    """自定义容器类"""
    
    def __init__(self, items=None):
        self._items = list(items) if items else []
    
    def __contains__(self, item):
        """实现Container协议"""
        return item in self._items
    
    def __len__(self):
        """实现Sized协议"""
        return len(self._items)
    
    def __iter__(self):
        """实现Iterable协议"""
        return iter(self._items)
    
    def add(self, item):
        """添加元素"""
        if item not in self._items:
            self._items.append(item)
    
    def remove(self, item):
        """移除元素"""
        if item in self._items:
            self._items.remove(item)
    
    def __repr__(self):
        return f"CustomContainer({self._items})"

class CustomMapping(MutableMapping):
    """自定义映射类"""
    
    def __init__(self, data=None):
        self._data = dict(data) if data else {}
    
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
    
    def __repr__(self):
        return f"CustomMapping({self._data})"

print("=== 内置抽象基类使用 ===")

# 测试自定义容器
container = CustomContainer([1, 2, 3])
print(f"容器: {container}")
print(f"长度: {len(container)}")
print(f"包含2: {2 in container}")
print(f"包含5: {5 in container}")

print("\n迭代容器:")
for item in container:
    print(f"  {item}")

container.add(4)
container.add(2)  # 重复添加
print(f"\n添加元素后: {container}")

container.remove(2)
print(f"移除元素后: {container}")

# 测试类型检查
print(f"\n类型检查:")
print(f"是否为Container: {isinstance(container, Container)}")
print(f"是否为Sized: {isinstance(container, Sized)}")
print(f"是否为Iterable: {isinstance(container, Iterable)}")

# 测试自定义映射
print("\n--- 自定义映射测试 ---")
mapping = CustomMapping({'a': 1, 'b': 2})
print(f"映射: {mapping}")
print(f"键'a'的值: {mapping['a']}")

mapping['c'] = 3
print(f"添加键'c'后: {mapping}")

del mapping['b']
print(f"删除键'b'后: {mapping}")

print(f"\n映射类型检查:")
print(f"是否为Mapping: {isinstance(mapping, Mapping)}")
print(f"是否为MutableMapping: {isinstance(mapping, MutableMapping)}")
print()
```

## 抽象基类的实际应用

```python
# 6. 抽象基类实际应用 - 插件系统
from abc import ABC, abstractmethod
from typing import Dict, Any, List
import json

class DataExporter(ABC):
    """数据导出器抽象基类"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def export(self, data: Any, filename: str) -> bool:
        """导出数据到文件"""
        pass
    
    @abstractmethod
    def get_file_extension(self) -> str:
        """获取文件扩展名"""
        pass
    
    @abstractmethod
    def validate_data(self, data: Any) -> bool:
        """验证数据格式"""
        pass
    
    def get_info(self) -> Dict[str, str]:
        """获取导出器信息"""
        return {
            'name': self.name,
            'extension': self.get_file_extension(),
            'class': self.__class__.__name__
        }

class JSONExporter(DataExporter):
    """JSON导出器"""
    
    def __init__(self):
        super().__init__("JSON导出器")
    
    def export(self, data: Any, filename: str) -> bool:
        try:
            if not filename.endswith('.json'):
                filename += '.json'
            
            # 模拟文件写入
            json_str = json.dumps(data, ensure_ascii=False, indent=2)
            print(f"导出JSON到 {filename}:")
            print(json_str[:200] + "..." if len(json_str) > 200 else json_str)
            return True
        except Exception as e:
            print(f"JSON导出失败: {e}")
            return False
    
    def get_file_extension(self) -> str:
        return ".json"
    
    def validate_data(self, data: Any) -> bool:
        try:
            json.dumps(data)
            return True
        except (TypeError, ValueError):
            return False

class CSVExporter(DataExporter):
    """CSV导出器"""
    
    def __init__(self):
        super().__init__("CSV导出器")
    
    def export(self, data: Any, filename: str) -> bool:
        try:
            if not filename.endswith('.csv'):
                filename += '.csv'
            
            if isinstance(data, list) and data and isinstance(data[0], dict):
                # 模拟CSV写入
                headers = list(data[0].keys())
                print(f"导出CSV到 {filename}:")
                print(",".join(headers))
                for row in data[:3]:  # 只显示前3行
                    print(",".join(str(row.get(h, '')) for h in headers))
                if len(data) > 3:
                    print(f"... 还有 {len(data) - 3} 行")
                return True
            else:
                print("CSV导出需要字典列表格式的数据")
                return False
        except Exception as e:
            print(f"CSV导出失败: {e}")
            return False
    
    def get_file_extension(self) -> str:
        return ".csv"
    
    def validate_data(self, data: Any) -> bool:
        return (isinstance(data, list) and 
                data and 
                isinstance(data[0], dict))

class XMLExporter(DataExporter):
    """XML导出器"""
    
    def __init__(self):
        super().__init__("XML导出器")
    
    def export(self, data: Any, filename: str) -> bool:
        try:
            if not filename.endswith('.xml'):
                filename += '.xml'
            
            # 简单的XML生成
            xml_content = self._dict_to_xml(data)
            print(f"导出XML到 {filename}:")
            print(xml_content[:300] + "..." if len(xml_content) > 300 else xml_content)
            return True
        except Exception as e:
            print(f"XML导出失败: {e}")
            return False
    
    def _dict_to_xml(self, data: Any, root_name: str = "root") -> str:
        """简单的字典到XML转换"""
        if isinstance(data, dict):
            xml = f"<{root_name}>\n"
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    xml += f"  {self._dict_to_xml(value, key)}\n"
                else:
                    xml += f"  <{key}>{value}</{key}>\n"
            xml += f"</{root_name}>"
            return xml
        elif isinstance(data, list):
            xml = f"<{root_name}>\n"
            for i, item in enumerate(data):
                xml += f"  {self._dict_to_xml(item, f'item_{i}')}\n"
            xml += f"</{root_name}>"
            return xml
        else:
            return f"<{root_name}>{data}</{root_name}>"
    
    def get_file_extension(self) -> str:
        return ".xml"
    
    def validate_data(self, data: Any) -> bool:
        return isinstance(data, (dict, list))

class ExportManager:
    """导出管理器"""
    
    def __init__(self):
        self._exporters: Dict[str, DataExporter] = {}
    
    def register_exporter(self, exporter: DataExporter):
        """注册导出器"""
        if not isinstance(exporter, DataExporter):
            raise TypeError("导出器必须继承自DataExporter")
        
        extension = exporter.get_file_extension()
        self._exporters[extension] = exporter
        print(f"注册导出器: {exporter.name} ({extension})")
    
    def get_available_formats(self) -> List[str]:
        """获取可用格式"""
        return list(self._exporters.keys())
    
    def export_data(self, data: Any, filename: str, format_type: str = None) -> bool:
        """导出数据"""
        if format_type is None:
            # 从文件名推断格式
            for ext in self._exporters.keys():
                if filename.endswith(ext):
                    format_type = ext
                    break
            
            if format_type is None:
                print(f"无法从文件名 '{filename}' 推断格式")
                return False
        
        if format_type not in self._exporters:
            print(f"不支持的格式: {format_type}")
            print(f"支持的格式: {self.get_available_formats()}")
            return False
        
        exporter = self._exporters[format_type]
        
        if not exporter.validate_data(data):
            print(f"数据格式不适合 {exporter.name}")
            return False
        
        return exporter.export(data, filename)
    
    def list_exporters(self):
        """列出所有导出器"""
        print("已注册的导出器:")
        for ext, exporter in self._exporters.items():
            info = exporter.get_info()
            print(f"  {ext}: {info['name']} ({info['class']})")

print("=== 抽象基类实际应用 - 插件系统 ===")

# 创建导出管理器并注册导出器
manager = ExportManager()
manager.register_exporter(JSONExporter())
manager.register_exporter(CSVExporter())
manager.register_exporter(XMLExporter())

print()
manager.list_exporters()
print()

# 测试数据
test_data = [
    {'name': '张三', 'age': 25, 'city': '北京'},
    {'name': '李四', 'age': 30, 'city': '上海'},
    {'name': '王五', 'age': 28, 'city': '广州'}
]

# 测试不同格式的导出
print("=== 导出测试 ===")
formats_to_test = ['.json', '.csv', '.xml']

for fmt in formats_to_test:
    print(f"\n--- 导出为 {fmt} 格式 ---")
    success = manager.export_data(test_data, f"users{fmt}")
    print(f"导出结果: {'成功' if success else '失败'}")

# 测试无效数据
print("\n--- 测试无效数据 ---")
invalid_data = "这不是有效的数据格式"
success = manager.export_data(invalid_data, "invalid.csv")
print(f"无效数据导出结果: {'成功' if success else '失败'}")
print()
```

## 抽象基类的最佳实践

```python
# 7. 抽象基类最佳实践
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

print("=== 抽象基类最佳实践 ===")

# 实践1：使用Protocol进行结构化子类型
@runtime_checkable
class Drawable(Protocol):
    """可绘制协议"""
    def draw(self) -> str:
        ...
    
    def get_area(self) -> float:
        ...

# 实践2：组合抽象基类和具体实现
class GraphicsObject(ABC):
    """图形对象抽象基类"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self._visible = True
    
    @abstractmethod
    def draw(self) -> str:
        """绘制对象"""
        pass
    
    @abstractmethod
    def get_area(self) -> float:
        """获取面积"""
        pass
    
    # 具体方法提供通用功能
    def move(self, dx: float, dy: float):
        """移动对象"""
        self.x += dx
        self.y += dy
    
    def set_visible(self, visible: bool):
        """设置可见性"""
        self._visible = visible
    
    def is_visible(self) -> bool:
        """检查是否可见"""
        return self._visible
    
    def get_position(self) -> tuple:
        """获取位置"""
        return (self.x, self.y)
    
    def __str__(self):
        return f"{self.__class__.__name__} at ({self.x}, {self.y})"

class Circle(GraphicsObject):
    """圆形类"""
    
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y)
        self.radius = radius
    
    def draw(self) -> str:
        if self.is_visible():
            return f"绘制圆形: 中心({self.x}, {self.y}), 半径{self.radius}"
        return "圆形不可见"
    
    def get_area(self) -> float:
        import math
        return math.pi * self.radius ** 2

class Rectangle(GraphicsObject):
    """矩形类"""
    
    def __init__(self, x: float, y: float, width: float, height: float):
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    def draw(self) -> str:
        if self.is_visible():
            return f"绘制矩形: 左上角({self.x}, {self.y}), 宽{self.width}, 高{self.height}"
        return "矩形不可见"
    
    def get_area(self) -> float:
        return self.width * self.height

# 实践3：使用抽象基类进行类型检查和多态
def render_scene(objects: list[GraphicsObject]):
    """渲染场景中的所有对象"""
    print("渲染场景:")
    total_area = 0
    
    for obj in objects:
        if isinstance(obj, GraphicsObject):
            print(f"  {obj.draw()}")
            total_area += obj.get_area()
        else:
            print(f"  警告: {obj} 不是有效的图形对象")
    
    print(f"总面积: {total_area:.2f}")

# 实践4：抽象基类的文档和类型提示
class ConfigurableProcessor(ABC):
    """可配置处理器抽象基类
    
    这个抽象基类定义了所有处理器必须实现的接口。
    子类必须实现process方法来处理具体的业务逻辑。
    """
    
    def __init__(self, config: dict = None):
        """初始化处理器
        
        Args:
            config: 配置字典，包含处理器的配置参数
        """
        self.config = config or {}
        self._initialized = False
    
    @abstractmethod
    def process(self, data: any) -> any:
        """处理数据的抽象方法
        
        Args:
            data: 要处理的数据
            
        Returns:
            处理后的数据
            
        Raises:
            NotImplementedError: 子类必须实现此方法
        """
        raise NotImplementedError("子类必须实现process方法")
    
    def initialize(self):
        """初始化处理器（可选重写）"""
        self._initialized = True
        print(f"{self.__class__.__name__} 已初始化")
    
    def is_initialized(self) -> bool:
        """检查是否已初始化"""
        return self._initialized

# 测试最佳实践
print("\n图形对象测试:")
circle = Circle(10, 20, 5)
rectangle = Rectangle(0, 0, 10, 8)

print(f"圆形: {circle}")
print(f"矩形: {rectangle}")

# 移动对象
circle.move(5, 5)
print(f"移动后的圆形: {circle}")

# 设置可见性
rectangle.set_visible(False)

# 渲染场景
render_scene([circle, rectangle])

# 协议检查
print(f"\n协议检查:")
print(f"圆形实现了Drawable协议: {isinstance(circle, Drawable)}")
print(f"矩形实现了Drawable协议: {isinstance(rectangle, Drawable)}")
print()
```

## 总结

```python
print("=== 抽象基类总结 ===")
print("""
抽象基类（ABC）核心要点:

1. 基本概念
   - 定义接口和规范
   - 不能直接实例化
   - 强制子类实现抽象方法

2. 主要特性
   - @abstractmethod装饰器
   - @property + @abstractmethod组合
   - abc.register()虚拟子类
   - 模板方法模式支持

3. 使用场景
   - 定义接口规范
   - 插件系统设计
   - 框架和库开发
   - 多态实现

4. 内置抽象基类
   - collections.abc模块
   - Container, Iterable, Sized等
   - Mapping, MutableMapping等

5. 最佳实践
   - 组合抽象和具体方法
   - 提供清晰的文档
   - 使用类型提示
   - 合理的继承层次

6. 与Protocol的关系
   - Protocol用于结构化子类型
   - ABC用于名义子类型
   - 可以结合使用

抽象基类是设计清晰、可维护代码架构的重要工具！
""")
```

## 学习要点

1. **ABC概念**：理解抽象基类的作用和重要性
2. **抽象方法**：使用@abstractmethod装饰器定义抽象方法
3. **抽象属性**：结合@property和@abstractmethod定义抽象属性
4. **虚拟子类**：使用register()方法注册虚拟子类
5. **内置ABC**：了解collections.abc模块中的内置抽象基类
6. **实际应用**：在插件系统、框架设计中的应用
7. **最佳实践**：如何设计良好的抽象基类层次结构

## 注意事项

- 抽象基类不能直接实例化
- 子类必须实现所有抽象方法才能实例化
- 抽象基类可以包含具体方法
- 合理使用抽象基类，避免过度设计
- 考虑使用Protocol作为轻量级的接口定义
- 提供清晰的文档和类型提示