groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}

shop = []

while True:
  grocery = input("What do you want to buy(If you want to stop enter done.)")

  if grocery.lower == "done":
    break
  
  elif grocery in groceries:
    shop.append(grocery)

  else:
    print("Not found in groceries")




