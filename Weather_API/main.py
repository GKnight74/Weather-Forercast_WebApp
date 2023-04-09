from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/api/vi/<station>/<date>")
def about(station, date):
    df = pandas. read_csv("")
    temperature = df.
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)