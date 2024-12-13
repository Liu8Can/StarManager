"""
Author: Liu8Can

Description:
This script generates a Markdown report from the simplified starred repositories data.
The report includes repository name, URL, description, language, stars, license, and a placeholder for manual labels.
It also merges existing manual labels from a 'labels.json' file, if available.
The generated report is saved as 'starred_repos_report.md'.
"""
import json
from datetime import datetime

def generate_markdown_report(input_file, output_file, labels_file="data/labels.json"):
    """
    根据简化的星标仓库信息生成 Markdown 报告，包含生成日期、预留标签位和通用图标，并合并已有的手动标签。

    Args:
        input_file (str): 包含简化仓库信息的 JSON 文件路径。
        output_file (str): 输出 Markdown 文件的路径。
        labels_file (str): 存储手动标签的 JSON 文件路径，默认为 "data/labels.json"。
    """
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 读取已有的标签
    try:
        with open(labels_file, "r", encoding="utf-8") as f:
            existing_labels = json.load(f)
    except FileNotFoundError:
        existing_labels = {}

    with open(output_file, "w", encoding="utf-8") as f:
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d")

        f.write(f"# My Starred Repositories (Generated on {formatted_date})\n\n")
        for repo in data:
            repo_full_name = repo["name"]  # 使用仓库完整名称作为键

            # 合并已有的标签
            labels = existing_labels.get(repo_full_name, [])
            label_str = " ".join(labels)

            f.write(f"## [{repo_full_name}]({repo['url']})\n")
            if repo['description']:
                f.write(f"> {repo['description']}\n")
            f.write(f"- 💻 **Language:** {repo['language'] or 'Unknown'}\n")
            f.write(f"- ⭐ **Stars:** {repo['stars']}\n")
            f.write(f"- 📜 **License:** {repo['license']}\n")
            f.write(f"- 🏷️ **Label:** {label_str} \n\n")

    print(f"Markdown report generated: {output_file}")
    print(f"Manual labels loaded from: {labels_file}")

def main():
    """
    主函数，生成markdown报告
    """
    input_file = "data/simplified_starred_repos.json"
    output_file = "starred_repos_report.md"
    generate_markdown_report(input_file, output_file)

if __name__ == "__main__":
    main()