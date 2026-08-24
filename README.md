# 🛒 Smart Grocery Predictor

## Hybrid Product Recommendation System using Machine Learning

**Smart Grocery Predictor** is a personalized grocery product recommendation system that recommends the **Top 5 products** for a customer based on:

* Customer purchasing behavior
* Similar customers
* Product popularity
* Customer category preferences

The system uses a **Hybrid Recommendation Approach** that combines **Collaborative Filtering, Product Popularity, and Category Preference** to generate personalized recommendations.

---

## 📌 Project Overview

Online grocery platforms contain a large number of products, making it difficult for customers to discover products that may be relevant to them.

The **Smart Grocery Predictor** analyzes customer purchase data and generates personalized product recommendations.

For a given customer, the system:

1. Analyzes the customer's previous purchases.
2. Finds customers with similar purchasing behavior.
3. Identifies generally popular products.
4. Determines the customer's preferred product categories.
5. Combines these factors into a Hybrid Score.
6. Removes products that the customer has already purchased.
7. Returns the **Top 5 recommended products**.

---

## 🎯 Objectives

* Provide personalized grocery product recommendations.
* Analyze customer purchasing behavior.
* Find similar customers using Collaborative Filtering.
* Identify popular products.
* Analyze customer category preferences.
* Avoid recommending products already purchased.
* Generate a ranked Top 5 recommendation list.
* Evaluate recommendation performance.
* Provide a web interface using Flask, HTML, and CSS.

---

# 🧠 Recommendation System

The project uses three recommendation components.

## 1. Collaborative Filtering — 60%

Collaborative Filtering is the main component of the recommendation system.

It identifies customers with similar purchasing behavior and uses the products purchased by those similar customers to generate recommendations.

It answers:

> **"What products are purchased by customers who have purchasing behavior similar to this customer?"**

### How it works

1. A customer-product matrix is created.
2. Customers are compared based on their purchasing behavior.
3. Similar customers are identified.
4. Products purchased by similar customers are considered for recommendation.
5. A Collaborative Score is calculated for candidate products.

---

## 2. Product Popularity — 20%

The popularity component identifies products that are purchased frequently.

The total quantity sold for each product is calculated and normalized between **0 and 1**.

```text
1.0 → Most popular product
0.0 → Least popular product
```

Popular products receive a higher popularity score and contribute to the final recommendation score.

---

## 3. Category Preference — 20%

The category preference component identifies the product categories preferred by each customer.

For example:

```text
Snacks & Branded Foods → 1.00
Baby Care              → 0.90
Dairy & Bakery         → 0.80
Beverages              → 0.50
Grocery & Staples      → 0.30
```

Products belonging to categories preferred by the customer receive a higher category preference score.

---

# 🔢 Hybrid Recommendation Score

The three recommendation components are combined using the following formula:

```text
Hybrid Score =
    0.60 × Collaborative Score
  + 0.20 × Popularity Score
  + 0.20 × Category Preference Score
```

The products are then ranked according to their **Hybrid Score**.

The **Top 5 products** are returned as the final recommendations.

### Weight Distribution

| Component               |   Weight |
| ----------------------- | -------: |
| Collaborative Filtering |      60% |
| Product Popularity      |      20% |
| Category Preference     |      20% |
| **Total**               | **100%** |

---

# 🚫 Previously Purchased Products

The system checks the customer's purchase history and removes products that the customer has already purchased.

Therefore, the recommendation list focuses on **products that are new to the customer** rather than repeatedly recommending products they have already purchased.

---

# 📊 Dataset Structure

The project uses the following tables:

## Customer

Contains customer information.

| Column        | Description                |
| ------------- | -------------------------- |
| `customer_id` | Unique customer identifier |

---

## Product

Contains product information.

| Column         | Description               |
| -------------- | ------------------------- |
| `product_id`   | Unique product identifier |
| `product_name` | Name of the product       |
| `category`     | Product category          |

---

## Order

Connects customers with their orders.

| Column        | Description                   |
| ------------- | ----------------------------- |
| `order_id`    | Unique order identifier       |
| `customer_id` | Customer who placed the order |

---

## Transaction

Contains product-level transaction and quantity information.

| Column           | Description                   |
| ---------------- | ----------------------------- |
| `transaction_id` | Unique transaction identifier |
| `order_id`       | Associated order              |
| `product_id`     | Purchased product             |
| `quantity`       | Quantity purchased            |

---

## Rating

Contains rating information associated with orders.

| Column      | Description              |
| ----------- | ------------------------ |
| `rating_id` | Unique rating identifier |
| `order_id`  | Associated order         |

> **Note:** Rating information is available in the dataset but is not currently included in the Hybrid Recommendation Score.

---

## Delivery

Contains delivery information associated with orders.

| Column        | Description                |
| ------------- | -------------------------- |
| `delivery_id` | Unique delivery identifier |
| `order_id`    | Associated order           |

> **Note:** Delivery information is available in the dataset but is not currently included in the Hybrid Recommendation Score.

---

# 🔄 System Workflow

```text
                    Customer ID
                         │
                         ▼
              Customer Purchase History
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
  Collaborative     Popularity      Category
     Filtering         Score        Preference
       60%              20%             20%
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                   Hybrid Score
                         │
                         ▼
              Remove Purchased Products
                         │
                         ▼
                   Rank Products
                         │
                         ▼
                Top 5 Recommendations
                         │
                         ▼
                  Flask Web Application
```

---

# 🛠️ Technologies Used

## Programming Language

* **Python**

## Data Analysis & Machine Learning

* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Joblib**

## Web Development

* **Flask**
* **HTML**
* **CSS**

## Development Tools

* **Jupyter Notebook**
* **VS Code**
* **Anaconda**
* **Python**

---

# 📁 Project Structure

```text
Smart Grocery Predictor/
│
├── app.py
├── recommendation_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── Smart_Grocery_Project.ipynb
│
└── README.md
```

---

# 💾 Recommendation Model File

The project uses:

```text
recommendation_model.pkl
```

This file stores the precomputed objects required by the recommendation system.

It contains:

```text
customer_product
similarity_df
popularity_score
category_preference_df
product
```

These objects are loaded by the Flask application to generate recommendations.

The model objects are saved using **Joblib**.

### Model Creation

```python
import joblib

model_objects = {
    "customer_product": customer_product,
    "similarity_df": similarity_df,
    "popularity_score": popularity_score,
    "category_preference_df": category_preference_df,
    "product": product
}

joblib.dump(
    model_objects,
    "recommendation_model.pkl"
)
```

---

# 🌐 Web Application

The recommendation system is integrated with a **Flask web application**.

The user selects a customer ID, and the application generates personalized **Top 5 product recommendations**.

## Application Flow

```text
Select Customer ID
        ↓
Flask Backend
        ↓
Load Recommendation Components
        ↓
Collaborative Filtering
        ↓
Popularity Score
        ↓
Category Preference
        ↓
Hybrid Score
        ↓
Remove Previously Purchased Products
        ↓
Rank Products
        ↓
Display Top 5 Recommendations
```

---

# 🖥️ Web Application Features

* 👤 Customer selection
* 🛒 Personalized product recommendations
* ⭐ Top 5 recommendations
* 📊 Hybrid recommendation score
* 🏷️ Product category display
* 🚫 Exclusion of previously purchased products
* 🤖 Hybrid Machine Learning recommendation system
* 📈 Model performance display
* 📱 Responsive HTML/CSS interface

---

# 📊 Model Evaluation

The recommendation system was evaluated using a **holdout-based testing approach**.

A previously purchased product was hidden from the customer's purchase history.

The recommendation system was then tested to determine whether the hidden product appeared within the **Top 5 recommendations**.

## Results

| Metric                         | Result |
| ------------------------------ | -----: |
| Total Customers                |  8,417 |
| Customers with Recommendations |  8,417 |
| Recommendation Coverage        |   100% |
| Valid Test Customers           |    463 |
| Hits@5                         |    245 |
| Hit Rate@5                     | 52.92% |
| Precision@5                    | 10.58% |

---

# 🎯 Hit Rate@5

**Hit Rate@5** measures whether the relevant hidden product appears anywhere within the Top 5 recommendations.

The model achieved:

```text
Hit Rate@5 = 52.92%
```

This means the hidden product appeared in the Top 5 recommendations for:

```text
245 out of 463 valid test customers
```

---

# 📌 Precision@5

**Precision@5** measures how many of the recommended products are relevant to the customer.

The model achieved:

```text
Precision@5 = 10.58%
```

The evaluation uses a single hidden target product per valid test customer, so Precision@5 is calculated based on whether that relevant target appears among the five recommendations.

---

# 📈 Recommendation Coverage

The system generated recommendations for all customers in the customer-product matrix.

```text
Total Customers                    = 8,417
Customers with Recommendations    = 8,417
Recommendation Coverage            = 100%
```

This indicates that the system was able to generate recommendations for every customer included in the recommendation matrix.

---

# 🛒 Example Recommendation

Example Top 5 recommendations generated by the system:

| Rank | Product ID | Product                  | Category            | Hybrid Score |
| ---: | ---------- | ------------------------ | ------------------- | -----------: |
|    1 | P00268     | Fresh Eggs 500ml         | Baby Care           |     0.780253 |
|    2 | P00566     | Green Namkeen 1kg        | Dairy & Bakery      |     0.690556 |
|    3 | P00923     | Smart Namkeen 500g       | Fruits & Vegetables |     0.652778 |
|    4 | P00867     | Pure Juice 500g          | Dairy & Bakery      |     0.651875 |
|    5 | P01122     | Smart Floor Cleaner 500g | Baby Care           |     0.610593 |

> **Note:** The exact recommendations vary depending on the selected customer.

---

# 🚀 How to Run the Project

## Step 1 — Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project folder:

```bash
cd "Smart Grocery Predictor"
```

---

## Step 2 — Install Dependencies

Install the required Python libraries:

```bash
python -m pip install pandas numpy scikit-learn flask joblib pyarrow
```

---

## Step 3 — Run the Flask Application

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

---

## Step 4 — Open the Application

Open your web browser and visit:

```text
http://127.0.0.1:5000
```

Then:

1. Select a Customer ID.
2. Click **Recommend Products**.
3. The system generates personalized recommendations.
4. The **Top 5 products** are displayed.

---

# 🔮 Future Enhancements

The project can be further improved by adding:

* 🖼️ Product images
* 🛒 Customer purchase history
* 🔎 Product search
* 💡 Recommendation explanations
* ⭐ Rating-based recommendations
* 🚚 Delivery-performance information
* 🤖 Advanced recommendation algorithms
* 🧠 Deep Learning-based recommendation models
* 🔄 Real-time user feedback
* 👤 User login and personalized profiles
* ☁️ Cloud deployment
* 🧪 A/B testing of recommendation strategies

---

# ⚠️ Current Limitations

* The current recommendation score primarily uses purchase behavior, product popularity, and category preference.
* Rating information is not currently included in the Hybrid Recommendation Score.
* Delivery information is not currently included in the Hybrid Recommendation Score.
* The current evaluation uses a hidden previously purchased product as the test target.
* Recommendation quality depends on the available transaction data.
* The `recommendation_model.pkl` file is required by the Flask application.
* The recommendation system is based on historical purchasing behavior and may not capture sudden changes in customer preferences.

---

# 🎓 Project Highlights

## 🤖 Machine Learning

* Collaborative Filtering
* Customer Similarity
* Popularity-based Recommendation
* Category Preference
* Hybrid Recommendation

## 📊 Data Analysis

* Customer purchasing behavior
* Product popularity
* Category preferences
* Transaction analysis

## 🌐 Web Development

* Flask backend
* HTML frontend
* CSS styling
* Machine Learning model integration

## 📈 Evaluation

* Recommendation Coverage
* Hit Rate@5
* Precision@5

---

# 👥 Team

**Team Size:** 6 Members

The project combines skills in:

* Data Analysis
* Machine Learning
* Recommendation Systems
* Python
* Flask Web Development
* HTML & CSS

---

# 📄 Conclusion

**Smart Grocery Predictor** demonstrates how customer transaction data can be used to create personalized grocery product recommendations.

The system combines:

```text
60% Collaborative Filtering
        +
20% Product Popularity
        +
20% Category Preference
        =
Hybrid Recommendation Score
```

The system then ranks candidate products and returns the **Top 5 personalized recommendations**, while removing products that the customer has already purchased.

The final system integrates the Machine Learning recommendation engine with a **Flask web application** using HTML and CSS.

## 🏆 Model Performance

| Metric                  | Performance |
| ----------------------- | ----------: |
| Recommendation Coverage |    **100%** |
| Hit Rate@5              |  **52.92%** |
| Precision@5             |  **10.58%** |

---

# ⭐ Technologies

```text
Python
Pandas
NumPy
Scikit-learn
Joblib
Flask
HTML
CSS
Jupyter Notebook
```

---

## 🔑 Key Idea

> **Smart Grocery Predictor learns from customer purchasing behavior and combines similar-customer behavior, product popularity, and category preferences to recommend products that the customer is most likely to purchase next.**
