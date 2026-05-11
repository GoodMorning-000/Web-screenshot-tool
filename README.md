# Web网页截图工具

基于 Playwright 构建的现代化网页截图工具，具有高稳定性、高并发、反检测能力和自动重试机制。

## 功能特性

- ✅ **高稳定性**: 基于 Playwright 实现可靠的浏览器自动化
- ✅ **高并发**: 基于 AsyncIO 的并发截图处理
- ✅ **反检测**: 浏览器指纹伪装以绕过机器人检测
- ✅ **自动重试**: 使用 tenacity 实现失败自动重试
- ✅ **自动日志**: 使用 loguru 进行全面日志记录
- ✅ **自动懒加载**: 自动滚动触发懒加载内容
- ✅ **全页面截图**: 原生支持捕获整个网页
- ✅ **跨浏览器支持**: 支持 Chrome、Edge 和 Chromium

## 环境要求

- Python 3.11+
- Playwright
- Playwright-stealth
- loguru
- tenacity
- pydantic

## 安装步骤

```bash
# 安装依赖
pip install -r requirements.txt

# 安装浏览器（如果不使用系统 Chrome/Edge）
playwright install chromium
```

## 使用方法

1. 在 `data/urls.txt` 中添加要截图的 URL（每行一个）
2. 运行截图工具：

```bash
python main.py
```

1. 截图将保存在 `screenshots/` 目录中

## 配置说明

编辑 `config/settings.py` 来自定义配置：

- `HEADLESS`: 无头模式运行浏览器（默认: True）
- `WINDOW_WIDTH`: 浏览器窗口宽度（默认: 1920）
- `WINDOW_HEIGHT`: 浏览器窗口高度（默认: 1080）
- `PAGE_TIMEOUT`: 页面加载超时时间（毫秒）（默认: 60000）
- `MAX_CONCURRENT`: 最大并发截图数（默认: 5）
- `MAX_RETRY`: 最大重试次数（默认: 3）
- `MAX_SCROLL_STEP`: 懒加载滚动最大步数（默认: 10）

## 项目结构

```
modern_screenshot_project/
├── config/              # 配置文件目录
│   ├── settings.py      # 应用程序设置
│   └── browser.js       # 浏览器指纹伪装脚本
├── core/                # 核心模块
│   ├── browser.py       # 浏览器管理器
│   ├── screenshot.py    # 截图逻辑
│   ├── worker.py        # 并发任务处理器
│   └── retry.py         # 重试装饰器
├── utils/               # 工具函数
│   ├── file_utils.py    # 文件操作工具
│   ├── scroll.py        # 自动滚动（用于懒加载）
│   └── url_utils.py     # URL 验证和规范化
├── data/                # 数据文件目录
│   └── urls.txt         # 待截图的 URL 列表
├── screenshots/         # 截图输出目录
├── logs/                # 日志文件目录
├── main.py              # 主程序入口
└── requirements.txt     # Python 依赖列表
```

## 运行截图

<img width="2193" height="1411" alt="运行截图" src="https://github.com/user-attachments/assets/6ffeb3a5-c460-499d-82bd-dcf9fb835355" />

## 贡献

欢迎贡献代码！请随时提交 issue 和 pull request。
