# Prompt: 生成幻灯片

从 wiki 内容生成 Marp 格式幻灯片。

## 输入

- 主题：`{{topic}}`
- 相关 wiki 条目：`{{entries}}`
- 目标页数：`{{slide_count}}`（默认 10-15 页）

## 指令

1. 阅读相关 wiki 条目，提取核心内容
2. 按 `templates/content/marp-slide.md` 格式生成幻灯片
3. 结构建议：
   - 第 1 页：标题页
   - 第 2 页：目录/概述
   - 中间页：核心内容（每页一个要点）
   - 倒数第 2 页：总结
   - 最后一页：参考来源
4. 每页内容精简，使用项目符号
5. 适当使用 Marp 的布局指令（`<!-- _class: lead -->`等）

## 输出

保存到 `output/slides/` 目录，文件名为 `{{topic}}.md`。
