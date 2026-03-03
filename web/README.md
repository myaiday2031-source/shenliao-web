# 深聊 - AI驱动的行业智库平台前端

这是"深聊"智能行业研究平台的Web前端项目，基于 Next.js 14 构建，提供简洁大气的用户界面和完善的管理功能。

## 技术栈

- **框架**: Next.js 14 (App Router)
- **UI**: TailwindCSS + 自定义组件
- **图标**: Lucide React
- **语言**: TypeScript

## 功能特性

### 用户界面
- 🏠 **简洁大气的首页**: 展示平台价值、核心功能和工作流程
- 📋 **项目列表**: 查看和管理所有研究项目，支持搜索和筛选
- ➕ **创建项目**: 简单易用的项目创建表单
- 📊 **项目详情**: 实时查看项目进度和节点执行状态

### 管理后台
- 📈 **数据概览**: 统计总项目数、进行中、已完成、已取消
- 🗂️ **项目管理**: 查看所有项目，支持高级筛选
- 🔄 **实时监控**: 刷新数据获取最新状态

## 项目结构

```
web/
├── app/                      # Next.js App Router
│   ├── layout.tsx           # 根布局
│   ├── page.tsx             # 首页
│   ├── not-found.tsx        # 404页面
│   ├── projects/            # 项目相关页面
│   │   ├── page.tsx         # 项目列表
│   │   ├── create/          # 创建项目
│   │   │   └── page.tsx
│   │   └── [id]/            # 项目详情
│   │       └── page.tsx
│   └── admin/               # 管理后台
│       └── page.tsx
├── lib/                     # 工具库
│   ├── api.ts              # API调用层
│   └── utils.ts            # 工具函数
├── types/                   # TypeScript类型定义
│   └── index.ts
├── public/                  # 静态资源
├── package.json
├── tsconfig.json
├── tailwind.config.ts
├── postcss.config.js
└── next.config.js
```

## 快速开始

### 🚀 线上部署（推荐）

想要快速将网站部署到线上？我们提供两种方案：

#### 方案 1: Vercel 部署（推荐，最快，5分钟）

```bash
cd web
npm install -g vercel
vercel login
bash scripts/deploy-vercel.sh
```

**优势**:
- ✅ 5分钟快速上线
- ✅ 免费，无需服务器
- ✅ 全球 CDN 加速
- ✅ 自动 HTTPS
- ✅ GitHub 自动部署

详细文档: [Vercel 部署指南](VERCEL_DEPLOY.md)

#### 方案 2: Nginx 反向代理（自有服务器）

```bash
cd web
bash scripts/deploy-nginx.sh
```

**优势**:
- ✅ 完全控制服务器
- ✅ 灵活配置
- ✅ 适合长期运营

详细文档: [Nginx 部署指南](NGINX_DEPLOY.md)

📖 **完整部署指南**: [DEPLOYMENT.md](DEPLOYMENT.md)

### 🖥️ 本地开发

#### 1. 安装依赖

```bash
cd web
npm install
```

#### 2. 配置环境变量

创建 `.env.local` 文件：

```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

#### 3. 启动开发服务器

```bash
npm run dev
```

访问 http://localhost:3000

### 4. 构建生产版本

```bash
npm run build
npm start
```

## API 接口

前端通过 `lib/api.ts` 调用后端 API，主要接口：

### 项目相关
- `POST /api/projects/create` - 创建项目
- `GET /api/projects/list` - 获取项目列表
- `GET /api/projects/:id` - 获取项目详情
- `PUT /api/projects/:id/status` - 更新项目状态
- `PUT /api/projects/:id/cancel` - 取消项目
- `GET /api/projects/:id/progress` - 获取项目进度

### 节点执行相关
- `POST /api/projects/:projectId/nodes` - 记录节点执行
- `GET /api/projects/:projectId/nodes` - 获取节点执行记录

## 页面说明

### 首页 (`/`)
- 平台介绍和核心功能展示
- 两阶段工作流说明
- 数据统计展示

### 项目列表 (`/projects`)
- 查看所有项目
- 搜索和筛选功能
- 快速创建项目入口

### 创建项目 (`/projects/create`)
- 填写项目基本信息
- 项目名称（必填）
- 行业关键词（必填）
- 客户邮箱（可选）

### 项目详情 (`/projects/[id]`)
- 项目基本信息展示
- 实时进度百分比
- 阶段1节点执行状态
- 阶段2节点执行状态
- 刷新数据功能

### 管理后台 (`/admin`)
- 数据概览统计
- 项目列表管理
- 高级筛选功能

## 设计特点

### 视觉设计
- 渐变色主题（紫色到蓝色）
- 简洁大气的卡片布局
- 流畅的动画效果
- 响应式设计，支持移动端

### 用户体验
- 直观的导航结构
- 清晰的状态标识
- 实时数据刷新
- 友好的错误提示

## 开发注意事项

1. **API 代理**: 开发环境下，Next.js 会将 `/api/*` 请求代理到后端服务
2. **类型安全**: 所有 API 响应都有对应的 TypeScript 类型定义
3. **状态管理**: 使用 React hooks 进行本地状态管理
4. **样式约定**: 使用 TailwindCSS 的 utility-first 方式

## 浏览器支持

- Chrome (最新版)
- Firefox (最新版)
- Safari (最新版)
- Edge (最新版)

## 后续优化

- [ ] 添加用户认证
- [ ] 实现项目编辑功能
- [ ] 添加数据导出功能
- [ ] 增加更多图表可视化
- [ ] 优化移动端体验
- [ ] 添加实时通知

## 联系支持

如有问题或建议，请联系开发团队。

## 📚 相关文档

### 部署相关
- 🚀 **[线上部署指南](DEPLOYMENT.md)** - Vercel 和 Nginx 两种部署方案
- ☁️ **[Vercel 部署](VERCEL_DEPLOY.md)** - 详细的 Vercel 部署步骤
- 🔧 **[Nginx 部署](NGINX_DEPLOY.md)** - Nginx 反向代理配置
- 🏠 **[快速启动](QUICKSTART.md)** - 快速启动指南

### 访问相关
- 🌐 **[访问指南](ACCESS.md)** - 网站访问问题和解决方案
- 🔍 **[解决方案](SOLUTION.md)** - 访问问题解决方案

### 其他
- ⚙️ **[项目文档](README.md)** - 本文档
- 🔧 **[开发指南](#开发注意事项)** - 开发规范和注意事项

## 🎯 快速链接

### 想要快速上线？
```bash
cd web
bash scripts/deploy-vercel.sh  # Vercel 部署（推荐）
# 或
bash scripts/deploy-nginx.sh   # Nginx 部署
```

### 想要本地开发？
```bash
cd web
npm install
npm run dev
```

### 想要测试访问？
```bash
cd web
bash scripts/test-access.sh
```
