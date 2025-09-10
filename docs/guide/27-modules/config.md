# 辅助模块：config.py

## 模块概述

`config.py` 是一个配置管理模块，演示了如何在Python中管理应用程序配置、常量定义和环境设置。该模块包含了应用程序常量、各种配置类、配置管理器以及环境相关的配置，展示了配置模块的设计模式和最佳实践。

## 模块结构

### 模块信息和应用程序常量

```python
"""配置模块 - 管理应用程序配置和常量。

这个模块包含了应用程序的所有配置信息，包括数据库配置、
网络设置、日志配置等。支持多环境配置和动态配置管理。

Example:
    基本使用：
        from config import app_config, DATABASE_CONFIG
        db_host = DATABASE_CONFIG['host']
        app_name = app_config.get('app_name')

Author: Python学习者
Version: 1.0.0
Date: 2024
"""

# 模块信息
__version__ = "1.0.0"
__author__ = "Python学习者"
__email__ = "learner@python.org"
__status__ = "Development"

# 应用程序基本常量
APP_NAME = "Python学习应用"
APP_VERSION = "2.0.0"
APP_DESCRIPTION = "用于学习Python模块开发的示例应用"
APP_AUTHOR = "Python学习者"

# 路径常量
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
LOG_DIR = os.path.join(BASE_DIR, 'logs')
CONFIG_DIR = os.path.join(BASE_DIR, 'config')
TEMP_DIR = os.path.join(BASE_DIR, 'temp')

# 文件扩展名常量
ALLOWED_EXTENSIONS = {'.txt', '.csv', '.json', '.xml', '.yaml'}
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
DOCUMENT_EXTENSIONS = {'.pdf', '.doc', '.docx', '.xls', '.xlsx'}

# 数值常量
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50MB
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100
SESSION_TIMEOUT = 3600  # 1小时

# 状态常量
STATUS_ACTIVE = 'active'
STATUS_INACTIVE = 'inactive'
STATUS_PENDING = 'pending'
STATUS_DELETED = 'deleted'

VALID_STATUSES = {STATUS_ACTIVE, STATUS_INACTIVE, STATUS_PENDING, STATUS_DELETED}

# 优先级常量
PRIORITY_LOW = 1
PRIORITY_MEDIUM = 2
PRIORITY_HIGH = 3
PRIORITY_URGENT = 4

PRIORITY_NAMES = {
    PRIORITY_LOW: '低',
    PRIORITY_MEDIUM: '中',
    PRIORITY_HIGH: '高',
    PRIORITY_URGENT: '紧急'
}
```

### 数据库配置

```python
# 数据库配置
DATABASE_CONFIG = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': os.path.join(DATA_DIR, 'app.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'timeout': 20,
            'check_same_thread': False,
        }
    },
    'mysql': {
        'ENGINE': 'mysql',
        'NAME': 'python_learning',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    },
    'postgresql': {
        'ENGINE': 'postgresql',
        'NAME': 'python_learning',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'prefer',
        }
    }
}

# 数据库连接池配置
DATABASE_POOL_CONFIG = {
    'pool_size': 5,
    'max_overflow': 10,
    'pool_timeout': 30,
    'pool_recycle': 3600,
    'pool_pre_ping': True
}
```

### 网络和API配置

```python
# 网络配置
NETWORK_CONFIG = {
    'host': '0.0.0.0',
    'port': 8000,
    'debug': True,
    'reload': True,
    'workers': 1,
    'timeout': 30,
    'keep_alive': 2,
    'max_requests': 1000,
    'max_requests_jitter': 100
}

# API配置
API_CONFIG = {
    'version': 'v1',
    'prefix': '/api',
    'title': 'Python学习API',
    'description': 'Python模块学习的API接口',
    'contact': {
        'name': 'Python学习者',
        'email': 'learner@python.org'
    },
    'license': {
        'name': 'MIT',
        'url': 'https://opensource.org/licenses/MIT'
    }
}

# 外部API配置
EXTERNAL_APIS = {
    'weather': {
        'base_url': 'https://api.openweathermap.org/data/2.5',
        'api_key': 'your_weather_api_key',
        'timeout': 10,
        'retries': 3
    },
    'geocoding': {
        'base_url': 'https://api.mapbox.com/geocoding/v5',
        'api_key': 'your_mapbox_api_key',
        'timeout': 5,
        'retries': 2
    }
}

# HTTP配置
HTTP_CONFIG = {
    'user_agent': f'{APP_NAME}/{APP_VERSION}',
    'timeout': 30,
    'max_retries': 3,
    'backoff_factor': 0.3,
    'status_forcelist': [500, 502, 504],
    'headers': {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
}
```

### 日志配置

```python
# 日志配置
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'detailed': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': os.path.join(LOG_DIR, 'app.log'),
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
            'encoding': 'utf8'
        },
        'error_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'detailed',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'maxBytes': 10485760,  # 10MB
            'backupCount': 3,
            'encoding': 'utf8'
        }
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'app': {
            'handlers': ['console', 'file', 'error_file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'requests': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False
        }
    }
}

# 日志级别映射
LOG_LEVELS = {
    'DEBUG': 10,
    'INFO': 20,
    'WARNING': 30,
    'ERROR': 40,
    'CRITICAL': 50
}
```

### 缓存配置

```python
# 缓存配置
CACHE_CONFIG = {
    'default': {
        'BACKEND': 'memory',
        'LOCATION': 'default',
        'TIMEOUT': 300,  # 5分钟
        'OPTIONS': {
            'MAX_ENTRIES': 1000,
            'CULL_FREQUENCY': 3
        }
    },
    'redis': {
        'BACKEND': 'redis',
        'LOCATION': 'redis://localhost:6379/1',
        'TIMEOUT': 3600,  # 1小时
        'OPTIONS': {
            'CLIENT_CLASS': 'redis.client.Redis',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 50,
                'retry_on_timeout': True
            }
        }
    },
    'memcached': {
        'BACKEND': 'memcached',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 1800,  # 30分钟
        'OPTIONS': {
            'server_max_value_length': 1024*1024*2,  # 2MB
        }
    }
}

# 缓存键前缀
CACHE_KEY_PREFIX = 'python_learning'
CACHE_VERSION = 1

# 缓存超时设置
CACHE_TIMEOUTS = {
    'short': 300,      # 5分钟
    'medium': 1800,    # 30分钟
    'long': 3600,      # 1小时
    'very_long': 86400 # 1天
}
```

### 安全配置

```python
# 安全配置
SECURITY_CONFIG = {
    'secret_key': 'your-secret-key-change-in-production',
    'algorithm': 'HS256',
    'access_token_expire_minutes': 30,
    'refresh_token_expire_days': 7,
    'password_min_length': 8,
    'password_require_uppercase': True,
    'password_require_lowercase': True,
    'password_require_numbers': True,
    'password_require_symbols': False,
    'max_login_attempts': 5,
    'lockout_duration': 900,  # 15分钟
    'session_cookie_secure': True,
    'session_cookie_httponly': True,
    'session_cookie_samesite': 'Lax'
}

# 加密配置
ENCRYPTION_CONFIG = {
    'algorithm': 'AES-256-GCM',
    'key_derivation': 'PBKDF2',
    'iterations': 100000,
    'salt_length': 32,
    'iv_length': 12
}

# CORS配置
CORS_CONFIG = {
    'allow_origins': ['http://localhost:3000', 'http://localhost:8080'],
    'allow_methods': ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    'allow_headers': ['*'],
    'allow_credentials': True,
    'max_age': 86400
}
```

### 环境配置类

```python
class EnvironmentConfig:
    """环境配置基类。
    
    定义不同环境下的配置参数。
    
    Attributes:
        DEBUG (bool): 调试模式
        TESTING (bool): 测试模式
        DATABASE_URL (str): 数据库连接URL
        LOG_LEVEL (str): 日志级别
    """
    
    DEBUG = False
    TESTING = False
    DATABASE_URL = DATABASE_CONFIG['default']
    LOG_LEVEL = 'INFO'
    CACHE_TYPE = 'default'
    
    @classmethod
    def get_config(cls):
        """获取配置字典。
        
        Returns:
            dict: 配置参数字典
        """
        config = {}
        for key in dir(cls):
            if not key.startswith('_') and not callable(getattr(cls, key)):
                config[key] = getattr(cls, key)
        return config
    
    @classmethod
    def validate_config(cls):
        """验证配置的有效性。
        
        Returns:
            bool: 配置是否有效
        
        Raises:
            ValueError: 当配置无效时
        """
        # 基本验证逻辑
        if not isinstance(cls.DEBUG, bool):
            raise ValueError("DEBUG必须是布尔值")
        
        if not isinstance(cls.TESTING, bool):
            raise ValueError("TESTING必须是布尔值")
        
        if cls.LOG_LEVEL not in LOG_LEVELS:
            raise ValueError(f"LOG_LEVEL必须是以下值之一: {list(LOG_LEVELS.keys())}")
        
        return True

class DevelopmentConfig(EnvironmentConfig):
    """开发环境配置。
    
    用于本地开发的配置参数。
    """
    
    DEBUG = True
    TESTING = False
    DATABASE_URL = DATABASE_CONFIG['default']
    LOG_LEVEL = 'DEBUG'
    CACHE_TYPE = 'default'
    
    # 开发环境特定配置
    AUTO_RELOAD = True
    SHOW_SQL = True
    PROFILING = True

class TestingConfig(EnvironmentConfig):
    """测试环境配置。
    
    用于单元测试和集成测试的配置参数。
    """
    
    DEBUG = True
    TESTING = True
    DATABASE_URL = ':memory:'  # 内存数据库
    LOG_LEVEL = 'WARNING'
    CACHE_TYPE = 'default'
    
    # 测试环境特定配置
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(EnvironmentConfig):
    """生产环境配置。
    
    用于生产部署的配置参数。
    """
    
    DEBUG = False
    TESTING = False
    DATABASE_URL = DATABASE_CONFIG['postgresql']
    LOG_LEVEL = 'INFO'
    CACHE_TYPE = 'redis'
    
    # 生产环境特定配置
    SSL_REQUIRED = True
    SESSION_COOKIE_SECURE = True
    PERMANENT_SESSION_LIFETIME = 1800  # 30分钟

class StagingConfig(EnvironmentConfig):
    """预发布环境配置。
    
    用于预发布测试的配置参数。
    """
    
    DEBUG = False
    TESTING = False
    DATABASE_URL = DATABASE_CONFIG['mysql']
    LOG_LEVEL = 'INFO'
    CACHE_TYPE = 'memcached'
    
    # 预发布环境特定配置
    SIMULATE_PRODUCTION = True
    MONITORING_ENABLED = True

# 环境配置映射
CONFIG_MAP = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
```

### 配置管理类

```python
class ConfigManager:
    """配置管理器。
    
    负责加载、管理和验证应用程序配置。
    
    Attributes:
        _config (dict): 当前配置字典
        _environment (str): 当前环境名称
        _config_class (class): 当前配置类
    
    Example:
        >>> manager = ConfigManager()
        >>> manager.load_config('development')
        >>> debug_mode = manager.get('DEBUG')
        >>> manager.set('CUSTOM_SETTING', 'value')
    """
    
    def __init__(self, environment=None):
        """初始化配置管理器。
        
        Args:
            environment (str, optional): 环境名称，默认为development
        """
        self._config = {}
        self._environment = environment or 'development'
        self._config_class = None
        self._observers = []  # 配置变更观察者
        
        # 自动加载配置
        self.load_config(self._environment)
    
    def load_config(self, environment):
        """加载指定环境的配置。
        
        Args:
            environment (str): 环境名称
        
        Raises:
            ValueError: 当环境名称无效时
        """
        if environment not in CONFIG_MAP:
            raise ValueError(f"未知的环境: {environment}. 可用环境: {list(CONFIG_MAP.keys())}")
        
        self._environment = environment
        self._config_class = CONFIG_MAP[environment]
        
        # 验证配置
        self._config_class.validate_config()
        
        # 加载配置
        self._config = self._config_class.get_config()
        
        # 添加模块级配置
        self._config.update({
            'APP_NAME': APP_NAME,
            'APP_VERSION': APP_VERSION,
            'APP_DESCRIPTION': APP_DESCRIPTION,
            'BASE_DIR': BASE_DIR,
            'DATA_DIR': DATA_DIR,
            'LOG_DIR': LOG_DIR,
            'NETWORK_CONFIG': NETWORK_CONFIG,
            'API_CONFIG': API_CONFIG,
            'LOGGING_CONFIG': LOGGING_CONFIG,
            'CACHE_CONFIG': CACHE_CONFIG,
            'SECURITY_CONFIG': SECURITY_CONFIG
        })
        
        print(f"已加载 {environment} 环境配置")
        
        # 通知观察者
        self._notify_observers('config_loaded', environment)
    
    def get(self, key, default=None):
        """获取配置值。
        
        Args:
            key (str): 配置键名
            default: 默认值
        
        Returns:
            配置值或默认值
        
        Example:
            >>> manager = ConfigManager()
            >>> debug = manager.get('DEBUG', False)
            >>> app_name = manager.get('APP_NAME')
        """
        return self._config.get(key, default)
    
    def set(self, key, value):
        """设置配置值。
        
        Args:
            key (str): 配置键名
            value: 配置值
        
        Example:
            >>> manager = ConfigManager()
            >>> manager.set('CUSTOM_SETTING', 'my_value')
        """
        old_value = self._config.get(key)
        self._config[key] = value
        
        # 通知观察者
        self._notify_observers('config_changed', key, old_value, value)
    
    def update(self, config_dict):
        """批量更新配置。
        
        Args:
            config_dict (dict): 配置字典
        
        Example:
            >>> manager = ConfigManager()
            >>> manager.update({'SETTING1': 'value1', 'SETTING2': 'value2'})
        """
        for key, value in config_dict.items():
            self.set(key, value)
    
    def get_section(self, section_name):
        """获取配置节。
        
        Args:
            section_name (str): 节名称
        
        Returns:
            dict: 配置节字典
        
        Example:
            >>> manager = ConfigManager()
            >>> db_config = manager.get_section('DATABASE_CONFIG')
        """
        return self.get(section_name, {})
    
    def get_environment(self):
        """获取当前环境名称。
        
        Returns:
            str: 环境名称
        """
        return self._environment
    
    def get_all_config(self):
        """获取所有配置。
        
        Returns:
            dict: 完整配置字典的副本
        """
        return self._config.copy()
    
    def add_observer(self, observer):
        """添加配置变更观察者。
        
        Args:
            observer (callable): 观察者函数，接收事件类型和相关参数
        
        Example:
            >>> def config_observer(event_type, *args):
            ...     print(f"配置事件: {event_type}, 参数: {args}")
            >>> manager = ConfigManager()
            >>> manager.add_observer(config_observer)
        """
        if callable(observer):
            self._observers.append(observer)
    
    def remove_observer(self, observer):
        """移除配置变更观察者。
        
        Args:
            observer (callable): 要移除的观察者函数
        """
        if observer in self._observers:
            self._observers.remove(observer)
    
    def _notify_observers(self, event_type, *args):
        """通知所有观察者。
        
        Args:
            event_type (str): 事件类型
            *args: 事件参数
        """
        for observer in self._observers:
            try:
                observer(event_type, *args)
            except Exception as e:
                print(f"观察者通知失败: {e}")
    
    def validate_current_config(self):
        """验证当前配置。
        
        Returns:
            bool: 配置是否有效
        
        Raises:
            ValueError: 当配置无效时
        """
        if self._config_class:
            return self._config_class.validate_config()
        return True
    
    def reload_config(self):
        """重新加载当前环境的配置。
        
        Example:
            >>> manager = ConfigManager()
            >>> manager.reload_config()
        """
        self.load_config(self._environment)
    
    def export_config(self, file_path=None, format='json'):
        """导出配置到文件。
        
        Args:
            file_path (str, optional): 文件路径
            format (str): 导出格式，支持json、yaml
        
        Returns:
            str: 导出的文件路径
        """
        if file_path is None:
            file_path = os.path.join(CONFIG_DIR, f'config_{self._environment}.{format}')
        
        # 确保目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        if format.lower() == 'json':
            import json
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self._config, f, indent=2, ensure_ascii=False, default=str)
        elif format.lower() == 'yaml':
            try:
                import yaml
                with open(file_path, 'w', encoding='utf-8') as f:
                    yaml.dump(self._config, f, default_flow_style=False, allow_unicode=True)
            except ImportError:
                raise ImportError("需要安装PyYAML库来支持YAML格式")
        else:
            raise ValueError(f"不支持的格式: {format}")
        
        print(f"配置已导出到: {file_path}")
        return file_path
    
    def __str__(self):
        """返回配置管理器的字符串表示。
        
        Returns:
            str: 配置管理器信息
        """
        return f"ConfigManager(environment='{self._environment}', config_count={len(self._config)})"
    
    def __repr__(self):
        """返回配置管理器的详细表示。
        
        Returns:
            str: 配置管理器详细信息
        """
        return (f"ConfigManager(environment='{self._environment}', "
                f"config_class={self._config_class.__name__ if self._config_class else None}, "
                f"config_count={len(self._config)})")
```

### 模块级函数和全局配置实例

```python
def get_config(key, default=None):
    """获取全局配置值的便捷函数。
    
    Args:
        key (str): 配置键名
        default: 默认值
    
    Returns:
        配置值或默认值
    
    Example:
        >>> app_name = get_config('APP_NAME')
        >>> debug_mode = get_config('DEBUG', False)
    """
    return app_config.get(key, default)

def set_config(key, value):
    """设置全局配置值的便捷函数。
    
    Args:
        key (str): 配置键名
        value: 配置值
    
    Example:
        >>> set_config('CUSTOM_SETTING', 'my_value')
    """
    app_config.set(key, value)

def get_environment():
    """获取当前环境名称。
    
    Returns:
        str: 环境名称
    
    Example:
        >>> env = get_environment()
        >>> print(f"当前环境: {env}")
    """
    return app_config.get_environment()

def switch_environment(environment):
    """切换到指定环境。
    
    Args:
        environment (str): 目标环境名称
    
    Example:
        >>> switch_environment('production')
        >>> print(f"切换到环境: {get_environment()}")
    """
    app_config.load_config(environment)

def create_directories():
    """创建必要的目录。
    
    创建数据目录、日志目录、配置目录和临时目录。
    
    Example:
        >>> create_directories()
        >>> print("目录创建完成")
    """
    directories = [DATA_DIR, LOG_DIR, CONFIG_DIR, TEMP_DIR]
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"目录已创建或已存在: {directory}")
        except Exception as e:
            print(f"创建目录失败 {directory}: {e}")

def get_database_config(db_type='default'):
    """获取数据库配置。
    
    Args:
        db_type (str): 数据库类型
    
    Returns:
        dict: 数据库配置字典
    
    Example:
        >>> db_config = get_database_config('mysql')
        >>> host = db_config['HOST']
    """
    return DATABASE_CONFIG.get(db_type, DATABASE_CONFIG['default'])

def get_cache_config(cache_type=None):
    """获取缓存配置。
    
    Args:
        cache_type (str, optional): 缓存类型，默认使用当前环境配置
    
    Returns:
        dict: 缓存配置字典
    
    Example:
        >>> cache_config = get_cache_config('redis')
        >>> location = cache_config['LOCATION']
    """
    if cache_type is None:
        cache_type = app_config.get('CACHE_TYPE', 'default')
    
    return CACHE_CONFIG.get(cache_type, CACHE_CONFIG['default'])

def validate_all_configs():
    """验证所有环境配置。
    
    Returns:
        dict: 验证结果字典
    
    Example:
        >>> results = validate_all_configs()
        >>> for env, result in results.items():
        ...     print(f"{env}: {'有效' if result else '无效'}")
    """
    results = {}
    
    for env_name, config_class in CONFIG_MAP.items():
        try:
            config_class.validate_config()
            results[env_name] = True
        except Exception as e:
            results[env_name] = False
            print(f"环境 {env_name} 配置验证失败: {e}")
    
    return results

def print_config_summary():
    """打印配置摘要信息。
    
    Example:
        >>> print_config_summary()
    """
    print(f"\n=== 配置摘要 ===")
    print(f"应用名称: {APP_NAME}")
    print(f"应用版本: {APP_VERSION}")
    print(f"当前环境: {get_environment()}")
    print(f"调试模式: {get_config('DEBUG')}")
    print(f"测试模式: {get_config('TESTING')}")
    print(f"日志级别: {get_config('LOG_LEVEL')}")
    print(f"缓存类型: {get_config('CACHE_TYPE')}")
    print(f"基础目录: {BASE_DIR}")
    print(f"数据目录: {DATA_DIR}")
    print(f"日志目录: {LOG_DIR}")
    print(f"配置数量: {len(app_config.get_all_config())}")
    print()

# 创建全局配置实例
app_config = ConfigManager()

# 模块初始化
print(f"配置模块已加载 - 版本: {__version__}")
print(f"当前环境: {app_config.get_environment()}")

# 创建必要目录
create_directories()
```

## 模块测试代码

### 完整的测试示例

```python
if __name__ == '__main__':
    print("=== 配置模块测试 ===")
    print(f"模块版本: {__version__}")
    print(f"作者: {__author__}")
    print()
    
    try:
        # 1. 应用程序信息测试
        print("1. 应用程序信息:")
        print(f"   应用名称: {APP_NAME}")
        print(f"   应用版本: {APP_VERSION}")
        print(f"   应用描述: {APP_DESCRIPTION}")
        print(f"   应用作者: {APP_AUTHOR}")
        print()
        
        # 2. 路径配置测试
        print("2. 路径配置:")
        print(f"   基础目录: {BASE_DIR}")
        print(f"   数据目录: {DATA_DIR}")
        print(f"   日志目录: {LOG_DIR}")
        print(f"   配置目录: {CONFIG_DIR}")
        print(f"   临时目录: {TEMP_DIR}")
        print()
        
        # 3. 环境配置测试
        print("3. 环境配置测试:")
        for env_name in CONFIG_MAP.keys():
            print(f"   测试 {env_name} 环境...")
            test_manager = ConfigManager(env_name)
            print(f"     调试模式: {test_manager.get('DEBUG')}")
            print(f"     测试模式: {test_manager.get('TESTING')}")
            print(f"     日志级别: {test_manager.get('LOG_LEVEL')}")
            print(f"     缓存类型: {test_manager.get('CACHE_TYPE')}")
        print()
        
        # 4. 配置管理器测试
        print("4. 配置管理器测试:")
        manager = ConfigManager('development')
        print(f"   当前环境: {manager.get_environment()}")
        print(f"   配置数量: {len(manager.get_all_config())}")
        
        # 测试配置获取和设置
        original_debug = manager.get('DEBUG')
        manager.set('DEBUG', not original_debug)
        print(f"   DEBUG值变更: {original_debug} -> {manager.get('DEBUG')}")
        manager.set('DEBUG', original_debug)  # 恢复原值
        
        # 测试配置节获取
        db_config = manager.get_section('DATABASE_CONFIG')
        print(f"   数据库配置类型: {type(db_config).__name__}")
        print()
        
        # 5. 环境设置测试
        print("5. 环境设置测试:")
        print(f"   可用环境: {list(CONFIG_MAP.keys())}")
        print(f"   状态常量: {list(VALID_STATUSES)}")
        print(f"   优先级映射: {PRIORITY_NAMES}")
        print(f"   允许的文件扩展名: {len(ALLOWED_EXTENSIONS)}个")
        print(f"   最大文件大小: {MAX_FILE_SIZE / (1024*1024):.1f}MB")
        print()
        
        # 6. 常量测试
        print("6. 常量测试:")
        print(f"   会话超时: {SESSION_TIMEOUT}秒")
        print(f"   默认页面大小: {DEFAULT_PAGE_SIZE}")
        print(f"   最大页面大小: {MAX_PAGE_SIZE}")
        print(f"   数学常量π: {PI}")
        print(f"   数学常量e: {E}")
        print()
        
        # 7. 配置验证测试
        print("7. 配置验证测试:")
        validation_results = validate_all_configs()
        for env, is_valid in validation_results.items():
            status = "✓ 有效" if is_valid else "✗ 无效"
            print(f"   {env}: {status}")
        print()
        
        # 8. 便捷函数测试
        print("8. 便捷函数测试:")
        app_name = get_config('APP_NAME')
        debug_mode = get_config('DEBUG', False)
        current_env = get_environment()
        
        print(f"   应用名称: {app_name}")
        print(f"   调试模式: {debug_mode}")
        print(f"   当前环境: {current_env}")
        
        # 测试配置设置
        set_config('TEST_SETTING', 'test_value')
        test_value = get_config('TEST_SETTING')
        print(f"   测试设置: {test_value}")
        print()
        
        # 9. 数据库和缓存配置测试
        print("9. 数据库和缓存配置测试:")
        default_db = get_database_config()
        mysql_db = get_database_config('mysql')
        default_cache = get_cache_config()
        redis_cache = get_cache_config('redis')
        
        print(f"   默认数据库引擎: {default_db.get('ENGINE')}")
        print(f"   MySQL数据库名: {mysql_db.get('NAME')}")
        print(f"   默认缓存后端: {default_cache.get('BACKEND')}")
        print(f"   Redis缓存位置: {redis_cache.get('LOCATION')}")
        print()
        
        # 10. 配置摘要
        print("10. 配置摘要:")
        print_config_summary()
        
        # 11. 模块信息
        print("11. 模块信息:")
        print(f"   模块名: {__name__}")
        print(f"   版本: {__version__}")
        print(f"   作者: {__author__}")
        print(f"   邮箱: {__email__}")
        print(f"   状态: {__status__}")
        print(f"   配置管理器: {app_config}")
        
    except Exception as e:
        print(f"测试过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n=== 测试完成 ===")
```

## 使用示例

### 基本使用

```python
# 导入配置模块
from config import app_config, get_config, APP_NAME

# 获取配置值
app_name = get_config('APP_NAME')
debug_mode = get_config('DEBUG')
log_level = get_config('LOG_LEVEL')

print(f"应用: {app_name}")
print(f"调试: {debug_mode}")
print(f"日志级别: {log_level}")

# 获取配置节
db_config = app_config.get_section('DATABASE_CONFIG')
network_config = app_config.get_section('NETWORK_CONFIG')

print(f"数据库配置: {db_config}")
print(f"网络配置: {network_config}")
```

### 环境切换

```python
from config import app_config, switch_environment, get_environment

# 查看当前环境
print(f"当前环境: {get_environment()}")

# 切换到生产环境
switch_environment('production')
print(f"切换后环境: {get_environment()}")

# 查看生产环境配置
print(f"生产环境调试模式: {app_config.get('DEBUG')}")
print(f"生产环境缓存类型: {app_config.get('CACHE_TYPE')}")
```

### 自定义配置管理

```python
from config import ConfigManager, DevelopmentConfig

# 创建自定义配置管理器
custom_manager = ConfigManager('testing')

# 添加自定义配置
custom_manager.set('CUSTOM_API_KEY', 'my-secret-key')
custom_manager.set('CUSTOM_TIMEOUT', 60)

# 批量更新配置
custom_config = {
    'FEATURE_FLAG_A': True,
    'FEATURE_FLAG_B': False,
    'MAX_CONNECTIONS': 100
}
custom_manager.update(custom_config)

# 获取所有配置
all_config = custom_manager.get_all_config()
print(f"配置总数: {len(all_config)}")

# 导出配置
config_file = custom_manager.export_config(format='json')
print(f"配置已导出到: {config_file}")
```

### 配置观察者

```python
from config import app_config

# 定义配置变更观察者
def config_change_handler(event_type, *args):
    if event_type == 'config_changed':
        key, old_value, new_value = args
        print(f"配置变更: {key} 从 {old_value} 变为 {new_value}")
    elif event_type == 'config_loaded':
        environment = args[0]
        print(f"配置已加载: {environment}")

# 添加观察者
app_config.add_observer(config_change_handler)

# 修改配置（会触发观察者）
app_config.set('TEST_SETTING', 'new_value')

# 重新加载配置（会触发观察者）
app_config.reload_config()
```

## 学习要点

1. **配置管理**：如何设计和实现配置管理系统
2. **环境配置**：多环境配置的设计模式
3. **常量定义**：模块级常量的组织和使用
4. **类继承**：配置类的继承结构设计
5. **观察者模式**：配置变更通知机制
6. **文件操作**：配置的导入导出功能
7. **错误处理**：配置验证和异常处理
8. **模块初始化**：模块加载时的初始化逻辑

## 扩展练习

1. **配置加密**：为敏感配置添加加密存储功能
2. **远程配置**：支持从远程服务器加载配置
3. **配置热更新**：实现配置的热更新机制
4. **配置模板**：创建配置模板和生成工具
5. **配置校验**：添加更严格的配置验证规则
6. **配置版本控制**：实现配置的版本管理
7. **配置UI**：创建配置管理的Web界面
8. **配置同步**：多实例间的配置同步机制

这个config模块展示了如何创建一个功能完整的配置管理系统，包含了多环境支持、配置验证、观察者模式等高级特性，是学习Python配置管理和模块设计的优秀示例。