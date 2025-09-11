#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04_pathlib_shutil.py - 文件和目录操作模块学习

本文件演示Python pathlib和shutil模块的各种功能：
1. pathlib模块的现代路径操作
2. 文件和目录的创建、删除、移动
3. 文件属性和权限操作
4. 目录遍历和搜索
5. 文件复制和归档操作
6. 实际应用示例

学习目标：
- 掌握pathlib的面向对象路径操作
- 学会使用shutil进行高级文件操作
- 了解文件系统的各种操作方法
- 掌握文件和目录的批量处理
"""

import os
import shutil
import tempfile
import zipfile
import tarfile
from pathlib import Path
from datetime import datetime
import stat
import glob

def pathlib_basics_demo():
    """pathlib基础操作演示"""
    print("=" * 50)
    print("pathlib基础操作演示")
    print("=" * 50)
    
    # 创建Path对象
    current_dir = Path.cwd()
    print(f"当前工作目录: {current_dir}")
    
    home_dir = Path.home()
    print(f"用户主目录: {home_dir}")
    
    # 路径拼接
    file_path = current_dir / "test_file.txt"
    print(f"拼接路径: {file_path}")
    
    # 路径属性
    sample_path = Path("/home/user/documents/report.pdf")
    print(f"\n路径分析:")
    print(f"  完整路径: {sample_path}")
    print(f"  父目录: {sample_path.parent}")
    print(f"  文件名: {sample_path.name}")
    print(f"  文件主名: {sample_path.stem}")
    print(f"  文件扩展名: {sample_path.suffix}")
    print(f"  所有扩展名: {sample_path.suffixes}")
    print(f"  根目录: {sample_path.root}")
    print(f"  路径部分: {sample_path.parts}")
    
    # 路径判断
    print(f"\n路径判断:")
    print(f"  是否绝对路径: {sample_path.is_absolute()}")
    print(f"  当前目录是否存在: {current_dir.exists()}")
    print(f"  当前目录是否为目录: {current_dir.is_dir()}")
    print(f"  当前目录是否为文件: {current_dir.is_file()}")
    
    print()

def file_operations_demo():
    """文件操作演示"""
    print("=" * 50)
    print("文件操作演示")
    print("=" * 50)
    
    # 创建临时目录进行演示
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        print(f"临时目录: {temp_path}")
        
        # 创建文件
        test_file = temp_path / "test.txt"
        test_file.write_text("Hello, World!\n这是测试文件内容。", encoding='utf-8')
        print(f"创建文件: {test_file}")
        
        # 读取文件
        content = test_file.read_text(encoding='utf-8')
        print(f"文件内容: {repr(content)}")
        
        # 文件信息
        stat_info = test_file.stat()
        print(f"\n文件信息:")
        print(f"  文件大小: {stat_info.st_size} 字节")
        print(f"  创建时间: {datetime.fromtimestamp(stat_info.st_ctime)}")
        print(f"  修改时间: {datetime.fromtimestamp(stat_info.st_mtime)}")
        print(f"  访问时间: {datetime.fromtimestamp(stat_info.st_atime)}")
        
        # 文件权限
        print(f"  文件权限: {oct(stat_info.st_mode)}")
        print(f"  是否可读: {os.access(test_file, os.R_OK)}")
        print(f"  是否可写: {os.access(test_file, os.W_OK)}")
        print(f"  是否可执行: {os.access(test_file, os.X_OK)}")
        
        # 创建二进制文件
        binary_file = temp_path / "binary.dat"
        binary_data = b'\x00\x01\x02\x03\x04\x05'
        binary_file.write_bytes(binary_data)
        print(f"\n创建二进制文件: {binary_file}")
        
        # 读取二进制文件
        read_data = binary_file.read_bytes()
        print(f"二进制数据: {read_data.hex()}")
        
        # 追加内容
        with test_file.open('a', encoding='utf-8') as f:
            f.write("追加的内容\n")
        
        updated_content = test_file.read_text(encoding='utf-8')
        print(f"\n追加后的内容: {repr(updated_content)}")
    
    print()

def directory_operations_demo():
    """目录操作演示"""
    print("=" * 50)
    print("目录操作演示")
    print("=" * 50)
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # 创建目录结构
        project_dir = temp_path / "my_project"
        src_dir = project_dir / "src"
        docs_dir = project_dir / "docs"
        tests_dir = project_dir / "tests"
        
        # 创建多级目录
        src_dir.mkdir(parents=True, exist_ok=True)
        docs_dir.mkdir(parents=True, exist_ok=True)
        tests_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"创建项目目录结构:")
        print(f"  {project_dir}")
        print(f"  ├── {src_dir.name}/")
        print(f"  ├── {docs_dir.name}/")
        print(f"  └── {tests_dir.name}/")
        
        # 创建一些文件
        files_to_create = [
            src_dir / "main.py",
            src_dir / "utils.py",
            docs_dir / "README.md",
            docs_dir / "API.md",
            tests_dir / "test_main.py"
        ]
        
        for file_path in files_to_create:
            file_path.write_text(f"# {file_path.name}\n这是 {file_path.name} 文件")
        
        print(f"\n创建了 {len(files_to_create)} 个文件")
        
        # 遍历目录
        print("\n目录遍历:")
        for item in project_dir.rglob("*"):
            if item.is_file():
                print(f"  文件: {item.relative_to(project_dir)}")
            elif item.is_dir():
                print(f"  目录: {item.relative_to(project_dir)}/")
        
        # 按模式搜索文件
        print("\n搜索Python文件:")
        for py_file in project_dir.rglob("*.py"):
            print(f"  {py_file.relative_to(project_dir)}")
        
        print("\n搜索Markdown文件:")
        for md_file in project_dir.rglob("*.md"):
            print(f"  {md_file.relative_to(project_dir)}")
        
        # 目录统计
        all_files = list(project_dir.rglob("*"))
        files = [f for f in all_files if f.is_file()]
        dirs = [d for d in all_files if d.is_dir()]
        
        print(f"\n目录统计:")
        print(f"  总文件数: {len(files)}")
        print(f"  总目录数: {len(dirs)}")
        
        # 计算目录大小
        total_size = sum(f.stat().st_size for f in files)
        print(f"  总大小: {total_size} 字节")
    
    print()

def shutil_operations_demo():
    """shutil高级操作演示"""
    print("=" * 50)
    print("shutil高级操作演示")
    print("=" * 50)
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # 创建源文件和目录
        source_dir = temp_path / "source"
        source_dir.mkdir()
        
        # 创建一些测试文件
        (source_dir / "file1.txt").write_text("内容1")
        (source_dir / "file2.txt").write_text("内容2")
        
        subdir = source_dir / "subdir"
        subdir.mkdir()
        (subdir / "file3.txt").write_text("内容3")
        
        print(f"创建源目录: {source_dir}")
        
        # 复制文件
        dest_file = temp_path / "copied_file.txt"
        shutil.copy2(source_dir / "file1.txt", dest_file)
        print(f"复制文件: {dest_file}")
        
        # 复制整个目录树
        dest_dir = temp_path / "destination"
        shutil.copytree(source_dir, dest_dir)
        print(f"复制目录树: {dest_dir}")
        
        # 移动文件
        moved_file = temp_path / "moved_file.txt"
        shutil.move(dest_file, moved_file)
        print(f"移动文件: {moved_file}")
        
        # 获取磁盘使用情况
        disk_usage = shutil.disk_usage(temp_path)
        print(f"\n磁盘使用情况:")
        print(f"  总空间: {disk_usage.total / (1024**3):.2f} GB")
        print(f"  已使用: {disk_usage.used / (1024**3):.2f} GB")
        print(f"  可用空间: {disk_usage.free / (1024**3):.2f} GB")
        
        # 查找可执行文件
        python_path = shutil.which("python3")
        if python_path:
            print(f"\nPython3路径: {python_path}")
        
        # 删除目录树
        shutil.rmtree(dest_dir)
        print(f"删除目录树: {dest_dir}")
    
    print()

def archive_operations_demo():
    """归档操作演示"""
    print("=" * 50)
    print("归档操作演示")
    print("=" * 50)
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # 创建要归档的目录
        archive_source = temp_path / "to_archive"
        archive_source.mkdir()
        
        # 创建一些文件
        (archive_source / "readme.txt").write_text("这是说明文件")
        (archive_source / "data.csv").write_text("name,age\nAlice,25\nBob,30")
        
        subdir = archive_source / "config"
        subdir.mkdir()
        (subdir / "settings.ini").write_text("[DEFAULT]\ndebug=true")
        
        print(f"创建归档源目录: {archive_source}")
        
        # 创建ZIP归档
        zip_file = temp_path / "archive.zip"
        shutil.make_archive(str(zip_file.with_suffix('')), 'zip', archive_source)
        print(f"创建ZIP归档: {zip_file}")
        
        # 创建TAR归档
        tar_file = temp_path / "archive.tar.gz"
        shutil.make_archive(str(tar_file.with_suffix('').with_suffix('')), 'gztar', archive_source)
        print(f"创建TAR归档: {tar_file}")
        
        # 解压ZIP文件
        extract_dir = temp_path / "extracted_zip"
        shutil.unpack_archive(zip_file, extract_dir)
        print(f"解压ZIP到: {extract_dir}")
        
        # 使用zipfile模块进行更精细的控制
        detailed_zip = temp_path / "detailed.zip"
        with zipfile.ZipFile(detailed_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file_path in archive_source.rglob("*"):
                if file_path.is_file():
                    arcname = file_path.relative_to(archive_source)
                    zf.write(file_path, arcname)
                    print(f"  添加到ZIP: {arcname}")
        
        print(f"创建详细ZIP: {detailed_zip}")
        
        # 查看ZIP内容
        print("\nZIP文件内容:")
        with zipfile.ZipFile(detailed_zip, 'r') as zf:
            for info in zf.infolist():
                print(f"  {info.filename} ({info.file_size} 字节)")
        
        # 归档文件大小比较
        original_size = sum(f.stat().st_size for f in archive_source.rglob("*") if f.is_file())
        zip_size = zip_file.stat().st_size
        tar_size = tar_file.stat().st_size
        
        print(f"\n大小比较:")
        print(f"  原始大小: {original_size} 字节")
        print(f"  ZIP大小: {zip_size} 字节 (压缩率: {(1-zip_size/original_size)*100:.1f}%)")
        print(f"  TAR.GZ大小: {tar_size} 字节 (压缩率: {(1-tar_size/original_size)*100:.1f}%)")
    
    print()

def glob_patterns_demo():
    """文件模式匹配演示"""
    print("=" * 50)
    print("文件模式匹配演示")
    print("=" * 50)
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # 创建各种类型的文件
        files_to_create = [
            "document.txt", "report.pdf", "image.jpg", "image.png",
            "script.py", "config.json", "data.csv", "backup.tar.gz",
            "test_file.py", "main.py", "utils.py"
        ]
        
        for filename in files_to_create:
            (temp_path / filename).write_text(f"# {filename}")
        
        # 创建子目录和文件
        subdir = temp_path / "subdir"
        subdir.mkdir()
        (subdir / "nested.txt").write_text("嵌套文件")
        (subdir / "another.py").write_text("# 另一个Python文件")
        
        print(f"创建了 {len(files_to_create) + 2} 个文件")
        
        # 使用glob模式匹配
        print("\n模式匹配结果:")
        
        # 匹配所有.py文件
        py_files = list(temp_path.glob("*.py"))
        print(f"  *.py: {[f.name for f in py_files]}")
        
        # 匹配所有图片文件
        image_files = list(temp_path.glob("*.jpg")) + list(temp_path.glob("*.png"))
        print(f"  图片文件: {[f.name for f in image_files]}")
        
        # 递归匹配所有.py文件
        all_py_files = list(temp_path.rglob("*.py"))
        print(f"  递归*.py: {[f.relative_to(temp_path) for f in all_py_files]}")
        
        # 匹配以test开头的文件
        test_files = list(temp_path.glob("test*"))
        print(f"  test*: {[f.name for f in test_files]}")
        
        # 使用字符类匹配
        char_class_files = list(temp_path.glob("[dit]*"))
        print(f"  [dit]*: {[f.name for f in char_class_files]}")
        
        # 使用问号匹配单个字符
        question_files = list(temp_path.glob("????.*"))
        print(f"  ????.*: {[f.name for f in question_files]}")
    
    print()

def practical_applications():
    """实际应用示例"""
    print("=" * 50)
    print("实际应用示例")
    print("=" * 50)
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # 1. 批量重命名文件
        def batch_rename_demo():
            """批量重命名演示"""
            print("1. 批量重命名文件:")
            
            # 创建一些文件
            old_files = []
            for i in range(5):
                filename = f"old_name_{i}.txt"
                file_path = temp_path / filename
                file_path.write_text(f"文件 {i}")
                old_files.append(file_path)
            
            print(f"  原始文件: {[f.name for f in old_files]}")
            
            # 批量重命名
            new_files = []
            for i, old_file in enumerate(old_files):
                new_name = f"new_name_{i:03d}.txt"
                new_file = old_file.parent / new_name
                old_file.rename(new_file)
                new_files.append(new_file)
            
            print(f"  重命名后: {[f.name for f in new_files]}")
        
        # 2. 清理临时文件
        def cleanup_temp_files_demo():
            """清理临时文件演示"""
            print("\n2. 清理临时文件:")
            
            # 创建一些临时文件
            temp_files = []
            for ext in ['.tmp', '.bak', '.log', '.cache']:
                for i in range(3):
                    filename = f"temp_{i}{ext}"
                    file_path = temp_path / filename
                    file_path.write_text("临时数据")
                    temp_files.append(file_path)
            
            print(f"  创建临时文件: {len(temp_files)} 个")
            
            # 清理特定扩展名的文件
            cleanup_extensions = ['.tmp', '.bak', '.cache']
            cleaned_count = 0
            
            for ext in cleanup_extensions:
                for file_path in temp_path.glob(f"*{ext}"):
                    file_path.unlink()
                    cleaned_count += 1
            
            print(f"  清理了 {cleaned_count} 个临时文件")
            
            remaining_files = list(temp_path.glob("*"))
            print(f"  剩余文件: {[f.name for f in remaining_files]}")
        
        # 3. 文件备份
        def backup_files_demo():
            """文件备份演示"""
            print("\n3. 文件备份:")
            
            # 创建要备份的文件
            important_file = temp_path / "important.txt"
            important_file.write_text("重要数据")
            
            # 创建备份
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{important_file.stem}_{timestamp}{important_file.suffix}"
            backup_file = important_file.parent / backup_name
            
            shutil.copy2(important_file, backup_file)
            print(f"  备份文件: {backup_file.name}")
            
            # 验证备份
            original_content = important_file.read_text()
            backup_content = backup_file.read_text()
            print(f"  备份验证: {'成功' if original_content == backup_content else '失败'}")
        
        # 4. 目录同步
        def sync_directories_demo():
            """目录同步演示"""
            print("\n4. 目录同步:")
            
            # 创建源目录和目标目录
            source = temp_path / "source_sync"
            target = temp_path / "target_sync"
            
            source.mkdir()
            target.mkdir()
            
            # 在源目录创建文件
            (source / "file1.txt").write_text("文件1")
            (source / "file2.txt").write_text("文件2")
            
            # 在目标目录创建一个旧文件
            (target / "old_file.txt").write_text("旧文件")
            
            print(f"  源目录文件: {[f.name for f in source.iterdir()]}")
            print(f"  目标目录文件（同步前）: {[f.name for f in target.iterdir()]}")
            
            # 简单同步（复制新文件）
            for source_file in source.iterdir():
                if source_file.is_file():
                    target_file = target / source_file.name
                    if not target_file.exists():
                        shutil.copy2(source_file, target_file)
            
            print(f"  目标目录文件（同步后）: {[f.name for f in target.iterdir()]}")
        
        batch_rename_demo()
        cleanup_temp_files_demo()
        backup_files_demo()
        sync_directories_demo()
    
    print()

def main():
    """主函数"""
    print("Python pathlib和shutil模块学习演示")
    print("=" * 60)
    
    pathlib_basics_demo()
    file_operations_demo()
    directory_operations_demo()
    shutil_operations_demo()
    archive_operations_demo()
    glob_patterns_demo()
    practical_applications()
    
    print("=" * 50)
    print("学习要点总结:")
    print("=" * 50)
    print("1. pathlib提供面向对象的路径操作接口")
    print("2. Path对象支持 / 操作符进行路径拼接")
    print("3. 使用glob()和rglob()进行文件模式匹配")
    print("4. shutil提供高级文件和目录操作功能")
    print("5. 支持文件复制、移动、删除等操作")
    print("6. 可以创建和解压各种格式的归档文件")
    print("7. 实际应用包括批量处理、备份、同步等")
    print("8. 结合使用pathlib和shutil可以高效处理文件系统操作")

if __name__ == "__main__":
    main()