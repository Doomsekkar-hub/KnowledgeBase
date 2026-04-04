---
name: slide
description: "从 wiki 条目生成 Marp 格式幻灯片。Use when the user wants to create a presentation from wiki content."
argument-hint: "[主题名]"
---

# /slide — 生成幻灯片

从 wiki 内容生成 Marp 格式幻灯片，保存到 `output/slides/`。

## 工作流

1. 确认幻灯片主题（用户指定或从 wiki 条目推断）
2. 读取相关 wiki 条目
3. 按 `templates/content/marp-slide.md` 格式生成幻灯片
4. 保存到 `output/slides/{topic-name}.md`

## 幻灯片结构

- 第 1 页：标题页（主题名 + 日期）
- 第 2 页：目录/概述
- 中间页：核心内容（每页 1 个要点，精简项目符号）
- 倒数第 2 页：总结/关键要点
- 最后一页：参考来源（链接到 wiki 条目）

## 参数

- 主题名：必需
- 页数：可选，默认 10-15 页
- 深度：概览 / 详细，默认概览
