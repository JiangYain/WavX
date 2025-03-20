#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
清理Git历史中的敏感信息
"""

import os
import subprocess
import sys

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

def backup_repo():
    """备份当前仓库"""
    print("备份当前仓库...")
    backup_dir = "../WavX_backup_" + os.path.basename(os.getcwd())
    if os.path.exists(backup_dir):
        print(f"备份目录 {backup_dir} 已存在，请手动备份或删除该目录后重试")
        return False
    
    # 创建仓库的完整副本
    parent_dir = os.path.dirname(os.path.abspath(backup_dir))
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    
    # 使用xcopy（Windows）或cp（Linux/Mac）命令进行复制
    if sys.platform.startswith('win'):
        run_command(f'xcopy /E /I /H "{os.getcwd()}" "{backup_dir}"', "备份仓库失败")
    else:
        run_command(f'cp -R "{os.getcwd()}" "{backup_dir}"', "备份仓库失败")
    
    print(f"仓库已备份到: {backup_dir}")
    return True

def clean_history():
    """清理Git历史中的敏感信息"""
    print("\n警告: 此操作将重写Git历史，对协作开发有重大影响!")
    print("所有合作者需要重新克隆仓库或执行复杂的重基操作。")
    confirmation = input("您确定要继续吗？(y/n): ").lower()
    if confirmation != 'y':
        print("操作已取消")
        return False
    
    print("\n开始清理Git历史...")
    
    # 创建新的孤立分支
    branch = input("请输入要创建的新分支名 (默认: 'clean-main'): ") or "clean-main"
    run_command(f"git checkout --orphan {branch}", "创建孤立分支失败")
    
    # 添加所有当前文件
    run_command("git add --all", "添加文件失败")
    
    # 提交
    commit_message = input("请输入初始提交信息 (默认: 'Initial clean commit'): ") or "Initial clean commit"
    run_command(f'git commit -m "{commit_message}"', "提交更改失败")
    
    # 删除其他所有分支
    original_branch = input("请输入当前主分支名 (默认: 'main'): ") or "main"
    run_command(f"git branch -D {original_branch}", f"删除 {original_branch} 分支失败")
    
    # 重命名当前分支为主分支
    run_command(f"git branch -m {original_branch}", "重命名分支失败")
    
    print(f"\n历史已清理。新的干净历史在 '{original_branch}' 分支上。")
    print("注意: 您需要强制推送此分支来覆盖远程仓库:")
    print(f"  git push -f origin {original_branch}")
    
    return True

def main():
    """主函数"""
    print("=== Git历史清理工具 ===")
    print("此工具将帮助您清理Git历史中的敏感信息")
    print("警告: 此操作不可逆，将永久更改您的Git历史!")
    
    # 检查是否是Git仓库
    if not os.path.exists(".git"):
        print("错误: 当前目录不是Git仓库")
        sys.exit(1)
    
    # 备份仓库
    if not backup_repo():
        print("备份失败，操作已取消")
        sys.exit(1)
    
    # 清理历史
    if not clean_history():
        print("清理历史取消")
        sys.exit(1)
    
    print("\n操作完成!")
    print("记得更新.gitignore文件，确保所有敏感文件都被排除。")
    print("强制推送到远程仓库前，请确保您了解此操作的影响。")

if __name__ == "__main__":
    main() 