# S-P500-Prediction-Using-Deep-Learning-Models-Python-FNN-CNN-LSTM-
Forecasts next-day S&amp;P 500 closing prices using deep learning architectures: Feedforward Neural Network (FNN), Convolutional Neural Network (CNN), and Long Short-Term Memory (LSTM). Trained on macroeconomic indicators from FRED (2022–2023). Models were tuned via Optuna/KerasTuner.

**Author:** Sebastian Heredia  
**Course:** BSAN6070 – INTRODUCTION TO MACHINE LEARNING  
**Tools:** Python (TensorFlow, Keras, Pandas, NumPy, Scikit-learn, Optuna)  

---

## 📘 Overview  
This project applies **deep learning architectures** — Feedforward Neural Network (FNN), Convolutional Neural Network (CNN), and Long Short-Term Memory (LSTM) — to forecast **S&P 500 daily closing prices** using macroeconomic indicators and technical data from **FRED (Federal Reserve Economic Data)** covering 2022–2023.  

The models were trained, tuned, and evaluated to determine which architecture delivers the **most accurate short-term market predictions**.  

---

## 🧩 Project Files  

| File | Description |
|------|--------------|
| `Final Project Proposal.docx` | Initial proposal outlining project scope, objectives, and expected outcomes. |
| `Final Project_Data Preparation.py` | Python script for cleaning, transforming, and merging financial and macroeconomic data. |
| `Final_Project_FNN.ipynb` | Feedforward Neural Network implementation with hyperparameter tuning. |
| `Final_Project_CNN.ipynb` | Convolutional Neural Network implementation optimized with Keras Tuner. |
| `Final Project LSTM.ipynb` | LSTM model for time series forecasting of S&P 500 daily returns. |
| `Final Project Report.pdf` | Full analytical report with results, evaluation metrics, and model comparison. |

---

## ⚙️ Methodology  

### 1. **Data Preparation**
- Collected daily S&P 500 data (2022–2023) and macroeconomic variables such as CPI, unemployment rate, interest rates, and VIX.  
- Data processed with **Pandas** and normalized for neural network training.  
- Generated lagged features and rolling averages for trend detection.  

### 2. **Modeling**
Three deep learning models were developed:  

| Model | Description | Key Layers |
|--------|--------------|-------------|
| **FNN** | Fully connected baseline for nonlinear feature learning | Dense, ReLU, Dropout |
| **CNN** | Captures spatial-temporal dependencies in rolling windows | Conv1D, MaxPooling, Flatten, Dense |
| **LSTM** | Sequential model capturing time dependencies | LSTM, Dropout, Dense |

### 3. **Optimization**
- Hyperparameter tuning using **Optuna** and **KerasTuner**.  
- Batch sizes (32–128), learning rates (1e-2–1e-5), and layer depths optimized via cross-validation.  

### 4. **Evaluation Metrics**
- Root Mean Squared Error (**RMSE**)  
- Mean Absolute Percentage Error (**MAPE**)  
- R² (Coefficient of Determination)  

---

## 📊 Results  

| Model | RMSE | MAPE | R² | Notes |
|--------|------|------|----|-------|
| FNN | 62.3 | 1.58% | 0.921 | Baseline neural model |
| **CNN** | **59.5** | **1.36%** | **0.938** | Best-performing model |
| LSTM | 61.2 | 1.49% | 0.930 | Strong sequence learning |

**Key Finding:**  
The **CNN model** outperformed FNN and LSTM, demonstrating superior pattern extraction from lagged input sequences.  

---

## 💡 Insights  
- **Macroeconomic indicators** (e.g., interest rate and CPI) significantly influence short-term price movement.  
- **CNN models** are effective for financial data when combined with lag-window feature engineering.  
- Ensemble or hybrid architectures (CNN+LSTM) may further enhance forecast accuracy.  

---

## 🚀 Future Work  
- Integrate **sentiment analysis** from financial news or Twitter data.  
- Extend models to **multi-step forecasts** (weekly/monthly).  
- Deploy as an interactive dashboard using **Streamlit** or **Plotly Dash**.  

---

## 📬 Contact  
**Sebastian Heredia**  
📧 andy_9149@hotmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/seb-heredia/)  
💻 [GitHub](https://github.com/andy9149)
