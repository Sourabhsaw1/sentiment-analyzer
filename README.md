# 📊 Student Performance Data Analysis
### QSkill Python Development Internship — Task 1
**Author:** Sourabh Saw | **GitHub:** [@Sourabhsaw1](https://github.com/Sourabhsaw1)

---

## 🎯 Objective
Using **Pandas** and **Matplotlib/Seaborn**, perform data analysis on the Students Performance dataset and generate meaningful visualizations with insights.

---

## 📁 Project Structure
```
qskill_task1/
│
├── StudentsPerformance.csv   ← Dataset (Kaggle)
├── analysis.py               ← Main Python script
├── README.md                 ← This file
└── charts/
    ├── 01_bar_gender_scores.png
    ├── 02_bar_testprep_scores.png
    ├── 03_scatter_math_reading.png
    ├── 04_heatmap_correlation.png
    ├── 05_scatter_writing_reading.png
    └── 06_bar_parent_edu.png
```

---

## 🛠️ Libraries Used
| Library | Purpose |
|---------|---------|
| `pandas` | Data loading, cleaning & analysis |
| `matplotlib` | Creating charts & visualizations |
| `seaborn` | Enhanced statistical plots (heatmap) |
| `numpy` | Numerical operations & trend lines |

---

## ▶️ How to Run

```bash
# Step 1: Install dependencies
pip install pandas matplotlib seaborn numpy

# Step 2: Run the script
python analysis.py
```

Charts will be saved in the `charts/` folder automatically.

---

## 📊 Visualizations Generated

| # | Chart | Description |
|---|-------|-------------|
| 1 | Bar Chart | Average scores by Gender |
| 2 | Bar Chart | Impact of Test Preparation on scores |
| 3 | Scatter Plot | Math vs Reading (by Gender) with trend line |
| 4 | Heatmap | Correlation matrix of all scores |
| 5 | Scatter Plot | Writing vs Reading (by Lunch type) |
| 6 | Bar Chart | Average score by Parental Education level |

---

## 🔍 Key Insights & Observations

### 1. 📚 Test Preparation Matters!
- Students who **completed** test prep scored **72.67** on average
- Students who **did not** prepare scored **65.04** on average
- **Difference: 7.63 points** — Test prep clearly improves performance!

### 2. 🍱 Lunch Type = Socioeconomic Indicator
- **Standard lunch** students: **70.84** average
- **Free/reduced lunch** students: **62.20** average
- **Difference: 8.64 points** — Reflects real-world socioeconomic impact on education

### 3. 📈 High Correlation Between Reading & Writing
- Reading & Writing: **0.95 correlation** (very strong!)
- Math & Reading: **0.82 correlation** (strong)
- Students who excel in one subject tend to do well in others

### 4. 🎓 Parental Education Influences Performance
- Students with parents having a **Master's Degree** scored highest: **73.60 avg**
- Higher parental education = better academic environment at home

### 5. 👥 Gender Observations
- Females scored higher in **Reading** and **Writing**
- Males performed slightly better in **Math**
- Overall average is nearly equal across genders

---

## 📌 Dataset
- **Source:** [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Rows:** 1000 students
- **Columns:** 8 features (gender, race, parental education, lunch, test prep, math/reading/writing scores)

---

## 🏢 Internship Details
- **Organization:** QSkill (Squarcell Resource India Pvt. Ltd)
- **Domain:** Python Development
- **Duration:** 1st June – 1st July 2026
- **Mode:** Virtual | **Stipend:** Unpaid
