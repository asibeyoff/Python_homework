def invest(amount, rate, years):
    current_amount = amount
    for year in range(1, years + 1):
        current_amount += current_amount * rate
        print(f"year {year}: ${current_amount:.2f}")

amount = float(input("Enter initial amount: "))
rate = float(input("Enter annual percentage rate (as decimal, e.g. 0.05 for 5%): "))
years = int(input("Enter number of years: "))

invest(amount, rate, years)

# Calculates investment growth over time with compound interest