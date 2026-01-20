import duckdb
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "reviews.duckdb")


def get_reviews(language=None, limit=None, table="ff7rebirth_reviews_15_01_2025"):
    """
    Get reviews for a given language in database
    :param language: language code
    :param limit: number of reviews to return
    :param table: table name
    :return: dataframe of reviews
    """

    connection = duckdb.connect(DB_PATH)
    query = f"SELECT * FROM {table}"
    conditions = []
    if language:
        conditions.append(f"language = '{language}'")
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    if limit:
        query += f" LIMIT {limit}"
    return connection.execute(query).fetchdf()
