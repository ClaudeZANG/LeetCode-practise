import subprocess
import os

def git_command(command):
    """执行 Git 命令，并输出结果"""
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")

def update_leetcode_folder():
    """自动提交并上传 `D:\LeetCode-practise` 文件夹到 GitHub"""
    
    # 进入 Git 项目目录（确保 Git 仓库已初始化）
    os.chdir(r"D:\LeetCode-practise")

    # 添加所有修改
    git_command(["git", "add", "."])

    # 提交更改
    commit_message = "Auto-update LeetCode practise folder"
    git_command(["git", "commit", "-m", commit_message])

    # 推送到 GitHub（确保使用正确的分支）
    git_command(["git", "push", "origin", "main"])  # 适用于 `main` 分支
    # 如果你的仓库仍然使用 `master`，请改成 `git push origin master`

if __name__ == "__main__":
    update_leetcode_folder()
