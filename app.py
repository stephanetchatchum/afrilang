from flask import Flask, render_template
import json
app = Flask(__name__)

with open("data/twi.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@app.route("/translate/<word>")
def translate(word):
    word = word.lower()
    if word in data:
        return {"Word": word, "translation": data[word]}
    else:
        return {"Error": "Word not found"}
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
