# 🚀 Vercel 部署 - 立即开始

本指南将帮助你**5分钟内**将深聊网站部署到 Vercel，获得一个免费、稳定、支持 HTTPS 的线上环境。

## ⚡ 快速部署（推荐）

### 方式 1: 使用部署向导（最简单）

```bash
cd web
bash scripts/vercel-wizard.sh
```

这个脚本会引导你完成所有步骤：
1. ✅ 检查并安装 Vercel CLI
2. ✅ 登录 Vercel 账号
3. ✅ 构建项目测试
4. ✅ 部署到预览环境
5. ✅ 部署到生产环境

### 方式 2: 使用快速部署脚本

```bash
cd web
npm install -g vercel
vercel login
bash scripts/deploy-vercel.sh
```

## 📋 手动部署步骤

如果你想了解每个步骤的细节，可以手动执行：

### 步骤 1: 安装 Vercel CLI（已完成 ✅）

```bash
npm install -g vercel
```

**当前状态**: Vercel CLI 50.25.6 已安装

### 步骤 2: 登录 Vercel

```bash
vercel login
```

**登录方式选择**:
- **GitHub** (推荐) - 如果你有 GitHub 账号
- **GitLab** - 如果你有 GitLab 账号
- **Bitbucket** - 如果你有 Bitbucket 账号
- **Email** - 使用邮箱登录

**登录流程**:
1. 运行 `vercel login`
2. 选择登录方式（推荐选择 GitHub）
3. 按照提示在浏览器中授权
4. 等待登录完成

### 步骤 3: 部署项目

#### 部署到预览环境（Preview）

```bash
cd web
vercel
```

Vercel 会问你几个问题：

```
? Set up and deploy "~/web"? [Y/n] Y
? Which scope do you want to deploy to? (选择你的用户名)
? Link to existing project? [y/N] N
? What's your project's name? deepchat-web
? In which directory is your code located? ./
? Want to override the settings? [y/N] N
```

**预览环境地址**: https://deepchat-web-<username>.vercel.app

#### 部署到生产环境（Production）

```bash
vercel --prod
```

**生产环境地址**: https://deepchat-web.vercel.app

## 🔧 配置环境变量（可选）

如果你有后端 API，需要配置环境变量：

### 1. 访问 Vercel Dashboard

https://vercel.com/dashboard

### 2. 进入项目设置

1. 找到你的项目 `deepchat-web`
2. 点击 "Settings"
3. 点击 "Environment Variables"

### 3. 添加环境变量

```
Name: NEXT_PUBLIC_API_URL
Value: https://your-backend-api.com
Environment: Production, Preview, Development
```

### 4. 重新部署

添加环境变量后，需要重新部署：

```bash
vercel --prod
```

## 🌐 访问你的网站

### 预览环境
```
https://deepchat-web-<username>.vercel.app
```

### 生产环境
```
https://deepchat-web.vercel.app
```

**替换 `<username>` 为你的 Vercel 用户名**

## 📱 测试你的网站

部署成功后，在浏览器中访问你的网站，测试以下功能：

### ✅ 基础功能
- [ ] 首页正常显示
- [ ] 导航栏正常工作
- [ ] 页面样式正常

### ✅ 页面功能
- [ ] 项目列表页面
- [ ] 创建项目页面
- [ ] 项目详情页面
- [ ] 管理后台页面

### ✅ 交互功能
- [ ] 搜索功能
- [ ] 筛选功能
- [ ] 表单提交
- [ ] 数据刷新

## 🔄 更新部署

### 方式 1: 自动部署（GitHub 集成）

如果你将代码推送到 GitHub，每次推送都会自动部署：

```bash
git add .
git commit -m "Update website"
git push origin main
```

### 方式 2: 手动部署

```bash
cd web
vercel --prod
```

## 📊 查看部署状态

### 查看部署历史

```bash
vercel list
```

### 查看当前部署

```bash
vercel inspect
```

### 查看日志

```bash
vercel logs
```

### 实时查看日志

```bash
vercel logs --follow
```

## 🎨 自定义域名（可选）

### 1. 添加域名

1. 访问 Vercel Dashboard
2. 进入你的项目
3. 点击 "Domains"
4. 添加你的域名（例如: `deepchat.yourdomain.com`）

### 2. 配置 DNS

在你的域名 DNS 管理中添加 CNAME 记录：

```
Type: CNAME
Name: deepchat
Value: cname.vercel-dns.com
```

### 3. 等待生效

DNS 生效通常需要几分钟到几小时不等。

## 🔒 HTTPS

✅ **自动配置**: Vercel 会自动为你的网站配置 HTTPS 证书，无需手动操作。

## 📈 监控和分析

### 访问 Vercel Analytics

1. 访问 Vercel Dashboard
2. 进入你的项目
3. 点击 "Analytics"

### 查看的数据

- 访问量
- 页面浏览量
- 用户地理位置
- 设备类型
- 页面加载时间

## 🐛 常见问题

### Q1: 登录失败怎么办？

**解决**:
1. 确保网络连接正常
2. 尝试使用不同的登录方式
3. 清除浏览器缓存后重试

### Q2: 部署失败怎么办？

**解决**:
1. 查看部署日志: `vercel logs`
2. 检查构建错误
3. 确保依赖已安装

### Q3: 环境变量不生效？

**解决**:
1. 确保变量名以 `NEXT_PUBLIC_` 开头
2. 重新部署: `vercel --prod`
3. 确认环境变量在所有环境中都配置了

### Q4: 如何回滚到之前的版本？

**解决**:
1. 访问 Vercel Dashboard
2. 进入你的项目
3. 点击 "Deployments"
4. 选择要回滚的部署
5. 点击 "..." → "Promote to Production"

### Q5: 访问速度慢？

**解决**:
1. 检查是否有大文件未优化
2. 启用 Vercel Analytics 分析性能
3. 使用 Vercel 的 Image Optimization

## 💡 优化建议

### 1. 启用图片优化

Next.js Image 组件已经配置好了，确保使用：

```javascript
import Image from 'next/image'

<Image src="/image.jpg" width={500} height={300} />
```

### 2. 配置缓存

在 `vercel.json` 中配置重定向和缓存规则。

### 3. 使用 Edge Functions

将一些计算密集型操作放到 Edge Functions 中。

## 📚 相关文档

- **完整指南**: web/VERCEL_DEPLOY.md
- **总体部署指南**: web/DEPLOYMENT.md
- **项目文档**: web/README.md
- **Vercel 官方文档**: https://vercel.com/docs

## 🎉 部署完成清单

- [ ] Vercel CLI 已安装
- [ ] 已登录 Vercel 账号
- [ ] 项目已部署到预览环境
- [ ] 预览环境测试通过
- [ ] 项目已部署到生产环境
- [ ] 生产环境测试通过
- [ ] 环境变量已配置（如需要）
- [ ] 自定义域名已配置（可选）

## 🚀 立即开始

选择以下任一方式开始部署：

### 方式 1: 使用部署向导（推荐新手）
```bash
cd web
bash scripts/vercel-wizard.sh
```

### 方式 2: 使用快速部署脚本
```bash
cd web
npm install -g vercel
vercel login
bash scripts/deploy-vercel.sh
```

### 方式 3: 手动部署
```bash
cd web
npm install -g vercel
vercel login
vercel
vercel --prod
```

## 📞 需要帮助？

- 查看 Vercel 文档
- 检查部署日志
- 访问 Vercel 社区

---

**祝你部署顺利！5分钟后你将拥有一个线上网站！** 🎊

开始部署吧！🚀
