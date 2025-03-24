#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
构建并上传 WavX 包到 PyPI
"""

import os
import sys
import shutil
import getpass
import re
from datetime import datetime

# PyPI API Token 文件
PYPI_TOKEN_FILE = ".pypi_token"

def update_version_in_file(file_path: str, new_version: str):
    """
    更新文件中的版本号
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 根据文件类型选择不同的替换模式
    if file_path.endswith('setup.py'):
        content = re.sub(r'version="[\d\.]+"', f'version="{new_version}"', content)
    elif file_path.endswith('__init__.py'):
        content = re.sub(r"__version__ = '[\d\.]+'", f"__version__ = '{new_version}'", content)
    elif file_path.endswith(('.md')):
        # 添加新版本记录
        today = datetime.now().strftime('%Y-%m-%d')
        new_version_line = f"- v{new_version} ({today}): Version control upgrade"
        new_version_line_zh = f"- v{new_version} ({today}): 版本控制升级"
        
        if file_path.endswith('README_zh.md'):
            content = re.sub(r'(## 发布说明\n\n)', f'\\1{new_version_line_zh}\n', content)
        else:
            content = re.sub(r'(## Release Notes\n\n)', f'\\1{new_version_line}\n', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def update_all_versions(new_version: str):
    """
    更新所有文件中的版本号
    """
    files_to_update = [
        'setup.py',
        'wavx/__init__.py',
        'README.md',
        'README_zh.md',
        'docs/index.md'
    ]
    
    for file_path in files_to_update:
        if os.path.exists(file_path):
            print(f"更新版本号在: {file_path}")
            update_version_in_file(file_path, new_version)

def get_pypi_token():
    """
    获取PyPI令牌，优先从环境变量获取，
    如果环境变量不存在，则尝试从文件读取，
    如果文件不存在，则提示用户输入
    """
    # 首先检查环境变量
    token = os.environ.get("PYPI_TOKEN")
    if token:
        return token
    
    # 其次检查令牌文件
    if os.path.exists(PYPI_TOKEN_FILE):
        with open(PYPI_TOKEN_FILE, "r") as f:
            token = f.read().strip()
            if token:
                return token
    
    # 最后提示用户输入（不显示输入内容）
    print("未找到PyPI令牌，请输入:")
    token = getpass.getpass("PyPI令牌: ")
    
    # 询问是否保存令牌到文件
    save_token = input("是否保存令牌到文件中以便下次使用？(y/n): ").lower() == 'y'
    if save_token:
        with open(PYPI_TOKEN_FILE, "w") as f:
            f.write(token)
        print(f"令牌已保存到 {PYPI_TOKEN_FILE} 文件")
    
    return token

def clean_build_folders():
    """清理构建文件夹"""
    folders_to_clean = ["build", "dist", "wavx.egg-info"]
    for folder in folders_to_clean:
        if os.path.exists(folder):
            print(f"清理文件夹：{folder}")
            shutil.rmtree(folder)

def build_package():
    """构建源码分发包和轮子"""
    print("构建源码分发包和轮子...")
    os.system(f"{sys.executable} -m pip install --upgrade pip")
    os.system(f"{sys.executable} -m pip install --upgrade setuptools wheel twine")
    os.system(f"{sys.executable} setup.py sdist bdist_wheel")

def upload_to_pypi_test():
    """上传到 TestPyPI"""
    print("上传到 TestPyPI...")
    os.environ['TWINE_USERNAME'] = "__token__"
    os.environ['TWINE_PASSWORD'] = get_pypi_token()
    os.system(f"{sys.executable} -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*")

def upload_to_pypi():
    """上传到 PyPI"""
    print("上传到 PyPI...")
    os.environ['TWINE_USERNAME'] = "__token__"
    os.environ['TWINE_PASSWORD'] = get_pypi_token()
    os.system(f"{sys.executable} -m twine upload dist/*")

def main():
    """主函数"""
    # 获取新版本号
    new_version = input("请输入新的版本号 (例如 0.1.6): ").strip()
    if not re.match(r'^\d+\.\d+\.\d+$', new_version):
        print("错误：版本号格式不正确，应为 x.y.z 格式")
        return
    
    # 更新所有文件中的版本号
    update_all_versions(new_version)
    
    # 清理旧的构建文件
    clean_build_folders()
    
    # 构建包
    build_package()
    
    # 询问是否上传到 TestPyPI
    test_upload = input("是否上传到 TestPyPI 进行测试？(y/n): ").lower() == 'y'
    if test_upload:
        upload_to_pypi_test()
    
    # 询问是否上传到 PyPI
    pypi_upload = input("是否上传到 PyPI？(y/n): ").lower() == 'y'
    if pypi_upload:
        upload_to_pypi()
    
    print("完成！")

if __name__ == "__main__":
    main() 