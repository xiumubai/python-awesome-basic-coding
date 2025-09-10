#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多态的设计模式 - Design Patterns with Polymorphism

多态是许多设计模式的核心机制，通过多态可以实现灵活、可扩展的软件架构。
本文件演示几种常见的基于多态的设计模式。

学习目标：
1. 理解策略模式（Strategy Pattern）
2. 掌握工厂模式（Factory Pattern）
3. 学会观察者模式（Observer Pattern）
4. 了解模板方法模式（Template Method Pattern）
5. 掌握状态模式（State Pattern）
6. 学会装饰器模式（Decorator Pattern）
"""

from abc import ABC, abstractmethod
from typing import List, Protocol, Any
import time
import random


# ============================================================================
# 1. 策略模式 (Strategy Pattern)
# ============================================================================

class SortStrategy(ABC):
    """排序策略抽象基类"""
    
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        """排序方法"""
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """策略名称"""
        pass


class BubbleSortStrategy(SortStrategy):
    """冒泡排序策略"""
    
    def sort(self, data: List[int]) -> List[int]:
        """冒泡排序实现"""
        result = data.copy()
        n = len(result)
        for i in range(n):
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result
    
    @property
    def name(self) -> str:
        return "冒泡排序"


class QuickSortStrategy(SortStrategy):
    """快速排序策略"""
    
    def sort(self, data: List[int]) -> List[int]:
        """快速排序实现"""
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
    
    @property
    def name(self) -> str:
        return "快速排序"


class MergeSortStrategy(SortStrategy):
    """归并排序策略"""
    
    def sort(self, data: List[int]) -> List[int]:
        """归并排序实现"""
        if len(data) <= 1:
            return data.copy()
        
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    @property
    def name(self) -> str:
        return "归并排序"


class SortContext:
    """排序上下文类"""
    
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: SortStrategy):
        """设置排序策略"""
        self._strategy = strategy
    
    def sort(self, data: List[int]) -> List[int]:
        """执行排序"""
        print(f"使用{self._strategy.name}进行排序...")
        start_time = time.time()
        result = self._strategy.sort(data)
        end_time = time.time()
        print(f"排序完成，耗时: {(end_time - start_time) * 1000:.2f}ms")
        return result


# ============================================================================
# 2. 工厂模式 (Factory Pattern)
# ============================================================================

class Animal(ABC):
    """动物抽象基类"""
    
    @abstractmethod
    def make_sound(self) -> str:
        """发出声音"""
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        """获取动物类型"""
        pass


class Dog(Animal):
    """狗类"""
    
    def make_sound(self) -> str:
        return "汪汪！"
    
    def get_type(self) -> str:
        return "狗"


class Cat(Animal):
    """猫类"""
    
    def make_sound(self) -> str:
        return "喵喵！"
    
    def get_type(self) -> str:
        return "猫"


class Bird(Animal):
    """鸟类"""
    
    def make_sound(self) -> str:
        return "啾啾！"
    
    def get_type(self) -> str:
        return "鸟"


class AnimalFactory:
    """动物工厂类"""
    
    _animals = {
        "dog": Dog,
        "cat": Cat,
        "bird": Bird
    }
    
    @classmethod
    def create_animal(cls, animal_type: str) -> Animal:
        """创建动物对象"""
        animal_class = cls._animals.get(animal_type.lower())
        if animal_class:
            return animal_class()
        else:
            raise ValueError(f"不支持的动物类型: {animal_type}")
    
    @classmethod
    def get_supported_types(cls) -> List[str]:
        """获取支持的动物类型"""
        return list(cls._animals.keys())


# ============================================================================
# 3. 观察者模式 (Observer Pattern)
# ============================================================================

class Observer(ABC):
    """观察者抽象基类"""
    
    @abstractmethod
    def update(self, subject: 'Subject', data: Any):
        """接收通知"""
        pass


class Subject(ABC):
    """主题抽象基类"""
    
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        """添加观察者"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer):
        """移除观察者"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, data: Any = None):
        """通知所有观察者"""
        for observer in self._observers:
            observer.update(self, data)


class WeatherStation(Subject):
    """天气站（主题）"""
    
    def __init__(self):
        super().__init__()
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0
    
    def set_weather_data(self, temperature: float, humidity: float, pressure: float):
        """设置天气数据"""
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify({
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure
        })
    
    @property
    def temperature(self) -> float:
        return self._temperature
    
    @property
    def humidity(self) -> float:
        return self._humidity
    
    @property
    def pressure(self) -> float:
        return self._pressure


class CurrentConditionsDisplay(Observer):
    """当前天气显示器"""
    
    def __init__(self, name: str):
        self.name = name
    
    def update(self, subject: Subject, data: Any):
        """更新显示"""
        if isinstance(subject, WeatherStation) and data:
            print(f"[{self.name}] 当前天气: {data['temperature']}°C, "
                  f"湿度: {data['humidity']}%, 气压: {data['pressure']}hPa")


class StatisticsDisplay(Observer):
    """统计显示器"""
    
    def __init__(self):
        self.temperatures = []
    
    def update(self, subject: Subject, data: Any):
        """更新统计"""
        if isinstance(subject, WeatherStation) and data:
            self.temperatures.append(data['temperature'])
            avg_temp = sum(self.temperatures) / len(self.temperatures)
            max_temp = max(self.temperatures)
            min_temp = min(self.temperatures)
            print(f"[统计] 平均温度: {avg_temp:.1f}°C, "
                  f"最高: {max_temp}°C, 最低: {min_temp}°C")


class ForecastDisplay(Observer):
    """预报显示器"""
    
    def __init__(self):
        self.last_pressure = 0
    
    def update(self, subject: Subject, data: Any):
        """更新预报"""
        if isinstance(subject, WeatherStation) and data:
            current_pressure = data['pressure']
            if self.last_pressure != 0:
                if current_pressure > self.last_pressure:
                    forecast = "天气转好"
                elif current_pressure < self.last_pressure:
                    forecast = "可能下雨"
                else:
                    forecast = "天气稳定"
                print(f"[预报] {forecast}")
            self.last_pressure = current_pressure


# ============================================================================
# 4. 模板方法模式 (Template Method Pattern)
# ============================================================================

class DataProcessor(ABC):
    """数据处理模板类"""
    
    def process(self, data: str) -> str:
        """模板方法 - 定义处理流程"""
        print(f"开始处理数据: {data[:20]}...")
        
        # 1. 验证数据
        if not self.validate_data(data):
            raise ValueError("数据验证失败")
        
        # 2. 预处理
        processed_data = self.preprocess(data)
        
        # 3. 核心处理
        result = self.core_process(processed_data)
        
        # 4. 后处理
        final_result = self.postprocess(result)
        
        # 5. 保存结果（可选）
        if self.should_save():
            self.save_result(final_result)
        
        print("数据处理完成")
        return final_result
    
    def validate_data(self, data: str) -> bool:
        """验证数据 - 默认实现"""
        return data is not None and len(data) > 0
    
    @abstractmethod
    def preprocess(self, data: str) -> str:
        """预处理 - 子类必须实现"""
        pass
    
    @abstractmethod
    def core_process(self, data: str) -> str:
        """核心处理 - 子类必须实现"""
        pass
    
    def postprocess(self, data: str) -> str:
        """后处理 - 默认实现"""
        return data
    
    def should_save(self) -> bool:
        """是否保存结果 - 默认不保存"""
        return False
    
    def save_result(self, result: str):
        """保存结果 - 默认实现"""
        print(f"保存结果: {result[:50]}...")


class TextProcessor(DataProcessor):
    """文本处理器"""
    
    def preprocess(self, data: str) -> str:
        """文本预处理"""
        print("执行文本预处理: 去除多余空格")
        return ' '.join(data.split())
    
    def core_process(self, data: str) -> str:
        """文本核心处理"""
        print("执行文本核心处理: 转换为大写")
        return data.upper()
    
    def should_save(self) -> bool:
        return True


class JSONProcessor(DataProcessor):
    """JSON处理器"""
    
    def validate_data(self, data: str) -> bool:
        """JSON数据验证"""
        try:
            import json
            json.loads(data)
            return True
        except:
            return False
    
    def preprocess(self, data: str) -> str:
        """JSON预处理"""
        print("执行JSON预处理: 格式化")
        import json
        return json.dumps(json.loads(data), indent=2)
    
    def core_process(self, data: str) -> str:
        """JSON核心处理"""
        print("执行JSON核心处理: 提取键值")
        import json
        obj = json.loads(data)
        keys = list(obj.keys()) if isinstance(obj, dict) else []
        return f"JSON包含键: {keys}"


# ============================================================================
# 5. 状态模式 (State Pattern)
# ============================================================================

class State(ABC):
    """状态抽象基类"""
    
    @abstractmethod
    def handle_request(self, context: 'StateContext') -> str:
        """处理请求"""
        pass
    
    @abstractmethod
    def get_state_name(self) -> str:
        """获取状态名称"""
        pass


class IdleState(State):
    """空闲状态"""
    
    def handle_request(self, context: 'StateContext') -> str:
        print("设备处于空闲状态，开始工作...")
        context.set_state(WorkingState())
        return "设备开始工作"
    
    def get_state_name(self) -> str:
        return "空闲"


class WorkingState(State):
    """工作状态"""
    
    def handle_request(self, context: 'StateContext') -> str:
        print("设备正在工作，完成任务...")
        context.set_state(IdleState())
        return "任务完成，设备空闲"
    
    def get_state_name(self) -> str:
        return "工作中"


class ErrorState(State):
    """错误状态"""
    
    def handle_request(self, context: 'StateContext') -> str:
        print("设备出现错误，正在修复...")
        context.set_state(IdleState())
        return "错误已修复，设备恢复空闲"
    
    def get_state_name(self) -> str:
        return "错误"


class StateContext:
    """状态上下文"""
    
    def __init__(self):
        self._state = IdleState()
    
    def set_state(self, state: State):
        """设置状态"""
        print(f"状态切换: {self._state.get_state_name()} -> {state.get_state_name()}")
        self._state = state
    
    def request(self) -> str:
        """处理请求"""
        return self._state.handle_request(self)
    
    def get_current_state(self) -> str:
        """获取当前状态"""
        return self._state.get_state_name()
    
    def trigger_error(self):
        """触发错误"""
        print("触发设备错误...")
        self.set_state(ErrorState())


# ============================================================================
# 6. 装饰器模式 (Decorator Pattern)
# ============================================================================

class Component(ABC):
    """组件抽象基类"""
    
    @abstractmethod
    def operation(self) -> str:
        """执行操作"""
        pass
    
    @abstractmethod
    def get_cost(self) -> float:
        """获取成本"""
        pass


class Coffee(Component):
    """基础咖啡"""
    
    def operation(self) -> str:
        return "基础咖啡"
    
    def get_cost(self) -> float:
        return 10.0


class Decorator(Component):
    """装饰器抽象基类"""
    
    def __init__(self, component: Component):
        self._component = component
    
    def operation(self) -> str:
        return self._component.operation()
    
    def get_cost(self) -> float:
        return self._component.get_cost()


class MilkDecorator(Decorator):
    """牛奶装饰器"""
    
    def operation(self) -> str:
        return f"{self._component.operation()} + 牛奶"
    
    def get_cost(self) -> float:
        return self._component.get_cost() + 2.0


class SugarDecorator(Decorator):
    """糖装饰器"""
    
    def operation(self) -> str:
        return f"{self._component.operation()} + 糖"
    
    def get_cost(self) -> float:
        return self._component.get_cost() + 1.0


class ChocolateDecorator(Decorator):
    """巧克力装饰器"""
    
    def operation(self) -> str:
        return f"{self._component.operation()} + 巧克力"
    
    def get_cost(self) -> float:
        return self._component.get_cost() + 3.0


# ============================================================================
# 演示函数
# ============================================================================

def demonstrate_strategy_pattern():
    """演示策略模式"""
    print("=== 策略模式演示 ===")
    
    # 创建测试数据
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"原始数据: {data}")
    
    # 创建排序上下文
    sorter = SortContext(BubbleSortStrategy())
    
    # 使用不同策略排序
    strategies = [BubbleSortStrategy(), QuickSortStrategy(), MergeSortStrategy()]
    
    for strategy in strategies:
        print(f"\n--- {strategy.name} ---")
        sorter.set_strategy(strategy)
        result = sorter.sort(data)
        print(f"排序结果: {result}")


def demonstrate_factory_pattern():
    """演示工厂模式"""
    print("\n=== 工厂模式演示 ===")
    
    print(f"支持的动物类型: {AnimalFactory.get_supported_types()}")
    
    # 创建不同类型的动物
    animal_types = ["dog", "cat", "bird"]
    animals = []
    
    for animal_type in animal_types:
        try:
            animal = AnimalFactory.create_animal(animal_type)
            animals.append(animal)
            print(f"创建{animal.get_type()}: {animal.make_sound()}")
        except ValueError as e:
            print(f"创建失败: {e}")
    
    # 多态调用
    print("\n动物大合唱:")
    for animal in animals:
        print(f"{animal.get_type()}: {animal.make_sound()}")


def demonstrate_observer_pattern():
    """演示观察者模式"""
    print("\n=== 观察者模式演示 ===")
    
    # 创建天气站
    weather_station = WeatherStation()
    
    # 创建观察者
    current_display = CurrentConditionsDisplay("显示器1")
    current_display2 = CurrentConditionsDisplay("显示器2")
    stats_display = StatisticsDisplay()
    forecast_display = ForecastDisplay()
    
    # 注册观察者
    weather_station.attach(current_display)
    weather_station.attach(current_display2)
    weather_station.attach(stats_display)
    weather_station.attach(forecast_display)
    
    # 更新天气数据
    print("\n第一次天气更新:")
    weather_station.set_weather_data(25.0, 65.0, 1013.2)
    
    print("\n第二次天气更新:")
    weather_station.set_weather_data(27.0, 70.0, 1015.5)
    
    print("\n第三次天气更新:")
    weather_station.set_weather_data(23.0, 60.0, 1010.8)
    
    # 移除一个观察者
    print("\n移除显示器2后的更新:")
    weather_station.detach(current_display2)
    weather_station.set_weather_data(26.0, 68.0, 1012.0)


def demonstrate_template_method_pattern():
    """演示模板方法模式"""
    print("\n=== 模板方法模式演示 ===")
    
    # 文本处理
    print("\n--- 文本处理 ---")
    text_processor = TextProcessor()
    text_data = "  hello   world  python   "
    result1 = text_processor.process(text_data)
    print(f"处理结果: {result1}")
    
    # JSON处理
    print("\n--- JSON处理 ---")
    json_processor = JSONProcessor()
    json_data = '{"name": "张三", "age": 25, "city": "北京"}'
    result2 = json_processor.process(json_data)
    print(f"处理结果: {result2}")


def demonstrate_state_pattern():
    """演示状态模式"""
    print("\n=== 状态模式演示 ===")
    
    # 创建设备
    device = StateContext()
    
    print(f"初始状态: {device.get_current_state()}")
    
    # 执行操作
    for i in range(3):
        print(f"\n第{i+1}次操作:")
        result = device.request()
        print(f"操作结果: {result}")
        print(f"当前状态: {device.get_current_state()}")
    
    # 触发错误
    print("\n触发错误:")
    device.trigger_error()
    print(f"当前状态: {device.get_current_state()}")
    
    # 从错误恢复
    print("\n从错误恢复:")
    result = device.request()
    print(f"操作结果: {result}")
    print(f"当前状态: {device.get_current_state()}")


def demonstrate_decorator_pattern():
    """演示装饰器模式"""
    print("\n=== 装饰器模式演示 ===")
    
    # 基础咖啡
    coffee = Coffee()
    print(f"订单: {coffee.operation()}, 价格: ¥{coffee.get_cost():.1f}")
    
    # 添加牛奶
    coffee_with_milk = MilkDecorator(coffee)
    print(f"订单: {coffee_with_milk.operation()}, 价格: ¥{coffee_with_milk.get_cost():.1f}")
    
    # 添加糖
    coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)
    print(f"订单: {coffee_with_milk_sugar.operation()}, 价格: ¥{coffee_with_milk_sugar.get_cost():.1f}")
    
    # 添加巧克力
    deluxe_coffee = ChocolateDecorator(coffee_with_milk_sugar)
    print(f"订单: {deluxe_coffee.operation()}, 价格: ¥{deluxe_coffee.get_cost():.1f}")
    
    # 另一种组合
    print("\n另一种组合:")
    simple_coffee = ChocolateDecorator(SugarDecorator(Coffee()))
    print(f"订单: {simple_coffee.operation()}, 价格: ¥{simple_coffee.get_cost():.1f}")


def demonstrate_polymorphism_in_patterns():
    """演示设计模式中的多态性"""
    print("\n=== 设计模式中的多态性 ===")
    
    print("1. 多态使得客户端代码与具体实现解耦")
    print("2. 支持运行时动态选择具体实现")
    print("3. 便于扩展新的实现类")
    print("4. 提高代码的可维护性和可测试性")
    
    # 演示多态的威力
    print("\n多态演示 - 统一接口处理不同对象:")
    
    # 不同的排序策略
    strategies = [BubbleSortStrategy(), QuickSortStrategy(), MergeSortStrategy()]
    data = [5, 2, 8, 1, 9]
    
    for strategy in strategies:
        # 同样的接口，不同的实现
        result = strategy.sort(data)
        print(f"{strategy.name}: {result}")
    
    print("\n不同的动物，同样的接口:")
    animals = [Dog(), Cat(), Bird()]
    for animal in animals:
        # 同样的方法调用，不同的行为
        print(f"{animal.get_type()}: {animal.make_sound()}")


if __name__ == "__main__":
    print("Python 多态设计模式学习")
    print("=" * 50)
    
    # 演示各种设计模式
    demonstrate_strategy_pattern()
    demonstrate_factory_pattern()
    demonstrate_observer_pattern()
    demonstrate_template_method_pattern()
    demonstrate_state_pattern()
    demonstrate_decorator_pattern()
    demonstrate_polymorphism_in_patterns()
    
    print("\n=== 多态设计模式的核心要点 ===")
    print("1. 多态是许多设计模式的基础")
    print("2. 策略模式：封装算法族，使它们可以互换")
    print("3. 工厂模式：创建对象而不指定具体类")
    print("4. 观察者模式：定义对象间的一对多依赖")
    print("5. 模板方法模式：定义算法骨架，子类实现细节")
    print("6. 状态模式：对象状态改变时改变其行为")
    print("7. 装饰器模式：动态地给对象添加职责")
    print("8. 多态提供了设计的灵活性和可扩展性")