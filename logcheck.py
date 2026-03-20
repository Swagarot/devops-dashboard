def check_log():
    # Ask the user for a filename
    filename = input("Please enter the filename to check: ")
    
    try:
        # Try to open the file
        with open(filename, 'r') as file:
            for line in file:
                # Print every line that contains 'ERROR'
                if "ERROR" in line:
                    print(line.strip())
                    
    except FileNotFoundError:
        # If the file does not exist, print a clear error message
        print(f"Error: The file '{filename}' was not found. Please check the path and try again.")
    except Exception as e:
        # Catch-all for any other weird errors (like permission issues)
        print(f"An unexpected error occurred: {e}")
