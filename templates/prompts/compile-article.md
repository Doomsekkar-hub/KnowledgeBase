# Prompt: 编译文章到 Wiki

将原始文章编译为 wiki 条目。

## 输入

- 原始文章路径：`{{source_path}}`
- 当前 wiki 索引：`wiki/_index.md`
- 素材注册表：`raw/_registry.md`

## 指令

1. 阅读原始文章，提取所有核心概念（列出概念名称清单）
2. **匹配已有条目**：
   a. 读取 `wiki/_index.md` 获取所有已有条目列表
   b. 对每个概念，通过标题、别名、内容关键词搜索确定是否已有对应条目
   c. 标记每个概念为 CREATE（新建）或 UPDATE（更新）
3. 对每个 CREATE 概念：
   - 按 `templates/content/wiki-concept.md` 模板创建新条目
   - 填写完整 frontmatter，sources 包含当前素材路径
4. 对每个 UPDATE 概念：
   - 读取已有条目完整内容
   - 将新信息补充到对应小节（概述、核心内容、应用等），不删除已有内容
   - 如有矛盾信息，保留两者并用"注：[新素材标题] 指出..."标注
   - 在 frontmatter 的 `sources` 列表追加当前素材路径
   - 更新 `updated` 日期
5. **扩散更新**：逐一检查所有已有 wiki 条目（不仅是步骤 1 提取的概念），如果文章中的信息与某个已有条目相关：
   - 补充相关信息
   - 添加 source 引用
   - 更新日期
6. 仅当文章涉及较宽泛的主题且该主题已有 3 个以上 `concepts/` 条目时，才创建或更新 `wiki/topics/` 条目。不要为每篇文章都创建单独的 topic 条目
7. 确保所有新条目和更新条目之间用 `[[wikilinks]]` 互相链接
8. 更新 `wiki/_index.md`，将新条目加入对应分类
9. 更新 `wiki/_graph.md`，添加新的概念关系
10. 更新 `raw/_registry.md`，将该文章状态改为 `compiled`，填写关联条目
11. 在 `wiki/_changelog.md` 追加编译记录，格式：
   ```
   ## [YYYY-MM-DD] compile | 文章标题
   - 新增: [[concepts/xxx]]（每个新创建的条目一行）
   - 更新: [[concepts/xxx]]（每个更新的条目一行）
   - 关系: [[a]] → [[b]]（每个新增关系一行）
   - 素材: raw/articles/xxx.md → compiled
   ```

## 输出质量要求

- 条目内容用中文，术语首次出现附英文原文
- 避免照搬原文，用自己的语言重新组织
- 每个条目的"概述"部分不超过 3 句话
- 关联部分要说明关系类型（依赖、对比、包含等）
