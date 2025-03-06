import json
import os
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def downloadQuestions(driver, soupPage, file_path="app/scraper/scraperOutput/questions12.json"):
    print(os.getcwd())
    """ 
    Downloads questions, optionally taking a screenshot if an image is present
    and appends them to a JSON file.
    """
    questions_list = []

    # Find all exam question cards
    results = soupPage.find_all('div', class_='card exam-question-card')
    

    if results:
        for questionCard in results:
            question = questionCard.find("p", class_="card-text")
            sampleAnswers = questionCard.find_all(
                "li", class_="multi-choice-item")

            # Extract text safely
            question_text = question.getText(strip=True) if question else "No question found"
            
            answers_text = []
            for answer in sampleAnswers:
                answers_text.append(answer.getText(strip=True))

            # Check if an image is present and take a screenshot
            image_path = None
            image_element = questionCard.find("img", class_="in-exam-image")
            
            # Reveal final answer
            questionCard.find("a", class_ = "btn btn-primary reveal-solution d-print-none")
            answer = questionCard.find("span", class_ = "correct-answer").text.strip()
            
            if image_element:
                image_path = "https://www.examtopics.com" + image_element['src']

            questions_list.append({
                "question": question_text,
                "sampleAnswers": answers_text,
                "image": image_path,
                "answer" : answer
            })

    # Load existing JSON data (if file exists)
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                existing_data = json.load(file)
                if not isinstance(existing_data, list):
                    existing_data = []
        except (json.JSONDecodeError, FileNotFoundError):
            existing_data = []
    else:
        existing_data = []

    # Append new questions
    existing_data.extend(questions_list)

    # Write back to JSON file
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

