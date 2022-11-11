FLAVOR_COL = 0
NUMBER_FORMAT = "{:>12.2f}"
FLAVOR_FORMAT = "{:<15}"

def main():
    file_name = input("Enter file name: ")
    file_object = open_file(file_name)
    if file_object is None:
        print("File {} not found".format(file_name))
    else:
        total_per_store = input("Show totals per store (y/n)?: ")
        sales_dict = read_sales_data(file_object)
        file_object.close()
        print_sales(sales_dict)
        if total_per_store == 'y':
            total_store_sales_list = compute_store_totals(sales_dict)
            print_store_totals(total_store_sales_list)


def open_file(filename):
  '''Opens the given file, returning its file object if found, otherwise None'''
  try:
    file_object = open(filename, 'r')
    return file_object
  except FileNotFoundError:
    return None


def read_sales_data(file_object):
    '''Reads the sales data associated with the file object, converting number strings to floats.
    The data is returned as a dictionary of lists: the keys are icecream flavours, the values are a list of sales'''
    sales_dict = {}

    for line in file_object:
        fields = line.split(';')
        flavor = fields[FLAVOR_COL]
        sales_str_list = fields[1:]
        if flavor not in sales_dict:    # Then this flavor does not exist in the dictionary
            sales_dict[flavor] = [float(sales_str) for sales_str in sales_str_list]
        else:   # We need to update the sales list already stored as a value for the key flavor
            sales_list = sales_dict[flavor]
            for i in range(len(sales_list)):
                sales_list[i] += float(sales_str_list[i])

    return sales_dict 


def print_sales(sales_dict):
    '''Prints each ice cream flavor in alphabetical order along with sales data'''
    for flavor in sorted(sales_dict):
        print(FLAVOR_FORMAT.format(flavor), end='')
        for sale in sales_dict[flavor]:
            print(NUMBER_FORMAT.format(sale), end='')
        print(NUMBER_FORMAT.format(sum(sales_dict[flavor])))
       

def compute_store_totals(sales_dict):
    '''Returns a list of the total sales of each store'''
    # Initialize the total sales for each store 0, 1, ..., n
    total_sales_list = [0.0] * get_number_of_stores(sales_dict)

    # Accumulate the sale for each store
    for flavor in sales_dict:
        for idx, sale in enumerate(sales_dict[flavor]):
            total_sales_list[idx] += sale

    return total_sales_list 

def get_number_of_stores(sales_dict):
    '''Return the number of stores as the length of the longest sales list'''
    number_of_stores = 0
    for sales_list in sales_dict.values():
        if len(sales_list) > number_of_stores:
            number_of_stores = len(sales_list)
    return number_of_stores


def print_store_totals(total_store_sales_list):
    '''Prints the total sale in each store'''
    print(FLAVOR_FORMAT.format('Total:'), end='')
    for sale in total_store_sales_list:
        print(NUMBER_FORMAT.format(sale), end='')
    print()


# Main program starts here
if __name__ == "__main__":
    main()
