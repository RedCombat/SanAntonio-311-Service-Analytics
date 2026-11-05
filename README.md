# SanAntonio-311-Service-Analytics

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com)

## Overview
* **Dataset:** 311 Municipal Service Calls (90,000+ test records evaluated)
* **Goal:** Replicate service classification methodology to predict ticket delays and cluster request volumes by location.
* **Tech Stack:** Python, Pandas, Scikit-learn, Matplotlib, TF-IDF Vectorization

## Methodology
1. **Feature Engineering & NLP:** Combined textual fields (`Reason Name` + `Type Name`) and applied `TfidfVectorizer` (max 1,000 features) to extract predictive text features.
2. **Modeling:** Trained and benchmarked Support Vector Classifier (`SVC`), `RandomForestClassifier`, and `DecisionTreeClassifier` using an 80/20 train-test split.
3. **Geospatial Clustering:** Performed K-Means spatial clustering on coordinates to map the geographic distribution of city service requests.

## Key Results
* **Classification Accuracy:** Achieved **~84% overall accuracy** on the test split for request classification.
* **Confusion Matrix:** Correctly flagged over 73,500 standard resolution cases while isolating delinquent resolution patterns.
* Spatial plotting clearly delineates municipal boundaries and unpopulated/federal zones, showing distinct data voids over major federal installations (JBSA-Fort Sam Houston and Lackland Air Force Base) and natural reservoirs where city 311 services do not operate.
