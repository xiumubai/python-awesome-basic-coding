# 文件输出操作

## 概述

文件输出是Python编程中的重要技能，涉及将数据写入到文件中。本章将详细介绍Python中各种文件输出方法，包括基本写入、格式化输出、特殊格式文件处理、安全写入等内容。

## 学习目标

- 掌握Python文件写入的基本方法
- 理解不同文件打开模式的区别和应用场景
- 学会处理各种格式的文件输出（文本、JSON、CSV等）
- 掌握安全文件写入的最佳实践
- 了解批量文件操作和性能优化技巧

## 完整代码

```python
"""
文件输出操作学习

学习目标：
1. 掌握基本文件写入操作
2. 理解不同文件打开模式
3. 学会格式化输出到文件
4. 掌握JSON和CSV文件写入
5. 了解安全文件写入方法
6. 学会批量文件操作

重点内容：
- write()和writelines()方法
- 文件打开模式：'w', 'a', 'x', 'wb'
- print()函数输出到文件
- JSON和CSV文件处理
- 异常处理和安全写入
- 原子性写入和备份机制
"""

import os
import json
import csv
import datetime

# 创建输出目录
output_dir = "output_examples"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"已创建输出目录：{output_dir}")

# ============================================================================
# 1. 基本文件写入操作
# ============================================================================

print("=" * 50)
print("1. 基本文件写入操作")
print("=" * 50)

print("\n--- write()方法 ---")

# 使用write()方法写入单个字符串
with open(f"{output_dir}/basic_write.txt", 'w', encoding='utf-8') as f:
    f.write("这是第一行文本\n")
    f.write("这是第二行文本\n")
    f.write("这是第三行文本")

print("已使用write()方法写入文件")

print("\n--- writelines()方法 ---")

# 使用writelines()方法写入字符串列表
lines = [
    "第一行内容\n",
    "第二行内容\n",
    "第三行内容\n",
    "第四行内容"
]

with open(f"{output_dir}/writelines_demo.txt", 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("已使用writelines()方法写入文件")

# 注意：writelines()不会自动添加换行符
print("\n--- writelines()注意事项 ---")

# 错误示例：没有换行符
wrong_lines = ["第一行", "第二行", "第三行"]
with open(f"{output_dir}/wrong_lines.txt", 'w', encoding='utf-8') as f:
    f.writelines(wrong_lines)

# 正确示例：手动添加换行符
correct_lines = [line + "\n" for line in ["第一行", "第二行", "第三行"]]
with open(f"{output_dir}/correct_lines.txt", 'w', encoding='utf-8') as f:
    f.writelines(correct_lines)

print("演示了writelines()的正确和错误用法")

# ============================================================================
# 2. 文件打开模式
# ============================================================================

print("\n" + "=" * 50)
print("2. 文件打开模式")
print("=" * 50)

print("\n--- 'w'模式（写入/覆盖） ---")

# 创建初始文件
with open(f"{output_dir}/mode_test.txt", 'w', encoding='utf-8') as f:
    f.write("初始内容\n第二行\n")

print("已创建初始文件")

# 使用'w'模式会覆盖原内容
with open(f"{output_dir}/mode_test.txt", 'w', encoding='utf-8') as f:
    f.write("新内容（覆盖了原内容）\n")

print("使用'w'模式覆盖了原内容")

print("\n--- 'a'模式（追加） ---")

# 使用'a'模式追加内容
with open(f"{output_dir}/mode_test.txt", 'a', encoding='utf-8') as f:
    f.write("追加的第一行\n")
    f.write("追加的第二行\n")

print("使用'a'模式追加了内容")

print("\n--- 'x'模式（独占创建） ---")

# 'x'模式只能创建新文件，如果文件存在会报错
try:
    with open(f"{output_dir}/exclusive_file.txt", 'x', encoding='utf-8') as f:
        f.write("这是独占创建的文件\n")
    print("成功使用'x'模式创建文件")
except FileExistsError:
    print("文件已存在，'x'模式创建失败")

# 再次尝试创建同名文件
try:
    with open(f"{output_dir}/exclusive_file.txt", 'x', encoding='utf-8') as f:
        f.write("尝试再次创建\n")
except FileExistsError:
    print("文件已存在，'x'模式创建失败（符合预期）")

# ============================================================================
# 3. 二进制文件写入
# ============================================================================

print("\n" + "=" * 50)
print("3. 二进制文件写入")
print("=" * 50)

print("\n--- 二进制模式写入 ---")

# 写入二进制数据
binary_data = b"\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64"  # "Hello World"

with open(f"{output_dir}/binary_file.bin", 'wb') as f:
    f.write(binary_data)

print("已写入二进制文件")

# 写入字节数组
text = "你好，世界！"
text_bytes = text.encode('utf-8')

with open(f"{output_dir}/text_as_binary.bin", 'wb') as f:
    f.write(text_bytes)

print("已将文本转换为字节写入二进制文件")

# 验证二进制文件
with open(f"{output_dir}/text_as_binary.bin", 'rb') as f:
    read_bytes = f.read()
    decoded_text = read_bytes.decode('utf-8')
    print(f"从二进制文件读取的文本：{decoded_text}")

# ============================================================================
# 4. 格式化输出到文件
# ============================================================================

print("\n" + "=" * 50)
print("4. 格式化输出到文件")
print("=" * 50)

print("\n--- 使用print()函数输出到文件 ---")

# 使用print()函数的file参数
with open(f"{output_dir}/print_output.txt", 'w', encoding='utf-8') as f:
    print("这是使用print()函数写入的内容", file=f)
    print("可以使用print()的所有参数", file=f)
    print("数字：", 42, "字符串：", "Hello", file=f)
    print("分隔符测试", "用逗号分隔", sep=" | ", file=f)
    print("结束符测试", end=" [结束]\n", file=f)

print("已使用print()函数写入文件")

print("\n--- 格式化字符串写入 ---")

# 准备数据
students = [
    {"name": "张三", "age": 20, "score": 85.5},
    {"name": "李四", "age": 21, "score": 92.0},
    {"name": "王五", "age": 19, "score": 78.5}
]

# 使用格式化字符串写入
with open(f"{output_dir}/formatted_output.txt", 'w', encoding='utf-8') as f:
    f.write("学生成绩单\n")
    f.write("=" * 30 + "\n")
    f.write(f"{'姓名':<8} {'年龄':<6} {'成绩':<8}\n")
    f.write("-" * 30 + "\n")
    
    for student in students:
        line = f"{student['name']:<8} {student['age']:<6} {student['score']:<8.1f}\n"
        f.write(line)
    
    f.write("-" * 30 + "\n")
    avg_score = sum(s['score'] for s in students) / len(students)
    f.write(f"平均分：{avg_score:.1f}\n")

print("已创建格式化输出文件")

# 验证内容
with open(f"{output_dir}/formatted_output.txt", 'r', encoding='utf-8') as f:
    print(f"文件内容：\n{f.read()}")

# ============================================================================
# 5. JSON文件写入
# ============================================================================

print("\n" + "=" * 50)
print("5. JSON文件写入")
print("=" * 50)

# 创建JSON数据
data = {
    "应用信息": {
        "名称": "学生管理系统",
        "版本": "1.0.0",
        "作者": "Python学习者"
    },
    "学生列表": [
        {
            "id": 1,
            "姓名": "张三",
            "年龄": 20,
            "成绩": [85, 92, 78],
            "信息": {
                "城市": "北京",
                "邮箱": "zhangsan@example.com"
            }
        },
        {
            "id": 2,
            "姓名": "李四",
            "年龄": 21,
            "成绩": [92, 88, 95],
            "信息": {
                "城市": "上海",
                "邮箱": "lisi@example.com"
            }
        }
    ],
    "统计信息": {
        "总人数": 2,
        "创建时间": datetime.datetime.now().isoformat()
    }
}

print("\n--- JSON文件写入 ---")

# 写入JSON文件（紧凑格式）
with open(f"{output_dir}/data_compact.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

print("已创建紧凑格式JSON文件")

# 写入JSON文件（格式化）
with open(f"{output_dir}/data_formatted.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)

print("已创建格式化JSON文件")

# 验证JSON文件
with open(f"{output_dir}/data_formatted.json", 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
    print(f"JSON数据验证成功，学生数量：{len(loaded_data['学生列表'])}")

# ============================================================================
# 6. CSV文件写入
# ============================================================================

print("\n" + "=" * 50)
print("6. CSV文件写入")
print("=" * 50)

# 准备CSV数据
csv_data = [
    ['姓名', '年龄', '城市', '数学', '英语', '科学'],
    ['张三', 20, '北京', 85, 92, 78],
    ['李四', 21, '上海', 92, 88, 95],
    ['王五', 19, '广州', 78, 85, 82],
    ['赵六', 22, '深圳', 95, 90, 88]
]

print("\n--- CSV文件写入 ---")

# 使用csv.writer写入
with open(f"{output_dir}/students.csv", 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)

print("已创建CSV文件（使用writer）")

# 使用csv.DictWriter写入
dict_data = [
    {'姓名': '张三', '年龄': 20, '城市': '北京', '数学': 85, '英语': 92, '科学': 78},
    {'姓名': '李四', '年龄': 21, '城市': '上海', '数学': 92, '英语': 88, '科学': 95},
    {'姓名': '王五', '年龄': 19, '城市': '广州', '数学': 78, '英语': 85, '科学': 82},
    {'姓名': '赵六', '年龄': 22, '城市': '深圳', '数学': 95, '英语': 90, '科学': 88}
]

with open(f"{output_dir}/students_dict.csv", 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['姓名', '年龄', '城市', '数学', '英语', '科学']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # 写入表头
    writer.writerows(dict_data)

print("已创建CSV文件（使用DictWriter）")

# 验证CSV文件
with open(f"{output_dir}/students.csv", 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)
    print(f"CSV验证：{len(rows)}行数据（包含表头）")

# ============================================================================
# 7. 安全文件写入
# ============================================================================

print("\n" + "=" * 50)
print("7. 安全文件写入")
print("=" * 50)

def safe_write_file(filename, content, encoding='utf-8', backup=True):
    """
    安全写入文件的函数
    """
    try:
        # 如果需要备份且文件存在
        if backup and os.path.exists(filename):
            backup_name = f"{filename}.backup"
            with open(filename, 'r', encoding=encoding) as src:
                with open(backup_name, 'w', encoding=encoding) as dst:
                    dst.write(src.read())
            print(f"已创建备份文件：{backup_name}")
        
        # 写入新内容
        with open(filename, 'w', encoding=encoding) as f:
            f.write(content)
        
        print(f"成功写入文件：{filename}")
        return True
        
    except PermissionError:
        print(f"错误：没有权限写入文件 '{filename}'")
        return False
    except OSError as e:
        print(f"错误：写入文件时发生系统错误 - {e}")
        return False
    except Exception as e:
        print(f"未知错误：{e}")
        return False

def atomic_write_file(filename, content, encoding='utf-8'):
    """
    原子性写入文件（先写临时文件，再重命名）
    """
    temp_filename = f"{filename}.tmp"
    try:
        # 写入临时文件
        with open(temp_filename, 'w', encoding=encoding) as f:
            f.write(content)
        
        # 原子性重命名
        os.rename(temp_filename, filename)
        print(f"原子性写入成功：{filename}")
        return True
        
    except Exception as e:
        # 清理临时文件
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
        print(f"原子性写入失败：{e}")
        return False

print("\n--- 安全写入演示 ---")

# 创建测试文件
test_content = "这是原始内容\n第二行内容\n"
with open(f"{output_dir}/test_safe.txt", 'w', encoding='utf-8') as f:
    f.write(test_content)

print("已创建测试文件")

# 安全写入（带备份）
new_content = "这是新的内容\n已替换原始内容\n"
safe_write_file(f"{output_dir}/test_safe.txt", new_content)

# 原子性写入
atomic_content = "这是原子性写入的内容\n保证数据完整性\n"
atomic_write_file(f"{output_dir}/atomic_test.txt", atomic_content)

# ============================================================================
# 8. 批量文件操作
# ============================================================================

print("\n" + "=" * 50)
print("8. 批量文件操作")
print("=" * 50)

def create_multiple_files(base_name, count, content_template):
    """
    批量创建文件
    """
    created_files = []
    for i in range(count):
        filename = f"{output_dir}/{base_name}_{i+1:03d}.txt"
        content = content_template.format(index=i+1, filename=filename)
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            created_files.append(filename)
        except Exception as e:
            print(f"创建文件 {filename} 失败：{e}")
    
    return created_files

def write_log_files(log_entries):
    """
    写入日志文件
    """
    log_filename = f"{output_dir}/application.log"
    
    with open(log_filename, 'w', encoding='utf-8') as f:
        for entry in log_entries:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_line = f"[{timestamp}] {entry['level']} - {entry['message']}\n"
            f.write(log_line)
    
    return log_filename

print("\n--- 批量文件创建 ---")

# 批量创建文件
template = """文件编号：{index}
文件名：{filename}
创建时间：{timestamp}
内容：这是第{index}个测试文件
"""

content_template = template.format(
    index="{index}",
    filename="{filename}", 
    timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

files = create_multiple_files("batch_file", 5, content_template)
print(f"成功创建 {len(files)} 个文件")

# 创建日志文件
log_entries = [
    {"level": "INFO", "message": "应用程序启动"},
    {"level": "DEBUG", "message": "初始化配置"},
    {"level": "INFO", "message": "连接数据库成功"},
    {"level": "WARNING", "message": "内存使用率较高"},
    {"level": "ERROR", "message": "网络连接超时"},
    {"level": "INFO", "message": "应用程序正常运行"}
]

log_file = write_log_files(log_entries)
print(f"已创建日志文件：{log_file}")

# ============================================================================
# 9. 实际应用示例
# ============================================================================

print("\n" + "=" * 50)
print("9. 实际应用示例")
print("=" * 50)

def generate_report(data, filename):
    """
    生成报告文件
    """
    with open(filename, 'w', encoding='utf-8') as f:
        # 报告头部
        f.write("学生成绩分析报告\n")
        f.write("=" * 40 + "\n")
        f.write(f"生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"数据来源：学生管理系统\n\n")
        
        # 基本统计
        total_students = len(data)
        total_score = sum(s['总分'] for s in data)
        avg_score = total_score / total_students if total_students > 0 else 0
        
        f.write("基本统计信息\n")
        f.write("-" * 20 + "\n")
        f.write(f"学生总数：{total_students}\n")
        f.write(f"平均总分：{avg_score:.1f}\n")
        f.write(f"最高总分：{max(s['总分'] for s in data):.1f}\n")
        f.write(f"最低总分：{min(s['总分'] for s in data):.1f}\n\n")
        
        # 详细成绩
        f.write("详细成绩单\n")
        f.write("-" * 20 + "\n")
        f.write(f"{'姓名':<8} {'数学':>6} {'英语':>6} {'科学':>6} {'总分':>6} {'等级':<4}\n")
        f.write("-" * 40 + "\n")
        
        for student in sorted(data, key=lambda x: x['总分'], reverse=True):
            grade = 'A' if student['总分'] >= 270 else 'B' if student['总分'] >= 240 else 'C' if student['总分'] >= 210 else 'D'
            f.write(f"{student['姓名']:<8} {student['数学']:>6d} {student['英语']:>6d} "
                   f"{student['科学']:>6d} {student['总分']:>6.0f} {grade:<4}\n")
        
        f.write("\n报告生成完成\n")

def export_to_multiple_formats(data, base_filename):
    """
    导出数据到多种格式
    """
    # 导出为JSON
    json_file = f"{base_filename}.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 导出为CSV
    csv_file = f"{base_filename}.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        if data:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    
    # 导出为文本
    txt_file = f"{base_filename}.txt"
    with open(txt_file, 'w', encoding='utf-8') as f:
        for item in data:
            for key, value in item.items():
                f.write(f"{key}: {value}\n")
            f.write("-" * 30 + "\n")
    
    return [json_file, csv_file, txt_file]

print("\n--- 应用示例演示 ---")

# 准备示例数据
student_data = [
    {'姓名': '张三', '数学': 85, '英语': 92, '科学': 78, '总分': 255},
    {'姓名': '李四', '数学': 92, '英语': 88, '科学': 95, '总分': 275},
    {'姓名': '王五', '数学': 78, '英语': 85, '科学': 82, '总分': 245},
    {'姓名': '赵六', '数学': 95, '英语': 90, '科学': 88, '总分': 273}
]

# 生成报告
report_file = f"{output_dir}/student_report.txt"
generate_report(student_data, report_file)
print(f"已生成报告：{report_file}")

# 导出多种格式
exported_files = export_to_multiple_formats(student_data, f"{output_dir}/student_data")
print(f"已导出多种格式：{', '.join(os.path.basename(f) for f in exported_files)}")

# ============================================================================
# 10. 练习题
# ============================================================================

print("\n" + "=" * 50)
print("10. 练习题")
print("=" * 50)

print("""
练习题：

1. 基础练习：
   - 编写函数将列表数据写入文本文件，每行一个元素
   - 创建程序生成乘法表并保存到文件
   - 实现简单的日志记录功能

2. 进阶练习：
   - 编写CSV数据导出器，支持自定义分隔符
   - 创建配置文件生成器，支持多种格式
   - 实现数据备份和恢复功能

3. 思考题：
   - 什么时候使用'w'模式，什么时候使用'a'模式？
   - 如何保证文件写入的原子性？
   - 大量数据写入时如何优化性能？

4. 挑战练习：
   - 实现一个通用的数据导出系统
   - 创建支持模板的报告生成器
   - 编写一个文件同步工具
""")

# ============================================================================
# 11. 文件清理
# ============================================================================

print("\n" + "=" * 50)
print("11. 演示文件清理")
print("=" * 50)

# 列出创建的文件
if os.path.exists(output_dir):
    files = os.listdir(output_dir)
    print(f"\n创建的文件数量：{len(files)}")
    print("文件列表：")
    for file in sorted(files):
        file_path = os.path.join(output_dir, file)
        size = os.path.getsize(file_path)
        print(f"  {file} ({size} 字节)")

# 注意：实际使用中可以选择是否清理文件
print("\n提示：演示文件保存在 output_examples 目录中")
print("可以手动查看这些文件来验证写入效果")

# ============================================================================
# 12. 知识点总结
# ============================================================================

print("\n" + "=" * 50)
print("12. 知识点总结")
print("=" * 50)

print("""
知识点总结：

1. 文件写入模式：
   - 'w'：写入模式（覆盖）
   - 'a'：追加模式
   - 'x'：独占创建模式
   - 'wb'：二进制写入模式

2. 写入方法：
   - write()：写入字符串
   - writelines()：写入字符串列表
   - print(file=f)：使用print函数写入

3. 特殊格式：
   - JSON：json.dump()和json.dumps()
   - CSV：csv.writer和csv.DictWriter
   - 二进制：使用'wb'模式

4. 安全写入：
   - 异常处理
   - 备份机制
   - 原子性写入
   - 权限检查

5. 最佳实践：
   - 使用with语句
   - 指定正确编码
   - 处理异常情况
   - 选择合适的写入模式
   - 考虑数据完整性

6. 性能优化：
   - 批量写入
   - 缓冲区管理
   - 避免频繁开关文件
   - 选择合适的数据格式
""")

print("\n程序运行完成！")
print("建议：查看 output_examples 目录中的文件，了解不同写入方式的效果。")
```

## 代码详解

### 1. 基本文件写入操作

**write()方法**：
- 用于写入单个字符串
- 不会自动添加换行符
- 返回写入的字符数

**writelines()方法**：
- 用于写入字符串列表
- 不会自动添加换行符
- 需要手动在每个字符串末尾添加`\n`

### 2. 文件打开模式

- **'w'模式**：写入模式，会覆盖原有内容
- **'a'模式**：追加模式，在文件末尾添加内容
- **'x'模式**：独占创建模式，只能创建新文件
- **'wb'模式**：二进制写入模式

### 3. 格式化输出到文件

**使用print()函数**：
```python
with open('file.txt', 'w') as f:
    print("内容", file=f)
```

**格式化字符串**：
```python
with open('file.txt', 'w') as f:
    f.write(f"姓名：{name}, 年龄：{age}\n")
```

### 4. 特殊格式文件处理

**JSON文件写入**：
```python
import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

**CSV文件写入**：
```python
import csv
with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

### 5. 安全文件写入

**异常处理**：
- 捕获`PermissionError`、`OSError`等异常
- 提供错误信息和恢复机制

**原子性写入**：
- 先写入临时文件
- 写入成功后重命名为目标文件
- 保证数据完整性

**备份机制**：
- 写入前创建原文件备份
- 防止数据丢失

## 学习要点

### 1. 文件写入模式选择
- 新建文件或完全替换：使用'w'模式
- 添加内容到现有文件：使用'a'模式
- 确保文件不存在才创建：使用'x'模式
- 处理二进制数据：使用'wb'模式

### 2. 编码处理
- 明确指定编码格式（通常使用'utf-8'）
- 处理中文等非ASCII字符时特别重要
- JSON文件使用`ensure_ascii=False`参数

### 3. 异常处理
- 使用try-except捕获文件操作异常
- 提供有意义的错误信息
- 实现错误恢复机制

### 4. 性能优化
- 批量写入比逐行写入效率更高
- 使用适当的缓冲区大小
- 避免频繁打开关闭文件

### 5. 数据完整性
- 使用原子性写入防止数据损坏
- 实现备份机制
- 验证写入结果

## 实践练习

### 基础练习
1. 编写函数将购物清单写入文本文件
2. 创建程序生成课程表并保存为CSV文件
3. 实现简单的错误日志记录功能

### 进阶练习
1. 编写通用的数据导出器，支持多种格式
2. 创建配置文件管理器
3. 实现文件备份和版本控制功能

### 挑战练习
1. 开发一个报告生成系统
2. 创建数据同步工具
3. 实现大文件的分块写入功能

## 运行示例

```bash
# 运行文件输出示例
python 06_file_output.py

# 查看生成的文件
ls output_examples/

# 查看特定文件内容
cat output_examples/formatted_output.txt
cat output_examples/data_formatted.json
```

## 扩展思考

1. **文件写入模式的选择策略**：
   - 什么情况下使用覆盖模式？
   - 什么情况下使用追加模式？
   - 如何处理并发写入问题？

2. **大文件处理**：
   - 如何高效写入大量数据？
   - 如何处理内存限制？
   - 如何实现断点续写？

3. **数据格式选择**：
   - 什么时候使用JSON格式？
   - 什么时候使用CSV格式？
   - 如何选择合适的数据格式？

4. **安全性考虑**：
   - 如何防止数据泄露？
   - 如何处理敏感信息？
   - 如何实现访问控制？

## 模块导航

- [上一节：文件输入操作](./file-input.md)
- [下一节：高级输入输出](./advanced-io.md)
- [返回目录](./index.md)

---

*学习建议：通过实际运行代码和查看生成的文件来理解不同写入方式的效果，重点掌握安全写入和异常处理的最佳实践。*