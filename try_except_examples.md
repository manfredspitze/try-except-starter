### What is an Exception in Python?

**An exception in Python is an error that occurs during the execution of a program.** 

Exceptions are bad because they can crash your script, and users get frustrated with scripts that keep crashing.

Even worse is a script that crashes and doesn't give the user a clear explanation *why* the script just crashed.

**Think of it like this:** You're following a recipe to bake a cake. If you don't have enough flour, that's an exception. You can't continue following the recipe until you do something about the exception (such as borrow three cups of flour from your neighbor).

In Python, exceptions are handled using `try-except` blocks. 

`try-except` blocks help you avoid crashes and let you briefly explain to the user *why* the script didn't work as expected.

### `try-except` Block Examples

```python
# Example 1
# Using try-except block to handle attempting to divide a number by zero
try:
    print(2/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

```python
# Example 2
def get_validated_input(min_length=1, max_length=10):
  """
  Prompts the user for a string input and validates its length.

  Arguments used in the function call:
    min_length: The minimum allowed length of the string.
    max_length: The maximum allowed length of the string.

  Returns:
    The validated string if valid, otherwise raises a ValueError.
  """
  while True:
    try:
      user_input = input("Enter a string: ")
      if len(user_input) < min_length:
        raise ValueError(f"Input string must be at least {min_length} characters long.")
      if len(user_input) > max_length:
        raise ValueError(f"Input string cannot exceed {max_length} characters.")
      return user_input
    except ValueError as e:
      print(f"Error: {e}")

# Calling the function that validates the input string
validated_string = get_validated_input(min_length=3, max_length=8)

if validated_string:
  print(f"Validated string: {validated_string}")
```
