from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import joblib

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/CustomerSegmentation"
# mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form", methods=["POST"])
def brain():
    try:
        # Extract form data from request
        education = float(request.form["education"])
        marital_status = int(request.form["marital_status"])
        income = float(request.form["income"])
        kidhome = int(request.form["kidhome"])
        teenhome = int(request.form["teenhome"])
        recency = int(request.form["recency"])
        mnt_wines = float(request.form["mnt_wines"])
        mnt_fruits = float(request.form["mnt_fruits"])
        mnt_meat_products = float(request.form["mnt_meat_products"])
        mnt_fish_products = float(request.form["mnt_fish_products"])
        mnt_sweet_products = float(request.form["mnt_sweet_products"])
        mnt_gold_prods = float(request.form["mnt_gold_prods"])
        num_deals_purchases = int(request.form["num_deals_purchases"])
        num_web_purchases = int(request.form["num_web_purchases"])
        num_catalog_purchases = int(request.form["num_catalog_purchases"])
        num_store_purchases = int(request.form["num_store_purchases"])
        num_web_visits_month = int(request.form["num_web_visits_month"])
        age = int(request.form["age"])
        years_customer = int(request.form["years_customer"])
        total_expenses = float(request.form["total_expenses"])
        total_acc_cmp = int(request.form["total_acc_cmp"])

        # Prepare data for the model
        values = [education, marital_status,
            income, kidhome, teenhome, recency, mnt_wines, mnt_fruits,
            mnt_meat_products, mnt_fish_products, mnt_sweet_products,
            mnt_gold_prods, num_deals_purchases, num_web_purchases,
            num_catalog_purchases, num_store_purchases, num_web_visits_month,
            age, years_customer, total_expenses, total_acc_cmp
        ]
        arr = [values]

        # customer_data = {
        #     "education": education,
        #     "marital_status": marital_status,
        #     "income": income,
        #     "kidhome": kidhome,
        #     "teenhome": teenhome,
        #     "recency": recency,
        #     "mnt_wines": mnt_wines,
        #     "mnt_fruits": mnt_fruits,
        #     "mnt_meat_products": mnt_meat_products,
        #     "mnt_fish_products": mnt_fish_products,
        #     "mnt_sweet_products": mnt_sweet_products,
        #     "mnt_gold_prods": mnt_gold_prods,
        #     "num_deals_purchases": num_deals_purchases,
        #     "num_web_purchases": num_web_purchases,
        #     "num_catalog_purchases": num_catalog_purchases,
        #     "num_store_purchases": num_store_purchases,
        #     "num_web_visits_month": num_web_visits_month,
        #     "age": age,
        #     "years_customer": years_customer,
        #     "total_expenses": total_expenses,
        #     "total_acc_cmp": total_acc_cmp
        #     }


        # mongo.db.CustomerSeg.insert_one(customer_data)
        # Load model
        model = joblib.load("customer_segmentation_model.pkl")

        # Make prediction
        prediction = model.predict(arr)

        # Return prediction result
        if prediction[0] == 0:
            result_message = "Segment 0 (few opportunities)"
        else:
            result_message = "Segment 1 (well-off)"
        return render_template("result.html", result_message=result_message)

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
