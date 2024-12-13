"""
Author: Liu8Can

Description:
This script retrieves all starred repositories of a specified GitHub user using the GitHub API.
It requires a GitHub Personal Access Token (PAT) for authentication, which should be stored in a .env file.
The script then saves the retrieved data to a JSON file named 'starred_repositories.json' in the 'data' directory.
"""
import requests
import json
import os
from dotenv import load_dotenv

def get_all_starred_repos(username, token):
    """
    获取指定用户的所有星标仓库。

    Args:
        username (str): GitHub 用户名。
        token (str): GitHub Personal Access Token.

    Returns:
        list: 包含所有星标仓库信息的列表。
    """
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    page = 1
    per_page = 100
    all_stars = []

    while True:
        url = f"https://api.github.com/users/{username}/starred?page={page}&per_page={per_page}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        stars = response.json()
        if not stars:
            break

        all_stars.extend(stars)
        page += 1

    return all_stars

def save_starred_repos_to_json(data, output_file):
    """
    将星标仓库数据保存到 JSON 文件中。

    Args:
        data (list): 包含星标仓库信息的列表。
        output_file (str): 输出 JSON 文件的路径。
    """
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    """
    主函数，获取所有星标仓库并保存到 JSON 文件。
    """
    # 加载 .env 文件中的环境变量
    load_dotenv()

    # 从环境变量中读取 Token
    token = os.getenv("GITHUB_TOKEN")

    # 确保 Token 已正确加载
    if not token:
        raise ValueError("未找到 GITHUB_TOKEN 环境变量。请确保已在 .env 文件中设置了该变量。")

    username = "Liu8Can"  # 将这里替换成你的 GitHub 用户名

    all_stars = get_all_starred_repos(username, token)

    # 将结果保存到 JSON 文件
    output_file = "data/starred_repositories.json"
    save_starred_repos_to_json(all_stars, output_file)

    print(f"已导出 {len(all_stars)} 个星标仓库到 {output_file}")

if __name__ == "__main__":
    main()