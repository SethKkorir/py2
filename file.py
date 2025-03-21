def read_and_modify_file():
    try:
        filename = input("Enter the name of the file to read: ")
        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.upper()
        new_filename = "modified_" + filename

        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been saved to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please enter a valid filename.")
    except PermissionError:
        print("Error: Permission denied. Cannot read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_modify_file()
