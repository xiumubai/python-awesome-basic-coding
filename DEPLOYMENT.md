# 部署指南

本文档提供了将 Python 基础编程学习文档网站部署到不同平台的详细指南。

## 📋 部署前准备

### 1. 环境要求
- Node.js 18+ 
- npm 或 yarn
- Git

### 2. 本地构建测试
```bash
# 进入文档目录
cd docs

# 安装依赖
npm install

# 本地开发
npm run dev

# 构建测试
npm run build

# 预览构建结果
npm run preview
```

## 🚀 部署方案

### 方案一：GitHub Pages（推荐）

#### 自动部署（推荐）
1. **启用 GitHub Pages**
   - 进入仓库 Settings → Pages
   - Source 选择 "GitHub Actions"
   - 配置文件已创建：`.github/workflows/deploy.yml`

2. **触发部署**
   ```bash
   git add .
   git commit -m "feat: add deployment configuration"
   git push origin main
   ```

3. **访问网站**
   - 部署完成后访问：`https://[username].github.io/python-awesome-basic-coding/`

#### 手动部署
```bash
# 安装 gh-pages
npm install -g gh-pages

# 构建并部署
cd docs
npm run deploy:github
```

### 方案二：Vercel

#### 通过 Vercel CLI
1. **安装 Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **登录并部署**
   ```bash
   vercel login
   vercel --prod
   ```

#### 通过 Vercel 网站
1. 访问 [vercel.com](https://vercel.com)
2. 连接 GitHub 仓库
3. 选择项目并导入
4. Vercel 会自动检测 `vercel.json` 配置
5. 点击 Deploy

### 方案三：Netlify

#### 通过 Netlify CLI
1. **安装 Netlify CLI**
   ```bash
   npm install -g netlify-cli
   ```

2. **登录并部署**
   ```bash
   netlify login
   netlify deploy --prod
   ```

#### 通过 Netlify 网站
1. 访问 [netlify.com](https://netlify.com)
2. 连接 GitHub 仓库
3. 配置构建设置：
   - Build command: `cd docs && npm run build`
   - Publish directory: `docs/.vitepress/dist`
4. 点击 Deploy

## ⚙️ 配置说明

### VitePress 配置
- **base 路径**：根据部署环境自动调整
- **输出目录**：`docs/.vitepress/dist`
- **清理 URLs**：启用友好的 URL 格式

### 构建脚本
- `npm run build`：标准构建
- `npm run build:github`：GitHub Pages 构建（带 base 路径）
- `npm run preview`：本地预览构建结果
- `npm run clean`：清理构建文件

## 🔧 常见问题

### 1. 资源路径问题
**问题**：部署后样式或图片无法加载

**解决方案**：
- 检查 `base` 配置是否正确
- 确保所有资源使用相对路径
- 验证构建输出的路径结构

### 2. 路由问题
**问题**：刷新页面出现 404

**解决方案**：
- GitHub Pages：确保启用了 `cleanUrls`
- Vercel/Netlify：检查重定向规则配置

### 3. 构建失败
**问题**：部署时构建失败

**解决方案**：
```bash
# 检查 Node.js 版本
node --version

# 清理依赖重新安装
rm -rf node_modules package-lock.json
npm install

# 本地测试构建
npm run build
```

### 4. 环境变量
**问题**：不同环境需要不同配置

**解决方案**：
- 使用 `process.env.NODE_ENV` 判断环境
- 在部署平台设置环境变量
- 检查 `.env` 文件配置

## 📊 性能优化

### 1. 缓存策略
- 静态资源：长期缓存（1年）
- HTML 文件：不缓存或短期缓存
- API 响应：根据更新频率设置

### 2. 压缩优化
- 启用 Gzip/Brotli 压缩
- 图片优化和懒加载
- 代码分割和按需加载

### 3. CDN 配置
- 使用 CDN 加速静态资源
- 配置合适的缓存策略
- 启用 HTTP/2 和 HTTP/3

## 🔍 监控和维护

### 1. 部署监控
- 设置部署通知
- 监控构建时间和成功率
- 配置错误报告

### 2. 性能监控
- 使用 Lighthouse 检查性能
- 监控页面加载时间
- 检查 Core Web Vitals

### 3. 定期维护
- 更新依赖包
- 检查安全漏洞
- 优化构建配置

## 📞 技术支持

如果在部署过程中遇到问题，可以：

1. 查看构建日志获取详细错误信息
2. 检查各平台的官方文档
3. 在项目仓库提交 Issue
4. 参考社区解决方案

---

**注意**：首次部署可能需要几分钟时间，请耐心等待。部署完成后，通常在 1-2 分钟内即可访问网