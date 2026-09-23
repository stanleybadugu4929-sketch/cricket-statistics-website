from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Cricket Statistics and Match Analysis Website"


if __name__ == "__main__":
    app.run(debug=True)