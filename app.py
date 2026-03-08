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

@app.route("/contribute", methods=["GET", "POST"])
def contribute():
    message = None
    if request.method == "POST":
        new_word = request.form["word"].lower()
        translation = request.form["translation"].lower()
        if new_word in data:
            message = "Word already exists."
        else:
            data[new_word] = translation
            with open("data/twi.json", "w", encoding="utf-8") as f:
                json.dump(data, f)
            message = f"'{new_word}' added successfully. Thank you"
    return render_template("contribute.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)