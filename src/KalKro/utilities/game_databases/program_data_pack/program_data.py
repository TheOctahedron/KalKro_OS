# ========== System Apps ========== 
from KalKro.modules.apps.ai_dojdo.dojdo_main import DojDo_Main

from KalKro.modules.apps.boring_calculator import Boring_Calculator

from KalKro.modules.apps.garbage_truck import Garbage_Truck

from KalKro.modules.apps.randomizer import Randomizer

from KalKro.modules.apps.installer import Installer

from KalKro.modules.apps.save_load import SaveLoad

from KalKro.modules.apps.catfish.catfish_browser import CatFishBrowser

from KalKro.file_conductor.file_conductor import File_Conductor



# ============= Games =============
from KalKro.modules.games.tic_tac_toe import Tic_Tac_Toe

from KalKro.modules.games.marketing_simulator.simulator.welcome_office import Welcome_Market

from KalKro.modules.games.rock_paper_scissors import Rock_Paper_Scissors



# ========= OfficePackage =========
from KalKro.modules.apps.octice_office.octice import OcticeSelect



program_data = {
  "downloadable_programs": [
    {"id": 1, "name": "Rock-Paper-Scissors", "weight": 120},  # added to prg_link
    {"id": 2, "name": "Marketing-Simulator", "weight": 1000},  # added to prg_link
    {"id": 3, "name": "DojDo AI", "weight": 200}  # added to prg_link
  ],


  "system_programs": [
    {"id": 1, "name": "Garbage Truck"}, # added to prg_link
    {"id": 2, "name": "Catfish-Browser (internet)"},  # added to prg_link
    {"id": 3, "name": "tic-tac-toe"}, # added to prg_link
    {"id": 4, "name": "The Randomizer"},  # added to prg_link
    {"id": 5, "name": "SaVeLoAd"},  # added to prg_link
    {"id": 6, "name": "diskS"}, # added to prg_link
    {"id": 7, "name": "Boring Calculator"}, # added to prg_link
    {"id": 8, "name": "Octice Office"}, # added to prg_link
    {"id": 9, "name": "File Conductor"} # added to prg_link
  ],


  "installed_programs": [],

  "program_link": {
    # ============ SYSTEM ============
    "Garbage Truck": Garbage_Truck().garbage,
    "Catfish-Browser (internet)": CatFishBrowser().catfish_go,
    "tic-tac-toe": Tic_Tac_Toe().tic_tac_toe,
    "The Randomizer": Randomizer().random_go,
    "SaveLoad": SaveLoad().saveload,
    "Installer": Installer().diskS,
    "Boring Calculator": Boring_Calculator().hi_calculator,
    "Octice Office": OcticeSelect(),
    "File Conductor": File_Conductor().main_menu,
    # ========== DOWNLOADED ==========
    "Rock-Paper-Scissors": Rock_Paper_Scissors().game_rps,
    "Marketing-Simulator": Welcome_Market().main_menu,
    "DojDo AI": DojDo_Main.DojDo_go
  }
}
  