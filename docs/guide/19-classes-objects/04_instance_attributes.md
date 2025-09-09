# 实例属性的操作

## 学习目标
- 深入理解实例属性的概念和特性
- 掌握实例属性的创建、访问、修改和删除
- 学会动态属性的使用和管理
- 理解属性的生命周期和作用域
- 掌握属性的验证和保护机制

## 实例属性基础

### 什么是实例属性

实例属性是属于特定对象实例的数据，每个对象都有自己独立的属性副本。实例属性通常在 `__init__` 方法中初始化，但也可以在任何时候动态添加。

```python
class Student:
    def __init__(self, name, age, student_id):
        # 在构造方法中定义实例属性
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []  # 空列表作为默认值
        self.enrollment_date = None
        self.is_active = True
    
    def add_grade(self, subject, score):
        """添加成绩"""
        grade_entry = {
            "subject": subject,
            "score": score,
            "date": self._get_current_date()
        }
        self.grades.append(grade_entry)
    
    def get_average_grade(self):
        """计算平均成绩"""
        if not self.grades:
            return 0
        total = sum(grade["score"] for grade in self.grades)
        return total / len(self.grades)
    
    def update_info(self, **kwargs):
        """更新学生信息"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
                print(f"更新 {key}: {value}")
            else:
                print(f"属性 {key} 不存在")
    
    def _get_current_date(self):
        """获取当前日期"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d")
    
    def get_student_info(self):
        """获取学生完整信息"""
        return {
            "姓名": self.name,
            "年龄": self.age,
            "学号": self.student_id,
            "成绩数量": len(self.grades),
            "平均成绩": round(self.get_average_grade(), 2),
            "注册日期": self.enrollment_date,
            "状态": "在读" if self.is_active else "休学"
        }

# 实例属性基础演示
print("=== 实例属性基础演示 ===")

# 创建学生对象
student1 = Student("张三", 20, "2023001")
student2 = Student("李四", 19, "2023002")

print("初始学生信息:")
print(f"学生1: {student1.get_student_info()}")
print(f"学生2: {student2.get_student_info()}")

# 添加成绩
print("\n添加成绩:")
student1.add_grade("数学", 95)
student1.add_grade("英语", 88)
student1.add_grade("物理", 92)

student2.add_grade("数学", 87)
student2.add_grade("英语", 94)

print(f"学生1平均成绩: {student1.get_average_grade():.2f}")
print(f"学生2平均成绩: {student2.get_average_grade():.2f}")

# 更新学生信息
print("\n更新学生信息:")
student1.update_info(age=21, enrollment_date="2023-09-01")
student2.update_info(name="李四四", is_active=False)

print("\n更新后的学生信息:")
print(f"学生1: {student1.get_student_info()}")
print(f"学生2: {student2.get_student_info()}")

# 验证属性独立性
print("\n=== 属性独立性验证 ===")
print(f"学生1成绩列表长度: {len(student1.grades)}")
print(f"学生2成绩列表长度: {len(student2.grades)}")
print(f"两个对象是否相同: {student1 is student2}")
print(f"成绩列表是否相同: {student1.grades is student2.grades}")
```

### 动态属性操作

```python
class DynamicObject:
    def __init__(self, name):
        self.name = name
        self.creation_time = self._get_timestamp()
        self._attribute_history = []  # 记录属性变更历史
    
    def _get_timestamp(self):
        """获取时间戳"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def add_attribute(self, attr_name, attr_value):
        """动态添加属性"""
        if hasattr(self, attr_name):
            old_value = getattr(self, attr_name)
            setattr(self, attr_name, attr_value)
            self._attribute_history.append({
                "操作": "修改",
                "属性": attr_name,
                "旧值": old_value,
                "新值": attr_value,
                "时间": self._get_timestamp()
            })
            return f"属性 '{attr_name}' 已更新: {old_value} -> {attr_value}"
        else:
            setattr(self, attr_name, attr_value)
            self._attribute_history.append({
                "操作": "添加",
                "属性": attr_name,
                "值": attr_value,
                "时间": self._get_timestamp()
            })
            return f"属性 '{attr_name}' 已添加: {attr_value}"
    
    def remove_attribute(self, attr_name):
        """动态删除属性"""
        if hasattr(self, attr_name):
            # 保护核心属性
            protected_attrs = ['name', 'creation_time', '_attribute_history']
            if attr_name in protected_attrs:
                return f"属性 '{attr_name}' 是受保护的，不能删除"
            
            old_value = getattr(self, attr_name)
            delattr(self, attr_name)
            self._attribute_history.append({
                "操作": "删除",
                "属性": attr_name,
                "旧值": old_value,
                "时间": self._get_timestamp()
            })
            return f"属性 '{attr_name}' 已删除，原值: {old_value}"
        else:
            return f"属性 '{attr_name}' 不存在"
    
    def get_attribute(self, attr_name, default=None):
        """安全获取属性"""
        return getattr(self, attr_name, default)
    
    def has_attribute(self, attr_name):
        """检查属性是否存在"""
        return hasattr(self, attr_name)
    
    def list_attributes(self, include_private=False):
        """列出所有属性"""
        attrs = {}
        for attr_name in dir(self):
            # 跳过方法和特殊属性
            if not callable(getattr(self, attr_name)) and not attr_name.startswith('__'):
                if include_private or not attr_name.startswith('_'):
                    attrs[attr_name] = getattr(self, attr_name)
        return attrs
    
    def get_attribute_history(self):
        """获取属性变更历史"""
        return self._attribute_history.copy()
    
    def batch_set_attributes(self, **kwargs):
        """批量设置属性"""
        results = []
        for attr_name, attr_value in kwargs.items():
            result = self.add_attribute(attr_name, attr_value)
            results.append(result)
        return results
    
    def copy_attributes_from(self, other_object, *attr_names):
        """从其他对象复制属性"""
        if not attr_names:
            # 如果没有指定属性名，复制所有公共属性
            attr_names = [attr for attr in dir(other_object) 
                         if not attr.startswith('_') and not callable(getattr(other_object, attr))]
        
        results = []
        for attr_name in attr_names:
            if hasattr(other_object, attr_name):
                attr_value = getattr(other_object, attr_name)
                result = self.add_attribute(attr_name, attr_value)
                results.append(result)
            else:
                results.append(f"源对象没有属性 '{attr_name}'")
        
        return results
    
    def get_object_summary(self):
        """获取对象摘要"""
        attrs = self.list_attributes(include_private=False)
        return {
            "对象名称": self.name,
            "创建时间": self.creation_time,
            "属性数量": len(attrs),
            "属性列表": list(attrs.keys()),
            "变更历史数量": len(self._attribute_history)
        }

# 动态属性操作演示
print("\n=== 动态属性操作演示 ===")

# 创建动态对象
obj1 = DynamicObject("测试对象1")
obj2 = DynamicObject("测试对象2")

print("初始对象状态:")
print(f"obj1属性: {obj1.list_attributes()}")
print(f"obj2属性: {obj2.list_attributes()}")

print("\n=== 动态添加属性 ===")
print(obj1.add_attribute("color", "红色"))
print(obj1.add_attribute("size", "大"))
print(obj1.add_attribute("weight", 10.5))
print(obj1.add_attribute("tags", ["重要", "测试"]))

print(obj2.add_attribute("color", "蓝色"))
print(obj2.add_attribute("temperature", 25.0))

print("\n添加属性后:")
print(f"obj1属性: {obj1.list_attributes()}")
print(f"obj2属性: {obj2.list_attributes()}")

print("\n=== 修改属性 ===")
print(obj1.add_attribute("color", "绿色"))  # 修改已存在的属性
print(obj1.add_attribute("weight", 15.2))

print("\n=== 批量设置属性 ===")
results = obj2.batch_set_attributes(
    material="塑料",
    price=99.99,
    available=True,
    color="黄色"  # 修改已存在的属性
)
for result in results:
    print(result)

print("\n=== 属性查询 ===")
print(f"obj1是否有color属性: {obj1.has_attribute('color')}")
print(f"obj1的color属性: {obj1.get_attribute('color')}")
print(f"obj1的不存在属性: {obj1.get_attribute('nonexistent', '默认值')}")

print("\n=== 复制属性 ===")
copy_results = obj2.copy_attributes_from(obj1, "size", "weight", "tags")
for result in copy_results:
    print(result)

print(f"\n复制后obj2属性: {obj2.list_attributes()}")

print("\n=== 删除属性 ===")
print(obj1.remove_attribute("tags"))
print(obj1.remove_attribute("nonexistent"))  # 删除不存在的属性
print(obj1.remove_attribute("name"))  # 尝试删除受保护的属性

print("\n=== 属性变更历史 ===")
print("obj1的变更历史:")
for i, change in enumerate(obj1.get_attribute_history(), 1):
    print(f"  {i}. {change}")

print("\n=== 对象摘要 ===")
print(f"obj1摘要: {obj1.get_object_summary()}")
print(f"obj2摘要: {obj2.get_object_summary()}")
```

## 属性访问控制

### 使用属性装饰器

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius  # 私有属性
        self._fahrenheit = None  # 缓存华氏温度
        self._kelvin = None      # 缓存开尔文温度
        self._conversion_count = 0  # 转换次数统计
    
    @property
    def celsius(self):
        """摄氏温度属性（只读）"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """设置摄氏温度"""
        if not isinstance(value, (int, float)):
            raise TypeError("温度必须是数字")
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度(-273.15°C)")
        
        self._celsius = value
        # 清空缓存
        self._fahrenheit = None
        self._kelvin = None
        self._conversion_count += 1
    
    @property
    def fahrenheit(self):
        """华氏温度属性（计算属性）"""
        if self._fahrenheit is None:
            self._fahrenheit = (self._celsius * 9/5) + 32
        return self._fahrenheit
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """通过华氏温度设置"""
        if not isinstance(value, (int, float)):
            raise TypeError("温度必须是数字")
        
        celsius = (value - 32) * 5/9
        self.celsius = celsius  # 使用celsius的setter进行验证
    
    @property
    def kelvin(self):
        """开尔文温度属性（计算属性）"""
        if self._kelvin is None:
            self._kelvin = self._celsius + 273.15
        return self._kelvin
    
    @kelvin.setter
    def kelvin(self, value):
        """通过开尔文温度设置"""
        if not isinstance(value, (int, float)):
            raise TypeError("温度必须是数字")
        if value < 0:
            raise ValueError("开尔文温度不能为负数")
        
        celsius = value - 273.15
        self.celsius = celsius  # 使用celsius的setter进行验证
    
    @property
    def conversion_count(self):
        """转换次数（只读属性）"""
        return self._conversion_count
    
    @property
    def state(self):
        """物质状态（只读计算属性）"""
        if self._celsius < 0:
            return "固态"
        elif self._celsius < 100:
            return "液态"
        else:
            return "气态"
    
    @property
    def is_freezing(self):
        """是否结冰（只读布尔属性）"""
        return self._celsius <= 0
    
    @property
    def is_boiling(self):
        """是否沸腾（只读布尔属性）"""
        return self._celsius >= 100
    
    def reset_conversion_count(self):
        """重置转换计数"""
        self._conversion_count = 0
    
    def get_all_temperatures(self):
        """获取所有温度单位"""
        return {
            "摄氏度": self.celsius,
            "华氏度": self.fahrenheit,
            "开尔文": self.kelvin,
            "状态": self.state,
            "转换次数": self.conversion_count
        }

# 属性装饰器演示
print("\n=== 属性装饰器演示 ===")

# 创建温度对象
temp = Temperature(25)

print("初始温度:")
print(f"摄氏度: {temp.celsius}°C")
print(f"华氏度: {temp.fahrenheit}°F")
print(f"开尔文: {temp.kelvin}K")
print(f"状态: {temp.state}")
print(f"转换次数: {temp.conversion_count}")

print("\n=== 通过不同单位设置温度 ===")
print("设置华氏度为100°F:")
temp.fahrenheit = 100
print(f"摄氏度: {temp.celsius:.2f}°C")
print(f"华氏度: {temp.fahrenheit}°F")
print(f"状态: {temp.state}")
print(f"转换次数: {temp.conversion_count}")

print("\n设置开尔文为300K:")
temp.kelvin = 300
print(f"摄氏度: {temp.celsius:.2f}°C")
print(f"开尔文: {temp.kelvin}K")
print(f"状态: {temp.state}")
print(f"转换次数: {temp.conversion_count}")

print("\n=== 属性验证测试 ===")
try:
    print("尝试设置无效温度(-300°C):")
    temp.celsius = -300
except ValueError as e:
    print(f"捕获异常: {e}")

try:
    print("尝试设置非数字温度:")
    temp.celsius = "热"
except TypeError as e:
    print(f"捕获异常: {e}")

print("\n=== 只读属性测试 ===")
print(f"当前状态: {temp.state}")
print(f"是否结冰: {temp.is_freezing}")
print(f"是否沸腾: {temp.is_boiling}")

# 尝试修改只读属性（会报错）
try:
    temp.state = "等离子态"
except AttributeError as e:
    print(f"尝试修改只读属性失败: {e}")

print(f"\n所有温度信息: {temp.get_all_temperatures()}")
```

### 属性描述符

```python
class ValidatedAttribute:
    """属性描述符 - 用于属性验证"""
    
    def __init__(self, name, validator=None, default=None):
        self.name = name
        self.validator = validator
        self.default = default
        self.private_name = f'_{name}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, self.default)
    
    def __set__(self, obj, value):
        if self.validator:
            self.validator(value)
        setattr(obj, self.private_name, value)
    
    def __delete__(self, obj):
        if hasattr(obj, self.private_name):
            delattr(obj, self.private_name)

class RangeValidator:
    """范围验证器"""
    
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def __call__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"值必须是数字，得到 {type(value).__name__}")
        
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"值 {value} 小于最小值 {self.min_value}")
        
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"值 {value} 大于最大值 {self.max_value}")

class TypeValidator:
    """类型验证器"""
    
    def __init__(self, *types):
        self.types = types
    
    def __call__(self, value):
        if not isinstance(value, self.types):
            type_names = [t.__name__ for t in self.types]
            raise TypeError(f"值必须是 {' 或 '.join(type_names)} 类型，得到 {type(value).__name__}")

class LengthValidator:
    """长度验证器"""
    
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length
    
    def __call__(self, value):
        if not hasattr(value, '__len__'):
            raise TypeError("值必须有长度属性")
        
        length = len(value)
        
        if self.min_length is not None and length < self.min_length:
            raise ValueError(f"长度 {length} 小于最小长度 {self.min_length}")
        
        if self.max_length is not None and length > self.max_length:
            raise ValueError(f"长度 {length} 大于最大长度 {self.max_length}")

class Product:
    """使用属性描述符的产品类"""
    
    # 使用描述符定义属性
    name = ValidatedAttribute(
        'name', 
        validator=lambda x: TypeValidator(str)(x) or LengthValidator(1, 50)(x)
    )
    
    price = ValidatedAttribute(
        'price',
        validator=RangeValidator(0, 10000),
        default=0.0
    )
    
    quantity = ValidatedAttribute(
        'quantity',
        validator=RangeValidator(0, 1000),
        default=0
    )
    
    weight = ValidatedAttribute(
        'weight',
        validator=RangeValidator(0.1, 100),
        default=1.0
    )
    
    category = ValidatedAttribute(
        'category',
        validator=TypeValidator(str),
        default="未分类"
    )
    
    def __init__(self, name, price, quantity=1, weight=1.0, category="未分类"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.weight = weight
        self.category = category
        self.creation_time = self._get_timestamp()
    
    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @property
    def total_value(self):
        """总价值（只读计算属性）"""
        return self.price * self.quantity
    
    @property
    def total_weight(self):
        """总重量（只读计算属性）"""
        return self.weight * self.quantity
    
    def update_stock(self, change):
        """更新库存"""
        new_quantity = self.quantity + change
        if new_quantity < 0:
            raise ValueError("库存不能为负数")
        self.quantity = new_quantity
        return f"库存更新: {change:+d}，当前库存: {self.quantity}"
    
    def apply_discount(self, discount_percent):
        """应用折扣"""
        if not 0 <= discount_percent <= 100:
            raise ValueError("折扣百分比必须在0-100之间")
        
        original_price = self.price
        self.price = original_price * (1 - discount_percent / 100)
        return f"应用 {discount_percent}% 折扣: ¥{original_price:.2f} -> ¥{self.price:.2f}"
    
    def get_product_info(self):
        """获取产品完整信息"""
        return {
            "名称": self.name,
            "价格": f"¥{self.price:.2f}",
            "数量": self.quantity,
            "单重": f"{self.weight}kg",
            "类别": self.category,
            "总价值": f"¥{self.total_value:.2f}",
            "总重量": f"{self.total_weight}kg",
            "创建时间": self.creation_time
        }

# 属性描述符演示
print("\n=== 属性描述符演示 ===")

# 创建产品对象
print("创建有效产品:")
product1 = Product("笔记本电脑", 5999.99, 10, 2.5, "电子产品")
print(f"产品信息: {product1.get_product_info()}")

print("\n=== 属性验证测试 ===")

# 测试价格验证
print("测试价格验证:")
try:
    product1.price = -100  # 负价格
except ValueError as e:
    print(f"价格验证失败: {e}")

try:
    product1.price = 15000  # 超出范围
except ValueError as e:
    print(f"价格验证失败: {e}")

# 测试名称验证
print("\n测试名称验证:")
try:
    product1.name = ""  # 空名称
except ValueError as e:
    print(f"名称验证失败: {e}")

try:
    product1.name = "a" * 60  # 名称太长
except ValueError as e:
    print(f"名称验证失败: {e}")

try:
    product1.name = 123  # 错误类型
except TypeError as e:
    print(f"名称验证失败: {e}")

# 测试数量验证
print("\n测试数量验证:")
try:
    product1.quantity = -5  # 负数量
except ValueError as e:
    print(f"数量验证失败: {e}")

try:
    product1.quantity = 1500  # 超出范围
except ValueError as e:
    print(f"数量验证失败: {e}")

print("\n=== 正常操作测试 ===")
print("更新库存:")
print(product1.update_stock(-3))
print(product1.update_stock(5))

print("\n应用折扣:")
print(product1.apply_discount(15))

print("\n更新后的产品信息:")
for key, value in product1.get_product_info().items():
    print(f"  {key}: {value}")

print("\n=== 创建多个产品测试独立性 ===")
product2 = Product("手机", 2999.99, 5, 0.2, "电子产品")
product3 = Product("书籍", 29.99, 100, 0.3, "图书")

print("产品2信息:")
for key, value in product2.get_product_info().items():
    print(f"  {key}: {value}")

print("\n产品3信息:")
for key, value in product3.get_product_info().items():
    print(f"  {key}: {value}")

# 验证属性独立性
print(f"\n属性独立性验证:")
print(f"产品1价格: ¥{product1.price:.2f}")
print(f"产品2价格: ¥{product2.price:.2f}")
print(f"产品3价格: ¥{product3.price:.2f}")

product2.price = 2499.99
print(f"\n修改产品2价格后:")
print(f"产品1价格: ¥{product1.price:.2f}")
print(f"产品2价格: ¥{product2.price:.2f}")
print(f"产品3价格: ¥{product3.price:.2f}")
```

## 特殊属性操作

### 使用__slots__限制属性

```python
class OptimizedStudent:
    """使用__slots__优化的学生类"""
    
    __slots__ = ['name', 'age', 'student_id', 'grades', '_gpa']
    
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []
        self._gpa = None
    
    def add_grade(self, subject, score):
        """添加成绩"""
        if not 0 <= score <= 100:
            raise ValueError("成绩必须在0-100之间")
        
        self.grades.append({"subject": subject, "score": score})
        self._gpa = None  # 清空GPA缓存
    
    @property
    def gpa(self):
        """计算GPA（缓存结果）"""
        if self._gpa is None and self.grades:
            total_score = sum(grade["score"] for grade in self.grades)
            self._gpa = total_score / len(self.grades) / 25  # 简化的GPA计算
        return self._gpa or 0.0
    
    def get_memory_usage(self):
        """获取内存使用情况"""
        import sys
        return sys.getsizeof(self)
    
    def __repr__(self):
        return f"OptimizedStudent(name='{self.name}', age={self.age}, id='{self.student_id}')"

class RegularStudent:
    """常规学生类（用于对比）"""
    
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []
        self._gpa = None
    
    def add_grade(self, subject, score):
        """添加成绩"""
        if not 0 <= score <= 100:
            raise ValueError("成绩必须在0-100之间")
        
        self.grades.append({"subject": subject, "score": score})
        self._gpa = None
    
    @property
    def gpa(self):
        """计算GPA"""
        if self._gpa is None and self.grades:
            total_score = sum(grade["score"] for grade in self.grades)
            self._gpa = total_score / len(self.grades) / 25
        return self._gpa or 0.0
    
    def get_memory_usage(self):
        """获取内存使用情况"""
        import sys
        return sys.getsizeof(self)
    
    def __repr__(self):
        return f"RegularStudent(name='{self.name}', age={self.age}, id='{self.student_id}')"

# __slots__演示
print("\n=== __slots__演示 ===")

# 创建两种学生对象
optimized_student = OptimizedStudent("张三", 20, "2023001")
regular_student = RegularStudent("李四", 19, "2023002")

print("基本功能测试:")
optimized_student.add_grade("数学", 95)
optimized_student.add_grade("英语", 88)
regular_student.add_grade("数学", 92)
regular_student.add_grade("英语", 85)

print(f"优化学生: {optimized_student}")
print(f"GPA: {optimized_student.gpa:.2f}")
print(f"常规学生: {regular_student}")
print(f"GPA: {regular_student.gpa:.2f}")

print("\n内存使用对比:")
print(f"优化学生内存使用: {optimized_student.get_memory_usage()} 字节")
print(f"常规学生内存使用: {regular_student.get_memory_usage()} 字节")

print("\n属性访问测试:")
print(f"优化学生可访问属性: {[attr for attr in dir(optimized_student) if not attr.startswith('_')]}")
print(f"常规学生可访问属性: {[attr for attr in dir(regular_student) if not attr.startswith('_')]}")

print("\n动态属性测试:")
# 常规学生可以动态添加属性
regular_student.extra_info = "可以添加额外属性"
print(f"常规学生添加额外属性成功: {regular_student.extra_info}")

# 优化学生不能动态添加属性
try:
    optimized_student.extra_info = "尝试添加额外属性"
except AttributeError as e:
    print(f"优化学生添加额外属性失败: {e}")

print("\n__dict__属性对比:")
print(f"常规学生有__dict__: {hasattr(regular_student, '__dict__')}")
print(f"优化学生有__dict__: {hasattr(optimized_student, '__dict__')}")

if hasattr(regular_student, '__dict__'):
    print(f"常规学生__dict__: {regular_student.__dict__}")

print(f"优化学生__slots__: {optimized_student.__slots__}")
```

## 学习要点总结

### 核心概念
1. **实例属性**：属于特定对象实例的数据，每个对象独立拥有
2. **动态属性**：可以在运行时添加、修改、删除的属性
3. **属性访问控制**：通过property装饰器和描述符控制属性访问
4. **属性验证**：确保属性值符合预期的类型和范围

### 重要特性
1. **属性独立性**：不同对象的同名属性是独立的
2. **动态性**：Python允许动态添加和删除属性
3. **访问控制**：可以通过多种方式控制属性的读写权限
4. **内存优化**：使用__slots__可以减少内存使用

### 属性操作方法
1. **直接访问**：`obj.attr`
2. **getattr/setattr**：`getattr(obj, 'attr')`, `setattr(obj, 'attr', value)`
3. **hasattr/delattr**：`hasattr(obj, 'attr')`, `delattr(obj, 'attr')`
4. **property装饰器**：创建计算属性和访问控制
5. **属性描述符**：更高级的属性控制机制

### 最佳实践
1. **属性命名**：使用清晰、有意义的属性名
2. **私有属性**：使用下划线前缀表示内部属性
3. **属性验证**：在setter中验证属性值的有效性
4. **文档说明**：为重要属性编写文档字符串
5. **内存考虑**：对于大量对象，考虑使用__slots__

### 注意事项
1. 避免在循环中频繁使用getattr/setattr
2. 谨慎使用动态属性，可能影响代码可读性
3. property装饰器的getter、setter、deleter要保持一致
4. __slots__限制了动态属性添加，需要权衡利弊

## 练习建议

1. **基础练习**：创建一个 `Person` 类，实现姓名、年龄等属性的管理

2. **进阶练习**：设计一个 `BankAccount` 类，使用property控制余额访问

3. **高级练习**：实现一个配置管理类，支持动态属性和属性验证

## 下一步学习

掌握了实例属性的操作后，接下来学习：
- [构造方法__init__](./05_constructor_method.md)
- [私有属性和访问控制](./06_private_attributes.md)
- [类属性和类方法](./07_class_attributes.md)