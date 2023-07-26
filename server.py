from flask import Flask
from ranking_api import rankingApi

app = Flask(__name__)

@app.route("/api/ranking")
def apiRanking():
    return rankingApi()

if __name__ == '__main__':
    app.run(port=5000)