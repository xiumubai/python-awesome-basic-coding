#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
elif多分支语句

本文件演示Python中elif语句的用法，包括：
1. elif语句的基本语法
2. 多分支条件判断
3. elif与if-else的区别
4. 复杂的多条件判断场景

学习目标：
- 掌握elif语句的语法结构
- 理解多分支逻辑的应用场景
- 学会处理多个互斥条件
- 能够编写复杂的条件分支程序
"""

# 1. 基本的if-elif-else语句
print("=== 1. 基本if-elif-else语句 ===")
score = 85

if score >= 90:
    grade = "A"
    comment = "优秀！"
elif score >= 80:
    grade = "B"
    comment = "良好！"
elif score >= 70:
    grade = "C"
    comment = "中等"
elif score >= 60:
    grade = "D"
    comment = "及格"
else:
    grade = "F"
    comment = "不及格"

print(f"分数：{score}")
print(f"等级：{grade}")
print(f"评价：{comment}")
print()

# 2. 年龄段分类
print("=== 2. 年龄段分类 ===")
age = 25

if age < 13:
    category = "儿童"
    activities = ["玩游戏", "看动画片", "学习基础知识"]
elif age < 20:
    category = "青少年"
    activities = ["上学", "运动", "培养兴趣爱好"]
elif age < 60:
    category = "成年人"
    activities = ["工作", "照顾家庭", "职业发展"]
else:
    category = "老年人"
    activities = ["享受退休生活", "锻炼身体", "含饴弄孙"]

print(f"年龄：{age}岁")
print(f"分类：{category}")
print(f"主要活动：{', '.join(activities)}")
print()

# 3. 季节判断
print("=== 3. 季节判断 ===")
month = 7

if month in [12, 1, 2]:
    season = "冬季"
    weather = "寒冷"
    clothing = "厚外套、毛衣"
elif month in [3, 4, 5]:
    season = "春季"
    weather = "温和"
    clothing = "薄外套、长袖"
elif month in [6, 7, 8]:
    season = "夏季"
    weather = "炎热"
    clothing = "短袖、短裤"
elif month in [9, 10, 11]:
    season = "秋季"
    weather = "凉爽"
    clothing = "长袖、薄外套"
else:
    season = "无效月份"
    weather = "未知"
    clothing = "未知"

print(f"月份：{month}月")
print(f"季节：{season}")
print(f"天气：{weather}")
print(f"穿衣建议：{clothing}")
print()

# 4. BMI指数分类
print("=== 4. BMI指数分类 ===")
weight = 70  # 公斤
height = 1.75  # 米
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "体重过轻"
    advice = "建议增加营养，适当增重"
elif bmi < 24:
    category = "正常体重"
    advice = "保持现有的健康生活方式"
elif bmi < 28:
    category = "体重过重"
    advice = "建议控制饮食，增加运动"
elif bmi < 32:
    category = "肥胖"
    advice = "建议咨询医生，制定减重计划"
else:
    category = "严重肥胖"
    advice = "强烈建议就医，需要专业指导"

print(f"身高：{height}m，体重：{weight}kg")
print(f"BMI指数：{bmi:.2f}")
print(f"分类：{category}")
print(f"建议：{advice}")
print()

# 5. 交通工具选择
print("=== 5. 交通工具选择 ===")
distance = 15  # 公里
budget = 50   # 元

if distance <= 2:
    transport = "步行"
    cost = 0
    time = distance * 12  # 分钟
elif distance <= 5:
    transport = "自行车"
    cost = 0
    time = distance * 4
elif distance <= 10 and budget >= 10:
    transport = "公交车"
    cost = 2
    time = distance * 3
elif distance <= 30 and budget >= 20:
    transport = "地铁"
    cost = 5
    time = distance * 2
elif budget >= 30:
    transport = "出租车"
    cost = distance * 2
    time = distance * 1.5
else:
    transport = "预算不足，建议步行或自行车"
    cost = 0
    time = distance * 12

print(f"距离：{distance}公里，预算：{budget}元")
print(f"推荐交通工具：{transport}")
print(f"预计费用：{cost}元")
print(f"预计时间：{time}分钟")
print()

# 6. 用户权限管理
print("=== 6. 用户权限管理 ===")
user_role = "editor"
user_level = 3

if user_role == "admin":
    permissions = ["读取", "写入", "删除", "管理用户", "系统设置"]
    access_level = "完全访问"
elif user_role == "editor" and user_level >= 3:
    permissions = ["读取", "写入", "编辑内容"]
    access_level = "编辑访问"
elif user_role == "editor":
    permissions = ["读取", "基础编辑"]
    access_level = "基础编辑访问"
elif user_role == "viewer":
    permissions = ["读取"]
    access_level = "只读访问"
else:
    permissions = []
    access_level = "无访问权限"

print(f"用户角色：{user_role}，等级：{user_level}")
print(f"访问级别：{access_level}")
print(f"权限列表：{', '.join(permissions) if permissions else '无权限'}")
print()

# 7. 考试成绩统计
print("=== 7. 考试成绩统计 ===")
scores = [95, 87, 76, 92, 68, 84, 91, 73, 89, 77]

excellent_count = 0
good_count = 0
average_count = 0
fail_count = 0

for score in scores:
    if score >= 90:
        excellent_count += 1
    elif score >= 80:
        good_count += 1
    elif score >= 60:
        average_count += 1
    else:
        fail_count += 1

print(f"总人数：{len(scores)}")
print(f"优秀（90+）：{excellent_count}人")
print(f"良好（80-89）：{good_count}人")
print(f"及格（60-79）：{average_count}人")
print(f"不及格（<60）：{fail_count}人")
print()

# 8. 温度和湿度的舒适度判断
print("=== 8. 温度和湿度舒适度判断 ===")
temperature = 25
humidity = 60

if 20 <= temperature <= 26 and 40 <= humidity <= 60:
    comfort = "非常舒适"
    action = "无需调整"
elif 18 <= temperature <= 28 and 30 <= humidity <= 70:
    comfort = "比较舒适"
    action = "可以微调空调"
elif temperature < 18:
    comfort = "偏冷"
    action = "建议升高温度"
elif temperature > 28:
    comfort = "偏热"
    action = "建议降低温度"
elif humidity < 30:
    comfort = "过于干燥"
    action = "建议使用加湿器"
elif humidity > 70:
    comfort = "过于潮湿"
    action = "建议使用除湿器"
else:
    comfort = "不太舒适"
    action = "建议调整温湿度"

print(f"温度：{temperature}°C，湿度：{humidity}%")
print(f"舒适度：{comfort}")
print(f"建议：{action}")
print()

# 9. 多条件组合判断
print("=== 9. 多条件组合判断 ===")
student_age = 20
student_grade = 85
attendance_rate = 0.9

if student_age < 18:
    scholarship = "未成年学生奖学金"
    amount = 1000
elif student_grade >= 90 and attendance_rate >= 0.95:
    scholarship = "优秀学生奖学金"
    amount = 5000
elif student_grade >= 85 and attendance_rate >= 0.9:
    scholarship = "优良学生奖学金"
    amount = 3000
elif student_grade >= 80 and attendance_rate >= 0.85:
    scholarship = "进步学生奖学金"
    amount = 2000
elif attendance_rate >= 0.95:
    scholarship = "全勤奖学金"
    amount = 1500
else:
    scholarship = "无奖学金"
    amount = 0

print(f"学生年龄：{student_age}岁")
print(f"学生成绩：{student_grade}分")
print(f"出勤率：{attendance_rate*100}%")
print(f"奖学金类型：{scholarship}")
print(f"奖学金金额：{amount}元")
print()

print("=== 程序结束 ===")

# 练习题
print("\n=== 练习题 ===")
print("1. 编写程序根据月份判断季节（使用elif）")
print("2. 编写程序根据分数给出等级（A、B、C、D、F）")
print("3. 编写程序根据年龄判断票价（儿童、学生、成人、老人）")
print("4. 编写程序根据BMI值给出健康建议")
print("5. 编写程序实现简单的计算器（+、-、*、/）")