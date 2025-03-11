# Twitter URL ID 提取服务部署说明

## 系统要求

- Ubuntu 服务器（推荐 Ubuntu 20.04 LTS 或更高版本）
- Python 3.8 或更高版本
- 至少 1GB 可用内存
- 至少 1GB 可用磁盘空间

## 安装步骤

### 1. 安装依赖项

首先，确保系统已安装 Python 和必要的开发工具：

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git
```

### 2. 克隆代码库

```bash
git clone https://github.com/yourusername/twitter_id_service.git
cd twitter_id_service
```

### 3. 创建虚拟环境并安装依赖

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. 配置服务

服务默认配置已经适合大多数使用场景，如需自定义配置，可以修改 `app/main.py` 文件中的相关参数。

### 5. 部署方式

#### 方式一：使用 systemd 服务（推荐用于生产环境）

```bash
# 安装 systemd 服务
sudo cp deployment/twitter_id_service.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable twitter_id_service
sudo systemctl start twitter_id_service

# 检查服务状态
sudo systemctl status twitter_id_service
```

#### 方式二：使用脚本手动启动（适用于测试环境）

```bash
# 启动服务
./start_service.sh

# 停止服务
./stop_service.sh
```

### 6. 验证部署

服务启动后，可以通过以下方式验证部署是否成功：

```bash
# 检查服务是否正在运行
ps aux | grep uvicorn

# 测试健康检查接口
curl http://localhost:8000/health
```

如果返回 `{"status":"healthy"}`，则表示服务已成功部署。

## 服务配置

### 端口配置

默认情况下，服务运行在 8000 端口。如需更改端口，请修改以下文件：

1. `start_service.sh` 中的端口号
2. `deployment/twitter_id_service.service` 中的端口号

### 文件上传配置

上传文件存储在 `uploads` 目录中，处理后的文件存储在 `temp` 目录中。这些文件会在 1 小时后自动删除。

如需更改文件保存时间，请修改 `app/main.py` 中的 `cleanup_temp_files` 函数。

## 日志管理

### 查看日志

使用 systemd 服务部署时，可以通过以下命令查看日志：

```bash
sudo journalctl -u twitter_id_service -f
```

使用脚本手动启动时，日志保存在 `service.log` 文件中：

```bash
tail -f service.log
```

### 日志级别

日志级别默认设置为 INFO。如需更改日志级别，请修改 `app/main.py` 中的 `logging.basicConfig` 配置。

## 故障排除

### 服务无法启动

1. 检查 Python 版本是否满足要求
2. 检查依赖项是否正确安装
3. 检查端口是否被占用
4. 检查日志中的错误信息

### 文件上传失败

1. 检查上传目录是否存在并具有正确的权限
2. 检查文件大小是否超过限制
3. 检查磁盘空间是否充足

### API 请求失败

1. 检查服务是否正在运行
2. 检查请求参数是否正确
3. 检查日志中的错误信息

## 更新服务

要更新服务，请按照以下步骤操作：

```bash
# 停止服务
sudo systemctl stop twitter_id_service

# 更新代码
git pull

# 更新依赖
source venv/bin/activate
pip install -r requirements.txt

# 启动服务
sudo systemctl start twitter_id_service
```

## 备份与恢复

服务本身不存储任何永久数据，因此不需要特殊的备份策略。如果需要备份配置，可以备份以下文件：

- `app/main.py`
- `deployment/twitter_id_service.service`
- `requirements.txt`

## 安全建议

1. 在生产环境中，建议配置 HTTPS
2. 限制上传文件的大小和类型
3. 定期更新依赖项以修复安全漏洞
4. 使用防火墙限制对服务的访问
