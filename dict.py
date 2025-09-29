groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}

shop = []

while True:
  grocery = input("What do you want to buy.If you want to stop enter done: ")

  if grocery.lower() == "done" :
    break
  
  elif grocery in groceries:
    shop.append(grocery)

  else:
    print("Not found in groceries")


total = 0 

for i in shop:
  total += groceries[i]

print("You bought: ",shop)
print("Total: $", total)

if total > 10 :
  print("You spent a lot!")
else:
  print("You spent a little!")
