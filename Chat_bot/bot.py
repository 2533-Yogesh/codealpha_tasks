import random

responses = {
    "hello": ["Hi!", "Hola Amigo!", "Moshi Mosh!"],
    "how are you": ["Very well, Thank you. And yourself?",
                    "I am surviving, how about you?",
                    "As Good as Today's weather, what about you?"],
    "what is your name?": ["Call me Max, BayMax!",
                           "You can Call me..Avizandium",
                           "Ore wa Tenjin des."],
    "bye": ["Bye,Bye!", "Adios Amigo", "Sayonara!"]
}

def chatbot():
    while True:
        u_inp = input("You: ").lower().strip()
        matched_key = None
        for key in responses.keys():
            if key in u_inp:  # partial match check
                matched_key = key
                break
        
        if matched_key:
            reply = random.choice(responses[matched_key])
            print("Bot:", reply)
            
            if matched_key == "bye":
                break
        else:
            print("Bot: I am sorry I didn't understand what you said.")  

chatbot()
