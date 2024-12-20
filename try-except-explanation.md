---

# **Python Try-Except Block: Error Handling Basics**

### What is an Exception?

In Python, an **exception** is an error that occurs when you run your script. When something goes wrong (e.g., trying to divide by zero, or attempting to access an item in a list that doesn’t exist), Python **raises** an exception. 

An **exception** is a signal that something went wrong, and it can be caught and handled using a `try-except` block. If the exception is not handled, the script will crash and stop running.

### Example of an Exception

Here’s a simple example of an exception:

```python
x = 5
y = 0
result = x / y  # This raises a ZeroDivisionError
```

**Explanation:**
- When we attempt to divide by zero, Python raises a `ZeroDivisionError`. This is an exception that tells us we cannot divide a number by zero.

---

### What is a Try-Except Block?

The `try-except` block in Python allows you to **catch exceptions** and handle them in a way that keeps your script from crashing. 

### Syntax

```python
try:
    # Code that might cause an error
except <ErrorType>:
    # Code to handle the error
```

- The **`try`** block contains code that might cause an exception.
- The **`except`** block contains code that handles the exception if it occurs.

It's always a good idea to try to catch specific types of exceptions, such as `ZeroDivisionError` or `ValueError`.

That way, you can let the user know what the problem was with the script.

---

### Example 1: Handling a Division by Zero Error

This example shows how to handle a `ZeroDivisionError`.

```python
try:
    x = 10
    y = 0
    result = x / y  # This will raise a ZeroDivisionError
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```

**Explanation:**
- The code tries to divide `x` by `y`.
- Since `y` is zero, a `ZeroDivisionError` occurs.
- The `except` block catches this exception and prints a message instead of allowing the script to crash.

---

### Example 2: Handling Invalid User Input

We can use `try-except` to catch invalid input, such as when the user enters something that isn’t a number or a number that's negative when the script is expecting a positive number.

```python
def get_positive_number():
    try:
        number = int(input("Please enter a positive number: "))
        if number < 0:
            print("Error: The number must be positive!")
            return None
        return number
    except ValueError:
        print("Error: That's not a valid number!")
        return None

# Call the function
my_number = get_positive_number()
print(my_number)

```

**Explanation:**
- The function checks if the number is negative inside the `try` block (if the number is negative, the function returns `None`, otherwise the function returns the value of the number)
- If the input is not a valid number (i.e., the user enters a non-numeric value such as *cat* or *#&mj!$*), the `except ValueError` block catches the error and prints an error message, and returns `None`
- So we're handling both invalid inputs and negative numbers directly within the `try` and `except` blocks
---

### Example 3: Catching Multiple Types of Errors

You can handle different types of exceptions separately, using multiple `except` blocks.

```python
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 + num2
    print(f"The sum is: {result}")
except ValueError:
    print("Error: Please enter valid numbers.")
except TypeError:
    print("Error: There was a problem with the type of input entered.")
```

**Explanation:**
- The program asks the user to input two numbers.
- If the user enters invalid data (like text), a `ValueError` is raised.
- If there’s a data type mismatch (e.g., trying to add numbers and strings together), a `TypeError` is raised.
- Each exception is handled separately with a specific message.

---

### Conclusion

In Python, **exceptions** are errors that occur during the execution of a program. When an exception occurs, Python stops executing the current code and looks for an `except` block to handle the error. The `try-except` block lets you catch and handle exceptions, making your program more stable and user-friendly.

You can:
- handle specific exceptions (like `ZeroDivisionError` or `ValueError`).
- prevent the script from crashing by catching errors and displaying helpful messages to the user about what caused the error.
- use multiple `except` blocks to handle different types of exceptions.

**Remember**: Always try to handle exceptions gracefully, so users can understand what went wrong and can fix the problems with their script so their script doesn't crash!

--- 

