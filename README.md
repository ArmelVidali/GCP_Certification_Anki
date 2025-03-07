# GCP certification scraper

Small project to scrape exams questions for GCP certification from various websites

Generates a JSON with questions and answers, and sets up ChatGPT querying to give context and explaination for each question, final goal being to insert the questions, answers and explaination into an Anki deck like this project <a>**https**://github.com/ArmelVidali/derja_ninja_scraper</a>

# Setup

Create a virtual environment

```
python -m venv GCP_env
```

Activate the environment

#### Windows

```
GCP_env\Scripts\activate
```

#### MacOS/Linux

```
source myenv/GCP_env/activate
```

#### Install dependencies

```
pip install requirements.txt
```

#### Add a params.json file at the directory root with credentials

```
{
  "examTopicEmail": "email",
  "examTopicPassword": "pwd",
  "chatGptApiKey": "yourGptApiKey"
}

```

# Run Scripts

#### To scrape data

```
python app/scraper/examsTopic/main.py
```

#### To query chat GPT to explain the questions from the generated JSON

```
python app/ai/GPT_explain.py
```

Change the query on `gpt_explain.py` to custom the query to your neeeds (more depth, translation ...)

### TODO

---

Still needs to add a Anki script to add GPT explained JSON into a deck, like this project <a>**https**://github.com/ArmelVidali/derja_ninja_scraper</a>
