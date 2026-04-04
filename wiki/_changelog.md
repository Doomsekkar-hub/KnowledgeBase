# 编译变更日志

记录每次 LLM 编译操作的变化。

<!-- 格式规范：
每次操作记录一个二级标题，格式：
## [YYYY-MM-DD] operation | Subject
operation = ingest | compile | query-wiki | lint-fix | reindex
Subject = 简短描述（素材标题或操作目标）

子条目用 bullet 记录细节：
- 新增: [[concepts/xxx]]
- 更新: [[topics/xxx]]
- 关系: [[a]] → [[b]]
- 素材: raw/articles/xxx.md → compiled
- 修复: 描述修复内容

示例：
## [2026-04-05] compile | Karpathy LLM Knowledge Bases
- 新增: [[concepts/retrieval-augmented-generation]]
- 新增: [[concepts/vector-database]]
- 更新: [[topics/llm-applications]]
- 关系: [[concepts/retrieval-augmented-generation]] → [[concepts/vector-database]]
- 素材: raw/articles/2026-04-02-karpathy-llm-knowledge-bases.md → compiled

可用 grep 快速检索：
  grep '^\## \[' wiki/_changelog.md          # 所有操作
  grep '| compile' wiki/_changelog.md        # 所有编译
  grep '2026-04' wiki/_changelog.md          # 某月操作
-->
