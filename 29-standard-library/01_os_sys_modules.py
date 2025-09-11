#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_os_sys_modules.py - os和sys模块的使用

本文件演示Python标准库中os和sys模块的常用功能：
- os模块：操作系统接口，文件和目录操作
- sys模块：系统相关的参数和函数

学习目标：
1. 掌握os模块的基本用法
2. 理解sys模块的核心功能
3. 学会处理路径和环境变量
4. 了解系统信息获取方法
"""

import os
import sys
import platform
from pathlib import Path


def demonstrate_os_module():
    """演示os模块的基本功能"""
    print("=" * 50)
    print("OS模块功能演示")
    print("=" * 50)
    
    # 1. 获取当前工作目录
    current_dir = os.getcwd()
    print(f"当前工作目录: {current_dir}")
    
    # 2. 列出目录内容
    print(f"\n当前目录内容:")
    try:
        files = os.listdir('.')
        for i, file in enumerate(files[:5], 1):  # 只显示前5个文件
            print(f"  {i}. {file}")
        if len(files) > 5:
            print(f"  ... 还有 {len(files) - 5} 个文件")
    except PermissionError:
        print("  权限不足，无法列出目录内容")
    
    # 3. 环境变量操作
    print(f"\n环境变量示例:")
    print(f"PATH变量长度: {len(os.environ.get('PATH', ''))} 字符")
    print(f"HOME目录: {os.environ.get('HOME', '未设置')}")
    print(f"用户名: {os.environ.get('USER', os.environ.get('USERNAME', '未知'))}")
    
    # 4. 路径操作
    print(f"\n路径操作示例:")
    sample_path = "/home/user/documents/file.txt"
    print(f"示例路径: {sample_path}")
    print(f"目录名: {os.path.dirname(sample_path)}")
    print(f"文件名: {os.path.basename(sample_path)}")
    print(f"文件名(无扩展名): {os.path.splitext(sample_path)[0]}")
    print(f"扩展名: {os.path.splitext(sample_path)[1]}")
    
    # 5. 路径拼接
    joined_path = os.path.join("home", "user", "documents", "file.txt")
    print(f"路径拼接结果: {joined_path}")
    
    # 6. 文件和目录检查
    print(f"\n文件系统检查:")
    print(f"当前目录是否存在: {os.path.exists('.')}")
    print(f"当前目录是否为目录: {os.path.isdir('.')}")
    print(f"README.md是否存在: {os.path.exists('README.md')}")
    if os.path.exists('README.md'):
        print(f"README.md是否为文件: {os.path.isfile('README.md')}")
        stat_info = os.stat('README.md')
        print(f"README.md文件大小: {stat_info.st_size} 字节")


def demonstrate_sys_module():
    """演示sys模块的基本功能"""
    print("\n" + "=" * 50)
    print("SYS模块功能演示")
    print("=" * 50)
    
    # 1. Python版本信息
    print(f"Python版本: {sys.version}")
    print(f"Python版本信息: {sys.version_info}")
    print(f"Python可执行文件路径: {sys.executable}")
    
    # 2. 平台信息
    print(f"\n平台信息:")
    print(f"操作系统: {sys.platform}")
    print(f"字节序: {sys.byteorder}")
    print(f"默认编码: {sys.getdefaultencoding()}")
    
    # 3. 模块搜索路径
    print(f"\n模块搜索路径 (前5个):")
    for i, path in enumerate(sys.path[:5], 1):
        print(f"  {i}. {path}")
    if len(sys.path) > 5:
        print(f"  ... 还有 {len(sys.path) - 5} 个路径")
    
    # 4. 命令行参数
    print(f"\n命令行参数:")
    print(f"脚本名称: {sys.argv[0] if sys.argv else '无'}")
    print(f"参数个数: {len(sys.argv)}")
    if len(sys.argv) > 1:
        print(f"其他参数: {sys.argv[1:]}")
    else:
        print("没有额外的命令行参数")
    
    # 5. 内存和性能信息
    print(f"\n系统信息:")
    print(f"最大整数值: {sys.maxsize}")
    print(f"递归限制: {sys.getrecursionlimit()}")
    
    # 6. 标准输入输出
    print(f"\n标准流信息:")
    print(f"标准输入: {sys.stdin.name}")
    print(f"标准输出: {sys.stdout.name}")
    print(f"标准错误: {sys.stderr.name}")


def demonstrate_platform_info():
    """演示平台相关信息获取"""
    print("\n" + "=" * 50)
    print("平台信息详细演示")
    print("=" * 50)
    
    print(f"系统名称: {platform.system()}")
    print(f"系统版本: {platform.release()}")
    print(f"系统详细版本: {platform.version()}")
    print(f"机器类型: {platform.machine()}")
    print(f"处理器信息: {platform.processor()}")
    print(f"架构信息: {platform.architecture()}")
    print(f"完整平台信息: {platform.platform()}")
    
    # 网络主机名
    print(f"主机名: {platform.node()}")
    
    # Python实现信息
    print(f"\nPython实现信息:")
    print(f"Python实现: {platform.python_implementation()}")
    print(f"Python版本: {platform.python_version()}")
    print(f"Python编译器: {platform.python_compiler()}")


def demonstrate_environment_operations():
    """演示环境变量操作"""
    print("\n" + "=" * 50)
    print("环境变量操作演示")
    print("=" * 50)
    
    # 1. 设置和获取环境变量
    test_var = "PYTHON_DEMO_VAR"
    test_value = "Hello, Python Standard Library!"
    
    print(f"设置环境变量: {test_var} = {test_value}")
    os.environ[test_var] = test_value
    
    # 获取环境变量
    retrieved_value = os.environ.get(test_var)
    print(f"获取环境变量: {test_var} = {retrieved_value}")
    
    # 2. 使用默认值
    non_existent = os.environ.get("NON_EXISTENT_VAR", "默认值")
    print(f"不存在的环境变量(使用默认值): {non_existent}")
    
    # 3. 检查环境变量是否存在
    if test_var in os.environ:
        print(f"环境变量 {test_var} 存在")
    
    # 4. 删除环境变量
    if test_var in os.environ:
        del os.environ[test_var]
        print(f"已删除环境变量: {test_var}")
    
    # 5. 常用环境变量
    print(f"\n常用环境变量:")
    common_vars = ['PATH', 'HOME', 'USER', 'SHELL', 'LANG']
    for var in common_vars:
        value = os.environ.get(var, '未设置')
        if len(value) > 50:
            value = value[:47] + "..."
        print(f"  {var}: {value}")


def demonstrate_file_operations():
    """演示文件操作相关功能"""
    print("\n" + "=" * 50)
    print("文件操作演示")
    print("=" * 50)
    
    # 1. 创建临时文件进行演示
    demo_file = "demo_file.txt"
    demo_dir = "demo_directory"
    
    try:
        # 创建演示文件
        with open(demo_file, 'w', encoding='utf-8') as f:
            f.write("这是一个演示文件\n")
            f.write("用于展示os模块的文件操作功能\n")
        
        print(f"创建演示文件: {demo_file}")
        
        # 文件信息
        stat_info = os.stat(demo_file)
        print(f"文件大小: {stat_info.st_size} 字节")
        print(f"文件权限: {oct(stat_info.st_mode)}")
        
        # 创建目录
        if not os.path.exists(demo_dir):
            os.mkdir(demo_dir)
            print(f"创建演示目录: {demo_dir}")
        
        # 重命名文件
        new_name = "renamed_demo.txt"
        os.rename(demo_file, new_name)
        print(f"文件重命名: {demo_file} -> {new_name}")
        
        # 移动文件到目录
        moved_path = os.path.join(demo_dir, new_name)
        os.rename(new_name, moved_path)
        print(f"文件移动到: {moved_path}")
        
        # 列出目录内容
        print(f"\n目录 {demo_dir} 的内容:")
        for item in os.listdir(demo_dir):
            item_path = os.path.join(demo_dir, item)
            if os.path.isfile(item_path):
                print(f"  文件: {item}")
            elif os.path.isdir(item_path):
                print(f"  目录: {item}")
        
    except Exception as e:
        print(f"文件操作出错: {e}")
    
    finally:
        # 清理演示文件和目录
        try:
            if os.path.exists(moved_path):
                os.remove(moved_path)
                print(f"\n清理文件: {moved_path}")
            if os.path.exists(demo_dir):
                os.rmdir(demo_dir)
                print(f"清理目录: {demo_dir}")
        except Exception as e:
            print(f"清理时出错: {e}")


def main():
    """主函数 - 运行所有演示"""
    print("Python标准库 - os和sys模块学习")
    print("本程序演示os和sys模块的常用功能")
    
    try:
        demonstrate_os_module()
        demonstrate_sys_module()
        demonstrate_platform_info()
        demonstrate_environment_operations()
        demonstrate_file_operations()
        
        print("\n" + "=" * 50)
        print("学习要点总结:")
        print("=" * 50)
        print("1. os模块主要用于操作系统接口操作")
        print("2. sys模块提供Python解释器相关信息")
        print("3. 环境变量可以通过os.environ访问和修改")
        print("4. 路径操作使用os.path模块更安全")
        print("5. platform模块提供详细的平台信息")
        print("6. 文件操作要注意异常处理和资源清理")
        
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"\n程序执行出错: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()