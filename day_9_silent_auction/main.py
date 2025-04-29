auction_bids = {}

is_auction_on = True

print("")
while is_auction_on:
    name = input("What is your name ")
    bid_value = int(input("What is your bid? "))
    auction_bids[name] = bid_value
    to_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
    if to_continue == "yes":
        continue
    else:
        is_auction_on = False

highest_bid = ""
for key in auction_bids:
    try:
        if auction_bids[highest_bid] <= auction_bids[key]:
            highest_bid = key
    except KeyError:
        highest_bid = key

print(f"The winner is {highest_bid} with a bid of ${auction_bids[highest_bid]}")
