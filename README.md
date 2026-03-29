# Apex Trace — User Activity Monitoring

## 1. What We Do (Current Capabilities)
Build a **local-first desktop application** that monitors user activity on a Windows PC to provide **truthful, analyzable data** about how the computer is used. It acts as an observation-only foundation.

### Core Tracking & Processing:
* **OS-Level Activity Monitoring**: Captures active applications, foreground/background window changes, and Idle/AFK states.
* **Interaction Metrics**: Tracks keyboard/mouse signal presence to weight active vs passive usage (e.g., active browsing vs leaving an app open in the background).
* **Data Aggregation Architecture**: 
  - Raw JSON logs act as the source of truth (highly detailed, rotated daily).
  - Background daily aggregation processes summarize raw data into lightweight, UI-ready metrics.
* **Desktop Dashboard (MVP)**:
  - Built with **Next.js + Tauri** fetching aggregated JSON data via secure native Rust IPC.
  - Displays **Weekly Activity charts**, **Tracked Time** summaries, and **Daily Uptime Targets**.
  - Includes user settings interface (General, Notifications) aligned to the brand aesthetic.
* **Privacy & Safety First**: 
  - 100% Local-only data storage. No network uploads.
  - Non-destructive and entirely reversible.

---

## 2. What We Don't Do (Yet)
This phase establishes **ground truth data** only. Currently, the system explicitly **does NOT**:
* **Use AI Analysis**: There is no machine learning or intelligence scoring occurring.
* **Enforce Discipline**: The app will not block your usage, close your games, or force you to work.
* **Log Key Content**: We do not log the actual keys pressed or text typed (only the signal that a keystroke occurred).
* **Upload to Cloud**: There is no remote dashboard or cloud syncing.

---

## 3. Features That Will Be Implemented (Roadmap)
Based on current backend architecture plans, the following features will be integrated in later phases:

### Productivity & Enforcements
* **Productivity Detection & Analysis**: Categorize and score the efficiency of time spent.
* **Access Control & App Blocking**: Firewall rules or process execution blocking to prevent access to certain apps/websites during focus periods.
* **Time-Limit Enforcement**: Automatically closing applications when they are used for too much time (e.g., closing League of Legends after 2 hours and blocking it for 24H).

### Enhanced Monitoring
* **Background Content Tracking**: Monitor specific media details like YouTube videos playing or Music players.
* **Game-Specific Detection**: Deep integration to detect when a user is in Champion Select, In-Game, or in Lobby (e.g., League of Legends).
* **Granular Logging**: More detailed raw logging of exact keystrokes, mouse movements, and application clicks.

### AI & Reporting Features
* **Full Visualization Dashboard**: Expanding the UI to include exhaustive reports and data breakdowns.
* **Smart Notifications**: Proactive desktop alerts regarding productivity trends and time sinks.
* **AI Assistant & Guider**: Help with tasks, scheduling, reminders, and projections regarding progress on the user's skill level.
* **AI Controller**: An optional AI agent that can manage your PC environment dynamically based on your focus state.

---

## Technology Stack
* **Background Agent**: Python (Packaged to EXE via PyInstaller).
* **Desktop UI**: Next.js + TailwindCSS + ApexCharts.
* **Application Shell**: Tauri (Rust IPC bridging).
* **Storage**: Local JSON filesystem.