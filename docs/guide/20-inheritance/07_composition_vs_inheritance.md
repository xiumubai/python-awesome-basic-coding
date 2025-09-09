# 组合vs继承

组合（Composition）和继承（Inheritance）是面向对象编程中两种重要的代码复用机制。理解它们的区别、优缺点和适用场景对于设计良好的软件架构至关重要。

## 基本概念对比

### 继承（Inheritance）
继承是"is-a"关系，子类是父类的一种特殊类型。

### 组合（Composition）
组合是"has-a"关系，一个类包含其他类的实例作为其组成部分。

```python
# 1. 继承vs组合基本概念
print("=== 继承vs组合基本概念 ===")

# 继承示例 - "is-a" 关系
class Vehicle:
    """交通工具基类"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
    
    def start(self):
        return f"{self.brand} {self.model} 启动了"
    
    def stop(self):
        return f"{self.brand} {self.model} 停止了"
    
    def accelerate(self, increment):
        self.speed += increment
        return f"加速到 {self.speed} km/h"

class Car(Vehicle):  # 继承关系：汽车 IS-A 交通工具
    """汽车类 - 继承自Vehicle"""
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def honk(self):
        return f"{self.brand} {self.model} 鸣笛: 嘀嘀!"
    
    def open_door(self):
        return f"打开 {self.doors} 门中的一扇门"

class Motorcycle(Vehicle):  # 继承关系：摩托车 IS-A 交通工具
    """摩托车类 - 继承自Vehicle"""
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size
    
    def wheelie(self):
        return f"{self.brand} {self.model} 做后轮着地特技!"

# 组合示例 - "has-a" 关系
class Engine:
    """发动机类"""
    def __init__(self, type_name, horsepower):
        self.type = type_name
        self.horsepower = horsepower
        self.running = False
    
    def start(self):
        self.running = True
        return f"{self.type}发动机启动 ({self.horsepower}马力)"
    
    def stop(self):
        self.running = False
        return f"{self.type}发动机停止"
    
    def get_status(self):
        status = "运行中" if self.running else "停止"
        return f"{self.type}发动机状态: {status}"

class Transmission:
    """变速箱类"""
    def __init__(self, type_name, gears):
        self.type = type_name
        self.gears = gears
        self.current_gear = 1
    
    def shift_up(self):
        if self.current_gear < self.gears:
            self.current_gear += 1
        return f"换到 {self.current_gear} 档"
    
    def shift_down(self):
        if self.current_gear > 1:
            self.current_gear -= 1
        return f"换到 {self.current_gear} 档"
    
    def get_status(self):
        return f"{self.type}变速箱: {self.current_gear}/{self.gears} 档"

class ComposedCar:  # 组合关系：汽车 HAS-A 发动机和变速箱
    """使用组合的汽车类"""
    def __init__(self, brand, model, engine, transmission):
        self.brand = brand
        self.model = model
        self.engine = engine  # 组合：汽车有一个发动机
        self.transmission = transmission  # 组合：汽车有一个变速箱
        self.speed = 0
    
    def start(self):
        engine_msg = self.engine.start()
        return f"{self.brand} {self.model} 启动: {engine_msg}"
    
    def stop(self):
        engine_msg = self.engine.stop()
        return f"{self.brand} {self.model} 停止: {engine_msg}"
    
    def accelerate(self):
        if self.engine.running:
            self.speed += 10
            return f"加速到 {self.speed} km/h"
        return "发动机未启动，无法加速"
    
    def shift_gear(self, direction):
        if direction == "up":
            return self.transmission.shift_up()
        elif direction == "down":
            return self.transmission.shift_down()
    
    def get_status(self):
        return f"""{self.brand} {self.model} 状态:
  速度: {self.speed} km/h
  {self.engine.get_status()}
  {self.transmission.get_status()}"""

# 测试继承
print("--- 继承示例 ---")
car = Car("丰田", "卡罗拉", 4)
motorcycle = Motorcycle("本田", "CBR600", "600cc")

print(car.start())
print(car.accelerate(50))
print(car.honk())
print(car.open_door())
print()

print(motorcycle.start())
print(motorcycle.accelerate(80))
print(motorcycle.wheelie())
print()

# 测试组合
print("--- 组合示例 ---")
engine = Engine("V6", 300)
transmission = Transmission("自动", 6)
composed_car = ComposedCar("宝马", "X5", engine, transmission)

print(composed_car.start())
print(composed_car.accelerate())
print(composed_car.shift_gear("up"))
print(composed_car.shift_gear("up"))
print()
print(composed_car.get_status())
print()
```

## 继承的优缺点分析

```python
# 2. 继承的优缺点分析
print("=== 继承的优缺点分析 ===")

# 继承的优点示例
class Animal:
    """动物基类"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100
    
    def eat(self, food):
        self.energy += 10
        return f"{self.name} 吃了 {food}，能量增加到 {self.energy}"
    
    def sleep(self):
        self.energy = 100
        return f"{self.name} 睡觉恢复了体力"
    
    def move(self):
        self.energy -= 5
        return f"{self.name} 移动了，能量减少到 {self.energy}"

class Dog(Animal):
    """狗类 - 继承的优点：代码复用"""
    def __init__(self, name, breed):
        super().__init__(name, "犬科")
        self.breed = breed
    
    def bark(self):
        return f"{self.name}({self.breed}) 汪汪叫"
    
    def fetch(self, item):
        move_msg = self.move()
        return f"{self.name} 去捡 {item}。{move_msg}"

class Cat(Animal):
    """猫类 - 继承的优点：多态性"""
    def __init__(self, name, color):
        super().__init__(name, "猫科")
        self.color = color
    
    def meow(self):
        return f"{self.name}({self.color}色) 喵喵叫"
    
    def climb(self, target):
        move_msg = self.move()
        return f"{self.name} 爬到 {target} 上。{move_msg}"

# 继承的缺点示例
class Bird(Animal):
    """鸟类 - 继承的缺点：不合适的继承"""
    def __init__(self, name, can_fly=True):
        super().__init__(name, "鸟类")
        self.can_fly = can_fly
    
    def fly(self):
        if self.can_fly:
            move_msg = self.move()
            return f"{self.name} 飞翔。{move_msg}"
        else:
            return f"{self.name} 不会飞"
    
    # 问题：企鹅不会飞，但继承了fly方法
    # 这违反了里氏替换原则

class Penguin(Bird):
    """企鹅 - 继承的问题：不适当的方法继承"""
    def __init__(self, name):
        super().__init__(name, can_fly=False)  # 企鹅不会飞
    
    def swim(self):
        move_msg = self.move()
        return f"{self.name} 游泳。{move_msg}"
    
    # 重写fly方法，但这表明继承关系可能不合适
    def fly(self):
        return f"{self.name} 是企鹅，不会飞！"

def demonstrate_polymorphism(animals):
    """演示多态性 - 继承的优点"""
    print("多态性演示:")
    for animal in animals:
        print(f"  {animal.eat('食物')}")
        print(f"  {animal.move()}")
        
        # 调用特定方法
        if isinstance(animal, Dog):
            print(f"  {animal.bark()}")
        elif isinstance(animal, Cat):
            print(f"  {animal.meow()}")
        elif isinstance(animal, Bird):
            print(f"  {animal.fly()}")
        print()

print("--- 继承的优点：代码复用和多态 ---")
dog = Dog("旺财", "金毛")
cat = Cat("咪咪", "橘")
bird = Bird("小黄", True)
penguin = Penguin("波波")

demonstrate_polymorphism([dog, cat, bird, penguin])

print("--- 继承的缺点：不合适的继承关系 ---")
print(f"企鹅尝试飞行: {penguin.fly()}")
print("这表明企鹅可能不应该继承自Bird，或者需要重新设计继承层次")
print()
```

## 组合的优缺点分析

```python
# 3. 组合的优缺点分析
print("=== 组合的优缺点分析 ===")

# 组合的优点：灵活性和可扩展性
class Flyable:
    """飞行能力组件"""
    def __init__(self, max_altitude=1000):
        self.max_altitude = max_altitude
    
    def fly(self, altitude=100):
        if altitude <= self.max_altitude:
            return f"飞行到 {altitude} 米高度"
        else:
            return f"无法飞行到 {altitude} 米，最大高度 {self.max_altitude} 米"

class Swimmable:
    """游泳能力组件"""
    def __init__(self, max_depth=50):
        self.max_depth = max_depth
    
    def swim(self, depth=10):
        if depth <= self.max_depth:
            return f"游泳到 {depth} 米深度"
        else:
            return f"无法游泳到 {depth} 米，最大深度 {self.max_depth} 米"

class Walkable:
    """行走能力组件"""
    def __init__(self, max_speed=50):
        self.max_speed = max_speed
    
    def walk(self, speed=10):
        if speed <= self.max_speed:
            return f"以 {speed} km/h 的速度行走"
        else:
            return f"无法以 {speed} km/h 行走，最大速度 {self.max_speed} km/h"

# 使用组合创建灵活的动物类
class FlexibleAnimal:
    """使用组合的灵活动物类"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.abilities = {}  # 存储能力组件
    
    def add_ability(self, ability_name, ability_component):
        """添加能力"""
        self.abilities[ability_name] = ability_component
        return f"{self.name} 获得了 {ability_name} 能力"
    
    def use_ability(self, ability_name, *args, **kwargs):
        """使用能力"""
        if ability_name in self.abilities:
            ability = self.abilities[ability_name]
            method_name = ability_name.replace('able', '').lower()  # flyable -> fly
            if hasattr(ability, method_name):
                method = getattr(ability, method_name)
                result = method(*args, **kwargs)
                return f"{self.name} {result}"
            else:
                return f"{self.name} 的 {ability_name} 能力没有对应的方法"
        else:
            return f"{self.name} 没有 {ability_name} 能力"
    
    def list_abilities(self):
        """列出所有能力"""
        if self.abilities:
            abilities = ", ".join(self.abilities.keys())
            return f"{self.name} 的能力: {abilities}"
        else:
            return f"{self.name} 没有特殊能力"

# 创建不同能力组合的动物
print("--- 组合的优点：灵活的能力组合 ---")

# 鸟类：会飞和走
bird = FlexibleAnimal("小鸟", "鸟类")
print(bird.add_ability("flyable", Flyable(5000)))
print(bird.add_ability("walkable", Walkable(20)))
print(bird.list_abilities())
print(bird.use_ability("flyable", 1000))
print(bird.use_ability("walkable", 15))
print()

# 鸭子：会飞、游泳和走
duck = FlexibleAnimal("鸭子", "水鸟")
print(duck.add_ability("flyable", Flyable(3000)))
print(duck.add_ability("swimmable", Swimmable(20)))
print(duck.add_ability("walkable", Walkable(25)))
print(duck.list_abilities())
print(duck.use_ability("swimmable", 5))
print(duck.use_ability("flyable", 500))
print()

# 企鹅：只会游泳和走（不会飞）
penguin_composed = FlexibleAnimal("企鹅", "不会飞的鸟")
print(penguin_composed.add_ability("swimmable", Swimmable(200)))
print(penguin_composed.add_ability("walkable", Walkable(10)))
print(penguin_composed.list_abilities())
print(penguin_composed.use_ability("swimmable", 50))
print(penguin_composed.use_ability("flyable", 100))  # 没有飞行能力
print()

# 组合的缺点：复杂性增加
class ComplexVehicle:
    """复杂的交通工具 - 展示组合的缺点"""
    def __init__(self, name):
        self.name = name
        # 需要管理多个组件
        self.engine = None
        self.transmission = None
        self.brakes = None
        self.steering = None
        self.electronics = None
    
    def add_engine(self, engine):
        self.engine = engine
    
    def add_transmission(self, transmission):
        self.transmission = transmission
    
    # ... 需要为每个组件添加方法
    
    def start(self):
        # 需要协调多个组件
        if not self.engine:
            return f"{self.name}: 没有发动机，无法启动"
        if not self.transmission:
            return f"{self.name}: 没有变速箱，无法启动"
        
        # 复杂的启动逻辑
        engine_result = self.engine.start()
        return f"{self.name} 启动: {engine_result}"

print("--- 组合的缺点：增加复杂性 ---")
complex_vehicle = ComplexVehicle("复杂汽车")
print(complex_vehicle.start())  # 缺少组件

complex_vehicle.add_engine(Engine("V8", 400))
complex_vehicle.add_transmission(Transmission("手动", 5))
print(complex_vehicle.start())  # 现在可以启动
print()
```

## 设计原则和选择指南

```python
# 4. 设计原则和选择指南
print("=== 设计原则和选择指南 ===")

# 里氏替换原则（LSP）示例
class Shape:
    """形状基类"""
    def area(self):
        raise NotImplementedError("子类必须实现area方法")
    
    def perimeter(self):
        raise NotImplementedError("子类必须实现perimeter方法")

class Rectangle(Shape):
    """矩形 - 符合LSP"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    """正方形 - 可能违反LSP的例子"""
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_width(self, width):
        # 正方形的宽高必须相等
        self.width = width
        self.height = width
    
    def set_height(self, height):
        # 正方形的宽高必须相等
        self.width = height
        self.height = height

def test_lsp_violation(rectangle):
    """测试里氏替换原则"""
    print(f"原始矩形: 宽={rectangle.width}, 高={rectangle.height}")
    
    # 这个操作对Rectangle是安全的，但对Square可能不符合预期
    original_width = rectangle.width
    rectangle.width = 10
    rectangle.height = 5
    
    expected_area = 10 * 5  # 50
    actual_area = rectangle.area()
    
    print(f"设置后: 宽={rectangle.width}, 高={rectangle.height}")
    print(f"期望面积: {expected_area}, 实际面积: {actual_area}")
    print(f"LSP测试: {'通过' if expected_area == actual_area else '失败'}")

print("--- 里氏替换原则测试 ---")
rectangle = Rectangle(4, 6)
square = Square(4)

print("矩形测试:")
test_lsp_violation(rectangle)
print()

print("正方形测试:")
test_lsp_violation(square)
print()

# 组合优于继承的原则示例
class BadVehicleHierarchy:
    """不好的继承层次示例"""
    pass

class BadCar(BadVehicleHierarchy):
    def drive(self): pass
    def fly(self): raise NotImplementedError("汽车不会飞")
    def sail(self): raise NotImplementedError("汽车不会航行")

class BadPlane(BadVehicleHierarchy):
    def drive(self): raise NotImplementedError("飞机不在地面行驶")
    def fly(self): pass
    def sail(self): raise NotImplementedError("飞机不会航行")

class BadBoat(BadVehicleHierarchy):
    def drive(self): raise NotImplementedError("船不在陆地行驶")
    def fly(self): raise NotImplementedError("船不会飞")
    def sail(self): pass

# 更好的组合设计
class DrivingCapability:
    """驾驶能力"""
    def drive(self):
        return "在陆地上行驶"

class FlyingCapability:
    """飞行能力"""
    def fly(self):
        return "在空中飞行"

class SailingCapability:
    """航行能力"""
    def sail(self):
        return "在水上航行"

class GoodVehicle:
    """使用组合的良好设计"""
    def __init__(self, name):
        self.name = name
        self.capabilities = []
    
    def add_capability(self, capability):
        self.capabilities.append(capability)
    
    def move(self):
        if not self.capabilities:
            return f"{self.name} 没有移动能力"
        
        movements = []
        for capability in self.capabilities:
            if hasattr(capability, 'drive'):
                movements.append(capability.drive())
            elif hasattr(capability, 'fly'):
                movements.append(capability.fly())
            elif hasattr(capability, 'sail'):
                movements.append(capability.sail())
        
        return f"{self.name} 可以: {', '.join(movements)}"

print("--- 组合优于继承示例 ---")

# 创建不同类型的交通工具
car = GoodVehicle("汽车")
car.add_capability(DrivingCapability())
print(car.move())

plane = GoodVehicle("飞机")
plane.add_capability(FlyingCapability())
print(plane.move())

amphibious_vehicle = GoodVehicle("水陆两用车")
amphibious_vehicle.add_capability(DrivingCapability())
amphibious_vehicle.add_capability(SailingCapability())
print(amphibious_vehicle.move())

# 甚至可以创建科幻交通工具
flying_car = GoodVehicle("飞行汽车")
flying_car.add_capability(DrivingCapability())
flying_car.add_capability(FlyingCapability())
print(flying_car.move())
print()
```

## 实际应用场景对比

```python
# 5. 实际应用场景对比
print("=== 实际应用场景对比 ===")

# 场景1：GUI组件 - 适合继承
class Widget:
    """GUI组件基类"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
    
    def draw(self):
        if self.visible:
            return f"绘制组件在 ({self.x}, {self.y}), 大小 {self.width}x{self.height}"
        return "组件不可见"
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def resize(self, width, height):
        self.width = width
        self.height = height

class Button(Widget):
    """按钮 - 继承适合，因为Button IS-A Widget"""
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        self.text = text
        self.clicked = False
    
    def click(self):
        self.clicked = True
        return f"按钮 '{self.text}' 被点击"
    
    def draw(self):
        base_draw = super().draw()
        return f"{base_draw} - 按钮文本: '{self.text}'"

class TextBox(Widget):
    """文本框 - 继承适合"""
    def __init__(self, x, y, width, height, placeholder=""):
        super().__init__(x, y, width, height)
        self.text = ""
        self.placeholder = placeholder
    
    def type_text(self, text):
        self.text += text
        return f"输入文本: '{self.text}'"
    
    def clear(self):
        self.text = ""
        return "文本框已清空"

print("--- 场景1: GUI组件 (适合继承) ---")
button = Button(10, 20, 100, 30, "确定")
textbox = TextBox(10, 60, 200, 25, "请输入文本")

print(button.draw())
print(button.click())
print(textbox.draw())
print(textbox.type_text("Hello World"))
print()

# 场景2：游戏实体 - 适合组合
class HealthComponent:
    """生命值组件"""
    def __init__(self, max_health):
        self.max_health = max_health
        self.current_health = max_health
    
    def take_damage(self, damage):
        self.current_health = max(0, self.current_health - damage)
        return f"受到 {damage} 点伤害，剩余生命值: {self.current_health}/{self.max_health}"
    
    def heal(self, amount):
        self.current_health = min(self.max_health, self.current_health + amount)
        return f"恢复 {amount} 点生命值，当前生命值: {self.current_health}/{self.max_health}"
    
    def is_alive(self):
        return self.current_health > 0

class MovementComponent:
    """移动组件"""
    def __init__(self, speed):
        self.speed = speed
        self.x = 0
        self.y = 0
    
    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        return f"移动到 ({self.x}, {self.y})"
    
    def get_position(self):
        return (self.x, self.y)

class AttackComponent:
    """攻击组件"""
    def __init__(self, damage, range_val):
        self.damage = damage
        self.range = range_val
    
    def attack(self, target):
        if hasattr(target, 'health') and target.health:
            return target.health.take_damage(self.damage)
        return "无法攻击目标"

class GameEntity:
    """游戏实体 - 使用组合"""
    def __init__(self, name):
        self.name = name
        self.health = None
        self.movement = None
        self.attack = None
    
    def add_health(self, max_health):
        self.health = HealthComponent(max_health)
        return f"{self.name} 获得生命值组件"
    
    def add_movement(self, speed):
        self.movement = MovementComponent(speed)
        return f"{self.name} 获得移动组件"
    
    def add_attack(self, damage, range_val):
        self.attack = AttackComponent(damage, range_val)
        return f"{self.name} 获得攻击组件"
    
    def get_status(self):
        status = [f"实体: {self.name}"]
        if self.health:
            alive = "存活" if self.health.is_alive() else "死亡"
            status.append(f"  生命值: {self.health.current_health}/{self.health.max_health} ({alive})")
        if self.movement:
            pos = self.movement.get_position()
            status.append(f"  位置: {pos}, 速度: {self.movement.speed}")
        if self.attack:
            status.append(f"  攻击力: {self.attack.damage}, 攻击范围: {self.attack.range}")
        return "\n".join(status)

print("--- 场景2: 游戏实体 (适合组合) ---")

# 创建不同类型的游戏实体
warrior = GameEntity("战士")
print(warrior.add_health(100))
print(warrior.add_movement(5))
print(warrior.add_attack(20, 2))
print()

mage = GameEntity("法师")
print(mage.add_health(60))
print(mage.add_movement(3))
print(mage.add_attack(35, 8))
print()

npc = GameEntity("村民")
print(npc.add_health(50))
print(npc.add_movement(2))
# 村民没有攻击能力
print()

# 测试实体交互
print("实体状态:")
print(warrior.get_status())
print()
print(mage.get_status())
print()
print(npc.get_status())
print()

# 战斗测试
print("战斗测试:")
if warrior.attack and mage.health:
    print(f"战士攻击法师: {warrior.attack.attack(mage)}")
if mage.attack and warrior.health:
    print(f"法师攻击战士: {mage.attack.attack(warrior)}")
print()

print("战斗后状态:")
print(warrior.get_status())
print()
print(mage.get_status())
print()
```

## 混合使用：继承与组合结合

```python
# 6. 混合使用：继承与组合结合
print("=== 混合使用：继承与组合结合 ===")

# 基础设备类
class Device:
    """设备基类"""
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.power_on = False
    
    def turn_on(self):
        self.power_on = True
        return f"{self.name} {self.model} 已开机"
    
    def turn_off(self):
        self.power_on = False
        return f"{self.name} {self.model} 已关机"
    
    def get_status(self):
        status = "开机" if self.power_on else "关机"
        return f"{self.name} {self.model}: {status}"

# 功能组件
class WiFiModule:
    """WiFi模块"""
    def __init__(self):
        self.connected = False
        self.network_name = None
    
    def connect(self, network_name):
        self.connected = True
        self.network_name = network_name
        return f"已连接到WiFi网络: {network_name}"
    
    def disconnect(self):
        self.connected = False
        network = self.network_name
        self.network_name = None
        return f"已断开WiFi网络: {network}"
    
    def get_status(self):
        if self.connected:
            return f"WiFi: 已连接到 {self.network_name}"
        return "WiFi: 未连接"

class BluetoothModule:
    """蓝牙模块"""
    def __init__(self):
        self.enabled = False
        self.paired_devices = []
    
    def enable(self):
        self.enabled = True
        return "蓝牙已启用"
    
    def disable(self):
        self.enabled = False
        self.paired_devices.clear()
        return "蓝牙已禁用"
    
    def pair_device(self, device_name):
        if self.enabled:
            self.paired_devices.append(device_name)
            return f"已配对设备: {device_name}"
        return "蓝牙未启用，无法配对设备"
    
    def get_status(self):
        if self.enabled:
            devices = ", ".join(self.paired_devices) if self.paired_devices else "无"
            return f"蓝牙: 已启用，配对设备: {devices}"
        return "蓝牙: 已禁用"

class CameraModule:
    """摄像头模块"""
    def __init__(self, resolution):
        self.resolution = resolution
        self.recording = False
    
    def start_recording(self):
        self.recording = True
        return f"开始录制 ({self.resolution})"
    
    def stop_recording(self):
        self.recording = False
        return f"停止录制"
    
    def take_photo(self):
        return f"拍照 ({self.resolution})"
    
    def get_status(self):
        status = "录制中" if self.recording else "待机"
        return f"摄像头 ({self.resolution}): {status}"

# 智能手机类 - 继承Device，组合各种模块
class SmartPhone(Device):
    """智能手机 - 混合使用继承和组合"""
    def __init__(self, name, model):
        super().__init__(name, model)  # 继承基础设备功能
        # 组合各种功能模块
        self.wifi = WiFiModule()
        self.bluetooth = BluetoothModule()
        self.camera = CameraModule("1080p")
        self.apps = []
    
    def install_app(self, app_name):
        self.apps.append(app_name)
        return f"已安装应用: {app_name}"
    
    def make_call(self, number):
        if self.power_on:
            return f"正在拨打 {number}"
        return "设备未开机，无法拨打电话"
    
    def send_message(self, number, message):
        if self.power_on:
            return f"发送短信到 {number}: {message}"
        return "设备未开机，无法发送短信"
    
    def get_full_status(self):
        status = [super().get_status()]  # 继承的状态
        if self.power_on:
            # 组合模块的状态
            status.append(f"  {self.wifi.get_status()}")
            status.append(f"  {self.bluetooth.get_status()}")
            status.append(f"  {self.camera.get_status()}")
            status.append(f"  已安装应用: {len(self.apps)} 个")
        return "\n".join(status)

# 平板电脑类 - 继承Device，组合不同的模块组合
class Tablet(Device):
    """平板电脑 - 不同的模块组合"""
    def __init__(self, name, model):
        super().__init__(name, model)
        self.wifi = WiFiModule()
        self.bluetooth = BluetoothModule()
        self.camera = CameraModule("4K")  # 更高分辨率
        # 平板没有通话功能，但有其他功能
    
    def draw(self, content):
        if self.power_on:
            return f"在平板上绘制: {content}"
        return "设备未开机，无法绘制"
    
    def read_ebook(self, book_title):
        if self.power_on:
            return f"正在阅读电子书: {book_title}"
        return "设备未开机，无法阅读"
    
    def get_full_status(self):
        status = [super().get_status()]
        if self.power_on:
            status.append(f"  {self.wifi.get_status()}")
            status.append(f"  {self.bluetooth.get_status()}")
            status.append(f"  {self.camera.get_status()}")
        return "\n".join(status)

print("--- 混合使用示例 ---")

# 创建智能手机
phone = SmartPhone("iPhone", "14 Pro")
print(phone.turn_on())
print(phone.wifi.connect("家庭WiFi"))
print(phone.bluetooth.enable())
print(phone.bluetooth.pair_device("AirPods"))
print(phone.camera.take_photo())
print(phone.install_app("微信"))
print(phone.install_app("支付宝"))
print(phone.make_call("10086"))
print()

print("智能手机完整状态:")
print(phone.get_full_status())
print()

# 创建平板电脑
tablet = Tablet("iPad", "Pro 12.9")
print(tablet.turn_on())
print(tablet.wifi.connect("办公室WiFi"))
print(tablet.camera.start_recording())
print(tablet.draw("设计草图"))
print(tablet.read_ebook("Python编程指南"))
print()

print("平板电脑完整状态:")
print(tablet.get_full_status())
print()
```

## 总结和最佳实践

```python
print("=== 组合vs继承总结 ===")
print("""
选择指南:

1. 使用继承的情况:
   - 明确的 "is-a" 关系
   - 需要多态性
   - 子类是父类的特殊化
   - 符合里氏替换原则
   
   示例: Button is-a Widget, Dog is-a Animal

2. 使用组合的情况:
   - "has-a" 关系
   - 需要灵活的功能组合
   - 运行时改变行为
   - 避免深层继承
   
   示例: Car has-a Engine, Player has-a Weapon

3. 混合使用的情况:
   - 基础功能用继承
   - 可选功能用组合
   - 框架设计
   
   示例: SmartPhone extends Device, has WiFiModule

设计原则:

1. 优先考虑组合
   - "组合优于继承" 原则
   - 更灵活，耦合度低
   - 易于测试和维护

2. 谨慎使用继承
   - 确保符合LSP
   - 避免深层继承
   - 考虑接口隔离

3. 实际考虑因素
   - 代码复用需求
   - 性能要求
   - 团队熟悉度
   - 维护成本

最佳实践:

1. 设计阶段
   - 明确关系类型 (is-a vs has-a)
   - 考虑未来扩展性
   - 遵循SOLID原则

2. 实现阶段
   - 保持接口简洁
   - 使用抽象基类定义契约
   - 合理使用Mixin

3. 维护阶段
   - 定期重构
   - 监控继承深度
   - 评估组合复杂度

记住：没有银弹，根据具体情况选择最合适的方案！
""")
```

## 学习要点

1. **关系理解**：区分"is-a"（继承）和"has-a"（组合）关系
2. **优缺点分析**：理解继承和组合各自的优势和局限性
3. **设计原则**：掌握里氏替换原则和"组合优于继承"原则
4. **选择指南**：根据具体场景选择合适的设计方案
5. **混合使用**：学会在同一个设计中合理结合继承和组合
6. **实际应用**：通过具体例子理解不同场景的最佳实践
7. **重构技巧**：知道何时从继承重构为组合，或反之

## 注意事项

- 继承创建强耦合，组合创建松耦合
- 继承在编译时确定，组合可以在运行时改变
- 过度使用继承会导致脆弱的基类问题
- 过度使用组合会增加代码复杂性
- 要根据具体需求和约束做出权衡
- 定期审查和重构设计决策