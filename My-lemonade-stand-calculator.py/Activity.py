def greet_customer():
    print("Welcome to the lemonade stand!")
    print("fresh lemonade, made just for you.")
greet_customer()
price_per_cup = float(input("Enter the price per cup in $ "))
cups_sold = int(input("Enter the number of cups sold: "))
def calculate_total (price, cups):
    total = price * cups
    return total
rounded_total = calculate_total(price_per_cup, cups_sold)
rounded_total = round(rounded_total, 2)
print("Total cost:", rounded_total)

amount_paid = float(input("Enter the amount paid by the customer in:  "))
def calculate_change(paid, total):
    change = paid - total
    return change
change_due = calculate_change(amount_paid, rounded_total)
rounded_change_due = round(change_due, 2)
def thank_you_message(cups):
    if cups > 5:
        return "Wow big order! thanks so much for the support!"
    else:
        return "Thanks for stopping by the stand!"
closing_message = thank_you_message(cups_sold)
print("")
print("===== LEMONADE STAND RECEIPT =====")
print("Cups sold:", cups_sold)
print("price per cup: ", price_per_cup)
print("cups sold: ", cups_sold)
print("total_cost:", rounded_total)
print("Amount paid: ", amount_paid)
print("Change due: ", rounded_change_due)
print(closing_message)
print("===================================")