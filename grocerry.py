grocery_items = {
    "apple": 1.0,
    "banana": 0.5,
    "milk": 3.0,
    "bread": 2.0,
}
cart = {}
while True:
    item = input("What do you want to buy?:").strip()
    if item == "done":
        break
    parts = item.split()
    item_name = parts[0]
    quantity = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1

    if item_name in grocery_items:
        if item_name in cart:
            cart[item_name] += quantity
        else:
            cart[item_name] = quantity
    else:
        print("Sorry, we don't have that item.")

total_cost = 0
for item, quantity in cart.items():
    item_cost = grocery_items[item] * quantity
    total_cost += item_cost
    if item == "milk" and quantity >= 2:
        total_cost -= 1  


print("Final list of items:")
for item, quantity in cart.items():
    print(
        f"{item}: {quantity} x ${grocery_items[item]} = ${grocery_items[item] * quantity}")
print(f"Total cost: ${total_cost}")

if total_cost > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")