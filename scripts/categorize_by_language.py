"""
Author: Liu8Can

Description:
This script categorizes the simplified starred repositories data by programming language.
It creates a JSON file where repositories are grouped under their respective programming languages.
The output is saved to 'repos_by_language.json' in the 'data' directory.
"""
import json
from collections import defaultdict

def categorize_by_language(input_file, output_file):
    """
    按编程语言对星标仓库进行分类，包括开源协议和星标数，并保存到 JSON 文件中。

    Args:
        input_file (str): 包含简化仓库信息的 JSON 文件路径。
        output_file (str): 输出 JSON 文件的路径。
    """
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    repos_by_language = defaultdict(list)
    for repo in data:
        language = repo["language"] or "Unknown"  # 处理没有语言信息的仓库
        repos_by_language[language].append(repo)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(repos_by_language, f, indent=4, ensure_ascii=False)

def main():
    """
    主函数，执行分类
    """
    input_file = "data/simplified_starred_repos.json"
    output_file = "data/repos_by_language.json"
    categorize_by_language(input_file, output_file)

if __name__ == "__main__":
    main()