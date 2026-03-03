# 🚀 国内访问优化部署指南

本指南帮助你在 **5 分钟内** 将深聊平台部署到线上，并优化国内访问速度。

## 📋 部署方案对比

| 方案 | 免费额度 | 国内访问速度 | 部署难度 | 推荐度 |
|------|---------|-------------|---------|--------|
| **Vercel 香港节点** ⭐ | ✅ 100GB/月 | ⭐⭐⭐⭐ | 简单 | ⭐⭐⭐⭐⭐ |
| Cloudflare Pages | ✅ 无限 | ⭐⭐⭐ | 简单 | ⭐⭐⭐⭐ |
| Netlify | ✅ 100GB/月 | ⭐⭐⭐ | 简单 | ⭐⭐⭐ |
| 阿里云 OSS + CDN | ❌ 需付费 | ⭐⭐⭐⭐⭐ | 复杂 | ⭐⭐⭐ |

## 🎯 推荐：Vercel 香港节点

### 优势
- ✅ **国内访问速度快**：使用香港节点，延迟 <100ms
- ✅ **免费额度充足**：100GB 带宽/月
- ✅ **自动 HTTPS**
- ✅ **GitHub 自动部署**
- ✅ **原生支持 Next.js**

## 📝 部署步骤

### 方法 1：通过 GitHub 部署（推荐）

#### 步骤 1：准备 GitHub 仓库

```bash
# 在 web 目录下执行
cd /path/to/your/project/web

# 初始化 Git 仓库（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "feat: 深聊平台前端初始化"

# 连接到 GitHub 仓库
# 方式 A：如果已创建 GitHub 仓库
git remote add origin https://github.com/YOUR_USERNAME/shenliao-web.git
git branch -M main
git push -u origin main

# 方式 B：通过 GitHub CLI 创建并推送
gh repo create shenliao-web --public --source=. --remote=origin --push
```

#### 步骤 2：部署到 Vercel

1. **访问 Vercel**
   - 打开 https://vercel.com
   - 使用 GitHub 账号登录

2. **创建新项目**
   - 点击 "Add New" → "Project"
   - 从 "Import Git Repository" 选择你的 `shenliao-web` 仓库
   - 点击 "Import"

3. **配置项目**
   - **Project Name**: `shenliao-web`
   - **Framework Preset**: `Next.js`（自动检测）
   - **Root Directory**: `./`（默认）
   - **Build Command**: `npm run build`（自动填充）
   - **Output Directory**: `.next`（自动填充）
   - **Install Command**: `npm install`（自动填充）

4. **配置环境变量**
   - 点击 "Environment Variables"
   - 添加以下变量：
     ```
     NEXT_PUBLIC_API_URL=https://your-api-domain.com
     ```

5. **配置区域（关键步骤）**
   - 滚动到底部，点击 "Advanced"
   - 在 "Region" 下拉菜单中选择 **Hong Kong (hkg1)**
   - 这会显著改善国内访问速度！

6. **部署**
   - 点击 "Deploy" 按钮
   - 等待 2-3 分钟，部署完成！

7. **获取访问地址**
   - 部署完成后，Vercel 会提供一个默认域名
   - 格式：`https://shenliao-web.vercel.app`

#### 步骤 3：配置自定义域名（可选）

1. **准备域名**
   - 在阿里云/腾讯云购买域名（如 `shenliao.com`）

2. **在 Vercel 添加域名**
   - 进入项目设置 → Domains
   - 添加你的域名（如 `app.shenliao.com`）

3. **配置 DNS**
   - Vercel 会提供 DNS 记录
   - 在域名服务商添加 CNAME 记录：
     ```
     Type: CNAME
     Name: app
     Value: cname.vercel-dns.com
     ```

4. **等待生效**
   - DNS 传播通常需要 10-30 分钟
   - 访问 `https://app.shenliao.com` 测试

---

### 方法 2：使用 Vercel CLI 快速部署

```bash
# 安装 Vercel CLI
npm install -g vercel

# 登录 Vercel
vercel login

# 在 web 目录下执行
cd /path/to/your/project/web

# 部署
vercel --prod --regions=hkg1

# 按照提示操作：
# 1. Set up and deploy "~/your/project/web"? [Y/n] → Y
# 2. Link to existing project? [y/N] → N
# 3. What's your project's name? → shenliao-web
# 4. In which directory is your code located? → ./
# 5. Want to override the settings? [y/N] → N

# 部署完成后，你会得到一个 URL
# 例如：https://shenliao-web.vercel.app
```

---

## 🌐 其他部署方案

### Cloudflare Pages 部署

1. **访问 Cloudflare Pages**
   - 打开 https://pages.cloudflare.com
   - 使用 Cloudflare 账号登录（免费注册）

2. **创建项目**
   - 点击 "Create a project"
   - 选择 "Connect to Git"
   - 连接你的 GitHub 仓库

3. **配置构建设置**
   - **Framework preset**: `Next.js`
   - **Build command**: `npm run build`
   - **Build output directory**: `.next`

4. **部署**
   - 点击 "Save and Deploy"
   - 等待 2-3 分钟

5. **获取访问地址**
   - 格式：`https://your-project.pages.dev`

### Netlify 部署

```bash
# 安装 Netlify CLI
npm install -g netlify-cli

# 登录 Netlify
netlify login

# 在 web 目录下执行
cd /path/to/your/project/web

# 部署
netlify deploy --prod

# 按照提示操作
# 部署完成后，你会得到一个 URL
```

---

## ⚡ 性能优化建议

### 1. 启用 CDN 缓存

在 `next.config.js` 中添加：

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ['your-cdn-domain.com'],
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.vercel.app',
      },
    ],
  },
  compress: true,
  swcMinify: true,
}

module.exports = nextConfig
```

### 2. 配置国内 CDN（可选）

如果你使用阿里云 OSS：

```javascript
// next.config.js
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.aliyuncs.com',
      },
    ],
  },
}
```

### 3. 使用国内镜像加速依赖

在 `.npmrc` 中添加：

```
registry=https://registry.npmmirror.com
```

---

## 🔍 验证部署

部署完成后，执行以下验证：

### 1. 检查网站访问

```bash
# 检查网站是否可访问
curl -I https://shenliao-web.vercel.app

# 应该返回 200 OK
```

### 2. 测试国内访问速度

```bash
# 使用国内节点测试延迟
# 从北京访问
ping shenliao-web.vercel.app

# 预期延迟：<100ms（香港节点）
```

### 3. 检查 HTTPS

访问 `https://shenliao-web.vercel.app`，确认：
- ✅ 浏览器显示锁形图标
- ✅ 地址栏显示 "https://"
- ✅ 没有安全警告

---

## 🐛 常见问题

### Q1: 部署后页面 404

**原因**：Next.js 构建配置问题

**解决**：
```json
// vercel.json
{
  "buildCommand": "npm run build",
  "outputDirectory": ".next"
}
```

### Q2: 国内访问很慢

**原因**：使用了默认的美国节点

**解决**：在 `vercel.json` 中配置香港节点：
```json
{
  "regions": ["hkg1"]
}
```

### Q3: 图片无法加载

**原因**：Next.js 图片域名未配置

**解决**：在 `next.config.js` 中添加域名：
```javascript
images: {
  domains: ['your-image-domain.com']
}
```

### Q4: API 跨域问题

**原因**：后端 API 未配置 CORS

**解决**：在后端添加 CORS 中间件：
```python
# FastAPI 示例
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📞 技术支持

如果遇到部署问题：

1. **查看部署日志**：在 Vercel Dashboard 查看构建日志
2. **检查环境变量**：确认所有环境变量已正确配置
3. **检查 API 连接**：确认后端 API 可以访问
4. **查看 Next.js 文档**：https://nextjs.org/docs/deployment

---

## 🎉 完成！

现在你可以访问：
- **生产环境**: https://shenliao-web.vercel.app
- **自定义域名**: https://app.shenliao.com（如果配置）

恭喜！深聊平台已成功部署到线上！🚀
