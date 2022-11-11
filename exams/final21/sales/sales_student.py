YES = "y"


def main():
    file_name = input("Enter file name: ")
    file_object = open_file(file_name)
    # Your continue the program from here
    if file_object:
        sales_list = create_sales_list(file_object)
        show_totals = input("Show totals per store (y/n)?: ")
        ice_cream_sales = find_icecream_sum(sales_list)
        print_display(sales_list)
        if show_totals == YES:
            # print_totals_display(sales_list)
            pass
        else:
            pass
    else:
        print(f"File {file_name} not found")

def open_file(filename):
  '''Opens the given file, returning its file object if found, otherwise None'''
  try:
    file_object = open(filename, 'r')
    return file_object
  except FileNotFoundError:
    return None

def create_sales_list(file_object):
    sales_list = []
    for line in file_object:
        line = line.strip().split(";")
        ice_cream_tuple = get_tuple_from_line(line)
        sales_list.append(ice_cream_tuple)
    return sales_list

def get_tuple_from_line(line):
    name, sales = line[0], line[1:]
    sales = [float(sale) for sale in sales]
    return (name, sales)

def find_icecream_sum(sales_list):
    icecream_sum = [(name, sales, find_sales_sum(sales)) for name, sales in sales_list]
    return icecream_sum

def find_sales_sum(sales):
    ice_cream_sales = 0
    for sale in sales:
        ice_cream_sales += sale
    return ice_cream_sales

def print_display(ice_cream_sales):
    for name, sales, sum_of_sales in sorted(ice_cream_sales):
        display_row(name, sales, sum_of_sales)

def display_row(name, sales, sum_of_sales):
    print(f"{name:<15s}", end=" ")
    for sale in sales:
        print(f"{sale:>11.2f}", end=" ") # Ég breytti í 11 því það kom eins og það væri auka bil ef ég gerði 12
    print(f"{sum_of_sales:>11.2f}") # Myndi annars gera 12.2f

# def print_totals_display(sales_list):
    # store_sum = find_col_sum(sales_list)

# Hefði haldið áfram með totals ef ég hefði tíma.
# Myndi reyna að finna summuna á hverjum dálk og prenta í sama formati og hitt displayið

    
        
    
        


# Main program starts here.  Do NOT change the starter code.
if __name__ == "__main__":
    main()
