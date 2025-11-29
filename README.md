# RCA_AGENT
A Multi-Agent System for Autonomous Root Cause Analysis and Self-Correction

🔍 RCA Agent – Root Cause Analysis using Gemini (Agentic AI)

This project contains an **RCA Agent (Root Cause Analysis Agent)** powered by
Google’s **Gemini 1.5 Flash** model.  
It was developed as part of the **Kaggle 5-Day Agentic AI Program** and is
fully deployable to **Vertex AI** or **Cloud Run**.

The agent takes a problem description as input and returns:

✅ The root cause  
✅ Impact & severity  
✅ Required fixes  
✅ Timeline  
✅ Preventive measures  
✅ Confidence score  
---

# 🧠 What is the RCA Agent?

RCA (Root Cause Analysis) is used in engineering, IT, manufacturing, and business
to identify *why* a problem occurred and *how* to prevent it from happening again.

This agent automates the ENTIRE RCA workflow.

### ✨ Features of the RCA Agent

- Accepts **any type of incident or problem statement**
- Uses **Gemini reasoning** to analyze cause–effect relationships
- Produces structured RCA sections:
  - Problem Summary  
  - Root Cause  
  - Contributing Factors  
  - Severity & Impact  
  - Fixes  
  - Action Plan  
  - Prevention Measures  
  - Confidence Score  
- Fast inference using **Gemini 1.5 Flash** (cheap & lightweight)
- Deployable as a REST API for apps, dashboards, chatbots, and internal tools

---

# 🏗️ System Architecture

User Input → FastAPI Server → Gemini Model → Structured RCA Response → JSON Output

When deployed to **Vertex AI / Cloud Run**, the pipeline becomes:

Client (UI / App / Agent)
↓
Cloud Run API (this app.py)
↓
Gemini API (Google Generative AI)
↓
RCA Output

# 🚀 Deployment Options

This project supports:

### **1. Google Cloud Run (Easiest)**
- Simple to deploy  
- Auto-scaling  
- Best for APIs & webhooks  

### **2. Vertex AI Endpoints (Advanced)**
- Enterprise-grade model hosting  
- Can integrate with Vertex AI Agents  
- Perfect for production workloads  

---

# 📁 Files Included

| File | Description |
|------|-------------|
| `app.py` | FastAPI server exposing `/predict` endpoint |
| `requirements.txt` | Python dependencies |
| `README.md` | Documentation (this file) |

---

# 🧪 Local Development

### Install dependencies
pip install -r requirements.txt


### Set your Gemini API key
export GEMINI_API_KEY="your_key_here"

shell
Copy code

### Run the server
uvicorn app:app --reload --port 8080


# 📡 API Usage

### POST request:

POST /predict
{
"query": "Our website is crashing during checkout when more than 200 users are active."
}

### Sample Response:

{
"response": {
"root_cause": "Unoptimized database queries causing a bottleneck.",
"contributing_factors": ["High traffic peak", "No caching layer"],
"impact": "30% drop in sales during peak hours",
"severity": "High",
"confidence": "92%"
}
}
