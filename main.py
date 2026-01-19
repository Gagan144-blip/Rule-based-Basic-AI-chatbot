# Rule-Based  Basic AI Chatbot

import datetime
import time

presentHour = datetime.datetime.now().hour

name=input("Welcome to ChatBot! Please enter your name: ")

if 5 <= presentHour <=11:
    print("Good Morning!", name)
elif 11<= presentHour <=17:
    print("Good Afternoon!", name)
elif 17<= presentHour <=20:
    print("Good Evening!", name)
else:
    print("Good Night!", name)
print("Namaste! welcome to Your ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

#Chatbot Memory Creation [dictionary of responese ]

responses = {
    "hello": "Hi, welcome, How can I help you?",
    "how are you?": "I am fine. Thankyou",
    "Who are you?": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project  makes you a better developer",
    "happy": "Great to hear that",
    "functions kya hote hai?": "Functions are reusable pieces of code that perform a specific task",
    "bye": "Goodbye! Have a nice day"
}

#Method/Function to get response of Chatbot

def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
        
    return "I am not able to tell that yet. I am still in learning mode"

# Take user Input

while True:
    userInput = input("please ask your Question: ")
    reply = getResponseBot(userInput)
    print("ChatBot: ", reply)


    if "bye" in userInput.lower():
        break