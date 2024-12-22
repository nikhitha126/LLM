def calculate(initial, interest_rate, years):
    amount = initial
    for i in range(1, years + 1):
        amount += amount * (interest_rate / 100)
        print(f"Year {i}: Amount = {amount:.2f}")
    return amount
initial= float(input("Enter the initial balance (K0): "))
interest_rate= float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the number of years: "))
print("\n--- Capital Growth ---")
final= calculate(initial, interest_rate, years)
print(f"\nAfter {years} years, the final amount is: {final:.2f}")