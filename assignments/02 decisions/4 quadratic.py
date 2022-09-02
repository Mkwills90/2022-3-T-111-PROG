val_a_int = int(input("Enter the value for a: "))
val_b_int = int(input("Enter the value for b: "))
val_c_int = int(input("Enter the value for c: "))

d = (val_b_int * val_b_int) - (4 * val_a_int * val_c_int)

if d > 0:
    print("2 solutions.")
elif d == 0:
    print("1 solution.")
else:
    print("No solutions.")
