from art import logo
print(logo)
import os


bidding_mode_on = True
def find_highest_bidder(bidding_record):
    higher=0
    winner=""
    for bidder in bidding_record:
        new_bid = bidding_record[bidder]
        if new_bid>higher:
            higher=new_bid
            winner=bidder
    print(f"the highest bidder is {winner} with ${higher}")

        
bid_bidder={}
while bidding_mode_on:
    name= input("enter your name")
    price =int(input("enter the amount you wanna bid\n"))
    bid_bidder[name]=price
    print(bid_bidder)
    choice = input("type 'yes' to continue bidding\n")
    if choice=="yes":
        os.system('cls')
        print(logo)
        continue
    elif choice=="no":
        bidding_mode_on=False
        find_highest_bidder(bid_bidder)
       
        
