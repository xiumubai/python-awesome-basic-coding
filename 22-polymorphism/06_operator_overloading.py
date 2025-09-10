#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
运算符重载 - Operator Overloading

运算符重载是多态的一种特殊形式，允许自定义类的对象使用内置运算符。
通过定义特殊方法（魔术方法），可以让自定义对象支持各种运算符操作。

学习目标：
1. 理解运算符重载的概念
2. 掌握常用魔术方法的使用
3. 学会实现算术运算符重载
4. 了解比较运算符重载
5. 掌握容器类型运算符重载
6. 学会字符串表示方法重载
"""

import math
from typing import Union, Iterator


class Vector:
    """向量类 - 演示算术运算符重载"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    # 字符串表示
    def __str__(self) -> str:
        """用户友好的字符串表示"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        """开发者友好的字符串表示"""
        return f"Vector(x={self.x}, y={self.y})"
    
    # 算术运算符重载
    def __add__(self, other: 'Vector') -> 'Vector':
        """向量加法：v1 + v2"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        """向量减法：v1 - v2"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar: Union[float, int]) -> 'Vector':
        """向量数乘：v * scalar"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar: Union[float, int]) -> 'Vector':
        """反向数乘：scalar * v"""
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar: Union[float, int]) -> 'Vector':
        """向量除法：v / scalar"""
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented
    
    def __neg__(self) -> 'Vector':
        """向量取负：-v"""
        return Vector(-self.x, -self.y)
    
    def __abs__(self) -> float:
        """向量模长：abs(v)"""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    # 比较运算符重载
    def __eq__(self, other: 'Vector') -> bool:
        """相等比较：v1 == v2"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __ne__(self, other: 'Vector') -> bool:
        """不等比较：v1 != v2"""
        return not self.__eq__(other)
    
    def __lt__(self, other: 'Vector') -> bool:
        """小于比较（按模长）：v1 < v2"""
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return NotImplemented
    
    def __le__(self, other: 'Vector') -> bool:
        """小于等于比较：v1 <= v2"""
        return self < other or self == other
    
    def __gt__(self, other: 'Vector') -> bool:
        """大于比较：v1 > v2"""
        if isinstance(other, Vector):
            return abs(self) > abs(other)
        return NotImplemented
    
    def __ge__(self, other: 'Vector') -> bool:
        """大于等于比较：v1 >= v2"""
        return self > other or self == other
    
    # 哈希支持
    def __hash__(self) -> int:
        """哈希值计算，使对象可以作为字典键或集合元素"""
        return hash((self.x, self.y))


class Matrix:
    """矩阵类 - 演示更复杂的运算符重载"""
    
    def __init__(self, data: list):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
    
    def __str__(self) -> str:
        """矩阵的字符串表示"""
        lines = []
        for row in self.data:
            lines.append('[' + ', '.join(f'{x:6.2f}' for x in row) + ']')
        return '[\n  ' + '\n  '.join(lines) + '\n]'
    
    def __getitem__(self, key):
        """索引访问：matrix[i][j] 或 matrix[i, j]"""
        if isinstance(key, tuple):
            row, col = key
            return self.data[row][col]
        return self.data[key]
    
    def __setitem__(self, key, value):
        """索引赋值：matrix[i][j] = value"""
        if isinstance(key, tuple):
            row, col = key
            self.data[row][col] = value
        else:
            self.data[key] = value
    
    def __add__(self, other: 'Matrix') -> 'Matrix':
        """矩阵加法"""
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("矩阵维度不匹配")
            
            result = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.data[i][j] + other.data[i][j])
                result.append(row)
            return Matrix(result)
        return NotImplemented
    
    def __mul__(self, other: Union['Matrix', float, int]) -> 'Matrix':
        """矩阵乘法或数乘"""
        if isinstance(other, (int, float)):
            # 数乘
            result = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.data[i][j] * other)
                result.append(row)
            return Matrix(result)
        
        elif isinstance(other, Matrix):
            # 矩阵乘法
            if self.cols != other.rows:
                raise ValueError("矩阵维度不匹配，无法相乘")
            
            result = []
            for i in range(self.rows):
                row = []
                for j in range(other.cols):
                    sum_val = 0
                    for k in range(self.cols):
                        sum_val += self.data[i][k] * other.data[k][j]
                    row.append(sum_val)
                result.append(row)
            return Matrix(result)
        
        return NotImplemented
    
    def __eq__(self, other: 'Matrix') -> bool:
        """矩阵相等比较"""
        if isinstance(other, Matrix):
            return self.data == other.data
        return False


class CustomList:
    """自定义列表类 - 演示容器类型运算符重载"""
    
    def __init__(self, items=None):
        self.items = items or []
    
    def __str__(self) -> str:
        return f"CustomList({self.items})"
    
    def __len__(self) -> int:
        """长度：len(custom_list)"""
        return len(self.items)
    
    def __getitem__(self, index) -> any:
        """索引访问：custom_list[index]"""
        return self.items[index]
    
    def __setitem__(self, index, value) -> None:
        """索引赋值：custom_list[index] = value"""
        self.items[index] = value
    
    def __delitem__(self, index) -> None:
        """删除元素：del custom_list[index]"""
        del self.items[index]
    
    def __contains__(self, item) -> bool:
        """成员测试：item in custom_list"""
        return item in self.items
    
    def __iter__(self) -> Iterator:
        """迭代支持：for item in custom_list"""
        return iter(self.items)
    
    def __add__(self, other: 'CustomList') -> 'CustomList':
        """列表连接：list1 + list2"""
        if isinstance(other, CustomList):
            return CustomList(self.items + other.items)
        return NotImplemented
    
    def __iadd__(self, other: 'CustomList') -> 'CustomList':
        """就地加法：list1 += list2"""
        if isinstance(other, CustomList):
            self.items.extend(other.items)
            return self
        return NotImplemented
    
    def __mul__(self, times: int) -> 'CustomList':
        """重复：custom_list * n"""
        if isinstance(times, int):
            return CustomList(self.items * times)
        return NotImplemented
    
    def append(self, item):
        """添加元素"""
        self.items.append(item)


class Money:
    """货币类 - 演示实际应用中的运算符重载"""
    
    def __init__(self, amount: float, currency: str = "CNY"):
        self.amount = round(amount, 2)
        self.currency = currency
    
    def __str__(self) -> str:
        return f"{self.amount} {self.currency}"
    
    def __repr__(self) -> str:
        return f"Money({self.amount}, '{self.currency}')"
    
    def __add__(self, other: 'Money') -> 'Money':
        """货币加法"""
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"货币类型不匹配: {self.currency} vs {other.currency}")
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented
    
    def __sub__(self, other: 'Money') -> 'Money':
        """货币减法"""
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"货币类型不匹配: {self.currency} vs {other.currency}")
            return Money(self.amount - other.amount, self.currency)
        return NotImplemented
    
    def __mul__(self, factor: Union[int, float]) -> 'Money':
        """货币乘法（如计算税费）"""
        if isinstance(factor, (int, float)):
            return Money(self.amount * factor, self.currency)
        return NotImplemented
    
    def __rmul__(self, factor: Union[int, float]) -> 'Money':
        """反向乘法"""
        return self.__mul__(factor)
    
    def __truediv__(self, divisor: Union[int, float]) -> 'Money':
        """货币除法（如平分费用）"""
        if isinstance(divisor, (int, float)) and divisor != 0:
            return Money(self.amount / divisor, self.currency)
        return NotImplemented
    
    def __eq__(self, other: 'Money') -> bool:
        """相等比较"""
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return False
    
    def __lt__(self, other: 'Money') -> bool:
        """小于比较"""
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"货币类型不匹配: {self.currency} vs {other.currency}")
            return self.amount < other.amount
        return NotImplemented
    
    def __le__(self, other: 'Money') -> bool:
        return self < other or self == other
    
    def __gt__(self, other: 'Money') -> bool:
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"货币类型不匹配: {self.currency} vs {other.currency}")
            return self.amount > other.amount
        return NotImplemented
    
    def __ge__(self, other: 'Money') -> bool:
        return self > other or self == other
    
    def __hash__(self) -> int:
        return hash((self.amount, self.currency))


def demonstrate_vector_operations():
    """演示向量运算符重载"""
    print("=== 向量运算符重载演示 ===")
    
    # 创建向量
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1的模长: {abs(v1):.2f}")
    print(f"v2的模长: {abs(v2):.2f}")
    
    # 算术运算
    print(f"\n算术运算:")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"3 * v2 = {3 * v2}")
    print(f"v1 / 2 = {v1 / 2}")
    print(f"-v1 = {-v1}")
    
    # 比较运算
    print(f"\n比较运算:")
    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 != v2: {v1 != v2}")
    print(f"v1 > v2 (按模长): {v1 > v2}")
    print(f"v1 < v2 (按模长): {v1 < v2}")
    
    # 集合操作
    print(f"\n集合操作:")
    vectors = {v1, v2, Vector(3, 4)}  # 重复的v1会被去重
    print(f"向量集合: {vectors}")
    print(f"集合大小: {len(vectors)}")


def demonstrate_matrix_operations():
    """演示矩阵运算符重载"""
    print("\n=== 矩阵运算符重载演示 ===")
    
    # 创建矩阵
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    
    print(f"矩阵 m1:")
    print(m1)
    print(f"矩阵 m2:")
    print(m2)
    
    # 矩阵加法
    print(f"\n矩阵加法 m1 + m2:")
    print(m1 + m2)
    
    # 数乘
    print(f"\n数乘 m1 * 2:")
    print(m1 * 2)
    
    # 矩阵乘法
    print(f"\n矩阵乘法 m1 * m2:")
    print(m1 * m2)
    
    # 索引访问
    print(f"\n索引访问:")
    print(f"m1[0][1] = {m1[0][1]}")
    print(f"m1[1, 0] = {m1[1, 0]}")
    
    # 修改元素
    m1[0, 0] = 10
    print(f"\n修改后的 m1:")
    print(m1)


def demonstrate_custom_list_operations():
    """演示自定义列表运算符重载"""
    print("\n=== 自定义列表运算符重载演示 ===")
    
    # 创建自定义列表
    list1 = CustomList([1, 2, 3])
    list2 = CustomList([4, 5, 6])
    
    print(f"list1 = {list1}")
    print(f"list2 = {list2}")
    print(f"len(list1) = {len(list1)}")
    
    # 索引操作
    print(f"\n索引操作:")
    print(f"list1[0] = {list1[0]}")
    list1[0] = 10
    print(f"修改后 list1[0] = {list1[0]}")
    
    # 成员测试
    print(f"\n成员测试:")
    print(f"2 in list1: {2 in list1}")
    print(f"10 in list1: {10 in list1}")
    
    # 迭代
    print(f"\n迭代:")
    print("list1中的元素:", end=" ")
    for item in list1:
        print(item, end=" ")
    print()
    
    # 列表连接
    print(f"\n列表连接:")
    list3 = list1 + list2
    print(f"list1 + list2 = {list3}")
    
    # 就地加法
    list1 += CustomList([7, 8])
    print(f"list1 += [7, 8]: {list1}")
    
    # 重复
    list4 = CustomList([1, 2]) * 3
    print(f"[1, 2] * 3 = {list4}")


def demonstrate_money_operations():
    """演示货币运算符重载"""
    print("\n=== 货币运算符重载演示 ===")
    
    # 创建货币对象
    price1 = Money(100.50, "CNY")
    price2 = Money(50.25, "CNY")
    tax_rate = 0.1
    
    print(f"商品1价格: {price1}")
    print(f"商品2价格: {price2}")
    print(f"税率: {tax_rate * 100}%")
    
    # 货币运算
    print(f"\n货币运算:")
    total = price1 + price2
    print(f"总价: {price1} + {price2} = {total}")
    
    tax = total * tax_rate
    print(f"税费: {total} * {tax_rate} = {tax}")
    
    final_price = total + tax
    print(f"含税总价: {total} + {tax} = {final_price}")
    
    # 平分费用
    per_person = final_price / 3
    print(f"三人平分: {final_price} / 3 = {per_person}")
    
    # 比较
    print(f"\n价格比较:")
    print(f"{price1} > {price2}: {price1 > price2}")
    print(f"{price1} == {price2}: {price1 == price2}")
    
    # 货币集合
    prices = {price1, price2, Money(100.50, "CNY")}  # 重复会被去重
    print(f"\n价格集合: {prices}")
    print(f"集合大小: {len(prices)}")


def demonstrate_operator_overloading_benefits():
    """演示运算符重载的好处"""
    print("\n=== 运算符重载的好处 ===")
    
    print("1. 代码更直观和自然")
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    # 使用运算符重载
    result1 = v1 + v2
    print(f"   使用运算符: {v1} + {v2} = {result1}")
    # 不使用运算符重载需要调用方法
    # result2 = v1.add(v2)  # 假设有add方法
    
    print("\n2. 支持链式操作")
    v3 = Vector(1, 1)
    result2 = v1 + v2 + v3
    print(f"   链式操作: {v1} + {v2} + {v3} = {result2}")
    
    print("\n3. 与内置函数兼容")
    vectors = [Vector(1, 0), Vector(0, 1), Vector(1, 1)]
    max_vector = max(vectors)  # 使用__gt__比较
    print(f"   最大向量: {max_vector}")
    
    print("\n4. 支持多态操作")
    def calculate_total_length(shapes):
        """计算所有形状的总长度（这里用向量模长演示）"""
        total = 0
        for shape in shapes:
            total += abs(shape)  # 使用__abs__方法
        return total
    
    total_length = calculate_total_length(vectors)
    print(f"   向量总模长: {total_length:.2f}")


if __name__ == "__main__":
    print("Python 运算符重载学习")
    print("=" * 50)
    
    # 演示各种运算符重载
    demonstrate_vector_operations()
    demonstrate_matrix_operations()
    demonstrate_custom_list_operations()
    demonstrate_money_operations()
    demonstrate_operator_overloading_benefits()
    
    print("\n=== 运算符重载的核心要点 ===")
    print("1. 通过魔术方法实现运算符重载")
    print("2. 让自定义对象支持内置运算符")
    print("3. 提高代码的可读性和直观性")
    print("4. 支持链式操作和复合表达式")
    print("5. 与Python内置函数和语法兼容")
    print("6. 实现多态的重要机制之一")
    print("7. 需要考虑类型检查和错误处理")
    print("8. 遵循Python的运算符语义")