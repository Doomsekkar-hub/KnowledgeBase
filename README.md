# 🧠 KnowledgeBase - Turn Raw Notes Into Clear Wiki

[![Download KnowledgeBase](https://img.shields.io/badge/Download%20KnowledgeBase-Purple?style=for-the-badge&logo=github)](https://github.com/Doomsekkar-hub/KnowledgeBase/releases)

## 📥 Download

1. Open the release page: https://github.com/Doomsekkar-hub/KnowledgeBase/releases
2. Get the latest Windows package from the release list
3. Save the file to your computer
4. If the file comes as a ZIP archive, extract it to a folder you can find again
5. Open the app from the extracted folder or from the installer file

## 🪟 Run on Windows

1. Download the latest release from the link above
2. If Windows shows a security prompt, choose to keep the file if you trust the source
3. Right-click the downloaded ZIP file and choose Extract All
4. Open the extracted folder
5. Double-click the main app file to start KnowledgeBase
6. If the app opens in a browser or local window, keep that window open while you use it

## 🗂️ What KnowledgeBase Does

KnowledgeBase helps you turn raw notes into a structured personal wiki.

Use it to:

- collect notes in one place
- turn rough material into clean wiki pages
- search your knowledge base
- ask questions about your notes
- check the health of your wiki links and pages
- export content for slides, charts, and reports

It uses a simple workflow:

raw files → LLM compile → wiki pages → output files

## 🧭 How to Use It

1. Open the KnowledgeBase folder in Obsidian as a vault
2. Put your source files in the `raw/` folder
3. Sort files into the right subfolder if you want to keep them organized
4. Run the compile step to turn raw material into wiki pages
5. Open the `wiki/` folder in Obsidian to read and edit your knowledge base
6. Use the output tools when you need slides, charts, or reports

## ✨ Main Features

- **Import notes** — bring raw material into the system
- **Translate content** — convert English source notes to Chinese
- **Compile knowledge** — turn rough files into structured wiki pages
- **Ask questions** — query your wiki in plain language
- **Check health** — find broken links and page issues
- **Create outputs** — generate slides, charts, and reports
- **Rebuild index** — refresh the search index when needed

## 📁 Folder Layout

The project uses a simple folder setup:

- `raw/` — source material you add by hand
- `wiki/` — compiled knowledge pages
- `output/` — generated slides, charts, and reports
- `tools/` — helper scripts for search, stats, validation, and graph export

## 🛠️ Tool Setup

If you want to use the extra tools, open a terminal in the `tools` folder and run:

```bash
pip install -r requirements.txt
```

After that, you can use these commands:

```bash
python search.py "关键词"
python stats.py
python validate.py
python graph_export.py
```

## 🔍 Common Actions

- Use **search.py** to find text across your knowledge base
- Use **stats.py** to view wiki size and page counts
- Use **validate.py** to check links
- Use **graph_export.py** to export a knowledge graph

## 🧩 Claude Code Skills

These commands help you work with the knowledge base:

- `/ingest` — import material and register it
- `/translate` — translate English material into Chinese
- `/compile` — compile `raw` into `wiki`
- `/query` — ask questions about the wiki
- `/lint` — run a health check
- `/slide` — create slides
- `/chart` — create charts
- `/reindex` — rebuild the index

## 📌 Suggested First Use

1. Download the latest release from the link above
2. Open the folder in Obsidian
3. Add one or two sample files to `raw/`
4. Run `/ingest` to register them
5. Run `/compile` to create wiki pages
6. Open `wiki/` and check the result
7. Run `/query` to test search and question answering

## 🖥️ System Needs

For smooth use on Windows, keep these basics in mind:

- Windows 10 or Windows 11
- A modern web browser
- Obsidian for viewing the vault
- Enough free disk space for your notes and outputs
- Internet access for download and LLM-based steps

## 📚 License

Apache 2.0