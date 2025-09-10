#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""命名空间包管理工具"""

import sys
import os
from pathlib import Path
import pkgutil
import importlib.util

class NamespaceManager:
    """命名空间包管理器"""
    
    def __init__(self):
        self.namespace_paths = {}
    
    def add_namespace_path(self, namespace, path):
        """添加命名空间路径"""
        if namespace not in self.namespace_paths:
            self.namespace_paths[namespace] = []
        
        abs_path = os.path.abspath(path)
        if abs_path not in self.namespace_paths[namespace]:
            self.namespace_paths[namespace].append(abs_path)
            
            # 添加到sys.path
            if abs_path not in sys.path:
                sys.path.insert(0, abs_path)
                print(f"添加命名空间路径: {namespace} -> {abs_path}")
    
    def discover_modules(self, namespace):
        """发现命名空间中的所有模块"""
        if namespace not in self.namespace_paths:
            return []
        
        modules = []
        try:
            # 导入命名空间包
            ns_module = importlib.import_module(namespace)
            
            # 遍历所有模块
            for importer, modname, ispkg in pkgutil.walk_packages(
                ns_module.__path__, 
                ns_module.__name__ + "."
            ):
                modules.append({
                    "name": modname,
                    "is_package": ispkg,
                    "importer": str(importer)
                })
        except Exception as e:
            print(f"发现模块时出错: {e}")
        
        return modules
    
    def get_module_info(self, module_name):
        """获取模块详细信息"""
        try:
            module = importlib.import_module(module_name)
            return {
                "name": module.__name__,
                "file": getattr(module, "__file__", "无文件"),
                "package": getattr(module, "__package__", "无包信息"),
                "path": getattr(module, "__path__", "无路径信息")
            }
        except Exception as e:
            return {"error": str(e)}
    
    def list_namespaces(self):
        """列出所有管理的命名空间"""
        return dict(self.namespace_paths)

# 使用示例
if __name__ == "__main__":
    manager = NamespaceManager()
    
    # 添加命名空间路径
    manager.add_namespace_path("myproject", "namespace_demo/path1")
    manager.add_namespace_path("myproject", "namespace_demo/path2")
    manager.add_namespace_path("myproject", "namespace_demo/path3")
    
    # 发现模块
    modules = manager.discover_modules("myproject")
    print(f"发现的模块: {len(modules)}个")
    for module in modules:
        print(f"  {module['name']} ({'包' if module['is_package'] else '模块'})")
    
    # 获取模块信息
    if modules:
        first_module = modules[0]["name"]
        info = manager.get_module_info(first_module)
        print(f"
模块信息 ({first_module}):")
        for key, value in info.items():
            print(f"  {key}: {value}")
