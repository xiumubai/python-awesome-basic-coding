# 09. 异常处理最佳实践

## 学习目标

- 掌握异常处理的设计原则和最佳实践
- 学会构建健壮的异常处理架构
- 理解异常处理的性能考虑和优化策略
- 掌握异常处理的测试方法和策略
- 学会在实际项目中应用异常处理模式
- 理解异常处理与系统设计的关系

## 异常处理设计原则

### 1. 核心设计原则

```python
def demonstrate_exception_design_principles():
    """演示异常处理的核心设计原则"""
    
    import logging
    from abc import ABC, abstractmethod
    from typing import Optional, Dict, Any, List
    from dataclasses import dataclass
    from enum import Enum
    
    # 原则1: 异常层次化设计
    class ApplicationError(Exception):
        """应用程序基础异常类"""
        
        def __init__(self, message: str, error_code: str = None, 
                     context: Dict[str, Any] = None):
            super().__init__(message)
            self.error_code = error_code
            self.context = context or {}
            self.timestamp = datetime.now()
        
        def to_dict(self) -> Dict[str, Any]:
            """转换为字典格式"""
            return {
                'error_type': self.__class__.__name__,
                'message': str(self),
                'error_code': self.error_code,
                'context': self.context,
                'timestamp': self.timestamp.isoformat()
            }
    
    class ValidationError(ApplicationError):
        """验证错误 - 客户端错误"""
        pass
    
    class BusinessError(ApplicationError):
        """业务逻辑错误 - 客户端错误"""
        pass
    
    class InfrastructureError(ApplicationError):
        """基础设施错误 - 服务端错误"""
        pass
    
    class ExternalServiceError(InfrastructureError):
        """外部服务错误"""
        
        def __init__(self, message: str, service_name: str, 
                     status_code: int = None, **kwargs):
            super().__init__(message, **kwargs)
            self.service_name = service_name
            self.status_code = status_code
    
    class DatabaseError(InfrastructureError):
        """数据库错误"""
        
        def __init__(self, message: str, operation: str = None, 
                     table: str = None, **kwargs):
            super().__init__(message, **kwargs)
            self.operation = operation
            self.table = table
    
    # 原则2: 异常处理策略枚举
    class ErrorHandlingStrategy(Enum):
        """错误处理策略"""
        FAIL_FAST = "fail_fast"  # 快速失败
        RETRY = "retry"  # 重试
        FALLBACK = "fallback"  # 降级
        IGNORE = "ignore"  # 忽略
        LOG_AND_CONTINUE = "log_and_continue"  # 记录并继续
    
    @dataclass
    class ErrorPolicy:
        """错误处理策略配置"""
        strategy: ErrorHandlingStrategy
        max_retries: int = 3
        retry_delay: float = 1.0
        fallback_value: Any = None
        should_log: bool = True
        log_level: str = 'error'
    
    # 原则3: 上下文管理器模式
    class ErrorContext:
        """错误上下文管理器"""
        
        def __init__(self, operation: str, policy: ErrorPolicy, 
                     logger: logging.Logger = None):
            self.operation = operation
            self.policy = policy
            self.logger = logger or logging.getLogger(__name__)
            self.attempt = 0
            self.errors = []
        
        def __enter__(self):
            self.attempt += 1
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is None:
                return False  # 没有异常，正常退出
            
            self.errors.append(exc_val)
            
            # 根据策略处理异常
            if self.policy.strategy == ErrorHandlingStrategy.FAIL_FAST:
                return False  # 不抑制异常，快速失败
            
            elif self.policy.strategy == ErrorHandlingStrategy.RETRY:
                if self.attempt < self.policy.max_retries:
                    if self.policy.should_log:
                        self.logger.warning(
                            f"操作 {self.operation} 第 {self.attempt} 次尝试失败: {exc_val}，将重试"
                        )
                    
                    import time
                    time.sleep(self.policy.retry_delay)
                    return True  # 抑制异常，准备重试
                else:
                    if self.policy.should_log:
                        self.logger.error(
                            f"操作 {self.operation} 重试 {self.policy.max_retries} 次后仍然失败"
                        )
                    return False  # 不抑制异常
            
            elif self.policy.strategy == ErrorHandlingStrategy.IGNORE:
                if self.policy.should_log:
                    getattr(self.logger, self.policy.log_level)(
                        f"忽略操作 {self.operation} 的异常: {exc_val}"
                    )
                return True  # 抑制异常
            
            elif self.policy.strategy == ErrorHandlingStrategy.LOG_AND_CONTINUE:
                if self.policy.should_log:
                    getattr(self.logger, self.policy.log_level)(
                        f"操作 {self.operation} 发生异常但继续执行: {exc_val}"
                    )
                return True  # 抑制异常
            
            return False  # 默认不抑制异常
    
    # 原则4: 异常处理装饰器
    def handle_exceptions(policy: ErrorPolicy):
        """异常处理装饰器"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                operation = f"{func.__module__}.{func.__name__}"
                
                while True:
                    with ErrorContext(operation, policy) as ctx:
                        try:
                            return func(*args, **kwargs)
                        except Exception as e:
                            # 让上下文管理器处理异常
                            raise
                    
                    # 如果上下文管理器抑制了异常，检查是否需要重试
                    if policy.strategy != ErrorHandlingStrategy.RETRY or \
                       ctx.attempt >= policy.max_retries:
                        # 如果有降级值，返回降级值
                        if policy.strategy == ErrorHandlingStrategy.FALLBACK:
                            return policy.fallback_value
                        # 否则返回None或抛出最后一个异常
                        if ctx.errors:
                            raise ctx.errors[-1]
                        return None
            
            return wrapper
        return decorator
    
    def demonstrate_design_principles():
        """演示设计原则的应用"""
        
        # 配置日志
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        
        # 示例服务类
        class UserService:
            """用户服务"""
            
            def __init__(self):
                self.logger = logging.getLogger(f'{__name__}.UserService')
                self.failure_count = 0
            
            @handle_exceptions(ErrorPolicy(
                strategy=ErrorHandlingStrategy.RETRY,
                max_retries=3,
                retry_delay=0.5,
                should_log=True
            ))
            def get_user_with_retry(self, user_id: int) -> Dict[str, Any]:
                """带重试的获取用户信息"""
                self.failure_count += 1
                
                if self.failure_count <= 2:  # 前两次失败
                    raise ExternalServiceError(
                        f"用户服务暂时不可用",
                        service_name="user_api",
                        status_code=503,
                        error_code="SERVICE_UNAVAILABLE"
                    )
                
                # 第三次成功
                return {
                    'user_id': user_id,
                    'name': f'User_{user_id}',
                    'email': f'user{user_id}@example.com'
                }
            
            @handle_exceptions(ErrorPolicy(
                strategy=ErrorHandlingStrategy.FALLBACK,
                fallback_value={'user_id': None, 'name': 'Unknown', 'email': 'unknown@example.com'},
                should_log=True
            ))
            def get_user_with_fallback(self, user_id: int) -> Dict[str, Any]:
                """带降级的获取用户信息"""
                if user_id < 0:
                    raise ValidationError(
                        f"用户ID必须为正数: {user_id}",
                        error_code="INVALID_USER_ID",
                        context={'user_id': user_id}
                    )
                
                if user_id > 1000:
                    raise ExternalServiceError(
                        "用户服务过载",
                        service_name="user_api",
                        status_code=503
                    )
                
                return {
                    'user_id': user_id,
                    'name': f'User_{user_id}',
                    'email': f'user{user_id}@example.com'
                }
            
            def validate_user_data(self, user_data: Dict[str, Any]) -> bool:
                """验证用户数据"""
                errors = []
                
                # 使用上下文管理器处理验证错误
                validation_policy = ErrorPolicy(
                    strategy=ErrorHandlingStrategy.LOG_AND_CONTINUE,
                    should_log=True,
                    log_level='warning'
                )
                
                # 验证必需字段
                required_fields = ['name', 'email', 'age']
                for field in required_fields:
                    with ErrorContext(f'validate_{field}', validation_policy, self.logger) as ctx:
                        if field not in user_data or not user_data[field]:
                            raise ValidationError(
                                f"缺少必需字段: {field}",
                                error_code="MISSING_FIELD",
                                context={'field': field, 'data': user_data}
                            )
                
                # 验证邮箱格式
                with ErrorContext('validate_email_format', validation_policy, self.logger) as ctx:
                    email = user_data.get('email', '')
                    if '@' not in email or '.' not in email.split('@')[-1]:
                        raise ValidationError(
                            f"邮箱格式无效: {email}",
                            error_code="INVALID_EMAIL_FORMAT",
                            context={'email': email}
                        )
                
                # 验证年龄范围
                with ErrorContext('validate_age_range', validation_policy, self.logger) as ctx:
                    age = user_data.get('age')
                    if not isinstance(age, int) or age < 0 or age > 150:
                        raise ValidationError(
                            f"年龄必须是0-150之间的整数: {age}",
                            error_code="INVALID_AGE_RANGE",
                            context={'age': age}
                        )
                
                return True
        
        # 测试设计原则
        user_service = UserService()
        
        print("=" * 60)
        print("测试重试策略")
        print("=" * 60)
        
        try:
            user = user_service.get_user_with_retry(123)
            print(f"✅ 获取用户成功: {user}")
        except Exception as e:
            print(f"❌ 获取用户失败: {e}")
        
        print("\n" + "=" * 60)
        print("测试降级策略")
        print("=" * 60)
        
        test_cases = [100, -1, 2000]
        for user_id in test_cases:
            try:
                user = user_service.get_user_with_fallback(user_id)
                print(f"用户ID {user_id}: {user}")
            except Exception as e:
                print(f"用户ID {user_id} 处理失败: {e}")
        
        print("\n" + "=" * 60)
        print("测试验证策略")
        print("=" * 60)
        
        test_data = [
            {'name': 'Alice', 'email': 'alice@example.com', 'age': 25},
            {'name': 'Bob', 'email': 'invalid-email', 'age': 30},
            {'email': 'charlie@example.com', 'age': 35},  # 缺少name
            {'name': 'David', 'email': 'david@example.com', 'age': -5}
        ]
        
        for i, data in enumerate(test_data, 1):
            print(f"\n测试数据 {i}: {data}")
            try:
                is_valid = user_service.validate_user_data(data)
                print(f"验证结果: {'通过' if is_valid else '失败'}")
            except Exception as e:
                print(f"验证异常: {e}")
    
    demonstrate_design_principles()

demonstrate_exception_design_principles()
```

### 2. 异常处理架构模式

```python
def demonstrate_exception_architecture_patterns():
    """演示异常处理的架构模式"""
    
    from abc import ABC, abstractmethod
    from typing import Protocol, runtime_checkable, Union, Callable, Any
    from dataclasses import dataclass, field
    from contextlib import contextmanager
    import asyncio
    import functools
    
    # 模式1: 责任链模式处理异常
    @runtime_checkable
    class ExceptionHandler(Protocol):
        """异常处理器协议"""
        
        def can_handle(self, exception: Exception) -> bool:
            """判断是否能处理该异常"""
            ...
        
        def handle(self, exception: Exception, context: Dict[str, Any]) -> Any:
            """处理异常"""
            ...
    
    class BaseExceptionHandler:
        """异常处理器基类"""
        
        def __init__(self, next_handler: Optional['BaseExceptionHandler'] = None):
            self.next_handler = next_handler
        
        def set_next(self, handler: 'BaseExceptionHandler') -> 'BaseExceptionHandler':
            """设置下一个处理器"""
            self.next_handler = handler
            return handler
        
        def handle_exception(self, exception: Exception, context: Dict[str, Any]) -> Any:
            """处理异常的入口方法"""
            if self.can_handle(exception):
                return self.handle(exception, context)
            elif self.next_handler:
                return self.next_handler.handle_exception(exception, context)
            else:
                # 没有处理器能处理该异常，重新抛出
                raise exception
        
        @abstractmethod
        def can_handle(self, exception: Exception) -> bool:
            """判断是否能处理该异常"""
            pass
        
        @abstractmethod
        def handle(self, exception: Exception, context: Dict[str, Any]) -> Any:
            """处理异常"""
            pass
    
    class ValidationExceptionHandler(BaseExceptionHandler):
        """验证异常处理器"""
        
        def can_handle(self, exception: Exception) -> bool:
            return isinstance(exception, (ValueError, TypeError))
        
        def handle(self, exception: Exception, context: Dict[str, Any]) -> Any:
            logger = context.get('logger')
            if logger:
                logger.warning(f"验证异常: {exception}")
            
            return {
                'success': False,
                'error': 'validation_error',
                'message': str(exception),
                'code': 400
            }
    
    class BusinessExceptionHandler(BaseExceptionHandler):
        """业务异常处理器"""
        
        def can_handle(self, exception: Exception) -> bool:
            return isinstance(exception, BusinessError)
        
        def handle(self, exception: Exception, context: Dict[str, Any]) -> Any:
            logger = context.get('logger')
            if logger:
                logger.info(f"业务异常: {exception}")
            
            return {
                'success': False,
                'error': 'business_error',
                'message': str(exception),
                'code': exception.error_code or 'BUSINESS_ERROR',
                'context': exception.context
            }
    
    class InfrastructureExceptionHandler(BaseExceptionHandler):
        """基础设施异常处理器"""
        
        def can_handle(self, exception: Exception) -> bool:
            return isinstance(exception, (ConnectionError, TimeoutError, InfrastructureError))
        
        def handle(self, exception: Exception, context: Dict[str, Any]) -> Any:
            logger = context.get('logger')
            if logger:
                logger.error(f"基础设施异常: {exception}")
            
            # 对于基础设施异常，可能需要重试或降级
            retry_count = context.get('retry_count', 0)
            max_retries = context.get('max_retries', 3)
            
            if retry_count < max_retries:
                context['retry_count'] = retry_count + 1
                return {
                    'success': False,
                    'error': 'infrastructure_error',
                    'message': str(exception),
                    'should_retry': True,
                    'retry_after': 2 ** retry_count  # 指数退避
                }
            else:
                return {
                    'success': False,
                    'error': 'infrastructure_error',
                    'message': str(exception),
                    'code': 503,
                    'should_retry': False
                }
    
    class DefaultExceptionHandler(BaseExceptionHandler):
        """默认异常处理器"""
        
        def can_handle(self, exception: Exception) -> bool:
            return True  # 处理所有异常
        
        def handle(self, exception: Exception, context: Dict[str, Any]) -> Any:
            logger = context.get('logger')
            if logger:
                logger.exception(f"未处理的异常: {exception}")
            
            return {
                'success': False,
                'error': 'internal_error',
                'message': 'An unexpected error occurred',
                'code': 500
            }
    
    # 模式2: 异常处理工厂
    class ExceptionHandlerFactory:
        """异常处理器工厂"""
        
        @staticmethod
        def create_web_api_handler() -> BaseExceptionHandler:
            """创建Web API异常处理链"""
            # 构建处理链：验证 -> 业务 -> 基础设施 -> 默认
            default_handler = DefaultExceptionHandler()
            infra_handler = InfrastructureExceptionHandler(default_handler)
            business_handler = BusinessExceptionHandler(infra_handler)
            validation_handler = ValidationExceptionHandler(business_handler)
            
            return validation_handler
        
        @staticmethod
        def create_batch_processing_handler() -> BaseExceptionHandler:
            """创建批处理异常处理链"""
            # 批处理可能需要不同的处理策略
            default_handler = DefaultExceptionHandler()
            infra_handler = InfrastructureExceptionHandler(default_handler)
            business_handler = BusinessExceptionHandler(infra_handler)
            
            return business_handler
    
    # 模式3: 异常处理中间件
    class ExceptionMiddleware:
        """异常处理中间件"""
        
        def __init__(self, handler: BaseExceptionHandler):
            self.handler = handler
            self.logger = logging.getLogger(__name__)
        
        def __call__(self, func: Callable) -> Callable:
            """装饰器形式的中间件"""
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                context = {
                    'function': func.__name__,
                    'module': func.__module__,
                    'args': args,
                    'kwargs': kwargs,
                    'logger': self.logger
                }
                
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    return self.handler.handle_exception(e, context)
            
            return wrapper
        
        @contextmanager
        def handle_context(self, **context_data):
            """上下文管理器形式的中间件"""
            context = {
                'logger': self.logger,
                **context_data
            }
            
            try:
                yield context
            except Exception as e:
                result = self.handler.handle_exception(e, context)
                # 如果处理结果表明需要重新抛出异常
                if isinstance(result, dict) and result.get('should_reraise'):
                    raise
                return result
    
    # 模式4: 异步异常处理
    class AsyncExceptionHandler:
        """异步异常处理器"""
        
        def __init__(self, handler: BaseExceptionHandler):
            self.handler = handler
            self.logger = logging.getLogger(__name__)
        
        def __call__(self, func: Callable) -> Callable:
            """异步函数装饰器"""
            if asyncio.iscoroutinefunction(func):
                @functools.wraps(func)
                async def async_wrapper(*args, **kwargs):
                    context = {
                        'function': func.__name__,
                        'module': func.__module__,
                        'logger': self.logger,
                        'is_async': True
                    }
                    
                    try:
                        return await func(*args, **kwargs)
                    except Exception as e:
                        return self.handler.handle_exception(e, context)
                
                return async_wrapper
            else:
                # 同步函数的处理
                @functools.wraps(func)
                def sync_wrapper(*args, **kwargs):
                    context = {
                        'function': func.__name__,
                        'module': func.__module__,
                        'logger': self.logger,
                        'is_async': False
                    }
                    
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        return self.handler.handle_exception(e, context)
                
                return sync_wrapper
    
    def demonstrate_architecture_patterns():
        """演示架构模式的应用"""
        
        # 配置日志
        logging.basicConfig(level=logging.INFO)
        
        # 创建异常处理链
        web_handler = ExceptionHandlerFactory.create_web_api_handler()
        middleware = ExceptionMiddleware(web_handler)
        async_handler = AsyncExceptionHandler(web_handler)
        
        # 示例服务类
        class ProductService:
            """产品服务"""
            
            @middleware
            def get_product(self, product_id: int) -> Dict[str, Any]:
                """获取产品信息"""
                if product_id <= 0:
                    raise ValueError(f"产品ID必须为正数: {product_id}")
                
                if product_id == 404:
                    raise BusinessError(
                        f"产品不存在: {product_id}",
                        error_code="PRODUCT_NOT_FOUND",
                        context={'product_id': product_id}
                    )
                
                if product_id == 503:
                    raise ConnectionError("数据库连接失败")
                
                if product_id == 999:
                    raise RuntimeError("未知错误")
                
                return {
                    'product_id': product_id,
                    'name': f'Product_{product_id}',
                    'price': product_id * 10
                }
            
            @async_handler
            async def get_product_async(self, product_id: int) -> Dict[str, Any]:
                """异步获取产品信息"""
                # 模拟异步操作
                await asyncio.sleep(0.1)
                
                if product_id <= 0:
                    raise ValueError(f"产品ID必须为正数: {product_id}")
                
                if product_id == 404:
                    raise BusinessError(
                        f"产品不存在: {product_id}",
                        error_code="PRODUCT_NOT_FOUND"
                    )
                
                return {
                    'product_id': product_id,
                    'name': f'AsyncProduct_{product_id}',
                    'price': product_id * 15
                }
            
            def batch_process_products(self, product_ids: List[int]) -> List[Dict[str, Any]]:
                """批量处理产品"""
                results = []
                
                for product_id in product_ids:
                    with middleware.handle_context(batch_item=product_id) as context:
                        if product_id <= 0:
                            raise ValueError(f"产品ID必须为正数: {product_id}")
                        
                        if product_id == 503:
                            raise InfrastructureError(
                                "服务暂时不可用",
                                error_code="SERVICE_UNAVAILABLE"
                            )
                        
                        results.append({
                            'product_id': product_id,
                            'name': f'BatchProduct_{product_id}',
                            'processed': True
                        })
                
                return results
        
        # 测试架构模式
        product_service = ProductService()
        
        print("=" * 60)
        print("测试同步异常处理")
        print("=" * 60)
        
        test_ids = [1, -1, 404, 503, 999]
        for product_id in test_ids:
            print(f"\n获取产品 {product_id}:")
            result = product_service.get_product(product_id)
            print(f"结果: {result}")
        
        print("\n" + "=" * 60)
        print("测试异步异常处理")
        print("=" * 60)
        
        async def test_async():
            for product_id in [1, -1, 404]:
                print(f"\n异步获取产品 {product_id}:")
                result = await product_service.get_product_async(product_id)
                print(f"结果: {result}")
        
        # 运行异步测试
        try:
            asyncio.run(test_async())
        except Exception as e:
            print(f"异步测试失败: {e}")
        
        print("\n" + "=" * 60)
        print("测试批量处理异常处理")
        print("=" * 60)
        
        batch_ids = [1, 2, -1, 3, 503, 4]
        print(f"\n批量处理产品 {batch_ids}:")
        try:
            results = product_service.batch_process_products(batch_ids)
            print(f"批量处理结果: {results}")
        except Exception as e:
            print(f"批量处理失败: {e}")
    
    demonstrate_architecture_patterns()

demonstrate_exception_architecture_patterns()
```

## 性能优化和测试策略

### 1. 异常处理性能优化

```python
def demonstrate_performance_optimization():
    """演示异常处理的性能优化策略"""
    
    import time
    import cProfile
    import pstats
    from functools import wraps
    from typing import Callable, Any
    import weakref
    
    # 优化策略1: 异常缓存和复用
    class ExceptionCache:
        """异常缓存器"""
        
        def __init__(self, max_size: int = 1000):
            self.cache = {}
            self.max_size = max_size
            self.access_count = {}
        
        def get_or_create_exception(self, exc_type: type, message: str, **kwargs) -> Exception:
            """获取或创建异常实例"""
            cache_key = (exc_type.__name__, message, tuple(sorted(kwargs.items())))
            
            if cache_key in self.cache:
                self.access_count[cache_key] = self.access_count.get(cache_key, 0) + 1
                return self.cache[cache_key]
            
            # 缓存已满，清理最少使用的异常
            if len(self.cache) >= self.max_size:
                self._cleanup_cache()
            
            # 创建新异常
            exception = exc_type(message, **kwargs)
            self.cache[cache_key] = exception
            self.access_count[cache_key] = 1
            
            return exception
        
        def _cleanup_cache(self):
            """清理缓存"""
            # 移除使用次数最少的异常
            if self.access_count:
                min_key = min(self.access_count.keys(), key=lambda k: self.access_count[k])
                del self.cache[min_key]
                del self.access_count[min_key]
    
    # 优化策略2: 延迟异常信息收集
    class LazyExceptionInfo:
        """延迟异常信息收集"""
        
        def __init__(self, exception: Exception):
            self.exception = exception
            self._traceback_str = None
            self._context_info = None
        
        @property
        def traceback_str(self) -> str:
            """延迟获取堆栈跟踪字符串"""
            if self._traceback_str is None:
                import traceback
                self._traceback_str = ''.join(
                    traceback.format_exception(
                        type(self.exception),
                        self.exception,
                        self.exception.__traceback__
                    )
                )
            return self._traceback_str
        
        @property
        def context_info(self) -> Dict[str, Any]:
            """延迟收集上下文信息"""
            if self._context_info is None:
                import inspect
                frame = inspect.currentframe()
                
                self._context_info = {
                    'exception_type': type(self.exception).__name__,
                    'message': str(self.exception),
                    'timestamp': time.time(),
                    'frame_info': self._collect_frame_info(frame)
                }
            
            return self._context_info
        
        def _collect_frame_info(self, frame) -> List[Dict[str, Any]]:
            """收集调用栈信息"""
            frame_info = []
            current_frame = frame
            
            while current_frame and len(frame_info) < 10:  # 限制深度
                frame_info.append({
                    'filename': current_frame.f_code.co_filename,
                    'function': current_frame.f_code.co_name,
                    'lineno': current_frame.f_lineno,
                    'locals': {k: str(v)[:100] for k, v in current_frame.f_locals.items() 
                              if not k.startswith('_')}
                })
                current_frame = current_frame.f_back
            
            return frame_info
    
    # 优化策略3: 异常处理性能监控
    class ExceptionPerformanceMonitor:
        """异常处理性能监控器"""
        
        def __init__(self):
            self.stats = {
                'exception_counts': {},
                'handling_times': {},
                'total_handling_time': 0,
                'total_exceptions': 0
            }
        
        def monitor_exception_handling(self, func: Callable) -> Callable:
            """监控异常处理性能的装饰器"""
            @wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                exception_occurred = False
                exception_type = None
                
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    exception_occurred = True
                    exception_type = type(e).__name__
                    raise
                finally:
                    end_time = time.perf_counter()
                    execution_time = end_time - start_time
                    
                    if exception_occurred:
                        self._record_exception_handling(exception_type, execution_time)
            
            return wrapper
        
        def _record_exception_handling(self, exception_type: str, handling_time: float):
            """记录异常处理统计信息"""
            self.stats['exception_counts'][exception_type] = \
                self.stats['exception_counts'].get(exception_type, 0) + 1
            
            if exception_type not in self.stats['handling_times']:
                self.stats['handling_times'][exception_type] = []
            
            self.stats['handling_times'][exception_type].append(handling_time)
            self.stats['total_handling_time'] += handling_time
            self.stats['total_exceptions'] += 1
        
        def get_performance_report(self) -> Dict[str, Any]:
            """获取性能报告"""
            report = {
                'total_exceptions': self.stats['total_exceptions'],
                'total_handling_time': self.stats['total_handling_time'],
                'average_handling_time': 0,
                'exception_types': {}
            }
            
            if self.stats['total_exceptions'] > 0:
                report['average_handling_time'] = \
                    self.stats['total_handling_time'] / self.stats['total_exceptions']
            
            for exc_type, times in self.stats['handling_times'].items():
                report['exception_types'][exc_type] = {
                    'count': len(times),
                    'total_time': sum(times),
                    'average_time': sum(times) / len(times),
                    'min_time': min(times),
                    'max_time': max(times)
                }
            
            return report
    
    # 优化策略4: 快速失败模式
    class FastFailValidator:
        """快速失败验证器"""
        
        def __init__(self):
            self.validation_cache = {}
        
        def validate_fast(self, data: Any, validation_rules: List[Callable]) -> bool:
            """快速验证，遇到第一个错误立即失败"""
            # 使用数据的哈希作为缓存键
            cache_key = hash(str(data))
            
            if cache_key in self.validation_cache:
                cached_result, cached_exception = self.validation_cache[cache_key]
                if not cached_result:
                    raise cached_exception
                return cached_result
            
            try:
                for rule in validation_rules:
                    if not rule(data):
                        error = ValueError(f"验证规则失败: {rule.__name__}")
                        self.validation_cache[cache_key] = (False, error)
                        raise error
                
                self.validation_cache[cache_key] = (True, None)
                return True
                
            except Exception as e:
                self.validation_cache[cache_key] = (False, e)
                raise
    
    def demonstrate_performance_optimization():
        """演示性能优化策略"""
        
        # 创建性能监控器
        monitor = ExceptionPerformanceMonitor()
        exception_cache = ExceptionCache()
        validator = FastFailValidator()
        
        # 示例服务类
        class OptimizedService:
            """优化的服务类"""
            
            def __init__(self):
                self.cache = exception_cache
            
            @monitor.monitor_exception_handling
            def process_data_with_cache(self, data: Dict[str, Any]) -> Dict[str, Any]:
                """使用异常缓存的数据处理"""
                if not data:
                    # 使用缓存的异常
                    raise self.cache.get_or_create_exception(
                        ValueError, 
                        "数据不能为空",
                        error_code="EMPTY_DATA"
                    )
                
                if 'error' in data:
                    # 使用缓存的异常
                    raise self.cache.get_or_create_exception(
                        RuntimeError,
                        f"处理错误: {data['error']}",
                        error_code="PROCESSING_ERROR"
                    )
                
                return {'result': f"处理成功: {data}"}
            
            @monitor.monitor_exception_handling
            def process_data_with_lazy_info(self, data: Dict[str, Any]) -> Dict[str, Any]:
                """使用延迟异常信息的数据处理"""
                try:
                    if not data:
                        raise ValueError("数据不能为空")
                    
                    if 'error' in data:
                        raise RuntimeError(f"处理错误: {data['error']}")
                    
                    return {'result': f"处理成功: {data}"}
                    
                except Exception as e:
                    # 创建延迟异常信息
                    lazy_info = LazyExceptionInfo(e)
                    
                    # 只在需要时才收集详细信息
                    if data.get('debug'):
                        print(f"异常详细信息: {lazy_info.context_info}")
                    
                    raise
            
            def validate_data_fast(self, data: Dict[str, Any]) -> bool:
                """快速验证数据"""
                validation_rules = [
                    lambda d: isinstance(d, dict),
                    lambda d: 'name' in d,
                    lambda d: len(d.get('name', '')) > 0,
                    lambda d: 'age' in d,
                    lambda d: isinstance(d.get('age'), int),
                    lambda d: 0 <= d.get('age', -1) <= 150
                ]
                
                return validator.validate_fast(data, validation_rules)
        
        def performance_test():
            """性能测试"""
            service = OptimizedService()
            
            print("=" * 60)
            print("性能优化测试")
            print("=" * 60)
            
            # 测试数据
            test_cases = [
                {},  # 空数据
                {'error': 'test'},  # 错误数据
                {'data': 'valid'},  # 正常数据
                {'error': 'test'},  # 重复错误数据（测试缓存）
                {},  # 重复空数据（测试缓存）
            ]
            
            # 测试异常缓存
            print("\n测试异常缓存:")
            for i, data in enumerate(test_cases):
                try:
                    result = service.process_data_with_cache(data)
                    print(f"测试 {i+1}: 成功 - {result}")
                except Exception as e:
                    print(f"测试 {i+1}: 异常 - {type(e).__name__}: {e}")
            
            # 测试延迟异常信息
            print("\n测试延迟异常信息:")
            debug_cases = [
                {'error': 'debug_error', 'debug': True},
                {'error': 'normal_error', 'debug': False}
            ]
            
            for i, data in enumerate(debug_cases):
                try:
                    result = service.process_data_with_lazy_info(data)
                    print(f"调试测试 {i+1}: 成功 - {result}")
                except Exception as e:
                    print(f"调试测试 {i+1}: 异常 - {type(e).__name__}: {e}")
            
            # 测试快速验证
            print("\n测试快速验证:")
            validation_cases = [
                {'name': 'Alice', 'age': 25},  # 有效数据
                {'name': 'Bob'},  # 缺少age
                {'name': '', 'age': 30},  # 空name
                {'name': 'Charlie', 'age': -5},  # 无效age
                {'name': 'Alice', 'age': 25},  # 重复有效数据（测试缓存）
            ]
            
            for i, data in enumerate(validation_cases):
                try:
                    is_valid = service.validate_data_fast(data)
                    print(f"验证 {i+1}: {'通过' if is_valid else '失败'} - {data}")
                except Exception as e:
                    print(f"验证 {i+1}: 异常 - {type(e).__name__}: {e}")
            
            # 显示性能报告
            print("\n" + "=" * 60)
            print("性能报告")
            print("=" * 60)
            
            report = monitor.get_performance_report()
            print(f"总异常数: {report['total_exceptions']}")
            print(f"总处理时间: {report['total_handling_time']:.6f}秒")
            print(f"平均处理时间: {report['average_handling_time']:.6f}秒")
            
            print("\n各异常类型统计:")
            for exc_type, stats in report['exception_types'].items():
                print(f"  {exc_type}:")
                print(f"    数量: {stats['count']}")
                print(f"    总时间: {stats['total_time']:.6f}秒")
                print(f"    平均时间: {stats['average_time']:.6f}秒")
                print(f"    最短时间: {stats['min_time']:.6f}秒")
                print(f"    最长时间: {stats['max_time']:.6f}秒")
        
        performance_test()
    
    demonstrate_performance_optimization()

demonstrate_performance_optimization()
```

### 2. 异常处理测试策略

```python
def demonstrate_exception_testing_strategies():
    """演示异常处理的测试策略"""
    
    import unittest
    from unittest.mock import Mock, patch, MagicMock
    import pytest
    from contextlib import contextmanager
    from typing import Type, Callable, Any
    
    # 测试策略1: 异常测试工具类
    class ExceptionTestHelper:
        """异常测试辅助类"""
        
        @staticmethod
        def assert_raises_with_message(exception_type: Type[Exception], 
                                     expected_message: str,
                                     func: Callable, 
                                     *args, **kwargs):
            """断言抛出特定异常和消息"""
            try:
                func(*args, **kwargs)
                raise AssertionError(f"期望抛出 {exception_type.__name__} 异常，但没有抛出")
            except exception_type as e:
                if expected_message not in str(e):
                    raise AssertionError(
                        f"异常消息不匹配。期望包含: '{expected_message}'，实际: '{str(e)}'"
                    )
            except Exception as e:
                raise AssertionError(
                    f"期望抛出 {exception_type.__name__}，实际抛出 {type(e).__name__}: {e}"
                )
        
        @staticmethod
        def assert_exception_chain(func: Callable, 
                                 expected_chain: List[Type[Exception]],
                                 *args, **kwargs):
            """断言异常链"""
            try:
                func(*args, **kwargs)
                raise AssertionError("期望抛出异常，但没有抛出")
            except Exception as e:
                actual_chain = []
                current = e
                
                while current:
                    actual_chain.append(type(current))
                    current = current.__cause__ or current.__context__
                
                if actual_chain != expected_chain:
                    raise AssertionError(
                        f"异常链不匹配。期望: {[c.__name__ for c in expected_chain]}，"
                        f"实际: {[c.__name__ for c in actual_chain]}"
                    )
        
        @staticmethod
        @contextmanager
        def capture_exceptions():
            """捕获异常的上下文管理器"""
            exceptions = []
            
            class ExceptionCapture:
                def add(self, exception: Exception):
                    exceptions.append(exception)
                
                @property
                def captured(self) -> List[Exception]:
                    return exceptions.copy()
                
                def clear(self):
                    exceptions.clear()
            
            yield ExceptionCapture()
    
    # 测试策略2: 模拟异常场景
    class ExceptionScenarioMocker:
        """异常场景模拟器"""
        
        def __init__(self):
            self.scenarios = {}
        
        def register_scenario(self, name: str, exception: Exception, 
                            trigger_condition: Callable = None):
            """注册异常场景"""
            self.scenarios[name] = {
                'exception': exception,
                'trigger_condition': trigger_condition or (lambda: True)
            }
        
        def mock_function_with_scenarios(self, func: Callable, 
                                       scenario_name: str) -> Mock:
            """使用场景模拟函数"""
            if scenario_name not in self.scenarios:
                raise ValueError(f"未知场景: {scenario_name}")
            
            scenario = self.scenarios[scenario_name]
            mock_func = Mock(side_effect=scenario['exception'])
            
            return mock_func
        
        @contextmanager
        def simulate_scenario(self, scenario_name: str):
            """模拟异常场景的上下文管理器"""
            if scenario_name not in self.scenarios:
                raise ValueError(f"未知场景: {scenario_name}")
            
            scenario = self.scenarios[scenario_name]
            
            if scenario['trigger_condition']():
                yield scenario['exception']
            else:
                yield None
    
    # 测试策略3: 异常处理覆盖率测试
    class ExceptionCoverageTracker:
        """异常处理覆盖率跟踪器"""
        
        def __init__(self):
            self.exception_handlers = set()
            self.triggered_handlers = set()
        
        def register_handler(self, handler_name: str, exception_types: List[Type[Exception]]):
            """注册异常处理器"""
            for exc_type in exception_types:
                self.exception_handlers.add((handler_name, exc_type.__name__))
        
        def mark_handler_triggered(self, handler_name: str, exception_type: str):
            """标记处理器被触发"""
            self.triggered_handlers.add((handler_name, exception_type))
        
        def get_coverage_report(self) -> Dict[str, Any]:
            """获取覆盖率报告"""
            total_handlers = len(self.exception_handlers)
            triggered_handlers = len(self.triggered_handlers)
            
            untested_handlers = self.exception_handlers - self.triggered_handlers
            
            return {
                'total_handlers': total_handlers,
                'triggered_handlers': triggered_handlers,
                'coverage_percentage': (triggered_handlers / total_handlers * 100) if total_handlers > 0 else 0,
                'untested_handlers': list(untested_handlers)
            }
    
    def demonstrate_testing_strategies():
        """演示测试策略的应用"""
        
        # 被测试的服务类
        class OrderService:
            """订单服务（被测试类）"""
            
            def __init__(self, payment_service=None, inventory_service=None):
                self.payment_service = payment_service
                self.inventory_service = inventory_service
                self.coverage_tracker = ExceptionCoverageTracker()
                
                # 注册异常处理器
                self.coverage_tracker.register_handler(
                    'validate_order', [ValueError, TypeError]
                )
                self.coverage_tracker.register_handler(
                    'check_inventory', [RuntimeError, ConnectionError]
                )
                self.coverage_tracker.register_handler(
                    'process_payment', [PermissionError, TimeoutError]
                )
            
            def validate_order(self, order_data: Dict[str, Any]) -> bool:
                """验证订单"""
                try:
                    if not isinstance(order_data, dict):
                        raise TypeError("订单数据必须是字典类型")
                    
                    if not order_data.get('items'):
                        raise ValueError("订单必须包含商品")
                    
                    if order_data.get('total', 0) <= 0:
                        raise ValueError("订单总额必须大于0")
                    
                    return True
                    
                except (ValueError, TypeError) as e:
                    self.coverage_tracker.mark_handler_triggered(
                        'validate_order', type(e).__name__
                    )
                    raise
            
            def check_inventory(self, items: List[Dict[str, Any]]) -> bool:
                """检查库存"""
                try:
                    if not self.inventory_service:
                        raise ConnectionError("库存服务不可用")
                    
                    for item in items:
                        available = self.inventory_service.check_availability(item['id'])
                        if not available:
                            raise RuntimeError(f"商品 {item['name']} 库存不足")
                    
                    return True
                    
                except (RuntimeError, ConnectionError) as e:
                    self.coverage_tracker.mark_handler_triggered(
                        'check_inventory', type(e).__name__
                    )
                    raise
            
            def process_payment(self, payment_data: Dict[str, Any]) -> Dict[str, Any]:
                """处理支付"""
                try:
                    if not self.payment_service:
                        raise ConnectionError("支付服务不可用")
                    
                    if payment_data.get('amount', 0) > 10000:
                        raise PermissionError("支付金额超过限制")
                    
                    result = self.payment_service.charge(payment_data)
                    
                    if not result.get('success'):
                        raise TimeoutError("支付处理超时")
                    
                    return result
                    
                except (PermissionError, TimeoutError, ConnectionError) as e:
                    self.coverage_tracker.mark_handler_triggered(
                        'process_payment', type(e).__name__
                    )
                    raise
            
            def create_order(self, order_data: Dict[str, Any]) -> Dict[str, Any]:
                """创建订单（组合方法）"""
                try:
                    # 验证订单
                    self.validate_order(order_data)
                    
                    # 检查库存
                    self.check_inventory(order_data['items'])
                    
                    # 处理支付
                    payment_result = self.process_payment(order_data['payment'])
                    
                    return {
                        'order_id': f"order_{hash(str(order_data)) % 10000:04d}",
                        'status': 'created',
                        'payment': payment_result
                    }
                    
                except Exception as e:
                    # 异常链处理
                    raise BusinessError(
                        f"订单创建失败: {e}",
                        error_code="ORDER_CREATION_FAILED"
                    ) from e
        
        # 测试类
        class TestOrderService(unittest.TestCase):
            """订单服务测试类"""
            
            def setUp(self):
                """测试设置"""
                self.helper = ExceptionTestHelper()
                self.mocker = ExceptionScenarioMocker()
                
                # 注册异常场景
                self.mocker.register_scenario(
                    'inventory_unavailable',
                    ConnectionError("库存服务不可用")
                )
                self.mocker.register_scenario(
                    'payment_timeout',
                    TimeoutError("支付处理超时")
                )
                self.mocker.register_scenario(
                    'insufficient_inventory',
                    RuntimeError("商品库存不足")
                )
            
            def test_validate_order_with_invalid_type(self):
                """测试无效类型的订单验证"""
                service = OrderService()
                
                # 测试类型错误
                self.helper.assert_raises_with_message(
                    TypeError,
                    "订单数据必须是字典类型",
                    service.validate_order,
                    "invalid_data"
                )
            
            def test_validate_order_with_empty_items(self):
                """测试空商品列表的订单验证"""
                service = OrderService()
                
                # 测试值错误
                self.helper.assert_raises_with_message(
                    ValueError,
                    "订单必须包含商品",
                    service.validate_order,
                    {'items': [], 'total': 100}
                )
            
            def test_check_inventory_with_mock_service(self):
                """测试使用模拟服务的库存检查"""
                # 创建模拟库存服务
                mock_inventory = Mock()
                mock_inventory.check_availability.return_value = False
                
                service = OrderService(inventory_service=mock_inventory)
                
                items = [{'id': 1, 'name': '商品A'}]
                
                # 测试库存不足异常
                self.helper.assert_raises_with_message(
                    RuntimeError,
                    "商品 商品A 库存不足",
                    service.check_inventory,
                    items
                )
                
                # 验证模拟服务被调用
                mock_inventory.check_availability.assert_called_with(1)
            
            def test_process_payment_with_scenarios(self):
                """测试使用场景模拟的支付处理"""
                # 创建模拟支付服务
                mock_payment = Mock()
                mock_payment.charge.return_value = {'success': False}
                
                service = OrderService(payment_service=mock_payment)
                
                payment_data = {'amount': 100, 'method': 'credit_card'}
                
                # 测试支付超时异常
                self.helper.assert_raises_with_message(
                    TimeoutError,
                    "支付处理超时",
                    service.process_payment,
                    payment_data
                )
            
            def test_exception_chain_in_create_order(self):
                """测试订单创建中的异常链"""
                service = OrderService()
                
                invalid_order = "invalid_order_data"
                
                # 测试异常链
                self.helper.assert_exception_chain(
                    service.create_order,
                    [BusinessError, TypeError],
                    invalid_order
                )
            
            def test_exception_coverage(self):
                """测试异常处理覆盖率"""
                service = OrderService()
                
                # 触发各种异常以测试覆盖率
                test_cases = [
                    (lambda: service.validate_order("invalid"), TypeError),
                    (lambda: service.validate_order({'items': []}), ValueError),
                    (lambda: service.check_inventory([]), ConnectionError),
                ]
                
                for test_func, expected_exception in test_cases:
                    with self.assertRaises(expected_exception):
                        test_func()
                
                # 检查覆盖率
                coverage_report = service.coverage_tracker.get_coverage_report()
                
                print(f"\n异常处理覆盖率报告:")
                print(f"总处理器数: {coverage_report['total_handlers']}")
                print(f"已触发处理器数: {coverage_report['triggered_handlers']}")
                print(f"覆盖率: {coverage_report['coverage_percentage']:.1f}%")
                print(f"未测试的处理器: {coverage_report['untested_handlers']}")
        
        def run_exception_tests():
            """运行异常测试"""
            print("=" * 60)
            print("异常处理测试策略演示")
            print("=" * 60)
            
            # 创建测试套件
            suite = unittest.TestLoader().loadTestsFromTestCase(TestOrderService)
            
            # 运行测试
            runner = unittest.TextTestRunner(verbosity=2)
            result = runner.run(suite)
            
            print(f"\n测试结果:")
            print(f"运行测试数: {result.testsRun}")
            print(f"失败数: {len(result.failures)}")
            print(f"错误数: {len(result.errors)}")
            print(f"成功率: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
        
        run_exception_tests()
    
    demonstrate_testing_strategies()

demonstrate_exception_testing_strategies()
```

## 实际应用场景

### 1. Web API异常处理

```python
def demonstrate_web_api_exception_handling():
    """演示Web API中的异常处理最佳实践"""
    
    from flask import Flask, request, jsonify
    from functools import wraps
    import traceback
    
    app = Flask(__name__)
    
    # API异常处理装饰器
    def api_exception_handler(func):
        """API异常处理装饰器"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValidationError as e:
                return jsonify({
                    'success': False,
                    'error': 'validation_error',
                    'message': str(e),
                    'code': e.error_code,
                    'context': e.context
                }), 400
            except BusinessError as e:
                return jsonify({
                    'success': False,
                    'error': 'business_error',
                    'message': str(e),
                    'code': e.error_code
                }), 422
            except InfrastructureError as e:
                return jsonify({
                    'success': False,
                    'error': 'service_error',
                    'message': 'Service temporarily unavailable'
                }), 503
            except Exception as e:
                # 记录未预期的异常
                app.logger.exception(f"Unexpected error in {func.__name__}: {e}")
                return jsonify({
                    'success': False,
                    'error': 'internal_error',
                    'message': 'An unexpected error occurred'
                }), 500
        
        return wrapper
    
    @app.route('/api/users', methods=['POST'])
    @api_exception_handler
    def create_user():
        """创建用户API"""
        data = request.get_json()
        
        # 验证输入
        if not data:
            raise ValidationError(
                "请求体不能为空",
                error_code="EMPTY_REQUEST_BODY"
            )
        
        if 'email' not in data:
            raise ValidationError(
                "邮箱是必需的",
                error_code="MISSING_EMAIL",
                context={'provided_fields': list(data.keys())}
            )
        
        # 业务逻辑验证
        if '@' not in data['email']:
            raise BusinessError(
                "邮箱格式无效",
                error_code="INVALID_EMAIL_FORMAT"
            )
        
        # 模拟数据库操作
        if data['email'] == 'error@example.com':
            raise InfrastructureError(
                "数据库连接失败",
                error_code="DATABASE_ERROR"
            )
        
        return jsonify({
            'success': True,
            'data': {
                'user_id': 12345,
                'email': data['email'],
                'created_at': '2024-01-01T00:00:00Z'
            }
        })
    
    print("Web API异常处理示例已配置")

demonstrate_web_api_exception_handling()
```

### 2. 微服务异常传播

```python
def demonstrate_microservice_exception_propagation():
    """演示微服务中的异常传播最佳实践"""
    
    import requests
    from dataclasses import dataclass
    from typing import Optional
    
    @dataclass
    class ServiceError:
        """服务错误信息"""
        service_name: str
        error_code: str
        message: str
        trace_id: Optional[str] = None
        upstream_errors: Optional[List['ServiceError']] = None
    
    class MicroserviceClient:
        """微服务客户端基类"""
        
        def __init__(self, service_name: str, base_url: str):
            self.service_name = service_name
            self.base_url = base_url
            self.logger = logging.getLogger(f'{__name__}.{service_name}')
        
        def make_request(self, endpoint: str, method: str = 'GET', 
                       data: Dict[str, Any] = None, 
                       trace_id: str = None) -> Dict[str, Any]:
            """发起请求并处理异常"""
            url = f"{self.base_url}{endpoint}"
            headers = {'Content-Type': 'application/json'}
            
            if trace_id:
                headers['X-Trace-ID'] = trace_id
            
            try:
                if method == 'GET':
                    response = requests.get(url, headers=headers, timeout=30)
                elif method == 'POST':
                    response = requests.post(url, json=data, headers=headers, timeout=30)
                else:
                    raise ValueError(f"不支持的HTTP方法: {method}")
                
                # 检查响应状态
                if response.status_code >= 500:
                    raise InfrastructureError(
                        f"{self.service_name}服务内部错误",
                        error_code="UPSTREAM_SERVICE_ERROR",
                        context={
                            'service': self.service_name,
                            'status_code': response.status_code,
                            'trace_id': trace_id
                        }
                    )
                elif response.status_code >= 400:
                    error_data = response.json() if response.content else {}
                    raise BusinessError(
                        f"{self.service_name}服务业务错误: {error_data.get('message', '未知错误')}",
                        error_code=error_data.get('code', 'UPSTREAM_BUSINESS_ERROR'),
                        context={
                            'service': self.service_name,
                            'upstream_error': error_data,
                            'trace_id': trace_id
                        }
                    )
                
                return response.json()
                
            except requests.exceptions.Timeout:
                raise InfrastructureError(
                    f"{self.service_name}服务请求超时",
                    error_code="SERVICE_TIMEOUT",
                    context={'service': self.service_name, 'trace_id': trace_id}
                )
            except requests.exceptions.ConnectionError:
                raise InfrastructureError(
                    f"{self.service_name}服务连接失败",
                    error_code="SERVICE_UNAVAILABLE",
                    context={'service': self.service_name, 'trace_id': trace_id}
                )
    
    class OrderOrchestrator:
        """订单编排服务"""
        
        def __init__(self):
            self.user_service = MicroserviceClient('user-service', 'http://user-service')
            self.inventory_service = MicroserviceClient('inventory-service', 'http://inventory-service')
            self.payment_service = MicroserviceClient('payment-service', 'http://payment-service')
            self.logger = logging.getLogger(__name__)
        
        def create_order(self, order_data: Dict[str, Any], trace_id: str = None) -> Dict[str, Any]:
            """创建订单（编排多个服务）"""
            errors = []
            
            try:
                # 步骤1: 验证用户
                try:
                    user = self.user_service.make_request(
                        f"/users/{order_data['user_id']}",
                        trace_id=trace_id
                    )
                except Exception as e:
                    error = ServiceError(
                        service_name='user-service',
                        error_code=getattr(e, 'error_code', 'USER_SERVICE_ERROR'),
                        message=str(e),
                        trace_id=trace_id
                    )
                    errors.append(error)
                    raise BusinessError(
                        "用户验证失败",
                        error_code="USER_VALIDATION_FAILED",
                        context={'upstream_errors': [error]}
                    ) from e
                
                # 步骤2: 检查库存
                try:
                    for item in order_data['items']:
                        inventory = self.inventory_service.make_request(
                            f"/inventory/{item['product_id']}",
                            trace_id=trace_id
                        )
                        if inventory['available'] < item['quantity']:
                            raise BusinessError(
                                f"商品 {item['product_id']} 库存不足",
                                error_code="INSUFFICIENT_INVENTORY"
                            )
                except Exception as e:
                    if not isinstance(e, BusinessError):
                        error = ServiceError(
                            service_name='inventory-service',
                            error_code=getattr(e, 'error_code', 'INVENTORY_SERVICE_ERROR'),
                            message=str(e),
                            trace_id=trace_id
                        )
                        errors.append(error)
                        raise BusinessError(
                            "库存检查失败",
                            error_code="INVENTORY_CHECK_FAILED",
                            context={'upstream_errors': [error]}
                        ) from e
                    else:
                        raise
                
                # 步骤3: 处理支付
                try:
                    payment_result = self.payment_service.make_request(
                        "/payments",
                        method='POST',
                        data=order_data['payment'],
                        trace_id=trace_id
                    )
                except Exception as e:
                    error = ServiceError(
                        service_name='payment-service',
                        error_code=getattr(e, 'error_code', 'PAYMENT_SERVICE_ERROR'),
                        message=str(e),
                        trace_id=trace_id
                    )
                    errors.append(error)
                    
                    # 支付失败需要回滚库存
                    try:
                        self._rollback_inventory(order_data['items'], trace_id)
                    except Exception as rollback_error:
                        self.logger.error(f"库存回滚失败: {rollback_error}")
                    
                    raise BusinessError(
                        "支付处理失败",
                        error_code="PAYMENT_FAILED",
                        context={'upstream_errors': [error]}
                    ) from e
                
                return {
                    'order_id': f"order_{hash(str(order_data)) % 10000:04d}",
                    'status': 'created',
                    'user': user,
                    'payment': payment_result,
                    'trace_id': trace_id
                }
                
            except Exception as e:
                # 记录完整的错误上下文
                self.logger.error(
                    f"订单创建失败 [trace_id: {trace_id}]: {e}",
                    extra={
                        'trace_id': trace_id,
                        'order_data': order_data,
                        'upstream_errors': errors
                    }
                )
                raise
        
        def _rollback_inventory(self, items: List[Dict[str, Any]], trace_id: str):
            """回滚库存"""
            for item in items:
                try:
                    self.inventory_service.make_request(
                        f"/inventory/{item['product_id']}/rollback",
                        method='POST',
                        data={'quantity': item['quantity']},
                        trace_id=trace_id
                    )
                except Exception as e:
                    self.logger.warning(
                        f"库存回滚失败 [product_id: {item['product_id']}]: {e}"
                    )
    
    def demonstrate_microservice_usage():
        """演示微服务异常处理"""
        orchestrator = OrderOrchestrator()
        
        # 测试订单数据
        order_data = {
            'user_id': 123,
            'items': [
                {'product_id': 'prod_001', 'quantity': 2},
                {'product_id': 'prod_002', 'quantity': 1}
            ],
            'payment': {
                'method': 'credit_card',
                'amount': 299.99
            }
        }
        
        trace_id = f"trace_{int(time.time())}"
        
        try:
            result = orchestrator.create_order(order_data, trace_id)
            print(f"订单创建成功: {result}")
        except Exception as e:
            print(f"订单创建失败: {e}")
            if hasattr(e, 'context') and e.context.get('upstream_errors'):
                print("上游服务错误:")
                for error in e.context['upstream_errors']:
                    print(f"  - {error.service_name}: {error.message}")
    
    print("微服务异常传播示例已配置")
    # demonstrate_microservice_usage()  # 注释掉实际调用，因为需要真实的服务

demonstrate_microservice_exception_propagation()
```

## 学习要点总结

### 核心原则

1. **异常层次化设计**
   - 建立清晰的异常继承体系
   - 区分客户端错误和服务端错误
   - 提供丰富的异常上下文信息

2. **异常处理策略**
   - 快速失败 vs 容错处理
   - 重试机制和指数退避
   - 降级和熔断策略

3. **性能考虑**
   - 异常缓存和复用
   - 延迟信息收集
   - 性能监控和优化

4. **测试策略**
   - 全面的异常场景测试
   - 异常处理覆盖率跟踪
   - 模拟和场景测试

### 实际应用

1. **Web API设计**
   - 统一的错误响应格式
   - 适当的HTTP状态码
   - 详细的错误信息

2. **微服务架构**
   - 异常传播和上下文保持
   - 分布式追踪
   - 服务间错误处理

3. **系统监控**
   - 异常指标收集
   - 告警和通知
   - 错误分析和优化

### 最佳实践建议

1. **设计时考虑异常**
   - 在系统设计阶段就考虑异常处理
   - 定义清晰的错误码和消息
   - 建立异常处理规范

2. **平衡性能和可维护性**
   - 避免过度的异常处理
   - 合理使用异常缓存
   - 监控异常处理性能

3. **持续改进**
   - 定期审查异常处理逻辑
   - 分析异常模式和趋势
   - 优化异常处理策略

## 下一步学习

1. **深入学习**
   - 研究具体框架的异常处理机制
   - 学习分布式系统的错误处理模式
   - 掌握异常监控和分析工具

2. **实践项目**
   - 在实际项目中应用这些最佳实践
   - 建立项目的异常处理规范
   - 实现异常监控和告警系统

3. **扩展学习**
   - 学习其他语言的异常处理机制
   - 研究云原生环境下的错误处理
   - 掌握可观测性和错误追踪技术