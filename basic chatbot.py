def chatbot_response(user):
    if user.lower()=='hello' or  user.lower()=='hi'or  'hello ' in user.lower() or 'hi ' in user.lower():
        return("Chatbot : Hi")
    elif 'how are you' in user.lower():
        return("Chatbot: I am a bot I am doing well.")
    elif 'your name' in user.lower() or user.lower()=='what is your name':
        return("Chatbot: I am chatbot your virtual assistant")
    else:
        return("Chatbot : Sorry I dont have information regarding this can you please ask something else.")
print("Chatbot: Hello you can start the conversation")
flag=0
while True:
    user=input("You :")
    if "bye" in user:
        print('Chatbot: Good bye Have a great Day')
        break
    response=chatbot_response(user)
    print(response)
    
