# Covid-19 Pandemic Analysis Dashboard

An interactive dashboard built using **Streamlit**, **Pandas**, and **Plotly** to visualize Covid-19 pandemic data. The dashboard provides daily case trends, country-wise statistics, and visualizations for recovery and death rates.

---

## Features

- **Bar Chart:** Total Cases by Country
- **Line Chart:** Daily Cases Trend
- **Pie Chart:** Recovery vs Death Rate
- **KPIs:** Total Cases, Deaths, Recovered
- **Sidebar:** Switch between visualizations

---

## Project Structure

```
country_wise_latest.csv
day_wise.csv
covid19.py
LICENSE
README.md
```

---

## Requirements

- Python 3.8+
- Streamlit
- Pandas
- Plotly
- Matplotlib

---

## Setup Instructions

1. **Create a Virtual Environment (Recommended):**
   ```sh
   python -m venv venv
   ```
   Activate the environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

2. **Install Dependencies:**
   ```sh
   pip install streamlit pandas plotly matplotlib
   ```

3. **Download/Place Data Files:**
   Ensure `country_wise_latest.csv` and `day_wise.csv` are in the project directory.

---

## How to Run

1. Open a terminal in the project directory.
2. Run the Streamlit app:
   ```sh
   streamlit run covid19.py
   ```
3. The dashboard will open in your browser.

---

