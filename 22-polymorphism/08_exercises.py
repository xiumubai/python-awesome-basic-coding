#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多态练习题 - Polymorphism Exercises

本文件包含多态相关的练习题，从基础到高级，帮助巩固多态的概念和应用。
每个练习都包含题目描述、解答和详细说明。

学习目标：
1. 巩固多态的基本概念
2. 练习方法重写和抽象类
3. 掌握设计模式的应用
4. 提高面向对象编程能力
5. 学会解决实际问题
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import random
import time
from datetime import datetime


# ============================================================================
# 练习1：基础多态 - 图形计算系统
# ============================================================================

print("=== 练习1：图形计算系统 ===")
print("题目：创建一个图形计算系统，支持不同类型的图形（圆形、矩形、三角形）")
print("要求：使用多态实现统一的面积和周长计算接口")

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
    
    def info(self) -> str:
        """获取图形信息"""
        return f"{self.name}: 面积={self.area():.2f}, 周长={self.perimeter():.2f}"


class Circle(Shape):
    """圆形"""
    
    def __init__(self, radius: float):
        super().__init__("圆形")
        self.radius = radius
    
    def area(self) -> float:
        return 3.14159 * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    """矩形"""
    
    def __init__(self, width: float, height: float):
        super().__init__("矩形")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Triangle(Shape):
    """三角形"""
    
    def __init__(self, a: float, b: float, c: float):
        super().__init__("三角形")
        self.a = a
        self.b = b
        self.c = c
    
    def area(self) -> float:
        # 使用海伦公式
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c


def exercise1_demo():
    """练习1演示"""
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5)
    ]
    
    print("\n图形计算结果:")
    total_area = 0
    for shape in shapes:
        print(shape.info())
        total_area += shape.area()
    
    print(f"\n总面积: {total_area:.2f}")
    print("解答说明：通过抽象基类定义统一接口，各子类实现具体计算逻辑")


# ============================================================================
# 练习2：策略模式 - 排序算法比较
# ============================================================================

print("\n=== 练习2：排序算法比较 ===")
print("题目：实现一个排序算法比较器，支持多种排序算法")
print("要求：使用策略模式，能够动态切换排序算法并比较性能")

class SortStrategy(ABC):
    """排序策略接口"""
    
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        """排序方法"""
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """获取算法名称"""
        pass


class BubbleSort(SortStrategy):
    """冒泡排序"""
    
    def sort(self, data: List[int]) -> List[int]:
        result = data.copy()
        n = len(result)
        for i in range(n):
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result
    
    def get_name(self) -> str:
        return "冒泡排序"


class SelectionSort(SortStrategy):
    """选择排序"""
    
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
    
    def get_name(self) -> str:
        return "选择排序"


class InsertionSort(SortStrategy):
    """插入排序"""
    
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
    
    def get_name(self) -> str:
        return "插入排序"


class SortComparator:
    """排序比较器"""
    
    def __init__(self):
        self.strategies = [
            BubbleSort(),
            SelectionSort(),
            InsertionSort()
        ]
    
    def compare_algorithms(self, data: List[int]):
        """比较不同算法的性能"""
        print(f"\n原始数据: {data}")
        print("算法性能比较:")
        
        results = []
        for strategy in self.strategies:
            start_time = time.time()
            sorted_data = strategy.sort(data)
            end_time = time.time()
            
            execution_time = (end_time - start_time) * 1000  # 转换为毫秒
            results.append({
                'name': strategy.get_name(),
                'time': execution_time,
                'result': sorted_data
            })
            
            print(f"{strategy.get_name()}: {execution_time:.4f}ms")
        
        # 找出最快的算法
        fastest = min(results, key=lambda x: x['time'])
        print(f"\n最快算法: {fastest['name']} ({fastest['time']:.4f}ms)")
        print(f"排序结果: {fastest['result']}")
        
        return results


def exercise2_demo():
    """练习2演示"""
    comparator = SortComparator()
    test_data = [64, 34, 25, 12, 22, 11, 90, 5]
    comparator.compare_algorithms(test_data)
    print("解答说明：策略模式允许在运行时选择算法，便于性能比较和算法切换")


# ============================================================================
# 练习3：工厂模式 - 数据库连接器
# ============================================================================

print("\n=== 练习3：数据库连接器 ===")
print("题目：创建一个数据库连接器工厂，支持不同类型的数据库")
print("要求：使用工厂模式和多态，实现统一的数据库操作接口")

class DatabaseConnection(ABC):
    """数据库连接抽象基类"""
    
    def __init__(self, host: str, port: int, database: str):
        self.host = host
        self.port = port
        self.database = database
        self.connected = False
    
    @abstractmethod
    def connect(self) -> bool:
        """连接数据库"""
        pass
    
    @abstractmethod
    def execute_query(self, query: str) -> List[Dict]:
        """执行查询"""
        pass
    
    @abstractmethod
    def close(self):
        """关闭连接"""
        pass
    
    @abstractmethod
    def get_db_type(self) -> str:
        """获取数据库类型"""
        pass


class MySQLConnection(DatabaseConnection):
    """MySQL连接"""
    
    def connect(self) -> bool:
        print(f"连接到MySQL数据库: {self.host}:{self.port}/{self.database}")
        self.connected = True
        return True
    
    def execute_query(self, query: str) -> List[Dict]:
        if not self.connected:
            raise Exception("数据库未连接")
        print(f"执行MySQL查询: {query}")
        # 模拟查询结果
        return [{"id": 1, "name": "MySQL数据", "type": "mysql"}]
    
    def close(self):
        if self.connected:
            print("关闭MySQL连接")
            self.connected = False
    
    def get_db_type(self) -> str:
        return "MySQL"


class PostgreSQLConnection(DatabaseConnection):
    """PostgreSQL连接"""
    
    def connect(self) -> bool:
        print(f"连接到PostgreSQL数据库: {self.host}:{self.port}/{self.database}")
        self.connected = True
        return True
    
    def execute_query(self, query: str) -> List[Dict]:
        if not self.connected:
            raise Exception("数据库未连接")
        print(f"执行PostgreSQL查询: {query}")
        # 模拟查询结果
        return [{"id": 1, "name": "PostgreSQL数据", "type": "postgresql"}]
    
    def close(self):
        if self.connected:
            print("关闭PostgreSQL连接")
            self.connected = False
    
    def get_db_type(self) -> str:
        return "PostgreSQL"


class SQLiteConnection(DatabaseConnection):
    """SQLite连接"""
    
    def connect(self) -> bool:
        print(f"连接到SQLite数据库: {self.database}")
        self.connected = True
        return True
    
    def execute_query(self, query: str) -> List[Dict]:
        if not self.connected:
            raise Exception("数据库未连接")
        print(f"执行SQLite查询: {query}")
        # 模拟查询结果
        return [{"id": 1, "name": "SQLite数据", "type": "sqlite"}]
    
    def close(self):
        if self.connected:
            print("关闭SQLite连接")
            self.connected = False
    
    def get_db_type(self) -> str:
        return "SQLite"


class DatabaseFactory:
    """数据库工厂"""
    
    @staticmethod
    def create_connection(db_type: str, host: str = "localhost", 
                         port: int = 3306, database: str = "test") -> DatabaseConnection:
        """创建数据库连接"""
        db_type = db_type.lower()
        
        if db_type == "mysql":
            return MySQLConnection(host, port, database)
        elif db_type == "postgresql":
            return PostgreSQLConnection(host, port, database)
        elif db_type == "sqlite":
            return SQLiteConnection(host, port, database)
        else:
            raise ValueError(f"不支持的数据库类型: {db_type}")
    
    @staticmethod
    def get_supported_types() -> List[str]:
        """获取支持的数据库类型"""
        return ["mysql", "postgresql", "sqlite"]


class DatabaseManager:
    """数据库管理器"""
    
    def __init__(self):
        self.connections: Dict[str, DatabaseConnection] = {}
    
    def add_connection(self, name: str, db_type: str, **kwargs):
        """添加数据库连接"""
        connection = DatabaseFactory.create_connection(db_type, **kwargs)
        connection.connect()
        self.connections[name] = connection
        print(f"添加连接: {name} ({connection.get_db_type()})")
    
    def execute_on_all(self, query: str):
        """在所有数据库上执行查询"""
        print(f"\n在所有数据库上执行查询: {query}")
        results = {}
        for name, connection in self.connections.items():
            try:
                result = connection.execute_query(query)
                results[name] = result
                print(f"{name} ({connection.get_db_type()}): 查询成功")
            except Exception as e:
                print(f"{name}: 查询失败 - {e}")
        return results
    
    def close_all(self):
        """关闭所有连接"""
        print("\n关闭所有数据库连接:")
        for name, connection in self.connections.items():
            connection.close()
            print(f"已关闭: {name}")
        self.connections.clear()


def exercise3_demo():
    """练习3演示"""
    print(f"\n支持的数据库类型: {DatabaseFactory.get_supported_types()}")
    
    # 创建数据库管理器
    manager = DatabaseManager()
    
    # 添加不同类型的数据库连接
    manager.add_connection("主数据库", "mysql", host="localhost", port=3306, database="main")
    manager.add_connection("分析数据库", "postgresql", host="localhost", port=5432, database="analytics")
    manager.add_connection("缓存数据库", "sqlite", database="cache.db")
    
    # 在所有数据库上执行查询
    manager.execute_on_all("SELECT * FROM users")
    
    # 关闭所有连接
    manager.close_all()
    
    print("解答说明：工厂模式隐藏对象创建细节，多态提供统一的操作接口")


# ============================================================================
# 练习4：观察者模式 - 股票价格监控系统
# ============================================================================

print("\n=== 练习4：股票价格监控系统 ===")
print("题目：创建一个股票价格监控系统，当价格变化时通知所有观察者")
print("要求：使用观察者模式，支持多种类型的通知方式")

class Observer(ABC):
    """观察者接口"""
    
    @abstractmethod
    def update(self, stock_symbol: str, price: float, change: float):
        """接收价格更新通知"""
        pass


class Stock:
    """股票类（被观察者）"""
    
    def __init__(self, symbol: str, price: float):
        self.symbol = symbol
        self._price = price
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        """添加观察者"""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"观察者已添加到 {self.symbol}")
    
    def detach(self, observer: Observer):
        """移除观察者"""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"观察者已从 {self.symbol} 移除")
    
    def notify(self, change: float):
        """通知所有观察者"""
        for observer in self._observers:
            observer.update(self.symbol, self._price, change)
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, new_price: float):
        old_price = self._price
        self._price = new_price
        change = new_price - old_price
        print(f"\n{self.symbol} 价格更新: {old_price:.2f} -> {new_price:.2f} (变化: {change:+.2f})")
        self.notify(change)


class EmailNotifier(Observer):
    """邮件通知器"""
    
    def __init__(self, email: str):
        self.email = email
    
    def update(self, stock_symbol: str, price: float, change: float):
        direction = "上涨" if change > 0 else "下跌" if change < 0 else "持平"
        print(f"📧 邮件通知 ({self.email}): {stock_symbol} {direction} {abs(change):.2f}, 当前价格: {price:.2f}")


class SMSNotifier(Observer):
    """短信通知器"""
    
    def __init__(self, phone: str):
        self.phone = phone
    
    def update(self, stock_symbol: str, price: float, change: float):
        if abs(change) > 5:  # 只有变化超过5元才发送短信
            direction = "📈" if change > 0 else "📉"
            print(f"📱 短信通知 ({self.phone}): {direction} {stock_symbol} 大幅变动 {change:+.2f}, 价格: {price:.2f}")


class AlertSystem(Observer):
    """警报系统"""
    
    def __init__(self, threshold: float):
        self.threshold = threshold
    
    def update(self, stock_symbol: str, price: float, change: float):
        if abs(change) > self.threshold:
            alert_type = "🚨 涨停警报" if change > 0 else "⚠️ 跌停警报"
            print(f"{alert_type}: {stock_symbol} 变动 {change:+.2f} 超过阈值 {self.threshold}")


class TradingBot(Observer):
    """交易机器人"""
    
    def __init__(self, name: str):
        self.name = name
        self.portfolio = {}
    
    def update(self, stock_symbol: str, price: float, change: float):
        # 简单的交易策略
        if change > 3:
            action = "卖出"
            reason = "价格上涨，获利了结"
        elif change < -3:
            action = "买入"
            reason = "价格下跌，抄底机会"
        else:
            return
        
        print(f"🤖 交易机器人 ({self.name}): {action} {stock_symbol} - {reason}")


def exercise4_demo():
    """练习4演示"""
    # 创建股票
    apple = Stock("AAPL", 150.00)
    tesla = Stock("TSLA", 800.00)
    
    # 创建观察者
    email_notifier = EmailNotifier("investor@example.com")
    sms_notifier = SMSNotifier("+86-138-0000-0000")
    alert_system = AlertSystem(10.0)
    trading_bot = TradingBot("AlphaBot")
    
    # 注册观察者
    apple.attach(email_notifier)
    apple.attach(sms_notifier)
    apple.attach(alert_system)
    
    tesla.attach(email_notifier)
    tesla.attach(trading_bot)
    tesla.attach(alert_system)
    
    # 模拟价格变化
    print("\n开始股票价格监控...")
    
    # 苹果股票价格变化
    apple.price = 155.50  # 小幅上涨
    apple.price = 148.20  # 下跌
    apple.price = 165.80  # 大幅上涨
    
    # 特斯拉股票价格变化
    tesla.price = 795.30  # 小幅下跌
    tesla.price = 785.60  # 继续下跌
    tesla.price = 820.40  # 反弹
    
    print("解答说明：观察者模式实现了松耦合的通知机制，支持动态添加/移除观察者")


# ============================================================================
# 练习5：综合应用 - 游戏角色系统
# ============================================================================

print("\n=== 练习5：游戏角色系统 ===")
print("题目：设计一个RPG游戏的角色系统，包含不同职业和技能")
print("要求：综合运用多态、抽象类、策略模式等概念")

class Skill(ABC):
    """技能抽象基类"""
    
    def __init__(self, name: str, damage: int, mana_cost: int):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
    
    @abstractmethod
    def use(self, caster: 'Character', target: 'Character') -> str:
        """使用技能"""
        pass


class AttackSkill(Skill):
    """攻击技能"""
    
    def use(self, caster: 'Character', target: 'Character') -> str:
        if caster.mana < self.mana_cost:
            return f"{caster.name} 魔法值不足，无法使用 {self.name}"
        
        caster.mana -= self.mana_cost
        actual_damage = self.damage + caster.attack // 2
        target.take_damage(actual_damage)
        
        return f"{caster.name} 对 {target.name} 使用 {self.name}，造成 {actual_damage} 点伤害"


class HealSkill(Skill):
    """治疗技能"""
    
    def __init__(self, name: str, heal_amount: int, mana_cost: int):
        super().__init__(name, 0, mana_cost)
        self.heal_amount = heal_amount
    
    def use(self, caster: 'Character', target: 'Character') -> str:
        if caster.mana < self.mana_cost:
            return f"{caster.name} 魔法值不足，无法使用 {self.name}"
        
        caster.mana -= self.mana_cost
        actual_heal = self.heal_amount + caster.magic // 3
        target.heal(actual_heal)
        
        return f"{caster.name} 对 {target.name} 使用 {self.name}，恢复 {actual_heal} 点生命值"


class Character(ABC):
    """角色抽象基类"""
    
    def __init__(self, name: str, hp: int, mana: int, attack: int, defense: int, magic: int):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mana = mana
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.skills: List[Skill] = []
    
    @abstractmethod
    def get_class_name(self) -> str:
        """获取职业名称"""
        pass
    
    @abstractmethod
    def special_ability(self) -> str:
        """职业特殊能力"""
        pass
    
    def add_skill(self, skill: Skill):
        """学习技能"""
        self.skills.append(skill)
    
    def use_skill(self, skill_index: int, target: 'Character') -> str:
        """使用技能"""
        if 0 <= skill_index < len(self.skills):
            skill = self.skills[skill_index]
            return skill.use(self, target)
        return "无效的技能索引"
    
    def take_damage(self, damage: int):
        """受到伤害"""
        actual_damage = max(1, damage - self.defense // 2)
        self.hp = max(0, self.hp - actual_damage)
    
    def heal(self, amount: int):
        """恢复生命值"""
        self.hp = min(self.max_hp, self.hp + amount)
    
    def is_alive(self) -> bool:
        """是否存活"""
        return self.hp > 0
    
    def get_status(self) -> str:
        """获取状态信息"""
        return (f"{self.name} ({self.get_class_name()}) - "
                f"HP: {self.hp}/{self.max_hp}, MP: {self.mana}/{self.max_mana}")


class Warrior(Character):
    """战士"""
    
    def __init__(self, name: str):
        super().__init__(name, hp=120, mana=30, attack=25, defense=20, magic=5)
        # 学习战士技能
        self.add_skill(AttackSkill("重击", 30, 10))
        self.add_skill(AttackSkill("旋风斩", 20, 15))
    
    def get_class_name(self) -> str:
        return "战士"
    
    def special_ability(self) -> str:
        self.defense += 5
        return f"{self.name} 使用防御姿态，防御力提升！"


class Mage(Character):
    """法师"""
    
    def __init__(self, name: str):
        super().__init__(name, hp=80, mana=100, attack=10, defense=8, magic=30)
        # 学习法师技能
        self.add_skill(AttackSkill("火球术", 35, 20))
        self.add_skill(AttackSkill("冰锥术", 25, 15))
        self.add_skill(HealSkill("治疗术", 40, 25))
    
    def get_class_name(self) -> str:
        return "法师"
    
    def special_ability(self) -> str:
        self.mana = min(self.max_mana, self.mana + 20)
        return f"{self.name} 使用魔法恢复，魔法值恢复！"


class Priest(Character):
    """牧师"""
    
    def __init__(self, name: str):
        super().__init__(name, hp=100, mana=80, attack=12, defense=15, magic=25)
        # 学习牧师技能
        self.add_skill(HealSkill("治愈术", 50, 20))
        self.add_skill(HealSkill("群体治疗", 30, 35))
        self.add_skill(AttackSkill("神圣之光", 20, 15))
    
    def get_class_name(self) -> str:
        return "牧师"
    
    def special_ability(self) -> str:
        heal_amount = 25
        self.heal(heal_amount)
        return f"{self.name} 使用神圣祝福，恢复 {heal_amount} 点生命值！"


class GameBattle:
    """游戏战斗系统"""
    
    def __init__(self):
        self.characters: List[Character] = []
    
    def add_character(self, character: Character):
        """添加角色"""
        self.characters.append(character)
        print(f"{character.name} ({character.get_class_name()}) 加入战斗！")
    
    def show_status(self):
        """显示所有角色状态"""
        print("\n=== 角色状态 ===")
        for char in self.characters:
            print(char.get_status())
            if char.skills:
                print(f"  技能: {[skill.name for skill in char.skills]}")
    
    def simulate_battle(self):
        """模拟战斗"""
        print("\n=== 战斗开始 ===")
        
        if len(self.characters) < 2:
            print("需要至少2个角色才能开始战斗")
            return
        
        # 简单的回合制战斗
        turn = 0
        while len([c for c in self.characters if c.is_alive()]) > 1 and turn < 10:
            turn += 1
            print(f"\n--- 第 {turn} 回合 ---")
            
            for i, attacker in enumerate(self.characters):
                if not attacker.is_alive():
                    continue
                
                # 随机选择目标和技能
                targets = [c for j, c in enumerate(self.characters) if j != i and c.is_alive()]
                if not targets:
                    break
                
                target = random.choice(targets)
                
                # 30% 概率使用特殊能力，70% 概率使用技能
                if random.random() < 0.3:
                    result = attacker.special_ability()
                    print(result)
                elif attacker.skills:
                    skill_index = random.randint(0, len(attacker.skills) - 1)
                    result = attacker.use_skill(skill_index, target)
                    print(result)
                
                # 检查是否有角色死亡
                for char in self.characters:
                    if not char.is_alive():
                        print(f"💀 {char.name} 被击败了！")
        
        # 显示战斗结果
        survivors = [c for c in self.characters if c.is_alive()]
        if len(survivors) == 1:
            print(f"\n🏆 {survivors[0].name} 获得胜利！")
        else:
            print("\n⏰ 战斗时间结束，平局！")


def exercise5_demo():
    """练习5演示"""
    # 创建不同职业的角色
    warrior = Warrior("亚瑟")
    mage = Mage("梅林")
    priest = Priest("艾莉丝")
    
    # 创建战斗系统
    battle = GameBattle()
    battle.add_character(warrior)
    battle.add_character(mage)
    battle.add_character(priest)
    
    # 显示初始状态
    battle.show_status()
    
    # 模拟战斗
    battle.simulate_battle()
    
    # 显示最终状态
    battle.show_status()
    
    print("解答说明：综合运用了抽象类、多态、策略模式等概念，实现了灵活的游戏系统")


# ============================================================================
# 主程序
# ============================================================================

if __name__ == "__main__":
    print("Python 多态练习题")
    print("=" * 50)
    
    # 执行所有练习
    exercise1_demo()
    exercise2_demo()
    exercise3_demo()
    exercise4_demo()
    exercise5_demo()
    
    print("\n=== 练习总结 ===")
    print("1. 练习1：基础多态 - 掌握抽象基类和方法重写")
    print("2. 练习2：策略模式 - 学会算法封装和动态切换")
    print("3. 练习3：工厂模式 - 理解对象创建和接口统一")
    print("4. 练习4：观察者模式 - 实现松耦合的事件通知")
    print("5. 练习5：综合应用 - 多种模式的组合使用")
    
    print("\n=== 学习建议 ===")
    print("1. 多练习不同场景下的多态应用")
    print("2. 理解设计模式的核心思想")
    print("3. 注重代码的可扩展性和可维护性")
    print("4. 学会选择合适的设计模式")
    print("5. 在实际项目中应用所学知识")