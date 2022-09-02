# problem derived from https://open.kattis.com/problems/tarifa
mb_per_month = int(input("How much data (in Mb) do you get per month?: "))
n = int(input("How many months have you had this plan?: "))

mb_allowance = 0

for i in range(n):
    mb_allowance += mb_per_month
    usage = int(input("How much data did you use this month?: "))
    mb_allowance -= usage

print(mb_allowance + mb_per_month)
