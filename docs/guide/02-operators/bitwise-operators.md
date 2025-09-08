# 位运算符

## 学习目标

通过本节学习，你将掌握：
- 二进制数的表示方法
- 所有位运算符的使用
- 位运算的实际应用场景
- 位运算的性能优势

## 位运算符概览

Python中的位运算符直接操作数字的二进制位：

| 运算符 | 名称 | 描述 | 示例 |
|--------|------|------|------|
| & | 按位与 | 两个位都为1时结果为1 | 12 & 10 = 8 |
| \| | 按位或 | 两个位中有一个为1时结果为1 | 12 \| 10 = 14 |
| ^ | 按位异或 | 两个位不同时结果为1 | 12 ^ 10 = 6 |
| ~ | 按位取反 | 0变1，1变0 | ~12 = -13 |
| << | 左移 | 向左移动指定位数 | 12 << 2 = 48 |
| >> | 右移 | 向右移动指定位数 | 12 >> 2 = 3 |

## 二进制基础

### 进制转换

```python
# 十进制到二进制
numbers = [5, 10, 15, 255]
print("十进制到二进制的转换：")
for num in numbers:
    binary = bin(num)
    print(f"{num:3d} = {binary} = {binary[2:].zfill(8)}")

# 输出：
#   5 = 0b101 = 00000101
#  10 = 0b1010 = 00001010
#  15 = 0b1111 = 00001111
# 255 = 0b11111111 = 11111111

# 二进制到十进制
binary_nums = ['1010', '1111', '10000', '11111111']
print("\n二进制到十进制的转换：")
for binary in binary_nums:
    decimal = int(binary, 2)
    print(f"{binary} = {decimal}")

# 输出：
# 1010 = 10
# 1111 = 15
# 10000 = 16
# 11111111 = 255
```

## 按位与运算符 (&)

### 基本用法

```python
a = 12  # 1100
b = 10  # 1010
result = a & b  # 1000 = 8

print(f"a = {a:2d} = {bin(a)[2:].zfill(4)}")
print(f"b = {b:2d} = {bin(b)[2:].zfill(4)}")
print(f"a & b = {result:2d} = {bin(result)[2:].zfill(4)}")
```

### 实际应用：检查奇偶性

```python
# 检查数字是否为奇数
def is_odd(num):
    return num & 1  # 与1进行按位与

test_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for num in test_numbers:
    result = is_odd(num)
    print(f"{num} & 1 = {result} ({'奇数' if result else '偶数'})")
```

## 按位或运算符 (|)

### 基本用法

```python
a = 12  # 1100
b = 10  # 1010
result = a | b  # 1110 = 14

print(f"a = {a:2d} = {bin(a)[2:].zfill(4)}")
print(f"b = {b:2d} = {bin(b)[2:].zfill(4)}")
print(f"a | b = {result:2d} = {bin(result)[2:].zfill(4)}")
```

### 实际应用：权限系统

```python
# 定义权限常量
READ = 1    # 001
WRITE = 2   # 010
EXECUTE = 4 # 100

# 设置权限
user_permission = READ | WRITE  # 011 = 3
admin_permission = READ | WRITE | EXECUTE  # 111 = 7

print(f"READ权限:    {READ} = {bin(read)[2:].zfill(3)}")
print(f"WRITE权限:   {WRITE} = {bin(WRITE)[2:].zfill(3)}")
print(f"EXECUTE权限: {EXECUTE} = {bin(EXECUTE)[2:].zfill(3)}")
print(f"用户权限:    {user_permission} = {bin(user_permission)[2:].zfill(3)}")
print(f"管理员权限:  {admin_permission} = {bin(admin_permission)[2:].zfill(3)}")
```

## 按位异或运算符 (^)

### 基本用法

```python
a = 12  # 1100
b = 10  # 1010
result = a ^ b  # 0110 = 6

print(f"a = {a:2d} = {bin(a)[2:].zfill(4)}")
print(f"b = {b:2d} = {bin(b)[2:].zfill(4)}")
print(f"a ^ b = {result:2d} = {bin(result)[2:].zfill(4)}")
```

### 异或的特殊性质

```python
x = 25
print(f"x = {x}")
print(f"x ^ x = {x ^ x}")  # 任何数与自己异或等于0
print(f"x ^ 0 = {x ^ 0}")  # 任何数与0异或等于自己

# 使用异或交换变量（不推荐，仅作演示）
a, b = 15, 25
print(f"交换前: a={a}, b={b}")
a = a ^ b
b = a ^ b  # b = (a^b) ^ b = a
a = a ^ b  # a = (a^b) ^ a = b
print(f"交换后: a={a}, b={b}")
```

## 按位取反运算符 (~)

```python
a = 12  # 00001100
result = ~a  # 11110011 (补码表示)

print(f"a = {a:2d} = {bin(a)[2:].zfill(8)}")
print(f"~a = {result:2d} = {bin(result & 0xFF)[2:].zfill(8)}")
print(f"注意：Python中 ~x = -(x+1)，所以 ~{a} = {result}")
```

## 左移运算符 (<<)

### 基本用法

```python
a = 5  # 00000101
print(f"原数: a = {a} = {bin(a)[2:].zfill(8)}")

for i in range(1, 4):
    result = a << i
    print(f"a << {i} = {result:2d} = {bin(result)[2:].zfill(8)} (相当于乘以 2^{i} = {2**i})")

# 输出：
# a << 1 = 10 = 00001010 (相当于乘以 2^1 = 2)
# a << 2 = 20 = 00010100 (相当于乘以 2^2 = 4)
# a << 3 = 40 = 00101000 (相当于乘以 2^3 = 8)
```

### 应用：快速计算2的幂

```python
print("2的幂次方：")
for i in range(8):
    power_of_2 = 1 << i
    print(f"2^{i} = 1 << {i} = {power_of_2}")

# 输出：
# 2^0 = 1 << 0 = 1
# 2^1 = 1 << 1 = 2
# 2^2 = 1 << 2 = 4
# ...
```

## 右移运算符 (>>)

```python
a = 40  # 00101000
print(f"原数: a = {a} = {bin(a)[2:].zfill(8)}")

for i in range(1, 4):
    result = a >> i
    print(f"a >> {i} = {result:2d} = {bin(result)[2:].zfill(8)} (相当于除以 2^{i} = {2**i})")

# 输出：
# a >> 1 = 20 = 00010100 (相当于除以 2^1 = 2)
# a >> 2 = 10 = 00001010 (相当于除以 2^2 = 4)
# a >> 3 =  5 = 00000101 (相当于除以 2^3 = 8)
```

## 实际应用示例

### 1. 权限检查系统

```python
class Permission:
    READ = 1     # 0001
    WRITE = 2    # 0010
    EXECUTE = 4  # 0100
    DELETE = 8   # 1000
    
    @staticmethod
    def has_permission(user_perms, required_perm):
        return (user_perms & required_perm) == required_perm
    
    @staticmethod
    def add_permission(user_perms, new_perm):
        return user_perms | new_perm
    
    @staticmethod
    def remove_permission(user_perms, remove_perm):
        return user_perms & (~remove_perm)

# 使用示例
user_perms = Permission.READ | Permission.WRITE  # 用户有读写权限
print(f"用户权限: {user_perms} = {bin(user_perms)[2:].zfill(4)}")

print(f"有读权限: {Permission.has_permission(user_perms, Permission.READ)}")
print(f"有执行权限: {Permission.has_permission(user_perms, Permission.EXECUTE)}")

# 添加执行权限
user_perms = Permission.add_permission(user_perms, Permission.EXECUTE)
print(f"添加执行权限后: {user_perms} = {bin(user_perms)[2:].zfill(4)}")
```

### 2. 状态标志管理

```python
class StatusFlags:
    ONLINE = 1      # 0001
    BUSY = 2        # 0010
    AWAY = 4        # 0100
    INVISIBLE = 8   # 1000

# 设置用户状态
user_status = StatusFlags.ONLINE | StatusFlags.BUSY
print(f"用户状态: {user_status} = {bin(user_status)[2:].zfill(4)}")

# 检查状态
is_online = bool(user_status & StatusFlags.ONLINE)
is_busy = bool(user_status & StatusFlags.BUSY)
print(f"在线且忙碌: {is_online and is_busy}")
```

### 3. 颜色RGB值处理

```python
# RGB颜色值处理
color = 0xFF5733  # 红色=FF, 绿色=57, 蓝色=33

# 提取各颜色分量
red = (color >> 16) & 0xFF
green = (color >> 8) & 0xFF
blue = color & 0xFF

print(f"颜色值: 0x{color:06X}")
print(f"红色分量: {red} (0x{red:02X})")
print(f"绿色分量: {green} (0x{green:02X})")
print(f"蓝色分量: {blue} (0x{blue:02X})")

# 重新组合颜色
new_color = (red << 16) | (green << 8) | blue
print(f"重新组合: 0x{new_color:06X}")
```

### 4. 位图数据结构

```python
class BitMap:
    def __init__(self, size=32):
        self.size = size
        self.bits = 0
    
    def set_bit(self, position):
        """设置指定位为1"""
        if 0 <= position < self.size:
            self.bits |= (1 << position)
    
    def clear_bit(self, position):
        """设置指定位为0"""
        if 0 <= position < self.size:
            self.bits &= ~(1 << position)
    
    def get_bit(self, position):
        """获取指定位的值"""
        if 0 <= position < self.size:
            return (self.bits >> position) & 1
        return 0
    
    def toggle_bit(self, position):
        """切换指定位的值"""
        if 0 <= position < self.size:
            self.bits ^= (1 << position)
    
    def __str__(self):
        return bin(self.bits)[2:].zfill(self.size)

# 使用示例
bitmap = BitMap(8)
bitmap.set_bit(0)
bitmap.set_bit(3)
bitmap.set_bit(7)
print(f"设置位0,3,7后: {bitmap}")  # 10001001
print(f"位3的值: {bitmap.get_bit(3)}")  # 1
bitmap.clear_bit(3)
print(f"清除位3后: {bitmap}")  # 10000001
```

## 性能优势

### 位运算 vs 普通运算

```python
import time

# 比较乘法和左移
def multiply_by_8(n):
    return n * 8

def shift_by_3(n):
    return n << 3  # 左移3位相当于乘以8

# 性能测试
test_num = 12345
iterations = 100000

# 测试乘法
start = time.time()
for _ in range(iterations):
    result1 = multiply_by_8(test_num)
time1 = time.time() - start

# 测试位移
start = time.time()
for _ in range(iterations):
    result2 = shift_by_3(test_num)
time2 = time.time() - start

print(f"乘法运算 ({test_num} * 8): {result1}")
print(f"位移运算 ({test_num} << 3): {result2}")
print(f"结果相同: {result1 == result2}")
print(f"位移通常比乘法更快")
```

## 练习题

### 基础练习

1. 计算以下位运算的结果：
```python
print(f"13 & 7 = {13 & 7}")   # ?
print(f"13 | 7 = {13 | 7}")   # ?
print(f"13 ^ 7 = {13 ^ 7}")   # ?
print(f"~13 = {~13}")         # ?
print(f"13 << 2 = {13 << 2}") # ?
print(f"13 >> 1 = {13 >> 1}") # ?
```

### 编程练习

1. **数字属性检查器**：编写函数检查数字的位属性
```python
def check_bit_properties(num):
    properties = []
    
    # 检查是否为2的幂
    if num > 0 and (num & (num - 1)) == 0:
        properties.append("2的幂")
    
    # 检查奇偶性
    if num & 1:
        properties.append("奇数")
    else:
        properties.append("偶数")
    
    # 计算二进制中1的个数
    count = bin(num).count('1')
    properties.append(f"包含{count}个1")
    
    return properties

# 测试
test_nums = [8, 15, 16, 31]
for num in test_nums:
    props = check_bit_properties(num)
    print(f"{num} ({bin(num)[2:].zfill(8)}): {', '.join(props)}")
```

2. **简单异或加密**：实现基于异或的加密解密
```python
def xor_encrypt_decrypt(text, key):
    result = ""
    for char in text:
        encrypted_char = chr(ord(char) ^ key)
        result += encrypted_char
    return result

# 使用示例
original = "Hello World"
key = 123
encrypted = xor_encrypt_decrypt(original, key)
decrypted = xor_encrypt_decrypt(encrypted, key)

print(f"原文: '{original}'")
print(f"密钥: {key}")
print(f"加密: '{encrypted}'")
print(f"解密: '{decrypted}'")
print(f"解密成功: {original == decrypted}")
```

## 常见错误和注意事项

### 1. 负数的位运算

```python
# Python中负数使用补码表示
num = -5
print(f"{num} 的二进制: {bin(num)}")
print(f"~{num} = {~num}")

# 注意：~x = -(x+1)
print(f"~5 = {~5}")  # -6
print(f"~(-5) = {~(-5)}")  # 4
```

### 2. 位移操作的边界

```python
# 左移可能导致数值变得很大
num = 1
for i in range(5):
    result = num << (i * 10)
    print(f"1 << {i * 10} = {result}")

# 右移负数的行为
print(f"-8 >> 1 = {-8 >> 1}")  # -4 (算术右移)
```

### 3. 位运算符优先级

```python
# 位运算符的优先级低于算术运算符
result1 = 2 + 3 << 1  # 等价于 (2 + 3) << 1 = 10
result2 = 2 + (3 << 1)  # 等价于 2 + 6 = 8

print(f"2 + 3 << 1 = {result1}")
print(f"2 + (3 << 1) = {result2}")
```

## 学习要点总结

1. **基本概念**：位运算直接操作二进制位，效率高
2. **运算符掌握**：&、|、^、~、<<、>> 六种运算符的用法
3. **实际应用**：权限控制、状态管理、颜色处理、性能优化
4. **特殊性质**：
   - 左移相当于乘以2的幂
   - 右移相当于除以2的幂
   - 异或有自反性：x ^ x = 0, x ^ 0 = x
   - 按位与可用于掩码操作
5. **性能优势**：位运算通常比对应的算术运算更快
6. **注意事项**：负数的补码表示、运算符优先级、边界情况

位运算是计算机科学的基础，掌握它们有助于理解计算机底层原理，并能在特定场景下显著提升程序性能。