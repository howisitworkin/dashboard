import webbrowser
from threading import Timer
from flask import Flask, jsonify, render_template
from metrics import get_metrics

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("homework.html")

@app.route("/metrics")
def metrics():
    data = get_metrics()
    return jsonify(data)

if __name__ == "__main__":
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(debug=True)

