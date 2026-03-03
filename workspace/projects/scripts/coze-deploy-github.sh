#!/bin/bash

# 深聊平台 - Coze 云端环境部署脚本
# 方案：通过 GitHub + Vercel 自动部署

set -e

echo "=========================================="
echo "🚀 深聊平台 - Coze 云端环境部署"
echo "=========================================="
echo ""

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 检查 Git
echo -e "${YELLOW}📋 检查 Git 配置...${NC}"

if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git 未安装！${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Git 版本：$(git --version | cut -d' ' -f3)${NC}"
echo ""

# 提交当前更改
echo -e "${YELLOW}📋 提交当前更改...${NC}"

cd /workspace/projects

# 提交所有更改
git add .
git commit -m "feat: 准备部署深聊平台前端" || echo -e "${YELLOW}⚠️  没有需要提交的更改${NC}"

echo -e "${GREEN}✅ 代码已提交${NC}"
echo ""

# 显示下一步操作
echo -e "${BLUE}==========================================${NC}"
echo -e "${BLUE}📋 下一步操作指南${NC}"
echo -e "${BLUE}==========================================${NC}"
echo ""
echo -e "${YELLOW}步骤 1：创建 GitHub 仓库${NC}"
echo "  1. 访问 https://github.com/new"
echo "  2. 创建新仓库，命名为 'shenliao-web'"
echo "  3. 勾选 'Initialize this repository with a README'"
echo "  4. 点击 'Create repository'"
echo ""

echo -e "${YELLOW}步骤 2：连接 Git remote${NC}"
echo "  在 Coze 环境中执行："
echo -e "${GREEN}  git remote add origin https://github.com/YOUR_USERNAME/shenliao-web.git${NC}"
echo "  （请将 YOUR_USERNAME 替换为你的 GitHub 用户名）"
echo ""

echo -e "${YELLOW}步骤 3：推送到 GitHub${NC}"
echo "  在 Coze 环境中执行："
echo -e "${GREEN}  git branch -M main${NC}"
echo -e "${GREEN}  git push -u origin main${NC}"
echo ""

echo -e "${YELLOW}步骤 4：部署到 Vercel${NC}"
echo "  1. 访问 https://vercel.com/new"
echo "  2. 使用 GitHub 账号登录"
echo "  3. 点击 'Import' 导入 'shenliao-web' 仓库"
echo "  4. 配置项目："
echo "     - Framework Preset: Next.js"
echo "     - Build Command: npm run build"
echo "     - Output Directory: .next"
echo "     - Install Command: npm install"
echo "  5. 点击 'Deploy'"
echo ""

echo -e "${YELLOW}步骤 5：配置香港节点（优化国内访问）${NC}"
echo "  1. 部署完成后，进入项目设置"
echo "  2. 找到 'Regions' 或 '区域' 设置"
echo "  3. 选择 'Hong Kong (hkg1)'"
echo "  4. 保存并重新部署"
echo ""

echo -e "${GREEN}=========================================="
echo -e "✅ 准备工作完成！"
echo -e "==========================================${NC}"
echo ""
echo -e "${YELLOW}💡 提示：${NC}"
echo "  1. 需要先在 GitHub 创建仓库"
echo "  2. 需要提供 GitHub 凭证来推送代码"
echo "  3. Vercel 会自动部署，2-3 分钟后即可访问"
echo ""
