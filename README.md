# 📊 LLM-Powered Exploratory Data Analysis (EDA)

This project is a web-based application that performs **automated Exploratory Data Analysis (EDA)** on any uploaded CSV file using **Gradio**, **Pandas**, **Seaborn**, and **Ollama's Mistral model** for AI-generated insights.

---

## 🚀 Features

- 📁 Upload a CSV dataset
- 📈 Automatically generates:
  - Statistical summaries
  - Missing value analysis
  - Histograms for numeric features
  - Correlation heatmap
- 🤖 AI-powered insights using the **Mistral-7B** language model via Ollama
- 🧠 Auto-handles missing values using median (numerical) or mode (categorical)

---

## 🛠️ Requirements

- Python 3.8+
- Install dependencies using pip:

```bash
pip install gradio pandas matplotlib seaborn ollama

