#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
嵌套条件语句

本文件演示Python中嵌套条件语句的用法，包括：
1. 嵌套if语句的基本语法
2. 多层嵌套的条件判断
3. 嵌套与elif的选择
4. 复杂业务逻辑的实现

学习目标：
- 掌握嵌套条件语句的语法结构
- 理解多层条件判断的逻辑
- 学会处理复杂的条件组合
- 能够编写清晰的嵌套条件代码
"""

# 1. 基本的嵌套if语句
print("=== 1. 基本嵌套if语句 ===")
age = 25
income = 50000

if age >= 18:
    print("已成年")
    if income >= 30000:
        print("收入达标，可以申请信用卡")
        if income >= 100000:
            print("可以申请白金卡")
        else:
            print("可以申请普通卡")
    else:
        print("收入不足，暂时无法申请信用卡")
else:
    print("未成年，无法申请信用卡")

print()

# 2. 学生成绩评定系统
print("=== 2. 学生成绩评定系统 ===")
math_score = 85
english_score = 78
attendance = 0.92

if math_score >= 60:  # 数学及格
    print("数学：及格")
    if english_score >= 60:  # 英语也及格
        print("英语：及格")
        print("两门课程都及格！")
        
        if attendance >= 0.9:  # 出勤率也达标
            print(f"出勤率：{attendance*100}% - 优秀")
            if math_score >= 90 and english_score >= 90:
                print("综合评定：优秀学生")
                print("奖励：奖学金 + 荣誉证书")
            elif math_score >= 80 and english_score >= 80:
                print("综合评定：良好学生")
                print("奖励：表扬信")
            else:
                print("综合评定：合格学生")
                print("奖励：继续努力")
        else:
            print(f"出勤率：{attendance*100}% - 不达标")
            print("综合评定：需要改善出勤")
    else:
        print("英语：不及格")
        print("需要补考英语")
else:
    print("数学：不及格")
    if english_score >= 60:
        print("英语：及格")
        print("需要补考数学")
    else:
        print("英语：不及格")
        print("需要补考数学和英语")

print()

# 3. 用户登录验证系统
print("=== 3. 用户登录验证系统 ===")
username = "admin"
password = "admin123"
is_account_active = True
login_attempts = 2
max_attempts = 3

if username:  # 用户名不为空
    print(f"用户名：{username}")
    if is_account_active:  # 账户是激活状态
        print("账户状态：激活")
        if login_attempts < max_attempts:  # 登录次数未超限
            print(f"登录尝试：{login_attempts}/{max_attempts}")
            if password == "admin123":  # 密码正确
                print("密码验证：通过")
                if username == "admin":  # 管理员账户
                    print("登录成功！欢迎管理员")
                    print("权限：完全访问")
                else:  # 普通用户
                    print("登录成功！欢迎用户")
                    print("权限：标准访问")
            else:
                print("密码验证：失败")
                print("登录失败：密码错误")
        else:
            print("登录失败：尝试次数过多，账户已锁定")
    else:
        print("登录失败：账户未激活")
else:
    print("登录失败：用户名不能为空")

print()

# 4. 购物折扣计算系统
print("=== 4. 购物折扣计算系统 ===")
total_amount = 1200
is_vip = True
is_first_purchase = False
has_coupon = True
coupon_value = 100

print(f"原始金额：{total_amount}元")
final_amount = total_amount
discount_info = []

if total_amount > 0:  # 金额有效
    if total_amount >= 1000:  # 满1000
        print("满1000元，可享受折扣")
        if is_vip:  # VIP用户
            print("VIP用户额外优惠")
            if total_amount >= 2000:  # VIP且满2000
                discount_rate = 0.7  # 7折
                discount_info.append("VIP满2000享7折")
            else:  # VIP且满1000
                discount_rate = 0.8  # 8折
                discount_info.append("VIP满1000享8折")
            final_amount *= discount_rate
        else:  # 非VIP用户
            if total_amount >= 2000:  # 非VIP但满2000
                discount_rate = 0.85  # 8.5折
                discount_info.append("满2000享8.5折")
            else:  # 非VIP且满1000
                discount_rate = 0.9  # 9折
                discount_info.append("满1000享9折")
            final_amount *= discount_rate
        
        # 检查是否有优惠券
        if has_coupon:
            print(f"使用优惠券：{coupon_value}元")
            final_amount -= coupon_value
            discount_info.append(f"优惠券减{coupon_value}元")
        
        # 首次购买额外优惠
        if is_first_purchase:
            first_purchase_discount = 50
            final_amount -= first_purchase_discount
            discount_info.append(f"首次购买减{first_purchase_discount}元")
            print("首次购买额外优惠")
    else:
        print("金额不足1000元，无折扣")
else:
    print("无效金额")

print(f"优惠详情：{', '.join(discount_info) if discount_info else '无优惠'}")
print(f"最终金额：{final_amount:.2f}元")
print(f"节省金额：{total_amount - final_amount:.2f}元")
print()

# 5. 天气穿衣建议系统
print("=== 5. 天气穿衣建议系统 ===")
temperature = 15
humidity = 70
is_raining = True
wind_speed = 20  # km/h

clothing_suggestions = []
accessories = []

if temperature < 0:  # 严寒
    clothing_suggestions.append("羽绒服")
    clothing_suggestions.append("保暖内衣")
    if wind_speed > 15:
        accessories.append("防风面罩")
elif temperature < 10:  # 寒冷
    clothing_suggestions.append("厚外套")
    if humidity > 60:
        clothing_suggestions.append("防潮衣物")
    if is_raining:
        accessories.append("雨衣")
        accessories.append("雨靴")
elif temperature < 20:  # 凉爽
    clothing_suggestions.append("薄外套或毛衣")
    if is_raining:
        accessories.append("雨伞")
        if wind_speed > 20:
            accessories.append("防风雨衣")
        else:
            accessories.append("轻便雨衣")
elif temperature < 30:  # 温暖
    clothing_suggestions.append("长袖衬衫")
    if humidity > 70:
        clothing_suggestions.append("透气材质")
    if is_raining:
        accessories.append("雨伞")
else:  # 炎热
    clothing_suggestions.append("短袖")
    clothing_suggestions.append("短裤")
    if humidity > 80:
        accessories.append("毛巾")
        clothing_suggestions.append("速干材质")

# 通用配饰建议
if wind_speed > 25:
    accessories.append("帽子")
if humidity < 30:
    accessories.append("润肤霜")

print(f"天气条件：温度{temperature}°C，湿度{humidity}%")
print(f"降雨：{'是' if is_raining else '否'}，风速：{wind_speed}km/h")
print(f"穿衣建议：{', '.join(clothing_suggestions)}")
print(f"配饰建议：{', '.join(accessories) if accessories else '无特殊配饰'}")
print()

# 6. 银行贷款审批系统
print("=== 6. 银行贷款审批系统 ===")
applicant_age = 35
monthly_income = 15000
credit_score = 750
employment_years = 5
existing_debt = 200000
loan_amount = 500000

approval_status = "待审核"
interest_rate = 0
max_loan_amount = 0
requirements = []

if applicant_age >= 18 and applicant_age <= 65:  # 年龄符合
    print(f"年龄：{applicant_age}岁 - 符合要求")
    if monthly_income >= 5000:  # 收入符合
        print(f"月收入：{monthly_income}元 - 符合要求")
        if credit_score >= 600:  # 信用分符合
            print(f"信用分：{credit_score} - 符合要求")
            if employment_years >= 2:  # 工作年限符合
                print(f"工作年限：{employment_years}年 - 符合要求")
                
                # 计算债务收入比
                debt_to_income_ratio = existing_debt / (monthly_income * 12)
                print(f"债务收入比：{debt_to_income_ratio:.2f}")
                
                if debt_to_income_ratio <= 0.5:  # 债务比例合理
                    print("债务收入比 - 符合要求")
                    
                    # 根据条件确定贷款额度和利率
                    if credit_score >= 800 and monthly_income >= 20000:
                        max_loan_amount = monthly_income * 12 * 10  # 10倍年收入
                        interest_rate = 0.035  # 3.5%
                        approval_status = "优质客户 - 预批准"
                    elif credit_score >= 700 and monthly_income >= 10000:
                        max_loan_amount = monthly_income * 12 * 8  # 8倍年收入
                        interest_rate = 0.045  # 4.5%
                        approval_status = "良好客户 - 预批准"
                    else:
                        max_loan_amount = monthly_income * 12 * 5  # 5倍年收入
                        interest_rate = 0.055  # 5.5%
                        approval_status = "标准客户 - 预批准"
                    
                    # 检查申请金额是否在范围内
                    if loan_amount <= max_loan_amount:
                        print(f"申请金额：{loan_amount}元 - 在批准范围内")
                        final_approval = "批准"
                    else:
                        print(f"申请金额：{loan_amount}元 - 超出最大额度")
                        final_approval = "需要降低贷款金额"
                else:
                    approval_status = "拒绝 - 债务负担过重"
                    requirements.append("降低现有债务")
            else:
                approval_status = "拒绝 - 工作年限不足"
                requirements.append("至少2年工作经验")
        else:
            approval_status = "拒绝 - 信用分不足"
            requirements.append("提高信用分至600以上")
    else:
        approval_status = "拒绝 - 收入不足"
        requirements.append("月收入至少5000元")
else:
    approval_status = "拒绝 - 年龄不符合要求"
    requirements.append("年龄需在18-65岁之间")

print(f"\n审批结果：{approval_status}")
if max_loan_amount > 0:
    print(f"最大贷款额度：{max_loan_amount}元")
    print(f"利率：{interest_rate*100}%")
if requirements:
    print(f"改进建议：{', '.join(requirements)}")
print()

print("=== 程序结束 ===")

# 练习题
print("\n=== 练习题 ===")
print("1. 编写嵌套条件判断一个数是正数、负数还是零，如果是正数再判断是否为偶数")
print("2. 编写程序判断三个数的大小关系（使用嵌套条件）")
print("3. 编写学生奖学金评定系统（考虑成绩、出勤率、品行等多个因素）")
print("4. 编写电影票价计算系统（考虑年龄、时间段、会员等级等因素）")
print("5. 编写简单的游戏角色升级系统（考虑等级、经验值、任务完成情况等）")