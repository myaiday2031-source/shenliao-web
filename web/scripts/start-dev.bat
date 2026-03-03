@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo 🚀 启动深聊项目...
echo.

REM 检查 Node.js
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ 错误: 未安装 Node.js
    echo 请先安装 Node.js: https://nodejs.org/
    pause
    exit /b 1
)

REM 检查 Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ 错误: 未安装 Python3
    echo 请先安装 Python3
    pause
    exit /b 1
)

REM 进入 web 目录
cd /d "%~dp0.."

REM 检查 node_modules
if not exist "node_modules" (
    echo 📦 安装前端依赖...
    call npm install
)

REM 检查后端虚拟环境
if not exist "..\venv" (
    echo 📦 创建后端虚拟环境...
    cd ..
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
    cd web
)

echo.
echo ✅ 检查完成，启动服务...
echo.

REM 启动后端（在后台）
echo 🔧 启动后端服务...
cd ..
call venv\Scripts\activate.bat
start /B python src/main.py

REM 等待后端启动
timeout /t 5 /nobreak >nul

REM 启动前端
echo 🎨 启动前端服务...
cd web
start /B npm run dev

echo.
echo ✨ 服务启动成功！
echo.
echo 📌 前端地址: http://localhost:3000
echo 📌 后端地址: http://localhost:8000
echo.
echo 按任意键停止所有服务...
pause >nul

REM 停止服务
echo.
echo 🛑 停止服务...
taskkill /F /IM node.exe 2>nul
taskkill /F /IM python.exe 2>nul
echo ✅ 服务已停止
pause
