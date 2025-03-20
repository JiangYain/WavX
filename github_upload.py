#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
将WavX项目一键上传到GitHub
安全地使用GitHub令牌（通过环境变量或文件读取）
"""

import os
import sys
import subprocess
import getpass

# GitHub 配置
GITHUB_USERNAME = "JiangYain"
GITHUB_EMAIL = "Jiangya200123@gmail.com"
GITHUB_REPO = "https://github.com/JiangYain/WavX.git"
TOKEN_FILE = ".github_token"  # 存储令牌的文件

def get_github_token():
    """
    获取GitHub令牌，优先从环境变量获取，
    如果环境变量不存在，则尝试从文件读取，
    如果文件不存在，则提示用户输入
    """
    # 首先检查环境变量
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    
    # 其次检查令牌文件
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            token = f.read().strip()
            if token:
                return token
    
    # 最后提示用户输入（不显示输入内容）
    print("未找到GitHub令牌，请输入:")
    token = getpass.getpass("GitHub令牌: ")
    
    # 询问是否保存令牌到文件
    save_token = input("是否保存令牌到文件中以便下次使用？(y/n): ").lower() == 'y'
    if save_token:
        with open(TOKEN_FILE, "w") as f:
            f.write(token)
        print(f"令牌已保存到 {TOKEN_FILE} 文件")
    
    return token

def run_command(command, error_message=None):
    """运行命令并处理可能的错误"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            encoding="utf-8"
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        if error_message:
            print(f"错误: {error_message}")
        print(f"命令执行失败: {e.stderr}")
        return False

def configure_git(username, email):
    """配置Git用户信息"""
    print("配置Git用户信息...")
    run_command(f'git config --global user.name "{username}"', "配置用户名失败")
    run_command(f'git config --global user.email "{email}"', "配置邮箱失败")

def init_repo_if_needed():
    """如果需要，初始化Git仓库"""
    if not os.path.exists(".git"):
        print("初始化Git仓库...")
        run_command("git init", "初始化Git仓库失败")

def add_remote(repo_url, token):
    """添加远程仓库"""
    # 移除现有的origin（如果存在）
    run_command("git remote remove origin", None)
    
    # 添加带有令牌的远程仓库URL
    remote_url = repo_url.replace("https://", f"https://{token}@")
    run_command(f'git remote add origin {remote_url}', "添加远程仓库失败")

def commit_changes():
    """提交更改"""
    message = input("请输入提交信息 (默认: 'Update files'): ") or "Update files"
    
    print("添加文件到暂存区...")
    run_command("git add --all", "添加文件失败")
    
    print("提交更改...")
    run_command(f'git commit -m "{message}"', "提交更改失败")

def push_to_github():
    """推送到GitHub"""
    branch = input("请输入要推送的分支名 (默认: 'main'): ") or "main"
    
    print(f"推送到 {branch} 分支...")
    # 使用 -u 参数设置上游分支，以便将来可以直接使用 git push
    if not run_command(f"git push -u origin {branch}", "推送失败"):
        # 如果推送失败，尝试强制推送
        force_push = input("推送失败，是否尝试强制推送？(y/n): ").lower() == 'y'
        if force_push:
            run_command(f"git push -f origin {branch}", "强制推送失败")

def main():
    """主函数"""
    print("=== WavX GitHub 上传工具 ===")
    
    # 获取GitHub令牌
    token = get_github_token()
    if not token:
        print("错误: 未提供GitHub令牌，无法继续")
        sys.exit(1)
    
    # 配置Git
    configure_git(GITHUB_USERNAME, GITHUB_EMAIL)
    
    # 初始化仓库（如果需要）
    init_repo_if_needed()
    
    # 添加远程仓库
    add_remote(GITHUB_REPO, token)
    
    # 提交更改
    commit_changes()
    
    # 推送到GitHub
    push_to_github()
    
    print("完成！项目已上传到GitHub")

if __name__ == "__main__":
    main() 