#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
列表内置方法 - 列表的内置方法详解

本文件演示了Python列表的所有内置方法：
1. 添加和插入方法：append, insert, extend
2. 删除方法：remove, pop, clear
3. 查找和计数方法：index, count
4. 排序和反转方法：sort, reverse
5. 复制方法：copy
6. 实用方法组合和最佳实践

作者：Python学习教程
日期：2024年
"""

def demonstrate_adding_methods():
    """演示添加和插入方法"""
    print("=== 添加和插入方法 ===")
    
    # append() - 在列表末尾添加元素
    fruits = ['apple', 'banana']
    print(f"初始列表: {fruits}")
    
    fruits.append('orange')
    print(f"append('orange')后: {fruits}")
    
    # append可以添加任何类型的对象
    fruits.append([1, 2, 3])
    fruits.append({'key': 'value'})
    print(f"添加列表和字典后: {fruits}")
    
    # insert() - 在指定位置插入元素
    numbers = [1, 2, 4, 5]
    print(f"\n数字列表: {numbers}")
    
    numbers.insert(2, 3)  # 在索引2处插入3
    print(f"insert(2, 3)后: {numbers}")
    
    numbers.insert(0, 0)  # 在开头插入
    print(f"insert(0, 0)后: {numbers}")
    
    numbers.insert(len(numbers), 6)  # 在末尾插入（等同于append）
    print(f"在末尾插入6后: {numbers}")
    
    # extend() - 扩展列表
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(f"\n列表1: {list1}")
    print(f"列表2: {list2}")
    
    list1.extend(list2)
    print(f"list1.extend(list2)后: {list1}")
    
    # extend可以接受任何可迭代对象
    colors = ['red', 'green']
    colors.extend('blue')  # 字符串是可迭代的
    print(f"extend('blue')后: {colors}")
    
    colors.extend(range(3))
    print(f"extend(range(3))后: {colors}")

def demonstrate_removing_methods():
    """演示删除方法"""
    print("\n=== 删除方法 ===")
    
    # remove() - 删除第一个匹配的元素
    items = ['a', 'b', 'c', 'b', 'd']
    print(f"初始列表: {items}")
    
    items.remove('b')
    print(f"remove('b')后: {items}")
    
    # 删除不存在的元素会引发ValueError
    try:
        items.remove('x')
    except ValueError as e:
        print(f"删除不存在元素的错误: {e}")
    
    # pop() - 删除并返回元素
    numbers = [10, 20, 30, 40, 50]
    print(f"\n数字列表: {numbers}")
    
    # 不指定索引时删除最后一个元素
    last = numbers.pop()
    print(f"pop()返回: {last}, 剩余: {numbers}")
    
    # 指定索引删除
    second = numbers.pop(1)
    print(f"pop(1)返回: {second}, 剩余: {numbers}")
    
    # 对空列表使用pop会引发IndexError
    empty_list = []
    try:
        empty_list.pop()
    except IndexError as e:
        print(f"空列表pop错误: {e}")
    
    # clear() - 清空列表
    temp_list = [1, 2, 3, 4, 5]
    print(f"\n清空前: {temp_list}")
    temp_list.clear()
    print(f"clear()后: {temp_list}")

def demonstrate_search_methods():
    """演示查找和计数方法"""
    print("\n=== 查找和计数方法 ===")
    
    # index() - 查找元素的索引
    fruits = ['apple', 'banana', 'orange', 'banana', 'grape']
    print(f"水果列表: {fruits}")
    
    # 查找第一个匹配元素的索引
    banana_index = fruits.index('banana')
    print(f"'banana'的索引: {banana_index}")
    
    # 在指定范围内查找
    banana_index2 = fruits.index('banana', 2)  # 从索引2开始查找
    print(f"从索引2开始查找'banana': {banana_index2}")
    
    # 在指定范围内查找（指定开始和结束）
    try:
        orange_index = fruits.index('orange', 0, 3)  # 在索引0-2范围内查找
        print(f"在索引0-2范围内'orange'的索引: {orange_index}")
    except ValueError:
        print("在指定范围内未找到'orange'")
    
    # 查找不存在的元素会引发ValueError
    try:
        fruits.index('kiwi')
    except ValueError as e:
        print(f"查找不存在元素的错误: {e}")
    
    # count() - 计算元素出现次数
    numbers = [1, 2, 3, 2, 4, 2, 5]
    print(f"\n数字列表: {numbers}")
    
    count_2 = numbers.count(2)
    print(f"数字2出现次数: {count_2}")
    
    count_6 = numbers.count(6)
    print(f"数字6出现次数: {count_6}")
    
    # 统计所有元素的出现次数
    unique_numbers = list(set(numbers))
    print(f"\n各元素出现次数:")
    for num in unique_numbers:
        print(f"  {num}: {numbers.count(num)}次")

def demonstrate_sorting_methods():
    """演示排序和反转方法"""
    print("\n=== 排序和反转方法 ===")
    
    # sort() - 就地排序
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"原始数字列表: {numbers}")
    
    # 升序排序（默认）
    numbers_copy1 = numbers.copy()
    numbers_copy1.sort()
    print(f"升序排序后: {numbers_copy1}")
    
    # 降序排序
    numbers_copy2 = numbers.copy()
    numbers_copy2.sort(reverse=True)
    print(f"降序排序后: {numbers_copy2}")
    
    # 字符串排序
    words = ['banana', 'apple', 'cherry', 'date']
    print(f"\n原始单词列表: {words}")
    
    words_copy1 = words.copy()
    words_copy1.sort()
    print(f"字母序排序: {words_copy1}")
    
    # 按长度排序
    words_copy2 = words.copy()
    words_copy2.sort(key=len)
    print(f"按长度排序: {words_copy2}")
    
    # 按长度降序排序
    words_copy3 = words.copy()
    words_copy3.sort(key=len, reverse=True)
    print(f"按长度降序: {words_copy3}")
    
    # 自定义排序键
    students = [('Alice', 85), ('Bob', 90), ('Charlie', 78), ('Diana', 92)]
    print(f"\n学生成绩: {students}")
    
    # 按成绩排序
    students_by_grade = students.copy()
    students_by_grade.sort(key=lambda x: x[1])
    print(f"按成绩排序: {students_by_grade}")
    
    # 按姓名排序
    students_by_name = students.copy()
    students_by_name.sort(key=lambda x: x[0])
    print(f"按姓名排序: {students_by_name}")
    
    # reverse() - 反转列表
    original = [1, 2, 3, 4, 5]
    print(f"\n原始列表: {original}")
    
    original.reverse()
    print(f"reverse()后: {original}")
    
    # 注意：sort()和reverse()都是就地操作，返回None
    result = [3, 1, 2].sort()
    print(f"\nsort()的返回值: {result}")

def demonstrate_copy_method():
    """演示复制方法"""
    print("\n=== 复制方法 ===")
    
    # copy() - 创建浅复制
    original = [1, 2, [3, 4], 5]
    copied = original.copy()
    
    print(f"原始列表: {original}")
    print(f"复制列表: {copied}")
    print(f"是否为同一对象: {original is copied}")
    print(f"内容是否相等: {original == copied}")
    
    # 修改复制列表的简单元素
    copied[0] = 100
    print(f"\n修改复制列表的第一个元素后:")
    print(f"原始列表: {original}")
    print(f"复制列表: {copied}")
    
    # 修改嵌套列表（浅复制的限制）
    copied[2][0] = 999
    print(f"\n修改嵌套列表后:")
    print(f"原始列表: {original}")
    print(f"复制列表: {copied}")
    print("注意：嵌套对象被共享了！")
    
    # 深复制解决方案
    import copy as copy_module
    
    original2 = [1, 2, [3, 4], 5]
    shallow_copy = original2.copy()
    deep_copy = copy_module.deepcopy(original2)
    
    print(f"\n深复制演示:")
    print(f"原始列表: {original2}")
    print(f"浅复制: {shallow_copy}")
    print(f"深复制: {deep_copy}")
    
    # 修改嵌套列表
    original2[2][0] = 888
    print(f"\n修改原始列表的嵌套元素后:")
    print(f"原始列表: {original2}")
    print(f"浅复制: {shallow_copy}")
    print(f"深复制: {deep_copy}")

def demonstrate_method_chaining():
    """演示方法链式调用的注意事项"""
    print("\n=== 方法链式调用注意事项 ===")
    
    # 错误的链式调用（返回None的方法）
    numbers = [3, 1, 4, 1, 5]
    print(f"原始列表: {numbers}")
    
    # 这些方法返回None，不能链式调用
    try:
        # result = numbers.sort().reverse()  # 这会出错
        numbers.sort()
        print(f"排序后: {numbers}")
        numbers.reverse()
        print(f"反转后: {numbers}")
    except AttributeError as e:
        print(f"链式调用错误: {e}")
    
    # 正确的做法：分步操作
    numbers2 = [3, 1, 4, 1, 5]
    numbers2.sort()
    numbers2.reverse()
    print(f"正确操作结果: {numbers2}")
    
    # 或者使用内置函数（返回新列表）
    numbers3 = [3, 1, 4, 1, 5]
    sorted_desc = sorted(numbers3, reverse=True)
    print(f"使用sorted()函数: {sorted_desc}")
    print(f"原列表未改变: {numbers3}")

def demonstrate_practical_examples():
    """演示实际应用示例"""
    print("\n=== 实际应用示例 ===")
    
    # 1. 去重并保持顺序
    def remove_duplicates_keep_order(lst):
        """去除重复元素但保持顺序"""
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    numbers_with_duplicates = [1, 2, 3, 2, 4, 1, 5, 3]
    unique_numbers = remove_duplicates_keep_order(numbers_with_duplicates)
    print(f"原列表: {numbers_with_duplicates}")
    print(f"去重后: {unique_numbers}")
    
    # 2. 统计元素频率
    def count_frequencies(lst):
        """统计列表中各元素的频率"""
        frequencies = {}
        for item in lst:
            frequencies[item] = frequencies.get(item, 0) + 1
        return frequencies
    
    text_list = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    freq = count_frequencies(text_list)
    print(f"\n文本列表: {text_list}")
    print(f"频率统计: {freq}")
    
    # 3. 安全的列表操作
    def safe_list_operations(lst, operations):
        """安全执行列表操作"""
        result_list = lst.copy()  # 不修改原列表
        results = []
        
        for operation, *args in operations:
            try:
                if operation == 'append':
                    result_list.append(args[0])
                    results.append(f"成功添加 {args[0]}")
                elif operation == 'remove':
                    result_list.remove(args[0])
                    results.append(f"成功删除 {args[0]}")
                elif operation == 'pop':
                    index = args[0] if args else None
                    if index is not None:
                        item = result_list.pop(index)
                    else:
                        item = result_list.pop()
                    results.append(f"成功弹出 {item}")
                elif operation == 'insert':
                    result_list.insert(args[0], args[1])
                    results.append(f"成功在索引{args[0]}插入{args[1]}")
            except (ValueError, IndexError) as e:
                results.append(f"操作{operation}失败: {e}")
        
        return result_list, results
    
    test_list = [1, 2, 3, 4, 5]
    operations = [
        ('append', 6),
        ('remove', 3),
        ('pop', 0),
        ('insert', 1, 'new'),
        ('remove', 10),  # 这个会失败
        ('pop', 20)      # 这个也会失败
    ]
    
    final_list, operation_results = safe_list_operations(test_list, operations)
    print(f"\n原列表: {test_list}")
    print(f"操作结果:")
    for result in operation_results:
        print(f"  {result}")
    print(f"最终列表: {final_list}")

def main():
    """主函数，演示所有列表方法"""
    print("Python列表内置方法大全")
    print("=" * 50)
    
    demonstrate_adding_methods()
    demonstrate_removing_methods()
    demonstrate_search_methods()
    demonstrate_sorting_methods()
    demonstrate_copy_method()
    demonstrate_method_chaining()
    demonstrate_practical_examples()
    
    print("\n=== 总结 ===")
    print("列表的主要内置方法:")
    print("\n修改列表的方法（就地操作，返回None）:")
    print("- append(item): 在末尾添加元素")
    print("- insert(index, item): 在指定位置插入元素")
    print("- extend(iterable): 扩展列表")
    print("- remove(item): 删除第一个匹配元素")
    print("- pop(index): 删除并返回指定位置元素")
    print("- clear(): 清空列表")
    print("- sort(key, reverse): 排序列表")
    print("- reverse(): 反转列表")
    print("\n查询方法（不修改列表）:")
    print("- index(item, start, end): 查找元素索引")
    print("- count(item): 计算元素出现次数")
    print("- copy(): 创建浅复制")
    print("\n注意事项:")
    print("- 修改方法返回None，不能链式调用")
    print("- 查找不存在的元素会引发ValueError")
    print("- 索引超出范围会引发IndexError")
    print("- copy()只创建浅复制，嵌套对象仍被共享")

if __name__ == "__main__":
    main()