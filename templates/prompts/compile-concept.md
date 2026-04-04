# Prompt: 生成概念条目

从多个来源综合生成一个概念条目。

## 输入

- 概念名称：`{{concept_name}}`
- 相关素材列表：`{{source_files}}`
- 已有相关条目：`{{related_entries}}`

## 指令

1. 综合所有相关素材中关于该概念的信息
2. 按 `templates/content/wiki-concept.md` 模板生成条目
3. 确保：
   - 概述部分精准、简洁（3 句以内）
   - 核心内容由浅入深，逻辑清晰
   - 关联部分完整列出所有相关概念
   - sources 字段列出所有参考素材
4. 如果该概念是其他概念的上位/下位概念，在两边都添加链接
5. 更新 `wiki/concepts/_index.md`
