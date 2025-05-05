from flask import Flask, jsonify
from collect import collect_metrics

app = Flask(__name__)

@app.route("/metrics")
def metrics():
	data = collect_metrics()
	return jsonify(data)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')
