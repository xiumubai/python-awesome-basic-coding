# 08. 异常日志记录

## 学习目标

- 掌握Python logging模块的基本使用
- 学会记录异常信息和堆栈跟踪
- 理解不同日志级别的使用场景
- 掌握结构化日志记录的最佳实践
- 学会配置日志格式和输出目标
- 理解异常监控和告警机制

## 基础异常日志记录

### 1. 基本日志配置和异常记录

```python
import logging
import traceback
import sys
from datetime import datetime

def demonstrate_basic_exception_logging():
    """演示基本的异常日志记录"""
    
    # 配置基本日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('application.log')
        ]
    )
    
    logger = logging.getLogger(__name__)
    
    def risky_operation(data):
        """有风险的操作"""
        if not data:
            raise ValueError("数据不能为空")
        
        if not isinstance(data, dict):
            raise TypeError(f"期望字典类型，得到 {type(data).__name__}")
        
        if 'error' in data:
            raise RuntimeError(f"处理错误: {data['error']}")
        
        return f"处理成功: {data}"
    
    def demonstrate_different_logging_methods():
        """演示不同的日志记录方法"""
        test_cases = [
            (None, "空数据测试"),
            ("invalid_type", "类型错误测试"),
            ({'error': '模拟错误'}, "运行时错误测试"),
            ({'data': 'valid'}, "正常数据测试")
        ]
        
        for data, description in test_cases:
            logger.info(f"开始测试: {description}")
            
            try:
                result = risky_operation(data)
                logger.info(f"操作成功: {result}")
                
            except ValueError as e:
                # 方法1: 基本异常记录
                logger.error(f"值错误: {e}")
                
                # 方法2: 记录异常类型和消息
                logger.error(f"异常类型: {type(e).__name__}, 消息: {e}")
                
            except TypeError as e:
                # 方法3: 使用exc_info参数记录完整堆栈
                logger.error(f"类型错误: {e}", exc_info=True)
                
            except RuntimeError as e:
                # 方法4: 使用exception()方法（自动包含堆栈信息）
                logger.exception(f"运行时错误: {e}")
                
            except Exception as e:
                # 方法5: 手动格式化异常信息
                exc_type, exc_value, exc_traceback = sys.exc_info()
                logger.error(
                    f"未预期的异常:\n"
                    f"  类型: {exc_type.__name__}\n"
                    f"  消息: {exc_value}\n"
                    f"  文件: {exc_traceback.tb_frame.f_code.co_filename}\n"
                    f"  行号: {exc_traceback.tb_lineno}"
                )
                
                # 方法6: 使用traceback模块
                tb_str = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
                logger.error(f"完整堆栈跟踪:\n{tb_str}")
            
            logger.info(f"完成测试: {description}\n")
    
    demonstrate_different_logging_methods()

demonstrate_basic_exception_logging()
```

### 2. 结构化异常日志记录

```python
def demonstrate_structured_exception_logging():
    """演示结构化异常日志记录"""
    
    import json
    import uuid
    from typing import Dict, Any, Optional
    
    class StructuredLogger:
        """结构化日志记录器"""
        
        def __init__(self, name: str):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.INFO)
            
            # 创建结构化格式化器
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            
            # 控制台处理器
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
            
            # 文件处理器（JSON格式）
            file_handler = logging.FileHandler('structured_logs.jsonl')
            json_formatter = self.JSONFormatter()
            file_handler.setFormatter(json_formatter)
            self.logger.addHandler(file_handler)
        
        class JSONFormatter(logging.Formatter):
            """JSON格式化器"""
            
            def format(self, record):
                log_entry = {
                    'timestamp': datetime.fromtimestamp(record.created).isoformat(),
                    'level': record.levelname,
                    'logger': record.name,
                    'message': record.getMessage(),
                    'module': record.module,
                    'function': record.funcName,
                    'line': record.lineno
                }
                
                # 添加异常信息
                if record.exc_info:
                    log_entry['exception'] = {
                        'type': record.exc_info[0].__name__,
                        'message': str(record.exc_info[1]),
                        'traceback': traceback.format_exception(*record.exc_info)
                    }
                
                # 添加自定义字段
                if hasattr(record, 'custom_fields'):
                    log_entry.update(record.custom_fields)
                
                return json.dumps(log_entry, ensure_ascii=False)
        
        def log_exception(self, level: str, message: str, 
                         exception: Optional[Exception] = None,
                         **kwargs):
            """记录异常日志"""
            extra = {'custom_fields': kwargs}
            
            if exception:
                # 手动添加异常信息
                extra['custom_fields']['exception_info'] = {
                    'type': type(exception).__name__,
                    'message': str(exception),
                    'args': exception.args
                }
                
                # 如果异常有自定义属性，也记录下来
                if hasattr(exception, '__dict__'):
                    custom_attrs = {k: v for k, v in exception.__dict__.items() 
                                  if not k.startswith('_')}
                    if custom_attrs:
                        extra['custom_fields']['exception_attributes'] = custom_attrs
            
            getattr(self.logger, level.lower())(message, extra=extra, exc_info=exception is not None)
        
        def log_operation(self, operation: str, status: str, 
                         duration: Optional[float] = None,
                         **context):
            """记录操作日志"""
            extra = {
                'custom_fields': {
                    'operation': operation,
                    'status': status,
                    'duration_ms': duration * 1000 if duration else None,
                    **context
                }
            }
            
            level = 'info' if status == 'success' else 'error'
            message = f"Operation {operation} {status}"
            
            getattr(self.logger, level)(message, extra=extra)
    
    # 自定义异常类
    class BusinessError(Exception):
        """业务错误"""
        
        def __init__(self, message, error_code=None, user_id=None, context=None):
            super().__init__(message)
            self.error_code = error_code
            self.user_id = user_id
            self.context = context or {}
    
    class ValidationError(Exception):
        """验证错误"""
        
        def __init__(self, message, field=None, value=None, rule=None):
            super().__init__(message)
            self.field = field
            self.value = value
            self.rule = rule
    
    # 业务服务类
    class UserService:
        """用户服务"""
        
        def __init__(self):
            self.logger = StructuredLogger('UserService')
        
        def validate_user_data(self, user_data: Dict[str, Any]) -> bool:
            """验证用户数据"""
            operation_id = str(uuid.uuid4())
            start_time = datetime.now()
            
            try:
                self.logger.log_operation(
                    'validate_user_data',
                    'started',
                    operation_id=operation_id,
                    input_data=user_data
                )
                
                # 验证必需字段
                required_fields = ['name', 'email', 'age']
                for field in required_fields:
                    if field not in user_data:
                        raise ValidationError(
                            f"缺少必需字段: {field}",
                            field=field,
                            value=None,
                            rule='required'
                        )
                
                # 验证邮箱格式
                email = user_data.get('email', '')
                if '@' not in email or '.' not in email:
                    raise ValidationError(
                        f"邮箱格式无效: {email}",
                        field='email',
                        value=email,
                        rule='email_format'
                    )
                
                # 验证年龄范围
                age = user_data.get('age')
                if not isinstance(age, int) or age < 0 or age > 150:
                    raise ValidationError(
                        f"年龄必须是0-150之间的整数: {age}",
                        field='age',
                        value=age,
                        rule='age_range'
                    )
                
                duration = (datetime.now() - start_time).total_seconds()
                self.logger.log_operation(
                    'validate_user_data',
                    'success',
                    duration=duration,
                    operation_id=operation_id
                )
                
                return True
                
            except ValidationError as e:
                duration = (datetime.now() - start_time).total_seconds()
                self.logger.log_exception(
                    'warning',
                    f"用户数据验证失败: {e}",
                    exception=e,
                    operation_id=operation_id,
                    duration_ms=duration * 1000,
                    validation_field=e.field,
                    validation_rule=e.rule,
                    input_value=e.value
                )
                raise
            
            except Exception as e:
                duration = (datetime.now() - start_time).total_seconds()
                self.logger.log_exception(
                    'error',
                    f"用户数据验证时发生未预期错误: {e}",
                    exception=e,
                    operation_id=operation_id,
                    duration_ms=duration * 1000,
                    input_data=user_data
                )
                raise
        
        def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
            """创建用户"""
            operation_id = str(uuid.uuid4())
            start_time = datetime.now()
            
            try:
                self.logger.log_operation(
                    'create_user',
                    'started',
                    operation_id=operation_id,
                    user_email=user_data.get('email', 'unknown')
                )
                
                # 验证用户数据
                self.validate_user_data(user_data)
                
                # 检查用户是否已存在
                if user_data.get('email') == 'existing@example.com':
                    raise BusinessError(
                        f"用户已存在: {user_data['email']}",
                        error_code='USER_ALREADY_EXISTS',
                        user_id=None,
                        context={
                            'email': user_data['email'],
                            'attempted_creation_time': datetime.now().isoformat()
                        }
                    )
                
                # 模拟数据库操作
                import random
                if random.random() < 0.3:  # 30% 概率模拟数据库错误
                    raise ConnectionError("数据库连接失败")
                
                # 创建成功
                user_id = f"user_{hash(user_data['email']) % 10000:04d}"
                result = {
                    'user_id': user_id,
                    'email': user_data['email'],
                    'name': user_data['name'],
                    'created_at': datetime.now().isoformat()
                }
                
                duration = (datetime.now() - start_time).total_seconds()
                self.logger.log_operation(
                    'create_user',
                    'success',
                    duration=duration,
                    operation_id=operation_id,
                    user_id=user_id,
                    user_email=user_data['email']
                )
                
                return result
                
            except ValidationError as e:
                duration = (datetime.now() - start_time).total_seconds()
                self.logger.log_exception(
                    'warning',
                    f"用户创建失败 - 验证错误: {e}",
                    exception=e,
                    operation_id=operation_id,
                    duration_ms=duration * 1000,
                    user_email=user_data.get('email', 'unknown'),
                    error_category='validation'
                )
                raise
            
            except BusinessError as e:
                duration = (datetime.now() - start_time).total_seconds()
                self.logger.log_exception(
                    'warning',
                    f"用户创建失败 - 业务错误: {e}",
                    exception=e,
                    operation_id=operation_id,
                    duration_ms=duration * 1000,
                    user_email=user_data.get('email', 'unknown'),
                    error_category='business',
                    error_code=e.error_code
                )
                raise
            
            except ConnectionError as e:
                duration = (datetime.now() - start_time).total_seconds()
                self.logger.log_exception(
                    'error',
                    f"用户创建失败 - 数据库连接错误: {e}",
                    exception=e,
                    operation_id=operation_id,
                    duration_ms=duration * 1000,
                    user_email=user_data.get('email', 'unknown'),
                    error_category='infrastructure',
                    retry_recommended=True
                )
                raise
            
            except Exception as e:
                duration = (datetime.now() - start_time).total_seconds()
                self.logger.log_exception(
                    'error',
                    f"用户创建失败 - 未预期错误: {e}",
                    exception=e,
                    operation_id=operation_id,
                    duration_ms=duration * 1000,
                    user_email=user_data.get('email', 'unknown'),
                    error_category='unknown'
                )
                raise
    
    def demonstrate_structured_logging():
        """演示结构化日志记录"""
        user_service = UserService()
        
        test_cases = [
            ({'name': 'Alice', 'email': 'alice@example.com', 'age': 25}, "正常用户数据"),
            ({'name': 'Bob', 'email': 'invalid-email', 'age': 30}, "无效邮箱格式"),
            ({'name': 'Charlie', 'age': 35}, "缺少邮箱字段"),
            ({'name': 'David', 'email': 'david@example.com', 'age': -5}, "无效年龄"),
            ({'name': 'Eve', 'email': 'existing@example.com', 'age': 28}, "用户已存在"),
            ({'name': 'Frank', 'email': 'frank@example.com', 'age': 40}, "可能的数据库错误")
        ]
        
        for user_data, description in test_cases:
            print(f"\n{'='*60}")
            print(f"测试: {description}")
            print(f"数据: {user_data}")
            print(f"{'='*60}")
            
            try:
                result = user_service.create_user(user_data)
                print(f"✅ 用户创建成功: {result['user_id']}")
            except (ValidationError, BusinessError, ConnectionError) as e:
                print(f"❌ 用户创建失败: {type(e).__name__}: {e}")
            except Exception as e:
                print(f"💥 未预期错误: {type(e).__name__}: {e}")
    
    demonstrate_structured_logging()

demonstrate_structured_exception_logging()
```

## 高级日志记录技术

### 1. 异常上下文和相关性追踪

```python
def demonstrate_advanced_exception_logging():
    """演示高级异常日志记录技术"""
    
    import threading
    import contextvars
    from functools import wraps
    from typing import Callable, Any
    
    # 上下文变量用于追踪请求
    request_id_var = contextvars.ContextVar('request_id')
    user_id_var = contextvars.ContextVar('user_id')
    operation_stack_var = contextvars.ContextVar('operation_stack', default=[])
    
    class ContextualLogger:
        """上下文感知的日志记录器"""
        
        def __init__(self, name: str):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.INFO)
            
            # 创建自定义格式化器
            formatter = self.ContextualFormatter()
            
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        
        class ContextualFormatter(logging.Formatter):
            """上下文感知的格式化器"""
            
            def format(self, record):
                # 获取上下文信息
                try:
                    request_id = request_id_var.get()
                    user_id = user_id_var.get()
                    operation_stack = operation_stack_var.get()
                except LookupError:
                    request_id = None
                    user_id = None
                    operation_stack = []
                
                # 构建上下文字符串
                context_parts = []
                if request_id:
                    context_parts.append(f"req:{request_id}")
                if user_id:
                    context_parts.append(f"user:{user_id}")
                if operation_stack:
                    context_parts.append(f"ops:{'>'.join(operation_stack)}")
                
                context_str = f"[{','.join(context_parts)}]" if context_parts else ""
                
                # 格式化基本信息
                base_format = f"%(asctime)s - %(name)s - %(levelname)s {context_str} - %(message)s"
                formatter = logging.Formatter(base_format)
                
                return formatter.format(record)
        
        def log_with_context(self, level: str, message: str, **kwargs):
            """带上下文的日志记录"""
            # 添加上下文信息到消息中
            context_info = []
            
            try:
                request_id = request_id_var.get()
                context_info.append(f"request_id={request_id}")
            except LookupError:
                pass
            
            try:
                user_id = user_id_var.get()
                context_info.append(f"user_id={user_id}")
            except LookupError:
                pass
            
            if kwargs:
                context_info.extend(f"{k}={v}" for k, v in kwargs.items())
            
            if context_info:
                message = f"{message} ({', '.join(context_info)})"
            
            getattr(self.logger, level.lower())(message)
        
        def log_exception_with_context(self, message: str, exception: Exception, **kwargs):
            """带上下文的异常日志记录"""
            # 收集异常链信息
            exception_chain = []
            current_exc = exception
            
            while current_exc:
                exception_chain.append({
                    'type': type(current_exc).__name__,
                    'message': str(current_exc),
                    'module': getattr(current_exc, '__module__', 'unknown')
                })
                current_exc = current_exc.__cause__ or current_exc.__context__
            
            # 记录异常链
            self.log_with_context(
                'error',
                f"{message}: {exception}",
                exception_chain_length=len(exception_chain),
                root_cause=exception_chain[-1]['type'] if exception_chain else 'unknown',
                **kwargs
            )
            
            # 记录完整的异常信息
            self.logger.exception(f"Exception details for: {message}")
    
    def with_operation_context(operation_name: str):
        """操作上下文装饰器"""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                # 获取当前操作栈
                current_stack = operation_stack_var.get([])
                new_stack = current_stack + [operation_name]
                
                # 设置新的操作栈
                token = operation_stack_var.set(new_stack)
                
                try:
                    return func(*args, **kwargs)
                finally:
                    # 恢复操作栈
                    operation_stack_var.reset(token)
            
            return wrapper
        return decorator
    
    def with_request_context(request_id: str, user_id: str = None):
        """请求上下文装饰器"""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                # 设置请求上下文
                req_token = request_id_var.set(request_id)
                user_token = None
                
                if user_id:
                    user_token = user_id_var.set(user_id)
                
                try:
                    return func(*args, **kwargs)
                finally:
                    # 清理上下文
                    request_id_var.reset(req_token)
                    if user_token:
                        user_id_var.reset(user_token)
            
            return wrapper
        return decorator
    
    # 业务服务类
    class OrderService:
        """订单服务"""
        
        def __init__(self):
            self.logger = ContextualLogger('OrderService')
        
        @with_operation_context('validate_order')
        def validate_order(self, order_data: dict) -> bool:
            """验证订单"""
            self.logger.log_with_context('info', '开始验证订单', order_id=order_data.get('id'))
            
            if not order_data.get('items'):
                raise ValueError("订单必须包含商品")
            
            if order_data.get('total', 0) <= 0:
                raise ValueError("订单总额必须大于0")
            
            self.logger.log_with_context('info', '订单验证通过')
            return True
        
        @with_operation_context('check_inventory')
        def check_inventory(self, items: list) -> bool:
            """检查库存"""
            self.logger.log_with_context('info', '开始检查库存', item_count=len(items))
            
            for item in items:
                if item.get('quantity', 0) > 100:  # 模拟库存不足
                    raise RuntimeError(f"商品 {item.get('name')} 库存不足")
            
            self.logger.log_with_context('info', '库存检查通过')
            return True
        
        @with_operation_context('calculate_price')
        def calculate_price(self, items: list) -> float:
            """计算价格"""
            self.logger.log_with_context('info', '开始计算价格')
            
            total = 0
            for item in items:
                price = item.get('price', 0)
                quantity = item.get('quantity', 0)
                
                if price < 0:
                    raise ValueError(f"商品 {item.get('name')} 价格无效: {price}")
                
                total += price * quantity
            
            self.logger.log_with_context('info', '价格计算完成', total=total)
            return total
        
        @with_operation_context('process_payment')
        def process_payment(self, payment_data: dict) -> dict:
            """处理支付"""
            self.logger.log_with_context(
                'info', 
                '开始处理支付', 
                payment_method=payment_data.get('method'),
                amount=payment_data.get('amount')
            )
            
            # 模拟支付失败
            if payment_data.get('method') == 'invalid_card':
                raise ConnectionError("支付网关连接失败")
            
            if payment_data.get('amount', 0) > 10000:
                raise PermissionError("支付金额超过限制")
            
            payment_id = f"pay_{hash(str(payment_data)) % 10000:04d}"
            result = {
                'payment_id': payment_id,
                'status': 'completed',
                'amount': payment_data.get('amount')
            }
            
            self.logger.log_with_context('info', '支付处理完成', payment_id=payment_id)
            return result
        
        @with_operation_context('create_order')
        def create_order(self, order_data: dict) -> dict:
            """创建订单"""
            self.logger.log_with_context('info', '开始创建订单')
            
            try:
                # 第一步：验证订单
                self.validate_order(order_data)
                
                # 第二步：检查库存
                self.check_inventory(order_data['items'])
                
                # 第三步：计算价格
                calculated_total = self.calculate_price(order_data['items'])
                
                # 第四步：处理支付
                payment_result = self.process_payment({
                    'method': order_data.get('payment_method', 'credit_card'),
                    'amount': calculated_total
                })
                
                # 第五步：创建订单记录
                order_id = f"order_{hash(str(order_data)) % 10000:04d}"
                result = {
                    'order_id': order_id,
                    'status': 'created',
                    'total': calculated_total,
                    'payment': payment_result
                }
                
                self.logger.log_with_context('info', '订单创建成功', order_id=order_id)
                return result
                
            except ValueError as e:
                self.logger.log_exception_with_context(
                    '订单验证失败',
                    e,
                    error_category='validation',
                    order_data=order_data
                )
                raise
            
            except RuntimeError as e:
                self.logger.log_exception_with_context(
                    '库存检查失败',
                    e,
                    error_category='inventory',
                    items=order_data.get('items', [])
                )
                raise
            
            except (ConnectionError, PermissionError) as e:
                self.logger.log_exception_with_context(
                    '支付处理失败',
                    e,
                    error_category='payment',
                    payment_method=order_data.get('payment_method'),
                    amount=order_data.get('total')
                )
                raise
            
            except Exception as e:
                self.logger.log_exception_with_context(
                    '订单创建过程中发生未预期错误',
                    e,
                    error_category='unknown',
                    order_data=order_data
                )
                raise
    
    def demonstrate_contextual_logging():
        """演示上下文感知的日志记录"""
        order_service = OrderService()
        
        test_cases = [
            (
                {
                    'id': 'ord_001',
                    'items': [{'name': '商品A', 'price': 100, 'quantity': 2}],
                    'total': 200,
                    'payment_method': 'credit_card'
                },
                'req_001',
                'user_123',
                "正常订单"
            ),
            (
                {
                    'id': 'ord_002',
                    'items': [],
                    'total': 0
                },
                'req_002',
                'user_456',
                "空订单（验证失败）"
            ),
            (
                {
                    'id': 'ord_003',
                    'items': [{'name': '商品B', 'price': 50, 'quantity': 150}],
                    'total': 7500
                },
                'req_003',
                'user_789',
                "库存不足"
            ),
            (
                {
                    'id': 'ord_004',
                    'items': [{'name': '商品C', 'price': 5000, 'quantity': 3}],
                    'total': 15000,
                    'payment_method': 'credit_card'
                },
                'req_004',
                'user_999',
                "支付金额超限"
            ),
            (
                {
                    'id': 'ord_005',
                    'items': [{'name': '商品D', 'price': 200, 'quantity': 1}],
                    'total': 200,
                    'payment_method': 'invalid_card'
                },
                'req_005',
                'user_888',
                "支付网关错误"
            )
        ]
        
        for order_data, request_id, user_id, description in test_cases:
            print(f"\n{'='*80}")
            print(f"测试场景: {description}")
            print(f"请求ID: {request_id}, 用户ID: {user_id}")
            print(f"订单数据: {order_data}")
            print(f"{'='*80}")
            
            @with_request_context(request_id, user_id)
            def process_order():
                try:
                    result = order_service.create_order(order_data)
                    print(f"✅ 订单创建成功: {result['order_id']}")
                    return result
                except Exception as e:
                    print(f"❌ 订单创建失败: {type(e).__name__}: {e}")
                    return None
            
            process_order()
    
    demonstrate_contextual_logging()

demonstrate_advanced_exception_logging()
```

### 2. 异常监控和告警系统

```python
def demonstrate_exception_monitoring():
    """演示异常监控和告警系统"""
    
    import time
    import threading
    from collections import defaultdict, deque
    from typing import Dict, List, Callable
    from dataclasses import dataclass, field
    from datetime import datetime, timedelta
    
    @dataclass
    class ExceptionEvent:
        """异常事件"""
        timestamp: datetime
        exception_type: str
        message: str
        module: str
        function: str
        line_number: int
        request_id: str = None
        user_id: str = None
        context: Dict = field(default_factory=dict)
        severity: str = 'medium'  # low, medium, high, critical
        
        def to_dict(self):
            return {
                'timestamp': self.timestamp.isoformat(),
                'exception_type': self.exception_type,
                'message': self.message,
                'module': self.module,
                'function': self.function,
                'line_number': self.line_number,
                'request_id': self.request_id,
                'user_id': self.user_id,
                'context': self.context,
                'severity': self.severity
            }
    
    class ExceptionMonitor:
        """异常监控器"""
        
        def __init__(self, window_size_minutes: int = 5):
            self.window_size = timedelta(minutes=window_size_minutes)
            self.events = deque()  # 存储异常事件
            self.exception_counts = defaultdict(int)  # 异常类型计数
            self.alert_handlers = []  # 告警处理器
            self.lock = threading.Lock()
            
            # 告警阈值配置
            self.thresholds = {
                'exception_rate': 10,  # 每分钟异常数量
                'same_exception_rate': 5,  # 相同异常每分钟数量
                'critical_exceptions': ['DatabaseError', 'SecurityError'],
                'error_rate_by_user': 3  # 单用户每分钟错误数
            }
            
            # 启动清理线程
            self.cleanup_thread = threading.Thread(target=self._cleanup_old_events, daemon=True)
            self.cleanup_thread.start()
        
        def add_alert_handler(self, handler: Callable[[str, Dict], None]):
            """添加告警处理器"""
            self.alert_handlers.append(handler)
        
        def record_exception(self, exception: Exception, context: Dict = None):
            """记录异常事件"""
            import inspect
            
            # 获取调用栈信息
            frame = inspect.currentframe().f_back
            
            # 确定异常严重程度
            severity = self._determine_severity(exception)
            
            event = ExceptionEvent(
                timestamp=datetime.now(),
                exception_type=type(exception).__name__,
                message=str(exception),
                module=frame.f_globals.get('__name__', 'unknown'),
                function=frame.f_code.co_name,
                line_number=frame.f_lineno,
                context=context or {},
                severity=severity
            )
            
            # 从上下文中提取请求和用户信息
            if context:
                event.request_id = context.get('request_id')
                event.user_id = context.get('user_id')
            
            with self.lock:
                self.events.append(event)
                self.exception_counts[event.exception_type] += 1
            
            # 检查是否需要触发告警
            self._check_alerts(event)
        
        def _determine_severity(self, exception: Exception) -> str:
            """确定异常严重程度"""
            exception_type = type(exception).__name__
            
            if exception_type in ['SecurityError', 'AuthenticationError']:
                return 'critical'
            elif exception_type in ['DatabaseError', 'ConnectionError']:
                return 'high'
            elif exception_type in ['ValidationError', 'BusinessError']:
                return 'medium'
            else:
                return 'low'
        
        def _cleanup_old_events(self):
            """清理过期事件"""
            while True:
                time.sleep(60)  # 每分钟清理一次
                
                cutoff_time = datetime.now() - self.window_size
                
                with self.lock:
                    # 移除过期事件
                    while self.events and self.events[0].timestamp < cutoff_time:
                        old_event = self.events.popleft()
                        self.exception_counts[old_event.exception_type] -= 1
                        
                        if self.exception_counts[old_event.exception_type] <= 0:
                            del self.exception_counts[old_event.exception_type]
        
        def _check_alerts(self, event: ExceptionEvent):
            """检查是否需要触发告警"""
            current_time = datetime.now()
            window_start = current_time - timedelta(minutes=1)
            
            with self.lock:
                recent_events = [e for e in self.events if e.timestamp >= window_start]
            
            # 检查总异常率
            if len(recent_events) >= self.thresholds['exception_rate']:
                self._trigger_alert(
                    'HIGH_EXCEPTION_RATE',
                    {
                        'rate': len(recent_events),
                        'threshold': self.thresholds['exception_rate'],
                        'window': '1 minute',
                        'latest_event': event.to_dict()
                    }
                )
            
            # 检查相同异常率
            same_type_events = [e for e in recent_events if e.exception_type == event.exception_type]
            if len(same_type_events) >= self.thresholds['same_exception_rate']:
                self._trigger_alert(
                    'HIGH_SAME_EXCEPTION_RATE',
                    {
                        'exception_type': event.exception_type,
                        'rate': len(same_type_events),
                        'threshold': self.thresholds['same_exception_rate'],
                        'window': '1 minute',
                        'latest_event': event.to_dict()
                    }
                )
            
            # 检查关键异常
            if event.exception_type in self.thresholds['critical_exceptions']:
                self._trigger_alert(
                    'CRITICAL_EXCEPTION',
                    {
                        'exception_type': event.exception_type,
                        'severity': 'critical',
                        'event': event.to_dict()
                    }
                )
            
            # 检查单用户错误率
            if event.user_id:
                user_events = [e for e in recent_events if e.user_id == event.user_id]
                if len(user_events) >= self.thresholds['error_rate_by_user']:
                    self._trigger_alert(
                        'HIGH_USER_ERROR_RATE',
                        {
                            'user_id': event.user_id,
                            'rate': len(user_events),
                            'threshold': self.thresholds['error_rate_by_user'],
                            'window': '1 minute',
                            'latest_event': event.to_dict()
                        }
                    )
        
        def _trigger_alert(self, alert_type: str, data: Dict):
            """触发告警"""
            alert_data = {
                'alert_type': alert_type,
                'timestamp': datetime.now().isoformat(),
                'data': data
            }
            
            for handler in self.alert_handlers:
                try:
                    handler(alert_type, alert_data)
                except Exception as e:
                    print(f"告警处理器执行失败: {e}")
        
        def get_statistics(self) -> Dict:
            """获取统计信息"""
            with self.lock:
                current_events = list(self.events)
            
            if not current_events:
                return {'total_events': 0}
            
            # 按时间分组统计
            now = datetime.now()
            last_hour = now - timedelta(hours=1)
            last_day = now - timedelta(days=1)
            
            hour_events = [e for e in current_events if e.timestamp >= last_hour]
            day_events = [e for e in current_events if e.timestamp >= last_day]
            
            # 按异常类型统计
            type_stats = defaultdict(int)
            severity_stats = defaultdict(int)
            
            for event in current_events:
                type_stats[event.exception_type] += 1
                severity_stats[event.severity] += 1
            
            return {
                'total_events': len(current_events),
                'events_last_hour': len(hour_events),
                'events_last_day': len(day_events),
                'exception_types': dict(type_stats),
                'severity_distribution': dict(severity_stats),
                'window_size_minutes': self.window_size.total_seconds() / 60
            }
    
    # 告警处理器
    class AlertHandler:
        """告警处理器"""
        
        def __init__(self, name: str):
            self.name = name
            self.logger = logging.getLogger(f'AlertHandler.{name}')
        
        def handle_alert(self, alert_type: str, alert_data: Dict):
            """处理告警"""
            self.logger.warning(f"🚨 [{self.name}] 告警触发: {alert_type}")
            self.logger.warning(f"告警数据: {json.dumps(alert_data, indent=2, ensure_ascii=False)}")
            
            # 根据告警类型执行不同的处理逻辑
            if alert_type == 'CRITICAL_EXCEPTION':
                self._handle_critical_exception(alert_data)
            elif alert_type == 'HIGH_EXCEPTION_RATE':
                self._handle_high_exception_rate(alert_data)
            elif alert_type == 'HIGH_SAME_EXCEPTION_RATE':
                self._handle_high_same_exception_rate(alert_data)
            elif alert_type == 'HIGH_USER_ERROR_RATE':
                self._handle_high_user_error_rate(alert_data)
        
        def _handle_critical_exception(self, alert_data: Dict):
            """处理关键异常告警"""
            self.logger.critical(f"🔥 关键异常告警: {alert_data['data']['exception_type']}")
            # 这里可以集成短信、邮件、钉钉等通知方式
            print(f"📱 发送紧急通知: 系统出现关键异常 {alert_data['data']['exception_type']}")
        
        def _handle_high_exception_rate(self, alert_data: Dict):
            """处理高异常率告警"""
            rate = alert_data['data']['rate']
            threshold = alert_data['data']['threshold']
            self.logger.warning(f"⚠️ 异常率过高: {rate}/分钟 (阈值: {threshold}/分钟)")
            print(f"📊 建议检查系统负载和服务健康状态")
        
        def _handle_high_same_exception_rate(self, alert_data: Dict):
            """处理相同异常高频告警"""
            exception_type = alert_data['data']['exception_type']
            rate = alert_data['data']['rate']
            self.logger.warning(f"🔄 相同异常频发: {exception_type} ({rate}/分钟)")
            print(f"🔍 建议检查 {exception_type} 的根本原因")
        
        def _handle_high_user_error_rate(self, alert_data: Dict):
            """处理用户高错误率告警"""
            user_id = alert_data['data']['user_id']
            rate = alert_data['data']['rate']
            self.logger.warning(f"👤 用户错误率过高: {user_id} ({rate}/分钟)")
            print(f"🛡️ 建议检查用户 {user_id} 的行为模式，可能存在异常操作")
    
    # 集成监控的服务类
    class MonitoredService:
        """集成监控的服务类"""
        
        def __init__(self, name: str, monitor: ExceptionMonitor):
            self.name = name
            self.monitor = monitor
            self.logger = logging.getLogger(f'MonitoredService.{name}')
        
        def execute_with_monitoring(self, operation: str, func: Callable, *args, **kwargs):
            """带监控的执行"""
            context = {
                'service': self.name,
                'operation': operation,
                'request_id': kwargs.pop('request_id', None),
                'user_id': kwargs.pop('user_id', None)
            }
            
            try:
                self.logger.info(f"开始执行操作: {operation}")
                result = func(*args, **kwargs)
                self.logger.info(f"操作执行成功: {operation}")
                return result
                
            except Exception as e:
                self.logger.error(f"操作执行失败: {operation} - {e}")
                
                # 记录异常到监控系统
                self.monitor.record_exception(e, context)
                
                raise
    
    def demonstrate_monitoring_system():
        """演示监控系统"""
        # 创建监控器
        monitor = ExceptionMonitor(window_size_minutes=5)
        
        # 添加告警处理器
        email_handler = AlertHandler('Email')
        sms_handler = AlertHandler('SMS')
        slack_handler = AlertHandler('Slack')
        
        monitor.add_alert_handler(email_handler.handle_alert)
        monitor.add_alert_handler(sms_handler.handle_alert)
        monitor.add_alert_handler(slack_handler.handle_alert)
        
        # 创建被监控的服务
        user_service = MonitoredService('UserService', monitor)
        order_service = MonitoredService('OrderService', monitor)
        
        # 模拟各种异常场景
        def simulate_exceptions():
            """模拟异常场景"""
            
            # 场景1: 正常操作
            try:
                user_service.execute_with_monitoring(
                    'get_user',
                    lambda user_id: {'id': user_id, 'name': 'Alice'},
                    123,
                    request_id='req_001',
                    user_id='user_123'
                )
            except Exception:
                pass
            
            # 场景2: 触发高频相同异常
            for i in range(6):
                try:
                    user_service.execute_with_monitoring(
                        'validate_user',
                        lambda: (_ for _ in ()).throw(ValueError("用户数据无效")),
                        request_id=f'req_val_{i}',
                        user_id='user_456'
                    )
                except Exception:
                    pass
                time.sleep(0.1)
            
            # 场景3: 触发关键异常
            try:
                order_service.execute_with_monitoring(
                    'process_payment',
                    lambda: (_ for _ in ()).throw(type('SecurityError', (Exception,), {})('安全验证失败')),
                    request_id='req_sec_001',
                    user_id='user_789'
                )
            except Exception:
                pass
            
            # 场景4: 触发用户高错误率
            for i in range(4):
                try:
                    user_service.execute_with_monitoring(
                        'update_profile',
                        lambda: (_ for _ in ()).throw(RuntimeError(f"更新失败 {i}")),
                        request_id=f'req_update_{i}',
                        user_id='user_problem'
                    )
                except Exception:
                    pass
                time.sleep(0.1)
            
            # 场景5: 触发总体高异常率
            for i in range(12):
                try:
                    service = user_service if i % 2 == 0 else order_service
                    service.execute_with_monitoring(
                        f'operation_{i}',
                        lambda: (_ for _ in ()).throw(RuntimeError(f"批量错误 {i}")),
                        request_id=f'req_batch_{i}',
                        user_id=f'user_{i % 3}'
                    )
                except Exception:
                    pass
                time.sleep(0.05)
        
        print("开始模拟异常场景...")
        simulate_exceptions()
        
        # 等待一段时间让监控系统处理
        time.sleep(2)
        
        # 显示统计信息
        print("\n" + "="*60)
        print("监控统计信息")
        print("="*60)
        
        stats = monitor.get_statistics()
        print(f"总异常事件数: {stats['total_events']}")
        print(f"最近1小时事件数: {stats['events_last_hour']}")
        print(f"最近1天事件数: {stats['events_last_day']}")
        print(f"监控窗口大小: {stats['window_size_minutes']} 分钟")
        
        print("\n异常类型分布:")
        for exc_type, count in stats['exception_types'].items():
            print(f"  {exc_type}: {count}")
        
        print("\n严重程度分布:")
        for severity, count in stats['severity_distribution'].items():
            print(f"  {severity}: {count}")
    
    demonstrate_monitoring_system()

demonstrate_exception_monitoring()
```

## 学习要点总结

### 异常日志记录的核心原则
1. **完整性**: 记录足够的信息用于问题诊断
2. **结构化**: 使用结构化格式便于分析和查询
3. **上下文**: 包含请求ID、用户ID等上下文信息
4. **分级**: 根据异常严重程度使用不同的日志级别

### 日志记录的最佳实践
1. **异常链记录**: 记录完整的异常传播链
2. **性能考虑**: 避免日志记录影响系统性能
3. **敏感信息**: 避免记录密码、密钥等敏感信息
4. **日志轮转**: 合理配置日志文件大小和保留策略

### 监控和告警策略
1. **阈值设置**: 根据业务特点设置合理的告警阈值
2. **告警分级**: 不同严重程度的异常使用不同的通知方式
3. **防止告警风暴**: 实现告警聚合和抑制机制
4. **可观测性**: 提供丰富的统计信息和可视化界面

### 实际应用场景
1. **微服务架构**: 跨服务的异常追踪和关联
2. **生产环境**: 实时异常监控和快速响应
3. **性能优化**: 基于异常模式进行系统优化
4. **安全监控**: 检测异常的用户行为和安全威胁

## 下一步学习

掌握了异常日志记录后，接下来将学习：
- [09. 异常处理最佳实践](./09_best_practices.md) - 综合应用和最佳实践模式

通过掌握异常日志记录技术，你可以构建完善的异常监控体系，及时发现和解决系统问题，提高应用的可靠性和可维护性。