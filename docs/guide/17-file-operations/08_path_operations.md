# 文件路径操作

## 学习目标

通过本节学习，你将掌握：
- os.path 模块的传统路径操作方法
- pathlib 模块的现代化路径操作
- 文件和目录信息的获取方法
- glob 模式匹配和文件查找
- 跨平台路径处理的最佳实践
- 目录树遍历和文件系统分析

## 核心概念

### 路径操作概述

文件路径操作是文件系统编程的基础，涉及路径的构建、解析、验证和转换。Python 提供了两套主要的路径操作工具：

- **os.path 模块**：传统的函数式接口
- **pathlib 模块**：现代的面向对象接口（推荐）

### 路径的基本概念

- **绝对路径**：从根目录开始的完整路径
- **相对路径**：相对于当前工作目录的路径
- **路径分隔符**：不同操作系统使用不同的分隔符（`/` 或 `\`）
- **路径组件**：目录名、文件名、扩展名等

## 代码示例

### 1. os.path 模块使用

```python
import os

def demonstrate_os_path():
    """演示os.path模块的使用"""
    print("=== os.path模块使用 ===")
    
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
```

### 2. 路径规范化和转换

```python
def demonstrate_path_normalization():
    """演示路径规范化"""
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
    
    # 相对路径计算
    print("\n5. 相对路径计算：")
    
    start_path = os.path.dirname(__file__)
    target_path = os.path.join(start_path, '..', 'other_module')
    
    try:
        relative_path = os.path.relpath(target_path, start_path)
        print(f"从 {start_path}")
        print(f"到 {target_path}")
        print(f"相对路径：{relative_path}")
    except ValueError as e:
        print(f"无法计算相对路径：{e}")
```

### 3. pathlib 模块使用

```python
from pathlib import Path
import time

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
```

### 4. 文件信息获取

```python
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
```

### 5. glob 模式匹配

```python
import glob

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
```

### 6. 路径实用工具

```python
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
```

### 7. 跨平台路径处理

```python
import sys

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
```

### 8. 目录树遍历

```python
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
```

## 重要知识点

### 1. os.path vs pathlib 对比

| 功能 | os.path | pathlib |
|------|---------|----------|
| 路径构建 | `os.path.join()` | `Path() / 'sub'` |
| 路径分解 | `os.path.dirname()` | `path.parent` |
| 文件名 | `os.path.basename()` | `path.name` |
| 扩展名 | `os.path.splitext()` | `path.suffix` |
| 存在判断 | `os.path.exists()` | `path.exists()` |
| 文件判断 | `os.path.isfile()` | `path.is_file()` |
| 目录判断 | `os.path.isdir()` | `path.is_dir()` |

### 2. glob 模式语法

- `*`：匹配任意数量的字符（不包括路径分隔符）
- `?`：匹配单个字符
- `[seq]`：匹配序列中的任意字符
- `[!seq]`：匹配不在序列中的任意字符
- `**`：递归匹配目录（需要 `recursive=True`）

### 3. 路径安全性

- **路径遍历攻击**：防止 `../` 等相对路径跳出限制目录
- **路径注入**：验证用户输入的路径
- **权限检查**：确保有足够权限访问路径
- **路径长度**：注意不同系统的路径长度限制

## 最佳实践

### 1. 选择合适的工具

```python
# 推荐：使用 pathlib（Python 3.4+）
from pathlib import Path

path = Path('data') / 'files' / 'document.txt'
if path.exists():
    content = path.read_text()

# 传统：使用 os.path
import os

path = os.path.join('data', 'files', 'document.txt')
if os.path.exists(path):
    with open(path, 'r') as f:
        content = f.read()
```

### 2. 跨平台兼容性

```python
# 好的做法
config_dir = Path.home() / '.myapp'
log_file = config_dir / 'app.log'

# 避免硬编码
# 坏的做法
config_dir = '/home/user/.myapp'  # 只在 Unix 系统工作
log_file = config_dir + '\\app.log'  # 只在 Windows 系统工作
```

### 3. 错误处理

```python
def safe_path_operation(path_str):
    try:
        path = Path(path_str)
        if path.exists():
            return path.stat().st_size
        else:
            return None
    except (OSError, PermissionError) as e:
        print(f"路径操作错误: {e}")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None
```

### 4. 性能优化

```python
# 批量操作时缓存路径对象
base_path = Path('/data/files')
files_to_process = []

for filename in file_list:
    file_path = base_path / filename
    if file_path.is_file():
        files_to_process.append(file_path)

# 避免重复的路径解析
for file_path in files_to_process:
    process_file(file_path)
```

## 注意事项

### 1. 编码问题

- 文件名可能包含非 ASCII 字符
- 不同系统的默认编码可能不同
- 使用 UTF-8 编码处理文件名

### 2. 大小写敏感性

- Windows 系统不区分大小写
- Unix/Linux 系统区分大小写
- 编写跨平台代码时要考虑这个差异

### 3. 路径长度限制

- Windows：260 字符（传统限制）
- Unix/Linux：通常 4096 字符
- 现代 Windows 可以启用长路径支持

### 4. 特殊字符处理

- 某些字符在文件名中有特殊含义
- 需要适当转义或替换
- 考虑不同文件系统的限制

## 练习建议

1. **基础练习**：
   - 编写函数分析目录结构
   - 实现文件查找和过滤功能
   - 创建路径验证工具

2. **进阶练习**：
   - 实现跨平台的配置文件管理
   - 编写文件同步工具
   - 创建目录监控程序

3. **实际应用**：
   - 日志文件轮转工具
   - 备份和归档系统
   - 文件整理和分类工具

## 下一步学习

学习完文件路径操作后，建议继续学习：
- 文件异常处理和错误恢复
- 文件操作的综合练习
- 高级文件系统操作
- 文件监控和事件处理

通过掌握文件路径操作，你将能够编写更加健壮和跨平台兼容的文件处理程序。