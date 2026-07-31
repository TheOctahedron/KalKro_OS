import time
from KalKro.utilities.helpers import printsl, loading_effect, yes_no
from KalKro.utilities.game_databases.market_data_pack.market_data import market_actions
from KalKro.modules.games.marketing_simulator.simulator.main_office import Marketing_Simulator



class Welcome_Market:
  def __init__(self, marketdata):
    self.marketd = marketdata
    self.market_office = Marketing_Simulator(self.marketd).market_office
    
  def welcome_to_game(self):
    time.sleep(1)
    print("\n\n= You can always use the command '!Exit' by typing it in the terminal to exit the game. =\n\n")
    loading_effect(3)
    printsl("Welcome.")
    time.sleep(1)
    self.main_menu()

  def main_menu(self):
    printsl("\n\n= Menu Items =\n")
    print("\n1. Play")
    print("\n2. Basic idea")
    print("\n3. New game")
    print("\n4. Exit ")
    time.sleep(1.5)
    printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED MENU-ITEM")
    question = input("\n\n> ").lower().strip()
    match question:
      case "1":
        time.sleep(1)
        self.market_office()
      case "2":
        time.sleep(1)
        self.rules()
      case "3":
        self.new_game()
      case "4":
        print("\n\nSee you again! investor ;)")
        time.sleep(1)
        return

  def rules(self):
    print("\n\n")
    print("="*80)
    print("\nMAIN IDEA: \n")
    printsl("\nThe main idea: is that you are an investor, you open up startups, your own virtual currencies, monitor charts, and so on...")
    printsl("\n\nCommands: ")
    market_actions("!othercmd")
    print("="*80)
    time.sleep(1)
    input("\n\nPress Enter to menu\n")
    return
  
  def new_game(self):
    question = yes_no("Are you sure you want to start new game?")
    if question:
        loading_effect(0.5)
        self.marketd.__dict__.update(market_actions)
        return
    else:
        return
    

