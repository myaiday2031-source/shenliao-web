#!/bin/bash

# 深聊项目启动脚本

echo "🚀 启动深聊项目..."
echo ""

# 检查 Node.js
if ! command -v node &> /dev/null; then
    echo "❌ 错误: 未安装 Node.js"
    echo "请先安装 Node.js: https://nodejs.org/"
    exit 1
fi

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未安装 Python3"
    echo "请先安装 Python3"
    exit 1
fi

# 进入 web 目录
cd "$(dirname "$0")/.."

# 检查 node_modules
if [ ! -d "node_modules" ]; then
    echo "📦 安装前端依赖..."
    npm install
fi

# 检查后端依赖
if [ ! -d "../venv" ]; then
    echo "📦 创建后端虚拟环境..."
    cd ..
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cd web
fi

echo ""
echo "✅ 检查完成，启动服务..."
echo ""

# 启动后端（在后台）
echo "🔧 启动后端服务..."
cd ..
source venv/bin/activate
python src/main.py &
BACKEND_PID=$!

# 等待后端启动
sleep 5

# 启动前端
echo "🎨 启动前端服务..."
cd web
npm run dev &
FRONTEND_PID=$!

echo ""
echo "✨ 服务启动成功！"
echo ""
echo "📌 前端地址: http://localhost:3000"
echo "📌 后端地址: http://localhost:8000"
echo ""
echo "按 Ctrl+C 停止所有服务"
echo ""

# 等待用户中断
trap "echo ''; echo '🛑 停止服务...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT TERM

wait
