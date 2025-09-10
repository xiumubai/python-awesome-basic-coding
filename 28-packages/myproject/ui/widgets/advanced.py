
"""高级控件模块"""

from typing import List, Dict, Any, Optional
from .basic import Widget

class ListView(Widget):
    """列表视图控件"""
    
    def __init__(self, name: str = "listview"):
        super().__init__(name)
        self.items = []
        self.selected_index = -1
    
    def add_item(self, item: Any):
        """添加项目"""
        self.items.append(item)
        print(f"添加列表项: {item}")
    
    def remove_item(self, index: int):
        """移除项目"""
        if 0 <= index < len(self.items):
            item = self.items.pop(index)
            print(f"移除列表项: {item}")
            if self.selected_index == index:
                self.selected_index = -1
    
    def select_item(self, index: int):
        """选择项目"""
        if 0 <= index < len(self.items):
            self.selected_index = index
            print(f"选择列表项: {self.items[index]}")
    
    def get_selected_item(self) -> Optional[Any]:
        """获取选中项目"""
        if 0 <= self.selected_index < len(self.items):
            return self.items[self.selected_index]
        return None
    
    def clear(self):
        """清空列表"""
        self.items.clear()
        self.selected_index = -1
        print("列表已清空")

class TreeView(Widget):
    """树视图控件"""
    
    def __init__(self, name: str = "treeview"):
        super().__init__(name)
        self.root_nodes = []
    
    def add_root_node(self, text: str, data: Any = None) -> 'TreeNode':
        """添加根节点"""
        node = TreeNode(text, data)
        self.root_nodes.append(node)
        print(f"添加根节点: {text}")
        return node
    
    def get_all_nodes(self) -> List['TreeNode']:
        """获取所有节点"""
        nodes = []
        for root in self.root_nodes:
            nodes.extend(root.get_all_descendants())
        return nodes
    
    def clear(self):
        """清空树"""
        self.root_nodes.clear()
        print("树视图已清空")

class TreeNode:
    """树节点"""
    
    def __init__(self, text: str, data: Any = None):
        self.text = text
        self.data = data
        self.children = []
        self.parent = None
        self.expanded = False
    
    def add_child(self, text: str, data: Any = None) -> 'TreeNode':
        """添加子节点"""
        child = TreeNode(text, data)
        child.parent = self
        self.children.append(child)
        print(f"添加子节点: {text} (父节点: {self.text})")
        return child
    
    def remove_child(self, child: 'TreeNode'):
        """移除子节点"""
        if child in self.children:
            child.parent = None
            self.children.remove(child)
            print(f"移除子节点: {child.text}")
    
    def expand(self):
        """展开节点"""
        self.expanded = True
        print(f"展开节点: {self.text}")
    
    def collapse(self):
        """折叠节点"""
        self.expanded = False
        print(f"折叠节点: {self.text}")
    
    def get_all_descendants(self) -> List['TreeNode']:
        """获取所有后代节点"""
        descendants = [self]
        for child in self.children:
            descendants.extend(child.get_all_descendants())
        return descendants

class TabControl(Widget):
    """标签页控件"""
    
    def __init__(self, name: str = "tabcontrol"):
        super().__init__(name)
        self.tabs = []
        self.selected_index = 0
    
    def add_tab(self, title: str, content: Any = None) -> 'Tab':
        """添加标签页"""
        tab = Tab(title, content)
        self.tabs.append(tab)
        print(f"添加标签页: {title}")
        return tab
    
    def remove_tab(self, index: int):
        """移除标签页"""
        if 0 <= index < len(self.tabs):
            tab = self.tabs.pop(index)
            print(f"移除标签页: {tab.title}")
            if self.selected_index >= len(self.tabs) and self.tabs:
                self.selected_index = len(self.tabs) - 1
    
    def select_tab(self, index: int):
        """选择标签页"""
        if 0 <= index < len(self.tabs):
            self.selected_index = index
            print(f"选择标签页: {self.tabs[index].title}")
    
    def get_selected_tab(self) -> Optional['Tab']:
        """获取当前选中的标签页"""
        if 0 <= self.selected_index < len(self.tabs):
            return self.tabs[self.selected_index]
        return None

class Tab:
    """标签页"""
    
    def __init__(self, title: str, content: Any = None):
        self.title = title
        self.content = content
        self.visible = True
    
    def set_title(self, title: str):
        """设置标题"""
        self.title = title
        print(f"标签页标题已更改为: {title}")
    
    def set_content(self, content: Any):
        """设置内容"""
        self.content = content
        print(f"标签页内容已更新")
