# 🎯 Vercel Dashboard 部署 - 详细步骤

由于命令行需要登录认证，使用 Vercel Dashboard（网页端）是最简单的方式。

## 📋 部署步骤（5分钟完成）

### 步骤 1: 准备代码 ✅

**已完成！** 代码已构建完成，可以直接部署。

### 步骤 2: 访问 Vercel Dashboard

**在浏览器中打开**: https://vercel.com/new

### 步骤 3: 创建新项目

#### 选项 A: 如果你的代码在 GitHub 上（推荐）

1. **登录 Vercel**
   - 使用 GitHub、GitLab、Bitbucket 或 Email 登录

2. **导入项目**
   - 点击 "Import Project"
   - 选择你的 GitHub 仓库
   - 如果仓库在 `web/` 目录，设置 Root Directory 为 `./web`

3. **配置项目**
   ```
   Framework Preset: Next.js
   Root Directory: ./web
   Build Command: npm run build
   Output Directory: .next
   ```

4. **环境变量（可选）**
   - 如果需要配置后端 API
   - 添加: `NEXT_PUBLIC_API_URL`
   - Value: 你的后端 API 地址

5. **部署**
   - 点击 "Deploy" 按钮
   - 等待 3-5 分钟

#### 选项 B: 如果代码没有在 GitHub 上

**方法 1: 上传文件夹**

1. **创建 GitHub 仓库** (2分钟)
   ```bash
   cd /path/to/project
   git init
   git add .
   git commit -m "Initial commit"
   
   # 创建 GitHub 仓库（在 GitHub 网站上操作）
   # 然后推送
   git remote add origin https://github.com/your-username/deepchat-web.git
   git branch -M main
   git push -u origin main
   ```

2. **然后在 Vercel 导入**（同选项 A）

**方法 2: 使用 Vercel CLI（需要登录）**

1. **登录 Vercel**
   ```bash
   vercel login
   ```
   然后在浏览器中完成 OAuth 认证。

2. **部署**
   ```bash
   cd web
   vercel
   ```
   按照提示操作，选择部署到预览环境。

3. **部署到生产环境**
   ```bash
   vercel --prod
   ```

### 步骤 4: 等待部署完成

- 构建时间: 2-3 分钟
- 部署时间: 1-2 分钟
- 总计: 3-5 分钟

### 步骤 5: 获取部署地址

部署完成后，你会得到：

- **预览环境**: https://deepchat-web-<username>.vercel.app
- **生产环境**: https://deepchat-web.vercel.app

## 🎯 推荐的完整流程

### 如果你还没有 GitHub 仓库

```bash
# 1. 初始化 Git
cd /path/to/project
git init
git add .
git commit -m "Initial commit"

# 2. 在 GitHub 上创建新仓库
# 访问: https://github.com/new
# 仓库名: deepchat-web
# 设为 Public 或 Private（都可以）

# 3. 推送代码
git remote add origin https://github.com/your-username/deepchat-web.git
git branch -M main
git push -u origin main

# 4. 在 Vercel 导入
# 访问: https://vercel.com/new
# 选择 GitHub 仓库
# 配置:
#   - Framework: Next.js
#   - Root Directory: ./web
#   - Build Command: npm run build
#   - Output Directory: .next

# 5. 点击 Deploy
```

### 如果你已经有 GitHub 仓库

直接在 Vercel 导入即可！

## ✅ 部署检查清单

- [ ] 已在 Vercel 注册/登录
- [ ] 代码已推送到 GitHub
- [ ] 在 Vercel 导入项目
- [ ] 配置正确（Framework: Next.js, Root Directory: ./web）
- [ ] 点击 Deploy
- [ ] 等待部署完成
- [ ] 获取部署地址
- [ ] 在浏览器中测试访问

## 🌐 访问你的网站

部署成功后，在浏览器中访问：

```
https://deepchat-web.vercel.app
```

或你的预览地址。

## 🧪 测试功能

访问网站后，测试以下功能：

- [ ] 首页正常显示
- [ ] 导航栏正常工作
- [ ] 项目列表页面
- [ ] 创建项目页面
- [ ] 项目详情页面
- [ ] 管理后台页面
- [ ] 响应式设计（移动端测试）

## 🔄 更新网站

### 自动部署（推荐）

使用 Git 集成后，每次推送代码会自动部署：

```bash
git add .
git commit -m "Update website"
git push origin main
```

### 手动部署

```bash
cd web
vercel --prod
```

## 🔧 配置自定义域名（可选）

1. 访问 Vercel Dashboard
2. 进入项目设置
3. 点击 "Domains"
4. 添加你的域名
5. 配置 DNS CNAME 记录

## 📊 监控部署

访问 Vercel Dashboard 查看：
- 部署历史
- 构建日志
- 访问日志
- 性能分析

## 🎉 完成！

恭喜！你的深聊网站现在已经上线了！

你现在拥有：
- ✅ 稳定的线上网站
- ✅ https://deepchat-web.vercel.app
- ✅ 自动 HTTPS
- ✅ 全球 CDN
- ✅ 免费托管
- ✅ 自动部署能力

## 💡 提示

- 使用 GitHub 集成是最简单的方式
- 每次推送代码会自动部署
- 可以随时回滚到之前的版本
- 免费套餐完全够用

---

**现在就开始部署吧！** 🚀

访问: https://vercel.com/new
