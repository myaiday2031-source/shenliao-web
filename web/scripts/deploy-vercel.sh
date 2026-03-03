#!/bin/bash

# 深聊网站一键部署到 Vercel 脚本

set -e

echo "🚀 深聊网站 Vercel 一键部署"
echo "================================"
echo ""

# 检查是否在 web 目录
if [ ! -f "package.json" ]; then
    echo "❌ 错误: 请在 web 目录下运行此脚本"
    echo "   使用方法: bash scripts/deploy-vercel.sh"
    exit 1
fi

# 检查是否已安装 vercel CLI
if ! command -v vercel &> /dev/null; then
    echo "📦 正在安装 Vercel CLI..."
    npm install -g vercel
    echo "✅ Vercel CLI 安装完成"
fi

echo ""
echo "🔍 检查项目配置..."
echo ""

# 检查必要文件
if [ -f "vercel.json" ]; then
    echo "✅ vercel.json 已配置"
else
    echo "❌ 缺少 vercel.json 配置文件"
    exit 1
fi

if [ -f ".env.example" ]; then
    echo "✅ .env.example 已配置"
else
    echo "❌ 缺少 .env.example 文件"
    exit 1
fi

echo ""
echo "📝 部署前检查..."
echo ""

# 检查 node_modules
if [ ! -d "node_modules" ]; then
    echo "📦 正在安装依赖..."
    npm install
    echo "✅ 依赖安装完成"
fi

# 构建测试
echo "🔨 正在构建项目测试..."
npm run build

if [ $? -eq 0 ]; then
    echo "✅ 构建成功"
else
    echo "❌ 构建失败，请检查错误"
    exit 1
fi

echo ""
echo "🚀 开始部署..."
echo ""

# 部署到预览环境
echo "1️⃣  部署到预览环境..."
vercel --yes

if [ $? -eq 0 ]; then
    echo "✅ 预览环境部署成功"
else
    echo "❌ 预览环境部署失败"
    exit 1
fi

echo ""
echo "🎯 部署到生产环境..."
echo ""

# 询问是否部署到生产环境
read -p "是否部署到生产环境？(y/N): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    vercel --prod --yes

    if [ $? -eq 0 ]; then
        echo "✅ 生产环境部署成功"
    else
        echo "❌ 生产环境部署失败"
        exit 1
    fi
else
    echo "⏭️  跳过生产环境部署"
fi

echo ""
echo "================================"
echo "🎉 部署完成！"
echo ""
echo "📋 后续步骤："
echo ""
echo "1. 访问 Vercel Dashboard: https://vercel.com/dashboard"
echo "2. 配置环境变量:"
echo "   - NEXT_PUBLIC_API_URL = https://your-backend-api.com"
echo "3. 如有自定义域名，在 Vercel 中配置"
echo ""
echo "📚 详细文档请查看: web/VERCEL_DEPLOY.md"
echo ""
