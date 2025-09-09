# 03. 多异常处理

## 学习目标

- 掌握处理多种异常类型的不同方法
- 理解异常捕获的优先级和顺序
- 学会设计灵活的异常处理策略
- 掌握异常分组和分类处理技巧

## 多异常处理的基本方法

### 1. 多个except子句

```python
def process_user_input(user_input):
    """处理用户输入的多种异常情况"""
    try:
        # 尝试转换为数字
        number = float(user_input)
        
        # 尝试进行计算
        result = 100 / number
        
        # 尝试访问列表
        my_list = [1, 2, 3, 4, 5]
        index = int(number)
        value = my_list[index]
        
        return {
            'input': user_input,
            'number': number,
            'division_result': result,
            'list_value': value
        }
        
    except ValueError as e:
        print(f"输入格式错误: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"除零错误: {e}")
        return None
    except IndexError as e:
        print(f"索引超出范围: {e}")
        return None
    except TypeError as e:
        print(f"类型错误: {e}")
        return None

# 测试不同输入
test_inputs = ["2.5", "abc", "0", "10", None]
for inp in test_inputs:
    print(f"\n输入: {inp}")
    result = process_user_input(inp)
    if result:
        print(f"处理成功: {result}")
```

### 2. 单个except捕获多种异常

```python
def safe_file_operations(filename, content=None):
    """安全的文件操作，统一处理相关异常"""
    try:
        if content is None:
            # 读取文件
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            # 写入文件
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
                return f"成功写入 {len(content)} 个字符"
                
    except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
        # 统一处理文件系统相关错误
        print(f"文件系统错误: {type(e).__name__} - {e}")
        return None
    except (UnicodeDecodeError, UnicodeEncodeError) as e:
        # 统一处理编码相关错误
        print(f"编码错误: {type(e).__name__} - {e}")
        return None
    except OSError as e:
        # 处理其他操作系统错误
        print(f"操作系统错误: {e}")
        return None

# 测试文件操作
print("=== 读取不存在的文件 ===")
result = safe_file_operations("nonexistent.txt")

print("\n=== 写入文件 ===")
result = safe_file_operations("test.txt", "Hello, World!")
if result:
    print(result)

print("\n=== 读取刚创建的文件 ===")
result = safe_file_operations("test.txt")
if result:
    print(f"文件内容: {result}")
```

### 3. 混合异常处理策略

```python
def advanced_data_processing(data_source):
    """高级数据处理，混合使用不同的异常处理策略"""
    try:
        # 第一步：数据获取
        if isinstance(data_source, str):
            # 从文件读取
            with open(data_source, 'r') as f:
                raw_data = f.read()
        elif isinstance(data_source, (list, tuple)):
            # 直接使用列表数据
            raw_data = str(data_source)
        else:
            # 尝试转换为字符串
            raw_data = str(data_source)
        
        # 第二步：数据解析
        import json
        if raw_data.strip().startswith('[') or raw_data.strip().startswith('{'):
            parsed_data = json.loads(raw_data)
        else:
            # 按行分割
            parsed_data = raw_data.strip().split('\n')
        
        # 第三步：数据处理
        if isinstance(parsed_data, list):
            result = [item.strip() for item in parsed_data if item.strip()]
        else:
            result = parsed_data
        
        return result
        
    except (FileNotFoundError, PermissionError) as e:
        # 文件相关错误 - 提供替代方案
        print(f"文件访问错误: {e}")
        print("尝试使用默认数据...")
        return ["default", "data"]
        
    except json.JSONDecodeError as e:
        # JSON解析错误 - 尝试其他解析方式
        print(f"JSON解析失败: {e}")
        print("尝试按行解析...")
        try:
            return raw_data.strip().split('\n')
        except:
            return ["parse_error"]
            
    except (ValueError, TypeError) as e:
        # 数据类型错误 - 记录并返回错误信息
        print(f"数据处理错误: {e}")
        return None
        
    except Exception as e:
        # 未预期的错误 - 详细记录
        print(f"未知错误: {type(e).__name__} - {e}")
        import traceback
        traceback.print_exc()
        return None

# 测试不同数据源
test_sources = [
    '["item1", "item2", "item3"]',  # JSON字符串
    "line1\nline2\nline3",           # 普通文本
    ["list", "item", "data"],       # 列表
    "nonexistent_file.txt",         # 不存在的文件
    None,                            # None值
]

for i, source in enumerate(test_sources):
    print(f"\n=== 测试 {i+1}: {type(source).__name__} ===")
    result = advanced_data_processing(source)
    print(f"处理结果: {result}")
```

## 异常捕获的优先级和顺序

### 1. 异常继承层次的影响

```python
def demonstrate_exception_order():
    """演示异常捕获顺序的重要性"""
    
    # 错误的顺序 - 父类异常在前
    def bad_order_example(test_case):
        try:
            if test_case == 1:
                raise IndexError("索引错误")
            elif test_case == 2:
                raise KeyError("键错误")
            elif test_case == 3:
                raise ValueError("值错误")
        except Exception as e:  # 父类在前，会捕获所有异常
            print(f"捕获到通用异常: {type(e).__name__}")
        except IndexError as e:  # 这个永远不会执行
            print(f"捕获到索引错误: {e}")
        except KeyError as e:    # 这个也永远不会执行
            print(f"捕获到键错误: {e}")
    
    # 正确的顺序 - 子类异常在前
    def good_order_example(test_case):
        try:
            if test_case == 1:
                raise IndexError("索引错误")
            elif test_case == 2:
                raise KeyError("键错误")
            elif test_case == 3:
                raise ValueError("值错误")
        except IndexError as e:
            print(f"捕获到索引错误: {e}")
        except KeyError as e:
            print(f"捕获到键错误: {e}")
        except ValueError as e:
            print(f"捕获到值错误: {e}")
        except Exception as e:  # 通用异常在最后
            print(f"捕获到其他异常: {type(e).__name__}")
    
    print("=== 错误的异常顺序 ===")
    for i in range(1, 4):
        print(f"测试用例 {i}:")
        bad_order_example(i)
    
    print("\n=== 正确的异常顺序 ===")
    for i in range(1, 4):
        print(f"测试用例 {i}:")
        good_order_example(i)

demonstrate_exception_order()
```

### 2. 异常层次结构的利用

```python
def hierarchical_exception_handling():
    """利用异常层次结构进行分层处理"""
    
    def risky_operation(operation_type):
        """模拟可能出现各种异常的操作"""
        operations = {
            'lookup_index': lambda: [1, 2, 3][10],
            'lookup_key': lambda: {'a': 1}['z'],
            'arithmetic': lambda: 10 / 0,
            'type_error': lambda: "string" + 5,
            'value_error': lambda: int("abc"),
            'custom_error': lambda: exec('raise RuntimeError("自定义运行时错误")')
        }
        
        if operation_type in operations:
            operations[operation_type]()
        else:
            raise ValueError(f"未知操作类型: {operation_type}")
    
    test_operations = [
        'lookup_index', 'lookup_key', 'arithmetic', 
        'type_error', 'value_error', 'custom_error', 'unknown'
    ]
    
    for op in test_operations:
        print(f"\n执行操作: {op}")
        try:
            risky_operation(op)
        except LookupError as e:
            # 捕获所有查找相关错误（IndexError, KeyError等）
            print(f"  查找错误: {type(e).__name__} - {e}")
        except ArithmeticError as e:
            # 捕获所有算术相关错误（ZeroDivisionError等）
            print(f"  算术错误: {type(e).__name__} - {e}")
        except (TypeError, ValueError) as e:
            # 捕获类型和值错误
            print(f"  数据错误: {type(e).__name__} - {e}")
        except RuntimeError as e:
            # 捕获运行时错误
            print(f"  运行时错误: {e}")
        except Exception as e:
            # 捕获其他所有异常
            print(f"  其他错误: {type(e).__name__} - {e}")

hierarchical_exception_handling()
```

## 异常分组和分类处理

### 1. 按功能分组处理异常

```python
class DataProcessor:
    """数据处理器，演示按功能分组的异常处理"""
    
    def __init__(self):
        self.processed_count = 0
        self.error_count = 0
    
    def process_data_item(self, item):
        """处理单个数据项"""
        try:
            # 数据验证阶段
            validated_item = self._validate_item(item)
            
            # 数据转换阶段
            transformed_item = self._transform_item(validated_item)
            
            # 数据存储阶段
            result = self._store_item(transformed_item)
            
            self.processed_count += 1
            return result
            
        except (ValueError, TypeError) as e:
            # 数据验证错误
            print(f"数据验证失败: {e}")
            self.error_count += 1
            return self._handle_validation_error(item, e)
            
        except (KeyError, AttributeError) as e:
            # 数据结构错误
            print(f"数据结构错误: {e}")
            self.error_count += 1
            return self._handle_structure_error(item, e)
            
        except (IOError, OSError) as e:
            # 存储相关错误
            print(f"存储错误: {e}")
            self.error_count += 1
            return self._handle_storage_error(item, e)
            
        except Exception as e:
            # 未预期错误
            print(f"未知错误: {type(e).__name__} - {e}")
            self.error_count += 1
            return self._handle_unknown_error(item, e)
    
    def _validate_item(self, item):
        """验证数据项"""
        if item is None:
            raise ValueError("数据项不能为None")
        if not isinstance(item, dict):
            raise TypeError(f"期望dict类型，得到{type(item).__name__}")
        if 'id' not in item:
            raise KeyError("缺少必需的'id'字段")
        return item
    
    def _transform_item(self, item):
        """转换数据项"""
        transformed = item.copy()
        transformed['processed_at'] = "2024-01-01"
        
        # 模拟可能的转换错误
        if 'value' in item:
            try:
                transformed['numeric_value'] = float(item['value'])
            except (ValueError, TypeError):
                raise ValueError(f"无法转换value字段: {item['value']}")
        
        return transformed
    
    def _store_item(self, item):
        """存储数据项（模拟）"""
        # 模拟存储操作
        if item.get('id') == 'error_storage':
            raise IOError("模拟存储失败")
        
        return f"已存储项目: {item['id']}"
    
    def _handle_validation_error(self, item, error):
        """处理验证错误"""
        return f"验证失败的项目: {item} - {error}"
    
    def _handle_structure_error(self, item, error):
        """处理结构错误"""
        return f"结构错误的项目: {item} - {error}"
    
    def _handle_storage_error(self, item, error):
        """处理存储错误"""
        return f"存储失败的项目: {item} - {error}"
    
    def _handle_unknown_error(self, item, error):
        """处理未知错误"""
        import traceback
        traceback.print_exc()
        return f"未知错误的项目: {item} - {error}"
    
    def get_statistics(self):
        """获取处理统计信息"""
        total = self.processed_count + self.error_count
        return {
            'total': total,
            'processed': self.processed_count,
            'errors': self.error_count,
            'success_rate': self.processed_count / total if total > 0 else 0
        }

# 测试数据处理器
processor = DataProcessor()

test_data = [
    {'id': '001', 'value': '123'},           # 正常数据
    {'id': '002', 'value': 'abc'},           # 值转换错误
    {'id': '003'},                           # 缺少value字段（正常）
    None,                                    # 验证错误
    "not_a_dict",                           # 类型错误
    {'name': 'test'},                        # 缺少id字段
    {'id': 'error_storage', 'value': '456'}, # 存储错误
]

print("=== 批量处理数据 ===")
for i, item in enumerate(test_data):
    print(f"\n处理项目 {i+1}:")
    result = processor.process_data_item(item)
    print(f"结果: {result}")

print(f"\n=== 处理统计 ===")
stats = processor.get_statistics()
for key, value in stats.items():
    print(f"{key}: {value}")
```

### 2. 按严重程度分类处理

```python
class SeverityBasedExceptionHandler:
    """基于严重程度的异常处理器"""
    
    def __init__(self):
        self.critical_errors = []
        self.warnings = []
        self.info_messages = []
    
    def execute_operation(self, operation_name, operation_func):
        """执行操作并按严重程度处理异常"""
        try:
            result = operation_func()
            self.info_messages.append(f"{operation_name}: 执行成功")
            return result
            
        except (SystemExit, KeyboardInterrupt) as e:
            # 严重错误 - 系统级别
            self._handle_critical_error(operation_name, e)
            raise  # 重新抛出系统级异常
            
        except (MemoryError, RecursionError) as e:
            # 严重错误 - 资源耗尽
            self._handle_critical_error(operation_name, e)
            return None
            
        except (FileNotFoundError, PermissionError, ConnectionError) as e:
            # 中等错误 - 外部资源问题
            self._handle_warning(operation_name, e)
            return self._get_fallback_result(operation_name)
            
        except (ValueError, TypeError, KeyError, IndexError) as e:
            # 轻微错误 - 数据问题
            self._handle_info(operation_name, e)
            return self._get_default_result(operation_name)
            
        except Exception as e:
            # 未知错误 - 按严重处理
            self._handle_critical_error(operation_name, e)
            return None
    
    def _handle_critical_error(self, operation, error):
        """处理严重错误"""
        error_info = {
            'operation': operation,
            'error_type': type(error).__name__,
            'error_message': str(error),
            'timestamp': '2024-01-01 12:00:00'
        }
        self.critical_errors.append(error_info)
        print(f"🚨 严重错误 - {operation}: {error}")
    
    def _handle_warning(self, operation, error):
        """处理警告级别错误"""
        warning_info = {
            'operation': operation,
            'error_type': type(error).__name__,
            'error_message': str(error),
            'timestamp': '2024-01-01 12:00:00'
        }
        self.warnings.append(warning_info)
        print(f"⚠️  警告 - {operation}: {error}")
    
    def _handle_info(self, operation, error):
        """处理信息级别错误"""
        info = {
            'operation': operation,
            'error_type': type(error).__name__,
            'error_message': str(error),
            'timestamp': '2024-01-01 12:00:00'
        }
        self.info_messages.append(info)
        print(f"ℹ️  信息 - {operation}: {error}")
    
    def _get_fallback_result(self, operation):
        """获取备用结果"""
        fallback_results = {
            'read_config': {'default': True},
            'connect_database': 'offline_mode',
            'fetch_data': []
        }
        return fallback_results.get(operation, 'fallback_result')
    
    def _get_default_result(self, operation):
        """获取默认结果"""
        default_results = {
            'parse_data': {},
            'calculate': 0,
            'validate': False
        }
        return default_results.get(operation, 'default_result')
    
    def get_error_summary(self):
        """获取错误摘要"""
        return {
            'critical_count': len(self.critical_errors),
            'warning_count': len(self.warnings),
            'info_count': len(self.info_messages),
            'critical_errors': self.critical_errors,
            'warnings': self.warnings,
            'info_messages': self.info_messages
        }

# 测试严重程度分类处理
handler = SeverityBasedExceptionHandler()

# 定义测试操作
test_operations = {
    'normal_operation': lambda: "success",
    'value_error': lambda: int("abc"),
    'file_error': lambda: open("nonexistent.txt").read(),
    'memory_error': lambda: exec('raise MemoryError("内存不足")'),
    'unknown_error': lambda: exec('raise RuntimeError("未知运行时错误")')
}

print("=== 按严重程度处理异常 ===")
for op_name, op_func in test_operations.items():
    print(f"\n执行操作: {op_name}")
    result = handler.execute_operation(op_name, op_func)
    print(f"返回结果: {result}")

print(f"\n=== 错误摘要 ===")
summary = handler.get_error_summary()
print(f"严重错误: {summary['critical_count']}")
print(f"警告: {summary['warning_count']}")
print(f"信息: {summary['info_count']}")
```

## 实际应用场景

### 1. Web API错误处理

```python
class APIErrorHandler:
    """Web API的多异常处理示例"""
    
    def handle_api_request(self, request_data):
        """处理API请求的多种异常情况"""
        try:
            # 请求验证
            self._validate_request(request_data)
            
            # 业务逻辑处理
            result = self._process_business_logic(request_data)
            
            # 数据库操作
            saved_result = self._save_to_database(result)
            
            return {
                'status': 'success',
                'data': saved_result,
                'code': 200
            }
            
        except (ValueError, KeyError) as e:
            # 客户端错误 - 400系列
            return {
                'status': 'error',
                'message': f'请求数据无效: {e}',
                'code': 400
            }
            
        except PermissionError as e:
            # 权限错误 - 403
            return {
                'status': 'error',
                'message': f'权限不足: {e}',
                'code': 403
            }
            
        except FileNotFoundError as e:
            # 资源不存在 - 404
            return {
                'status': 'error',
                'message': f'资源不存在: {e}',
                'code': 404
            }
            
        except (ConnectionError, TimeoutError) as e:
            # 服务不可用 - 503
            return {
                'status': 'error',
                'message': f'服务暂时不可用: {e}',
                'code': 503
            }
            
        except Exception as e:
            # 服务器内部错误 - 500
            import traceback
            traceback.print_exc()
            return {
                'status': 'error',
                'message': '服务器内部错误',
                'code': 500,
                'debug_info': str(e) if __debug__ else None
            }
    
    def _validate_request(self, request_data):
        """验证请求数据"""
        if not request_data:
            raise ValueError("请求数据不能为空")
        if 'user_id' not in request_data:
            raise KeyError("缺少user_id字段")
        if not isinstance(request_data['user_id'], (int, str)):
            raise ValueError("user_id必须是数字或字符串")
    
    def _process_business_logic(self, request_data):
        """处理业务逻辑"""
        user_id = request_data['user_id']
        
        # 模拟权限检查
        if user_id == 'forbidden':
            raise PermissionError("用户被禁止访问")
        
        # 模拟资源查找
        if user_id == 'notfound':
            raise FileNotFoundError("用户不存在")
        
        return {'processed_user_id': user_id, 'timestamp': '2024-01-01'}
    
    def _save_to_database(self, data):
        """保存到数据库"""
        # 模拟数据库连接问题
        if data.get('processed_user_id') == 'connection_error':
            raise ConnectionError("数据库连接失败")
        
        # 模拟保存成功
        return {'id': 123, **data}

# 测试API错误处理
api_handler = APIErrorHandler()

test_requests = [
    {'user_id': '123'},                    # 正常请求
    {},                                    # 缺少数据
    {'user_id': None},                     # 无效user_id
    {'user_id': 'forbidden'},              # 权限错误
    {'user_id': 'notfound'},               # 资源不存在
    {'user_id': 'connection_error'},       # 连接错误
]

print("=== API多异常处理测试 ===")
for i, request in enumerate(test_requests):
    print(f"\n请求 {i+1}: {request}")
    response = api_handler.handle_api_request(request)
    print(f"响应: {response}")
```

## 学习要点总结

### 核心技巧
1. **多种处理方式**: 可以用多个except、单个except捕获多种异常、或混合策略
2. **异常顺序**: 子类异常要在父类异常之前捕获
3. **分组处理**: 按功能、严重程度或业务逻辑分组处理异常
4. **层次利用**: 利用异常继承层次进行分层处理

### 设计原则
1. **具体优先**: 优先处理具体的异常类型
2. **分类处理**: 根据异常性质采用不同的处理策略
3. **优雅降级**: 提供合理的备用方案和默认值
4. **信息记录**: 记录足够的信息用于调试和监控

### 实际应用
- Web API的错误响应处理
- 数据处理管道的异常管理
- 文件操作的多重保护
- 网络请求的容错处理

## 下一步学习

掌握了多异常处理技巧后，接下来将学习：
- [04. else和finally子句](./04_else_finally.md) - 完整的异常处理结构
- [05. 抛出异常](./05_raise_exception.md) - 主动抛出和传播异常
- [06. 自定义异常](./06_custom_exceptions.md) - 创建业务相关的异常类

通过掌握多异常处理技巧，你可以构建更加健壮和用户友好的异常处理系统，有效应对复杂的错误场景。