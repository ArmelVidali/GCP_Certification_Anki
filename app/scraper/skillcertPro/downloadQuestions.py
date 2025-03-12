import json
import os
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def downloadQuestions(driver, soupPage, file_path="app/scraper/skillcertPro/scraperOutput/output_dev.json"):
    print(os.getcwd())
    """ 
    Downloads questions, optionally taking a screenshot if an image is present
    and appends them to a JSON file.
    """
    questions_list = []

    # Find all exam question cards
    results = soup.find_all('div', class_=re.compile(r'wp_pro_legend_\d+'))    

    if results:
        for questionNumberBtn in results:
            #Get the question text
            question = soup.find("div", class_='wpProQuiz_question_text')
            questionText = question.getText(strip=True)
            
            #Get the possible answers            
            possibleAnswers = soup.find('input', class_='wpProQuiz_questionListItem')    
            answers_text = []            
            for answer in possibleAnswers:
                answers_text.append(answer.getText(strip=True))
            
            # Click on check to show the solution
            checkAnswerBtn = soup.find('input', class_='wpProQuiz_button wpProQuiz_QuestionButton')    
            checkAnswerBtn.click()
            
            #Get the solution text
            solution = soup.find("div",class_='wpProQuiz_unattempted')
            solutionText = solution.find("p").getText(strip=True)


            # Check if an image is present and save the src url
            has_image = solution.find("img") is not None
            image_src = image["src"] if image else None
            
            questions_list.append({
                "question": questionText,
                "sampleAnswers": answers_text,
                "image": image_src,
                "answer" : solutionText
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

