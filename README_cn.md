[English](./README.md) | 简体中文

# 简介

这是一个通过命令行管理文件备注的工具，有以下功能。

- [x] 给文件（夹）添加备注。  
- [x] 查询添加备注的文件。
- [x] 查询指定目录下添加备注的文件。
- [x] 根据关键词搜索添加备注的文件。
- [x] 添加文件关系。
- [x] 查看与某个文件相关的文件。
- [ ] 导出所有文件备注数据。

这个工具有一个缺点就是，一个文件被移动或重命名后，跟它的备注信息就关联不上了。

# 安装

1. 安装python

   安装版本>=3.6的python

2. 下载并安装本软件

   2.1 下载工程
   
   ```
   git clone https://github.com/wapping/FileNote.git
   cd FileNote
   ```
   
   2.2 以下方式二选一
   
   - 安装包安装

   
   ```
   pip install dist/FileNote-0.0.1-py3-none-any.whl
   ```
   
   - 源码编译安装
   
   ```
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    python3 -m build
    pip install dist/FileNote-0.0.1-py3-none-any.whl
   ```
   
3. 测试


在命令行终端执行 `fnote`，确认是否成功安装 。

# 快速开始

1. 给一个文件添加备注

`fnote -a /path/to/your/file note`

`/path/to/your/file`：你要备注的文件的路径，可以是相对路径。

`note`：你的备注。

2. 查看一个文件的备注

`fnote -pf -k keyword`

`keyword`：关键词，可以是文件路径关键词，也可以是备注的关键词。

