print("=== ATM cash dipenser ===\n")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_serverd = 0
total_dispensed = 0

serving = True
while serving:
    name = input("Enter customer name: ")
    amount = int(input(f"hello {name}! Enter widthdrawal amount: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.\n")
        continue

    print(f"\nDispensing {amount} units for name: {name}")
    remaining = amount
    idx = 1
    while idx <= 6:
        if idx == 1:
            bill_value = 100
        elif idx == 2:
            bill_value = 50
        elif idx == 3:
            bill_value = 20
        elif idx == 4:
            bill_value = 10
        elif idx == 5:
            bill_value = 5
        else: value = 1
        count = remaining // value
        if count > 0:
            print(f" {count} x {value}-unit note(s) = {count * value}")
            remaining -= count * value
            if value == 100: total_100 += count
            elif value == 50: total_50 += count
            elif value == 20: total_20 += count
            elif value == 10: total_10 += count
            elif value == 5: total_5 += count
            else: total_1 += count
        idx += 1

        customers_serverd += 1
        total_dispensed += amount
        print(f"Transactions complete, {name}!\n")
        again = input("Next customer? (yes/no): ").strip().lower()
    if again != "yes":
        serving = False

print("\n=== Daily Denomination Report ===")
for slot in range(1, 7):                      # outer for -- one denomination per loop
    if slot == 1: value, total = 100, total_100
    elif slot == 2: value, total = 50, total_50
    elif slot == 3: value, total = 20, total_20
    elif slot == 4: value, total = 10, total_10
    elif slot == 5: value, total = 5, total_5
    else: value, total = 1, total_1
    if total > 0:
        print(f"  {value}-unit notes dispensed : {total} ", end="")
        for note in range(total):             # inner for -- one symbol per note
            print("=", end="")
        print()

print(f"\nCustomers served : {customers_served}")
print(f"Total dispensed  : {total_dispensed} units")
print("ATM session closed. Goodbye!")
       