import os
from dotenv import load_dotenv
from run_pipeline import run_data_pipeline


def main():
    # Load environment variables
    load_dotenv()

    # Load API key
    RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
    url = os.getenv("URL")

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    }

    # league 39 = premier league
    params = {"league": "39", "season": "2023"}

    host = ("localhost",)
    database = (os.getenv("MYSQL_DATABASE"),)
    user = (os.getenv("MYSQL_USER"),)
    password = os.getenv("MYSQL_PASSWORD")

    run_data_pipeline(host[0], user[0], password, database[0], url, headers, params)


if __name__ == "__main__":
    main()
