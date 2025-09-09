#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
组合 vs 继承（Composition vs Inheritance）

组合和继承是面向对象编程中两种重要的代码复用机制。
理解它们的区别、优缺点和适用场景对于设计良好的软件架构至关重要。

学习要点：
1. 继承的特点和应用
2. 组合的特点和应用
3. 组合vs继承的对比
4. "优先使用组合而非继承"原则
5. 实际应用场景分析
6. 混合使用组合和继承
7. 设计模式中的应用
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import time

# 1. 继承方式的实现
print("=== 1. 继承方式的实现 ===")

class Vehicle:
    """交通工具基类"""
    
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self) -> None:
        """启动"""
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} 已启动")
        else:
            print(f"{self.brand} {self.model} 已经在运行中")
    
    def stop(self) -> None:
        """停止"""
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} 已停止")
        else:
            print(f"{self.brand} {self.model} 已经停止")
    
    def get_info(self) -> str:
        """获取信息"""
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    """汽车类 - 继承方式"""
    
    def __init__(self, brand: str, model: str, year: int, doors: int):
        super().__init__(brand, model, year)
        self.doors = doors
        self.fuel_level = 100
    
    def drive(self, distance: float) -> None:
        """驾驶"""
        if not self.is_running:
            print("请先启动汽车")
            return
        
        fuel_consumed = distance * 0.1  # 假设每公里消耗0.1升油
        if self.fuel_level >= fuel_consumed:
            self.fuel_level -= fuel_consumed
            print(f"驾驶了 {distance} 公里，剩余油量: {self.fuel_level:.1f}升")
        else:
            print("油量不足，无法完成行程")
    
    def refuel(self, amount: float) -> None:
        """加油"""
        self.fuel_level = min(100, self.fuel_level + amount)
        print(f"加油 {amount} 升，当前油量: {self.fuel_level:.1f}升")
    
    def get_info(self) -> str:
        """重写获取信息方法"""
        base_info = super().get_info()
        return f"{base_info}, {self.doors}门汽车"

class Motorcycle(Vehicle):
    """摩托车类 - 继承方式"""
    
    def __init__(self, brand: str, model: str, year: int, engine_size: int):
        super().__init__(brand, model, year)
        self.engine_size = engine_size
        self.fuel_level = 20
    
    def ride(self, distance: float) -> None:
        """骑行"""
        if not self.is_running:
            print("请先启动摩托车")
            return
        
        fuel_consumed = distance * 0.05  # 摩托车更省油
        if self.fuel_level >= fuel_consumed:
            self.fuel_level -= fuel_consumed
            print(f"骑行了 {distance} 公里，剩余油量: {self.fuel_level:.1f}升")
        else:
            print("油量不足，无法完成行程")
    
    def wheelie(self) -> None:
        """翘头"""
        if self.is_running:
            print(f"{self.brand} {self.model} 正在翘头!")
        else:
            print("请先启动摩托车")
    
    def get_info(self) -> str:
        """重写获取信息方法"""
        base_info = super().get_info()
        return f"{base_info}, {self.engine_size}cc摩托车"

# 测试继承方式
print("测试继承方式:")
car = Car("丰田", "卡罗拉", 2023, 4)
motorcycle = Motorcycle("本田", "CBR600RR", 2023, 600)

for vehicle in [car, motorcycle]:
    print(f"\n{vehicle.get_info()}")
    vehicle.start()
    
    if isinstance(vehicle, Car):
        vehicle.drive(50)
        vehicle.refuel(20)
    elif isinstance(vehicle, Motorcycle):
        vehicle.ride(30)
        vehicle.wheelie()
    
    vehicle.stop()

print("\n=== 2. 组合方式的实现 ===")

# 2. 组合方式的实现
class Engine:
    """引擎组件"""
    
    def __init__(self, engine_type: str, power: int):
        self.engine_type = engine_type
        self.power = power  # 马力
        self.is_running = False
        self.temperature = 20  # 温度
    
    def start(self) -> None:
        """启动引擎"""
        if not self.is_running:
            self.is_running = True
            self.temperature = 90
            print(f"{self.engine_type}引擎已启动，功率: {self.power}马力")
        else:
            print("引擎已经在运行中")
    
    def stop(self) -> None:
        """停止引擎"""
        if self.is_running:
            self.is_running = False
            self.temperature = 20
            print(f"{self.engine_type}引擎已停止")
        else:
            print("引擎已经停止")
    
    def get_status(self) -> Dict[str, Any]:
        """获取引擎状态"""
        return {
            "type": self.engine_type,
            "power": self.power,
            "running": self.is_running,
            "temperature": self.temperature
        }

class FuelTank:
    """油箱组件"""
    
    def __init__(self, capacity: float):
        self.capacity = capacity
        self.current_level = capacity
    
    def consume(self, amount: float) -> bool:
        """消耗燃料"""
        if self.current_level >= amount:
            self.current_level -= amount
            return True
        return False
    
    def refuel(self, amount: float) -> None:
        """加油"""
        self.current_level = min(self.capacity, self.current_level + amount)
        print(f"加油 {amount} 升，当前油量: {self.current_level:.1f}/{self.capacity}升")
    
    def get_level(self) -> float:
        """获取油量"""
        return self.current_level
    
    def get_percentage(self) -> float:
        """获取油量百分比"""
        return (self.current_level / self.capacity) * 100

class GPS:
    """GPS导航组件"""
    
    def __init__(self):
        self.current_location = (0.0, 0.0)
        self.destination = None
        self.is_navigating = False
    
    def set_destination(self, latitude: float, longitude: float) -> None:
        """设置目的地"""
        self.destination = (latitude, longitude)
        print(f"目的地已设置: ({latitude}, {longitude})")
    
    def start_navigation(self) -> None:
        """开始导航"""
        if self.destination:
            self.is_navigating = True
            print("GPS导航已启动")
        else:
            print("请先设置目的地")
    
    def update_location(self, latitude: float, longitude: float) -> None:
        """更新位置"""
        self.current_location = (latitude, longitude)
        if self.is_navigating:
            print(f"当前位置: ({latitude}, {longitude})")
    
    def stop_navigation(self) -> None:
        """停止导航"""
        self.is_navigating = False
        print("GPS导航已停止")

class ModernCar:
    """现代汽车类 - 组合方式"""
    
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        
        # 组合各种组件
        self.engine = Engine("V6汽油", 200)
        self.fuel_tank = FuelTank(60.0)
        self.gps = GPS()
        
        # 汽车特有属性
        self.odometer = 0.0  # 里程表
        self.doors_locked = False
    
    def start(self) -> None:
        """启动汽车"""
        print(f"启动 {self.brand} {self.model}...")
        self.engine.start()
    
    def stop(self) -> None:
        """停止汽车"""
        print(f"停止 {self.brand} {self.model}...")
        self.engine.stop()
        self.gps.stop_navigation()
    
    def drive(self, distance: float) -> None:
        """驾驶"""
        if not self.engine.is_running:
            print("请先启动汽车")
            return
        
        fuel_needed = distance * 0.08  # 每公里消耗0.08升
        if self.fuel_tank.consume(fuel_needed):
            self.odometer += distance
            print(f"驾驶了 {distance} 公里，总里程: {self.odometer:.1f}公里")
            print(f"剩余油量: {self.fuel_tank.get_percentage():.1f}%")
            
            # 更新GPS位置（模拟）
            new_lat = 39.9042 + distance * 0.001
            new_lng = 116.4074 + distance * 0.001
            self.gps.update_location(new_lat, new_lng)
        else:
            print("油量不足，无法完成行程")
    
    def refuel(self, amount: float) -> None:
        """加油"""
        self.fuel_tank.refuel(amount)
    
    def navigate_to(self, latitude: float, longitude: float) -> None:
        """导航到指定位置"""
        self.gps.set_destination(latitude, longitude)
        self.gps.start_navigation()
    
    def lock_doors(self) -> None:
        """锁门"""
        self.doors_locked = True
        print("车门已锁定")
    
    def unlock_doors(self) -> None:
        """开锁"""
        self.doors_locked = False
        print("车门已解锁")
    
    def get_status(self) -> Dict[str, Any]:
        """获取汽车状态"""
        return {
            "vehicle": f"{self.year} {self.brand} {self.model}",
            "odometer": self.odometer,
            "doors_locked": self.doors_locked,
            "engine": self.engine.get_status(),
            "fuel_percentage": self.fuel_tank.get_percentage(),
            "gps_navigating": self.gps.is_navigating
        }

# 测试组合方式
print("测试组合方式:")
modern_car = ModernCar("特斯拉", "Model S", 2023)

print(f"\n汽车状态: {modern_car.get_status()}")
modern_car.start()
modern_car.navigate_to(40.7128, -74.0060)  # 纽约坐标
modern_car.drive(100)
modern_car.lock_doors()
print(f"\n更新后状态: {modern_car.get_status()}")
modern_car.stop()

print("\n=== 3. 组合vs继承的详细对比 ===")

# 3. 对比分析：灵活性
print("灵活性对比:")

# 继承方式的限制
class ElectricCar(Vehicle):
    """电动汽车 - 继承方式的问题"""
    
    def __init__(self, brand: str, model: str, year: int):
        super().__init__(brand, model, year)
        self.battery_level = 100
        # 问题：继承了不需要的燃油相关方法
    
    def charge(self, amount: float) -> None:
        """充电"""
        self.battery_level = min(100, self.battery_level + amount)
        print(f"充电 {amount}%，当前电量: {self.battery_level}%")

# 组合方式的灵活性
class Battery:
    """电池组件"""
    
    def __init__(self, capacity: float):
        self.capacity = capacity  # kWh
        self.current_charge = capacity
    
    def consume(self, amount: float) -> bool:
        """消耗电量"""
        if self.current_charge >= amount:
            self.current_charge -= amount
            return True
        return False
    
    def charge(self, amount: float) -> None:
        """充电"""
        self.current_charge = min(self.capacity, self.current_charge + amount)
        print(f"充电 {amount} kWh，当前电量: {self.current_charge:.1f}/{self.capacity} kWh")
    
    def get_percentage(self) -> float:
        """获取电量百分比"""
        return (self.current_charge / self.capacity) * 100

class ElectricMotor:
    """电动机组件"""
    
    def __init__(self, power: int):
        self.power = power
        self.is_running = False
    
    def start(self) -> None:
        """启动电机"""
        self.is_running = True
        print(f"电动机已启动，功率: {self.power}kW")
    
    def stop(self) -> None:
        """停止电机"""
        self.is_running = False
        print("电动机已停止")

class FlexibleElectricCar:
    """灵活的电动汽车 - 组合方式"""
    
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        
        # 组合适合的组件
        self.motor = ElectricMotor(300)
        self.battery = Battery(75.0)
        self.gps = GPS()  # 复用GPS组件
        
        self.odometer = 0.0
    
    def start(self) -> None:
        """启动"""
        print(f"启动 {self.brand} {self.model}...")
        self.motor.start()
    
    def stop(self) -> None:
        """停止"""
        print(f"停止 {self.brand} {self.model}...")
        self.motor.stop()
    
    def drive(self, distance: float) -> None:
        """驾驶"""
        if not self.motor.is_running:
            print("请先启动汽车")
            return
        
        energy_needed = distance * 0.2  # 每公里消耗0.2kWh
        if self.battery.consume(energy_needed):
            self.odometer += distance
            print(f"驾驶了 {distance} 公里，总里程: {self.odometer:.1f}公里")
            print(f"剩余电量: {self.battery.get_percentage():.1f}%")
        else:
            print("电量不足，无法完成行程")
    
    def charge(self, amount: float) -> None:
        """充电"""
        self.battery.charge(amount)

# 测试灵活性
print("\n测试组合方式的灵活性:")
electric_car = FlexibleElectricCar("比亚迪", "汉EV", 2023)
electric_car.start()
electric_car.drive(80)
electric_car.charge(20)
electric_car.stop()

print("\n=== 4. 实际应用场景分析 ===")

# 4. 复杂场景：游戏角色系统
print("游戏角色系统设计对比:")

# 继承方式的问题
class GameCharacter:
    """游戏角色基类"""
    
    def __init__(self, name: str, health: int, mana: int):
        self.name = name
        self.health = health
        self.max_health = health
        self.mana = mana
        self.max_mana = mana
        self.level = 1
    
    def attack(self) -> int:
        """攻击"""
        return 10
    
    def take_damage(self, damage: int) -> None:
        """受到伤害"""
        self.health = max(0, self.health - damage)
        print(f"{self.name} 受到 {damage} 点伤害，剩余生命值: {self.health}")

class Warrior(GameCharacter):
    """战士 - 继承方式"""
    
    def __init__(self, name: str):
        super().__init__(name, 150, 50)
        self.armor = 20
    
    def attack(self) -> int:
        """重写攻击方法"""
        return 25
    
    def shield_block(self) -> None:
        """盾牌格挡"""
        print(f"{self.name} 使用盾牌格挡")

class Mage(GameCharacter):
    """法师 - 继承方式"""
    
    def __init__(self, name: str):
        super().__init__(name, 80, 200)
        self.spell_power = 30
    
    def cast_spell(self, spell_name: str, mana_cost: int) -> int:
        """施法"""
        if self.mana >= mana_cost:
            self.mana -= mana_cost
            damage = self.spell_power + 20
            print(f"{self.name} 施放 {spell_name}，造成 {damage} 点魔法伤害")
            return damage
        else:
            print(f"{self.name} 法力值不足")
            return 0

# 组合方式的解决方案
class HealthComponent:
    """生命值组件"""
    
    def __init__(self, max_health: int):
        self.max_health = max_health
        self.current_health = max_health
    
    def take_damage(self, damage: int) -> None:
        """受到伤害"""
        self.current_health = max(0, self.current_health - damage)
    
    def heal(self, amount: int) -> None:
        """治疗"""
        self.current_health = min(self.max_health, self.current_health + amount)
    
    def is_alive(self) -> bool:
        """是否存活"""
        return self.current_health > 0
    
    def get_percentage(self) -> float:
        """获取生命值百分比"""
        return (self.current_health / self.max_health) * 100

class ManaComponent:
    """法力值组件"""
    
    def __init__(self, max_mana: int):
        self.max_mana = max_mana
        self.current_mana = max_mana
    
    def consume(self, amount: int) -> bool:
        """消耗法力值"""
        if self.current_mana >= amount:
            self.current_mana -= amount
            return True
        return False
    
    def restore(self, amount: int) -> None:
        """恢复法力值"""
        self.current_mana = min(self.max_mana, self.current_mana + amount)

class CombatComponent:
    """战斗组件"""
    
    def __init__(self, base_damage: int, attack_speed: float = 1.0):
        self.base_damage = base_damage
        self.attack_speed = attack_speed
        self.critical_chance = 0.1  # 10%暴击率
    
    def calculate_damage(self) -> int:
        """计算伤害"""
        import random
        damage = self.base_damage
        if random.random() < self.critical_chance:
            damage *= 2
            print("暴击!")
        return damage

class MagicComponent:
    """魔法组件"""
    
    def __init__(self, spell_power: int):
        self.spell_power = spell_power
        self.spells = {
            "火球术": {"damage": 30, "mana_cost": 20},
            "冰箭": {"damage": 25, "mana_cost": 15},
            "治疗术": {"heal": 40, "mana_cost": 25}
        }
    
    def cast_spell(self, spell_name: str, mana_component: ManaComponent, 
                   target_health: Optional[HealthComponent] = None) -> int:
        """施法"""
        if spell_name not in self.spells:
            print(f"未知法术: {spell_name}")
            return 0
        
        spell = self.spells[spell_name]
        if not mana_component.consume(spell["mana_cost"]):
            print("法力值不足")
            return 0
        
        if "damage" in spell:
            damage = spell["damage"] + self.spell_power
            print(f"施放 {spell_name}，造成 {damage} 点魔法伤害")
            return damage
        elif "heal" in spell and target_health:
            heal_amount = spell["heal"] + self.spell_power // 2
            target_health.heal(heal_amount)
            print(f"施放 {spell_name}，治疗 {heal_amount} 点生命值")
            return 0
        
        return 0

class FlexibleCharacter:
    """灵活的游戏角色 - 组合方式"""
    
    def __init__(self, name: str, character_type: str):
        self.name = name
        self.character_type = character_type
        self.level = 1
        
        # 根据角色类型组合不同的组件
        if character_type == "warrior":
            self.health = HealthComponent(150)
            self.mana = ManaComponent(50)
            self.combat = CombatComponent(25, 1.2)
            self.magic = None
        elif character_type == "mage":
            self.health = HealthComponent(80)
            self.mana = ManaComponent(200)
            self.combat = CombatComponent(10, 0.8)
            self.magic = MagicComponent(30)
        elif character_type == "paladin":  # 混合职业
            self.health = HealthComponent(120)
            self.mana = ManaComponent(100)
            self.combat = CombatComponent(20, 1.0)
            self.magic = MagicComponent(15)  # 较弱的魔法能力
    
    def attack(self, target: 'FlexibleCharacter') -> None:
        """攻击目标"""
        if not self.health.is_alive():
            print(f"{self.name} 已死亡，无法攻击")
            return
        
        damage = self.combat.calculate_damage()
        print(f"{self.name} 攻击 {target.name}")
        target.take_damage(damage)
    
    def cast_spell(self, spell_name: str, target: Optional['FlexibleCharacter'] = None) -> None:
        """施法"""
        if not self.magic:
            print(f"{self.name} 无法使用魔法")
            return
        
        if not self.health.is_alive():
            print(f"{self.name} 已死亡，无法施法")
            return
        
        target_health = target.health if target else self.health
        self.magic.cast_spell(spell_name, self.mana, target_health)
    
    def take_damage(self, damage: int) -> None:
        """受到伤害"""
        self.health.take_damage(damage)
        print(f"{self.name} 受到 {damage} 点伤害，剩余生命值: {self.health.current_health}/{self.health.max_health}")
        
        if not self.health.is_alive():
            print(f"{self.name} 已死亡!")
    
    def get_status(self) -> Dict[str, Any]:
        """获取状态"""
        return {
            "name": self.name,
            "type": self.character_type,
            "level": self.level,
            "health": f"{self.health.current_health}/{self.health.max_health}",
            "mana": f"{self.mana.current_mana}/{self.mana.max_mana}",
            "alive": self.health.is_alive()
        }

# 测试游戏角色系统
print("\n测试组合方式的游戏角色系统:")
warrior = FlexibleCharacter("阿尔萨斯", "warrior")
mage = FlexibleCharacter("吉安娜", "mage")
paladin = FlexibleCharacter("乌瑟尔", "paladin")

characters = [warrior, mage, paladin]
for char in characters:
    print(f"{char.name} 状态: {char.get_status()}")

print("\n战斗演示:")
mage.cast_spell("火球术", warrior)
warrior.attack(mage)
paladin.cast_spell("治疗术", warrior)

print("\n战斗后状态:")
for char in characters:
    print(f"{char.name} 状态: {char.get_status()}")

print("\n=== 5. 设计原则和最佳实践 ===")

# 5. 设计原则演示
print("设计原则演示:")

class Logger:
    """日志记录器组件"""
    
    def __init__(self, name: str):
        self.name = name
    
    def log(self, level: str, message: str) -> None:
        """记录日志"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{self.name}] {level}: {message}")

class Cache:
    """缓存组件"""
    
    def __init__(self):
        self._cache = {}
    
    def get(self, key: str) -> Any:
        """获取缓存"""
        return self._cache.get(key)
    
    def set(self, key: str, value: Any) -> None:
        """设置缓存"""
        self._cache[key] = value
    
    def clear(self) -> None:
        """清空缓存"""
        self._cache.clear()

class Database:
    """数据库组件"""
    
    def __init__(self, name: str):
        self.name = name
        self._data = {}
    
    def save(self, key: str, data: Any) -> None:
        """保存数据"""
        self._data[key] = data
    
    def load(self, key: str) -> Any:
        """加载数据"""
        return self._data.get(key)
    
    def delete(self, key: str) -> None:
        """删除数据"""
        if key in self._data:
            del self._data[key]

class DataService:
    """数据服务 - 组合多个组件"""
    
    def __init__(self, service_name: str):
        self.service_name = service_name
        
        # 组合各种功能组件
        self.logger = Logger(service_name)
        self.cache = Cache()
        self.database = Database(f"{service_name}_db")
    
    def get_data(self, key: str) -> Any:
        """获取数据（带缓存）"""
        self.logger.log("INFO", f"请求数据: {key}")
        
        # 先检查缓存
        cached_data = self.cache.get(key)
        if cached_data is not None:
            self.logger.log("INFO", f"从缓存获取数据: {key}")
            return cached_data
        
        # 从数据库加载
        data = self.database.load(key)
        if data is not None:
            self.cache.set(key, data)
            self.logger.log("INFO", f"从数据库加载数据并缓存: {key}")
            return data
        
        self.logger.log("WARNING", f"数据不存在: {key}")
        return None
    
    def save_data(self, key: str, data: Any) -> None:
        """保存数据"""
        self.logger.log("INFO", f"保存数据: {key}")
        
        # 保存到数据库
        self.database.save(key, data)
        
        # 更新缓存
        self.cache.set(key, data)
        
        self.logger.log("INFO", f"数据保存完成: {key}")
    
    def delete_data(self, key: str) -> None:
        """删除数据"""
        self.logger.log("INFO", f"删除数据: {key}")
        
        # 从数据库删除
        self.database.delete(key)
        
        # 清除缓存
        self.cache.set(key, None)
        
        self.logger.log("INFO", f"数据删除完成: {key}")
    
    def clear_cache(self) -> None:
        """清空缓存"""
        self.cache.clear()
        self.logger.log("INFO", "缓存已清空")

# 测试数据服务
print("\n测试组合式数据服务:")
user_service = DataService("UserService")

# 保存和获取数据
user_service.save_data("user_1", {"name": "张三", "age": 25})
user_data = user_service.get_data("user_1")  # 从数据库获取
user_data_cached = user_service.get_data("user_1")  # 从缓存获取

# 尝试获取不存在的数据
missing_data = user_service.get_data("user_999")

print("\n=== 总结：组合vs继承的选择指南 ===")
print("""
组合 vs 继承的选择指南：

何时使用继承：
1. 存在明确的"is-a"关系
2. 需要多态性
3. 子类是父类的特化版本
4. 需要重写父类的行为
5. 继承层次相对简单

何时使用组合：
1. 存在"has-a"关系
2. 需要运行时改变行为
3. 需要组合多个功能
4. 避免复杂的继承层次
5. 需要更好的测试性

组合的优势：
- 更好的灵活性
- 更容易测试
- 更好的封装性
- 避免继承的脆弱性
- 支持运行时组合

继承的优势：
- 代码复用更直接
- 支持多态性
- 更符合某些设计模式
- 类型关系更明确

最佳实践：
1. 优先考虑组合
2. 保持继承层次简单
3. 使用抽象基类定义接口
4. 避免深层继承
5. 组合和继承可以混合使用
""")

if __name__ == "__main__":
    print("\n组合vs继承演示完成!")
    print("理解何时使用组合、何时使用继承是面向对象设计的关键技能。")
    print("记住：优先使用组合，在合适的场景下使用继承。")