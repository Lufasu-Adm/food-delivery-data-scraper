# 🚀 Enterprise Food Delivery Data Pipeline & Analytics

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Docker](https://img.shields.io/badge/Docker-Microservices-2496ED)
![Playwright](https://img.shields.io/badge/Playwright-Stealth-2EAD33)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57)

An end-to-end automated data pipeline that extracts restaurant data, ensures data integrity, and provides real-time analytics. Built with a **Microservices architecture using Docker**.

---

# 🏗️ System Architecture

This project consists of two containerized microservices running in parallel:

### 1️⃣ Scraper Bot (`food_scraper_bot`)
A headless **Microsoft Edge browser** running in stealth mode to bypass anti-bot systems.

Responsibilities:
- Schedule automated data extraction
- Scrape restaurant listings from YellowPages
- Clean and transform raw data
- Validate schema integrity
- Load processed data into SQLite database

### 2️⃣ Analytics Dashboard (`food_analytics_dashboard`)
A **Streamlit web application** that visualizes the scraped data.

Capabilities:
- Real-time data analytics
- Interactive charts and metrics
- Business insights from collected restaurant data

---

# 📊 Project Screenshots

## 1. Real-Time Analytics Dashboard
Interactive Streamlit dashboard displaying key metrics from scraped food delivery data.

```
https://github.com/Lufasu-Adm/food-delivery-data-scraper/blob/main/public/Food_Delivery_Data_Analytics.png
```

## 2. Telegram Bot Monitoring
The integrated Telegram bot sends execution logs and business insights directly to your Telegram account.

```
https://github.com/Lufasu-Adm/food-delivery-data-scraper/blob/main/public/TELE.jpeg
```

---

# ✨ Key Features

### 🕵️ Stealth Scraping
Uses **Microsoft Edge + Playwright** with automation evasion techniques to bypass anti-bot detection.

Features include:
- `navigator.webdriver` bypass
- `AutomationControlled` flag removal
- Dynamic content scraping

### ✅ Strict Data Validation
Uses **Pydantic schemas** to enforce data integrity.

Example validations:
- Rating must be between `0.0 – 5.0`
- Required fields enforcement
- Data type validation

### 📢 Automated Alerting
Integrated **Telegram Bot API** sends:

- Pipeline execution status
- Scraping completion notifications
- Business insights summaries

### 🐳 Containerized Deployment
Full environment reproducibility using:

- Docker
- Docker Compose
- Microservices architecture

---

# 🛠️ Tech Stack

| Layer | Technology |
|------|-------------|
| Extraction | Playwright (Python), BeautifulSoup4 |
| Transformation | Pandas, Pydantic |
| Storage | SQLite3 |
| Visualization | Streamlit |
| Infrastructure | Docker, Docker Compose |
| Monitoring | Telegram API, Python Logging |

---

# 🚀 How to Run (Local Deployment)

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Lufasu-Adm/food-delivery-data-scraper.git
cd food-delivery-data-scraper
```

---

## 2️⃣ Set Up Environment Variables

Create a `.env` file in the project root directory.

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

---

## 3️⃣ Deploy with Docker Compose

```bash
docker-compose up -d --build
```

This will start:

- Scraper microservice
- Streamlit analytics dashboard

---

## 4️⃣ Access the Dashboard

Open your browser and navigate to:

```
http://localhost:8501
```

---

# 📦 Project Structure

```
food-delivery-data-scraper
│
├── scraper/
│   ├── scraper.py
│   ├── parser.py
│   ├── validator.py
│
├── dashboard/
│   ├── app.py
│
├── database/
│   └── food_data.db
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

---

# 📡 Pipeline Workflow

```
YellowPages Website
        │
        ▼
Playwright Scraper
        │
        ▼
Data Cleaning (Pandas)
        │
        ▼
Schema Validation (Pydantic)
        │
        ▼
SQLite Database
        │
        ▼
Streamlit Analytics Dashboard
        │
        ▼
Telegram Notification
```

---

# 📬 Telegram Monitoring Example

When a pipeline finishes, the bot sends a message like:

```
✅ Pipeline Completed

Restaurants Scraped: 120
Average Rating: 4.2
Top Category: Japanese Food
Execution Time: 3m 42s
```

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

Developed by **Lufasu**

GitHub:  
https://github.com/Lufasu-Adm

