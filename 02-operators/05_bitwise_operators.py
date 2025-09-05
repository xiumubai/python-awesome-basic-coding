#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
位运算符学习教程

本文件演示Python中的位运算符的使用方法和特性
包括：按位与(&)、按位或(|)、按位异或(^)、按位取反(~)、左移(<<)、右移(>>)

学习目标：
1. 理解二进制数的表示方法
2. 掌握所有位运算符的使用
3. 学会位运算的实际应用
4. 了解位运算的性能优势
"""

def main():
    print("="*50)
    print("Python 位运算符学习教程")
    print("="*50)
    
    # 1. 二进制基础
    print("\n1. 二进制基础")
    print("-" * 30)
    
    numbers = [5, 10, 15, 255]
    print("十进制到二进制的转换：")
    for num in numbers:
        binary = bin(num)
        print(f"{num:3d} = {binary} = {binary[2:].zfill(8)}")
    
    print("\n二进制到十进制的转换：")
    binary_nums = ['1010', '1111', '10000', '11111111']
    for binary in binary_nums:
        decimal = int(binary, 2)
        print(f"{binary} = {decimal}")
    
    # 2. 按位与运算符 (&)
    print("\n2. 按位与运算符 (&)")
    print("-" * 30)
    
    a = 12  # 1100
    b = 10  # 1010
    result = a & b
    
    print(f"a = {a:2d} = {bin(a)[2:].zfill(4)}")
    print(f"b = {b:2d} = {bin(b)[2:].zfill(4)}")
    print(f"a & b = {result:2d} = {bin(result)[2:].zfill(4)}")
    print("按位与：两个位都为1时结果为1，否则为0")
    
    # 按位与的应用：检查奇偶性
    print("\n按位与的应用 - 检查奇偶性：")
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    for num in test_numbers:
        is_odd = num & 1  # 与1进行按位与
        print(f"{num} & 1 = {is_odd} ({'奇数' if is_odd else '偶数'})")
    
    # 3. 按位或运算符 (|)
    print("\n3. 按位或运算符 (|)")
    print("-" * 30)
    
    a = 12  # 1100
    b = 10  # 1010
    result = a | b
    
    print(f"a = {a:2d} = {bin(a)[2:].zfill(4)}")
    print(f"b = {b:2d} = {bin(b)[2:].zfill(4)}")
    print(f"a | b = {result:2d} = {bin(result)[2:].zfill(4)}")
    print("按位或：两个位中有一个为1时结果为1")
    
    # 按位或的应用：设置标志位
    print("\n按位或的应用 - 权限系统：")
    READ = 1    # 001
    WRITE = 2   # 010
    EXECUTE = 4 # 100
    
    # 设置权限
    user_permission = READ | WRITE  # 011
    admin_permission = READ | WRITE | EXECUTE  # 111
    
    print(f"READ权限:    {READ} = {bin(READ)[2:].zfill(3)}")
    print(f"WRITE权限:   {WRITE} = {bin(WRITE)[2:].zfill(3)}")
    print(f"EXECUTE权限: {EXECUTE} = {bin(EXECUTE)[2:].zfill(3)}")
    print(f"用户权限:    {user_permission} = {bin(user_permission)[2:].zfill(3)}")
    print(f"管理员权限:  {admin_permission} = {bin(admin_permission)[2:].zfill(3)}")
    
    # 4. 按位异或运算符 (^)
    print("\n4. 按位异或运算符 (^)")
    print("-" * 30)
    
    a = 12  # 1100
    b = 10  # 1010
    result = a ^ b
    
    print(f"a = {a:2d} = {bin(a)[2:].zfill(4)}")
    print(f"b = {b:2d} = {bin(b)[2:].zfill(4)}")
    print(f"a ^ b = {result:2d} = {bin(result)[2:].zfill(4)}")
    print("按位异或：两个位不同时结果为1，相同时为0")
    
    # 异或的特殊性质
    print("\n异或的特殊性质：")
    x = 25
    print(f"x = {x}")
    print(f"x ^ x = {x ^ x} (任何数与自己异或等于0)")
    print(f"x ^ 0 = {x ^ 0} (任何数与0异或等于自己)")
    
    # 异或交换变量（不推荐，仅作演示）
    print("\n使用异或交换变量：")
    a, b = 15, 25
    print(f"交换前: a={a}, b={b}")
    a = a ^ b
    b = a ^ b  # b = (a^b) ^ b = a
    a = a ^ b  # a = (a^b) ^ a = b
    print(f"交换后: a={a}, b={b}")
    
    # 5. 按位取反运算符 (~)
    print("\n5. 按位取反运算符 (~)")
    print("-" * 30)
    
    a = 12  # 1100
    result = ~a
    
    print(f"a = {a:2d} = {bin(a)[2:].zfill(8)}")
    print(f"~a = {result:2d} = {bin(result & 0xFF)[2:].zfill(8)}")
    print("按位取反：0变1，1变0")
    print(f"注意：Python中 ~x = -(x+1)，所以 ~{a} = {result}")
    
    # 6. 左移运算符 (<<)
    print("\n6. 左移运算符 (<<)")
    print("-" * 30)
    
    a = 5  # 101
    print(f"原数: a = {a} = {bin(a)[2:].zfill(8)}")
    
    for i in range(1, 4):
        result = a << i
        print(f"a << {i} = {result:2d} = {bin(result)[2:].zfill(8)} (相当于乘以 2^{i} = {2**i})")
    
    print("\n左移的应用 - 快速计算2的幂：")
    for i in range(8):
        power_of_2 = 1 << i
        print(f"2^{i} = 1 << {i} = {power_of_2}")
    
    # 7. 右移运算符 (>>)
    print("\n7. 右移运算符 (>>)")
    print("-" * 30)
    
    a = 40  # 101000
    print(f"原数: a = {a} = {bin(a)[2:].zfill(8)}")
    
    for i in range(1, 4):
        result = a >> i
        print(f"a >> {i} = {result:2d} = {bin(result)[2:].zfill(8)} (相当于除以 2^{i} = {2**i})")
    
    # 8. 位运算的实际应用
    print("\n8. 位运算的实际应用")
    print("-" * 30)
    
    # 应用1：权限检查系统
    class Permission:
        READ = 1     # 001
        WRITE = 2    # 010
        EXECUTE = 4  # 100
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
    
    print("权限系统示例：")
    user_perms = Permission.READ | Permission.WRITE  # 用户有读写权限
    print(f"用户权限: {user_perms} = {bin(user_perms)[2:].zfill(4)}")
    
    print(f"有读权限: {Permission.has_permission(user_perms, Permission.READ)}")
    print(f"有执行权限: {Permission.has_permission(user_perms, Permission.EXECUTE)}")
    
    # 添加执行权限
    user_perms = Permission.add_permission(user_perms, Permission.EXECUTE)
    print(f"添加执行权限后: {user_perms} = {bin(user_perms)[2:].zfill(4)}")
    
    # 应用2：状态标志
    class StatusFlags:
        ONLINE = 1      # 0001
        BUSY = 2        # 0010
        AWAY = 4        # 0100
        INVISIBLE = 8   # 1000
    
    print("\n状态标志示例：")
    user_status = StatusFlags.ONLINE | StatusFlags.BUSY
    print(f"用户状态: {user_status} = {bin(user_status)[2:].zfill(4)}")
    print(f"在线且忙碌: {(user_status & StatusFlags.ONLINE) and (user_status & StatusFlags.BUSY)}")
    
    # 应用3：颜色RGB值处理
    print("\n颜色RGB值处理：")
    color = 0xFF5733  # 红色=FF, 绿色=57, 蓝色=33
    
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
    
    # 9. 位运算的性能优势
    print("\n9. 位运算的性能优势")
    print("-" * 30)
    
    import time
    
    # 比较乘法和左移
    def multiply_by_8(n):
        return n * 8
    
    def shift_by_3(n):
        return n << 3
    
    # 简单性能测试
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
    print(f"乘法耗时: {time1:.6f} 秒")
    print(f"位移耗时: {time2:.6f} 秒")
    if time2 > 0:
        print(f"位移快了约 {time1/time2:.1f} 倍")

def practice_exercises():
    """
    练习题部分
    """
    print("\n" + "="*50)
    print("练习题")
    print("="*50)
    
    print("\n请计算以下位运算的结果：")
    print("1. 13 & 7 = ?")
    print("2. 13 | 7 = ?")
    print("3. 13 ^ 7 = ?")
    print("4. ~13 = ? (8位表示)")
    print("5. 13 << 2 = ?")
    print("6. 13 >> 1 = ?")
    
    print("\n答案：")
    print(f"1. 13 & 7 = {13 & 7} ({bin(13)[2:].zfill(4)} & {bin(7)[2:].zfill(4)} = {bin(13 & 7)[2:].zfill(4)})")
    print(f"2. 13 | 7 = {13 | 7} ({bin(13)[2:].zfill(4)} | {bin(7)[2:].zfill(4)} = {bin(13 | 7)[2:].zfill(4)})")
    print(f"3. 13 ^ 7 = {13 ^ 7} ({bin(13)[2:].zfill(4)} ^ {bin(7)[2:].zfill(4)} = {bin(13 ^ 7)[2:].zfill(4)})")
    print(f"4. ~13 = {~13 & 0xFF} ({bin(13)[2:].zfill(8)} -> {bin(~13 & 0xFF)[2:].zfill(8)})")
    print(f"5. 13 << 2 = {13 << 2} ({bin(13)[2:].zfill(4)} -> {bin(13 << 2)[2:].zfill(6)})")
    print(f"6. 13 >> 1 = {13 >> 1} ({bin(13)[2:].zfill(4)} -> {bin(13 >> 1)[2:].zfill(3)})")
    
    print("\n编程练习：")
    print("1. 实现一个简单的位图类")
    print("2. 编写函数检查数字的特定位")
    print("3. 实现位运算的加密解密")
    
    # 示例解答
    print("\n示例解答：")
    
    # 1. 位图类
    class BitMap:
        def __init__(self, size=32):
            self.size = size
            self.bits = 0
        
        def set_bit(self, position):
            if 0 <= position < self.size:
                self.bits |= (1 << position)
        
        def clear_bit(self, position):
            if 0 <= position < self.size:
                self.bits &= ~(1 << position)
        
        def get_bit(self, position):
            if 0 <= position < self.size:
                return (self.bits >> position) & 1
            return 0
        
        def toggle_bit(self, position):
            if 0 <= position < self.size:
                self.bits ^= (1 << position)
        
        def __str__(self):
            return bin(self.bits)[2:].zfill(self.size)
    
    print("1. 位图类示例：")
    bitmap = BitMap(8)
    bitmap.set_bit(0)
    bitmap.set_bit(3)
    bitmap.set_bit(7)
    print(f"   设置位0,3,7后: {bitmap}")
    print(f"   位3的值: {bitmap.get_bit(3)}")
    bitmap.clear_bit(3)
    print(f"   清除位3后: {bitmap}")
    
    # 2. 检查特定位
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
    
    print("\n2. 数字位属性检查：")
    test_nums = [8, 15, 16, 31]
    for num in test_nums:
        props = check_bit_properties(num)
        print(f"   {num} ({bin(num)[2:].zfill(8)}): {', '.join(props)}")
    
    # 3. 简单的异或加密
    def xor_encrypt_decrypt(text, key):
        result = ""
        for char in text:
            encrypted_char = chr(ord(char) ^ key)
            result += encrypted_char
        return result
    
    print("\n3. 异或加密解密示例：")
    original = "Hello World"
    key = 123
    encrypted = xor_encrypt_decrypt(original, key)
    decrypted = xor_encrypt_decrypt(encrypted, key)
    
    print(f"   原文: '{original}'")
    print(f"   密钥: {key}")
    print(f"   加密: '{encrypted}'")
    print(f"   解密: '{decrypted}'")
    print(f"   解密成功: {original == decrypted}")

if __name__ == "__main__":
    main()
    practice_exercises()
    
    print("\n" + "="*50)
    print("学习小结")
    print("="*50)
    print("1. 位运算符包括：&、|、^、~、<<、>>")
    print("2. 位运算直接操作二进制位，效率很高")
    print("3. 常用于权限控制、状态标志、性能优化")
    print("4. 左移相当于乘以2的幂，右移相当于除以2的幂")
    print("5. 异或运算有特殊性质，可用于加密和变量交换")
    print("6. 掌握位运算有助于理解计算机底层原理")