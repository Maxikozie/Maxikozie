<h1 align="center">Maximilian Schutte</h1>

<p align="center">
  Applied Computer Science student at Howest · Ghent, Belgium<br>
  <sub>Small tools, mostly built because I wanted them to exist.</sub>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/maximilian-schutte"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0yMC40NSAyMC40NWgtMy41NnYtNS41N2MwLTEuMzMtLjAyLTMuMDQtMS44NS0zLjA0LTEuODUgMC0yLjE0IDEuNDUtMi4xNCAyLjk0djUuNjdIOS4zNVY5aDMuNDF2MS41NmguMDVjLjQ4LS45IDEuNjQtMS44NSAzLjM3LTEuODUgMy42IDAgNC4yNyAyLjM3IDQuMjcgNS40NnY2LjI4ek01LjM0IDcuNDNhMi4wNiAyLjA2IDAgMSAxIDAtNC4xMyAyLjA2IDIuMDYgMCAwIDEgMCA0LjEzek03LjEyIDIwLjQ1SDMuNTZWOWgzLjU2djExLjQ1ek0yMi4yMiAwSDEuNzdDLjc5IDAgMCAuNzcgMCAxLjczdjIwLjU0QzAgMjMuMjMuNzkgMjQgMS43NyAyNGgyMC40NWMuOTggMCAxLjc4LS43NyAxLjc4LTEuNzNWMS43M0MyNCAuNzcgMjMuMiAwIDIyLjIyIDB6Ii8+PC9zdmc+" alt="LinkedIn"></a>
  <a href="https://www.kaggle.com/maximilianschutte"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white" alt="Kaggle"></a>
  <a href="mailto:maxikozie@proton.me"><img src="https://img.shields.io/badge/Email-6D4AFF?style=flat-square&logo=protonmail&logoColor=white" alt="Email"></a>
</p>

---

- 🎓 Second year of a Bachelor in Applied Computer Science at **Howest**, Bruges
- 🗺️ Spent summer 2025 as a **data engineering intern** at [Accurat.ai](https://accurat.ai): OpenStreetMap → MySQL → BigQuery pipelines, and a lot of polygon geometry
- 🖥️ Run a **Proxmox homelab** at home, which is where most of my Linux knowledge comes from
- 🗣️ Dutch · English · French

---

## Projects

### [TrustLayer](https://github.com/Maxikozie/good-will-prompting)

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-server-000000?style=flat-square)
![Hackathon](https://img.shields.io/badge/Tectonic%20Hackathon-Ghent%202026-6f42c1?style=flat-square)

An MCP server that tells AI assistants *which* internal document to trust. Given a question and the sources an assistant found, it scores each source 0–100 with readable reasons (owner, freshness, scope, corroboration), flags conflicts, and routes them to the person who can fix them. Scoring is deterministic, so no LLM is called at runtime. Built in a team of three for the SD Worx track.

<br>

### [FMHY SafeLink Guard](https://github.com/Maxikozie/FMHY-SafeLink-Guard)

![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=flat-square&logo=javascript&logoColor=F7DF1E)
![Stars](https://img.shields.io/github/stars/Maxikozie/FMHY-SafeLink-Guard?style=flat-square&color=DBAB0A)
![Status](https://img.shields.io/badge/status-merged%20upstream-6f42c1?style=flat-square)

Userscript that flags malicious and scam domains inline on any webpage, using the [FMHY](https://github.com/fmhy) filterlist as its source of truth. Cached client-side with a 7-day TTL, with a `MutationObserver` for dynamically injected links and a settings panel for personal overrides.

> Merged into the official [FMHY SafeGuard](https://github.com/fmhy/FMHY-SafeGuard) extension, so this repo is archived.

<br>

### [shira-ui](https://github.com/Maxikozie/shira-ui)

![Python](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=ffdd54)
![PyQt6](https://img.shields.io/badge/PyQt6-41CD52?style=flat-square&logo=qt&logoColor=white)
![Release](https://img.shields.io/github/v/release/Maxikozie/shira-ui?style=flat-square&color=2ea44f)

A desktop front-end for [shira](https://github.com/KraXen72/shira), a command-line music downloader for YouTube, YouTube Music and SoundCloud. Paste links, pick a folder, press Download: link queue, live progress with a working Cancel, and light/dark themes.

<br>

### Smaller things

| Project | What it does | Built with |
|---|---|---|
| [cover-posterizer](https://github.com/Maxikozie/cover-posterizer) | Turns a folder of `.cbz`/`.cbr` comics into one tiled poster of their covers, plus BBCode/Markdown file lists | Python, Pillow |
| [code-exam-trainer](https://github.com/Maxikozie/code-exam-trainer) | Desktop study tool that quizzes me on my own codebase for oral exams, with optional LLM grading of my answers | Python, PyQt6 |
| [CountryBoundaries](https://github.com/Maxikozie/CountryBoundaries) | Builds detailed European borders: OSM boundaries clipped against a high-res Natural Earth coastline | Python, GeoPandas, OSMnx |
| [NVIDIsolate-VFIOPassthrough](https://github.com/Maxikozie/NVIDIsolate-VFIOPassthrough) | Guide and toggle script for isolating an NVIDIA GPU for VFIO passthrough to a VM | Linux, Python |

<details>
<summary><b>Homelab</b></summary>
<br>

- **Proxmox VE** host running about a dozen LXC containers: reverse proxy, DNS sinkhole, media services and traffic monitoring
- **OpenWrt** router on a 1 Gbps fibre line, set up end to end: VLAN-tagged IPoE, a second access point, SQM/cake shaping and vnStat WAN accounting
- **16 TB** of bulk storage on an `mdadm` RAID 1 array

</details>

---

## Stack

<p>
  <img src="https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/JavaScript-323330?style=flat-square&logo=javascript&logoColor=F7DF1E" alt="JavaScript">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white" alt="Java">
  <img src="https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white" alt="PHP">
  <img src="https://img.shields.io/badge/Laravel-FF2D20?style=flat-square&logo=laravel&logoColor=white" alt="Laravel">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS-663399?style=flat-square&logo=css&logoColor=white" alt="CSS">
  <img src="https://img.shields.io/badge/Bash-121011?style=flat-square&logo=gnu-bash&logoColor=white" alt="Bash">
</p>

<p>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/BigQuery-669DF6?style=flat-square&logo=googlebigquery&logoColor=white" alt="BigQuery">
  <img src="https://img.shields.io/badge/Google%20Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white" alt="Google Cloud">
  <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="pandas">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/OpenStreetMap-7EBC6F?style=flat-square&logo=openstreetmap&logoColor=white" alt="OpenStreetMap">
</p>

<p>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux">
  <img src="https://img.shields.io/badge/Docker-0db7ed?style=flat-square&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Proxmox-E57000?style=flat-square&logo=proxmox&logoColor=white" alt="Proxmox">
  <img src="https://img.shields.io/badge/OpenWrt-00B5E2?style=flat-square&logo=openwrt&logoColor=white" alt="OpenWrt">
  <img src="https://img.shields.io/badge/Git-F05033?style=flat-square&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>
