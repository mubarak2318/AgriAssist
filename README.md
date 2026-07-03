# 🌾 AgriAssist

## Smart Farmer Advisory, Market Intelligence & Vendor Recommendation System

AgriAssist is a console-based Python application that helps farmers make informed agricultural decisions by providing recommendations for crop selection, fertilizers, pesticides, government schemes, market prices, vendors, risk assessment, and profit prediction.

The system combines multiple agricultural decision-support modules into a single advisory report, enabling farmers to make better decisions before starting a cultivation cycle.

---

## 📌 Project Overview

Indian farmers often depend on informal advice, middlemen, or guesswork while making farming decisions. AgriAssist addresses this problem by providing personalized recommendations based on the farmer's profile, including:

- Location
- Land size
- Soil type
- Water availability
- Season
- Budget

Using these inputs, the system generates a comprehensive Farmer Advisory Report covering crop planning, finance, inputs, and market recommendations.

---

## ✨ Features

- 🌱 Crop Recommendation
- 🌿 Fertilizer Recommendation
- 🐛 Pesticide Recommendation
- 🏛 Government Scheme Eligibility
- 💰 Loan Assistance
- 🏢 Company Recommendation
- 🛒 Vendor Recommendation
- 📈 Market Intelligence
- ⚠ Risk Assessment
- 💹 Profit Prediction
- 📄 Farmer Advisory Report Generation

---

## 🏗 Project Architecture

The application follows a modular layered architecture.

```
Presentation Layer
        │
        ▼
Application Controller (main.py)
        │
        ▼
Business Logic Modules
        │
        ▼
Data Loader
        │
        ▼
JSON Datasets
```

---

## 📂 Folder Structure

```
AgriAssist/
│
├── main.py
├── data/
├── modules/
│   ├── member1_crop_intelligence/
│   ├── member2_finance_gov/
│   └── member3_market_vendor/
│
├── utils/
├── models/
├── storage/
├── tests/
├── requirements.txt
└── README.md
```

---

## ⚙ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- CSV
- Modular Programming
- Console-Based User Interface

---

## 📊 Datasets

The project uses static JSON datasets including:

- Crops
- Fertilizers
- Pesticides
- Government Schemes
- Loan Information
- Vendors
- Companies
- Market Prices
- Risk Factors

---

## 🔄 System Workflow

```
Farmer Profile
       │
       ▼
Crop Recommendation
       │
       ├───────────────┐
       ▼               ▼
Government       Fertilizer
Schemes          Pesticides
       │               │
       └───────┬───────┘
               ▼
Loan Assistance
               ▼
Company Recommendation
               ▼
Vendor Recommendation
               ▼
Market Intelligence
               ▼
Risk Assessment
               ▼
Profit Prediction
               ▼
Farmer Advisory Report
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/mubarak2318/AgriAssist.git
```

### Navigate to the project

```bash
cd AgriAssist
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python main.py
```

---

## 👨‍💻 Team Structure

### Member 1
- Farmer Profile Analysis
- Crop Recommendation
- Fertilizer Recommendation
- Pesticide Recommendation

### Member 2
- Government Scheme Advisor
- Loan Assistance
- Risk Assessment
- Profit Prediction

### Member 3
- Company Categorization
- Vendor Recommendation
- Market Intelligence
- Report Generation

---

## 🎯 Objectives

- Assist farmers in selecting suitable crops.
- Recommend fertilizers and pesticides based on crop and soil.
- Provide government scheme recommendations.
- Suggest vendors and buyers based on location and pricing.
- Estimate cultivation cost, revenue, and profit.
- Generate a comprehensive farmer advisory report.

---

## 🔮 Future Enhancements

- Weather-based recommendations
- Crop rotation advisory
- Multi-crop comparison
- Local language support
- Session history
- PDF report generation
- Live market price integration
- Machine learning-based recommendations

---

## 📄 License

This project is developed for academic and educational purposes.
