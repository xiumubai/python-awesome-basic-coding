#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
条件语句综合练习

本文件包含各种条件语句的综合练习，涵盖：
1. 基础练习：简单的条件判断
2. 进阶练习：复杂的逻辑组合
3. 实际应用：模拟真实场景
4. 挑战练习：综合运用所有知识点

学习目标：
- 综合运用所有条件语句知识
- 解决实际编程问题
- 提高逻辑思维能力
- 掌握代码优化技巧
"""

# 1. 基础练习
print("=== 1. 基础练习 ===")

# 练习1.1：判断数字的性质
def analyze_number(num):
    """分析数字的各种性质"""
    print(f"\n分析数字: {num}")
    
    # 正负性
    if num > 0:
        sign = "正数"
    elif num < 0:
        sign = "负数"
    else:
        sign = "零"
    
    # 奇偶性
    parity = "偶数" if num % 2 == 0 else "奇数"
    
    # 大小范围
    if abs(num) < 10:
        size = "个位数"
    elif abs(num) < 100:
        size = "两位数"
    elif abs(num) < 1000:
        size = "三位数"
    else:
        size = "多位数"
    
    print(f"  性质: {sign}, {parity}, {size}")
    
    # 特殊数字判断
    if num == 0:
        print("  特殊: 这是零")
    elif num in [1, -1]:
        print("  特殊: 这是单位数")
    elif num > 0 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1:
        print("  特殊: 这是质数")
    elif num > 0 and num == int(num**0.5)**2:
        print("  特殊: 这是完全平方数")

# 测试数字分析
test_numbers = [0, 1, -5, 16, 23, 100, -144, 1001]
for number in test_numbers:
    analyze_number(number)

print()

# 练习1.2：成绩等级判定系统
def grade_system(score, subject="数学"):
    """成绩等级判定"""
    # 输入验证
    if not isinstance(score, (int, float)):
        return "错误：分数必须是数字"
    
    if not (0 <= score <= 100):
        return "错误：分数必须在0-100之间"
    
    # 等级判定
    if score >= 95:
        grade = "A+"
        comment = "优秀"
    elif score >= 90:
        grade = "A"
        comment = "优秀"
    elif score >= 85:
        grade = "B+"
        comment = "良好"
    elif score >= 80:
        grade = "B"
        comment = "良好"
    elif score >= 75:
        grade = "C+"
        comment = "中等"
    elif score >= 70:
        grade = "C"
        comment = "中等"
    elif score >= 60:
        grade = "D"
        comment = "及格"
    else:
        grade = "F"
        comment = "不及格"
    
    # 特殊情况
    if score == 100:
        special = "满分！"
    elif score >= 98:
        special = "接近满分"
    elif score == 60:
        special = "刚好及格"
    elif score < 60 and score >= 50:
        special = "接近及格"
    else:
        special = ""
    
    result = f"{subject}成绩: {score}分 -> {grade} ({comment})"
    if special:
        result += f" {special}"
    
    return result

# 测试成绩系统
test_scores = [100, 95, 87, 75, 60, 45, 0, 105, "abc"]
for score in test_scores:
    print(grade_system(score))

print()

# 2. 进阶练习
print("=== 2. 进阶练习 ===")

# 练习2.1：用户登录验证系统
class LoginSystem:
    def __init__(self):
        self.users = {
            "admin": {"password": "admin123", "role": "administrator", "attempts": 0, "locked": False},
            "user1": {"password": "pass123", "role": "user", "attempts": 0, "locked": False},
            "user2": {"password": "mypass", "role": "user", "attempts": 2, "locked": False},
        }
        self.max_attempts = 3
    
    def login(self, username, password):
        """用户登录验证"""
        # 检查用户是否存在
        if username not in self.users:
            return False, "用户不存在"
        
        user = self.users[username]
        
        # 检查账户是否被锁定
        if user["locked"]:
            return False, "账户已被锁定，请联系管理员"
        
        # 检查登录尝试次数
        if user["attempts"] >= self.max_attempts:
            user["locked"] = True
            return False, "登录尝试次数过多，账户已被锁定"
        
        # 验证密码
        if user["password"] == password:
            user["attempts"] = 0  # 重置尝试次数
            return True, f"登录成功！欢迎 {username} ({user['role']})"
        else:
            user["attempts"] += 1
            remaining = self.max_attempts - user["attempts"]
            if remaining > 0:
                return False, f"密码错误，还有 {remaining} 次尝试机会"
            else:
                user["locked"] = True
                return False, "密码错误次数过多，账户已被锁定"
    
    def reset_user(self, username):
        """重置用户状态（管理员功能）"""
        if username in self.users:
            self.users[username]["attempts"] = 0
            self.users[username]["locked"] = False
            return f"用户 {username} 状态已重置"
        return "用户不存在"

# 测试登录系统
login_sys = LoginSystem()
test_logins = [
    ("admin", "admin123"),  # 正确
    ("user1", "wrong"),     # 错误密码
    ("user1", "wrong"),     # 错误密码
    ("user1", "pass123"),   # 正确
    ("user2", "wrong"),     # 错误密码（已有2次尝试）
    ("user2", "mypass"),    # 正确但可能被锁定
    ("nonuser", "any"),     # 用户不存在
]

print("登录测试:")
for username, password in test_logins:
    success, message = login_sys.login(username, password)
    status = "✓" if success else "✗"
    print(f"{status} {username}: {message}")

print()

# 练习2.2：智能推荐系统
def recommend_activity(weather, temperature, time_of_day, season, user_preferences):
    """根据多种条件推荐活动"""
    recommendations = []
    
    # 基于天气的推荐
    if weather == "sunny":
        if temperature > 25:
            recommendations.extend(["游泳", "海滩活动", "户外烧烤"])
        elif temperature > 15:
            recommendations.extend(["徒步", "骑自行车", "公园散步"])
        else:
            recommendations.extend(["户外摄影", "短途徒步"])
    elif weather == "rainy":
        recommendations.extend(["看电影", "读书", "室内游戏", "博物馆参观"])
    elif weather == "cloudy":
        if temperature > 20:
            recommendations.extend(["户外运动", "城市探索"])
        else:
            recommendations.extend(["咖啡厅", "购物"])
    elif weather == "snowy":
        recommendations.extend(["滑雪", "堆雪人", "室内活动"])
    
    # 基于时间的推荐
    if time_of_day == "morning":
        recommendations.extend(["晨跑", "瑜伽", "早餐"])
    elif time_of_day == "afternoon":
        recommendations.extend(["午餐", "购物", "会友"])
    elif time_of_day == "evening":
        recommendations.extend(["晚餐", "看电影", "散步"])
    elif time_of_day == "night":
        recommendations.extend(["夜景观赏", "酒吧", "在家休息"])
    
    # 基于季节的推荐
    if season == "spring":
        recommendations.extend(["赏花", "踏青", "放风筝"])
    elif season == "summer":
        recommendations.extend(["游泳", "冰淇淋", "夜市"])
    elif season == "autumn":
        recommendations.extend(["赏叶", "登山", "采摘"])
    elif season == "winter":
        recommendations.extend(["温泉", "火锅", "室内运动"])
    
    # 基于用户偏好过滤
    if "outdoor" not in user_preferences:
        recommendations = [r for r in recommendations if r not in ["徒步", "骑自行车", "户外烧烤", "户外摄影", "户外运动"]]
    
    if "sports" not in user_preferences:
        recommendations = [r for r in recommendations if r not in ["游泳", "晨跑", "瑜伽", "室内运动", "滑雪"]]
    
    if "food" in user_preferences:
        recommendations.extend(["美食探索", "烹饪", "品酒"])
    
    # 去重并返回前5个推荐
    unique_recommendations = list(dict.fromkeys(recommendations))[:5]
    
    return unique_recommendations

# 测试推荐系统
test_scenarios = [
    {"weather": "sunny", "temperature": 28, "time_of_day": "afternoon", "season": "summer", "user_preferences": ["outdoor", "sports"]},
    {"weather": "rainy", "temperature": 15, "time_of_day": "evening", "season": "autumn", "user_preferences": ["indoor", "food"]},
    {"weather": "snowy", "temperature": -5, "time_of_day": "morning", "season": "winter", "user_preferences": ["sports", "outdoor"]},
]

print("活动推荐:")
for i, scenario in enumerate(test_scenarios, 1):
    recommendations = recommend_activity(**scenario)
    print(f"场景 {i}: {scenario['weather']}, {scenario['temperature']}°C, {scenario['time_of_day']}, {scenario['season']}")
    print(f"用户偏好: {scenario['user_preferences']}")
    print(f"推荐活动: {', '.join(recommendations)}")
    print()

# 3. 实际应用练习
print("=== 3. 实际应用练习 ===")

# 练习3.1：电商折扣计算系统
class DiscountCalculator:
    def __init__(self):
        self.vip_levels = {
            "bronze": 0.05,
            "silver": 0.10,
            "gold": 0.15,
            "platinum": 0.20
        }
    
    def calculate_discount(self, original_price, user_type="regular", vip_level=None, 
                         quantity=1, is_first_purchase=False, coupon_discount=0):
        """计算最终价格和折扣"""
        total_price = original_price * quantity
        total_discount = 0
        discount_details = []
        
        # VIP折扣
        if user_type == "vip" and vip_level in self.vip_levels:
            vip_discount = self.vip_levels[vip_level]
            vip_amount = total_price * vip_discount
            total_discount += vip_amount
            discount_details.append(f"VIP {vip_level} 折扣: -{vip_amount:.2f}")
        
        # 数量折扣
        if quantity >= 10:
            quantity_discount = total_price * 0.1
            total_discount += quantity_discount
            discount_details.append(f"批量购买折扣(10+): -{quantity_discount:.2f}")
        elif quantity >= 5:
            quantity_discount = total_price * 0.05
            total_discount += quantity_discount
            discount_details.append(f"批量购买折扣(5+): -{quantity_discount:.2f}")
        
        # 首次购买折扣
        if is_first_purchase:
            first_purchase_discount = min(total_price * 0.1, 50)  # 最多50元
            total_discount += first_purchase_discount
            discount_details.append(f"首次购买折扣: -{first_purchase_discount:.2f}")
        
        # 优惠券折扣
        if coupon_discount > 0:
            coupon_amount = min(coupon_discount, total_price * 0.5)  # 最多50%
            total_discount += coupon_amount
            discount_details.append(f"优惠券折扣: -{coupon_amount:.2f}")
        
        # 计算最终价格
        final_price = max(total_price - total_discount, 0)
        
        # 满减活动
        if final_price >= 500:
            full_reduction = 50
            final_price -= full_reduction
            discount_details.append(f"满500减50: -{full_reduction}")
        elif final_price >= 200:
            full_reduction = 20
            final_price -= full_reduction
            discount_details.append(f"满200减20: -{full_reduction}")
        
        return {
            "original_total": total_price,
            "final_price": final_price,
            "total_saved": total_price - final_price,
            "discount_rate": (total_price - final_price) / total_price * 100,
            "discount_details": discount_details
        }

# 测试折扣计算
discount_calc = DiscountCalculator()
test_purchases = [
    {"original_price": 100, "user_type": "regular", "quantity": 1},
    {"original_price": 100, "user_type": "vip", "vip_level": "gold", "quantity": 6},
    {"original_price": 50, "user_type": "regular", "quantity": 12, "is_first_purchase": True},
    {"original_price": 200, "user_type": "vip", "vip_level": "platinum", "quantity": 3, "coupon_discount": 30},
]

print("折扣计算测试:")
for i, purchase in enumerate(test_purchases, 1):
    result = discount_calc.calculate_discount(**purchase)
    print(f"\n购买场景 {i}:")
    print(f"原价总计: ¥{result['original_total']:.2f}")
    print(f"最终价格: ¥{result['final_price']:.2f}")
    print(f"节省金额: ¥{result['total_saved']:.2f} ({result['discount_rate']:.1f}%)")
    if result['discount_details']:
        print("折扣明细:")
        for detail in result['discount_details']:
            print(f"  - {detail}")

print()

# 练习3.2：智能交通信号灯系统
class TrafficLightSystem:
    def __init__(self):
        self.current_time = 0  # 模拟时间（小时）
        self.traffic_density = "normal"  # low, normal, high
        self.emergency_vehicle = False
        self.pedestrian_waiting = False
    
    def get_light_timing(self, direction="north_south"):
        """根据条件计算信号灯时间"""
        base_green = 30  # 基础绿灯时间
        base_yellow = 5
        base_red = 35
        
        # 根据交通密度调整
        if self.traffic_density == "high":
            green_time = base_green + 15
            red_time = base_red + 10
        elif self.traffic_density == "low":
            green_time = base_green - 10
            red_time = base_red - 5
        else:
            green_time = base_green
            red_time = base_red
        
        # 根据时间段调整（高峰期）
        if (7 <= self.current_time <= 9) or (17 <= self.current_time <= 19):
            green_time += 10
            red_time += 5
        
        # 夜间模式
        elif 22 <= self.current_time or self.current_time <= 6:
            green_time = max(green_time - 15, 15)
            red_time = max(red_time - 10, 20)
        
        # 紧急车辆优先
        if self.emergency_vehicle:
            return {"green": 60, "yellow": 3, "red": 10, "mode": "emergency"}
        
        # 行人等待
        if self.pedestrian_waiting:
            green_time = min(green_time + 10, 60)
        
        return {
            "green": green_time,
            "yellow": base_yellow,
            "red": red_time,
            "mode": "normal"
        }
    
    def simulate_day(self):
        """模拟一天的交通信号"""
        scenarios = [
            {"time": 6, "density": "low", "emergency": False, "pedestrian": False},
            {"time": 8, "density": "high", "emergency": False, "pedestrian": True},
            {"time": 12, "density": "normal", "emergency": False, "pedestrian": True},
            {"time": 18, "density": "high", "emergency": True, "pedestrian": False},
            {"time": 23, "density": "low", "emergency": False, "pedestrian": False},
        ]
        
        print("交通信号灯一天模拟:")
        for scenario in scenarios:
            self.current_time = scenario["time"]
            self.traffic_density = scenario["density"]
            self.emergency_vehicle = scenario["emergency"]
            self.pedestrian_waiting = scenario["pedestrian"]
            
            timing = self.get_light_timing()
            
            print(f"\n时间: {scenario['time']:02d}:00")
            print(f"交通密度: {scenario['density']}, 紧急车辆: {scenario['emergency']}, 行人等待: {scenario['pedestrian']}")
            print(f"信号时间 - 绿灯: {timing['green']}s, 黄灯: {timing['yellow']}s, 红灯: {timing['red']}s")
            print(f"模式: {timing['mode']}")

# 运行交通信号灯模拟
traffic_system = TrafficLightSystem()
traffic_system.simulate_day()

print()

# 4. 挑战练习
print("=== 4. 挑战练习 ===")

# 练习4.1：复杂的游戏角色战斗系统
class Character:
    def __init__(self, name, level, health, mana, attack, defense, agility):
        self.name = name
        self.level = level
        self.max_health = health
        self.health = health
        self.max_mana = mana
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.status_effects = []
    
    def can_use_skill(self, skill_name):
        """检查是否可以使用技能"""
        skills = {
            "fireball": {"mana_cost": 20, "min_level": 5},
            "heal": {"mana_cost": 15, "min_level": 3},
            "lightning": {"mana_cost": 30, "min_level": 8},
            "shield": {"mana_cost": 10, "min_level": 2},
        }
        
        if skill_name not in skills:
            return False, "未知技能"
        
        skill = skills[skill_name]
        
        if self.level < skill["min_level"]:
            return False, f"等级不足，需要等级 {skill['min_level']}"
        
        if self.mana < skill["mana_cost"]:
            return False, f"魔法值不足，需要 {skill['mana_cost']} 点魔法值"
        
        if "silence" in self.status_effects:
            return False, "沉默状态，无法使用技能"
        
        return True, "可以使用"
    
    def calculate_damage(self, target, skill_type="normal"):
        """计算伤害"""
        base_damage = self.attack
        
        # 技能伤害修正
        if skill_type == "fireball":
            base_damage *= 1.5
        elif skill_type == "lightning":
            base_damage *= 2.0
        elif skill_type == "critical":
            base_damage *= 2.5
        
        # 等级差异
        level_diff = self.level - target.level
        if level_diff > 0:
            base_damage *= (1 + level_diff * 0.1)
        elif level_diff < 0:
            base_damage *= (1 + level_diff * 0.05)
        
        # 防御计算
        defense_reduction = target.defense / (target.defense + 100)
        final_damage = base_damage * (1 - defense_reduction)
        
        # 状态效果
        if "weakness" in target.status_effects:
            final_damage *= 1.3
        if "shield" in target.status_effects:
            final_damage *= 0.7
        
        return max(int(final_damage), 1)
    
    def get_battle_status(self):
        """获取战斗状态"""
        health_percent = (self.health / self.max_health) * 100
        mana_percent = (self.mana / self.max_mana) * 100
        
        if health_percent <= 0:
            return "defeated"
        elif health_percent <= 20:
            return "critical"
        elif health_percent <= 50:
            return "wounded"
        elif mana_percent <= 20:
            return "exhausted"
        else:
            return "healthy"

def battle_simulation(char1, char2):
    """战斗模拟"""
    print(f"\n=== 战斗开始: {char1.name} vs {char2.name} ===")
    
    round_num = 1
    while char1.health > 0 and char2.health > 0 and round_num <= 10:
        print(f"\n第 {round_num} 回合:")
        
        # 决定行动顺序（基于敏捷）
        if char1.agility >= char2.agility:
            attacker, defender = char1, char2
        else:
            attacker, defender = char2, char1
        
        # 攻击者行动
        attacker_status = attacker.get_battle_status()
        
        if attacker_status == "critical" and attacker.mana >= 15:
            # 危急时使用治疗
            can_heal, _ = attacker.can_use_skill("heal")
            if can_heal:
                heal_amount = 30
                attacker.health = min(attacker.health + heal_amount, attacker.max_health)
                attacker.mana -= 15
                print(f"{attacker.name} 使用治疗，恢复 {heal_amount} 生命值")
            else:
                damage = attacker.calculate_damage(defender)
                defender.health -= damage
                print(f"{attacker.name} 普通攻击 {defender.name}，造成 {damage} 伤害")
        
        elif attacker.mana >= 30 and attacker.level >= 8:
            # 有足够魔法值使用强力技能
            can_use, _ = attacker.can_use_skill("lightning")
            if can_use:
                damage = attacker.calculate_damage(defender, "lightning")
                defender.health -= damage
                attacker.mana -= 30
                print(f"{attacker.name} 使用闪电术，造成 {damage} 伤害")
            else:
                damage = attacker.calculate_damage(defender)
                defender.health -= damage
                print(f"{attacker.name} 普通攻击 {defender.name}，造成 {damage} 伤害")
        
        elif attacker.mana >= 20 and attacker.level >= 5:
            # 使用火球术
            can_use, _ = attacker.can_use_skill("fireball")
            if can_use:
                damage = attacker.calculate_damage(defender, "fireball")
                defender.health -= damage
                attacker.mana -= 20
                print(f"{attacker.name} 使用火球术，造成 {damage} 伤害")
            else:
                damage = attacker.calculate_damage(defender)
                defender.health -= damage
                print(f"{attacker.name} 普通攻击 {defender.name}，造成 {damage} 伤害")
        
        else:
            # 普通攻击
            damage = attacker.calculate_damage(defender)
            defender.health -= damage
            print(f"{attacker.name} 普通攻击 {defender.name}，造成 {damage} 伤害")
        
        # 显示状态
        print(f"{char1.name}: HP {max(char1.health, 0)}/{char1.max_health}, MP {char1.mana}/{char1.max_mana}")
        print(f"{char2.name}: HP {max(char2.health, 0)}/{char2.max_health}, MP {char2.mana}/{char2.max_mana}")
        
        round_num += 1
    
    # 战斗结果
    if char1.health <= 0:
        print(f"\n{char2.name} 获胜！")
    elif char2.health <= 0:
        print(f"\n{char1.name} 获胜！")
    else:
        print("\n战斗平局！")

# 创建角色并进行战斗
warrior = Character("战士", 10, 150, 50, 45, 30, 20)
mage = Character("法师", 8, 100, 120, 35, 15, 25)

battle_simulation(warrior, mage)

print()
print("=== 所有练习完成 ===")

# 总结练习要点
print("\n=== 练习总结 ===")
print("通过这些练习，你应该掌握了：")
print("1. 基本条件语句的使用（if, elif, else）")
print("2. 逻辑运算符的组合使用（and, or, not）")
print("3. 比较运算符的各种应用")
print("4. 条件表达式的简洁写法")
print("5. 复杂业务逻辑的条件判断")
print("6. 实际项目中的条件语句应用")
print("7. 代码优化和可读性提升")

# 进阶挑战
print("\n=== 进阶挑战题 ===")
print("1. 实现一个完整的学生管理系统（成绩、出勤、奖惩等多维度判断）")
print("2. 编写一个智能家居控制系统（温度、湿度、时间、用户偏好等条件）")
print("3. 设计一个复杂的游戏AI决策系统（多种策略选择）")
print("4. 实现一个金融风险评估系统（多指标综合判断）")
print("5. 创建一个智能推荐算法（用户行为、偏好、历史数据等）")