# 发布指南 / Release Guidelines

[English](#release-process) | [中文](#发布流程)

## Release Process

### 1. Prerequisites

Before releasing a new version of WavX, make sure you have:

- An account on [PyPI](https://pypi.org/)
- An account on [TestPyPI](https://test.pypi.org/) (for testing)
- Required Python packages: `setuptools`, `wheel`, `twine`

You can install these packages with:

```bash
pip install --upgrade setuptools wheel twine
```

### 2. Prepare for Release

1. Update the version number in:
   - `wavx/__init__.py`
   - `setup.py`
   - Documentation and README files if necessary

2. Update the release notes in:
   - `README.md`
   - `README_zh.md` 
   - `docs/index.md`

3. Make sure all tests pass:
   ```bash
   python -m unittest discover
   ```

4. Commit all changes:
   ```bash
   git add .
   git commit -m "Prepare for release vX.Y.Z"
   git push
   ```

### 3. Build Distribution Packages

Run the build script:

```bash
python build_and_upload.py
```

Alternatively, you can run the commands manually:

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build distributions
python setup.py sdist bdist_wheel
```

### 4. Upload to TestPyPI (Optional but Recommended)

First, upload to TestPyPI to verify everything works:

```bash
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Install from TestPyPI to test:

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps wavx
```

Verify the package works correctly.

### 5. Upload to PyPI

Once you've confirmed everything works, upload to PyPI:

```bash
python -m twine upload dist/*
```

### 6. Create a GitHub Release

1. Create a new tag for the release:
   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```

2. Go to your GitHub repository
3. Click on "Releases"
4. Click "Create new release"
5. Select the tag you just created
6. Fill in the release title and description
7. Attach the distribution files (optional)
8. Publish the release

### 7. Announce the Release

Announce the new release through appropriate channels.

---

## 发布流程

### 1. 准备工作

在发布 WavX 的新版本之前，请确保您有：

- [PyPI](https://pypi.org/) 账户
- [TestPyPI](https://test.pypi.org/) 账户（用于测试）
- 所需的 Python 包：`setuptools`、`wheel`、`twine`

您可以通过以下命令安装这些包：

```bash
pip install --upgrade setuptools wheel twine
```

### 2. 准备发布

1. 更新以下文件中的版本号：
   - `wavx/__init__.py`
   - `setup.py`
   - 如果需要，更新文档和 README 文件

2. 更新以下文件中的发布说明：
   - `README.md`
   - `README_zh.md` 
   - `docs/index.md`

3. 确保所有测试通过：
   ```bash
   python -m unittest discover
   ```

4. 提交所有更改：
   ```bash
   git add .
   git commit -m "准备发布 vX.Y.Z"
   git push
   ```

### 3. 构建分发包

运行构建脚本：

```bash
python build_and_upload.py
```

或者，您可以手动运行以下命令：

```bash
# 清理之前的构建
rm -rf build/ dist/ *.egg-info/

# 构建分发包
python setup.py sdist bdist_wheel
```

### 4. 上传到 TestPyPI（可选但推荐）

首先，上传到 TestPyPI 以验证一切正常：

```bash
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

从 TestPyPI 安装并测试：

```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps wavx
```

验证包是否正常工作。

### 5. 上传到 PyPI

确认一切正常后，上传到 PyPI：

```bash
python -m twine upload dist/*
```

### 6. 创建 GitHub 发布

1. 为发布创建新标签：
   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```

2. 转到您的 GitHub 仓库
3. 点击"Releases"
4. 点击"Create new release"
5. 选择您刚创建的标签
6. 填写发布标题和描述
7. 附加分发文件（可选）
8. 发布

### 7. 宣布发布

通过适当的渠道宣布新版本发布。 