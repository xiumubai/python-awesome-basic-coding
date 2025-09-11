# 04_pathlib_shutil.py - 文件和目录操作模块学习

## 学习目标

通过本节学习，你将掌握：
- pathlib模块的现代路径操作方法
- 文件和目录的创建、删除、移动操作
- 文件属性和权限的查看与修改
- 目录遍历和文件搜索技巧
- shutil模块的高级文件操作
- 文件归档和压缩操作
- 实际项目中的文件处理应用

## 核心概念

### 1. pathlib模块
- `Path`: 面向对象的路径操作类
- 路径拼接：使用 `/` 操作符
- 路径属性：parent、name、stem、suffix等
- 路径判断：exists()、is_file()、is_dir()等

### 2. shutil模块
- 文件复制：copy()、copy2()、copytree()
- 文件移动：move()
- 目录删除：rmtree()
- 归档操作：make_archive()、unpack_archive()

### 3. 文件模式匹配
- glob模式：*、?、[]等通配符
- 递归搜索：rglob()
- 文件过滤和批量处理

## 代码示例

### pathlib基础操作

```python
from pathlib import Path

# 创建Path对象
current_dir = Path.cwd()
home_dir = Path.home()

# 路径拼接
file_path = current_dir / "test_file.txt"
print(f"拼接路径: {file_path}")

# 路径属性
sample_path = Path("/home/user/documents/report.pdf")
print(f"父目录: {sample_path.parent}")
print(f"文件名: {sample_path.name}")
print(f"文件主名: {sample_path.stem}")
print(f"文件扩展名: {sample_path.suffix}")
print(f"路径部分: {sample_path.parts}")

# 路径判断
print(f"是否绝对路径: {sample_path.is_absolute()}")
print(f"是否存在: {current_dir.exists()}")
print(f"是否为目录: {current_dir.is_dir()}")
print(f"是否为文件: {current_dir.is_file()}")
```

### 文件操作

```python
# 创建和读写文件
test_file = Path("test.txt")
test_file.write_text("Hello, World!\n这是测试文件内容。", encoding='utf-8')
content = test_file.read_text(encoding='utf-8')
print(f"文件内容: {content}")

# 二进制文件操作
binary_file = Path("binary.dat")
binary_data = b'\x00\x01\x02\x03\x04\x05'
binary_file.write_bytes(binary_data)
read_data = binary_file.read_bytes()
print(f"二进制数据: {read_data.hex()}")

# 文件信息
stat_info = test_file.stat()
print(f"文件大小: {stat_info.st_size} 字节")
print(f"修改时间: {datetime.fromtimestamp(stat_info.st_mtime)}")
print(f"文件权限: {oct(stat_info.st_mode)}")
```

### 目录操作

```python
# 创建目录结构
project_dir = Path("my_project")
src_dir = project_dir / "src"
docs_dir = project_dir / "docs"
tests_dir = project_dir / "tests"

# 创建多级目录
src_dir.mkdir(parents=True, exist_ok=True)
docs_dir.mkdir(parents=True, exist_ok=True)
tests_dir.mkdir(parents=True, exist_ok=True)

# 遍历目录
for item in project_dir.rglob("*"):
    if item.is_file():
        print(f"文件: {item.relative_to(project_dir)}")
    elif item.is_dir():
        print(f"目录: {item.relative_to(project_dir)}/")

# 搜索特定文件
for py_file in project_dir.rglob("*.py"):
    print(f"Python文件: {py_file.relative_to(project_dir)}")
```

### shutil高级操作

```python
import shutil

# 复制文件
shutil.copy2("source.txt", "destination.txt")

# 复制整个目录树
shutil.copytree("source_dir", "dest_dir")

# 移动文件或目录
shutil.move("old_location", "new_location")

# 删除目录树
shutil.rmtree("directory_to_delete")

# 获取磁盘使用情况
disk_usage = shutil.disk_usage(".")
print(f"总空间: {disk_usage.total / (1024**3):.2f} GB")
print(f"已使用: {disk_usage.used / (1024**3):.2f} GB")
print(f"可用空间: {disk_usage.free / (1024**3):.2f} GB")

# 查找可执行文件
python_path = shutil.which("python3")
print(f"Python3路径: {python_path}")
```

### 归档操作

```python
# 创建ZIP归档
shutil.make_archive("archive", 'zip', "source_directory")

# 创建TAR归档
shutil.make_archive("archive", 'gztar', "source_directory")

# 解压归档
shutil.unpack_archive("archive.zip", "extract_directory")

# 使用zipfile进行精细控制
import zipfile

with zipfile.ZipFile("detailed.zip", 'w', zipfile.ZIP_DEFLATED) as zf:
    for file_path in Path("source").rglob("*"):
        if file_path.is_file():
            arcname = file_path.relative_to(Path("source"))
            zf.write(file_path, arcname)

# 查看ZIP内容
with zipfile.ZipFile("archive.zip", 'r') as zf:
    for info in zf.infolist():
        print(f"{info.filename} ({info.file_size} 字节)")
```

### 文件模式匹配

```python
# glob模式匹配
py_files = list(Path(".").glob("*.py"))
print(f"Python文件: {[f.name for f in py_files]}")

# 递归匹配
all_py_files = list(Path(".").rglob("*.py"))
print(f"所有Python文件: {[str(f) for f in all_py_files]}")

# 复杂模式
test_files = list(Path(".").glob("test*.py"))
config_files = list(Path(".").glob("*config*"))
image_files = list(Path(".").glob("*.{jpg,png,gif}"))

# 字符类匹配
char_files = list(Path(".").glob("[abc]*.txt"))
question_files = list(Path(".").glob("????.py"))
```

### 实际应用示例

```python
# 批量重命名文件
def batch_rename(directory, old_pattern, new_pattern):
    """批量重命名文件"""
    path = Path(directory)
    for i, file_path in enumerate(path.glob(old_pattern)):
        new_name = new_pattern.format(i=i, name=file_path.stem)
        new_file = file_path.parent / f"{new_name}{file_path.suffix}"
        file_path.rename(new_file)
        print(f"重命名: {file_path.name} -> {new_file.name}")

# 清理临时文件
def cleanup_temp_files(directory, extensions):
    """清理临时文件"""
    path = Path(directory)
    cleaned_count = 0
    for ext in extensions:
        for file_path in path.glob(f"*{ext}"):
            file_path.unlink()
            cleaned_count += 1
    print(f"清理了 {cleaned_count} 个临时文件")

# 文件备份
def backup_file(file_path):
    """创建文件备份"""
    path = Path(file_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{path.stem}_{timestamp}{path.suffix}"
    backup_path = path.parent / backup_name
    shutil.copy2(path, backup_path)
    return backup_path

# 目录同步
def sync_directories(source, target):
    """同步目录"""
    source_path = Path(source)
    target_path = Path(target)
    
    for source_file in source_path.rglob("*"):
        if source_file.is_file():
            relative_path = source_file.relative_to(source_path)
            target_file = target_path / relative_path
            
            # 创建目标目录
            target_file.parent.mkdir(parents=True, exist_ok=True)
            
            # 复制文件（如果不存在或更新）
            if not target_file.exists() or source_file.stat().st_mtime > target_file.stat().st_mtime:
                shutil.copy2(source_file, target_file)
                print(f"同步: {relative_path}")
```

## 重要知识点

### 1. pathlib优势
- 面向对象的设计，更直观易用
- 跨平台路径处理
- 丰富的路径操作方法
- 与字符串路径兼容

### 2. 文件操作最佳实践
- 使用with语句确保文件正确关闭
- 指定编码避免乱码问题
- 处理文件不存在等异常情况
- 大文件操作考虑内存使用

### 3. 目录操作注意事项
- 使用parents=True创建多级目录
- 使用exist_ok=True避免目录已存在错误
- 删除目录前确认内容
- 权限问题的处理

### 4. 性能考虑
- 大量文件操作时使用批量处理
- 避免频繁的磁盘I/O操作
- 合理使用缓存和临时文件
- 异步操作处理大文件

## 运行方式

```bash
# 在29-standard-library目录下运行
cd 29-standard-library
python3 04_pathlib_shutil.py
```

## 练习建议

1. **基础练习**：
   - 编写文件管理器的基本功能
   - 实现文件搜索和过滤功能
   - 创建目录结构生成器

2. **进阶练习**：
   - 开发文件同步工具
   - 实现智能备份系统
   - 编写日志文件分析器

3. **实际应用**：
   - 构建项目模板生成器
   - 开发文件批量处理工具
   - 实现自动化部署脚本

## 注意事项

1. **路径处理**：注意不同操作系统的路径分隔符差异
2. **权限管理**：确保有足够权限进行文件操作
3. **异常处理**：妥善处理文件不存在、权限不足等异常
4. **资源管理**：及时关闭文件句柄，避免资源泄露
5. **安全考虑**：验证文件路径，防止路径遍历攻击