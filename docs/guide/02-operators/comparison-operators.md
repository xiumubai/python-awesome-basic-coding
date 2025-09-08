# 比较运算符

## 学习目标

- 掌握所有比较运算符的使用方法
- 理解比较运算符的返回值（布尔类型）
- 学会不同数据类型之间的比较
- 了解比较运算符的链式使用
- 掌握比较运算符在实际编程中的应用

## 比较运算符概览

Python中的比较运算符用于比较两个值，返回布尔值（True或False）：

| 运算符 | 名称 | 示例 | 结果 |
|--------|------|------|------|
| == | 等于 | 5 == 5 | True |
| != | 不等于 | 5 != 3 | True |
| < | 小于 | 3 < 5 | True |
| > | 大于 | 5 > 3 | True |
| <= | 小于等于 | 3 <= 5 | True |
| >= | 大于等于 | 5 >= 5 | True |

## 基本比较运算

### 数值比较

```python
a = 10
b = 5
c = 10

print(f"等于 (a == b): {a} == {b} = {a == b}")        # False
print(f"等于 (a == c): {a} == {c} = {a == c}")        # True
print(f"不等于 (a != b): {a} != {b} = {a != b}")      # True
print(f"小于 (a < b): {a} < {b} = {a < b}")          # False
print(f"大于 (a > b): {a} > {b} = {a > b}")          # True
print(f"小于等于 (a <= c): {a} <= {c} = {a <= c}")    # True
print(f"大于等于 (a >= b): {a} >= {b} = {a >= b}")    # True
```

### 字符串比较

字符串按字典序（ASCII码）进行比较，区分大小写：

```python
str1 = "apple"
str2 = "banana"
str3 = "apple"

print(f"字符串相等: '{str1}' == '{str3}' = {str1 == str3}")  # True
print(f"字符串不等: '{str1}' != '{str2}' = {str1 != str2}")  # True
print(f"字典序比较: '{str1}' < '{str2}' = {str1 < str2}")    # True

# 大小写敏感
print(f"'Apple' == 'apple' = {'Apple' == 'apple'}")          # False
print(f"'Apple'.lower() == 'apple' = {'Apple'.lower() == 'apple'}")  # True
```

## 不同数据类型的比较

### 数字类型间比较

```python
int_num = 5
float_num = 5.0
complex_num = 5+0j

print(f"整数与浮点数: {int_num} == {float_num} = {int_num == float_num}")    # True
print(f"整数与复数: {int_num} == {complex_num} = {int_num == complex_num}")  # True
print(f"浮点数与复数: {float_num} == {complex_num} = {float_num == complex_num}")  # True
```

### 浮点数精度问题

```python
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")                           # 0.30000000000000004
print(f"0.1 + 0.2 == 0.3 = {result == 0.3}")            # False
print(f"abs((0.1 + 0.2) - 0.3) < 1e-10 = {abs(result - 0.3) < 1e-10}")  # True
```

### 容器类型比较

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
tuple1 = (1, 2, 3)

print(f"列表相等: {list1} == {list2} = {list1 == list2}")      # True
print(f"列表不等: {list1} == {list3} = {list1 == list3}")      # False
print(f"列表字典序: {list1} < {list3} = {list1 < list3}")      # True
print(f"列表与元组: {list1} == {tuple1} = {list1 == tuple1}")  # False
```

### 布尔值比较

```python
print(f"True == 1 = {True == 1}")      # True
print(f"False == 0 = {False == 0}")    # True
print(f"True > False = {True > False}") # True
```

### None值比较

```python
value1 = None
value2 = None
value3 = 0
value4 = ""

print(f"None == None = {value1 == value2}")  # True
print(f"None == 0 = {value1 == value3}")     # False
print(f"None == '' = {value1 == value4}")    # False
print(f"None is None = {value1 is value2}")  # True
```

## 链式比较

Python支持链式比较，可以简化复杂的条件判断：

```python
x = 5
print(f"1 < x < 10 = {1 < x < 10}")      # True
print(f"1 < x < 3 = {1 < x < 3}")        # False
print(f"0 <= x <= 10 = {0 <= x <= 10}")  # True

# 等价的非链式写法
print(f"(1 < x) and (x < 10) = {(1 < x) and (x < 10)}")  # True
```

## 实际应用示例

### 成绩等级判定

```python
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

scores = [95, 85, 75, 65, 55]
for score in scores:
    grade = get_grade(score)
    print(f"分数 {score}: 等级 {grade}")
```

### 年龄分组

```python
def age_group(age):
    if age < 13:
        return "儿童"
    elif 13 <= age < 20:
        return "青少年"
    elif 20 <= age < 60:
        return "成年人"
    else:
        return "老年人"

ages = [8, 16, 25, 65]
for age in ages:
    group = age_group(age)
    print(f"年龄 {age}: {group}")
```

### 范围判断函数

```python
def in_range(num, min_val, max_val):
    return min_val <= num <= max_val

test_num = 15
print(f"{test_num} 是否在 10-20 范围内？{in_range(test_num, 10, 20)}")
```

## 练习题

### 基础练习

判断以下表达式的结果：

```python
# 1. 10 > 5 and 3 < 7
# 2. 'hello' == 'Hello'
# 3. [1, 2] == [1, 2]
# 4. 5.0 == 5
# 5. 1 < 2 < 3 < 4

# 答案
print(f"1. 10 > 5 and 3 < 7 = {10 > 5 and 3 < 7}")        # True
print(f"2. 'hello' == 'Hello' = {'hello' == 'Hello'}")    # False
print(f"3. [1, 2] == [1, 2] = {[1, 2] == [1, 2]}")        # True
print(f"4. 5.0 == 5 = {5.0 == 5}")                        # True
print(f"5. 1 < 2 < 3 < 4 = {1 < 2 < 3 < 4}")              # True
```

### 编程练习

1. **字符串长度比较**

```python
def compare_string_length(str1, str2):
    len1, len2 = len(str1), len(str2)
    if len1 > len2:
        return f"'{str1}' 比 '{str2}' 长"
    elif len1 < len2:
        return f"'{str1}' 比 '{str2}' 短"
    else:
        return f"'{str1}' 和 '{str2}' 长度相同"

result = compare_string_length("hello", "world")
print(result)
```

2. **找最大值和最小值**

```python
def find_min_max(numbers):
    if not numbers:
        return None, None
    min_val = max_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

test_list = [3, 7, 1, 9, 4, 6]
min_val, max_val = find_min_max(test_list)
print(f"列表 {test_list} 中最小值: {min_val}, 最大值: {max_val}")
```

## 常见错误和注意事项

### 1. 浮点数比较精度问题

```python
# 错误的做法
if 0.1 + 0.2 == 0.3:
    print("相等")
else:
    print("不相等")  # 实际输出

# 正确的做法
if abs((0.1 + 0.2) - 0.3) < 1e-10:
    print("相等")
```

### 2. 字符串大小写敏感

```python
# 区分大小写
print("Apple" == "apple")  # False

# 忽略大小写比较
print("Apple".lower() == "apple".lower())  # True
```

### 3. 不同类型比较

```python
# 字符串和数字不能直接比较相等
print("5" == 5)        # False
print(int("5") == 5)   # True
print(str(5) == "5")   # True
```

## 学习要点总结

1. **比较运算符类型**：==、!=、<、>、<=、>=
2. **返回值**：所有比较运算符都返回布尔值（True或False）
3. **字符串比较**：按字典序比较，区分大小写
4. **数字类型**：不同数字类型可以直接比较
5. **链式比较**：可以简化复杂的条件判断
6. **浮点数精度**：比较浮点数时要注意精度问题
7. **实际应用**：广泛用于条件判断、数据筛选等场景

## 运行代码

```bash
cd 02-operators
python 02_comparison_operators.py
```

通过本节学习，你应该能够熟练使用各种比较运算符，理解不同数据类型的比较规则，并能在实际编程中正确应用这些知识。