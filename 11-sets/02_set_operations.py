#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
集合的基本操作

本文件演示了Python中集合的基本操作：
1. 添加元素（add, update）
2. 删除元素（remove, discard, pop, clear）
3. 检查元素存在性
4. 集合长度和判空
5. 集合的复制
6. 集合的比较

作者：Python学习教程
日期：2024年
"""

def main():
    print("=" * 50)
    print("集合的基本操作演示")
    print("=" * 50)
    
    # 1. 添加元素
    print("\n1. 添加元素")
    print("-" * 30)
    
    # 使用add()方法添加单个元素
    fruits = {"apple", "banana"}
    print(f"初始集合: {fruits}")
    
    fruits.add("orange")
    print(f"添加'orange'后: {fruits}")
    
    # 尝试添加已存在的元素
    fruits.add("apple")
    print(f"尝试添加已存在的'apple': {fruits}")
    print("注意：添加已存在的元素不会改变集合")
    
    # 使用update()方法添加多个元素
    print("\n使用update()添加多个元素:")
    fruits.update(["grape", "kiwi"])
    print(f"添加列表元素后: {fruits}")
    
    fruits.update({"mango", "pear"})
    print(f"添加集合元素后: {fruits}")
    
    fruits.update("cherry")  # 字符串会被拆分为字符
    print(f"添加字符串'cherry'后: {fruits}")
    print("注意：字符串被拆分为单个字符添加")
    
    # 2. 删除元素
    print("\n2. 删除元素")
    print("-" * 30)
    
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print(f"初始数字集合: {numbers}")
    
    # 使用remove()方法删除元素
    numbers.remove(5)
    print(f"删除5后: {numbers}")
    
    # remove()删除不存在的元素会报错
    try:
        numbers.remove(15)  # 不存在的元素
    except KeyError as e:
        print(f"使用remove()删除不存在的元素会报错: {e}")
    
    # 使用discard()方法删除元素（推荐）
    numbers.discard(3)
    print(f"使用discard()删除3后: {numbers}")
    
    numbers.discard(15)  # 删除不存在的元素不会报错
    print(f"使用discard()删除不存在的元素15: {numbers}")
    print("注意：discard()删除不存在的元素不会报错")
    
    # 使用pop()方法随机删除并返回一个元素
    print("\n使用pop()随机删除元素:")
    original_numbers = numbers.copy()
    print(f"删除前: {numbers}")
    
    removed_element = numbers.pop()
    print(f"pop()返回的元素: {removed_element}")
    print(f"删除后: {numbers}")
    
    # 从空集合pop会报错
    empty_set = set()
    try:
        empty_set.pop()
    except KeyError as e:
        print(f"从空集合pop会报错: {e}")
    
    # 使用clear()清空集合
    test_set = {1, 2, 3}
    print(f"\n清空前: {test_set}")
    test_set.clear()
    print(f"清空后: {test_set}")
    
    # 3. 检查元素存在性
    print("\n3. 检查元素存在性")
    print("-" * 30)
    
    colors = {"red", "green", "blue", "yellow"}
    print(f"颜色集合: {colors}")
    
    # 使用in操作符
    print(f"'red' in colors: {'red' in colors}")
    print(f"'purple' in colors: {'purple' in colors}")
    
    # 使用not in操作符
    print(f"'purple' not in colors: {'purple' not in colors}")
    
    # 实际应用：检查用户权限
    user_permissions = {"read", "write", "execute"}
    required_permission = "admin"
    
    if required_permission in user_permissions:
        print(f"用户具有{required_permission}权限")
    else:
        print(f"用户没有{required_permission}权限")
    
    # 4. 集合长度和判空
    print("\n4. 集合长度和判空")
    print("-" * 30)
    
    sample_set = {"a", "b", "c", "d", "e"}
    print(f"集合: {sample_set}")
    print(f"集合长度: {len(sample_set)}")
    
    # 判断集合是否为空
    empty_set = set()
    print(f"\n空集合: {empty_set}")
    print(f"空集合长度: {len(empty_set)}")
    print(f"空集合是否为空: {len(empty_set) == 0}")
    print(f"使用bool()判断: {bool(empty_set)}")
    print(f"使用bool()判断非空集合: {bool(sample_set)}")
    
    # 5. 集合的复制
    print("\n5. 集合的复制")
    print("-" * 30)
    
    original = {1, 2, 3, 4, 5}
    print(f"原始集合: {original}")
    
    # 浅复制
    copy1 = original.copy()
    copy2 = set(original)
    
    print(f"使用copy()复制: {copy1}")
    print(f"使用set()复制: {copy2}")
    
    # 验证是不同的对象
    print(f"original is copy1: {original is copy1}")
    print(f"original == copy1: {original == copy1}")
    
    # 修改原集合不影响复制的集合
    original.add(6)
    print(f"\n修改原集合后:")
    print(f"原始集合: {original}")
    print(f"复制的集合: {copy1}")
    
    # 6. 集合的比较
    print("\n6. 集合的比较")
    print("-" * 30)
    
    set1 = {1, 2, 3}
    set2 = {3, 2, 1}  # 顺序不同但元素相同
    set3 = {1, 2, 3, 4}
    set4 = {1, 2}
    
    print(f"集合1: {set1}")
    print(f"集合2: {set2}")
    print(f"集合3: {set3}")
    print(f"集合4: {set4}")
    
    # 相等比较
    print(f"\nset1 == set2: {set1 == set2}")
    print(f"set1 == set3: {set1 == set3}")
    
    # 子集和超集
    print(f"\nset4 是 set1 的子集: {set4.issubset(set1)}")
    print(f"set1 是 set3 的子集: {set1.issubset(set3)}")
    print(f"set1 是 set4 的超集: {set1.issuperset(set4)}")
    print(f"set3 是 set1 的超集: {set3.issuperset(set1)}")
    
    # 不相交集合
    set5 = {7, 8, 9}
    print(f"\nset1 和 set5 是否不相交: {set1.isdisjoint(set5)}")
    print(f"set1 和 set3 是否不相交: {set1.isdisjoint(set3)}")
    
    print("\n=" * 50)
    print("集合基本操作演示完成！")
    print("=" * 50)

def demonstrate_advanced_operations():
    """
    演示高级操作
    """
    print("\n补充：高级操作演示")
    print("-" * 30)
    
    # 批量操作
    base_set = {1, 2, 3}
    print(f"基础集合: {base_set}")
    
    # 批量添加不同类型的数据
    base_set.update([4, 5], {6, 7}, (8, 9))
    print(f"批量添加后: {base_set}")
    
    # 条件删除
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print(f"\n原始数字集合: {numbers}")
    
    # 删除所有偶数
    even_numbers = {x for x in numbers if x % 2 == 0}
    numbers -= even_numbers  # 使用差集操作
    print(f"删除偶数后: {numbers}")
    
    # 集合的动态操作
    dynamic_set = set()
    for i in range(5):
        dynamic_set.add(i * 2)
        print(f"第{i+1}次添加后: {dynamic_set}")

def practical_examples():
    """
    实际应用示例
    """
    print("\n实际应用示例")
    print("-" * 30)
    
    # 示例1：用户标签管理
    user_tags = {"python", "programming", "beginner"}
    print(f"用户标签: {user_tags}")
    
    # 添加新标签
    new_tags = ["web", "django", "python"]  # python重复
    user_tags.update(new_tags)
    print(f"添加新标签后: {user_tags}")
    
    # 删除过时标签
    outdated_tags = {"beginner"}
    user_tags -= outdated_tags
    print(f"删除过时标签后: {user_tags}")
    
    # 示例2：在线用户管理
    online_users = set()
    
    # 用户上线
    def user_login(username):
        online_users.add(username)
        print(f"用户 {username} 上线，当前在线用户: {online_users}")
    
    # 用户下线
    def user_logout(username):
        online_users.discard(username)
        print(f"用户 {username} 下线，当前在线用户: {online_users}")
    
    # 模拟用户操作
    user_login("Alice")
    user_login("Bob")
    user_login("Charlie")
    user_logout("Bob")
    user_logout("David")  # 不存在的用户
    
    print(f"最终在线用户: {online_users}")

def practice_exercises():
    """
    练习题
    """
    print("\n练习题：")
    print("-" * 20)
    
    # 练习1：实现一个简单的购物车
    shopping_cart = set()
    
    def add_to_cart(item):
        shopping_cart.add(item)
        return f"已添加 {item} 到购物车"
    
    def remove_from_cart(item):
        if item in shopping_cart:
            shopping_cart.remove(item)
            return f"已从购物车移除 {item}"
        else:
            return f"{item} 不在购物车中"
    
    def show_cart():
        return f"购物车内容: {shopping_cart}"
    
    print("1. 购物车操作:")
    print(add_to_cart("苹果"))
    print(add_to_cart("香蕉"))
    print(add_to_cart("苹果"))  # 重复添加
    print(show_cart())
    print(remove_from_cart("香蕉"))
    print(remove_from_cart("橙子"))  # 不存在的商品
    print(show_cart())
    
    # 练习2：统计两个文本的共同单词
    text1 = "python is a powerful programming language"
    text2 = "java is also a programming language"
    
    words1 = set(text1.split())
    words2 = set(text2.split())
    
    print(f"\n2. 文本分析:")
    print(f"文本1单词: {words1}")
    print(f"文本2单词: {words2}")
    print(f"共同单词: {words1 & words2}")
    print(f"文本1独有单词: {words1 - words2}")
    print(f"文本2独有单词: {words2 - words1}")

if __name__ == "__main__":
    main()
    demonstrate_advanced_operations()
    practical_examples()
    practice_exercises()