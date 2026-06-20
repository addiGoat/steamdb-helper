from steamgrid import SteamGridDB

sgdb = SteamGridDB('77d20bdbd03525d8324af4daf9b2ac1a')

def SearchGames(name):
    result = sgdb.search_game(name)
    if result is None:
        raise RuntimeError("No games found!")
    return result

print("Search for a game")
query = input()
result = SearchGames(query)
print(result)
