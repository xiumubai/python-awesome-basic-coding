# 日期时间处理

本节学习Python标准库中datetime模块的使用，这是处理日期和时间的核心模块。

## 学习目标

- 掌握datetime模块的基本用法
- 学会日期时间的创建、格式化和解析
- 理解时间间隔的计算
- 了解时区处理的基本方法

## datetime基本功能

datetime模块提供了处理日期和时间的类和函数。

### 获取当前日期时间

```python
from datetime import date, time, datetime as dt, timedelta, timezone

# 获取当前日期和时间
now = dt.now()
today = date.today()
current_time = dt.now().time()

print(f"当前日期时间: {now}")
print(f"当前日期: {today}")
print(f"当前时间: {current_time}")
```

### 创建特定日期时间

```python
# 创建特定的日期时间
specific_date = date(2024, 12, 25)
specific_time = time(14, 30, 0)
specific_datetime = dt(2024, 12, 25, 14, 30, 0)

print(f"特定日期: {specific_date}")
print(f"特定时间: {specific_time}")
print(f"特定日期时间: {specific_datetime}")
```

### 日期时间组成部分

```python
now = dt.now()

# 获取各个组成部分
print(f"年份: {now.year}")
print(f"月份: {now.month}")
print(f"日期: {now.day}")
print(f"小时: {now.hour}")
print(f"分钟: {now.minute}")
print(f"秒数: {now.second}")
print(f"微秒: {now.microsecond}")
print(f"星期几: {now.weekday()}")  # 0=周一, 6=周日
print(f"ISO星期几: {now.isoweekday()}")  # 1=周一, 7=周日
```

## 日期时间格式化

### 标准格式化

```python
now = dt.now()

# 标准格式
print(f"原始格式: {now}")
print(f"ISO格式: {now.isoformat()}")
print(f"日期ISO格式: {now.date().isoformat()}")
print(f"时间ISO格式: {now.time().isoformat()}")
```

### 自定义格式化

```python
# 使用strftime进行自定义格式化
formats = [
    ("%Y-%m-%d", "年-月-日"),
    ("%Y/%m/%d", "年/月/日"),
    ("%d/%m/%Y", "日/月/年"),
    ("%Y-%m-%d %H:%M:%S", "完整日期时间"),
    ("%Y年%m月%d日", "中文日期"),
    ("%A, %B %d, %Y", "英文完整格式"),
    ("%a %b %d %H:%M:%S %Y", "简短英文格式")
]

for fmt, description in formats:
    formatted = now.strftime(fmt)
    print(f"{description}: {formatted}")
```

### 字符串解析

```python
# 使用strptime从字符串解析日期时间
date_strings = [
    ("2024-12-25", "%Y-%m-%d"),
    ("25/12/2024", "%d/%m/%Y"),
    ("2024-12-25 14:30:00", "%Y-%m-%d %H:%M:%S"),
    ("Dec 25, 2024", "%b %d, %Y")
]

for date_str, fmt in date_strings:
    try:
        parsed = dt.strptime(date_str, fmt)
        print(f"'{date_str}' -> {parsed}")
    except ValueError as e:
        print(f"'{date_str}' -> 解析失败: {e}")
```

## 时间间隔计算

### 基本时间间隔

```python
from datetime import timedelta

now = dt.now()

# 创建时间间隔
one_day = timedelta(days=1)
one_week = timedelta(weeks=1)
one_hour = timedelta(hours=1)
thirty_minutes = timedelta(minutes=30)

print(f"当前时间: {now}")
print(f"一天后: {now + one_day}")
print(f"一周后: {now + one_week}")
print(f"一小时后: {now + one_hour}")
print(f"30分钟后: {now + thirty_minutes}")
```

### 复杂时间间隔

```python
# 复杂时间间隔
complex_delta = timedelta(days=7, hours=3, minutes=30, seconds=45)
print(f"复杂时间间隔: {complex_delta}")
print(f"总秒数: {complex_delta.total_seconds()}")
print(f"应用后的时间: {now + complex_delta}")
```

### 日期差值计算

```python
# 计算两个日期之间的差值
birthday = dt(2024, 1, 1)
new_year = dt(2025, 1, 1)

diff = new_year - birthday
print(f"从 {birthday.date()} 到 {new_year.date()}")
print(f"相差: {diff.days} 天")
print(f"相差: {diff.total_seconds()} 秒")
```

### 实用日期计算

```python
now = dt.now()

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
```

## 时区处理

### 基本时区操作

```python
from datetime import timezone

# UTC时间
utc_now = dt.now(timezone.utc)
local_now = dt.now()

print(f"本地时间: {local_now}")
print(f"UTC时间: {utc_now}")
```

### 时区转换

```python
# 创建带时区的时间
utc_tz = timezone.utc
beijing_tz = timezone(timedelta(hours=8))  # 北京时间 UTC+8

utc_time = dt(2024, 12, 25, 12, 0, 0, tzinfo=utc_tz)
beijing_time = utc_time.astimezone(beijing_tz)

print(f"UTC时间: {utc_time}")
print(f"北京时间: {beijing_time}")
```

### 多时区转换

```python
# 多个时区转换
timezones = {
    'UTC': timezone.utc,
    'Beijing': timezone(timedelta(hours=8)),
    'Tokyo': timezone(timedelta(hours=9)),
    'London': timezone(timedelta(hours=0)),
    'New York': timezone(timedelta(hours=-5))
}

base_time = dt(2024, 12, 25, 12, 0, 0, tzinfo=timezone.utc)

for tz_name, tz in timezones.items():
    converted = base_time.astimezone(tz)
    print(f"{tz_name}: {converted.strftime('%Y-%m-%d %H:%M:%S %Z')}")
```

## 日历操作

```python
import calendar

now = dt.now()

# 月历显示
print(f"当前月份日历 ({now.year}年{now.month}月):")
cal = calendar.monthcalendar(now.year, now.month)

print("  Mo Tu We Th Fr Sa Su")
for week in cal:
    week_str = ""
    for day in week:
        if day == 0:
            week_str += "   "
        else:
            week_str += f"{day:3d}"
    print(f" {week_str}")

# 日历信息
print(f"今年是否闰年: {calendar.isleap(now.year)}")
print(f"本月天数: {calendar.monthrange(now.year, now.month)[1]}")
print(f"本月第一天是星期几: {calendar.monthrange(now.year, now.month)[0]}")
```

## 性能计时

```python
import time as time_module

# 使用time模块计时
start_time = time_module.time()

# 模拟工作
total = sum(range(1000000))

end_time = time_module.time()
elapsed = end_time - start_time

print(f"计算结果: {total}")
print(f"耗时: {elapsed:.6f} 秒")

# 使用datetime计时
start_dt = dt.now()

# 模拟工作
result = sum(range(1000000))

end_dt = dt.now()
elapsed_dt = end_dt - start_dt

print(f"使用datetime计时: {elapsed_dt.total_seconds():.6f} 秒")
```

## 实际应用示例

### 年龄计算

```python
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
```

### 工作日判断

```python
def is_workday(check_date):
    """判断是否为工作日 (周一到周五)"""
    return check_date.weekday() < 5

def next_workday(start_date):
    """获取下一个工作日"""
    next_day = start_date + timedelta(days=1)
    while not is_workday(next_day):
        next_day += timedelta(days=1)
    return next_day

today = dt.now().date()
print(f"今天是工作日吗: {is_workday(today)}")
print(f"下一个工作日: {next_workday(today)}")
```

### 倒计时计算

```python
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
print(f"距离2025年新年还有: {countdown}")
```

### 日期范围生成

```python
def date_range(start_date, end_date, step_days=1):
    """生成日期范围"""
    current = start_date
    while current <= end_date:
        yield current
        current += timedelta(days=step_days)

start = date(2024, 12, 25)
end = date(2024, 12, 31)
print(f"从 {start} 到 {end} 的所有日期:")
for d in date_range(start, end):
    weekday_name = ['周一', '周二', '周三', '周四', '周五', '周六', '周日'][d.weekday()]
    print(f"  {d} ({weekday_name})")
```

## 学习要点

### 重点知识

1. **datetime模块**：提供完整的日期时间处理功能
2. **格式化和解析**：使用strftime()格式化，strptime()解析字符串
3. **时间间隔**：timedelta用于时间间隔计算和日期运算
4. **时区处理**：使用timezone类处理不同时区
5. **日历功能**：calendar模块提供日历相关功能

### 注意事项

1. **时区意识**：处理时区时要明确是否需要时区信息
2. **格式字符串**：strftime和strptime的格式字符串要匹配
3. **闰年处理**：日期计算时要考虑闰年情况
4. **性能考虑**：大量时间计算时选择合适的方法
5. **本地化**：不同地区的日期时间格式可能不同

### 实践建议

1. 熟练掌握常用的日期时间格式
2. 理解时区转换的原理和方法
3. 学会使用timedelta进行日期运算
4. 掌握实际应用中的日期时间处理技巧
5. 注意处理边界情况和异常情况

## 运行示例

```bash
# 运行完整示例
python3 02_datetime_module.py
```

通过本节学习，你将掌握Python中日期时间处理的各种方法，能够处理实际项目中的时间相关需求。