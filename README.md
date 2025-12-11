# Indian Corporate Market Intelligence Dashboard 🚀

A comprehensive ecosystem to analyze and visualize data from Indian companies. This application provides insights into ratings, job openings, reviews, and hiring trends across the Indian corporate landscape.

## 🌟 Features

### 1. **Company Intelligence Dashboard** �
   - **Key Performance Indicators (KPIs)**: Instant view of Average Ratings, Total Job Openings, and Total Reviews across the market.
   - **Top Performers**: Visual rankings of:
     - 🏆 **Top Rated Companies**
     - 🚀 **Most Active Hiring Companies**
     - 💬 **Most Reviewed Companies**
     - 🗣️ **Companies with Most Interviews**
     - 💰 **Companies with Most Salary Data**
   - **Rating Distribution**: Histogram analysis of company ratings.

### 2. **Interactive Filtering & Exploration** �
   - **Smart Filters**:
     - Filter companies by minimum **Rating** (0.0 - 5.0).
     - Multi-select search for specific **Companies**.
   - **Full Database Access**: A detailed, sortable data grid showing:
     - Company Name
     - Rating (with visuals)
     - Open Jobs
     - Review Counts
     - Salary & Interview Data Points

### 3. **Premium UI Experience** 🎨
   - **Glassmorphism Design**: Modern, dark-themed interface with translucent cards and radial gradients.
   - **Responsive Layout**: Optimized grid layout for charts and metrics.
   - **Dynamic Visuals**: Polished Plotly charts with custom color scales (Magma, Viridis, Plasma).

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) (Python web framework)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
- **Visualization**: [Plotly Express](https://plotly.com/python/plotly-express/) & [Plotly Graph Objects](https://plotly.com/python/graph_objects/)

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed. You can check by running:
```bash
python --version
```

### Installation

1. **Clone or Download** this repository.
2. **Install Dependencies**:
   ```bash
   pip install streamlit pandas plotly numpy
   ```

### Running the App

Navigate to the project directory and run:

```bash
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`.

---

## 📂 Project Structure

```
├── app.py                      # Main application code
├── archive (4)/                # Data directory
│   └── companies.csv           # Company dataset
└── README.md                   # Project documentation
```

---

*Built for the Data Analysis Community.*
