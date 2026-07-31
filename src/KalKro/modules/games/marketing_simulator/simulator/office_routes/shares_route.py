from KalKro.utilities.helpers import printsl, loading_effect, yes_no
import time, random

class Share_market:
    def __init__(self, marketdata):
      self.marketd = marketdata


    def show_shares(self):  # SHOW THE CATEGORIES OF SHARES AND GIVE A CHOICE
      Low_Shares = ["Say'S Farm", "Fish And Worm", "EatButDS", "TVmyLOVE"]
      Middle_Shares = ["ChairI mperia", "CroCodyle", "StopStopItem", "History Bottle"]
      High_Shares = ["Myster-Sy", "GroundWound", "LuxaR", "MSIB", "Ultra&CycLe", "GranDO"]
      while True:
        printsl("\n\nShare markets!")
        print("\n\n1. Little-known stocks")
        print("\n2. Ordinary stocks")
        print("\n3. Well-known stocks")
        printsl("\nRECOMMENDED: \nREAD MORE: Type '!Help' to get useful information.")
        time.sleep(0.2)
        printsl("\n\nWRITE THE NUMBER OF THE SELECTED SHARE SECTION = '!Back' to exit. =")
        question = input("\n\n> ").lower().strip()
        match question:
          case "1":
            selected_section = Low_Shares
            share_category = "LK"  # Little Known
          case "2":
            selected_section = Middle_Shares
            share_category = "OY"  # Ordinary
          case "3":
            selected_section = High_Shares
            share_category = "WK"  # Well Known
          case "!back":
            printsl("\nGo back...")
            time.sleep(0.4)
            return
          case "!help":
            self.get_share_help() 
          case _:
            self.etc_actions(question)
            continue
        self.found_shares(selected_section, share_category)
        
    
    
    
    def get_share_help(self): # A LITTLE INSTRUCTION
      time.sleep(0.5)
      print("\n\nINFORMATION\n")
      print("\nFirst step: Select the desired stock section from the main menu.")
      print("\nSecond step: choose the desired increase")
      print("\nThird step: choose the number of shares to be purchased, and formalize.")
      print("\nFIGHT: the price of a stock varies rapidly, can fall or rise, you are shown the price.\n" \
      "You choose whether to wait further or sell all the shares.\n " \
      "At one point, the stock may collapse and have to be sold at the last price.")
      input("\n\nPress Enter To Exit")
      time.sleep(0.3)
      return




    def found_shares(self, selected_section, share_category): # FIND PROMOTIONS IN THE SELECTED CATEGORY
      match share_category:
        case "LK":
          price_value = (10, 300)
        case "OY":
          price_value = (300, 1000)
        case "WK":
          price_value = (1000, 10000)
      while True:
        time.sleep(0.3)
        printsl("\nUPDATED...")
        share_number = 0
        random_shares = random.sample(selected_section, k=3)
        share_data = []
        all_shares = {}
        for share_name in random_shares:
          share_number += 1
          share_price = random.randint(*price_value)
          share_data.append((share_name, share_number, share_price))
          all_shares = {"data": share_data}
          exiter = self.choose_shares(all_shares, share_category)
          if exiter == "back":
            return 
          elif exiter == "continue":
            continue




    def choose_shares(self, all_shares, category):  # GIVING A CHOICE OF PROMOTIONS
      while True:  
        for share_number, share_name, share_price in  all_shares["data"]:
          print(f"\n{share_number}. {share_name}: {share_price}")
        printsl("\n\nENTER THE NUMBER OF THE SELECTED PROMOTION  = '!R' to refresh the list of stocks, '!Back' to exit. =")
        time.sleep(0.1)
        question = input("\n\n> ").lower().strip()
        if question == "!r":
          return "continue"
        elif question == "!back":
          printsl("\nGo back...")
          time.sleep(0.4)
          return "back"
        
        try:
          idx = int(question)
          found = False
          for name, number, price in all_shares["data"]:
            if number == idx:
              share_price = price
              share_name = name
              share_number = number
              found = True
              break

          if not found:
            printsl("\n\nSorry, but this promotion number was not found.")  
            time.sleep(0.6)
            continue

        except Exception as e:
          printsl(f"\nERROR... {e}\n\n\n")
          continue
        self.buy_share(share_number, share_name, share_price, category)




    def buy_share(self, share_number, share_name, share_price, category):  # MAKING A PURCHASE
      while True:
        printsl(f"\n\n{share_number}. {share_name}.")   
        print(f"\nPRICE: {share_price}$ for 1 share.") 
        time.sleep(0.2)
        total_price = 0
        printsl("\n\nHOW MANY OF THESE SHARES DO YOU WANT TO BUY? = '!Back' to exit. =")
        quantity = input("\n\n> ").lower().strip()
        if quantity == "!back":
          printsl("\n\nGo back...")
          time.sleep(0.4)
          return
        try:
          quantity_idx = int(quantity)
          total_price = share_price * quantity_idx
          loading_effect(0.5)
          print(f"TAKEN: {quantity_idx} SHARES.\nTOTAL PRICE: {total_price}$")
          time.sleep(0.4)

          printsl("\n\nPLEASE TAKE INTO ACCOUNT ALL THE RISKS, TO FIND OUT MORE, ENTER '!Help'")

          time.sleep(0.3)
          agree = yes_no(f"\nDO YOU AGREE TO PURCHASE {quantity_idx} SHARES? (price: {total_price})")
          loading_effect(0.5)
          if agree:
            if self.marketd.money < total_price:
              printsl(f"\n\nYOU DON'T HAVE ENOUGH MONEY. ON YOUR BALANCE: {self.marketd.money}$ \nAND IT IS REQUIRED: {total_price}$")
              input("\nPress Enter To Continue")
              continue
            else:
              self.marketd.money -= total_price
              printsl(f"\n\nFormalized! {quantity} shares. (-{total_price}$)")
              loading_effect(0.5)
              self.share_battle(total_price, share_name, category)
              return
            
        except Exception as e:
          printsl(f"\nERROR... {e}\n\n\n")
          continue




    def share_battle(self, total_price, name, category):  # GROWTH/DECLINE OF STOCKS
      loading_effect(1)
      wave = 0
      starting_price = total_price
      while True:
        while True:
          wave += 1
          difference = total_price - starting_price  
          print(f"\n\nSHARE: {name} (ctg: {category}) \nCURRENT PRICE: {total_price} \nSTARTING PRICE: {starting_price} \nDIFFERENCE FROM THE INITIAL PRICE: {difference}")
          if total_price < 0:
            printsl("\n\nERROR 119")
            time.sleep(1)
            return
          print("\n\nACTIONS:")
          print("\n1. CONTINUE TO FOLLOW PRICE (risk)")
          print("\n2. SELL EVERYTHING AT THE CURRENT PRICE (exit)")
          printsl("\nENTER THE NUMBER OF THE SELECTED ACTION")
          question = input("\n\n> ")
          match question:
            case "1":
              break
            case "2":
              self.sell_share(total_price)
              return
            case _:
              self.etc_actions(question)
        
        chance = random.randint(1, 50)
        match category:
          case "LK":
            lose_chanse = 20
            high_chance = 45
          case "OY":
            lose_chanse = 10
            high_chance = 40
          case "WK":
            lose_chanse = 5
            high_chance = 35

        if chance <= lose_chanse:
          printsl("\n")
          total_price = total_price * random.uniform(0.1, 0.4)
        elif chance >= high_chance:
          printsl("\n")
          total_price = total_price * random.uniform(2, 10)
        
        loseOrHigh = random.randint(1, 3)
        if loseOrHigh == 1:
          total_price = total_price * random.uniform(0.5, 0.9)
        else:
          total_price = total_price * random.uniform(1.1, 2.3)

        continue
  


    
    def sell_share(self, total_price):  # RECEIVING FUNDS FOR SHARES
      loading_effect(1)
      self.marketd.money += total_price
      printsl(f"\n\nSuccessfully received {total_price}$! \nYour wallet: {self.marketd.money}")
      input("\n\nPress Enter To exit")
      return
    