"""主模块 - 演示不同的导入方式"""

# 绝对导入示例
from import_demo.utils import helper
from import_demo.core.engine import Engine

def main():
    """主函数"""
    print("主模块运行中...")
    helper.show_info()
    engine = Engine()
    engine.start()

if __name__ == "__main__":
    main()
