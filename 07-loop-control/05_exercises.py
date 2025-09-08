#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
循环控制 - 综合练习

本文件包含循环控制的综合练习，涵盖break、continue、else子句
以及各种循环控制技巧的实际应用。

练习目标：
1. 综合运用break、continue和else子句
2. 解决实际的编程问题
3. 提高循环控制的熟练度
4. 学会分析和优化循环逻辑
"""

# 练习1: 数字猜测游戏
print("=== 练习1: 数字猜测游戏 ===")

def number_guessing_game():
    """数字猜测游戏"""
    import random
    
    target = random.randint(1, 100)
    max_attempts = 7
    
    print(f"猜数字游戏！我想了一个1-100之间的数字，你有{max_attempts}次机会。")
    
    # 模拟用户输入
    guesses = [50, 75, 88, 82, 85, 87, 86]  # 假设目标是86
    target = 86  # 为了演示，固定目标
    
    for attempt in range(max_attempts):
        guess = guesses[attempt] if attempt < len(guesses) else target
        print(f"\n第{attempt + 1}次猜测: {guess}")
        
        if guess == target:
            print(f"🎉 恭喜！你猜对了！数字就是 {target}")
            print(f"你用了 {attempt + 1} 次猜测")
            break
        elif guess < target:
            print("太小了！")
        else:
            print("太大了！")
    else:
        print(f"\n😞 很遗憾，你没有在{max_attempts}次内猜中。")
        print(f"正确答案是: {target}")

number_guessing_game()
print()

# 练习2: 素数查找器
print("=== 练习2: 素数查找器 ===")

def find_primes(start, end, max_count=None):
    """查找指定范围内的素数"""
    primes = []
    
    for num in range(start, end + 1):
        if num < 2:
            continue  # 跳过小于2的数
        
        # 检查是否为素数
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break  # 不是素数
        else:
            primes.append(num)
            print(f"找到素数: {num}")
            
            # 如果指定了最大数量，检查是否达到
            if max_count and len(primes) >= max_count:
                print(f"已找到{max_count}个素数，停止搜索")
                break
    
    return primes

# 查找前10个素数
print("查找2-50范围内的前5个素数:")
primes = find_primes(2, 50, max_count=5)
print(f"结果: {primes}\n")

# 练习3: 文本处理器
print("=== 练习3: 文本处理器 ===")

def process_text(text):
    """处理文本，统计单词和字符"""
    words = []
    current_word = ""
    word_count = 0
    char_count = 0
    
    for char in text:
        char_count += 1
        
        # 跳过标点符号和数字
        if not char.isalpha() and not char.isspace():
            print(f"跳过特殊字符: '{char}'")
            continue
        
        # 处理空格
        if char.isspace():
            if current_word:
                words.append(current_word)
                word_count += 1
                print(f"完成单词: '{current_word}'")
                current_word = ""
            continue
        
        # 累积字母
        current_word += char.lower()
    
    # 处理最后一个单词
    if current_word:
        words.append(current_word)
        word_count += 1
        print(f"完成单词: '{current_word}'")
    
    return words, word_count, char_count

test_text = "Hello, World! 123 Python is great."
print(f"处理文本: '{test_text}'")
words, word_count, char_count = process_text(test_text)
print(f"\n结果:")
print(f"单词列表: {words}")
print(f"单词数量: {word_count}")
print(f"字符数量: {char_count}\n")

# 练习4: 数据验证器
print("=== 练习4: 数据验证器 ===")

def validate_user_data(users):
    """验证用户数据"""
    valid_users = []
    error_count = 0
    max_errors = 3
    
    for i, user in enumerate(users):
        print(f"\n验证用户 {i + 1}: {user}")
        
        # 检查必需字段
        required_fields = ['name', 'email', 'age']
        for field in required_fields:
            if field not in user or not user[field]:
                print(f"  ❌ 缺少必需字段: {field}")
                error_count += 1
                break
        else:
            # 所有必需字段都存在，继续验证
            
            # 验证年龄
            if not isinstance(user['age'], int) or user['age'] < 0 or user['age'] > 150:
                print(f"  ❌ 年龄无效: {user['age']}")
                error_count += 1
                continue
            
            # 验证邮箱
            if '@' not in user['email'] or '.' not in user['email']:
                print(f"  ❌ 邮箱格式无效: {user['email']}")
                error_count += 1
                continue
            
            # 验证姓名
            if len(user['name']) < 2:
                print(f"  ❌ 姓名太短: {user['name']}")
                error_count += 1
                continue
            
            # 所有验证通过
            valid_users.append(user)
            print(f"  ✅ 用户数据有效")
        
        # 检查错误数量
        if error_count >= max_errors:
            print(f"\n⚠️ 错误过多 ({error_count})，停止验证")
            break
    
    return valid_users, error_count

# 测试数据
test_users = [
    {'name': 'Alice', 'email': 'alice@example.com', 'age': 25},
    {'name': '', 'email': 'bob@example.com', 'age': 30},  # 姓名为空
    {'name': 'Charlie', 'email': 'invalid-email', 'age': 35},  # 邮箱无效
    {'name': 'David', 'email': 'david@example.com', 'age': -5},  # 年龄无效
    {'name': 'Eve', 'email': 'eve@example.com', 'age': 28}
]

valid_users, error_count = validate_user_data(test_users)
print(f"\n验证完成:")
print(f"有效用户数量: {len(valid_users)}")
print(f"错误数量: {error_count}\n")

# 练习5: 游戏分数统计
print("=== 练习5: 游戏分数统计 ===")

def analyze_game_scores(scores):
    """分析游戏分数"""
    total_score = 0
    valid_scores = 0
    high_scores = []
    bonus_rounds = 0
    
    print("分析游戏分数:")
    
    for round_num, score in enumerate(scores, 1):
        print(f"\n第{round_num}轮: {score}")
        
        # 跳过无效分数
        if score is None or score < 0:
            print(f"  跳过无效分数: {score}")
            continue
        
        # 检查是否为奖励轮
        if score == 0:
            print(f"  第{round_num}轮得分为0，跳过")
            continue
        
        # 累计有效分数
        total_score += score
        valid_scores += 1
        print(f"  累计分数: {total_score}")
        
        # 检查高分
        if score >= 100:
            high_scores.append((round_num, score))
            print(f"  🌟 高分轮次！")
            
            # 连续高分奖励
            if len(high_scores) >= 2:
                prev_round = high_scores[-2][0]
                if round_num - prev_round == 1:
                    bonus_rounds += 1
                    total_score += 50  # 奖励分数
                    print(f"  🎉 连续高分奖励！+50分")
        
        # 检查是否达到目标分数
        if total_score >= 500:
            print(f"  🏆 达到目标分数500！游戏结束")
            break
    else:
        print(f"\n所有轮次完成")
    
    return {
        'total_score': total_score,
        'valid_rounds': valid_scores,
        'high_scores': high_scores,
        'bonus_rounds': bonus_rounds
    }

# 测试游戏分数
game_scores = [85, 120, 95, None, 110, 0, 130, 75, 105, 90]
result = analyze_game_scores(game_scores)

print(f"\n游戏统计:")
print(f"总分: {result['total_score']}")
print(f"有效轮次: {result['valid_rounds']}")
print(f"高分轮次: {len(result['high_scores'])}")
print(f"奖励轮次: {result['bonus_rounds']}\n")

# 练习6: 密码强度检查器
print("=== 练习6: 密码强度检查器 ===")

def check_password_strength(password):
    """检查密码强度"""
    print(f"检查密码: {'*' * len(password)}")
    
    # 密码要求
    requirements = {
        'length': False,      # 至少8位
        'uppercase': False,   # 包含大写字母
        'lowercase': False,   # 包含小写字母
        'digit': False,       # 包含数字
        'special': False      # 包含特殊字符
    }
    
    # 检查长度
    if len(password) >= 8:
        requirements['length'] = True
        print("✅ 长度符合要求 (≥8位)")
    else:
        print("❌ 长度不足 (<8位)")
    
    # 检查字符类型
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    for char in password:
        if char.isupper():
            if not requirements['uppercase']:
                requirements['uppercase'] = True
                print("✅ 包含大写字母")
        elif char.islower():
            if not requirements['lowercase']:
                requirements['lowercase'] = True
                print("✅ 包含小写字母")
        elif char.isdigit():
            if not requirements['digit']:
                requirements['digit'] = True
                print("✅ 包含数字")
        elif char in special_chars:
            if not requirements['special']:
                requirements['special'] = True
                print("✅ 包含特殊字符")
        
        # 如果所有要求都满足，提前退出
        if all(requirements.values()):
            print("🎉 所有要求都满足！")
            break
    else:
        # 检查未满足的要求
        missing = []
        if not requirements['uppercase']:
            missing.append("大写字母")
        if not requirements['lowercase']:
            missing.append("小写字母")
        if not requirements['digit']:
            missing.append("数字")
        if not requirements['special']:
            missing.append("特殊字符")
        
        if missing:
            print(f"❌ 缺少: {', '.join(missing)}")
    
    # 计算强度分数
    score = sum(requirements.values())
    strength_levels = ['很弱', '弱', '一般', '强', '很强']
    strength = strength_levels[min(score, 4)]
    
    return {
        'score': score,
        'strength': strength,
        'requirements': requirements
    }

# 测试不同强度的密码
test_passwords = [
    "123",                    # 很弱
    "password",               # 弱
    "Password",               # 一般
    "Password123",            # 强
    "Password123!",           # 很强
]

for password in test_passwords:
    result = check_password_strength(password)
    print(f"强度: {result['strength']} (分数: {result['score']}/5)\n")

print("=== 循环控制综合练习总结 ===")
print("1. break用于提前退出循环")
print("2. continue用于跳过当前迭代")
print("3. else子句在循环正常结束时执行")
print("4. 合理使用循环控制可以提高代码效率")
print("5. 在复杂逻辑中，循环控制是重要的工具")
print("6. 实际应用中要考虑性能和可读性的平衡")