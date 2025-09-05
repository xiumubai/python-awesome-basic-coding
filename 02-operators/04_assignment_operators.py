#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
赋值运算符学习教程

本文件演示Python中的赋值运算符的使用方法和特性
包括：基本赋值(=)、复合赋值(+=, -=, *=, /=, //=, %=, **=)、位赋值(&=, |=, ^=, <<=, >>=)

学习目标：
1. 掌握基本赋值运算符的使用
2. 理解复合赋值运算符的便利性
3. 学会多重赋值和解包赋值
4. 了解赋值运算符的注意事项
"""

def main():
    print("="*50)
    print("Python 赋值运算符学习教程")
    print("="*50)
    
    # 1. 基本赋值运算符
    print("\n1. 基本赋值运算符 (=)")
    print("-" * 30)
    
    # 简单赋值
    x = 10
    y = 20
    name = "Python"
    is_valid = True
    
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"name = '{name}'")
    print(f"is_valid = {is_valid}")
    
    # 变量重新赋值
    print("\n变量重新赋值：")
    x = 30
    print(f"x 重新赋值后: {x}")
    
    # 2. 复合赋值运算符
    print("\n2. 复合赋值运算符")
    print("-" * 30)
    
    # 算术复合赋值
    a = 10
    print(f"初始值 a = {a}")
    
    a += 5  # 等价于 a = a + 5
    print(f"a += 5 后: a = {a}")
    
    a -= 3  # 等价于 a = a - 3
    print(f"a -= 3 后: a = {a}")
    
    a *= 2  # 等价于 a = a * 2
    print(f"a *= 2 后: a = {a}")
    
    a /= 4  # 等价于 a = a / 4
    print(f"a /= 4 后: a = {a}")
    
    a //= 2  # 等价于 a = a // 2
    print(f"a //= 2 后: a = {a}")
    
    a %= 3  # 等价于 a = a % 3
    print(f"a %= 3 后: a = {a}")
    
    a **= 3  # 等价于 a = a ** 3
    print(f"a **= 3 后: a = {a}")
    
    # 3. 字符串和列表的复合赋值
    print("\n3. 字符串和列表的复合赋值")
    print("-" * 30)
    
    # 字符串复合赋值
    text = "Hello"
    print(f"初始字符串: '{text}'")
    
    text += " World"  # 字符串连接
    print(f"text += ' World' 后: '{text}'")
    
    text *= 2  # 字符串重复
    print(f"text *= 2 后: '{text}'")
    
    # 列表复合赋值
    numbers = [1, 2, 3]
    print(f"\n初始列表: {numbers}")
    
    numbers += [4, 5]  # 列表扩展
    print(f"numbers += [4, 5] 后: {numbers}")
    
    numbers *= 2  # 列表重复
    print(f"numbers *= 2 后: {numbers}")
    
    # 注意：+= 和 extend() 的区别
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    
    list1 += [4, 5]  # 修改原列表
    list2 = list2 + [4, 5]  # 创建新列表
    
    print(f"\nlist1 += [4, 5]: {list1}")
    print(f"list2 = list2 + [4, 5]: {list2}")
    
    # 4. 多重赋值
    print("\n4. 多重赋值")
    print("-" * 30)
    
    # 同时给多个变量赋相同值
    x = y = z = 100
    print(f"x = y = z = 100: x={x}, y={y}, z={z}")
    
    # 修改其中一个变量
    x = 200
    print(f"x = 200 后: x={x}, y={y}, z={z}")
    
    # 注意：可变对象的多重赋值陷阱
    print("\n可变对象的多重赋值：")
    list_a = list_b = [1, 2, 3]  # 两个变量指向同一个列表
    print(f"初始: list_a={list_a}, list_b={list_b}")
    
    list_a.append(4)  # 修改列表
    print(f"list_a.append(4) 后: list_a={list_a}, list_b={list_b}")
    
    # 正确的方式：创建独立的列表
    list_c = [1, 2, 3]
    list_d = [1, 2, 3]  # 或者 list_d = list_c.copy()
    print(f"\n独立列表: list_c={list_c}, list_d={list_d}")
    
    list_c.append(4)
    print(f"list_c.append(4) 后: list_c={list_c}, list_d={list_d}")
    
    # 5. 解包赋值（元组赋值）
    print("\n5. 解包赋值")
    print("-" * 30)
    
    # 基本解包
    point = (3, 4)
    x, y = point
    print(f"点坐标 {point} 解包: x={x}, y={y}")
    
    # 列表解包
    colors = ['red', 'green', 'blue']
    color1, color2, color3 = colors
    print(f"颜色列表 {colors} 解包: {color1}, {color2}, {color3}")
    
    # 变量交换
    a, b = 10, 20
    print(f"交换前: a={a}, b={b}")
    a, b = b, a  # 优雅的变量交换
    print(f"交换后: a={a}, b={b}")
    
    # 扩展解包（Python 3.0+）
    numbers = [1, 2, 3, 4, 5]
    first, *middle, last = numbers
    print(f"\n扩展解包 {numbers}:")
    print(f"first={first}, middle={middle}, last={last}")
    
    # 忽略不需要的值
    data = ('Alice', 25, 'Engineer', 'New York')
    name, age, _, city = data  # 使用 _ 忽略职业
    print(f"\n忽略部分值: name={name}, age={age}, city={city}")
    
    # 6. 位赋值运算符
    print("\n6. 位赋值运算符")
    print("-" * 30)
    
    # 位运算复合赋值
    num = 12  # 二进制: 1100
    print(f"初始值 num = {num} (二进制: {bin(num)})")
    
    num &= 10  # 按位与，10的二进制是1010
    print(f"num &= 10 后: {num} (二进制: {bin(num)})")
    
    num |= 5   # 按位或，5的二进制是101
    print(f"num |= 5 后: {num} (二进制: {bin(num)})")
    
    num ^= 3   # 按位异或，3的二进制是11
    print(f"num ^= 3 后: {num} (二进制: {bin(num)})")
    
    num <<= 2  # 左移2位
    print(f"num <<= 2 后: {num} (二进制: {bin(num)})")
    
    num >>= 1  # 右移1位
    print(f"num >>= 1 后: {num} (二进制: {bin(num)})")
    
    # 7. 实际应用示例
    print("\n7. 实际应用示例")
    print("-" * 30)
    
    # 计数器
    counter = 0
    items = ['apple', 'banana', 'cherry', 'date']
    
    print("计数器示例：")
    for item in items:
        counter += 1
        print(f"处理第 {counter} 个项目: {item}")
    
    # 累加器
    total = 0
    prices = [10.5, 25.0, 15.75, 8.25]
    
    print("\n累加器示例：")
    for price in prices:
        total += price
        print(f"当前总价: {total:.2f}")
    
    # 字符串构建
    message = ""
    words = ['Hello', 'beautiful', 'world']
    
    print("\n字符串构建示例：")
    for word in words:
        if message:  # 如果不是第一个词，添加空格
            message += " "
        message += word
        print(f"当前消息: '{message}'")
    
    # 8. 性能考虑
    print("\n8. 性能考虑")
    print("-" * 30)
    
    import time
    
    # 字符串连接性能比较
    def string_concat_plus():
        result = ""
        for i in range(1000):
            result += str(i)
        return result
    
    def string_concat_join():
        parts = []
        for i in range(1000):
            parts.append(str(i))
        return ''.join(parts)
    
    # 测试性能（简化版）
    print("字符串连接性能比较（1000次操作）：")
    
    start = time.time()
    result1 = string_concat_plus()
    time1 = time.time() - start
    print(f"使用 += 连接: {time1:.6f} 秒")
    
    start = time.time()
    result2 = string_concat_join()
    time2 = time.time() - start
    print(f"使用 join() 连接: {time2:.6f} 秒")
    
    print(f"join() 方法快了约 {time1/time2:.1f} 倍")

def practice_exercises():
    """
    练习题部分
    """
    print("\n" + "="*50)
    print("练习题")
    print("="*50)
    
    print("\n请预测以下代码的输出：")
    print("1. x = 5; x += 3; x *= 2; print(x)")
    print("2. s = 'Hello'; s += ' World'; s *= 2; print(len(s))")
    print("3. a = [1, 2]; b = a; a += [3]; print(b)")
    print("4. x, y = 10, 20; x, y = y, x; print(x, y)")
    
    print("\n答案：")
    
    # 1. 数值运算
    x = 5
    x += 3  # x = 8
    x *= 2  # x = 16
    print(f"1. {x}")
    
    # 2. 字符串运算
    s = 'Hello'
    s += ' World'  # s = 'Hello World'
    s *= 2  # s = 'Hello WorldHello World'
    print(f"2. {len(s)}")
    
    # 3. 列表引用
    a = [1, 2]
    b = a  # b 和 a 指向同一个列表
    a += [3]  # 修改原列表
    print(f"3. {b}")
    
    # 4. 变量交换
    x, y = 10, 20
    x, y = y, x
    print(f"4. {x} {y}")
    
    print("\n编程练习：")
    print("1. 实现一个简单的银行账户类")
    print("2. 创建一个购物车系统")
    print("3. 编写一个文本处理器")
    
    # 示例解答
    print("\n示例解答：")
    
    # 1. 银行账户类
    class BankAccount:
        def __init__(self, initial_balance=0):
            self.balance = initial_balance
        
        def deposit(self, amount):
            self.balance += amount
            return self.balance
        
        def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                print("余额不足")
                return self.balance
        
        def get_balance(self):
            return self.balance
    
    print("1. 银行账户示例：")
    account = BankAccount(1000)
    print(f"   初始余额: {account.get_balance()}")
    account.deposit(500)
    print(f"   存款500后: {account.get_balance()}")
    account.withdraw(200)
    print(f"   取款200后: {account.get_balance()}")
    
    # 2. 购物车系统
    class ShoppingCart:
        def __init__(self):
            self.items = {}
            self.total = 0
        
        def add_item(self, item, price, quantity=1):
            if item in self.items:
                self.items[item]['quantity'] += quantity
            else:
                self.items[item] = {'price': price, 'quantity': quantity}
            self.total += price * quantity
        
        def remove_item(self, item, quantity=1):
            if item in self.items:
                if quantity >= self.items[item]['quantity']:
                    self.total -= self.items[item]['price'] * self.items[item]['quantity']
                    del self.items[item]
                else:
                    self.items[item]['quantity'] -= quantity
                    self.total -= self.items[item]['price'] * quantity
        
        def get_total(self):
            return self.total
    
    print("\n2. 购物车示例：")
    cart = ShoppingCart()
    cart.add_item("苹果", 5.0, 3)
    cart.add_item("香蕉", 3.0, 2)
    print(f"   添加商品后总价: {cart.get_total()}")
    cart.remove_item("苹果", 1)
    print(f"   移除1个苹果后总价: {cart.get_total()}")
    
    # 3. 文本处理器
    class TextProcessor:
        def __init__(self):
            self.text = ""
            self.word_count = 0
            self.char_count = 0
        
        def add_text(self, new_text):
            self.text += new_text
            self.word_count += len(new_text.split())
            self.char_count += len(new_text)
        
        def clear(self):
            self.text = ""
            self.word_count = 0
            self.char_count = 0
        
        def get_stats(self):
            return {
                'text': self.text,
                'words': self.word_count,
                'characters': self.char_count
            }
    
    print("\n3. 文本处理器示例：")
    processor = TextProcessor()
    processor.add_text("Hello world ")
    processor.add_text("Python is great!")
    stats = processor.get_stats()
    print(f"   文本: '{stats['text']}'")
    print(f"   单词数: {stats['words']}, 字符数: {stats['characters']}")

if __name__ == "__main__":
    main()
    practice_exercises()
    
    print("\n" + "="*50)
    print("学习小结")
    print("="*50)
    print("1. 赋值运算符包括：=、+=、-=、*=、/=、//=、%=、**=")
    print("2. 复合赋值运算符可以简化代码")
    print("3. 多重赋值要注意可变对象的陷阱")
    print("4. 解包赋值可以优雅地处理多个值")
    print("5. 位赋值运算符用于位操作")
    print("6. 选择合适的方法可以提高性能")