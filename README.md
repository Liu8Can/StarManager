# StarManager ✨

[![GitHub license](https://img.shields.io/github/license/Liu8Can/StarManager)](https://github.com/Liu8Can/StarManager/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Liu8Can/StarManager)](https://github.com/Liu8Can/StarManager/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Liu8Can/StarManager)](https://github.com/Liu8Can/StarManager/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Liu8Can/StarManager)](https://github.com/Liu8Can/StarManager/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/Liu8Can/StarManager)](https://github.com/Liu8Can/StarManager/commits/main)

> 🌟 A powerful GitHub starred repository management tool, developed by **[Liu8Can](https://github.com/Liu8Can)**.

[**简体中文说明**](README_CN.md)

## Introduction

Are you tired of searching for the tools you need among your numerous starred repositories on GitHub? **StarManager** can help you manage your starred repositories more effectively! It can:

*   🚀 Fetch all your starred repository data from the GitHub API.
*   🗂️ Preprocess and simplify repository data.
*   ⭐ Sort repositories by the number of stars.
*   🔠 Categorize repositories by programming language.
*   📝 Generate a beautiful Markdown report for easy browsing and searching of repositories.
*   🏷️ **Support adding and updating labels manually, and the label information is persistently saved, even if you regenerate the report!** (This is the core feature of our project)

## 📂 Directory Structure

```
StarManager/
├── .env                  # Stores environment variables (GitHub Personal Access Token)
├── main.py               # Main entry point of the project
├── README.md             # Project documentation (the file you are currently reading)
├── starred_repos_report.md # Generated Markdown report
├── update_labels.py      # Standalone script to extract labels from the Markdown report and update labels.json
├── data/                 # Stores project data files
│   ├── labels.json       # Stores manually added labels for each repository
│   ├── repos_by_language.json # Repositories categorized by programming language
│   ├── simplified_starred_repos.json # Simplified repository data
│   ├── sorted_starred_repos.json # Repositories sorted by the number of stars
│   └── starred_repositories.json # Raw starred repository data fetched from the GitHub API
└── scripts/              # Stores project Python scripts
    ├── categorize_by_language.py # Categorizes repositories by programming language
    ├── generate_markdown_report.py # Generates the Markdown report
    ├── get_starred_repos.py # Fetches all starred repositories from the GitHub API
    ├── process_data.py     # Preprocesses and simplifies raw data
    ├── sort_by_stars.py    # Sorts repositories by the number of stars
    └── update_labels_from_markdown.py # Internal module to extract labels from the Markdown report and update labels.json
```

## 🛠️ Getting Started

### 1. Installation

```bash
pip install requests python-dotenv
```

### 2. Configuration

*   Create a `.env` file in the project root directory.
*   Generate a new Personal Access Token (PAT) on the [GitHub settings page](https://github.com/settings/tokens/new) and add it to the `.env` file:

```
GITHUB_TOKEN=your_github_pat
```

> **Note:** You need to grant the `repo` and `read:user` scopes to the PAT. And do not commit the `.env` file to your Git repository!

### 3. Running the Program

*   **Execute the full process (fetch data, process, sort, categorize, generate report):**

    ```bash
    python main.py
    ```

*   **Update labels manually:**
    1. Open the `starred_repos_report.md` file and add labels after the `- 🏷️ **Label:**` line for each repository, for example:

        ```markdown
        ## [owner/repo-name](repo-url)
        > repo-description
        - 💻 **Language:** Python
        - ⭐ **Stars:** 123
        - 📜 **License:** MIT License
        - 🏷️ **Label:** #label1 #label2 #label3
        ```

    2. Run the following command to update the labels:

        ```bash
        python update_labels.py
        ```

    > **💡 Core Feature:** The label information you added is saved in the `data/labels.json` file. Even if you rerun `python main.py` to regenerate the report, your label information will **not be lost**!

### 4. View the Report

After running `main.py`, a `starred_repos_report.md` file will be generated in the project root directory, which contains information about all your starred repositories and manually added labels.

## ✍️ Author

This project is developed and maintained by **[Liu8Can](https://github.com/Liu8Can)**.

*   **GitHub:** [https://github.com/Liu8Can](https://github.com/Liu8Can)
*   **Email:** liucan01234@gmail.com

## 📜 License

This project is licensed under the [MIT License](https://github.com/Liu8Can/StarManager/blob/main/LICENSE).

## 🙌 Acknowledgements

*   Thanks to the [GitHub API](https://docs.github.com/en/rest) for providing powerful functionality.
*   Thanks to all the contributors to the open-source community!

---

**Hope StarManager can help you manage your GitHub starred repositories better!** 😄
