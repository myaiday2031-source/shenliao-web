#!/bin/bash

# 深聊网站访问诊断脚本

echo "🔍 深聊网站访问诊断"
echo "======================"
echo ""

# 检查服务是否运行
echo "1️⃣  检查服务状态..."
if pgrep -f "next-server" > /dev/null; then
    echo "✅ Next.js 服务正在运行"
    PID=$(pgrep -f "next-server")
    echo "   进程 ID: $PID"
else
    echo "❌ Next.js 服务未运行"
    echo "   尝试启动服务..."
    cd "$(dirname "$0")"
    npm run dev > /tmp/web-start.log 2>&1 &
    echo "   服务正在启动，请等待 5 秒..."
    sleep 5
fi

echo ""

# 检查端口监听
echo "2️⃣  检查端口监听..."
if netstat -tlnp 2>/dev/null | grep -q ":3000"; then
    echo "✅ 端口 3000 正在监听"
    netstat -tlnp 2>/dev/null | grep ":3000"
else
    echo "❌ 端口 3000 未监听"
fi

echo ""

# 检查本地访问
echo "3️⃣  测试本地访问..."
if curl -s -o /dev/null -w "%{http_code}" http://localhost:3000 | grep -q "200"; then
    echo "✅ 本地访问成功 (HTTP 200)"
else
    echo "❌ 本地访问失败"
fi

echo ""

# 获取服务器IP
echo "4️⃣  获取服务器信息..."
echo "   本地地址: http://localhost:3000"
echo "   0.0.0.0地址: http://0.0.0.0:3000"

# 尝试获取公网IP
echo "   正在获取公网IP..."
PUBLIC_IP=$(curl -s --max-time 3 ifconfig.me 2>/dev/null || echo "无法获取")
if [ "$PUBLIC_IP" != "无法获取" ]; then
    echo "   公网IP: $PUBLIC_IP"
    echo "   外部访问地址: http://$PUBLIC_IP:3000"
else
    echo "   ⚠️  无法获取公网IP，请检查网络连接"
fi

echo ""

echo "5️⃣  检查防火墙..."
if command -v ufw > /dev/null; then
    echo "   UFW 状态:"
    ufw status | grep 3000 || echo "   端口 3000 未在 UFW 中配置"
elif command -v firewall-cmd > /dev/null; then
    echo "   FirewallD 状态:"
    firewall-cmd --list-ports 2>/dev/null | grep 3000 || echo "   端口 3000 未在 FirewallD 中配置"
else
    echo "   ⚠️  无法检测防火墙状态"
fi

echo ""
echo "======================"
echo "📋 访问方式："
echo ""
echo "   方式 1（本地）: http://localhost:3000"
echo "   方式 2（IP）:   http://0.0.0.0:3000"
echo "   方式 3（外网）: http://<你的服务器IP>:3000"
echo ""
echo "💡 提示："
echo "   - 如果使用云服务器，请确保安全组已开放 3000 端口"
echo "   - 如果使用本地开发，直接使用 localhost 访问"
echo "   - 如果无法访问，请检查防火墙设置"
echo ""
