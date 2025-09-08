# 集合的基本操作

## 学习目标

通过本节学习，你将掌握：
- 集合元素的添加操作（add、update）
- 集合元素的删除操作（remove、discard、pop、clear）
- 元素存在性检查
- 集合长度和判空操作
- 集合的复制方法
- 集合的比较操作
- 实际应用场景和最佳实践

## 集合操作概述

集合提供了丰富的操作方法，这些操作可以分为以下几类：
- **修改操作**：添加、删除、清空元素
- **查询操作**：检查元素存在性、获取长度
- **比较操作**：相等性、子集、超集关系
- **复制操作**：创建集合的副本

## 1. 添加元素

### 使用 add() 方法添加单个元素

```python
# 创建初始集合
fruits = {"apple", "banana"}
print(f"初始集合: {fruits}")

# 添加新元素
fruits.add("orange")
print(f"添加'orange'后: {fruits}")

# 尝试添加已存在的元素
fruits.add("apple")
print(f"尝试添加已存在的'apple': {fruits}")
print("注意：添加已存在的元素不会改变集合")
```

**输出结果：**
```
初始集合: {'banana', 'apple'}
添加'orange'后: {'banana', 'orange', 'apple'}
尝试添加已存在的'apple': {'banana', 'orange', 'apple'}
注意：添加已存在的元素不会改变集合
```

### 使用 update() 方法添加多个元素

```python
# 从列表添加多个元素
fruits = {"apple", "banana"}
fruits.update(["grape", "kiwi"])
print(f"添加列表元素后: {fruits}")

# 从集合添加元素
fruits.update({"mango", "pear"})
print(f"添加集合元素后: {fruits}")

# 从字符串添加元素（注意：字符串会被拆分）
fruits.update("cherry")
print(f"添加字符串'cherry'后: {fruits}")
print("注意：字符串被拆分为单个字符添加")

# 同时从多个可迭代对象添加
base_set = {1, 2, 3}
base_set.update([4, 5], {6, 7}, (8, 9))
print(f"批量添加后: {base_set}")
```

**输出结果：**
```
添加列表元素后: {'grape', 'kiwi', 'banana', 'apple'}
添加集合元素后: {'grape', 'kiwi', 'mango', 'pear', 'banana', 'apple'}
添加字符串'cherry'后: {'grape', 'kiwi', 'mango', 'pear', 'banana', 'apple', 'c', 'h', 'e', 'r', 'y'}
注意：字符串被拆分为单个字符添加

批量添加后: {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

## 2. 删除元素

### remove() 方法：删除指定元素

```python
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f"初始数字集合: {numbers}")

# 删除存在的元素
numbers.remove(5)
print(f"删除5后: {numbers}")

# 尝试删除不存在的元素会报错
try:
    numbers.remove(15)  # 不存在的元素
except KeyError as e:
    print(f"使用remove()删除不存在的元素会报错: {e}")
```

**输出结果：**
```
初始数字集合: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
删除5后: {1, 2, 3, 4, 6, 7, 8, 9, 10}
使用remove()删除不存在的元素会报错: 15
```

### discard() 方法：安全删除元素（推荐）

```python
numbers = {1, 2, 3, 4, 6, 7, 8, 9, 10}
print(f"初始集合: {numbers}")

# 删除存在的元素
numbers.discard(3)
print(f"使用discard()删除3后: {numbers}")

# 删除不存在的元素不会报错
numbers.discard(15)
print(f"使用discard()删除不存在的元素15: {numbers}")
print("注意：discard()删除不存在的元素不会报错")
```

**输出结果：**
```
初始集合: {1, 2, 4, 6, 7, 8, 9, 10}
使用discard()删除3后: {1, 2, 4, 6, 7, 8, 9, 10}
使用discard()删除不存在的元素15: {1, 2, 4, 6, 7, 8, 9, 10}
注意：discard()删除不存在的元素不会报错
```

### pop() 方法：随机删除并返回元素

```python
numbers = {1, 2, 4, 6, 7, 8, 9, 10}
print(f"删除前: {numbers}")

# 随机删除一个元素
removed_element = numbers.pop()
print(f"pop()返回的元素: {removed_element}")
print(f"删除后: {numbers}")

# 从空集合pop会报错
empty_set = set()
try:
    empty_set.pop()
except KeyError as e:
    print(f"从空集合pop会报错: 'pop from an empty set'")
```

**输出结果：**
```
删除前: {1, 2, 4, 6, 7, 8, 9, 10}
pop()返回的元素: 1
删除后: {2, 4, 6, 7, 8, 9, 10}
从空集合pop会报错: 'pop from an empty set'
```

### clear() 方法：清空集合

```python
test_set = {1, 2, 3}
print(f"清空前: {test_set}")
test_set.clear()
print(f"清空后: {test_set}")
print(f"清空后的类型: {type(test_set)}")
```

**输出结果：**
```
清空前: {1, 2, 3}
清空后: set()
清空后的类型: <class 'set'>
```

## 3. 检查元素存在性

### 使用 in 和 not in 操作符

```python
colors = {"red", "green", "blue", "yellow"}
print(f"颜色集合: {colors}")

# 检查元素是否存在
print(f"'red' in colors: {'red' in colors}")
print(f"'purple' in colors: {'purple' in colors}")
print(f"'purple' not in colors: {'purple' not in colors}")

# 实际应用：权限检查
user_permissions = {"read", "write", "execute"}
required_permission = "admin"

if required_permission in user_permissions:
    print(f"用户具有{required_permission}权限")
else:
    print(f"用户没有{required_permission}权限")
```

**输出结果：**
```
颜色集合: {'yellow', 'green', 'blue', 'red'}
'red' in colors: True
'purple' in colors: False
'purple' not in colors: True
用户没有admin权限
```

## 4. 集合长度和判空

### 获取集合长度

```python
sample_set = {"a", "b", "c", "d", "e"}
print(f"集合: {sample_set}")
print(f"集合长度: {len(sample_set)}")

# 空集合的长度
empty_set = set()
print(f"空集合: {empty_set}")
print(f"空集合长度: {len(empty_set)}")
```

### 判断集合是否为空

```python
empty_set = set()
non_empty_set = {1, 2, 3}

# 方法1：使用len()
print(f"空集合是否为空: {len(empty_set) == 0}")
print(f"非空集合是否为空: {len(non_empty_set) == 0}")

# 方法2：使用bool()（推荐）
print(f"使用bool()判断空集合: {bool(empty_set)}")
print(f"使用bool()判断非空集合: {bool(non_empty_set)}")

# 方法3：直接在条件语句中使用
if empty_set:
    print("集合不为空")
else:
    print("集合为空")
```

**输出结果：**
```
集合: {'a', 'b', 'c', 'd', 'e'}
集合长度: 5

空集合: set()
空集合长度: 0

空集合是否为空: True
非空集合是否为空: False
使用bool()判断空集合: False
使用bool()判断非空集合: True
集合为空
```

## 5. 集合的复制

### 浅复制方法

```python
original = {1, 2, 3, 4, 5}
print(f"原始集合: {original}")

# 方法1：使用copy()方法
copy1 = original.copy()
print(f"使用copy()复制: {copy1}")

# 方法2：使用set()构造函数
copy2 = set(original)
print(f"使用set()复制: {copy2}")

# 验证是不同的对象
print(f"original is copy1: {original is copy1}")
print(f"original == copy1: {original == copy1}")

# 修改原集合不影响复制的集合
original.add(6)
print(f"\n修改原集合后:")
print(f"原始集合: {original}")
print(f"复制的集合: {copy1}")
```

**输出结果：**
```
原始集合: {1, 2, 3, 4, 5}
使用copy()复制: {1, 2, 3, 4, 5}
使用set()复制: {1, 2, 3, 4, 5}
original is copy1: False
original == copy1: True

修改原集合后:
原始集合: {1, 2, 3, 4, 5, 6}
复制的集合: {1, 2, 3, 4, 5}
```

## 6. 集合的比较

### 相等性比较

```python
set1 = {1, 2, 3}
set2 = {3, 2, 1}  # 顺序不同但元素相同
set3 = {1, 2, 3, 4}
set4 = {1, 2}

print(f"集合1: {set1}")
print(f"集合2: {set2}")
print(f"集合3: {set3}")
print(f"集合4: {set4}")

# 相等比较（顺序无关）
print(f"\nset1 == set2: {set1 == set2}")
print(f"set1 == set3: {set1 == set3}")
```

### 子集和超集关系

```python
# 子集检查
print(f"\nset4 是 set1 的子集: {set4.issubset(set1)}")
print(f"set1 是 set3 的子集: {set1.issubset(set3)}")

# 超集检查
print(f"set1 是 set4 的超集: {set1.issuperset(set4)}")
print(f"set3 是 set1 的超集: {set3.issuperset(set1)}")

# 真子集和真超集
print(f"\nset4 是 set1 的真子集: {set4 < set1}")
print(f"set1 是 set1 的真子集: {set1 < set1}")
print(f"set1 是 set4 的真超集: {set1 > set4}")
```

### 不相交集合

```python
set5 = {7, 8, 9}
print(f"\nset1 和 set5 是否不相交: {set1.isdisjoint(set5)}")
print(f"set1 和 set3 是否不相交: {set1.isdisjoint(set3)}")
```

**输出结果：**
```
集合1: {1, 2, 3}
集合2: {1, 2, 3}
集合3: {1, 2, 3, 4}
集合4: {1, 2}

set1 == set2: True
set1 == set3: False

set4 是 set1 的子集: True
set1 是 set3 的子集: True
set1 是 set4 的超集: True
set3 是 set1 的超集: True

set4 是 set1 的真子集: True
set1 是 set1 的真子集: False
set1 是 set4 的真超集: True

set1 和 set5 是否不相交: True
set1 和 set3 是否不相交: False
```

## 实际应用示例

### 用户标签管理系统

```python
# 用户标签管理
user_tags = {"python", "programming", "beginner"}
print(f"用户标签: {user_tags}")

# 添加新标签（自动去重）
new_tags = ["web", "django", "python"]  # python重复
user_tags.update(new_tags)
print(f"添加新标签后: {user_tags}")

# 删除过时标签
outdated_tags = {"beginner"}
user_tags -= outdated_tags  # 使用差集操作
print(f"删除过时标签后: {user_tags}")
```

### 在线用户管理

```python
# 在线用户管理系统
online_users = set()

def user_login(username):
    online_users.add(username)
    print(f"用户 {username} 上线，当前在线用户: {online_users}")

def user_logout(username):
    online_users.discard(username)  # 使用discard避免KeyError
    print(f"用户 {username} 下线，当前在线用户: {online_users}")

# 模拟用户操作
user_login("Alice")
user_login("Bob")
user_login("Charlie")
user_logout("Bob")
user_logout("David")  # 不存在的用户，不会报错

print(f"最终在线用户: {online_users}")
```

### 购物车系统

```python
# 简单的购物车实现
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

# 使用示例
print(add_to_cart("苹果"))
print(add_to_cart("香蕉"))
print(add_to_cart("苹果"))  # 重复添加
print(show_cart())
print(remove_from_cart("香蕉"))
print(remove_from_cart("橙子"))  # 不存在的商品
print(show_cart())
```

## 性能优化技巧

### 批量操作vs单个操作

```python
import time

# 方法1：单个添加（较慢）
start_time = time.time()
set1 = set()
for i in range(10000):
    set1.add(i)
time1 = time.time() - start_time

# 方法2：批量添加（较快）
start_time = time.time()
set2 = set(range(10000))
time2 = time.time() - start_time

print(f"单个添加耗时: {time1:.4f}秒")
print(f"批量添加耗时: {time2:.4f}秒")
print(f"批量操作快 {time1/time2:.2f} 倍")
```

### 条件删除

```python
# 删除满足条件的元素
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f"原始数字集合: {numbers}")

# 方法1：创建新集合（推荐）
odd_numbers = {x for x in numbers if x % 2 == 1}
print(f"奇数集合: {odd_numbers}")

# 方法2：使用差集操作
even_numbers = {x for x in numbers if x % 2 == 0}
numbers_copy = numbers.copy()
numbers_copy -= even_numbers
print(f"删除偶数后: {numbers_copy}")
```

## 运行完整代码

你可以运行以下完整代码来查看所有示例：

```bash
python3 02_set_operations.py
```

## 学习要点

1. **添加操作**：
   - `add()`: 添加单个元素
   - `update()`: 添加多个元素，可接受多种可迭代对象

2. **删除操作**：
   - `remove()`: 删除指定元素，元素不存在会报错
   - `discard()`: 安全删除，元素不存在不报错（推荐）
   - `pop()`: 随机删除并返回元素
   - `clear()`: 清空集合

3. **查询操作**：
   - `in` / `not in`: 检查元素存在性
   - `len()`: 获取集合长度
   - `bool()`: 判断集合是否为空

4. **比较操作**：
   - `==` / `!=`: 相等性比较
   - `issubset()` / `<=`: 子集检查
   - `issuperset()` / `>=`: 超集检查
   - `isdisjoint()`: 不相交检查

5. **最佳实践**：
   - 优先使用 `discard()` 而不是 `remove()`
   - 使用 `update()` 进行批量添加
   - 利用集合的自动去重特性
   - 在条件语句中直接使用集合判断是否为空

## 注意事项

- 集合是可变的，操作会直接修改原集合
- `pop()` 的结果是不可预测的，因为集合是无序的
- 空集合的 `pop()` 操作会抛出 `KeyError`
- 集合的比较是基于元素内容，与顺序无关
- 使用 `copy()` 创建浅复制，修改原集合不影响副本

通过掌握这些基本操作，你就可以高效地使用集合来处理各种数据操作需求了。