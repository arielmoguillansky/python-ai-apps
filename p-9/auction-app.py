from art import logo
import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

# Initialize the client with your API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
  model="gpt-5-nano",
  instructions="You are an auctioneer running a secret auction. Your task is to provide with objects to bid. Return ONLY the name of the object a description and a starting bid price in USD. Format the response in JSON as {\"item\": \"item_name\", \"description\": \"item_description\", \"starting_bid\": starting_bid_amount}. Do not include any additional text.",
  input="Provide an item for a secret auction.",
)

print(logo)
print("Welcome to the secret auction program.")
response_json = json.loads(response.output_text)
starting_bid = response_json["starting_bid"]
print("-----------------------------------")
print(f"Item: {response_json["item"]}\nDescription: {response_json["description"]}\nStarting Bid: ${starting_bid}")

more_bidders = True
bidders = {}

while more_bidders:
    bidder = input("What is your name? ")
    bid = 0
    while bid < starting_bid:
      bid = float(input("What's your bid? $"))
      if bid < starting_bid:
          print(f"Your bid must be at least the starting bid of ${starting_bid}. Please enter a valid bid.")
    bidders[bidder] = bid
    add_bidder = input("Are there any other bidders? Type 'yes' or 'no'")
    if add_bidder == 'no':
        more_bidders = False

def get_winner():
    return max(bidders, key=lambda key:bidders[key])

bidder_winner = get_winner()
print(f"Bidder {bidder_winner} won with ${bidders[bidder_winner]}")


