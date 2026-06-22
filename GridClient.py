from steamgrid import SteamGridDB
from steamgrid.http import HTTPException
import requests

r = requests.get("https://cdn2.steamgriddb.com/grid/3410a21fe74b678181d2cd2b4195abf0.png")
# print(r.status_code)
# print(r.content)
# with open("test.jpg", "wb") as f:
#     f.write(r.content)

class GridDBClient:
    database: SteamGridDB
    def __init__(self, key):
        if key is None:
            raise RuntimeError("No api key found!")

        self.database = SteamGridDB(key)
        try:
            self.database.get_game_by_steam_appid(730)
        except HTTPException as e:
            raise RuntimeError("Invalid Auth Key") from e

    # def CacheGrids(self, grids)
    def SearchGames(self, name):
        results = self.database.search_game(name)
        if results is None:
            raise RuntimeError("No games found!")
        return results
