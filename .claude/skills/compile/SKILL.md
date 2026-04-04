---
name: compile
description: "将 raw/ 中的素材编译为 wiki 条目，更新索引和关系图谱。Use when the user wants to process pending raw materials into wiki entries."
argument-hint: "[素材文件路径]"
---

# /compile — 编译素材到 Wiki

将 `raw/` 中状态为 `pending` 的素材编译为 wiki 条目。

## 工作流

1. 读取 `raw/_registry.md`，找出所有 `pending` 状态的素材
2. 如果用户指定了具体素材，只编译该素材；否则编译所有 pending 素材
3. 对每个待编译素材：
   a. 读取素材内容
   b. 根据素材类型选择对应的 prompt 模板（`templates/prompts/compile-article.md` 或 `compile-paper.md`）
   c. 提取核心概念，创建或更新 `wiki/concepts/` 条目
   d. 如涉及较宽泛主题，创建或更新 `wiki/topics/` 条目
   e. 用 `[[wikilinks]]` 链接所有相关条目
4. 更新全局文件：
   - `wiki/_index.md` — 添加新条目到对应分类
   - `wiki/_graph.md` — 添加新的概念关系
   - `wiki/_changelog.md` — 记录本次编译变化
   - `wiki/concepts/_index.md`、`wiki/topics/_index.md` 等分类索引
   - `raw/_registry.md` — 将素材状态更新为 `compiled`，填写关联条目

## Wiki 条目格式要求

- 遵循 `templates/content/wiki-concept.md` 或 `wiki-topic.md` 模板
- 必须包含完整的 YAML frontmatter
- 内容用中文，术语首次出现附英文原文
- 每个条目的"概述"不超过 3 句话

## 注意事项

- 编译前先检查是否已有相关条目，避免创建重复内容
- 如果已有条目需要更新，保留原有内容并补充新信息
- 更新条目时同步更新 frontmatter 的 `updated` 和 `sources` 字段
