import dearpygui.dearpygui as dpg
from dotenv import load_dotenv
import os

import GridClient

load_dotenv()

client = GridClient.GridDBClient(os.getenv("STEAMGRIDDB_API_KEY"))

results = client.SearchGames("white Knuckle")

def save_callback():
    print("Save Clicked")

dpg.create_context()

with dpg.window(tag='Main Window'):
    for index, game in enumerate(results):
        if game.name is None:
            raise(RuntimeError("Game Name Not Found"))
    
        dpg.add_button(tag=f"Btn{index}", label=f"Button {index}: {game}")
dpg.show_item_registry()

dpg.create_viewport(title='Helper Window', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Main Window", True)
dpg.start_dearpygui()
dpg.destroy_context()


    

# print("Search for a game:")
# query = input()
# searchResult = client.SearchGames(query)
#
# print("=========")
# for index, game in enumerate(searchResult):
#     if game is None:
#         raise RuntimeError("Search failed")
#     print(f"{index + 1}: {game.name} - {game.id}")
#
# print("=========")
#
# choice = None
# print("Select result:")
# while True:
#     choice = input()
#     try:
#         choice = int(choice)
#     except:
#         print("please enter a number")
#         continue
#
#     if not (0 < choice <= 10):
#         print("please select 1-10")
#         continue
#     else:
#         choice = choice - 1
#         break
#
# gameChoice = searchResult[choice]
# if gameChoice.id is None:
#     raise RuntimeError("Game ID not found")
#
# grids = sgdb.get_grids_by_gameid([gameChoice.id])
# assert grids
# for grid in grids:
#     print(grid.url)
#
# # ================ RAYLIB TESTING ================ 
# from raylib import *
#
# windowWidth = 1280
# windowHeight = 1280
# InitWindow(windowWidth, windowHeight, b"Grid Helper")
# SetTargetFPS(120)
#
# while not WindowShouldClose():
#
#
#
