length = int(input("Length of sequence: ")) 

the_sum = 0
for i in range(1, length + 1):
    the_sum += i
    print(i, the_sum)