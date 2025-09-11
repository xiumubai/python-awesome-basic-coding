# 03_random_module.py - Random模块详解

## 学习目标

通过本节学习，你将掌握：
- random模块的基本随机数生成方法
- 随机选择和抽样操作
- 随机序列操作（打乱、排序等）
- 概率分布函数的使用
- 随机种子的设置和状态管理
- 安全随机数的生成（secrets模块）
- random模块在实际项目中的应用

## 重点知识

### 1. 基本随机数生成
```python
import random
import secrets
import string
from collections import Counter

def basic_random_demo():
    """基本随机数生成演示"""
    print("=" * 50)
    print("基本随机数生成")
    print("=" * 50)
    
    # 生成0-1之间的随机浮点数
    print(f"random(): {random.random()}")
    
    # 生成指定范围的随机整数
    print(f"randint(1, 10): {random.randint(1, 10)}")
    print(f"randrange(0, 10, 2): {random.randrange(0, 10, 2)}")
    
    # 生成指定范围的随机浮点数
    print(f"uniform(1.0, 10.0): {random.uniform(1.0, 10.0)}")
    
    # 生成多个随机数
    random_ints = [random.randint(1, 100) for _ in range(5)]
    print(f"5个随机整数: {random_ints}")
    
    random_floats = [round(random.uniform(0, 1), 3) for _ in range(5)]
    print(f"5个随机浮点数: {random_floats}")
    
    print()
```

### 2. 随机选择和抽样
```python
def random_choice_demo():
    """随机选择和抽样演示"""
    print("=" * 50)
    print("随机选择和抽样")
    print("=" * 50)
    
    # 从序列中随机选择一个元素
    colors = ['红', '绿', '蓝', '黄', '紫']
    print(f"随机选择颜色: {random.choice(colors)}")
    
    # 从序列中随机选择多个元素（有重复）
    choices = random.choices(colors, k=3)
    print(f"随机选择3个颜色（可重复）: {choices}")
    
    # 带权重的随机选择
    weights = [1, 2, 3, 4, 5]  # 权重越大，被选中概率越高
    weighted_choices = random.choices(colors, weights=weights, k=5)
    print(f"带权重的随机选择: {weighted_choices}")
    
    # 从序列中随机抽样（无重复）
    numbers = list(range(1, 21))  # 1到20的数字
    sample = random.sample(numbers, 5)
    print(f"从1-20中随机抽取5个数: {sample}")
    
    # 随机选择字符
    letters = string.ascii_letters
    random_string = ''.join(random.choices(letters, k=8))
    print(f"随机8位字符串: {random_string}")
    
    print()
```

### 3. 随机序列操作
```python
def sequence_operations_demo():
    """随机序列操作演示"""
    print("=" * 50)
    print("随机序列操作")
    print("=" * 50)
    
    # 随机打乱列表
    numbers = list(range(1, 11))
    print(f"原始列表: {numbers}")
    
    # shuffle()会直接修改原列表
    random.shuffle(numbers)
    print(f"打乱后: {numbers}")
    
    # 如果不想修改原列表，先复制
    original = list(range(1, 6))
    shuffled = original.copy()
    random.shuffle(shuffled)
    print(f"原列表: {original}")
    print(f"打乱的副本: {shuffled}")
    
    # 随机排列字符串
    word = "PYTHON"
    word_list = list(word)
    random.shuffle(word_list)
    shuffled_word = ''.join(word_list)
    print(f"原单词: {word}")
    print(f"打乱后: {shuffled_word}")
    
    # 生成随机排列
    cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7']
    print(f"\n洗牌前: {cards}")
    for i in range(3):
        deck = cards.copy()
        random.shuffle(deck)
        print(f"第{i+1}次洗牌: {deck}")
    
    print()
```

### 4. 概率分布
```python
def probability_distributions_demo():
    """概率分布演示"""
    print("=" * 50)
    print("概率分布")
    print("=" * 50)
    
    # 正态分布（高斯分布）
    normal_sample = [random.gauss(100, 15) for _ in range(10)]
    print(f"正态分布样本 (μ=100, σ=15): {[round(x, 1) for x in normal_sample]}")
    
    # 指数分布
    exp_sample = [random.expovariate(1.5) for _ in range(5)]
    print(f"指数分布样本 (λ=1.5): {[round(x, 2) for x in exp_sample]}")
    
    # 伽马分布
    gamma_sample = [random.gammavariate(2, 3) for _ in range(5)]
    print(f"伽马分布样本 (α=2, β=3): {[round(x, 2) for x in gamma_sample]}")
    
    # 贝塔分布
    beta_sample = [random.betavariate(2, 5) for _ in range(5)]
    print(f"贝塔分布样本 (α=2, β=5): {[round(x, 3) for x in beta_sample]}")
    
    # 均匀分布
    uniform_sample = [random.uniform(10, 20) for _ in range(5)]
    print(f"均匀分布样本 [10,20]: {[round(x, 2) for x in uniform_sample]}")
    
    # 三角分布
    triangle_sample = [random.triangular(0, 10, 3) for _ in range(5)]
    print(f"三角分布样本 (low=0, high=10, mode=3): {[round(x, 2) for x in triangle_sample]}")
    
    print()
```

### 5. 随机种子管理
```python
def random_seed_demo():
    """随机种子演示"""
    print("=" * 50)
    print("随机种子演示")
    print("=" * 50)
    
    # 设置随机种子，保证结果可重现
    print("使用相同种子生成随机数:")
    
    # 第一次
    random.seed(42)
    result1 = [random.randint(1, 100) for _ in range(5)]
    print(f"种子42，第一次: {result1}")
    
    # 第二次，使用相同种子
    random.seed(42)
    result2 = [random.randint(1, 100) for _ in range(5)]
    print(f"种子42，第二次: {result2}")
    
    print(f"两次结果相同: {result1 == result2}")
    
    # 不同种子产生不同结果
    random.seed(123)
    result3 = [random.randint(1, 100) for _ in range(5)]
    print(f"种子123: {result3}")
    
    # 获取当前随机状态
    state = random.getstate()
    num1 = random.randint(1, 100)
    
    # 恢复状态
    random.setstate(state)
    num2 = random.randint(1, 100)
    
    print(f"保存状态后的数字: {num1}")
    print(f"恢复状态后的数字: {num2}")
    print(f"两个数字相同: {num1 == num2}")
    
    print()
```

### 6. 安全随机数
```python
def secure_random_demo():
    """安全随机数演示"""
    print("=" * 50)
    print("安全随机数演示（用于密码学）")
    print("=" * 50)
    
    # secrets模块提供加密安全的随机数
    print(f"安全随机整数: {secrets.randbelow(1000)}")
    print(f"安全随机字节: {secrets.token_bytes(16).hex()}")
    print(f"安全随机字符串: {secrets.token_hex(16)}")
    print(f"安全URL安全字符串: {secrets.token_urlsafe(16)}")
    
    # 生成安全密码
    def generate_secure_password(length=12):
        """生成加密安全的密码"""
        alphabet = string.ascii_letters + string.digits + '!@#$%^&*'
        return ''.join(secrets.choice(alphabet) for _ in range(length))
    
    print(f"安全密码: {generate_secure_password()}")
    
    print()
```

### 7. 实际应用示例
```python
def practical_applications():
    """实际应用示例"""
    print("=" * 50)
    print("实际应用示例")
    print("=" * 50)
    
    # 1. 模拟掷骰子
    def roll_dice(num_dice=2, num_sides=6):
        """模拟掷骰子"""
        return [random.randint(1, num_sides) for _ in range(num_dice)]
    
    dice_result = roll_dice()
    print(f"掷两个骰子: {dice_result}, 总和: {sum(dice_result)}")
    
    # 2. 随机抽奖
    def lottery_draw(participants, num_winners=3):
        """随机抽奖"""
        if len(participants) < num_winners:
            return participants
        return random.sample(participants, num_winners)
    
    participants = [f"参与者{i}" for i in range(1, 21)]
    winners = lottery_draw(participants)
    print(f"抽奖获奖者: {winners}")
    
    # 3. 随机分组
    def random_groups(people, group_size=4):
        """随机分组"""
        shuffled = people.copy()
        random.shuffle(shuffled)
        groups = []
        for i in range(0, len(shuffled), group_size):
            groups.append(shuffled[i:i + group_size])
        return groups
    
    students = [f"学生{i}" for i in range(1, 13)]
    groups = random_groups(students, 3)
    print("随机分组结果:")
    for i, group in enumerate(groups, 1):
        print(f"  第{i}组: {group}")
    
    # 4. 生成测试数据
    def generate_test_data(num_records=5):
        """生成测试数据"""
        names = ['张三', '李四', '王五', '赵六', '钱七', '孙八', '周九', '吴十']
        departments = ['技术部', '销售部', '市场部', '人事部', '财务部']
        
        data = []
        for _ in range(num_records):
            record = {
                'name': random.choice(names),
                'age': random.randint(22, 60),
                'department': random.choice(departments),
                'salary': random.randint(5000, 20000),
                'score': round(random.uniform(60, 100), 1)
            }
            data.append(record)
        return data
    
    test_data = generate_test_data()
    print("\n生成的测试数据:")
    for record in test_data:
        print(f"  {record}")
    
    # 5. 随机颜色生成
    def random_color():
        """生成随机RGB颜色"""
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def random_hex_color():
        """生成随机十六进制颜色"""
        return f"#{random.randint(0, 0xFFFFFF):06x}"
    
    print(f"\n随机RGB颜色: {random_color()}")
    print(f"随机十六进制颜色: {random_hex_color()}")
    
    print()
```

### 8. 统计验证
```python
def statistics_demo():
    """统计演示"""
    print("=" * 50)
    print("随机数统计演示")
    print("=" * 50)
    
    # 生成大量随机数并统计分布
    sample_size = 10000
    dice_rolls = [random.randint(1, 6) for _ in range(sample_size)]
    
    # 统计每个数字出现的次数
    counter = Counter(dice_rolls)
    print(f"掷骰子{sample_size}次的统计结果:")
    for number in sorted(counter.keys()):
        count = counter[number]
        percentage = (count / sample_size) * 100
        print(f"  {number}: {count}次 ({percentage:.1f}%)")
    
    # 验证随机性（理论上每个数字应该出现约1/6的概率）
    expected = sample_size / 6
    print(f"\n理论期望值: {expected:.0f}次 (16.7%)")
    
    print()
```

## 运行示例

```bash
cd 29-standard-library
python3 03_random_module.py
```

## 学习要点

1. **基本随机数生成**：
   - `random()`: 生成0-1之间的随机浮点数
   - `randint(a, b)`: 生成指定范围的随机整数
   - `uniform(a, b)`: 生成指定范围的随机浮点数

2. **随机选择和抽样**：
   - `choice()`: 从序列中随机选择一个元素
   - `choices()`: 从序列中随机选择多个元素（可重复）
   - `sample()`: 从序列中随机抽样（无重复）

3. **序列操作**：
   - `shuffle()`: 随机打乱列表（就地修改）
   - 复制列表后再打乱可保留原列表

4. **概率分布**：
   - 支持正态分布、指数分布、伽马分布等
   - 适用于统计模拟和数据生成

5. **随机种子**：
   - `seed()`: 设置随机种子保证结果可重现
   - `getstate()`和`setstate()`: 保存和恢复随机状态

6. **安全随机数**：
   - `secrets`模块提供加密安全的随机数
   - 适用于密码生成、令牌创建等安全场景

## 注意事项

1. **random模块不适用于安全场景**，密码学应用请使用secrets模块
2. **shuffle()会直接修改原列表**，如需保留原列表请先复制
3. **随机种子的设置**会影响后续所有随机数生成
4. **大样本统计**可以验证随机数的分布特性
5. **权重选择**可以实现不均匀的随机选择
6. **状态管理**允许在特定点恢复随机数生成器状态

## 扩展练习

1. 实现一个简单的抽奖系统
2. 编写随机密码生成器
3. 模拟蒙特卡洛方法计算π值
4. 创建随机数据生成器用于测试
5. 实现加权随机选择算法