#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
封装练习题

本文件包含了关于封装的各种练习题，从基础到高级，
帮助学习者巩固封装的概念和实践技能。

练习内容：
1. 基础封装练习
2. 属性访问控制练习
3. 数据验证练习
4. 复杂系统设计练习
5. 综合应用练习
"""

import re
import math
from datetime import datetime, date
from typing import List, Dict, Optional, Union
from enum import Enum
from abc import ABC, abstractmethod


# ============================================================================
# 练习1：基础封装 - 学生管理系统
# ============================================================================

class Student:
    """
    练习1：创建一个学生类
    
    要求：
    1. 私有属性：学号(student_id)、姓名(name)、年龄(age)、成绩列表(grades)
    2. 提供适当的getter和setter方法
    3. 实现添加成绩、计算平均分、获取等级等方法
    4. 确保数据的有效性（年龄1-100，成绩0-100）
    """
    
    def __init__(self, student_id: str, name: str, age: int):
        # TODO: 实现初始化方法
        # 提示：使用属性设置器进行验证
        self.student_id = student_id
        self.name = name
        self.age = age
        self._grades = []
    
    @property
    def student_id(self) -> str:
        return self._student_id
    
    @student_id.setter
    def student_id(self, value: str):
        # TODO: 实现学号验证
        # 要求：8位数字
        if not isinstance(value, str):
            raise TypeError("学号必须是字符串")
        if not re.match(r'^\d{8}$', value):
            raise ValueError("学号必须是8位数字")
        self._student_id = value
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        # TODO: 实现姓名验证
        # 要求：非空字符串，长度2-20
        if not isinstance(value, str):
            raise TypeError("姓名必须是字符串")
        if not value.strip():
            raise ValueError("姓名不能为空")
        if not (2 <= len(value.strip()) <= 20):
            raise ValueError("姓名长度必须在2-20个字符之间")
        self._name = value.strip()
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int):
        # TODO: 实现年龄验证
        # 要求：1-100之间的整数
        if not isinstance(value, int):
            raise TypeError("年龄必须是整数")
        if not (1 <= value <= 100):
            raise ValueError("年龄必须在1-100之间")
        self._age = value
    
    def add_grade(self, subject: str, score: float):
        """添加成绩"""
        # TODO: 实现添加成绩方法
        # 要求：验证科目名称和分数（0-100）
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("科目名称不能为空")
        if not isinstance(score, (int, float)):
            raise TypeError("分数必须是数字")
        if not (0 <= score <= 100):
            raise ValueError("分数必须在0-100之间")
        
        self._grades.append({'subject': subject.strip(), 'score': float(score)})
    
    def get_average_score(self) -> float:
        """计算平均分"""
        # TODO: 实现计算平均分
        if not self._grades:
            return 0.0
        total = sum(grade['score'] for grade in self._grades)
        return round(total / len(self._grades), 2)
    
    def get_grade_level(self) -> str:
        """获取等级"""
        # TODO: 实现等级计算
        # A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59
        avg = self.get_average_score()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    
    def get_grades(self) -> List[Dict]:
        """获取成绩列表（只读）"""
        # TODO: 返回成绩列表的副本，防止外部修改
        return self._grades.copy()
    
    def __str__(self):
        return f"Student({self.student_id}, {self.name}, {self.age}岁, 平均分:{self.get_average_score()}, 等级:{self.get_grade_level()})"


# ============================================================================
# 练习2：属性访问控制 - 图书管理系统
# ============================================================================

class BookStatus(Enum):
    """图书状态枚举"""
    AVAILABLE = "可借阅"
    BORROWED = "已借出"
    RESERVED = "已预约"
    MAINTENANCE = "维护中"


class Book:
    """
    练习2：创建图书类
    
    要求：
    1. 使用不同级别的访问控制（公有、保护、私有）
    2. 实现借阅、归还、预约等功能
    3. 记录借阅历史
    4. 确保状态转换的合理性
    """
    
    def __init__(self, isbn: str, title: str, author: str, price: float):
        # 公有属性
        self.isbn = isbn
        self.title = title
        self.author = author
        
        # 保护属性（子类可访问）
        self._price = price
        self._status = BookStatus.AVAILABLE
        self._borrow_count = 0
        
        # 私有属性（仅本类访问）
        self.__borrow_history = []
        self.__current_borrower = None
    
    @property
    def price(self) -> float:
        """价格（只读）"""
        return self._price
    
    @property
    def status(self) -> BookStatus:
        """状态（只读）"""
        return self._status
    
    @property
    def borrow_count(self) -> int:
        """借阅次数（只读）"""
        return self._borrow_count
    
    @property
    def current_borrower(self) -> Optional[str]:
        """当前借阅者（只读）"""
        return self.__current_borrower
    
    def borrow(self, borrower_name: str) -> bool:
        """借阅图书"""
        # TODO: 实现借阅逻辑
        # 要求：只有可借阅状态的图书才能被借出
        if self._status != BookStatus.AVAILABLE:
            print(f"图书《{self.title}》当前状态为{self._status.value}，无法借阅")
            return False
        
        if not isinstance(borrower_name, str) or not borrower_name.strip():
            print("借阅者姓名不能为空")
            return False
        
        self._status = BookStatus.BORROWED
        self.__current_borrower = borrower_name.strip()
        self._borrow_count += 1
        
        # 记录借阅历史
        self.__borrow_history.append({
            'borrower': borrower_name.strip(),
            'borrow_date': datetime.now(),
            'return_date': None
        })
        
        print(f"图书《{self.title}》已借给{borrower_name}")
        return True
    
    def return_book(self) -> bool:
        """归还图书"""
        # TODO: 实现归还逻辑
        if self._status != BookStatus.BORROWED:
            print(f"图书《{self.title}》当前状态为{self._status.value}，无需归还")
            return False
        
        # 更新借阅历史
        if self.__borrow_history:
            self.__borrow_history[-1]['return_date'] = datetime.now()
        
        self._status = BookStatus.AVAILABLE
        borrower = self.__current_borrower
        self.__current_borrower = None
        
        print(f"图书《{self.title}》已由{borrower}归还")
        return True
    
    def reserve(self, reserver_name: str) -> bool:
        """预约图书"""
        # TODO: 实现预约逻辑
        # 要求：只有已借出的图书才能被预约
        if self._status != BookStatus.BORROWED:
            print(f"图书《{self.title}》当前状态为{self._status.value}，无法预约")
            return False
        
        if not isinstance(reserver_name, str) or not reserver_name.strip():
            print("预约者姓名不能为空")
            return False
        
        self._status = BookStatus.RESERVED
        print(f"图书《{self.title}》已被{reserver_name}预约")
        return True
    
    def get_borrow_history(self) -> List[Dict]:
        """获取借阅历史（只读）"""
        # TODO: 返回借阅历史的副本
        return self.__borrow_history.copy()
    
    def _set_maintenance(self, reason: str = "维护"):
        """设置维护状态（保护方法，子类可调用）"""
        if self._status == BookStatus.BORROWED:
            print("图书正在借阅中，无法设置为维护状态")
            return False
        
        self._status = BookStatus.MAINTENANCE
        print(f"图书《{self.title}》已设置为维护状态：{reason}")
        return True
    
    def _restore_from_maintenance(self):
        """从维护状态恢复（保护方法）"""
        if self._status == BookStatus.MAINTENANCE:
            self._status = BookStatus.AVAILABLE
            print(f"图书《{self.title}》已从维护状态恢复")
            return True
        return False
    
    def __str__(self):
        return f"Book(《{self.title}》, {self.author}, {self._status.value})"


# ============================================================================
# 练习3：数据验证 - 电商订单系统
# ============================================================================

class OrderStatus(Enum):
    """订单状态"""
    PENDING = "待支付"
    PAID = "已支付"
    SHIPPED = "已发货"
    DELIVERED = "已送达"
    CANCELLED = "已取消"


class OrderItem:
    """订单项"""
    
    def __init__(self, product_name: str, price: float, quantity: int):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
    
    @property
    def product_name(self) -> str:
        return self._product_name
    
    @product_name.setter
    def product_name(self, value: str):
        # TODO: 验证商品名称
        if not isinstance(value, str) or not value.strip():
            raise ValueError("商品名称不能为空")
        if len(value.strip()) > 100:
            raise ValueError("商品名称长度不能超过100个字符")
        self._product_name = value.strip()
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float):
        # TODO: 验证价格
        if not isinstance(value, (int, float)):
            raise TypeError("价格必须是数字")
        if value < 0:
            raise ValueError("价格不能为负数")
        if value > 100000:
            raise ValueError("价格不能超过100000")
        self._price = float(value)
    
    @property
    def quantity(self) -> int:
        return self._quantity
    
    @quantity.setter
    def quantity(self, value: int):
        # TODO: 验证数量
        if not isinstance(value, int):
            raise TypeError("数量必须是整数")
        if value <= 0:
            raise ValueError("数量必须大于0")
        if value > 1000:
            raise ValueError("数量不能超过1000")
        self._quantity = value
    
    @property
    def total_price(self) -> float:
        """计算总价"""
        return round(self._price * self._quantity, 2)
    
    def __str__(self):
        return f"OrderItem({self.product_name}, ¥{self.price}, {self.quantity}件)"


class Order:
    """
    练习3：创建订单类
    
    要求：
    1. 严格的数据验证
    2. 状态管理和转换控制
    3. 订单项管理
    4. 价格计算和优惠处理
    """
    
    def __init__(self, order_id: str, customer_name: str, customer_email: str):
        self.order_id = order_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self._items = []
        self._status = OrderStatus.PENDING
        self._discount_rate = 0.0
        self._created_at = datetime.now()
        self._status_history = [{'status': OrderStatus.PENDING, 'timestamp': self._created_at}]
    
    @property
    def order_id(self) -> str:
        return self._order_id
    
    @order_id.setter
    def order_id(self, value: str):
        # TODO: 验证订单ID
        # 格式：ORD + 8位数字
        if not isinstance(value, str):
            raise TypeError("订单ID必须是字符串")
        if not re.match(r'^ORD\d{8}$', value):
            raise ValueError("订单ID格式错误，应为ORD+8位数字")
        self._order_id = value
    
    @property
    def customer_name(self) -> str:
        return self._customer_name
    
    @customer_name.setter
    def customer_name(self, value: str):
        # TODO: 验证客户姓名
        if not isinstance(value, str) or not value.strip():
            raise ValueError("客户姓名不能为空")
        if len(value.strip()) > 50:
            raise ValueError("客户姓名长度不能超过50个字符")
        self._customer_name = value.strip()
    
    @property
    def customer_email(self) -> str:
        return self._customer_email
    
    @customer_email.setter
    def customer_email(self, value: str):
        # TODO: 验证邮箱
        if not isinstance(value, str):
            raise TypeError("邮箱必须是字符串")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValueError("邮箱格式不正确")
        self._customer_email = value.lower().strip()
    
    @property
    def status(self) -> OrderStatus:
        return self._status
    
    @property
    def discount_rate(self) -> float:
        return self._discount_rate
    
    @discount_rate.setter
    def discount_rate(self, value: float):
        # TODO: 验证折扣率
        if not isinstance(value, (int, float)):
            raise TypeError("折扣率必须是数字")
        if not (0 <= value <= 0.5):
            raise ValueError("折扣率必须在0-0.5之间")
        self._discount_rate = float(value)
    
    def add_item(self, product_name: str, price: float, quantity: int):
        """添加订单项"""
        # TODO: 实现添加订单项
        if self._status != OrderStatus.PENDING:
            raise RuntimeError(f"订单状态为{self._status.value}，无法添加商品")
        
        item = OrderItem(product_name, price, quantity)
        self._items.append(item)
        print(f"已添加商品：{item}")
    
    def remove_item(self, product_name: str) -> bool:
        """移除订单项"""
        # TODO: 实现移除订单项
        if self._status != OrderStatus.PENDING:
            print(f"订单状态为{self._status.value}，无法移除商品")
            return False
        
        for i, item in enumerate(self._items):
            if item.product_name == product_name:
                removed_item = self._items.pop(i)
                print(f"已移除商品：{removed_item}")
                return True
        
        print(f"未找到商品：{product_name}")
        return False
    
    def calculate_total(self) -> float:
        """计算订单总价"""
        # TODO: 计算总价（含折扣）
        if not self._items:
            return 0.0
        
        subtotal = sum(item.total_price for item in self._items)
        discount_amount = subtotal * self._discount_rate
        total = subtotal - discount_amount
        return round(total, 2)
    
    def pay(self) -> bool:
        """支付订单"""
        # TODO: 实现支付逻辑
        if self._status != OrderStatus.PENDING:
            print(f"订单状态为{self._status.value}，无法支付")
            return False
        
        if not self._items:
            print("订单为空，无法支付")
            return False
        
        self._change_status(OrderStatus.PAID)
        print(f"订单{self.order_id}支付成功，金额：¥{self.calculate_total()}")
        return True
    
    def ship(self) -> bool:
        """发货"""
        # TODO: 实现发货逻辑
        if self._status != OrderStatus.PAID:
            print(f"订单状态为{self._status.value}，无法发货")
            return False
        
        self._change_status(OrderStatus.SHIPPED)
        print(f"订单{self.order_id}已发货")
        return True
    
    def deliver(self) -> bool:
        """确认送达"""
        # TODO: 实现送达逻辑
        if self._status != OrderStatus.SHIPPED:
            print(f"订单状态为{self._status.value}，无法确认送达")
            return False
        
        self._change_status(OrderStatus.DELIVERED)
        print(f"订单{self.order_id}已送达")
        return True
    
    def cancel(self) -> bool:
        """取消订单"""
        # TODO: 实现取消逻辑
        if self._status in [OrderStatus.SHIPPED, OrderStatus.DELIVERED]:
            print(f"订单状态为{self._status.value}，无法取消")
            return False
        
        self._change_status(OrderStatus.CANCELLED)
        print(f"订单{self.order_id}已取消")
        return True
    
    def _change_status(self, new_status: OrderStatus):
        """改变订单状态（私有方法）"""
        self._status = new_status
        self._status_history.append({
            'status': new_status,
            'timestamp': datetime.now()
        })
    
    def get_items(self) -> List[OrderItem]:
        """获取订单项列表（只读）"""
        return self._items.copy()
    
    def get_status_history(self) -> List[Dict]:
        """获取状态历史（只读）"""
        return self._status_history.copy()
    
    def __str__(self):
        return f"Order({self.order_id}, {self.customer_name}, {self._status.value}, ¥{self.calculate_total()})"


# ============================================================================
# 练习4：综合应用 - 智能家居控制系统
# ============================================================================

class Device(ABC):
    """设备抽象基类"""
    
    def __init__(self, device_id: str, name: str):
        self._device_id = device_id
        self._name = name
        self._is_on = False
        self._last_operation = None
    
    @property
    def device_id(self) -> str:
        return self._device_id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def is_on(self) -> bool:
        return self._is_on
    
    @abstractmethod
    def turn_on(self):
        """开启设备"""
        pass
    
    @abstractmethod
    def turn_off(self):
        """关闭设备"""
        pass
    
    @abstractmethod
    def get_status(self) -> Dict:
        """获取设备状态"""
        pass


class SmartLight(Device):
    """智能灯泡"""
    
    def __init__(self, device_id: str, name: str):
        super().__init__(device_id, name)
        self._brightness = 0  # 0-100
        self._color = "white"
    
    @property
    def brightness(self) -> int:
        return self._brightness
    
    @brightness.setter
    def brightness(self, value: int):
        # TODO: 验证亮度值
        if not isinstance(value, int):
            raise TypeError("亮度必须是整数")
        if not (0 <= value <= 100):
            raise ValueError("亮度必须在0-100之间")
        self._brightness = value
        if value > 0 and not self._is_on:
            self._is_on = True
        elif value == 0:
            self._is_on = False
    
    @property
    def color(self) -> str:
        return self._color
    
    @color.setter
    def color(self, value: str):
        # TODO: 验证颜色
        valid_colors = ["white", "red", "green", "blue", "yellow", "purple", "orange"]
        if not isinstance(value, str):
            raise TypeError("颜色必须是字符串")
        if value.lower() not in valid_colors:
            raise ValueError(f"颜色必须是以下之一：{valid_colors}")
        self._color = value.lower()
    
    def turn_on(self):
        self._is_on = True
        if self._brightness == 0:
            self._brightness = 50  # 默认亮度
        self._last_operation = datetime.now()
        print(f"智能灯泡 {self._name} 已开启")
    
    def turn_off(self):
        self._is_on = False
        self._brightness = 0
        self._last_operation = datetime.now()
        print(f"智能灯泡 {self._name} 已关闭")
    
    def get_status(self) -> Dict:
        return {
            'device_id': self._device_id,
            'name': self._name,
            'type': 'SmartLight',
            'is_on': self._is_on,
            'brightness': self._brightness,
            'color': self._color,
            'last_operation': self._last_operation
        }


class SmartThermostat(Device):
    """智能温控器"""
    
    def __init__(self, device_id: str, name: str):
        super().__init__(device_id, name)
        self._target_temperature = 22.0  # 目标温度
        self._current_temperature = 20.0  # 当前温度
        self._mode = "auto"  # auto, heat, cool, off
    
    @property
    def target_temperature(self) -> float:
        return self._target_temperature
    
    @target_temperature.setter
    def target_temperature(self, value: float):
        # TODO: 验证目标温度
        if not isinstance(value, (int, float)):
            raise TypeError("温度必须是数字")
        if not (10 <= value <= 35):
            raise ValueError("温度必须在10-35度之间")
        self._target_temperature = float(value)
    
    @property
    def current_temperature(self) -> float:
        return self._current_temperature
    
    @property
    def mode(self) -> str:
        return self._mode
    
    @mode.setter
    def mode(self, value: str):
        # TODO: 验证模式
        valid_modes = ["auto", "heat", "cool", "off"]
        if not isinstance(value, str):
            raise TypeError("模式必须是字符串")
        if value.lower() not in valid_modes:
            raise ValueError(f"模式必须是以下之一：{valid_modes}")
        self._mode = value.lower()
        if value.lower() == "off":
            self._is_on = False
        else:
            self._is_on = True
    
    def turn_on(self):
        self._is_on = True
        if self._mode == "off":
            self._mode = "auto"
        self._last_operation = datetime.now()
        print(f"智能温控器 {self._name} 已开启")
    
    def turn_off(self):
        self._is_on = False
        self._mode = "off"
        self._last_operation = datetime.now()
        print(f"智能温控器 {self._name} 已关闭")
    
    def simulate_temperature_change(self):
        """模拟温度变化"""
        if not self._is_on:
            return
        
        if self._mode == "heat" and self._current_temperature < self._target_temperature:
            self._current_temperature += 0.5
        elif self._mode == "cool" and self._current_temperature > self._target_temperature:
            self._current_temperature -= 0.5
        elif self._mode == "auto":
            if self._current_temperature < self._target_temperature - 1:
                self._current_temperature += 0.5
            elif self._current_temperature > self._target_temperature + 1:
                self._current_temperature -= 0.5
    
    def get_status(self) -> Dict:
        return {
            'device_id': self._device_id,
            'name': self._name,
            'type': 'SmartThermostat',
            'is_on': self._is_on,
            'target_temperature': self._target_temperature,
            'current_temperature': self._current_temperature,
            'mode': self._mode,
            'last_operation': self._last_operation
        }


class SmartHome:
    """智能家居控制系统"""
    
    def __init__(self, home_name: str):
        self._home_name = home_name
        self._devices = {}
        self._scenes = {}
        self._is_armed = False  # 安防状态
    
    @property
    def home_name(self) -> str:
        return self._home_name
    
    @property
    def is_armed(self) -> bool:
        return self._is_armed
    
    def add_device(self, device: Device):
        """添加设备"""
        # TODO: 实现添加设备
        if not isinstance(device, Device):
            raise TypeError("必须是Device类型的对象")
        if device.device_id in self._devices:
            raise ValueError(f"设备ID {device.device_id} 已存在")
        
        self._devices[device.device_id] = device
        print(f"设备 {device.name} 已添加到智能家居系统")
    
    def remove_device(self, device_id: str) -> bool:
        """移除设备"""
        # TODO: 实现移除设备
        if device_id in self._devices:
            device = self._devices.pop(device_id)
            print(f"设备 {device.name} 已从智能家居系统移除")
            return True
        print(f"未找到设备ID：{device_id}")
        return False
    
    def get_device(self, device_id: str) -> Optional[Device]:
        """获取设备"""
        return self._devices.get(device_id)
    
    def list_devices(self) -> List[Device]:
        """列出所有设备"""
        return list(self._devices.values())
    
    def create_scene(self, scene_name: str, device_settings: Dict[str, Dict]):
        """创建场景"""
        # TODO: 实现创建场景
        # device_settings格式：{device_id: {setting_name: value, ...}}
        if not isinstance(scene_name, str) or not scene_name.strip():
            raise ValueError("场景名称不能为空")
        
        # 验证设备设置
        for device_id, settings in device_settings.items():
            if device_id not in self._devices:
                raise ValueError(f"设备ID {device_id} 不存在")
        
        self._scenes[scene_name] = device_settings
        print(f"场景 '{scene_name}' 已创建")
    
    def activate_scene(self, scene_name: str) -> bool:
        """激活场景"""
        # TODO: 实现激活场景
        if scene_name not in self._scenes:
            print(f"场景 '{scene_name}' 不存在")
            return False
        
        scene_settings = self._scenes[scene_name]
        print(f"正在激活场景 '{scene_name}'...")
        
        for device_id, settings in scene_settings.items():
            device = self._devices.get(device_id)
            if device:
                try:
                    for setting_name, value in settings.items():
                        if hasattr(device, setting_name):
                            setattr(device, setting_name, value)
                        elif setting_name == "turn_on" and value:
                            device.turn_on()
                        elif setting_name == "turn_off" and value:
                            device.turn_off()
                except Exception as e:
                    print(f"设置设备 {device.name} 时出错：{e}")
        
        print(f"场景 '{scene_name}' 已激活")
        return True
    
    def arm_security(self):
        """开启安防"""
        self._is_armed = True
        print("智能家居安防系统已开启")
    
    def disarm_security(self):
        """关闭安防"""
        self._is_armed = False
        print("智能家居安防系统已关闭")
    
    def get_system_status(self) -> Dict:
        """获取系统状态"""
        device_statuses = {}
        for device_id, device in self._devices.items():
            device_statuses[device_id] = device.get_status()
        
        return {
            'home_name': self._home_name,
            'is_armed': self._is_armed,
            'device_count': len(self._devices),
            'scene_count': len(self._scenes),
            'devices': device_statuses,
            'scenes': list(self._scenes.keys())
        }


# ============================================================================
# 练习测试和演示
# ============================================================================

def test_student_system():
    """测试学生管理系统"""
    print("=" * 60)
    print("练习1：学生管理系统测试")
    print("=" * 60)
    
    try:
        # 创建学生
        student = Student("20230001", "张三", 20)
        print(f"学生创建成功: {student}")
        
        # 添加成绩
        student.add_grade("数学", 95)
        student.add_grade("英语", 87)
        student.add_grade("物理", 92)
        
        print(f"添加成绩后: {student}")
        print(f"成绩列表: {student.get_grades()}")
        
        # 测试验证
        try:
            student.age = -5  # 无效年龄
        except ValueError as e:
            print(f"年龄验证成功: {e}")
        
        try:
            student.add_grade("化学", 105)  # 无效分数
        except ValueError as e:
            print(f"分数验证成功: {e}")
            
    except Exception as e:
        print(f"测试失败: {e}")


def test_book_system():
    """测试图书管理系统"""
    print("\n" + "=" * 60)
    print("练习2：图书管理系统测试")
    print("=" * 60)
    
    # 创建图书
    book = Book("9787111213826", "Python编程：从入门到实践", "埃里克·马瑟斯", 89.0)
    print(f"图书创建成功: {book}")
    
    # 借阅流程
    book.borrow("张三")
    print(f"借阅后状态: {book}")
    
    # 尝试再次借阅
    book.borrow("李四")
    
    # 预约
    book.reserve("李四")
    
    # 归还
    book.return_book()
    print(f"归还后状态: {book}")
    
    # 查看借阅历史
    print("\n借阅历史:")
    for record in book.get_borrow_history():
        borrow_time = record['borrow_date'].strftime('%Y-%m-%d %H:%M:%S')
        return_time = record['return_date'].strftime('%Y-%m-%d %H:%M:%S') if record['return_date'] else "未归还"
        print(f"  借阅者: {record['borrower']}, 借阅时间: {borrow_time}, 归还时间: {return_time}")


def test_order_system():
    """测试订单系统"""
    print("\n" + "=" * 60)
    print("练习3：电商订单系统测试")
    print("=" * 60)
    
    try:
        # 创建订单
        order = Order("ORD12345678", "王五", "wangwu@example.com")
        print(f"订单创建成功: {order}")
        
        # 添加商品
        order.add_item("iPhone 15", 5999.0, 1)
        order.add_item("AirPods Pro", 1999.0, 1)
        order.add_item("保护壳", 99.0, 2)
        
        print(f"添加商品后: {order}")
        
        # 设置折扣
        order.discount_rate = 0.1  # 9折
        print(f"设置折扣后: {order}")
        
        # 订单流程
        order.pay()
        order.ship()
        order.deliver()
        
        # 查看状态历史
        print("\n订单状态历史:")
        for record in order.get_status_history():
            print(f"  {record['timestamp'].strftime('%H:%M:%S')}: {record['status'].value}")
        
        # 测试验证
        try:
            invalid_order = Order("INVALID", "测试", "invalid-email")
        except ValueError as e:
            print(f"\n订单验证成功: {e}")
            
    except Exception as e:
        print(f"测试失败: {e}")


def test_smart_home_system():
    """测试智能家居系统"""
    print("\n" + "=" * 60)
    print("练习4：智能家居控制系统测试")
    print("=" * 60)
    
    # 创建智能家居系统
    home = SmartHome("我的智能家居")
    
    # 创建设备
    living_room_light = SmartLight("light_001", "客厅灯")
    bedroom_light = SmartLight("light_002", "卧室灯")
    thermostat = SmartThermostat("thermo_001", "客厅温控器")
    
    # 添加设备
    home.add_device(living_room_light)
    home.add_device(bedroom_light)
    home.add_device(thermostat)
    
    print(f"\n设备列表:")
    for device in home.list_devices():
        print(f"  {device.name} ({device.device_id})")
    
    # 控制设备
    living_room_light.turn_on()
    living_room_light.brightness = 80
    living_room_light.color = "blue"
    
    thermostat.turn_on()
    thermostat.target_temperature = 25.0
    thermostat.mode = "heat"
    
    # 创建场景
    home.create_scene("晚安模式", {
        "light_001": {"turn_off": True},
        "light_002": {"turn_off": True},
        "thermo_001": {"target_temperature": 22.0, "mode": "auto"}
    })
    
    home.create_scene("回家模式", {
        "light_001": {"turn_on": True, "brightness": 70, "color": "white"},
        "light_002": {"turn_on": True, "brightness": 50},
        "thermo_001": {"target_temperature": 24.0, "mode": "auto"}
    })
    
    # 激活场景
    print("\n激活回家模式:")
    home.activate_scene("回家模式")
    
    # 显示系统状态
    print("\n系统状态:")
    status = home.get_system_status()
    print(f"家庭名称: {status['home_name']}")
    print(f"设备数量: {status['device_count']}")
    print(f"场景数量: {status['scene_count']}")
    print(f"安防状态: {'已开启' if status['is_armed'] else '已关闭'}")
    
    print("\n设备详细状态:")
    for device_id, device_status in status['devices'].items():
        print(f"  {device_status['name']}: {device_status['type']}, 开启状态: {device_status['is_on']}")


def show_exercise_summary():
    """显示练习总结"""
    print("\n" + "=" * 60)
    print("封装练习总结")
    print("=" * 60)
    
    summary = """
通过以上练习，你应该掌握了：

1. 基础封装技能:
   ✓ 使用私有属性保护数据
   ✓ 提供公有接口访问数据
   ✓ 实现数据验证和错误处理
   ✓ 设计合理的类结构

2. 高级封装技术:
   ✓ 属性装饰器的使用
   ✓ 访问控制级别的应用
   ✓ 数据验证装饰器的设计
   ✓ 状态管理和转换控制

3. 系统设计能力:
   ✓ 模块化设计思想
   ✓ 接口设计原则
   ✓ 异常处理策略
   ✓ 代码复用和扩展性

4. 实际应用场景:
   ✓ 学生管理系统
   ✓ 图书管理系统
   ✓ 电商订单系统
   ✓ 智能家居控制系统

继续练习建议:
1. 尝试扩展现有系统的功能
2. 设计自己的封装类
3. 学习更多设计模式
4. 关注代码的可维护性和可测试性

记住：好的封装不仅保护数据，更重要的是提供清晰、易用的接口！
    """
    
    print(summary)


if __name__ == "__main__":
    test_student_system()
    test_book_system()
    test_order_system()
    test_smart_home_system()
    show_exercise_summary()