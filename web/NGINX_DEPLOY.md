# 🚀 深聊网站 Nginx 反向代理部署指南

本指南将帮助你使用 Nginx 反向代理部署深聊网站，适合在自己的服务器上快速部署。

## ✨ 为什么使用 Nginx 反向代理？

- ✅ **简化访问**: 使用 80 端口，无需记住端口号
- ✅ **负载均衡**: 支持多个实例负载均衡
- ✅ **静态资源缓存**: 加速静态资源加载
- ✅ **SSL 支持**: 方便配置 HTTPS
- ✅ **访问控制**: 可以配置 IP 限制等
- ✅ **日志管理**: 统一的访问和错误日志

## 📋 前置要求

- 服务器（Linux，推荐 Ubuntu）
- Root 或 sudo 权限
- 已安装 Node.js 和 npm
- 深聊网站代码

## 🚀 部署步骤

### 方式 1: 使用一键部署脚本（推荐）

#### 1. 运行部署脚本

```bash
cd web
bash scripts/deploy-nginx.sh
```

脚本会自动：
- 检查并安装 Nginx
- 启动 Next.js 服务
- 配置 Nginx 反向代理
- 测试配置并重启 Nginx

#### 2. 访问网站

部署完成后，访问：
- http://localhost
- http://你的服务器IP

### 方式 2: 手动部署

#### 1. 安装 Nginx

```bash
sudo apt-get update
sudo apt-get install -y nginx
```

#### 2. 启动 Next.js 服务

```bash
cd web
nohup npm run dev > /tmp/web-start.log 2>&1 &
```

#### 3. 配置 Nginx

##### 创建配置文件

```bash
sudo nano /etc/nginx/sites-available/deepchat-web.conf
```

##### 复制以下配置

```nginx
server {
    listen 80;
    server_name localhost;

    access_log /var/log/nginx/deepchat-access.log;
    error_log /var/log/nginx/deepchat-error.log;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }

    location /_next/static/ {
        proxy_pass http://127.0.0.1:3000;
        proxy_cache_valid 200 60m;
        add_header Cache-Control "public, immutable, max-age=31536000";
    }

    location /health {
        access_log off;
        return 200 "healthy\n";
        add_header Content-Type text/plain;
    }
}
```

##### 启用配置

```bash
sudo ln -s /etc/nginx/sites-available/deepchat-web.conf /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
```

#### 4. 测试并重启 Nginx

```bash
# 测试配置
sudo nginx -t

# 重启 Nginx
sudo systemctl restart nginx

# 查看状态
sudo systemctl status nginx
```

## 🔧 高级配置

### 配置 HTTPS

#### 1. 安装 Certbot

```bash
sudo apt-get install -y certbot python3-certbot-nginx
```

#### 2. 获取 SSL 证书

```bash
sudo certbot --nginx -d yourdomain.com
```

#### 3. 自动续期

```bash
sudo certbot renew --dry-run
```

Certbot 会自动配置续期任务。

### 配置自定义域名

编辑 Nginx 配置：

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    # ... 其他配置
}
```

### 配置负载均衡

如果运行多个 Next.js 实例：

```nginx
upstream deepchat_backend {
    server 127.0.0.1:3000;
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}

server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://deepchat_backend;
        # ... 其他配置
    }
}
```

### 配置缓存

在 Nginx 配置中添加缓存：

```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=deepchat_cache:10m max_size=1g inactive=60m;

server {
    # ... 其他配置

    location / {
        proxy_cache deepchat_cache;
        proxy_cache_valid 200 302 10m;
        proxy_cache_valid 404 1m;
        proxy_cache_bypass $http_upgrade;
        # ... 其他配置
    }
}
```

### 配置 Gzip 压缩

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css text/xml text/javascript application/x-javascript application/xml+rss application/javascript application/json;
```

### 配置安全头

```nginx
add_header X-Frame-Options "DENY" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
```

### 配置访问限制

```nginx
location /admin {
    allow 192.168.1.0/24;
    allow 127.0.0.1;
    deny all;

    location / {
        # ... 其他配置
    }
}
```

## 📊 监控和管理

### 查看访问日志

```bash
sudo tail -f /var/log/nginx/deepchat-access.log
```

### 查看错误日志

```bash
sudo tail -f /var/log/nginx/deepchat-error.log
```

### 查看 Nginx 状态

```bash
sudo systemctl status nginx
```

### 重启 Nginx

```bash
sudo systemctl restart nginx
```

### 重载配置

```bash
sudo systemctl reload nginx
```

### 停止 Nginx

```bash
sudo systemctl stop nginx
```

## 🚀 使用 PM2 管理 Next.js 服务

### 1. 安装 PM2

```bash
npm install -g pm2
```

### 2. 启动服务

```bash
cd web
pm2 start npm --name "deepchat-web" -- run dev
```

### 3. 保存配置

```bash
pm2 save
pm2 startup
```

### 4. 管理服务

```bash
# 查看状态
pm2 status

# 查看日志
pm2 logs deepchat-web

# 重启服务
pm2 restart deepchat-web

# 停止服务
pm2 stop deepchat-web
```

## 🐛 常见问题

### Q1: 502 Bad Gateway

**原因**: Next.js 服务未运行

**解决**:
```bash
# 检查服务
ps aux | grep next

# 重启服务
cd web
npm run dev
```

### Q2: 静态资源 404

**原因**: 配置问题

**解决**: 确保 Nginx 配置正确，特别是 `_next/static` 路径

### Q3: 访问慢

**原因**: 未启用缓存

**解决**: 启用 Nginx 缓存和 Gzip 压缩

### Q4: 端口被占用

**原因**: 80 端口被其他服务占用

**解决**:
```bash
# 查看占用端口的进程
sudo lsof -i :80

# 停止占用进程或使用其他端口
```

## 📈 性能优化

### 1. 启用 HTTP/2

```nginx
server {
    listen 443 ssl http2;
    # ... 其他配置
}
```

### 2. 优化工作进程

```nginx
worker_processes auto;
worker_connections 1024;
```

### 3. 配置缓冲区

```nginx
proxy_buffer_size 128k;
proxy_buffers 4 256k;
proxy_busy_buffers_size 256k;
```

### 4. 启用 Keep-Alive

```nginx
keepalive_timeout 65;
keepalive_requests 100;
```

## 🔐 安全配置

### 1. 隐藏 Nginx 版本

```nginx
server_tokens off;
```

### 2. 限制请求大小

```nginx
client_max_body_size 10M;
```

### 3. 防止 DDoS

```nginx
limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s;

location / {
    limit_req zone=one burst=20 nodelay;
    # ... 其他配置
}
```

## 📚 相关链接

- Nginx 官网: https://nginx.org
- Nginx 文档: https://nginx.org/en/docs
- PM2 文档: https://pm2.keymetrics.io/docs

## 🎉 部署完成

部署完成后，你将获得：

- ✅ 稳定的线上网站
- ✅ 可配置的 HTTPS
- ✅ 优化的性能
- ✅ 详细的访问日志
- ✅ 灵活的配置选项

## 🚀 下一步

1. 访问你的网站
2. 配置 HTTPS（推荐）
3. 配置自定义域名
4. 监控访问日志
5. 优化性能配置

---

**祝你部署顺利！** 🎊

如有问题，请查阅 Nginx 文档或寻求社区帮助。
