# 🚀 深聊网站 Vercel 部署指南

本指南将帮助你将深聊网站快速部署到 Vercel，获得一个免费、稳定、支持 HTTPS 的线上环境。

## ✨ 为什么选择 Vercel？

- ✅ **完全免费**: 免费套餐足够使用
- ✅ **自动 HTTPS**: 自动配置 SSL 证书
- ✅ **全球 CDN**: 自动部署到全球节点
- ✅ **Next.js 原生支持**: 由 Next.js 团队开发
- ✅ **一键部署**: 连接 GitHub 即可自动部署
- ✅ **自定义域名**: 支持绑定自己的域名

## 📋 前置要求

- 一个 GitHub 账号（免费）
- 一个 Vercel 账号（免费，使用 GitHub 登录）
- 深聊网站代码（已完成）

## 🚀 部署步骤

### 方式 1: 通过 Vercel CLI 部署（推荐）

#### 1. 安装 Vercel CLI

```bash
npm install -g vercel
```

#### 2. 登录 Vercel

```bash
vercel login
```

会提示你选择登录方式，推荐使用 GitHub 登录。

#### 3. 部署项目

```bash
cd web
vercel
```

Vercel 会问你几个问题：

```
? Set up and deploy "~/web"? [Y/n] Y
? Which scope do you want to deploy to? (选择你的用户名/组织)
? Link to existing project? [y/N] N
? What's your project's name? deepchat-web
? In which directory is your code located? ./
? Want to override the settings? [y/N] N
```

等待部署完成，Vercel 会给你一个预览链接。

#### 4. 配置环境变量

在 Vercel 项目设置中添加环境变量：

1. 访问 https://vercel.com/dashboard
2. 进入你的项目
3. 点击 Settings → Environment Variables
4. 添加环境变量：
   - Name: `NEXT_PUBLIC_API_URL`
   - Value: 你的后端 API 地址
   - Environment: Production, Preview, Development

#### 5. 生产部署

```bash
vercel --prod
```

这会部署到生产环境，给你一个稳定的 `.vercel.app` 域名。

### 方式 2: 通过 GitHub 集成部署

#### 1. 推送代码到 GitHub

```bash
# 如果还没有 Git 仓库
cd web
git init
git add .
git commit -m "Initial commit"

# 推送到 GitHub（替换为你的仓库地址）
git remote add origin https://github.com/your-username/deepchat-web.git
git branch -M main
git push -u origin main
```

#### 2. 在 Vercel 创建项目

1. 访问 https://vercel.com/new
2. 选择 "Import Project"
3. 选择你的 GitHub 仓库
4. Vercel 会自动检测到这是一个 Next.js 项目

#### 3. 配置项目

**Framework Preset**: Next.js
**Root Directory**: ./web
**Build Command**: `npm run build`
**Output Directory**: `.next`

#### 4. 配置环境变量

在 "Environment Variables" 部分添加：

```
NEXT_PUBLIC_API_URL = https://your-backend-api.com
```

#### 5. 部署

点击 "Deploy" 按钮，等待几分钟即可完成。

## 🌐 访问你的网站

### 预览环境（Preview）
每次推送代码都会自动部署预览版本：
```
https://deepchat-web-<username>.vercel.app
```

### 生产环境（Production）
部署到生产环境后：
```
https://deepchat-web.vercel.app
```

## 🔧 常见配置

### 修改域名

#### 1. 添加自定义域名

1. 访问 Vercel 项目设置
2. 点击 Domains
3. 添加你的域名（例如: `deepchat.yourdomain.com`）
4. 按照提示在域名 DNS 管理中添加 CNAME 记录

#### 2. DNS 配置

如果你使用自己的域名，需要添加以下 DNS 记录：

```
Type: CNAME
Name: deepchat
Value: cname.vercel-dns.com
```

### 配置后端 API

如果你有后端 API，需要：

#### 1. 后端部署

可以选择：
- Vercel Serverless Functions
- Railway
- Render
- 自己的服务器

#### 2. 配置 CORS

确保后端 API 允许来自 Vercel 域名的跨域请求：

```javascript
// 示例：CORS 配置
app.use(cors({
  origin: [
    'https://deepchat-web.vercel.app',
    'http://localhost:3000'
  ],
  credentials: true
}))
```

#### 3. 更新环境变量

在 Vercel 中更新 `NEXT_PUBLIC_API_URL`：

```
NEXT_PUBLIC_API_URL = https://your-backend-api.com
```

## 📊 查看部署日志

### 通过 Vercel Dashboard

1. 访问 https://vercel.com/dashboard
2. 进入你的项目
3. 点击 "Deployments"
4. 选择一个部署，查看日志

### 通过 CLI

```bash
vercel logs
```

## 🔄 自动部署

配置 GitHub 集成后，每次推送代码到 `main` 分支会自动触发部署：

```bash
git add .
git commit -m "Update website"
git push origin main
```

## 💡 优化建议

### 1. 启用图片优化

Next.js Image 组件已经配置好了 Vercel 的图片优化。

### 2. 配置缓存

在 `next.config.js` 中配置：

```javascript
module.exports = {
  // ...其他配置
  compress: true,
  swcMinify: true,
}
```

### 3. 使用 Edge Functions

将一些计算密集型操作放到 Edge Functions 中。

### 4. 配置重定向

在 `vercel.json` 中配置重定向：

```json
{
  "rewrites": [
    {
      "source": "/api/:path*",
      "destination": "https://your-backend-api.com/api/:path*"
    }
  ]
}
```

## 🐛 常见问题

### Q1: 部署失败怎么办？

1. 检查构建日志：`vercel logs`
2. 确保依赖已正确安装
3. 检查是否有语法错误

### Q2: 环境变量不生效？

1. 确保变量名以 `NEXT_PUBLIC_` 开头
2. 重新部署项目：`vercel --prod`
3. 检查环境变量是否在所有环境中都配置了

### Q3: 访问速度慢？

1. 确保选择了最近的 Region（如 hkg1）
2. 检查是否有大文件未优化
3. 使用 Vercel Analytics 分析性能

### Q4: 如何回滚到之前的版本？

1. 访问 Vercel Dashboard
2. 进入你的项目
3. 点击 "Deployments"
4. 选择要回滚的部署，点击 "..."
5. 选择 "Promote to Production"

## 📈 监控和分析

### Vercel Analytics

Vercel 提供免费的 Web Analytics：

1. 在项目设置中启用 Analytics
2. 添加 Analytics 脚本

### 查看访问数据

访问 Vercel Dashboard 的 Analytics 页面查看：
- 访问量
- 页面浏览量
- 用户地理位置
- 设备类型

## 🔐 安全配置

### 1. 环境变量保护

不要在代码中硬编码敏感信息，使用环境变量：

```javascript
// ❌ 错误
const API_KEY = "your-secret-key"

// ✅ 正确
const API_KEY = process.env.NEXT_PUBLIC_API_KEY
```

### 2. CORS 配置

确保你的 API 只允许特定域名访问。

### 3. 安全头配置

在 `next.config.js` 中添加安全头：

```javascript
module.exports = {
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'X-Frame-Options',
            value: 'DENY',
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff',
          },
        ],
      },
    ]
  },
}
```

## 📚 相关链接

- Vercel 官网: https://vercel.com
- Vercel 文档: https://vercel.com/docs
- Next.js 文档: https://nextjs.org/docs
- 部署示例: https://vercel.com/templates/next.js

## 🎉 部署完成

部署完成后，你将获得：

- ✅ 一个稳定的线上网站
- ✅ 自动 HTTPS 证书
- ✅ 全球 CDN 加速
- ✅ 自动部署和回滚
- ✅ 详细的访问分析

## 🚀 下一步

1. 访问你的网站
2. 测试所有功能
3. 绑定自定义域名（可选）
4. 配置后端 API
5. 持续优化和迭代

---

**祝你部署顺利！** 🎊

如有问题，请查阅 Vercel 文档或寻求社区帮助。
