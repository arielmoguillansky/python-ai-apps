import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize the client with your API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def play_avengers_ai():
    print("--- AVENGERS: AI EDITION ---")
    context = "You are the narrator of a game. The player is Iron Man fighting Thanos."
    
    # We keep a history so the AI remembers what happened in Step 1, 2, etc.
    messages = [{"role": "system", "content": context}]

    for step in range(1, 6): # 5 Steps to win
        user_action = input(f"Step {step}: What do you do? ")
        
        # Add player's action to the conversation
        messages.append({"role": "user", "content": user_action})

        # Ask the AI to continue the story
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages + [{"role": "system", "content": "Describe the result in 2 sentences. If the player dies, include 'GAME OVER'. If they win step 5, say 'YOU WIN'."}],
            max_tokens=150,
            temperature=0.7
        )

        reply = response.choices[0].message.content
        print(f"\n{reply}\n")

        if "GAME OVER" in reply.upper():
            break
        if "YOU WIN" in reply.upper():
            print("Congratulations, Avenger!")
            break

play_avengers_ai()