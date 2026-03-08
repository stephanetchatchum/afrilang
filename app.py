from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os
import json
import random
app = Flask(__name__)

with open("data/twi.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pronounce/<word>")
def pronounce(word):
    tts = gTTS(text=word, lang="en")
    filepath = f"static/{word}.mp3"
    tts.save(filepath)
    return send_file(filepath, mimetype="audio/mpeg")

@app.route("/translate", methods=["POST"])
def translate():
    word = request.form["word"].lower()
    if word in data:
        result = data[word]
    else:
        result = "Word not found"
    return render_template("index.html", result=result)


@app.route("/list")
def list_words():
    return render_template("list.html", data=data)

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    message = None
    if request.method == "POST":
        english = request.form["english"]
        question = data[english]
        ans = request.form["ans"].lower()
        if ans == english:
            message = "Correct ✅"
        else:
            message = f"Wrong, the meaning is '{english}'"
    else:
        english = random.choice(list(data.keys()))
        question = data[english]
    return render_template("quiz.html", question=question, english=english, message=message)

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