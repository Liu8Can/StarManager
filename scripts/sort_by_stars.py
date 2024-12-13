"""
Author: Liu8Can

Description:
This script sorts the simplified starred repositories data by the number of stars in descending order.
The sorted data is then saved to a new JSON file named 'sorted_starred_repos.json' in the 'data' directory.
"""
import json

def sort_starred_repos_by_stars(input_file, output_file):
    """
    从简化的 GitHub 星标仓库 JSON 文件中提取关键信息，并根据 star 数量进行排序。

    Args:
        input_file (str): 输入 JSON 文件的路径。
        output_file (str): 输出 JSON 文件的路径。
    """
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 已经是简化后的数据，不需要再次提取，可以直接排序
    data.sort(key=lambda x: x["stars"], reverse=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    """
    主函数，执行排序
    """
    input_file = "data/simplified_starred_repos.json"
    output_file = "data/sorted_starred_repos.json"
    sort_starred_repos_by_stars(input_file, output_file)

if __name__ == "__main__":
    main()