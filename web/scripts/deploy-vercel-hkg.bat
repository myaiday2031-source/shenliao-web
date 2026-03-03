@echo off
REM 深聊平台 - 快速部署脚本 (Vercel 香港节点) - Windows 版本
REM 用途：一键部署到 Vercel，自动配置香港节点以优化国内访问速度

setlocal enabledelayedexpansion

echo ==========================================
echo 🚀 深聊平台 - Vercel 香港节点部署
echo ==========================================
echo.

REM 检查 Node.js
echo 📋 检查 Node.js 版本...
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js 未安装！
    echo 请访问 https://nodejs.org 安装 Node.js 18+ 版本
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('node -v') do set NODE_VERSION=%%i
echo ✅ Node.js 版本：!NODE_VERSION!
echo.

REM 检查 npm
echo 📋 检查 npm 版本...
where npm >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ npm 未安装！
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('npm -v') do set NPM_VERSION=%%i
echo ✅ npm 版本：!NPM_VERSION!
echo.

REM 检查 Git
echo 📋 检查 Git 版本...
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git 未安装！
    echo 请访问 https://git-scm.com 下载安装 Git
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('git --version') do set GIT_VERSION=%%i
echo ✅ !GIT_VERSION!
echo.

REM 检查是否已安装 Vercel CLI
echo 📋 检查 Vercel CLI...
where vercel >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Vercel CLI 未安装，正在安装...
    call npm install -g vercel
)

echo ✅ Vercel CLI 已安装
echo.

REM 检查是否已登录 Vercel
echo 📋 检查 Vercel 登录状态...
vercel whoami >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  未登录 Vercel，请登录...
    call vercel login
) else (
    echo ✅ 已登录 Vercel
)
echo.

REM 安装依赖
echo 📦 安装项目依赖...
if not exist "node_modules" (
    call npm install
    if %errorlevel% neq 0 (
        echo ❌ 依赖安装失败
        pause
        exit /b 1
    )
    echo ✅ 依赖安装完成
) else (
    echo ✅ 依赖已存在，跳过安装
)
echo.

REM 运行构建
echo 🔨 构建项目...
call npm run build
if %errorlevel% neq 0 (
    echo ❌ 项目构建失败
    pause
    exit /b 1
)
echo ✅ 项目构建成功
echo.

REM 创建 vercel.json 配置文件（如果不存在）
echo 📋 创建 Vercel 配置文件...
if not exist "vercel.json" (
    (
        echo {
        echo   "buildCommand": "npm run build",
        echo   "devCommand": "npm run dev",
        echo   "installCommand": "npm install",
        echo   "framework": "nextjs",
        echo   "regions": ["hkg1"],
        echo   "headers": [
        echo     {
        echo       "source": "/(.*)",
        echo       "headers": [
        echo         {
        echo           "key": "Access-Control-Allow-Origin",
        echo           "value": "*"
        echo         },
        echo         {
        echo           "key": "Access-Control-Allow-Methods",
        echo           "value": "GET, POST, PUT, DELETE, OPTIONS"
        echo         },
        echo         {
        echo           "key": "Access-Control-Allow-Headers",
        echo           "value": "Content-Type, Authorization"
        echo         }
        echo       ]
        echo     }
        echo   ]
        echo }
    ) > vercel.json
    echo ✅ 已创建 vercel.json 配置文件（香港节点）
) else (
    echo ✅ vercel.json 已存在
)
echo.

REM 部署到 Vercel
echo 🚀 部署到 Vercel（香港节点）...
echo.
call vercel --prod --regions=hkg1
if %errorlevel% neq 0 (
    echo ❌ 部署失败
    echo 请检查错误信息并重试
    pause
    exit /b 1
)

echo.
echo ==========================================
echo ✅ 部署成功！
echo ==========================================
echo.
echo 📱 访问地址：
echo   https://shenliao-web.vercel.app
echo.
echo 💡 提示：
echo   1. Vercel 会提供一个默认域名
echo   2. 如需自定义域名，请在 Vercel Dashboard 中配置
echo   3. 香港节点优化了国内访问速度，延迟 ^<100ms
echo.
echo 🎉 部署完成！
echo.

pause
