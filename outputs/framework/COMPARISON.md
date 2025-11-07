# Comparison Report

| file | topic | days | kept | scanned | unique hosts | top hosts | avg len | med len |
|---|---:|---:|---:|---:|---:|---|---:|---:|
| antibiotics.json | antibiotics | 21 | 8 | 8 | 1 | news.google.com×8 | 89.2 | 80.5 |
| vaccines.json | vaccines | 21 | 8 | 8 | 1 | news.google.com×8 | 101.1 | 100.0 |
| antibiotics_zh.json | 抗生素 | 21 | 8 | 8 | 1 | news.google.com×8 | 59.1 | 52.0 |

---

**Interpretation (template):**
- Higher `kept` and `unique hosts` → better coverage/diversity.
- If `top hosts` concentrates on syndicators, tighten dedup or filter sources.
- `avg/med len` around 200–400 is reasonable for lead-3; much shorter → weak extraction.