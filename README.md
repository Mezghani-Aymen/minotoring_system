# Small Product — User Activity Monitoring (No AI Yet)

## Purpose

Build a **local-first desktop application** that monitors user activity on a Windows PC to provide **truthful, analyzable data** about how the computer is used. This phase contains **no AI and no enforcement**. It is observation only.

The product is a foundation for later AI-based skill analysis and discipline enforcement.

---

## Core Goals

* Monitor **OS-level user activity**
* Classify activities by **type** (browser, folder, editor, games, files, etc.)
* Measure **time and interaction**, not just presence
* Store data **locally** and privately
* Provide a **dashboard** for analysis
* Be safe, reversible, and non-destructive

---

## What Is Tracked

### Application Events

* Application opened
* Application closed
* Foreground (active window) and background changes  

### Application Types

Each application is classified into a type:

* Browser
* Folder (File Explorer)
* Editor / IDE
* Game
* File viewer
* Other

### Time Metrics

* Foreground duration per app
* Total duration per app type
* Idle time
* Background duraction per app

### Interaction Metrics

* Keyboard activity (signal only, no content)
* Mouse activity (signal only)
* Interaction-weighted time

Example:

* Browser open 20 min, high interaction
* Folder open 20 min, low interaction
  → Browser is considered dominant activity

---

## Data Processing

### Aggregation

* Time per application
* Interaction vs passive time
* App-switch timeline (A → Z)

### Filtering

* By date
* By time range
* By application type

---

## Dashboard (MVP)

### Views

1. **Timeline View**

   * Sequential app usage (A → Z)

2. **Grouped Statistics**

   * Time by app
   * Time by type

3. **Interaction Analysis**

   * Active vs passive usage

4. **Daily Summary**

   * Focus-heavy vs distraction-heavy periods

No scoring, judgment, or enforcement in this phase.

---

## Technology Stack

### Core System

* Language: Python
* Role: Background activity agent

### Storage

* JSON file 

### API Layer

* NULL

### Desktop UI

* React + TypeScript
* Packaged with Tauri

### Distribution

* Python packaged to EXE (PyInstaller)
* Desktop app packaged as EXE

---

## Safety & Privacy Rules

* Local-only data storage
* No cloud or network upload
* No key content logging
* No destructive system actions
* Fully uninstallable

---

## What This Phase Is NOT

* No AI analysis
* No skill scoring
* No enforcement or blocking
* No motivation logic

This phase establishes **ground truth data** only.

---

## Future Integration (Later Phases)

* AI behavior pattern detection
* Skill-based project analysis
* Automatic discipline mode escalation
* OS-level enforcement

---

## One-Line Summary

This product is a **desktop-based activity observability system** designed to measure real computer usage accurately and safely, serving as the foundation for future AI-driven discipline and skill monitoring.