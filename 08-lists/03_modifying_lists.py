#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
列表修改操作 - 修改列表元素、添加和删除

本文件演示了Python中修改列表的各种方法：
1. 修改单个元素
2. 修改多个元素（切片赋值）
3. 添加元素的方法
4. 删除元素的方法
5. 列表的清空和复制

作者：Python学习教程
日期：2024年
"""

def demonstrate_single_element_modification():
    """演示单个元素的修改"""
    print("=== 单个元素修改 ===")
    
    # 基本元素修改
    fruits = ['apple', 'banana', 'orange']
    print(f"原始列表: {fruits}")
    
    # 通过索引修改
    fruits[0] = 'grape'
    print(f"修改索引0后: {fruits}")
    
    fruits[1] = 'kiwi'
    print(f"修改索引1后: {fruits}")
    
    # 使用负索引修改
    fruits[-1] = 'mango'
    print(f"修改最后一个元素后: {fruits}")
    
    # 修改数字列表
    numbers = [1, 2, 3, 4, 5]
    print(f"\n原始数字列表: {numbers}")
    
    numbers[2] = 100
    print(f"修改索引2后: {numbers}")
    
    # 批量修改
    for i in range(len(numbers)):
        numbers[i] *= 2
    print(f"所有元素乘以2后: {numbers}")

def demonstrate_slice_modification():
    """演示切片修改"""
    print("\n=== 切片修改 ===")
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    print(f"原始列表: {letters}")
    
    # 替换连续的元素
    letters[1:3] = ['X', 'Y']
    print(f"替换索引1-2: {letters}")
    
    # 替换为不同数量的元素
    letters[1:3] = ['P', 'Q', 'R', 'S']
    print(f"替换为更多元素: {letters}")
    
    # 替换为更少的元素
    letters[1:5] = ['M']
    print(f"替换为更少元素: {letters}")
    
    # 在指定位置插入元素
    letters[2:2] = ['N', 'O']
    print(f"在索引2插入元素: {letters}")
    
    # 使用步长修改
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"\n原始数字列表: {numbers}")
    
    numbers[::2] = [10, 30, 50, 80]
    print(f"修改偶数索引位置: {numbers}")

def demonstrate_adding_elements():
    """演示添加元素的方法"""
    print("\n=== 添加元素方法 ===")
    
    # 1. append() - 在末尾添加单个元素
    fruits = ['apple', 'banana']
    print(f"初始列表: {fruits}")
    
    fruits.append('orange')
    print(f"append('orange')后: {fruits}")
    
    fruits.append(['grape', 'kiwi'])  # 注意：整个列表作为一个元素
    print(f"append(['grape', 'kiwi'])后: {fruits}")
    
    # 2. insert() - 在指定位置插入元素
    colors = ['red', 'green', 'blue']
    print(f"\n初始颜色列表: {colors}")
    
    colors.insert(1, 'yellow')
    print(f"insert(1, 'yellow')后: {colors}")
    
    colors.insert(0, 'purple')
    print(f"insert(0, 'purple')后: {colors}")
    
    colors.insert(len(colors), 'orange')  # 等同于append
    print(f"在末尾插入后: {colors}")
    
    # 3. extend() - 扩展列表（添加多个元素）
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]
    print(f"\n列表1: {numbers1}")
    print(f"列表2: {numbers2}")
    
    numbers1.extend(numbers2)
    print(f"extend后的列表1: {numbers1}")
    
    # extend vs append 的区别
    list_a = [1, 2]
    list_b = [1, 2]
    
    list_a.append([3, 4])
    list_b.extend([3, 4])
    
    print(f"\nappend([3, 4]): {list_a}")
    print(f"extend([3, 4]): {list_b}")
    
    # 4. 使用 + 操作符
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list1 + list2
    print(f"\n使用+操作符: {list1} + {list2} = {combined}")
    print(f"原列表1未改变: {list1}")
    
    # 5. 使用 += 操作符
    list1 += list2
    print(f"使用+=操作符后的list1: {list1}")

def demonstrate_removing_elements():
    """演示删除元素的方法"""
    print("\n=== 删除元素方法 ===")
    
    # 1. remove() - 删除第一个匹配的元素
    fruits = ['apple', 'banana', 'orange', 'banana', 'grape']
    print(f"初始列表: {fruits}")
    
    fruits.remove('banana')
    print(f"remove('banana')后: {fruits}")
    
    # 尝试删除不存在的元素会报错
    try:
        fruits.remove('kiwi')
    except ValueError as e:
        print(f"删除不存在元素的错误: {e}")
    
    # 2. pop() - 删除并返回指定位置的元素
    numbers = [10, 20, 30, 40, 50]
    print(f"\n初始数字列表: {numbers}")
    
    last_item = numbers.pop()
    print(f"pop()删除最后元素: {last_item}, 剩余: {numbers}")
    
    second_item = numbers.pop(1)
    print(f"pop(1)删除索引1: {second_item}, 剩余: {numbers}")
    
    # 3. del 语句 - 删除指定位置或切片
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(f"\n初始字母列表: {letters}")
    
    del letters[2]
    print(f"del letters[2]后: {letters}")
    
    del letters[1:3]
    print(f"del letters[1:3]后: {letters}")
    
    del letters[::2]
    print(f"del letters[::2]后: {letters}")
    
    # 4. clear() - 清空整个列表
    temp_list = [1, 2, 3, 4, 5]
    print(f"\n清空前: {temp_list}")
    temp_list.clear()
    print(f"clear()后: {temp_list}")

def demonstrate_advanced_modifications():
    """演示高级修改操作"""
    print("\n=== 高级修改操作 ===")
    
    # 1. 条件修改
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"原始列表: {numbers}")
    
    # 将所有偶数替换为其平方
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            numbers[i] = numbers[i] ** 2
    print(f"偶数平方后: {numbers}")
    
    # 2. 使用列表推导式进行修改
    original = [1, 2, 3, 4, 5]
    modified = [x * 2 if x % 2 == 0 else x for x in original]
    print(f"\n原始: {original}")
    print(f"条件修改: {modified}")
    
    # 3. 批量替换
    text_list = ['hello', 'world', 'python', 'hello']
    print(f"\n原始文本列表: {text_list}")
    
    # 替换所有'hello'为'hi'
    for i in range(len(text_list)):
        if text_list[i] == 'hello':
            text_list[i] = 'hi'
    print(f"替换hello为hi后: {text_list}")
    
    # 4. 嵌套列表修改
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"\n原始矩阵:")
    for row in matrix:
        print(row)
    
    # 修改特定位置
    matrix[1][1] = 100
    print(f"\n修改matrix[1][1]为100后:")
    for row in matrix:
        print(row)
    
    # 修改整行
    matrix[0] = [10, 20, 30]
    print(f"\n修改第一行后:")
    for row in matrix:
        print(row)

def demonstrate_list_operations_comparison():
    """演示不同列表操作的比较"""
    print("\n=== 列表操作比较 ===")
    
    # 创建测试数据
    original = [1, 2, 3]
    
    # 1. append vs extend vs +
    list1 = original.copy()
    list2 = original.copy()
    list3 = original.copy()
    
    print(f"原始列表: {original}")
    
    list1.append([4, 5])
    print(f"append([4, 5]): {list1}")
    
    list2.extend([4, 5])
    print(f"extend([4, 5]): {list2}")
    
    list3 = list3 + [4, 5]
    print(f"+ [4, 5]: {list3}")
    
    # 2. remove vs pop vs del
    test_lists = {
        'remove': [1, 2, 3, 2, 4],
        'pop': [1, 2, 3, 2, 4],
        'del': [1, 2, 3, 2, 4]
    }
    
    print(f"\n删除操作比较:")
    print(f"初始列表: {test_lists['remove']}")
    
    # remove - 删除第一个匹配值
    test_lists['remove'].remove(2)
    print(f"remove(2)后: {test_lists['remove']}")
    
    # pop - 删除指定索引并返回值
    popped = test_lists['pop'].pop(1)
    print(f"pop(1)返回{popped}, 列表: {test_lists['pop']}")
    
    # del - 删除指定索引
    del test_lists['del'][1]
    print(f"del [1]后: {test_lists['del']}")

def demonstrate_safe_modifications():
    """演示安全的修改操作"""
    print("\n=== 安全修改操作 ===")
    
    def safe_remove(lst, item):
        """安全删除元素"""
        if item in lst:
            lst.remove(item)
            return True
        return False
    
    def safe_pop(lst, index=None):
        """安全弹出元素"""
        if not lst:
            return None
        if index is None:
            return lst.pop()
        if 0 <= index < len(lst):
            return lst.pop(index)
        return None
    
    def safe_modify(lst, index, value):
        """安全修改元素"""
        if 0 <= index < len(lst):
            old_value = lst[index]
            lst[index] = value
            return old_value
        return None
    
    # 测试安全操作
    test_list = [1, 2, 3, 4, 5]
    print(f"测试列表: {test_list}")
    
    # 安全删除
    result1 = safe_remove(test_list, 3)
    print(f"safe_remove(3): {result1}, 列表: {test_list}")
    
    result2 = safe_remove(test_list, 10)
    print(f"safe_remove(10): {result2}, 列表: {test_list}")
    
    # 安全弹出
    result3 = safe_pop(test_list, 1)
    print(f"safe_pop(1): {result3}, 列表: {test_list}")
    
    result4 = safe_pop(test_list, 10)
    print(f"safe_pop(10): {result4}, 列表: {test_list}")
    
    # 安全修改
    result5 = safe_modify(test_list, 0, 100)
    print(f"safe_modify(0, 100): 旧值{result5}, 列表: {test_list}")
    
    result6 = safe_modify(test_list, 10, 200)
    print(f"safe_modify(10, 200): {result6}, 列表: {test_list}")

def main():
    """主函数，演示所有列表修改方法"""
    print("Python列表修改操作大全")
    print("=" * 50)
    
    demonstrate_single_element_modification()
    demonstrate_slice_modification()
    demonstrate_adding_elements()
    demonstrate_removing_elements()
    demonstrate_advanced_modifications()
    demonstrate_list_operations_comparison()
    demonstrate_safe_modifications()
    
    print("\n=== 总结 ===")
    print("列表修改的主要方法:")
    print("\n添加元素:")
    print("- append(item): 在末尾添加单个元素")
    print("- insert(index, item): 在指定位置插入元素")
    print("- extend(iterable): 扩展列表，添加多个元素")
    print("- +=: 就地扩展列表")
    print("\n删除元素:")
    print("- remove(item): 删除第一个匹配的元素")
    print("- pop(index): 删除并返回指定位置的元素")
    print("- del: 删除指定位置或切片")
    print("- clear(): 清空整个列表")
    print("\n修改元素:")
    print("- 直接赋值: list[index] = new_value")
    print("- 切片赋值: list[start:end] = new_values")
    print("\n注意事项:")
    print("- 修改操作会改变原列表")
    print("- 索引超出范围会引发错误")
    print("- 删除不存在的元素会引发ValueError")

if __name__ == "__main__":
    main()