from flask import Flask, render_template

app = Flask(__name__)


players_data = [
    {
        "name": "Virat Kohli",
        "country": "India",
        "role": "Batsman",
        "matches": 292,
        "runs": 13848,
        "average": 58.67,
        "strike_rate": 93.54
    },
    {
        "name": "Rohit Sharma",
        "country": "India",
        "role": "Batsman",
        "matches": 275,
        "runs": 11200,
        "average": 48.50,
        "strike_rate": 92.43
    },
    {
        "name": "Jasprit Bumrah",
        "country": "India",
        "role": "Bowler",
        "matches": 150,
        "runs": 250,
        "average": 12.50,
        "strike_rate": 85.00
    },
    {
        "name": "Babar Azam",
        "country": "Pakistan",
        "role": "Batsman",
        "matches": 190,
        "runs": 9500,
        "average": 56.80,
        "strike_rate": 88.20
    },
    {
        "name": "Kane Williamson",
        "country": "New Zealand",
        "role": "Batsman",
        "matches": 170,
        "runs": 8500,
        "average": 54.30,
        "strike_rate": 81.70
    },
    {
        "name": "Pat Cummins",
        "country": "Australia",
        "role": "Bowler",
        "matches": 180,
        "runs": 1200,
        "average": 18.40,
        "strike_rate": 75.60
    }
]

teams_data = [
    {
        "name": "India",
        "short_name": "IND",
        "captain": "Rohit Sharma",
        "matches": 120,
        "wins": 78
    },
    {
        "name": "Australia",
        "short_name": "AUS",
        "captain": "Pat Cummins",
        "matches": 115,
        "wins": 72
    },
    {
        "name": "England",
        "short_name": "ENG",
        "captain": "Jos Buttler",
        "matches": 110,
        "wins": 64
    },
    {
        "name": "New Zealand",
        "short_name": "NZ",
        "captain": "Kane Williamson",
        "matches": 105,
        "wins": 61
    },
    {
        "name": "Pakistan",
        "short_name": "PAK",
        "captain": "Babar Azam",
        "matches": 108,
        "wins": 59
    },
    {
        "name": "South Africa",
        "short_name": "SA",
        "captain": "Temba Bavuma",
        "matches": 100,
        "wins": 55
    }
]
matches_data = [
    {
        "team1": "India",
        "team2": "Australia",
        "team1_score": "285/6",
        "team2_score": "276/9",
        "result": "India won by 9 runs",
        "player_of_match": "Virat Kohli"
    },
    {
        "team1": "England",
        "team2": "New Zealand",
        "team1_score": "312/7",
        "team2_score": "298/8",
        "result": "England won by 14 runs",
        "player_of_match": "Joe Root"
    },
    {
        "team1": "Pakistan",
        "team2": "South Africa",
        "team1_score": "267/8",
        "team2_score": "268/6",
        "result": "South Africa won by 4 wickets",
        "player_of_match": "Kagiso Rabada"
    }
]
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/players")
def players():
    return render_template("players.html", players=players_data)
@app.route("/players/<player_name>")
def player_profile(player_name):

    for player in players_data:
        if player["name"].lower().replace(" ", "-") == player_name.lower():
            return render_template(
                "player_profile.html",
                player=player
            )

    return "Player not found", 404
@app.route("/teams")
def teams():
    return render_template("teams.html", teams=teams_data)
@app.route("/matches")
def matches():
    return render_template("matches.html", matches=matches_data)

if __name__ == "__main__":
    app.run(debug=True)