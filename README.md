<div align="center">

# FRAME — Boutique Private Wealth Advisory & AI Intake Platform

> *Sophisticated wealth advisory intake, dynamic risk profiling, and compliance automation tailored for high-net-worth clients.*

[![Vercel Deployment](https://img.shields.io/badge/Status-Live%20Production-success?style=flat-square)](https://vercel.com)
[![Tech Stack](https://img.shields.io/badge/Stack-HTML5%20%7C%20CSS3%20%7C%20FastAPI%20%7C%20OpenAI-informational?style=flat-square)]()
[![Design System](https://img.shields.io/badge/Aesthetic-Alabaster%20%26%20Champagne%20Gold-9c8456?style=flat-square)]()

</div>

---

## 🌟 Overview

**FRAME** is a next-generation boutique wealth advisory intake and compliance review platform designed to bridge the gap between high-net-worth individuals (HNWIs) and private wealth advisers. 

Traditional wealth onboarding is often cumbersome, fragmented, and lacks immediate quantitative visualization. FRAME streamlines this entire journey into a seamless, high-end digital experience—combining a refined 10-question intake assessment, a dynamic 5-dimension risk/readiness radar chart, AI-driven executive summaries, and an automated adviser compliance review workflow.

---

## ✨ Core Features

* **High-End "Alabaster" Design System**: 
  * Custom-crafted UI inspired by top-tier private banks and family offices.
  * Features a sophisticated warm Alabaster background, Charcoal typography, and Champagne Gold accents.
* **Comprehensive 10-Question Client Intake**: 
  * Seamless multi-step questionnaire capturing client aspirations, risk appetites, and structural financial complexity.
* **Dynamic 5-Dimension Pentagon Radar Chart**: 
  * Native HTML5 Canvas visualization mapping client profiles across *Goal Clarity*, *Investment Knowledge*, *Risk Comfort*, *Planning Readiness*, and *Financial Complexity*.
* **AI-Powered Executive Insights**: 
  * Integrated with OpenAI GPT-4o to instantly generate professional 3-sentence executive summaries for incoming client profiles.
* **Adviser Command Center & Workflow Controls**: 
  * Interactive compliance decision panel (`✔ GREEN TICK`, `⚠ ORANGE REVIEW`, `✖ RED X`) ensuring rigorous audit trails and automated reporting.

---

## 🚀 System Architecture

```text
┌─────────────────────────┐          ┌─────────────────────────┐          ┌─────────────────────────┐
│   Client Intake Web UI  │ ───────> │  Python FastAPI Backend │ ───────> │    OpenAI GPT-4o API    │
│  (HTML5 / CSS3 / JS)    │          │  (AI Analysis & Router) │          │ (Executive Risk Insight)│
└─────────────────────────┘          └─────────────────────────┘          └─────────────────────────┘
             │                                    │
             └──────────────────┬─────────────────┘
                                ▼
                     ┌─────────────────────┐
                     │ Adviser Review Hub  │
                     │ (Workflow Decision) │
                     └─────────────────────┘
