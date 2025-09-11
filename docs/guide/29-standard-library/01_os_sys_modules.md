# os和sys模块的使用

本节学习Python标准库中os和sys模块的常用功能，这两个模块是Python程序与操作系统交互的重要工具。

## 学习目标

- 掌握os模块的基本用法
- 理解sys模块的核心功能
- 学会处理路径和环境变量
- 了解系统信息获取方法

## os模块功能

os模块提供了与操作系统交互的接口，主要用于文件和目录操作。

### 基本目录操作

```python
import os

# 获取当前工作目录
current_dir = os.getcwd()
print(f"当前工作目录: {current_dir}")

# 列出目录内容
files = os.listdir('.')
for file in files[:5]:  # 只显示前5个文件
    print(f"文件: {file}")
```

### 环境变量操作

```python
# 获取环境变量
path_var = os.environ.get('PATH')
home_dir = os.environ.get('HOME', '未设置')
user_name = os.environ.get('USER', os.environ.get('USERNAME', '未知'))

# 设置环境变量
os.environ['PYTHON_DEMO_VAR'] = 'Hello, Python!'

# 删除环境变量
if 'PYTHON_DEMO_VAR' in os.environ:
    del os.environ['PYTHON_DEMO_VAR']
```

### 路径操作

```python
sample_path = "/home/user/documents/file.txt"

# 路径分解
dir_name = os.path.dirname(sample_path)  # /home/user/documents
file_name = os.path.basename(sample_path)  # file.txt
name, ext = os.path.splitext(sample_path)  # ('/home/user/documents/file', '.txt')

# 路径拼接
joined_path = os.path.join("home", "user", "documents", "file.txt")
```

### 文件系统检查

```python
# 检查文件/目录是否存在
if os.path.exists('README.md'):
    print("README.md存在")
    
# 检查是否为文件或目录
if os.path.isfile('README.md'):
    print("这是一个文件")
    
if os.path.isdir('.'):
    print("这是一个目录")

# 获取文件信息
stat_info = os.stat('README.md')
print(f"文件大小: {stat_info.st_size} 字节")
```

## sys模块功能

sys模块提供了与Python解释器相关的变量和函数。

### Python版本信息

```python
import sys

# Python版本信息
print(f"Python版本: {sys.version}")
print(f"版本信息: {sys.version_info}")
print(f"可执行文件路径: {sys.executable}")
```

### 平台信息

```python
# 平台相关信息
print(f"操作系统: {sys.platform}")
print(f"字节序: {sys.byteorder}")
print(f"默认编码: {sys.getdefaultencoding()}")
```

### 模块搜索路径

```python
# 模块搜索路径
print("模块搜索路径:")
for i, path in enumerate(sys.path[:5], 1):
    print(f"  {i}. {path}")
```

### 命令行参数

```python
# 命令行参数
print(f"脚本名称: {sys.argv[0]}")
print(f"参数个数: {len(sys.argv)}")
if len(sys.argv) > 1:
    print(f"其他参数: {sys.argv[1:]}")
```

### 系统限制信息

```python
# 系统限制
print(f"最大整数值: {sys.maxsize}")
print(f"递归限制: {sys.getrecursionlimit()}")

# 标准流
print(f"标准输入: {sys.stdin.name}")
print(f"标准输出: {sys.stdout.name}")
print(f"标准错误: {sys.stderr.name}")
```

## platform模块

platform模块提供了更详细的平台信息。

```python
import platform

# 系统信息
print(f"系统名称: {platform.system()}")
print(f"系统版本: {platform.release()}")
print(f"机器类型: {platform.machine()}")
print(f"处理器信息: {platform.processor()}")
print(f"架构信息: {platform.architecture()}")
print(f"主机名: {platform.node()}")

# Python实现信息
print(f"Python实现: {platform.python_implementation()}")
print(f"Python版本: {platform.python_version()}")
print(f"Python编译器: {platform.python_compiler()}")
```

## 文件操作示例

```python
# 文件和目录操作
demo_file = "demo_file.txt"
demo_dir = "demo_directory"

try:
    # 创建文件
    with open(demo_file, 'w', encoding='utf-8') as f:
        f.write("演示文件内容\n")
    
    # 获取文件信息
    stat_info = os.stat(demo_file)
    print(f"文件大小: {stat_info.st_size} 字节")
    
    # 创建目录
    if not os.path.exists(demo_dir):
        os.mkdir(demo_dir)
    
    # 重命名和移动文件
    new_name = "renamed_demo.txt"
    os.rename(demo_file, new_name)
    
    moved_path = os.path.join(demo_dir, new_name)
    os.rename(new_name, moved_path)
    
    # 列出目录内容
    for item in os.listdir(demo_dir):
        item_path = os.path.join(demo_dir, item)
        if os.path.isfile(item_path):
            print(f"文件: {item}")
        elif os.path.isdir(item_path):
            print(f"目录: {item}")
            
finally:
    # 清理资源
    if os.path.exists(moved_path):
        os.remove(moved_path)
    if os.path.exists(demo_dir):
        os.rmdir(demo_dir)
```

## 学习要点

### 重点知识

1. **os模块**：主要用于操作系统接口操作
2. **sys模块**：提供Python解释器相关信息
3. **环境变量**：通过os.environ访问和修改
4. **路径操作**：使用os.path模块更安全
5. **platform模块**：提供详细的平台信息

### 注意事项

1. **跨平台兼容性**：使用os.path.join()而不是手动拼接路径
2. **异常处理**：文件操作要注意异常处理
3. **资源清理**：及时清理创建的临时文件和目录
4. **权限问题**：注意文件和目录的访问权限
5. **编码问题**：处理文件时指定正确的编码格式

### 实践建议

1. 多练习不同的路径操作方法
2. 了解不同操作系统的差异
3. 学会使用环境变量配置程序
4. 掌握文件权限和属性的获取
5. 熟悉系统信息的获取方法

## 运行示例

```bash
# 运行完整示例
python3 01_os_sys_modules.py

# 带参数运行
python3 01_os_sys_modules.py arg1 arg2
```

通过本节学习，你将掌握Python与操作系统交互的基本方法，为后续的文件处理和系统编程打下基础。