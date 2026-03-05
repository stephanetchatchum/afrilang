AfriLang 🌍

Digitising African languages, one word at a time.

AfriLang is a command-line tool built to digitise African languages that mainstream technology has ignored. With over 2,000 languages spoken across the continent, the vast majority have no presence in software, no translation tools, and no digital resources. When our languages don't exist in technology, we are forced to communicate, learn, and build on someone else's terms. AfriLang is a step toward changing that.

Why This Exists
Google Translate supports 133 languages. There are over 2,000 African languages. Most of them don't exist in any technology.
AfriLang starts with Twi (Ghana) and is designed to grow — one language, one word at a time. The belief behind this project is simple: technology should reflect the people who use it, and African languages deserve to exist in the digital world just as much as any other.

Features

Translate — type an English word and get the translation in a supported African language
Pronunciation guide — know how to actually say the word
Example sentences — see the word used in context
Quiz mode — test yourself on words you have learned
Contribute — add new words to the dictionary directly from the CLI
Multi-language — switch between languages in one session


Languages Currently Supported
LanguageRegionWordsTwiGhanaGrowing

More languages coming. Contributions welcome.


Getting Started
Requirements: Python 3.6+
bash# Clone the repository
git clone https://github.com/stephanetchatchum/afrilang.git
cd afrilang

# Run the app
python afrilang.py
No external libraries needed. Just Python.

How to Use
afrilang > translate hello
afrilang > list
afrilang > quiz
afrilang > add
afrilang > switch twi
afrilang > languages
afrilang > help
afrilang > exit

Project Structure
afrilang/
│
├── afrilang.py        # Main CLI application
├── data/
│   └── twi.json       # Twi (Ghana) language dictionary
├── tests/
│   └── test_afrilang.py
└── README.md

How to Add a New Language

Create a new JSON file in the data/ folder — e.g. yoruba.json
Follow this structure:

json{
  "language": "Yoruba",
  "region": "Nigeria",
  "words": {
    "hello": {
      "translation": "Ẹ káàbọ̀",
      "pronunciation": "eh-kah-boh",
      "example": "Ẹ káàbọ̀ — Welcome"
    }
  }
}

Run python afrilang.py and switch to it with switch yoruba


Roadmap

 CLI — translate, list, quiz, contribute, multi-language
 Twi (Ghana) starter dictionary
 Yoruba (Nigeria) dictionary
 Swahili (East Africa) dictionary
 Flask web interface
 Audio pronunciation via text-to-speech
 Public REST API
 Browser extension


Contributing
This project grows through community input. If you speak an African language and want to help digitise it, open a pull request or use the add command in the CLI.
Every word added is a small act of technological independence.

Built By
Stephane Tchatchum
Software Engineering Student — African Leadership University, Kigali
Mission: Contribute to Africa's technological independence

GitHub: github.com/stephanetchatchum
LinkedIn: linkedin.com/in/stephane-tchatchum-7b4666383


License
MIT — free to use, share, and build on.
