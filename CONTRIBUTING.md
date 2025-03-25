# 贡献指南 / Contributing Guidelines

[English](#contributing-to-wavx) | [中文](#贡献到-wavx)

## Contributing to WavX

Thank you for your interest in contributing to WavX! This document provides guidelines and instructions for contributing.

### Code of Conduct

Please be respectful and considerate of others when contributing to this project.

### Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/JiangYain/WavX.git
   cd wavx
   ```
3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

### Development Workflow

1. Create a branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following the code style guidelines

3. Add tests for your changes if applicable

4. Run tests to ensure your changes don't break existing functionality:
   ```bash
   python -m unittest discover
   ```

5. Commit your changes with descriptive commit messages

6. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Create a Pull Request from your fork to the main repository

### Code Style Guidelines

- Follow PEP 8 for Python code
- Use docstrings for functions, classes, and modules
- Keep lines under 100 characters
- Use 4 spaces for indentation (no tabs)
- Import modules in the following order:
  1. Standard library imports
  2. Related third-party imports
  3. Local application/library specific imports

### Documentation

- Update documentation for any changed functionality
- Add documentation for new features
- Ensure examples accurately reflect current API behavior

### Testing

- Add tests for new features
- Ensure all tests pass before submitting a Pull Request
- Maintain or improve code coverage

### Pull Request Process

1. Ensure your code passes all tests
2. Update documentation if needed
3. The Pull Request will be reviewed by maintainers
4. Address any feedback from code reviews
5. Once approved, a maintainer will merge your Pull Request

---

## 贡献到 WavX

感谢您对 WavX 的贡献兴趣！本文档提供了贡献的指南和说明。

### 行为准则

在贡献这个项目时，请尊重并考虑他人。

### 开始

1. Fork 这个仓库
2. 克隆你的 fork：
   ```bash
   git clone https://github.com/JiangYain/WavX.git
   cd wavx
   ```
3. 安装开发依赖：
   ```bash
   pip install -e ".[dev]"
   ```

### 开发流程

1. 为你的功能或错误修复创建一个分支：
   ```bash
   git checkout -b feature/你的功能名称
   ```

2. 按照代码风格指南进行修改

3. 如果适用，为你的更改添加测试

4. 运行测试，确保你的更改不会破坏现有功能：
   ```bash
   python -m unittest discover
   ```

5. 使用描述性提交消息提交你的更改

6. 将你的分支推送到你的 fork：
   ```bash
   git push origin feature/你的功能名称
   ```

7. 从你的 fork 到主仓库创建一个拉取请求

### 代码风格指南

- 遵循 PEP 8 的 Python 代码规范
- 为函数、类和模块使用文档字符串
- 保持行长度在 100 个字符以内
- 使用 4 个空格进行缩进（不使用制表符）
- 按以下顺序导入模块：
  1. 标准库导入
  2. 相关第三方库导入
  3. 本地应用程序/库特定导入

### 文档

- 为任何更改的功能更新文档
- 为新功能添加文档
- 确保示例准确反映当前 API 行为

### 测试

- 为新功能添加测试
- 确保所有测试在提交拉取请求之前通过
- 保持或提高代码覆盖率

### 拉取请求流程

1. 确保你的代码通过所有测试
2. 如果需要，更新文档
3. 拉取请求将由维护者审查
4. 解决代码审查中的任何反馈
5. 一旦获得批准，维护者将合并你的拉取请求 