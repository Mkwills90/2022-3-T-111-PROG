PROMPT = "Input f(ibonacci), c(ubes) or any other letter to quit: "

choice = input(PROMPT)
while choice == 'f' or choice == 'c':

    # In the Fibonacci sequence, the first two numbers are 0 and 1, 
    # but thereafter each number in the sequence is the sum of the two previous numbers.
    if choice == 'f':
        max_len = int(input("Input the length (>= 2) of the sequence: "))
        
        first_number = 0
        second_number = 1
        print(first_number)
        print(second_number)

        for i in range(1, max_len - 1):
            next_number = first_number + second_number
            print(next_number)
            first_number = second_number
            second_number = next_number

    # Find numbers between 100 and n <= 999, which are the sums of the cubes of their digits
    elif (choice == 'c'):
        max_number = int(input("Input the max number (<= 999) to check: "))

        for num in range(100, max_number + 1):
            num_to_divide = num
            total = 0
            for _ in range(3):
                digit = num_to_divide % 10
                total += digit ** 3
                num_to_divide = num_to_divide // 10
            if total == num:
                print(num)

    choice = input(PROMPT)
