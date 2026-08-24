from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


# -----------------------------------
# LOAD MODEL
# -----------------------------------

model = joblib.load("recommendation_model.pkl")

customer_product = model["customer_product"]
similarity_df = model["similarity_df"]
popularity_score = model["popularity_score"]
category_preference_df = model["category_preference_df"]
product = model["product"]


# -----------------------------------
# RECOMMENDATION FUNCTION
# -----------------------------------

def recommend_products(customer_id, top_n=5):

    if customer_id not in customer_product.index:
        return None

    # Collaborative Filtering
    similar_customers = (
        similarity_df[customer_id]
        .drop(customer_id)
        .sort_values(ascending=False)
        .head(10)
    )

    collaborative_score = customer_product.loc[
        similar_customers.index
    ].T.dot(similar_customers)

    # Remove products already purchased
    purchased_products = customer_product.loc[
        customer_id
    ]

    purchased_products = purchased_products[
        purchased_products > 0
    ].index

    collaborative_score = collaborative_score.drop(
        purchased_products,
        errors="ignore"
    )

    # Normalize collaborative score
    if collaborative_score.max() > 0:
        collaborative_score = (
            collaborative_score /
            collaborative_score.max()
        )

    # Popularity
    popularity = popularity_score.reindex(
        collaborative_score.index
    ).fillna(0)

    # Category Preference
    customer_categories = (
        category_preference_df[
            category_preference_df["customer_id"] == customer_id
        ]
        .set_index("category")["category_score"]
    )

    product_categories = (
        product[
            ["product_id", "category"]
        ]
        .set_index("product_id")
    )

    category_score = (
        product_categories
        .loc[
            collaborative_score.index,
            "category"
        ]
        .map(customer_categories)
        .fillna(0)
    )

    # Hybrid Score
    hybrid_score = (
        0.6 * collaborative_score
        + 0.2 * popularity
        + 0.2 * category_score
    )

    # Top recommendations
    recommendations = (
        hybrid_score
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    recommendations.columns = [
        "product_id",
        "hybrid_score"
    ]

    recommendations = recommendations.merge(
        product[
            [
                "product_id",
                "product_name",
                "category"
            ]
        ],
        on="product_id",
        how="left"
    )

    return recommendations.to_dict("records")


# -----------------------------------
# HOME PAGE
# -----------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = None
    selected_customer = None

    if request.method == "POST":

        selected_customer = request.form["customer_id"]

        recommendations = recommend_products(
            selected_customer,
            5
        )

    customers = customer_product.index.tolist()

    return render_template(
        "index.html",
        customers=customers,
        recommendations=recommendations,
        selected_customer=selected_customer
    )


# -----------------------------------
# RUN APPLICATION
# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)