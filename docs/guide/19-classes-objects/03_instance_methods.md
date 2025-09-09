# 实例方法的定义和使用

## 学习目标
- 深入理解实例方法的概念和作用
- 掌握实例方法的定义语法和调用方式
- 理解self参数的含义和使用
- 学会设计和实现各种类型的实例方法
- 掌握方法的参数传递和返回值处理

## 实例方法基础

### 什么是实例方法

实例方法是定义在类中的函数，用于操作对象的属性或执行与对象相关的操作。每个实例方法的第一个参数必须是 `self`，它代表调用该方法的对象实例。

```python
class Calculator:
    def __init__(self, name):
        self.name = name
        self.result = 0
        self.history = []
    
    def add(self, number):
        """加法方法"""
        self.result += number
        self.history.append(f"+ {number} = {self.result}")
        return self.result
    
    def subtract(self, number):
        """减法方法"""
        self.result -= number
        self.history.append(f"- {number} = {self.result}")
        return self.result
    
    def multiply(self, number):
        """乘法方法"""
        self.result *= number
        self.history.append(f"× {number} = {self.result}")
        return self.result
    
    def divide(self, number):
        """除法方法"""
        if number != 0:
            self.result /= number
            self.history.append(f"÷ {number} = {self.result}")
            return self.result
        else:
            print("错误：除数不能为零")
            return self.result
    
    def clear(self):
        """清零方法"""
        self.result = 0
        self.history.append("清零")
    
    def get_result(self):
        """获取当前结果"""
        return self.result
    
    def get_history(self):
        """获取计算历史"""
        return self.history.copy()
    
    def show_info(self):
        """显示计算器信息"""
        print(f"计算器: {self.name}")
        print(f"当前结果: {self.result}")
        print(f"操作历史: {len(self.history)} 次操作")

# 实例方法使用演示
print("=== 实例方法基础演示 ===")
calc = Calculator("我的计算器")

# 调用实例方法
print("执行计算操作:")
print(f"初始值: {calc.get_result()}")
print(f"加 10: {calc.add(10)}")
print(f"乘 3: {calc.multiply(3)}")
print(f"减 5: {calc.subtract(5)}")
print(f"除 5: {calc.divide(5)}")

# 显示计算器信息
print("\n计算器状态:")
calc.show_info()

print("\n计算历史:")
for operation in calc.get_history():
    print(f"  {operation}")
```

### self参数详解

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []
    
    def introduce(self):
        """自我介绍方法 - 展示self的使用"""
        # self指向调用此方法的对象实例
        return f"大家好，我是{self.name}，今年{self.age}岁"
    
    def add_friend(self, friend_name):
        """添加朋友方法 - self用于访问实例属性"""
        if friend_name not in self.friends:
            self.friends.append(friend_name)
            return f"{self.name}和{friend_name}成为了朋友"
        return f"{friend_name}已经是{self.name}的朋友了"
    
    def remove_friend(self, friend_name):
        """删除朋友方法"""
        if friend_name in self.friends:
            self.friends.remove(friend_name)
            return f"{self.name}和{friend_name}不再是朋友了"
        return f"{friend_name}不在{self.name}的朋友列表中"
    
    def count_friends(self):
        """统计朋友数量"""
        return len(self.friends)
    
    def list_friends(self):
        """列出所有朋友"""
        if self.friends:
            return f"{self.name}的朋友有: {', '.join(self.friends)}"
        return f"{self.name}还没有朋友"
    
    def is_friend_with(self, friend_name):
        """检查是否是朋友"""
        return friend_name in self.friends
    
    def get_info(self):
        """获取完整信息 - 调用其他实例方法"""
        info = {
            "姓名": self.name,
            "年龄": self.age,
            "朋友数量": self.count_friends(),  # 调用其他实例方法
            "朋友列表": self.friends.copy()
        }
        return info

# self参数演示
print("\n=== self参数演示 ===")
person1 = Person("张三", 25)
person2 = Person("李四", 28)

print("创建两个Person对象:")
print(f"  {person1.introduce()}")
print(f"  {person2.introduce()}")

print("\n添加朋友关系:")
print(f"  {person1.add_friend('王五')}")
print(f"  {person1.add_friend('赵六')}")
print(f"  {person2.add_friend('钱七')}")
print(f"  {person2.add_friend('孙八')}")

print("\n查看朋友信息:")
print(f"  {person1.list_friends()}")
print(f"  {person2.list_friends()}")

print("\n对象信息对比:")
print(f"person1信息: {person1.get_info()}")
print(f"person2信息: {person2.get_info()}")

# 展示self的本质：self就是调用方法的对象
print("\n=== self的本质 ===")
print(f"person1对象ID: {id(person1)}")
print(f"person2对象ID: {id(person2)}")

# 这两种调用方式是等价的
print("\n等价的方法调用:")
print(f"person1.introduce(): {person1.introduce()}")
print(f"Person.introduce(person1): {Person.introduce(person1)}")
```

## 方法的参数和返回值

### 带参数的实例方法

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        self.account_status = "活跃"
    
    def deposit(self, amount, description="存款"):
        """存款方法 - 多个参数"""
        if amount <= 0:
            return False, "存款金额必须大于0"
        
        self.balance += amount
        transaction = {
            "类型": "存款",
            "金额": amount,
            "描述": description,
            "余额": self.balance,
            "时间": self._get_timestamp()
        }
        self.transaction_history.append(transaction)
        return True, f"存款成功，当前余额: ¥{self.balance}"
    
    def withdraw(self, amount, description="取款", allow_overdraft=False):
        """取款方法 - 包含默认参数和布尔参数"""
        if amount <= 0:
            return False, "取款金额必须大于0"
        
        if not allow_overdraft and amount > self.balance:
            return False, f"余额不足，当前余额: ¥{self.balance}"
        
        self.balance -= amount
        transaction = {
            "类型": "取款",
            "金额": amount,
            "描述": description,
            "余额": self.balance,
            "时间": self._get_timestamp()
        }
        self.transaction_history.append(transaction)
        return True, f"取款成功，当前余额: ¥{self.balance}"
    
    def transfer(self, target_account, amount, description="转账"):
        """转账方法 - 对象参数"""
        if amount <= 0:
            return False, "转账金额必须大于0"
        
        if amount > self.balance:
            return False, f"余额不足，当前余额: ¥{self.balance}"
        
        # 从当前账户扣款
        success, message = self.withdraw(amount, f"转账给{target_account.account_holder}")
        if not success:
            return False, message
        
        # 向目标账户存款
        target_success, target_message = target_account.deposit(amount, f"来自{self.account_holder}的转账")
        if not target_success:
            # 如果目标账户存款失败，回滚操作
            self.deposit(amount, "转账失败回滚")
            return False, "转账失败"
        
        return True, f"转账成功，向{target_account.account_holder}转账¥{amount}"
    
    def get_balance(self):
        """获取余额 - 无参数方法"""
        return self.balance
    
    def get_transaction_history(self, limit=None, transaction_type=None):
        """获取交易历史 - 可选参数"""
        history = self.transaction_history.copy()
        
        # 按类型过滤
        if transaction_type:
            history = [t for t in history if t["类型"] == transaction_type]
        
        # 限制数量
        if limit:
            history = history[-limit:]
        
        return history
    
    def calculate_interest(self, rate, months=12, compound=True):
        """计算利息 - 数值参数和布尔参数"""
        if self.balance <= 0:
            return 0
        
        if compound:
            # 复利计算
            final_amount = self.balance * ((1 + rate/12) ** months)
        else:
            # 单利计算
            final_amount = self.balance * (1 + rate * months/12)
        
        interest = final_amount - self.balance
        return {
            "本金": self.balance,
            "利率": f"{rate*100:.2f}%",
            "期限": f"{months}个月",
            "计息方式": "复利" if compound else "单利",
            "利息": round(interest, 2),
            "本息合计": round(final_amount, 2)
        }
    
    def _get_timestamp(self):
        """私有方法 - 获取时间戳"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_account_summary(self):
        """账户摘要 - 返回字典"""
        return {
            "账户持有人": self.account_holder,
            "当前余额": self.balance,
            "账户状态": self.account_status,
            "交易次数": len(self.transaction_history),
            "最后交易时间": self.transaction_history[-1]["时间"] if self.transaction_history else "无"
        }

# 方法参数和返回值演示
print("\n=== 方法参数和返回值演示 ===")

# 创建银行账户
account1 = BankAccount("张三", 1000)
account2 = BankAccount("李四", 500)

print("初始账户状态:")
print(f"  {account1.account_holder}: ¥{account1.get_balance()}")
print(f"  {account2.account_holder}: ¥{account2.get_balance()}")

print("\n=== 存款操作 ===")
success, message = account1.deposit(500, "工资存款")
print(f"张三存款: {message}")

success, message = account2.deposit(300)
print(f"李四存款: {message}")

print("\n=== 取款操作 ===")
success, message = account1.withdraw(200, "日常消费")
print(f"张三取款: {message}")

# 尝试透支
success, message = account2.withdraw(1000)
print(f"李四尝试取款¥1000: {message}")

print("\n=== 转账操作 ===")
success, message = account1.transfer(account2, 300, "朋友借款")
print(f"转账结果: {message}")

print("\n转账后余额:")
print(f"  {account1.account_holder}: ¥{account1.get_balance()}")
print(f"  {account2.account_holder}: ¥{account2.get_balance()}")

print("\n=== 利息计算 ===")
interest_info = account1.calculate_interest(0.05, 12, True)
print(f"张三账户利息计算:")
for key, value in interest_info.items():
    print(f"  {key}: {value}")

print("\n=== 交易历史 ===")
print("张三最近3笔交易:")
for transaction in account1.get_transaction_history(limit=3):
    print(f"  {transaction['时间']} - {transaction['类型']}: ¥{transaction['金额']} ({transaction['描述']})")

print("\n李四存款记录:")
for transaction in account2.get_transaction_history(transaction_type="存款"):
    print(f"  {transaction['时间']} - {transaction['类型']}: ¥{transaction['金额']} ({transaction['描述']})")
```

### 可变参数和关键字参数

```python
class DataProcessor:
    def __init__(self, name):
        self.name = name
        self.data = []
        self.processing_log = []
    
    def add_data(self, *values):
        """添加数据 - 可变位置参数"""
        added_count = 0
        for value in values:
            if isinstance(value, (int, float)):
                self.data.append(value)
                added_count += 1
        
        log_entry = f"添加了 {added_count} 个数据点"
        self.processing_log.append(log_entry)
        return added_count
    
    def calculate_statistics(self, **options):
        """计算统计信息 - 关键字参数"""
        if not self.data:
            return {"错误": "没有数据"}
        
        # 默认选项
        default_options = {
            "mean": True,
            "median": True,
            "mode": False,
            "std": False,
            "min_max": True,
            "count": True
        }
        
        # 更新选项
        default_options.update(options)
        
        stats = {}
        
        if default_options["count"]:
            stats["数据量"] = len(self.data)
        
        if default_options["mean"]:
            stats["平均值"] = sum(self.data) / len(self.data)
        
        if default_options["median"]:
            sorted_data = sorted(self.data)
            n = len(sorted_data)
            if n % 2 == 0:
                stats["中位数"] = (sorted_data[n//2-1] + sorted_data[n//2]) / 2
            else:
                stats["中位数"] = sorted_data[n//2]
        
        if default_options["min_max"]:
            stats["最小值"] = min(self.data)
            stats["最大值"] = max(self.data)
            stats["范围"] = max(self.data) - min(self.data)
        
        if default_options["std"]:
            mean = sum(self.data) / len(self.data)
            variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
            stats["标准差"] = variance ** 0.5
        
        if default_options["mode"]:
            from collections import Counter
            counter = Counter(self.data)
            most_common = counter.most_common(1)
            if most_common:
                stats["众数"] = most_common[0][0]
                stats["众数频次"] = most_common[0][1]
        
        self.processing_log.append(f"计算统计信息: {list(stats.keys())}")
        return stats
    
    def filter_data(self, condition_func, *args, **kwargs):
        """过滤数据 - 函数参数和混合参数"""
        original_count = len(self.data)
        
        try:
            # 应用过滤条件
            self.data = [x for x in self.data if condition_func(x, *args, **kwargs)]
            filtered_count = original_count - len(self.data)
            
            log_entry = f"过滤掉 {filtered_count} 个数据点，剩余 {len(self.data)} 个"
            self.processing_log.append(log_entry)
            return True, log_entry
        except Exception as e:
            return False, f"过滤失败: {str(e)}"
    
    def transform_data(self, transform_func, *args, **kwargs):
        """转换数据"""
        try:
            original_data = self.data.copy()
            self.data = [transform_func(x, *args, **kwargs) for x in self.data]
            
            log_entry = f"数据转换完成，处理了 {len(self.data)} 个数据点"
            self.processing_log.append(log_entry)
            return True, log_entry
        except Exception as e:
            self.data = original_data  # 回滚
            return False, f"转换失败: {str(e)}"
    
    def batch_process(self, *operations):
        """批量处理 - 可变参数（元组列表）"""
        results = []
        
        for operation in operations:
            if isinstance(operation, tuple) and len(operation) >= 2:
                method_name = operation[0]
                args = operation[1:] if len(operation) > 1 else ()
                
                if hasattr(self, method_name):
                    method = getattr(self, method_name)
                    try:
                        result = method(*args)
                        results.append((method_name, True, result))
                    except Exception as e:
                        results.append((method_name, False, str(e)))
                else:
                    results.append((method_name, False, "方法不存在"))
        
        return results
    
    def get_summary(self):
        """获取处理摘要"""
        return {
            "处理器名称": self.name,
            "数据量": len(self.data),
            "数据范围": f"{min(self.data) if self.data else 'N/A'} ~ {max(self.data) if self.data else 'N/A'}",
            "处理步骤": len(self.processing_log),
            "处理日志": self.processing_log.copy()
        }

# 可变参数演示
print("\n=== 可变参数和关键字参数演示 ===")

# 创建数据处理器
processor = DataProcessor("销售数据分析")

print("=== 添加数据（可变位置参数）===")
count1 = processor.add_data(100, 150, 200, 175, 300)
print(f"第一批添加: {count1} 个数据")

count2 = processor.add_data(250, 180, 220, 190, 280, 320, 150)
print(f"第二批添加: {count2} 个数据")

print(f"\n当前数据: {processor.data}")

print("\n=== 统计分析（关键字参数）===")
# 基本统计
basic_stats = processor.calculate_statistics()
print("基本统计:")
for key, value in basic_stats.items():
    print(f"  {key}: {value}")

# 详细统计
detailed_stats = processor.calculate_statistics(std=True, mode=True)
print("\n详细统计:")
for key, value in detailed_stats.items():
    print(f"  {key}: {value}")

# 自定义统计
custom_stats = processor.calculate_statistics(mean=False, median=False, std=True, min_max=True)
print("\n自定义统计:")
for key, value in custom_stats.items():
    print(f"  {key}: {value}")

print("\n=== 数据过滤和转换 ===")
# 定义过滤和转换函数
def greater_than(value, threshold):
    return value > threshold

def multiply_by(value, factor):
    return value * factor

def in_range(value, min_val, max_val):
    return min_val <= value <= max_val

# 过滤数据
print("过滤大于200的数据:")
success, message = processor.filter_data(greater_than, 200)
print(f"  {message}")
print(f"  过滤后数据: {processor.data}")

# 转换数据
print("\n将数据乘以1.1:")
success, message = processor.transform_data(multiply_by, 1.1)
print(f"  {message}")
print(f"  转换后数据: {[round(x, 1) for x in processor.data]}")

print("\n=== 批量处理 ===")
# 创建新的处理器进行批量操作
batch_processor = DataProcessor("批量处理器")

# 批量操作
operations = [
    ("add_data", 50, 75, 100, 125, 150),
    ("calculate_statistics",),
    ("filter_data", greater_than, 80),
    ("transform_data", multiply_by, 2)
]

results = batch_processor.batch_process(*operations)
print("批量处理结果:")
for method_name, success, result in results:
    status = "成功" if success else "失败"
    print(f"  {method_name}: {status}")
    if success and isinstance(result, dict):
        print(f"    结果: {result}")

print("\n=== 处理摘要 ===")
summary = processor.get_summary()
print(f"处理器: {summary['处理器名称']}")
print(f"数据量: {summary['数据量']}")
print(f"数据范围: {summary['数据范围']}")
print(f"处理步骤: {summary['处理步骤']}")
print("处理日志:")
for i, log in enumerate(summary['处理日志'], 1):
    print(f"  {i}. {log}")
```

## 方法的类型和分类

### 访问器方法（Getter）和修改器方法（Setter）

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius  # 使用下划线表示内部属性
    
    # Getter方法
    def get_celsius(self):
        """获取摄氏温度"""
        return self._celsius
    
    def get_fahrenheit(self):
        """获取华氏温度"""
        return (self._celsius * 9/5) + 32
    
    def get_kelvin(self):
        """获取开尔文温度"""
        return self._celsius + 273.15
    
    # Setter方法
    def set_celsius(self, celsius):
        """设置摄氏温度"""
        if celsius < -273.15:
            raise ValueError("温度不能低于绝对零度(-273.15°C)")
        self._celsius = celsius
    
    def set_fahrenheit(self, fahrenheit):
        """通过华氏温度设置"""
        celsius = (fahrenheit - 32) * 5/9
        self.set_celsius(celsius)
    
    def set_kelvin(self, kelvin):
        """通过开尔文温度设置"""
        if kelvin < 0:
            raise ValueError("开尔文温度不能为负数")
        celsius = kelvin - 273.15
        self.set_celsius(celsius)
    
    # 状态查询方法
    def is_freezing(self):
        """是否结冰"""
        return self._celsius <= 0
    
    def is_boiling(self):
        """是否沸腾（标准大气压下）"""
        return self._celsius >= 100
    
    def get_state(self):
        """获取物质状态"""
        if self._celsius < 0:
            return "固态（冰）"
        elif self._celsius < 100:
            return "液态（水）"
        else:
            return "气态（水蒸气）"
    
    # 比较方法
    def is_hotter_than(self, other_temp):
        """比较温度高低"""
        if isinstance(other_temp, Temperature):
            return self._celsius > other_temp._celsius
        return False
    
    def temperature_difference(self, other_temp):
        """计算温度差"""
        if isinstance(other_temp, Temperature):
            return abs(self._celsius - other_temp._celsius)
        return None
    
    # 格式化输出方法
    def to_string(self, unit="celsius"):
        """格式化温度字符串"""
        if unit.lower() == "celsius":
            return f"{self._celsius:.1f}°C"
        elif unit.lower() == "fahrenheit":
            return f"{self.get_fahrenheit():.1f}°F"
        elif unit.lower() == "kelvin":
            return f"{self.get_kelvin():.1f}K"
        else:
            return f"{self._celsius:.1f}°C"
    
    def get_all_units(self):
        """获取所有单位的温度"""
        return {
            "摄氏度": f"{self._celsius:.1f}°C",
            "华氏度": f"{self.get_fahrenheit():.1f}°F",
            "开尔文": f"{self.get_kelvin():.1f}K",
            "状态": self.get_state()
        }

# 访问器和修改器方法演示
print("\n=== 访问器和修改器方法演示 ===")

# 创建温度对象
temp1 = Temperature(25)  # 25°C
temp2 = Temperature()

print("初始温度:")
print(f"temp1: {temp1.to_string()}")
print(f"temp2: {temp2.to_string()}")

print("\n=== Getter方法演示 ===")
print(f"temp1的各种单位:")
all_units = temp1.get_all_units()
for unit, value in all_units.items():
    print(f"  {unit}: {value}")

print("\n=== Setter方法演示 ===")
print("设置temp2为华氏度100度:")
temp2.set_fahrenheit(100)
print(f"temp2: {temp2.to_string()} = {temp2.to_string('fahrenheit')}")

print("\n设置temp1为开尔文300度:")
temp1.set_kelvin(300)
print(f"temp1: {temp1.to_string()} = {temp1.to_string('kelvin')}")

print("\n=== 状态查询方法 ===")
temperatures = [
    Temperature(-10),
    Temperature(0),
    Temperature(25),
    Temperature(100),
    Temperature(150)
]

for i, temp in enumerate(temperatures):
    print(f"\n温度{i+1}: {temp.to_string()}")
    print(f"  状态: {temp.get_state()}")
    print(f"  结冰: {'是' if temp.is_freezing() else '否'}")
    print(f"  沸腾: {'是' if temp.is_boiling() else '否'}")

print("\n=== 比较方法 ===")
room_temp = Temperature(22)
hot_temp = Temperature(80)
cold_temp = Temperature(-5)

print(f"室温: {room_temp.to_string()}")
print(f"热水: {hot_temp.to_string()}")
print(f"冰水: {cold_temp.to_string()}")

print(f"\n热水比室温热: {hot_temp.is_hotter_than(room_temp)}")
print(f"冰水比室温热: {cold_temp.is_hotter_than(room_temp)}")
print(f"热水与室温差: {hot_temp.temperature_difference(room_temp):.1f}°C")
print(f"冰水与室温差: {cold_temp.temperature_difference(room_temp):.1f}°C")
```

### 工具方法和辅助方法

```python
class TextAnalyzer:
    def __init__(self, text=""):
        self.text = text
        self.analysis_cache = {}  # 缓存分析结果
    
    def set_text(self, text):
        """设置文本并清空缓存"""
        self.text = text
        self.analysis_cache.clear()
    
    # 基础工具方法
    def _clean_text(self, text=None):
        """私有方法：清理文本"""
        if text is None:
            text = self.text
        
        # 移除多余空格，转换为小写
        cleaned = ' '.join(text.split()).lower()
        return cleaned
    
    def _extract_words(self, text=None, include_punctuation=False):
        """私有方法：提取单词"""
        if text is None:
            text = self.text
        
        if include_punctuation:
            words = text.split()
        else:
            import re
            words = re.findall(r'\b\w+\b', text.lower())
        
        return words
    
    def _calculate_readability_score(self, sentences, words, syllables):
        """私有方法：计算可读性分数（简化版Flesch分数）"""
        if sentences == 0 or words == 0:
            return 0
        
        avg_sentence_length = words / sentences
        avg_syllables_per_word = syllables / words
        
        # 简化的Flesch可读性分数
        score = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syllables_per_word)
        return max(0, min(100, score))  # 限制在0-100之间
    
    def _count_syllables(self, word):
        """私有方法：估算单词音节数"""
        word = word.lower()
        vowels = 'aeiouy'
        syllable_count = 0
        prev_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not prev_was_vowel:
                syllable_count += 1
            prev_was_vowel = is_vowel
        
        # 至少有一个音节
        return max(1, syllable_count)
    
    # 公共分析方法
    def count_characters(self, include_spaces=True):
        """统计字符数"""
        cache_key = f"chars_{include_spaces}"
        if cache_key not in self.analysis_cache:
            if include_spaces:
                count = len(self.text)
            else:
                count = len(self.text.replace(' ', ''))
            self.analysis_cache[cache_key] = count
        
        return self.analysis_cache[cache_key]
    
    def count_words(self):
        """统计单词数"""
        if 'word_count' not in self.analysis_cache:
            words = self._extract_words()
            self.analysis_cache['word_count'] = len(words)
        
        return self.analysis_cache['word_count']
    
    def count_sentences(self):
        """统计句子数"""
        if 'sentence_count' not in self.analysis_cache:
            import re
            sentences = re.split(r'[.!?]+', self.text)
            # 过滤空句子
            sentences = [s.strip() for s in sentences if s.strip()]
            self.analysis_cache['sentence_count'] = len(sentences)
        
        return self.analysis_cache['sentence_count']
    
    def count_paragraphs(self):
        """统计段落数"""
        if 'paragraph_count' not in self.analysis_cache:
            paragraphs = [p.strip() for p in self.text.split('\n\n') if p.strip()]
            self.analysis_cache['paragraph_count'] = len(paragraphs)
        
        return self.analysis_cache['paragraph_count']
    
    def get_word_frequency(self, top_n=10):
        """获取词频统计"""
        cache_key = f"word_freq_{top_n}"
        if cache_key not in self.analysis_cache:
            words = self._extract_words()
            
            # 统计词频
            word_count = {}
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
            
            # 排序并取前N个
            sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
            self.analysis_cache[cache_key] = sorted_words[:top_n]
        
        return self.analysis_cache[cache_key]
    
    def get_readability_analysis(self):
        """获取可读性分析"""
        if 'readability' not in self.analysis_cache:
            words = self._extract_words()
            sentences = self.count_sentences()
            
            # 计算总音节数
            total_syllables = sum(self._count_syllables(word) for word in words)
            
            # 计算各种指标
            word_count = len(words)
            avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
            avg_sentence_length = word_count / sentences if sentences > 0 else 0
            
            readability_score = self._calculate_readability_score(sentences, word_count, total_syllables)
            
            # 可读性等级
            if readability_score >= 90:
                level = "非常容易"
            elif readability_score >= 80:
                level = "容易"
            elif readability_score >= 70:
                level = "较容易"
            elif readability_score >= 60:
                level = "标准"
            elif readability_score >= 50:
                level = "较难"
            elif readability_score >= 30:
                level = "困难"
            else:
                level = "非常困难"
            
            self.analysis_cache['readability'] = {
                "可读性分数": round(readability_score, 1),
                "可读性等级": level,
                "平均单词长度": round(avg_word_length, 1),
                "平均句子长度": round(avg_sentence_length, 1),
                "总音节数": total_syllables
            }
        
        return self.analysis_cache['readability']
    
    def get_comprehensive_analysis(self):
        """获取综合分析报告"""
        return {
            "基本统计": {
                "字符数（含空格）": self.count_characters(True),
                "字符数（不含空格）": self.count_characters(False),
                "单词数": self.count_words(),
                "句子数": self.count_sentences(),
                "段落数": self.count_paragraphs()
            },
            "词频分析": dict(self.get_word_frequency(5)),
            "可读性分析": self.get_readability_analysis(),
            "文本预览": self.text[:100] + "..." if len(self.text) > 100 else self.text
        }
    
    def clear_cache(self):
        """清空分析缓存"""
        self.analysis_cache.clear()
        return "缓存已清空"
    
    def get_cache_info(self):
        """获取缓存信息"""
        return {
            "缓存项数量": len(self.analysis_cache),
            "缓存键": list(self.analysis_cache.keys())
        }

# 工具方法和辅助方法演示
print("\n=== 工具方法和辅助方法演示 ===")

# 示例文本
sample_text = """
人工智能是计算机科学的一个分支，它企图了解智能的实质，并生产出一种新的能以人类智能相似的方式做出反应的智能机器。

该领域的研究包括机器人、语言识别、图像识别、自然语言处理和专家系统等。人工智能从诞生以来，理论和技术日益成熟，应用领域也不断扩大。

可以设想，未来人工智能带来的科技产品，将会是人类智慧的"容器"。人工智能可以对人的意识、思维的信息过程进行模拟。

人工智能不是人的智能，但能像人那样思考、也可能超过人的智能。
"""

# 创建文本分析器
analyzer = TextAnalyzer(sample_text)

print("=== 基本统计 ===")
print(f"字符数（含空格）: {analyzer.count_characters(True)}")
print(f"字符数（不含空格）: {analyzer.count_characters(False)}")
print(f"单词数: {analyzer.count_words()}")
print(f"句子数: {analyzer.count_sentences()}")
print(f"段落数: {analyzer.count_paragraphs()}")

print("\n=== 词频分析 ===")
word_freq = analyzer.get_word_frequency(8)
print("最常用的8个词:")
for word, count in word_freq:
    print(f"  '{word}': {count}次")

print("\n=== 可读性分析 ===")
readability = analyzer.get_readability_analysis()
for key, value in readability.items():
    print(f"{key}: {value}")

print("\n=== 缓存信息 ===")
cache_info = analyzer.get_cache_info()
print(f"缓存项数量: {cache_info['缓存项数量']}")
print(f"缓存键: {cache_info['缓存键']}")

print("\n=== 综合分析报告 ===")
comprehensive = analyzer.get_comprehensive_analysis()
for section, data in comprehensive.items():
    print(f"\n{section}:")
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"  {key}: {value}")
    else:
        print(f"  {data}")

# 测试缓存清理
print(f"\n清理前缓存项: {analyzer.get_cache_info()['缓存项数量']}")
analyzer.clear_cache()
print(f"清理后缓存项: {analyzer.get_cache_info()['缓存项数量']}")
```

## 学习要点总结

### 核心概念
1. **实例方法定义**：`def method_name(self, parameters):`
2. **self参数**：代表调用方法的对象实例，必须是第一个参数
3. **方法调用**：`object.method_name(arguments)`
4. **方法类型**：访问器、修改器、工具方法、辅助方法

### 重要特性
1. **参数传递**：支持位置参数、关键字参数、默认参数、可变参数
2. **返回值**：可以返回任何类型的数据，包括None
3. **方法重载**：Python不支持传统意义的方法重载，但可以通过默认参数实现
4. **私有方法**：以下划线开头的方法（约定为私有）

### 设计原则
1. **单一职责**：每个方法应该只做一件事
2. **命名清晰**：方法名应该清楚地表达其功能
3. **参数合理**：避免过多的参数，考虑使用对象或字典
4. **返回一致**：同一方法的返回值类型应该一致

### 最佳实践
1. **文档字符串**：为每个方法编写清晰的文档
2. **错误处理**：适当处理异常情况
3. **参数验证**：验证输入参数的有效性
4. **缓存机制**：对于计算密集的方法考虑缓存结果

### 注意事项
1. 实例方法必须通过对象实例调用
2. self参数由Python自动传递，调用时不需要显式传递
3. 在方法内部访问实例属性必须使用self
4. 私有方法只是约定，仍然可以从外部访问

## 练习建议

1. **基础练习**：创建一个 `Rectangle` 类，实现计算面积、周长等方法

2. **进阶练习**：设计一个 `ShoppingList` 类，支持添加、删除、搜索商品等功能

3. **综合练习**：实现一个 `StudentGradeManager` 类，包含成绩录入、统计分析等方法

## 下一步学习

掌握了实例方法的定义和使用后，接下来学习：
- [实例属性的操作](./04_instance_attributes.md)
- [构造方法__init__](./05_constructor_method.md)
- [私有属性和访问控制](./06_private_attributes.md)