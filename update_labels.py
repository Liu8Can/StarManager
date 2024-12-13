"""
Author: Liu8Can

Description:
This script provides a quick way to update labels from the Markdown report. 
It calls the `update_labels_from_markdown` function from the `scripts.update_labels_from_markdown` module.
"""

import sys
import os

# 将 scripts 目录添加到 Python 路径中，以便可以导入其中的模块
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))

from update_labels_from_markdown import update_labels_from_markdown

def main():
    """
    主函数，执行标签更新。
    """
    markdown_file = "starred_repos_report.md"  # Markdown 报告文件路径
    labels_file = "data/labels.json"  # 标签文件路径
    update_labels_from_markdown(markdown_file, labels_file)
    print(f"Labels updated from '{markdown_file}' to '{labels_file}'")

if __name__ == "__main__":
    main()