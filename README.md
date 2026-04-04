# KnowledgeBase

LLM 驱动的个人知识库系统。原始素材经 LLM "编译"为结构化 wiki，通过 Obsidian 浏览，支持问答、健康检查和多种输出格式。

## 工作流

```
raw/ (人工输入) → LLM 编译 → wiki/ (知识库) → output/ (幻灯片/图表/报告)
```

## 快速开始

1. 用 Obsidian 打开本目录作为 vault
2. 将素材放入 `raw/` 对应子目录
3. 使用 Claude Code skills 操作知识库：
   - `/ingest` — 导入素材并登记
   - `/compile` — 编译 raw → wiki
   - `/query` — 对 wiki 问答
   - `/lint` — 健康检查
   - `/slide` — 生成幻灯片
   - `/chart` — 生成图表
   - `/reindex` — 重建索引

## 工具

```bash
cd tools
pip install -r requirements.txt
python search.py "关键词"       # 全文搜索
python stats.py                 # wiki 统计
python validate.py              # 链接检查
python graph_export.py          # 导出知识图谱
```

## License

Apache 2.0
