#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
访问控制：公有、私有、保护属性

Python中的访问控制通过命名约定来实现：
1. 公有属性/方法：正常命名，如 name
2. 保护属性/方法：单下划线开头，如 _name（约定为内部使用）
3. 私有属性/方法：双下划线开头，如 __name（名称修饰）

注意：Python没有真正的私有属性，这些都是约定和机制来实现访问控制。
"""

# 示例1：演示不同访问级别的属性
class Student:
    """学生类 - 演示不同的访问控制级别"""
    
    def __init__(self, name, age, student_id):
        # 公有属性 - 可以自由访问
        self.name = name
        self.age = age
        
        # 保护属性 - 约定为内部使用，但仍可访问
        self._student_id = student_id
        self._grade = "未设置"
        
        # 私有属性 - 通过名称修饰隐藏
        self.__password = "default123"
        self.__secret_score = 0
    
    # 公有方法
    def introduce(self):
        """公有方法：自我介绍"""
        return f"我是{self.name}，今年{self.age}岁"
    
    def get_basic_info(self):
        """公有方法：获取基本信息"""
        return {
            'name': self.name,
            'age': self.age,
            'student_id': self._student_id
        }
    
    # 保护方法 - 约定为内部使用
    def _calculate_gpa(self, scores):
        """保护方法：计算GPA（内部使用）"""
        if not scores:
            return 0.0
        return sum(scores) / len(scores)
    
    def _update_grade(self, new_grade):
        """保护方法：更新年级"""
        self._grade = new_grade
        print(f"年级已更新为: {self._grade}")
    
    # 私有方法 - 通过名称修饰隐藏
    def __validate_password(self, password):
        """私有方法：验证密码"""
        return self.__password == password
    
    def __encrypt_score(self, score):
        """私有方法：加密分数"""
        return score * 7 + 13  # 简单的加密算法
    
    def __decrypt_score(self, encrypted_score):
        """私有方法：解密分数"""
        return (encrypted_score - 13) // 7
    
    # 公有方法调用私有方法
    def set_secret_score(self, score, password):
        """设置秘密分数（需要密码）"""
        if self.__validate_password(password):
            self.__secret_score = self.__encrypt_score(score)
            print(f"秘密分数设置成功")
            return True
        else:
            print("密码错误！")
            return False
    
    def get_secret_score(self, password):
        """获取秘密分数（需要密码）"""
        if self.__validate_password(password):
            return self.__decrypt_score(self.__secret_score)
        else:
            print("密码错误！")
            return None
    
    def change_password(self, old_password, new_password):
        """修改密码"""
        if self.__validate_password(old_password):
            self.__password = new_password
            print("密码修改成功")
            return True
        else:
            print("原密码错误！")
            return False


# 示例2：继承中的访问控制
class Person:
    """人员基类"""
    
    def __init__(self, name, age):
        self.name = name  # 公有属性
        self._age = age   # 保护属性
        self.__id = id(self)  # 私有属性
    
    def get_info(self):
        """公有方法"""
        return f"姓名: {self.name}, 年龄: {self._age}"
    
    def _get_age_category(self):
        """保护方法：获取年龄分类"""
        if self._age < 18:
            return "未成年"
        elif self._age < 60:
            return "成年人"
        else:
            return "老年人"
    
    def __generate_secret_code(self):
        """私有方法：生成密码"""
        return f"SECRET_{self.__id}"


class Employee(Person):
    """员工类 - 继承自Person"""
    
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id  # 公有属性
        self._salary = salary           # 保护属性
        self.__bonus = 0                # 私有属性
    
    def get_employee_info(self):
        """获取员工信息"""
        # 可以访问父类的公有和保护成员
        basic_info = self.get_info()  # 公有方法
        age_category = self._get_age_category()  # 保护方法
        
        return f"{basic_info}, 员工ID: {self.employee_id}, 分类: {age_category}"
    
    def calculate_total_salary(self):
        """计算总薪资"""
        return self._salary + self.__bonus
    
    def set_bonus(self, bonus):
        """设置奖金"""
        if bonus >= 0:
            self.__bonus = bonus
            print(f"奖金设置为: {bonus}")
        else:
            print("奖金不能为负数")
    
    def try_access_parent_private(self):
        """尝试访问父类的私有成员"""
        try:
            # 这会失败，因为私有属性不能被子类访问
            code = self.__generate_secret_code()
            print(f"访问成功: {code}")
        except AttributeError as e:
            print(f"无法访问父类私有方法: {e}")


# 示例3：访问控制的实际应用
class BankAccount:
    """银行账户类 - 实际应用访问控制"""
    
    def __init__(self, account_holder, initial_balance=0):
        # 公有属性
        self.account_holder = account_holder
        self.account_type = "储蓄账户"
        
        # 保护属性 - 子类可以访问
        self._account_number = self._generate_account_number()
        self._creation_date = self._get_current_date()
        
        # 私有属性 - 严格保护
        self.__balance = max(0, initial_balance)
        self.__pin = "0000"  # 默认密码
        self.__transaction_count = 0
        self.__is_frozen = False
    
    def _generate_account_number(self):
        """保护方法：生成账户号"""
        import random
        return f"ACC{random.randint(100000, 999999)}"
    
    def _get_current_date(self):
        """保护方法：获取当前日期"""
        import datetime
        return datetime.date.today()
    
    def _log_transaction(self, transaction_type, amount):
        """保护方法：记录交易"""
        self.__transaction_count += 1
        print(f"交易记录 #{self.__transaction_count}: {transaction_type} {amount}")
    
    def __verify_pin(self, pin):
        """私有方法：验证密码"""
        return self.__pin == pin and not self.__is_frozen
    
    def __check_daily_limit(self, amount):
        """私有方法：检查每日限额"""
        daily_limit = 10000
        return amount <= daily_limit
    
    # 公有接口方法
    def get_account_info(self):
        """获取账户基本信息"""
        return {
            'holder': self.account_holder,
            'account_number': self._account_number,
            'account_type': self.account_type,
            'creation_date': self._creation_date,
            'status': '正常' if not self.__is_frozen else '冻结'
        }
    
    def check_balance(self, pin):
        """查询余额"""
        if self.__verify_pin(pin):
            return self.__balance
        else:
            print("密码错误或账户被冻结")
            return None
    
    def deposit(self, amount, pin):
        """存款"""
        if not self.__verify_pin(pin):
            print("密码错误或账户被冻结")
            return False
        
        if amount <= 0:
            print("存款金额必须大于0")
            return False
        
        self.__balance += amount
        self._log_transaction("存款", amount)
        print(f"存款成功，当前余额: {self.__balance}")
        return True
    
    def withdraw(self, amount, pin):
        """取款"""
        if not self.__verify_pin(pin):
            print("密码错误或账户被冻结")
            return False
        
        if amount <= 0:
            print("取款金额必须大于0")
            return False
        
        if not self.__check_daily_limit(amount):
            print("超过每日取款限额")
            return False
        
        if amount > self.__balance:
            print("余额不足")
            return False
        
        self.__balance -= amount
        self._log_transaction("取款", amount)
        print(f"取款成功，当前余额: {self.__balance}")
        return True
    
    def change_pin(self, old_pin, new_pin):
        """修改密码"""
        if self.__verify_pin(old_pin):
            if len(new_pin) == 4 and new_pin.isdigit():
                self.__pin = new_pin
                print("密码修改成功")
                return True
            else:
                print("新密码必须是4位数字")
                return False
        else:
            print("原密码错误")
            return False
    
    def freeze_account(self, admin_code):
        """冻结账户（管理员功能）"""
        if admin_code == "ADMIN123":
            self.__is_frozen = True
            print("账户已冻结")
            return True
        else:
            print("管理员代码错误")
            return False
    
    def unfreeze_account(self, admin_code):
        """解冻账户（管理员功能）"""
        if admin_code == "ADMIN123":
            self.__is_frozen = False
            print("账户已解冻")
            return True
        else:
            print("管理员代码错误")
            return False


def demonstrate_access_control():
    """演示访问控制"""
    print("=" * 60)
    print("访问控制演示")
    print("=" * 60)
    
    # 创建学生对象
    student = Student("张三", 20, "2021001")
    
    print("\n1. 公有属性访问：")
    print(f"姓名: {student.name}")
    print(f"年龄: {student.age}")
    print(f"自我介绍: {student.introduce()}")
    
    print("\n2. 保护属性访问：")
    print(f"学号: {student._student_id}")  # 可以访问，但不推荐
    print(f"年级: {student._grade}")
    student._update_grade("大二")  # 可以调用，但不推荐
    
    print("\n3. 私有属性访问：")
    # 直接访问会失败
    try:
        print(student.__password)
    except AttributeError:
        print("无法直接访问私有属性 __password")
    
    # 通过公有方法访问
    student.set_secret_score(95, "default123")
    score = student.get_secret_score("default123")
    print(f"秘密分数: {score}")
    
    # 修改密码
    student.change_password("default123", "new456")
    score = student.get_secret_score("new456")
    print(f"用新密码获取分数: {score}")


def demonstrate_inheritance_access():
    """演示继承中的访问控制"""
    print("\n" + "=" * 60)
    print("继承中的访问控制")
    print("=" * 60)
    
    # 创建员工对象
    employee = Employee("李四", 30, "EMP001", 8000)
    
    print("\n1. 子类访问父类成员：")
    print(employee.get_employee_info())
    
    print("\n2. 子类无法访问父类私有成员：")
    employee.try_access_parent_private()
    
    print("\n3. 子类自己的私有成员：")
    employee.set_bonus(2000)
    total = employee.calculate_total_salary()
    print(f"总薪资: {total}")


def demonstrate_practical_example():
    """演示实际应用示例"""
    print("\n" + "=" * 60)
    print("实际应用示例 - 银行账户")
    print("=" * 60)
    
    # 创建银行账户
    account = BankAccount("王五", 5000)
    
    print("\n1. 账户信息：")
    info = account.get_account_info()
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    print("\n2. 正常操作：")
    balance = account.check_balance("0000")
    print(f"当前余额: {balance}")
    
    account.deposit(1000, "0000")
    account.withdraw(500, "0000")
    
    print("\n3. 错误操作：")
    account.check_balance("1111")  # 错误密码
    account.withdraw(20000, "0000")  # 超过限额
    
    print("\n4. 管理员操作：")
    account.freeze_account("ADMIN123")
    account.check_balance("0000")  # 账户被冻结
    account.unfreeze_account("ADMIN123")
    
    print("\n5. 尝试直接访问私有属性：")
    try:
        print(f"余额: {account.__balance}")
    except AttributeError:
        print("无法直接访问私有属性 __balance")
    
    # 通过名称修饰可以访问（不推荐）
    print(f"通过名称修饰访问余额: {account._BankAccount__balance}")
    print("注意：这破坏了封装性，实际开发中不应该这样做！")


def access_control_summary():
    """访问控制总结"""
    print("\n" + "=" * 60)
    print("访问控制总结")
    print("=" * 60)
    
    summary = {
        "公有属性/方法": {
            "命名": "正常命名，如 name",
            "访问性": "任何地方都可以访问",
            "用途": "对外提供的接口",
            "示例": "self.name = name"
        },
        "保护属性/方法": {
            "命名": "单下划线开头，如 _name",
            "访问性": "约定为内部使用，但仍可访问",
            "用途": "类内部和子类使用",
            "示例": "self._internal_value = value"
        },
        "私有属性/方法": {
            "命名": "双下划线开头，如 __name",
            "访问性": "通过名称修饰隐藏，外部难以访问",
            "用途": "严格的内部实现",
            "示例": "self.__secret = secret"
        }
    }
    
    for access_type, details in summary.items():
        print(f"\n{access_type}:")
        for key, value in details.items():
            print(f"  {key}: {value}")
    
    print("\n重要提醒:")
    print("1. Python的访问控制主要基于约定")
    print("2. 没有真正的私有属性，都可以通过特殊方式访问")
    print("3. 遵循约定是良好编程习惯的体现")
    print("4. 合理使用访问控制可以提高代码质量")


if __name__ == "__main__":
    # 运行所有演示
    demonstrate_access_control()
    demonstrate_inheritance_access()
    demonstrate_practical_example()
    access_control_summary()