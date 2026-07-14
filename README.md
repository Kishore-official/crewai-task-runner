<div align="center">

# 📄 CrewAI Research & Report Writer

### A 3-agent pipeline that researches a topic and writes a formatted markdown report

[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-FF5A1F?style=for-the-badge)](https://crewai.com/)
[![Python](https://img.shields.io/badge/Python-3.10--3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/LLM-OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)

[![Agents](https://img.shields.io/badge/Agents-3-blueviolet?style=flat-square)](#the-crew)
[![uv](https://img.shields.io/badge/Managed_with-uv-DE5FE9?style=flat-square)](https://docs.astral.sh/uv/)

</div>

A [CrewAI](https://crewai.com) crew (`AiLatestDevelopment`) that takes a topic and the current year as input, researches it, expands the findings into a full report, and writes the final markdown output to disk.

## 🤖 The Crew

| Agent | Role |
|---|---|
| 🔍 **Researcher** | Finds the 10 most relevant, up-to-date bullet points on the given topic |
| 📊 **Reporting Analyst** | Expands each finding into a full report section |
| 📝 **File Writer** | Formats and writes the final report as markdown |

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Agent Framework | CrewAI |
| LLM | OpenAI |
| Dependency management | uv |
| Config | YAML (`agents.yaml`, `tasks.yaml`) |

## 🚀 Getting Started

```bash
# Install uv
pip install uv

# Install dependencies
crewai install

# Add your OPENAI_API_KEY to .env

# Run the crew
crewai run
```

Customize via `agents.yaml`, `tasks.yaml`, `crew.py`, and `main.py` (topic/year inputs).

## 📬 Contact

- **Email:** arunkishore757@gmail.com
- **GitHub:** [@Kishore-official](https://github.com/Kishore-official)
