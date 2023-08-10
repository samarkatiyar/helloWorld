import json
import os
import random
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
def SpeakText(command):
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	
def hear_microphone():
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
			#SpeakText(MyText)
            return MyText 
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return "0"
    except sr.UnknownValueError:
        print("unknown error occurred")
        return "0"

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
    choices = ['one', 'two', 'three', 'four']
    while response not in choices:
          SpeakText("What is your answer")
          #response = input("Please enter your answer ---> ")
          response = hear_microphone()
          if response:
              response = response.lower()
    return str((choices.index(response) + 1))

def print_question(QuestionSet, question_id):
    print("-"*20)
    print("Question --> {}".format(QuestionSet[str(question_id)]['Question']))
    SpeakText(QuestionSet[str(question_id)]['Question'])
    print("Choices")
    SpeakText("Your choices are")
    for choice in QuestionSet[str(question_id)]['Choices']:
        print("{} : {}".format(choice, QuestionSet[str(question_id)]['Choices'][choice]))
        SpeakText(choice + "," + QuestionSet[str(question_id)]['Choices'][choice])

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
        SpeakText("Bingo, you are correct!")
        score = score + 1
    else:
        print("Your response is not correct, the correct answer is {}".format(QuestionSet[str(question_id)]['Answer']))    
        SpeakText("Your response is not correct, the correct answer is" + QuestionSet[str(question_id)]['Answer'])
    return question_asked, score

#Start Quiz
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
SpeakText("Thank you for playing. Your score is " +  str(score) + "%")