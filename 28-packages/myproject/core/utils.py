
"""核心工具模块"""

import platform
import psutil
import json
from typing import Dict, Any

def get_system_info() -> Dict[str, Any]:
    """获取系统信息"""
    try:
        return {
            'platform': platform.platform(),
            'python_version': platform.python_version(),
            'cpu_count': psutil.cpu_count() if 'psutil' in globals() else 'N/A',
            'memory_total': 'N/A',  # 简化实现
            'disk_usage': 'N/A'     # 简化实现
        }
    except:
        return {
            'platform': platform.platform(),
            'python_version': platform.python_version(),
            'cpu_count': 'N/A',
            'memory_total': 'N/A',
            'disk_usage': 'N/A'
        }

def format_size(bytes_size: int) -> str:
    """格式化文件大小"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.1f} PB"

def validate_config(config: Dict[str, Any]) -> bool:
    """验证配置"""
    required_keys = ['engine_timeout', 'max_connections']
    
    for key in required_keys:
        if key not in config:
            print(f"缺少必需的配置项: {key}")
            return False
    
    if config.get('engine_timeout', 0) <= 0:
        print("engine_timeout必须大于0")
        return False
    
    if config.get('max_connections', 0) <= 0:
        print("max_connections必须大于0")
        return False
    
    return True

def save_config(config: Dict[str, Any], filename: str) -> bool:
    """保存配置到文件"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"保存配置失败: {e}")
        return False

def load_config(filename: str) -> Dict[str, Any]:
    """从文件加载配置"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载配置失败: {e}")
        return {}
