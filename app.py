from flask import Flask, render_template, request
import json
app = Flask(__name__)

with open("data/twi.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@app.route("/translate", methods=["POST"])
def translate():
    word = request.form["word"].lower()
    if word in data:
        result = data[word]
    else:
        result = "Word not found"
    return render_template("index.html", result=result)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/list")
def list():
    return render_template("list.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)