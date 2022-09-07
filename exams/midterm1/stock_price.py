PROMPT = "Input a stock price (0 to quit): "
DIGITS = 2

total_price = 0.0
max_price = 0.0
num_days = 0

price = float(input(PROMPT))
while price != 0:
    num_days += 1
    total_price += price
    print("Price on day", num_days, "is:", price)
    
    if price > max_price:
        max_price = price
        
    price = float(input(PROMPT))

if num_days > 0:
    average = total_price/num_days
    print("Maximum stock price:", max_price)
    print("Average stock price:", round(average, 2))