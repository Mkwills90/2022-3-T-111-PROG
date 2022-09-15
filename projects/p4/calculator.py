OPERATORS = "+-*/"
PROMPT = "Enter an equation: "
equation = input(PROMPT)

while equation.lower() != "q":
    error = False
    operand_1, operator, operand_2 = equation.strip().split()
    if operator not in OPERATORS:
        print("Invalid operator")
        error = True
    elif not operand_1.isdigit() or not operand_2.isdigit():
        print("Invalid operands")
        error = True
    else:
        operand_1 = int(operand_1)
        operand_2 = int(operand_2)
        result = 0
        if operator == "+":
            result = operand_1 + operand_2
        elif operator == "-":
            result = operand_1 - operand_2
        elif operator == "*":
            result = operand_1 * operand_2
        else:
            if operand_2 == 0:
                print("Can't divide by 0")
                error = True
            else:
                result = operand_1 / operand_2
    
    if not error:
        print('Result: {:.2f}'.format(result))
    equation = input(PROMPT)
