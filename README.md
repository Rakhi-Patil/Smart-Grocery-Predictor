# 🛒 Smart Grocery Predictor

## Hybrid Grocery Product Recommendation System

**Smart Grocery Predictor** is a personalized grocery product recommendation system that recommends the **Top 5 products** for a customer based on:

* 👤 Customer purchasing behavior
* 🤝 Similar customers
* 🛒 Product popularity
* 🏷️ Customer category preferences

The project uses a **Hybrid Recommendation Approach** that combines **Collaborative Filtering, Product Popularity, and Category Preference** to generate personalized recommendations.

---

## 🎯 Key Features

* 👤 Personalized customer recommendations
* 🤝 Similarity-based Collaborative Filtering
* 🛒 Product Popularity
* 🏷️ Category Preference
* 🚫 Excludes previously purchased products
* ⭐ Top 5 product recommendations
* 📊 Hit Rate@5 and Precision@5 evaluation
* 📌 100% recommendation coverage
* 🌐 Flask web application

---

## 🧠 Recommendation Approach

The system combines three recommendation components:

| Component                  |   Weight |
| -------------------------- | -------: |
| 🤝 Collaborative Filtering |      60% |
| 🛒 Product Popularity      |      20% |
| 🏷️ Category Preference    |      20% |
| **Total**                  | **100%** |

### 🔢 Hybrid Score

```text
Hybrid Score =
    0.60 × Collaborative Score
  + 0.20 × Popularity Score
  + 0.20 × Category Preference Score
```

### 1. 🤝 Collaborative Filtering — 60%

A **customer-product matrix** is created from historical purchasing behavior.

Customers are compared based on their purchase patterns using similarity-based collaborative filtering.

Products purchased by customers with similar purchasing behavior become recommendation candidates.

### 2. 🛒 Product Popularity — 20%

Products are ranked according to their **total quantity sold**.

The popularity score is normalized between **0 and 1** and contributes 20% to the final recommendation score.

### 3. 🏷️ Category Preference — 20%

The system identifies categories preferred by each customer.

Products belonging to a customer's preferred categories receive a higher category preference score.

### ⭐ Final Recommendation

Previously purchased products are removed from the candidate list.

The remaining products are ranked using the **Hybrid Score**, and the **Top 5 products** are displayed.

---

## 🔄 System Workflow

```text
Customer ID
     ↓
Purchase History
     ↓
Customer Similarity
     ↓
Similar Customer Products
     ↓
Popularity + Category Preference
     ↓
Hybrid Score
     ↓
Remove Previously Purchased Products
     ↓
Rank Products
     ↓
Top 5 Recommendations
     ↓
Flask Web Application
```

---

## 📊 Dataset

The project uses grocery transaction data containing information related to:

* 👤 Customer
* 🛒 Product
* 📦 Order
* 💳 Transaction
* ⭐ Rating
* 🚚 Delivery

> **Note:** Rating and Delivery information are available in the dataset but are **not currently included in the Hybrid Recommendation Score**.

---

## 📈 Model Evaluation

The recommendation system uses a **holdout-based evaluation**.

For each valid test customer, one previously purchased product is hidden. The model then generates recommendations and checks whether the hidden product appears within the **Top 5 recommendations**.

### 📊 Evaluation Results

| Metric                            |     Result |
| --------------------------------- | ---------: |
| 👥 Total Customers                |  **8,417** |
| 👤 Customers with Recommendations |  **8,417** |
| 📌 Recommendation Coverage        |   **100%** |
| 🧪 Valid Test Customers           |    **463** |
| 🎯 Hits@5                         |    **245** |
| 📈 Hit Rate@5                     | **52.92%** |
| 🎯 Precision@5                    | **10.58%** |

### 🎯 Hit Rate@5

The hidden target product appeared in the Top 5 recommendations for:

```text
245 / 463 customers
```

Therefore:

```text
Hit Rate@5 = 52.92%
```

### 🎯 Precision@5

Precision@5 measures the average proportion of the five recommended products that are relevant to the hidden target.

```text
Precision@5 = 10.58%
```

---

## 🛠️ Technologies Used

### 💻 Programming

* Python

### 📊 Data & Machine Learning

* Pandas
* NumPy
* Scikit-learn
* Joblib

### 🌐 Web Development

* Flask
* HTML
* CSS

### 🔧 Tools

* Jupyter Notebook
* VS Code
* Anaconda
* Git
* GitHub

---

## 📁 Project Structure

```text
Smart-Grocery-Predictor/
│
|── screenshot/
│   ├── recommendations.png
│ 
├── app.py
├── Smart_Grocery_Project.ipynb
├── Zepto_Dataset.xlsx
├── README.md
├── .gitignore
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

---

## 💾 Recommendation Model

The Flask application uses a precomputed model file:

```text
recommendation_model.pkl
```

The model contains:

```text
customer_product
similarity_df
popularity_score
category_preference_df
product
```

The model is saved using **Joblib**.

### ⚠️ Important

The `recommendation_model.pkl` file is approximately **649 MB**, so it is **not stored in this GitHub repository** because GitHub has a **100 MB per-file limit**.

The file is included in `.gitignore`.

To run the Flask application, generate the model using the Jupyter Notebook and place the generated `recommendation_model.pkl` file in the project root directory.

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Rakhi-Patil/Smart-Grocery-Predictor.git
cd Smart-Grocery-Predictor
```

### 2. Install Dependencies

```bash
python -m pip install pandas numpy scikit-learn flask joblib pyarrow openpyxl
```

### 3. Generate the Recommendation Model

Open:

```text
Smart_Grocery_Project.ipynb
```

Run the required model-generation cells to create:

```text
recommendation_model.pkl
```

Place the generated file in the project root:

```text
Smart-Grocery-Predictor/
│
├── recommendation_model.pkl
├── app.py
├── Smart_Grocery_Project.ipynb
└── ...
```

### 4. Run Flask

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

Open the URL in your browser.

Select a **Customer ID** and click:

**Recommend Products**

---

## 🖥️ Screenshot

### ⭐ Recommendation Result


```markdown
<img width="3148" height="1734" alt="top%" src="https://github.com/user-attachments/assets/b3e2e821-1a90-4fad-96a2-3a7d8d088fc2" />

```

---

## ⚠️ Limitations

* Recommendations depend on historical transaction data.
* Ratings are not currently used in the recommendation score.
* Delivery information is not currently used.
* The evaluation uses a single hidden target product per test customer.
* The model currently uses predefined weights of **60%, 20%, and 20%**.
* The large `.pkl` model file is not included in GitHub.
* New customers with no purchase history may have limited personalization.

---

## 🔮 Future Enhancements

* ⭐ Include customer ratings
* 🚚 Include delivery performance
* 🖼️ Add product images
* 💡 Add recommendation explanations
* 🔎 Add product search
* 🧠 Explore advanced recommendation algorithms
* 👤 Add user login and customer profiles
* ☁️ Deploy the application to the cloud
* 🧪 Perform A/B testing
* ⚡ Improve model storage and loading performance

---

## 🏆 Results

| Performance Metric         |     Result |
| -------------------------- | ---------: |
| 📌 Recommendation Coverage |   **100%** |
| 🎯 Hit Rate@5              | **52.92%** |
| 📈 Precision@5             | **10.58%** |

---

## 🔑 Key Idea

> **Smart Grocery Predictor learns from customer purchasing behavior and combines similar-customer behavior, product popularity, and category preferences to recommend products that the customer is most likely to purchase next.**

---


---

## ⭐ Project Highlights

```text
🤝 Collaborative Filtering       → 60%
🛒 Product Popularity            → 20%
🏷️ Category Preference           → 20%
                                  ───
                                  100%

📌 Recommendation Coverage       → 100%
🎯 Hit Rate@5                    → 52.92%
📈 Precision@5                   → 10.58%
⭐ Recommendations per Customer  → Top 5
```

**Smart Grocery Predictor — Personalized recommendations powered by customer behavior and machine learning.** 🛒🤖
