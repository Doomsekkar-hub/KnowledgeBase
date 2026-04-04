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
   c. 提取核心概念列表
   d. **匹配阶段**：读取 `wiki/_index.md` 和 `wiki/_graph.md`，扫描已有 wiki 条目，为每个概念判定：
      - **CREATE** — wiki 中无对应条目 → 按模板新建
      - **UPDATE** — wiki 中已有对应条目 → 读取原条目，合并新信息
   e. 执行创建新条目 / 更新已有条目
   f. **扩散更新阶段**：扫描 wiki 中所有已有条目，检查是否有条目应该补充本次新素材的信息（即使该条目不在步骤 c 的概念列表中）。一个素材可能触及 10-15 个已有条目。对这些条目：
      - 补充相关新信息到合适的小节
      - 在 frontmatter 的 `sources` 中添加本次素材路径
      - 更新 `updated` 日期
      - 添加新的 `[[wikilinks]]` 如果出现了新的关联
   g. 用 `[[wikilinks]]` 链接所有相关条目
4. 更新全局文件：
   - `wiki/_index.md` — 添加新条目到对应分类
   - `wiki/_graph.md` — 添加新的概念关系
   - `wiki/_changelog.md` — 追加条目，格式: `## [YYYY-MM-DD] compile | 素材标题`，子条目列出新增/更新的条目和关系
   - 仅更新有变化的分类 `_index.md`（如只新增了 concepts/ 条目，不需要更新 topics/_index.md）
   - `raw/_registry.md` — 将素材状态更新为 `compiled`，填写关联条目

## Wiki 条目格式要求

- 遵循 `templates/content/wiki-concept.md` 或 `wiki-topic.md` 模板
- 必须包含完整的 YAML frontmatter
- 内容用中文，术语首次出现附英文原文
- 每个条目的"概述"不超过 3 句话

## 注意事项

- **先匹配再创建**：编译前必须读取所有已有 wiki 条目的标题和别名，通过标题匹配、别名匹配、内容关键词匹配三种方式确定已有条目
- **合并而非覆盖**：更新已有条目时，保留原有内容，将新信息插入到对应小节，必要时扩展小节
- **处理矛盾**：如果新素材与已有条目存在矛盾信息，两者都保留，用"注：[新素材] 提出不同观点..."标注
- **更新 frontmatter**：更新条目时同步更新 `updated` 日期和 `sources` 字段
- **扩散意识**：一篇关于 Transformer 的文章不仅要更新 [[concepts/transformer]]，还可能要更新 [[concepts/attention-mechanism]]、[[concepts/self-attention]]、[[topics/nlp]] 等
