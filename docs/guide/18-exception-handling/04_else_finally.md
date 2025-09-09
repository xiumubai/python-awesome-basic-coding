# 04. else和finally子句

## 学习目标

- 掌握try-except-else-finally的完整语法结构
- 理解else子句的执行条件和使用场景
- 掌握finally子句的特性和最佳实践
- 学会设计完整的异常处理流程
- 理解资源管理和清理操作的重要性

## else子句的使用

### 1. else子句的基本概念

```python
def demonstrate_else_clause():
    """演示else子句的基本使用"""
    
    def safe_division(a, b):
        """安全除法运算，演示else子句"""
        try:
            result = a / b
        except ZeroDivisionError:
            print(f"错误: 不能除以零")
            return None
        except TypeError:
            print(f"错误: 参数类型不正确")
            return None
        else:
            # 只有在没有异常时才执行
            print(f"计算成功: {a} / {b} = {result}")
            return result
    
    # 测试不同情况
    test_cases = [
        (10, 2),      # 正常情况
        (10, 0),      # 除零错误
        ("10", 2),    # 类型错误
        (15, 3),      # 正常情况
    ]
    
    print("=== else子句演示 ===")
    for a, b in test_cases:
        print(f"\n计算 {a} / {b}:")
        result = safe_division(a, b)
        if result is not None:
            print(f"最终结果: {result}")

demonstrate_else_clause()
```

### 2. else子句的实际应用场景

```python
def file_processing_with_else():
    """文件处理中else子句的应用"""
    
    def process_config_file(filename):
        """处理配置文件"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"配置文件 {filename} 不存在，使用默认配置")
            return {'default': True}
        except PermissionError:
            print(f"没有权限读取 {filename}")
            return None
        except UnicodeDecodeError:
            print(f"配置文件 {filename} 编码错误")
            return None
        else:
            # 文件读取成功，进行后续处理
            print(f"成功读取配置文件 {filename}")
            try:
                import json
                config = json.loads(content)
                print(f"配置解析成功，包含 {len(config)} 个配置项")
                return config
            except json.JSONDecodeError:
                print("配置文件格式错误，使用默认配置")
                return {'default': True}
    
    # 测试不同的配置文件
    test_files = [
        'valid_config.json',
        'nonexistent.json',
        'invalid_format.txt'
    ]
    
    # 创建测试文件
    import json
    with open('valid_config.json', 'w') as f:
        json.dump({'debug': True, 'port': 8080, 'host': 'localhost'}, f)
    
    with open('invalid_format.txt', 'w') as f:
        f.write('这不是有效的JSON格式')
    
    print("\n=== 文件处理中的else子句 ===")
    for filename in test_files:
        print(f"\n处理文件: {filename}")
        config = process_config_file(filename)
        if config:
            print(f"获得配置: {config}")

file_processing_with_else()
```

### 3. else子句与循环的结合

```python
def search_with_else():
    """搜索操作中else子句的使用"""
    
    def find_user_by_id(user_list, target_id):
        """在用户列表中查找指定ID的用户"""
        try:
            for user in user_list:
                if not isinstance(user, dict):
                    raise TypeError(f"用户数据格式错误: {user}")
                
                if 'id' not in user:
                    raise KeyError(f"用户数据缺少id字段: {user}")
                
                if user['id'] == target_id:
                    return user
        except (TypeError, KeyError) as e:
            print(f"数据格式错误: {e}")
            return None
        else:
            # 循环正常结束，没有找到用户
            print(f"未找到ID为 {target_id} 的用户")
            return None
    
    def batch_search_users(user_list, target_ids):
        """批量搜索用户"""
        results = []
        
        try:
            for target_id in target_ids:
                user = find_user_by_id(user_list, target_id)
                if user:
                    results.append(user)
        except Exception as e:
            print(f"批量搜索过程中出错: {e}")
            return []
        else:
            # 所有搜索都完成了
            print(f"批量搜索完成，找到 {len(results)} 个用户")
            return results
    
    # 测试数据
    users = [
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
        {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'},
        {'name': 'David'},  # 缺少id字段
        'invalid_user',     # 格式错误
    ]
    
    search_ids = [1, 2, 5, 3]
    
    print("\n=== 搜索操作中的else子句 ===")
    found_users = batch_search_users(users, search_ids)
    
    print("\n找到的用户:")
    for user in found_users:
        print(f"  {user['name']} (ID: {user['id']})")

search_with_else()
```

## finally子句的使用

### 1. finally子句的基本特性

```python
def demonstrate_finally_clause():
    """演示finally子句的基本特性"""
    
    def test_finally_execution(test_case):
        """测试finally子句的执行"""
        print(f"\n--- 测试用例: {test_case} ---")
        
        try:
            print("执行try块")
            
            if test_case == 'normal':
                result = 10 / 2
                print(f"计算结果: {result}")
                return result
            elif test_case == 'exception':
                result = 10 / 0  # 引发异常
            elif test_case == 'return_early':
                print("提前返回")
                return "early_return"
            elif test_case == 'raise_exception':
                raise ValueError("手动抛出异常")
                
        except ZeroDivisionError:
            print("捕获到除零异常")
            return "division_error"
        except ValueError as e:
            print(f"捕获到值异常: {e}")
            return "value_error"
        else:
            print("执行else块")
            return "else_executed"
        finally:
            print("执行finally块 - 无论如何都会执行")
    
    # 测试不同情况
    test_cases = ['normal', 'exception', 'return_early', 'raise_exception']
    
    print("=== finally子句执行演示 ===")
    for case in test_cases:
        try:
            result = test_finally_execution(case)
            print(f"函数返回值: {result}")
        except Exception as e:
            print(f"未捕获的异常: {e}")
        print("-" * 40)

demonstrate_finally_clause()
```

### 2. 资源管理和清理操作

```python
class ResourceManager:
    """资源管理器，演示finally子句在资源清理中的应用"""
    
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.is_acquired = False
        self.data = None
    
    def acquire_resource(self):
        """获取资源"""
        print(f"正在获取资源: {self.resource_name}")
        # 模拟资源获取可能失败
        if self.resource_name == 'unavailable':
            raise ConnectionError(f"无法获取资源: {self.resource_name}")
        
        self.is_acquired = True
        print(f"成功获取资源: {self.resource_name}")
    
    def use_resource(self, operation):
        """使用资源"""
        if not self.is_acquired:
            raise RuntimeError("资源未获取")
        
        print(f"正在使用资源进行操作: {operation}")
        
        # 模拟不同的操作结果
        if operation == 'read':
            self.data = f"从{self.resource_name}读取的数据"
            return self.data
        elif operation == 'write':
            print(f"向{self.resource_name}写入数据")
            return "写入成功"
        elif operation == 'error':
            raise IOError("操作过程中发生IO错误")
        else:
            raise ValueError(f"不支持的操作: {operation}")
    
    def release_resource(self):
        """释放资源"""
        if self.is_acquired:
            print(f"正在释放资源: {self.resource_name}")
            self.is_acquired = False
            self.data = None
            print(f"资源已释放: {self.resource_name}")
        else:
            print(f"资源未获取，无需释放: {self.resource_name}")

def resource_operation_with_finally(resource_name, operation):
    """使用finally确保资源清理"""
    resource_manager = ResourceManager(resource_name)
    
    try:
        # 获取资源
        resource_manager.acquire_resource()
        
        # 使用资源
        result = resource_manager.use_resource(operation)
        
        return result
        
    except ConnectionError as e:
        print(f"连接错误: {e}")
        return None
    except (RuntimeError, IOError, ValueError) as e:
        print(f"操作错误: {e}")
        return None
    else:
        print("资源操作成功完成")
    finally:
        # 无论成功还是失败，都要释放资源
        print("执行资源清理...")
        resource_manager.release_resource()

# 测试资源管理
test_scenarios = [
    ('database', 'read'),        # 正常操作
    ('file_system', 'write'),    # 正常写入
    ('network', 'error'),        # 操作错误
    ('unavailable', 'read'),     # 资源获取失败
]

print("\n=== 资源管理中的finally子句 ===")
for resource, operation in test_scenarios:
    print(f"\n{'='*50}")
    print(f"测试: 资源={resource}, 操作={operation}")
    print(f"{'='*50}")
    
    result = resource_operation_with_finally(resource, operation)
    print(f"操作结果: {result}")
```

### 3. 复杂的清理逻辑

```python
class DatabaseConnection:
    """数据库连接类，演示复杂的清理逻辑"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
        self.transaction = None
        self.cursor = None
        self.is_connected = False
    
    def connect(self):
        """建立连接"""
        print(f"连接到数据库: {self.connection_string}")
        if 'invalid' in self.connection_string:
            raise ConnectionError("无效的连接字符串")
        
        self.connection = f"connection_to_{self.connection_string}"
        self.is_connected = True
        print("数据库连接成功")
    
    def begin_transaction(self):
        """开始事务"""
        if not self.is_connected:
            raise RuntimeError("数据库未连接")
        
        print("开始数据库事务")
        self.transaction = "active_transaction"
    
    def create_cursor(self):
        """创建游标"""
        if not self.transaction:
            raise RuntimeError("事务未开始")
        
        print("创建数据库游标")
        self.cursor = "active_cursor"
    
    def execute_query(self, query):
        """执行查询"""
        if not self.cursor:
            raise RuntimeError("游标未创建")
        
        print(f"执行查询: {query}")
        
        if 'error' in query.lower():
            raise IOError("查询执行失败")
        
        return f"查询结果: {query}"
    
    def commit_transaction(self):
        """提交事务"""
        if self.transaction:
            print("提交事务")
            self.transaction = None
    
    def rollback_transaction(self):
        """回滚事务"""
        if self.transaction:
            print("回滚事务")
            self.transaction = None
    
    def close_cursor(self):
        """关闭游标"""
        if self.cursor:
            print("关闭游标")
            self.cursor = None
    
    def disconnect(self):
        """断开连接"""
        if self.is_connected:
            print("断开数据库连接")
            self.connection = None
            self.is_connected = False

def database_operation_with_cleanup(connection_string, query):
    """数据库操作，包含完整的清理逻辑"""
    db = DatabaseConnection(connection_string)
    operation_success = False
    
    try:
        # 建立连接
        db.connect()
        
        try:
            # 开始事务
            db.begin_transaction()
            
            try:
                # 创建游标
                db.create_cursor()
                
                # 执行查询
                result = db.execute_query(query)
                
                # 如果到这里，说明操作成功
                operation_success = True
                return result
                
            except (RuntimeError, IOError) as e:
                print(f"查询执行错误: {e}")
                return None
            finally:
                # 清理游标
                print("清理游标...")
                db.close_cursor()
                
        except RuntimeError as e:
            print(f"事务错误: {e}")
            return None
        finally:
            # 处理事务
            print("处理事务...")
            if operation_success:
                db.commit_transaction()
            else:
                db.rollback_transaction()
                
    except ConnectionError as e:
        print(f"连接错误: {e}")
        return None
    finally:
        # 断开连接
        print("清理连接...")
        db.disconnect()

# 测试数据库操作
test_db_scenarios = [
    ('localhost:5432/mydb', 'SELECT * FROM users'),           # 正常操作
    ('localhost:5432/mydb', 'SELECT * FROM error_table'),     # 查询错误
    ('invalid_connection', 'SELECT * FROM users'),            # 连接错误
]

print("\n=== 数据库操作中的复杂清理逻辑 ===")
for conn_str, query in test_db_scenarios:
    print(f"\n{'='*60}")
    print(f"测试: 连接={conn_str}, 查询={query}")
    print(f"{'='*60}")
    
    result = database_operation_with_cleanup(conn_str, query)
    print(f"操作结果: {result}")
```

## 完整的异常处理结构

### 1. try-except-else-finally的完整用法

```python
def complete_exception_handling_example():
    """完整的异常处理结构示例"""
    
    def comprehensive_file_processor(filename, operation, data=None):
        """综合文件处理器，展示完整的异常处理结构"""
        
        # 初始化状态变量
        file_handle = None
        backup_created = False
        operation_completed = False
        
        try:
            print(f"开始处理文件: {filename}")
            
            # 根据操作类型进行不同处理
            if operation == 'read':
                file_handle = open(filename, 'r', encoding='utf-8')
                content = file_handle.read()
                print(f"成功读取文件，内容长度: {len(content)}")
                return content
                
            elif operation == 'write':
                # 写入前先备份
                try:
                    with open(filename, 'r') as f:
                        backup_content = f.read()
                    with open(f"{filename}.backup", 'w') as f:
                        f.write(backup_content)
                    backup_created = True
                    print("创建备份文件成功")
                except FileNotFoundError:
                    print("原文件不存在，无需备份")
                
                file_handle = open(filename, 'w', encoding='utf-8')
                file_handle.write(data)
                print(f"成功写入数据，长度: {len(data)}")
                operation_completed = True
                return f"写入完成: {len(data)} 字符"
                
            elif operation == 'append':
                file_handle = open(filename, 'a', encoding='utf-8')
                file_handle.write(data)
                print(f"成功追加数据，长度: {len(data)}")
                operation_completed = True
                return f"追加完成: {len(data)} 字符"
                
            else:
                raise ValueError(f"不支持的操作: {operation}")
                
        except FileNotFoundError as e:
            print(f"文件不存在: {e}")
            return None
            
        except PermissionError as e:
            print(f"权限不足: {e}")
            # 如果创建了备份但操作失败，恢复备份
            if backup_created and not operation_completed:
                try:
                    import os
                    os.rename(f"{filename}.backup", filename)
                    print("已恢复备份文件")
                except:
                    print("恢复备份失败")
            return None
            
        except (UnicodeDecodeError, UnicodeEncodeError) as e:
            print(f"编码错误: {e}")
            return None
            
        except ValueError as e:
            print(f"参数错误: {e}")
            return None
            
        except Exception as e:
            print(f"未预期的错误: {type(e).__name__} - {e}")
            # 如果创建了备份但操作失败，恢复备份
            if backup_created and not operation_completed:
                try:
                    import os
                    os.rename(f"{filename}.backup", filename)
                    print("已恢复备份文件")
                except:
                    print("恢复备份失败")
            return None
            
        else:
            # 只有在没有异常时才执行
            print(f"文件操作 '{operation}' 成功完成")
            
            # 如果是写入操作且成功，删除备份
            if operation == 'write' and backup_created:
                try:
                    import os
                    os.remove(f"{filename}.backup")
                    print("删除备份文件")
                except:
                    print("删除备份文件失败")
                    
        finally:
            # 无论如何都要执行的清理操作
            print("执行清理操作...")
            
            # 关闭文件句柄
            if file_handle and not file_handle.closed:
                file_handle.close()
                print("文件句柄已关闭")
            
            # 记录操作日志
            log_entry = {
                'filename': filename,
                'operation': operation,
                'timestamp': '2024-01-01 12:00:00',
                'success': operation_completed
            }
            print(f"记录操作日志: {log_entry}")
    
    # 创建测试文件
    test_content = "这是测试文件的内容\n包含多行文本\n用于演示文件操作"
    with open('test_file.txt', 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    # 测试各种操作
    test_operations = [
        ('test_file.txt', 'read', None),
        ('test_file.txt', 'write', '新的文件内容\n覆盖原有内容'),
        ('test_file.txt', 'append', '\n追加的内容'),
        ('nonexistent.txt', 'read', None),
        ('test_file.txt', 'invalid_op', None),
    ]
    
    print("=== 完整异常处理结构演示 ===")
    for filename, operation, data in test_operations:
        print(f"\n{'='*60}")
        print(f"操作: {operation} 文件: {filename}")
        if data:
            print(f"数据: {data[:30]}..." if len(data) > 30 else f"数据: {data}")
        print(f"{'='*60}")
        
        result = comprehensive_file_processor(filename, operation, data)
        print(f"最终结果: {result}")

complete_exception_handling_example()
```

### 2. 异常处理的最佳实践模式

```python
class BestPracticeExceptionHandler:
    """异常处理最佳实践示例"""
    
    def __init__(self):
        self.operation_log = []
        self.error_count = 0
        self.success_count = 0
    
    def execute_with_full_handling(self, operation_name, operation_func, *args, **kwargs):
        """使用完整异常处理结构执行操作"""
        
        start_time = '2024-01-01 12:00:00'
        operation_id = f"{operation_name}_{len(self.operation_log) + 1}"
        
        try:
            print(f"开始执行操作: {operation_name} (ID: {operation_id})")
            
            # 执行实际操作
            result = operation_func(*args, **kwargs)
            
            # 验证结果
            if result is None:
                raise ValueError("操作返回了None结果")
            
            return result
            
        except (ValueError, TypeError) as e:
            # 参数或数据错误
            error_msg = f"数据错误: {e}"
            print(error_msg)
            self.error_count += 1
            return self._handle_data_error(operation_name, e)
            
        except (FileNotFoundError, PermissionError, IOError) as e:
            # 文件或IO错误
            error_msg = f"IO错误: {e}"
            print(error_msg)
            self.error_count += 1
            return self._handle_io_error(operation_name, e)
            
        except (ConnectionError, TimeoutError) as e:
            # 网络或连接错误
            error_msg = f"连接错误: {e}"
            print(error_msg)
            self.error_count += 1
            return self._handle_connection_error(operation_name, e)
            
        except Exception as e:
            # 未预期的错误
            error_msg = f"未知错误: {type(e).__name__} - {e}"
            print(error_msg)
            self.error_count += 1
            
            # 记录详细错误信息
            import traceback
            traceback.print_exc()
            
            return self._handle_unknown_error(operation_name, e)
            
        else:
            # 操作成功完成
            print(f"操作 {operation_name} 成功完成")
            self.success_count += 1
            
            # 执行成功后的额外处理
            self._post_success_processing(operation_name, result)
            
        finally:
            # 记录操作日志
            end_time = '2024-01-01 12:00:01'
            
            log_entry = {
                'operation_id': operation_id,
                'operation_name': operation_name,
                'start_time': start_time,
                'end_time': end_time,
                'success': self.success_count > len(self.operation_log),
                'args': str(args)[:100],
                'kwargs': str(kwargs)[:100]
            }
            
            self.operation_log.append(log_entry)
            print(f"操作日志已记录: {operation_id}")
            
            # 清理临时资源
            self._cleanup_resources(operation_name)
    
    def _handle_data_error(self, operation_name, error):
        """处理数据错误"""
        print(f"为操作 {operation_name} 提供默认数据")
        return f"default_result_for_{operation_name}"
    
    def _handle_io_error(self, operation_name, error):
        """处理IO错误"""
        print(f"为操作 {operation_name} 启用离线模式")
        return f"offline_result_for_{operation_name}"
    
    def _handle_connection_error(self, operation_name, error):
        """处理连接错误"""
        print(f"为操作 {operation_name} 使用缓存数据")
        return f"cached_result_for_{operation_name}"
    
    def _handle_unknown_error(self, operation_name, error):
        """处理未知错误"""
        print(f"操作 {operation_name} 遇到未知错误，返回安全默认值")
        return None
    
    def _post_success_processing(self, operation_name, result):
        """成功后的处理"""
        print(f"对操作 {operation_name} 的结果进行后处理")
        # 这里可以添加缓存、通知、统计等逻辑
    
    def _cleanup_resources(self, operation_name):
        """清理资源"""
        print(f"清理操作 {operation_name} 的临时资源")
        # 这里可以添加清理临时文件、关闭连接等逻辑
    
    def get_statistics(self):
        """获取统计信息"""
        total_operations = len(self.operation_log)
        return {
            'total_operations': total_operations,
            'successful_operations': self.success_count,
            'failed_operations': self.error_count,
            'success_rate': self.success_count / total_operations if total_operations > 0 else 0
        }

# 定义测试操作函数
def normal_operation(x, y):
    """正常操作"""
    return x + y

def data_error_operation():
    """数据错误操作"""
    return int("abc")

def io_error_operation():
    """IO错误操作"""
    with open("nonexistent_file.txt", 'r') as f:
        return f.read()

def connection_error_operation():
    """连接错误操作"""
    raise ConnectionError("无法连接到服务器")

def unknown_error_operation():
    """未知错误操作"""
    raise RuntimeError("这是一个未知的运行时错误")

def none_result_operation():
    """返回None的操作"""
    return None

# 测试最佳实践处理器
handler = BestPracticeExceptionHandler()

test_operations = [
    ('正常加法', normal_operation, 10, 20),
    ('数据错误', data_error_operation),
    ('IO错误', io_error_operation),
    ('连接错误', connection_error_operation),
    ('未知错误', unknown_error_operation),
    ('None结果', none_result_operation),
]

print("\n=== 异常处理最佳实践演示 ===")
for operation_name, operation_func, *args in test_operations:
    print(f"\n{'='*70}")
    print(f"测试操作: {operation_name}")
    print(f"{'='*70}")
    
    result = handler.execute_with_full_handling(operation_name, operation_func, *args)
    print(f"操作结果: {result}")

print(f"\n=== 统计信息 ===")
stats = handler.get_statistics()
for key, value in stats.items():
    print(f"{key}: {value}")
```

## 学习要点总结

### else子句的特点
1. **执行条件**: 只有在try块没有异常时才执行
2. **位置要求**: 必须在所有except子句之后，finally子句之前
3. **使用场景**: 只有在操作成功时才需要执行的代码
4. **与return的关系**: else块中的return会正常执行

### finally子句的特点
1. **必定执行**: 无论是否有异常都会执行
2. **执行时机**: 在try、except、else块之后执行
3. **主要用途**: 资源清理、日志记录、状态重置
4. **与return的关系**: finally块会在return之前执行

### 完整结构的优势
1. **清晰的逻辑分离**: 正常流程、异常处理、清理操作分离
2. **资源安全**: 确保资源得到正确释放
3. **错误恢复**: 提供多层次的错误处理和恢复机制
4. **可维护性**: 代码结构清晰，易于理解和维护

### 实际应用场景
- 文件操作的完整处理流程
- 数据库事务的提交和回滚
- 网络连接的建立和清理
- 资源的获取和释放

## 下一步学习

掌握了完整的异常处理结构后，接下来将学习：
- [05. 抛出异常](./05_raise_exception.md) - 主动抛出和传播异常
- [06. 自定义异常](./06_custom_exceptions.md) - 创建业务相关的异常类
- [07. 异常链和上下文](./07_exception_chaining.md) - 异常的传播和链接

通过掌握else和finally子句，你可以构建更加完整和健壮的异常处理系统，确保程序在各种情况下都能正确处理资源和状态。