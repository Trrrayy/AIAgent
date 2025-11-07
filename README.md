# AIAgent — Automated Topic-to-News Summarization Pipeline

A reproducible pipeline that turns a **topic** (e.g., “antibiotics”, “vaccines”) into a **Markdown report** summarizing recent news. No API keys required. The system fetches public articles via Google News RSS, extracts main text, performs light de-duplication, and produces **extractive lead-3** summaries alongside a JSON sidecar for evaluation.

This repository also includes a tiny **offline multi-agent simulation** (Manager → Researcher → Coder) to demonstrate an “AI framework” workflow without external services—useful for teaching and ablations.

---

## Highlights

- **Deterministic & Auditable**: Same inputs → same outputs. Each report embeds a transparent **Methods** section.
- **No Keys, No Docker**: Runs in a local Python venv; network is only used to fetch public webpages.
- **Locale-Aware**: Switch language/region (`--locale/--region/--ceid`) for broader coverage (e.g., Chinese sources).
- **Evaluation-Ready**: JSON sidecars + a small evaluator produce a quantitative `COMPARISON.md` (coverage, host diversity, summary lengths).

---

## Quick Start

> Recommended: Python **3.10+**. Python 3.9 also works (you may see a harmless `urllib3`/LibreSSL warning on macOS).

```bash
# Clone
git clone https://github.com/Trrrayy/AIAgent.git
cd AIAgent

# Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Windows PowerShell: .\.venv\Scripts\Activate.ps1

# (Deps auto-install at runtime, but you can preinstall)
python -m pip install -U pip
python -m pip install feedparser trafilatura requests
