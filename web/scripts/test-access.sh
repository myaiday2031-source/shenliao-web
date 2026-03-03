#!/bin/bash

# 深聊网站快速访问测试

echo "🚀 深聊网站快速访问测试"
echo "================================"
echo ""

# 测试本地访问
echo "1️⃣  测试本地访问 (localhost:3000)..."
if curl -s -o /dev/null -w "%{http_code}\n" http://localhost:3000 | grep -q "200"; then
    echo "✅ 本地访问成功！"
    echo "   访问地址: http://localhost:3000"
else
    echo "❌ 本地访问失败"
fi

echo ""

# 测试0.0.0.0访问
echo "2️⃣  测试 0.0.0.0 访问..."
if curl -s -o /dev/null -w "%{http_code}\n" http://0.0.0.0:3000 | grep -q "200"; then
    echo "✅ 0.0.0.0 访问成功！"
    echo "   访问地址: http://0.0.0.0:3000"
else
    echo "❌ 0.0.0.0 访问失败"
fi

echo ""

# 测试公网访问
echo "3️⃣  测试公网访问..."
PUBLIC_IP=$(curl -s --max-time 3 ifconfig.me 2>/dev/null || echo "")
if [ -n "$PUBLIC_IP" ]; then
    echo "   公网IP: $PUBLIC_IP"
    echo "   测试访问: http://$PUBLIC_IP:3000"
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://$PUBLIC_IP:3000 --max-time 5 2>/dev/null)
    if [ "$HTTP_CODE" = "200" ]; then
        echo "✅ 公网访问成功！"
        echo "   访问地址: http://$PUBLIC_IP:3000"
    elif [ -n "$HTTP_CODE" ]; then
        echo "⚠️  公网访问返回: HTTP $HTTP_CODE"
        echo "   可能原因：防火墙或安全组未开放 3000 端口"
        echo "   解决方案：请查看 web/ACCESS.md 文档"
    else
        echo "❌ 公网访问失败（超时或连接被拒绝）"
        echo "   可能原因：防火墙或安全组未开放 3000 端口"
        echo "   解决方案：请查看 web/ACCESS.md 文档"
    fi
else
    echo "❌ 无法获取公网IP"
    echo "   请检查网络连接"
fi

echo ""

# 获取内网IP
echo "4️⃣  获取网络信息..."
echo "   监听地址: 0.0.0.0:3000"
echo "   本地地址: 127.0.0.1:3000"
echo "   localhost: localhost:3000"

# 获取内网IP
if command -v hostname > /dev/null; then
    INTERNAL_IP=$(hostname -I | awk '{print $1}')
    if [ -n "$INTERNAL_IP" ]; then
        echo "   内网IP: $INTERNAL_IP:3000"
        echo "   内网访问地址: http://$INTERNAL_IP:3000"
    fi
fi

echo ""
echo "================================"
echo "📝 推荐访问方式："
echo ""
echo "   • 本地开发: http://localhost:3000"
echo "   • 局域网访问: http://<你的内网IP>:3000"
echo "   • 外网访问: http://<你的公网IP>:3000"
echo ""
echo "💡 提示："
echo "   • 如果外网无法访问，请检查云服务器安全组或系统防火墙"
echo "   • 详细配置指南请查看: web/ACCESS.md"
echo "   • 运行诊断脚本: bash web/scripts/check-access.sh"
echo ""
