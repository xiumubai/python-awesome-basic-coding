#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
集合的数学运算

本文件演示了Python中集合的数学运算：
1. 并集（Union）
2. 交集（Intersection）
3. 差集（Difference）
4. 对称差集（Symmetric Difference）
5. 运算符和方法的对比
6. 复合运算
7. 实际应用场景

作者：Python学习教程
日期：2024年
"""

def main():
    print("=" * 50)
    print("集合的数学运算演示")
    print("=" * 50)
    
    # 准备测试数据
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    set_c = {1, 3, 5, 7, 9}
    
    print(f"集合A: {set_a}")
    print(f"集合B: {set_b}")
    print(f"集合C: {set_c}")
    
    # 1. 并集（Union）- 包含两个集合中所有不重复的元素
    print("\n1. 并集运算（Union）")
    print("-" * 30)
    
    # 使用 | 操作符
    union_operator = set_a | set_b
    print(f"A | B = {union_operator}")
    
    # 使用 union() 方法
    union_method = set_a.union(set_b)
    print(f"A.union(B) = {union_method}")
    
    # 多个集合的并集
    union_multiple = set_a | set_b | set_c
    print(f"A | B | C = {union_multiple}")
    
    union_multiple_method = set_a.union(set_b, set_c)
    print(f"A.union(B, C) = {union_multiple_method}")
    
    # 与其他可迭代对象的并集
    union_with_list = set_a.union([10, 11, 12])
    print(f"A.union([10, 11, 12]) = {union_with_list}")
    
    # 2. 交集（Intersection）- 两个集合共有的元素
    print("\n2. 交集运算（Intersection）")
    print("-" * 30)
    
    # 使用 & 操作符
    intersection_operator = set_a & set_b
    print(f"A & B = {intersection_operator}")
    
    # 使用 intersection() 方法
    intersection_method = set_a.intersection(set_b)
    print(f"A.intersection(B) = {intersection_method}")
    
    # 多个集合的交集
    intersection_multiple = set_a & set_b & set_c
    print(f"A & B & C = {intersection_multiple}")
    
    intersection_multiple_method = set_a.intersection(set_b, set_c)
    print(f"A.intersection(B, C) = {intersection_multiple_method}")
    
    # 空交集示例
    set_d = {10, 11, 12}
    empty_intersection = set_a & set_d
    print(f"A & {{10, 11, 12}} = {empty_intersection}")
    
    # 3. 差集（Difference）- 在第一个集合但不在第二个集合中的元素
    print("\n3. 差集运算（Difference）")
    print("-" * 30)
    
    # 使用 - 操作符
    difference_operator = set_a - set_b
    print(f"A - B = {difference_operator}")
    print(f"B - A = {set_b - set_a}")
    
    # 使用 difference() 方法
    difference_method = set_a.difference(set_b)
    print(f"A.difference(B) = {difference_method}")
    
    # 多个集合的差集
    difference_multiple = set_a - set_b - set_c
    print(f"A - B - C = {difference_multiple}")
    
    difference_multiple_method = set_a.difference(set_b, set_c)
    print(f"A.difference(B, C) = {difference_multiple_method}")
    
    # 4. 对称差集（Symmetric Difference）- 在两个集合中但不在交集中的元素
    print("\n4. 对称差集运算（Symmetric Difference）")
    print("-" * 30)
    
    # 使用 ^ 操作符
    symmetric_diff_operator = set_a ^ set_b
    print(f"A ^ B = {symmetric_diff_operator}")
    
    # 使用 symmetric_difference() 方法
    symmetric_diff_method = set_a.symmetric_difference(set_b)
    print(f"A.symmetric_difference(B) = {symmetric_diff_method}")
    
    # 对称差集的性质：A ^ B = (A - B) | (B - A)
    manual_symmetric_diff = (set_a - set_b) | (set_b - set_a)
    print(f"(A - B) | (B - A) = {manual_symmetric_diff}")
    print(f"验证：A ^ B == (A - B) | (B - A): {symmetric_diff_operator == manual_symmetric_diff}")
    
    # 5. 运算符 vs 方法的区别
    print("\n5. 运算符 vs 方法的区别")
    print("-" * 30)
    
    # 运算符只能用于集合
    try:
        result = set_a | [1, 2, 3]  # 这会报错
    except TypeError as e:
        print(f"运算符与列表操作报错: {e}")
    
    # 方法可以接受任何可迭代对象
    result_method = set_a.union([1, 2, 3])
    print(f"方法可以接受列表: {result_method}")
    
    # 运算符创建新集合，方法也创建新集合
    original_a = set_a.copy()
    result_op = set_a | set_b
    result_method = set_a.union(set_b)
    print(f"原集合是否改变: {set_a == original_a}")
    
    # 6. 就地运算（修改原集合）
    print("\n6. 就地运算（修改原集合）")
    print("-" * 30)
    
    # 就地并集
    test_set = {1, 2, 3}
    print(f"原集合: {test_set}")
    test_set |= {4, 5, 6}
    print(f"就地并集后: {test_set}")
    
    # 使用update()方法（等同于|=）
    test_set.update({7, 8})
    print(f"使用update()后: {test_set}")
    
    # 就地交集
    test_set &= {1, 2, 3, 4, 5}
    print(f"就地交集后: {test_set}")
    
    # 使用intersection_update()方法
    test_set.intersection_update({1, 2, 3})
    print(f"使用intersection_update()后: {test_set}")
    
    # 就地差集
    test_set -= {2}
    print(f"就地差集后: {test_set}")
    
    # 使用difference_update()方法
    test_set.difference_update({3})
    print(f"使用difference_update()后: {test_set}")
    
    # 就地对称差集
    test_set ^= {1, 5, 6}
    print(f"就地对称差集后: {test_set}")
    
    # 使用symmetric_difference_update()方法
    test_set.symmetric_difference_update({5, 7})
    print(f"使用symmetric_difference_update()后: {test_set}")
    
    print("\n=" * 50)
    print("集合数学运算演示完成！")
    print("=" * 50)

def demonstrate_complex_operations():
    """
    演示复杂的集合运算
    """
    print("\n复杂集合运算演示")
    print("-" * 30)
    
    # 多个集合的复合运算
    students_math = {"Alice", "Bob", "Charlie", "David"}
    students_physics = {"Bob", "Charlie", "Eve", "Frank"}
    students_chemistry = {"Alice", "Charlie", "Frank", "Grace"}
    
    print(f"数学课学生: {students_math}")
    print(f"物理课学生: {students_physics}")
    print(f"化学课学生: {students_chemistry}")
    
    # 至少选修一门课的学生
    all_students = students_math | students_physics | students_chemistry
    print(f"\n至少选修一门课的学生: {all_students}")
    
    # 三门课都选修的学生
    all_three = students_math & students_physics & students_chemistry
    print(f"三门课都选修的学生: {all_three}")
    
    # 只选修数学课的学生
    only_math = students_math - students_physics - students_chemistry
    print(f"只选修数学课的学生: {only_math}")
    
    # 选修数学和物理但不选化学的学生
    math_physics_not_chemistry = (students_math & students_physics) - students_chemistry
    print(f"选修数学和物理但不选化学的学生: {math_physics_not_chemistry}")
    
    # 恰好选修两门课的学生
    exactly_two = ((students_math & students_physics) - students_chemistry) | \
                  ((students_math & students_chemistry) - students_physics) | \
                  ((students_physics & students_chemistry) - students_math)
    print(f"恰好选修两门课的学生: {exactly_two}")

def demonstrate_set_properties():
    """
    演示集合运算的数学性质
    """
    print("\n集合运算的数学性质")
    print("-" * 30)
    
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    C = {5, 6, 7, 8}
    
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")
    
    # 交换律
    print(f"\n交换律:")
    print(f"A | B = {A | B}")
    print(f"B | A = {B | A}")
    print(f"并集交换律成立: {A | B == B | A}")
    
    print(f"A & B = {A & B}")
    print(f"B & A = {B & A}")
    print(f"交集交换律成立: {A & B == B & A}")
    
    # 结合律
    print(f"\n结合律:")
    print(f"(A | B) | C = {(A | B) | C}")
    print(f"A | (B | C) = {A | (B | C)}")
    print(f"并集结合律成立: {(A | B) | C == A | (B | C)}")
    
    # 分配律
    print(f"\n分配律:")
    print(f"A & (B | C) = {A & (B | C)}")
    print(f"(A & B) | (A & C) = {(A & B) | (A & C)}")
    print(f"交集对并集的分配律成立: {A & (B | C) == (A & B) | (A & C)}")
    
    # 德摩根定律（需要全集概念，这里用示例说明）
    U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # 假设的全集
    print(f"\n德摩根定律示例（假设全集U = {U}）:")
    complement_A = U - A
    complement_B = U - B
    complement_union = U - (A | B)
    intersection_complements = complement_A & complement_B
    
    print(f"A的补集: {complement_A}")
    print(f"B的补集: {complement_B}")
    print(f"(A | B)的补集: {complement_union}")
    print(f"A补集 & B补集: {intersection_complements}")
    print(f"德摩根定律成立: {complement_union == intersection_complements}")

def practical_applications():
    """
    实际应用场景
    """
    print("\n实际应用场景")
    print("-" * 30)
    
    # 应用1：权限管理
    admin_permissions = {"read", "write", "delete", "admin"}
    user_permissions = {"read", "write"}
    guest_permissions = {"read"}
    
    print("权限管理系统:")
    print(f"管理员权限: {admin_permissions}")
    print(f"用户权限: {user_permissions}")
    print(f"访客权限: {guest_permissions}")
    
    # 检查用户缺少的权限
    missing_permissions = admin_permissions - user_permissions
    print(f"用户缺少的权限: {missing_permissions}")
    
    # 检查共同权限
    common_permissions = user_permissions & guest_permissions
    print(f"用户和访客的共同权限: {common_permissions}")
    
    # 应用2：数据分析
    print("\n数据分析应用:")
    customers_2023 = {"Alice", "Bob", "Charlie", "David", "Eve"}
    customers_2024 = {"Bob", "Charlie", "Frank", "Grace", "Henry"}
    
    print(f"2023年客户: {customers_2023}")
    print(f"2024年客户: {customers_2024}")
    
    # 老客户（两年都有）
    returning_customers = customers_2023 & customers_2024
    print(f"回头客户: {returning_customers}")
    
    # 流失客户（2023有但2024没有）
    lost_customers = customers_2023 - customers_2024
    print(f"流失客户: {lost_customers}")
    
    # 新客户（2024有但2023没有）
    new_customers = customers_2024 - customers_2023
    print(f"新客户: {new_customers}")
    
    # 总客户数
    total_customers = customers_2023 | customers_2024
    print(f"总客户数: {len(total_customers)}")
    
    # 应用3：标签系统
    print("\n标签系统应用:")
    article1_tags = {"python", "programming", "tutorial", "beginner"}
    article2_tags = {"python", "web", "django", "advanced"}
    article3_tags = {"javascript", "web", "frontend", "tutorial"}
    
    print(f"文章1标签: {article1_tags}")
    print(f"文章2标签: {article2_tags}")
    print(f"文章3标签: {article3_tags}")
    
    # 找到所有标签
    all_tags = article1_tags | article2_tags | article3_tags
    print(f"所有标签: {all_tags}")
    
    # 找到共同标签
    common_tags = article1_tags & article2_tags & article3_tags
    print(f"三篇文章的共同标签: {common_tags}")
    
    # 找到Python相关文章的标签
    python_articles_tags = article1_tags | article2_tags
    print(f"Python相关文章的所有标签: {python_articles_tags}")
    
    # 找到Web相关但不是Python的标签
    web_not_python_tags = (article2_tags | article3_tags) - article1_tags
    print(f"Web相关但不是Python的标签: {web_not_python_tags}")

def practice_exercises():
    """
    练习题
    """
    print("\n练习题：")
    print("-" * 20)
    
    # 练习1：学生选课分析
    math_students = {"张三", "李四", "王五", "赵六", "钱七"}
    english_students = {"李四", "王五", "孙八", "周九", "吴十"}
    physics_students = {"张三", "王五", "赵六", "孙八", "郑十一"}
    
    print("1. 学生选课分析:")
    print(f"数学课学生: {math_students}")
    print(f"英语课学生: {english_students}")
    print(f"物理课学生: {physics_students}")
    
    # 分析结果
    all_subjects = math_students | english_students | physics_students
    print(f"选课学生总数: {len(all_subjects)}")
    
    math_english = math_students & english_students
    print(f"同时选数学和英语的学生: {math_english}")
    
    all_three_subjects = math_students & english_students & physics_students
    print(f"三门课都选的学生: {all_three_subjects}")
    
    only_math = math_students - english_students - physics_students
    print(f"只选数学的学生: {only_math}")
    
    # 练习2：网站用户行为分析
    visited_homepage = {"user1", "user2", "user3", "user4", "user5"}
    visited_product = {"user2", "user3", "user6", "user7", "user8"}
    made_purchase = {"user3", "user4", "user9", "user10"}
    
    print("\n2. 网站用户行为分析:")
    print(f"访问首页用户: {visited_homepage}")
    print(f"访问产品页用户: {visited_product}")
    print(f"购买用户: {made_purchase}")
    
    # 转化分析
    homepage_to_product = visited_homepage & visited_product
    print(f"从首页到产品页的用户: {homepage_to_product}")
    
    product_to_purchase = visited_product & made_purchase
    print(f"从产品页到购买的用户: {product_to_purchase}")
    
    full_funnel = visited_homepage & visited_product & made_purchase
    print(f"完整转化路径的用户: {full_funnel}")
    
    bounce_users = visited_homepage - visited_product
    print(f"只访问首页就离开的用户: {bounce_users}")

if __name__ == "__main__":
    main()
    demonstrate_complex_operations()
    demonstrate_set_properties()
    practical_applications()
    practice_exercises()