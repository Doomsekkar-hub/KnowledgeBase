---
name: ingest
description: "导入原始素材到知识库 raw/ 目录，并登记到素材注册表。Use when the user provides articles, papers, URLs, or files to add to the knowledge base."
argument-hint: "[url-or-filepath]"
---

# /ingest — 导入素材

将用户提供的素材导入到 `raw/` 对应子目录，并更新 `raw/_registry.md` 注册表。

## 工作流

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

## 注意事项

- 如果用户提供 URL，使用 WebFetch 获取内容
- 如果用户提供文件路径，直接读取
- 图片文件复制到 `raw/images/` 对应子目录
- 文件名使用小写英文 + 连字符
