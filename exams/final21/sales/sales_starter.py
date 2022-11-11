def main():
    file_name = input("Enter file name: ")
    file_object = open_file(file_name)
    # Your continue the program from here

def open_file(filename):
  '''Opens the given file, returning its file object if found, otherwise None'''
  try:
    file_object = open(filename, 'r')
    return file_object
  except FileNotFoundError:
    return None

# Main program starts here. Do NOT change the starter code.
if __name__ == "__main__":
    main()