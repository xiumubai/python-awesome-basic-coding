# 多态的设计模式

## 策略模式 (Strategy Pattern)

策略模式定义了一系列算法，把它们一个个封装起来，并且使它们可相互替换。策略模式让算法的变化独立于使用算法的客户。这是多态性的经典应用。

### 基本实现

```python
from abc import ABC, abstractmethod
from typing import List, Protocol
import math

# 策略接口
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

# 具体策略实现
class BubbleSortStrategy(SortStrategy):
    """冒泡排序策略"""
    
    @property
    def name(self) -> str:
        return "冒泡排序"
    
    def sort(self, data: List[int]) -> List[int]:
        """冒泡排序实现"""
        result = data.copy()
        n = len(result)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        
        return result

class QuickSortStrategy(SortStrategy):
    """快速排序策略"""
    
    @property
    def name(self) -> str:
        return "快速排序"
    
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

class MergeSortStrategy(SortStrategy):
    """归并排序策略"""
    
    @property
    def name(self) -> str:
        return "归并排序"
    
    def sort(self, data: List[int]) -> List[int]:
        """归并排序实现"""
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

# 上下文类
class SortContext:
    """排序上下文类"""
    
    def __init__(self, strategy: SortStrategy = None):
        self._strategy = strategy
    
    def set_strategy(self, strategy: SortStrategy):
        """设置排序策略"""
        self._strategy = strategy
    
    def sort(self, data: List[int]) -> List[int]:
        """执行排序"""
        if not self._strategy:
            raise ValueError("未设置排序策略")
        
        print(f"使用{self._strategy.name}进行排序...")
        return self._strategy.sort(data)
    
    def get_strategy_name(self) -> str:
        """获取当前策略名称"""
        return self._strategy.name if self._strategy else "未设置"

# 演示策略模式
def demonstrate_strategy_pattern():
    """演示策略模式"""
    print("=== 策略模式演示 ===")
    
    # 测试数据
    test_data = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"原始数据: {test_data}")
    print()
    
    # 创建排序上下文
    sorter = SortContext()
    
    # 创建不同的排序策略
    strategies = [
        BubbleSortStrategy(),
        QuickSortStrategy(),
        MergeSortStrategy()
    ]
    
    # 使用不同策略进行排序
    for strategy in strategies:
        sorter.set_strategy(strategy)
        sorted_data = sorter.sort(test_data)
        print(f"结果: {sorted_data}")
        print(f"当前策略: {sorter.get_strategy_name()}")
        print()
    
    print("=== 策略模式演示完成 ===\n")

demonstrate_strategy_pattern()
```

## 工厂模式 (Factory Pattern)

工厂模式提供了一种创建对象的最佳方式。在工厂模式中，我们在创建对象时不会对客户端暴露创建逻辑，并且是通过使用一个共同的接口来指向新创建的对象。

### 简单工厂模式

```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Type

# 产品接口
class Animal(ABC):
    """动物抽象基类"""
    
    @abstractmethod
    def make_sound(self) -> str:
        """发出声音"""
        pass
    
    @abstractmethod
    def move(self) -> str:
        """移动方式"""
        pass
    
    @property
    @abstractmethod
    def species(self) -> str:
        """物种名称"""
        pass

# 具体产品
class Dog(Animal):
    """狗类"""
    
    @property
    def species(self) -> str:
        return "狗"
    
    def make_sound(self) -> str:
        return "汪汪!"
    
    def move(self) -> str:
        return "跑步"

class Cat(Animal):
    """猫类"""
    
    @property
    def species(self) -> str:
        return "猫"
    
    def make_sound(self) -> str:
        return "喵喵!"
    
    def move(self) -> str:
        return "悄悄走路"

class Bird(Animal):
    """鸟类"""
    
    @property
    def species(self) -> str:
        return "鸟"
    
    def make_sound(self) -> str:
        return "啾啾!"
    
    def move(self) -> str:
        return "飞翔"

class Fish(Animal):
    """鱼类"""
    
    @property
    def species(self) -> str:
        return "鱼"
    
    def make_sound(self) -> str:
        return "咕噜咕噜!"
    
    def move(self) -> str:
        return "游泳"

# 动物类型枚举
class AnimalType(Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"
    FISH = "fish"

# 简单工厂
class AnimalFactory:
    """动物工厂"""
    
    # 注册表
    _animals: Dict[AnimalType, Type[Animal]] = {
        AnimalType.DOG: Dog,
        AnimalType.CAT: Cat,
        AnimalType.BIRD: Bird,
        AnimalType.FISH: Fish
    }
    
    @classmethod
    def create_animal(cls, animal_type: AnimalType) -> Animal:
        """创建动物对象"""
        if animal_type not in cls._animals:
            raise ValueError(f"不支持的动物类型: {animal_type}")
        
        animal_class = cls._animals[animal_type]
        return animal_class()
    
    @classmethod
    def register_animal(cls, animal_type: AnimalType, animal_class: Type[Animal]):
        """注册新的动物类型"""
        cls._animals[animal_type] = animal_class
    
    @classmethod
    def get_supported_types(cls) -> List[AnimalType]:
        """获取支持的动物类型"""
        return list(cls._animals.keys())

# 抽象工厂模式
class VehicleFactory(ABC):
    """交通工具抽象工厂"""
    
    @abstractmethod
    def create_car(self) -> 'Car':
        """创建汽车"""
        pass
    
    @abstractmethod
    def create_motorcycle(self) -> 'Motorcycle':
        """创建摩托车"""
        pass

# 交通工具接口
class Vehicle(ABC):
    """交通工具抽象基类"""
    
    @abstractmethod
    def start_engine(self) -> str:
        """启动引擎"""
        pass
    
    @abstractmethod
    def get_info(self) -> str:
        """获取信息"""
        pass

class Car(Vehicle):
    """汽车抽象基类"""
    pass

class Motorcycle(Vehicle):
    """摩托车抽象基类"""
    pass

# 具体产品 - 德国车系
class GermanCar(Car):
    """德国汽车"""
    
    def start_engine(self) -> str:
        return "德国汽车引擎启动: 精密而安静"
    
    def get_info(self) -> str:
        return "德国汽车: 工艺精良，性能卓越"

class GermanMotorcycle(Motorcycle):
    """德国摩托车"""
    
    def start_engine(self) -> str:
        return "德国摩托车引擎启动: 强劲有力"
    
    def get_info(self) -> str:
        return "德国摩托车: 技术先进，操控精准"

# 具体产品 - 日本车系
class JapaneseCar(Car):
    """日本汽车"""
    
    def start_engine(self) -> str:
        return "日本汽车引擎启动: 经济省油"
    
    def get_info(self) -> str:
        return "日本汽车: 可靠耐用，燃油经济"

class JapaneseMotorcycle(Motorcycle):
    """日本摩托车"""
    
    def start_engine(self) -> str:
        return "日本摩托车引擎启动: 平稳顺畅"
    
    def get_info(self) -> str:
        return "日本摩托车: 质量可靠，维护简单"

# 具体工厂
class GermanVehicleFactory(VehicleFactory):
    """德国交通工具工厂"""
    
    def create_car(self) -> Car:
        return GermanCar()
    
    def create_motorcycle(self) -> Motorcycle:
        return GermanMotorcycle()

class JapaneseVehicleFactory(VehicleFactory):
    """日本交通工具工厂"""
    
    def create_car(self) -> Car:
        return JapaneseCar()
    
    def create_motorcycle(self) -> Motorcycle:
        return JapaneseMotorcycle()

# 演示工厂模式
def demonstrate_factory_pattern():
    """演示工厂模式"""
    print("=== 工厂模式演示 ===")
    
    # 简单工厂模式演示
    print("1. 简单工厂模式:")
    
    # 创建不同类型的动物
    animal_types = [AnimalType.DOG, AnimalType.CAT, AnimalType.BIRD, AnimalType.FISH]
    
    for animal_type in animal_types:
        animal = AnimalFactory.create_animal(animal_type)
        print(f"   创建了{animal.species}: {animal.make_sound()} 移动方式: {animal.move()}")
    
    print(f"\n   支持的动物类型: {[t.value for t in AnimalFactory.get_supported_types()]}")
    
    # 抽象工厂模式演示
    print("\n2. 抽象工厂模式:")
    
    # 创建不同国家的交通工具工厂
    factories = [
        ("德国", GermanVehicleFactory()),
        ("日本", JapaneseVehicleFactory())
    ]
    
    for country, factory in factories:
        print(f"\n   {country}工厂生产的交通工具:")
        
        # 创建汽车
        car = factory.create_car()
        print(f"     汽车: {car.get_info()}")
        print(f"     启动: {car.start_engine()}")
        
        # 创建摩托车
        motorcycle = factory.create_motorcycle()
        print(f"     摩托车: {motorcycle.get_info()}")
        print(f"     启动: {motorcycle.start_engine()}")
    
    print("\n=== 工厂模式演示完成 ===\n")

demonstrate_factory_pattern()
```

## 观察者模式 (Observer Pattern)

观察者模式定义了一种一对多的依赖关系，让多个观察者对象同时监听某一个主题对象。这个主题对象在状态发生变化时，会通知所有观察者对象，使它们能够自动更新自己。

### 基本实现

```python
from abc import ABC, abstractmethod
from typing import List, Any
from datetime import datetime
import random

# 观察者接口
class Observer(ABC):
    """观察者抽象基类"""
    
    @abstractmethod
    def update(self, subject: 'Subject', *args, **kwargs):
        """更新方法"""
        pass

# 主题接口
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
    
    def notify(self, *args, **kwargs):
        """通知所有观察者"""
        for observer in self._observers:
            observer.update(self, *args, **kwargs)
    
    def get_observer_count(self) -> int:
        """获取观察者数量"""
        return len(self._observers)

# 具体主题 - 股票价格
class Stock(Subject):
    """股票类"""
    
    def __init__(self, symbol: str, price: float):
        super().__init__()
        self._symbol = symbol
        self._price = price
        self._history = [(datetime.now(), price)]
    
    @property
    def symbol(self) -> str:
        return self._symbol
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, new_price: float):
        if new_price != self._price:
            old_price = self._price
            self._price = new_price
            self._history.append((datetime.now(), new_price))
            
            # 通知观察者价格变化
            self.notify(
                event_type="price_change",
                old_price=old_price,
                new_price=new_price,
                change=new_price - old_price,
                change_percent=(new_price - old_price) / old_price * 100
            )
    
    def get_history(self) -> List[tuple]:
        """获取价格历史"""
        return self._history.copy()
    
    def simulate_price_change(self):
        """模拟价格变化"""
        # 随机变化 -5% 到 +5%
        change_percent = random.uniform(-0.05, 0.05)
        new_price = self._price * (1 + change_percent)
        self.price = round(new_price, 2)

# 具体观察者 - 投资者
class Investor(Observer):
    """投资者类"""
    
    def __init__(self, name: str):
        self.name = name
        self.portfolio = {}  # 持仓信息
    
    def update(self, subject: Subject, *args, **kwargs):
        """接收股票价格更新"""
        if isinstance(subject, Stock):
            event_type = kwargs.get('event_type')
            
            if event_type == 'price_change':
                old_price = kwargs.get('old_price')
                new_price = kwargs.get('new_price')
                change = kwargs.get('change')
                change_percent = kwargs.get('change_percent')
                
                print(f"[投资者 {self.name}] 收到 {subject.symbol} 价格更新:")
                print(f"  价格: {old_price:.2f} -> {new_price:.2f} (变化: {change:+.2f}, {change_percent:+.2f}%)")
                
                # 根据价格变化做出投资决策
                self._make_investment_decision(subject, change_percent)
    
    def _make_investment_decision(self, stock: Stock, change_percent: float):
        """根据价格变化做投资决策"""
        if change_percent > 3:
            print(f"  -> {self.name} 考虑卖出 {stock.symbol}")
        elif change_percent < -3:
            print(f"  -> {self.name} 考虑买入 {stock.symbol}")
        else:
            print(f"  -> {self.name} 继续观望 {stock.symbol}")
    
    def buy_stock(self, stock: Stock, shares: int):
        """买入股票"""
        if stock.symbol not in self.portfolio:
            self.portfolio[stock.symbol] = 0
        self.portfolio[stock.symbol] += shares
        print(f"{self.name} 买入 {shares} 股 {stock.symbol}")
    
    def sell_stock(self, stock: Stock, shares: int):
        """卖出股票"""
        if stock.symbol in self.portfolio and self.portfolio[stock.symbol] >= shares:
            self.portfolio[stock.symbol] -= shares
            print(f"{self.name} 卖出 {shares} 股 {stock.symbol}")
        else:
            print(f"{self.name} 持仓不足，无法卖出 {shares} 股 {stock.symbol}")

# 具体观察者 - 交易系统
class TradingSystem(Observer):
    """交易系统类"""
    
    def __init__(self, name: str):
        self.name = name
        self.alerts = []
    
    def update(self, subject: Subject, *args, **kwargs):
        """接收股票价格更新"""
        if isinstance(subject, Stock):
            event_type = kwargs.get('event_type')
            
            if event_type == 'price_change':
                new_price = kwargs.get('new_price')
                change_percent = kwargs.get('change_percent')
                
                # 检查是否需要发出警报
                if abs(change_percent) > 5:
                    alert = f"[{self.name}] 警报: {subject.symbol} 价格剧烈波动 {change_percent:+.2f}%"
                    self.alerts.append(alert)
                    print(alert)
                
                # 记录交易数据
                self._log_trade_data(subject, new_price, change_percent)
    
    def _log_trade_data(self, stock: Stock, price: float, change_percent: float):
        """记录交易数据"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{self.name}] 记录: {timestamp} - {stock.symbol}: {price:.2f} ({change_percent:+.2f}%)")
    
    def get_alerts(self) -> List[str]:
        """获取所有警报"""
        return self.alerts.copy()

# 具体观察者 - 新闻系统
class NewsSystem(Observer):
    """新闻系统类"""
    
    def __init__(self):
        self.news_items = []
    
    def update(self, subject: Subject, *args, **kwargs):
        """接收股票价格更新"""
        if isinstance(subject, Stock):
            event_type = kwargs.get('event_type')
            
            if event_type == 'price_change':
                change_percent = kwargs.get('change_percent')
                
                # 生成新闻
                if abs(change_percent) > 2:
                    news = self._generate_news(subject, change_percent)
                    self.news_items.append(news)
                    print(f"[新闻系统] 发布: {news}")
    
    def _generate_news(self, stock: Stock, change_percent: float) -> str:
        """生成新闻"""
        direction = "上涨" if change_percent > 0 else "下跌"
        magnitude = "大幅" if abs(change_percent) > 5 else "小幅" if abs(change_percent) < 3 else "明显"
        
        return f"{stock.symbol} 股价{magnitude}{direction} {abs(change_percent):.2f}%，当前价格 {stock.price:.2f}"
    
    def get_news(self) -> List[str]:
        """获取所有新闻"""
        return self.news_items.copy()

# 演示观察者模式
def demonstrate_observer_pattern():
    """演示观察者模式"""
    print("=== 观察者模式演示 ===")
    
    # 创建股票
    apple_stock = Stock("AAPL", 150.00)
    google_stock = Stock("GOOGL", 2800.00)
    
    # 创建观察者
    investor1 = Investor("张三")
    investor2 = Investor("李四")
    trading_system = TradingSystem("华尔街交易系统")
    news_system = NewsSystem()
    
    # 注册观察者
    print("1. 注册观察者:")
    apple_stock.attach(investor1)
    apple_stock.attach(investor2)
    apple_stock.attach(trading_system)
    apple_stock.attach(news_system)
    
    google_stock.attach(investor1)  # 张三也关注谷歌股票
    google_stock.attach(trading_system)
    google_stock.attach(news_system)
    
    print(f"   AAPL 观察者数量: {apple_stock.get_observer_count()}")
    print(f"   GOOGL 观察者数量: {google_stock.get_observer_count()}")
    
    # 模拟股票价格变化
    print("\n2. 模拟股票价格变化:")
    
    print("\n--- 第一轮价格变化 ---")
    apple_stock.simulate_price_change()
    
    print("\n--- 第二轮价格变化 ---")
    google_stock.simulate_price_change()
    
    print("\n--- 第三轮价格变化 ---")
    apple_stock.simulate_price_change()
    
    # 手动设置大幅价格变化
    print("\n--- 手动设置大幅价格变化 ---")
    apple_stock.price = 160.50  # 大幅上涨
    
    print("\n--- 再次大幅变化 ---")
    google_stock.price = 2650.00  # 大幅下跌
    
    # 移除观察者
    print("\n3. 移除观察者:")
    apple_stock.detach(investor2)
    print(f"   移除李四后，AAPL 观察者数量: {apple_stock.get_observer_count()}")
    
    print("\n--- 移除观察者后的价格变化 ---")
    apple_stock.price = 155.75
    
    # 显示统计信息
    print("\n4. 统计信息:")
    print(f"   交易系统警报数量: {len(trading_system.get_alerts())}")
    print(f"   新闻系统新闻数量: {len(news_system.get_news())}")
    
    print("\n   最新新闻:")
    for news in news_system.get_news()[-3:]:  # 显示最新3条新闻
        print(f"     - {news}")
    
    print("\n=== 观察者模式演示完成 ===\n")

demonstrate_observer_pattern()
```

## 模板方法模式 (Template Method Pattern)

模板方法模式在一个方法中定义一个算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以在不改变算法结构的情况下，重新定义算法中的某些步骤。

### 基本实现

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any
import time
import random

# 抽象模板类
class DataProcessor(ABC):
    """数据处理模板类"""
    
    def process_data(self, data_source: str) -> Dict[str, Any]:
        """模板方法 - 定义数据处理的算法骨架"""
        print(f"开始处理数据源: {data_source}")
        
        # 1. 读取数据
        raw_data = self.read_data(data_source)
        print(f"读取到 {len(raw_data)} 条原始数据")
        
        # 2. 验证数据
        if self.validate_data(raw_data):
            print("数据验证通过")
        else:
            print("数据验证失败")
            return {"status": "failed", "reason": "数据验证失败"}
        
        # 3. 清洗数据
        cleaned_data = self.clean_data(raw_data)
        print(f"数据清洗完成，剩余 {len(cleaned_data)} 条有效数据")
        
        # 4. 转换数据
        transformed_data = self.transform_data(cleaned_data)
        print(f"数据转换完成")
        
        # 5. 保存数据（可选步骤）
        if self.should_save_data():
            self.save_data(transformed_data)
            print("数据已保存")
        
        # 6. 生成报告
        report = self.generate_report(transformed_data)
        
        print("数据处理完成")
        return {
            "status": "success",
            "processed_count": len(transformed_data),
            "report": report
        }
    
    # 抽象方法 - 子类必须实现
    @abstractmethod
    def read_data(self, source: str) -> List[Dict[str, Any]]:
        """读取数据"""
        pass
    
    @abstractmethod
    def clean_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """清洗数据"""
        pass
    
    @abstractmethod
    def transform_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """转换数据"""
        pass
    
    # 钩子方法 - 子类可以选择性重写
    def validate_data(self, data: List[Dict[str, Any]]) -> bool:
        """验证数据 - 默认实现"""
        return len(data) > 0
    
    def should_save_data(self) -> bool:
        """是否应该保存数据 - 钩子方法"""
        return True
    
    def save_data(self, data: List[Dict[str, Any]]):
        """保存数据 - 默认实现"""
        print(f"使用默认方式保存 {len(data)} 条数据")
    
    def generate_report(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """生成报告 - 默认实现"""
        return {
            "total_records": len(data),
            "processing_time": time.time()
        }

# 具体实现类 - CSV数据处理器
class CSVDataProcessor(DataProcessor):
    """CSV数据处理器"""
    
    def read_data(self, source: str) -> List[Dict[str, Any]]:
        """读取CSV数据"""
        print(f"从CSV文件读取数据: {source}")
        # 模拟读取CSV数据
        return [
            {"id": i, "name": f"用户{i}", "age": random.randint(18, 80), "score": random.randint(0, 100)}
            for i in range(1, random.randint(50, 100))
        ]
    
    def validate_data(self, data: List[Dict[str, Any]]) -> bool:
        """验证CSV数据"""
        # 检查必要字段
        required_fields = ["id", "name", "age", "score"]
        for record in data:
            if not all(field in record for field in required_fields):
                return False
        return True
    
    def clean_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """清洗CSV数据"""
        cleaned = []
        for record in data:
            # 过滤无效数据
            if (record["age"] > 0 and record["age"] < 120 and 
                record["score"] >= 0 and record["score"] <= 100 and
                record["name"].strip()):
                cleaned.append(record)
        return cleaned
    
    def transform_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """转换CSV数据"""
        transformed = []
        for record in data:
            # 添加等级字段
            if record["score"] >= 90:
                grade = "A"
            elif record["score"] >= 80:
                grade = "B"
            elif record["score"] >= 70:
                grade = "C"
            elif record["score"] >= 60:
                grade = "D"
            else:
                grade = "F"
            
            # 添加年龄组
            if record["age"] < 30:
                age_group = "青年"
            elif record["age"] < 60:
                age_group = "中年"
            else:
                age_group = "老年"
            
            transformed_record = record.copy()
            transformed_record["grade"] = grade
            transformed_record["age_group"] = age_group
            transformed.append(transformed_record)
        
        return transformed
    
    def save_data(self, data: List[Dict[str, Any]]):
        """保存到CSV文件"""
        print(f"保存 {len(data)} 条数据到CSV文件")
    
    def generate_report(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """生成CSV处理报告"""
        # 统计各等级人数
        grade_count = {}
        age_group_count = {}
        total_score = 0
        
        for record in data:
            grade = record["grade"]
            age_group = record["age_group"]
            
            grade_count[grade] = grade_count.get(grade, 0) + 1
            age_group_count[age_group] = age_group_count.get(age_group, 0) + 1
            total_score += record["score"]
        
        return {
            "total_records": len(data),
            "average_score": total_score / len(data) if data else 0,
            "grade_distribution": grade_count,
            "age_group_distribution": age_group_count,
            "processing_time": time.time()
        }

# 具体实现类 - JSON数据处理器
class JSONDataProcessor(DataProcessor):
    """JSON数据处理器"""
    
    def read_data(self, source: str) -> List[Dict[str, Any]]:
        """读取JSON数据"""
        print(f"从JSON文件读取数据: {source}")
        # 模拟读取JSON数据
        return [
            {
                "user_id": i, 
                "username": f"user_{i}", 
                "email": f"user{i}@example.com",
                "profile": {
                    "age": random.randint(18, 80),
                    "city": random.choice(["北京", "上海", "广州", "深圳"]),
                    "interests": random.sample(["编程", "音乐", "运动", "阅读", "旅游"], 2)
                },
                "activity_score": random.randint(0, 1000)
            }
            for i in range(1, random.randint(30, 80))
        ]
    
    def validate_data(self, data: List[Dict[str, Any]]) -> bool:
        """验证JSON数据"""
        required_fields = ["user_id", "username", "email", "profile", "activity_score"]
        for record in data:
            if not all(field in record for field in required_fields):
                return False
            if "age" not in record["profile"] or "city" not in record["profile"]:
                return False
        return True
    
    def clean_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """清洗JSON数据"""
        cleaned = []
        for record in data:
            # 过滤无效数据
            if (record["profile"]["age"] > 0 and 
                record["activity_score"] >= 0 and
                "@" in record["email"] and
                record["username"].strip()):
                cleaned.append(record)
        return cleaned
    
    def transform_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """转换JSON数据"""
        transformed = []
        for record in data:
            # 扁平化数据结构
            flat_record = {
                "user_id": record["user_id"],
                "username": record["username"],
                "email": record["email"],
                "age": record["profile"]["age"],
                "city": record["profile"]["city"],
                "interests_count": len(record["profile"].get("interests", [])),
                "activity_score": record["activity_score"]
            }
            
            # 添加活跃度等级
            if record["activity_score"] >= 800:
                flat_record["activity_level"] = "高度活跃"
            elif record["activity_score"] >= 500:
                flat_record["activity_level"] = "中度活跃"
            elif record["activity_score"] >= 200:
                flat_record["activity_level"] = "低度活跃"
            else:
                flat_record["activity_level"] = "不活跃"
            
            transformed.append(flat_record)
        
        return transformed
    
    def should_save_data(self) -> bool:
        """JSON处理器选择不自动保存"""
        return False
    
    def generate_report(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """生成JSON处理报告"""
        # 统计城市分布和活跃度分布
        city_count = {}
        activity_level_count = {}
        total_activity_score = 0
        
        for record in data:
            city = record["city"]
            activity_level = record["activity_level"]
            
            city_count[city] = city_count.get(city, 0) + 1
            activity_level_count[activity_level] = activity_level_count.get(activity_level, 0) + 1
            total_activity_score += record["activity_score"]
        
        return {
            "total_records": len(data),
            "average_activity_score": total_activity_score / len(data) if data else 0,
            "city_distribution": city_count,
            "activity_level_distribution": activity_level_count,
            "processing_time": time.time()
        }

# 具体实现类 - 数据库数据处理器
class DatabaseDataProcessor(DataProcessor):
    """数据库数据处理器"""
    
    def read_data(self, source: str) -> List[Dict[str, Any]]:
        """从数据库读取数据"""
        print(f"从数据库读取数据: {source}")
        # 模拟从数据库读取数据
        return [
            {
                "order_id": i,
                "customer_id": random.randint(1, 1000),
                "product_name": random.choice(["笔记本电脑", "手机", "平板", "耳机", "键盘"]),
                "quantity": random.randint(1, 5),
                "unit_price": random.uniform(100, 5000),
                "order_date": f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
                "status": random.choice(["pending", "completed", "cancelled", "shipped"])
            }
            for i in range(1, random.randint(100, 200))
        ]
    
    def validate_data(self, data: List[Dict[str, Any]]) -> bool:
        """验证数据库数据"""
        required_fields = ["order_id", "customer_id", "product_name", "quantity", "unit_price"]
        for record in data:
            if not all(field in record for field in required_fields):
                return False
            if record["quantity"] <= 0 or record["unit_price"] <= 0:
                return False
        return True
    
    def clean_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """清洗数据库数据"""
        cleaned = []
        for record in data:
            # 只保留已完成和已发货的订单
            if record["status"] in ["completed", "shipped"]:
                cleaned.append(record)
        return cleaned
    
    def transform_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """转换数据库数据"""
        transformed = []
        for record in data:
            # 计算总价
            total_price = record["quantity"] * record["unit_price"]
            
            # 添加订单类型
            if total_price >= 5000:
                order_type = "大额订单"
            elif total_price >= 1000:
                order_type = "中额订单"
            else:
                order_type = "小额订单"
            
            transformed_record = record.copy()
            transformed_record["total_price"] = round(total_price, 2)
            transformed_record["order_type"] = order_type
            transformed.append(transformed_record)
        
        return transformed
    
    def save_data(self, data: List[Dict[str, Any]]):
        """保存到数据仓库"""
        print(f"保存 {len(data)} 条数据到数据仓库")
    
    def generate_report(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """生成数据库处理报告"""
        # 统计订单类型和产品销量
        order_type_count = {}
        product_sales = {}
        total_revenue = 0
        
        for record in data:
            order_type = record["order_type"]
            product_name = record["product_name"]
            quantity = record["quantity"]
            total_price = record["total_price"]
            
            order_type_count[order_type] = order_type_count.get(order_type, 0) + 1
            product_sales[product_name] = product_sales.get(product_name, 0) + quantity
            total_revenue += total_price
        
        return {
            "total_records": len(data),
            "total_revenue": round(total_revenue, 2),
            "average_order_value": round(total_revenue / len(data), 2) if data else 0,
            "order_type_distribution": order_type_count,
            "product_sales": product_sales,
            "processing_time": time.time()
        }

# 演示模板方法模式
def demonstrate_template_method_pattern():
    """演示模板方法模式"""
    print("=== 模板方法模式演示 ===")
    
    # 创建不同类型的数据处理器
    processors = [
        ("CSV数据处理器", CSVDataProcessor(), "students.csv"),
        ("JSON数据处理器", JSONDataProcessor(), "users.json"),
        ("数据库数据处理器", DatabaseDataProcessor(), "orders_table")
    ]
    
    # 使用相同的模板方法处理不同类型的数据
    for name, processor, data_source in processors:
        print(f"\n{'='*50}")
        print(f"使用 {name} 处理数据")
        print(f"{'='*50}")
        
        # 调用模板方法
        result = processor.process_data(data_source)
        
        # 显示处理结果
        print(f"\n处理结果: {result['status']}")
        if result['status'] == 'success':
            print(f"处理记录数: {result['processed_count']}")
            
            # 显示报告详情
            report = result['report']
            print("\n详细报告:")
            for key, value in report.items():
                if key != 'processing_time':
                    print(f"  {key}: {value}")
        
        print("\n" + "-"*50)
    
    print("\n=== 模板方法模式演示完成 ===\n")

demonstrate_template_method_pattern()
```

## 设计模式中的多态性总结

```python
def demonstrate_polymorphism_in_design_patterns():
    """演示设计模式中的多态性"""
    print("=== 设计模式中的多态性总结 ===")
    
    print("1. 策略模式中的多态性:")
    print("   - 不同的策略类实现相同的接口")
    print("   - 客户端可以透明地切换不同的算法")
    print("   - 运行时动态选择具体的实现")
    
    print("\n2. 工厂模式中的多态性:")
    print("   - 工厂方法返回抽象产品类型")
    print("   - 客户端通过统一接口使用不同的具体产品")
    print("   - 隐藏了具体产品的创建细节")
    
    print("\n3. 观察者模式中的多态性:")
    print("   - 不同的观察者实现相同的更新接口")
    print("   - 主题对象可以通知任意类型的观察者")
    print("   - 支持动态添加和移除观察者")
    
    print("\n4. 模板方法模式中的多态性:")
    print("   - 抽象类定义算法骨架")
    print("   - 子类重写特定步骤的实现")
    print("   - 相同的模板方法调用不同的具体实现")
    
    print("\n5. 多态设计模式的核心要点:")
    print("   - 面向接口编程，而不是面向实现")
    print("   - 使用抽象基类或接口定义契约")
    print("   - 通过继承和重写实现多态行为")
    print("   - 提高代码的可扩展性和可维护性")
    print("   - 支持开闭原则：对扩展开放，对修改关闭")
    
    print("\n6. 实际应用建议:")
    print("   - 识别变化点，使用多态封装变化")
    print("   - 优先使用组合而不是继承")
    print("   - 保持接口简单和稳定")
    print("   - 合理使用设计模式，避免过度设计")
    
    print("\n=== 总结完成 ===\n")

demonstrate_polymorphism_in_design_patterns()
```

## 总结

设计模式是多态性的重要应用场景，通过合理运用设计模式，我们可以：

1. **提高代码的可扩展性**：新增功能时无需修改现有代码
2. **降低代码耦合度**：组件之间通过接口交互
3. **提高代码复用性**：相同的接口可以有多种实现
4. **简化系统维护**：修改实现不影响客户端代码

### 关键设计原则：

- **开闭原则**：对扩展开放，对修改关闭
- **里氏替换原则**：子类可以替换父类
- **依赖倒置原则**：依赖抽象而不是具体实现
- **接口隔离原则**：使用多个专门的接口
- **单一职责原则**：每个类只有一个变化的原因

掌握这些设计模式和多态性的应用，能帮助你设计出更加灵活、可维护的软件系统。