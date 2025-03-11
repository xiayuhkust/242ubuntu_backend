# Twitter URL ID 提取工具使用说明

## 简介

Twitter URL ID 提取工具是一个简单易用的网页应用，可以帮助您从Excel文件中提取Twitter URL并获取对应的Twitter用户ID。该工具支持批量处理多个Twitter URL，并生成包含Twitter ID的新Excel文件。

## 功能特点

- 支持Excel文件上传（.xlsx和.xls格式）
- 自动识别包含Twitter URL的列
- 提取Twitter用户名和ID
- 生成包含Twitter ID的新Excel文件
- 提供简单的Web界面进行操作
- 支持批量处理多个Twitter URL
- 支持twitter.com和x.com两种域名格式

## 使用步骤

### 1. 准备Excel文件

首先，准备一个包含Twitter URL的Excel文件。文件格式可以是.xlsx或.xls。文件中至少应包含一列Twitter URL，格式如下：

| 名称 | Twitter链接 |
|------|------------|
| 用户1 | https://twitter.com/elonmusk |
| 用户2 | https://x.com/BillGates |

系统会自动识别包含Twitter URL的列，无需特定的列名。

### 2. 访问工具网页

在浏览器中访问以下地址：

```
http://服务器IP:8000
```

您将看到如下界面：

![工具界面](../screenshots/tool_interface.png)

### 3. 上传Excel文件

点击"选择文件"按钮，选择您准备好的Excel文件，然后点击"上传并处理"按钮。

### 4. 查看处理结果

系统会自动处理您上传的Excel文件，并显示处理结果，包括：

- 总URL数：文件中识别到的Twitter URL总数
- 成功处理：成功提取ID的URL数量
- 处理失败：提取ID失败的URL数量
- 详细结果表格：显示每个URL的处理结果，包括URL、用户名、用户ID和处理状态

### 5. 下载处理后的Excel文件

处理完成后，点击"下载处理后的Excel文件"按钮，即可下载包含Twitter ID的新Excel文件。

新Excel文件将包含原始文件的所有数据，并在包含Twitter URL的列旁边添加两个新列：

- `列名_handle`：Twitter用户名
- `列名_user_id`：Twitter用户ID

例如，如果原始列名为"Twitter链接"，则新增的列名将是"Twitter链接_handle"和"Twitter链接_user_id"。

## 注意事项

1. **文件大小限制**：上传的Excel文件大小不应超过10MB。
2. **处理时间**：处理时间取决于文件大小和URL数量，通常在几秒钟内完成。
3. **文件保存时间**：上传的文件和处理后的文件会在服务器上保存1小时，之后自动删除。
4. **支持的URL格式**：系统支持以下格式的Twitter URL：
   - https://twitter.com/用户名
   - https://x.com/用户名
5. **ID提取方法**：当前版本使用简化的ID提取方法，直接使用Twitter用户名作为ID。

## 常见问题

### 上传文件后没有反应

请确保您的Excel文件格式正确，并且文件大小不超过限制。如果问题仍然存在，请尝试使用不同的浏览器或刷新页面。

### 某些URL无法提取ID

可能的原因包括：
- URL格式不正确
- Twitter用户不存在或已被删除
- 网络连接问题

### 下载的Excel文件无法打开

请确保您的计算机安装了支持.xlsx格式的Excel或其他电子表格软件。如果问题仍然存在，请尝试重新处理文件。

## 技术支持

如果您在使用过程中遇到任何问题，请联系系统管理员获取帮助。
