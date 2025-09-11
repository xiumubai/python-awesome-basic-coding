#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
06_urllib_http.py - 网络编程基础模块学习

本文件演示Python网络编程基础的各种功能：
1. urllib模块的使用
2. HTTP请求处理
3. URL解析和构建
4. 网络异常处理
5. 简单的HTTP服务器
6. 实际应用示例

学习目标：
- 掌握urllib模块的基本用法
- 学会发送HTTP请求和处理响应
- 了解URL的解析和构建方法
- 掌握网络编程的异常处理
- 学会创建简单的HTTP服务器
"""

import urllib.request
import urllib.parse
import urllib.error
from urllib.parse import urlparse, urljoin, parse_qs, urlencode
import json
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time
from datetime import datetime
import ssl
import base64

def urllib_basic_demo():
    """urllib基础操作演示"""
    print("=" * 50)
    print("urllib基础操作演示")
    print("=" * 50)
    
    # 1. 简单的GET请求
    print("1. 发送GET请求:")
    try:
        # 使用一个公共的测试API
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
    except Exception as e:
        print(f"  其他错误: {e}")
    
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
        query_string = urlencode(params)
        full_url = f"{base_url}?{query_string}"
        print(f"  完整URL: {full_url}")
        
        with urllib.request.urlopen(full_url, timeout=10) as response:
            content = response.read().decode('utf-8')
            data = json.loads(content)
            print(f"  接收到的参数: {data.get('args', {})}")
            
    except Exception as e:
        print(f"  请求失败: {e}")
    
    # 3. POST请求
    print("\n3. 发送POST请求:")
    try:
        url = "https://httpbin.org/post"
        post_data = {
            'username': 'testuser',
            'password': 'testpass',
            'email': 'test@example.com'
        }
        
        # 编码POST数据
        data = urlencode(post_data).encode('utf-8')
        
        # 创建请求
        req = urllib.request.Request(url, data=data, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        req.add_header('User-Agent', 'Python-urllib/3.0')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')
            data = json.loads(content)
            print(f"  POST数据: {data.get('form', {})}")
            print(f"  请求头: {data.get('headers', {}).get('User-Agent', 'N/A')}")
            
    except Exception as e:
        print(f"  POST请求失败: {e}")
    
    # 4. JSON数据POST请求
    print("\n4. 发送JSON数据:")
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
    
    print()

def url_parsing_demo():
    """URL解析演示"""
    print("=" * 50)
    print("URL解析演示")
    print("=" * 50)
    
    # 1. URL解析
    urls = [
        "https://www.example.com:8080/path/to/page?name=value&age=25#section1",
        "http://user:pass@localhost:3000/api/users?filter=active",
        "ftp://files.example.com/downloads/file.zip",
        "mailto:admin@example.com?subject=Hello"
    ]
    
    print("1. URL组件解析:")
    for url in urls:
        parsed = urlparse(url)
        print(f"  URL: {url}")
        print(f"    协议: {parsed.scheme}")
        print(f"    主机: {parsed.netloc}")
        print(f"    路径: {parsed.path}")
        print(f"    查询: {parsed.query}")
        print(f"    片段: {parsed.fragment}")
        
        # 解析查询参数
        if parsed.query:
            params = parse_qs(parsed.query)
            print(f"    参数: {params}")
        print()
    
    # 2. URL构建
    print("2. URL构建:")
    base_url = "https://api.example.com/v1/users"
    
    # 构建查询参数
    params = {
        'page': 1,
        'limit': 10,
        'sort': 'created_at',
        'filter': ['active', 'verified']
    }
    
    query_string = urlencode(params, doseq=True)  # doseq=True处理列表参数
    full_url = f"{base_url}?{query_string}"
    print(f"  构建的URL: {full_url}")
    
    # 3. URL连接
    print("\n3. URL连接:")
    base = "https://www.example.com/api/v1/"
    paths = [
        "users",
        "users/123",
        "../admin/settings",
        "/absolute/path",
        "?query=test"
    ]
    
    for path in paths:
        joined = urljoin(base, path)
        print(f"  {base} + {path} = {joined}")
    
    # 4. URL编码和解码
    print("\n4. URL编码和解码:")
    test_strings = [
        "Hello World!",
        "中文测试",
        "user@example.com",
        "a=1&b=2",
        "100% success"
    ]
    
    for s in test_strings:
        encoded = urllib.parse.quote(s)
        decoded = urllib.parse.unquote(encoded)
        print(f"  原始: {s}")
        print(f"  编码: {encoded}")
        print(f"  解码: {decoded}")
        print()
    
    print()

def http_headers_demo():
    """HTTP头部处理演示"""
    print("=" * 50)
    print("HTTP头部处理演示")
    print("=" * 50)
    
    # 1. 自定义请求头
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
            print(f"  Accept: {headers.get('Accept', 'N/A')}")
            print(f"  Custom-Header: {headers.get('Custom-Header', 'N/A')}")
            
    except Exception as e:
        print(f"  请求失败: {e}")
    
    # 2. 基本认证
    print("\n2. HTTP基本认证演示:")
    try:
        # 注意：这只是演示，实际使用时需要真实的认证服务器
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
    except Exception as e:
        print(f"  请求失败: {e}")
    
    # 3. 处理重定向
    print("\n3. 重定向处理:")
    try:
        # httpbin.org/redirect/3 会进行3次重定向
        url = "https://httpbin.org/redirect/2"
        print(f"  请求URL: {url}")
        
        with urllib.request.urlopen(url, timeout=10) as response:
            print(f"  最终URL: {response.url}")
            print(f"  状态码: {response.getcode()}")
            
    except Exception as e:
        print(f"  请求失败: {e}")
    
    print()

def error_handling_demo():
    """网络异常处理演示"""
    print("=" * 50)
    print("网络异常处理演示")
    print("=" * 50)
    
    # 测试不同类型的网络错误
    test_cases = [
        ("https://httpbin.org/status/404", "404错误"),
        ("https://httpbin.org/status/500", "500错误"),
        ("https://nonexistent-domain-12345.com", "域名不存在"),
        ("https://httpbin.org/delay/15", "超时测试")
    ]
    
    for url, description in test_cases:
        print(f"测试 {description}:")
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=5) as response:
                print(f"  成功: 状态码 {response.getcode()}")
                
        except urllib.error.HTTPError as e:
            print(f"  HTTP错误: {e.code} - {e.reason}")
            # 读取错误响应内容
            try:
                error_content = e.read().decode('utf-8')
                if error_content:
                    print(f"  错误内容: {error_content[:100]}...")
            except:
                pass
                
        except urllib.error.URLError as e:
            print(f"  URL错误: {e.reason}")
            
        except socket.timeout:
            print(f"  请求超时")
            
        except Exception as e:
            print(f"  其他错误: {type(e).__name__}: {e}")
        
        print()
    
    # 重试机制演示
    print("重试机制演示:")
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
                    print(f"    所有重试都失败了")
                    raise
    
    # 测试重试机制（使用一个可能不稳定的URL）
    try:
        status, content = request_with_retry("https://httpbin.org/status/200", max_retries=2)
        print(f"  最终成功: 状态码 {status}")
    except Exception as e:
        print(f"  最终失败: {e}")
    
    print()

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
                <ul>
                    <li><a href="/api/time">获取时间API</a></li>
                    <li><a href="/api/info">服务器信息API</a></li>
                </ul>
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
            
        elif self.path == '/api/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {
                'server': 'Python HTTP Server',
                'version': '1.0',
                'client_ip': self.client_address[0],
                'user_agent': self.headers.get('User-Agent', 'Unknown')
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
                # 尝试解析JSON数据
                json_data = json.loads(post_data.decode('utf-8'))
                response = {
                    'received': json_data,
                    'timestamp': datetime.now().isoformat(),
                    'content_type': self.headers.get('Content-Type', 'unknown')
                }
            except:
                # 如果不是JSON，返回原始数据
                response = {
                    'received': post_data.decode('utf-8', errors='ignore'),
                    'timestamp': datetime.now().isoformat(),
                    'content_type': self.headers.get('Content-Type', 'unknown')
                }
            
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')
    
    def log_message(self, format, *args):
        """自定义日志格式"""
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {format % args}")

def http_server_demo():
    """HTTP服务器演示"""
    print("=" * 50)
    print("HTTP服务器演示")
    print("=" * 50)
    
    # 启动HTTP服务器
    server_port = 8000
    
    def start_server():
        """启动服务器的函数"""
        try:
            server = HTTPServer(('localhost', server_port), SimpleHTTPHandler)
            print(f"HTTP服务器启动在 http://localhost:{server_port}")
            server.serve_forever()
        except Exception as e:
            print(f"服务器启动失败: {e}")
    
    # 在后台线程中启动服务器
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # 等待服务器启动
    time.sleep(2)
    
    # 测试服务器
    print("\n测试HTTP服务器:")
    test_urls = [
        f"http://localhost:{server_port}/",
        f"http://localhost:{server_port}/api/time",
        f"http://localhost:{server_port}/api/info"
    ]
    
    for url in test_urls:
        try:
            print(f"\n请求: {url}")
            with urllib.request.urlopen(url, timeout=5) as response:
                content = response.read().decode('utf-8')
                if 'application/json' in response.headers.get('Content-Type', ''):
                    data = json.loads(content)
                    print(f"  JSON响应: {data}")
                else:
                    print(f"  HTML响应长度: {len(content)} 字符")
                    
        except Exception as e:
            print(f"  请求失败: {e}")
    
    # 测试POST请求
    print("\n测试POST请求:")
    try:
        url = f"http://localhost:{server_port}/api/echo"
        post_data = {
            'message': 'Hello from client!',
            'timestamp': datetime.now().isoformat(),
            'data': [1, 2, 3, 4, 5]
        }
        
        data = json.dumps(post_data).encode('utf-8')
        req = urllib.request.Request(url, data=data, method='POST')
        req.add_header('Content-Type', 'application/json')
        
        with urllib.request.urlopen(req, timeout=5) as response:
            content = response.read().decode('utf-8')
            response_data = json.loads(content)
            print(f"  服务器回显: {response_data['received']}")
            
    except Exception as e:
        print(f"  POST请求失败: {e}")
    
    print(f"\n注意: HTTP服务器将在后台继续运行在端口 {server_port}")
    print("你可以在浏览器中访问 http://localhost:8000 查看效果")
    
    print()

def practical_applications():
    """实际应用示例"""
    print("=" * 50)
    print("实际应用示例")
    print("=" * 50)
    
    # 1. 网页内容抓取
    def web_scraping_demo():
        """网页内容抓取演示"""
        print("1. 网页内容抓取:")
        try:
            # 获取一个简单的文本页面
            url = "https://httpbin.org/robots.txt"
            
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (compatible; Python scraper)')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                content = response.read().decode('utf-8')
                lines = content.strip().split('\n')
                
                print(f"  获取到 {len(lines)} 行内容")
                print(f"  前3行: {lines[:3]}")
                
        except Exception as e:
            print(f"  抓取失败: {e}")
    
    # 2. API客户端
    def api_client_demo():
        """API客户端演示"""
        print("\n2. API客户端:")
        
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
            
            def get_user_agent(self):
                """获取User-Agent信息"""
                try:
                    url = f"{self.base_url}/user-agent"
                    req = urllib.request.Request(url)
                    req.add_header('User-Agent', 'MyAPIClient/1.0')
                    
                    with urllib.request.urlopen(req, timeout=10) as response:
                        data = json.loads(response.read().decode('utf-8'))
                        return data.get('user-agent')
                except Exception as e:
                    print(f"获取User-Agent失败: {e}")
                    return None
        
        # 使用API客户端
        client = HTTPBinClient()
        ip = client.get_ip()
        user_agent = client.get_user_agent()
        
        print(f"  客户端IP: {ip}")
        print(f"  User-Agent: {user_agent}")
    
    # 3. 文件下载
    def file_download_demo():
        """文件下载演示"""
        print("\n3. 文件下载:")
        try:
            # 下载一个小的测试文件
            url = "https://httpbin.org/json"
            
            print(f"  开始下载: {url}")
            
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=10) as response:
                # 获取文件信息
                content_length = response.headers.get('Content-Length')
                content_type = response.headers.get('Content-Type')
                
                print(f"  文件类型: {content_type}")
                if content_length:
                    print(f"  文件大小: {content_length} 字节")
                
                # 读取内容
                content = response.read()
                print(f"  下载完成: {len(content)} 字节")
                
                # 如果是JSON，解析并显示
                if 'json' in content_type:
                    data = json.loads(content.decode('utf-8'))
                    print(f"  JSON数据: {list(data.keys())}")
                
        except Exception as e:
            print(f"  下载失败: {e}")
    
    web_scraping_demo()
    api_client_demo()
    file_download_demo()
    
    print()

def main():
    """主函数"""
    print("Python网络编程基础模块学习演示")
    print("=" * 60)
    
    urllib_basic_demo()
    url_parsing_demo()
    http_headers_demo()
    error_handling_demo()
    http_server_demo()
    practical_applications()
    
    print("=" * 50)
    print("学习要点总结:")
    print("=" * 50)
    print("1. urllib是Python标准库中的网络编程模块")
    print("2. 支持HTTP/HTTPS、FTP等多种协议")
    print("3. 可以发送GET、POST等各种HTTP请求")
    print("4. 支持自定义请求头、认证、重定向等")
    print("5. 提供完整的URL解析和构建功能")
    print("6. 需要合理处理网络异常和超时")
    print("7. 可以创建简单的HTTP服务器")
    print("8. 适合构建API客户端和网页抓取工具")
    print("9. 对于复杂需求，建议使用requests库")
    print("10. 注意网络安全和访问频率限制")

if __name__ == "__main__":
    main()