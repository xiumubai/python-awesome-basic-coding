#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python文件操作 - 文件路径操作

本模块演示文件路径的各种操作：
1. os.path模块的使用
2. pathlib模块的现代化路径操作
3. 路径的构建和解析
4. 文件和目录的信息获取
5. 路径的规范化和转换
6. 跨平台路径处理
7. 文件系统遍历

作者：Python学习助手
日期：2024年
"""

import os
import sys
import glob
import time
from pathlib import Path
from typing import List, Tuple, Generator


def demonstrate_os_path():
    """演示os.path模块的使用"""
    print("\n=== os.path模块使用 ===")
    
    # 1. 路径构建和分解
    print("\n1. 路径构建和分解：")
    
    # 当前文件的路径信息
    current_file = __file__
    print(f"当前文件：{current_file}")
    
    # 路径分解
    dirname = os.path.dirname(current_file)
    basename = os.path.basename(current_file)
    name, ext = os.path.splitext(basename)
    
    print(f"目录名：{dirname}")
    print(f"文件名：{basename}")
    print(f"文件名（无扩展名）：{name}")
    print(f"扩展名：{ext}")
    
    # 路径构建
    new_path = os.path.join(dirname, 'test_folder', 'test_file.txt')
    print(f"构建的路径：{new_path}")
    
    # 2. 路径判断
    print("\n2. 路径判断：")
    
    test_paths = [
        current_file,
        dirname,
        '/nonexistent/path',
        '.',
        '..'
    ]
    
    for path in test_paths:
        print(f"\n路径：{path}")
        print(f"  存在：{os.path.exists(path)}")
        print(f"  是文件：{os.path.isfile(path)}")
        print(f"  是目录：{os.path.isdir(path)}")
        print(f"  是绝对路径：{os.path.isabs(path)}")
        if os.path.exists(path):
            print(f"  是链接：{os.path.islink(path)}")
    
    # 3. 路径规范化
    print("\n3. 路径规范化：")
    
    messy_paths = [
        './test/../test/file.txt',
        '/home/user//documents/./file.txt',
        '~/documents/file.txt'
    ]
    
    for path in messy_paths:
        normalized = os.path.normpath(path)
        expanded = os.path.expanduser(path)
        absolute = os.path.abspath(path)
        
        print(f"\n原始路径：{path}")
        print(f"规范化：{normalized}")
        print(f"展开用户目录：{expanded}")
        print(f"绝对路径：{absolute}")
    
    # 4. 路径比较
    print("\n4. 路径比较：")
    
    path1 = os.path.abspath('.')
    path2 = os.getcwd()
    print(f"路径1：{path1}")
    print(f"路径2：{path2}")
    print(f"相同：{os.path.samefile(path1, path2) if os.path.exists(path1) and os.path.exists(path2) else '无法比较'}")
    
    # 5. 相对路径计算
    print("\n5. 相对路径计算：")
    
    start_path = os.path.dirname(current_file)
    target_path = os.path.join(start_path, '..', 'other_module')
    
    try:
        relative_path = os.path.relpath(target_path, start_path)
        print(f"从 {start_path}")
        print(f"到 {target_path}")
        print(f"相对路径：{relative_path}")
    except ValueError as e:
        print(f"无法计算相对路径：{e}")


def demonstrate_pathlib():
    """演示pathlib模块的现代化路径操作"""
    print("\n=== pathlib模块使用 ===")
    
    # 1. Path对象的创建和基本操作
    print("\n1. Path对象的基本操作：")
    
    # 创建Path对象
    current_file = Path(__file__)
    print(f"当前文件：{current_file}")
    
    # 路径属性
    print(f"父目录：{current_file.parent}")
    print(f"文件名：{current_file.name}")
    print(f"文件名（无扩展名）：{current_file.stem}")
    print(f"扩展名：{current_file.suffix}")
    print(f"所有扩展名：{current_file.suffixes}")
    print(f"绝对路径：{current_file.absolute()}")
    
    # 2. 路径构建
    print("\n2. 路径构建：")
    
    # 使用 / 操作符构建路径
    base_dir = Path.cwd()
    test_file = base_dir / 'test_folder' / 'test_file.txt'
    print(f"基础目录：{base_dir}")
    print(f"构建的路径：{test_file}")
    
    # 使用joinpath方法
    another_path = base_dir.joinpath('data', 'files', 'document.pdf')
    print(f"另一个路径：{another_path}")
    
    # 3. 路径判断和属性
    print("\n3. 路径判断和属性：")
    
    paths_to_check = [
        current_file,
        current_file.parent,
        Path('/nonexistent/path'),
        Path.home(),
        Path.cwd()
    ]
    
    for path in paths_to_check:
        print(f"\n路径：{path}")
        print(f"  存在：{path.exists()}")
        print(f"  是文件：{path.is_file()}")
        print(f"  是目录：{path.is_dir()}")
        print(f"  是绝对路径：{path.is_absolute()}")
        if path.exists():
            print(f"  是符号链接：{path.is_symlink()}")
    
    # 4. 文件信息获取
    print("\n4. 文件信息获取：")
    
    if current_file.exists():
        stat_info = current_file.stat()
        print(f"文件大小：{stat_info.st_size} 字节")
        print(f"修改时间：{time.ctime(stat_info.st_mtime)}")
        print(f"创建时间：{time.ctime(stat_info.st_ctime)}")
        print(f"访问时间：{time.ctime(stat_info.st_atime)}")
        print(f"文件权限：{oct(stat_info.st_mode)}")
    
    # 5. 路径操作
    print("\n5. 路径操作：")
    
    # 创建测试目录结构
    test_dir = Path('test_pathlib')
    test_dir.mkdir(exist_ok=True)
    
    # 创建子目录
    sub_dir = test_dir / 'subdirectory'
    sub_dir.mkdir(exist_ok=True)
    
    # 创建测试文件
    test_file = test_dir / 'test.txt'
    test_file.write_text('Hello, pathlib!', encoding='utf-8')
    
    print(f"创建了目录：{test_dir}")
    print(f"创建了子目录：{sub_dir}")
    print(f"创建了文件：{test_file}")
    print(f"文件内容：{test_file.read_text(encoding='utf-8')}")
    
    # 6. 路径遍历
    print("\n6. 路径遍历：")
    
    print("当前目录下的所有项目：")
    for item in Path('.').iterdir():
        item_type = "目录" if item.is_dir() else "文件"
        print(f"  {item_type}: {item.name}")
    
    # 递归查找Python文件
    print("\n当前目录及子目录中的Python文件：")
    for py_file in Path('.').rglob('*.py'):
        print(f"  {py_file}")
    
    # 清理测试文件
    if test_file.exists():
        test_file.unlink()
    if sub_dir.exists():
        sub_dir.rmdir()
    if test_dir.exists():
        test_dir.rmdir()


def demonstrate_file_info():
    """演示文件和目录信息获取"""
    print("\n=== 文件和目录信息获取 ===")
    
    # 1. 文件统计信息
    print("\n1. 文件统计信息：")
    
    current_file = Path(__file__)
    if current_file.exists():
        stat_info = current_file.stat()
        
        print(f"文件：{current_file.name}")
        print(f"大小：{stat_info.st_size:,} 字节")
        print(f"大小：{stat_info.st_size / 1024:.2f} KB")
        print(f"修改时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat_info.st_mtime))}")
        print(f"访问时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat_info.st_atime))}")
        print(f"创建时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat_info.st_ctime))}")
        print(f"inode：{stat_info.st_ino}")
        print(f"设备：{stat_info.st_dev}")
        print(f"硬链接数：{stat_info.st_nlink}")
        print(f"用户ID：{stat_info.st_uid}")
        print(f"组ID：{stat_info.st_gid}")
        print(f"权限模式：{oct(stat_info.st_mode)}")
    
    # 2. 目录信息
    print("\n2. 目录信息：")
    
    current_dir = Path('.')
    print(f"当前目录：{current_dir.absolute()}")
    
    # 统计目录内容
    files_count = 0
    dirs_count = 0
    total_size = 0
    
    for item in current_dir.iterdir():
        if item.is_file():
            files_count += 1
            total_size += item.stat().st_size
        elif item.is_dir():
            dirs_count += 1
    
    print(f"文件数量：{files_count}")
    print(f"目录数量：{dirs_count}")
    print(f"总大小：{total_size:,} 字节 ({total_size / 1024:.2f} KB)")
    
    # 3. 磁盘使用情况（仅在支持的系统上）
    print("\n3. 磁盘使用情况：")
    
    try:
        if hasattr(os, 'statvfs'):  # Unix系统
            statvfs = os.statvfs('.')
            total_space = statvfs.f_frsize * statvfs.f_blocks
            free_space = statvfs.f_frsize * statvfs.f_available
            used_space = total_space - free_space
            
            print(f"总空间：{total_space / (1024**3):.2f} GB")
            print(f"已用空间：{used_space / (1024**3):.2f} GB")
            print(f"可用空间：{free_space / (1024**3):.2f} GB")
            print(f"使用率：{(used_space / total_space) * 100:.1f}%")
        else:
            print("当前系统不支持磁盘使用情况查询")
    except Exception as e:
        print(f"获取磁盘信息时出错：{e}")


def demonstrate_glob_patterns():
    """演示glob模式匹配"""
    print("\n=== glob模式匹配 ===")
    
    # 1. 基本glob模式
    print("\n1. 基本glob模式：")
    
    patterns = [
        '*.py',      # 所有Python文件
        '0*.py',     # 以0开头的Python文件
        '??_*.py',   # 两个字符开头，下划线，然后任意字符的Python文件
        '*[0-9]*.py' # 包含数字的Python文件
    ]
    
    for pattern in patterns:
        matches = glob.glob(pattern)
        print(f"\n模式 '{pattern}' 匹配的文件：")
        for match in matches:
            print(f"  {match}")
        if not matches:
            print("  无匹配文件")
    
    # 2. 递归glob
    print("\n2. 递归glob：")
    
    recursive_patterns = [
        '**/*.py',   # 递归查找所有Python文件
        '**/test*',  # 递归查找以test开头的文件或目录
    ]
    
    for pattern in recursive_patterns:
        matches = glob.glob(pattern, recursive=True)
        print(f"\n递归模式 '{pattern}' 匹配的文件：")
        for match in matches[:5]:  # 只显示前5个
            print(f"  {match}")
        if len(matches) > 5:
            print(f"  ... 还有 {len(matches) - 5} 个文件")
        if not matches:
            print("  无匹配文件")
    
    # 3. pathlib的glob
    print("\n3. pathlib的glob：")
    
    current_dir = Path('.')
    
    # 使用pathlib的glob方法
    py_files = list(current_dir.glob('*.py'))
    print(f"\n当前目录的Python文件（pathlib）：")
    for py_file in py_files:
        print(f"  {py_file.name} ({py_file.stat().st_size} 字节)")
    
    # 递归glob
    all_py_files = list(current_dir.rglob('*.py'))
    print(f"\n递归查找的Python文件数量：{len(all_py_files)}")


def demonstrate_path_utilities():
    """演示路径实用工具函数"""
    print("\n=== 路径实用工具 ===")
    
    # 1. 路径清理和规范化
    print("\n1. 路径清理和规范化：")
    
    def clean_path(path_str: str) -> str:
        """清理和规范化路径"""
        path = Path(path_str)
        # 展开用户目录
        path = path.expanduser()
        # 解析符号链接
        try:
            path = path.resolve()
        except (OSError, RuntimeError):
            # 如果路径不存在或有循环链接，使用绝对路径
            path = path.absolute()
        return str(path)
    
    messy_paths = [
        '~/documents/../documents/file.txt',
        './test//file.txt',
        '../17-file-operations/./08_path_operations.py'
    ]
    
    for messy_path in messy_paths:
        clean = clean_path(messy_path)
        print(f"原始：{messy_path}")
        print(f"清理：{clean}")
        print()
    
    # 2. 路径安全检查
    print("\n2. 路径安全检查：")
    
    def is_safe_path(base_path: str, target_path: str) -> bool:
        """检查目标路径是否在基础路径内（防止路径遍历攻击）"""
        base = Path(base_path).resolve()
        target = Path(target_path).resolve()
        
        try:
            target.relative_to(base)
            return True
        except ValueError:
            return False
    
    base_directory = str(Path.cwd())
    test_paths = [
        'safe_file.txt',
        'subdir/safe_file.txt',
        '../dangerous_file.txt',
        '/etc/passwd'
    ]
    
    print(f"基础目录：{base_directory}")
    for test_path in test_paths:
        safe = is_safe_path(base_directory, test_path)
        status = "安全" if safe else "危险"
        print(f"  {test_path}: {status}")
    
    # 3. 文件类型判断
    print("\n3. 文件类型判断：")
    
    def get_file_type(file_path: str) -> str:
        """根据扩展名判断文件类型"""
        path = Path(file_path)
        suffix = path.suffix.lower()
        
        type_mapping = {
            '.py': 'Python源代码',
            '.txt': '文本文件',
            '.md': 'Markdown文档',
            '.json': 'JSON数据',
            '.xml': 'XML文档',
            '.html': 'HTML文档',
            '.css': 'CSS样式表',
            '.js': 'JavaScript代码',
            '.jpg': 'JPEG图像',
            '.png': 'PNG图像',
            '.pdf': 'PDF文档',
            '.zip': 'ZIP压缩包',
            '.tar': 'TAR归档',
            '.gz': 'GZIP压缩文件'
        }
        
        return type_mapping.get(suffix, f'未知类型 ({suffix})')
    
    # 获取当前目录的文件并分类
    file_types = {}
    for file_path in Path('.').glob('*'):
        if file_path.is_file():
            file_type = get_file_type(str(file_path))
            if file_type not in file_types:
                file_types[file_type] = []
            file_types[file_type].append(file_path.name)
    
    print("当前目录文件分类：")
    for file_type, files in file_types.items():
        print(f"  {file_type}: {len(files)} 个文件")
        for file_name in files[:3]:  # 只显示前3个
            print(f"    - {file_name}")
        if len(files) > 3:
            print(f"    ... 还有 {len(files) - 3} 个文件")


def demonstrate_cross_platform():
    """演示跨平台路径处理"""
    print("\n=== 跨平台路径处理 ===")
    
    # 1. 系统信息
    print("\n1. 系统信息：")
    print(f"操作系统：{os.name}")
    print(f"平台：{sys.platform}")
    print(f"路径分隔符：'{os.sep}'")
    print(f"路径列表分隔符：'{os.pathsep}'")
    print(f"行结束符：{repr(os.linesep)}")
    
    # 2. 路径分隔符处理
    print("\n2. 路径分隔符处理：")
    
    # 错误的硬编码路径
    wrong_paths = [
        'folder\\subfolder\\file.txt',  # Windows风格
        'folder/subfolder/file.txt',     # Unix风格
    ]
    
    print("硬编码路径的问题：")
    for wrong_path in wrong_paths:
        print(f"  原始：{wrong_path}")
        print(f"  规范化：{os.path.normpath(wrong_path)}")
    
    # 正确的跨平台路径构建
    print("\n正确的跨平台路径构建：")
    correct_path = os.path.join('folder', 'subfolder', 'file.txt')
    pathlib_path = Path('folder') / 'subfolder' / 'file.txt'
    
    print(f"os.path.join：{correct_path}")
    print(f"pathlib：{pathlib_path}")
    
    # 3. 特殊目录获取
    print("\n3. 特殊目录获取：")
    
    special_dirs = {
        '当前工作目录': os.getcwd(),
        '用户主目录': str(Path.home()),
        '临时目录': os.path.expandvars('$TMPDIR') if os.name != 'nt' else os.path.expandvars('%TEMP%'),
    }
    
    for name, path in special_dirs.items():
        print(f"  {name}：{path}")
    
    # 4. 环境变量中的路径
    print("\n4. 环境变量中的路径：")
    
    path_env = os.environ.get('PATH', '')
    if path_env:
        paths = path_env.split(os.pathsep)
        print(f"PATH环境变量包含 {len(paths)} 个路径：")
        for i, path in enumerate(paths[:5]):
            print(f"  {i+1}. {path}")
        if len(paths) > 5:
            print(f"  ... 还有 {len(paths) - 5} 个路径")


def demonstrate_directory_tree():
    """演示目录树遍历和显示"""
    print("\n=== 目录树遍历 ===")
    
    def print_directory_tree(directory: str, max_depth: int = 2, current_depth: int = 0):
        """打印目录树结构"""
        if current_depth > max_depth:
            return
        
        path = Path(directory)
        if not path.exists() or not path.is_dir():
            return
        
        # 获取目录内容并排序
        try:
            items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        except PermissionError:
            print(f"{'  ' * current_depth}[权限拒绝]")
            return
        
        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            prefix = '  ' * current_depth
            
            if current_depth > 0:
                prefix += '└── ' if is_last else '├── '
            
            if item.is_dir():
                print(f"{prefix}{item.name}/")
                if current_depth < max_depth:
                    print_directory_tree(str(item), max_depth, current_depth + 1)
            else:
                size = item.stat().st_size if item.exists() else 0
                size_str = f" ({size:,} bytes)" if size < 1024 else f" ({size/1024:.1f} KB)"
                print(f"{prefix}{item.name}{size_str}")
    
    print("\n当前目录结构：")
    print_directory_tree('.', max_depth=1)
    
    # 统计目录信息
    def analyze_directory(directory: str) -> dict:
        """分析目录的统计信息"""
        path = Path(directory)
        stats = {
            'total_files': 0,
            'total_dirs': 0,
            'total_size': 0,
            'file_types': {},
            'largest_file': None,
            'largest_size': 0
        }
        
        try:
            for item in path.rglob('*'):
                if item.is_file():
                    stats['total_files'] += 1
                    size = item.stat().st_size
                    stats['total_size'] += size
                    
                    # 记录最大文件
                    if size > stats['largest_size']:
                        stats['largest_size'] = size
                        stats['largest_file'] = str(item)
                    
                    # 统计文件类型
                    suffix = item.suffix.lower() or '无扩展名'
                    stats['file_types'][suffix] = stats['file_types'].get(suffix, 0) + 1
                    
                elif item.is_dir():
                    stats['total_dirs'] += 1
        except PermissionError:
            pass
        
        return stats
    
    print("\n目录统计信息：")
    stats = analyze_directory('.')
    print(f"文件总数：{stats['total_files']}")
    print(f"目录总数：{stats['total_dirs']}")
    print(f"总大小：{stats['total_size']:,} 字节 ({stats['total_size']/1024:.2f} KB)")
    
    if stats['largest_file']:
        print(f"最大文件：{stats['largest_file']} ({stats['largest_size']:,} 字节)")
    
    if stats['file_types']:
        print("\n文件类型分布：")
        sorted_types = sorted(stats['file_types'].items(), key=lambda x: x[1], reverse=True)
        for file_type, count in sorted_types:
            print(f"  {file_type}: {count} 个文件")


def main():
    """主函数"""
    print("Python文件操作 - 文件路径操作")
    print("=" * 50)
    
    try:
        # 演示各种路径操作
        demonstrate_os_path()
        demonstrate_pathlib()
        demonstrate_file_info()
        demonstrate_glob_patterns()
        demonstrate_path_utilities()
        demonstrate_cross_platform()
        demonstrate_directory_tree()
        
    except Exception as e:
        print(f"\n演示过程中出现错误：{e}")
        import traceback
        traceback.print_exc()
    
    # 学习总结
    print("\n" + "=" * 50)
    print("=== 学习总结 ===")
    print("""
文件路径操作核心概念：
1. 路径表示：绝对路径vs相对路径
2. 路径分隔符：跨平台兼容性
3. 路径组件：目录名、文件名、扩展名
4. 路径规范化：清理和标准化路径

os.path模块（传统方式）：
- os.path.join()：跨平台路径构建
- os.path.dirname()、os.path.basename()：路径分解
- os.path.exists()、os.path.isfile()：路径判断
- os.path.abspath()、os.path.relpath()：路径转换
- os.path.normpath()：路径规范化

pathlib模块（现代方式）：
- Path对象：面向对象的路径操作
- / 操作符：直观的路径构建
- .parent、.name、.suffix：路径属性
- .exists()、.is_file()、.is_dir()：路径判断
- .iterdir()、.glob()、.rglob()：目录遍历
- .stat()：文件信息获取

glob模式匹配：
- * 匹配任意字符
- ? 匹配单个字符
- [] 匹配字符集合
- ** 递归匹配（需要recursive=True）

跨平台注意事项：
- 使用os.path.join()或pathlib构建路径
- 避免硬编码路径分隔符
- 注意大小写敏感性差异
- 处理不同的文件系统限制

实际应用场景：
- 配置文件路径管理
- 日志文件组织
- 数据文件处理
- 备份和归档
- 文件系统监控
- 批量文件操作

最佳实践：
- 优先使用pathlib（Python 3.4+）
- 进行路径安全检查
- 处理权限和异常
- 使用适当的路径规范化
- 考虑性能和内存使用
- 编写跨平台兼容的代码
""")


if __name__ == "__main__":
    main()