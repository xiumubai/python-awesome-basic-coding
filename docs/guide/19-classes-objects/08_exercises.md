# 综合练习

## 学习目标
- 综合运用类和对象的所有知识点
- 掌握面向对象程序设计的实际应用
- 学会设计和实现完整的类系统
- 提高代码组织和结构设计能力
- 理解面向对象编程的最佳实践

## 练习1：银行账户管理系统

### 需求分析
设计一个银行账户管理系统，包含基本账户、储蓄账户和信用账户三种类型。

```python
from datetime import datetime
from abc import ABC, abstractmethod

class BankAccount:
    """银行账户基类"""
    
    # 类属性
    _account_counter = 0
    _total_accounts = 0
    _bank_name = "Python银行"
    _interest_rate = 0.02  # 基础利率2%
    
    def __init__(self, owner_name, initial_balance=0):
        """初始化账户"""
        # 生成账户号
        BankAccount._account_counter += 1
        BankAccount._total_accounts += 1
        
        # 实例属性
        self._account_number = f"ACC{BankAccount._account_counter:06d}"
        self._owner_name = owner_name
        self._balance = initial_balance
        self._created_at = datetime.now()
        self._transaction_history = []
        self._is_active = True
        
        # 记录开户交易
        if initial_balance > 0:
            self._add_transaction("开户存款", initial_balance, self._balance)
        
        print(f"账户创建成功: {self._account_number} - {owner_name}")
    
    # 私有方法
    def _add_transaction(self, transaction_type, amount, balance_after):
        """添加交易记录"""
        transaction = {
            "时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "类型": transaction_type,
            "金额": amount,
            "余额": balance_after
        }
        self._transaction_history.append(transaction)
    
    def _validate_amount(self, amount):
        """验证金额"""
        if not isinstance(amount, (int, float)):
            raise TypeError("金额必须是数字")
        if amount <= 0:
            raise ValueError("金额必须大于0")
        return True
    
    def _check_account_active(self):
        """检查账户是否激活"""
        if not self._is_active:
            raise Exception(f"账户 {self._account_number} 已被冻结")
    
    # 公共方法
    def deposit(self, amount):
        """存款"""
        self._check_account_active()
        self._validate_amount(amount)
        
        self._balance += amount
        self._add_transaction("存款", amount, self._balance)
        
        print(f"存款成功: {amount:.2f}，当前余额: {self._balance:.2f}")
        return self._balance
    
    def withdraw(self, amount):
        """取款"""
        self._check_account_active()
        self._validate_amount(amount)
        
        if amount > self._balance:
            raise ValueError(f"余额不足，当前余额: {self._balance:.2f}")
        
        self._balance -= amount
        self._add_transaction("取款", -amount, self._balance)
        
        print(f"取款成功: {amount:.2f}，当前余额: {self._balance:.2f}")
        return self._balance
    
    def transfer(self, target_account, amount):
        """转账"""
        self._check_account_active()
        target_account._check_account_active()
        self._validate_amount(amount)
        
        if amount > self._balance:
            raise ValueError(f"余额不足，当前余额: {self._balance:.2f}")
        
        # 执行转账
        self._balance -= amount
        target_account._balance += amount
        
        # 记录交易
        self._add_transaction(f"转出到{target_account._account_number}", -amount, self._balance)
        target_account._add_transaction(f"转入自{self._account_number}", amount, target_account._balance)
        
        print(f"转账成功: {amount:.2f} 从 {self._account_number} 到 {target_account._account_number}")
        return self._balance
    
    def get_balance(self):
        """获取余额"""
        return self._balance
    
    def get_account_info(self):
        """获取账户信息"""
        return {
            "账户号": self._account_number,
            "户主": self._owner_name,
            "余额": self._balance,
            "开户时间": self._created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "账户状态": "正常" if self._is_active else "冻结",
            "交易次数": len(self._transaction_history)
        }
    
    def get_transaction_history(self, limit=10):
        """获取交易历史"""
        return self._transaction_history[-limit:] if limit else self._transaction_history
    
    def freeze_account(self):
        """冻结账户"""
        self._is_active = False
        print(f"账户 {self._account_number} 已被冻结")
    
    def unfreeze_account(self):
        """解冻账户"""
        self._is_active = True
        print(f"账户 {self._account_number} 已解冻")
    
    # 类方法
    @classmethod
    def get_bank_info(cls):
        """获取银行信息"""
        return {
            "银行名称": cls._bank_name,
            "总账户数": cls._total_accounts,
            "基础利率": f"{cls._interest_rate * 100:.2f}%",
            "下一个账户号": f"ACC{cls._account_counter + 1:06d}"
        }
    
    @classmethod
    def set_interest_rate(cls, rate):
        """设置基础利率"""
        if not 0 <= rate <= 1:
            raise ValueError("利率必须在0-1之间")
        cls._interest_rate = rate
        print(f"基础利率已设置为: {rate * 100:.2f}%")
    
    @classmethod
    def create_joint_account(cls, owner1, owner2, initial_balance=0):
        """创建联名账户"""
        joint_name = f"{owner1} & {owner2}"
        account = cls(joint_name, initial_balance)
        account._account_type = "联名账户"
        return account
    
    # 静态方法
    @staticmethod
    def calculate_compound_interest(principal, rate, time, compound_frequency=12):
        """计算复利"""
        return principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    
    @staticmethod
    def validate_account_number(account_number):
        """验证账户号格式"""
        import re
        pattern = r'^ACC\d{6}$'
        return bool(re.match(pattern, account_number))
    
    # 特殊方法
    def __str__(self):
        return f"BankAccount({self._account_number}, {self._owner_name}, {self._balance:.2f})"
    
    def __repr__(self):
        return f"BankAccount(owner_name='{self._owner_name}', initial_balance={self._balance})"
    
    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False
        return self._account_number == other._account_number
    
    def __lt__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self._balance < other._balance

class SavingsAccount(BankAccount):
    """储蓄账户 - 有利息，有最低余额要求"""
    
    _savings_interest_rate = 0.035  # 储蓄利率3.5%
    _minimum_balance = 100  # 最低余额
    
    def __init__(self, owner_name, initial_balance=0):
        super().__init__(owner_name, initial_balance)
        self._account_type = "储蓄账户"
        self._last_interest_date = datetime.now()
        
        if initial_balance < self._minimum_balance:
            print(f"警告: 储蓄账户最低余额为 {self._minimum_balance}")
    
    def withdraw(self, amount):
        """重写取款方法，检查最低余额"""
        self._check_account_active()
        self._validate_amount(amount)
        
        if self._balance - amount < self._minimum_balance:
            raise ValueError(f"取款后余额不能低于最低余额 {self._minimum_balance}")
        
        return super().withdraw(amount)
    
    def calculate_interest(self):
        """计算利息"""
        current_date = datetime.now()
        days_passed = (current_date - self._last_interest_date).days
        
        if days_passed >= 30:  # 每月结息
            interest = self._balance * self._savings_interest_rate / 12
            self._balance += interest
            self._add_transaction("利息收入", interest, self._balance)
            self._last_interest_date = current_date
            
            print(f"利息结算: {interest:.2f}，当前余额: {self._balance:.2f}")
            return interest
        
        return 0
    
    @classmethod
    def set_savings_rate(cls, rate):
        """设置储蓄利率"""
        if not 0 <= rate <= 1:
            raise ValueError("利率必须在0-1之间")
        cls._savings_interest_rate = rate
        print(f"储蓄利率已设置为: {rate * 100:.2f}%")
    
    @classmethod
    def set_minimum_balance(cls, amount):
        """设置最低余额"""
        if amount < 0:
            raise ValueError("最低余额不能为负数")
        cls._minimum_balance = amount
        print(f"最低余额已设置为: {amount}")

class CreditAccount(BankAccount):
    """信用账户 - 可以透支，有信用额度"""
    
    _credit_interest_rate = 0.18  # 信用利率18%
    _default_credit_limit = 5000  # 默认信用额度
    
    def __init__(self, owner_name, initial_balance=0, credit_limit=None):
        super().__init__(owner_name, initial_balance)
        self._account_type = "信用账户"
        self._credit_limit = credit_limit or self._default_credit_limit
        self._credit_used = 0
        
        print(f"信用账户创建，信用额度: {self._credit_limit}")
    
    def get_available_credit(self):
        """获取可用信用额度"""
        return self._credit_limit - self._credit_used
    
    def withdraw(self, amount):
        """重写取款方法，支持透支"""
        self._check_account_active()
        self._validate_amount(amount)
        
        total_available = self._balance + self.get_available_credit()
        
        if amount > total_available:
            raise ValueError(f"超出信用额度，可用金额: {total_available:.2f}")
        
        if amount <= self._balance:
            # 正常取款
            self._balance -= amount
        else:
            # 需要使用信用额度
            credit_needed = amount - self._balance
            self._credit_used += credit_needed
            self._balance = 0
            
            print(f"使用信用额度: {credit_needed:.2f}")
        
        self._add_transaction("取款", -amount, self._balance)
        print(f"取款成功: {amount:.2f}，余额: {self._balance:.2f}，已用信用: {self._credit_used:.2f}")
        return self._balance
    
    def repay_credit(self, amount):
        """还款"""
        self._check_account_active()
        self._validate_amount(amount)
        
        if self._credit_used == 0:
            raise ValueError("当前无需还款")
        
        repay_amount = min(amount, self._credit_used)
        self._credit_used -= repay_amount
        
        # 剩余金额存入账户
        remaining = amount - repay_amount
        if remaining > 0:
            self._balance += remaining
        
        self._add_transaction(f"还款 {repay_amount:.2f}", amount, self._balance)
        print(f"还款成功: {repay_amount:.2f}，剩余欠款: {self._credit_used:.2f}")
        
        return self._credit_used
    
    def calculate_credit_interest(self):
        """计算信用利息"""
        if self._credit_used > 0:
            monthly_interest = self._credit_used * self._credit_interest_rate / 12
            self._credit_used += monthly_interest
            
            self._add_transaction("信用利息", -monthly_interest, self._balance)
            print(f"信用利息: {monthly_interest:.2f}，当前欠款: {self._credit_used:.2f}")
            return monthly_interest
        
        return 0
    
    def get_account_info(self):
        """重写账户信息，包含信用信息"""
        info = super().get_account_info()
        info.update({
            "信用额度": self._credit_limit,
            "已用信用": self._credit_used,
            "可用信用": self.get_available_credit(),
            "总可用金额": self._balance + self.get_available_credit()
        })
        return info
    
    @classmethod
    def set_credit_rate(cls, rate):
        """设置信用利率"""
        if not 0 <= rate <= 1:
            raise ValueError("利率必须在0-1之间")
        cls._credit_interest_rate = rate
        print(f"信用利率已设置为: {rate * 100:.2f}%")

# 银行账户系统演示
print("=== 银行账户管理系统演示 ===")

# 1. 创建不同类型的账户
print("\n1. 创建账户:")
basic_account = BankAccount("张三", 1000)
savings_account = SavingsAccount("李四", 5000)
credit_account = CreditAccount("王五", 2000, 8000)

# 2. 查看银行信息
print("\n2. 银行信息:")
bank_info = BankAccount.get_bank_info()
for key, value in bank_info.items():
    print(f"  {key}: {value}")

# 3. 基本操作
print("\n3. 基本账户操作:")
basic_account.deposit(500)
basic_account.withdraw(200)

print("\n储蓄账户操作:")
savings_account.deposit(1000)
try:
    savings_account.withdraw(5500)  # 会失败，低于最低余额
except ValueError as e:
    print(f"取款失败: {e}")

savings_account.withdraw(900)  # 成功

print("\n信用账户操作:")
credit_account.withdraw(3000)  # 使用信用额度
credit_account.repay_credit(1000)  # 还款

# 4. 转账操作
print("\n4. 转账操作:")
basic_account.transfer(savings_account, 300)

# 5. 查看账户信息
print("\n5. 账户信息:")
accounts = [basic_account, savings_account, credit_account]

for account in accounts:
    print(f"\n{account._account_type}信息:")
    info = account.get_account_info()
    for key, value in info.items():
        print(f"  {key}: {value}")

# 6. 交易历史
print("\n6. 交易历史（最近3笔）:")
for account in accounts:
    print(f"\n{account._account_number} 交易历史:")
    history = account.get_transaction_history(3)
    for transaction in history:
        print(f"  {transaction['时间']} - {transaction['类型']}: {transaction['金额']:.2f}")

# 7. 利息计算
print("\n7. 利息计算:")
savings_account.calculate_interest()
credit_account.calculate_credit_interest()

# 8. 静态方法使用
print("\n8. 静态方法演示:")
future_value = BankAccount.calculate_compound_interest(10000, 0.05, 5)
print(f"10000元，5%年利率，5年后复利价值: {future_value:.2f}")

valid = BankAccount.validate_account_number("ACC000001")
print(f"账户号 ACC000001 格式验证: {valid}")

# 9. 账户比较
print("\n9. 账户比较:")
accounts_sorted = sorted(accounts)
print("按余额排序的账户:")
for account in accounts_sorted:
    print(f"  {account._account_number}: {account._balance:.2f}")

# 10. 联名账户
print("\n10. 联名账户:")
joint_account = BankAccount.create_joint_account("张三", "李四", 3000)
print(f"联名账户: {joint_account}")

print("\n=== 银行账户系统演示完成 ===")
```

## 练习2：学生成绩管理系统

### 需求分析
设计一个学生成绩管理系统，包含学生、课程、成绩等类。

```python
class Student:
    """学生类"""
    
    _student_counter = 0
    _all_students = {}
    
    def __init__(self, name, age, student_id=None):
        """初始化学生"""
        Student._student_counter += 1
        
        self._student_id = student_id or f"STU{Student._student_counter:04d}"
        self._name = name
        self._age = age
        self._courses = {}  # 课程ID -> Course对象
        self._grades = {}   # 课程ID -> Grade对象
        self._enrollment_date = datetime.now()
        
        # 注册到全局学生字典
        Student._all_students[self._student_id] = self
        
        print(f"学生注册成功: {self._student_id} - {name}")
    
    def enroll_course(self, course):
        """选课"""
        if course.course_id in self._courses:
            print(f"已经选择了课程: {course.course_name}")
            return
        
        if len(self._courses) >= 10:  # 最多选10门课
            raise ValueError("选课数量已达上限（10门）")
        
        self._courses[course.course_id] = course
        course.add_student(self)
        
        print(f"{self._name} 选课成功: {course.course_name}")
    
    def drop_course(self, course):
        """退课"""
        if course.course_id not in self._courses:
            print(f"未选择课程: {course.course_name}")
            return
        
        del self._courses[course.course_id]
        course.remove_student(self)
        
        # 删除相关成绩
        if course.course_id in self._grades:
            del self._grades[course.course_id]
        
        print(f"{self._name} 退课成功: {course.course_name}")
    
    def add_grade(self, course, score, exam_type="期末考试"):
        """添加成绩"""
        if course.course_id not in self._courses:
            raise ValueError(f"未选择课程: {course.course_name}")
        
        if course.course_id not in self._grades:
            self._grades[course.course_id] = Grade(self, course)
        
        self._grades[course.course_id].add_score(score, exam_type)
        print(f"{self._name} {course.course_name} {exam_type}成绩: {score}")
    
    def get_gpa(self):
        """计算GPA"""
        if not self._grades:
            return 0.0
        
        total_points = 0
        total_credits = 0
        
        for course_id, grade in self._grades.items():
            course = self._courses[course_id]
            final_score = grade.get_final_score()
            gpa_point = self._score_to_gpa(final_score)
            
            total_points += gpa_point * course.credits
            total_credits += course.credits
        
        return total_points / total_credits if total_credits > 0 else 0.0
    
    def _score_to_gpa(self, score):
        """分数转换为GPA点数"""
        if score >= 90: return 4.0
        elif score >= 80: return 3.0
        elif score >= 70: return 2.0
        elif score >= 60: return 1.0
        else: return 0.0
    
    def get_transcript(self):
        """获取成绩单"""
        transcript = {
            "学生信息": {
                "学号": self._student_id,
                "姓名": self._name,
                "年龄": self._age,
                "入学日期": self._enrollment_date.strftime("%Y-%m-%d")
            },
            "课程成绩": [],
            "统计信息": {}
        }
        
        total_credits = 0
        passed_credits = 0
        
        for course_id, grade in self._grades.items():
            course = self._courses[course_id]
            final_score = grade.get_final_score()
            
            course_info = {
                "课程代码": course.course_id,
                "课程名称": course.course_name,
                "学分": course.credits,
                "最终成绩": final_score,
                "等级": self._score_to_grade(final_score),
                "GPA点数": self._score_to_gpa(final_score)
            }
            
            transcript["课程成绩"].append(course_info)
            total_credits += course.credits
            
            if final_score >= 60:
                passed_credits += course.credits
        
        transcript["统计信息"] = {
            "总学分": total_credits,
            "已获学分": passed_credits,
            "GPA": round(self.get_gpa(), 2),
            "选课门数": len(self._courses)
        }
        
        return transcript
    
    def _score_to_grade(self, score):
        """分数转换为等级"""
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        else: return "F"
    
    @classmethod
    def find_student(cls, student_id):
        """查找学生"""
        return cls._all_students.get(student_id)
    
    @classmethod
    def get_all_students(cls):
        """获取所有学生"""
        return list(cls._all_students.values())
    
    @classmethod
    def get_top_students(cls, limit=10):
        """获取GPA最高的学生"""
        students = cls.get_all_students()
        return sorted(students, key=lambda s: s.get_gpa(), reverse=True)[:limit]
    
    def __str__(self):
        return f"Student({self._student_id}, {self._name}, GPA: {self.get_gpa():.2f})"
    
    def __repr__(self):
        return f"Student(name='{self._name}', age={self._age}, student_id='{self._student_id}')"

class Course:
    """课程类"""
    
    _course_counter = 0
    _all_courses = {}
    
    def __init__(self, course_name, credits, instructor, course_id=None):
        """初始化课程"""
        Course._course_counter += 1
        
        self.course_id = course_id or f"CS{Course._course_counter:03d}"
        self.course_name = course_name
        self.credits = credits
        self.instructor = instructor
        self._students = {}  # 学生ID -> Student对象
        self._max_students = 50
        self._created_at = datetime.now()
        
        # 注册到全局课程字典
        Course._all_courses[self.course_id] = self
        
        print(f"课程创建成功: {self.course_id} - {course_name}")
    
    def add_student(self, student):
        """添加学生"""
        if len(self._students) >= self._max_students:
            raise ValueError(f"课程 {self.course_name} 已满员")
        
        self._students[student._student_id] = student
    
    def remove_student(self, student):
        """移除学生"""
        if student._student_id in self._students:
            del self._students[student._student_id]
    
    def get_student_list(self):
        """获取学生名单"""
        return list(self._students.values())
    
    def get_course_statistics(self):
        """获取课程统计"""
        students = self.get_student_list()
        if not students:
            return {"选课人数": 0}
        
        scores = []
        for student in students:
            if self.course_id in student._grades:
                score = student._grades[self.course_id].get_final_score()
                scores.append(score)
        
        if not scores:
            return {"选课人数": len(students), "已评分人数": 0}
        
        return {
            "选课人数": len(students),
            "已评分人数": len(scores),
            "平均分": sum(scores) / len(scores),
            "最高分": max(scores),
            "最低分": min(scores),
            "及格率": len([s for s in scores if s >= 60]) / len(scores) * 100
        }
    
    @classmethod
    def find_course(cls, course_id):
        """查找课程"""
        return cls._all_courses.get(course_id)
    
    @classmethod
    def get_all_courses(cls):
        """获取所有课程"""
        return list(cls._all_courses.values())
    
    def __str__(self):
        return f"Course({self.course_id}, {self.course_name}, {self.credits}学分)"
    
    def __repr__(self):
        return f"Course(course_name='{self.course_name}', credits={self.credits}, instructor='{self.instructor}')"

class Grade:
    """成绩类"""
    
    def __init__(self, student, course):
        """初始化成绩"""
        self.student = student
        self.course = course
        self._scores = {}  # 考试类型 -> 分数
        self._weights = {   # 各类考试权重
            "平时成绩": 0.2,
            "期中考试": 0.3,
            "期末考试": 0.5
        }
        self._created_at = datetime.now()
    
    def add_score(self, score, exam_type="期末考试"):
        """添加分数"""
        if not 0 <= score <= 100:
            raise ValueError("分数必须在0-100之间")
        
        self._scores[exam_type] = score
        
        # 如果是新的考试类型，设置默认权重
        if exam_type not in self._weights:
            self._weights[exam_type] = 0.1
            self._normalize_weights()
    
    def _normalize_weights(self):
        """标准化权重，确保总和为1"""
        total_weight = sum(self._weights.values())
        if total_weight > 0:
            for exam_type in self._weights:
                self._weights[exam_type] /= total_weight
    
    def set_weights(self, weights):
        """设置权重"""
        total = sum(weights.values())
        if abs(total - 1.0) > 0.01:
            raise ValueError("权重总和必须为1")
        
        self._weights.update(weights)
    
    def get_final_score(self):
        """计算最终成绩"""
        if not self._scores:
            return 0
        
        final_score = 0
        total_weight = 0
        
        for exam_type, score in self._scores.items():
            weight = self._weights.get(exam_type, 0)
            final_score += score * weight
            total_weight += weight
        
        # 如果权重不足1，按实际权重计算
        if total_weight > 0:
            final_score = final_score / total_weight if total_weight < 1 else final_score
        
        return round(final_score, 1)
    
    def get_grade_details(self):
        """获取成绩详情"""
        return {
            "学生": self.student._name,
            "课程": self.course.course_name,
            "各项成绩": self._scores.copy(),
            "权重设置": self._weights.copy(),
            "最终成绩": self.get_final_score(),
            "录入时间": self._created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def __str__(self):
        return f"Grade({self.student._name}, {self.course.course_name}, {self.get_final_score()})"

# 学生成绩管理系统演示
print("\n=== 学生成绩管理系统演示 ===")

# 1. 创建课程
print("\n1. 创建课程:")
courses = [
    Course("Python程序设计", 3, "张教授"),
    Course("数据结构", 4, "李教授"),
    Course("算法分析", 3, "王教授"),
    Course("数据库原理", 3, "赵教授")
]

# 2. 创建学生
print("\n2. 创建学生:")
students = [
    Student("张三", 20),
    Student("李四", 19),
    Student("王五", 21),
    Student("赵六", 20)
]

# 3. 学生选课
print("\n3. 学生选课:")
for student in students:
    for course in courses[:3]:  # 每个学生选前3门课
        student.enroll_course(course)

# 额外选课
students[0].enroll_course(courses[3])  # 张三多选一门课

# 4. 录入成绩
print("\n4. 录入成绩:")

# 张三的成绩
students[0].add_grade(courses[0], 85, "平时成绩")
students[0].add_grade(courses[0], 88, "期中考试")
students[0].add_grade(courses[0], 92, "期末考试")

students[0].add_grade(courses[1], 78, "平时成绩")
students[0].add_grade(courses[1], 82, "期中考试")
students[0].add_grade(courses[1], 85, "期末考试")

students[0].add_grade(courses[2], 90, "期末考试")
students[0].add_grade(courses[3], 88, "期末考试")

# 李四的成绩
students[1].add_grade(courses[0], 92, "期末考试")
students[1].add_grade(courses[1], 88, "期末考试")
students[1].add_grade(courses[2], 85, "期末考试")

# 王五的成绩
students[2].add_grade(courses[0], 78, "期末考试")
students[2].add_grade(courses[1], 75, "期末考试")
students[2].add_grade(courses[2], 82, "期末考试")

# 5. 查看成绩单
print("\n5. 学生成绩单:")
for student in students[:2]:  # 显示前两个学生的成绩单
    print(f"\n{student._name} 的成绩单:")
    transcript = student.get_transcript()
    
    print(f"学号: {transcript['学生信息']['学号']}")
    print(f"GPA: {transcript['统计信息']['GPA']}")
    print("课程成绩:")
    
    for course_grade in transcript['课程成绩']:
        print(f"  {course_grade['课程名称']}: {course_grade['最终成绩']} ({course_grade['等级']})")

# 6. 课程统计
print("\n6. 课程统计:")
for course in courses:
    print(f"\n{course.course_name} 统计:")
    stats = course.get_course_statistics()
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.1f}")
        else:
            print(f"  {key}: {value}")

# 7. 优秀学生排行
print("\n7. 优秀学生排行:")
top_students = Student.get_top_students(3)
for i, student in enumerate(top_students, 1):
    print(f"  {i}. {student._name} - GPA: {student.get_gpa():.2f}")

# 8. 成绩详情
print("\n8. 成绩详情示例:")
if courses[0].course_id in students[0]._grades:
    grade_detail = students[0]._grades[courses[0].course_id].get_grade_details()
    print(f"{students[0]._name} 的 {courses[0].course_name} 成绩详情:")
    for key, value in grade_detail.items():
        print(f"  {key}: {value}")

print("\n=== 学生成绩管理系统演示完成 ===")
```

## 练习3：图书馆管理系统

### 需求分析
设计一个图书馆管理系统，包含图书、读者、借阅记录等功能。

```python
from datetime import datetime, timedelta
from enum import Enum

class BookStatus(Enum):
    """图书状态枚举"""
    AVAILABLE = "可借阅"
    BORROWED = "已借出"
    RESERVED = "已预约"
    MAINTENANCE = "维护中"
    LOST = "丢失"

class ReaderType(Enum):
    """读者类型枚举"""
    STUDENT = "学生"
    TEACHER = "教师"
    STAFF = "职工"
    VISITOR = "访客"

class Book:
    """图书类"""
    
    _book_counter = 0
    _all_books = {}
    
    def __init__(self, title, author, isbn, category, publisher=None, publish_year=None):
        """初始化图书"""
        Book._book_counter += 1
        
        self.book_id = f"BK{Book._book_counter:06d}"
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.publisher = publisher
        self.publish_year = publish_year
        self.status = BookStatus.AVAILABLE
        self.location = f"A{Book._book_counter % 10 + 1}-{Book._book_counter % 100 + 1:02d}"
        self.added_date = datetime.now()
        self.borrow_count = 0
        self.current_borrower = None
        self.reservation_queue = []  # 预约队列
        
        # 注册到全局图书字典
        Book._all_books[self.book_id] = self
        
        print(f"图书入库: {self.book_id} - {title}")
    
    def is_available(self):
        """检查是否可借阅"""
        return self.status == BookStatus.AVAILABLE
    
    def borrow(self, reader):
        """借阅图书"""
        if not self.is_available():
            raise ValueError(f"图书 {self.title} 当前状态: {self.status.value}，无法借阅")
        
        if not reader.can_borrow():
            raise ValueError(f"读者 {reader.name} 无法借阅更多图书")
        
        self.status = BookStatus.BORROWED
        self.current_borrower = reader
        self.borrow_count += 1
        
        # 创建借阅记录
        borrow_record = BorrowRecord(reader, self)
        reader.add_borrow_record(borrow_record)
        
        print(f"{reader.name} 借阅了 {self.title}")
        return borrow_record
    
    def return_book(self):
        """归还图书"""
        if self.status != BookStatus.BORROWED:
            raise ValueError(f"图书 {self.title} 未被借出")
        
        borrower = self.current_borrower
        self.current_borrower = None
        
        # 检查是否有预约
        if self.reservation_queue:
            next_reader = self.reservation_queue.pop(0)
            self.status = BookStatus.RESERVED
            print(f"{self.title} 已为 {next_reader.name} 保留")
        else:
            self.status = BookStatus.AVAILABLE
        
        print(f"{borrower.name} 归还了 {self.title}")
        return borrower
    
    def reserve(self, reader):
        """预约图书"""
        if self.is_available():
            raise ValueError(f"图书 {self.title} 当前可借阅，无需预约")
        
        if reader in self.reservation_queue:
            raise ValueError(f"{reader.name} 已预约此图书")
        
        self.reservation_queue.append(reader)
        print(f"{reader.name} 预约了 {self.title}，排队位置: {len(self.reservation_queue)}")
    
    def cancel_reservation(self, reader):
        """取消预约"""
        if reader in self.reservation_queue:
            self.reservation_queue.remove(reader)
            print(f"{reader.name} 取消了对 {self.title} 的预约")
        else:
            print(f"{reader.name} 未预约此图书")
    
    def get_book_info(self):
        """获取图书信息"""
        return {
            "图书ID": self.book_id,
            "书名": self.title,
            "作者": self.author,
            "ISBN": self.isbn,
            "分类": self.category,
            "出版社": self.publisher,
            "出版年份": self.publish_year,
            "状态": self.status.value,
            "位置": self.location,
            "借阅次数": self.borrow_count,
            "当前借阅者": self.current_borrower.name if self.current_borrower else None,
            "预约人数": len(self.reservation_queue)
        }
    
    @classmethod
    def search_books(cls, **kwargs):
        """搜索图书"""
        results = []
        
        for book in cls._all_books.values():
            match = True
            
            for key, value in kwargs.items():
                if key == "title" and value.lower() not in book.title.lower():
                    match = False
                    break
                elif key == "author" and value.lower() not in book.author.lower():
                    match = False
                    break
                elif key == "category" and value.lower() != book.category.lower():
                    match = False
                    break
                elif key == "status" and book.status != value:
                    match = False
                    break
            
            if match:
                results.append(book)
        
        return results
    
    @classmethod
    def get_popular_books(cls, limit=10):
        """获取热门图书"""
        books = list(cls._all_books.values())
        return sorted(books, key=lambda b: b.borrow_count, reverse=True)[:limit]
    
    def __str__(self):
        return f"Book({self.book_id}, {self.title}, {self.status.value})"
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"

class Reader:
    """读者类"""
    
    _reader_counter = 0
    _all_readers = {}
    
    # 不同类型读者的借阅限制
    _borrow_limits = {
        ReaderType.STUDENT: {"max_books": 5, "max_days": 30},
        ReaderType.TEACHER: {"max_books": 10, "max_days": 60},
        ReaderType.STAFF: {"max_books": 8, "max_days": 45},
        ReaderType.VISITOR: {"max_books": 2, "max_days": 14}
    }
    
    def __init__(self, name, reader_type, contact_info, reader_id=None):
        """初始化读者"""
        Reader._reader_counter += 1
        
        self.reader_id = reader_id or f"RD{Reader._reader_counter:06d}"
        self.name = name
        self.reader_type = reader_type
        self.contact_info = contact_info
        self.registration_date = datetime.now()
        self.is_active = True
        self.borrow_records = []  # 借阅记录
        self.current_borrows = []  # 当前借阅的图书
        self.fine_amount = 0.0  # 罚金
        
        # 注册到全局读者字典
        Reader._all_readers[self.reader_id] = self
        
        print(f"读者注册: {self.reader_id} - {name} ({reader_type.value})")
    
    def can_borrow(self):
        """检查是否可以借阅"""
        if not self.is_active:
            return False
        
        if self.fine_amount > 0:
            return False
        
        max_books = self._borrow_limits[self.reader_type]["max_books"]
        return len(self.current_borrows) < max_books
    
    def add_borrow_record(self, borrow_record):
        """添加借阅记录"""
        self.borrow_records.append(borrow_record)
        self.current_borrows.append(borrow_record)
    
    def return_book(self, book):
        """归还图书"""
        # 找到对应的借阅记录
        borrow_record = None
        for record in self.current_borrows:
            if record.book == book:
                borrow_record = record
                break
        
        if not borrow_record:
            raise ValueError(f"{self.name} 未借阅图书 {book.title}")
        
        # 计算罚金
        fine = borrow_record.calculate_fine()
        if fine > 0:
            self.fine_amount += fine
            print(f"逾期归还，罚金: {fine:.2f} 元")
        
        # 完成归还
        borrow_record.return_date = datetime.now()
        self.current_borrows.remove(borrow_record)
        book.return_book()
    
    def pay_fine(self, amount):
        """缴纳罚金"""
        if amount <= 0:
            raise ValueError("缴费金额必须大于0")
        
        if amount > self.fine_amount:
            raise ValueError(f"缴费金额超过欠费金额 {self.fine_amount:.2f}")
        
        self.fine_amount -= amount
        print(f"{self.name} 缴费 {amount:.2f} 元，剩余欠费: {self.fine_amount:.2f} 元")
    
    def get_reader_info(self):
        """获取读者信息"""
        return {
            "读者ID": self.reader_id,
            "姓名": self.name,
            "类型": self.reader_type.value,
            "联系方式": self.contact_info,
            "注册日期": self.registration_date.strftime("%Y-%m-%d"),
            "状态": "正常" if self.is_active else "停用",
            "当前借阅": len(self.current_borrows),
            "借阅限制": self._borrow_limits[self.reader_type]["max_books"],
            "欠费金额": self.fine_amount,
            "总借阅次数": len(self.borrow_records)
        }
    
    def get_borrow_history(self, limit=None):
        """获取借阅历史"""
        history = self.borrow_records[-limit:] if limit else self.borrow_records
        return [record.get_record_info() for record in history]
    
    @classmethod
    def find_reader(cls, reader_id):
        """查找读者"""
        return cls._all_readers.get(reader_id)
    
    @classmethod
    def get_overdue_readers(cls):
        """获取有逾期图书的读者"""
        overdue_readers = []
        
        for reader in cls._all_readers.values():
            for record in reader.current_borrows:
                if record.is_overdue():
                    overdue_readers.append(reader)
                    break
        
        return overdue_readers
    
    def __str__(self):
        return f"Reader({self.reader_id}, {self.name}, {self.reader_type.value})"
    
    def __repr__(self):
        return f"Reader(name='{self.name}', reader_type={self.reader_type}, contact_info='{self.contact_info}')"

class BorrowRecord:
    """借阅记录类"""
    
    def __init__(self, reader, book):
        """初始化借阅记录"""
        self.reader = reader
        self.book = book
        self.borrow_date = datetime.now()
        self.due_date = self._calculate_due_date()
        self.return_date = None
        self.fine_paid = 0.0
    
    def _calculate_due_date(self):
        """计算应还日期"""
        max_days = Reader._borrow_limits[self.reader.reader_type]["max_days"]
        return self.borrow_date + timedelta(days=max_days)
    
    def is_overdue(self):
        """检查是否逾期"""
        if self.return_date:  # 已归还
            return False
        return datetime.now() > self.due_date
    
    def days_overdue(self):
        """计算逾期天数"""
        if not self.is_overdue():
            return 0
        
        check_date = self.return_date or datetime.now()
        return (check_date - self.due_date).days
    
    def calculate_fine(self):
        """计算罚金"""
        overdue_days = self.days_overdue()
        if overdue_days <= 0:
            return 0.0
        
        # 罚金规则：每天0.5元
        fine_per_day = 0.5
        return overdue_days * fine_per_day
    
    def get_record_info(self):
        """获取记录信息"""
        return {
            "读者": self.reader.name,
            "图书": self.book.title,
            "借阅日期": self.borrow_date.strftime("%Y-%m-%d %H:%M"),
            "应还日期": self.due_date.strftime("%Y-%m-%d"),
            "归还日期": self.return_date.strftime("%Y-%m-%d %H:%M") if self.return_date else "未归还",
            "是否逾期": self.is_overdue(),
            "逾期天数": self.days_overdue(),
            "应缴罚金": self.calculate_fine()
        }
    
    def __str__(self):
        status = "已归还" if self.return_date else ("逾期" if self.is_overdue() else "借阅中")
        return f"BorrowRecord({self.reader.name}, {self.book.title}, {status})"

class Library:
    """图书馆类 - 管理整个系统"""
    
    def __init__(self, name, address):
        """初始化图书馆"""
        self.name = name
        self.address = address
        self.established_date = datetime.now()
        self.daily_fine_rate = 0.5  # 每天罚金
    
    def add_book(self, title, author, isbn, category, publisher=None, publish_year=None):
        """添加图书"""
        book = Book(title, author, isbn, category, publisher, publish_year)
        return book
    
    def register_reader(self, name, reader_type, contact_info):
        """注册读者"""
        reader = Reader(name, reader_type, contact_info)
        return reader
    
    def borrow_book(self, reader_id, book_id):
        """借阅图书"""
        reader = Reader.find_reader(reader_id)
        book = Book._all_books.get(book_id)
        
        if not reader:
            raise ValueError(f"读者 {reader_id} 不存在")
        
        if not book:
            raise ValueError(f"图书 {book_id} 不存在")
        
        return book.borrow(reader)
    
    def return_book(self, reader_id, book_id):
        """归还图书"""
        reader = Reader.find_reader(reader_id)
        book = Book._all_books.get(book_id)
        
        if not reader:
            raise ValueError(f"读者 {reader_id} 不存在")
        
        if not book:
            raise ValueError(f"图书 {book_id} 不存在")
        
        reader.return_book(book)
    
    def get_library_statistics(self):
        """获取图书馆统计信息"""
        total_books = len(Book._all_books)
        available_books = len([b for b in Book._all_books.values() if b.is_available()])
        borrowed_books = len([b for b in Book._all_books.values() if b.status == BookStatus.BORROWED])
        
        total_readers = len(Reader._all_readers)
        active_readers = len([r for r in Reader._all_readers.values() if r.is_active])
        
        overdue_readers = Reader.get_overdue_readers()
        total_fines = sum(r.fine_amount for r in Reader._all_readers.values())
        
        return {
            "图书馆名称": self.name,
            "地址": self.address,
            "成立日期": self.established_date.strftime("%Y-%m-%d"),
            "图书统计": {
                "总图书数": total_books,
                "可借阅": available_books,
                "已借出": borrowed_books,
                "借阅率": f"{borrowed_books/total_books*100:.1f}%" if total_books > 0 else "0%"
            },
            "读者统计": {
                "总读者数": total_readers,
                "活跃读者": active_readers,
                "逾期读者": len(overdue_readers),
                "总欠费": f"{total_fines:.2f}元"
            }
        }
    
    def generate_overdue_report(self):
        """生成逾期报告"""
        overdue_readers = Reader.get_overdue_readers()
        
        report = {
            "报告生成时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "逾期读者数量": len(overdue_readers),
            "逾期详情": []
        }
        
        for reader in overdue_readers:
            reader_overdue = []
            for record in reader.current_borrows:
                if record.is_overdue():
                    reader_overdue.append({
                        "图书": record.book.title,
                        "借阅日期": record.borrow_date.strftime("%Y-%m-%d"),
                        "应还日期": record.due_date.strftime("%Y-%m-%d"),
                        "逾期天数": record.days_overdue(),
                        "应缴罚金": record.calculate_fine()
                    })
            
            if reader_overdue:
                report["逾期详情"].append({
                    "读者ID": reader.reader_id,
                    "姓名": reader.name,
                    "联系方式": reader.contact_info,
                    "逾期图书": reader_overdue,
                    "总罚金": sum(item["应缴罚金"] for item in reader_overdue)
                })
        
        return report

# 图书馆管理系统演示
print("\n=== 图书馆管理系统演示 ===")

# 1. 创建图书馆
print("\n1. 创建图书馆:")
library = Library("Python大学图书馆", "北京市海淀区")

# 2. 添加图书
print("\n2. 添加图书:")
books = [
    library.add_book("Python编程从入门到实践", "埃里克·马瑟斯", "9787115428028", "计算机", "人民邮电出版社", 2016),
    library.add_book("算法导论", "托马斯·科尔曼", "9787111407010", "计算机", "机械工业出版社", 2012),
    library.add_book("深度学习", "伊恩·古德费洛", "9787115461476", "人工智能", "人民邮电出版社", 2017),
    library.add_book("数据结构与算法分析", "马克·艾伦·维斯", "9787111562801", "计算机", "机械工业出版社", 2016)
]

# 3. 注册读者
print("\n3. 注册读者:")
readers = [
    library.register_reader("张三", ReaderType.STUDENT, "zhang@example.com"),
    library.register_reader("李教授", ReaderType.TEACHER, "li@university.edu"),
    library.register_reader("王职工", ReaderType.STAFF, "wang@university.edu"),
    library.register_reader("赵访客", ReaderType.VISITOR, "zhao@visitor.com")
]

# 4. 借阅操作
print("\n4. 借阅操作:")
try:
    # 张三借阅两本书
    library.borrow_book(readers[0].reader_id, books[0].book_id)
    library.borrow_book(readers[0].reader_id, books[1].book_id)
    
    # 李教授借阅一本书
    library.borrow_book(readers[1].reader_id, books[2].book_id)
    
    # 王职工借阅一本书
    library.borrow_book(readers[2].reader_id, books[3].book_id)
    
except Exception as e:
    print(f"借阅失败: {e}")

# 5. 预约操作
print("\n5. 预约操作:")
try:
    # 赵访客预约已借出的书
    books[0].reserve(readers[3])
    books[1].reserve(readers[3])
except Exception as e:
    print(f"预约失败: {e}")

# 6. 查看图书信息
print("\n6. 图书状态:")
for book in books:
    info = book.get_book_info()
    print(f"{info['书名']}: {info['状态']} - 借阅者: {info['当前借阅者'] or '无'}")

# 7. 查看读者信息
print("\n7. 读者信息:")
for reader in readers[:2]:  # 显示前两个读者
    info = reader.get_reader_info()
    print(f"{info['姓名']} ({info['类型']}): 当前借阅 {info['当前借阅']}/{info['借阅限制']} 本")

# 8. 归还操作
print("\n8. 归还操作:")
try:
    # 张三归还一本书
    library.return_book(readers[0].reader_id, books[0].book_id)
except Exception as e:
    print(f"归还失败: {e}")

# 9. 搜索图书
print("\n9. 搜索图书:")
search_results = Book.search_books(category="计算机")
print(f"计算机类图书 ({len(search_results)} 本):")
for book in search_results:
    print(f"  {book.title} - {book.status.value}")

# 10. 图书馆统计
print("\n10. 图书馆统计:")
stats = library.get_library_statistics()
print(f"图书馆: {stats['图书馆名称']}")
print(f"图书统计: 总数 {stats['图书统计']['总图书数']}, 可借 {stats['图书统计']['可借阅']}, 已借 {stats['图书统计']['已借出']}")
print(f"读者统计: 总数 {stats['读者统计']['总读者数']}, 活跃 {stats['读者统计']['活跃读者']}")

print("\n=== 图书馆管理系统演示完成 ===")
```

## 练习4：员工管理系统

### 需求分析
设计一个员工管理系统，包含不同类型的员工和薪资计算。

```python
from abc import ABC, abstractmethod
from datetime import datetime, date
from enum import Enum

class EmployeeType(Enum):
    """员工类型枚举"""
    FULL_TIME = "全职员工"
    PART_TIME = "兼职员工"
    CONTRACT = "合同工"
    INTERN = "实习生"

class Department(Enum):
    """部门枚举"""
    IT = "信息技术部"
    HR = "人力资源部"
    FINANCE = "财务部"
    MARKETING = "市场部"
    SALES = "销售部"
    OPERATIONS = "运营部"

class Employee(ABC):
    """员工抽象基类"""
    
    _employee_counter = 0
    _all_employees = {}
    
    def __init__(self, name, department, hire_date=None):
        """初始化员工"""
        Employee._employee_counter += 1
        
        self.employee_id = f"EMP{Employee._employee_counter:05d}"
        self.name = name
        self.department = department
        self.hire_date = hire_date or date.today()
        self.is_active = True
        self.performance_ratings = []  # 绩效评分历史
        
        # 注册到全局员工字典
        Employee._all_employees[self.employee_id] = self
        
        print(f"员工入职: {self.employee_id} - {name} ({self.get_employee_type().value})")
    
    @abstractmethod
    def calculate_salary(self, period_data=None):
        """计算薪资 - 抽象方法"""
        pass
    
    @abstractmethod
    def get_employee_type(self):
        """获取员工类型 - 抽象方法"""
        pass
    
    def add_performance_rating(self, rating, period, comments=""):
        """添加绩效评分"""
        if not 1 <= rating <= 5:
            raise ValueError("绩效评分必须在1-5之间")
        
        performance = {
            "评分": rating,
            "期间": period,
            "评价": comments,
            "评分日期": datetime.now()
        }
        
        self.performance_ratings.append(performance)
        print(f"{self.name} 绩效评分: {rating}/5 ({period})")
    
    def get_average_performance(self):
        """获取平均绩效"""
        if not self.performance_ratings:
            return 0.0
        
        total = sum(rating["评分"] for rating in self.performance_ratings)
        return total / len(self.performance_ratings)
    
    def get_years_of_service(self):
        """获取工作年限"""
        today = date.today()
        years = today.year - self.hire_date.year
        
        # 调整不满一年的情况
        if today.month < self.hire_date.month or \
           (today.month == self.hire_date.month and today.day < self.hire_date.day):
            years -= 1
        
        return max(0, years)
    
    def get_employee_info(self):
        """获取员工信息"""
        return {
            "员工ID": self.employee_id,
            "姓名": self.name,
            "类型": self.get_employee_type().value,
            "部门": self.department.value,
            "入职日期": self.hire_date.strftime("%Y-%m-%d"),
            "工作年限": self.get_years_of_service(),
            "状态": "在职" if self.is_active else "离职",
            "平均绩效": round(self.get_average_performance(), 2),
            "绩效次数": len(self.performance_ratings)
        }
    
    @classmethod
    def find_employee(cls, employee_id):
        """查找员工"""
        return cls._all_employees.get(employee_id)
    
    @classmethod
    def get_employees_by_department(cls, department):
        """按部门获取员工"""
        return [emp for emp in cls._all_employees.values() 
                if emp.department == department and emp.is_active]
    
    @classmethod
    def get_employees_by_type(cls, employee_type):
        """按类型获取员工"""
        return [emp for emp in cls._all_employees.values() 
                if emp.get_employee_type() == employee_type and emp.is_active]
    
    def __str__(self):
        return f"Employee({self.employee_id}, {self.name}, {self.department.value})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', department={self.department})"

class FullTimeEmployee(Employee):
    """全职员工"""
    
    def __init__(self, name, department, base_salary, hire_date=None):
        super().__init__(name, department, hire_date)
        self.base_salary = base_salary
        self.bonus_rate = 0.1  # 默认奖金比例10%
        self.benefits = {
            "医疗保险": 500,
            "住房补贴": 1000,
            "交通补贴": 300
        }
    
    def get_employee_type(self):
        return EmployeeType.FULL_TIME
    
    def calculate_salary(self, period_data=None):
        """计算全职员工薪资"""
        # 基本工资
        salary = self.base_salary
        
        # 绩效奖金
        avg_performance = self.get_average_performance()
        if avg_performance >= 4.0:
            bonus_multiplier = 1.5
        elif avg_performance >= 3.5:
            bonus_multiplier = 1.2
        elif avg_performance >= 3.0:
            bonus_multiplier = 1.0
        else:
            bonus_multiplier = 0.5
        
        bonus = self.base_salary * self.bonus_rate * bonus_multiplier
        
        # 工龄奖金
        years = self.get_years_of_service()
        seniority_bonus = min(years * 200, 2000)  # 每年200元，最高2000元
        
        # 福利
        total_benefits = sum(self.benefits.values())
        
        total_salary = salary + bonus + seniority_bonus + total_benefits
        
        return {
            "基本工资": salary,
            "绩效奖金": bonus,
            "工龄奖金": seniority_bonus,
            "福利补贴": total_benefits,
            "应发工资": total_salary,
            "计算日期": datetime.now().strftime("%Y-%m-%d")
        }
    
    def set_bonus_rate(self, rate):
        """设置奖金比例"""
        if not 0 <= rate <= 1:
            raise ValueError("奖金比例必须在0-1之间")
        self.bonus_rate = rate
    
    def update_benefits(self, benefits):
        """更新福利"""
        self.benefits.update(benefits)

class PartTimeEmployee(Employee):
    """兼职员工"""
    
    def __init__(self, name, department, hourly_rate, hire_date=None):
        super().__init__(name, department, hire_date)
        self.hourly_rate = hourly_rate
        self.max_hours_per_week = 20  # 每周最大工作小时数
    
    def get_employee_type(self):
        return EmployeeType.PART_TIME
    
    def calculate_salary(self, period_data=None):
        """计算兼职员工薪资"""
        if not period_data or "hours_worked" not in period_data:
            raise ValueError("兼职员工需要提供工作小时数")
        
        hours_worked = period_data["hours_worked"]
        weeks = period_data.get("weeks", 4)  # 默认4周
        
        # 检查是否超过每周最大工作时间
        weekly_hours = hours_worked / weeks
        if weekly_hours > self.max_hours_per_week:
            print(f"警告: 每周工作时间 {weekly_hours:.1f} 小时超过限制 {self.max_hours_per_week} 小时")
        
        # 基本工资
        base_pay = hours_worked * self.hourly_rate
        
        # 超时加班费（超过每周20小时的部分按1.5倍计算）
        overtime_hours = max(0, hours_worked - self.max_hours_per_week * weeks)
        overtime_pay = overtime_hours * self.hourly_rate * 0.5
        
        total_salary = base_pay + overtime_pay
        
        return {
            "工作小时": hours_worked,
            "时薪": self.hourly_rate,
            "基本工资": base_pay,
            "加班费": overtime_pay,
            "应发工资": total_salary,
            "计算日期": datetime.now().strftime("%Y-%m-%d")
        }

class ContractEmployee(Employee):
    """合同工"""
    
    def __init__(self, name, department, project_rate, contract_duration, hire_date=None):
        super().__init__(name, department, hire_date)
        self.project_rate = project_rate  # 项目费率
        self.contract_duration = contract_duration  # 合同期限（月）
        self.projects_completed = []
    
    def get_employee_type(self):
        return EmployeeType.CONTRACT
    
    def add_project(self, project_name, completion_percentage, difficulty_level=1.0):
        """添加项目"""
        if not 0 <= completion_percentage <= 100:
            raise ValueError("完成百分比必须在0-100之间")
        
        project = {
            "项目名称": project_name,
            "完成度": completion_percentage,
            "难度系数": difficulty_level,
            "完成日期": datetime.now()
        }
        
        self.projects_completed.append(project)
        print(f"{self.name} 完成项目: {project_name} ({completion_percentage}%)")
    
    def calculate_salary(self, period_data=None):
        """计算合同工薪资"""
        if not self.projects_completed:
            return {
                "项目数量": 0,
                "应发工资": 0,
                "计算日期": datetime.now().strftime("%Y-%m-%d")
            }
        
        total_payment = 0
        project_details = []
        
        for project in self.projects_completed:
            # 根据完成度和难度系数计算项目费用
            project_payment = (self.project_rate * 
                             project["完成度"] / 100 * 
                             project["难度系数"])
            
            total_payment += project_payment
            
            project_details.append({
                "项目名称": project["项目名称"],
                "完成度": project["完成度"],
                "难度系数": project["难度系数"],
                "项目费用": project_payment
            })
        
        # 质量奖金
        avg_completion = sum(p["完成度"] for p in self.projects_completed) / len(self.projects_completed)
        quality_bonus = total_payment * 0.1 if avg_completion >= 95 else 0
        
        return {
            "项目数量": len(self.projects_completed),
            "项目详情": project_details,
            "项目总费用": total_payment,
            "质量奖金": quality_bonus,
            "应发工资": total_payment + quality_bonus,
            "平均完成度": round(avg_completion, 1),
            "计算日期": datetime.now().strftime("%Y-%m-%d")
        }

class InternEmployee(Employee):
    """实习生"""
    
    def __init__(self, name, department, monthly_stipend, internship_duration, hire_date=None):
        super().__init__(name, department, hire_date)
        self.monthly_stipend = monthly_stipend  # 月度津贴
        self.internship_duration = internship_duration  # 实习期限（月）
        self.learning_progress = {}  # 学习进度
        self.mentor = None  # 导师
    
    def get_employee_type(self):
        return EmployeeType.INTERN
    
    def set_mentor(self, mentor_employee):
        """设置导师"""
        if not isinstance(mentor_employee, Employee):
            raise ValueError("导师必须是员工对象")
        
        self.mentor = mentor_employee
        print(f"{self.name} 的导师设置为: {mentor_employee.name}")
    
    def update_learning_progress(self, skill, progress_percentage):
        """更新学习进度"""
        if not 0 <= progress_percentage <= 100:
            raise ValueError("进度百分比必须在0-100之间")
        
        self.learning_progress[skill] = {
            "进度": progress_percentage,
            "更新日期": datetime.now()
        }
        
        print(f"{self.name} {skill} 学习进度: {progress_percentage}%")
    
    def calculate_salary(self, period_data=None):
        """计算实习生薪资"""
        # 基础津贴
        base_stipend = self.monthly_stipend
        
        # 学习进度奖励
        if self.learning_progress:
            avg_progress = sum(skill["进度"] for skill in self.learning_progress.values()) / len(self.learning_progress)
            
            if avg_progress >= 90:
                progress_bonus = base_stipend * 0.3
            elif avg_progress >= 80:
                progress_bonus = base_stipend * 0.2
            elif avg_progress >= 70:
                progress_bonus = base_stipend * 0.1
            else:
                progress_bonus = 0
        else:
            avg_progress = 0
            progress_bonus = 0
        
        # 绩效奖励
        performance_bonus = 0
        if self.performance_ratings:
            avg_performance = self.get_average_performance()
            if avg_performance >= 4.0:
                performance_bonus = base_stipend * 0.2
            elif avg_performance >= 3.5:
                performance_bonus = base_stipend * 0.1
        
        total_stipend = base_stipend + progress_bonus + performance_bonus
        
        return {
            "基础津贴": base_stipend,
            "学习进度奖励": progress_bonus,
            "绩效奖励": performance_bonus,
            "应发津贴": total_stipend,
            "平均学习进度": round(avg_progress, 1) if self.learning_progress else 0,
            "导师": self.mentor.name if self.mentor else "未分配",
            "计算日期": datetime.now().strftime("%Y-%m-%d")
        }

class Company:
    """公司类 - 管理整个员工系统"""
    
    def __init__(self, name, address):
        """初始化公司"""
        self.name = name
        self.address = address
        self.established_date = date.today()
        self.payroll_history = []  # 工资发放历史
    
    def hire_employee(self, employee_class, *args, **kwargs):
        """招聘员工"""
        employee = employee_class(*args, **kwargs)
        return employee
    
    def fire_employee(self, employee_id, reason=""):
        """解雇员工"""
        employee = Employee.find_employee(employee_id)
        if not employee:
            raise ValueError(f"员工 {employee_id} 不存在")
        
        if not employee.is_active:
            raise ValueError(f"员工 {employee.name} 已经离职")
        
        employee.is_active = False
        print(f"员工 {employee.name} 已离职。原因: {reason or '未说明'}")
    
    def calculate_payroll(self, department=None, employee_type=None):
        """计算工资单"""
        employees = Employee._all_employees.values()
        
        # 筛选条件
        if department:
            employees = [emp for emp in employees if emp.department == department]
        
        if employee_type:
            employees = [emp for emp in employees if emp.get_employee_type() == employee_type]
        
        # 只计算在职员工
        employees = [emp for emp in employees if emp.is_active]
        
        payroll = {
            "公司": self.name,
            "计算日期": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "员工数量": len(employees),
            "工资详情": [],
            "总计": 0
        }
        
        for employee in employees:
            try:
                # 根据员工类型提供不同的期间数据
                period_data = None
                if isinstance(employee, PartTimeEmployee):
                    period_data = {"hours_worked": 80, "weeks": 4}  # 示例数据
                
                salary_info = employee.calculate_salary(period_data)
                
                employee_payroll = {
                    "员工ID": employee.employee_id,
                    "姓名": employee.name,
                    "部门": employee.department.value,
                    "类型": employee.get_employee_type().value,
                    "薪资详情": salary_info
                }
                
                payroll["工资详情"].append(employee_payroll)
                payroll["总计"] += salary_info.get("应发工资", salary_info.get("应发津贴", 0))
                
            except Exception as e:
                print(f"计算 {employee.name} 工资时出错: {e}")
        
        # 保存到历史记录
        self.payroll_history.append(payroll)
        
        return payroll
    
    def get_company_statistics(self):
        """获取公司统计信息"""
        all_employees = list(Employee._all_employees.values())
        active_employees = [emp for emp in all_employees if emp.is_active]
        
        # 按部门统计
        dept_stats = {}
        for dept in Department:
            dept_employees = [emp for emp in active_employees if emp.department == dept]
            dept_stats[dept.value] = len(dept_employees)
        
        # 按类型统计
        type_stats = {}
        for emp_type in EmployeeType:
            type_employees = [emp for emp in active_employees if emp.get_employee_type() == emp_type]
            type_stats[emp_type.value] = len(type_employees)
        
        # 平均工作年限
        if active_employees:
            avg_years = sum(emp.get_years_of_service() for emp in active_employees) / len(active_employees)
        else:
            avg_years = 0
        
        return {
            "公司名称": self.name,
            "成立日期": self.established_date.strftime("%Y-%m-%d"),
            "员工统计": {
                "总员工数": len(all_employees),
                "在职员工": len(active_employees),
                "离职员工": len(all_employees) - len(active_employees)
            },
            "部门分布": dept_stats,
            "员工类型分布": type_stats,
            "平均工作年限": round(avg_years, 1),
            "工资发放次数": len(self.payroll_history)
        }

# 员工管理系统演示
print("\n=== 员工管理系统演示 ===")

# 1. 创建公司
print("\n1. 创建公司:")
company = Company("Python科技有限公司", "北京市朝阳区")

# 2. 招聘不同类型的员工
print("\n2. 招聘员工:")
employees = [
    company.hire_employee(FullTimeEmployee, "张经理", Department.IT, 15000),
    company.hire_employee(FullTimeEmployee, "李工程师", Department.IT, 12000),
    company.hire_employee(PartTimeEmployee, "王设计师", Department.MARKETING, 80),
    company.hire_employee(ContractEmployee, "赵顾问", Department.IT, 5000, 6),
    company.hire_employee(InternEmployee, "钱实习生", Department.IT, 3000, 3)
]

# 3. 设置绩效评分
print("\n3. 绩效评估:")
employees[0].add_performance_rating(4.5, "2024Q1", "表现优秀")
employees[1].add_performance_rating(4.0, "2024Q1", "工作认真")
employees[4].add_performance_rating(3.8, "2024Q1", "学习积极")

# 4. 特殊操作
print("\n4. 特殊操作:")

# 合同工完成项目
employees[3].add_project("网站重构", 95, 1.2)
employees[3].add_project("API开发", 88, 1.0)

# 实习生学习进度
employees[4].set_mentor(employees[1])  # 设置导师
employees[4].update_learning_progress("Python编程", 85)
employees[4].update_learning_progress("数据库设计", 78)

# 5. 计算工资
print("\n5. 工资计算:")

# 全职员工工资
print("\n全职员工工资:")
for emp in employees[:2]:
    salary = emp.calculate_salary()
    print(f"{emp.name}: 应发工资 {salary['应发工资']:.2f} 元")
    print(f"  基本工资: {salary['基本工资']}, 绩效奖金: {salary['绩效奖金']:.2f}")

# 兼职员工工资
print("\n兼职员工工资:")
part_time_salary = employees[2].calculate_salary({"hours_worked": 85, "weeks": 4})
print(f"{employees[2].name}: 应发工资 {part_time_salary['应发工资']:.2f} 元")
print(f"  工作 {part_time_salary['工作小时']} 小时，加班费: {part_time_salary['加班费']:.2f}")

# 合同工工资
print("\n合同工工资:")
contract_salary = employees[3].calculate_salary()
print(f"{employees[3].name}: 应发工资 {contract_salary['应发工资']:.2f} 元")
print(f"  完成 {contract_salary['项目数量']} 个项目，平均完成度: {contract_salary['平均完成度']}%")

# 实习生津贴
print("\n实习生津贴:")
intern_salary = employees[4].calculate_salary()
print(f"{employees[4].name}: 应发津贴 {intern_salary['应发津贴']:.2f} 元")
print(f"  学习进度: {intern_salary['平均学习进度']}%, 导师: {intern_salary['导师']}")

# 6. 部门工资单
print("\n6. IT部门工资单:")
it_payroll = company.calculate_payroll(department=Department.IT)
print(f"IT部门员工数: {it_payroll['员工数量']}")
print(f"IT部门工资总计: {it_payroll['总计']:.2f} 元")

# 7. 公司统计
print("\n7. 公司统计:")
stats = company.get_company_statistics()
print(f"公司: {stats['公司名称']}")
print(f"员工统计: 总数 {stats['员工统计']['总员工数']}, 在职 {stats['员工统计']['在职员工']}")
print("部门分布:")
for dept, count in stats['部门分布'].items():
    if count > 0:
        print(f"  {dept}: {count} 人")

print("员工类型分布:")
for emp_type, count in stats['员工类型分布'].items():
    if count > 0:
        print(f"  {emp_type}: {count} 人")

print(f"平均工作年限: {stats['平均工作年限']} 年")

print("\n=== 员工管理系统演示完成 ===")
```

## 学习要点总结

### 1. 面向对象设计原则
- **单一职责原则**: 每个类只负责一个功能
- **开闭原则**: 对扩展开放，对修改关闭
- **里氏替换原则**: 子类可以替换父类
- **接口隔离原则**: 使用多个专门的接口
- **依赖倒置原则**: 依赖抽象而不是具体实现

### 2. 类设计技巧
- 合理使用抽象基类和接口
- 正确实现继承和多态
- 适当使用类方法和静态方法
- 有效管理类属性和实例属性
- 实现特殊方法增强类功能

### 3. 代码组织
- 使用枚举提高代码可读性
- 合理划分模块和包
- 统一的命名规范
- 完善的错误处理
- 详细的文档注释

### 4. 实际应用
- 数据验证和业务逻辑
- 状态管理和生命周期
- 权限控制和安全性
- 性能优化和资源管理
- 扩展性和维护性

## 练习建议

### 基础练习
1. 修改银行账户系统，添加定期存款功能
2. 扩展学生管理系统，增加课程评价功能
3. 完善图书馆系统，添加图书推荐算法
4. 优化员工系统，实现部门预算管理

### 进阶练习
1. 设计电商系统（商品、订单、用户、支付）
2. 实现游戏角色系统（角色、技能、装备、战斗）
3. 开发医院管理系统（患者、医生、科室、预约）
4. 创建学校管理系统（学生、教师、课程、排课）

### 高级练习
1. 使用设计模式重构现有代码
2. 添加数据持久化功能（文件/数据库）
3. 实现多线程安全的类设计
4. 集成Web框架创建API接口

## 下一步学习

1. **继承和多态** - 深入学习面向对象的核心特性
2. **异常处理** - 学习Python的异常处理机制
3. **模块和包** - 掌握代码组织和重用
4. **文件操作** - 学习数据持久化
5. **数据库操作** - 集成数据库存储
6. **Web开发** - 使用Flask/Django创建Web应用
7. **测试驱动开发** - 学习单元测试和集成测试
8. **设计模式** - 学习常用的设计模式

## 参考资料

- [Python官方文档 - 类](https://docs.python.org/3/tutorial/classes.html)
- [Python面向对象编程指南](https://realpython.com/python3-object-oriented-programming/)
- [设计模式：可复用面向对象软件的基础](https://book.douban.com/subject/1052241/)
- [重构：改善既有代码的设计](https://book.douban.com/subject/4262627/)
- [代码大全](https://book.douban.com/subject/1477390/)