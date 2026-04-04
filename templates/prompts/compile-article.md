# Prompt: 编译文章到 Wiki

将原始文章编译为 wiki 条目。

## 输入

- 原始文章路径：`{{source_path}}`
- 当前 wiki 索引：`wiki/_index.md`
- 素材注册表：`raw/_registry.md`

## 指令

1. 阅读原始文章，提取所有核心概念
2. 对每个概念：
   - 检查 `wiki/concepts/` 是否已有对应条目
   - 如已有：用新信息更新条目，添加 source 引用
   - 如没有：按 `templates/content/wiki-concept.md` 模板创建新条目
3. 如果文章涉及较宽泛的主题，检查并更新 `wiki/topics/` 下的对应条目
4. 确保所有新条目之间用 `[[wikilinks]]` 互相链接
5. 更新 `wiki/_index.md`，将新条目加入对应分类
6. 更新 `wiki/_graph.md`，添加新的概念关系
7. 更新 `raw/_registry.md`，将该文章状态改为 `compiled`，填写关联条目
8. 在 `wiki/_changelog.md` 添加编译记录

## 输出质量要求

- 条目内容用中文，术语首次出现附英文原文
- 避免照搬原文，用自己的语言重新组织
- 每个条目的"概述"部分不超过 3 句话
- 关联部分要说明关系类型（依赖、对比、包含等）
