from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return f"Hello! Container ID: {socket.gethostname()}"


if __name__ == "__main__":
    app.run(debug=True)
