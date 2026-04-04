---
name: ingest
description: "导入素材到 raw/ 或扫描注册未登记文件。Use when the user provides articles, papers, URLs, files, or wants to scan raw/ for unregistered materials."
argument-hint: "[url, filepath, or --scan]"
---

# /ingest — 导入素材

两种模式：**导入模式**（提供 URL/文件/文本）和**扫描模式**（`--scan` 或无参数）。

---

## 模式一：导入（提供了 URL / 文件路径 / 文本内容）

1. 确认素材类型（article / paper / book / repo / dataset / image / video / misc）
2. 根据类型确定目标目录和文件命名：
   - articles: `raw/articles/YYYY-MM-DD-slug.md`
   - papers: `raw/papers/author-YYYY-short-title.md`
   - books: `raw/books/book-title/_meta.md`
   - repos: `raw/repos/repo-name.md`
   - datasets: `raw/datasets/dataset-name.md`
   - images: `raw/images/{diagrams|screenshots|photos}/filename`
   - videos: `raw/videos/YYYY-MM-DD-title.md`
   - misc: `raw/misc/filename.md`
3. 如果素材是文本内容，按 `templates/content/raw-article.md` 或 `templates/content/raw-paper.md` 模板格式化
4. 将素材写入目标路径
5. 在 `raw/_registry.md` 添加一行，状态设为 `pending`
6. 告知用户素材已导入，可以运行 `/compile` 编译到 wiki

### 注意事项

- 如果用户提供 URL，使用 WebFetch 获取内容
- 如果用户提供文件路径，直接读取
- 图片文件复制到 `raw/images/` 对应子目录
- 文件名使用小写英文 + 连字符

---

## 模式二：扫描注册（`--scan`、无参数、或用户要求扫描）

用于将 Obsidian Web Clipper 等外部工具已放入 `raw/` 的文件补录到注册表。

1. 读取 `raw/_registry.md`，提取已注册文件路径集合
2. 递归扫描 `raw/` 所有子目录，找出所有 `.md` 文件（排除 `_registry.md`、`_index.md`、`.gitkeep`）
3. 对比两个集合，找出未注册的文件
4. 如果没有未注册文件，告知用户"全部已登记"
5. 如果有未注册文件：
   a. 列出所有未注册文件，附带推断的类型（根据所在子目录判断）
   b. 读取每个文件的 frontmatter 提取 title、date 等信息
   c. 将每个文件追加到 `raw/_registry.md`，状态设为 `pending`
   d. 报告：新注册 N 个文件，可运行 `/compile` 编译到 wiki

### 类型推断规则

根据文件所在目录自动判断类型：
- `raw/articles/` → article
- `raw/papers/` → paper
- `raw/books/` → book
- `raw/repos/` → repo
- `raw/datasets/` → dataset
- `raw/images/` → image
- `raw/videos/` → video
- `raw/misc/` → misc
