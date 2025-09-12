# Shopping Cart - List of Dictionaries
cart = [
    {"item": "Laptop", "price": 80000, "qty": 1},
    {"item": "Mouse", "price": 1200, "qty": 2},
    {"item": "Keyboard", "price": 2500, "qty": 1}
]

# 1. Print each item with its total cost
print("Item-wise total costs:")
for product in cart:
    item_total = product["price"] * product["qty"]
    print(f"{product['item']} - Qty: {product['qty']}, Total: Rs.{item_total}")
print()

# 2. Calculate total bill
total_bill = 0
for product in cart:
    total_bill += product["price"] * product["qty"]
print(f"Total Bill: Rs.{total_bill}")
print()

# 3. Find the most expensive item
most_expensive = cart[0]
for product in cart[1:]:
    if product["price"] > most_expensive["price"]:
        most_expensive = product
print(f"Most expensive item: {most_expensive['item']} at Rs.{most_expensive['price']}")
print()

# 4. Apply 10% discount on each item and show discounted total
discounted_total = 0
print("Item-wise discounted prices and totals:")
for product in cart:
    discounted_price = product["price"] * 0.90  # 10% discount
    item_total = discounted_price * product["qty"]
    print(f"{product['item']} - Discounted Price: Rs.{discounted_price:.2f}, Total: Rs.{item_total:.2f}")
    discounted_total += item_total
print(f"Total after discount: Rs.{discounted_total:.2f}")
print()

# Bonus: Add a new item and recalculate totals
new_item = {"item": "Monitor", "price": 15000, "qty": 1}
cart.append(new_item)
print("Added new item: Monitor\n")

# Recalculate total bill after adding new item
total_bill = 0
for product in cart:
    total_bill += product["price"] * product["qty"]
print(f"New Total Bill after adding Monitor: Rs.{total_bill}")
