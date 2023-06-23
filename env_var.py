from dotenv import load_dotenv
import os

load_dotenv() #loads the .env file

password = os.getenv("PASSWORD")

print(password)