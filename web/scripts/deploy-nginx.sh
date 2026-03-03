#!/bin/bash

# 深聊网站 Nginx 反向代理部署脚本

set -e

echo "🚀 深聊网站 Nginx 反向代理部署"
echo "================================"
echo ""

# 检查是否在 web 目录
if [ ! -f "package.json" ]; then
    echo "❌ 错误: 请在 web 目录下运行此脚本"
    echo "   使用方法: bash scripts/deploy-nginx.sh"
    exit 1
fi

# 检查是否安装了 nginx
if ! command -v nginx &> /dev/null; then
    echo "📦 正在安装 Nginx..."
    sudo apt-get update
    sudo apt-get install -y nginx
    echo "✅ Nginx 安装完成"
fi

echo ""
echo "🔍 检查 Next.js 服务..."
echo ""

# 检查 Next.js 服务是否运行
if pgrep -f "next-server" > /dev/null; then
    echo "✅ Next.js 服务正在运行"
else
    echo "⚠️  Next.js 服务未运行，正在启动..."
    cd "$(dirname "$0")/.."
    nohup npm run dev > /tmp/web-start.log 2>&1 &
    echo "⏳ 等待服务启动..."
    sleep 10
fi

echo ""
echo "📝 配置 Nginx..."
echo ""

# 复制配置文件
NGINX_CONF_DIR="/etc/nginx/sites-available"
NGINX_CONF_LINK_DIR="/etc/nginx/sites-enabled"
NGINX_CONF_FILE="deepchat-web.conf"

# 创建配置目录
sudo mkdir -p $NGINX_CONF_DIR
sudo mkdir -p $NGINX_CONF_LINK_DIR

# 复制配置文件
echo "📋 复制 Nginx 配置文件..."
sudo cp nginx/nginx.conf $NGINX_CONF_DIR/$NGINX_CONF_FILE

# 创建软链接
echo "🔗 创建配置软链接..."
sudo ln -sf $NGINX_CONF_DIR/$NGINX_CONF_FILE $NGINX_CONF_LINK_DIR/$NGINX_CONF_FILE

# 删除默认配置（可选）
sudo rm -f $NGINX_CONF_LINK_DIR/default

echo ""
echo "🧪 测试 Nginx 配置..."
echo ""

# 测试配置
sudo nginx -t

if [ $? -eq 0 ]; then
    echo "✅ Nginx 配置测试通过"
else
    echo "❌ Nginx 配置测试失败"
    exit 1
fi

echo ""
echo "🔄 重启 Nginx..."
echo ""

# 重启 Nginx
sudo systemctl restart nginx

if [ $? -eq 0 ]; then
    echo "✅ Nginx 重启成功"
else
    echo "❌ Nginx 重启失败"
    exit 1
fi

echo ""
echo "🔍 检查服务状态..."
echo ""

# 检查服务状态
echo "Nginx 状态:"
sudo systemctl status nginx | head -n 10

echo ""
echo "Next.js 状态:"
if pgrep -f "next-server" > /dev/null; then
    PID=$(pgrep -f "next-server")
    echo "✅ Next.js 正在运行 (PID: $PID)"
else
    echo "❌ Next.js 未运行"
fi

echo ""
echo "🌐 获取访问地址..."
echo ""

# 获取服务器IP
LOCAL_IP=$(hostname -I | awk '{print $1}')
PUBLIC_IP=$(curl -s --max-time 3 ifconfig.me 2>/dev/null || echo "无法获取")

echo "================================"
echo "🎉 部署完成！"
echo ""
echo "📌 访问地址："
echo ""
echo "   本地访问: http://localhost"
echo "   内网访问: http://$LOCAL_IP"
if [ "$PUBLIC_IP" != "无法获取" ]; then
    echo "   外网访问: http://$PUBLIC_IP"
fi
echo ""
echo "📋 访问日志："
echo "   sudo tail -f /var/log/nginx/deepchat-access.log"
echo "   sudo tail -f /var/log/nginx/deepchat-error.log"
echo ""
echo "🔧 管理 Nginx："
echo "   重启: sudo systemctl restart nginx"
echo "   停止: sudo systemctl stop nginx"
echo "   状态: sudo systemctl status nginx"
echo ""
echo "📚 详细文档请查看: web/NGINX_DEPLOY.md"
echo ""
