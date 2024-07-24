from pinecone import Pinecone
import os

# from dotenv import load_dotenv

# # Load environment variables from the .env file
# load_dotenv()


key = os.getenv("PINECONE_API_KEY")
client = Pinecone(api_key = key)

def get_index(name):
    index = client.Index(name)
    return index