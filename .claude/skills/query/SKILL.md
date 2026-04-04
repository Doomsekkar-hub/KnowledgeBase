---
name: query
description: "基于 wiki 内容进行问答，返回结构化的回答。Use when the user asks questions about knowledge base content."
argument-hint: "[问题]"
---

# /query — Wiki 问答

基于知识库 wiki 内容回答用户问题。

## 工作流

1. 接收用户问题
2. 读取 `wiki/_index.md` 确定相关条目范围
3. 读取所有相关 wiki 条目
4. 如果 wiki 信息不够详细，进一步查阅 `raw/` 原始素材
5. 综合信息生成回答

## 输出要求

- 回答要有结构（标题、列表）
- 用 `[[wikilinks]]` 引用具体 wiki 条目
- 区分"wiki 中已有的信息"和"推测/需进一步研究的内容"
- 如果问题超出 wiki 覆盖范围，建议应该导入什么素材

## 输出选项

用户可以指定回答形式：
- 默认：直接在终端输出
- `--file`：保存为 `output/reports/` 下的 markdown 文件
- `--slide`：生成 Marp 幻灯片到 `output/slides/`
- `--wiki`：将回答保存为 wiki 条目（见下方详细流程）

## --wiki 保存流程

当用户指定 `--wiki` 时，将回答转化为正式 wiki 条目：

1. **确定条目类型和路径**：根据回答内容自动判断最合适的类别：
   - 单个概念的解释 → `wiki/concepts/concept-name.md`
   - 两个概念的对比 → `wiki/comparisons/a-vs-b.md`
   - 一个主题领域的综述 → `wiki/topics/topic-name.md`
   - 操作性的指导内容 → `wiki/guides/guide-name.md`
   - 如不确定，默认使用 `wiki/concepts/`

2. **检查已有条目**：如果对应路径已有条目，将新信息合并到已有条目中，而不是创建新文件

3. **生成 wiki 格式内容**：
   - 添加完整的 YAML frontmatter（title, aliases, created, updated, sources, tags, origin: query, query: "原始问题"）
   - sources 字段填入回答过程中引用的所有 wiki 条目和 raw/ 素材
   - 使用 `[[wikilinks]]` 链接所有相关概念
   - 内容结构遵循对应的 `templates/content/` 模板

4. **更新索引文件**：
   - `wiki/_index.md` — 添加新条目到对应分类
   - 对应分类的 `_index.md`（如 `wiki/concepts/_index.md`）
   - `wiki/_graph.md` — 添加新的概念关系
   - `wiki/_changelog.md` — 追加记录，格式: `## [YYYY-MM-DD] query-wiki | 问题摘要`
