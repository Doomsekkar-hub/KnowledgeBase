---
name: chart
description: "从 wiki 数据生成 matplotlib 可视化图表。Use when the user wants to create charts, diagrams, or visualizations from wiki data."
argument-hint: "[图表主题]"
---

# /chart — 生成图表

从 wiki 内容生成 matplotlib 可视化图表。

## 工作流

1. 确认图表主题和类型
2. 读取相关 wiki 条目，提取可视化数据
3. 生成 Python 脚本 (`output/charts/{name}.py`)
4. 执行脚本生成图片 (`output/charts/{name}.png`)
5. 图片可在 Obsidian 中直接查看

## 支持的图表类型

- **时间线图**：概念/技术发展历程
- **关系图**：概念之间的关联网络
- **对比图**：多个概念/方法的特征对比（雷达图、柱状图）
- **层级图**：概念分类的树状结构
- **统计图**：wiki 自身的统计数据（条目分布、覆盖度等）

## 参数

- 图表主题：必需
- 图表类型：可选（自动推断）
- 输出尺寸：可选，默认 12x8 inches

## 注意事项

- Python 脚本和图片同时保存，确保可复现
- 脚本中注释数据来源（wiki 条目路径）
- 图片使用中文标签，字体设置 `plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']`
