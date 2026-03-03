# 🚀 深聊网站线上部署指南

本指南提供两种快速将深聊网站部署到线上的方案，你可以根据自己的需求选择最适合的一种。

## 📋 两种方案对比

| 特性 | Vercel 部署 | Nginx 反向代理 |
|-----|------------|---------------|
| **部署难度** | ⭐ 简单 | ⭐⭐⭐ 中等 |
| **免费额度** | ✅ 免费 | ✅ 免费（自有服务器） |
| **部署时间** | 5-10 分钟 | 10-20 分钟 |
| **需要服务器** | ❌ 不需要 | ✅ 需要 |
| **HTTPS** | ✅ 自动配置 | ⚠️ 需手动配置 |
| **自定义域名** | ✅ 简单 | ⚠️ 需手动配置 |
| **访问速度** | ⭐⭐⭐⭐⭐ 全球CDN | ⭐⭐⭐ 取决于服务器 |
| **适合场景** | 快速上线、演示 | 长期运行、可控性高 |

## 🎯 选择建议

### 选择 Vercel 如果：
- ✅ 想要快速上线（5分钟）
- ✅ 没有自己的服务器
- ✅ 需要全球 CDN 加速
- ✅ 需要 HTTPS
- ✅ 项目在 GitHub 上

### 选择 Nginx 如果：
- ✅ 有自己的服务器
- ✅ 需要完全控制
- ✅ 需要自定义配置
- ✅ 长期运行
- ✅ 需要集成其他服务

## 🚀 方案 1: Vercel 部署（推荐，最快）

### 快速开始

#### 1. 安装 Vercel CLI

```bash
npm install -g vercel
```

#### 2. 登录 Vercel

```bash
vercel login
```

#### 3. 一键部署

```bash
cd web
bash scripts/deploy-vercel.sh
```

### 详细文档

查看 `web/VERCEL_DEPLOY.md` 获取详细的 Vercel 部署指南。

### 优势

- ⚡ **超快部署**: 5分钟内完成
- 🌍 **全球CDN**: 自动部署到全球节点
- 🔒 **自动HTTPS**: 自动配置SSL证书
- 🔄 **自动部署**: GitHub集成，推送即部署
- 📊 **内置分析**: 免费Web Analytics
- 💰 **完全免费**: 免费套餐足够使用

### 访问地址

部署完成后，你会得到：
- 预览地址: `https://deepchat-web-<username>.vercel.app`
- 生产地址: `https://deepchat-web.vercel.app`

## 🚀 方案 2: Nginx 反向代理

### 快速开始

#### 1. 运行部署脚本

```bash
cd web
bash scripts/deploy-nginx.sh
```

### 详细文档

查看 `web/NGINX_DEPLOY.md` 获取详细的 Nginx 部署指南。

### 优势

- 🔧 **完全控制**: 完全掌控服务器配置
- 💾 **本地存储**: 可以访问本地文件系统
- 🌐 **自定义域名**: 灵活配置域名和SSL
- 🔌 **服务集成**: 方便集成其他服务
- 📈 **性能优化**: 可自定义优化配置
- 💰 **成本低**: 使用自有服务器

### 访问地址

部署完成后，你可以通过以下地址访问：
- http://localhost
- http://你的服务器IP
- http://你的自定义域名

## 📊 部署流程对比

### Vercel 部署流程

```
1. 安装 Vercel CLI (1分钟)
2. 登录 Vercel (1分钟)
3. 运行部署脚本 (2分钟)
4. 配置环境变量 (1分钟)
5. 完成！
```

**总时间**: 约5分钟

### Nginx 部署流程

```
1. 安装 Nginx (2分钟)
2. 启动 Next.js 服务 (1分钟)
3. 配置 Nginx (3分钟)
4. 测试配置 (2分钟)
5. 重启 Nginx (1分钟)
6. 完成！
```

**总时间**: 约10-15分钟

## 🔧 配置后端 API

无论选择哪种部署方式，都需要配置后端 API：

### 1. 配置环境变量

在部署平台中添加环境变量：

```
NEXT_PUBLIC_API_URL = https://your-backend-api.com
```

### 2. 配置 CORS

确保后端 API 允许来自你的前端域名的跨域请求。

### 3. 测试连接

部署后，测试前后端连接是否正常。

## 🎯 部署检查清单

### Vercel 部署检查清单

- [ ] 安装 Vercel CLI
- [ ] 登录 Vercel 账号
- [ ] 运行部署脚本
- [ ] 配置环境变量
- [ ] 测试预览环境
- [ ] 部署到生产环境
- [ ] 测试生产环境
- [ ] 配置自定义域名（可选）
- [ ] 配置后端 API

### Nginx 部署检查清单

- [ ] 安装 Nginx
- [ ] 启动 Next.js 服务
- [ ] 配置 Nginx 反向代理
- [ ] 测试 Nginx 配置
- [ ] 重启 Nginx
- [ ] 测试访问
- [ ] 配置 HTTPS（推荐）
- [ ] 配置自定义域名（可选）
- [ ] 配置后端 API
- [ ] 设置 PM2 守护进程（推荐）

## 📝 环境变量配置

无论哪种方案，都需要配置以下环境变量：

```bash
# 后端 API 地址（必填）
NEXT_PUBLIC_API_URL=https://your-backend-api.com
```

### 在 Vercel 中配置

1. 访问 Vercel Dashboard
2. 进入项目设置
3. Environment Variables
4. 添加变量

### 在 Nginx 部署中配置

在 `web/.env.local` 文件中配置：

```bash
NEXT_PUBLIC_API_URL=https://your-backend-api.com
```

## 🌐 配置自定义域名

### Vercel

1. 访问 Vercel Dashboard
2. 进入项目设置
3. Domains
4. 添加域名
5. 配置 DNS CNAME 记录

### Nginx

1. 编辑 Nginx 配置文件
2. 修改 `server_name`
3. 重启 Nginx
4. 配置 DNS A 记录

## 🔒 配置 HTTPS

### Vercel

✅ 自动配置，无需操作

### Nginx

```bash
# 安装 Certbot
sudo apt-get install -y certbot python3-certbot-nginx

# 获取证书
sudo certbot --nginx -d yourdomain.com
```

## 📊 监控和日志

### Vercel

- 访问 Vercel Dashboard
- 查看 Analytics 和 Logs

### Nginx

```bash
# 访问日志
sudo tail -f /var/log/nginx/deepchat-access.log

# 错误日志
sudo tail -f /var/log/nginx/deepchat-error.log
```

## 🔄 更新部署

### Vercel

```bash
# 推送代码到 GitHub
git add .
git commit -m "Update"
git push origin main

# 或者使用 CLI
vercel --prod
```

### Nginx

```bash
# 更新代码
cd web
git pull

# 重启服务
pm2 restart deepchat-web

# 或
sudo systemctl restart nginx
```

## 🐛 常见问题

### Q: 部署后无法访问？

**Vercel**:
1. 检查部署日志
2. 检查环境变量
3. 查看构建错误

**Nginx**:
1. 检查 Nginx 状态
2. 检查 Next.js 服务
3. 查看错误日志

### Q: 如何回滚？

**Vercel**:
在 Dashboard 中选择之前的部署，点击 "Promote to Production"

**Nginx**:
```bash
git checkout <previous-commit>
pm2 restart deepchat-web
```

### Q: 性能如何优化？

查看各自的详细文档：
- Vercel: `web/VERCEL_DEPLOY.md`
- Nginx: `web/NGINX_DEPLOY.md`

## 📚 相关文档

- **Vercel 部署**: `web/VERCEL_DEPLOY.md`
- **Nginx 部署**: `web/NGINX_DEPLOY.md`
- **快速启动**: `web/QUICKSTART.md`
- **访问指南**: `web/ACCESS.md`

## 🎉 部署成功标志

部署成功后，你应该能够：

- ✅ 在浏览器中访问网站
- ✅ 看到完整的首页
- ✅ 正常导航到各个页面
- ✅ 创建新项目
- ✅ 查看项目详情
- ✅ 访问管理后台

## 🚀 立即开始

### 选择 Vercel（推荐新手）

```bash
cd web
bash scripts/deploy-vercel.sh
```

### 选择 Nginx（推荐有服务器的用户）

```bash
cd web
bash scripts/deploy-nginx.sh
```

## 💡 建议

- **快速上线**: 使用 Vercel，5分钟搞定
- **长期运营**: 使用 Nginx，可控性更高
- **两者结合**: Vercel 做前端，Nginx 做反向代理

## 📞 需要帮助？

- 查看详细文档
- 检查部署日志
- 寻求社区帮助

---

**祝你部署顺利！** 🎊

选择适合你的方案，5-15分钟即可完成部署！
