# 🎯 深聊平台部署方案选择指南

## 快速决策树

```
需要部署深聊平台？
    │
    ├─ 是否需要国内访问速度快？
    │   ├─ 是 → 选择 [方案 1: Vercel 香港节点] ⭐推荐
    │   └─ 否 → 选择 [方案 2: Vercel 默认节点]
    │
    ├─ 是否有一键部署需求？
    │   ├─ 是 → 使用 [一键部署脚本]
    │   └─ 否 → 手动部署
    │
    ├─ 是否有自有服务器？
    │   ├─ 是 → 选择 [方案 3: Nginx]
    │   └─ 否 → 使用 Vercel
    │
    └─ 是否需要完全控制？
        ├─ 是 → 选择 [方案 3: Nginx]
        └─ 否 → 使用 Vercel
```

---

## 方案对比总览

| 特性 | 方案 1: Vercel 香港节点 ⭐ | 方案 2: Vercel 默认节点 | 方案 3: Nginx |
|------|-------------------------|----------------------|-------------|
| **部署难度** | ⭐ 简单 | ⭐ 简单 | ⭐⭐⭐ 中等 |
| **部署时间** | 3 分钟 | 5 分钟 | 15-30 分钟 |
| **国内访问速度** | ⭐⭐⭐⭐⭐ 极快 | ⭐⭐ 较慢 | ⭐⭐⭐⭐⭐ 极快 |
| **费用** | ✅ 免费 | ✅ 免费 | ❌ 需要服务器费用 |
| **需要服务器** | ❌ 不需要 | ❌ 不需要 | ✅ 需要 |
| **自动 HTTPS** | ✅ 是 | ✅ 是 | ⚠️ 需配置 |
| **自动部署** | ✅ 是 | ✅ 是 | ⚠️ 需配置 |
| **自定义域名** | ✅ 支持 | ✅ 支持 | ✅ 支持 |
| **控制灵活度** | ⭐⭐ 中等 | ⭐⭐ 中等 | ⭐⭐⭐⭐⭐ 极高 |
| **推荐指数** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 🚀 方案 1: Vercel 香港节点（强烈推荐）⭐⭐⭐⭐⭐

### 适用场景
- ✅ 需要国内访问速度快
- ✅ 想要快速上线
- ✅ 不想配置服务器
- ✅ 需要自动 HTTPS
- ✅ 预算有限

### 优势
- ⚡ **国内访问速度极快**：使用香港节点，延迟 <100ms
- 🚀 **一键部署**：3 分钟完成部署
- 💰 **完全免费**：100GB 带宽/月
- 🔒 **自动 HTTPS**：无需配置 SSL
- 🔄 **自动部署**：GitHub 集成

### 部署步骤

#### Windows 用户
```powershell
cd web
.\scripts\deploy-vercel-hkg.bat
```

#### Mac/Linux 用户
```bash
cd web
chmod +x scripts/deploy-vercel-hkg.sh
./scripts/deploy-vercel-hkg.sh
```

### 访问地址
- 默认：`https://shenliao-web.vercel.app`
- 自定义：`https://your-domain.com`（可配置）

### 文档
- 📖 [3分钟快速部署指南](3_MIN_DEPLOY.md)
- 📖 [国内访问优化部署指南](QUICK_DEPLOY_CN.md)
- 📖 [Vercel 部署详细指南](VERCEL_DEPLOY.md)

---

## 🌐 方案 2: Vercel 默认节点

### 适用场景
- ✅ 国内访问速度要求不高
- ✅ 主要面向海外用户
- ✅ 想要快速上线
- ✅ 不想配置服务器

### 优势
- 🚀 **快速部署**：5 分钟完成
- 💰 **完全免费**：100GB 带宽/月
- 🔒 **自动 HTTPS**
- 🔄 **自动部署**

### 劣势
- ⚠️ **国内访问较慢**：使用美国节点，延迟 200-500ms

### 部署步骤
```bash
cd web
npm install -g vercel
vercel login
vercel --prod
```

### 访问地址
- 默认：`https://shenliao-web.vercel.app`

### 文档
- 📖 [Vercel 部署详细指南](VERCEL_DEPLOY.md)

---

## 🔧 方案 3: Nginx 反向代理

### 适用场景
- ✅ 有自有服务器
- ✅ 需要完全控制服务器
- ✅ 需要极快的国内访问速度
- ✅ 需要自定义配置
- ✅ 适合长期运营

### 优势
- ⚡ **国内访问速度极快**：部署在国内服务器
- 🎛️ **完全控制**：所有配置可自定义
- 🔒 **安全性高**：可配置防火墙、WAF 等
- 💾 **数据安全**：数据完全在自己服务器

### 劣势
- 💰 **需要服务器费用**：每月 50-200 元不等
- ⚠️ **配置复杂**：需要一定的服务器运维知识
- 🔄 **手动部署**：需要手动更新代码

### 部署步骤

#### 1. 准备服务器
- 购买云服务器（阿里云、腾讯云等）
- 安装 Node.js 18+ 和 Nginx

#### 2. 部署 Next.js
```bash
# 上传代码到服务器
cd /path/to/web
npm install
npm run build
pm2 start npm --name "shenliao-web" -- start
```

#### 3. 配置 Nginx
```bash
# 复制配置文件
sudo cp nginx/nginx.conf /etc/nginx/sites-available/shenliao-web

# 启用配置
sudo ln -s /etc/nginx/sites-available/shenliao-web /etc/nginx/sites-enabled/

# 测试配置
sudo nginx -t

# 重启 Nginx
sudo systemctl restart nginx
```

### 访问地址
- 默认：`http://your-server-ip`
- 自定义：`https://your-domain.com`

### 文档
- 📖 [Nginx 部署详细指南](NGINX_DEPLOY.md)

---

## 💡 推荐方案选择

### 个人开发者 / 小团队
**推荐：方案 1 - Vercel 香港节点**
- 快速上线
- 国内访问速度快
- 完全免费

### 企业用户 / 大流量网站
**推荐：方案 3 - Nginx**
- 完全控制
- 极快访问速度
- 可扩展性强

### 面向海外用户
**推荐：方案 2 - Vercel 默认节点**
- 全球访问均衡
- 部署简单

---

## 🎯 我的建议

### 首次部署？
→ **使用方案 1（Vercel 香港节点）**
```powershell
# Windows
cd web
.\scripts\deploy-vercel-hkg.bat

# Mac/Linux
cd web
./scripts/deploy-vercel-hkg.sh
```

### 需要自定义配置？
→ **使用方案 3（Nginx）**
```bash
cd web
bash scripts/deploy-nginx.sh
```

### 不确定？
→ **先用方案 1 快速体验，后续迁移到 Nginx**

---

## 📞 获取帮助

### 部署问题
- 📖 查看对应方案的详细文档
- 🔍 查看 [常见问题 FAQ](#常见问题)
- 📧 联系技术支持

### 常见问题

#### Q1: Vercel 香港节点和默认节点有什么区别？
**A**: 香港节点部署在香港，国内访问速度快（<100ms）；默认节点部署在美国，国内访问较慢（200-500ms）。

#### Q2: 如何从 Vercel 迁移到 Nginx？
**A**: 按照 Nginx 部署指南，将代码部署到服务器，配置 Nginx 反向代理即可。

#### Q3: 部署后如何访问？
**A**: Vercel 会提供一个 `.vercel.app` 域名，也可以配置自定义域名。

#### Q4: 如何配置 HTTPS？
**A**: Vercel 自动配置 HTTPS；Nginx 需要使用 Let's Encrypt 或购买 SSL 证书。

---

## 📚 完整文档列表

### 快速开始
- 🚀 [3分钟快速部署指南](3_MIN_DEPLOY.md)
- 📖 [国内访问优化部署指南](QUICK_DEPLOY_CN.md)

### 部署方案
- ⭐ [Vercel 香港节点部署](VERCEL_DEPLOY.md)
- 🌐 [Vercel 默认节点部署](VERCEL_DEPLOY.md)
- 🔧 [Nginx 部署指南](NGINX_DEPLOY.md)

### 访问问题
- 🔍 [访问问题解决方案](SOLUTION.md)
- 🌐 [访问指南](ACCESS.md)

### 其他
- 📖 [项目 README](README.md)
- ⚙️ [开发指南](README.md#开发注意事项)

---

## 🎉 选择一个方案，开始部署吧！

有问题？随时联系我们！💪
