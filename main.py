def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (convert to uppercase)
        modified_content = content.upper()
        
        # Open the output file in write mode
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File '{input_filename}' has been read and modified content written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: An IOError occurred while processing the file '{input_filename}'.")

# Example usage
input_file = 'input.txt'  # Replace with your input file name
output_file = 'output.txt'  # Replace with your desired output file name
read_and_modify_file(input_file, output_file)

def read_file_with_error_handling():
    filename = input("Please enter the filename to read: ")
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: An IOError occurred while reading the file '{filename}'.")

# Example usage
read_file_with_error_handling()

