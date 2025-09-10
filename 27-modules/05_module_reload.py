#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模块重新加载演示

本文件演示Python中模块重新加载的机制和用法，包括：
1. 模块加载和缓存机制
2. importlib.reload()的使用
3. 重新加载的注意事项
4. 动态模块更新
5. 实际应用场景
6. 最佳实践和限制

学习目标：
- 理解模块缓存机制
- 掌握模块重新加载的方法
- 了解重新加载的限制和注意事项
- 学会在开发中合理使用重新加载
"""

import sys
import os
import importlib
import time
from pathlib import Path

# ============================================================================
# 1. 模块缓存机制演示
# ============================================================================

def demonstrate_module_caching():
    """
    演示Python的模块缓存机制
    """
    print("=== 1. 模块缓存机制 ===")
    
    print("Python模块缓存机制：")
    print("1. 模块首次导入时会被加载和执行")
    print("2. 模块对象被缓存在sys.modules中")
    print("3. 后续导入直接从缓存返回，不重新执行")
    print("4. 这提高了性能，但也意味着模块修改不会自动生效")
    
    # 查看当前已加载的模块
    print(f"\n当前已加载的模块数量: {len(sys.modules)}")
    
    # 显示一些常见的已加载模块
    common_modules = ['sys', 'os', 'importlib', 'json', 'time']
    print("\n一些常见的已加载模块：")
    for module_name in common_modules:
        if module_name in sys.modules:
            module = sys.modules[module_name]
            print(f"  {module_name:12s}: {module}")
        else:
            print(f"  {module_name:12s}: [未加载]")
    
    # 演示重复导入
    print("\n演示重复导入：")
    print("第一次导入json模块...")
    import json
    json_id_1 = id(json)
    print(f"json模块对象ID: {json_id_1}")
    
    print("\n第二次导入json模块...")
    import json as json2
    json_id_2 = id(json2)
    print(f"json模块对象ID: {json_id_2}")
    print(f"两次导入是同一个对象: {json_id_1 == json_id_2}")

# ============================================================================
# 2. 创建可重新加载的演示模块
# ============================================================================

def create_reloadable_module():
    """
    创建一个可重新加载的演示模块
    """
    print("\n=== 2. 创建可重新加载的模块 ===")
    
    module_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
可重新加载的演示模块
"""

import time

# 模块版本（用于演示重新加载）
MODULE_VERSION = "1.0.0"
LOAD_TIME = time.time()
LOAD_COUNT = 0

# 每次加载时递增计数器
if 'LOAD_COUNT' in globals():
    LOAD_COUNT += 1
else:
    LOAD_COUNT = 1

print(f"可重新加载模块被加载，版本: {MODULE_VERSION}，第 {LOAD_COUNT} 次加载")

def get_module_info():
    """
    获取模块信息
    """
    return {
        'version': MODULE_VERSION,
        'load_time': LOAD_TIME,
        'load_count': LOAD_COUNT,
        'current_time': time.time()
    }

def greet(name="World"):
    """
    问候函数
    """
    return f"Hello, {name}! 来自版本 {MODULE_VERSION} (第 {LOAD_COUNT} 次加载)"

class ReloadableClass:
    """
    可重新加载的类
    """
    def __init__(self):
        self.version = MODULE_VERSION
        self.created_at = time.time()
    
    def get_info(self):
        return f"ReloadableClass 版本 {self.version}，创建于 {self.created_at}"

# 模块级别的变量
MODULE_DATA = {
    'name': '可重新加载模块',
    'version': MODULE_VERSION,
    'features': ['重新加载', '版本跟踪', '状态保持']
}
'''
    
    module_file = "reloadable_module.py"
    
    try:
        with open(module_file, 'w', encoding='utf-8') as f:
            f.write(module_content)
        print(f"创建可重新加载模块: {module_file}")
        return module_file
    except Exception as e:
        print(f"创建模块文件失败: {e}")
        return None

# ============================================================================
# 3. 演示模块重新加载
# ============================================================================

def demonstrate_module_reload(module_file):
    """
    演示模块重新加载过程
    """
    print("\n=== 3. 模块重新加载演示 ===")
    
    if not module_file or not os.path.exists(module_file):
        print("模块文件不存在，跳过重新加载演示")
        return
    
    # 首次导入模块
    print("\n步骤1: 首次导入模块")
    try:
        import reloadable_module
        print(f"模块信息: {reloadable_module.get_module_info()}")
        print(f"问候函数: {reloadable_module.greet('Python')}")
        
        # 创建类实例
        obj1 = reloadable_module.ReloadableClass()
        print(f"类实例: {obj1.get_info()}")
        
    except ImportError as e:
        print(f"导入模块失败: {e}")
        return
    
    # 等待一秒
    time.sleep(1)
    
    # 修改模块文件
    print("\n步骤2: 修改模块文件")
    try:
        # 读取原文件内容
        with open(module_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 修改版本号
        modified_content = content.replace('MODULE_VERSION = "1.0.0"', 'MODULE_VERSION = "2.0.0"')
        
        # 写回文件
        with open(module_file, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        print("模块文件已修改（版本号从1.0.0改为2.0.0）")
        
    except Exception as e:
        print(f"修改模块文件失败: {e}")
        return
    
    # 重新导入（不会生效）
    print("\n步骤3: 重新导入（不会生效）")
    import reloadable_module as reloaded_module
    print(f"重新导入后的模块信息: {reloaded_module.get_module_info()}")
    print("注意: 版本号仍然是1.0.0，因为模块被缓存了")
    
    # 使用importlib.reload()重新加载
    print("\n步骤4: 使用importlib.reload()重新加载")
    try:
        importlib.reload(reloadable_module)
        print(f"重新加载后的模块信息: {reloadable_module.get_module_info()}")
        print(f"问候函数: {reloadable_module.greet('重新加载')}")
        
        # 创建新的类实例
        obj2 = reloadable_module.ReloadableClass()
        print(f"新类实例: {obj2.get_info()}")
        
        # 比较旧实例
        print(f"旧类实例: {obj1.get_info()}")
        print("注意: 旧实例仍然使用旧版本的类定义")
        
    except Exception as e:
        print(f"重新加载失败: {e}")

# ============================================================================
# 4. 重新加载的注意事项和限制
# ============================================================================

def demonstrate_reload_limitations():
    """
    演示重新加载的注意事项和限制
    """
    print("\n=== 4. 重新加载的注意事项 ===")
    
    print("重新加载的限制：")
    print("\n1. 已存在的对象不会更新")
    print("   - 已创建的类实例仍使用旧的类定义")
    print("   - 已绑定的函数引用不会更新")
    
    print("\n2. 某些模块不能重新加载")
    print("   - C扩展模块")
    print("   - 内置模块")
    print("   - 某些系统模块")
    
    print("\n3. 重新加载可能导致问题")
    print("   - 状态不一致")
    print("   - 内存泄漏")
    print("   - 引用混乱")
    
    print("\n4. 不会重新加载依赖模块")
    print("   - 只重新加载指定的模块")
    print("   - 依赖的其他模块保持不变")
    
    # 演示不能重新加载的模块
    print("\n尝试重新加载内置模块：")
    try:
        importlib.reload(sys)
        print("sys模块重新加载成功")
    except TypeError as e:
        print(f"sys模块重新加载失败: {e}")
    
    try:
        importlib.reload(os)
        print("os模块重新加载成功")
    except Exception as e:
        print(f"os模块重新加载失败: {e}")

# ============================================================================
# 5. 实际应用场景
# ============================================================================

def demonstrate_practical_usage():
    """
    演示重新加载的实际应用场景
    """
    print("\n=== 5. 实际应用场景 ===")
    
    print("模块重新加载的实际用途：")
    
    print("\n1. 开发和调试")
    print("   - 在交互式环境中测试代码修改")
    print("   - 避免重启整个应用程序")
    print("   - 快速迭代开发")
    
    print("\n2. 配置文件重新加载")
    print("   - 动态更新应用配置")
    print("   - 不停机更新设置")
    
    print("\n3. 插件系统")
    print("   - 动态加载和卸载插件")
    print("   - 热更新功能模块")
    
    print("\n4. 长运行服务")
    print("   - 在不重启服务的情况下更新代码")
    print("   - 减少服务中断时间")
    
    # 演示配置重新加载的例子
    print("\n配置重新加载示例：")
    
    # 创建配置文件
    config_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
应用配置文件
"""

# 应用配置
APP_CONFIG = {
    'debug': True,
    'port': 8080,
    'host': 'localhost',
    'version': '1.0.0'
}

# 数据库配置
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'myapp'
}

def get_config():
    return {
        'app': APP_CONFIG,
        'database': DB_CONFIG
    }
'''
    
    config_file = "app_config.py"
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(config_content)
        print(f"创建配置文件: {config_file}")
        
        # 导入配置
        import app_config
        print(f"初始配置: {app_config.get_config()}")
        
        # 模拟配置更新
        time.sleep(0.5)
        modified_config = config_content.replace("'debug': True", "'debug': False")
        modified_config = modified_config.replace("'port': 8080", "'port': 9000")
        
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(modified_config)
        
        print("\n配置文件已更新")
        
        # 重新加载配置
        importlib.reload(app_config)
        print(f"重新加载后的配置: {app_config.get_config()}")
        
    except Exception as e:
        print(f"配置重新加载示例失败: {e}")

# ============================================================================
# 6. 高级重新加载技术
# ============================================================================

def demonstrate_advanced_reload():
    """
    演示高级重新加载技术
    """
    print("\n=== 6. 高级重新加载技术 ===")
    
    print("高级重新加载技术：")
    
    print("\n1. 递归重新加载")
    print("   - 重新加载模块及其依赖")
    print("   - 需要手动管理依赖关系")
    
    print("\n2. 智能重新加载")
    print("   - 检测文件修改时间")
    print("   - 自动重新加载修改的模块")
    
    print("\n3. 状态保持重新加载")
    print("   - 保存重要状态")
    print("   - 重新加载后恢复状态")
    
    # 演示文件监控重新加载
    def auto_reload_on_change(module_name, file_path, check_interval=1):
        """
        监控文件变化并自动重新加载模块
        """
        if not os.path.exists(file_path):
            return
        
        last_modified = os.path.getmtime(file_path)
        
        def check_and_reload():
            nonlocal last_modified
            current_modified = os.path.getmtime(file_path)
            
            if current_modified > last_modified:
                print(f"检测到文件变化，重新加载 {module_name}")
                try:
                    if module_name in sys.modules:
                        importlib.reload(sys.modules[module_name])
                        last_modified = current_modified
                        return True
                except Exception as e:
                    print(f"重新加载失败: {e}")
            return False
        
        return check_and_reload
    
    print("\n文件监控重新加载示例：")
    if os.path.exists("reloadable_module.py"):
        checker = auto_reload_on_change("reloadable_module", "reloadable_module.py")
        print("创建文件监控器（实际应用中会在后台运行）")
        print("调用checker()可检查文件是否需要重新加载")

# ============================================================================
# 7. 最佳实践和建议
# ============================================================================

def show_best_practices():
    """
    显示重新加载的最佳实践
    """
    print("\n=== 7. 最佳实践和建议 ===")
    
    practices = [
        "1. 仅在开发和调试时使用重新加载",
        "2. 生产环境避免使用重新加载",
        "3. 重新加载前保存重要状态",
        "4. 注意处理已存在的对象引用",
        "5. 测试重新加载后的功能完整性",
        "6. 使用版本控制跟踪模块变化",
        "7. 考虑使用热重载框架",
        "8. 文档化重新加载的副作用",
        "9. 提供重新加载的回滚机制",
        "10. 监控重新加载的性能影响"
    ]
    
    for practice in practices:
        print(f"  {practice}")
    
    print("\n替代方案：")
    print("  - 使用自动重启工具（如nodemon的Python版本）")
    print("  - 使用开发服务器的热重载功能")
    print("  - 使用容器化部署快速重启")
    print("  - 使用微服务架构减少重启影响")

# ============================================================================
# 8. 清理函数
# ============================================================================

def cleanup_demo_files():
    """
    清理演示文件
    """
    print("\n=== 8. 清理演示文件 ===")
    
    files_to_clean = [
        "reloadable_module.py",
        "app_config.py"
    ]
    
    for file_name in files_to_clean:
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
                print(f"清理文件: {file_name}")
        except Exception as e:
            print(f"清理文件 {file_name} 时出错: {e}")
    
    # 从sys.modules中移除演示模块
    modules_to_remove = []
    for module_name in sys.modules:
        if module_name in ['reloadable_module', 'app_config']:
            modules_to_remove.append(module_name)
    
    for module_name in modules_to_remove:
        try:
            del sys.modules[module_name]
            print(f"从缓存中移除模块: {module_name}")
        except KeyError:
            pass

# ============================================================================
# 主函数
# ============================================================================

def main():
    """
    主函数：演示所有模块重新加载相关功能
    """
    print("Python模块重新加载演示")
    print("=" * 60)
    
    try:
        demonstrate_module_caching()
        
        module_file = create_reloadable_module()
        if module_file:
            demonstrate_module_reload(module_file)
        
        demonstrate_reload_limitations()
        demonstrate_practical_usage()
        demonstrate_advanced_reload()
        show_best_practices()
        
    finally:
        # 确保清理演示文件
        cleanup_demo_files()
    
    print("\n" + "=" * 60)
    print("模块重新加载演示完成！")
    print("=" * 60)

if __name__ == '__main__':
    main()