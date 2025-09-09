# 类属性和类方法

## 学习目标
- 理解类属性与实例属性的区别
- 掌握类方法和静态方法的定义和使用
- 学会类属性的继承和重写机制
- 了解类方法的实际应用场景
- 掌握类级别的数据管理

## 类属性基础

### 类属性与实例属性的区别

```python
class AttributeDemo:
    """属性演示类"""
    
    # 类属性 - 属于类本身，所有实例共享
    class_name = "AttributeDemo"
    instance_count = 0
    default_settings = {
        "theme": "light",
        "language": "zh-CN",
        "auto_save": True
    }
    
    def __init__(self, name, value):
        """构造方法 - 创建实例属性"""
        # 实例属性 - 属于具体实例，每个实例独有
        self.name = name
        self.value = value
        self.created_at = self._get_current_time()
        
        # 修改类属性（通过类名访问）
        AttributeDemo.instance_count += 1
        
        print(f"创建实例: {name}, 当前实例总数: {AttributeDemo.instance_count}")
    
    def _get_current_time(self):
        """获取当前时间"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def show_attributes(self):
        """显示所有属性"""
        print(f"\n=== {self.name} 的属性信息 ===")
        
        print("实例属性:")
        print(f"  name: {self.name}")
        print(f"  value: {self.value}")
        print(f"  created_at: {self.created_at}")
        
        print("类属性（通过实例访问）:")
        print(f"  class_name: {self.class_name}")
        print(f"  instance_count: {self.instance_count}")
        print(f"  default_settings: {self.default_settings}")
        
        print("类属性（通过类名访问）:")
        print(f"  class_name: {AttributeDemo.class_name}")
        print(f"  instance_count: {AttributeDemo.instance_count}")
        print(f"  default_settings: {AttributeDemo.default_settings}")
    
    def modify_class_attribute(self, new_theme):
        """修改类属性"""
        print(f"\n{self.name} 尝试修改类属性...")
        
        # 错误方式：通过实例修改（实际上创建了同名的实例属性）
        print("错误方式 - 通过实例修改:")
        old_theme = self.default_settings["theme"]
        self.default_settings = self.default_settings.copy()  # 创建副本
        self.default_settings["theme"] = new_theme
        print(f"  实例 {self.name} 的 theme: {self.default_settings['theme']}")
        print(f"  类的 theme: {AttributeDemo.default_settings['theme']}")
        
        # 正确方式：通过类名修改
        print("\n正确方式 - 通过类名修改:")
        AttributeDemo.default_settings["theme"] = new_theme
        print(f"  类的 theme: {AttributeDemo.default_settings['theme']}")
        print(f"  所有实例都会看到这个变化")
    
    @classmethod
    def get_instance_count(cls):
        """类方法 - 获取实例数量"""
        return cls.instance_count
    
    @classmethod
    def reset_settings(cls):
        """类方法 - 重置默认设置"""
        cls.default_settings = {
            "theme": "light",
            "language": "zh-CN",
            "auto_save": True
        }
        print("默认设置已重置")
    
    def __str__(self):
        return f"AttributeDemo(name='{self.name}', value={self.value})"

# 类属性与实例属性演示
print("=== 类属性与实例属性演示 ===")

# 创建多个实例
print("创建实例:")
obj1 = AttributeDemo("对象1", 100)
obj2 = AttributeDemo("对象2", 200)
obj3 = AttributeDemo("对象3", 300)

print(f"\n当前实例总数: {AttributeDemo.get_instance_count()}")

# 显示属性信息
obj1.show_attributes()
obj2.show_attributes()

print("\n=== 类属性修改演示 ===")

# 通过类名修改类属性
print("通过类名修改类属性:")
AttributeDemo.default_settings["theme"] = "dark"
print(f"修改后，所有实例看到的 theme: {obj1.default_settings['theme']}")
print(f"obj2 看到的 theme: {obj2.default_settings['theme']}")
print(f"obj3 看到的 theme: {obj3.default_settings['theme']}")

# 通过实例"修改"类属性（实际创建实例属性）
print("\n通过实例'修改'类属性:")
obj1.default_settings = {"theme": "custom", "language": "en-US"}
print(f"obj1 的 theme: {obj1.default_settings['theme']}")
print(f"obj2 的 theme: {obj2.default_settings['theme']}")
print(f"类的 theme: {AttributeDemo.default_settings['theme']}")

print("\n检查属性归属:")
print(f"obj1 是否有自己的 default_settings: {'default_settings' in obj1.__dict__}")
print(f"obj2 是否有自己的 default_settings: {'default_settings' in obj2.__dict__}")

# 重置设置
AttributeDemo.reset_settings()
print(f"\n重置后 obj2 的 theme: {obj2.default_settings['theme']}")
print(f"重置后 obj1 的 theme: {obj1.default_settings['theme']}")
```

### 类方法和静态方法

```python
class MathUtils:
    """数学工具类 - 演示类方法和静态方法"""
    
    # 类属性
    calculation_count = 0
    pi = 3.14159265359
    
    def __init__(self, name="计算器"):
        """构造方法"""
        self.name = name
        self.history = []
        print(f"{name} 已创建")
    
    # 实例方法
    def add_to_history(self, operation, result):
        """添加到历史记录（实例方法）"""
        self.history.append({
            "operation": operation,
            "result": result,
            "timestamp": self._get_timestamp()
        })
    
    def _get_timestamp(self):
        """获取时间戳（实例方法）"""
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")
    
    def calculate(self, a, b, operation):
        """计算方法（实例方法）"""
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                raise ValueError("除数不能为零")
            result = a / b
        else:
            raise ValueError(f"不支持的操作: {operation}")
        
        # 更新类属性
        MathUtils.calculation_count += 1
        
        # 添加到实例历史
        self.add_to_history(f"{a} {operation} {b}", result)
        
        return result
    
    # 类方法 - 使用 @classmethod 装饰器
    @classmethod
    def get_calculation_count(cls):
        """获取总计算次数（类方法）"""
        return cls.calculation_count
    
    @classmethod
    def reset_calculation_count(cls):
        """重置计算次数（类方法）"""
        cls.calculation_count = 0
        print("计算次数已重置")
    
    @classmethod
    def create_scientific_calculator(cls):
        """工厂方法 - 创建科学计算器（类方法）"""
        calculator = cls("科学计算器")
        calculator.mode = "scientific"
        return calculator
    
    @classmethod
    def create_basic_calculator(cls):
        """工厂方法 - 创建基础计算器（类方法）"""
        calculator = cls("基础计算器")
        calculator.mode = "basic"
        return calculator
    
    @classmethod
    def from_config(cls, config):
        """从配置创建实例（类方法）"""
        name = config.get("name", "默认计算器")
        calculator = cls(name)
        
        if "pi_precision" in config:
            cls.pi = round(cls.pi, config["pi_precision"])
        
        return calculator
    
    # 静态方法 - 使用 @staticmethod 装饰器
    @staticmethod
    def is_even(number):
        """判断是否为偶数（静态方法）"""
        return number % 2 == 0
    
    @staticmethod
    def is_prime(number):
        """判断是否为质数（静态方法）"""
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n):
        """计算阶乘（静态方法）"""
        if n < 0:
            raise ValueError("阶乘的参数必须是非负整数")
        if n == 0 or n == 1:
            return 1
        
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def gcd(a, b):
        """计算最大公约数（静态方法）"""
        while b:
            a, b = b, a % b
        return abs(a)
    
    @staticmethod
    def lcm(a, b):
        """计算最小公倍数（静态方法）"""
        return abs(a * b) // MathUtils.gcd(a, b)
    
    @staticmethod
    def validate_number(value):
        """验证数字（静态方法）"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"期望数字类型，得到 {type(value).__name__}")
        if isinstance(value, float) and (value != value):  # 检查 NaN
            raise ValueError("不能是 NaN")
        return True
    
    # 混合使用示例
    @classmethod
    def batch_calculate(cls, operations):
        """批量计算（类方法调用静态方法）"""
        calculator = cls("批量计算器")
        results = []
        
        for op in operations:
            a, b, operation = op
            
            # 使用静态方法验证
            cls.validate_number(a)
            cls.validate_number(b)
            
            # 使用实例方法计算
            result = calculator.calculate(a, b, operation)
            results.append(result)
        
        return results, calculator
    
    def get_statistics(self):
        """获取统计信息（实例方法）"""
        return {
            "计算器名称": self.name,
            "个人计算次数": len(self.history),
            "全局计算次数": self.calculation_count,
            "最近计算": self.history[-3:] if self.history else []
        }
    
    def __str__(self):
        return f"MathUtils: {self.name}"
    
    def __repr__(self):
        return f"MathUtils(name='{self.name}')"

# 类方法和静态方法演示
print("\n=== 类方法和静态方法演示 ===")

# 1. 静态方法调用（不需要实例）
print("1. 静态方法调用:")
print(f"12 是偶数吗? {MathUtils.is_even(12)}")
print(f"13 是质数吗? {MathUtils.is_prime(13)}")
print(f"5 的阶乘: {MathUtils.factorial(5)}")
print(f"12 和 18 的最大公约数: {MathUtils.gcd(12, 18)}")
print(f"12 和 18 的最小公倍数: {MathUtils.lcm(12, 18)}")

# 2. 类方法调用
print("\n2. 类方法调用:")
print(f"当前计算次数: {MathUtils.get_calculation_count()}")

# 3. 工厂方法（类方法）
print("\n3. 工厂方法:")
scientific_calc = MathUtils.create_scientific_calculator()
basic_calc = MathUtils.create_basic_calculator()

print(f"科学计算器: {scientific_calc}, 模式: {scientific_calc.mode}")
print(f"基础计算器: {basic_calc}, 模式: {basic_calc.mode}")

# 4. 从配置创建（类方法）
print("\n4. 从配置创建:")
config = {"name": "高精度计算器", "pi_precision": 4}
config_calc = MathUtils.from_config(config)
print(f"配置计算器: {config_calc}, PI值: {MathUtils.pi}")

# 5. 实例方法使用
print("\n5. 实例方法使用:")
result1 = scientific_calc.calculate(10, 5, "+")
result2 = scientific_calc.calculate(20, 4, "/")
result3 = basic_calc.calculate(7, 3, "*")

print(f"科学计算器计算结果: {result1}, {result2}")
print(f"基础计算器计算结果: {result3}")
print(f"总计算次数: {MathUtils.get_calculation_count()}")

# 6. 批量计算（类方法）
print("\n6. 批量计算:")
operations = [(10, 2, "+"), (15, 3, "-"), (8, 4, "*"), (20, 5, "/")]
results, batch_calc = MathUtils.batch_calculate(operations)
print(f"批量计算结果: {results}")
print(f"批量计算后总次数: {MathUtils.get_calculation_count()}")

# 7. 统计信息
print("\n7. 统计信息:")
stats1 = scientific_calc.get_statistics()
stats2 = batch_calc.get_statistics()

print("科学计算器统计:")
for key, value in stats1.items():
    print(f"  {key}: {value}")

print("\n批量计算器统计:")
for key, value in stats2.items():
    print(f"  {key}: {value}")

# 8. 通过实例调用静态方法和类方法
print("\n8. 通过实例调用静态方法和类方法:")
print(f"通过实例调用静态方法 - 17 是质数吗? {scientific_calc.is_prime(17)}")
print(f"通过实例调用类方法 - 当前计算次数: {scientific_calc.get_calculation_count()}")

# 9. 重置计算次数
print("\n9. 重置计算次数:")
MathUtils.reset_calculation_count()
print(f"重置后计算次数: {MathUtils.get_calculation_count()}")
```

### 三种方法的比较

```python
class MethodComparison:
    """方法类型比较演示"""
    
    class_variable = "我是类变量"
    
    def __init__(self, name):
        self.name = name
        self.instance_variable = f"我是 {name} 的实例变量"
    
    # 实例方法
    def instance_method(self, value):
        """实例方法 - 可以访问实例和类的属性"""
        print(f"\n=== 实例方法 ===")
        print(f"调用者: {self.name}")
        print(f"参数: {value}")
        print(f"访问实例变量: {self.instance_variable}")
        print(f"访问类变量: {self.class_variable}")
        print(f"可以修改实例状态: {self.name} -> {self.name}_modified")
        self.name = f"{self.name}_modified"
        return f"实例方法返回: {value * 2}"
    
    # 类方法
    @classmethod
    def class_method(cls, value):
        """类方法 - 可以访问类属性，不能直接访问实例属性"""
        print(f"\n=== 类方法 ===")
        print(f"调用类: {cls.__name__}")
        print(f"参数: {value}")
        print(f"访问类变量: {cls.class_variable}")
        print(f"可以修改类状态: {cls.class_variable} -> 修改后的类变量")
        cls.class_variable = "修改后的类变量"
        
        # 不能访问实例属性
        # print(f"无法访问实例变量: {self.instance_variable}")  # 这会报错
        
        return f"类方法返回: {value * 3}"
    
    # 静态方法
    @staticmethod
    def static_method(value):
        """静态方法 - 不能访问类或实例属性"""
        print(f"\n=== 静态方法 ===")
        print(f"参数: {value}")
        print(f"无法访问类变量或实例变量")
        print(f"只能使用传入的参数和局部变量")
        
        # 不能访问类或实例属性
        # print(f"无法访问类变量: {cls.class_variable}")  # 这会报错
        # print(f"无法访问实例变量: {self.instance_variable}")  # 这会报错
        
        return f"静态方法返回: {value * 4}"
    
    # 演示方法
    def demonstrate_access(self):
        """演示不同方法的访问能力"""
        print(f"\n=== {self.name} 的方法访问演示 ===")
        
        # 实例方法调用
        result1 = self.instance_method(10)
        print(f"实例方法结果: {result1}")
        
        # 类方法调用（通过实例）
        result2 = self.class_method(10)
        print(f"类方法结果: {result2}")
        
        # 静态方法调用（通过实例）
        result3 = self.static_method(10)
        print(f"静态方法结果: {result3}")
        
        print(f"\n调用后实例状态: {self.name}")
        print(f"调用后类状态: {self.class_variable}")
    
    @classmethod
    def demonstrate_class_access(cls):
        """演示类方法的访问能力"""
        print(f"\n=== 类级别的方法访问演示 ===")
        
        # 类方法调用（通过类）
        result1 = cls.class_method(20)
        print(f"类方法结果: {result1}")
        
        # 静态方法调用（通过类）
        result2 = cls.static_method(20)
        print(f"静态方法结果: {result2}")
        
        # 不能调用实例方法
        # result3 = cls.instance_method(20)  # 这会报错
        
        print(f"类状态: {cls.class_variable}")
    
    @staticmethod
    def demonstrate_static_access():
        """演示静态方法的访问能力"""
        print(f"\n=== 静态方法访问演示 ===")
        print("静态方法完全独立，不依赖类或实例")
        print("只能处理传入的参数")
        
        # 可以调用其他静态方法
        result = MethodComparison.static_method(30)
        print(f"调用其他静态方法结果: {result}")
        
        # 不能访问类或实例属性
        # print(f"无法访问: {cls.class_variable}")  # 报错
        # print(f"无法访问: {self.instance_variable}")  # 报错

# 方法比较演示
print("\n=== 方法类型比较演示 ===")

# 创建实例
obj1 = MethodComparison("对象1")
obj2 = MethodComparison("对象2")

print(f"初始类变量: {MethodComparison.class_variable}")

# 实例级别的演示
obj1.demonstrate_access()
obj2.demonstrate_access()

# 类级别的演示
MethodComparison.demonstrate_class_access()

# 静态方法演示
MethodComparison.demonstrate_static_access()

print("\n=== 调用方式总结 ===")
print("1. 实例方法:")
print("   - 通过实例调用: obj.instance_method()")
print("   - 通过类调用: Class.instance_method(obj)")

print("\n2. 类方法:")
print("   - 通过类调用: Class.class_method()")
print("   - 通过实例调用: obj.class_method()")

print("\n3. 静态方法:")
print("   - 通过类调用: Class.static_method()")
print("   - 通过实例调用: obj.static_method()")

# 验证调用方式
print("\n=== 验证不同调用方式 ===")

# 实例方法的两种调用方式
print("实例方法调用:")
result1 = obj1.instance_method(5)  # 常规方式
result2 = MethodComparison.instance_method(obj1, 5)  # 通过类调用
print(f"两种方式结果相同: {result1 == result2}")

# 类方法的两种调用方式
print("\n类方法调用:")
MethodComparison.class_variable = "重置类变量"  # 重置
result3 = MethodComparison.class_method(5)  # 通过类调用
MethodComparison.class_variable = "重置类变量"  # 重置
result4 = obj1.class_method(5)  # 通过实例调用
print(f"两种方式结果相同: {result3 == result4}")

# 静态方法的两种调用方式
print("\n静态方法调用:")
result5 = MethodComparison.static_method(5)  # 通过类调用
result6 = obj1.static_method(5)  # 通过实例调用
print(f"两种方式结果相同: {result5 == result6}")
```

### 类属性的继承和重写

```python
class BaseClass:
    """基类 - 演示类属性继承"""
    
    # 基类的类属性
    base_name = "BaseClass"
    shared_config = {
        "version": "1.0",
        "debug": False,
        "max_connections": 100
    }
    instance_count = 0
    
    def __init__(self, name):
        self.name = name
        BaseClass.instance_count += 1
        print(f"BaseClass 实例创建: {name}")
    
    @classmethod
    def get_info(cls):
        """获取类信息"""
        return {
            "类名": cls.__name__,
            "base_name": cls.base_name,
            "配置": cls.shared_config,
            "实例数量": cls.instance_count
        }
    
    @classmethod
    def update_config(cls, key, value):
        """更新配置"""
        cls.shared_config[key] = value
        print(f"{cls.__name__} 配置更新: {key} = {value}")
    
    def show_inheritance_chain(self):
        """显示继承链中的类属性"""
        print(f"\n=== {self.__class__.__name__} 的继承链属性 ===")
        
        for cls in self.__class__.__mro__:
            if hasattr(cls, 'base_name'):
                print(f"{cls.__name__}: base_name = {getattr(cls, 'base_name', 'N/A')}")
            if hasattr(cls, 'shared_config'):
                print(f"{cls.__name__}: shared_config = {getattr(cls, 'shared_config', 'N/A')}")

class ChildClass(BaseClass):
    """子类 - 继承并重写部分类属性"""
    
    # 重写基类的类属性
    base_name = "ChildClass"
    
    # 添加新的类属性
    child_specific = "子类特有属性"
    
    # 继承 shared_config（不重写）
    
    def __init__(self, name, child_value):
        super().__init__(name)
        self.child_value = child_value
        print(f"ChildClass 扩展初始化: {child_value}")
    
    @classmethod
    def get_child_info(cls):
        """获取子类特有信息"""
        base_info = super().get_info()
        base_info["child_specific"] = cls.child_specific
        return base_info
    
    @classmethod
    def reset_parent_config(cls):
        """重置父类配置"""
        # 注意：这会影响父类的配置
        BaseClass.shared_config = {
            "version": "1.0",
            "debug": False,
            "max_connections": 100
        }
        print("父类配置已重置")

class GrandChildClass(ChildClass):
    """孙子类 - 进一步继承和重写"""
    
    # 再次重写类属性
    base_name = "GrandChildClass"
    
    # 重写继承的配置（创建自己的副本）
    shared_config = {
        "version": "2.0",
        "debug": True,
        "max_connections": 200,
        "advanced_features": True
    }
    
    # 添加孙子类特有属性
    grandchild_specific = "孙子类特有属性"
    
    def __init__(self, name, child_value, grandchild_value):
        super().__init__(name, child_value)
        self.grandchild_value = grandchild_value
        print(f"GrandChildClass 扩展初始化: {grandchild_value}")
    
    @classmethod
    def get_full_info(cls):
        """获取完整信息"""
        info = super().get_child_info()
        info["grandchild_specific"] = cls.grandchild_specific
        return info

# 类属性继承演示
print("\n=== 类属性继承和重写演示 ===")

# 创建各级实例
print("创建实例:")
base_obj = BaseClass("基类对象")
child_obj = ChildClass("子类对象", "子类值")
grandchild_obj = GrandChildClass("孙子类对象", "子类值", "孙子类值")

print("\n=== 类属性访问 ===")

# 查看各类的 base_name
print("base_name 属性:")
print(f"BaseClass.base_name: {BaseClass.base_name}")
print(f"ChildClass.base_name: {ChildClass.base_name}")
print(f"GrandChildClass.base_name: {GrandChildClass.base_name}")

print("\n通过实例访问:")
print(f"base_obj.base_name: {base_obj.base_name}")
print(f"child_obj.base_name: {child_obj.base_name}")
print(f"grandchild_obj.base_name: {grandchild_obj.base_name}")

# 查看共享配置
print("\nshared_config 属性:")
print(f"BaseClass.shared_config: {BaseClass.shared_config}")
print(f"ChildClass.shared_config: {ChildClass.shared_config}")
print(f"GrandChildClass.shared_config: {GrandChildClass.shared_config}")

print("\n=== 类属性修改影响 ===")

# 修改基类配置
print("修改基类配置:")
BaseClass.update_config("debug", True)
print(f"修改后 BaseClass.shared_config: {BaseClass.shared_config}")
print(f"修改后 ChildClass.shared_config: {ChildClass.shared_config}")
print(f"修改后 GrandChildClass.shared_config: {GrandChildClass.shared_config}")

# 修改子类配置（实际上修改的是基类的）
print("\n通过子类修改配置:")
ChildClass.update_config("max_connections", 150)
print(f"修改后 BaseClass.shared_config: {BaseClass.shared_config}")
print(f"修改后 ChildClass.shared_config: {ChildClass.shared_config}")

# 孙子类有自己的配置副本，不受影响
print(f"GrandChildClass.shared_config（不受影响）: {GrandChildClass.shared_config}")

print("\n=== 实例计数 ===")
print(f"BaseClass.instance_count: {BaseClass.instance_count}")
print(f"ChildClass.instance_count: {ChildClass.instance_count}")
print(f"GrandChildClass.instance_count: {GrandChildClass.instance_count}")

# 创建更多实例
print("\n创建更多实例:")
child_obj2 = ChildClass("子类对象2", "值2")
grandchild_obj2 = GrandChildClass("孙子类对象2", "值2", "孙子值2")

print(f"创建后 BaseClass.instance_count: {BaseClass.instance_count}")

print("\n=== 类信息获取 ===")

# 获取各类信息
print("基类信息:")
base_info = BaseClass.get_info()
for key, value in base_info.items():
    print(f"  {key}: {value}")

print("\n子类信息:")
child_info = ChildClass.get_child_info()
for key, value in child_info.items():
    print(f"  {key}: {value}")

print("\n孙子类信息:")
grandchild_info = GrandChildClass.get_full_info()
for key, value in grandchild_info.items():
    print(f"  {key}: {value}")

print("\n=== 继承链分析 ===")
base_obj.show_inheritance_chain()
child_obj.show_inheritance_chain()
grandchild_obj.show_inheritance_chain()

print("\n=== 属性查找顺序（MRO）===")
print(f"GrandChildClass 的 MRO: {[cls.__name__ for cls in GrandChildClass.__mro__]}")

# 验证属性查找
print("\n属性查找验证:")
print(f"grandchild_obj.base_name 来源: {GrandChildClass.base_name}")
print(f"grandchild_obj.child_specific 来源: {GrandChildClass.child_specific}")

# 检查是否有自己的属性
print("\n类属性归属检查:")
print(f"GrandChildClass 是否有自己的 base_name: {'base_name' in GrandChildClass.__dict__}")
print(f"GrandChildClass 是否有自己的 shared_config: {'shared_config' in GrandChildClass.__dict__}")
print(f"GrandChildClass 是否有自己的 child_specific: {'child_specific' in GrandChildClass.__dict__}")

print(f"ChildClass 是否有自己的 shared_config: {'shared_config' in ChildClass.__dict__}")
print(f"BaseClass 是否有自己的 shared_config: {'shared_config' in BaseClass.__dict__}")
```

### 类方法的实际应用场景

```python
class DatabaseConnection:
    """数据库连接类 - 演示类方法的实际应用"""
    
    # 类属性 - 连接池和配置
    _connection_pool = []
    _max_connections = 10
    _active_connections = 0
    _connection_config = {
        "host": "localhost",
        "port": 5432,
        "database": "testdb",
        "timeout": 30
    }
    
    def __init__(self, connection_id):
        """私有构造方法 - 不应直接调用"""
        self.connection_id = connection_id
        self.is_active = True
        self.created_at = self._get_timestamp()
        self.last_used = self.created_at
        self.query_count = 0
        
        print(f"数据库连接 {connection_id} 已建立")
    
    def _get_timestamp(self):
        """获取时间戳"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 类方法 - 连接管理
    @classmethod
    def get_connection(cls):
        """获取数据库连接（连接池模式）"""
        # 检查是否有可用连接
        for conn in cls._connection_pool:
            if not conn.is_active:
                conn.is_active = True
                conn.last_used = conn._get_timestamp()
                cls._active_connections += 1
                print(f"重用连接: {conn.connection_id}")
                return conn
        
        # 检查是否超出最大连接数
        if cls._active_connections >= cls._max_connections:
            raise Exception(f"连接池已满，最大连接数: {cls._max_connections}")
        
        # 创建新连接
        connection_id = f"conn_{len(cls._connection_pool) + 1:03d}"
        new_conn = cls(connection_id)
        cls._connection_pool.append(new_conn)
        cls._active_connections += 1
        
        return new_conn
    
    @classmethod
    def release_connection(cls, connection):
        """释放连接回连接池"""
        if connection in cls._connection_pool and connection.is_active:
            connection.is_active = False
            cls._active_connections -= 1
            print(f"连接 {connection.connection_id} 已释放")
        else:
            print(f"连接 {connection.connection_id} 不在活动状态")
    
    @classmethod
    def get_pool_status(cls):
        """获取连接池状态"""
        return {
            "总连接数": len(cls._connection_pool),
            "活动连接数": cls._active_connections,
            "空闲连接数": len(cls._connection_pool) - cls._active_connections,
            "最大连接数": cls._max_connections,
            "连接详情": [
                {
                    "ID": conn.connection_id,
                    "状态": "活动" if conn.is_active else "空闲",
                    "创建时间": conn.created_at,
                    "最后使用": conn.last_used,
                    "查询次数": conn.query_count
                }
                for conn in cls._connection_pool
            ]
        }
    
    @classmethod
    def configure(cls, **kwargs):
        """配置数据库连接参数"""
        for key, value in kwargs.items():
            if key in cls._connection_config:
                cls._connection_config[key] = value
                print(f"配置更新: {key} = {value}")
            elif key == "max_connections":
                cls._max_connections = value
                print(f"最大连接数设置为: {value}")
            else:
                print(f"未知配置项: {key}")
    
    @classmethod
    def cleanup_idle_connections(cls, max_idle_time=300):
        """清理长时间空闲的连接"""
        from datetime import datetime, timedelta
        
        current_time = datetime.now()
        cleaned_count = 0
        
        # 创建新的连接池列表，排除需要清理的连接
        new_pool = []
        for conn in cls._connection_pool:
            if not conn.is_active:
                # 检查空闲时间
                last_used = datetime.strptime(conn.last_used, "%Y-%m-%d %H:%M:%S")
                idle_time = (current_time - last_used).total_seconds()
                
                if idle_time > max_idle_time:
                    print(f"清理空闲连接: {conn.connection_id} (空闲 {idle_time:.0f} 秒)")
                    cleaned_count += 1
                    continue
            
            new_pool.append(conn)
        
        cls._connection_pool = new_pool
        print(f"清理完成，移除了 {cleaned_count} 个空闲连接")
        return cleaned_count
    
    @classmethod
    def create_connection_factory(cls, config_name):
        """工厂方法 - 根据配置创建特定类型的连接"""
        configs = {
            "development": {
                "host": "dev.example.com",
                "database": "dev_db",
                "max_connections": 5
            },
            "production": {
                "host": "prod.example.com",
                "database": "prod_db",
                "max_connections": 20
            },
            "testing": {
                "host": "test.example.com",
                "database": "test_db",
                "max_connections": 3
            }
        }
        
        if config_name not in configs:
            raise ValueError(f"未知配置: {config_name}")
        
        # 应用配置
        config = configs[config_name]
        cls.configure(**config)
        
        print(f"已配置为 {config_name} 环境")
        return cls
    
    # 实例方法
    def execute_query(self, query):
        """执行查询"""
        if not self.is_active:
            raise Exception(f"连接 {self.connection_id} 未激活")
        
        self.query_count += 1
        self.last_used = self._get_timestamp()
        
        # 模拟查询执行
        print(f"连接 {self.connection_id} 执行查询: {query[:50]}...")
        return f"查询结果 (连接: {self.connection_id}, 查询 #{self.query_count})"
    
    def get_connection_info(self):
        """获取连接信息"""
        return {
            "连接ID": self.connection_id,
            "状态": "活动" if self.is_active else "空闲",
            "创建时间": self.created_at,
            "最后使用": self.last_used,
            "查询次数": self.query_count
        }
    
    def close(self):
        """关闭连接"""
        DatabaseConnection.release_connection(self)
    
    def __enter__(self):
        """上下文管理器入口"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.close()
    
    def __str__(self):
        status = "活动" if self.is_active else "空闲"
        return f"DatabaseConnection({self.connection_id}, {status})"
    
    def __repr__(self):
        return f"DatabaseConnection(connection_id='{self.connection_id}')"

# 数据库连接池演示
print("\n=== 数据库连接池演示 ===")

# 1. 配置数据库连接
print("1. 配置数据库连接:")
DatabaseConnection.configure(host="192.168.1.100", port=3306, max_connections=5)

# 2. 获取连接
print("\n2. 获取数据库连接:")
conn1 = DatabaseConnection.get_connection()
conn2 = DatabaseConnection.get_connection()
conn3 = DatabaseConnection.get_connection()

print(f"获得连接: {conn1}, {conn2}, {conn3}")

# 3. 查看连接池状态
print("\n3. 连接池状态:")
status = DatabaseConnection.get_pool_status()
print(f"总连接数: {status['总连接数']}")
print(f"活动连接数: {status['活动连接数']}")
print(f"空闲连接数: {status['空闲连接数']}")

# 4. 使用连接执行查询
print("\n4. 执行数据库查询:")
result1 = conn1.execute_query("SELECT * FROM users WHERE age > 18")
result2 = conn2.execute_query("INSERT INTO logs (message) VALUES ('系统启动')")
result3 = conn3.execute_query("UPDATE settings SET theme = 'dark' WHERE user_id = 1")

print(f"查询结果: {result1}")
print(f"查询结果: {result2}")
print(f"查询结果: {result3}")

# 5. 释放连接
print("\n5. 释放连接:")
DatabaseConnection.release_connection(conn1)
DatabaseConnection.release_connection(conn2)

# 6. 重用连接
print("\n6. 重用连接:")
conn4 = DatabaseConnection.get_connection()  # 应该重用之前释放的连接
conn5 = DatabaseConnection.get_connection()

print(f"重用的连接: {conn4}, {conn5}")

# 7. 使用上下文管理器
print("\n7. 使用上下文管理器:")
with DatabaseConnection.get_connection() as conn:
    result = conn.execute_query("SELECT COUNT(*) FROM products")
    print(f"上下文管理器查询结果: {result}")
    print(f"连接信息: {conn.get_connection_info()}")

print("上下文管理器自动释放连接")

# 8. 工厂方法
print("\n8. 使用工厂方法配置不同环境:")

# 开发环境
dev_factory = DatabaseConnection.create_connection_factory("development")
dev_conn = dev_factory.get_connection()
print(f"开发环境连接: {dev_conn}")

# 9. 连接池清理
print("\n9. 连接池清理:")
import time
time.sleep(1)  # 等待一秒
cleaned = DatabaseConnection.cleanup_idle_connections(max_idle_time=0)  # 立即清理

# 10. 最终状态
print("\n10. 最终连接池状态:")
final_status = DatabaseConnection.get_pool_status()
print(f"最终状态 - 总连接: {final_status['总连接数']}, 活动: {final_status['活动连接数']}")

for detail in final_status['连接详情']:
    print(f"  {detail['ID']}: {detail['状态']}, 查询次数: {detail['查询次数']}")

# 11. 测试连接数限制
print("\n11. 测试连接数限制:")
try:
    # 尝试获取超过限制的连接
    connections = []
    for i in range(10):  # 尝试获取10个连接（超过限制）
        conn = DatabaseConnection.get_connection()
        connections.append(conn)
        print(f"获得连接 {i+1}: {conn}")
except Exception as e:
    print(f"达到连接限制: {e}")

print("\n=== 类方法应用总结 ===")
print("类方法的主要应用场景:")
print("1. 工厂方法 - 创建类的实例")
print("2. 配置管理 - 管理类级别的配置")
print("3. 资源池管理 - 管理共享资源")
print("4. 统计信息 - 获取类级别的统计数据")
print("5. 替代构造器 - 提供多种创建实例的方式")
```

## 学习要点总结

### 类属性特点
1. **共享性**：所有实例共享同一个类属性
2. **访问方式**：可通过类名或实例访问
3. **修改影响**：通过类名修改会影响所有实例
4. **继承性**：子类继承父类的类属性

### 实例属性 vs 类属性
| 特性 | 实例属性 | 类属性 |
|------|----------|--------|
| 归属 | 属于具体实例 | 属于类本身 |
| 共享 | 每个实例独有 | 所有实例共享 |
| 访问 | 通过实例访问 | 通过类名或实例访问 |
| 修改 | 只影响当前实例 | 影响所有实例 |
| 内存 | 每个实例占用内存 | 类级别占用内存 |

### 方法类型比较
| 方法类型 | 装饰器 | 第一个参数 | 访问能力 | 调用方式 |
|----------|--------|------------|----------|----------|
| 实例方法 | 无 | self | 实例+类属性 | obj.method() |
| 类方法 | @classmethod | cls | 类属性 | Class.method() |
| 静态方法 | @staticmethod | 无 | 无特殊访问 | Class.method() |

### 类方法应用场景
1. **工厂方法**：提供多种创建实例的方式
2. **配置管理**：管理类级别的配置参数
3. **资源管理**：管理连接池、缓存等共享资源
4. **统计功能**：获取类级别的统计信息
5. **替代构造器**：根据不同参数创建实例

### 静态方法应用场景
1. **工具函数**：与类相关但不需要访问类/实例属性
2. **验证函数**：参数验证、数据校验
3. **计算函数**：数学计算、算法实现
4. **转换函数**：数据格式转换

### 继承中的类属性
1. **继承规则**：子类继承父类的类属性
2. **重写机制**：子类可以重写父类的类属性
3. **查找顺序**：按照MRO（方法解析顺序）查找
4. **修改影响**：修改父类属性会影响未重写的子类

## 练习建议

1. **基础练习**：创建一个 `Counter` 类，使用类属性统计实例数量

2. **进阶练习**：设计一个 `ConfigManager` 类，使用类方法管理应用配置

3. **高级练习**：实现一个完整的对象池系统，包含获取、释放、清理功能

## 下一步学习

掌握了类属性和类方法后，接下来学习：
- [综合练习](./08_exercises.md) - 将所有知识点整合应用
- 继承和多态
- 特殊方法和运算符重载