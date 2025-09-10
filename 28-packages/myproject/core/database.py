
"""数据库管理模块"""

import sqlite3
import threading
from typing import List, Dict, Any, Optional

class ConnectionError(Exception):
    """连接异常"""
    pass

class DatabaseManager:
    """数据库管理器"""
    
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.connection = None
        self._lock = threading.Lock()
        
    def connect(self):
        """连接数据库"""
        try:
            with self._lock:
                if self.connection:
                    raise ConnectionError("数据库已连接")
                
                self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
                self.connection.row_factory = sqlite3.Row
                print(f"数据库连接成功: {self.db_path}")
                
        except sqlite3.Error as e:
            raise ConnectionError(f"数据库连接失败: {e}")
    
    def disconnect(self):
        """断开数据库连接"""
        with self._lock:
            if self.connection:
                self.connection.close()
                self.connection = None
                print("数据库连接已断开")
    
    def execute(self, sql: str, params: tuple = ()) -> sqlite3.Cursor:
        """执行SQL语句"""
        if not self.connection:
            raise ConnectionError("数据库未连接")
        
        try:
            with self._lock:
                cursor = self.connection.cursor()
                cursor.execute(sql, params)
                self.connection.commit()
                return cursor
        except sqlite3.Error as e:
            raise ConnectionError(f"SQL执行失败: {e}")
    
    def fetch_all(self, sql: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """查询所有结果"""
        cursor = self.execute(sql, params)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    
    def fetch_one(self, sql: str, params: tuple = ()) -> Optional[Dict[str, Any]]:
        """查询单个结果"""
        cursor = self.execute(sql, params)
        row = cursor.fetchone()
        return dict(row) if row else None
    
    def create_table(self, table_name: str, columns: Dict[str, str]):
        """创建表"""
        column_defs = [f"{name} {type_def}" for name, type_def in columns.items()]
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_defs)})"
        self.execute(sql)
        print(f"表 {table_name} 创建成功")
