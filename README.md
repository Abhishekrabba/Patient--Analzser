# 🏥 Healthcare Patient Data Analyzer

A Python-based Electronic Health Record (EHR) analyzer that reads patient vital signs from CSV files and automatically classifies them based on health thresholds.

---

## Features

- Analyzes heart rate, blood pressure, and glucose levels
- Flags patients as Critical based on thresholds
- CLI interface to filter by age, condition, and export results
- Uses only pandas and NumPy (no visualization)

---



- Python
- pandas
- NumPy

---
 Structure

```
patient-analyzer/
├── data/
│   └── patient_records.csv
├── analyzer.py
├── processed_results.csv
└── README.md
```

---

## 📄 Sample Input (`data/patient_records.csv`)

| PatientID | Name  | Age | HeartRate | SystolicBP | DiastolicBP | Glucose |
|-----------|-------|-----|-----------|------------|--------------|---------|
| P001      | Anil  | 65  | 88        | 150        | 95           | 180     |
| P002      | Sneha | 34  | 72        | 120        | 80           | 95      |

---



```bash
python analyzer.py
```

 `data/patient_records.csv` file exists.

---

## 🔍 Threshold Logic

| Vital         | Condition           | Status    |
|---------------|---------------------|-----------|
| Heart Rate    | <60 or >100 bpm     | Abnormal  |
| Blood Pressure| Systolic >140 or Diastolic >90 | High |
| Glucose       | >140 mg/dL          | High      |

If **any** of the above is true → the patient is marked **Critical = YES**


