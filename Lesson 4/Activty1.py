field1 = 250
field2 = 120
field3 = 75
field4 = 95
field5 = 110

total = field1 + field2 + field3 + field4 + field5
average = total / 5
print ("Total harvest field:", total, "kg")
print ("Average per field   :",average, "kg")
price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings   :Rs.", earnings)
bags   = total // 25
leftover = total % 25

print("Full bags packed   :", bags)
print("Leftover grain  :", leftover, "kg")

last_year = 500
print("Better than last year?  :", total > last_year)
print("Same as last year?", total == last_year)
print("At least as good?       :", total >= last_year)

# --- Assignment Operators (+=, -=) ---
# A bonus field adds 30 kg to the total
total += 30
print("After bonus crop   :", total, "kg")

# Subtract 15 kg saved as seeds for next season
total -= 15
print("After seed reserve :", total, "kg")

# Final bag count after all adjustments
bags = total // 25
print("Final bags packed  :", bags)
