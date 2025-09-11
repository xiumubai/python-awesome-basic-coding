# 网络编程基础 - urllib和HTTP

## 学习目标

通过本节学习，你将掌握：
- urllib模块的基本用法
- HTTP请求的发送和响应处理
- URL的解析和构建方法
- 网络编程的异常处理
- 简单HTTP服务器的创建
- 实际网络应用的开发

## 核心概念

### urllib模块组成
- **urllib.request**: 发送HTTP请求
- **urllib.parse**: URL解析和构建
- **urllib.error**: 网络异常处理
- **urllib.robotparser**: robots.txt解析

### HTTP基础
- **请求方法**: GET、POST、PUT、DELETE等
- **状态码**: 200成功、404未找到、500服务器错误等
- **请求头**: User-Agent、Content-Type、Authorization等
- **响应头**: Content-Length、Content-Type、Location等

## 代码示例

### 1. urllib基础操作

```python
import urllib.request
import urllib.parse
import urllib.error
import json

def urllib_basic_demo():
    """urllib基础操作演示"""
    print("=" * 50)
    print("urllib基础操作演示")
    print("=" * 50)
    
    # 1. 简单的GET请求
    print("1. 发送GET请求:")
    try:
        url = "https://httpbin.org/get"
        print(f"  请求URL: {url}")
        
        with urllib.request.urlopen(url, timeout=10) as response:
            # 获取响应信息
            print(f"  状态码: {response.getcode()}")
            print(f"  响应头: {dict(response.headers)}")
            
            # 读取响应内容
            content = response.read().decode('utf-8')
            data = json.loads(content)
            print(f"  响应数据: {data.get('url', 'N/A')}")
            
    except urllib.error.URLError as e:
        print(f"  请求失败: {e}")
    
    # 2. 带参数的GET请求
    print("\n2. 带参数的GET请求:")
    try:
        base_url = "https://httpbin.org/get"
        params = {
            'name': '张三',
            'age': '25',
            'city': '北京'
        }
        
        # 构建查询字符串
        query_string = urllib.parse.urlencode(params)
        full_url = f"{base_url}?{query_string}"
        print(f"  完整URL: {full_url}")
        
        with urllib.request.urlopen(full_url, timeout=10) as response:
            content = response.read().decode('utf-8')
            data = json.loads(content)
            print(f"  接收到的参数: {data.get('args', {})}")
            
    except Exception as e:
        print(f"  请求失败: {e}")
```

### 2. POST请求处理

```python
def post_request_demo():
    """POST请求演示"""
    # 表单数据POST请求
    print("发送POST请求:")
    try:
        url = "https://httpbin.org/post"
        post_data = {
            'username': 'testuser',
            'password': 'testpass',
            'email': 'test@example.com'
        }
        
        # 编码POST数据
        data = urllib.parse.urlencode(post_data).encode('utf-8')
        
        # 创建请求
        req = urllib.request.Request(url, data=data, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        req.add_header('User-Agent', 'Python-urllib/3.0')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')
            data = json.loads(content)
            print(f"  POST数据: {data.get('form', {})}")
            
    except Exception as e:
        print(f"  POST请求失败: {e}")
    
    # JSON数据POST请求
    print("\n发送JSON数据:")
    try:
        url = "https://httpbin.org/post"
        json_data = {
            'name': '李四',
            'age': 30,
            'skills': ['Python', 'JavaScript', 'SQL'],
            'active': True
        }
        
        # 转换为JSON字符串
        data = json.dumps(json_data).encode('utf-8')
        
        req = urllib.request.Request(url, data=data, method='POST')
        req.add_header('Content-Type', 'application/json')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')
            response_data = json.loads(content)
            print(f"  发送的JSON: {response_data.get('json', {})}")
            
    except Exception as e:
        print(f"  JSON请求失败: {e}")
```

### 3. URL解析和构建

```python
from urllib.parse import urlparse, urljoin, parse_qs, urlencode

def url_parsing_demo():
    """URL解析演示"""
    print("=" * 50)
    print("URL解析演示")
    print("=" * 50)
    
    # URL解析
    url = "https://www.example.com:8080/path/to/page?name=value&age=25#section1"
    parsed = urlparse(url)
    
    print(f"URL: {url}")
    print(f"  协议: {parsed.scheme}")
    print(f"  主机: {parsed.netloc}")
    print(f"  路径: {parsed.path}")
    print(f"  查询: {parsed.query}")
    print(f"  片段: {parsed.fragment}")
    
    # 解析查询参数
    if parsed.query:
        params = parse_qs(parsed.query)
        print(f"  参数: {params}")
    
    # URL构建
    print("\nURL构建:")
    base_url = "https://api.example.com/v1/users"
    params = {
        'page': 1,
        'limit': 10,
        'sort': 'created_at',
        'filter': ['active', 'verified']
    }
    
    query_string = urlencode(params, doseq=True)
    full_url = f"{base_url}?{query_string}"
    print(f"  构建的URL: {full_url}")
    
    # URL连接
    print("\nURL连接:")
    base = "https://www.example.com/api/v1/"
    paths = ["users", "users/123", "../admin/settings"]
    
    for path in paths:
        joined = urljoin(base, path)
        print(f"  {base} + {path} = {joined}")
```

### 4. HTTP头部处理

```python
import base64

def http_headers_demo():
    """HTTP头部处理演示"""
    print("=" * 50)
    print("HTTP头部处理演示")
    print("=" * 50)
    
    # 自定义请求头
    print("1. 自定义请求头:")
    try:
        url = "https://httpbin.org/headers"
        
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'MyApp/1.0 (Python)')
        req.add_header('Accept', 'application/json')
        req.add_header('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8')
        req.add_header('Custom-Header', 'MyCustomValue')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')
            data = json.loads(content)
            headers = data.get('headers', {})
            
            print(f"  User-Agent: {headers.get('User-Agent', 'N/A')}")
            print(f"  Custom-Header: {headers.get('Custom-Header', 'N/A')}")
            
    except Exception as e:
        print(f"  请求失败: {e}")
    
    # HTTP基本认证
    print("\n2. HTTP基本认证:")
    try:
        url = "https://httpbin.org/basic-auth/user/pass"
        
        # 创建认证字符串
        username = 'user'
        password = 'pass'
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        
        req = urllib.request.Request(url)
        req.add_header('Authorization', f'Basic {encoded_credentials}')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')
            data = json.loads(content)
            print(f"  认证成功: {data.get('authenticated', False)}")
            print(f"  用户: {data.get('user', 'N/A')}")
            
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("  认证失败: 401 Unauthorized")
        else:
            print(f"  HTTP错误: {e.code}")
```

### 5. 异常处理和重试机制

```python
import socket
import time

def error_handling_demo():
    """网络异常处理演示"""
    print("=" * 50)
    print("网络异常处理演示")
    print("=" * 50)
    
    # 测试不同类型的网络错误
    test_cases = [
        ("https://httpbin.org/status/404", "404错误"),
        ("https://httpbin.org/status/500", "500错误"),
        ("https://nonexistent-domain-12345.com", "域名不存在")
    ]
    
    for url, description in test_cases:
        print(f"测试 {description}:")
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=5) as response:
                print(f"  成功: 状态码 {response.getcode()}")
                
        except urllib.error.HTTPError as e:
            print(f"  HTTP错误: {e.code} - {e.reason}")
                
        except urllib.error.URLError as e:
            print(f"  URL错误: {e.reason}")
            
        except socket.timeout:
            print(f"  请求超时")
            
        except Exception as e:
            print(f"  其他错误: {type(e).__name__}: {e}")
    
    # 重试机制
    def request_with_retry(url, max_retries=3, delay=1):
        """带重试的请求函数"""
        for attempt in range(max_retries):
            try:
                print(f"  尝试 {attempt + 1}/{max_retries}: {url}")
                with urllib.request.urlopen(url, timeout=5) as response:
                    return response.getcode(), response.read()
                    
            except (urllib.error.URLError, socket.timeout) as e:
                print(f"    失败: {e}")
                if attempt < max_retries - 1:
                    print(f"    等待 {delay} 秒后重试...")
                    time.sleep(delay)
                    delay *= 2  # 指数退避
                else:
                    raise
    
    # 测试重试机制
    try:
        status, content = request_with_retry("https://httpbin.org/status/200")
        print(f"  最终成功: 状态码 {status}")
    except Exception as e:
        print(f"  最终失败: {e}")
```

### 6. 简单HTTP服务器

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
from datetime import datetime

class SimpleHTTPHandler(BaseHTTPRequestHandler):
    """简单的HTTP请求处理器"""
    
    def do_GET(self):
        """处理GET请求"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            html = '''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Python HTTP服务器</title>
                <meta charset="utf-8">
            </head>
            <body>
                <h1>欢迎访问Python HTTP服务器</h1>
                <p>当前时间: {}</p>
                <p>请求路径: {}</p>
                <p>客户端地址: {}</p>
            </body>
            </html>
            '''.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                      self.path, self.client_address[0])
            
            self.wfile.write(html.encode('utf-8'))
            
        elif self.path == '/api/time':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {
                'timestamp': datetime.now().isoformat(),
                'timezone': 'Asia/Shanghai',
                'format': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')
    
    def do_POST(self):
        """处理POST请求"""
        if self.path == '/api/echo':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            try:
                json_data = json.loads(post_data.decode('utf-8'))
                response = {
                    'received': json_data,
                    'timestamp': datetime.now().isoformat()
                }
            except:
                response = {
                    'received': post_data.decode('utf-8', errors='ignore'),
                    'timestamp': datetime.now().isoformat()
                }
            
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))

def start_http_server():
    """启动HTTP服务器"""
    server_port = 8000
    server = HTTPServer(('localhost', server_port), SimpleHTTPHandler)
    print(f"HTTP服务器启动在 http://localhost:{server_port}")
    server.serve_forever()
```

### 7. 实际应用示例

```python
def practical_applications():
    """实际应用示例"""
    # API客户端
    class HTTPBinClient:
        """HTTPBin API客户端"""
        
        def __init__(self, base_url="https://httpbin.org"):
            self.base_url = base_url
        
        def get_ip(self):
            """获取客户端IP"""
            try:
                url = f"{self.base_url}/ip"
                with urllib.request.urlopen(url, timeout=10) as response:
                    data = json.loads(response.read().decode('utf-8'))
                    return data.get('origin')
            except Exception as e:
                print(f"获取IP失败: {e}")
                return None
        
        def post_data(self, data):
            """发送POST数据"""
            try:
                url = f"{self.base_url}/post"
                json_data = json.dumps(data).encode('utf-8')
                
                req = urllib.request.Request(url, data=json_data, method='POST')
                req.add_header('Content-Type', 'application/json')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    return json.loads(response.read().decode('utf-8'))
            except Exception as e:
                print(f"POST请求失败: {e}")
                return None
    
    # 使用API客户端
    client = HTTPBinClient()
    ip = client.get_ip()
    print(f"客户端IP: {ip}")
    
    # 发送数据
    test_data = {'message': 'Hello from Python!', 'timestamp': datetime.now().isoformat()}
    response = client.post_data(test_data)
    if response:
        print(f"服务器响应: {response.get('json', {})}")
```

## 重要知识点

### 1. urllib模块特点
- **标准库**: 无需额外安装，Python内置
- **功能完整**: 支持HTTP/HTTPS、FTP等协议
- **底层控制**: 提供详细的请求和响应控制
- **学习价值**: 理解HTTP协议的好工具

### 2. 请求处理流程
1. **创建请求**: 使用Request对象或直接URL
2. **设置头部**: 添加必要的HTTP头部
3. **发送请求**: 使用urlopen()函数
4. **处理响应**: 读取状态码、头部和内容
5. **异常处理**: 捕获和处理各种网络异常

### 3. 常见应用场景
- **API客户端**: 调用REST API服务
- **网页抓取**: 获取网页内容和数据
- **文件下载**: 从网络下载文件
- **服务监控**: 检查服务可用性
- **数据同步**: 与远程服务同步数据

### 4. 最佳实践
- **设置超时**: 避免请求无限等待
- **异常处理**: 妥善处理网络异常
- **重试机制**: 实现指数退避重试
- **请求头**: 设置合适的User-Agent
- **编码处理**: 正确处理字符编码

## 运行方式

```bash
# 运行完整示例
python3 06_urllib_http.py

# 或者在Python解释器中
python3
>>> exec(open('06_urllib_http.py').read())
```

## 练习建议

1. **基础练习**：
   - 发送不同类型的HTTP请求
   - 解析和构建各种格式的URL
   - 处理不同的HTTP状态码

2. **进阶练习**：
   - 实现带认证的API客户端
   - 创建支持文件上传的HTTP客户端
   - 开发简单的网页爬虫

3. **实战项目**：
   - 构建REST API客户端库
   - 开发网站监控工具
   - 创建数据同步服务

## 注意事项

1. **网络安全**：
   - 验证SSL证书
   - 不要在URL中暴露敏感信息
   - 使用HTTPS进行敏感数据传输

2. **性能优化**：
   - 设置合理的超时时间
   - 使用连接池（考虑requests库）
   - 避免频繁的DNS查询

3. **错误处理**：
   - 区分不同类型的网络错误
   - 实现合适的重试策略
   - 记录详细的错误日志

4. **协议遵守**：
   - 遵守robots.txt规则
   - 控制请求频率
   - 设置合适的User-Agent

5. **替代方案**：
   - 对于复杂需求，考虑使用requests库
   - 异步需求可以使用aiohttp
   - WebSocket需求使用websockets库