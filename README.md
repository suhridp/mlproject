
# 🎓 Student Performance Indicator

This project analyzes how different factors affect student performance in exams.  
It follows the **complete Machine Learning lifecycle** — from data collection and exploration to model building and deployment via a Flask API.

## website : https://student-marks-prediction-xqlv.onrender.com
---

## 📊 Problem Statement

The goal is to understand how a student's exam scores are influenced by variables such as:

- Gender  
- Race/Ethnicity  
- Parental Level of Education  
- Lunch Type  
- Test Preparation Course  

Dataset: [Kaggle – Student Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)  
Shape: **1000 rows × 8 columns**

---

## 🔄 ML Project Lifecycle

1. **Understanding the Problem Statement** – Define scope and target variable (exam performance).  
2. **Data Collection** – Gather data from Kaggle.  
3. **Data Checks** – Handle missing values, duplicates, data types, unique categories.  
4. **Exploratory Data Analysis (EDA)** – Visualize trends, correlations, distributions.  
5. **Data Preprocessing** – Feature engineering, encoding categorical variables, scaling numerical features.  
6. **Model Training** – Train ML models (Scikit-learn, XGBoost, CatBoost).  
7. **Model Selection** – Choose the best-performing model.  
8. **Deployment** – Expose predictions through a Flask API (`/predict` endpoint).  

---

## 🏗️ ETL Pipeline Structure

The project adopts a **modular ETL (Extract → Transform → Load)** approach:

1. **Extract**  
   - Input data collected from CSV, API, or form submissions.  
   - Loaded into a Pandas DataFrame.  

2. **Transform**  
   - Data cleaning (missing values, duplicates).  
   - Feature engineering (e.g., `total_score`, `average`).  
   - Encoding categorical variables.  
   - Standardization/normalization of numerical features.  

3. **Load**  
   - Processed data fed into the trained ML model.  
   - Model outputs predictions and confidence scores.  
   - Predictions returned as a JSON response (via Flask API).  

---

## 📂 Project Structure

```

├── app.py               # Flask API entry point
├── application.py       # App factory & configuration
├── requirements.txt     # Project dependencies
├── setup.py             # Package configuration
├── data/                # Dataset folder (stud.csv)
├── notebooks/           # Jupyter notebooks for EDA & experiments
└── models/              # Trained model artifacts

````

---

## 📡 API Usage

### Endpoints
- `GET /` → Health check  
- `POST /predict` → Predict student performance from input features  

### Example Request
```bash
curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{
           "gender": "female",
           "race_ethnicity": "group C",
           "parental_level_of_education": "bachelor's degree",
           "lunch": "standard",
           "test_preparation_course": "completed",
           "math_score": 72,
           "reading_score": 80,
           "writing_score": 78
         }'
````

### Example Response

```json
{
  "prediction": "High Performance",
  "average_score": 76.7,
  "confidence": 0.89
}
```

---

## 📦 Dependencies

Core libraries (see `requirements.txt` for full list):

* **Flask** – Web framework
* **pandas, numpy** – Data processing
* **matplotlib, seaborn** – Visualization
* **scikit-learn, XGBoost, CatBoost** – Machine Learning
* **gunicorn** – Deployment

---

## ▶️ Running the Project

### Development

```bash
python app.py
```

App runs locally at: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### Production

```bash
gunicorn -w 4 -b 0.0.0.0:8000 application:app
```

---

## 📈 Exploratory Data Analysis (Highlights)

* Female students generally outperform male students in overall scores.
* Standard lunch is associated with higher performance.
* Parental education level shows some impact (master’s/bachelor’s → better scores).
* Group A & B students tend to score lower on average.
* Completing test preparation course improves scores in all subjects.

---

## 🏆 Key Insights

* Student performance is significantly correlated with **lunch type, race/ethnicity, and parental education**.
* **Females outperform males** overall, but **males score higher in math**.
* Students who complete a **test preparation course** achieve better results across all subjects.

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

✨ With this project, you have a **complete ML pipeline** — from raw data to insights, model training, and deployment via API.

