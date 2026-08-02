import time, httpx
from KalKro.utilities.helpers import printsl
from KalKro.utilities.game_databases.market_data_pack.market_data import market_actions
from KalKro.modules.games.marketing_simulator.simulator.office_routes.shares_route import Share_market
from KalKro.modules.games.marketing_simulator.simulator.office_routes.full_cycles import Full_Cycles

class Marketing_Simulator:
  def __init__(self, marketdata):
    self.marketd = marketdata
    self.share_market = Share_market(self.marketd)

    self.full_cycles_market = Full_Cycles.product_market(self.marketd)


  def market_actions(self, cmd):
    market_actions(cmd)
    return


    
  def market_office(self): # GREET THE PLAYER AND SEND HIM TO THE CENTER OF THE MAIN ACTION
    printsl("\n\nWelcome to your office!")
    self.actions_market()

  

  # ============================================================================



  def actions_market(self): # MAIN ACTIONS, THE OFFICE ITSELF
    time.sleep(1)
    while True:
      print("="*20)
      printsl("\n\nYour possible actions: ")
      print("\n1. View/Buy Crypto-Сurrency from the Crypto-Market.")
      print("\n2. Look at inflation")
      print("\n3. Market (with full cycles)")
      print("\n4. View the exchange rate.")
      print("\n5. View your wallet and rating.")
      print("\n6. View your rating.")
      print("\n7. Buy shares. (FIRE)\n\n")
      print("="*20)
      time.sleep(1)
      printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED ACTION\n== Write '!Back' to exit ==\n")
      question = input("\n\n> ").lower().strip()
      match question:
        case "1":
          self.crypto_market()
        case "2":
          self.inflation_market()
        case "3":
          self.full_cycles_market()
        case "4":
          self.exchange_rate()
        case "5":
          self.market_actions("!wallet")
        case "6":
          self.market_actions("!rating")
        case "6":
          self.share_market.show_shares()
        case "!back":
          printsl("\nGo back...")
          time.sleep(1)
          return
        case _:
          market_actions(question)
          continue



  # ============================================================================



  def crypto_market(self): # SHOWING IN-GAME CRYPTOCURRENCY
    time.sleep(1)
    print("="*20)
    printsl("\n\nCurrent market coins and their prices: ")
    for coin, value in self.marketd.coin.items():
      printsl(f"\n{coin}: {value}$")
    printsl("\nInflation is changing prices!")
    print("="*20)
    input("\nPress Enter to continue. ")
    return



  # ============================================================================



  def inflation_market(self): # JUST SHOWING IN-GAME INFLATION
    print(f"\ntotal inflation for all time: {self.marketd.inflation_procent}%.")
    input("\nPress Enter to continue. ")
    return



  # ============================================================================



  def exchange_rate(self):
    try:
      url = "https://open.er-api.com/v6/latest/USD"
      response = httpx.get(url, timeout=5)
      if response.status_code == 200:
        htdata  = response.json()
        rub = htdata["rates"]["RUB"]
        eur = htdata["rates"]["EUR"]
        update_time = htdata["time_last_update_utc"]
        printsl(f"\n\ndollar ($) exchange rate: \n")
        print("\nUSD = 1")
        print(f"RUB = {rub}")
        print(f"EUR = {eur}\n")
        printsl(f"\nRATE UPDATED: {update_time}\n")
        input("\n\n\nPress Enter to exit\n")
        return
    except Exception as e:
      printsl(f"\nERROR... {e}\n\n\n")
    input("\n\n\nPress Enter to exit\n")
    return



  # ============================================================================
 