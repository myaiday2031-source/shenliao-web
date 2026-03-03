#!/bin/bash

# 深聊平台 - 快速部署脚本 (Vercel 香港节点)
# 用途：一键部署到 Vercel，自动配置香港节点以优化国内访问速度

set -e  # 遇到错误立即退出

echo "=========================================="
echo "🚀 深聊平台 - Vercel 香港节点部署"
echo "=========================================="
echo ""

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 检查 Node.js
check_nodejs() {
    echo -e "${YELLOW}📋 检查 Node.js 版本...${NC}"

    if ! command -v node &> /dev/null; then
        echo -e "${RED}❌ Node.js 未安装！${NC}"
        echo "请访问 https://nodejs.org 安装 Node.js 18+ 版本"
        exit 1
    fi

    NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
    if [ "$NODE_VERSION" -lt 18 ]; then
        echo -e "${RED}❌ Node.js 版本过低！当前版本：$(node -v)，要求：18+${NC}"
        exit 1
    fi

    echo -e "${GREEN}✅ Node.js 版本：$(node -v)${NC}"
    echo ""
}

# 检查 npm
check_npm() {
    echo -e "${YELLOW}📋 检查 npm 版本...${NC}"

    if ! command -v npm &> /dev/null; then
        echo -e "${RED}❌ npm 未安装！${NC}"
        exit 1
    fi

    echo -e "${GREEN}✅ npm 版本：$(npm -v)${NC}"
    echo ""
}

# 检查 Git
check_git() {
    echo -e "${YELLOW}📋 检查 Git 版本...${NC}"

    if ! command -v git &> /dev/null; then
        echo -e "${RED}❌ Git 未安装！${NC}"
        echo "请访问 https://git-scm.com 下载安装 Git"
        exit 1
    fi

    echo -e "${GREEN}✅ Git 版本：$(git --version | cut -d' ' -f3)${NC}"
    echo ""
}

# 检查是否已登录 Vercel
check_vercel_auth() {
    echo -e "${YELLOW}📋 检查 Vercel 登录状态...${NC}"

    if ! command -v vercel &> /dev/null; then
        echo -e "${YELLOW}⚠️  Vercel CLI 未安装，正在安装...${NC}"
        npm install -g vercel
    fi

    if vercel whoami &> /dev/null; then
        echo -e "${GREEN}✅ 已登录 Vercel${NC}"
    else
        echo -e "${YELLOW}⚠️  未登录 Vercel，请登录...${NC}"
        vercel login
    fi
    echo ""
}

# 安装依赖
install_dependencies() {
    echo -e "${YELLOW}📦 安装项目依赖...${NC}"

    if [ ! -d "node_modules" ]; then
        npm install
        echo -e "${GREEN}✅ 依赖安装完成${NC}"
    else
        echo -e "${GREEN}✅ 依赖已存在，跳过安装${NC}"
    fi
    echo ""
}

# 运行构建
build_project() {
    echo -e "${YELLOW}🔨 构建项目...${NC}"

    npm run build

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ 项目构建成功${NC}"
    else
        echo -e "${RED}❌ 项目构建失败${NC}"
        exit 1
    fi
    echo ""
}

# 部署到 Vercel
deploy_to_vercel() {
    echo -e "${YELLOW}🚀 部署到 Vercel（香港节点）...${NC}"
    echo ""

    # 创建 vercel.json 配置文件（如果不存在）
    if [ ! -f "vercel.json" ]; then
        cat > vercel.json << 'EOF'
{
  "buildCommand": "npm run build",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "framework": "nextjs",
  "regions": ["hkg1"],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        },
        {
          "key": "Access-Control-Allow-Methods",
          "value": "GET, POST, PUT, DELETE, OPTIONS"
        },
        {
          "key": "Access-Control-Allow-Headers",
          "value": "Content-Type, Authorization"
        }
      ]
    }
  ]
}
EOF
        echo -e "${GREEN}✅ 已创建 vercel.json 配置文件（香港节点）${NC}"
    fi

    # 执行部署
    echo -e "${YELLOW}⏳ 正在部署到 Vercel...${NC}"
    vercel --prod --regions=hkg1

    if [ $? -eq 0 ]; then
        echo ""
        echo -e "${GREEN}=========================================="
        echo -e "✅ 部署成功！"
        echo -e "==========================================${NC}"
        echo ""
        echo -e "${YELLOW}📱 访问地址：${NC}"
        echo -e "${GREEN}  https://shenliao-web.vercel.app${NC}"
        echo ""
        echo -e "${YELLOW}💡 提示：${NC}"
        echo "  1. Vercel 会提供一个默认域名"
        echo "  2. 如需自定义域名，请在 Vercel Dashboard 中配置"
        echo "  3. 香港节点优化了国内访问速度，延迟 <100ms"
        echo ""
    else
        echo -e "${RED}❌ 部署失败${NC}"
        echo "请检查错误信息并重试"
        exit 1
    fi
}

# 主函数
main() {
    echo "开始部署流程..."
    echo ""

    check_nodejs
    check_npm
    check_git
    check_vercel_auth
    install_dependencies
    build_project
    deploy_to_vercel

    echo -e "${GREEN}🎉 部署完成！${NC}"
}

# 执行主函数
main
