# Student Exam Performance Indicator

This project aims to predict students' math scores based on various factors such as gender, ethnicity, parental level of education, lunch type, and test preparation course. By analyzing the dataset and training machine learning models, the project provides insights into how these factors influence student performance.

---

## Problem Statement

The goal of this project is to understand how students' performance (test scores) is affected by other variables such as:
- Gender
- Ethnicity
- Parental level of education
- Lunch type
- Test preparation course

The project also aims to build a machine learning model to predict math scores based on these factors.

---

## Dataset

- **Source**: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)
- **Description**: The dataset contains 1000 rows and 8 columns:
  - `gender`: Gender of the student (Male/Female)
  - `race/ethnicity`: Ethnicity of the student (Group A, B, C, D, E)
  - `parental level of education`: Parents' final education level
  - `lunch`: Type of lunch before the test (Standard/Free or Reduced)
  - `test preparation course`: Completion status of the test preparation course
  - `math score`: Math test score
  - `reading score`: Reading test score
  - `writing score`: Writing test score

---

## Project Workflow

### 1. Exploratory Data Analysis (EDA)
- Performed data cleaning, visualization, and statistical analysis to understand the dataset.
- Key insights:
  - Standard lunch improves performance.
  - Female students tend to perform better overall, except in math.
  - Test preparation courses positively impact scores.

### 2. Data Preprocessing
- Handled categorical variables using `OneHotEncoder`.
- Scaled numerical features using `StandardScaler`.
- Split the dataset into training and testing sets.

### 3. Model Training
- Trained multiple regression models, including:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - XGBoost Regressor
  - CatBoost Regressor
  - AdaBoost Regressor
- Evaluated models using metrics such as:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
  - R² Score

### 4. Deployment
- Built a Flask web application to allow users to input student details and predict math scores.
- Deployed the application on AWS Elastic Beanstalk.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/student-performance-indicator.git
   cd student-performance-indicator
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

---

## Usage

1. Open the application in your browser at `http://127.0.0.1:5000`.
2. Fill in the form with student details such as gender, ethnicity, parental education, etc.
3. Click "Predict Your Math Score" to get the predicted score.

---

## Project Structure

```
mlprojects/
├── app.py                     # Flask application
├── src/
│   ├── pipeline/
│   │   ├── predict_pipeline.py # Prediction pipeline
│   │   └── train_pipeline.py   # Training pipeline (if applicable)
│   ├── utils.py                # Utility functions
│   └── exception.py            # Custom exception handling
├── notebook/
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb  # Exploratory Data Analysis
│   ├── 2. MODEL TRAINING.ipynb           # Model Training
├── templates/
│   ├── index.html              # Home page
│   ├── home.html               # Prediction form
├── artifacts/                  # Saved models and preprocessors
├── data/
│   └── stud.csv                # Dataset
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Results

- **Best Model**: Random Forest Regressor
- **R² Score**: 0.92 (on test data)

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - Data Analysis: Pandas, NumPy
  - Visualization: Matplotlib, Seaborn
  - Machine Learning: Scikit-learn, XGBoost, CatBoost
- **Web Framework**: Flask
- **Deployment**: AWS Elastic Beanstalk

---

## Future Enhancements

- Add more features to improve prediction accuracy.
- Deploy the application using Docker and Kubernetes for scalability.
- Integrate additional machine learning models for comparison.

---

## Author

**Vijayakumar**

Feel free to reach out for any questions or suggestions!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.