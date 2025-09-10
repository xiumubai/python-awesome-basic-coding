#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置模块 - 用于演示模块配置和常量管理

这个模块包含应用程序的配置信息、常量定义和环境设置，
演示了如何在模块中管理配置数据。

Author: Python学习者
Version: 1.0.0
Date: 2024
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional

# 模块信息
MODULE_NAME = "config"
MODULE_VERSION = "1.0.0"

print(f"配置模块 {MODULE_NAME} v{MODULE_VERSION} 已加载")

# ============================================================================
# 应用程序常量
# ============================================================================

# 应用程序基本信息
APP_NAME = "Python学习系统"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Python学习者"
APP_EMAIL = "learner@python.org"
APP_DESCRIPTION = "用于学习Python模块系统的示例应用程序"

# 文件和路径常量
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
CONFIG_DIR = BASE_DIR / "config"
TEMP_DIR = BASE_DIR / "temp"

# 文件扩展名
SUPPORTED_FILE_EXTENSIONS = {
    'text': ['.txt', '.md', '.rst'],
    'data': ['.json', '.csv', '.xml', '.yaml'],
    'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'document': ['.pdf', '.doc', '.docx', '.xls', '.xlsx']
}

# 默认文件名
DEFAULT_CONFIG_FILE = "app_config.json"
DEFAULT_LOG_FILE = "app.log"
DEFAULT_DATA_FILE = "data.json"

# ============================================================================
# 数据库配置常量
# ============================================================================

# 数据库类型
DATABASE_TYPES = {
    'SQLITE': 'sqlite',
    'MYSQL': 'mysql',
    'POSTGRESQL': 'postgresql',
    'MONGODB': 'mongodb'
}

# 默认数据库配置
DEFAULT_DATABASE_CONFIG = {
    'type': DATABASE_TYPES['SQLITE'],
    'name': 'app_database.db',
    'host': 'localhost',
    'port': 5432,
    'username': 'user',
    'password': 'password',
    'charset': 'utf8mb4',
    'timeout': 30
}

# 连接池配置
CONNECTION_POOL_CONFIG = {
    'min_connections': 1,
    'max_connections': 10,
    'pool_timeout': 30,
    'pool_recycle': 3600
}

# ============================================================================
# 网络和API配置常量
# ============================================================================

# HTTP状态码
HTTP_STATUS_CODES = {
    'OK': 200,
    'CREATED': 201,
    'BAD_REQUEST': 400,
    'UNAUTHORIZED': 401,
    'FORBIDDEN': 403,
    'NOT_FOUND': 404,
    'INTERNAL_SERVER_ERROR': 500
}

# API配置
API_CONFIG = {
    'base_url': 'https://api.example.com',
    'version': 'v1',
    'timeout': 30,
    'max_retries': 3,
    'retry_delay': 1,
    'rate_limit': 100  # 每分钟请求数
}

# 请求头
DEFAULT_HEADERS = {
    'User-Agent': f'{APP_NAME}/{APP_VERSION}',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# ============================================================================
# 日志配置常量
# ============================================================================

# 日志级别
LOG_LEVELS = {
    'DEBUG': 10,
    'INFO': 20,
    'WARNING': 30,
    'ERROR': 40,
    'CRITICAL': 50
}

# 日志格式
LOG_FORMATS = {
    'simple': '%(levelname)s - %(message)s',
    'detailed': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'verbose': '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
}

# 默认日志配置
DEFAULT_LOG_CONFIG = {
    'level': LOG_LEVELS['INFO'],
    'format': LOG_FORMATS['detailed'],
    'file': DEFAULT_LOG_FILE,
    'max_size': 10 * 1024 * 1024,  # 10MB
    'backup_count': 5,
    'encoding': 'utf-8'
}

# ============================================================================
# 缓存配置常量
# ============================================================================

# 缓存类型
CACHE_TYPES = {
    'MEMORY': 'memory',
    'REDIS': 'redis',
    'MEMCACHED': 'memcached',
    'FILE': 'file'
}

# 默认缓存配置
DEFAULT_CACHE_CONFIG = {
    'type': CACHE_TYPES['MEMORY'],
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'password': None,
    'default_timeout': 300,  # 5分钟
    'max_entries': 1000
}

# 缓存键前缀
CACHE_KEY_PREFIXES = {
    'user': 'user:',
    'session': 'session:',
    'data': 'data:',
    'temp': 'temp:'
}

# ============================================================================
# 安全配置常量
# ============================================================================

# 密码策略
PASSWORD_POLICY = {
    'min_length': 8,
    'max_length': 128,
    'require_uppercase': True,
    'require_lowercase': True,
    'require_digits': True,
    'require_special_chars': True,
    'special_chars': '!@#$%^&*()_+-=[]{}|;:,.<>?'
}

# 会话配置
SESSION_CONFIG = {
    'timeout': 3600,  # 1小时
    'cookie_name': 'session_id',
    'cookie_secure': True,
    'cookie_httponly': True,
    'cookie_samesite': 'Strict'
}

# 加密配置
ENCRYPTION_CONFIG = {
    'algorithm': 'AES-256-GCM',
    'key_size': 32,
    'iv_size': 16,
    'salt_size': 16,
    'iterations': 100000
}

# ============================================================================
# 环境配置类
# ============================================================================

class Environment:
    """
    环境配置类
    
    用于管理不同环境（开发、测试、生产）的配置。
    """
    
    DEVELOPMENT = 'development'
    TESTING = 'testing'
    PRODUCTION = 'production'
    
    @classmethod
    def get_all_environments(cls) -> list:
        """
        获取所有可用的环境
        
        Returns:
            list: 环境列表
        """
        return [cls.DEVELOPMENT, cls.TESTING, cls.PRODUCTION]
    
    @classmethod
    def is_valid_environment(cls, env: str) -> bool:
        """
        检查环境是否有效
        
        Args:
            env (str): 环境名称
        
        Returns:
            bool: 是否有效
        """
        return env in cls.get_all_environments()

# ============================================================================
# 配置管理类
# ============================================================================

class ConfigManager:
    """
    配置管理器
    
    用于加载、保存和管理应用程序配置。
    """
    
    def __init__(self, config_file: Optional[str] = None):
        """
        初始化配置管理器
        
        Args:
            config_file (Optional[str]): 配置文件路径
        """
        self.config_file = config_file or (CONFIG_DIR / DEFAULT_CONFIG_FILE)
        self.config_data = {}
        self.environment = Environment.DEVELOPMENT
        self._load_default_config()
    
    def _load_default_config(self) -> None:
        """
        加载默认配置
        """
        self.config_data = {
            'app': {
                'name': APP_NAME,
                'version': APP_VERSION,
                'author': APP_AUTHOR,
                'email': APP_EMAIL,
                'description': APP_DESCRIPTION
            },
            'database': DEFAULT_DATABASE_CONFIG.copy(),
            'api': API_CONFIG.copy(),
            'logging': DEFAULT_LOG_CONFIG.copy(),
            'cache': DEFAULT_CACHE_CONFIG.copy(),
            'security': {
                'password_policy': PASSWORD_POLICY.copy(),
                'session': SESSION_CONFIG.copy(),
                'encryption': ENCRYPTION_CONFIG.copy()
            },
            'paths': {
                'base_dir': str(BASE_DIR),
                'data_dir': str(DATA_DIR),
                'log_dir': str(LOG_DIR),
                'config_dir': str(CONFIG_DIR),
                'temp_dir': str(TEMP_DIR)
            }
        }
    
    def load_from_file(self, file_path: Optional[str] = None) -> bool:
        """
        从文件加载配置
        
        Args:
            file_path (Optional[str]): 配置文件路径
        
        Returns:
            bool: 是否加载成功
        """
        file_path = file_path or self.config_file
        
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    loaded_config = json.load(f)
                    self.config_data.update(loaded_config)
                print(f"配置已从 {file_path} 加载")
                return True
            else:
                print(f"配置文件 {file_path} 不存在，使用默认配置")
                return False
        except Exception as e:
            print(f"加载配置文件失败: {e}")
            return False
    
    def save_to_file(self, file_path: Optional[str] = None) -> bool:
        """
        保存配置到文件
        
        Args:
            file_path (Optional[str]): 配置文件路径
        
        Returns:
            bool: 是否保存成功
        """
        file_path = file_path or self.config_file
        
        try:
            # 确保目录存在
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.config_data, f, indent=2, ensure_ascii=False)
            print(f"配置已保存到 {file_path}")
            return True
        except Exception as e:
            print(f"保存配置文件失败: {e}")
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        获取配置值
        
        Args:
            key (str): 配置键（支持点号分隔的嵌套键）
            default (Any): 默认值
        
        Returns:
            Any: 配置值
        
        Example:
            >>> config = ConfigManager()
            >>> config.get('app.name')
            'Python学习系统'
        """
        keys = key.split('.')
        value = self.config_data
        
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key: str, value: Any) -> None:
        """
        设置配置值
        
        Args:
            key (str): 配置键（支持点号分隔的嵌套键）
            value (Any): 配置值
        
        Example:
            >>> config = ConfigManager()
            >>> config.set('app.debug', True)
        """
        keys = key.split('.')
        data = self.config_data
        
        # 创建嵌套字典结构
        for k in keys[:-1]:
            if k not in data or not isinstance(data[k], dict):
                data[k] = {}
            data = data[k]
        
        data[keys[-1]] = value
    
    def has(self, key: str) -> bool:
        """
        检查配置键是否存在
        
        Args:
            key (str): 配置键
        
        Returns:
            bool: 是否存在
        
        Example:
            >>> config = ConfigManager()
            >>> config.has('app.name')
            True
        """
        return self.get(key) is not None
    
    def remove(self, key: str) -> bool:
        """
        删除配置键
        
        Args:
            key (str): 配置键
        
        Returns:
            bool: 是否删除成功
        
        Example:
            >>> config = ConfigManager()
            >>> config.remove('app.debug')
            True
        """
        keys = key.split('.')
        data = self.config_data
        
        try:
            # 导航到父级字典
            for k in keys[:-1]:
                data = data[k]
            
            # 删除最后一个键
            if keys[-1] in data:
                del data[keys[-1]]
                return True
            return False
        except (KeyError, TypeError):
            return False
    
    def get_section(self, section: str) -> Dict[str, Any]:
        """
        获取配置节
        
        Args:
            section (str): 节名称
        
        Returns:
            Dict[str, Any]: 配置节数据
        
        Example:
            >>> config = ConfigManager()
            >>> app_config = config.get_section('app')
        """
        return self.get(section, {})
    
    def set_environment(self, env: str) -> bool:
        """
        设置环境
        
        Args:
            env (str): 环境名称
        
        Returns:
            bool: 是否设置成功
        
        Example:
            >>> config = ConfigManager()
            >>> config.set_environment('production')
            True
        """
        if Environment.is_valid_environment(env):
            self.environment = env
            self.set('environment', env)
            print(f"环境已设置为: {env}")
            return True
        else:
            print(f"无效的环境: {env}")
            return False
    
    def get_environment(self) -> str:
        """
        获取当前环境
        
        Returns:
            str: 当前环境
        
        Example:
            >>> config = ConfigManager()
            >>> config.get_environment()
            'development'
        """
        return self.environment
    
    def is_development(self) -> bool:
        """
        是否为开发环境
        
        Returns:
            bool: 是否为开发环境
        """
        return self.environment == Environment.DEVELOPMENT
    
    def is_testing(self) -> bool:
        """
        是否为测试环境
        
        Returns:
            bool: 是否为测试环境
        """
        return self.environment == Environment.TESTING
    
    def is_production(self) -> bool:
        """
        是否为生产环境
        
        Returns:
            bool: 是否为生产环境
        """
        return self.environment == Environment.PRODUCTION
    
    def get_all_config(self) -> Dict[str, Any]:
        """
        获取所有配置
        
        Returns:
            Dict[str, Any]: 所有配置数据
        
        Example:
            >>> config = ConfigManager()
            >>> all_config = config.get_all_config()
        """
        return self.config_data.copy()
    
    def print_config(self, section: Optional[str] = None) -> None:
        """
        打印配置信息
        
        Args:
            section (Optional[str]): 要打印的节，None表示打印所有
        
        Example:
            >>> config = ConfigManager()
            >>> config.print_config('app')
        """
        if section:
            data = self.get_section(section)
            print(f"\n=== {section} 配置 ===")
        else:
            data = self.config_data
            print(f"\n=== 所有配置 ===")
        
        self._print_dict(data, indent=0)
        print("=" * 40)
    
    def _print_dict(self, data: Dict[str, Any], indent: int = 0) -> None:
        """
        递归打印字典（私有方法）
        
        Args:
            data (Dict[str, Any]): 要打印的字典
            indent (int): 缩进级别
        """
        for key, value in data.items():
            if isinstance(value, dict):
                print("  " * indent + f"{key}:")
                self._print_dict(value, indent + 1)
            else:
                print("  " * indent + f"{key}: {value}")

# ============================================================================
# 模块级别的函数
# ============================================================================

def get_app_info() -> Dict[str, str]:
    """
    获取应用程序信息
    
    Returns:
        Dict[str, str]: 应用程序信息
    
    Example:
        >>> info = get_app_info()
        >>> info['name']
        'Python学习系统'
    """
    return {
        'name': APP_NAME,
        'version': APP_VERSION,
        'author': APP_AUTHOR,
        'email': APP_EMAIL,
        'description': APP_DESCRIPTION
    }

def get_default_paths() -> Dict[str, str]:
    """
    获取默认路径配置
    
    Returns:
        Dict[str, str]: 路径配置
    
    Example:
        >>> paths = get_default_paths()
        >>> 'base_dir' in paths
        True
    """
    return {
        'base_dir': str(BASE_DIR),
        'data_dir': str(DATA_DIR),
        'log_dir': str(LOG_DIR),
        'config_dir': str(CONFIG_DIR),
        'temp_dir': str(TEMP_DIR)
    }

def create_default_directories() -> None:
    """
    创建默认目录结构
    
    Example:
        >>> create_default_directories()
    """
    directories = [DATA_DIR, LOG_DIR, CONFIG_DIR, TEMP_DIR]
    
    for directory in directories:
        try:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"目录已创建: {directory}")
        except Exception as e:
            print(f"创建目录失败 {directory}: {e}")

def get_environment_from_os() -> str:
    """
    从环境变量获取环境设置
    
    Returns:
        str: 环境名称
    
    Example:
        >>> env = get_environment_from_os()
        >>> env in ['development', 'testing', 'production']
        True
    """
    env = os.getenv('PYTHON_ENV', Environment.DEVELOPMENT).lower()
    
    if Environment.is_valid_environment(env):
        return env
    else:
        print(f"无效的环境变量值: {env}，使用默认环境: {Environment.DEVELOPMENT}")
        return Environment.DEVELOPMENT

def get_module_info() -> Dict[str, Any]:
    """
    获取模块信息
    
    Returns:
        Dict[str, Any]: 模块信息
    
    Example:
        >>> info = get_module_info()
        >>> info['name']
        'config'
    """
    return {
        'name': MODULE_NAME,
        'version': MODULE_VERSION,
        'app_info': get_app_info(),
        'default_paths': get_default_paths(),
        'supported_environments': Environment.get_all_environments(),
        'current_environment': get_environment_from_os(),
        'constants': {
            'database_types': list(DATABASE_TYPES.values()),
            'cache_types': list(CACHE_TYPES.values()),
            'log_levels': list(LOG_LEVELS.keys()),
            'http_status_codes': len(HTTP_STATUS_CODES)
        }
    }

def print_module_info() -> None:
    """
    打印模块信息
    
    Example:
        >>> print_module_info()
    """
    info = get_module_info()
    print(f"\n=== {info['name']} 模块信息 ===")
    print(f"版本: {info['version']}")
    print(f"应用程序: {info['app_info']['name']} v{info['app_info']['version']}")
    print(f"当前环境: {info['current_environment']}")
    print(f"支持的环境: {', '.join(info['supported_environments'])}")
    print(f"数据库类型: {', '.join(info['constants']['database_types'])}")
    print(f"缓存类型: {', '.join(info['constants']['cache_types'])}")
    print(f"日志级别: {', '.join(info['constants']['log_levels'])}")
    print("=" * 40)

# ============================================================================
# 全局配置实例
# ============================================================================

# 创建全局配置管理器实例
config = ConfigManager()

# 从环境变量设置环境
config.set_environment(get_environment_from_os())

# ============================================================================
# 模块级别的测试代码
# ============================================================================

if __name__ == '__main__':
    print("\n=== 配置模块测试 ===")
    
    # 测试应用程序信息
    print("\n1. 应用程序信息测试：")
    app_info = get_app_info()
    for key, value in app_info.items():
        print(f"  {key}: {value}")
    
    # 测试路径配置
    print("\n2. 路径配置测试：")
    paths = get_default_paths()
    for key, value in paths.items():
        print(f"  {key}: {value}")
    
    # 测试环境配置
    print("\n3. 环境配置测试：")
    print(f"所有环境: {Environment.get_all_environments()}")
    print(f"当前环境: {get_environment_from_os()}")
    print(f"是否为开发环境: {Environment.DEVELOPMENT == get_environment_from_os()}")
    
    # 测试配置管理器
    print("\n4. 配置管理器测试：")
    test_config = ConfigManager()
    
    # 设置和获取配置
    test_config.set('test.value', 42)
    test_config.set('test.name', '测试配置')
    print(f"test.value: {test_config.get('test.value')}")
    print(f"test.name: {test_config.get('test.name')}")
    print(f"不存在的键: {test_config.get('not.exist', '默认值')}")
    
    # 测试配置节
    print(f"\n5. 配置节测试：")
    app_section = test_config.get_section('app')
    print(f"应用程序名称: {app_section.get('name')}")
    print(f"应用程序版本: {app_section.get('version')}")
    
    # 测试环境设置
    print("\n6. 环境设置测试：")
    print(f"设置测试环境: {test_config.set_environment('testing')}")
    print(f"当前环境: {test_config.get_environment()}")
    print(f"是否为测试环境: {test_config.is_testing()}")
    
    # 测试常量
    print("\n7. 常量测试：")
    print(f"数据库类型: {list(DATABASE_TYPES.values())}")
    print(f"HTTP状态码数量: {len(HTTP_STATUS_CODES)}")
    print(f"日志级别: {list(LOG_LEVELS.keys())}")
    
    # 显示模块信息
    print("\n8. 模块信息：")
    print_module_info()
    
    # 打印部分配置
    print("\n9. 配置信息：")
    test_config.print_config('app')
    
    print("\n=== 测试完成 ===")