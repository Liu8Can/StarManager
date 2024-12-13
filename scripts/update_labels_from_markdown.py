"""
Author: Liu8Can

Description:
This script updates the 'labels.json' file with manual labels extracted from the Markdown report file.
It parses the Markdown file, identifies labels added by the user, and updates the corresponding entries in 'labels.json'.
"""
import json
import re

def update_labels_from_markdown(markdown_file, labels_file="data/labels.json"):
    """
    从 Markdown 文件中提取标签信息，并更新到 labels.json 文件中。

    Args:
        markdown_file (str): Markdown 文件的路径。
        labels_file (str): 存储手动标签的 JSON 文件路径，默认为 "data/labels.json"。
    """
    try:
        with open(labels_file, "r", encoding="utf-8") as f:
            labels_data = json.load(f)
    except FileNotFoundError:
        labels_data = {}

    with open(markdown_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_repo = None
    for line in lines:
        repo_match = re.match(r"## \[(.+)\]\(.+\)", line)
        if repo_match:
            current_repo = repo_match.group(1)
            if current_repo not in labels_data:
                labels_data[current_repo] = []  # 如果没有这个仓库，则创建，防止后续赋值报错
        else:
            label_match = re.findall(r"#\S+", line) # 匹配所有#开头的标签
            if label_match and current_repo:
                for label in label_match:
                    if label not in labels_data[current_repo]: # 防止重复标签
                        labels_data[current_repo].append(label)

    with open(labels_file, "w", encoding="utf-8") as f:
        json.dump(labels_data, f, indent=4, ensure_ascii=False)

def main():
    """
    主函数，执行标签更新
    """
    markdown_file = "starred_repos_report.md"
    labels_file = "data/labels.json"
    update_labels_from_markdown(markdown_file, labels_file)

if __name__ == "__main__":
    main()