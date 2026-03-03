#!/bin/bash

# 深聊平台 - 部署验证脚本
# 用途：验证部署是否成功，检查网站访问情况

set -e

echo "=========================================="
echo "🔍 深聊平台 - 部署验证"
echo "=========================================="
echo ""

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 默认 URL（可通过参数覆盖）
DEPLOY_URL=${1:-"https://shenliao-web.vercel.app"}

echo -e "${YELLOW}📋 部署 URL：${NC}"
echo "  $DEPLOY_URL"
echo ""

# 检查 curl 命令
check_curl() {
    echo -e "${YELLOW}📋 检查 curl 命令...${NC}"

    if ! command -v curl &> /dev/null; then
        echo -e "${RED}❌ curl 未安装！${NC}"
        echo "请安装 curl 后再试"
        exit 1
    fi

    echo -e "${GREEN}✅ curl 已安装${NC}"
    echo ""
}

# 检查网站是否可访问
check_website_access() {
    echo -e "${YELLOW}📋 检查网站访问...${NC}"

    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$DEPLOY_URL")

    if [ "$HTTP_CODE" -eq 200 ]; then
        echo -e "${GREEN}✅ 网站可访问 (HTTP $HTTP_CODE)${NC}"
    else
        echo -e "${RED}❌ 网站无法访问 (HTTP $HTTP_CODE)${NC}"
        echo "请检查："
        echo "  1. 部署 URL 是否正确"
        echo "  2. 网络连接是否正常"
        echo "  3. 网站是否已部署成功"
        exit 1
    fi
    echo ""
}

# 检查响应时间
check_response_time() {
    echo -e "${YELLOW}📋 检查响应时间...${NC}"

    RESPONSE_TIME=$(curl -o /dev/null -s -w "%{time_total}\n" "$DEPLOY_URL")
    RESPONSE_TIME_MS=$(echo "$RESPONSE_TIME * 1000" | bc | cut -d'.' -f1)

    echo -e "${GREEN}✅ 响应时间：${RESPONSE_TIME_MS}ms${NC}"

    if [ "$RESPONSE_TIME_MS" -lt 100 ]; then
        echo -e "${GREEN}   ⚡ 极快！${NC}"
    elif [ "$RESPONSE_TIME_MS" -lt 300 ]; then
        echo -e "${GREEN}   👍 速度不错！${NC}"
    elif [ "$RESPONSE_TIME_MS" -lt 1000 ]; then
        echo -e "${YELLOW}   ⚠️  速度稍慢${NC}"
    else
        echo -e "${RED}   ❌ 速度太慢！${NC}"
    fi
    echo ""
}

# 检查 HTTPS
check_https() {
    echo -e "${YELLOW}📋 检查 HTTPS 配置...${NC}"

    if [[ "$DEPLOY_URL" == https://* ]]; then
        echo -e "${GREEN}✅ 已启用 HTTPS${NC}"
    else
        echo -e "${YELLOW}⚠️  未使用 HTTPS${NC}"
        echo "建议配置 HTTPS 以提高安全性"
    fi
    echo ""
}

# 检查关键页面
check_pages() {
    echo -e "${YELLOW}📋 检查关键页面...${NC}"

    PAGES=(
        "$DEPLOY_URL"
        "$DEPLOY_URL/projects"
        "$DEPLOY_URL/admin"
    )

    for page in "${PAGES[@]}"; do
        HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$page")
        PAGE_NAME=$(echo "$page" | sed "s|$DEPLOY_URL||")

        if [ "$HTTP_CODE" -eq 200 ]; then
            echo -e "${GREEN}✅ $PAGE_NAME - 正常${NC}"
        else
            echo -e "${RED}❌ $PAGE_NAME - 失败 (HTTP $HTTP_CODE)${NC}"
        fi
    done
    echo ""
}

# 生成验证报告
generate_report() {
    echo -e "${YELLOW}📋 生成验证报告...${NC}"

    REPORT_FILE="deployment-report-$(date +%Y%m%d-%H%M%S).txt"

    cat > "$REPORT_FILE" << EOF
深聊平台部署验证报告
=====================

验证时间: $(date)
部署 URL: $DEPLOY_URL

验证结果:
- 网站访问: $(curl -s -o /dev/null -w "%{http_code}" "$DEPLOY_URL") - $([ $(curl -s -o /dev/null -w "%{http_code}" "$DEPLOY_URL") -eq 200 ] && echo "✅ 正常" || echo "❌ 失败")
- 响应时间: $(curl -o /dev/null -s -w "%{time_total}s" "$DEPLOY_URL")
- HTTPS: $([[ "$DEPLOY_URL" == https://* ]] && echo "✅ 已启用" || echo "❌ 未启用")

关键页面检查:
EOF

    for page in "${PAGES[@]}"; do
        HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$page")
        PAGE_NAME=$(echo "$page" | sed "s|$DEPLOY_URL||")
        echo "- $PAGE_NAME: HTTP $HTTP_CODE - $([ $HTTP_CODE -eq 200 ] && echo "✅ 正常" || echo "❌ 失败")" >> "$REPORT_FILE"
    done

    echo -e "${GREEN}✅ 报告已保存到：$REPORT_FILE${NC}"
    echo ""
}

# 主函数
main() {
    check_curl
    check_website_access
    check_response_time
    check_https
    check_pages
    generate_report

    echo -e "${GREEN}=========================================="
    echo -e "✅ 验证完成！"
    echo -e "==========================================${NC}"
    echo ""
    echo -e "${YELLOW}📱 访问地址：${NC}"
    echo -e "${GREEN}  $DEPLOY_URL${NC}"
    echo ""
    echo -e "${YELLOW}💡 建议：${NC}"
    echo "  1. 在浏览器中打开 URL 检查页面显示"
    echo "  2. 测试所有功能是否正常"
    echo "  3. 如有异常，查看部署日志"
    echo ""
}

# 执行主函数
main
