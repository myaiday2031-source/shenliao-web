# 🚀 深聊项目快速启动指南

## 前置要求

确保你的系统已安装以下软件：

- **Node.js**: 18.x 或更高版本 ([下载](https://nodejs.org/))
- **Python**: 3.9 或更高版本 ([下载](https://www.python.org/))
- **npm**: 随 Node.js 一起安装

## 快速启动（推荐）

### macOS / Linux

```bash
# 1. 进入 web 目录
cd web

# 2. 运行启动脚本
bash scripts/start-dev.sh
```

### Windows

```cmd
# 1. 进入 web 目录
cd web

# 2. 运行启动脚本
scripts\start-dev.bat
```

启动脚本会自动：
- ✅ 检查 Node.js 和 Python 环境
- ✅ 安装前端依赖（如果需要）
- ✅ 创建后端虚拟环境（如果需要）
- ✅ 安装后端依赖（如果需要）
- ✅ 启动后端服务（端口 8000）
- ✅ 启动前端服务（端口 3000）

## 手动启动

如果启动脚本无法使用，可以手动启动：

### 1. 安装前端依赖

```bash
cd web
npm install
```

### 2. 设置环境变量

在 `web` 目录下创建 `.env.local` 文件：

```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. 启动后端服务

在项目根目录（不是 web 目录）：

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate.bat  # Windows

# 安装依赖
pip install -r requirements.txt

# 启动后端
python src/main.py
```

### 4. 启动前端服务

在 `web` 目录：

```bash
npm run dev
```

## 访问应用

启动成功后，在浏览器中访问：

- **前端**: http://localhost:3000
- **后端 API**: http://localhost:8000

## 页面导航

- 🏠 **首页**: http://localhost:3000
- 📋 **项目列表**: http://localhost:3000/projects
- ➕ **创建项目**: http://localhost:3000/projects/create
- 🔧 **管理后台**: http://localhost:3000/admin
- 📊 **项目详情**: http://localhost:3000/projects/[id]

## 常见问题

### 1. 端口被占用

如果 3000 或 8000 端口被占用，可以修改端口：

```bash
# 前端（修改 web/next.config.js）
# 后端（修改 src/main.py）
```

### 2. 依赖安装失败

使用国内镜像加速：

```bash
# npm 淘宝镜像
npm config set registry https://registry.npmmirror.com

# pip 清华镜像
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 3. 后端 API 调用失败

确保：
- 后端服务已启动
- `.env.local` 中的 `NEXT_PUBLIC_API_URL` 配置正确
- 没有跨域问题

## 开发模式

### 前端开发

```bash
cd web
npm run dev       # 开发模式（热重载）
npm run build     # 构建生产版本
npm run start     # 启动生产版本
npm run lint      # 代码检查
```

### 后端开发

```bash
# 激活虚拟环境
source venv/bin/activate

# 运行工作流
python src/main.py

# 测试工作流
python -c "from src.graphs.graph import main_graph; import json; result = main_graph.invoke(json.loads('{\"industry_keyword\":\"人工智能\",\"client_email\":\"test@example.com\"}')); print(result)"
```

## 数据库

项目使用 Supabase 作为数据库，确保：
1. 在 `src/storage/database/supabase_client.py` 中配置数据库连接
2. 数据库已创建必要的表（projects, project_node_executions）

## 下一步

- ✅ 访问首页，了解平台功能
- ✅ 创建第一个项目
- ✅ 查看项目进度
- ✅ 访问管理后台

## 技术支持

如有问题，请查看：
- 前端文档: `web/README.md`
- 项目文档: 项目根目录 `README.md`

---

🎉 祝你使用愉快！
