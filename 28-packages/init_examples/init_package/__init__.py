
# 带初始化代码的__init__.py
print("正在初始化init_package包")

# 包级别的变量
PACKAGE_NAME = "init_package"
VERSION = "2.0.0"

# 包级别的函数
def get_package_info():
    return f"{PACKAGE_NAME} v{VERSION}"

# 初始化时执行的代码
print(f"包信息: {get_package_info()}")
