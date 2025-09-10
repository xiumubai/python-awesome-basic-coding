# 运算符重载

## 什么是运算符重载

运算符重载是指为自定义类定义运算符（如+、-、*、/、==、<等）的行为。通过重载运算符，我们可以让自定义对象像内置类型一样使用运算符，这是多态性的一种重要体现。在Python中，运算符重载通过特殊方法（魔术方法）实现。

## 算术运算符重载

### 基本算术运算符

```python
class Vector:
    """二维向量类 - 演示算术运算符重载"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    # 加法运算符 +
    def __add__(self, other):
        """向量加法"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            # 标量加法
            return Vector(self.x + other, self.y + other)
        return NotImplemented
    
    # 右加法运算符（当左操作数不支持加法时调用）
    def __radd__(self, other):
        """右加法"""
        return self.__add__(other)
    
    # 减法运算符 -
    def __sub__(self, other):
        """向量减法"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        return NotImplemented
    
    # 右减法运算符
    def __rsub__(self, other):
        """右减法"""
        if isinstance(other, (int, float)):
            return Vector(other - self.x, other - self.y)
        return NotImplemented
    
    # 乘法运算符 *
    def __mul__(self, other):
        """向量乘法"""
        if isinstance(other, Vector):
            # 点积
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            # 标量乘法
            return Vector(self.x * other, self.y * other)
        return NotImplemented
    
    # 右乘法运算符
    def __rmul__(self, other):
        """右乘法"""
        return self.__mul__(other)
    
    # 除法运算符 /
    def __truediv__(self, other):
        """向量除法"""
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("不能除以零")
            return Vector(self.x / other, self.y / other)
        return NotImplemented
    
    # 整除运算符 //
    def __floordiv__(self, other):
        """向量整除"""
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("不能除以零")
            return Vector(self.x // other, self.y // other)
        return NotImplemented
    
    # 取模运算符 %
    def __mod__(self, other):
        """向量取模"""
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("不能对零取模")
            return Vector(self.x % other, self.y % other)
        return NotImplemented
    
    # 幂运算符 **
    def __pow__(self, other):
        """向量幂运算"""
        if isinstance(other, (int, float)):
            return Vector(self.x ** other, self.y ** other)
        return NotImplemented
    
    # 负号运算符 -
    def __neg__(self):
        """向量取负"""
        return Vector(-self.x, -self.y)
    
    # 正号运算符 +
    def __pos__(self):
        """向量取正"""
        return Vector(self.x, self.y)
    
    # 绝对值运算符 abs()
    def __abs__(self):
        """向量的模长"""
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    # 复合赋值运算符 +=
    def __iadd__(self, other):
        """就地加法"""
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            return self
        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other
            return self
        return NotImplemented
    
    # 复合赋值运算符 -=
    def __isub__(self, other):
        """就地减法"""
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
            return self
        elif isinstance(other, (int, float)):
            self.x -= other
            self.y -= other
            return self
        return NotImplemented
    
    # 复合赋值运算符 *=
    def __imul__(self, other):
        """就地乘法"""
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
            return self
        return NotImplemented
    
    # 复合赋值运算符 /=
    def __itruediv__(self, other):
        """就地除法"""
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("不能除以零")
            self.x /= other
            self.y /= other
            return self
        return NotImplemented
    
    # 字符串表示
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # 相等比较
    def __eq__(self, other):
        if isinstance(other, Vector):
            return abs(self.x - other.x) < 1e-10 and abs(self.y - other.y) < 1e-10
        return False

# 演示向量运算符重载
def demonstrate_vector_operations():
    """演示向量运算符重载"""
    print("=== 向量运算符重载演示 ===")
    
    # 创建向量
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print()
    
    # 算术运算
    print("1. 算术运算:")
    print(f"   v1 + v2 = {v1 + v2}")
    print(f"   v1 - v2 = {v1 - v2}")
    print(f"   v1 * v2 = {v1 * v2}")  # 点积
    print(f"   v1 * 2 = {v1 * 2}")    # 标量乘法
    print(f"   3 * v1 = {3 * v1}")    # 右乘法
    print(f"   v1 / 2 = {v1 / 2}")
    print(f"   v1 // 2 = {v1 // 2}")
    print(f"   v1 % 3 = {v1 % 3}")
    print(f"   v1 ** 2 = {v1 ** 2}")
    print()
    
    # 一元运算
    print("2. 一元运算:")
    print(f"   -v1 = {-v1}")
    print(f"   +v1 = {+v1}")
    print(f"   abs(v1) = {abs(v1):.2f}")
    print()
    
    # 复合赋值运算
    print("3. 复合赋值运算:")
    v3 = Vector(5, 6)
    print(f"   v3 = {v3}")
    
    v3 += v2
    print(f"   v3 += v2 => {v3}")
    
    v3 -= Vector(1, 1)
    print(f"   v3 -= Vector(1, 1) => {v3}")
    
    v3 *= 2
    print(f"   v3 *= 2 => {v3}")
    
    v3 /= 2
    print(f"   v3 /= 2 => {v3}")
    print()
    
    print("=== 演示完成 ===\n")

demonstrate_vector_operations()
```

## 比较运算符重载

### 实现完整的比较操作

```python
from functools import total_ordering

@total_ordering
class Student:
    """学生类 - 演示比较运算符重载"""
    
    def __init__(self, name: str, grade: float, student_id: int):
        self.name = name
        self.grade = grade
        self.student_id = student_id
    
    # 相等比较 ==
    def __eq__(self, other):
        """基于学号判断相等"""
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False
    
    # 小于比较 <
    def __lt__(self, other):
        """基于成绩比较大小"""
        if isinstance(other, Student):
            # 成绩高的学生"更大"
            return self.grade < other.grade
        return NotImplemented
    
    # 哈希值（用于集合和字典）
    def __hash__(self):
        return hash(self.student_id)
    
    def __str__(self):
        return f"Student(name='{self.name}', grade={self.grade}, id={self.student_id})"
    
    def __repr__(self):
        return self.__str__()

class Temperature:
    """温度类 - 演示不同单位的比较"""
    
    def __init__(self, value: float, unit: str = "C"):
        self.value = value
        self.unit = unit.upper()
        if self.unit not in ["C", "F", "K"]:
            raise ValueError("单位必须是 C、F 或 K")
    
    def to_celsius(self) -> float:
        """转换为摄氏度"""
        if self.unit == "C":
            return self.value
        elif self.unit == "F":
            return (self.value - 32) * 5/9
        elif self.unit == "K":
            return self.value - 273.15
    
    def to_fahrenheit(self) -> float:
        """转换为华氏度"""
        celsius = self.to_celsius()
        return celsius * 9/5 + 32
    
    def to_kelvin(self) -> float:
        """转换为开尔文"""
        celsius = self.to_celsius()
        return celsius + 273.15
    
    # 相等比较
    def __eq__(self, other):
        if isinstance(other, Temperature):
            return abs(self.to_celsius() - other.to_celsius()) < 1e-10
        return False
    
    # 小于比较
    def __lt__(self, other):
        if isinstance(other, Temperature):
            return self.to_celsius() < other.to_celsius()
        return NotImplemented
    
    # 小于等于比较
    def __le__(self, other):
        if isinstance(other, Temperature):
            return self.to_celsius() <= other.to_celsius()
        return NotImplemented
    
    # 大于比较
    def __gt__(self, other):
        if isinstance(other, Temperature):
            return self.to_celsius() > other.to_celsius()
        return NotImplemented
    
    # 大于等于比较
    def __ge__(self, other):
        if isinstance(other, Temperature):
            return self.to_celsius() >= other.to_celsius()
        return NotImplemented
    
    # 不等比较
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return f"{self.value}°{self.unit}"
    
    def __repr__(self):
        return f"Temperature({self.value}, '{self.unit}')"

# 演示比较运算符重载
def demonstrate_comparison_operations():
    """演示比较运算符重载"""
    print("=== 比较运算符重载演示 ===")
    
    # 学生比较
    print("1. 学生成绩比较:")
    students = [
        Student("Alice", 85.5, 1001),
        Student("Bob", 92.0, 1002),
        Student("Charlie", 78.5, 1003),
        Student("Diana", 95.5, 1004),
        Student("Eve", 88.0, 1005)
    ]
    
    print("   原始顺序:")
    for student in students:
        print(f"     {student}")
    
    # 排序（基于重载的比较运算符）
    sorted_students = sorted(students)
    print("\n   按成绩排序（从低到高）:")
    for student in sorted_students:
        print(f"     {student}")
    
    # 比较操作
    alice = students[0]
    bob = students[1]
    print(f"\n   比较操作:")
    print(f"     {alice.name} == {bob.name}: {alice == bob}")
    print(f"     {alice.name} < {bob.name}: {alice < bob}")
    print(f"     {alice.name} > {bob.name}: {alice > bob}")
    print(f"     {alice.name} <= {bob.name}: {alice <= bob}")
    print(f"     {alice.name} >= {bob.name}: {alice >= bob}")
    print(f"     {alice.name} != {bob.name}: {alice != bob}")
    
    # 温度比较
    print("\n2. 温度比较:")
    temperatures = [
        Temperature(0, "C"),      # 0°C
        Temperature(32, "F"),     # 32°F = 0°C
        Temperature(100, "C"),    # 100°C
        Temperature(212, "F"),    # 212°F = 100°C
        Temperature(273.15, "K"), # 273.15K = 0°C
        Temperature(373.15, "K")  # 373.15K = 100°C
    ]
    
    print("   温度列表:")
    for temp in temperatures:
        print(f"     {temp} = {temp.to_celsius():.2f}°C")
    
    # 相等性测试
    print("\n   相等性测试:")
    print(f"     0°C == 32°F: {temperatures[0] == temperatures[1]}")
    print(f"     100°C == 212°F: {temperatures[2] == temperatures[3]}")
    print(f"     0°C == 273.15K: {temperatures[0] == temperatures[4]}")
    
    # 排序
    sorted_temps = sorted(temperatures)
    print("\n   按温度排序:")
    for temp in sorted_temps:
        print(f"     {temp} = {temp.to_celsius():.2f}°C")
    
    # 查找最高和最低温度
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    print(f"\n   最低温度: {min_temp} = {min_temp.to_celsius():.2f}°C")
    print(f"   最高温度: {max_temp} = {max_temp.to_celsius():.2f}°C")
    
    print("\n=== 演示完成 ===\n")

demonstrate_comparison_operations()
```

## 容器类型运算符重载

### 实现类似列表的行为

```python
class CustomList:
    """自定义列表类 - 演示容器运算符重载"""
    
    def __init__(self, items=None):
        self._items = list(items) if items else []
    
    # 长度运算符 len()
    def __len__(self):
        """返回列表长度"""
        return len(self._items)
    
    # 索引访问 []
    def __getitem__(self, index):
        """获取元素"""
        if isinstance(index, slice):
            return CustomList(self._items[index])
        return self._items[index]
    
    # 索引赋值 []
    def __setitem__(self, index, value):
        """设置元素"""
        self._items[index] = value
    
    # 删除元素 del
    def __delitem__(self, index):
        """删除元素"""
        del self._items[index]
    
    # 成员测试 in
    def __contains__(self, item):
        """检查元素是否存在"""
        return item in self._items
    
    # 迭代器 for ... in
    def __iter__(self):
        """返回迭代器"""
        return iter(self._items)
    
    # 反向迭代器 reversed()
    def __reversed__(self):
        """返回反向迭代器"""
        return reversed(self._items)
    
    # 加法运算符 + (连接)
    def __add__(self, other):
        """列表连接"""
        if isinstance(other, CustomList):
            return CustomList(self._items + other._items)
        elif isinstance(other, list):
            return CustomList(self._items + other)
        return NotImplemented
    
    # 右加法运算符
    def __radd__(self, other):
        """右加法"""
        if isinstance(other, list):
            return CustomList(other + self._items)
        return NotImplemented
    
    # 乘法运算符 * (重复)
    def __mul__(self, other):
        """列表重复"""
        if isinstance(other, int):
            return CustomList(self._items * other)
        return NotImplemented
    
    # 右乘法运算符
    def __rmul__(self, other):
        """右乘法"""
        return self.__mul__(other)
    
    # 复合赋值运算符 +=
    def __iadd__(self, other):
        """就地加法"""
        if isinstance(other, CustomList):
            self._items.extend(other._items)
        elif isinstance(other, list):
            self._items.extend(other)
        else:
            return NotImplemented
        return self
    
    # 复合赋值运算符 *=
    def __imul__(self, other):
        """就地乘法"""
        if isinstance(other, int):
            self._items *= other
            return self
        return NotImplemented
    
    # 相等比较
    def __eq__(self, other):
        if isinstance(other, CustomList):
            return self._items == other._items
        elif isinstance(other, list):
            return self._items == other
        return False
    
    # 不等比较
    def __ne__(self, other):
        return not self.__eq__(other)
    
    # 小于比较（字典序）
    def __lt__(self, other):
        if isinstance(other, CustomList):
            return self._items < other._items
        elif isinstance(other, list):
            return self._items < other
        return NotImplemented
    
    # 小于等于比较
    def __le__(self, other):
        if isinstance(other, CustomList):
            return self._items <= other._items
        elif isinstance(other, list):
            return self._items <= other
        return NotImplemented
    
    # 大于比较
    def __gt__(self, other):
        if isinstance(other, CustomList):
            return self._items > other._items
        elif isinstance(other, list):
            return self._items > other
        return NotImplemented
    
    # 大于等于比较
    def __ge__(self, other):
        if isinstance(other, CustomList):
            return self._items >= other._items
        elif isinstance(other, list):
            return self._items >= other
        return NotImplemented
    
    # 布尔值转换
    def __bool__(self):
        """布尔值转换"""
        return bool(self._items)
    
    # 字符串表示
    def __str__(self):
        return f"CustomList({self._items})"
    
    def __repr__(self):
        return f"CustomList({self._items!r})"
    
    # 添加一些列表方法
    def append(self, item):
        """添加元素"""
        self._items.append(item)
    
    def extend(self, items):
        """扩展列表"""
        self._items.extend(items)
    
    def insert(self, index, item):
        """插入元素"""
        self._items.insert(index, item)
    
    def remove(self, item):
        """移除元素"""
        self._items.remove(item)
    
    def pop(self, index=-1):
        """弹出元素"""
        return self._items.pop(index)
    
    def clear(self):
        """清空列表"""
        self._items.clear()
    
    def copy(self):
        """复制列表"""
        return CustomList(self._items.copy())
    
    def count(self, item):
        """计数元素"""
        return self._items.count(item)
    
    def index(self, item, start=0, end=None):
        """查找元素索引"""
        if end is None:
            return self._items.index(item, start)
        return self._items.index(item, start, end)
    
    def reverse(self):
        """反转列表"""
        self._items.reverse()
    
    def sort(self, key=None, reverse=False):
        """排序列表"""
        self._items.sort(key=key, reverse=reverse)

class Matrix:
    """矩阵类 - 演示二维容器运算符重载"""
    
    def __init__(self, rows, cols, initial_value=0):
        self.rows = rows
        self.cols = cols
        self._data = [[initial_value for _ in range(cols)] for _ in range(rows)]
    
    @classmethod
    def from_list(cls, data):
        """从二维列表创建矩阵"""
        if not data or not data[0]:
            raise ValueError("数据不能为空")
        
        rows = len(data)
        cols = len(data[0])
        
        # 检查所有行的长度是否相同
        for row in data:
            if len(row) != cols:
                raise ValueError("所有行的长度必须相同")
        
        matrix = cls(rows, cols)
        matrix._data = [row.copy() for row in data]
        return matrix
    
    # 索引访问 [row, col] 或 [row][col]
    def __getitem__(self, key):
        if isinstance(key, tuple) and len(key) == 2:
            row, col = key
            return self._data[row][col]
        elif isinstance(key, int):
            return self._data[key]
        else:
            raise TypeError("索引必须是整数或(row, col)元组")
    
    # 索引赋值
    def __setitem__(self, key, value):
        if isinstance(key, tuple) and len(key) == 2:
            row, col = key
            self._data[row][col] = value
        elif isinstance(key, int):
            if isinstance(value, list) and len(value) == self.cols:
                self._data[key] = value.copy()
            else:
                raise ValueError(f"行数据必须是长度为{self.cols}的列表")
        else:
            raise TypeError("索引必须是整数或(row, col)元组")
    
    # 矩阵加法
    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("矩阵维度必须相同")
            
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] + other[i, j]
            return result
        elif isinstance(other, (int, float)):
            # 标量加法
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] + other
            return result
        return NotImplemented
    
    # 矩阵减法
    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("矩阵维度必须相同")
            
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] - other[i, j]
            return result
        elif isinstance(other, (int, float)):
            # 标量减法
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] - other
            return result
        return NotImplemented
    
    # 矩阵乘法
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError(f"矩阵维度不匹配: ({self.rows}x{self.cols}) * ({other.rows}x{other.cols})")
            
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    sum_val = 0
                    for k in range(self.cols):
                        sum_val += self[i, k] * other[k, j]
                    result[i, j] = sum_val
            return result
        elif isinstance(other, (int, float)):
            # 标量乘法
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] * other
            return result
        return NotImplemented
    
    # 右乘法
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.__mul__(other)
        return NotImplemented
    
    # 相等比较
    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                return False
            
            for i in range(self.rows):
                for j in range(self.cols):
                    if abs(self[i, j] - other[i, j]) > 1e-10:
                        return False
            return True
        return False
    
    # 字符串表示
    def __str__(self):
        lines = []
        for row in self._data:
            line = "[" + ", ".join(f"{val:6.2f}" for val in row) + "]"
            lines.append(line)
        return "[\n  " + ",\n  ".join(lines) + "\n]"
    
    def __repr__(self):
        return f"Matrix({self.rows}x{self.cols})"
    
    # 矩阵转置
    def transpose(self):
        """矩阵转置"""
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result[j, i] = self[i, j]
        return result
    
    # 获取矩阵的形状
    def shape(self):
        """获取矩阵形状"""
        return (self.rows, self.cols)

# 演示容器运算符重载
def demonstrate_container_operations():
    """演示容器运算符重载"""
    print("=== 容器运算符重载演示 ===")
    
    # 自定义列表演示
    print("1. 自定义列表操作:")
    
    # 创建列表
    list1 = CustomList([1, 2, 3])
    list2 = CustomList([4, 5, 6])
    
    print(f"   list1 = {list1}")
    print(f"   list2 = {list2}")
    print(f"   len(list1) = {len(list1)}")
    
    # 索引操作
    print(f"   list1[0] = {list1[0]}")
    print(f"   list1[1:3] = {list1[1:3]}")
    
    # 成员测试
    print(f"   2 in list1 = {2 in list1}")
    print(f"   7 in list1 = {7 in list1}")
    
    # 算术操作
    list3 = list1 + list2
    print(f"   list1 + list2 = {list3}")
    
    list4 = list1 * 2
    print(f"   list1 * 2 = {list4}")
    
    # 比较操作
    print(f"   list1 == [1, 2, 3] = {list1 == [1, 2, 3]}")
    print(f"   list1 < list2 = {list1 < list2}")
    
    # 就地操作
    list5 = CustomList([7, 8])
    print(f"   list5 = {list5}")
    list5 += [9, 10]
    print(f"   list5 += [9, 10] => {list5}")
    
    # 迭代
    print("   迭代 list1:")
    for i, item in enumerate(list1):
        print(f"     [{i}] = {item}")
    
    # 矩阵演示
    print("\n2. 矩阵操作:")
    
    # 创建矩阵
    m1 = Matrix.from_list([
        [1, 2, 3],
        [4, 5, 6]
    ])
    
    m2 = Matrix.from_list([
        [7, 8],
        [9, 10],
        [11, 12]
    ])
    
    print(f"   矩阵 m1 ({m1.shape()}):")
    print(f"{m1}")
    
    print(f"   矩阵 m2 ({m2.shape()}):")
    print(f"{m2}")
    
    # 矩阵乘法
    m3 = m1 * m2
    print(f"   m1 * m2 ({m3.shape()}):")
    print(f"{m3}")
    
    # 标量操作
    m4 = m1 * 2
    print(f"   m1 * 2:")
    print(f"{m4}")
    
    m5 = m1 + 10
    print(f"   m1 + 10:")
    print(f"{m5}")
    
    # 矩阵转置
    m6 = m1.transpose()
    print(f"   m1.transpose() ({m6.shape()}):")
    print(f"{m6}")
    
    # 索引访问
    print(f"   m1[0, 1] = {m1[0, 1]}")
    print(f"   m1[1] = {m1[1]}")
    
    # 修改元素
    m1[0, 0] = 100
    print(f"   修改 m1[0, 0] = 100 后:")
    print(f"{m1}")
    
    print("\n=== 演示完成 ===\n")

demonstrate_container_operations()
```

## 字符串表示方法重载

### 实现友好的对象表示

```python
class Money:
    """货币类 - 演示字符串表示方法重载"""
    
    # 货币符号映射
    CURRENCY_SYMBOLS = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
        "CNY": "¥",
        "KRW": "₩"
    }
    
    def __init__(self, amount: float, currency: str = "USD"):
        self.amount = amount
        self.currency = currency.upper()
    
    # 字符串表示（用户友好）
    def __str__(self):
        """用户友好的字符串表示"""
        symbol = self.CURRENCY_SYMBOLS.get(self.currency, self.currency)
        return f"{symbol}{self.amount:.2f}"
    
    # 开发者表示（详细信息）
    def __repr__(self):
        """开发者友好的字符串表示"""
        return f"Money(amount={self.amount}, currency='{self.currency}')"
    
    # 格式化字符串
    def __format__(self, format_spec):
        """自定义格式化"""
        if format_spec == "":
            return str(self)
        elif format_spec == "full":
            symbol = self.CURRENCY_SYMBOLS.get(self.currency, self.currency)
            return f"{self.amount:.2f} {self.currency} ({symbol})"
        elif format_spec == "code":
            return f"{self.amount:.2f} {self.currency}"
        elif format_spec.startswith(".") and format_spec[1:].isdigit():
            # 自定义小数位数
            decimals = int(format_spec[1:])
            symbol = self.CURRENCY_SYMBOLS.get(self.currency, self.currency)
            return f"{symbol}{self.amount:.{decimals}f}"
        else:
            # 使用默认的数字格式化
            symbol = self.CURRENCY_SYMBOLS.get(self.currency, self.currency)
            return f"{symbol}{self.amount:{format_spec}}"
    
    # 算术运算
    def __add__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"不能直接相加不同货币: {self.currency} 和 {other.currency}")
            return Money(self.amount + other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"不能直接相减不同货币: {self.currency} 和 {other.currency}")
            return Money(self.amount - other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount - other, self.currency)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("不能除以零")
            return Money(self.amount / other, self.currency)
        return NotImplemented
    
    # 比较运算
    def __eq__(self, other):
        if isinstance(other, Money):
            return (abs(self.amount - other.amount) < 1e-10 and 
                   self.currency == other.currency)
        return False
    
    def __lt__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"不能比较不同货币: {self.currency} 和 {other.currency}")
            return self.amount < other.amount
        return NotImplemented
    
    def __le__(self, other):
        return self < other or self == other
    
    def __gt__(self, other):
        return not self <= other
    
    def __ge__(self, other):
        return not self < other
    
    def __ne__(self, other):
        return not self == other
    
    # 哈希值（用于集合和字典）
    def __hash__(self):
        return hash((round(self.amount, 2), self.currency))
    
    # 布尔值转换
    def __bool__(self):
        return self.amount != 0
    
    # 绝对值
    def __abs__(self):
        return Money(abs(self.amount), self.currency)
    
    # 取负
    def __neg__(self):
        return Money(-self.amount, self.currency)
    
    # 取正
    def __pos__(self):
        return Money(self.amount, self.currency)

class Person:
    """人员类 - 演示复杂对象的字符串表示"""
    
    def __init__(self, name: str, age: int, email: str, salary: Money = None):
        self.name = name
        self.age = age
        self.email = email
        self.salary = salary or Money(0)
        self.skills = []
        self.projects = []
    
    def add_skill(self, skill: str, level: str = "beginner"):
        """添加技能"""
        self.skills.append({"name": skill, "level": level})
    
    def add_project(self, project_name: str, role: str = "developer"):
        """添加项目"""
        self.projects.append({"name": project_name, "role": role})
    
    # 简单字符串表示
    def __str__(self):
        return f"{self.name} ({self.age}岁)"
    
    # 详细字符串表示
    def __repr__(self):
        return (f"Person(name='{self.name}', age={self.age}, "
                f"email='{self.email}', salary={self.salary!r})") 
    
    # 自定义格式化
    def __format__(self, format_spec):
        if format_spec == "":
            return str(self)
        elif format_spec == "full":
            lines = [
                f"姓名: {self.name}",
                f"年龄: {self.age}岁",
                f"邮箱: {self.email}",
                f"薪资: {self.salary}"
            ]
            
            if self.skills:
                lines.append("技能:")
                for skill in self.skills:
                    lines.append(f"  - {skill['name']} ({skill['level']})")
            
            if self.projects:
                lines.append("项目:")
                for project in self.projects:
                    lines.append(f"  - {project['name']} (担任{project['role']})")
            
            return "\n".join(lines)
        elif format_spec == "brief":
            return f"{self.name} <{self.email}>"
        elif format_spec == "card":
            return f"┌─ {self.name} ─┐\n│ 年龄: {self.age}岁    │\n│ 薪资: {self.salary} │\n└─────────────┘"
        else:
            return str(self)
    
    # 比较（按年龄）
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.email == other.email  # 按邮箱判断是否同一人
        return False
    
    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented
    
    def __hash__(self):
        return hash(self.email)

# 演示字符串表示方法重载
def demonstrate_string_representation():
    """演示字符串表示方法重载"""
    print("=== 字符串表示方法重载演示 ===")
    
    # 货币对象演示
    print("1. 货币对象的字符串表示:")
    
    money_objects = [
        Money(1234.56, "USD"),
        Money(999.99, "EUR"),
        Money(50000, "JPY"),
        Money(8888.88, "CNY")
    ]
    
    for money in money_objects:
        print(f"   str(): {str(money)}")
        print(f"   repr(): {repr(money)}")
        print(f"   format('full'): {money:full}")
        print(f"   format('code'): {money:code}")
        print(f"   format('.0'): {money:.0}")
        print(f"   format('.4'): {money:.4}")
        print(f"   format(',.2f'): {money:,.2f}")
        print()
    
    # 货币运算
    print("2. 货币运算:")
    usd1 = Money(100, "USD")
    usd2 = Money(50, "USD")
    
    print(f"   {usd1} + {usd2} = {usd1 + usd2}")
    print(f"   {usd1} - {usd2} = {usd1 - usd2}")
    print(f"   {usd1} * 1.5 = {usd1 * 1.5}")
    print(f"   {usd1} / 2 = {usd1 / 2}")
    print(f"   abs({-usd1}) = {abs(-usd1)}")
    
    # 人员对象演示
    print("\n3. 人员对象的字符串表示:")
    
    # 创建人员
    alice = Person("Alice Johnson", 28, "alice@example.com", Money(75000, "USD"))
    alice.add_skill("Python", "expert")
    alice.add_skill("JavaScript", "intermediate")
    alice.add_skill("SQL", "advanced")
    alice.add_project("电商网站", "后端开发")
    alice.add_project("数据分析平台", "技术负责人")
    
    bob = Person("Bob Smith", 32, "bob@example.com", Money(85000, "USD"))
    bob.add_skill("Java", "expert")
    bob.add_skill("Spring", "advanced")
    bob.add_project("企业管理系统", "架构师")
    
    people = [alice, bob]
    
    for person in people:
        print(f"   str(): {str(person)}")
        print(f"   repr(): {repr(person)}")
        print(f"   format('brief'): {person:brief}")
        print(f"   format('card'):\n{person:card}")
        print(f"   format('full'):\n{person:full}")
        print("-" * 50)
    
    # 比较和排序
    print("\n4. 对象比较和排序:")
    
    # 按年龄排序
    sorted_people = sorted(people)
    print("   按年龄排序:")
    for person in sorted_people:
        print(f"     {person}")
    
    # 按薪资排序
    sorted_by_salary = sorted(people, key=lambda p: p.salary.amount)
    print("\n   按薪资排序:")
    for person in sorted_by_salary:
        print(f"     {person} - {person.salary}")
    
    # 集合操作（需要__hash__和__eq__）
    print("\n5. 集合操作:")
    
    # 创建货币集合
    money_set = {Money(100, "USD"), Money(100, "USD"), Money(200, "USD")}
    print(f"   货币集合: {money_set}")  # 重复的Money(100, "USD")会被去重
    
    # 创建人员集合
    people_set = {alice, bob, alice}  # alice重复
    print(f"   人员集合: {people_set}")  # 重复的alice会被去重
    
    print("\n=== 演示完成 ===\n")

demonstrate_string_representation()
```

## 运算符重载的好处和注意事项

```python
def demonstrate_operator_overloading_benefits():
    """演示运算符重载的好处和注意事项"""
    print("=== 运算符重载的好处和注意事项 ===")
    
    print("1. 运算符重载的好处:")
    print("   - 提高代码可读性和直观性")
    print("   - 让自定义类型像内置类型一样使用")
    print("   - 支持多态性和泛型编程")
    print("   - 简化复杂操作的表达")
    
    print("\n2. 设计原则:")
    print("   - 保持运算符的直观含义")
    print("   - 遵循数学和逻辑约定")
    print("   - 保持一致性（如果实现了==，也应该实现!=）")
    print("   - 考虑性能影响")
    
    print("\n3. 常见陷阱:")
    print("   - 不要重载不相关的运算符")
    print("   - 注意返回类型的一致性")
    print("   - 处理边界情况和错误")
    print("   - 考虑运算符的交换律和结合律")
    
    print("\n4. 最佳实践:")
    print("   - 实现完整的运算符集合")
    print("   - 提供清晰的文档说明")
    print("   - 编写充分的测试用例")
    print("   - 考虑使用functools.total_ordering装饰器")
    
    print("\n5. 核心要点:")
    print("   - 运算符重载是多态性的重要体现")
    print("   - 通过魔术方法实现运算符行为")
    print("   - 让代码更加Pythonic和易读")
    print("   - 支持与内置类型的无缝集成")
    
    print("\n=== 总结完成 ===\n")

demonstrate_operator_overloading_benefits()
```

## 总结

运算符重载是Python中实现多态性的重要机制，它允许我们为自定义类定义运算符的行为。通过合理使用运算符重载，我们可以：

1. **提高代码可读性**：让自定义对象像内置类型一样使用
2. **实现直观的API**：使用熟悉的运算符表达复杂操作
3. **支持多态性**：不同类型的对象可以使用相同的运算符
4. **简化代码表达**：用简洁的语法表达复杂的逻辑

### 主要的魔术方法类别：

- **算术运算符**：`__add__`, `__sub__`, `__mul__`, `__truediv__`等
- **比较运算符**：`__eq__`, `__lt__`, `__le__`, `__gt__`等
- **容器运算符**：`__getitem__`, `__setitem__`, `__len__`, `__contains__`等
- **字符串表示**：`__str__`, `__repr__`, `__format__`
- **一元运算符**：`__neg__`, `__pos__`, `__abs__`
- **复合赋值**：`__iadd__`, `__isub__`, `__imul__`等

掌握运算符重载的技巧，能让你设计出更加直观和易用的Python类，提高代码的表达力和可维护性。