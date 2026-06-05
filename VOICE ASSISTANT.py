import pyttsx3
from datetime import datetime

def speak(text):
    print('AI BOT' , text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
print("Hi i am your AI assistant, how can i help you? Type 'exit' or 'quit' to end the conversation.")
def wish_me():
    hour = datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

while True:
    user_input = input("👤You: ").lower()
    if "hello" in user_input or "hi" in user_input or "salam" in user_input:
        speak("Hello! Assalam Alaikum How can I assist you today?")
    elif "how are you" in user_input:
        speak("I am doing well, thank you! How about you?")
    elif "what is your name" in user_input:
        speak("I am Ahmad's AI assistant. Nice to meet you!")
    elif "what time is it" in user_input:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "calculate" in user_input:
        try:
            expression = user_input.replace("calculate", "").strip()
            result = eval(expression)
            speak(f"The result of {expression} is {result}")
        except Exception as e:
            speak("Sorry, I couldn't calculate that. Please make sure to provide a valid expression.")
    elif "exit" in user_input or "quit" in user_input:
        speak("Goodbye! Have a great day!")
        break
