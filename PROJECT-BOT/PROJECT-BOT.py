import json
import random


def load_responses(filename):
    with open(filename, 'r') as file:
        return json.load(file)



def generate_agent_name():
    names = ["Arjun", "Riya", "Sanjay", "Bijay", "Pratik"]
    return random.choice(names)



def get_response(user_input, responses):
    user_input = user_input.lower()
    for keyword, response in responses.items():
        if keyword in user_input:
            return response
    return random.choice(responses["default"])


def main():
    responses = load_responses('responenes.json')
    
    user_name = input("Welcome! Please enter your name: ")
    print(f"Hello, {user_name}! I'm your virtual assistant today.")
    
    agent_name = generate_agent_name()
    print(f"Your agent today is {agent_name}.")

    while True:
        user_question = input(f"{user_name}: ")
        
        if user_question.lower() in ["bye", "quit", "exit"]:
            print("Thank you for chatting! Goodbye!")
            break
        
        response = get_response(user_question, responses)
        print(f"{agent_name}: {response}")

if __name__ == "__main__":
    main()