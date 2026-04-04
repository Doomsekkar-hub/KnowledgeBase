# Prompt: 编译论文到 Wiki

将学术论文编译为 wiki 条目。

## 输入

- 论文素材路径：`{{source_path}}`
- 当前 wiki 索引：`wiki/_index.md`

## 指令

1. 阅读论文笔记，识别：
   - 论文提出的新概念/方法
   - 论文依赖的已有概念
   - 论文的实验结论和贡献
2. **匹配已有条目**：读取 `wiki/_index.md`，对每个概念判定 CREATE 或 UPDATE
3. 为每个新概念创建 `wiki/concepts/` 条目（CREATE），或更新已有条目（UPDATE）
   - UPDATE 时：读取原条目，将新信息合并到对应小节，保留原有内容，处理矛盾
   - 更新 frontmatter 的 `updated` 和 `sources`
4. **扩散更新**：检查所有已有 wiki 条目，将论文中的相关信息补充到可能受影响的条目中
5. 如果论文涉及方法论，考虑创建或更新 `wiki/guides/` 条目
6. 仅当论文涉及的主题已有 3 个以上相关 `concepts/` 条目时，才更新 `wiki/topics/` 综述
7. 更新所有索引和注册表
8. 在 `wiki/_changelog.md` 追加编译记录，格式：
   ```
   ## [YYYY-MM-DD] compile | 论文简称
   - 新增: [[concepts/xxx]]（每个新创建的条目一行）
   - 更新: [[concepts/xxx]]（每个更新的条目一行）
   - 关系: [[a]] → [[b]]（每个新增关系一行）
   - 素材: raw/papers/xxx.md → compiled
   ```

## 论文特殊处理

- 注明论文的学术影响力和引用关系
- 在概念条目中标注"由 [论文] 首次提出"
- 将实验结论作为概念条目中的"证据/验证"部分
