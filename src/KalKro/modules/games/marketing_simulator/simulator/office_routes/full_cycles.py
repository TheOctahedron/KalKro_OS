from KalKro.modules.games.marketing_simulator.simulator.office_routes.make_deal import Deal_Maker
from KalKro.modules.games.marketing_simulator.simulator.main_office import Marketing_Simulator
from KalKro.utilities.helpers import printsl
import time

class Full_Cycles():
  def __init__(self, marketdata):
    self.marketd = marketdata
    self.market_actions = Marketing_Simulator.market_actions

    self.full_cycle_markets = {
      
    }



  def product_market(self): # WE SHOW ALL FULL-CYCLES STORES AND LOOK FOR THE RIGHT ONE.
    time.sleep(1)
    while True:
      print("\n\n")
      print("="*20)
      printsl("Buy full cycles (buy - automatic sell), buy knowing the risks of failure.")
      input("\nPress Enter to continue. ")
      print("\n\nselect an area to purchase a full-cycle product: ")
      for number, cycle in self.marketd.full_cycles.items():
        printsl(f"\n{number}: {cycle}")
      print("="*20)
      time.sleep(1)
      printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED SPHERE\n== Write '!Back' to exit ==\n")
      question = input("\n\n> ").lower().strip()
      match question:
        
        case "!back":
          printsl("\nGo back...")
          time.sleep(1)
          return
        case _:
          self.market_actions(question)
          continue
      self.product_price()


  def product_price(self): # WE SHOW THE MENU, FIND THE DESIRED PRODUCT.
    time.sleep(1)
    while True:
      print("\n\n\n")
      print("=" * 25)
      printsl("FULL-CYCLE MARKET: ")
      for product, price in self.marketd.market_name.items():
        printsl(f"\nPRODUCT: {product} PRICE: {price}$")
      print("=" * 25)
      printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED FULL-CYCLE PRODUCT\n== Write '!Back' to exit ==\n")
      products = list(self.marketd.market_name.values())
      question = input("\n\n> ").lower().strip()
      s_price = "" # STARTING PRISE
      match question:
        case "1":
          s_price = products[0]
        case "2":
          s_price = products[1]
        case "3":
          s_price = products[2]
        case "4":
          s_price = products[3]
        case "5":
          s_price = products[4]
        case "6":
          s_price = products[5]
        case "7":
          s_price = products[6]
        case "8":
          s_price = products[7]
        case "9":
          s_price = products[8]
        case "10":
          s_price = products[9]
        case "!back":
          printsl("\nGo back...")
          time.sleep(1)
          return
        case _:
          self.market_actions(question)
          continue

      self.marketd.starting_price = s_price
      Deal_Maker(self.marketd).product_category()


