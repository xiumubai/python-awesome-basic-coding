# 部署文档网站

本文档说明如何将 VitePress 文档网站部署到 GitHub Pages。

## 部署策略

本项目采用跨仓库部署策略，将构建后的静态文件部署到 `xiumubai/xiumubai.github.io` 仓库的 `python-awesome-basic-coding` 目录下。

### 部署流程

1. **触发条件**：代码推送到 `main` 分支时自动触发部署
2. **构建过程**：
   - 切换到 `docs` 目录
   - 执行 `npm install` 安装依赖
   - 执行 `npm run build` 构建静态文件
3. **部署过程**：
   - 将 `docs/.vitepress/dist` 目录下的文件部署到目标仓库
   - 目标仓库：`xiumubai/xiumubai.github.io`
   - 目标目录：`python-awesome-basic-coding`
   - 目标分支：`main`

### 访问地址

部署成功后，可通过以下地址访问文档网站：
```
http://xiumubai.github.io/python-awesome-basic-coding/
```

## 配置要求

### 1. Personal Access Token 配置

由于需要跨仓库部署，必须配置个人访问令牌（Personal Access Token）：

1. **生成 Token**：
   - 访问 GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)
   - 点击 "Generate new token (classic)"
   - 设置 Token 名称，如：`deploy-python-awesome-basic-coding`
   - 选择过期时间（建议选择较长时间或无过期时间）
   - 勾选以下权限：
     - `repo` (完整的仓库访问权限)
     - `workflow` (更新 GitHub Actions 工作流)

2. **配置 Secret**：
   - 在当前仓库中，访问 Settings > Secrets and variables > Actions
   - 点击 "New repository secret"
   - Name: `PERSONAL_TOKEN`
   - Value: 粘贴刚才生成的 Token
   - 点击 "Add secret"

### 2. 目标仓库权限

确保生成 Token 的用户对目标仓库 `xiumubai/xiumubai.github.io` 具有写入权限。

## 工作流文件

部署配置文件位于：`.github/workflows/deploy.yml`

### 主要特性

- **自动触发**：推送到 main 分支时自动部署
- **手动触发**：支持在 GitHub Actions 页面手动触发部署
- **跨仓库部署**：使用 `peaceiris/actions-gh-pages` Action 实现跨仓库部署
- **目录隔离**：部署到目标仓库的指定目录，不影响其他内容

### 部署步骤详解

1. **检出源码**：获取当前仓库的完整代码
2. **设置 Node.js**：配置 Node.js 20 环境，启用 npm 缓存
3. **安装依赖**：在 docs 目录下执行 npm install
4. **构建网站**：执行 npm run build 生成静态文件
5. **部署文件**：将构建结果推送到目标仓库

## 故障排除

### 常见问题

1. **Token 权限不足**
   - 检查 PERSONAL_TOKEN 是否正确配置
   - 确认 Token 具有 repo 权限
   - 验证 Token 未过期

2. **目标仓库访问失败**
   - 确认目标仓库存在且可访问
   - 检查 Token 所有者对目标仓库的权限

3. **构建失败**
   - 检查 docs/package.json 中的依赖是否正确
   - 确认 VitePress 配置文件无误
   - 查看 GitHub Actions 日志获取详细错误信息

4. **部署后访问 404**
   - 确认目标仓库已启用 GitHub Pages
   - 检查 GitHub Pages 设置中的源分支是否为 main
   - 验证文件是否正确部署到 python-awesome-basic-coding 目录

### 调试方法

1. **查看 Actions 日志**：
   - 访问仓库的 Actions 页面
   - 点击具体的工作流运行记录
   - 查看每个步骤的详细日志

2. **验证部署结果**：
   - 检查目标仓库 `xiumubai/xiumubai.github.io` 的 `python-awesome-basic-coding` 目录
   - 确认文件已正确更新

## 手动部署

如需手动触发部署：

1. 访问仓库的 Actions 页面
2. 选择 "Deploy VitePress site to GitHub Pages" 工作流
3. 点击 "Run workflow" 按钮
4. 选择分支（通常是 main）
5. 点击 "Run workflow" 确认执行

## 注意事项

- 确保 `docs` 目录下的 `package.json` 和 `package-lock.json` 文件存在且正确
- VitePress 配置文件 `docs/.vitepress/config.js` 中的 base 路径应设置为 `/python-awesome-basic-coding/`
- 部署过程中会覆盖目标仓库中 `python-awesome-basic-coding` 目录的内容
- Token 应定期更新以确保安全性