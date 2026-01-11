import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.environ.get(os.getenv("OPENAI_API_KEY")) 
)

print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))
country= input("Enter the name of the country: ")
food_rate = input("Rate the food quality out of 5: ")
service_rate = input("Rate the service quality out of 5: ")
ambient_rate = input("Rate the ambient quality out of 5: ")
client_number = int(input("How many people to split the bill? "))


response = client.responses.create(
  model="gpt-5-nano",
  instructions="You are a Global Tipping Expert. Your task is to calculate a recommended tip percentage based on the user's country and their rating of Service, Food, and Ambiance (each rated 1-5 stars). Respect local customs (e.g., 18-22% in the USA, 10% in Brazil, 0% in Japan/South Korea). If a country has a customary or 'expected' minimum (like 10% in many parts of Europe), do not go below it unless the ratings are 1 star.Return ONLY the numerical percentage as a float. Do not include '%' or any text. If the tip should be 15%, return '15.0'.",
  input=f"Country: {country}\nFood: {food_rate}\nService: {service_rate}\nAmbiance: {ambient_rate}"
)

percentage_tip = float(response.output_text)

tip_amount = (percentage_tip / 100) * total_bill

total = total_bill + tip_amount

total_per_person = total / client_number

print(f"Suggested tip percentage: {percentage_tip}%")
print(f"Each should pay: ${round(total_per_person,2)}")