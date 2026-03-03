# 🚀 深聊平台 - 快速命令参考

## 一键部署

### Windows
```powershell
cd web
.\scripts\deploy-vercel-hkg.bat
```

### Mac/Linux
```bash
cd web
chmod +x scripts/deploy-vercel-hkg.sh
./scripts/deploy-vercel-hkg.sh
```

---

## 本地开发

### 安装依赖
```bash
cd web
npm install
```

### 启动开发服务器
```bash
npm run dev
```
访问: http://localhost:3000

### 构建生产版本
```bash
npm run build
npm start
```

---

## 部署验证

### 验证部署是否成功
```bash
cd web
chmod +x scripts/verify-deployment.sh
./scripts/verify-deployment.sh https://your-url.vercel.app
```

---

## 手动部署

### Vercel CLI 部署
```bash
cd web
npm install -g vercel
vercel login
vercel --prod --regions=hkg1
```

---

## 快速链接

| 需求 | 文档 |
|------|------|
| 🚀 立即部署 | [START_HERE.md](START_HERE.md) |
| ⚡ 3 分钟部署 | [3_MIN_DEPLOY.md](3_MIN_DEPLOY.md) |
| 📋 方案选择 | [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) |
| 🔧 Vercel 详细教程 | [VERCEL_DEPLOY.md](VERCEL_DEPLOY.md) |
| 🔧 Nginx 详细教程 | [NGINX_DEPLOY.md](NGINX_DEPLOY.md) |
| ❓ 问题解决 | [SOLUTION.md](SOLUTION.md) |

---

## 常用命令

### Git 操作
```bash
# 初始化仓库
git init

# 添加所有文件
git add .

# 提交
git commit -m "feat: 更新内容"

# 推送到 GitHub
git push origin main
```

### NPM 操作
```bash
# 安装依赖
npm install

# 安装指定包
npm install package-name

# 运行开发服务器
npm run dev

# 构建
npm run build

# 启动生产服务器
npm start

# 检查依赖
npm audit
```

### Vercel 操作
```bash
# 登录
vercel login

# 部署到预览环境
vercel

# 部署到生产环境
vercel --prod

# 部署到指定区域（香港）
vercel --prod --regions=hkg1

# 查看部署日志
vercel logs

# 查看项目信息
vercel inspect
```

---

## 环境变量

### 本地开发
创建 `.env.local` 文件：
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 生产环境
在 Vercel Dashboard 中配置：
```
NEXT_PUBLIC_API_URL=https://your-api-domain.com
```

---

## 端口说明

| 服务 | 端口 | 说明 |
|------|------|------|
| Next.js 开发服务器 | 3000 | 本地开发 |
| Next.js 生产服务器 | 3000 | 生产环境 |
| 后端 API | 8000 | API 服务 |

---

## 目录结构

```
web/
├── scripts/              # 部署脚本
│   ├── deploy-vercel-hkg.bat     # Windows 部署脚本
│   ├── deploy-vercel-hkg.sh      # Mac/Linux 部署脚本
│   └── verify-deployment.sh      # 部署验证脚本
├── app/                  # Next.js App Router
├── lib/                  # 工具库
├── types/                # 类型定义
├── public/               # 静态资源
└── *.md                  # 文档
```

---

## 常见问题快速解决

### Q: 端口 3000 被占用？
```bash
# Windows
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:3000 | xargs kill -9
```

### Q: npm install 失败？
```bash
# 清除缓存
npm cache clean --force

# 删除 node_modules
rm -rf node_modules package-lock.json

# 重新安装
npm install
```

### Q: 部署失败？
```bash
# 检查 Node.js 版本
node -v  # 应该 >= 18

# 检查是否已登录 Vercel
vercel whoami

# 查看部署日志
vercel logs
```

### Q: 网站无法访问？
```bash
# 检查部署状态
vercel inspect

# 验证部署
./scripts/verify-deployment.sh https://your-url.vercel.app
```

---

## 📱 访问地址

| 环境 | 地址 |
|------|------|
| 本地开发 | http://localhost:3000 |
| 生产环境 (Vercel) | https://shenliao-web.vercel.app |
| 自定义域名 | https://your-domain.com |

---

## 🎯 快速开始

```bash
# 1. 进入项目目录
cd web

# 2. 本地测试
npm install
npm run dev

# 3. 部署到线上
# Windows
.\scripts\deploy-vercel-hkg.bat
# Mac/Linux
./scripts/deploy-vercel-hkg.sh
```

**就这么简单！** 🎉
