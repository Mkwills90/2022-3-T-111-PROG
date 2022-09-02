k = int(input("Enter value for k: "))
n = int(input("Enter value for n: "))

the_sum = 0
for i in range(n):
    exponent = int(input("Enter integer: "))
    the_sum += k ** exponent
print(the_sum)
