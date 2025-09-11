#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数学运算模块学习

本模块演示Python标准库中数学运算相关的模块：
- math: 基本数学函数
- statistics: 统计函数
- decimal: 精确十进制运算
- fractions: 分数运算
- cmath: 复数数学函数
- random: 随机数和概率分布

学习目标：
1. 掌握基本数学函数的使用
2. 理解统计计算的方法
3. 学会处理精确数值计算
4. 了解复数运算
5. 掌握概率分布的应用
"""

import math
import statistics
import decimal
import fractions
import cmath
import random
from decimal import Decimal, getcontext
from fractions import Fraction


def math_functions_demo():
    """演示math模块的基本数学函数"""
    print("=" * 50)
    print("Math模块基本函数演示")
    print("=" * 50)
    
    # 基本数学常数
    print("1. 数学常数:")
    print(f"  π (pi): {math.pi}")
    print(f"  e (自然对数底): {math.e}")
    print(f"  τ (tau): {math.tau}")
    print(f"  无穷大: {math.inf}")
    print(f"  NaN: {math.nan}")
    
    # 幂运算和对数
    print("\n2. 幂运算和对数:")
    x = 16
    print(f"  {x}的平方根: {math.sqrt(x)}")
    print(f"  {x}的立方根: {math.pow(x, 1/3)}")
    print(f"  2的{x}次方: {math.pow(2, x)}")
    print(f"  e的{x}次方: {math.exp(x)}")
    print(f"  {x}的自然对数: {math.log(x)}")
    print(f"  {x}的常用对数: {math.log10(x)}")
    print(f"  {x}的二进制对数: {math.log2(x)}")
    
    # 三角函数
    print("\n3. 三角函数:")
    angle = math.pi / 4  # 45度
    print(f"  角度: {angle} 弧度 ({math.degrees(angle)}度)")
    print(f"  sin({angle}): {math.sin(angle)}")
    print(f"  cos({angle}): {math.cos(angle)}")
    print(f"  tan({angle}): {math.tan(angle)}")
    print(f"  arcsin(0.5): {math.asin(0.5)} 弧度")
    print(f"  arccos(0.5): {math.acos(0.5)} 弧度")
    print(f"  arctan(1): {math.atan(1)} 弧度")
    
    # 双曲函数
    print("\n4. 双曲函数:")
    x = 1
    print(f"  sinh({x}): {math.sinh(x)}")
    print(f"  cosh({x}): {math.cosh(x)}")
    print(f"  tanh({x}): {math.tanh(x)}")
    
    # 取整函数
    print("\n5. 取整函数:")
    numbers = [3.2, 3.7, -3.2, -3.7]
    for num in numbers:
        print(f"  {num}: ceil={math.ceil(num)}, floor={math.floor(num)}, trunc={math.trunc(num)}")
    
    # 其他有用函数
    print("\n6. 其他函数:")
    print(f"  绝对值 abs(-5): {math.fabs(-5)}")
    print(f"  阶乘 5!: {math.factorial(5)}")
    print(f"  最大公约数 gcd(48, 18): {math.gcd(48, 18)}")
    print(f"  最小公倍数 lcm(12, 8): {math.lcm(12, 8)}")
    print(f"  组合数 C(10, 3): {math.comb(10, 3)}")
    print(f"  排列数 P(10, 3): {math.perm(10, 3)}")


def statistics_demo():
    """演示statistics模块的统计函数"""
    print("\n" + "=" * 50)
    print("Statistics模块统计函数演示")
    print("=" * 50)
    
    # 示例数据
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    scores = [85, 92, 78, 96, 88, 76, 89, 94, 82, 90]
    
    print("1. 基本统计量:")
    print(f"  数据: {data}")
    print(f"  平均数: {statistics.mean(data)}")
    print(f"  中位数: {statistics.median(data)}")
    print(f"  众数: {statistics.mode([1, 2, 2, 3, 3, 3, 4])}")
    
    print("\n2. 分散程度:")
    print(f"  成绩: {scores}")
    print(f"  总体方差: {statistics.pvariance(scores)}")
    print(f"  样本方差: {statistics.variance(scores)}")
    print(f"  总体标准差: {statistics.pstdev(scores)}")
    print(f"  样本标准差: {statistics.stdev(scores)}")
    
    print("\n3. 分位数:")
    print(f"  第一四分位数 (Q1): {statistics.quantiles(scores, n=4)[0]}")
    print(f"  第二四分位数 (Q2): {statistics.quantiles(scores, n=4)[1]}")
    print(f"  第三四分位数 (Q3): {statistics.quantiles(scores, n=4)[2]}")
    
    print("\n4. 其他统计函数:")
    print(f"  几何平均数: {statistics.geometric_mean([2, 8, 32])}")
    print(f"  调和平均数: {statistics.harmonic_mean([2, 4, 8])}")
    print(f"  多重众数: {statistics.multimode([1, 1, 2, 2, 3, 4])}")


def decimal_precision_demo():
    """演示decimal模块的精确十进制运算"""
    print("\n" + "=" * 50)
    print("Decimal模块精确十进制运算演示")
    print("=" * 50)
    
    # 浮点数精度问题
    print("1. 浮点数精度问题:")
    print(f"  0.1 + 0.2 = {0.1 + 0.2}")
    print(f"  0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")
    
    # 使用Decimal解决精度问题
    print("\n2. Decimal精确计算:")
    d1 = Decimal('0.1')
    d2 = Decimal('0.2')
    d3 = Decimal('0.3')
    print(f"  Decimal('0.1') + Decimal('0.2') = {d1 + d2}")
    print(f"  结果等于0.3: {d1 + d2 == d3}")
    
    # 设置精度
    print("\n3. 精度控制:")
    getcontext().prec = 10  # 设置10位精度
    result = Decimal(1) / Decimal(3)
    print(f"  1/3 (10位精度): {result}")
    
    getcontext().prec = 20  # 设置20位精度
    result = Decimal(1) / Decimal(3)
    print(f"  1/3 (20位精度): {result}")
    
    # 金融计算示例
    print("\n4. 金融计算示例:")
    price = Decimal('19.99')
    tax_rate = Decimal('0.08')
    quantity = 3
    
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    print(f"  商品价格: ${price}")
    print(f"  数量: {quantity}")
    print(f"  小计: ${subtotal}")
    print(f"  税费 (8%): ${tax}")
    print(f"  总计: ${total}")


def fractions_demo():
    """演示fractions模块的分数运算"""
    print("\n" + "=" * 50)
    print("Fractions模块分数运算演示")
    print("=" * 50)
    
    # 创建分数
    print("1. 创建分数:")
    f1 = Fraction(1, 3)
    f2 = Fraction(2, 5)
    f3 = Fraction('0.25')
    f4 = Fraction(0.125)
    
    print(f"  Fraction(1, 3): {f1}")
    print(f"  Fraction(2, 5): {f2}")
    print(f"  Fraction('0.25'): {f3}")
    print(f"  Fraction(0.125): {f4}")
    
    # 分数运算
    print("\n2. 分数运算:")
    print(f"  {f1} + {f2} = {f1 + f2}")
    print(f"  {f1} - {f2} = {f1 - f2}")
    print(f"  {f1} * {f2} = {f1 * f2}")
    print(f"  {f1} / {f2} = {f1 / f2}")
    
    # 分数属性
    print("\n3. 分数属性:")
    f = Fraction(6, 8)
    print(f"  原分数: {f}")
    print(f"  分子: {f.numerator}")
    print(f"  分母: {f.denominator}")
    print(f"  浮点值: {float(f)}")
    
    # 实际应用：比例计算
    print("\n4. 实际应用 - 配方比例:")
    flour = Fraction(2, 3)  # 2/3杯面粉
    sugar = Fraction(1, 4)  # 1/4杯糖
    butter = Fraction(1, 8)  # 1/8杯黄油
    
    # 制作3倍分量
    multiplier = 3
    print(f"  原配方 - 面粉: {flour}杯, 糖: {sugar}杯, 黄油: {butter}杯")
    print(f"  3倍分量 - 面粉: {flour * multiplier}杯, 糖: {sugar * multiplier}杯, 黄油: {butter * multiplier}杯")


def complex_math_demo():
    """演示cmath模块的复数数学函数"""
    print("\n" + "=" * 50)
    print("Cmath模块复数数学函数演示")
    print("=" * 50)
    
    # 创建复数
    print("1. 复数创建和表示:")
    z1 = 3 + 4j
    z2 = complex(1, 2)
    z3 = cmath.rect(5, cmath.pi/4)  # 极坐标形式
    
    print(f"  z1 = {z1}")
    print(f"  z2 = {z2}")
    print(f"  z3 = {z3} (极坐标 r=5, θ=π/4)")
    
    # 复数属性
    print("\n2. 复数属性:")
    z = 3 + 4j
    print(f"  复数: {z}")
    print(f"  实部: {z.real}")
    print(f"  虚部: {z.imag}")
    print(f"  共轭: {z.conjugate()}")
    print(f"  模长: {abs(z)}")
    print(f"  幅角: {cmath.phase(z)} 弧度")
    
    # 复数运算
    print("\n3. 复数数学函数:")
    z = 1 + 1j
    print(f"  z = {z}")
    print(f"  sqrt(z): {cmath.sqrt(z)}")
    print(f"  exp(z): {cmath.exp(z)}")
    print(f"  log(z): {cmath.log(z)}")
    print(f"  sin(z): {cmath.sin(z)}")
    print(f"  cos(z): {cmath.cos(z)}")
    
    # 极坐标转换
    print("\n4. 极坐标转换:")
    z = 3 + 4j
    r, theta = cmath.polar(z)
    print(f"  直角坐标: {z}")
    print(f"  极坐标: r={r}, θ={theta} 弧度")
    print(f"  转换回直角坐标: {cmath.rect(r, theta)}")


def probability_distributions_demo():
    """演示概率分布的应用"""
    print("\n" + "=" * 50)
    print("概率分布应用演示")
    print("=" * 50)
    
    # 设置随机种子
    random.seed(42)
    
    # 均匀分布
    print("1. 均匀分布:")
    uniform_samples = [random.uniform(0, 10) for _ in range(5)]
    print(f"  0-10均匀分布样本: {[round(x, 2) for x in uniform_samples]}")
    
    # 正态分布
    print("\n2. 正态分布:")
    normal_samples = [random.gauss(100, 15) for _ in range(5)]
    print(f"  正态分布(μ=100, σ=15)样本: {[round(x, 2) for x in normal_samples]}")
    
    # 指数分布
    print("\n3. 指数分布:")
    exp_samples = [random.expovariate(0.5) for _ in range(5)]
    print(f"  指数分布(λ=0.5)样本: {[round(x, 2) for x in exp_samples]}")
    
    # 伽马分布
    print("\n4. 伽马分布:")
    gamma_samples = [random.gammavariate(2, 3) for _ in range(5)]
    print(f"  伽马分布(α=2, β=3)样本: {[round(x, 2) for x in gamma_samples]}")
    
    # 贝塔分布
    print("\n5. 贝塔分布:")
    beta_samples = [random.betavariate(2, 5) for _ in range(5)]
    print(f"  贝塔分布(α=2, β=5)样本: {[round(x, 3) for x in beta_samples]}")


def practical_applications():
    """数学运算的实际应用示例"""
    print("\n" + "=" * 50)
    print("实际应用示例")
    print("=" * 50)
    
    # 1. 贷款计算器
    print("1. 贷款计算器:")
    principal = Decimal('100000')  # 本金
    annual_rate = Decimal('0.05')  # 年利率5%
    years = 30  # 30年
    
    monthly_rate = annual_rate / 12
    num_payments = years * 12
    
    # 月供计算公式
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                     ((1 + monthly_rate) ** num_payments - 1)
    
    print(f"  贷款本金: ${principal}")
    print(f"  年利率: {annual_rate * 100}%")
    print(f"  贷款期限: {years}年")
    print(f"  月供: ${monthly_payment.quantize(Decimal('0.01'))}")
    
    # 2. 统计分析
    print("\n2. 学生成绩统计分析:")
    grades = [85, 92, 78, 96, 88, 76, 89, 94, 82, 90, 87, 93, 79, 91, 86]
    
    mean_grade = statistics.mean(grades)
    median_grade = statistics.median(grades)
    std_dev = statistics.stdev(grades)
    
    print(f"  成绩列表: {grades}")
    print(f"  平均分: {mean_grade:.2f}")
    print(f"  中位数: {median_grade}")
    print(f"  标准差: {std_dev:.2f}")
    
    # 计算等级分布
    grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades:
        if grade >= 90:
            grade_counts['A'] += 1
        elif grade >= 80:
            grade_counts['B'] += 1
        elif grade >= 70:
            grade_counts['C'] += 1
        elif grade >= 60:
            grade_counts['D'] += 1
        else:
            grade_counts['F'] += 1
    
    print(f"  等级分布: {grade_counts}")
    
    # 3. 几何计算
    print("\n3. 几何计算 - 圆形面积和周长:")
    radius = 5.5
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    
    print(f"  半径: {radius}")
    print(f"  面积: {area:.2f}")
    print(f"  周长: {circumference:.2f}")
    
    # 4. 三角测量
    print("\n4. 三角测量 - 计算建筑物高度:")
    distance = 50  # 距离建筑物50米
    angle = math.radians(30)  # 仰角30度
    
    height = distance * math.tan(angle)
    print(f"  距离建筑物: {distance}米")
    print(f"  仰角: 30度")
    print(f"  建筑物高度: {height:.2f}米")


def performance_comparison():
    """性能比较示例"""
    print("\n" + "=" * 50)
    print("性能比较")
    print("=" * 50)
    
    import time
    
    # 比较不同计算方法的性能
    n = 1000000
    
    # 使用内置函数
    start_time = time.time()
    result1 = sum(i ** 2 for i in range(n))
    time1 = time.time() - start_time
    
    # 使用math.pow
    start_time = time.time()
    result2 = sum(math.pow(i, 2) for i in range(n))
    time2 = time.time() - start_time
    
    # 使用operator.pow
    import operator
    start_time = time.time()
    result3 = sum(operator.pow(i, 2) for i in range(n))
    time3 = time.time() - start_time
    
    print(f"计算 0 到 {n-1} 的平方和:")
    print(f"  内置 ** 运算符: {time1:.4f}秒")
    print(f"  math.pow函数: {time2:.4f}秒")
    print(f"  operator.pow函数: {time3:.4f}秒")
    print(f"  结果一致性: {result1 == int(result2) == int(result3)}")


def main():
    """主函数"""
    print("Python标准库 - 数学运算模块学习")
    print("=" * 60)
    
    # 演示各个模块
    math_functions_demo()
    statistics_demo()
    decimal_precision_demo()
    fractions_demo()
    complex_math_demo()
    probability_distributions_demo()
    practical_applications()
    performance_comparison()
    
    print("\n" + "=" * 50)
    print("学习要点总结")
    print("=" * 50)
    print("1. math模块提供基本数学函数和常数")
    print("2. statistics模块提供统计计算功能")
    print("3. decimal模块解决浮点数精度问题")
    print("4. fractions模块提供精确分数运算")
    print("5. cmath模块处理复数数学运算")
    print("6. random模块支持多种概率分布")
    print("7. 选择合适的数值类型很重要")
    print("8. 金融计算建议使用Decimal")
    print("9. 科学计算可以使用复数")
    print("10. 统计分析使用statistics模块")
    print("11. 性能敏感场景要考虑函数选择")
    print("12. 数学运算在数据分析、科学计算、工程应用中广泛使用")


if __name__ == "__main__":
    main()