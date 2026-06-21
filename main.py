from raylib import *
from steamgrid import SteamGridDB
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("STEAMGRIDDB_API_KEY")
if api_key is None:
    raise RuntimeError("No api key found!")

sgdb = SteamGridDB(api_key)

print(sgdb)

def SearchGames(name):
    result = sgdb.search_game(name)
    if result is None:
        raise RuntimeError("No games found!")
    return result

print("Search for a game:")
query = input()
searchResult = SearchGames(query)

print("=========")
for index, game in enumerate(searchResult):
    if game is None:
        raise RuntimeError("Search failed")
    assert game.name
    print(f"{index + 1}: {game.name} - {game.id}")

print("=========")

choice = None
print("Select result:")
while True:
    choice = input()
    try:
        choice = int(choice)
    except:
        print("please enter a number")
        continue

    if not (0 < choice <= 10):
        print("please select 1-10")
        continue
    else:
        choice = choice - 1
        break

gameChoice = searchResult[choice]
print(gameChoice.id)

assert gameChoice.id
grids = sgdb.get_grids_by_gameid([gameChoice.id])
print(grids)
print(grids[0].url)
