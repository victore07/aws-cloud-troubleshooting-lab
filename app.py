from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AWS Cloud Troubleshooting Lab is running."

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/debug")
def debug():
    return jsonify({
        "app": "aws-cloud-troubleshooting-lab",
        "version": "1.0",
        "environment": "dev"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)