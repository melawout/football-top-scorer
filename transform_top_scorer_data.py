from datetime import datetime
import pandas as pd


def process_top_scorer(data):
    top_scorers = []

    for scorer_data in data["response"]:
        statistics = scorer_data["statistics"][0]

        player = scorer_data["player"]
        player_name = player["name"]
        club_name = statistics["team"]["name"]
        total_goals = int(statistics["goals"]["total"])
        penalty_goals = int(statistics["penalty"]["scored"])
        assists = (
            int(statistics["goals"]["assists"]) if statistics["goals"]["assists"] else 0
        )
        matches_played = int(statistics["games"]["appearences"])
        minutes_played = int(statistics["games"]["minutes"])
        dob = datetime.strptime(player["birth"]["date"], "%Y-%m-%d")
        age = (datetime.now() - dob).days // 365

        top_scorers.append(
            {
                "player": player_name,
                "club": club_name,
                "total_goals": total_goals,
                "penalty_goals": penalty_goals,
                "assists": assists,
                "matches": matches_played,
                "mins": minutes_played,
                "age": age,
            }
        )

    return top_scorers


def create_dataframe(top_scorers):
    df = pd.DataFrame(top_scorers)

    df.sort_values(
        by=["total_goals", "assists"], ascending=[False, False], inplace=True
    )

    df.reset_index(drop=True, inplace=True)

    df["position"] = df["total_goals"].rank(method="dense", ascending=False).astype(int)

    df = df[
        [
            "position",
            "player",
            "club",
            "total_goals",
            "penalty_goals",
            "assists",
            "matches",
            "mins",
            "age",
        ]
    ]

    return df
