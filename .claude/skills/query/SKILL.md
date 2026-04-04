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
