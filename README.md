# San Antonio 311 Service Call Machine Learning & Geospatial Clustering

An end-to-end data science project analyzing City of San Antonio 311 municipal customer service records. The project extracts predictive signal from unstructured ticket descriptions, benchmarks machine learning classification models to forecast delayed service resolutions, and segments geographic call volumes using unsupervised spatial clustering.

---

## Project Overview

- **Dataset:** San Antonio 311 Municipal Service Calls (~450,000+ total historical records)
- **Evaluation Split:** 80/20 train-test split resulting in **90,153 holdout test cases**
- **Primary Tasks:**
  1. **Text Feature Extraction & Classification:** Predict service ticket delays and categories from unstructured case descriptions (`Reason Name` + `Type Name`).
  2. **Geospatial Clustering:** Cluster geographical coordinates across San Antonio into distinct municipal service zones using K-Means.
- **Tech Stack:** Python, Pandas, NumPy, Scikit-learn, Matplotlib, TF-IDF Vectorization

---

## Data Source

- **Portal:** City of San Antonio, 311 All Service Calls ([Open Data SA](https://data.sanantonio.gov/dataset/311-all-service-calls))
- **One-Click Export:** [ArcGIS CSV Download](https://opendata-cosagis.opendata.arcgis.com/api/download/v1/items/754d5490121e44b8b6f3712934b24839/csv?layers=0)
- **Underlying API:** [ArcGIS FeatureServer](https://services.arcgis.com/g1fRTDLeMgspWrYp/ArcGIS/rest/services/311_All_Service_Calls/FeatureServer)

*Note: The raw CSV (~100 MB+) is excluded from the Git repository. Use `download_data.py` to retrieve it locally.*

---

## How to Run

1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt

---

## Methodology

### 1. Data Cleaning & Feature Engineering
* Extracted and concatenated multi-field text descriptions:
  $$\text{text\_input} = \text{Reason Name} + \text{" "} + \text{Type Name}$$
* Processed text features using `TfidfVectorizer` (English stop words removed, top 1,000 max features).
* Structured an **80/20 train-test split** (`random_state=42`) yielding **90,153 evaluation samples**.

### 2. Supervised Modeling & Evaluation
Trained and benchmarked three predictive classification architectures using Scikit-learn:
* **Support Vector Classifier (SVC):** Linear kernel
* **Random Forest Classifier:** 100 estimators, maximum depth of 20
* **Decision Tree Classifier:** Maximum depth of 20

#### Results & Confusion Matrix Analysis
Evaluating the final model on the 90,153 holdout test cases produced the following confusion matrix:

```text
Confusion Matrix:
[[73546    666]
 [13765   2176]]
```

* **Overall Predictive Accuracy:** **83.99% (~84%)**
  $$\text{Accuracy} = \frac{73,546 + 2,176}{90,153} = 83.99\%$$
* **True Negatives:** 73,546 correctly classified standard/on-time resolutions.
* **True Positives:** 2,176 correctly identified delayed resolutions.
* **Class Imbalance Note:** The dataset displays a severe class imbalance characteristic of real-world municipal reporting (the vast majority of calls are resolved without systemic delays).

---

### 3. Geospatial K-Means Clustering ($k = 5$)
* Extracted spatial coordinate features (`X Coordinate`, `Y Coordinate`) across the metropolitan area.
* Applied **K-Means clustering** with $k = 5$ to partition municipal request volume into five geographic service sectors.

#### Domain Insights & Municipal Exclusion Zones
* **Federal Enclaves:** Plotting reveals distinct data voids corresponding to federal and military reservations—specifically **Joint Base San Antonio (JBSA) Fort Sam Houston** and **Lackland Air Force Base**—as well as regional reservoirs and municipal flood basins where city 311 services do not operate.
* **Density Distribution:** Ticket density concentrates heavily along major transit corridors surrounding Downtown San Antonio, providing clear visual boundaries between municipal districts.
* 
