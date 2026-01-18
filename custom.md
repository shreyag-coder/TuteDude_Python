# README.md

## Overview  
The README.md serves as the entry point for the **TuteDude_Python** repository. It introduces the project’s purpose and scope at a glance.

## Project Title  
- **TuteDude_Python**

## Description  
This repository contains simple Python assignments designed for learners. It outlines the main script (`main.py`) and its interactive tasks.

## Relationship to main.py  
- Acts as the project manifest.  
- Names the primary script (`main.py`).  
- Provides context for running and understanding the code.

---

# main.py

## Overview  
`main.py` is the core script of the TuteDude_Python project. It implements two interactive console tasks: basic arithmetic operations and a personalized greeting.

## Task 1: Arithmetic Operations 🧮  
This section prompts the user for two numbers, computes four basic operations, and prints the results.

```python
# Task 1
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", mul)
print("Division: ", div)
```

- **Inputs**:  
  - `num1`: First number (float)  
  - `num2`: Second number (float)  
- **Outputs**: Printed results for addition, subtraction, multiplication, and division.  

**Operation Mapping**

| Operation      | Symbol | Variable |
| -------------- | ------ | -------- |
| Addition       | +      | `add`    |
| Subtraction    | -      | `sub`    |
| Multiplication | *      | `mul`    |
| Division       | /      | `div`    |

## Task 2: User Greeting 👋  
This section collects the user’s first and last name, then displays a personalized welcome message.

```python
# Task 2
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Hello, {first_name}! Welcome to {last_name} the Python program.")
```

- **Inputs**:  
  - `first_name` (string)  
  - `last_name` (string)  
- **Output**: A formatted greeting combining both names.

## Execution  
To run the script:

1. Ensure **Python 3** is installed.  
2. In your terminal, navigate to the project directory.  
3. Execute:  
   ```bash
   python main.py
   ```

## Relationship to README.md  
- `main.py` implements the tasks described in README.md.  
- The README.md sets the context and points to `main.py` as the runnable component.