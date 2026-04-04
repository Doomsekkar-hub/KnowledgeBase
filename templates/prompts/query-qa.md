# Prompt: Wiki 问答

基于 wiki 内容回答用户的问题。

## 输入

- 用户问题：`{{question}}`

## 指令

1. 首先阅读 `wiki/_index.md` 确定相关条目
2. 阅读所有相关的 wiki 条目
3. 如果 wiki 条目不够详细，查阅 `raw/` 下的原始素材获取更多细节
4. 综合所有信息回答问题
5. 在回答中用 `[[wikilinks]]` 引用具体条目，方便用户跳转

## 输出要求

- 回答要有结构，使用标题和列表
- 区分"wiki 中已有的信息"和"需要进一步研究的部分"
- 如果问题超出 wiki 覆盖范围，明确指出并建议应该导入什么素材

## --wiki 格式要求

当用户指定 `--wiki` 保存到 wiki 时，在生成回答的基础上进行以下调整：

1. **选择条目类型**：根据问题和回答的性质判断：
   - "X 是什么" → `concepts/`
   - "X 和 Y 的区别" → `comparisons/`
   - "如何做 X" → `guides/`
   - "X 领域的现状" → `topics/`
   - 默认 → `concepts/`

2. **文件命名**：用小写英文 + 连字符，如 `attention-mechanism.md`、`rnn-vs-transformer.md`

3. **内容格式**：
   - 必须包含完整 YAML frontmatter:
     ```yaml
     ---
     title: 条目标题
     aliases: [别名]
     created: YYYY-MM-DD
     updated: YYYY-MM-DD
     sources:
       - 引用的 wiki 条目路径和 raw/ 素材路径
     tags: [相关标签]
     origin: query
     query: "原始问题"
     ---
     ```
   - `origin: query` 和 `query:` 字段标记此条目来源于问答
   - 遵循对应类别的 content 模板结构
   - 在回答中已有的 `[[wikilinks]]` 保持不变
   - "参考来源" 部分列出所有引用的 wiki 条目和 raw/ 素材

4. **合并规则**：如果目标路径已有条目：
   - 读取已有条目内容
   - 将新信息补充到对应小节
   - 更新 frontmatter 的 `updated` 日期和 `sources` 列表
   - 不删除已有内容
