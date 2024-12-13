"""
Author: Liu8Can

Description:
This script serves as the main entry point for the GitHub starred repositories management tool.
It orchestrates the execution of other scripts to perform tasks such as fetching starred repositories, 
processing data, generating a Markdown report, categorizing repositories by language, and updating labels.
"""
import subprocess
import os

def run_script(script_name):
    """运行指定的 Python 脚本。"""
    print(f"Running {script_name}...")
    try:
        subprocess.run(["python", os.path.join("scripts", script_name)], check=True)
        print(f"Finished running {script_name}\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
        exit(1)  # 如果出错，退出程序

def main():
    """主程序，按顺序执行各个脚本。"""
    # 确保 data 目录存在
    if not os.path.exists("data"):
        os.makedirs("data")

    # 删除 data 目录中除了 labels.json 之外的所有文件
    for filename in os.listdir("data"):
        if filename != "labels.json":
            file_path = os.path.join("data", filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

    run_script("get_starred_repos.py")
    run_script("process_data.py")
    run_script("sort_by_stars.py")
    run_script("categorize_by_language.py")
    run_script("generate_markdown_report.py")
    run_script("update_labels_from_markdown.py") # 在生成报告后运行

    print("All tasks completed successfully!")

if __name__ == "__main__":
    main()