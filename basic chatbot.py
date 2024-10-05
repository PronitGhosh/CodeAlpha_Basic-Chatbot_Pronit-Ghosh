import nltk
import random
import string
nltk.download('punkt')
nltk.download('wordnet')  
from nltk.corpus import wordnet
from nltk.chat.util import Chat, reflections
pairs = [
    [r"hi|hello|hey(.*)", ["Hello!", "Hi there!", "Hey!"]],
    [r"(.*)your name?", ["My name is ChatBot."]],
    [r"how are you ?", ["I'm doing well, how about you?"]],
    [r"(.*)sorry(.*)", ["No problem!", "That's okay!"]],
    [r"i am doing good", ["Nice to hear that!"]],
    [r"bye|exit", ["Goodbye!", "See you later!"]],
    [r"(.*)",["Sorry I dont have information regarding this."]]
]
chatbot = Chat(pairs, reflections)
print("ChatBot: Hello! Type 'bye' to exit the chat.")
chatbot.converse()
