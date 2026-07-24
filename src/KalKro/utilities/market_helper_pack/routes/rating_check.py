from KalKro.utilities.helpers import printsl
import time

def rating_check(self, level, specialization):
    requires_bubbles = 0
    time.sleep(0.5)
    print("===")
    printsl(f"\n\nYOUR WALLET AT THE MOMENT: {self.marketd.money}$.")
    printsl("\nYou can always quickly view your material account using the '!wallet' command.")
    print("===")
    
    printsl(f"\n\nYOUR RATING AT THE MOMENT: {self.marketd.level} bubbles.")
    all_levels = [ 
      1_000, # intern
      10_000, # junior analyst
      50_000, # analyst
      79_000, # senior analyst
      85_000, # associate
      105_000, # senior associate
      190_000, # junior vice-president (VC)
      1_000_000, # senior vice-president (VC)
      2_000_000, # managing director
      10_000_000, # partner
      50_000_000, # senior partner
      2_000_000_000, # CIO
      8_000_000_000, # board member
      50_000_000_000, # economic advistor
      60_000_000_000 # the one who resold the gum
    ]

    all_specialization = [
      "intern", # 1.000$
      "junior analyst", # 10.000$
      "analyst", # 50.000$
      "senior analyst", # 79.000$
      "associate", # 85.000$
      "senior associate", # 105.000$
      "junior vice-president (VC)", # 190.000$
      "senior vice-president (VC)", # 1.000.000$
      "managing director", # 2.000.000$
      "partner", # 10.000.000$
      "senior partner", # 50.000.000$
      "CIO", # 2.000.000.000$
      "board member", # 8.000.000.000$
      "economic advistor", # 50.000.000.000$
      "the one who resold the gum" # 60.000.000.000$
    ]


    for level, new_specilization in zip(all_levels, all_specialization):
      if level <= level:
        specialization = new_specilization
        requires_bubbles = level
        break

    printsl(f"\nSpecialization: {specialization}")
    time.sleep(0.5)
    requires_bubbles -= level
    print(f"\nYou need {requires_bubbles} bubble points to reach the next specialization. (1$ in wallet = 0.5 bubble)")
    input("\n\nPress Enter to exit\n")
    return
      