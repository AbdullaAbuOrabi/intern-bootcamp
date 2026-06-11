import logging
from datetime import datetime

import pandas as pd
import psycopg2
import joblib


logging.basicConfig(
    filename="batch_prediction.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DB_NAME = "intern_db"
DB_USER = "postgres"
DB_PASSWORD = "Abdulla11-11"
DB_HOST = "localhost"
DB_PORT = "5432"


def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )


MODEL_PATH = "best_model.pkl"

model = joblib.load(MODEL_PATH)


def load_customer_features():
    conn = get_connection()

    query = """
        SELECT
            c.customer_id,

            COUNT(o.order_id) AS num__total_orders,

            COALESCE(SUM(t.amount), 0) AS num__total_spent,

            COALESCE(AVG(t.amount), 0) AS num__average_order_amount,

            COUNT(
                CASE
                    WHEN t.payment_status = 'paid' THEN 1
                END
            ) AS num__successful_payments,

            CASE WHEN c.city = 'Abu Dhabi' THEN 1 ELSE 0 END AS "cat__city_Abu Dhabi",
            CASE WHEN c.city = 'Ajman' THEN 1 ELSE 0 END AS "cat__city_Ajman",
            CASE WHEN c.city = 'Dubai' THEN 1 ELSE 0 END AS "cat__city_Dubai",
            CASE WHEN c.city = 'Sharjah' THEN 1 ELSE 0 END AS "cat__city_Sharjah"

        FROM customers c

        LEFT JOIN orders o
            ON c.customer_id = o.customer_id

        LEFT JOIN transactions t
            ON o.order_id = t.order_id

        GROUP BY c.customer_id, c.city

        ORDER BY c.customer_id;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df


def save_predictions(results_df):
    conn = get_connection()
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO customer_predictions
        (customer_id, prediction, probability, prediction_timestamp)
        VALUES (%s, %s, %s, %s);
    """

    for _, row in results_df.iterrows():
        cursor.execute(
            insert_query,
            (
                int(row["customer_id"]),
                int(row["prediction"]),
                float(row["probability"]),
                row["prediction_timestamp"]
            )
        )

    conn.commit()
    cursor.close()
    conn.close()


def run_batch_prediction():
    logging.info("Batch prediction started.")

    features_df = load_customer_features()

    if features_df.empty:
        logging.warning("No customer records found for prediction.")
        return

    customer_ids = features_df["customer_id"]

    feature_columns = [
        "num__total_orders",
        "num__total_spent",
        "num__average_order_amount",
        "num__successful_payments",
        "cat__city_Abu Dhabi",
        "cat__city_Ajman",
        "cat__city_Dubai",
        "cat__city_Sharjah"
    ]

    X = features_df[feature_columns]

    predictions = model.predict(X)

    probabilities = model.predict_proba(X)[:, 1]

    results_df = pd.DataFrame({
        "customer_id": customer_ids,
        "prediction": predictions,
        "probability": probabilities,
        "prediction_timestamp": datetime.now()
    })

    save_predictions(results_df)

    logging.info("Batch prediction completed successfully.")
    logging.info(f"Total customers processed: {len(results_df)}")
    logging.info(f"Predicted positive cases: {sum(predictions)}")
    logging.info(
        f"Predicted negative cases: {len(predictions) - sum(predictions)}")


if __name__ == "__main__":
    run_batch_prediction()
