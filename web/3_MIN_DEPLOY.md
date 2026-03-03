# 🚀 3 分钟快速部署指南

## 方法 1：一键部署（最简单）⭐⭐⭐⭐⭐

### Windows 用户

```powershell
# 进入 web 目录
cd web

# 运行部署脚本
.\scripts\deploy-vercel-hkg.bat
```

### Mac/Linux 用户

```bash
# 进入 web 目录
cd web

# 赋予执行权限
chmod +x scripts/deploy-vercel-hkg.sh

# 运行部署脚本
./scripts/deploy-vercel-hkg.sh
```

脚本会自动完成以下步骤：
1. ✅ 检查环境（Node.js、npm、Git）
2. ✅ 安装 Vercel CLI（如果需要）
3. ✅ 登录 Vercel（如果未登录）
4. ✅ 安装项目依赖
5. ✅ 构建项目
6. ✅ 部署到 Vercel 香港节点
7. ✅ 获取访问地址

---

## 方法 2：手动部署（更灵活）

### 步骤 1：安装 Vercel CLI

```bash
npm install -g vercel
```

### 步骤 2：登录 Vercel

```bash
vercel login
```

按照提示操作，选择 GitHub 登录。

### 步骤 3：部署

```bash
# 在 web 目录下执行
vercel --prod --regions=hkg1
```

等待 2-3 分钟，部署完成！

---

## 📱 部署后访问

部署成功后，你会得到一个 URL，格式如下：

```
https://shenliao-web.vercel.app
```

直接在浏览器中访问即可！

---

## 🌟 为什么选择 Vercel 香港节点？

### 优势

✅ **国内访问速度快**
- 使用香港节点，延迟 <100ms
- 相比美国节点，速度提升 3-5 倍

✅ **完全免费**
- 100GB 带宽/月
- 无限构建次数
- 自动 HTTPS

✅ **简单易用**
- 一键部署
- GitHub 自动集成
- 自动更新

✅ **原生支持 Next.js**
- 无需额外配置
- 自动优化
- 支持 Server Components

---

## 🎯 下一步

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

### 3. 配置 GitHub 自动部署

连接 GitHub 仓库后，每次推送代码会自动部署：

```bash
git add .
git commit -m "feat: 新功能"
git push
```

---

## ❓ 常见问题

### Q1: 部署失败怎么办？

**A**: 检查以下几点：
1. Node.js 版本是否 >= 18
2. 是否已登录 Vercel
3. 网络连接是否正常
4. 查看错误日志

### Q2: 如何查看部署日志？

**A**: 访问 Vercel Dashboard：
1. 进入项目
2. 点击 "Deployments"
3. 选择最近的部署
4. 查看 "Build Logs"

### Q3: 如何回滚到上一个版本？

**A**: 在 Vercel Dashboard 中：
1. 进入项目
2. 点击 "Deployments"
3. 找到之前的版本
4. 点击右侧的 "..." → "Promote to Production"

### Q4: 国内访问还是很慢？

**A**: 确保配置了香港节点：
- 在 `vercel.json` 中添加：`"regions": ["hkg1"]`
- 重新部署

---

## 📞 需要帮助？

- 📖 [Vercel 文档](https://vercel.com/docs)
- 📖 [Next.js 部署指南](https://nextjs.org/docs/deployment)
- 📖 [详细部署指南](./QUICK_DEPLOY_CN.md)

---

## 🎉 完成！

恭喜！深聊平台已成功部署到线上！

现在你可以：
- ✅ 访问网站
- ✅ 分享给团队成员
- ✅ 开始使用平台

有问题？随时联系我们！💪
