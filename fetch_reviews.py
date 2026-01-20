import steamreviews
import duckdb

def create_table(connection, table_name):
    """
    Create table if not exists in database
    :param db_connection: duckdb.Connection
    """
    connection.execute("""
    CREATE TABLE IF NOT EXISTS %s (
        id STRING PRIMARY KEY,
        recommendation_id STRING,
        author_steamid STRING,
        author_num_games_owned INTEGER,
        author_num_reviews INTEGER,
        author_playtime_forever INTEGER,
        author_playtime_last_two_weeks INTEGER,
        author_playtime_at_review INTEGER,
        author_last_played BIGINT,
        language STRING,
        review STRING,
        timestamp_created BIGINT,
        timestamp_updated BIGINT,
        voted_up BOOLEAN,
        votes_up INTEGER,
        votes_funny INTEGER,
        weighted_vote_score DOUBLE,
        comment_count INTEGER,
        steam_purchase BOOLEAN,
        received_for_free BOOLEAN,
        written_during_early_access BOOLEAN,
        primarily_steam_deck BOOLEAN
    )
    """ % table_name)

def ingest_reviews(db_connection, app_id, table_name):
    """

    :param db_connection: duckdb.Connection
    :return:
    """

    results, query_count = steamreviews.download_reviews_for_app_id(app_id)
    print(f"Finished running {query_count} queries")

    reviews = results.get("reviews")
    inserted = 0
    for index, (review_id, review_data) in enumerate(reviews.items(), start=1):
        author = review_data.get("author", {})
        try:
            db_connection.execute("""
                INSERT INTO %s VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO NOTHING
            """ % table_name, (
                review_id,
                review_data.get("recommendation_id"),
                author.get("steamid"),
                author.get("num_games_owned", 0),
                author.get("num_reviews", 0),
                author.get("playtime_forever", 0),
                author.get("playtime_last_two_weeks", 0),
                author.get("playtime_at_review", 0),
                author.get("last_played", 0),
                review_data.get("language"),
                review_data.get("review"),
                review_data.get("timestamp_created"),
                review_data.get("timestamp_updated"),
                review_data.get("voted_up"),
                review_data.get("votes_up", 0),
                review_data.get("votes_funny", 0),
                review_data.get("weighted_vote_score", 0.0),
                review_data.get("comment_count", 0),
                review_data.get("steam_purchase", False),
                review_data.get("received_for_free", False),
                review_data.get("written_during_early_access", False),
                review_data.get("primarily_steam_deck", False),
            ))
            inserted += 1
        except Exception as e:
            print(f"Error inserting review {review_id}: {e}")

        if index % 1000 == 0:
            print(f"Processed {index} reviews so far...")

    print(f"Inserted {inserted} reviews into the database")

if __name__ == "__main__":

    db_connection = duckdb.connect("reviews.duckdb")

    # ff7 rebirth - 27476 reviews
    ff7rebirth_app_id = 2909400
    ff7rebirth_table_name = """ff7rebirth_reviews_15_01_2025""" # correct year is 2026 - my mistake on table name
    create_table(db_connection, ff7rebirth_table_name)
    ingest_reviews(db_connection, app_id=ff7rebirth_app_id, table_name=ff7rebirth_table_name)
    db_connection.execute("""
    COPY (SELECT * FROM ff7rebirth_reviews_15_01_2025) TO 'ff7rebirth_output.csv' (HEADER, DELIMITER ',');""")

    # ff7 remake - 43096 reviews
    ff7remake_app_id = 1462040
    ff7remake_table_name = """ff7remake_reviews_15_01_2025"""; # correct year is 2026 - my mistake on table name
    create_table(db_connection, ff7remake_table_name)
    ingest_reviews(db_connection, app_id=ff7remake_app_id, table_name=ff7remake_table_name)
    db_connection.execute("""
    COPY (SELECT * FROM ff7remake_reviews_15_01_2025) TO 'ff7remake_output.csv' (HEADER, DELIMITER ',');""")