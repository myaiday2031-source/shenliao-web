# 🌐 Coze 云端环境部署指南

## 📊 当前环境状态

你的项目位于 **Coze Coding 云端开发环境**：

- **项目路径**: `/workspace/projects/web`
- **Node.js**: v22.22.0 ✅
- **npm**: 10.9.4 ✅
- **Vercel CLI**: v50.25.6 ✅
- **项目状态**: 已构建 ✅

---

## 🎯 推荐方案：GitHub + Vercel 自动部署

由于 Coze 云端环境的限制，推荐使用 **GitHub + Vercel 自动部署** 方案。

### 为什么选择这个方案？

✅ **无需登录 Vercel CLI**
✅ **自动部署**
✅ **GitHub 版本管理**
✅ **简单易用**
✅ **香港节点支持**

---

## 📝 部署步骤

### 步骤 1：准备 GitHub 仓库

1. **创建 GitHub 仓库**
   - 访问 https://github.com/new
   - 仓库名：`shenliao-web`
   - 勾选 "Initialize this repository with a README"
   - 点击 "Create repository"

2. **获取仓库地址**
   - 复制你的仓库 URL，格式：
   ```
   https://github.com/YOUR_USERNAME/shenliao-web.git
   ```

### 步骤 2：在 Coze 环境中配置 Git

**在 Coze 的命令行中执行：**

```bash
# 进入项目目录
cd /workspace/projects

# 添加 Git remote（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/shenliao-web.git

# 设置主分支
git branch -M main

# 推送到 GitHub（需要输入 GitHub 凭证）
git push -u origin main
```

**输入凭证时：**
- Username: 你的 GitHub 用户名
- Password: 使用 **Personal Access Token**（不是密码）
  - 访问 https://github.com/settings/tokens
  - 点击 "Generate new token" → "Generate new token (classic)"
  - 勾选 `repo` 权限
  - 生成并复制 token

### 步骤 3：在 Vercel 中部署

1. **访问 Vercel**
   - 打开 https://vercel.com/new
   - 使用 GitHub 账号登录

2. **导入项目**
   - 在 "Import Git Repository" 中找到 `shenliao-web`
   - 点击 "Import"

3. **配置项目**

   保持默认设置即可：
   - **Framework Preset**: Next.js（自动检测）
   - **Root Directory**: `./`（默认）
   - **Build Command**: `npm run build`（自动填充）
   - **Output Directory**: `.next`（自动填充）
   - **Install Command**: `npm install`（自动填充）

4. **部署**
   - 点击 "Deploy"
   - 等待 2-3 分钟

5. **配置香港节点**（优化国内访问）

   部署完成后：
   - 进入项目设置
   - 找到 "General" → "Regions"
   - 选择 "Hong Kong (hkg1)"
   - 保存并重新部署

### 步骤 4：访问网站

部署成功后，Vercel 会提供一个 URL：

```
https://shenliao-web.vercel.app
```

直接在浏览器中访问即可！

---

## 🚀 快速命令参考

### 在 Coze 环境中执行

```bash
# 1. 提交代码
cd /workspace/projects
git add .
git commit -m "feat: 准备部署深聊平台前端"

# 2. 配置 Git remote（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/shenliao-web.git

# 3. 推送到 GitHub
git branch -M main
git push -u origin main
```

---

## ⚠️ 常见问题

### Q1: Git push 时提示 "Authentication failed"

**原因**: 使用了密码而不是 Personal Access Token

**解决**:
1. 访问 https://github.com/settings/tokens
2. 生成新 token（勾选 `repo` 权限）
3. 使用 token 作为密码（而不是 GitHub 密码）

### Q2: 提示 "remote origin already exists"

**原因**: 已经配置过 Git remote

**解决**:
```bash
# 删除已有的 remote
git remote remove origin

# 重新添加
git remote add origin https://github.com/YOUR_USERNAME/shenliao-web.git
```

### Q3: Vercel 部署失败

**原因**: 构建配置问题

**解决**:
- 查看 Vercel 的构建日志
- 确保构建命令是 `npm run build`
- 确保输出目录是 `.next`

### Q4: 如何配置香港节点？

**解决**:
1. 部署完成后，进入 Vercel 项目设置
2. 找到 "Regions" 或 "区域" 设置
3. 选择 "Hong Kong (hkg1)"
4. 保存并重新部署

---

## 📱 部署后访问

### 访问地址

- **默认地址**: `https://shenliao-web.vercel.app`
- **自定义域名**: 可在 Vercel 中配置

### 验证部署

在浏览器中访问 URL，检查：
- ✅ 页面正常显示
- ✅ 所有链接可点击
- ✅ 样式正常

---

## 🎉 完成！

恭喜！深聊平台已成功部署到线上！

### 后续更新

每次修改代码后：

```bash
cd /workspace/projects
git add .
git commit -m "feat: 更新内容"
git push
```

Vercel 会自动部署新版本！

---

## 📚 其他方案

### 方案 A：使用 Vercel Token 部署

如果你不想使用 GitHub，可以使用 Vercel Token：

1. 创建 Vercel Token
   - 访问 https://vercel.com/account/tokens
   - 点击 "Create"
   - 复制 Token

2. 在 Coze 环境中部署
   ```bash
   cd /workspace/projects/web
   vercel login --token YOUR_TOKEN
   vercel --prod --regions=hkg1
   ```

### 方案 B：下载到本地部署

如果云端环境操作不便：

1. 导出代码（联系 Coze 支持）
2. 在本地克隆或下载
3. 使用本地部署脚本

---

## 📞 需要帮助？

- 📖 查看详细文档：[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- 📖 查看 Vercel 文档：https://vercel.com/docs
- 🔍 查看 [常见问题](#常见问题)

---

**选择方案，开始部署吧！** 🚀
