from KalKro.utilities.helpers import printsl
import time


def wallet_check(money): # SHOWING THE PLAYER'S FINANCIAL MATERIALS
    time.sleep(0.3)
    printsl(f"\n\nYOUR WALLET AT THE MOMENT: {money}$.")
    printsl("\nYou can always quickly view your material account using the '!wallet' command.")
    input("\nPress Enter to continue. ")
    return
    