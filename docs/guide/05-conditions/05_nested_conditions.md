# 嵌套条件语句

## 概述

嵌套条件语句是指在一个条件语句的代码块内部再包含另一个条件语句。这种结构允许我们处理更复杂的逻辑关系，实现多层次的条件判断。虽然嵌套条件功能强大，但也需要谨慎使用，以保持代码的可读性和可维护性。

## 基本语法

```python
if outer_condition:
    # 外层条件为True时的代码
    if inner_condition1:
        # 内层条件1为True时的代码
        statement1
    elif inner_condition2:
        # 内层条件2为True时的代码
        statement2
    else:
        # 内层所有条件都为False时的代码
        statement3
else:
    # 外层条件为False时的代码
    statement4
```

### 语法要点

1. **缩进层次**：每一层嵌套都需要额外的缩进（通常4个空格）
2. **逻辑关系**：内层条件只有在外层条件满足时才会被检查
3. **代码块**：每个条件分支都形成独立的代码块
4. **可读性**：避免过深的嵌套（建议不超过3-4层）
5. **维护性**：复杂的嵌套可以考虑重构为函数或使用elif

## 基础示例

### 1. 学生成绩评定系统

```python
# 综合评定学生表现
math_score = 85
english_score = 78
attendance_rate = 92
extra_activities = 2

print("=== 学生综合评定系统 ===")
print(f"数学成绩：{math_score}")
print(f"英语成绩：{english_score}")
print(f"出勤率：{attendance_rate}%")
print(f"课外活动：{extra_activities}项")
print()

# 首先检查基本成绩要求
if math_score >= 60 and english_score >= 60:
    print("✅ 基本成绩要求：通过")
    
    # 在基本要求通过的基础上，进行进一步评定
    if math_score >= 90 and english_score >= 90:
        print("🌟 学术表现：优秀")
        
        # 优秀学生的额外评定
        if attendance_rate >= 95:
            print("🎯 出勤表现：完美")
            if extra_activities >= 3:
                print("🏆 最终评定：全优学生（推荐奖学金）")
            else:
                print("🏆 最终评定：优秀学生")
        else:
            print("⚠️ 出勤表现：需要改进")
            print("🏆 最终评定：学术优秀但需提高出勤")
    
    elif math_score >= 80 or english_score >= 80:
        print("👍 学术表现：良好")
        
        # 良好学生的评定
        if attendance_rate >= 90:
            print("✅ 出勤表现：良好")
            if extra_activities >= 2:
                print("🏆 最终评定：综合良好学生")
            else:
                print("🏆 最终评定：学术良好学生")
        else:
            print("⚠️ 出勤表现：一般")
            print("🏆 最终评定：需要全面提升")
    
    else:
        print("📚 学术表现：及格")
        if attendance_rate >= 85:
            print("✅ 出勤表现：尚可")
            print("🏆 最终评定：基础合格学生")
        else:
            print("❌ 出勤表现：不足")
            print("🏆 最终评定：需要重点关注")

else:
    print("❌ 基本成绩要求：未通过")
    
    # 不及格学生的特殊处理
    if math_score < 60 and english_score < 60:
        print("📚 两科都不及格，需要重点辅导")
        if attendance_rate < 70:
            print("🚨 出勤率过低，建议家长面谈")
        else:
            print("💪 出勤率尚可，重点加强学习")
    else:
        if math_score < 60:
            print("📊 数学需要补强")
        if english_score < 60:
            print("📝 英语需要补强")
        print("🎯 建议针对性辅导")
```

### 2. 用户登录验证系统

```python
# 多层安全验证系统
username = "admin"
password = "secure123"
is_account_active = True
failed_attempts = 2
max_attempts = 3
is_two_factor_enabled = True
two_factor_code = "123456"
input_two_factor = "123456"

print("=== 用户登录验证系统 ===")

# 第一层：检查账户状态
if is_account_active:
    print("✅ 账户状态：激活")
    
    # 第二层：检查登录尝试次数
    if failed_attempts < max_attempts:
        print(f"✅ 登录尝试：{failed_attempts}/{max_attempts}")
        
        # 第三层：验证用户名和密码
        input_username = "admin"
        input_password = "secure123"
        
        if input_username == username and input_password == password:
            print("✅ 用户名密码：验证通过")
            
            # 第四层：双因素认证
            if is_two_factor_enabled:
                print("🔐 双因素认证：已启用")
                
                if input_two_factor == two_factor_code:
                    print("✅ 双因素认证：验证通过")
                    print("🎉 登录成功！欢迎使用系统")
                    
                    # 根据用户角色显示不同界面
                    if username == "admin":
                        print("🔧 加载管理员界面...")
                        print("- 用户管理")
                        print("- 系统设置")
                        print("- 数据统计")
                    else:
                        print("👤 加载用户界面...")
                        print("- 个人资料")
                        print("- 基本功能")
                else:
                    print("❌ 双因素认证：验证失败")
                    print("🚨 登录失败：双因素认证码错误")
            else:
                print("⚠️ 双因素认证：未启用（建议启用）")
                print("🎉 登录成功！")
        else:
            print("❌ 用户名密码：验证失败")
            if input_username != username:
                print("🚨 用户名错误")
            if input_password != password:
                print("🚨 密码错误")
            print("🚫 登录失败")
    else:
        print(f"🚨 登录尝试：已达上限({max_attempts})")
        print("🔒 账户已被临时锁定")
        print("💡 请联系管理员或稍后再试")
else:
    print("❌ 账户状态：已禁用")
    print("🚫 无法登录")
    print("💡 请联系管理员激活账户")
```

### 3. 购物折扣计算系统

```python
# 复杂的购物折扣计算
total_amount = 250
is_member = True
member_level = "gold"
member_years = 3
is_birthday_month = True
has_coupon = True
coupon_discount = 0.1  # 10%折扣券
item_category = "electronics"

print("=== 购物折扣计算系统 ===")
print(f"购物金额：${total_amount}")
print(f"商品类别：{item_category}")
print()

final_amount = total_amount
discount_details = []

# 第一层：检查是否为会员
if is_member:
    print("✅ 会员身份：已确认")
    
    # 第二层：根据会员等级给予折扣
    if member_level == "platinum":
        member_discount = 0.2  # 20%折扣
        print(f"🌟 白金会员：{member_discount*100}%折扣")
    elif member_level == "gold":
        member_discount = 0.15  # 15%折扣
        print(f"🥇 金牌会员：{member_discount*100}%折扣")
        
        # 第三层：金牌会员的额外优惠
        if member_years >= 2:
            print("🎖️ 资深会员：额外5%折扣")
            member_discount += 0.05
    elif member_level == "silver":
        member_discount = 0.1  # 10%折扣
        print(f"🥈 银牌会员：{member_discount*100}%折扣")
    else:
        member_discount = 0.05  # 5%折扣
        print(f"🆕 普通会员：{member_discount*100}%折扣")
    
    final_amount *= (1 - member_discount)
    discount_details.append(f"会员折扣: -{member_discount*100}%")
    
    # 第三层：生日月特殊优惠
    if is_birthday_month:
        print("🎂 生日月特惠：额外10%折扣")
        birthday_discount = 0.1
        final_amount *= (1 - birthday_discount)
        discount_details.append(f"生日特惠: -{birthday_discount*100}%")
    
    # 第三层：检查优惠券
    if has_coupon:
        print(f"🎫 优惠券：{coupon_discount*100}%折扣")
        
        # 第四层：检查优惠券使用条件
        if total_amount >= 200:
            print("✅ 满足优惠券使用条件（满$200）")
            final_amount *= (1 - coupon_discount)
            discount_details.append(f"优惠券: -{coupon_discount*100}%")
        else:
            print("❌ 不满足优惠券使用条件（需满$200）")
    
    # 第三层：特定商品类别额外折扣
    if item_category == "electronics":
        if total_amount >= 300:
            print("💻 电子产品满$300：额外5%折扣")
            category_discount = 0.05
            final_amount *= (1 - category_discount)
            discount_details.append(f"电子产品特惠: -{category_discount*100}%")
        else:
            print("💻 电子产品：需满$300才能享受额外折扣")

else:
    print("❌ 非会员用户")
    
    # 非会员的特殊处理
    if total_amount >= 500:
        print("💰 大额购物：非会员也可享受5%折扣")
        non_member_discount = 0.05
        final_amount *= (1 - non_member_discount)
        discount_details.append(f"大额购物折扣: -{non_member_discount*100}%")
    else:
        print("💡 建议注册会员享受更多优惠")

# 显示最终结果
print("\n=== 结算详情 ===")
print(f"原价：${total_amount:.2f}")
for detail in discount_details:
    print(f"优惠：{detail}")
print(f"最终价格：${final_amount:.2f}")
print(f"总共节省：${total_amount - final_amount:.2f}")
print(f"折扣率：{((total_amount - final_amount) / total_amount * 100):.1f}%")
```

## 嵌套与elif的选择

### 1. 适合使用嵌套的场景

```python
# 场景：权限检查系统（层级关系明确）
user_role = "manager"
department = "sales"
is_active = True
project_access = True

# 这种情况适合嵌套，因为有明确的层级关系
if user_role == "admin":
    print("管理员权限：全部访问")
elif user_role == "manager":
    print("经理权限")
    if is_active:
        print("账户激活")
        if department == "sales":
            print("销售部门经理")
            if project_access:
                print("可以访问项目数据")
            else:
                print("无项目访问权限")
        elif department == "hr":
            print("人事部门经理")
            print("可以访问员工数据")
    else:
        print("账户未激活，无法访问")
else:
    print("普通用户权限")
```

### 2. 适合使用elif的场景

```python
# 场景：成绩等级判断（平级关系）
score = 85

# 这种情况适合elif，因为是平级的互斥条件
if score >= 90:
    grade = "A"
    print("优秀")
elif score >= 80:
    grade = "B"
    print("良好")
elif score >= 70:
    grade = "C"
    print("中等")
elif score >= 60:
    grade = "D"
    print("及格")
else:
    grade = "F"
    print("不及格")
```

## 复杂业务逻辑实现

### 1. 天气穿衣建议系统

```python
# 智能穿衣建议系统
temperature = 15  # 摄氏度
humidity = 70     # 湿度百分比
wind_speed = 20   # 风速 km/h
is_raining = True
is_sunny = False
activity = "outdoor_sports"  # 活动类型

print("=== 智能穿衣建议系统 ===")
print(f"温度：{temperature}°C")
print(f"湿度：{humidity}%")
print(f"风速：{wind_speed} km/h")
print(f"降雨：{'是' if is_raining else '否'}")
print(f"活动：{activity}")
print()

clothing_suggestions = []
accessories = []

# 第一层：根据温度确定基础着装
if temperature >= 25:
    print("🌡️ 温度：炎热")
    base_clothing = "短袖T恤 + 短裤"
    
    # 炎热天气的细分建议
    if humidity > 80:
        print("💧 湿度过高，选择透气材质")
        clothing_suggestions.append("选择棉质或透气面料")
        if activity == "outdoor_sports":
            clothing_suggestions.append("运动速干衣")
            accessories.append("运动毛巾")
    
    if is_sunny:
        accessories.extend(["太阳镜", "防晒帽", "防晒霜"])
        
elif temperature >= 15:
    print("🌡️ 温度：温和")
    base_clothing = "长袖衬衫 + 长裤"
    
    # 温和天气的细分建议
    if wind_speed > 15:
        print("💨 风力较大")
        if temperature < 20:
            clothing_suggestions.append("加一件薄外套")
            base_clothing += " + 薄外套"
    
    if activity == "outdoor_sports":
        if humidity > 70:
            clothing_suggestions.append("选择透气运动装")
        else:
            clothing_suggestions.append("标准运动装即可")
            
elif temperature >= 5:
    print("🌡️ 温度：凉爽")
    base_clothing = "毛衣 + 长裤 + 外套"
    
    # 凉爽天气的细分建议
    if wind_speed > 20:
        print("💨 风力强劲")
        clothing_suggestions.append("选择防风外套")
        if activity == "outdoor_sports":
            clothing_suggestions.append("运动防风衣")
            accessories.append("运动手套")
    
    if humidity < 40:
        clothing_suggestions.append("注意保湿")
        accessories.append("润肤霜")
        
else:
    print("🌡️ 温度：寒冷")
    base_clothing = "保暖内衣 + 毛衣 + 厚外套 + 长裤"
    
    # 寒冷天气的特殊建议
    if temperature < -5:
        print("🥶 严寒天气")
        clothing_suggestions.append("羽绒服或厚棉衣")
        accessories.extend(["保暖帽", "手套", "围巾"])
        
        if activity == "outdoor_sports":
            clothing_suggestions.append("专业保暖运动装")
            accessories.append("保暖面罩")
    
    if wind_speed > 25:
        print("🌪️ 强风天气")
        clothing_suggestions.append("防风保暖外套")

# 第二层：根据天气条件调整
if is_raining:
    print("🌧️ 雨天")
    accessories.extend(["雨伞", "雨衣或防水外套"])
    
    if activity == "outdoor_sports":
        print("⚠️ 雨天户外运动建议")
        clothing_suggestions.append("防水运动装")
        accessories.append("防滑运动鞋")
        
        if temperature < 10:
            print("🚨 低温雨天，建议室内活动")
            clothing_suggestions.append("考虑改为室内活动")

# 输出最终建议
print("\n=== 穿衣建议 ===")
print(f"基础搭配：{base_clothing}")

if clothing_suggestions:
    print("\n特殊建议：")
    for suggestion in clothing_suggestions:
        print(f"• {suggestion}")

if accessories:
    print("\n配件建议：")
    for accessory in accessories:
        print(f"• {accessory}")

# 健康提醒
print("\n=== 健康提醒 ===")
if temperature > 30 and humidity > 80:
    print("⚠️ 高温高湿，注意防暑降温")
elif temperature < 0 and wind_speed > 20:
    print("⚠️ 严寒大风，减少户外活动时间")
elif is_raining and temperature < 5:
    print("⚠️ 低温雨天，小心感冒")
else:
    print("✅ 天气条件良好，注意适当增减衣物")
```

### 2. 银行贷款审批系统

```python
# 银行贷款审批系统
applicant_age = 30
annual_income = 80000  # 年收入
credit_score = 750     # 信用评分
employment_years = 5   # 工作年限
existing_debt = 15000  # 现有债务
loan_amount = 200000   # 申请贷款金额
has_collateral = True  # 是否有抵押物
collateral_value = 300000  # 抵押物价值
is_first_time_buyer = True  # 是否首次购房

print("=== 银行贷款审批系统 ===")
print(f"申请人年龄：{applicant_age}岁")
print(f"年收入：${annual_income:,}")
print(f"信用评分：{credit_score}")
print(f"工作年限：{employment_years}年")
print(f"现有债务：${existing_debt:,}")
print(f"申请金额：${loan_amount:,}")
print()

approval_status = "待审核"
interest_rate = 0
approval_reasons = []
rejection_reasons = []
special_conditions = []

# 第一层：基本资格检查
if applicant_age >= 18 and applicant_age <= 65:
    print("✅ 年龄要求：符合（18-65岁）")
    
    # 第二层：收入和债务比例检查
    debt_to_income_ratio = (existing_debt + loan_amount * 0.05) / annual_income  # 假设贷款年还款为5%
    
    if debt_to_income_ratio <= 0.4:  # 债务收入比不超过40%
        print(f"✅ 债务收入比：{debt_to_income_ratio:.2%}（符合要求）")
        
        # 第三层：信用评分检查
        if credit_score >= 700:
            print(f"✅ 信用评分：{credit_score}（优秀）")
            base_interest_rate = 3.5
            
            # 第四层：工作稳定性检查
            if employment_years >= 2:
                print(f"✅ 工作年限：{employment_years}年（稳定）")
                
                # 第五层：贷款金额与收入比例
                loan_to_income_ratio = loan_amount / annual_income
                
                if loan_to_income_ratio <= 5:  # 贷款金额不超过年收入5倍
                    print(f"✅ 贷款收入比：{loan_to_income_ratio:.1f}倍（合理）")
                    
                    # 最终审批决定
                    approval_status = "批准"
                    interest_rate = base_interest_rate
                    approval_reasons.append("信用记录优秀")
                    approval_reasons.append("收入稳定")
                    approval_reasons.append("债务比例合理")
                    
                    # 优惠条件检查
                    if has_collateral:
                        if collateral_value >= loan_amount * 1.2:  # 抵押物价值超过贷款120%
                            print(f"🏠 抵押物价值：${collateral_value:,}（充足）")
                            interest_rate -= 0.5  # 利率优惠0.5%
                            approval_reasons.append("有充足抵押物担保")
                        else:
                            print(f"⚠️ 抵押物价值：${collateral_value:,}（不足）")
                            special_conditions.append("需要额外担保")
                    
                    if is_first_time_buyer:
                        print("🏡 首次购房者优惠")
                        interest_rate -= 0.2  # 首次购房优惠0.2%
                        approval_reasons.append("首次购房者优惠政策")
                    
                    # 根据信用评分调整利率
                    if credit_score >= 800:
                        interest_rate -= 0.3
                        approval_reasons.append("信用评分特优")
                    
                else:
                    print(f"❌ 贷款收入比：{loan_to_income_ratio:.1f}倍（过高）")
                    approval_status = "拒绝"
                    rejection_reasons.append("贷款金额超过收入承受能力")
            else:
                print(f"❌ 工作年限：{employment_years}年（不足2年）")
                approval_status = "拒绝"
                rejection_reasons.append("工作年限不足，收入稳定性存疑")
                
        elif credit_score >= 650:
            print(f"⚠️ 信用评分：{credit_score}（一般）")
            base_interest_rate = 4.5
            
            # 一般信用评分的特殊审核
            if employment_years >= 3 and annual_income >= 60000:
                print("✅ 工作和收入补偿信用不足")
                if has_collateral and collateral_value >= loan_amount * 1.5:
                    approval_status = "条件批准"
                    interest_rate = base_interest_rate
                    special_conditions.append("需要提供额外财务证明")
                    special_conditions.append("贷款期间定期审查")
                else:
                    approval_status = "拒绝"
                    rejection_reasons.append("信用评分偏低且缺乏足够担保")
            else:
                approval_status = "拒绝"
                rejection_reasons.append("信用评分偏低")
                
        else:
            print(f"❌ 信用评分：{credit_score}（不足）")
            approval_status = "拒绝"
            rejection_reasons.append("信用评分过低（需要650以上）")
            
    else:
        print(f"❌ 债务收入比：{debt_to_income_ratio:.2%}（过高）")
        approval_status = "拒绝"
        rejection_reasons.append("债务负担过重")
        
else:
    print(f"❌ 年龄要求：{applicant_age}岁（不符合18-65岁要求）")
    approval_status = "拒绝"
    rejection_reasons.append("年龄不符合贷款要求")

# 输出审批结果
print("\n=== 审批结果 ===")
print(f"审批状态：{approval_status}")

if approval_status == "批准" or approval_status == "条件批准":
    print(f"批准金额：${loan_amount:,}")
    print(f"利率：{interest_rate:.2f}%")
    print(f"月还款额：${loan_amount * (interest_rate/100/12) * (1 + interest_rate/100/12)**360 / ((1 + interest_rate/100/12)**360 - 1):.2f}")
    
    if approval_reasons:
        print("\n批准原因：")
        for reason in approval_reasons:
            print(f"• {reason}")
    
    if special_conditions:
        print("\n特殊条件：")
        for condition in special_conditions:
            print(f"• {condition}")
else:
    print("\n拒绝原因：")
    for reason in rejection_reasons:
        print(f"• {reason}")
    
    print("\n改进建议：")
    if credit_score < 650:
        print("• 提高信用评分至650以上")
    if employment_years < 2:
        print("• 增加工作稳定性（至少2年）")
    if debt_to_income_ratio > 0.4:
        print("• 降低现有债务或增加收入")
```

## 性能优化和最佳实践

### 1. 避免过深嵌套

```python
# 不好的做法：过深嵌套
def process_order_bad(order):
    if order:
        if order.get('customer'):
            if order['customer'].get('is_vip'):
                if order.get('total') > 100:
                    if order.get('items'):
                        if len(order['items']) > 0:
                            return "VIP大额订单处理"
                        else:
                            return "空订单"
                    else:
                        return "无商品信息"
                else:
                    return "VIP小额订单"
            else:
                return "普通客户订单"
        else:
            return "无客户信息"
    else:
        return "无效订单"

# 好的做法：早期返回 + 扁平化
def process_order_good(order):
    # 早期返回处理异常情况
    if not order:
        return "无效订单"
    
    if not order.get('customer'):
        return "无客户信息"
    
    if not order.get('items') or len(order['items']) == 0:
        return "空订单"
    
    # 主要逻辑
    customer = order['customer']
    total = order.get('total', 0)
    
    if customer.get('is_vip'):
        if total > 100:
            return "VIP大额订单处理"
        else:
            return "VIP小额订单"
    else:
        return "普通客户订单"

# 测试两种方法
test_order = {
    'customer': {'is_vip': True},
    'total': 150,
    'items': ['item1', 'item2']
}

print("过深嵌套结果:", process_order_bad(test_order))
print("优化后结果:", process_order_good(test_order))
```

### 2. 使用函数分解复杂逻辑

```python
# 将复杂的嵌套逻辑分解为多个函数
class LoanApprovalSystem:
    def __init__(self):
        self.min_age = 18
        self.max_age = 65
        self.max_debt_ratio = 0.4
        self.min_credit_score = 650
        self.min_employment_years = 2
    
    def check_age_eligibility(self, age):
        """检查年龄资格"""
        return self.min_age <= age <= self.max_age
    
    def check_debt_ratio(self, annual_income, existing_debt, loan_amount):
        """检查债务收入比"""
        total_debt = existing_debt + loan_amount * 0.05
        ratio = total_debt / annual_income
        return ratio <= self.max_debt_ratio, ratio
    
    def check_credit_score(self, credit_score):
        """检查信用评分"""
        if credit_score >= 800:
            return "excellent", 3.5
        elif credit_score >= 700:
            return "good", 4.0
        elif credit_score >= 650:
            return "fair", 4.5
        else:
            return "poor", 0
    
    def check_employment_stability(self, employment_years):
        """检查就业稳定性"""
        return employment_years >= self.min_employment_years
    
    def calculate_interest_rate(self, base_rate, credit_score, has_collateral, is_first_time):
        """计算最终利率"""
        rate = base_rate
        
        if credit_score >= 800:
            rate -= 0.3
        
        if has_collateral:
            rate -= 0.5
        
        if is_first_time:
            rate -= 0.2
        
        return max(rate, 2.0)  # 最低利率2%
    
    def approve_loan(self, applicant_data):
        """主要审批逻辑"""
        # 基本资格检查
        if not self.check_age_eligibility(applicant_data['age']):
            return {
                'status': 'rejected',
                'reason': '年龄不符合要求'
            }
        
        # 债务比例检查
        debt_ok, debt_ratio = self.check_debt_ratio(
            applicant_data['annual_income'],
            applicant_data['existing_debt'],
            applicant_data['loan_amount']
        )
        
        if not debt_ok:
            return {
                'status': 'rejected',
                'reason': f'债务收入比过高: {debt_ratio:.2%}'
            }
        
        # 信用评分检查
        credit_level, base_rate = self.check_credit_score(applicant_data['credit_score'])
        
        if credit_level == 'poor':
            return {
                'status': 'rejected',
                'reason': '信用评分不足'
            }
        
        # 就业稳定性检查
        if not self.check_employment_stability(applicant_data['employment_years']):
            return {
                'status': 'rejected',
                'reason': '工作年限不足'
            }
        
        # 计算最终利率
        final_rate = self.calculate_interest_rate(
            base_rate,
            applicant_data['credit_score'],
            applicant_data['has_collateral'],
            applicant_data['is_first_time_buyer']
        )
        
        return {
            'status': 'approved',
            'loan_amount': applicant_data['loan_amount'],
            'interest_rate': final_rate,
            'credit_level': credit_level
        }

# 使用示例
loan_system = LoanApprovalSystem()

applicant = {
    'age': 30,
    'annual_income': 80000,
    'existing_debt': 15000,
    'loan_amount': 200000,
    'credit_score': 750,
    'employment_years': 5,
    'has_collateral': True,
    'is_first_time_buyer': True
}

result = loan_system.approve_loan(applicant)
print("审批结果:", result)
```

## 常见错误和调试技巧

### 1. 缩进错误

```python
# 错误示例：缩进不一致
age = 25
if age >= 18:
    print("成年人")
    if age >= 65:
        print("老年人")
  print("可以工作")  # 错误：缩进不正确

# 正确示例
age = 25
if age >= 18:
    print("成年人")
    if age >= 65:
        print("老年人")
    print("可以工作")  # 正确：与if同级
```

### 2. 逻辑错误

```python
# 错误示例：逻辑重叠
score = 85
if score >= 80:
    print("良好")
    if score >= 90:  # 这个条件永远不会单独为真
        print("优秀")

# 正确示例
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
```

### 3. 调试技巧

```python
# 使用调试输出跟踪执行路径
def debug_nested_conditions(temperature, humidity, is_raining):
    print(f"DEBUG: 输入参数 - 温度:{temperature}, 湿度:{humidity}, 下雨:{is_raining}")
    
    if temperature > 25:
        print("DEBUG: 进入高温分支")
        if humidity > 80:
            print("DEBUG: 高湿度子分支")
            if is_raining:
                print("DEBUG: 雨天子分支")
                return "高温高湿雨天：建议室内活动"
            else:
                return "高温高湿：注意防暑"
        else:
            print("DEBUG: 低湿度子分支")
            return "高温低湿：适合户外活动"
    else:
        print("DEBUG: 进入低温分支")
        return "温度适宜"

# 测试调试
result = debug_nested_conditions(30, 85, True)
print(f"最终结果: {result}")
```

## 练习题

### 基础练习

1. **学生奖学金评定**：
   - 根据成绩、出勤率、课外活动综合评定
   - 实现多层次的奖学金等级

2. **员工绩效评估**：
   - 考虑工作表现、团队合作、创新能力
   - 给出详细的评估报告和改进建议

3. **智能家居控制**：
   - 根据时间、温度、光线自动调节设备
   - 考虑用户偏好和节能要求

### 进阶练习

1. **电商推荐系统**：
   - 根据用户历史、偏好、当前浏览推荐商品
   - 实现个性化推荐逻辑

2. **交通信号控制**：
   - 根据车流量、时间段、特殊情况调整信号
   - 优化交通流量

3. **医疗诊断辅助**：
   - 根据症状、年龄、病史给出初步建议
   - 实现多层次的诊断逻辑

### 挑战练习

1. **智能投资顾问**：
   - 根据风险偏好、年龄、收入推荐投资组合
   - 考虑市场条件和个人目标

2. **游戏AI决策系统**：
   - 实现复杂的游戏AI决策逻辑
   - 考虑多种游戏状态和策略

## 学习要点

1. **层次结构**：理解嵌套条件的层次关系
2. **代码组织**：学会合理组织复杂的条件逻辑
3. **性能优化**：掌握避免过深嵌套的技巧
4. **可读性**：保持代码的清晰和可维护性
5. **调试技能**：学会调试复杂的嵌套逻辑

通过掌握嵌套条件语句，你可以处理复杂的多层次逻辑判断。接下来学习逻辑运算符，可以更灵活地组合条件表达式。