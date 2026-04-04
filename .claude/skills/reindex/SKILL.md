---
name: reindex
description: "重建 wiki 索引文件、注册表和知识图谱。Use when indexes are out of sync or after manual edits to wiki files."
---

# /reindex — 重建索引

扫描整个知识库，重建所有索引和注册表文件。

## 工作流

1. 扫描 `raw/` 目录所有素材文件
2. 扫描 `wiki/` 目录所有条目文件
3. 重建以下文件：
   - `raw/_registry.md` — 重新生成素材注册表，根据 wiki 条目的 sources 字段推断编译状态
   - `wiki/_index.md` — 重新生成总索引
   - `wiki/concepts/_index.md` — 重建概念索引
   - `wiki/topics/_index.md` — 重建主题索引
   - `wiki/guides/_index.md` — 重建指南索引
   - `wiki/_graph.md` — 从所有条目的 `[[wikilinks]]` 重建关系图谱

## 何时使用

- 手动编辑了 wiki 文件后
- 索引文件与实际内容不同步时
- 批量导入素材后
- 作为 `/lint` 发现问题后的修复手段
