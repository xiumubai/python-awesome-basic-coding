#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
类和对象综合练习

本文件包含多个综合练习，涵盖类和对象的所有重要概念：
1. 银行账户管理系统
2. 学生成绩管理系统
3. 图书馆管理系统
4. 员工管理系统
5. 电商购物车系统
6. 动物园管理系统
7. 车辆租赁系统
8. 在线课程系统

每个练习都包含完整的类设计、方法实现和测试代码。

作者: Python学习助手
日期: 2024
"""

import datetime
from typing import List, Dict, Optional

print("=== Python类和对象综合练习 ===")
print()

# 练习1: 银行账户管理系统
print("=== 练习1: 银行账户管理系统 ===")

class BankAccount:
    """银行账户类"""
    
    # 类属性
    bank_name = "Python银行"
    total_accounts = 0
    interest_rate = 0.03  # 3%年利率
    
    def __init__(self, account_holder, initial_balance=0):
        """初始化银行账户"""
        if initial_balance < 0:
            raise ValueError("初始余额不能为负数")
        
        BankAccount.total_accounts += 1
        self.__account_number = f"ACC{BankAccount.total_accounts:06d}"
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__transaction_history = []
        self.__is_active = True
        
        self._add_transaction("开户", initial_balance, "账户开立")
        print(f"账户 {self.__account_number} 开立成功，持有人: {account_holder}")
    
    @property
    def account_number(self):
        """获取账户号码"""
        return self.__account_number
    
    @property
    def account_holder(self):
        """获取账户持有人"""
        return self.__account_holder
    
    @property
    def balance(self):
        """获取账户余额"""
        return self.__balance
    
    @property
    def is_active(self):
        """检查账户是否激活"""
        return self.__is_active
    
    def _add_transaction(self, transaction_type, amount, description=""):
        """添加交易记录（私有方法）"""
        transaction = {
            'timestamp': datetime.datetime.now(),
            'type': transaction_type,
            'amount': amount,
            'balance': self.__balance,
            'description': description
        }
        self.__transaction_history.append(transaction)
    
    def deposit(self, amount):
        """存款"""
        if not self.__is_active:
            raise RuntimeError("账户已冻结")
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        
        self.__balance += amount
        self._add_transaction("存款", amount, f"存入 ¥{amount}")
        print(f"存款成功，金额: ¥{amount}，余额: ¥{self.__balance}")
        return self.__balance
    
    def withdraw(self, amount):
        """取款"""
        if not self.__is_active:
            raise RuntimeError("账户已冻结")
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        if amount > self.__balance:
            raise ValueError(f"余额不足，当前余额: ¥{self.__balance}")
        
        self.__balance -= amount
        self._add_transaction("取款", -amount, f"取出 ¥{amount}")
        print(f"取款成功，金额: ¥{amount}，余额: ¥{self.__balance}")
        return self.__balance
    
    def transfer(self, target_account, amount):
        """转账"""
        if not isinstance(target_account, BankAccount):
            raise TypeError("目标必须是银行账户")
        if not self.__is_active or not target_account.is_active:
            raise RuntimeError("账户已冻结")
        
        # 从当前账户扣款
        self.withdraw(amount)
        # 向目标账户存款
        target_account.deposit(amount)
        
        # 更新交易记录
        self._add_transaction("转出", -amount, f"转账至 {target_account.account_number}")
        target_account._add_transaction("转入", amount, f"来自 {self.__account_number}")
        
        print(f"转账成功: ¥{amount} 从 {self.__account_number} 转至 {target_account.account_number}")
    
    def calculate_interest(self, months=12):
        """计算利息"""
        if self.__balance <= 0:
            return 0
        
        monthly_rate = BankAccount.interest_rate / 12
        interest = self.__balance * monthly_rate * months
        return round(interest, 2)
    
    def add_interest(self, months=12):
        """添加利息到账户"""
        interest = self.calculate_interest(months)
        if interest > 0:
            self.__balance += interest
            self._add_transaction("利息", interest, f"{months}个月利息")
            print(f"利息添加成功: ¥{interest}，余额: ¥{self.__balance}")
        return interest
    
    def freeze_account(self):
        """冻结账户"""
        self.__is_active = False
        self._add_transaction("冻结", 0, "账户被冻结")
        print(f"账户 {self.__account_number} 已冻结")
    
    def unfreeze_account(self):
        """解冻账户"""
        self.__is_active = True
        self._add_transaction("解冻", 0, "账户已解冻")
        print(f"账户 {self.__account_number} 已解冻")
    
    def get_transaction_history(self, limit=10):
        """获取交易历史"""
        return self.__transaction_history[-limit:]
    
    def print_statement(self):
        """打印账户对账单"""
        print(f"\n=== {BankAccount.bank_name} 账户对账单 ===")
        print(f"账户号码: {self.__account_number}")
        print(f"持有人: {self.__account_holder}")
        print(f"当前余额: ¥{self.__balance}")
        print(f"账户状态: {'激活' if self.__is_active else '冻结'}")
        print("\n最近交易记录:")
        
        for transaction in self.__transaction_history[-5:]:
            timestamp = transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
            print(f"  {timestamp} | {transaction['type']} | ¥{transaction['amount']:+.2f} | 余额: ¥{transaction['balance']:.2f} | {transaction['description']}")
    
    @classmethod
    def get_total_accounts(cls):
        """获取账户总数"""
        return cls.total_accounts
    
    @classmethod
    def set_interest_rate(cls, rate):
        """设置利率"""
        if not 0 <= rate <= 1:
            raise ValueError("利率必须在0-1之间")
        cls.interest_rate = rate
        print(f"银行利率已设置为: {rate*100}%")
    
    @staticmethod
    def validate_account_number(account_number):
        """验证账户号码格式"""
        return account_number.startswith('ACC') and len(account_number) == 9
    
    def __str__(self):
        status = "激活" if self.__is_active else "冻结"
        return f"BankAccount({self.__account_number}, {self.__account_holder}, ¥{self.__balance}, {status})"

# 测试银行账户系统
print("创建银行账户:")
account1 = BankAccount("张三", 1000)
account2 = BankAccount("李四", 500)
account3 = BankAccount("王五")

print(f"\n银行总账户数: {BankAccount.get_total_accounts()}")

print("\n进行银行操作:")
account1.deposit(500)
account1.withdraw(200)
account1.transfer(account2, 300)

print("\n计算和添加利息:")
interest = account2.calculate_interest(6)  # 6个月利息
print(f"账户2的6个月利息: ¥{interest}")
account2.add_interest(6)

print("\n打印对账单:")
account1.print_statement()
account2.print_statement()

print("\n测试账户冻结:")
account3.freeze_account()
try:
    account3.deposit(100)
except RuntimeError as e:
    print(f"操作失败: {e}")

account3.unfreeze_account()
account3.deposit(100)
print()

# 练习2: 学生成绩管理系统
print("=== 练习2: 学生成绩管理系统 ===")

class Subject:
    """科目类"""
    
    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits
    
    def __str__(self):
        return f"Subject({self.code}: {self.name}, {self.credits}学分)"

class Grade:
    """成绩类"""
    
    def __init__(self, subject, score, semester):
        self.subject = subject
        self.score = score
        self.semester = semester
        self.grade_point = self._calculate_grade_point(score)
        self.letter_grade = self._get_letter_grade(score)
    
    @staticmethod
    def _calculate_grade_point(score):
        """计算绩点"""
        if score >= 90:
            return 4.0
        elif score >= 80:
            return 3.0 + (score - 80) * 0.1
        elif score >= 70:
            return 2.0 + (score - 70) * 0.1
        elif score >= 60:
            return 1.0 + (score - 60) * 0.1
        else:
            return 0.0
    
    @staticmethod
    def _get_letter_grade(score):
        """获取等级成绩"""
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        return f"Grade({self.subject.name}: {self.score}分, {self.letter_grade}, GPA:{self.grade_point:.2f})"

class Student:
    """学生类"""
    
    total_students = 0
    
    def __init__(self, name, student_id, major):
        Student.total_students += 1
        self.name = name
        self.student_id = student_id
        self.major = major
        self.grades = []  # 存储Grade对象
        self.enrollment_date = datetime.date.today()
        print(f"学生 {self.name}({self.student_id}) 注册成功，专业: {self.major}")
    
    def add_grade(self, subject, score, semester):
        """添加成绩"""
        if not 0 <= score <= 100:
            raise ValueError("成绩必须在0-100之间")
        
        grade = Grade(subject, score, semester)
        self.grades.append(grade)
        print(f"成绩添加成功: {self.name} - {subject.name}: {score}分")
        return grade
    
    def get_gpa(self, semester=None):
        """计算GPA"""
        if semester:
            semester_grades = [g for g in self.grades if g.semester == semester]
        else:
            semester_grades = self.grades
        
        if not semester_grades:
            return 0.0
        
        total_points = sum(g.grade_point * g.subject.credits for g in semester_grades)
        total_credits = sum(g.subject.credits for g in semester_grades)
        
        return round(total_points / total_credits, 2) if total_credits > 0 else 0.0
    
    def get_total_credits(self, semester=None):
        """获取总学分"""
        if semester:
            semester_grades = [g for g in self.grades if g.semester == semester]
        else:
            semester_grades = self.grades
        
        return sum(g.subject.credits for g in semester_grades)
    
    def get_grades_by_semester(self, semester):
        """按学期获取成绩"""
        return [g for g in self.grades if g.semester == semester]
    
    def get_subject_grade(self, subject_code):
        """获取特定科目成绩"""
        for grade in self.grades:
            if grade.subject.code == subject_code:
                return grade
        return None
    
    def print_transcript(self):
        """打印成绩单"""
        print(f"\n=== {self.name} 成绩单 ===")
        print(f"学号: {self.student_id}")
        print(f"专业: {self.major}")
        print(f"入学日期: {self.enrollment_date}")
        print(f"总GPA: {self.get_gpa()}")
        print(f"总学分: {self.get_total_credits()}")
        
        # 按学期分组显示
        semesters = set(g.semester for g in self.grades)
        for semester in sorted(semesters):
            print(f"\n{semester}学期:")
            semester_grades = self.get_grades_by_semester(semester)
            for grade in semester_grades:
                print(f"  {grade.subject.code} {grade.subject.name}: {grade.score}分 ({grade.letter_grade}) GPA:{grade.grade_point:.2f} {grade.subject.credits}学分")
            print(f"  学期GPA: {self.get_gpa(semester)}")
            print(f"  学期学分: {self.get_total_credits(semester)}")
    
    @classmethod
    def get_total_students(cls):
        """获取学生总数"""
        return cls.total_students
    
    def __str__(self):
        return f"Student({self.student_id}: {self.name}, {self.major}, GPA:{self.get_gpa()})"

# 测试学生成绩管理系统
print("创建科目:")
math = Subject("高等数学", "MATH101", 4)
physics = Subject("大学物理", "PHYS101", 3)
chemistry = Subject("普通化学", "CHEM101", 3)
engineering = Subject("工程导论", "ENG101", 2)

print("\n创建学生:")
student1 = Student("张三", "2024001", "计算机科学")
student2 = Student("李四", "2024002", "电子工程")

print("\n添加成绩:")
student1.add_grade(math, 92, "2024春季")
student1.add_grade(physics, 88, "2024春季")
student1.add_grade(chemistry, 85, "2024春季")
student1.add_grade(engineering, 95, "2024春季")

student2.add_grade(math, 78, "2024春季")
student2.add_grade(physics, 82, "2024春季")
student2.add_grade(engineering, 90, "2024春季")

print("\n打印成绩单:")
student1.print_transcript()
student2.print_transcript()

print(f"\n学生总数: {Student.get_total_students()}")
print()

# 练习3: 图书馆管理系统
print("=== 练习3: 图书馆管理系统 ===")

class Book:
    """图书类"""
    
    def __init__(self, title, author, isbn, category, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.total_copies = copies
        self.available_copies = copies
        self.borrowed_by = []  # 借阅记录
    
    def is_available(self):
        """检查是否有可借阅的副本"""
        return self.available_copies > 0
    
    def borrow(self, member):
        """借阅图书"""
        if not self.is_available():
            raise ValueError(f"图书 '{self.title}' 暂无可借副本")
        
        self.available_copies -= 1
        borrow_record = {
            'member': member,
            'borrow_date': datetime.date.today(),
            'due_date': datetime.date.today() + datetime.timedelta(days=30),
            'returned': False
        }
        self.borrowed_by.append(borrow_record)
        print(f"图书借阅成功: {member.name} 借阅了 '{self.title}'")
        return borrow_record
    
    def return_book(self, member):
        """归还图书"""
        for record in self.borrowed_by:
            if record['member'] == member and not record['returned']:
                record['returned'] = True
                record['return_date'] = datetime.date.today()
                self.available_copies += 1
                print(f"图书归还成功: {member.name} 归还了 '{self.title}'")
                return record
        
        raise ValueError(f"{member.name} 没有借阅图书 '{self.title}'")
    
    def get_overdue_records(self):
        """获取逾期记录"""
        today = datetime.date.today()
        overdue = []
        for record in self.borrowed_by:
            if not record['returned'] and record['due_date'] < today:
                overdue.append(record)
        return overdue
    
    def __str__(self):
        return f"Book('{self.title}' by {self.author}, {self.available_copies}/{self.total_copies} available)"

class Member:
    """图书馆会员类"""
    
    total_members = 0
    
    def __init__(self, name, member_id, member_type="普通会员"):
        Member.total_members += 1
        self.name = name
        self.member_id = member_id
        self.member_type = member_type
        self.borrowed_books = []
        self.join_date = datetime.date.today()
        self.max_books = 5 if member_type == "VIP会员" else 3
        print(f"会员 {self.name}({self.member_id}) 注册成功，类型: {self.member_type}")
    
    def can_borrow(self):
        """检查是否可以借阅更多图书"""
        current_borrowed = len([book for book in self.borrowed_books if not self._is_returned(book)])
        return current_borrowed < self.max_books
    
    def _is_returned(self, book):
        """检查图书是否已归还"""
        for record in book.borrowed_by:
            if record['member'] == self and not record['returned']:
                return False
        return True
    
    def borrow_book(self, book):
        """借阅图书"""
        if not self.can_borrow():
            raise ValueError(f"借阅数量已达上限 ({self.max_books}本)")
        
        record = book.borrow(self)
        self.borrowed_books.append(book)
        return record
    
    def return_book(self, book):
        """归还图书"""
        record = book.return_book(self)
        return record
    
    def get_borrowed_books(self):
        """获取当前借阅的图书"""
        current_books = []
        for book in self.borrowed_books:
            if not self._is_returned(book):
                current_books.append(book)
        return current_books
    
    def get_overdue_books(self):
        """获取逾期图书"""
        overdue_books = []
        for book in self.borrowed_books:
            overdue_records = book.get_overdue_records()
            for record in overdue_records:
                if record['member'] == self:
                    overdue_books.append((book, record))
        return overdue_books
    
    def print_borrowing_history(self):
        """打印借阅历史"""
        print(f"\n=== {self.name} 借阅历史 ===")
        print(f"会员号: {self.member_id}")
        print(f"会员类型: {self.member_type}")
        print(f"加入日期: {self.join_date}")
        
        current_books = self.get_borrowed_books()
        print(f"\n当前借阅 ({len(current_books)}/{self.max_books}):")
        for book in current_books:
            for record in book.borrowed_by:
                if record['member'] == self and not record['returned']:
                    days_left = (record['due_date'] - datetime.date.today()).days
                    status = f"还有{days_left}天" if days_left > 0 else f"逾期{-days_left}天"
                    print(f"  '{book.title}' - 借阅日期: {record['borrow_date']}, 到期日期: {record['due_date']} ({status})")
        
        overdue_books = self.get_overdue_books()
        if overdue_books:
            print(f"\n逾期图书 ({len(overdue_books)}本):")
            for book, record in overdue_books:
                days_overdue = (datetime.date.today() - record['due_date']).days
                print(f"  '{book.title}' - 逾期{days_overdue}天")
    
    @classmethod
    def get_total_members(cls):
        """获取会员总数"""
        return cls.total_members
    
    def __str__(self):
        return f"Member({self.member_id}: {self.name}, {self.member_type})"

class Library:
    """图书馆类"""
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        """添加图书"""
        self.books.append(book)
        print(f"图书添加成功: '{book.title}'")
    
    def add_member(self, member):
        """添加会员"""
        self.members.append(member)
        print(f"会员添加成功: {member.name}")
    
    def search_books(self, keyword):
        """搜索图书"""
        results = []
        keyword = keyword.lower()
        for book in self.books:
            if (keyword in book.title.lower() or 
                keyword in book.author.lower() or 
                keyword in book.category.lower()):
                results.append(book)
        return results
    
    def get_available_books(self):
        """获取可借阅图书"""
        return [book for book in self.books if book.is_available()]
    
    def get_overdue_books(self):
        """获取所有逾期图书"""
        overdue_list = []
        for book in self.books:
            overdue_records = book.get_overdue_records()
            for record in overdue_records:
                overdue_list.append((book, record))
        return overdue_list
    
    def print_library_status(self):
        """打印图书馆状态"""
        print(f"\n=== {self.name} 状态报告 ===")
        print(f"图书总数: {len(self.books)}")
        print(f"会员总数: {len(self.members)}")
        
        available_books = self.get_available_books()
        print(f"可借图书: {len(available_books)}")
        
        overdue_books = self.get_overdue_books()
        print(f"逾期图书: {len(overdue_books)}")
        
        if overdue_books:
            print("\n逾期详情:")
            for book, record in overdue_books:
                days_overdue = (datetime.date.today() - record['due_date']).days
                print(f"  '{book.title}' - {record['member'].name} - 逾期{days_overdue}天")

# 测试图书馆管理系统
print("创建图书馆:")
library = Library("Python学习图书馆")

print("\n添加图书:")
book1 = Book("Python编程从入门到实践", "埃里克·马瑟斯", "9787115428028", "编程", 3)
book2 = Book("算法导论", "托马斯·科尔曼", "9787111407010", "算法", 2)
book3 = Book("深度学习", "伊恩·古德费洛", "9787115461476", "人工智能", 1)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("\n添加会员:")
member1 = Member("张三", "M001", "普通会员")
member2 = Member("李四", "M002", "VIP会员")

library.add_member(member1)
library.add_member(member2)

print("\n借阅图书:")
member1.borrow_book(book1)
member1.borrow_book(book2)
member2.borrow_book(book3)

print("\n搜索图书:")
search_results = library.search_books("Python")
print(f"搜索'Python'的结果: {len(search_results)}本")
for book in search_results:
    print(f"  {book}")

print("\n打印借阅历史:")
member1.print_borrowing_history()
member2.print_borrowing_history()

print("\n归还图书:")
member1.return_book(book1)

print("\n图书馆状态:")
library.print_library_status()
print()

# 练习4: 员工管理系统
print("=== 练习4: 员工管理系统 ===")

class Employee:
    """员工基类"""
    
    total_employees = 0
    company_name = "Python科技有限公司"
    
    def __init__(self, name, employee_id, department, base_salary):
        Employee.total_employees += 1
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.base_salary = base_salary
        self.hire_date = datetime.date.today()
        self.is_active = True
        print(f"员工 {self.name}({self.employee_id}) 入职成功，部门: {self.department}")
    
    def calculate_salary(self):
        """计算工资（基类方法，子类可重写）"""
        return self.base_salary
    
    def get_work_years(self):
        """获取工作年限"""
        today = datetime.date.today()
        years = (today - self.hire_date).days / 365.25
        return round(years, 1)
    
    def promote(self, new_department, salary_increase):
        """升职"""
        old_department = self.department
        self.department = new_department
        self.base_salary += salary_increase
        print(f"{self.name} 升职成功: {old_department} -> {new_department}, 薪资增加: ¥{salary_increase}")
    
    def terminate(self):
        """离职"""
        self.is_active = False
        print(f"{self.name} 已离职")
    
    @classmethod
    def get_total_employees(cls):
        """获取员工总数"""
        return cls.total_employees
    
    @classmethod
    def get_company_name(cls):
        """获取公司名称"""
        return cls.company_name
    
    def __str__(self):
        status = "在职" if self.is_active else "离职"
        return f"Employee({self.employee_id}: {self.name}, {self.department}, ¥{self.base_salary}, {status})"

class Developer(Employee):
    """开发人员类"""
    
    def __init__(self, name, employee_id, base_salary, programming_languages=None):
        super().__init__(name, employee_id, "技术部", base_salary)
        self.programming_languages = programming_languages or []
        self.projects_completed = 0
        self.code_reviews = 0
    
    def add_programming_language(self, language):
        """添加编程语言技能"""
        if language not in self.programming_languages:
            self.programming_languages.append(language)
            print(f"{self.name} 掌握了新技能: {language}")
    
    def complete_project(self):
        """完成项目"""
        self.projects_completed += 1
        print(f"{self.name} 完成了一个项目，总计: {self.projects_completed}个")
    
    def conduct_code_review(self):
        """进行代码审查"""
        self.code_reviews += 1
        print(f"{self.name} 进行了代码审查，总计: {self.code_reviews}次")
    
    def calculate_salary(self):
        """计算开发人员工资（包含项目奖金）"""
        project_bonus = self.projects_completed * 1000
        review_bonus = self.code_reviews * 200
        skill_bonus = len(self.programming_languages) * 500
        return self.base_salary + project_bonus + review_bonus + skill_bonus
    
    def get_performance_summary(self):
        """获取绩效总结"""
        return {
            'projects_completed': self.projects_completed,
            'code_reviews': self.code_reviews,
            'programming_languages': len(self.programming_languages),
            'total_salary': self.calculate_salary()
        }
    
    def __str__(self):
        return f"Developer({self.employee_id}: {self.name}, {len(self.programming_languages)}种语言, {self.projects_completed}个项目)"

class Manager(Employee):
    """管理人员类"""
    
    def __init__(self, name, employee_id, base_salary, team_size=0):
        super().__init__(name, employee_id, "管理部", base_salary)
        self.team_size = team_size
        self.meetings_held = 0
        self.team_members = []
    
    def add_team_member(self, employee):
        """添加团队成员"""
        if employee not in self.team_members:
            self.team_members.append(employee)
            self.team_size = len(self.team_members)
            print(f"{employee.name} 加入了 {self.name} 的团队")
    
    def remove_team_member(self, employee):
        """移除团队成员"""
        if employee in self.team_members:
            self.team_members.remove(employee)
            self.team_size = len(self.team_members)
            print(f"{employee.name} 离开了 {self.name} 的团队")
    
    def hold_meeting(self):
        """召开会议"""
        self.meetings_held += 1
        print(f"{self.name} 召开了会议，总计: {self.meetings_held}次")
    
    def calculate_salary(self):
        """计算管理人员工资（包含管理奖金）"""
        team_bonus = self.team_size * 800
        meeting_bonus = self.meetings_held * 300
        return self.base_salary + team_bonus + meeting_bonus
    
    def get_team_performance(self):
        """获取团队绩效"""
        total_projects = 0
        total_reviews = 0
        
        for member in self.team_members:
            if isinstance(member, Developer):
                total_projects += member.projects_completed
                total_reviews += member.code_reviews
        
        return {
            'team_size': self.team_size,
            'total_projects': total_projects,
            'total_reviews': total_reviews,
            'meetings_held': self.meetings_held
        }
    
    def __str__(self):
        return f"Manager({self.employee_id}: {self.name}, 团队{self.team_size}人, {self.meetings_held}次会议)"

# 测试员工管理系统
print("创建员工:")
dev1 = Developer("张三", "DEV001", 15000, ["Python", "JavaScript"])
dev2 = Developer("李四", "DEV002", 12000, ["Java", "C++"])
manager1 = Manager("王五", "MGR001", 20000)

print(f"\n公司: {Employee.get_company_name()}")
print(f"员工总数: {Employee.get_total_employees()}")

print("\n开发人员工作:")
dev1.add_programming_language("Go")
dev1.complete_project()
dev1.complete_project()
dev1.conduct_code_review()

dev2.complete_project()
dev2.conduct_code_review()
dev2.conduct_code_review()

print("\n管理人员工作:")
manager1.add_team_member(dev1)
manager1.add_team_member(dev2)
manager1.hold_meeting()
manager1.hold_meeting()

print("\n计算工资:")
print(f"{dev1.name} 工资: ¥{dev1.calculate_salary()}")
print(f"{dev2.name} 工资: ¥{dev2.calculate_salary()}")
print(f"{manager1.name} 工资: ¥{manager1.calculate_salary()}")

print("\n绩效报告:")
print(f"{dev1.name} 绩效: {dev1.get_performance_summary()}")
print(f"{manager1.name} 团队绩效: {manager1.get_team_performance()}")

print("\n员工升职:")
dev1.promote("高级技术部", 3000)
print()

print("=== 综合练习总结 ===")
print()
print("通过以上练习，你已经掌握了：")
print("1. 类的设计和实现")
print("2. 继承和多态的应用")
print("3. 封装和访问控制")
print("4. 类方法和静态方法的使用")
print("5. 属性管理和验证")
print("6. 复杂业务逻辑的面向对象建模")
print("7. 类之间的关系和交互")
print("8. 实际项目中的类设计模式")
print()
print("=== 程序执行完成 ===")
print("恭喜！你已经完成了Python类和对象的所有学习内容。")
print("继续加油，探索更多Python高级特性！")