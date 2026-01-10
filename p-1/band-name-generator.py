import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.environ.get(os.getenv("OPENAI_API_KEY")) 
)

music_genre = input("Enter the genre of music: ")
city_name= input("Enter the name of the city where the band was formed: ")
member_count = input("Enter the number of members in the band: ")

response = client.responses.create(
  model="gpt-5-nano",
  instructions="Given the genre of music, the number of members and the name of the city where the band was formed, provide just one possible name for the band. You need to get into account the city's culture and do not use the names given in the input",
  input=f"Genre: {music_genre}\nCity: {city_name}\nMembers: {member_count}"
)

print(response.output_text)