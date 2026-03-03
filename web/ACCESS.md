# 深聊网站访问指南

## ✅ 服务状态

当前服务已成功启动并运行：

- **服务状态**: ✅ 正在运行
- **监听端口**: ✅ 3000 (0.0.0.0)
- **本地访问**: ✅ 成功 (HTTP 200)
- **进程ID**: 1096

## 🌐 访问地址

### 方式 1: 本地访问（推荐用于开发）

```
http://localhost:3000
```

### 方式 2: 通过IP访问

```
http://0.0.0.0:3000
```

### 方式 3: 外网访问

```
http://115.190.51.49:3000
```

⚠️ **注意**: 外网访问目前无法访问，需要配置防火墙或安全组

## 🔧 解决外网无法访问的问题

### 情况 1: 使用云服务器（阿里云、腾讯云、AWS等）

如果你使用的是云服务器，需要在云服务商的控制台中配置**安全组**：

#### 阿里云
1. 登录 [阿里云控制台](https://ecs.console.aliyun.com/)
2. 找到你的实例
3. 点击"安全组" -> "配置规则"
4. 添加入方向规则：
   - 端口范围: 3000/3000
   - 授权对象: 0.0.0.0/0
   - 协议类型: TCP

#### 腾讯云
1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/cvm)
2. 找到你的实例
3. 点击"安全组" -> "修改规则"
4. 添加入站规则：
   - 端口: 3000
   - 来源: 0.0.0.0/0
   - 协议: TCP

#### AWS
1. 登录 [AWS Console](https://console.aws.amazon.com/)
2. 找到你的 EC2 实例
3. 编辑安全组
4. 添加入站规则：
   - 类型: 自定义 TCP
   - 端口范围: 3000
   - 源: 0.0.0.0/0

### 情况 2: 使用本地服务器

如果你在本地或内网服务器上运行，可能需要配置系统防火墙：

#### Ubuntu/Debian (使用 ufw)

```bash
# 开放 3000 端口
sudo ufw allow 3000

# 查看 ufw 状态
sudo ufw status

# 如果 ufw 未启用，启用它
sudo ufw enable
```

#### CentOS/RHEL (使用 firewalld)

```bash
# 开放 3000 端口
sudo firewall-cmd --zone=public --add-port=3000/tcp --permanent

# 重载防火墙规则
sudo firewall-cmd --reload

# 查看开放的端口
sudo firewall-cmd --list-ports
```

#### 使用 iptables

```bash
# 添加规则允许 3000 端口
sudo iptables -A INPUT -p tcp --dport 3000 -j ACCEPT

# 保存规则
sudo iptables-save > /etc/iptables/rules.v4
```

### 情况 3: 使用 Docker

如果你在 Docker 中运行，需要映射端口：

```bash
docker run -d -p 3000:3000 --name deepchat-web your-image
```

### 情况 4: 使用 nginx 反向代理

如果你使用 nginx 反向代理，配置示例：

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

## 🧪 测试访问

### 方法 1: 使用浏览器

直接在浏览器中输入访问地址。

### 方法 2: 使用 curl

```bash
# 测试本地访问
curl http://localhost:3000

# 测试外网访问
curl http://115.190.51.49:3000
```

### 方法 3: 使用诊断脚本

```bash
cd web
bash scripts/check-access.sh
```

## 📊 查看服务日志

```bash
# 查看启动日志
cat /tmp/web-start-new.log

# 实时查看日志
tail -f /tmp/web-start-new.log
```

## 🔄 重启服务

```bash
# 停止服务
pkill -f "next-server"

# 启动服务
cd web
npm run dev

# 或者使用后台启动
cd web
npm run dev > /tmp/web-start.log 2>&1 &
```

## 🎯 常见问题

### Q1: 端口被占用怎么办？

```bash
# 查找占用 3000 端口的进程
lsof -i :3000
# 或
netstat -tlnp | grep 3000

# 结束进程
kill -9 <PID>
```

### Q2: 修改默认端口？

编辑 `web/next.config.js`:

```javascript
module.exports = {
  reactStrictMode: true,
  devIndicators: {
    buildActivity: false,
  },
  // 添加端口配置
  devServer: {
    port: 3001, // 改成你想要的端口
  }
}
```

然后在 `web/package.json` 中也修改：

```json
"scripts": {
  "dev": "next dev -p 3001 -H 0.0.0.0"
}
```

### Q3: 本地可以访问，外网无法访问？

这是最常见的问题，检查以下几项：

1. ✅ 检查云服务器安全组是否开放 3000 端口
2. ✅ 检查系统防火墙是否开放 3000 端口
3. ✅ 检查网络策略是否限制访问
4. ✅ 确认服务监听在 0.0.0.0 而不是 127.0.0.1

### Q4: 访问速度慢？

可能的原因：
- 网络延迟
- 服务器性能不足
- CDN 加速未配置

解决方案：
- 使用 CDN
- 升级服务器配置
- 优化代码和资源

## 📞 获取帮助

如果以上方法都无法解决，请提供以下信息：

1. 操作系统类型和版本
2. 云服务商名称（如果使用云服务器）
3. 错误信息或截图
4. 诊断脚本输出结果

## 🎉 成功访问

成功访问后，你将看到：

- 🏠 **简洁大气的首页**: 展示平台价值
- 📋 **项目列表**: 管理你的研究项目
- ➕ **创建项目**: 开始新的研究
- 🔧 **管理后台**: 监控所有项目

---

**祝您使用愉快！** 🚀
