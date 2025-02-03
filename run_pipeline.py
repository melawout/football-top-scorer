from check_rate_limits import check_rate_limits
from get_top_scorers import get_top_scorers
from transform_top_scorer_data import process_top_scorer, create_dataframe
from db_operations import create_db_connection, create_table, insert_into_table


def run_data_pipeline(host, user, password, db_name, url, headers, params):
    check_rate_limits(url, headers)

    data = get_top_scorers(url, headers, params)

    if data and "response" in data and data["response"]:
        top_scorers = process_top_scorer(data)
        df = create_dataframe(top_scorers)

        print(df.to_string(index=False))

    else:
        print("No data available or an error occurred ❌")

    db_connection = create_db_connection(host, user, password, db_name)

    if db_connection is not None:
        create_table(db_connection)
        df = create_dataframe(top_scorers)
        insert_into_table(db_connection, df)
