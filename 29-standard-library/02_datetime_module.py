#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02_datetime_module.py - 日期时间处理

本文件演示Python标准库中datetime模块的使用：
- datetime类：日期和时间的表示
- date类：日期的表示
- time类：时间的表示
- timedelta类：时间间隔的计算
- 时区处理和格式化

学习目标：
1. 掌握datetime模块的基本用法
2. 学会日期时间的创建、格式化和解析
3. 理解时间间隔的计算
4. 了解时区处理的基本方法
"""

import datetime
from datetime import date, time, datetime as dt, timedelta, timezone
import time as time_module
import calendar


def demonstrate_datetime_basics():
    """演示datetime基本功能"""
    print("=" * 50)
    print("DateTime基本功能演示")
    print("=" * 50)
    
    # 1. 获取当前日期和时间
    now = dt.now()
    today = date.today()
    current_time = dt.now().time()
    
    print(f"当前日期时间: {now}")
    print(f"当前日期: {today}")
    print(f"当前时间: {current_time}")
    
    # 2. 创建特定的日期时间
    specific_date = date(2024, 12, 25)
    specific_time = time(14, 30, 0)
    specific_datetime = dt(2024, 12, 25, 14, 30, 0)
    
    print(f"\n特定日期: {specific_date}")
    print(f"特定时间: {specific_time}")
    print(f"特定日期时间: {specific_datetime}")
    
    # 3. 日期时间的各个组成部分
    print(f"\n日期时间组成部分:")
    print(f"年份: {now.year}")
    print(f"月份: {now.month}")
    print(f"日期: {now.day}")
    print(f"小时: {now.hour}")
    print(f"分钟: {now.minute}")
    print(f"秒数: {now.second}")
    print(f"微秒: {now.microsecond}")
    print(f"星期几: {now.weekday()} (0=周一, 6=周日)")
    print(f"ISO星期几: {now.isoweekday()} (1=周一, 7=周日)")


def demonstrate_datetime_formatting():
    """演示日期时间格式化"""
    print("\n" + "=" * 50)
    print("日期时间格式化演示")
    print("=" * 50)
    
    now = dt.now()
    
    # 1. 常用格式化
    print(f"原始格式: {now}")
    print(f"ISO格式: {now.isoformat()}")
    print(f"日期ISO格式: {now.date().isoformat()}")
    print(f"时间ISO格式: {now.time().isoformat()}")
    
    # 2. 自定义格式化
    print(f"\n自定义格式化:")
    formats = [
        ("%Y-%m-%d", "年-月-日"),
        ("%Y/%m/%d", "年/月/日"),
        ("%d/%m/%Y", "日/月/年"),
        ("%Y-%m-%d %H:%M:%S", "完整日期时间"),
        ("%Y年%m月%d日", "中文日期"),
        ("%Y年%m月%d日 %H时%M分%S秒", "中文日期时间"),
        ("%A, %B %d, %Y", "英文完整格式"),
        ("%a %b %d %H:%M:%S %Y", "简短英文格式")
    ]
    
    for fmt, description in formats:
        try:
            formatted = now.strftime(fmt)
            print(f"  {description}: {formatted}")
        except Exception as e:
            print(f"  {description}: 格式化失败 - {e}")
    
    # 3. 从字符串解析日期时间
    print(f"\n从字符串解析日期时间:")
    date_strings = [
        ("2024-12-25", "%Y-%m-%d"),
        ("25/12/2024", "%d/%m/%Y"),
        ("2024-12-25 14:30:00", "%Y-%m-%d %H:%M:%S"),
        ("Dec 25, 2024", "%b %d, %Y")
    ]
    
    for date_str, fmt in date_strings:
        try:
            parsed = dt.strptime(date_str, fmt)
            print(f"  '{date_str}' -> {parsed}")
        except ValueError as e:
            print(f"  '{date_str}' -> 解析失败: {e}")


def demonstrate_timedelta_operations():
    """演示时间间隔计算"""
    print("\n" + "=" * 50)
    print("时间间隔计算演示")
    print("=" * 50)
    
    now = dt.now()
    
    # 1. 创建时间间隔
    one_day = timedelta(days=1)
    one_week = timedelta(weeks=1)
    one_hour = timedelta(hours=1)
    thirty_minutes = timedelta(minutes=30)
    
    print(f"当前时间: {now}")
    print(f"\n时间间隔示例:")
    print(f"一天后: {now + one_day}")
    print(f"一周后: {now + one_week}")
    print(f"一小时后: {now + one_hour}")
    print(f"30分钟后: {now + thirty_minutes}")
    
    print(f"\n时间间隔计算:")
    print(f"一天前: {now - one_day}")
    print(f"一周前: {now - one_week}")
    
    # 2. 复杂时间间隔
    complex_delta = timedelta(days=7, hours=3, minutes=30, seconds=45)
    print(f"\n复杂时间间隔: {complex_delta}")
    print(f"总秒数: {complex_delta.total_seconds()}")
    print(f"应用后的时间: {now + complex_delta}")
    
    # 3. 计算两个日期之间的差值
    birthday = dt(2024, 1, 1)
    new_year = dt(2025, 1, 1)
    
    diff = new_year - birthday
    print(f"\n日期差值计算:")
    print(f"从 {birthday.date()} 到 {new_year.date()}")
    print(f"相差: {diff.days} 天")
    print(f"相差: {diff.total_seconds()} 秒")
    
    # 4. 实用的日期计算
    print(f"\n实用日期计算:")
    
    # 本月第一天
    first_day = now.replace(day=1)
    print(f"本月第一天: {first_day.date()}")
    
    # 下个月第一天
    if now.month == 12:
        next_month = now.replace(year=now.year + 1, month=1, day=1)
    else:
        next_month = now.replace(month=now.month + 1, day=1)
    print(f"下月第一天: {next_month.date()}")
    
    # 本月最后一天
    last_day = next_month - timedelta(days=1)
    print(f"本月最后一天: {last_day.date()}")


def demonstrate_timezone_handling():
    """演示时区处理"""
    print("\n" + "=" * 50)
    print("时区处理演示")
    print("=" * 50)
    
    # 1. UTC时间
    utc_now = dt.now(timezone.utc)
    local_now = dt.now()
    
    print(f"本地时间: {local_now}")
    print(f"UTC时间: {utc_now}")
    
    # 2. 创建带时区的时间
    utc_tz = timezone.utc
    beijing_tz = timezone(timedelta(hours=8))  # 北京时间 UTC+8
    
    utc_time = dt(2024, 12, 25, 12, 0, 0, tzinfo=utc_tz)
    beijing_time = utc_time.astimezone(beijing_tz)
    
    print(f"\nUTC时间: {utc_time}")
    print(f"北京时间: {beijing_time}")
    
    # 3. 时区转换
    print(f"\n时区转换示例:")
    
    # 创建几个不同时区
    timezones = {
        'UTC': timezone.utc,
        'Beijing': timezone(timedelta(hours=8)),
        'Tokyo': timezone(timedelta(hours=9)),
        'London': timezone(timedelta(hours=0)),  # 简化，实际需考虑夏令时
        'New York': timezone(timedelta(hours=-5))  # 简化，实际需考虑夏令时
    }
    
    base_time = dt(2024, 12, 25, 12, 0, 0, tzinfo=timezone.utc)
    
    for tz_name, tz in timezones.items():
        converted = base_time.astimezone(tz)
        print(f"  {tz_name}: {converted.strftime('%Y-%m-%d %H:%M:%S %Z')}")


def demonstrate_calendar_operations():
    """演示日历相关操作"""
    print("\n" + "=" * 50)
    print("日历操作演示")
    print("=" * 50)
    
    now = dt.now()
    
    # 1. 月历
    print(f"当前月份日历 ({now.year}年{now.month}月):")
    cal = calendar.monthcalendar(now.year, now.month)
    
    # 打印星期标题
    print("  Mo Tu We Th Fr Sa Su")
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                week_str += f"{day:3d}"
        print(f" {week_str}")
    
    # 2. 日历信息
    print(f"\n日历信息:")
    print(f"今年是否闰年: {calendar.isleap(now.year)}")
    print(f"本月天数: {calendar.monthrange(now.year, now.month)[1]}")
    print(f"本月第一天是星期几: {calendar.monthrange(now.year, now.month)[0]} (0=周一)")
    
    # 3. 星期名称
    print(f"\n星期名称:")
    print(f"英文星期名: {list(calendar.day_name)}")
    print(f"英文星期简称: {list(calendar.day_abbr)}")
    print(f"英文月份名: {list(calendar.month_name)[1:]}")
    print(f"英文月份简称: {list(calendar.month_abbr)[1:]}")


def demonstrate_performance_timing():
    """演示性能计时"""
    print("\n" + "=" * 50)
    print("性能计时演示")
    print("=" * 50)
    
    # 1. 使用time模块计时
    print("使用time模块计时:")
    start_time = time_module.time()
    
    # 模拟一些工作
    total = 0
    for i in range(1000000):
        total += i
    
    end_time = time_module.time()
    elapsed = end_time - start_time
    
    print(f"  计算1到1000000的和: {total}")
    print(f"  耗时: {elapsed:.6f} 秒")
    
    # 2. 使用datetime计时
    print(f"\n使用datetime计时:")
    start_dt = dt.now()
    
    # 模拟另一些工作
    result = sum(range(1000000))
    
    end_dt = dt.now()
    elapsed_dt = end_dt - start_dt
    
    print(f"  使用sum函数计算: {result}")
    print(f"  耗时: {elapsed_dt.total_seconds():.6f} 秒")
    
    # 3. 高精度计时
    print(f"\n高精度计时 (perf_counter):")
    start_perf = time_module.perf_counter()
    
    # 快速操作
    data = [i**2 for i in range(10000)]
    
    end_perf = time_module.perf_counter()
    elapsed_perf = end_perf - start_perf
    
    print(f"  生成10000个平方数")
    print(f"  耗时: {elapsed_perf:.6f} 秒")


def demonstrate_practical_examples():
    """演示实际应用示例"""
    print("\n" + "=" * 50)
    print("实际应用示例")
    print("=" * 50)
    
    now = dt.now()
    
    # 1. 年龄计算
    def calculate_age(birth_date):
        """计算年龄"""
        today = date.today()
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age
    
    birth = date(1990, 5, 15)
    age = calculate_age(birth)
    print(f"出生日期: {birth}")
    print(f"当前年龄: {age} 岁")
    
    # 2. 工作日计算
    def is_workday(check_date):
        """判断是否为工作日 (周一到周五)"""
        return check_date.weekday() < 5
    
    def next_workday(start_date):
        """获取下一个工作日"""
        next_day = start_date + timedelta(days=1)
        while not is_workday(next_day):
            next_day += timedelta(days=1)
        return next_day
    
    today = now.date()
    print(f"\n今天是工作日吗: {is_workday(today)}")
    print(f"下一个工作日: {next_workday(today)}")
    
    # 3. 倒计时计算
    def countdown_to_date(target_date):
        """计算到目标日期的倒计时"""
        now = dt.now()
        if isinstance(target_date, date) and not isinstance(target_date, dt):
            target_date = dt.combine(target_date, time())
        
        diff = target_date - now
        
        if diff.total_seconds() > 0:
            days = diff.days
            hours, remainder = divmod(diff.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{days}天 {hours}小时 {minutes}分钟 {seconds}秒"
        else:
            return "目标日期已过"
    
    new_year = dt(2025, 1, 1)
    countdown = countdown_to_date(new_year)
    print(f"\n距离2025年新年还有: {countdown}")
    
    # 4. 时间段判断
    def get_time_period(check_time=None):
        """判断时间段"""
        if check_time is None:
            check_time = dt.now().time()
        
        hour = check_time.hour
        
        if 5 <= hour < 12:
            return "上午"
        elif 12 <= hour < 18:
            return "下午"
        elif 18 <= hour < 22:
            return "晚上"
        else:
            return "深夜"
    
    current_period = get_time_period()
    print(f"\n当前时间段: {current_period}")
    
    # 5. 日期范围生成
    def date_range(start_date, end_date, step_days=1):
        """生成日期范围"""
        current = start_date
        while current <= end_date:
            yield current
            current += timedelta(days=step_days)
    
    start = date(2024, 12, 25)
    end = date(2024, 12, 31)
    print(f"\n从 {start} 到 {end} 的所有日期:")
    for d in date_range(start, end):
        weekday_name = ['周一', '周二', '周三', '周四', '周五', '周六', '周日'][d.weekday()]
        print(f"  {d} ({weekday_name})")


def main():
    """主函数 - 运行所有演示"""
    print("Python标准库 - datetime模块学习")
    print("本程序演示datetime模块的各种功能")
    
    try:
        demonstrate_datetime_basics()
        demonstrate_datetime_formatting()
        demonstrate_timedelta_operations()
        demonstrate_timezone_handling()
        demonstrate_calendar_operations()
        demonstrate_performance_timing()
        demonstrate_practical_examples()
        
        print("\n" + "=" * 50)
        print("学习要点总结:")
        print("=" * 50)
        print("1. datetime模块提供了完整的日期时间处理功能")
        print("2. 使用strftime()格式化，strptime()解析字符串")
        print("3. timedelta用于时间间隔计算和日期运算")
        print("4. 时区处理需要使用timezone类")
        print("5. calendar模块提供日历相关功能")
        print("6. 性能计时推荐使用time.perf_counter()")
        print("7. 实际应用中要注意闰年、工作日等特殊情况")
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"\n程序执行出错: {e}")
        import sys
        sys.exit(1)


if __name__ == "__main__":
    main()