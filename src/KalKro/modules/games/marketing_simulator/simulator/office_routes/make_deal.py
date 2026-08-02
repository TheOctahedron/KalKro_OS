import time, random
from KalKro.utilities.helpers import printsl, loading_effect
from KalKro.utilities.game_databases.market_data_pack.market_data import market_actions

class Deal_Maker():
  def __init__(self, marketdata):
    self.marketd = marketdata

  def make_deal(self, product_type): # SELECT A CATEGORY, AND TAKE THE RISK OF SUCCESS/FAILURE
    category_datas = {
      "small": {"title": "TRIFLE PRODUCT", "category": "small category", "bubbles_need": 0, "chance": 16},

      "decent": {"title": "DECENT PRODUCT", "category": "small+++ category", "bubbles_need": 1, "chance": 15},

      "middle": {"title": "MIDDLE PRODUCT", "category": "middle category", "bubbles_need": 2, "chance": 14},

      "middle_up": {"title": "LIMITED PRODUCT", "category": "middle+++ category", "bubbles_need": 3, "chance": 10},

      "demand": {"title": "DEMAND PRODUCT", "category": "top category", "bubbles_need": 4, "chance": 8},

      "advanched": {"title": "ADVANCHED PRODUCT", "category": "top+++ category", "bubbles_need": 5, "chance": 8},

      "global":  {"title": "GLOBAL PRODUCT", "category": "global category", "bubbles_need": 6, "chance": 8},
    }
    data_product = category_datas[product_type]
    while True:
      printsl(f"\n{data_product['title']}\n")
      printsl(f"This Full-Cycle packpage, f {data_product['category']}.")
      printsl("\nMake a Deal?")
      print("\n1. Yes\n\n2. No")
      question = input("\n\n> ")
      match question:
        case "1":
          loading_effect(1)
          win_chance = data_product['chance']
          chance = random.randint(1, 20)
          if chance <= win_chance:
            self.marketd.deal = True
          else:
            self.marketd.deal = False
          break
        case "2":
          return
        case _:
          market_actions(question)
          continue
          
    self.check_deal()
    return



  def check_deal(self): # WE MAKE AND TELL ABOUT THE RESULT OF THE TRANSACTION.
    self.marketd.level += self.marketd.starting_price / 2
    if self.marketd.deal:
      printsl("\nGreat! The deal was successful and brought you profit.")
      self.add = random.randint( 
        int(self.marketd.starting_price * 1.10), 
        int(self.marketd.starting_price * 2.5)
      )
      self.marketd.profit = self.marketd.starting_price + self.add
      self.marketd.starting_price = 0
    else: 
      printsl(f"\nUnfortunately, the deal failed, and the loss was: {self.marketd.starting_price}")
      time.sleep(1)
    input("\nPress Enter to complete this transaction.")
    return



  def product_category(self): # WE LOOK FOR THE CATEGORY OF THE SELECTED PRODUCT AND SEND IT TO MAKE A PURCHASE TRANSACTION
    all_category = {
      "small": 10000,
      "decent": 50000,
      "middle": 250000,
      "middle_up": 500000,
      "demand": 5000000,
      "advanched": 100000000,
    }
    for category, price in all_category.items():
      if self.marketd.starting_price <= price:
        self.make_deal(category)
        return
    self.make_deal("global")
    return
    
