import json
import os
import random

def read_question_bank():
    f = open('helloWorld/data/questionbank.json')
    return json.load(f)

def return_question_id(question_asked, num_questions):
    question_id = 0
    while question_id in question_asked:
       question_id = random.randint(1, num_questions)
    return question_id

def get_response():
    response = ""
    while response not in ['A', 'B', 'C', 'D']:
          response = input("Please enter your answer ---> ")
          response = response.upper()
    return response

def print_question(QuestionSet, question_id):
    print("-"*20)
    print("Question --> {}".format(QuestionSet[str(question_id)]['Question']))
    print("Choices")
    for choice in QuestionSet[str(question_id)]['Choices']:
        print("{} : {}".format(choice, QuestionSet[str(question_id)]['Choices'][choice]))

def check_answer(QuestionSet, question_id, response):
    if response == QuestionSet[str(question_id)]['Answer']:
        return True
    return False

def ask_question(question_asked, QuestionSet, score):
    question_id = return_question_id(question_asked, len(QuestionSet))
    question_asked.append(question_id)
    print_question(QuestionSet, question_id)
    response = get_response()
    if check_answer(QuestionSet, question_id, response):
        print("Your response is correct")
        score = score + 1
    else:
        print("Your response is not correct, the correct answer is {}".format(QuestionSet[str(question_id)]['Answer']))    
    return question_asked, score

QuestionSet = read_question_bank()
question_asked = [0]

question_to_ask = 5
if question_to_ask > len(QuestionSet):
    question_to_ask = len(QuestionSet)

i = 0
score = 0 
while i < question_to_ask:
      question_asked, score = ask_question(question_asked, QuestionSet, score)
      i = i + 1

score = int((score/question_to_ask)*100)
print("Thank you for playing. Your score is {}%".format(score))
