# daily-github-activity

An automated, transparent daily activity logger powered by Python 3 and GitHub Actions.

---

## 📌 Overview

`daily-github-activity` is an automated utility that appends a single timestamped entry to `daily_activity.txt` on a daily schedule using GitHub Actions.

> [!IMPORTANT]
> **Transparency Note**: This repository serves as an automated activity logger and a demonstration of GitHub Actions cron workflows. It is **not** a substitute for genuine software engineering, active problem solving, or meaningful contributions to open-source and commercial projects.

---

## ⚙️ How It Works

1. **GitHub Actions Runner**: At a scheduled time every day (or when triggered manually), GitHub spins up an isolated `ubuntu-latest` virtual machine.
2. **Environment Setup**: The runner checks out this repository and configures Python 3.x.
3. **Execution**: The runner executes [`daily_update.py`](daily_update.py), which determines the current UTC time and appends a formatted entry to [`daily_activity.txt`](daily_activity.txt).
4. **Commit & Push**: The runner inspects Git status. If changes are detected, it commits `daily_activity.txt` under the identity of `github-actions[bot]` and pushes the commit back to your repository's default branch.

---

## 🕒 How the Schedule Works & Timing Disclaimers

The automation is configured in [`.github/workflows/daily.yml`](.github/workflows/daily.yml) using a cron expression:

```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # Runs every day at 00:00 UTC
  workflow_dispatch:
```

### Why Scheduled Actions Can Be Delayed
GitHub Actions cron triggers run on shared infrastructure across GitHub's global servers. During peak usage hours, scheduled runs may experience delays of **several minutes up to an hour** or, on rare occasions, be skipped if GitHub experiences severe platform load. This is normal behavior documented by GitHub.

---

## 💻 Running the Script Locally

The script requires only Python 3 (standard library only; no third-party package installation needed).

### macOS / Linux
```bash
# Clone the repository (if not already local)
cd daily-github-activity

# Run the update script
python3 daily_update.py
```

### Windows
```cmd
cd daily-github-activity
python daily_update.py
```

Each run appends a new line formatted as:
```text
Daily activity: 2026-09-17 13:30:00
```

---

## 🚀 Manual Workflow Trigger

You can trigger the workflow on demand without waiting for the daily cron schedule:

1. Navigate to your repository on GitHub.
2. Click on the **Actions** tab at the top.
3. In the left sidebar under *Workflows*, click **Daily Activity Update**.
4. Click the **Run workflow** dropdown button on the right.
5. Select your branch (usually `main`) and click **Run workflow**.
6. Refresh the page after a few seconds to see the workflow running and review the generated commit.

---

## 🔒 Ensuring GitHub Actions Write Permissions

For the workflow to push commits back to your repository, ensure write permissions are enabled:

1. In your GitHub repository, navigate to **Settings**.
2. Under the *Code and automation* section in the left sidebar, click **Actions** > **General**.
3. Scroll down to **Workflow permissions**.
4. Select **Read and write permissions**.
5. Click **Save**.

---

## 📁 Repository Structure

```text
daily-github-activity/
├── .github/
│   └── workflows/
│       └── daily.yml         # GitHub Actions workflow definition
├── daily_update.py           # Core Python script for logging entries
├── daily_activity.txt        # Output log recording daily timestamps
├── README.md                 # Project documentation and instructions
└── .gitignore                # Git ignore patterns for Python & OS files
```
