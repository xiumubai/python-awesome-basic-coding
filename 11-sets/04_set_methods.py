#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
集合的内置方法详解

本文件详细演示了Python集合的所有内置方法：
1. 添加和删除方法
2. 集合运算方法
3. 集合比较方法
4. 集合复制和清空方法
5. 集合信息查询方法
6. 方法链式调用
7. 性能对比和最佳实践

作者：Python学习教程
日期：2024年
"""

import time
import random

def main():
    print("=" * 50)
    print("集合内置方法详解")
    print("=" * 50)
    
    # 1. 添加和删除方法
    print("\n1. 添加和删除方法")
    print("-" * 30)
    
    # add() - 添加单个元素
    fruits = {"apple", "banana"}
    print(f"初始集合: {fruits}")
    
    fruits.add("orange")
    print(f"add('orange')后: {fruits}")
    
    # 添加已存在的元素
    fruits.add("apple")
    print(f"add('apple')后: {fruits} (无变化)")
    
    # update() - 添加多个元素
    fruits.update(["grape", "kiwi"])
    print(f"update(['grape', 'kiwi'])后: {fruits}")
    
    fruits.update({"mango"}, ["pear"], "cherry")
    print(f"update()多参数后: {fruits}")
    
    # remove() - 删除指定元素（元素不存在会报错）
    fruits.remove("banana")
    print(f"remove('banana')后: {fruits}")
    
    try:
        fruits.remove("watermelon")  # 不存在的元素
    except KeyError as e:
        print(f"remove()删除不存在元素报错: {e}")
    
    # discard() - 删除指定元素（元素不存在不报错）
    fruits.discard("grape")
    print(f"discard('grape')后: {fruits}")
    
    fruits.discard("watermelon")  # 不存在的元素
    print(f"discard()删除不存在元素: {fruits} (无报错)")
    
    # pop() - 随机删除并返回一个元素
    removed = fruits.pop()
    print(f"pop()删除的元素: {removed}")
    print(f"pop()后的集合: {fruits}")
    
    # clear() - 清空集合
    test_set = {1, 2, 3}
    print(f"\nclear()前: {test_set}")
    test_set.clear()
    print(f"clear()后: {test_set}")
    
    # 2. 集合运算方法
    print("\n2. 集合运算方法")
    print("-" * 30)
    
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    set_c = {1, 3, 5, 7, 9}
    
    print(f"集合A: {set_a}")
    print(f"集合B: {set_b}")
    print(f"集合C: {set_c}")
    
    # union() - 并集
    union_result = set_a.union(set_b)
    print(f"\nA.union(B): {union_result}")
    
    union_multiple = set_a.union(set_b, set_c)
    print(f"A.union(B, C): {union_multiple}")
    
    # intersection() - 交集
    intersection_result = set_a.intersection(set_b)
    print(f"\nA.intersection(B): {intersection_result}")
    
    intersection_multiple = set_a.intersection(set_b, set_c)
    print(f"A.intersection(B, C): {intersection_multiple}")
    
    # difference() - 差集
    difference_result = set_a.difference(set_b)
    print(f"\nA.difference(B): {difference_result}")
    
    difference_multiple = set_a.difference(set_b, set_c)
    print(f"A.difference(B, C): {difference_multiple}")
    
    # symmetric_difference() - 对称差集
    symmetric_diff = set_a.symmetric_difference(set_b)
    print(f"\nA.symmetric_difference(B): {symmetric_diff}")
    
    # 就地运算方法（修改原集合）
    print("\n就地运算方法:")
    
    # update() - 就地并集
    test_set = {1, 2, 3}
    print(f"原集合: {test_set}")
    test_set.update({4, 5})
    print(f"update({4, 5})后: {test_set}")
    
    # intersection_update() - 就地交集
    test_set.intersection_update({1, 2, 3, 4})
    print(f"intersection_update({{1,2,3,4}})后: {test_set}")
    
    # difference_update() - 就地差集
    test_set.difference_update({2})
    print(f"difference_update({{2}})后: {test_set}")
    
    # symmetric_difference_update() - 就地对称差集
    test_set.symmetric_difference_update({3, 5, 6})
    print(f"symmetric_difference_update({{3,5,6}})后: {test_set}")
    
    # 3. 集合比较方法
    print("\n3. 集合比较方法")
    print("-" * 30)
    
    set1 = {1, 2, 3}
    set2 = {1, 2, 3, 4, 5}
    set3 = {6, 7, 8}
    set4 = {1, 2, 3}
    
    print(f"集合1: {set1}")
    print(f"集合2: {set2}")
    print(f"集合3: {set3}")
    print(f"集合4: {set4}")
    
    # issubset() - 检查是否为子集
    print(f"\nset1.issubset(set2): {set1.issubset(set2)}")
    print(f"set2.issubset(set1): {set2.issubset(set1)}")
    print(f"set1.issubset(set4): {set1.issubset(set4)}")
    
    # issuperset() - 检查是否为超集
    print(f"\nset2.issuperset(set1): {set2.issuperset(set1)}")
    print(f"set1.issuperset(set2): {set1.issuperset(set2)}")
    
    # isdisjoint() - 检查是否不相交
    print(f"\nset1.isdisjoint(set3): {set1.isdisjoint(set3)}")
    print(f"set1.isdisjoint(set2): {set1.isdisjoint(set2)}")
    
    # 4. 集合复制方法
    print("\n4. 集合复制方法")
    print("-" * 30)
    
    original = {1, 2, 3, 4, 5}
    print(f"原集合: {original}")
    
    # copy() - 浅复制
    copied = original.copy()
    print(f"复制的集合: {copied}")
    print(f"是否为同一对象: {original is copied}")
    print(f"内容是否相同: {original == copied}")
    
    # 修改原集合不影响复制的集合
    original.add(6)
    print(f"修改原集合后:")
    print(f"原集合: {original}")
    print(f"复制的集合: {copied}")
    
    print("\n=" * 50)
    print("集合内置方法演示完成！")
    print("=" * 50)

def demonstrate_advanced_methods():
    """
    演示高级方法使用
    """
    print("\n高级方法使用演示")
    print("-" * 30)
    
    # 方法链式调用的模拟（集合方法大多返回None或新集合）
    base_set = {1, 2, 3, 4, 5}
    print(f"基础集合: {base_set}")
    
    # 创建多个操作的组合
    result = base_set.union({6, 7}).intersection({1, 2, 3, 4, 5, 6}).difference({1, 2})
    print(f"链式操作结果: {result}")
    
    # 条件方法调用
    def conditional_operations(s, condition):
        if condition == "expand":
            s.update(range(10, 15))
        elif condition == "filter":
            s.intersection_update(range(1, 6))
        elif condition == "reduce":
            s.difference_update({1, 2})
        return s
    
    test_sets = [
        {1, 2, 3, 4, 5},
        {1, 2, 3, 4, 5},
        {1, 2, 3, 4, 5}
    ]
    
    conditions = ["expand", "filter", "reduce"]
    
    for i, (s, cond) in enumerate(zip(test_sets, conditions)):
        print(f"\n操作{i+1} ({cond}):")
        print(f"操作前: {s}")
        conditional_operations(s, cond)
        print(f"操作后: {s}")

def demonstrate_method_combinations():
    """
    演示方法组合使用
    """
    print("\n方法组合使用演示")
    print("-" * 30)
    
    # 数据清洗示例
    raw_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, "a", "b", "a", None, None]
    print(f"原始数据: {raw_data}")
    
    # 步骤1：转换为集合去重
    unique_data = set(raw_data)
    print(f"去重后: {unique_data}")
    
    # 步骤2：过滤掉None值
    unique_data.discard(None)
    print(f"移除None后: {unique_data}")
    
    # 步骤3：分离数字和字符串
    numbers = {x for x in unique_data if isinstance(x, (int, float))}
    strings = {x for x in unique_data if isinstance(x, str)}
    
    print(f"数字集合: {numbers}")
    print(f"字符串集合: {strings}")
    
    # 步骤4：对数字集合进行运算
    even_numbers = {x for x in numbers if x % 2 == 0}
    odd_numbers = numbers - even_numbers
    
    print(f"偶数: {even_numbers}")
    print(f"奇数: {odd_numbers}")
    
    # 用户权限管理示例
    print("\n用户权限管理示例:")
    
    class UserPermissionManager:
        def __init__(self):
            self.permissions = set()
        
        def grant_permission(self, permission):
            """授予权限"""
            self.permissions.add(permission)
            return self
        
        def grant_permissions(self, permissions):
            """批量授予权限"""
            self.permissions.update(permissions)
            return self
        
        def revoke_permission(self, permission):
            """撤销权限"""
            self.permissions.discard(permission)
            return self
        
        def revoke_permissions(self, permissions):
            """批量撤销权限"""
            self.permissions.difference_update(permissions)
            return self
        
        def has_permission(self, permission):
            """检查是否有权限"""
            return permission in self.permissions
        
        def has_all_permissions(self, permissions):
            """检查是否有所有权限"""
            return set(permissions).issubset(self.permissions)
        
        def has_any_permission(self, permissions):
            """检查是否有任一权限"""
            return not self.permissions.isdisjoint(permissions)
        
        def get_permissions(self):
            """获取所有权限"""
            return self.permissions.copy()
        
        def clear_permissions(self):
            """清空所有权限"""
            self.permissions.clear()
            return self
    
    # 使用权限管理器
    user = UserPermissionManager()
    
    # 链式调用授予权限
    user.grant_permission("read").grant_permissions(["write", "execute"])
    print(f"用户权限: {user.get_permissions()}")
    
    # 检查权限
    print(f"有读权限: {user.has_permission('read')}")
    print(f"有管理员权限: {user.has_permission('admin')}")
    print(f"有所有基础权限: {user.has_all_permissions(['read', 'write'])}")
    print(f"有任一高级权限: {user.has_any_permission(['admin', 'delete'])}")
    
    # 撤销部分权限
    user.revoke_permission("execute")
    print(f"撤销执行权限后: {user.get_permissions()}")

def performance_comparison():
    """
    性能对比
    """
    print("\n性能对比")
    print("-" * 30)
    
    # 创建大型数据集
    large_set1 = set(range(100000))
    large_set2 = set(range(50000, 150000))
    
    # 测试不同操作的性能
    operations = [
        ("并集运算符 |", lambda: large_set1 | large_set2),
        ("并集方法 union()", lambda: large_set1.union(large_set2)),
        ("交集运算符 &", lambda: large_set1 & large_set2),
        ("交集方法 intersection()", lambda: large_set1.intersection(large_set2)),
        ("差集运算符 -", lambda: large_set1 - large_set2),
        ("差集方法 difference()", lambda: large_set1.difference(large_set2))
    ]
    
    for name, operation in operations:
        start_time = time.time()
        result = operation()
        end_time = time.time()
        print(f"{name}: {end_time - start_time:.6f}秒, 结果大小: {len(result)}")
    
    # 测试成员检查性能
    print("\n成员检查性能:")
    test_list = list(range(100000))
    test_set = set(range(100000))
    search_value = 99999
    
    # 列表查找
    start_time = time.time()
    result_list = search_value in test_list
    end_time = time.time()
    list_time = end_time - start_time
    
    # 集合查找
    start_time = time.time()
    result_set = search_value in test_set
    end_time = time.time()
    set_time = end_time - start_time
    
    print(f"列表查找时间: {list_time:.6f}秒")
    print(f"集合查找时间: {set_time:.6f}秒")
    print(f"集合比列表快: {list_time / set_time:.2f}倍")

def best_practices():
    """
    最佳实践
    """
    print("\n最佳实践")
    print("-" * 30)
    
    print("1. 选择合适的删除方法:")
    print("   - 确定元素存在时使用 remove()")
    print("   - 不确定元素是否存在时使用 discard()")
    print("   - 需要获取删除的元素时使用 pop()")
    
    print("\n2. 集合运算的选择:")
    print("   - 只操作集合时使用运算符 (|, &, -, ^)")
    print("   - 需要与其他可迭代对象运算时使用方法")
    print("   - 需要修改原集合时使用就地运算方法")
    
    print("\n3. 性能优化:")
    print("   - 大量成员检查操作时优先使用集合")
    print("   - 需要保持顺序时考虑使用其他数据结构")
    print("   - 频繁修改时考虑使用就地运算")
    
    # 实际示例
    print("\n实际应用示例:")
    
    # 错误的做法
    def bad_practice():
        result = set()
        for i in range(1000):
            temp_set = {i, i+1, i+2}
            result = result.union(temp_set)  # 每次创建新集合
        return result
    
    # 正确的做法
    def good_practice():
        result = set()
        for i in range(1000):
            temp_set = {i, i+1, i+2}
            result.update(temp_set)  # 就地更新
        return result
    
    # 性能对比
    start_time = time.time()
    bad_result = bad_practice()
    bad_time = time.time() - start_time
    
    start_time = time.time()
    good_result = good_practice()
    good_time = time.time() - start_time
    
    print(f"错误做法耗时: {bad_time:.6f}秒")
    print(f"正确做法耗时: {good_time:.6f}秒")
    print(f"性能提升: {bad_time / good_time:.2f}倍")

def practice_exercises():
    """
    练习题
    """
    print("\n练习题：")
    print("-" * 20)
    
    # 练习1：实现集合的自定义操作
    def custom_set_operations():
        print("1. 自定义集合操作:")
        
        def find_unique_elements(*sets):
            """找到只在一个集合中出现的元素"""
            all_elements = set()
            element_count = {}
            
            for s in sets:
                all_elements.update(s)
                for element in s:
                    element_count[element] = element_count.get(element, 0) + 1
            
            unique = {element for element, count in element_count.items() if count == 1}
            return unique
        
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        set3 = {5, 6, 7, 8}
        
        unique_elements = find_unique_elements(set1, set2, set3)
        print(f"集合1: {set1}")
        print(f"集合2: {set2}")
        print(f"集合3: {set3}")
        print(f"唯一元素: {unique_elements}")
    
    # 练习2：集合的动态管理
    def dynamic_set_management():
        print("\n2. 动态集合管理:")
        
        class DynamicSetManager:
            def __init__(self):
                self.sets = {}
            
            def create_set(self, name, initial_data=None):
                self.sets[name] = set(initial_data or [])
                return self
            
            def add_to_set(self, name, *elements):
                if name in self.sets:
                    for element in elements:
                        if isinstance(element, (list, tuple, set)):
                            self.sets[name].update(element)
                        else:
                            self.sets[name].add(element)
                return self
            
            def remove_from_set(self, name, *elements):
                if name in self.sets:
                    for element in elements:
                        self.sets[name].discard(element)
                return self
            
            def merge_sets(self, name1, name2, result_name):
                if name1 in self.sets and name2 in self.sets:
                    self.sets[result_name] = self.sets[name1].union(self.sets[name2])
                return self
            
            def get_set(self, name):
                return self.sets.get(name, set())
            
            def list_sets(self):
                return {name: s.copy() for name, s in self.sets.items()}
        
        # 使用动态集合管理器
        manager = DynamicSetManager()
        
        # 创建和操作集合
        manager.create_set("fruits", ["apple", "banana"]) \
               .create_set("colors", ["red", "green"]) \
               .add_to_set("fruits", "orange", ["grape", "kiwi"]) \
               .add_to_set("colors", "blue", "yellow") \
               .merge_sets("fruits", "colors", "mixed")
        
        all_sets = manager.list_sets()
        for name, s in all_sets.items():
            print(f"{name}: {s}")
    
    # 练习3：集合的统计分析
    def set_statistics():
        print("\n3. 集合统计分析:")
        
        # 模拟数据
        departments = {
            "IT": {"Alice", "Bob", "Charlie"},
            "HR": {"David", "Eve", "Frank"},
            "Finance": {"Grace", "Henry", "Alice"},  # Alice在多个部门
            "Marketing": {"Ivan", "Julia", "Bob"}   # Bob在多个部门
        }
        
        print("部门员工分布:")
        for dept, employees in departments.items():
            print(f"{dept}: {employees}")
        
        # 统计分析
        all_employees = set()
        for employees in departments.values():
            all_employees.update(employees)
        
        print(f"\n总员工数: {len(all_employees)}")
        
        # 找出在多个部门工作的员工
        multi_dept_employees = set()
        for employee in all_employees:
            dept_count = sum(1 for employees in departments.values() if employee in employees)
            if dept_count > 1:
                multi_dept_employees.add(employee)
        
        print(f"多部门员工: {multi_dept_employees}")
        
        # 部门间的员工重叠分析
        dept_names = list(departments.keys())
        for i in range(len(dept_names)):
            for j in range(i + 1, len(dept_names)):
                dept1, dept2 = dept_names[i], dept_names[j]
                overlap = departments[dept1] & departments[dept2]
                if overlap:
                    print(f"{dept1}和{dept2}的共同员工: {overlap}")
    
    custom_set_operations()
    dynamic_set_management()
    set_statistics()

if __name__ == "__main__":
    main()
    demonstrate_advanced_methods()
    demonstrate_method_combinations()
    performance_comparison()
    best_practices()
    practice_exercises()