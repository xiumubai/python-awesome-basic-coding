# 封装练习题

本文档包含了一系列封装相关的练习题，帮助你巩固和应用所学的封装知识。

## 学习目标

- 综合运用封装的各种技术
- 设计合理的类接口
- 实现数据保护和验证
- 掌握面向对象设计原则

## 练习1：学生管理系统

设计一个学生管理系统，要求使用封装技术保护学生数据。

```python
class Student:
    """学生类 - 练习封装基础"""
    
    def __init__(self, student_id, name, age):
        self._student_id = student_id
        self._name = name
        self._age = age
        self._grades = {}
        self._gpa = 0.0
    
    @property
    def student_id(self):
        """学号（只读）"""
        return self._student_id
    
    @property
    def name(self):
        """姓名"""
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("姓名必须是非空字符串")
        self._name = value.strip()
    
    @property
    def age(self):
        """年龄"""
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0 or value > 150:
            raise ValueError("年龄必须是0-150之间的整数")
        self._age = value
    
    @property
    def gpa(self):
        """GPA（只读，自动计算）"""
        return self._gpa
    
    def add_grade(self, subject, grade):
        """添加成绩"""
        if not isinstance(subject, str) or len(subject.strip()) == 0:
            raise ValueError("科目名称必须是非空字符串")
        
        if not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
            raise ValueError("成绩必须是0-100之间的数字")
        
        self._grades[subject.strip()] = float(grade)
        self._calculate_gpa()
    
    def _calculate_gpa(self):
        """计算GPA（私有方法）"""
        if not self._grades:
            self._gpa = 0.0
            return
        
        total_points = 0.0
        for grade in self._grades.values():
            if grade >= 90:
                total_points += 4.0
            elif grade >= 80:
                total_points += 3.0
            elif grade >= 70:
                total_points += 2.0
            elif grade >= 60:
                total_points += 1.0
            else:
                total_points += 0.0
        
        self._gpa = round(total_points / len(self._grades), 2)
    
    def get_grades(self):
        """获取成绩副本"""
        return self._grades.copy()
    
    def __str__(self):
        return f"学生[{self._student_id}]: {self._name}, 年龄: {self._age}, GPA: {self._gpa}"

def test_student_system():
    """测试学生管理系统"""
    print("=== 学生管理系统测试 ===")
    
    # 创建学生
    student = Student("2023001", "张三", 20)
    print(f"创建学生: {student}")
    
    # 添加成绩
    student.add_grade("数学", 95)
    student.add_grade("英语", 87)
    student.add_grade("物理", 92)
    print(f"添加成绩后: {student}")
    print(f"成绩详情: {student.get_grades()}")
    
    # 修改信息
    student.name = "李四"
    student.age = 21
    print(f"修改信息后: {student}")
    
    # 错误处理测试
    try:
        student.age = -5
    except ValueError as e:
        print(f"年龄验证错误: {e}")
    
    try:
        student.add_grade("化学", 150)
    except ValueError as e:
        print(f"成绩验证错误: {e}")

test_student_system()
```

## 练习2：图书管理系统

设计一个图书管理系统，实现图书的借阅和归还功能。

```python
from datetime import datetime, timedelta
from enum import Enum

class BookStatus(Enum):
    """图书状态枚举"""
    AVAILABLE = "可借阅"
    BORROWED = "已借出"
    RESERVED = "已预约"
    MAINTENANCE = "维护中"

class Book:
    """图书类"""
    
    def __init__(self, isbn, title, author, category):
        self._isbn = isbn
        self._title = title
        self._author = author
        self._category = category
        self._status = BookStatus.AVAILABLE
        self._borrower = None
        self._borrow_date = None
        self._due_date = None
        self._borrow_count = 0
    
    @property
    def isbn(self):
        """ISBN（只读）"""
        return self._isbn
    
    @property
    def title(self):
        """书名"""
        return self._title
    
    @property
    def author(self):
        """作者"""
        return self._author
    
    @property
    def status(self):
        """状态（只读）"""
        return self._status
    
    @property
    def borrower(self):
        """借阅者（只读）"""
        return self._borrower
    
    @property
    def borrow_count(self):
        """借阅次数（只读）"""
        return self._borrow_count
    
    def is_available(self):
        """检查是否可借阅"""
        return self._status == BookStatus.AVAILABLE
    
    def borrow(self, borrower_name, days=30):
        """借阅图书"""
        if not self.is_available():
            raise ValueError(f"图书当前状态为{self._status.value}，无法借阅")
        
        if not isinstance(borrower_name, str) or len(borrower_name.strip()) == 0:
            raise ValueError("借阅者姓名不能为空")
        
        if not isinstance(days, int) or days <= 0 or days > 90:
            raise ValueError("借阅天数必须是1-90之间的整数")
        
        self._status = BookStatus.BORROWED
        self._borrower = borrower_name.strip()
        self._borrow_date = datetime.now()
        self._due_date = self._borrow_date + timedelta(days=days)
        self._borrow_count += 1
    
    def return_book(self):
        """归还图书"""
        if self._status != BookStatus.BORROWED:
            raise ValueError("图书未被借出，无法归还")
        
        self._status = BookStatus.AVAILABLE
        self._borrower = None
        self._borrow_date = None
        self._due_date = None
    
    def is_overdue(self):
        """检查是否逾期"""
        if self._status != BookStatus.BORROWED:
            return False
        return datetime.now() > self._due_date
    
    def get_borrow_info(self):
        """获取借阅信息"""
        if self._status != BookStatus.BORROWED:
            return None
        
        return {
            'borrower': self._borrower,
            'borrow_date': self._borrow_date.strftime('%Y-%m-%d'),
            'due_date': self._due_date.strftime('%Y-%m-%d'),
            'is_overdue': self.is_overdue()
        }
    
    def __str__(self):
        return f"《{self._title}》- {self._author} [{self._status.value}]"

def test_library_system():
    """测试图书管理系统"""
    print("\n=== 图书管理系统测试 ===")
    
    # 创建图书
    book = Book("978-7-111-12345-6", "Python编程", "张三", "计算机")
    print(f"创建图书: {book}")
    
    # 借阅图书
    book.borrow("李四", 14)
    print(f"借阅后: {book}")
    print(f"借阅信息: {book.get_borrow_info()}")
    
    # 尝试重复借阅
    try:
        book.borrow("王五", 7)
    except ValueError as e:
        print(f"重复借阅错误: {e}")
    
    # 归还图书
    book.return_book()
    print(f"归还后: {book}")
    print(f"总借阅次数: {book.borrow_count}")

test_library_system()
```

## 练习3：电商订单系统

设计一个电商订单系统，实现订单状态管理和金额计算。

```python
import uuid
from datetime import datetime
from enum import Enum
from decimal import Decimal, ROUND_HALF_UP

class OrderStatus(Enum):
    """订单状态枚举"""
    PENDING = "待付款"
    PAID = "已付款"
    SHIPPED = "已发货"
    DELIVERED = "已送达"
    CANCELLED = "已取消"
    REFUNDED = "已退款"

class OrderItem:
    """订单项类"""
    
    def __init__(self, product_name, price, quantity):
        self._product_name = product_name
        self._price = Decimal(str(price))
        self._quantity = int(quantity)
        
        if self._price < 0:
            raise ValueError("商品价格不能为负数")
        if self._quantity <= 0:
            raise ValueError("商品数量必须大于0")
    
    @property
    def product_name(self):
        return self._product_name
    
    @property
    def price(self):
        return self._price
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("商品数量必须是正整数")
        self._quantity = value
    
    @property
    def subtotal(self):
        """小计金额"""
        return self._price * self._quantity
    
    def __str__(self):
        return f"{self._product_name} x{self._quantity} = ¥{self.subtotal}"

class Order:
    """订单类"""
    
    def __init__(self, customer_name):
        self._order_id = str(uuid.uuid4())[:8].upper()
        self._customer_name = customer_name
        self._items = []
        self._status = OrderStatus.PENDING
        self._create_time = datetime.now()
        self._discount = Decimal('0')
        self._shipping_fee = Decimal('0')
    
    @property
    def order_id(self):
        """订单ID（只读）"""
        return self._order_id
    
    @property
    def customer_name(self):
        """客户姓名"""
        return self._customer_name
    
    @property
    def status(self):
        """订单状态（只读）"""
        return self._status
    
    @property
    def create_time(self):
        """创建时间（只读）"""
        return self._create_time
    
    @property
    def discount(self):
        """折扣金额"""
        return self._discount
    
    @discount.setter
    def discount(self, value):
        discount_amount = Decimal(str(value))
        if discount_amount < 0:
            raise ValueError("折扣金额不能为负数")
        if discount_amount > self.subtotal:
            raise ValueError("折扣金额不能超过商品总额")
        self._discount = discount_amount
    
    @property
    def shipping_fee(self):
        """运费"""
        return self._shipping_fee
    
    @shipping_fee.setter
    def shipping_fee(self, value):
        fee = Decimal(str(value))
        if fee < 0:
            raise ValueError("运费不能为负数")
        self._shipping_fee = fee
    
    def add_item(self, product_name, price, quantity):
        """添加订单项"""
        if self._status != OrderStatus.PENDING:
            raise ValueError(f"订单状态为{self._status.value}，无法修改")
        
        item = OrderItem(product_name, price, quantity)
        self._items.append(item)
    
    def remove_item(self, product_name):
        """移除订单项"""
        if self._status != OrderStatus.PENDING:
            raise ValueError(f"订单状态为{self._status.value}，无法修改")
        
        self._items = [item for item in self._items if item.product_name != product_name]
    
    @property
    def subtotal(self):
        """商品小计"""
        return sum(item.subtotal for item in self._items)
    
    @property
    def total(self):
        """订单总额"""
        total = self.subtotal - self._discount + self._shipping_fee
        return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    def pay(self):
        """支付订单"""
        if self._status != OrderStatus.PENDING:
            raise ValueError(f"订单状态为{self._status.value}，无法支付")
        
        if not self._items:
            raise ValueError("订单为空，无法支付")
        
        self._status = OrderStatus.PAID
    
    def ship(self):
        """发货"""
        if self._status != OrderStatus.PAID:
            raise ValueError(f"订单状态为{self._status.value}，无法发货")
        
        self._status = OrderStatus.SHIPPED
    
    def deliver(self):
        """确认收货"""
        if self._status != OrderStatus.SHIPPED:
            raise ValueError(f"订单状态为{self._status.value}，无法确认收货")
        
        self._status = OrderStatus.DELIVERED
    
    def cancel(self):
        """取消订单"""
        if self._status in [OrderStatus.SHIPPED, OrderStatus.DELIVERED]:
            raise ValueError(f"订单状态为{self._status.value}，无法取消")
        
        self._status = OrderStatus.CANCELLED
    
    def get_items(self):
        """获取订单项列表"""
        return self._items.copy()
    
    def __str__(self):
        return f"订单[{self._order_id}] - {self._customer_name} - {self._status.value} - ¥{self.total}"

def test_order_system():
    """测试订单系统"""
    print("\n=== 电商订单系统测试 ===")
    
    # 创建订单
    order = Order("张三")
    print(f"创建订单: {order}")
    
    # 添加商品
    order.add_item("Python编程书籍", 89.9, 2)
    order.add_item("编程键盘", 299.0, 1)
    print(f"添加商品后: {order}")
    
    # 设置折扣和运费
    order.discount = 20
    order.shipping_fee = 15
    print(f"设置折扣和运费后: {order}")
    
    # 显示订单详情
    print("\n订单详情:")
    for item in order.get_items():
        print(f"  {item}")
    print(f"  小计: ¥{order.subtotal}")
    print(f"  折扣: -¥{order.discount}")
    print(f"  运费: +¥{order.shipping_fee}")
    print(f"  总计: ¥{order.total}")
    
    # 订单流程
    order.pay()
    print(f"\n支付后: {order}")
    
    order.ship()
    print(f"发货后: {order}")
    
    order.deliver()
    print(f"确认收货后: {order}")
    
    # 错误处理测试
    try:
        order.cancel()
    except ValueError as e:
        print(f"\n取消订单错误: {e}")

test_order_system()
```

## 练习4：智能家居控制系统

设计一个智能家居控制系统，实现设备管理和场景控制。

```python
from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
import json

class DeviceType(Enum):
    """设备类型枚举"""
    LIGHT = "灯光"
    AIR_CONDITIONER = "空调"
    CURTAIN = "窗帘"
    SPEAKER = "音响"
    CAMERA = "摄像头"

class DeviceStatus(Enum):
    """设备状态枚举"""
    ONLINE = "在线"
    OFFLINE = "离线"
    ERROR = "故障"

class SmartDevice(ABC):
    """智能设备抽象基类"""
    
    def __init__(self, device_id, name, device_type):
        self._device_id = device_id
        self._name = name
        self._device_type = device_type
        self._status = DeviceStatus.OFFLINE
        self._is_on = False
        self._last_update = datetime.now()
    
    @property
    def device_id(self):
        """设备ID（只读）"""
        return self._device_id
    
    @property
    def name(self):
        """设备名称"""
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("设备名称不能为空")
        self._name = value.strip()
    
    @property
    def device_type(self):
        """设备类型（只读）"""
        return self._device_type
    
    @property
    def status(self):
        """设备状态（只读）"""
        return self._status
    
    @property
    def is_on(self):
        """开关状态（只读）"""
        return self._is_on
    
    def connect(self):
        """连接设备"""
        self._status = DeviceStatus.ONLINE
        self._last_update = datetime.now()
    
    def disconnect(self):
        """断开设备"""
        self._status = DeviceStatus.OFFLINE
        self._is_on = False
        self._last_update = datetime.now()
    
    def turn_on(self):
        """开启设备"""
        if self._status != DeviceStatus.ONLINE:
            raise ValueError(f"设备{self._status.value}，无法开启")
        self._is_on = True
        self._last_update = datetime.now()
    
    def turn_off(self):
        """关闭设备"""
        if self._status != DeviceStatus.ONLINE:
            raise ValueError(f"设备{self._status.value}，无法关闭")
        self._is_on = False
        self._last_update = datetime.now()
    
    @abstractmethod
    def get_device_info(self):
        """获取设备信息（抽象方法）"""
        pass
    
    def __str__(self):
        state = "开启" if self._is_on else "关闭"
        return f"{self._device_type.value}[{self._name}] - {self._status.value} - {state}"

class SmartLight(SmartDevice):
    """智能灯光"""
    
    def __init__(self, device_id, name):
        super().__init__(device_id, name, DeviceType.LIGHT)
        self._brightness = 100  # 亮度 0-100
        self._color = "白色"
    
    @property
    def brightness(self):
        """亮度"""
        return self._brightness
    
    @brightness.setter
    def brightness(self, value):
        if not isinstance(value, int) or value < 0 or value > 100:
            raise ValueError("亮度必须是0-100之间的整数")
        self._brightness = value
        self._last_update = datetime.now()
    
    @property
    def color(self):
        """颜色"""
        return self._color
    
    @color.setter
    def color(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("颜色不能为空")
        self._color = value.strip()
        self._last_update = datetime.now()
    
    def get_device_info(self):
        return {
            'device_id': self._device_id,
            'name': self._name,
            'type': self._device_type.value,
            'status': self._status.value,
            'is_on': self._is_on,
            'brightness': self._brightness,
            'color': self._color,
            'last_update': self._last_update.strftime('%Y-%m-%d %H:%M:%S')
        }

class Scene:
    """场景类"""
    
    def __init__(self, scene_id, name):
        self._scene_id = scene_id
        self._name = name
        self._device_settings = {}  # 设备ID -> 设置
        self._is_active = False
    
    @property
    def scene_id(self):
        """场景ID（只读）"""
        return self._scene_id
    
    @property
    def name(self):
        """场景名称"""
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("场景名称不能为空")
        self._name = value.strip()
    
    @property
    def is_active(self):
        """是否激活（只读）"""
        return self._is_active
    
    def add_device_setting(self, device_id, settings):
        """添加设备设置"""
        if not isinstance(settings, dict):
            raise ValueError("设备设置必须是字典类型")
        self._device_settings[device_id] = settings.copy()
    
    def remove_device_setting(self, device_id):
        """移除设备设置"""
        if device_id in self._device_settings:
            del self._device_settings[device_id]
    
    def get_device_settings(self):
        """获取设备设置副本"""
        return self._device_settings.copy()
    
    def activate(self, devices):
        """激活场景"""
        for device_id, settings in self._device_settings.items():
            if device_id in devices:
                device = devices[device_id]
                try:
                    # 应用设备设置
                    if 'is_on' in settings:
                        if settings['is_on']:
                            device.turn_on()
                        else:
                            device.turn_off()
                    
                    # 应用特定设备属性
                    if isinstance(device, SmartLight):
                        if 'brightness' in settings:
                            device.brightness = settings['brightness']
                        if 'color' in settings:
                            device.color = settings['color']
                
                except Exception as e:
                    print(f"设备{device_id}设置失败: {e}")
        
        self._is_active = True
    
    def deactivate(self):
        """停用场景"""
        self._is_active = False
    
    def __str__(self):
        status = "激活" if self._is_active else "未激活"
        return f"场景[{self._name}] - {status} - {len(self._device_settings)}个设备"

class SmartHome:
    """智能家居系统"""
    
    def __init__(self, home_name):
        self._home_name = home_name
        self._devices = {}  # 设备ID -> 设备对象
        self._scenes = {}   # 场景ID -> 场景对象
        self._active_scene = None
    
    @property
    def home_name(self):
        """家庭名称"""
        return self._home_name
    
    @property
    def active_scene(self):
        """当前激活场景（只读）"""
        return self._active_scene
    
    def add_device(self, device):
        """添加设备"""
        if not isinstance(device, SmartDevice):
            raise ValueError("必须是SmartDevice的实例")
        
        if device.device_id in self._devices:
            raise ValueError(f"设备ID {device.device_id} 已存在")
        
        self._devices[device.device_id] = device
        device.connect()
    
    def remove_device(self, device_id):
        """移除设备"""
        if device_id in self._devices:
            self._devices[device_id].disconnect()
            del self._devices[device_id]
    
    def get_device(self, device_id):
        """获取设备"""
        return self._devices.get(device_id)
    
    def get_all_devices(self):
        """获取所有设备"""
        return list(self._devices.values())
    
    def add_scene(self, scene):
        """添加场景"""
        if not isinstance(scene, Scene):
            raise ValueError("必须是Scene的实例")
        
        if scene.scene_id in self._scenes:
            raise ValueError(f"场景ID {scene.scene_id} 已存在")
        
        self._scenes[scene.scene_id] = scene
    
    def activate_scene(self, scene_id):
        """激活场景"""
        if scene_id not in self._scenes:
            raise ValueError(f"场景ID {scene_id} 不存在")
        
        # 停用当前场景
        if self._active_scene:
            self._active_scene.deactivate()
        
        # 激活新场景
        scene = self._scenes[scene_id]
        scene.activate(self._devices)
        self._active_scene = scene
    
    def get_system_status(self):
        """获取系统状态"""
        online_devices = sum(1 for device in self._devices.values() 
                           if device.status == DeviceStatus.ONLINE)
        
        return {
            'home_name': self._home_name,
            'total_devices': len(self._devices),
            'online_devices': online_devices,
            'total_scenes': len(self._scenes),
            'active_scene': self._active_scene.name if self._active_scene else None
        }
    
    def __str__(self):
        return f"智能家居[{self._home_name}] - {len(self._devices)}个设备 - {len(self._scenes)}个场景"

def test_smart_home_system():
    """测试智能家居系统"""
    print("\n=== 智能家居控制系统测试 ===")
    
    # 创建智能家居系统
    home = SmartHome("我的家")
    print(f"创建系统: {home}")
    
    # 添加设备
    living_room_light = SmartLight("light_001", "客厅主灯")
    bedroom_light = SmartLight("light_002", "卧室台灯")
    
    home.add_device(living_room_light)
    home.add_device(bedroom_light)
    print(f"\n添加设备后: {home}")
    
    # 控制设备
    living_room_light.turn_on()
    living_room_light.brightness = 80
    living_room_light.color = "暖白"
    print(f"客厅灯控制: {living_room_light}")
    
    # 创建场景
    evening_scene = Scene("scene_001", "晚间模式")
    evening_scene.add_device_setting("light_001", {
        'is_on': True,
        'brightness': 50,
        'color': '暖黄'
    })
    evening_scene.add_device_setting("light_002", {
        'is_on': True,
        'brightness': 30,
        'color': '暖白'
    })
    
    home.add_scene(evening_scene)
    print(f"\n创建场景: {evening_scene}")
    
    # 激活场景
    home.activate_scene("scene_001")
    print(f"\n激活场景后:")
    print(f"  {living_room_light}")
    print(f"  {bedroom_light}")
    
    # 显示系统状态
    status = home.get_system_status()
    print(f"\n系统状态: {json.dumps(status, ensure_ascii=False, indent=2)}")
    
    # 显示设备详情
    print("\n设备详情:")
    for device in home.get_all_devices():
        info = device.get_device_info()
        print(f"  {json.dumps(info, ensure_ascii=False, indent=4)}")

test_smart_home_system()
```

## 练习总结

通过这些练习，你应该掌握了：

### 基础封装技能
- 使用私有属性保护数据
- 实现属性的getter和setter
- 数据验证和错误处理
- 只读属性的实现

### 高级封装技术
- 抽象基类的设计
- 枚举类型的使用
- 复杂业务逻辑的封装
- 状态管理和转换

### 系统设计能力
- 类之间的协作关系
- 接口设计原则
- 数据一致性保证
- 异常处理策略

### 实际应用场景
- 管理系统设计
- 业务流程控制
- 状态机实现
- 配置和设置管理

### 继续练习建议

1. **扩展现有练习**：为每个系统添加更多功能
2. **设计新系统**：尝试设计银行系统、医院管理系统等
3. **重构代码**：改进现有代码的封装性和可维护性
4. **性能优化**：考虑大数据量下的性能问题
5. **测试驱动**：为每个类编写完整的单元测试

记住，良好的封装是面向对象编程的基础，它能让你的代码更加安全、可维护和可扩展。

## 运行所有测试

```python
if __name__ == "__main__":
    print("封装练习题演示")
    print("=" * 50)
    
    # 运行所有测试
    test_student_system()
    test_library_system()
    test_order_system()
    test_smart_home_system()
    
    print("\n" + "=" * 50)
    print("所有练习演示完成！")
    print("\n封装练习总结:")
    print("1. 学生管理系统 - 基础封装和数据验证")
    print("2. 图书管理系统 - 状态管理和业务流程")
    print("3. 电商订单系统 - 复杂业务逻辑和金额计算")
    print("4. 智能家居系统 - 抽象设计和系统架构")
    print("\n通过这些练习，你已经掌握了封装的核心技能！")
```