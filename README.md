# Fresher Market Intelligence Dashboard 2025 🚀

A comprehensive, market-intelligence dashboard designed to help fresh graduates navigate the Indian job market. This application provides insights into salary trends, in-demand skills, and company hiring patterns, powered by a Machine Learning model.

## 🌟 Features

### 1. **Market Trends Dashboard** 📈
   - **Key Performance Indicators (KPIs)**: Instant view of Average Salary, Selection Rounds, and Total Opportunities.
   - **Skill Analysis**: Interactive bar chart displaying the top 8 most in-demand technical skills for selected roles.
   - **Salary Distribution**: Box plots analyzing salary ranges across different company types (Product, Service, Startups, MNCs).

### 2. **Salary Predictor** 💰
   - **Machine Learning**: Uses a **Random Forest Regressor** to estimate salary packages.
   - **Customizable Inputs**: Predict your potential salary based on your:
     - **Role**: (e.g., Data Scientist, Backend Developer)
     - **Degree**: (e.g., B.Tech, MCA)
     - **Company Type**: (e.g., Product-based, Startup)
     - **City**: (e.g., Bangalore, Pune, Remote)

### 3. **Premium UI Experience** 🎨
   - **Glassmorphism Design**: Modern, dark-themed interface with translucent cards and radial gradients.
   - **Responsive Layout**: Top-bar navigation and filtering system for better usability.
   - **Dynamic Data Generation**: Automatically generates dummy market data if the source CSV is missing, ensuring the app always runs.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) (Python web framework)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
- **Visualization**: [Plotly Express](https://plotly.com/python/plotly-express/)
- **Machine Learning**: [Scikit-learn](https://scikit-learn.org/) (Random Forest, Pipelines)

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed. You can check by running:
```bash
python --version
```

### Installation

1. **Clone or Download** this repository to your local machine.
2. **Install Dependencies**:
   Open your terminal/command prompt and run:
   ```bash
   pip install streamlit pandas plotly scikit-learn
   ```

### Running the App

Navigate to the project directory and run the Streamlit server:

```bash
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`.

---

## 📂 Project Structure

```
├── app.py                                  # Main application code
├── Indian_Fresher_Salary_Skills_2025.csv   # Data source (Optional - app generates data if missing)
└── README.md                               # Project documentation
```

## 📝 Notes

- The application uses a **Random Forest Regressor** pipeline with **OneHotEncoding** to handle categorical data (City, Role, Company Type) effectively.
- If the dataset `Indian_Fresher_Salary_Skills_2025.csv` is not present, the app uses a robust internal data generator to create realistic dummy data for demonstration purposes.

---

*Built with ❤️ for the Data Analysis & Engineering Community.*
