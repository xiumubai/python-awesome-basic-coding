# 数学运算模块学习

## 学习目标

通过本节学习，你将掌握：

1. **math模块**：基本数学函数和常数的使用
2. **statistics模块**：统计计算和数据分析
3. **decimal模块**：精确十进制运算，解决浮点数精度问题
4. **fractions模块**：分数运算和精确比例计算
5. **cmath模块**：复数数学函数
6. **概率分布**：随机数生成和概率分布应用
7. **实际应用**：金融计算、统计分析、几何计算等

## 核心概念

### 数学运算模块分类

- **基础数学**：math模块提供基本数学函数
- **统计计算**：statistics模块提供统计分析功能
- **精确计算**：decimal和fractions模块解决精度问题
- **复数运算**：cmath模块处理复数数学
- **概率分布**：random模块支持多种分布

### 数值类型选择

- **float**：一般数值计算，速度快但有精度限制
- **Decimal**：金融计算，精确但速度较慢
- **Fraction**：分数运算，保持精确比例
- **complex**：复数运算，科学计算应用

## 代码示例

### 1. Math模块基本函数

```python
import math

# 数学常数
print(f"π (pi): {math.pi}")
print(f"e (自然对数底): {math.e}")
print(f"τ (tau): {math.tau}")

# 幂运算和对数
x = 16
print(f"{x}的平方根: {math.sqrt(x)}")
print(f"{x}的立方根: {math.pow(x, 1/3)}")
print(f"{x}的自然对数: {math.log(x)}")
print(f"{x}的常用对数: {math.log10(x)}")

# 三角函数
angle = math.pi / 4  # 45度
print(f"sin({angle}): {math.sin(angle)}")
print(f"cos({angle}): {math.cos(angle)}")
print(f"tan({angle}): {math.tan(angle)}")

# 取整函数
numbers = [3.2, 3.7, -3.2, -3.7]
for num in numbers:
    print(f"{num}: ceil={math.ceil(num)}, floor={math.floor(num)}, trunc={math.trunc(num)}")

# 其他有用函数
print(f"阶乘 5!: {math.factorial(5)}")
print(f"最大公约数 gcd(48, 18): {math.gcd(48, 18)}")
print(f"组合数 C(10, 3): {math.comb(10, 3)}")
```

### 2. Statistics模块统计计算

```python
import statistics

# 示例数据
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
scores = [85, 92, 78, 96, 88, 76, 89, 94, 82, 90]

# 基本统计量
print(f"平均数: {statistics.mean(data)}")
print(f"中位数: {statistics.median(data)}")
print(f"众数: {statistics.mode([1, 2, 2, 3, 3, 3, 4])}")

# 分散程度
print(f"总体方差: {statistics.pvariance(scores)}")
print(f"样本方差: {statistics.variance(scores)}")
print(f"总体标准差: {statistics.pstdev(scores)}")
print(f"样本标准差: {statistics.stdev(scores)}")

# 分位数
quartiles = statistics.quantiles(scores, n=4)
print(f"第一四分位数 (Q1): {quartiles[0]}")
print(f"第二四分位数 (Q2): {quartiles[1]}")
print(f"第三四分位数 (Q3): {quartiles[2]}")

# 其他统计函数
print(f"几何平均数: {statistics.geometric_mean([2, 8, 32])}")
print(f"调和平均数: {statistics.harmonic_mean([2, 4, 8])}")
```

### 3. Decimal精确十进制运算

```python
from decimal import Decimal, getcontext

# 浮点数精度问题
print(f"0.1 + 0.2 = {0.1 + 0.2}")
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")

# 使用Decimal解决精度问题
d1 = Decimal('0.1')
d2 = Decimal('0.2')
d3 = Decimal('0.3')
print(f"Decimal('0.1') + Decimal('0.2') = {d1 + d2}")
print(f"结果等于0.3: {d1 + d2 == d3}")

# 设置精度
getcontext().prec = 20  # 设置20位精度
result = Decimal(1) / Decimal(3)
print(f"1/3 (20位精度): {result}")

# 金融计算示例
price = Decimal('19.99')
tax_rate = Decimal('0.08')
quantity = 3

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"商品价格: ${price}")
print(f"小计: ${subtotal}")
print(f"税费 (8%): ${tax}")
print(f"总计: ${total}")
```

### 4. Fractions分数运算

```python
from fractions import Fraction

# 创建分数
f1 = Fraction(1, 3)
f2 = Fraction(2, 5)
f3 = Fraction('0.25')
f4 = Fraction(0.125)

print(f"Fraction(1, 3): {f1}")
print(f"Fraction('0.25'): {f3}")

# 分数运算
print(f"{f1} + {f2} = {f1 + f2}")
print(f"{f1} * {f2} = {f1 * f2}")

# 分数属性
f = Fraction(6, 8)
print(f"原分数: {f}")
print(f"分子: {f.numerator}")
print(f"分母: {f.denominator}")

# 实际应用：配方比例
flour = Fraction(2, 3)  # 2/3杯面粉
sugar = Fraction(1, 4)  # 1/4杯糖
multiplier = 3

print(f"原配方 - 面粉: {flour}杯, 糖: {sugar}杯")
print(f"3倍分量 - 面粉: {flour * multiplier}杯, 糖: {sugar * multiplier}杯")
```

### 5. Cmath复数数学函数

```python
import cmath

# 创建复数
z1 = 3 + 4j
z2 = complex(1, 2)
z3 = cmath.rect(5, cmath.pi/4)  # 极坐标形式

print(f"z1 = {z1}")
print(f"z3 = {z3} (极坐标 r=5, θ=π/4)")

# 复数属性
z = 3 + 4j
print(f"实部: {z.real}")
print(f"虚部: {z.imag}")
print(f"共轭: {z.conjugate()}")
print(f"模长: {abs(z)}")
print(f"幅角: {cmath.phase(z)} 弧度")

# 复数数学函数
z = 1 + 1j
print(f"sqrt(z): {cmath.sqrt(z)}")
print(f"exp(z): {cmath.exp(z)}")
print(f"log(z): {cmath.log(z)}")

# 极坐标转换
z = 3 + 4j
r, theta = cmath.polar(z)
print(f"直角坐标: {z}")
print(f"极坐标: r={r}, θ={theta} 弧度")
print(f"转换回直角坐标: {cmath.rect(r, theta)}")
```

### 6. 概率分布应用

```python
import random

# 设置随机种子
random.seed(42)

# 均匀分布
uniform_samples = [random.uniform(0, 10) for _ in range(5)]
print(f"0-10均匀分布样本: {[round(x, 2) for x in uniform_samples]}")

# 正态分布
normal_samples = [random.gauss(100, 15) for _ in range(5)]
print(f"正态分布(μ=100, σ=15)样本: {[round(x, 2) for x in normal_samples]}")

# 指数分布
exp_samples = [random.expovariate(0.5) for _ in range(5)]
print(f"指数分布(λ=0.5)样本: {[round(x, 2) for x in exp_samples]}")

# 伽马分布
gamma_samples = [random.gammavariate(2, 3) for _ in range(5)]
print(f"伽马分布(α=2, β=3)样本: {[round(x, 2) for x in gamma_samples]}")

# 贝塔分布
beta_samples = [random.betavariate(2, 5) for _ in range(5)]
print(f"贝塔分布(α=2, β=5)样本: {[round(x, 3) for x in beta_samples]}")
```

### 7. 实际应用示例

```python
# 贷款计算器
from decimal import Decimal

principal = Decimal('100000')  # 本金
annual_rate = Decimal('0.05')  # 年利率5%
years = 30  # 30年

monthly_rate = annual_rate / 12
num_payments = years * 12

# 月供计算公式
monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                 ((1 + monthly_rate) ** num_payments - 1)

print(f"贷款本金: ${principal}")
print(f"年利率: {annual_rate * 100}%")
print(f"月供: ${monthly_payment.quantize(Decimal('0.01'))}")

# 学生成绩统计分析
import statistics

grades = [85, 92, 78, 96, 88, 76, 89, 94, 82, 90, 87, 93, 79, 91, 86]

mean_grade = statistics.mean(grades)
median_grade = statistics.median(grades)
std_dev = statistics.stdev(grades)

print(f"平均分: {mean_grade:.2f}")
print(f"中位数: {median_grade}")
print(f"标准差: {std_dev:.2f}")

# 几何计算
import math

radius = 5.5
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"半径: {radius}")
print(f"面积: {area:.2f}")
print(f"周长: {circumference:.2f}")

# 三角测量
distance = 50  # 距离建筑物50米
angle = math.radians(30)  # 仰角30度

height = distance * math.tan(angle)
print(f"建筑物高度: {height:.2f}米")
```

## 重要知识点

### 1. 模块功能对比

| 模块 | 主要功能 | 适用场景 |
|------|----------|----------|
| math | 基本数学函数 | 一般数值计算 |
| statistics | 统计计算 | 数据分析 |
| decimal | 精确十进制 | 金融计算 |
| fractions | 分数运算 | 精确比例 |
| cmath | 复数数学 | 科学计算 |
| random | 概率分布 | 随机模拟 |

### 2. 精度问题

- **浮点数限制**：0.1 + 0.2 ≠ 0.3
- **Decimal解决方案**：精确十进制运算
- **Fraction优势**：保持精确分数形式
- **应用建议**：金融计算使用Decimal

### 3. 性能考虑

- **内置运算符**：** 比 math.pow() 更快
- **函数选择**：根据精度和性能需求选择
- **批量计算**：考虑使用NumPy等专业库

### 4. 统计分析要点

- **总体vs样本**：pvariance vs variance
- **分位数计算**：quantiles函数的使用
- **多重众数**：multimode处理多个众数

## 运行方式

```bash
# 运行完整示例
python3 08_math_statistics.py

# 或者在Python解释器中逐步测试
python3
>>> import math
>>> math.sqrt(16)
4.0
```

## 练习建议

### 基础练习

1. **数学函数练习**：
   - 计算三角形的面积和周长
   - 实现简单的科学计算器
   - 练习角度和弧度的转换

2. **统计计算练习**：
   - 分析一组数据的统计特征
   - 计算成绩的等级分布
   - 比较不同数据集的差异

3. **精确计算练习**：
   - 实现精确的货币计算
   - 处理分数的四则运算
   - 解决浮点数精度问题

### 进阶练习

1. **复数应用**：
   - 实现复数计算器
   - 解决工程中的复数问题
   - 绘制复数在复平面上的图形

2. **概率模拟**：
   - 模拟投掷硬币实验
   - 生成不同分布的随机数
   - 分析随机数的统计特性

3. **实际应用**：
   - 开发贷款计算器
   - 实现数据分析工具
   - 创建几何计算程序

## 注意事项

### 1. 精度选择

- 金融计算必须使用Decimal
- 科学计算可以使用float
- 分数运算保持Fraction形式

### 2. 性能优化

- 大量计算时考虑使用NumPy
- 避免不必要的类型转换
- 合理选择数学函数

### 3. 错误处理

- 检查除零错误
- 处理定义域问题（如负数开方）
- 验证输入数据的有效性

### 4. 最佳实践

- 根据应用场景选择合适的数值类型
- 注意浮点数的精度限制
- 使用统计函数进行数据分析
- 复数运算在信号处理中很有用

通过本节学习，你将掌握Python中各种数学运算模块的使用方法，能够处理从基础计算到复杂统计分析的各种数学问题。