from steamgrid import SteamGridDB
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("STEAMGRIDDB_API_KEY")
if api_key is None:
    raise RuntimeError("No api key found!")

sgdb = SteamGridDB(api_key)

def SearchGames(name):
    result = sgdb.search_game(name)
    if result is None:
        raise RuntimeError("No games found!")
    return result

print("Search for a game")
query = input()
result = SearchGames(query)
print(result)
