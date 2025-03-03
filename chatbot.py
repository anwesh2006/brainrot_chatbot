import random

def brainrot_chatbot():
    print("ChatBot: Yooo, it's ya boi, john pork")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("ChatBot: Ight imma head out 🏃💨 ")
            break
        
        if "hello" in user_input or "hi" in user_input:
            print(random.choice([
                "ChatBot: yall are chopped",
                "ChatBot: chopped chin this must be u",
                "ChatBot: should i date p diddy or chopped chin"
            ]))
        elif "how are you" in user_input:
            print(random.choice([
                "ChatBot: Living my best digital life, no cap 🧢",
                "ChatBot: I'm straight vibing, fam. It's bussin' 😤",
                "ChatBot: Feeling extra chopped"
            ]))
        elif "your name" in user_input:
            print(random.choice([
                "ChatBot: i am known as the sneaky gooners",
                "ChatBot: bedwetter",
                "ChatBot: I'm Terminally Online"
            ]))
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"ChatBot: It's {current_time} and you're still not over your flop era? Cringe ")
        else:
            print(random.choice([
                "ChatBot: that's so random. I'm living for it tho ",
                "ChatBot: Weird flex but ok",
                "ChatBot: its time gooning gang",
                "ChatBot: Sorry, I don't speak flop"
            ]))

if __name__ == "__main__":
    brainrot_chatbot()
 
