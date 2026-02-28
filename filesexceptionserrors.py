# ASSIGNMENT 4: Module 5: Files, Exceptions, and Errors in Python

# Task 1: Read a File and Handle Errors
def read_file():
    try:
        with open("sample.txt", "r") as file:
            print("Reading file content:")

            line_num  = 1
            for line in file:
                print(f"Line {line_num}: {line.strip()}")
                line_num += 1
    except FileNotFoundError:
        print("Error: The file 'sample.txt' was not found.")

# Task 2: Write and Append Data to a File
def write_and_append():
    try:
        text = input("Enter text to write to the file: ")
        with open("output.txt", "w") as file:
            file.write(text + '\n')
        print("Data successfully written to output.txt.\n")

        additional_text = input("Enter additional tet to append to: ")
        with open("output.txt", "a") as file:
            file.write(additional_text + '\n')
        print("Data successfully appended.\n")

        print("Final content of output.txt:")
        with open("output.txt", "r") as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")


def main():
    print("Choose a task: ")
    print("1. Read a file")
    print("2. Write and append to a file")

    choice = input("Enter your choice (1 or 2): ")

    if choice == 1:
        read_file()
    elif choice == 2:
        write_and_append()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()






