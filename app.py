from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "This is my first Kubernetes project! 🚀"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
