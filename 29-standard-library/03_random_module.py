#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_random_module.py - 随机数生成模块学习

本文件演示Python random模块的各种功能：
1. 基本随机数生成
2. 随机选择和抽样
3. 随机序列操作
4. 概率分布
5. 随机种子设置
6. 实际应用示例

学习目标：
- 掌握random模块的基本用法
- 了解不同类型的随机数生成方法
- 学会使用随机种子保证结果可重现
- 掌握随机抽样和洗牌操作
"""

import random
import string
import secrets  # 用于加密安全的随机数
from collections import Counter

def basic_random_demo():
    """基本随机数生成演示"""
    print("=" * 50)
    print("基本随机数生成演示")
    print("=" * 50)
    
    # 生成0-1之间的随机浮点数
    print(f"随机浮点数 [0,1): {random.random():.6f}")
    
    # 生成指定范围的随机整数
    print(f"随机整数 [1,10]: {random.randint(1, 10)}")
    print(f"随机整数 [0,10): {random.randrange(0, 10)}")
    print(f"随机整数 [0,10,2): {random.randrange(0, 10, 2)}")
    
    # 生成指定范围的随机浮点数
    print(f"随机浮点数 [1.5,10.5]: {random.uniform(1.5, 10.5):.3f}")
    
    # 生成随机字符
    letters = string.ascii_letters
    print(f"随机字母: {random.choice(letters)}")
    
    print()

def random_choice_demo():
    """随机选择和抽样演示"""
    print("=" * 50)
    print("随机选择和抽样演示")
    print("=" * 50)
    
    # 从序列中随机选择一个元素
    colors = ['红', '绿', '蓝', '黄', '紫']
    print(f"随机颜色: {random.choice(colors)}")
    
    # 从序列中随机选择多个元素（有重复）
    print(f"随机选择3个颜色（可重复）: {random.choices(colors, k=3)}")
    
    # 带权重的随机选择
    weights = [1, 2, 3, 4, 5]  # 权重越大，被选中概率越高
    print(f"带权重的随机选择: {random.choices(colors, weights=weights, k=5)}")
    
    # 从序列中随机抽样（无重复）
    numbers = list(range(1, 21))  # 1-20的数字
    sample = random.sample(numbers, 5)
    print(f"从1-20中随机抽取5个数字: {sample}")
    
    # 随机抽样比例
    population = list(range(100))
    sample_size = int(len(population) * 0.1)  # 抽取10%
    sample = random.sample(population, sample_size)
    print(f"从100个数字中抽取10%: {len(sample)}个数字")
    
    print()

def sequence_operations_demo():
    """随机序列操作演示"""
    print("=" * 50)
    print("随机序列操作演示")
    print("=" * 50)
    
    # 洗牌操作
    deck = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    print(f"原始牌组: {deck}")
    
    # 洗牌（就地修改）
    random.shuffle(deck)
    print(f"洗牌后: {deck}")
    
    # 生成随机字符串
    def generate_random_string(length=8):
        """生成指定长度的随机字符串"""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))
    
    print(f"随机字符串: {generate_random_string()}")
    print(f"随机密码: {generate_random_string(12)}")
    
    # 生成随机列表
    random_list = [random.randint(1, 100) for _ in range(10)]
    print(f"随机数列表: {random_list}")
    
    print()

def probability_distributions_demo():
    """概率分布演示"""
    print("=" * 50)
    print("概率分布演示")
    print("=" * 50)
    
    # 正态分布（高斯分布）
    mu, sigma = 100, 15  # 均值100，标准差15
    normal_sample = [random.gauss(mu, sigma) for _ in range(10)]
    print(f"正态分布样本 (μ={mu}, σ={sigma}): {[round(x, 2) for x in normal_sample]}")
    
    # 指数分布
    lambd = 1.5
    exp_sample = [random.expovariate(lambd) for _ in range(5)]
    print(f"指数分布样本 (λ={lambd}): {[round(x, 3) for x in exp_sample]}")
    
    # 均匀分布
    uniform_sample = [random.uniform(10, 20) for _ in range(5)]
    print(f"均匀分布样本 [10,20]: {[round(x, 2) for x in uniform_sample]}")
    
    # 三角分布
    triangle_sample = [random.triangular(0, 10, 3) for _ in range(5)]
    print(f"三角分布样本 (low=0, high=10, mode=3): {[round(x, 2) for x in triangle_sample]}")
    
    print()

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
    
    # 4. 模拟数据生成
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

def main():
    """主函数"""
    print("Python random模块学习演示")
    print("=" * 60)
    
    basic_random_demo()
    random_choice_demo()
    sequence_operations_demo()
    probability_distributions_demo()
    random_seed_demo()
    secure_random_demo()
    practical_applications()
    statistics_demo()
    
    print("=" * 50)
    print("学习要点总结:")
    print("=" * 50)
    print("1. random模块提供多种随机数生成方法")
    print("2. choice()和sample()用于随机选择和抽样")
    print("3. shuffle()可以随机打乱序列")
    print("4. 支持多种概率分布（正态、指数、均匀等）")
    print("5. 使用seed()设置随机种子保证结果可重现")
    print("6. secrets模块提供加密安全的随机数")
    print("7. 实际应用包括游戏、抽奖、数据生成等")
    print("8. 大样本统计可以验证随机数的分布特性")

if __name__ == "__main__":
    main()