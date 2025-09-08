# 循环控制综合练习

本章包含了循环控制的综合练习，涵盖了`break`、`continue`、`else`子句以及各种循环控制技巧的实际应用。通过这些练习，你将能够熟练掌握循环控制的各种技巧。

## 练习1：数字猜测游戏

这个练习展示了如何使用`break`、`continue`和循环计数来创建一个交互式游戏。

```python
import random

def number_guessing_game():
    """
    数字猜测游戏
    - 使用break在猜对时退出
    - 使用continue处理无效输入
    - 使用else子句处理游戏失败
    """
    print("=== 数字猜测游戏 ===")
    print("我想了一个1到100之间的数字，你有7次机会猜中它！")
    
    # 生成随机数
    secret_number = random.randint(1, 100)
    max_attempts = 7
    
    for attempt in range(1, max_attempts + 1):
        print(f"\n第 {attempt} 次尝试:")
        
        try:
            # 获取用户输入
            user_input = input("请输入你的猜测 (1-100): ")
            
            # 检查是否要退出
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("游戏退出！")
                print(f"答案是: {secret_number}")
                return
            
            # 转换为整数
            guess = int(user_input)
            
            # 验证输入范围
            if not 1 <= guess <= 100:
                print("请输入1到100之间的数字！")
                continue  # 跳过本次循环，不消耗尝试次数
            
            # 检查猜测结果
            if guess == secret_number:
                print(f"🎉 恭喜！你猜对了！答案就是 {secret_number}")
                print(f"你用了 {attempt} 次尝试")
                break  # 猜对了，退出循环
            elif guess < secret_number:
                print(f"太小了！还有 {max_attempts - attempt} 次机会")
            else:
                print(f"太大了！还有 {max_attempts - attempt} 次机会")
                
        except ValueError:
            print("请输入有效的数字！")
            continue  # 无效输入，不消耗尝试次数
    
    else:
        # 循环正常结束（没有被break），说明用完了所有尝试次数
        print(f"\n😞 很遗憾，你没有猜中！")
        print(f"答案是: {secret_number}")
        print("下次再来挑战吧！")

# 运行游戏
if __name__ == "__main__":
    number_guessing_game()
```

## 练习2：素数查找器

这个练习展示了如何使用`else`子句来优化素数检测算法。

```python
import math
import time

def find_primes_in_range(start, end, show_process=False):
    """
    在指定范围内查找所有素数
    - 使用for-else优化素数检测
    - 使用break提前退出
    - 展示算法优化技巧
    """
    print(f"查找 {start} 到 {end} 之间的素数...")
    
    primes = []
    start_time = time.time()
    
    for num in range(max(2, start), end + 1):
        if show_process:
            print(f"\n检测 {num}:")
        
        # 特殊情况：2是唯一的偶数素数
        if num == 2:
            primes.append(num)
            if show_process:
                print(f"  {num} 是素数（特殊情况）")
            continue
        
        # 跳过偶数（除了2）
        if num % 2 == 0:
            if show_process:
                print(f"  {num} 是偶数，跳过")
            continue
        
        # 检查奇数因子，只需检查到sqrt(num)
        limit = int(math.sqrt(num)) + 1
        
        for divisor in range(3, limit, 2):  # 只检查奇数
            if show_process:
                print(f"    检查是否能被 {divisor} 整除")
            
            if num % divisor == 0:
                if show_process:
                    print(f"    {num} = {divisor} × {num // divisor}，不是素数")
                break  # 找到因子，不是素数
        else:
            # 循环正常结束，没有找到因子，是素数
            primes.append(num)
            if show_process:
                print(f"  {num} 是素数")
    
    end_time = time.time()
    
    print(f"\n找到 {len(primes)} 个素数，耗时 {end_time - start_time:.4f} 秒")
    return primes

def sieve_of_eratosthenes(limit):
    """
    埃拉托斯特尼筛法：更高效的素数查找算法
    展示算法优化的重要性
    """
    print(f"使用筛法查找小于 {limit} 的所有素数...")
    
    start_time = time.time()
    
    # 创建布尔数组，初始都为True
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False  # 0和1不是素数
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            # 标记i的所有倍数为非素数
            for j in range(i * i, limit, i):
                is_prime[j] = False
    
    # 收集所有素数
    primes = [i for i in range(2, limit) if is_prime[i]]
    
    end_time = time.time()
    
    print(f"筛法找到 {len(primes)} 个素数，耗时 {end_time - start_time:.4f} 秒")
    return primes

# 测试素数查找器
if __name__ == "__main__":
    print("=== 素数查找器 ===")
    
    # 小范围详细演示
    print("\n1. 小范围详细演示:")
    small_primes = find_primes_in_range(10, 30, show_process=True)
    print(f"素数列表: {small_primes}")
    
    # 性能对比
    print("\n2. 性能对比:")
    range_limit = 1000
    
    method1_primes = find_primes_in_range(2, range_limit)
    method2_primes = sieve_of_eratosthenes(range_limit + 1)
    
    print(f"结果一致: {method1_primes == method2_primes}")
    print(f"前20个素数: {method1_primes[:20]}")
```

## 练习3：文本处理器

这个练习展示了如何使用`continue`来跳过不需要处理的数据。

```python
import re
from collections import Counter

def advanced_text_processor(text, options=None):
    """
    高级文本处理器
    - 使用continue跳过不需要的行
    - 使用break在满足条件时停止
    - 展示文本处理的实际应用
    """
    if options is None:
        options = {
            'skip_empty_lines': True,
            'skip_comments': True,
            'max_lines': None,
            'min_word_length': 2,
            'case_sensitive': False
        }
    
    print("=== 文本处理器 ===")
    print(f"处理选项: {options}")
    
    lines = text.strip().split('\n')
    processed_lines = []
    word_stats = Counter()
    line_stats = {
        'total': len(lines),
        'processed': 0,
        'skipped_empty': 0,
        'skipped_comments': 0,
        'skipped_short': 0
    }
    
    for line_num, line in enumerate(lines, 1):
        original_line = line
        line = line.strip()
        
        # 跳过空行
        if options['skip_empty_lines'] and not line:
            line_stats['skipped_empty'] += 1
            print(f"第 {line_num} 行: 跳过空行")
            continue
        
        # 跳过注释行
        if options['skip_comments'] and line.startswith('#'):
            line_stats['skipped_comments'] += 1
            print(f"第 {line_num} 行: 跳过注释 - {line[:30]}...")
            continue
        
        # 检查最大行数限制
        if options['max_lines'] and len(processed_lines) >= options['max_lines']:
            print(f"达到最大行数限制 ({options['max_lines']})，停止处理")
            break
        
        # 处理单词
        words = re.findall(r'\b\w+\b', line)
        
        if not options['case_sensitive']:
            words = [word.lower() for word in words]
        
        # 过滤短单词
        filtered_words = []
        for word in words:
            if len(word) >= options['min_word_length']:
                filtered_words.append(word)
                word_stats[word] += 1
            else:
                line_stats['skipped_short'] += 1
        
        if filtered_words:  # 只处理有有效单词的行
            processed_line = {
                'line_number': line_num,
                'original': original_line,
                'words': filtered_words,
                'word_count': len(filtered_words)
            }
            processed_lines.append(processed_line)
            line_stats['processed'] += 1
            
            print(f"第 {line_num} 行: 处理了 {len(filtered_words)} 个单词")
        else:
            print(f"第 {line_num} 行: 没有有效单词，跳过")
            continue
    
    # 生成处理报告
    print("\n=== 处理报告 ===")
    for key, value in line_stats.items():
        print(f"{key}: {value}")
    
    print(f"\n最常见的10个单词:")
    for word, count in word_stats.most_common(10):
        print(f"  {word}: {count}")
    
    return processed_lines, word_stats, line_stats

def analyze_code_file(filename):
    """
    分析代码文件的示例
    展示实际的文本处理应用
    """
    # 模拟代码文件内容
    code_content = """
# 这是一个Python文件示例
# 作者: 张三

import os
import sys

def hello_world():
    print("Hello, World!")
    return True

# 主函数
def main():
    # 调用hello_world函数
    result = hello_world()
    
    if result:
        print("程序执行成功")
    else:
        print("程序执行失败")

if __name__ == "__main__":
    main()
"""
    
    # 代码分析选项
    code_options = {
        'skip_empty_lines': True,
        'skip_comments': True,
        'max_lines': None,
        'min_word_length': 2,
        'case_sensitive': True  # 代码分析保持大小写敏感
    }
    
    print("分析代码文件:")
    return advanced_text_processor(code_content, code_options)

# 测试文本处理器
if __name__ == "__main__":
    # 测试基本文本处理
    sample_text = """
# 这是一个示例文本
这是第一行有用的内容

# 这是注释
这是第二行内容，包含更多单词
短行
这是一个很长的行，包含许多不同的单词和内容

# 另一个注释
最后一行内容
"""
    
    processed, words, stats = advanced_text_processor(sample_text)
    
    print("\n=== 代码文件分析 ===")
    code_processed, code_words, code_stats = analyze_code_file("example.py")
```

## 练习4：数据验证器

这个练习展示了如何结合使用多种循环控制技巧来验证复杂数据。

```python
import re
from datetime import datetime

class DataValidator:
    """
    数据验证器类
    展示循环控制在数据验证中的应用
    """
    
    def __init__(self):
        self.validation_rules = {
            'email': self._validate_email,
            'phone': self._validate_phone,
            'age': self._validate_age,
            'name': self._validate_name,
            'password': self._validate_password
        }
    
    def validate_batch(self, data_list, stop_on_first_error=False):
        """
        批量验证数据
        - 使用continue跳过无效记录
        - 使用break在遇到错误时停止（可选）
        - 使用else子句处理验证完成
        """
        print(f"开始批量验证 {len(data_list)} 条记录...")
        
        valid_records = []
        invalid_records = []
        
        for i, record in enumerate(data_list, 1):
            print(f"\n验证第 {i} 条记录: {record.get('name', 'Unknown')}")
            
            # 检查记录是否为空
            if not record:
                print(f"  跳过空记录")
                invalid_records.append({
                    'index': i,
                    'record': record,
                    'errors': ['记录为空']
                })
                continue
            
            # 验证单条记录
            is_valid, errors = self.validate_single(record)
            
            if is_valid:
                valid_records.append(record)
                print(f"  ✓ 记录有效")
            else:
                invalid_records.append({
                    'index': i,
                    'record': record,
                    'errors': errors
                })
                print(f"  ✗ 记录无效: {', '.join(errors)}")
                
                # 如果设置了遇到错误就停止
                if stop_on_first_error:
                    print(f"  遇到第一个错误，停止验证")
                    break
        else:
            # 循环正常结束，所有记录都已验证
            print(f"\n所有记录验证完成")
        
        # 生成验证报告
        self._generate_report(valid_records, invalid_records, len(data_list))
        
        return valid_records, invalid_records
    
    def validate_single(self, record):
        """
        验证单条记录
        返回 (是否有效, 错误列表)
        """
        errors = []
        
        # 检查必需字段
        required_fields = ['name', 'email', 'age']
        for field in required_fields:
            if field not in record or not record[field]:
                errors.append(f"缺少必需字段: {field}")
                continue  # 跳过对该字段的进一步验证
        
        # 验证各个字段
        for field, value in record.items():
            if field in self.validation_rules:
                field_errors = self.validation_rules[field](value)
                errors.extend(field_errors)
        
        return len(errors) == 0, errors
    
    def _validate_email(self, email):
        """验证邮箱格式"""
        errors = []
        
        if not isinstance(email, str):
            errors.append("邮箱必须是字符串")
            return errors
        
        # 基本格式检查
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            errors.append("邮箱格式无效")
        
        # 长度检查
        if len(email) > 254:
            errors.append("邮箱长度不能超过254字符")
        
        return errors
    
    def _validate_phone(self, phone):
        """验证手机号码"""
        errors = []
        
        if not isinstance(phone, str):
            errors.append("手机号必须是字符串")
            return errors
        
        # 移除所有非数字字符
        digits_only = re.sub(r'\D', '', phone)
        
        # 检查长度
        if len(digits_only) != 11:
            errors.append("手机号必须是11位数字")
        elif not digits_only.startswith('1'):
            errors.append("手机号必须以1开头")
        
        return errors
    
    def _validate_age(self, age):
        """验证年龄"""
        errors = []
        
        try:
            age_int = int(age)
            if age_int < 0:
                errors.append("年龄不能为负数")
            elif age_int > 150:
                errors.append("年龄不能超过150岁")
        except (ValueError, TypeError):
            errors.append("年龄必须是有效数字")
        
        return errors
    
    def _validate_name(self, name):
        """验证姓名"""
        errors = []
        
        if not isinstance(name, str):
            errors.append("姓名必须是字符串")
            return errors
        
        name = name.strip()
        
        if len(name) < 2:
            errors.append("姓名长度不能少于2个字符")
        elif len(name) > 50:
            errors.append("姓名长度不能超过50个字符")
        
        # 检查是否包含数字
        if re.search(r'\d', name):
            errors.append("姓名不能包含数字")
        
        return errors
    
    def _validate_password(self, password):
        """验证密码强度"""
        errors = []
        
        if not isinstance(password, str):
            errors.append("密码必须是字符串")
            return errors
        
        # 长度检查
        if len(password) < 8:
            errors.append("密码长度不能少于8位")
        
        # 复杂度检查
        checks = [
            (r'[a-z]', "密码必须包含小写字母"),
            (r'[A-Z]', "密码必须包含大写字母"),
            (r'\d', "密码必须包含数字"),
            (r'[!@#$%^&*(),.?":{}|<>]', "密码必须包含特殊字符")
        ]
        
        for pattern, error_msg in checks:
            if not re.search(pattern, password):
                errors.append(error_msg)
        
        return errors
    
    def _generate_report(self, valid_records, invalid_records, total):
        """生成验证报告"""
        print(f"\n=== 验证报告 ===")
        print(f"总记录数: {total}")
        print(f"有效记录: {len(valid_records)}")
        print(f"无效记录: {len(invalid_records)}")
        print(f"成功率: {len(valid_records)/total*100:.1f}%")
        
        if invalid_records:
            print(f"\n无效记录详情:")
            for record in invalid_records:
                print(f"  第 {record['index']} 条: {', '.join(record['errors'])}")

# 测试数据验证器
if __name__ == "__main__":
    validator = DataValidator()
    
    # 测试数据
    test_data = [
        {
            'name': '张三',
            'email': 'zhangsan@example.com',
            'age': 25,
            'phone': '13812345678',
            'password': 'StrongPass123!'
        },
        {
            'name': 'Li4',  # 包含数字，无效
            'email': 'invalid-email',  # 邮箱格式无效
            'age': -5,  # 年龄无效
            'phone': '123',  # 手机号无效
        },
        {},  # 空记录
        {
            'name': '王五',
            'email': 'wangwu@test.com',
            'age': 30,
            'phone': '13987654321'
        },
        {
            'name': '赵六',
            'email': 'zhaoliu@example.org',
            'age': 'invalid',  # 年龄格式无效
            'phone': '15612345678',
            'password': '123'  # 密码太简单
        }
    ]
    
    print("=== 数据验证器测试 ===")
    
    # 正常模式：验证所有记录
    print("\n1. 正常模式（验证所有记录）:")
    valid, invalid = validator.validate_batch(test_data, stop_on_first_error=False)
    
    # 严格模式：遇到错误就停止
    print("\n\n2. 严格模式（遇到错误就停止）:")
    valid_strict, invalid_strict = validator.validate_batch(test_data, stop_on_first_error=True)
```

## 练习5：游戏分数统计

这个练习展示了如何在游戏开发中使用循环控制来处理用户输入和游戏逻辑。

```python
import random
from collections import defaultdict

class GameScoreTracker:
    """
    游戏分数统计器
    展示循环控制在游戏开发中的应用
    """
    
    def __init__(self):
        self.players = {}
        self.game_history = []
        self.current_game = None
    
    def start_tournament(self, player_names, rounds_per_game=3):
        """
        开始锦标赛
        - 使用嵌套循环处理多轮游戏
        - 使用break处理提前结束
        - 使用continue跳过无效输入
        """
        print(f"=== 开始锦标赛 ===")
        print(f"参赛选手: {', '.join(player_names)}")
        print(f"每场游戏 {rounds_per_game} 轮")
        
        # 初始化玩家数据
        for name in player_names:
            self.players[name] = {
                'total_score': 0,
                'games_played': 0,
                'games_won': 0,
                'best_score': 0
            }
        
        game_number = 1
        
        while True:
            print(f"\n=== 第 {game_number} 场游戏 ===")
            
            # 询问是否继续
            if game_number > 1:
                continue_game = input("是否继续下一场游戏？(y/n): ").lower()
                if continue_game in ['n', 'no', 'quit', 'exit']:
                    print("锦标赛结束！")
                    break
                elif continue_game not in ['y', 'yes', '']:
                    print("无效输入，默认继续游戏")
                    continue
            
            # 开始一场游戏
            game_result = self.play_single_game(player_names, rounds_per_game)
            
            if game_result is None:
                print("游戏被取消")
                continue
            
            # 更新统计数据
            self.update_statistics(game_result)
            
            # 显示当前排名
            self.show_leaderboard()
            
            game_number += 1
        
        # 显示最终结果
        self.show_final_results()
    
    def play_single_game(self, player_names, rounds):
        """
        进行单场游戏
        """
        game_scores = {name: 0 for name in player_names}
        round_details = []
        
        for round_num in range(1, rounds + 1):
            print(f"\n--- 第 {round_num} 轮 ---")
            
            round_scores = {}
            
            for player in player_names:
                while True:  # 循环直到获得有效输入
                    try:
                        score_input = input(f"{player} 的得分 (0-100, 或输入 'skip' 跳过): ")
                        
                        if score_input.lower() == 'skip':
                            print(f"{player} 跳过本轮")
                            round_scores[player] = 0
                            break
                        
                        if score_input.lower() in ['quit', 'exit']:
                            print("游戏被取消")
                            return None
                        
                        score = int(score_input)
                        
                        if not 0 <= score <= 100:
                            print("分数必须在0-100之间！")
                            continue  # 重新输入
                        
                        round_scores[player] = score
                        break  # 输入有效，退出输入循环
                        
                    except ValueError:
                        print("请输入有效的数字！")
                        continue  # 重新输入
            
            # 更新总分
            for player, score in round_scores.items():
                game_scores[player] += score
            
            round_details.append(round_scores.copy())
            
            # 显示本轮结果
            print("本轮得分:", round_scores)
            print("累计得分:", game_scores)
        
        # 确定获胜者
        winner = max(game_scores.items(), key=lambda x: x[1])
        
        game_result = {
            'scores': game_scores,
            'winner': winner[0],
            'winning_score': winner[1],
            'round_details': round_details
        }
        
        print(f"\n🏆 本场游戏获胜者: {winner[0]} (得分: {winner[1]})")
        
        return game_result
    
    def update_statistics(self, game_result):
        """更新玩家统计数据"""
        winner = game_result['winner']
        
        for player, score in game_result['scores'].items():
            stats = self.players[player]
            stats['total_score'] += score
            stats['games_played'] += 1
            
            if player == winner:
                stats['games_won'] += 1
            
            if score > stats['best_score']:
                stats['best_score'] = score
        
        self.game_history.append(game_result)
    
    def show_leaderboard(self):
        """显示排行榜"""
        print("\n=== 当前排行榜 ===")
        
        # 按总分排序
        sorted_players = sorted(
            self.players.items(),
            key=lambda x: (x[1]['total_score'], x[1]['games_won']),
            reverse=True
        )
        
        for i, (name, stats) in enumerate(sorted_players, 1):
            avg_score = stats['total_score'] / max(1, stats['games_played'])
            win_rate = stats['games_won'] / max(1, stats['games_played']) * 100
            
            print(f"{i}. {name}:")
            print(f"   总分: {stats['total_score']}")
            print(f"   场次: {stats['games_played']}")
            print(f"   胜场: {stats['games_won']}")
            print(f"   胜率: {win_rate:.1f}%")
            print(f"   平均分: {avg_score:.1f}")
            print(f"   最高分: {stats['best_score']}")
            print()
    
    def show_final_results(self):
        """显示最终结果"""
        print("\n=== 锦标赛最终结果 ===")
        
        if not self.players:
            print("没有游戏数据")
            return
        
        # 找出各项冠军
        total_score_champion = max(self.players.items(), key=lambda x: x[1]['total_score'])
        most_wins_champion = max(self.players.items(), key=lambda x: x[1]['games_won'])
        best_single_game = max(self.players.items(), key=lambda x: x[1]['best_score'])
        
        print(f"🏆 总分冠军: {total_score_champion[0]} ({total_score_champion[1]['total_score']} 分)")
        print(f"🏆 胜场最多: {most_wins_champion[0]} ({most_wins_champion[1]['games_won']} 胜)")
        print(f"🏆 单场最高: {best_single_game[0]} ({best_single_game[1]['best_score']} 分)")
        
        # 显示游戏历史
        print(f"\n总共进行了 {len(self.game_history)} 场游戏")
        
        self.show_leaderboard()

# 测试游戏分数统计器
if __name__ == "__main__":
    tracker = GameScoreTracker()
    
    # 模拟锦标赛
    players = ['Alice', 'Bob', 'Charlie']
    
    print("游戏分数统计器演示")
    print("注意：这是一个交互式演示，需要用户输入")
    print("在实际运行时，请按提示输入分数")
    
    # 为了演示，我们创建一些模拟数据
    print("\n=== 模拟游戏数据 ===")
    
    # 模拟几场游戏的结果
    mock_games = [
        {
            'scores': {'Alice': 85, 'Bob': 92, 'Charlie': 78},
            'winner': 'Bob',
            'winning_score': 92,
            'round_details': []
        },
        {
            'scores': {'Alice': 95, 'Bob': 88, 'Charlie': 91},
            'winner': 'Alice',
            'winning_score': 95,
            'round_details': []
        },
        {
            'scores': {'Alice': 82, 'Bob': 85, 'Charlie': 96},
            'winner': 'Charlie',
            'winning_score': 96,
            'round_details': []
        }
    ]
    
    # 初始化玩家
    for name in players:
        tracker.players[name] = {
            'total_score': 0,
            'games_played': 0,
            'games_won': 0,
            'best_score': 0
        }
    
    # 处理模拟游戏
    for i, game in enumerate(mock_games, 1):
        print(f"\n处理第 {i} 场游戏...")
        tracker.update_statistics(game)
    
    # 显示最终结果
    tracker.show_final_results()
    
    # 如果要运行真实的交互式锦标赛，取消下面的注释
    # tracker.start_tournament(players, rounds_per_game=2)
```

## 练习6：密码强度检查器

这个练习展示了如何使用循环控制来实现复杂的验证逻辑。

```python
import re
import string
from collections import Counter

class PasswordStrengthChecker:
    """
    密码强度检查器
    展示循环控制在安全验证中的应用
    """
    
    def __init__(self):
        self.common_passwords = {
            '123456', 'password', '123456789', '12345678', '12345',
            '1234567', '1234567890', 'qwerty', 'abc123', 'million2',
            '000000', '1234', 'iloveyou', 'aaron431', 'password1',
            'qqww1122', '123', 'omgpop', '123321', '654321'
        }
        
        self.keyboard_patterns = [
            'qwerty', 'asdf', 'zxcv', '1234', '4321',
            'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
        ]
    
    def check_password_strength(self, password, username=None, show_details=True):
        """
        检查密码强度
        - 使用多个循环检查不同的安全要求
        - 使用continue跳过某些检查
        - 使用break在发现严重问题时停止
        """
        if show_details:
            print(f"检查密码强度: {'*' * len(password)}")
        
        score = 0
        issues = []
        suggestions = []
        
        # 基本长度检查
        if len(password) < 8:
            issues.append("密码长度不足8位")
            suggestions.append("使用至少8个字符")
        elif len(password) >= 12:
            score += 2
        else:
            score += 1
        
        # 字符类型检查
        char_types = {
            'lowercase': False,
            'uppercase': False,
            'digits': False,
            'special': False
        }
        
        for char in password:
            if char.islower():
                char_types['lowercase'] = True
            elif char.isupper():
                char_types['uppercase'] = True
            elif char.isdigit():
                char_types['digits'] = True
            elif char in string.punctuation:
                char_types['special'] = True
        
        # 评估字符类型多样性
        types_used = sum(char_types.values())
        score += types_used
        
        if not char_types['lowercase']:
            issues.append("缺少小写字母")
            suggestions.append("添加小写字母")
        
        if not char_types['uppercase']:
            issues.append("缺少大写字母")
            suggestions.append("添加大写字母")
        
        if not char_types['digits']:
            issues.append("缺少数字")
            suggestions.append("添加数字")
        
        if not char_types['special']:
            issues.append("缺少特殊字符")
            suggestions.append("添加特殊字符 (!@#$%^&* 等)")
        
        # 检查常见密码
        if password.lower() in self.common_passwords:
            issues.append("使用了常见密码")
            suggestions.append("避免使用常见密码")
            score -= 3  # 严重扣分
        
        # 检查与用户名的关系
        if username and self._contains_username(password, username):
            issues.append("密码包含用户名")
            suggestions.append("避免在密码中使用用户名")
            score -= 2
        
        # 检查重复字符
        repeat_score, repeat_issues = self._check_repetition(password)
        score += repeat_score
        issues.extend(repeat_issues)
        
        # 检查键盘模式
        if self._has_keyboard_pattern(password):
            issues.append("包含键盘模式")
            suggestions.append("避免使用键盘上连续的字符")
            score -= 1
        
        # 检查数字模式
        if self._has_number_pattern(password):
            issues.append("包含简单数字模式")
            suggestions.append("避免使用连续数字或简单数字模式")
            score -= 1
        
        # 计算最终强度
        strength = self._calculate_strength(score)
        
        if show_details:
            self._show_detailed_report(password, score, strength, issues, suggestions)
        
        return {
            'score': score,
            'strength': strength,
            'issues': issues,
            'suggestions': suggestions
        }
    
    def _contains_username(self, password, username):
        """检查密码是否包含用户名"""
        password_lower = password.lower()
        username_lower = username.lower()
        
        # 检查完整用户名
        if username_lower in password_lower:
            return True
        
        # 检查用户名的子串（长度>=3）
        for i in range(len(username_lower) - 2):
            for j in range(i + 3, len(username_lower) + 1):
                substring = username_lower[i:j]
                if substring in password_lower:
                    return True
        
        return False
    
    def _check_repetition(self, password):
        """检查字符重复情况"""
        score = 0
        issues = []
        
        # 统计字符频率
        char_count = Counter(password.lower())
        
        # 检查过度重复
        max_repeat = max(char_count.values())
        if max_repeat > len(password) // 2:
            issues.append("字符重复过多")
            score -= 2
        elif max_repeat > 3:
            issues.append("存在重复字符")
            score -= 1
        
        # 检查连续重复
        consecutive_count = 1
        max_consecutive = 1
        
        for i in range(1, len(password)):
            if password[i].lower() == password[i-1].lower():
                consecutive_count += 1
                max_consecutive = max(max_consecutive, consecutive_count)
            else:
                consecutive_count = 1
        
        if max_consecutive > 2:
            issues.append(f"存在{max_consecutive}个连续相同字符")
            score -= 1
        
        return score, issues
    
    def _has_keyboard_pattern(self, password):
        """检查键盘模式"""
        password_lower = password.lower()
        
        for pattern in self.keyboard_patterns:
            # 正向检查
            if pattern in password_lower:
                return True
            # 反向检查
            if pattern[::-1] in password_lower:
                return True
        
        return False
    
    def _has_number_pattern(self, password):
        """检查数字模式"""
        # 提取所有数字
        numbers = ''.join(re.findall(r'\d', password))
        
        if len(numbers) < 3:
            return False
        
        # 检查连续数字
        for i in range(len(numbers) - 2):
            if (int(numbers[i+1]) == int(numbers[i]) + 1 and 
                int(numbers[i+2]) == int(numbers[i]) + 2):
                return True
            
            # 检查连续递减
            if (int(numbers[i+1]) == int(numbers[i]) - 1 and 
                int(numbers[i+2]) == int(numbers[i]) - 2):
                return True
        
        # 检查重复数字模式
        if re.search(r'(\d)\1{2,}', numbers):
            return True
        
        return False
    
    def _calculate_strength(self, score):
        """根据分数计算强度等级"""
        if score < 3:
            return "很弱"
        elif score < 5:
            return "弱"
        elif score < 7:
            return "中等"
        elif score < 9:
            return "强"
        else:
            return "很强"
    
    def _show_detailed_report(self, password, score, strength, issues, suggestions):
        """显示详细报告"""
        print(f"\n=== 密码强度报告 ===")
        print(f"密码长度: {len(password)}")
        print(f"强度评分: {score}/10")
        print(f"强度等级: {strength}")
        
        if issues:
            print(f"\n发现的问题:")
            for i, issue in enumerate(issues, 1):
                print(f"  {i}. {issue}")
        
        if suggestions:
            print(f"\n改进建议:")
            for i, suggestion in enumerate(suggestions, 1):
                print(f"  {i}. {suggestion}")
        
        # 强度条显示
        strength_bar = "█" * min(10, max(0, score)) + "░" * max(0, 10 - score)
        print(f"\n强度条: [{strength_bar}]")
    
    def batch_check_passwords(self, passwords, usernames=None):
        """
        批量检查密码
        展示循环控制在批量处理中的应用
        """
        print(f"=== 批量密码强度检查 ===")
        print(f"检查 {len(passwords)} 个密码...\n")
        
        results = []
        
        for i, password in enumerate(passwords):
            username = usernames[i] if usernames and i < len(usernames) else None
            
            print(f"检查第 {i+1} 个密码...")
            
            # 跳过空密码
            if not password:
                print("  跳过空密码\n")
                results.append(None)
                continue
            
            result = self.check_password_strength(password, username, show_details=False)
            results.append(result)
            
            print(f"  强度: {result['strength']} (评分: {result['score']}/10)")
            if result['issues']:
                print(f"  问题: {', '.join(result['issues'][:2])}{'...' if len(result['issues']) > 2 else ''}")
            print()
        
        # 生成统计报告
        self._generate_batch_report(results)
        
        return results
    
    def _generate_batch_report(self, results):
        """生成批量检查报告"""
        valid_results = [r for r in results if r is not None]
        
        if not valid_results:
            print("没有有效的检查结果")
            return
        
        print("=== 批量检查统计 ===")
        
        # 强度分布
        strength_count = Counter(r['strength'] for r in valid_results)
        print("强度分布:")
        for strength in ["很弱", "弱", "中等", "强", "很强"]:
            count = strength_count.get(strength, 0)
            percentage = count / len(valid_results) * 100
            print(f"  {strength}: {count} ({percentage:.1f}%)")
        
        # 平均分数
        avg_score = sum(r['score'] for r in valid_results) / len(valid_results)
        print(f"\n平均评分: {avg_score:.1f}/10")
        
        # 常见问题
        all_issues = []
        for result in valid_results:
            all_issues.extend(result['issues'])
        
        if all_issues:
            issue_count = Counter(all_issues)
            print(f"\n最常见的问题:")
            for issue, count in issue_count.most_common(5):
                percentage = count / len(valid_results) * 100
                print(f"  {issue}: {count} ({percentage:.1f}%)")

# 测试密码强度检查器
if __name__ == "__main__":
    checker = PasswordStrengthChecker()
    
    print("=== 密码强度检查器测试 ===")
    
    # 单个密码测试
    test_passwords = [
        ("123456", "john"),
        ("Password123!", "alice"),
        ("MyStr0ng!P@ssw0rd", "bob"),
        ("qwerty123", "charlie"),
        ("Tr0ub4dor&3", "david")
    ]
    
    print("\n1. 单个密码详细检查:")
    for password, username in test_passwords[:2]:
        print(f"\n检查密码 (用户: {username}):")
        result = checker.check_password_strength(password, username)
    
    # 批量测试
    print("\n\n2. 批量密码检查:")
    batch_passwords = [pwd for pwd, _ in test_passwords]
    batch_usernames = [usr for _, usr in test_passwords]
    
    batch_results = checker.batch_check_passwords(batch_passwords, batch_usernames)
```

## 总结

通过这些综合练习，我们学习了：

### 循环控制技巧应用

1. **break语句**：在找到目标、满足条件或遇到错误时提前退出
2. **continue语句**：跳过无效数据、错误输入或不需要处理的项目
3. **else子句**：处理循环正常结束的情况，如搜索失败、验证完成等
4. **嵌套循环控制**：使用标志变量、函数返回或异常来控制多层循环

### 实际应用场景

1. **用户交互**：游戏、输入验证、菜单系统
2. **数据处理**：批量验证、文本分析、数据清洗
3. **搜索算法**：查找元素、模式匹配、条件筛选
4. **错误处理**：异常恢复、重试机制、优雅降级
5. **性能优化**：早期退出、批处理、资源管理

### 最佳实践

1. **选择合适的控制语句**：根据具体需求选择break、continue或else
2. **保持代码可读性**：使用有意义的变量名和注释
3. **处理边界情况**：空数据、无效输入、异常情况
4. **优化性能**：避免不必要的计算和循环
5. **提供用户反馈**：进度显示、错误信息、操作提示

### 学习建议

1. **多练习**：通过实际项目加深理解
2. **读源码**：学习优秀项目中的循环控制技巧
3. **性能测试**：比较不同实现方式的效率
4. **代码审查**：与他人交流学习最佳实践
5. **持续改进**：不断优化和重构代码

掌握这些循环控制技巧，将帮助你编写更高效、更可靠、更易维护的Python程序。