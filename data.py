import requests

parameters = {
    "limit": 10,
    "difficult": "medium",
    "type": "text_choice",
}

response = requests.get("https://the-trivia-api.com/v2/questions")
response.raise_for_status()
question_data = response.json()
print(question_data)