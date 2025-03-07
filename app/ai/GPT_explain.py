from openai import OpenAI
import json 
def explain_GPT(apiKey, answerLetter, question, possibleAnswers):
    
    client = OpenAI(api_key =  apiKey)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Explain why Answer {answerLetter} is the right answer for this question {question}, given those choices {possibleAnswers}. Explain also why the other answers are wrong. Keep it short. Format your answer this way : first, the sentence 'Why answer x is correct' with the explaination, then 'Context' folowed by a short explaination of the context, then 'Why the other answers are wrong' followed by a short explaination. Format your answer in HTML"
            }
        ]
    )
    return completion.choices[0].message.content


# Main flow to query chatgpt and save output to a new json
def main(apiKey):
    AI_json = []
    try:
        with open("app/scraper/scraperOutput/questions.json", "r", encoding="utf-8") as file:
            questions = json.load(file)
            # For each element, ask gpt to elaborate
            for element in questions:
                # Copy the question element
                new_question_object = element
                
                GPT_explaination = explain_GPT(apiKey, element["answer"], element["question"], element["sampleAnswers"])
                # Add GPT output to a new JSON
                new_question_object["ai_explaination"] = GPT_explaination
                AI_json.append(new_question_object)
        
        # Write back to JSON file
        with open("app/ai/output/ai_output.json", "w", encoding="utf-8") as file:
            json.dump(AI_json, file, ensure_ascii=False, indent=4)
                    
                        
# Read  credentiales
with open("params.json", "r", encoding="utf-8") as paramsFile:
                credentials = json.load(paramsFile)
                main(credentials["chatGptApiKey"])
                