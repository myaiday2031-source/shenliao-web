# 🚀 开始使用深聊平台

欢迎来到深聊平台！按照以下步骤，快速将平台部署到线上。

---

## ⚡ 3 分钟快速部署（推荐）

### Windows 用户
```powershell
cd web
.\scripts\deploy-vercel-hkg.bat
```

### Mac/Linux 用户
```bash
cd web
chmod +x scripts/deploy-vercel-hkg.sh
./scripts/deploy-vercel-hkg.sh
```

**就这么简单！** 🎉

等待 3 分钟，你会得到一个访问地址，直接在浏览器中打开即可！

---

## 📋 我可以帮你部署吗？

**可以！** 我可以帮你完成以下操作：

### 我能做的：
- ✅ 创建部署脚本
- ✅ 生成部署配置文件
- ✅ 编写详细部署文档
- ✅ 提供部署问题解决方案

### 需要你做的：
- 📝 执行部署脚本
- 🔑 登录 Vercel 账号（首次需要）
- 🌐 访问部署后的网站

**为什么不能完全自动部署？**
- 部署需要访问你的 Vercel 账号
- 需要你授权（登录）
- 这是安全要求，必须由你完成

---

## 🎯 选择部署方案

### 方案对比

| 方案 | 部署时间 | 国内访问速度 | 费用 | 推荐度 |
|------|---------|-------------|------|--------|
| **Vercel 香港节点** ⭐ | 3 分钟 | ⭐⭐⭐⭐⭐ | 免费 | ⭐⭐⭐⭐⭐ |
| **Vercel 默认节点** | 5 分钟 | ⭐⭐ | 免费 | ⭐⭐⭐ |
| **Nginx** | 15-30 分钟 | ⭐⭐⭐⭐⭐ | 需付费 | ⭐⭐⭐⭐ |

### 推荐选择：
- **首次使用** → Vercel 香港节点
- **国内访问要求高** → Vercel 香港节点
- **长期运营** → Nginx

---

## 📖 详细文档

### 快速部署
- 🚀 [3分钟快速部署指南](3_MIN_DEPLOY.md)
- 🌐 [国内访问优化部署指南](QUICK_DEPLOY_CN.md)

### 方案选择
- 📋 [部署方案选择指南](DEPLOYMENT_GUIDE.md)

### 详细教程
- ⭐ [Vercel 香港节点部署](VERCEL_DEPLOY.md)
- 🔧 [Nginx 部署指南](NGINX_DEPLOY.md)
- 🌐 [Vercel 默认节点部署](VERCEL_DEPLOY.md)

### 问题解决
- 🔍 [访问问题解决方案](SOLUTION.md)
- 📖 [访问指南](ACCESS.md)

---

## 🎓 部署前准备

### 必需准备
- ✅ Node.js 18+ 已安装
- ✅ npm 已安装
- ✅ Git 已安装（可选，用于 GitHub 部署）

### 可选准备
- ✅ Vercel 账号（首次部署需要）
- ✅ GitHub 账号（用于自动部署）
- ✅ 自定义域名（可选）

### 检查环境
```bash
# 检查 Node.js 版本
node -v  # 应该 >= 18

# 检查 npm 版本
npm -v

# 检查 Git 版本（可选）
git --version
```

---

## 🚀 开始部署

### 方法 1: 一键部署（最简单）

#### Windows
```powershell
cd web
.\scripts\deploy-vercel-hkg.bat
```

#### Mac/Linux
```bash
cd web
chmod +x scripts/deploy-vercel-hkg.sh
./scripts/deploy-vercel-hkg.sh
```

脚本会自动完成：
1. ✅ 检查环境
2. ✅ 安装依赖
3. ✅ 构建项目
4. ✅ 部署到 Vercel 香港节点
5. ✅ 显示访问地址

### 方法 2: 手动部署

```bash
cd web

# 安装 Vercel CLI
npm install -g vercel

# 登录 Vercel
vercel login

# 部署
vercel --prod --regions=hkg1
```

---

## 🎉 部署成功！

部署完成后，你会看到：

```
✅ 部署成功！

📱 访问地址：
  https://shenliao-web.vercel.app

💡 提示：
  1. Vercel 会提供一个默认域名
  2. 如需自定义域名，请在 Vercel Dashboard 中配置
  3. 香港节点优化了国内访问速度，延迟 <100ms
```

直接在浏览器中访问地址即可！

---

## 🌟 下一步

### 1. 配置后端 API
在 Vercel Dashboard 中配置环境变量：
```
NEXT_PUBLIC_API_URL=https://your-api-domain.com
```

### 2. 配置自定义域名（可选）
如果你有自己的域名：
1. 在 Vercel Dashboard 中添加域名
2. 配置 DNS 记录
3. 等待 DNS 生效（10-30 分钟）

### 3. 连接 GitHub（可选）
连接 GitHub 仓库后，每次推送代码会自动部署：
```bash
git add .
git commit -m "feat: 新功能"
git push
```

---

## ❓ 常见问题

### Q1: 部署需要多长时间？
**A**: 使用一键部署脚本，大约 3-5 分钟。

### Q2: 需要多少钱？
**A**: Vercel 香港节点完全免费，100GB 带宽/月。

### Q3: 国内访问速度快吗？
**A**: 使用香港节点，国内访问延迟 <100ms，速度很快！

### Q4: 如何配置自定义域名？
**A**: 在 Vercel Dashboard 中添加域名，配置 DNS 记录即可。

### Q5: 部署失败了怎么办？
**A**: 查看部署日志，检查错误信息，参考[访问问题解决方案](SOLUTION.md)

---

## 📞 获取帮助

### 文档
- 📖 查看 [完整部署指南](DEPLOYMENT_GUIDE.md)
- 🔍 查看 [访问问题解决方案](SOLUTION.md)

### 常见问题
- 查看 [常见问题 FAQ](#常见问题)

### 联系支持
如有问题，随时联系我们！

---

## 🎉 准备好了吗？

选择一个部署方案，开始部署吧！

```powershell
# Windows
cd web
.\scripts\deploy-vercel-hkg.bat

# Mac/Linux
cd web
./scripts/deploy-vercel-hkg.sh
```

**3 分钟后，你的网站就可以上线了！** 🚀
