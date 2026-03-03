#!/bin/bash

# Vercel 部署向导 - 交互式部署脚本

set -e

echo "🚀 Vercel 部署向导"
echo "================================"
echo ""
echo "本脚本将引导你完成 Vercel 部署的全过程"
echo ""

# 检查是否在 web 目录
if [ ! -f "package.json" ]; then
    echo "❌ 错误: 请在 web 目录下运行此脚本"
    echo "   使用方法: bash scripts/vercel-wizard.sh"
    exit 1
fi

# 步骤 1: 检查 Vercel CLI
echo "📋 步骤 1/5: 检查 Vercel CLI"
echo "----------------------------"

if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI 未安装"
    echo "正在安装..."
    npm install -g vercel
    echo "✅ Vercel CLI 安装完成"
else
    VERCEL_VERSION=$(vercel --version)
    echo "✅ Vercel CLI 已安装 (版本: $VERCEL_VERSION)"
fi

echo ""

# 步骤 2: 检查登录状态
echo "📋 步骤 2/5: 检查登录状态"
echo "--------------------------"

# 检查是否已登录
if vercel whoami > /dev/null 2>&1; then
    VERCEL_USER=$(vercel whoami)
    echo "✅ 已登录 Vercel"
    echo "   用户: $VERCEL_USER"
else
    echo "⚠️  未登录 Vercel"
    echo ""
    echo "🔐 请登录 Vercel"
    echo "   支持的登录方式:"
    echo "   - GitHub (推荐)"
    echo "   - GitLab"
    echo "   - Bitbucket"
    echo "   - Email"
    echo ""
    read -p "按回车键开始登录..." -r

    vercel login

    if [ $? -eq 0 ]; then
        VERCEL_USER=$(vercel whoami)
        echo ""
        echo "✅ 登录成功"
        echo "   用户: $VERCEL_USER"
    else
        echo ""
        echo "❌ 登录失败，请重试"
        exit 1
    fi
fi

echo ""

# 步骤 3: 构建测试
echo "📋 步骤 3/5: 构建测试"
echo "----------------------"

if [ ! -d "node_modules" ]; then
    echo "📦 安装依赖..."
    npm install
fi

echo "🔨 开始构建..."
npm run build

if [ $? -eq 0 ]; then
    echo "✅ 构建成功"
else
    echo "❌ 构建失败"
    echo "请检查错误信息"
    exit 1
fi

echo ""

# 步骤 4: 部署到预览环境
echo "📋 步骤 4/5: 部署到预览环境"
echo "----------------------------"

read -p "是否部署到预览环境？(Y/n): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Nn]$ ]]; then
    echo "🚀 正在部署到预览环境..."
    echo ""

    # 部署到预览环境（非生产环境）
    vercel --yes --no-clipboard

    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ 预览环境部署成功"
        echo ""
        echo "📌 预览地址已在上方显示"
        echo "   你可以复制该链接在浏览器中测试"
    else
        echo ""
        echo "❌ 预览环境部署失败"
        exit 1
    fi
else
    echo "⏭️  跳过预览环境部署"
fi

echo ""

# 步骤 5: 部署到生产环境
echo "📋 步骤 5/5: 部署到生产环境"
echo "----------------------------"

read -p "是否部署到生产环境？(y/N): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🚀 正在部署到生产环境..."
    echo ""
    echo "⚠️  生产环境部署需要:"
    echo "   - 配置环境变量（如果有）"
    echo "   - 确认域名设置"
    echo ""

    # 部署到生产环境
    vercel --prod --yes

    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ 生产环境部署成功"
        echo ""
        echo "📌 生产地址已在上一步显示"
    else
        echo ""
        echo "❌ 生产环境部署失败"
        exit 1
    fi
else
    echo "⏭️  跳过生产环境部署"
    echo ""
    echo "💡 提示: 你可以稍后使用以下命令部署到生产环境:"
    echo "   vercel --prod"
fi

echo ""
echo "================================"
echo "🎉 部署流程完成！"
echo ""
echo "📋 后续步骤："
echo ""
echo "1. 访问 Vercel Dashboard"
echo "   https://vercel.com/dashboard"
echo ""
echo "2. 配置环境变量（如果需要）"
echo "   - 进入项目设置"
echo "   - 点击 Environment Variables"
echo "   - 添加: NEXT_PUBLIC_API_URL"
echo ""
echo "3. 配置自定义域名（可选）"
echo "   - 在 Vercel 中添加域名"
echo "   - 配置 DNS CNAME 记录"
echo ""
echo "4. 查看部署日志"
echo "   vercel logs"
echo ""
echo "📚 详细文档: web/VERCEL_DEPLOY.md"
echo ""
echo "🎯 访问你的网站并测试功能！"
echo ""
