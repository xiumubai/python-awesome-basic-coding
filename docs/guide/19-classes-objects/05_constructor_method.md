# 构造方法__init__

## 学习目标
- 深入理解构造方法的作用和重要性
- 掌握__init__方法的定义和使用
- 学会处理构造方法的参数和默认值
- 理解对象初始化的完整过程
- 掌握构造方法的高级用法和最佳实践

## 构造方法基础

### 什么是构造方法

构造方法`__init__`是Python类中的特殊方法，用于初始化新创建的对象实例。当使用类名创建对象时，Python会自动调用这个方法来设置对象的初始状态。

```python
class Book:
    """图书类 - 演示构造方法基础用法"""
    
    def __init__(self, title, author, isbn, pages=0, price=0.0):
        """构造方法 - 初始化图书对象
        
        Args:
            title (str): 书名
            author (str): 作者
            isbn (str): ISBN号
            pages (int): 页数，默认为0
            price (float): 价格，默认为0.0
        """
        print(f"正在创建图书对象: {title}")
        
        # 基本属性初始化
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages
        self.price = price
        
        # 自动生成的属性
        self.creation_time = self._get_current_time()
        self.book_id = self._generate_book_id()
        
        # 状态属性
        self.is_available = True
        self.borrow_count = 0
        self.rating = 0.0
        self.reviews = []
        
        # 调用初始化后的设置
        self._post_init_setup()
        
        print(f"图书对象创建完成，ID: {self.book_id}")
    
    def _get_current_time(self):
        """获取当前时间"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _generate_book_id(self):
        """生成图书ID"""
        import hashlib
        # 使用ISBN和创建时间生成唯一ID
        data = f"{self.isbn}_{self.creation_time}"
        return hashlib.md5(data.encode()).hexdigest()[:8].upper()
    
    def _post_init_setup(self):
        """初始化后的额外设置"""
        # 根据页数设置图书类型
        if self.pages < 100:
            self.book_type = "小册子"
        elif self.pages < 300:
            self.book_type = "普通图书"
        elif self.pages < 600:
            self.book_type = "厚书"
        else:
            self.book_type = "巨著"
        
        # 根据价格设置价格等级
        if self.price < 20:
            self.price_level = "经济型"
        elif self.price < 50:
            self.price_level = "标准型"
        elif self.price < 100:
            self.price_level = "高端型"
        else:
            self.price_level = "奢华型"
    
    def get_book_info(self):
        """获取图书完整信息"""
        return {
            "ID": self.book_id,
            "书名": self.title,
            "作者": self.author,
            "ISBN": self.isbn,
            "页数": self.pages,
            "价格": f"¥{self.price:.2f}",
            "类型": self.book_type,
            "价格等级": self.price_level,
            "创建时间": self.creation_time,
            "可借阅": "是" if self.is_available else "否",
            "借阅次数": self.borrow_count,
            "评分": self.rating
        }
    
    def add_review(self, rating, comment):
        """添加评价"""
        if not 1 <= rating <= 5:
            raise ValueError("评分必须在1-5之间")
        
        review = {
            "rating": rating,
            "comment": comment,
            "time": self._get_current_time()
        }
        self.reviews.append(review)
        
        # 重新计算平均评分
        total_rating = sum(review["rating"] for review in self.reviews)
        self.rating = total_rating / len(self.reviews)
        
        return f"评价已添加，当前平均评分: {self.rating:.1f}"
    
    def borrow(self):
        """借阅图书"""
        if not self.is_available:
            return "图书已被借出"
        
        self.is_available = False
        self.borrow_count += 1
        return f"借阅成功，这是第 {self.borrow_count} 次借阅"
    
    def return_book(self):
        """归还图书"""
        if self.is_available:
            return "图书未被借出"
        
        self.is_available = True
        return "归还成功"
    
    def __str__(self):
        return f"《{self.title}》 - {self.author}"
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"

# 构造方法基础演示
print("=== 构造方法基础演示 ===")

# 创建图书对象
print("创建图书1:")
book1 = Book("Python编程", "张三", "978-1234567890", 450, 89.99)

print("\n创建图书2（使用默认参数）:")
book2 = Book("数据结构", "李四", "978-0987654321")

print("\n创建图书3（指定部分参数）:")
book3 = Book("算法导论", "王五", "978-1122334455", pages=800)

print("\n=== 查看图书信息 ===")
print("图书1信息:")
for key, value in book1.get_book_info().items():
    print(f"  {key}: {value}")

print("\n图书2信息:")
for key, value in book2.get_book_info().items():
    print(f"  {key}: {value}")

print("\n图书3信息:")
for key, value in book3.get_book_info().items():
    print(f"  {key}: {value}")

print("\n=== 图书操作测试 ===")
print(book1.add_review(5, "非常好的Python教程"))
print(book1.add_review(4, "内容详实，推荐阅读"))
print(book1.borrow())
print(book1.borrow())  # 重复借阅
print(book1.return_book())

print(f"\n最终图书1信息: {book1}")
print(f"图书1详细信息: {book1.get_book_info()}")
```

### 构造方法的参数处理

```python
class Student:
    """学生类 - 演示构造方法的高级参数处理"""
    
    # 类属性 - 用于生成学号
    _next_student_id = 1
    _all_students = []
    
    def __init__(self, name, age=18, gender="未知", *subjects, **extra_info):
        """构造方法 - 支持可变参数和关键字参数
        
        Args:
            name (str): 学生姓名（必需）
            age (int): 年龄，默认18
            gender (str): 性别，默认"未知"
            *subjects: 可变参数，学习的科目列表
            **extra_info: 关键字参数，额外信息
        """
        # 参数验证
        self._validate_parameters(name, age, gender)
        
        # 基本信息
        self.name = name
        self.age = age
        self.gender = gender
        
        # 自动生成学号
        self.student_id = f"STU{Student._next_student_id:06d}"
        Student._next_student_id += 1
        
        # 处理科目列表
        self.subjects = list(subjects) if subjects else []
        
        # 处理额外信息
        self.extra_info = extra_info.copy()
        
        # 初始化其他属性
        self.grades = {}
        self.enrollment_date = self._get_current_date()
        self.is_active = True
        
        # 从额外信息中提取常用字段
        self.email = extra_info.get('email', '')
        self.phone = extra_info.get('phone', '')
        self.address = extra_info.get('address', '')
        self.emergency_contact = extra_info.get('emergency_contact', '')
        
        # 初始化成绩字典
        for subject in self.subjects:
            self.grades[subject] = []
        
        # 添加到学生列表
        Student._all_students.append(self)
        
        print(f"学生 {self.name}（{self.student_id}）注册成功")
    
    def _validate_parameters(self, name, age, gender):
        """验证构造参数"""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("姓名必须是非空字符串")
        
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError("年龄必须是0-150之间的整数")
        
        if not isinstance(gender, str):
            raise ValueError("性别必须是字符串")
        
        valid_genders = ["男", "女", "未知", "其他"]
        if gender not in valid_genders:
            print(f"警告: 性别 '{gender}' 不在标准列表中 {valid_genders}")
    
    def _get_current_date(self):
        """获取当前日期"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d")
    
    def add_subject(self, subject):
        """添加科目"""
        if subject not in self.subjects:
            self.subjects.append(subject)
            self.grades[subject] = []
            return f"科目 '{subject}' 已添加"
        return f"科目 '{subject}' 已存在"
    
    def add_grade(self, subject, score):
        """添加成绩"""
        if subject not in self.subjects:
            self.add_subject(subject)
        
        if not 0 <= score <= 100:
            raise ValueError("成绩必须在0-100之间")
        
        self.grades[subject].append({
            "score": score,
            "date": self._get_current_date()
        })
        return f"{subject} 成绩 {score} 已添加"
    
    def get_average_grade(self, subject=None):
        """获取平均成绩"""
        if subject:
            if subject in self.grades and self.grades[subject]:
                scores = [grade["score"] for grade in self.grades[subject]]
                return sum(scores) / len(scores)
            return 0
        
        # 计算总平均成绩
        all_scores = []
        for subject_grades in self.grades.values():
            all_scores.extend([grade["score"] for grade in subject_grades])
        
        return sum(all_scores) / len(all_scores) if all_scores else 0
    
    def update_info(self, **kwargs):
        """更新学生信息"""
        updatable_fields = ['age', 'gender', 'email', 'phone', 'address', 'emergency_contact']
        updated_fields = []
        
        for key, value in kwargs.items():
            if key in updatable_fields:
                setattr(self, key, value)
                self.extra_info[key] = value
                updated_fields.append(key)
            else:
                print(f"警告: 字段 '{key}' 不可更新")
        
        return f"已更新字段: {updated_fields}"
    
    def get_student_summary(self):
        """获取学生摘要信息"""
        return {
            "学号": self.student_id,
            "姓名": self.name,
            "年龄": self.age,
            "性别": self.gender,
            "科目数量": len(self.subjects),
            "科目列表": self.subjects,
            "总平均成绩": round(self.get_average_grade(), 2),
            "注册日期": self.enrollment_date,
            "状态": "在读" if self.is_active else "休学",
            "联系邮箱": self.email,
            "联系电话": self.phone
        }
    
    @classmethod
    def get_student_count(cls):
        """获取学生总数"""
        return len(cls._all_students)
    
    @classmethod
    def find_student_by_id(cls, student_id):
        """根据学号查找学生"""
        for student in cls._all_students:
            if student.student_id == student_id:
                return student
        return None
    
    @classmethod
    def get_all_students_summary(cls):
        """获取所有学生摘要"""
        return [student.get_student_summary() for student in cls._all_students]
    
    def __str__(self):
        return f"学生: {self.name}（{self.student_id}）"
    
    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, student_id='{self.student_id}')"

# 构造方法参数处理演示
print("\n=== 构造方法参数处理演示 ===")

# 创建不同参数组合的学生
print("创建学生1（基本参数）:")
student1 = Student("张三", 20, "男")

print("\n创建学生2（带科目的可变参数）:")
student2 = Student("李四", 19, "女", "数学", "物理", "化学")

print("\n创建学生3（带额外信息的关键字参数）:")
student3 = Student(
    "王五", 21, "男", "计算机科学", "数据结构",
    email="wangwu@example.com",
    phone="13800138000",
    address="北京市朝阳区",
    emergency_contact="王父 13900139000",
    hobby="编程",
    scholarship=True
)

print("\n创建学生4（使用默认参数）:")
student4 = Student("赵六", subjects=["英语", "文学"], email="zhaoliu@example.com")

print("\n=== 学生信息展示 ===")
for i, student in enumerate([student1, student2, student3, student4], 1):
    print(f"\n学生{i}摘要:")
    summary = student.get_student_summary()
    for key, value in summary.items():
        print(f"  {key}: {value}")

print("\n=== 学生操作测试 ===")
print("为学生添加成绩:")
print(student2.add_grade("数学", 95))
print(student2.add_grade("物理", 88))
print(student2.add_grade("化学", 92))
print(student2.add_grade("数学", 90))  # 同一科目多次成绩

print(student3.add_grade("计算机科学", 98))
print(student3.add_grade("数据结构", 94))

print("\n成绩统计:")
print(f"学生2数学平均成绩: {student2.get_average_grade('数学'):.2f}")
print(f"学生2总平均成绩: {student2.get_average_grade():.2f}")
print(f"学生3总平均成绩: {student3.get_average_grade():.2f}")

print("\n更新学生信息:")
print(student1.update_info(age=21, email="zhangsan@example.com", phone="13700137000"))

print("\n=== 类方法测试 ===")
print(f"当前学生总数: {Student.get_student_count()}")

print("\n查找学生:")
found_student = Student.find_student_by_id(student2.student_id)
if found_student:
    print(f"找到学生: {found_student}")

print("\n所有学生列表:")
all_students = Student.get_all_students_summary()
for student_info in all_students:
    print(f"  {student_info['学号']}: {student_info['姓名']} - {student_info['科目数量']}门课程")
```

### 构造方法的继承和重写

```python
class Person:
    """人员基类"""
    
    def __init__(self, name, age, gender="未知"):
        """人员基类构造方法"""
        print(f"Person.__init__ 被调用: {name}")
        
        self.name = name
        self.age = age
        self.gender = gender
        self.creation_time = self._get_timestamp()
        self.person_id = self._generate_id()
        
        print(f"Person 对象初始化完成: {self.person_id}")
    
    def _get_timestamp(self):
        """获取时间戳"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _generate_id(self):
        """生成ID"""
        import random
        return f"P{random.randint(100000, 999999)}"
    
    def get_basic_info(self):
        """获取基本信息"""
        return {
            "ID": self.person_id,
            "姓名": self.name,
            "年龄": self.age,
            "性别": self.gender,
            "创建时间": self.creation_time
        }
    
    def __str__(self):
        return f"Person: {self.name}（{self.person_id}）"

class Employee(Person):
    """员工类 - 继承自Person"""
    
    def __init__(self, name, age, gender, employee_id, department, salary, **kwargs):
        """员工构造方法"""
        print(f"Employee.__init__ 开始: {name}")
        
        # 调用父类构造方法
        super().__init__(name, age, gender)
        
        # 员工特有属性
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        
        # 处理额外参数
        self.position = kwargs.get('position', '普通员工')
        self.hire_date = kwargs.get('hire_date', self._get_current_date())
        self.manager = kwargs.get('manager', None)
        self.skills = kwargs.get('skills', [])
        
        # 员工状态
        self.is_active = True
        self.performance_score = 0.0
        self.projects = []
        
        print(f"Employee 对象初始化完成: {self.employee_id}")
    
    def _get_current_date(self):
        """获取当前日期"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d")
    
    def add_skill(self, skill):
        """添加技能"""
        if skill not in self.skills:
            self.skills.append(skill)
            return f"技能 '{skill}' 已添加"
        return f"技能 '{skill}' 已存在"
    
    def assign_project(self, project_name):
        """分配项目"""
        project = {
            "name": project_name,
            "start_date": self._get_current_date(),
            "status": "进行中"
        }
        self.projects.append(project)
        return f"项目 '{project_name}' 已分配"
    
    def update_performance(self, score):
        """更新绩效分数"""
        if not 0 <= score <= 100:
            raise ValueError("绩效分数必须在0-100之间")
        
        self.performance_score = score
        return f"绩效分数已更新为: {score}"
    
    def get_employee_info(self):
        """获取员工完整信息"""
        basic_info = self.get_basic_info()
        employee_info = {
            "员工ID": self.employee_id,
            "部门": self.department,
            "职位": self.position,
            "薪资": f"¥{self.salary:,.2f}",
            "入职日期": self.hire_date,
            "直属经理": self.manager or "无",
            "技能数量": len(self.skills),
            "技能列表": self.skills,
            "项目数量": len(self.projects),
            "绩效分数": self.performance_score,
            "状态": "在职" if self.is_active else "离职"
        }
        
        # 合并基本信息和员工信息
        return {**basic_info, **employee_info}
    
    def __str__(self):
        return f"Employee: {self.name}（{self.employee_id}）- {self.department}"

class Manager(Employee):
    """经理类 - 继承自Employee"""
    
    def __init__(self, name, age, gender, employee_id, department, salary, team_size=0, **kwargs):
        """经理构造方法"""
        print(f"Manager.__init__ 开始: {name}")
        
        # 调用父类构造方法
        super().__init__(name, age, gender, employee_id, department, salary, **kwargs)
        
        # 经理特有属性
        self.team_size = team_size
        self.team_members = []
        self.budget = kwargs.get('budget', 0.0)
        self.management_level = kwargs.get('management_level', '中级')
        
        # 重写职位（如果没有指定）
        if 'position' not in kwargs:
            self.position = '部门经理'
        
        print(f"Manager 对象初始化完成: {self.employee_id}")
    
    def add_team_member(self, employee):
        """添加团队成员"""
        if isinstance(employee, Employee):
            if employee not in self.team_members:
                self.team_members.append(employee)
                employee.manager = self.name  # 设置员工的经理
                self.team_size = len(self.team_members)
                return f"员工 {employee.name} 已加入团队"
            return f"员工 {employee.name} 已在团队中"
        return "只能添加Employee对象"
    
    def remove_team_member(self, employee):
        """移除团队成员"""
        if employee in self.team_members:
            self.team_members.remove(employee)
            employee.manager = None
            self.team_size = len(self.team_members)
            return f"员工 {employee.name} 已离开团队"
        return f"员工 {employee.name} 不在团队中"
    
    def get_team_summary(self):
        """获取团队摘要"""
        if not self.team_members:
            return "团队为空"
        
        team_info = []
        total_salary = 0
        avg_performance = 0
        
        for member in self.team_members:
            team_info.append({
                "姓名": member.name,
                "员工ID": member.employee_id,
                "职位": member.position,
                "薪资": member.salary,
                "绩效": member.performance_score
            })
            total_salary += member.salary
            avg_performance += member.performance_score
        
        return {
            "团队规模": self.team_size,
            "团队成员": team_info,
            "团队总薪资": f"¥{total_salary:,.2f}",
            "平均绩效": round(avg_performance / self.team_size, 2) if self.team_size > 0 else 0,
            "管理预算": f"¥{self.budget:,.2f}"
        }
    
    def get_manager_info(self):
        """获取经理完整信息"""
        employee_info = self.get_employee_info()
        manager_info = {
            "管理级别": self.management_level,
            "团队规模": self.team_size,
            "管理预算": f"¥{self.budget:,.2f}",
            "团队成员": [member.name for member in self.team_members]
        }
        
        return {**employee_info, **manager_info}
    
    def __str__(self):
        return f"Manager: {self.name}（{self.employee_id}）- {self.department}，团队规模: {self.team_size}"

# 构造方法继承演示
print("\n=== 构造方法继承演示 ===")

# 创建基础人员
print("创建基础人员:")
person1 = Person("普通人员", 30, "男")
print(f"基础人员信息: {person1.get_basic_info()}")

print("\n创建员工:")
employee1 = Employee(
    "张工程师", 28, "男", "EMP001", "技术部", 15000,
    position="高级工程师",
    skills=["Python", "Java", "数据库"],
    hire_date="2023-01-15"
)

employee2 = Employee(
    "李设计师", 26, "女", "EMP002", "设计部", 12000,
    position="UI设计师",
    skills=["Photoshop", "Sketch", "Figma"]
)

employee3 = Employee(
    "王分析师", 29, "男", "EMP003", "技术部", 13000,
    position="数据分析师",
    skills=["Python", "R", "SQL", "Tableau"]
)

print("\n创建经理:")
manager1 = Manager(
    "陈经理", 35, "女", "MGR001", "技术部", 25000,
    position="技术总监",
    budget=500000,
    management_level="高级",
    skills=["团队管理", "项目管理", "技术架构"]
)

print("\n=== 员工信息展示 ===")
print("员工1信息:")
for key, value in employee1.get_employee_info().items():
    print(f"  {key}: {value}")

print("\n员工2信息:")
for key, value in employee2.get_employee_info().items():
    print(f"  {key}: {value}")

print("\n=== 团队管理演示 ===")
print("构建团队:")
print(manager1.add_team_member(employee1))
print(manager1.add_team_member(employee3))
print(manager1.add_team_member(employee2))  # 跨部门添加

print("\n为员工分配项目和更新绩效:")
print(employee1.assign_project("电商平台开发"))
print(employee1.assign_project("移动端APP"))
print(employee1.update_performance(92))

print(employee3.assign_project("数据分析报告"))
print(employee3.update_performance(88))

print(employee2.assign_project("UI界面设计"))
print(employee2.update_performance(95))

print("\n团队摘要:")
team_summary = manager1.get_team_summary()
for key, value in team_summary.items():
    if key == "团队成员":
        print(f"  {key}:")
        for member in value:
            print(f"    - {member['姓名']} ({member['职位']}) - 绩效: {member['绩效']}")
    else:
        print(f"  {key}: {value}")

print("\n经理完整信息:")
for key, value in manager1.get_manager_info().items():
    print(f"  {key}: {value}")

print("\n=== 继承关系验证 ===")
print(f"person1 是 Person 的实例: {isinstance(person1, Person)}")
print(f"employee1 是 Person 的实例: {isinstance(employee1, Person)}")
print(f"employee1 是 Employee 的实例: {isinstance(employee1, Employee)}")
print(f"manager1 是 Person 的实例: {isinstance(manager1, Person)}")
print(f"manager1 是 Employee 的实例: {isinstance(manager1, Employee)}")
print(f"manager1 是 Manager 的实例: {isinstance(manager1, Manager)}")

print("\n类的继承关系:")
print(f"Employee 的父类: {Employee.__bases__}")
print(f"Manager 的父类: {Manager.__bases__}")
print(f"Manager 的方法解析顺序: {Manager.__mro__}")
```

## 构造方法的高级特性

### 工厂方法和类方法构造

```python
class Configuration:
    """配置类 - 演示多种构造方式"""
    
    def __init__(self, config_dict=None):
        """标准构造方法"""
        self.config_dict = config_dict or {}
        self.creation_method = "standard"
        self.creation_time = self._get_timestamp()
        self.config_id = self._generate_id()
        
        # 验证配置
        self._validate_config()
        
        print(f"Configuration 对象创建: {self.config_id} (方式: {self.creation_method})")
    
    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _generate_id(self):
        import random
        return f"CFG{random.randint(1000, 9999)}"
    
    def _validate_config(self):
        """验证配置"""
        if not isinstance(self.config_dict, dict):
            raise TypeError("配置必须是字典类型")
    
    @classmethod
    def from_file(cls, file_path):
        """从文件创建配置对象"""
        print(f"从文件创建配置: {file_path}")
        
        # 模拟从文件读取配置
        try:
            # 这里模拟不同类型的配置文件
            if file_path.endswith('.json'):
                config_data = {
                    "database": {
                        "host": "localhost",
                        "port": 5432,
                        "name": "myapp"
                    },
                    "cache": {
                        "type": "redis",
                        "ttl": 3600
                    },
                    "debug": True
                }
            elif file_path.endswith('.yaml'):
                config_data = {
                    "server": {
                        "host": "0.0.0.0",
                        "port": 8000
                    },
                    "logging": {
                        "level": "INFO",
                        "file": "app.log"
                    }
                }
            else:
                config_data = {"source": "unknown_file"}
            
            # 创建实例
            instance = cls(config_data)
            instance.creation_method = "from_file"
            instance.source_file = file_path
            return instance
            
        except Exception as e:
            print(f"读取配置文件失败: {e}")
            return cls({})
    
    @classmethod
    def from_env(cls, prefix="APP_"):
        """从环境变量创建配置对象"""
        print(f"从环境变量创建配置，前缀: {prefix}")
        
        import os
        
        # 模拟环境变量
        mock_env = {
            "APP_DATABASE_HOST": "prod-db.example.com",
            "APP_DATABASE_PORT": "5432",
            "APP_DATABASE_NAME": "production",
            "APP_CACHE_TYPE": "memcached",
            "APP_DEBUG": "false",
            "APP_SECRET_KEY": "super-secret-key"
        }
        
        config_data = {}
        for key, value in mock_env.items():
            if key.startswith(prefix):
                # 移除前缀并转换为嵌套字典
                config_key = key[len(prefix):].lower()
                parts = config_key.split('_')
                
                # 构建嵌套字典
                current = config_data
                for part in parts[:-1]:
                    if part not in current:
                        current[part] = {}
                    current = current[part]
                
                # 尝试转换值的类型
                if value.lower() in ['true', 'false']:
                    value = value.lower() == 'true'
                elif value.isdigit():
                    value = int(value)
                
                current[parts[-1]] = value
        
        instance = cls(config_data)
        instance.creation_method = "from_env"
        instance.env_prefix = prefix
        return instance
    
    @classmethod
    def from_dict(cls, **kwargs):
        """从关键字参数创建配置对象"""
        print(f"从关键字参数创建配置: {len(kwargs)} 个参数")
        
        instance = cls(kwargs)
        instance.creation_method = "from_dict"
        return instance
    
    @classmethod
    def default_web_config(cls):
        """创建默认Web应用配置"""
        print("创建默认Web应用配置")
        
        default_config = {
            "server": {
                "host": "127.0.0.1",
                "port": 8000,
                "workers": 4
            },
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "webapp",
                "pool_size": 10
            },
            "cache": {
                "type": "redis",
                "host": "localhost",
                "port": 6379,
                "ttl": 3600
            },
            "security": {
                "secret_key": "dev-secret-key",
                "session_timeout": 1800
            },
            "logging": {
                "level": "DEBUG",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            },
            "features": {
                "debug": True,
                "testing": False,
                "maintenance_mode": False
            }
        }
        
        instance = cls(default_config)
        instance.creation_method = "default_web"
        return instance
    
    @classmethod
    def merge_configs(cls, *configs):
        """合并多个配置对象"""
        print(f"合并 {len(configs)} 个配置对象")
        
        merged_config = {}
        
        for config in configs:
            if isinstance(config, cls):
                merged_config.update(config.config_dict)
            elif isinstance(config, dict):
                merged_config.update(config)
            else:
                print(f"警告: 跳过无效配置类型 {type(config)}")
        
        instance = cls(merged_config)
        instance.creation_method = "merged"
        instance.source_configs = len(configs)
        return instance
    
    def get(self, key, default=None):
        """获取配置值（支持点号分隔的嵌套键）"""
        keys = key.split('.')
        current = self.config_dict
        
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return default
        
        return current
    
    def set(self, key, value):
        """设置配置值（支持点号分隔的嵌套键）"""
        keys = key.split('.')
        current = self.config_dict
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
    
    def get_config_summary(self):
        """获取配置摘要"""
        def count_nested_items(d):
            count = 0
            for value in d.values():
                if isinstance(value, dict):
                    count += count_nested_items(value)
                else:
                    count += 1
            return count
        
        return {
            "配置ID": self.config_id,
            "创建方式": self.creation_method,
            "创建时间": self.creation_time,
            "顶级键数量": len(self.config_dict),
            "总配置项数量": count_nested_items(self.config_dict),
            "源文件": getattr(self, 'source_file', '无'),
            "环境变量前缀": getattr(self, 'env_prefix', '无'),
            "源配置数量": getattr(self, 'source_configs', 1)
        }
    
    def export_to_dict(self):
        """导出为字典"""
        return self.config_dict.copy()
    
    def __str__(self):
        return f"Configuration({self.config_id}) - {len(self.config_dict)} 个顶级配置"
    
    def __repr__(self):
        return f"Configuration(config_id='{self.config_id}', method='{self.creation_method}')"

# 工厂方法演示
print("\n=== 工厂方法演示 ===")

# 标准构造方法
print("1. 标准构造方法:")
config1 = Configuration({"app_name": "MyApp", "version": "1.0.0"})
print(f"配置摘要: {config1.get_config_summary()}")

# 从文件创建
print("\n2. 从文件创建:")
config2 = Configuration.from_file("config.json")
config3 = Configuration.from_file("config.yaml")

print(f"JSON配置摘要: {config2.get_config_summary()}")
print(f"YAML配置摘要: {config3.get_config_summary()}")

# 从环境变量创建
print("\n3. 从环境变量创建:")
config4 = Configuration.from_env("APP_")
print(f"环境变量配置摘要: {config4.get_config_summary()}")

# 从关键字参数创建
print("\n4. 从关键字参数创建:")
config5 = Configuration.from_dict(
    api_key="abc123",
    timeout=30,
    retry_count=3,
    enable_logging=True
)
print(f"关键字参数配置摘要: {config5.get_config_summary()}")

# 默认Web配置
print("\n5. 默认Web配置:")
config6 = Configuration.default_web_config()
print(f"默认Web配置摘要: {config6.get_config_summary()}")

# 合并配置
print("\n6. 合并配置:")
config7 = Configuration.merge_configs(config1, config5, {"merged": True})
print(f"合并配置摘要: {config7.get_config_summary()}")

print("\n=== 配置操作演示 ===")
print("配置值获取:")
print(f"数据库主机: {config2.get('database.host')}")
print(f"数据库端口: {config2.get('database.port')}")
print(f"缓存TTL: {config2.get('cache.ttl')}")
print(f"不存在的配置: {config2.get('nonexistent.key', '默认值')}")

print("\n配置值设置:")
config2.set('new_feature.enabled', True)
config2.set('new_feature.config.timeout', 60)
print(f"新功能启用: {config2.get('new_feature.enabled')}")
print(f"新功能超时: {config2.get('new_feature.config.timeout')}")

print("\n所有配置对象:")
for i, config in enumerate([config1, config2, config3, config4, config5, config6, config7], 1):
    print(f"  配置{i}: {config}")
    summary = config.get_config_summary()
    print(f"    创建方式: {summary['创建方式']}, 配置项: {summary['总配置项数量']}")
```

## 学习要点总结

### 核心概念
1. **构造方法**：`__init__`是对象初始化的特殊方法
2. **自动调用**：创建对象时Python自动调用构造方法
3. **参数处理**：支持位置参数、默认参数、可变参数和关键字参数
4. **继承机制**：子类可以重写父类的构造方法

### 重要特性
1. **初始化顺序**：父类构造方法 → 子类构造方法
2. **参数验证**：在构造方法中验证参数的有效性
3. **属性设置**：在构造方法中设置对象的初始状态
4. **后处理**：可以在构造方法中进行额外的初始化工作

### 构造方法的类型
1. **标准构造**：直接使用`__init__`方法
2. **类方法构造**：使用`@classmethod`装饰的工厂方法
3. **静态方法构造**：使用`@staticmethod`的辅助构造方法
4. **继承构造**：通过`super()`调用父类构造方法

### 参数处理技巧
1. **默认参数**：为可选参数提供默认值
2. **可变参数**：使用`*args`处理不定数量的位置参数
3. **关键字参数**：使用`**kwargs`处理不定数量的关键字参数
4. **参数验证**：在构造方法中验证参数类型和值

### 最佳实践
1. **参数验证**：始终验证构造参数的有效性
2. **文档说明**：为构造方法编写清晰的文档字符串
3. **异常处理**：对无效参数抛出适当的异常
4. **继承调用**：在子类中正确调用父类构造方法
5. **属性初始化**：确保所有必要的属性都被初始化

### 注意事项
1. 构造方法不能有返回值（除了None）
2. 避免在构造方法中进行复杂的计算
3. 谨慎使用可变对象作为默认参数
4. 确保异常安全，避免部分初始化的对象

## 练习建议

1. **基础练习**：创建一个 `Rectangle` 类，在构造方法中验证长宽参数

2. **进阶练习**：设计一个 `DatabaseConnection` 类，支持多种连接方式的构造方法

3. **高级练习**：实现一个配置管理系统，支持从文件、环境变量等多种方式创建配置对象

## 下一步学习

掌握了构造方法后，接下来学习：
- [私有属性和访问控制](./06_private_attributes.md)
- [类属性和类方法](./07_class_attributes.md)
- [综合练习](./08_exercises.md)