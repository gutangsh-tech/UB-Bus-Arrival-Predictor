# 🚌 Ulaanbaatar Bus Arrival Time Predictor (AI)

An AI-driven model designed to predict bus arrival times in Ulaanbaatar, Mongolia, by accounting for real-world urban challenges like heavy traffic congestion and peak hour variables.

## 📌 Project Overview
Living in Ulaanbaatar, traffic is a major daily challenge. Standard GPS-based arrival times often fail because they don't account for the "Ulaanbaatar Factor" (extreme congestion). This project uses a **Gradient Boosting Regressor** to provide more accurate estimates based on distance, time of day, and a custom-calculated traffic index.

## 🛠️ Tech Stack
- **Language:** Python 3.9
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib
- **Model:** Gradient Boosting Regressor (GBR)

## 📊 How it Works
1. **Data Generation:** Since public API access can be unstable, I built a synthetic data generator that models UB's traffic patterns (Peak hours at 08:00 and 18:00).
2. **Feature Engineering:** The model looks at `distance_km`, `hour_of_day`, and `traffic_density`.
3. **Training:** The data is split into training (80%) and testing (20%) sets to ensure accuracy.

## 🚀 How to Run
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/UB-Bus-Arrival-Predictor.git`
2. Install dependencies: `pip install pandas scikit-learn matplotlib`
3. Generate data: `python3 bus_data.py`
4. Train AI: `python3 bus_model.py`

---
*Created as part of my AI Portfolio for university applications.*
