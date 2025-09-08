# Python基础编程学习文档网站

这是一个基于VitePress构建的Python学习文档网站，将原有的Python学习代码转换为现代化的在线文档。

## 🚀 快速开始

### 安装依赖

```bash
cd docs
npm install
```

### 开发模式

```bash
npm run dev
```

访问 http://localhost:5173 查看网站

### 构建生产版本

```bash
npm run build
```

构建后的文件在 `.vitepress/dist` 目录

### 预览生产版本

```bash
npm run preview
```

## 📁 项目结构

```
docs/
├── .vitepress/
│   ├── config.js          # VitePress配置文件
│   └── dist/              # 构建输出目录
├── guide/                 # 教程文档
│   ├── index.md          # 教程首页
│   └── 01-variables-and-types/  # 变量和类型模块
│       └── index.md
├── index.md              # 网站首页
├── package.json          # 项目配置
└── README.md            # 项目说明
```

## 🎯 功能特性

- ✅ **现代化界面**：基于VitePress的美观文档界面
- ✅ **响应式设计**：支持桌面和移动设备
- ✅ **代码高亮**：Python代码语法高亮显示
- ✅ **搜索功能**：内置全文搜索
- ✅ **导航系统**：清晰的导航和侧边栏
- ✅ **快速构建**：基于Vite的快速热重载

## 📚 内容组织

### 已完成模块

- [x] **变量和数据类型** - 包含完整的学习内容和代码示例

### 待添加模块

- [ ] 运算符
- [ ] 输入输出
- [ ] 注释
- [ ] 条件语句
- [ ] 循环
- [ ] 数据结构
- [ ] 函数
- [ ] 面向对象
- [ ] 文件操作
- [ ] 异常处理
- [ ] 模块和包
- [ ] 标准库
- [ ] 实践项目

## 🔧 开发指南

### 添加新模块

1. 在 `guide/` 目录下创建新的模块文件夹
2. 创建 `index.md` 文件编写模块内容
3. 在 `.vitepress/config.js` 中更新侧边栏配置
4. 测试构建是否成功

### 内容编写规范

- 使用Markdown格式
- 代码块指定语言为 `python`
- 添加适当的标题层级
- 包含学习目标和重点概念
- 提供实际可运行的代码示例

### 配置说明

主要配置在 `.vitepress/config.js` 文件中：

- `title`: 网站标题
- `description`: 网站描述
- `themeConfig.nav`: 顶部导航
- `themeConfig.sidebar`: 侧边栏配置
- `ignoreDeadLinks`: 忽略死链接检查

## 🚀 部署

### GitHub Pages

1. 构建项目：`npm run build`
2. 将 `.vitepress/dist` 目录内容推送到 `gh-pages` 分支

### Vercel

1. 连接GitHub仓库
2. 设置构建命令：`cd docs && npm run build`
3. 设置输出目录：`docs/.vitepress/dist`

### Netlify

1. 连接GitHub仓库
2. 设置构建命令：`cd docs && npm run build`
3. 设置发布目录：`docs/.vitepress/dist`

## 📝 更新日志

### v1.0.0 (2024-01-08)

- ✅ 初始化VitePress项目
- ✅ 创建基本网站结构
- ✅ 完成变量和数据类型模块文档
- ✅ 配置导航和侧边栏
- ✅ 实现构建和部署流程

## 🤝 贡献

欢迎贡献内容和改进建议！

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 📄 许可证

MIT License

---

**开始你的Python学习之旅！** 🐍✨