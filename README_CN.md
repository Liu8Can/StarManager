# StarManager ✨

[![GitHub license](https://img.shields.io/github/license/Liu8Can/StarManager)](https://github.com/Liu8Can/StarManager/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Liu8Can/StarManager)](https://github.com/Liu8Can/StarManager/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Liu8Can/StarManager)](https://github.com/Liu8Can/StarManager/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Liu8Can/StarManager)](https://github.com/Liu8Can/StarManager/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/Liu8Can/StarManager)](https://github.com/Liu8Can/StarManager/commits/main)

> 🌟 一款强大的 GitHub 星标仓库管理工具，由 **[Liu8Can](https://github.com/Liu8Can)** 开发。

## 简介

你是否厌倦了在 GitHub 上繁杂的星标仓库中寻找你需要的工具？**StarManager** 可以帮助你更好地管理你的星标仓库！它可以：

*   🚀 从 GitHub API 获取你所有的星标仓库数据。
*   🗂️ 对仓库数据进行预处理和简化。
*   ⭐ 根据星标数量对仓库进行排序。
*   🔠 根据编程语言对仓库进行分类。
*   📝 生成精美的 Markdown 报告，方便你浏览和查找仓库。
*   🏷️ **支持手动添加和更新标签，并且标签信息会被持久化保存，即使重新生成报告也不会丢失！** (这是我们项目的核心特色)

## 📂目录结构

```
StarManager/
├── .env                  # 存储环境变量 (GitHub Personal Access Token)
├── main.py               # 项目的主入口
├── README.md             # 项目的说明文档 (就是你正在阅读的这个文件)
├── starred_repos_report.md # 生成的 Markdown 报告
├── update_labels.py      # 独立脚本，用于从 Markdown 报告中提取标签并更新 labels.json
├── data/                 # 存储项目的数据文件
│   ├── labels.json       # 存储用户为仓库添加的手动标签
│   ├── repos_by_language.json # 按编程语言分类的仓库数据
│   ├── simplified_starred_repos.json # 经过简化处理的仓库数据
│   ├── sorted_starred_repos.json # 按星标数排序后的仓库数据
│   └── starred_repositories.json # 从 GitHub API 获取的原始星标仓库数据
└── scripts/              # 存储项目的 Python 脚本
    ├── categorize_by_language.py # 按编程语言对仓库进行分类
    ├── generate_markdown_report.py # 生成 Markdown 报告
    ├── get_starred_repos.py # 从 GitHub API 获取所有星标仓库
    ├── process_data.py     # 对原始数据进行预处理和简化
    ├── sort_by_stars.py    # 按星标数对仓库进行排序
    └── update_labels_from_markdown.py # 从 Markdown 报告中提取标签并更新 labels.json 的内部模块
```

## 🛠️使用教程

### 1. 安装依赖

```bash
pip install requests python-dotenv
```

### 2. 配置

*   在项目根目录下创建 `.env` 文件。
*   在 [GitHub 设置页面](https://github.com/settings/tokens/new) 生成一个新的 Personal Access Token (PAT)，并将其添加到 `.env` 文件中：

```
GITHUB_TOKEN=your_github_pat
```

> **注意:**  需要授予 `repo` 和 `read:user` 权限,并且不要将 `.env` 文件提交到 Git 仓库中！

### 3. 运行程序

*   **执行完整流程 (获取数据、处理、排序、分类、生成报告):**

    ```bash
    python main.py
    ```

*   **手动更新标签:**
    1. 打开 `starred_repos_report.md` 文件，在每个仓库的 `- 🏷️ **Label:**` 后面添加标签，例如：

        ```markdown
        ## [owner/repo-name](repo-url)
        > repo-description
        - 💻 **Language:** Python
        - ⭐ **Stars:** 123
        - 📜 **License:** MIT License
        - 🏷️ **Label:** #标签1 #标签2 #标签3
        ```

    2. 执行以下命令更新标签：

        ```bash
        python update_labels.py
        ```

    > **💡 核心特色：** 你添加的标签信息会被保存在 `data/labels.json` 文件中。即使你再次运行 `python main.py` 重新生成报告，你的标签信息也 **不会丢失**！

### 4. 查看报告

运行 `main.py` 后，会在项目根目录下生成 `starred_repos_report.md` 文件，其中包含了你所有星标仓库的信息和手动添加的标签。

## ✍️作者

本项目由 **[Liu8Can](https://github.com/Liu8Can)** 开发和维护。

*   **GitHub:** [https://github.com/Liu8Can](https://github.com/Liu8Can)
*   **邮箱:** liucan01234@gmail.com

## 📜许可证

本项目使用 [MIT 许可证](https://github.com/Liu8Can/StarManager/blob/main/LICENSE)。

## 🙌致谢

*   感谢 [GitHub API](https://docs.github.com/en/rest) 提供的强大功能。
*   感谢所有为开源社区做出贡献的人们！

---

**希望 StarManager 能帮助你更好地管理你的 GitHub 星标仓库!** 😄
