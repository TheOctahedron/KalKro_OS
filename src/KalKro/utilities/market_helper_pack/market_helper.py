from KalKro.utilities.market_helper_pack.routes.wallet_check import wallet_check
from KalKro.utilities.market_helper_pack.routes.rating_check import rating_check

import time


market_data_pack = {
    "market_money": 1000,

    "level": 0,
   
    "coin": {
        "MilCoin": 2300,
        "ExCoin": 3000000,
        "NoCoin": 300,
        "TRIXCoin": 3190,
        "CoconCoin": 30303,
        "LaxCoin": 50
    },

    
    "inflation_percent": 0,
    "visits": 0,
    
    
    "full_cycles": { #####################
        "shop_segment": {"products": {
            "Snacks": 200,
            "Drinks": 300,
            "Fast_Food": 400,
            "Frozen_Food": 700,
            "Small_Equipment": 1100
        }},
        "restaurant_segment": {"products": {
            "Napkins": 300,
            "Juices": 450,
            "Cheese": 700,
            "Sauces": 1200,
            "Meats": 12000,
            "Caviars": 20000,
            "Caviars_Black": 45000
        }},
        "gaming_segment": {"products": {
            "Corpus": 2000,
            "HDD": 2040,
            "Coolers": 4000,
            "Processors": 6050,
            "SSD": 8500,
            "Monitors": 9700,
            "Adapters": 11000,
            "Videocards": 30000,
            "Full_Assembly": 99000
        }},
        "malls_segment": {"products": {
            "Toys": 20030,
            "Nutrition": 40000,
            "Clothes": 50000,
            "Shoes": 67000,
            "Furniture": 120000,
            "Gadgets": 240000,
            "Appliances": 310000
        }},
        "vehicle_segment": {"products": {
            "Diesel": 23400,
            "Engine_Oil": 40405,
            "Engines_S": 200300,
            "Engines_B": 400000,
            "Train_Engines": 500000,
            "Cars": 6700000,
            "Trucks": 12000000,
            "SportCars": 34000000,
            "Locomotives": 40000000
        }},
        "farm_segment": {"products": {
            "Fertilizer": 20600,
            "Vehicle_Connections": 440000,
            "Trailers": 520000,
            "Mini_Tractors": 810000,
            "Tractors": 12703000,
            "Cattle_Truck": 44300900,
            "Combine_Harvesters": 90000000
        }},
    },
    
    "specialization": "low_trainee_economist",
    "requires_bubbles": 0,
    "market_category": "shop_segment" ##
}

def market_actions(cmd):
    from KalKro.modules.games.marketing_simulator.simulator.welcome_office import Welcome_Market
    my_level = market_data_pack["level"]
    my_specilization = market_data_pack["specialization"]
    cmd = cmd.lower().strip()
    main_actions = {
        "!wallet": {"run": lambda: wallet_check(cmd), "description": "shows the current wallet account"},
        "!rating": {"run": lambda: rating_check(my_level, my_specilization), "description": "shows your ranking in marketing & economy"},
        "!menu": {"run": lambda: Welcome_Market.main_menu(), "description": ""}
    }
    if cmd in main_actions:
      main_actions[cmd]["run"]()
      return
    if cmd is "!othercmd":
        for cmd_name, content in main_actions.items():
           print(f"\n{cmd_name} {content['description']}:")
    else:
      print("\n\nSorry, but this command it not found. Type '!othermd' to view other programs.")

    print("\n\nGo back...")
    time.sleep(0.5)
    return
