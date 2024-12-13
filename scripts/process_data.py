"""
Author: Liu8Can

Description:
This script processes the raw starred repositories data obtained from the GitHub API.
It simplifies the data structure by extracting key information such as repository name, URL, description, 
language, stars, license, etc. The simplified data is then saved to a new JSON file named 
'simplified_starred_repos.json' in the 'data' directory.
"""

import json

def simplify_starred_repos(input_file, output_file):
    """
    从原始的 GitHub 星标仓库 JSON 文件中提取关键信息，包括开源协议和星标数，并保存到一个新的 JSON 文件中。

    Args:
        input_file (str): 原始 JSON 文件的路径。
        output_file (str): 输出 JSON 文件的路径。
    """
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    simplified_data = []
    for repo in data:
        simplified_repo = {
            "name": repo["full_name"],
            "url": repo["html_url"],
            "description": repo["description"],
            "language": repo["language"],
            "stars": repo["stargazers_count"],
            "license": repo["license"]["name"] if repo["license"] else "No License"  # 获取许可证名称
        }
        simplified_data.append(simplified_repo)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(simplified_data, f, indent=4, ensure_ascii=False)

def main():
    """
    主函数，处理数据
    """
    input_file = "data/starred_repositories.json"  # 输入文件路径
    output_file = "data/simplified_starred_repos.json"  # 输出文件路径
    simplify_starred_repos(input_file, output_file)

if __name__ == "__main__":
    main()